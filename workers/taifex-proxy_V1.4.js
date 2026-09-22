
/*
 * ============================================================
 * TAIFEX Proxy V1.1 — Production + OpenAPI Fallback + GEX Diagnostic + Date Validation => V1.1 Final_V2 
 * ============================================================
 *
 * STATUS:
 *   Production / Locked functional specification
 *
 * PURPOSE:
 *   Single production data gateway for the Daily Pre-market
 *   Analysis project.
 *
 * FUNCTIONAL SCOPE:
 *   1. Health
 *   2. TX futures price / after-hours price
 *   3. TX institutional flow / after-hours flow
 *   4. TX institutional OI / OI history
 *   5. TXO options chain
 *   6. TXO options delta
 *   7. TXO institutional / after-hours institutional data
 *   8. TXO options after-hours data
 *   9. Call Wall / Put Wall / Max Pain
 *  10. Black-Scholes Gamma / GEX model outputs where source data is sufficient
 *  11. Chain-Delta contract normalization and quality metrics
 *  12. Fail-safe status: usable / partial / unavailable
 *  13. Compact market-structure output for downstream analysis
 *  14. Explicit TAIEX spot/index dependency for Black-Scholes GEX
 *
 * IMPORTANT:
 *   GEX / Gamma Wall / Gamma Flip are derived model outputs, NOT
 *   TAIFEX-published official GEX fields. The model uses TAIFEX
 *   settlement, OI, strike, expiry and Delta for validation, with
 *   Black-Scholes implied volatility and a documented signed-GEX
 *   convention. Dealer-side positioning is not directly observable
 *   from aggregate OI, so outputs remain "TAIFEX-derived GEX".
 *
 * VERSION POLICY:
 *   This is the production baseline. Future changes should be
 *   additive and versioned; do not silently alter existing
 *   semantics or field meanings.
 *
 * V1.2 ADDITIVE (2026-09-18):
 *   + /futures-top10?date=YYYY-MM-DD[&month=YYYYMM]
 *   + /options-top10?date=YYYY-MM-DD&type=call|put[&month=YYYYMM]
 *   Both proxy TAIFEX OpenAPI Large-Traders OI with date validation.
 *
 * V1.3 ADDITIVE (2026-09-18):
 *   + /futures-night-ohlc?date=YYYY-MM-DD[&month=YYYYMM]
 *   + /put-call-ratio-history (PutCallRatio history rows)
 *
 * V1.4 ADDITIVE (2026-09-18):
 *   + scheduled daily snapshot (cron + KV SNAPSHOTS binding)
 *   + /snapshots/bundle?date=YYYY-MM-DD (exact or latest<=date)
 *   + /snapshots/write-now[?key=] (manual trigger for testing/backfill)
 *   Snapshot covers: top10fut/opt, chain, fut/opt day positions, walls.
 *   All prior endpoints byte-identical.
 * ============================================================
 */

const TAIFEX = "https://www.taifex.com.tw";

const TWSE_OPENAPI = "https://openapi.twse.com.tw/v1";

const TAIFEX_OPENAPI = "https://openapi.taifex.com.tw/v1";


/**
 * Production underlying resolver for TXO GEX.
 *
 * Priority:
 *   1) TAIEX spot/index value from an existing normalized TAIFEX response.
 *   2) Explicit TAIEX/TAIEX_INDEX fields found in the supplied source rows.
 *
 * Never substitute TX futures for TAIEX spot: the two are different
 * underlyings and doing so would silently distort Black-Scholes Gamma.
 */
function resolveTaiExUnderlying(rows) {
  const candidates = [];

  for (const r of Array.isArray(rows) ? rows : []) {
    const keys = Object.keys(r || {});
    for (const k of keys) {
      const n = String(k).toLowerCase().replace(/[^a-z0-9]/g, "");
      if (
        n === "taiex" ||
        n === "taiexindex" ||
        n === "taiexspot" ||
        n === "indexvalue" ||
        n === "indexprice"
      ) {
        const v = Number(r[k]);
        if (Number.isFinite(v) && v > 0) candidates.push(v);
      }
    }
  }

  if (!candidates.length) return null;

  // Use the first valid normalized spot value. Do not infer from TX futures.
  return candidates[0];
}


/* ============================================================
 * TAIFEX OpenAPI Fallback Layer — V1.1
 *
 * Primary source remains the existing TAIFEX web endpoints.
 * OpenAPI is used only when the primary source is unavailable,
 * malformed, or empty.  OpenAPI is latest-trading-day data for
 * the daily market feeds, so every fallback response is date-
 * checked before it is accepted.
 *
 * IMPORTANT:
 *   OpenAPI does NOT publish official GEX.  For GEX fallback,
 *   OpenAPI supplies the raw TXO chain + Delta inputs and the
 *   existing Black-Scholes GEX engine remains unchanged.
 * ============================================================ */

function apiDigits(value) {
  return String(value ?? "").replace(/\D/g, "");
}

function apiDateISO(value) {
  const d = apiDigits(value);
  if (d.length === 8) {
    return `${d.slice(0,4)}-${d.slice(4,6)}-${d.slice(6,8)}`;
  }
  return null;
}

function apiValue(row, keys) {
  for (const k of keys) {
    if (row && Object.prototype.hasOwnProperty.call(row, k)) {
      return row[k];
    }
  }
  return null;
}

async function fetchTAIFEXOpenAPI(path) {
  const source_url = `${TAIFEX_OPENAPI}${path}`;

  try {
    const response = await fetch(source_url, {
      headers: {
        "User-Agent":
          "Mozilla/5.0 (compatible; TAIFEX-Proxy/V1.1-OpenAPI-Fallback)",
        "Accept": "application/json,text/plain,*/*"
      }
    });

    const text = await response.text();

    if (!response.ok) {
      return {
        found: false,
        response,
        source_url,
        rows: [],
        reason: `TAIFEX OpenAPI HTTP ${response.status}`
      };
    }

    let payload;
    try {
      payload = JSON.parse(text);
    } catch (_) {
      return {
        found: false,
        response,
        source_url,
        rows: [],
        reason: "TAIFEX OpenAPI response is not valid JSON"
      };
    }

    const rows = Array.isArray(payload)
      ? payload
      : payload && Array.isArray(payload.data)
        ? payload.data
        : [];

    return {
      found: rows.length > 0,
      response,
      source_url,
      rows,
      reason: rows.length ? null : "TAIFEX OpenAPI returned no rows"
    };
  } catch (error) {
    return {
      found: false,
      response: new Response(null, { status: 599 }),
      source_url,
      rows: [],
      reason: `TAIFEX OpenAPI fetch failed: ${error?.message || String(error)}`
    };
  }
}

function openApiFuturesRows(apiRows, requestedISO = null) {
  const normalizedDate = apiRows.length
    ? apiDateISO(apiValue(apiRows[0], ["Date", "date"]))
    : null;

  if (requestedISO && normalizedDate && normalizedDate !== requestedISO) {
    return { found: false, date: normalizedDate, rows: [], reason: `OpenAPI date ${normalizedDate} != requested ${requestedISO}` };
  }

  const groups = new Map();
  for (const r of apiRows) {
    if (apiValue(r, ["Contract", "contract"]) !== "TX") continue;
    const session = String(apiValue(r, ["TradingSession", "tradingSession"]) ?? "");
    const month = apiValue(r, ["ContractMonth(Week)", "ContractMonth", "contractMonth"]);
    const key = `${month}|${session}`;
    const row = [
      "TX",
      month,
      apiValue(r, ["Open", "open"]),
      apiValue(r, ["High", "high"]),
      apiValue(r, ["Low", "low"]),
      apiValue(r, ["Last", "Close", "close"]),
      apiValue(r, ["Change", "change"]),
      apiValue(r, ["%", "Change%", "changePercent"]),
      apiValue(r, ["Volume", "volume"]),
      apiValue(r, ["SettlementPrice", "settlementPrice"]),
      apiValue(r, ["OpenInterest", "openInterest"]),
      apiValue(r, ["BestBid", "bestBid"]),
      apiValue(r, ["BestAsk", "bestAsk"]),
      apiValue(r, ["HistoricalHigh", "historicalHigh"]),
      apiValue(r, ["HistoricalLow", "historicalLow"]),
      session
    ];
    groups.set(key, row);
  }

  const regular = new Map();
  const after = new Map();
  for (const row of groups.values()) {
    const month = row[1];
    const session = row[15];
    if (session === "一般" || /regular/i.test(session)) regular.set(month, row);
    if (session === "盤後" || /after/i.test(session)) after.set(month, row);
  }

  const rows = [];
  const months = new Set([...regular.keys(), ...after.keys()]);
  for (const month of months) {
    const d = regular.get(month) || [];
    const a = after.get(month) || [];
    rows.push([
      "TX",
      month,
      d[2] ?? a[2], d[3] ?? a[3], d[4] ?? a[4], d[5] ?? a[5],
      d[6] ?? a[6], d[7] ?? a[7],
      a[8] ?? null,
      d[8] ?? null,
      (Number(d[8]) || 0) + (Number(a[8]) || 0),
      d[9] ?? null,
      d[10] ?? a[10] ?? null,
      d[11] ?? a[11] ?? null,
      d[12] ?? a[12] ?? null,
      d[13] ?? a[13] ?? null,
      d[14] ?? a[14] ?? null
    ]);
  }

  return { found: rows.length > 0, date: normalizedDate, rows };
}

function inferTXOExpiry(contractMonth, requestedISO) {
  const s = String(contractMonth ?? "");
  const m = s.match(/^(\d{4})(\d{2})(?:W(\d+)|F(\d+))?$/i);
  if (!m) return null;

  const y = Number(m[1]);
  const mo = Number(m[2]);
  const week = m[3] ? Number(m[3]) : null;
  const fridayWeek = m[4] ? Number(m[4]) : null;

  const weekday = d => d.getUTCDay();
  const nthWeekday = (year, month, wd, n) => {
    const first = new Date(Date.UTC(year, month - 1, 1));
    const offset = (wd - weekday(first) + 7) % 7;
    return new Date(Date.UTC(year, month - 1, 1 + offset + (n - 1) * 7));
  };

  if (week) return nthWeekday(y, mo, 3, week).toISOString().slice(0,10);
  if (fridayWeek) return nthWeekday(y, mo, 5, fridayWeek).toISOString().slice(0,10);

  // TAIFEX monthly index options settle on the third Wednesday.
  return nthWeekday(y, mo, 3, 3).toISOString().slice(0,10);
}

function openApiOptionRows(apiRows, requestedISO = null) {
  const dates = [...new Set(apiRows.map(r => apiDateISO(apiValue(r, ["Date", "date"]))).filter(Boolean))];
  const date = dates.includes(requestedISO) ? requestedISO : (dates[0] || null);
  if (requestedISO && !dates.includes(requestedISO)) {
    return {
      found: false,
      date,
      available_dates: dates,
      rows: [],
      reason: `OpenAPI date ${date || "unknown"} does not contain requested ${requestedISO}`
    };
  }

  const txo = apiRows.filter(r =>
    apiValue(r, ["Contract", "contract", "ContractCode", "contract_code"]) === "TXO"
  );

  const merged = new Map();
  for (const r of txo) {
    const month = apiValue(r, ["ContractMonth(Week)", "ContractMonth", "contractMonth"]);
    const strike = nullableNumber(apiValue(r, ["StrikePrice", "Strike", "strike"]));
    const cpRaw = String(apiValue(r, ["CallPut", "Call_Put", "callPut", "call_put"]) ?? "");
    const type = /Call|買權/i.test(cpRaw) ? "Call" : /Put|賣權/i.test(cpRaw) ? "Put" : null;
    if (!month || strike === null || !type) continue;

    const session = String(apiValue(r, ["TradingSession", "tradingSession"]) ?? "");
    const key = `${month}|${strike}|${type}`;
    const item = merged.get(key) || {
      contract_month: month,
      expiry: inferTXOExpiry(month, requestedISO || date),
      type,
      strike,
      regular: null,
      after: null
    };

    const v = {
      open: apiValue(r, ["Open", "open"]),
      high: apiValue(r, ["High", "high"]),
      low: apiValue(r, ["Low", "low"]),
      last: apiValue(r, ["Close", "Last", "close", "last"]),
      settlement: apiValue(r, ["SettlementPrice", "settlementPrice"]),
      change: apiValue(r, ["Change", "change"]),
      change_percent: apiValue(r, ["%", "Change%", "changePercent"]),
      volume: apiValue(r, ["Volume", "volume"]),
      oi: apiValue(r, ["OpenInterest", "openInterest"]),
      bid: apiValue(r, ["BestBid", "bestBid"]),
      ask: apiValue(r, ["BestAsk", "bestAsk"]),
      hh: apiValue(r, ["HistoricalHigh", "historicalHigh"]),
      ll: apiValue(r, ["HistoricalLow", "historicalLow"])
    };

    if (session === "一般" || /regular/i.test(session)) item.regular = v;
    else if (session === "盤後" || /after/i.test(session)) item.after = v;
    else item.regular = item.regular || v;
    merged.set(key, item);
  }

  const rows = [];
  for (const x of merged.values()) {
    const r = x.regular || {};
    const a = x.after || {};
    rows.push([
      "TXO", x.contract_month, x.expiry, x.strike, x.type,
      r.open ?? a.open ?? "-", r.high ?? a.high ?? "-", r.low ?? a.low ?? "-",
      r.last ?? a.last ?? "-", r.settlement ?? "-", r.change ?? a.change ?? "-",
      r.change_percent ?? a.change_percent ?? "-",
      a.volume ?? "-", r.volume ?? "-", (Number(r.volume)||0)+(Number(a.volume)||0),
      r.oi ?? "-", r.bid ?? a.bid ?? "-", r.ask ?? a.ask ?? "-",
      r.hh ?? a.hh ?? "-", r.ll ?? a.ll ?? "-"
    ]);
  }

  return { found: rows.length > 0, date, rows };
}

async function fetchOpenAPIChainForDate(requestedISO) {
  const result = await fetchTAIFEXOpenAPI("/DailyMarketReportOpt");
  if (!result.found) return result;
  return openApiOptionRows(result.rows, requestedISO);
}

async function fetchOpenAPIFuturesForDate(requestedISO = null) {
  const result = await fetchTAIFEXOpenAPI("/DailyMarketReportFut");
  if (!result.found) return result;
  return openApiFuturesRows(result.rows, requestedISO);
}

async function fetchOpenAPIInstitutionalFutures() {
  const result = await fetchTAIFEXOpenAPI(
    "/MarketDataOfMajorInstitutionalTradersDetailsOfFuturesContractsBytheDate"
  );
  if (!result.found) return result;

  const date = apiDateISO(apiValue(result.rows[0], ["Date", "date"]));
  const tx = result.rows.filter(r =>
    apiValue(r, ["ContractCode", "contractCode"]) === "臺股期貨"
  );

  const rows = [];
  for (const r of tx) {
    rows.push([
      "臺股期貨",
      apiValue(r, ["Item", "item"]),
      apiValue(r, ["TradingVolume(Long)"]),
      apiValue(r, ["TradingValue(Long)(Thousands)"]),
      apiValue(r, ["TradingVolume(Short)"]),
      apiValue(r, ["TradingValue(Short)(Thousands)"]),
      apiValue(r, ["TradingVolume(Net)"]),
      apiValue(r, ["TradingValue(Net)(Thousands)"]),
      apiValue(r, ["OpenInterest(Long)"]),
      apiValue(r, ["ContractValueofOpenInterest(Long)(Thousands)"]),
      apiValue(r, ["OpenInterest(Short)"]),
      apiValue(r, ["ContractValueofOpenInterest(Short)(Thousands)"]),
      apiValue(r, ["OpenInterest(Net)"]),
      apiValue(r, ["ContractValueofOpenInterest(Net)(Thousands)"])
    ]);
  }
  return { found: rows.length > 0, date, rows };
}


async function fetchOpenAPIInstitutionalOptionsRows() {
  const result = await fetchTAIFEXOpenAPI(
    "/MarketDataOfMajorInstitutionalTradersDetailsOfOptionsContractsBytheDate"
  );
  if (!result.found) return result;

  const date = apiDateISO(apiValue(result.rows[0], ["Date", "date"]));
  const txo = result.rows.filter(r =>
    apiValue(r, ["ContractCode", "contractCode"]) === "臺指選擇權"
  );

  const rows = [];
  for (const r of txo) {
    rows.push([
      "臺指選擇權",
      apiValue(r, ["Item", "item"]),
      apiValue(r, ["TradingVolume(Long)"]),
      apiValue(r, ["TradingValue(Long)(Thousands)"]),
      apiValue(r, ["TradingVolume(Short)"]),
      apiValue(r, ["TradingValue(Short)(Thousands)"]),
      apiValue(r, ["TradingVolume(Net)"]),
      apiValue(r, ["TradingValue(Net)(Thousands)"])
    ]);
  }

  return { found: rows.length > 0, date, rows };
}

async function fetchOpenAPIInstitutionalOptions() {
  return fetchOpenAPIInstitutionalOptionsRows();
}

function json(data, status = 200) {
  return new Response(JSON.stringify(data, null, 2), {
    status,
    headers: {
      "content-type": "application/json; charset=utf-8",
      "cache-control": "no-store",
      "access-control-allow-origin": "*"
    }
  });
}

function cleanText(html) {
  return html
    .replace(/<br\s*\/?>/gi, " ")
    .replace(/<[^>]*>/g, " ")
    .replace(/&nbsp;/gi, " ")
    .replace(/&amp;/gi, "&")
    .replace(/&lt;/gi, "<")
    .replace(/&gt;/gi, ">")
    .replace(/&#39;/gi, "'")
    .replace(/&quot;/gi, '"')
    .replace(/\s+/g, " ")
    .trim();
}

function number(value) {
  if (value === undefined || value === null) return null;

  const s = String(value)
    .replace(/,/g, "")
    .replace(/\s/g, "");

  if (!s || s === "-" || s === "--") return 0;

  const n = Number(s);
  return Number.isFinite(n) ? n : null;
}

function parseRows(html) {
  const rows = [];
  const trRegex = /<tr\b[^>]*>([\s\S]*?)<\/tr>/gi;

  let match;

  while ((match = trRegex.exec(html)) !== null) {
    const cells = [];
    const cellRegex =
      /<(td|th)\b[^>]*>([\s\S]*?)<\/\1>/gi;

    let cell;

    while ((cell = cellRegex.exec(match[1])) !== null) {
      cells.push(cleanText(cell[2]));
    }

    if (cells.length) {
      rows.push(cells);
    }
  }

  return rows;
}


async function fetchOpenAPIDeltaForDate(requestedISO) {
  const result = await fetchTAIFEXOpenAPI("/DailyOptionsDelta");
  if (!result.found) return result;

  const dates = [...new Set(result.rows.map(r =>
    apiDateISO(apiValue(r, ["Date", "date"]))
  ).filter(Boolean))];
  const date = dates.includes(requestedISO) ? requestedISO : (dates[0] || null);

  if (requestedISO && !dates.includes(requestedISO)) {
    return {
      found: false,
      date,
      available_dates: dates,
      rows: [],
      reason: `OpenAPI Delta date ${date || "unknown"} does not contain requested ${requestedISO}`
    };
  }

  const rows = [];
  for (const r of result.rows) {
    const contract = apiValue(r, ["Contract", "ContractCode", "contract"]);
    if (contract && contract !== "TXO") continue;

    const month = apiValue(r, ["ContractMonth(Week)", "ContractMonth", "contractMonth"]);
    const expiryRaw = apiValue(r, ["ContractExpiryDate", "ExpiryDate", "contract_expiry_date"]);
    const expiry = expiryRaw ? apiDateISO(expiryRaw) : inferTXOExpiry(month, requestedISO || date);
    const strike = nullableNumber(apiValue(r, ["StrikePrice", "Strike", "strike"]));
    const cpRaw = String(apiValue(r, ["CallPut", "Call_Put", "callPut", "call_put"]) ?? "");
    const type = /Call|買權/i.test(cpRaw) ? "call" : /Put|賣權/i.test(cpRaw) ? "put" : null;
    const delta = nullableNumber(apiValue(r, ["Delta", "delta"]));
    if (!month || !expiry || strike === null || !type || delta === null) continue;

    rows.push({
      contract: "TXO",
      contract_month: month,
      contract_expiry_date: expiry,
      strike,
      type,
      delta
    });
  }

  return {
    found: rows.length > 0,
    date,
    rows,
    source_url: result.source_url,
    reason: rows.length ? null : "OpenAPI Delta returned no usable TXO rows"
  };
}

function fallbackResponseFromRows(rows, status = 200) {
  const html = `<table><tbody>${rows.map(row =>
    `<tr>${row.map(cell => `<td>${String(cell ?? "")}</td>`).join("")}</tr>`
  ).join("")}</tbody></table>`;
  return new Response(html, { status });
}

async function fetchTAIFEXPost(path, body) {

  let primaryError = null;

  try {
    const response = await fetch(`${TAIFEX}${path}`, {
      method: "POST",
      headers: {
        "User-Agent":
          "Mozilla/5.0 (compatible; TAIFEX-Proxy/V1.0-Production)",
        "Accept":
          "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Accept-Language":
          "zh-TW,zh;q=0.9,en;q=0.8",
        "Content-Type":
          "application/x-www-form-urlencoded"
      },
      body
    });

    const html = await response.text();
    const rows = parseRows(html);

    if (response.ok && rows.length) {
      return {
        response,
        html,
        rows,
        source: "taifex_web",
        fallback: false,
        source_url: `${TAIFEX}${path}`
      };
    }

    primaryError = `TAIFEX primary HTTP ${response.status} / rows ${rows.length}`;
  } catch (error) {
    primaryError = error?.message || String(error);
  }

  /* OpenAPI fallback: current/latest TXO chain only. */
  if (path === "/cht/3/optDailyMarketReport") {
    const params = new URLSearchParams(body);
    const commodity = params.get("commodity_id");
    const requested = params.get("queryDate");
    if (commodity === "TXO" && requested) {
      const requestedISO = queryDateToISO(requested);
      const fb = await fetchOpenAPIChainForDate(requestedISO);
      if (fb.found) {
        return {
          response: fallbackResponseFromRows(fb.rows),
          html: `<openapi-fallback>${JSON.stringify(fb.rows)}</openapi-fallback>`,
          rows: fb.rows,
          source: "taifex_openapi",
          fallback: true,
          source_url: "https://openapi.taifex.com.tw/v1/DailyMarketReportOpt",
          requested_date: requestedISO,
          primary_error: primaryError
        };
      }
    }
  }

  /* OpenAPI fallback for Delta. */
  if (path === "/cht/3/optDailyDeltaExcel") {
    const params = new URLSearchParams(body);
    const raw = params.get("queryDate") || params.get("date");
    const requestedISO = raw && raw.length === 8
      ? `${raw.slice(0,4)}-${raw.slice(4,6)}-${raw.slice(6,8)}`
      : raw;
    const fb = await fetchOpenAPIDeltaForDate(requestedISO);
    if (fb.found) {
      return {
        response: fallbackResponseFromRows(fb.rows),
        html: `<openapi-fallback>${JSON.stringify(fb.rows)}</openapi-fallback>`,
        rows: fb.rows,
        source: "taifex_openapi",
        fallback: true,
        source_url: "https://openapi.taifex.com.tw/v1/DailyOptionsDelta",
        requested_date: requestedISO,
        primary_error: primaryError
      };
    }
  }

  return {
    response: new Response(null, { status: 502 }),
    html: "",
    rows: [],
    source: "taifex_web",
    fallback: false,
    source_url: `${TAIFEX}${path}`,
    primary_error: primaryError
  };
}

async function fetchTAIFEX(path) {
  let primaryError = null;

  try {
    const response = await fetch(`${TAIFEX}${path}`, {
      method: "GET",
      headers: {
        "User-Agent":
          "Mozilla/5.0 (compatible; TAIFEX-Proxy/V1.0-Production)",
        "Accept":
          "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Accept-Language":
          "zh-TW,zh;q=0.9,en;q=0.8"
      }
    });

    const html = await response.text();
    const rows = parseRows(html);

    if (response.ok && rows.length) {
      return {
        response,
        html,
        rows,
        source: "taifex_web",
        fallback: false,
        source_url: `${TAIFEX}${path}`
      };
    }
    primaryError = `TAIFEX primary HTTP ${response.status} / rows ${rows.length}`;
  } catch (error) {
    primaryError = error?.message || String(error);
  }

  /* Futures daily market / after-hours fallback. */
  if (path.includes("/futDailyMarketExcel")) {
    const fb = await fetchOpenAPIFuturesForDate();
    if (fb.found) {
      return {
        response: fallbackResponseFromRows(fb.rows),
        html: `<openapi-fallback>${JSON.stringify(fb.rows)}</openapi-fallback>`,
        rows: fb.rows,
        source: "taifex_openapi",
        fallback: true,
        source_url: "https://openapi.taifex.com.tw/v1/DailyMarketReportFut",
        primary_error: primaryError
      };
    }
  }

  /* Futures institutional current-day fallback. */
  if (path === "/cht/3/futContractsDate" || path === "/cht/3/futContractsDateAh") {
    if (path.endsWith("Date")) {
      const fb = await fetchOpenAPIInstitutionalFutures();
      if (fb.found) {
        return {
          response: fallbackResponseFromRows(fb.rows),
          html: `<openapi-fallback>${JSON.stringify(fb.rows)}</openapi-fallback>`,
          rows: fb.rows,
          source: "taifex_openapi",
          fallback: true,
          source_url: "https://openapi.taifex.com.tw/v1/MarketDataOfMajorInstitutionalTradersDetailsOfFuturesContractsBytheDate",
          primary_error: primaryError
        };
      }
    }
  }

  return {
    response: new Response(null, { status: 502 }),
    html: "",
    rows: [],
    source: "taifex_web",
    fallback: false,
    source_url: `${TAIFEX}${path}`,
    primary_error: primaryError
  };
}

function institutionCode(name) {
  if (name === "自營商") return "dealer";
  if (name === "投信") return "investment_trust";
  if (name === "外資") return "foreign";
  if (name === "陸資") return "china_capital";
  return null;
}

/* =========================
   TX 三大法人
========================= */

function parseFuturesInstitutional(rows) {

  const txIndex = rows.findIndex(row =>
    row.includes("臺股期貨")
  );

  if (txIndex < 0) {
    return {
      found: false,
      data: []
    };
  }

  const data = [];

  for (let i = txIndex; i < rows.length; i++) {

    const row = rows[i];

    if (i > txIndex) {

      const product = row.find(x =>
        x.includes("期貨")
      );

      if (
        product &&
        ![
          "自營商",
          "投信",
          "外資",
          "陸資"
        ].includes(product)
      ) {
        break;
      }
    }

    const idx = row.findIndex(x =>
      institutionCode(x)
    );

    if (idx < 0) continue;

    const institution =
      institutionCode(row[idx]);

    const v = row.slice(idx + 1);

    data.push({
      institution,
      long_volume: number(v[0]),
      long_amount: number(v[1]),
      short_volume: number(v[2]),
      short_amount: number(v[3]),
      net_volume: number(v[4]),
      net_amount: number(v[5])
    });

    if (data.length >= 3) break;
  }

  return {
    found: data.length === 3,
    data
  };
}

/* =========================
   TXO 三大法人
========================= */


/* =========================
   TX 三大法人 OI（指定日期）
========================= */

function parseFuturesInstitutionalOI(rows) {

  const txIndex = rows.findIndex(row =>
    row.includes("臺股期貨")
  );

  if (txIndex < 0) {
    return {
      found: false,
      data: []
    };
  }

  const data = [];

  for (let i = txIndex; i < rows.length; i++) {

    const row = rows[i];

    if (i > txIndex) {

      const product = row.find(x =>
        x.includes("期貨")
      );

      if (
        product &&
        ![
          "自營商",
          "投信",
          "外資",
          "陸資"
        ].includes(product)
      ) {
        break;
      }
    }

    const idx = row.findIndex(x =>
      institutionCode(x)
    );

    if (idx < 0) continue;

    const institution =
      institutionCode(row[idx]);

    const v = row.slice(idx + 1);

    /*
     * v:
     * [交易多方口數,
     *  交易多方金額,
     *  交易空方口數,
     *  交易空方金額,
     *  交易淨額口數,
     *  交易淨額金額,
     *  OI多方口數,
     *  OI多方金額,
     *  OI空方口數,
     *  OI空方金額,
     *  OI淨額口數,
     *  OI淨額金額]
     */

    if (v.length < 12) continue;

    data.push({
      institution,

      long_oi:
        number(v[6]),

      long_oi_amount:
        number(v[7]),

      short_oi:
        number(v[8]),

      short_oi_amount:
        number(v[9]),

      net_oi:
        number(v[10]),

      net_oi_amount:
        number(v[11])
    });

    if (data.length >= 3) break;
  }

  return {
    found: data.length === 3,
    data
  };
}

function normalizeQueryDate(value) {

  if (!value) {
    return today();
  }

  const m =
    String(value).match(
      /^(\d{4})-(\d{2})-(\d{2})$/
    );

  if (!m) {
    return null;
  }

  return `${m[1]}/${m[2]}/${m[3]}`;
}

function queryDateToISO(value) {

  const m =
    String(value).match(
      /^(\d{4})\/(\d{2})\/(\d{2})$/
    );

  if (!m) {
    return null;
  }

  return `${m[1]}-${m[2]}-${m[3]}`;
}

function parseOptionsInstitutional(rows) {

  const index = rows.findIndex(row =>
    row.includes("臺指選擇權")
  );

  if (index < 0) {
    return {
      found: false,
      data: []
    };
  }

  const data = [];

  for (let i = index; i < rows.length; i++) {

    const row = rows[i];

    const product = row.find(x =>
      x.includes("選擇權")
    );

    if (
      i > index &&
      product &&
      ![
        "自營商",
        "投信",
        "外資",
        "陸資"
      ].includes(product)
    ) {
      break;
    }

    const idx = row.findIndex(x =>
      institutionCode(x)
    );

    if (idx < 0) continue;

    const institution =
      institutionCode(row[idx]);

    const v = row.slice(idx + 1);

    data.push({
      institution,
      long_volume: number(v[0]),
      long_amount: number(v[1]),
      short_volume: number(v[2]),
      short_amount: number(v[3]),
      net_volume: number(v[4]),
      net_amount: number(v[5])
    });

    if (data.length >= 3) break;
  }

  return {
    found: data.length === 3,
    data
  };
}

/* =========================
   TX 行情
========================= */

function parseTXMarket(rows) {

  const data = [];

  for (const row of rows) {

    if (!row.includes("TX")) continue;

    const idx = row.indexOf("TX");

    if (idx < 0) continue;

    const v = row.slice(idx + 1);

    if (v.length < 12) continue;

    data.push({
      contract_month: v[0],
      open: number(v[1]),
      high: number(v[2]),
      low: number(v[3]),
      close: number(v[4]),
      change: number(
        String(v[5] || "")
          .replace(/[▲▼+]/g, "")
      ),
      change_percent: String(v[6] || "")
        .replace(/[▲▼%+]/g, ""),
      after_hours_volume: number(v[7]),
      regular_volume: number(v[8]),
      total_volume: number(v[9]),
      settlement_price: number(v[10]),
      open_interest: number(v[11]),
      best_bid: number(v[12]),
      best_ask: number(v[13]),
      historical_high: number(v[14]),
      historical_low: number(v[15])
    });
  }

  return data;
}

function nullableNumber(value) {

  if (
    value === undefined ||
    value === null
  ) {
    return null;
  }

  const s = String(value)
    .replace(/,/g, "")
    .replace(/\s/g, "")
    .replace(/[▲▼]/g, "")
    .replace(/%/g, "");

  if (!s || s === "-" || s === "--") {
    return null;
  }

  const n = Number(s);

  return Number.isFinite(n) ? n : null;
}

/* =========================
   TXO 完整 Option Chain
========================= */

function parseTXOOptionChain(rows) {

  const data = [];

  for (const row of rows) {

    /*
     * 官方完整 TXO 行情表的資料列以 TXO 開頭，
     * 欄位順序為：
     *
     * 0  契約
     * 1  到期月份(週別)
     * 2  契約到期日
     * 3  履約價
     * 4  買賣權
     * 5  開盤價
     * 6  最高價
     * 7  最低價
     * 8  最後成交價
     * 9  結算價
     * 10 漲跌價
     * 11 漲跌%
     * 12 盤後交易時段成交量
     * 13 一般交易時段成交量
     * 14 合計成交量
     * 15 未沖銷契約量
     * 16 最後最佳買價
     * 17 最後最佳賣價
     * 18 歷史最高價
     * 19 歷史最低價
     */

    if (
      row.length < 20 ||
      row[0] !== "TXO"
    ) {
      continue;
    }

    const optionType =
      row[4] === "Call"
        ? "call"
        : row[4] === "Put"
          ? "put"
          : null;

    if (!optionType) {
      continue;
    }

    const strike =
      nullableNumber(row[3]);

    if (strike === null) {
      continue;
    }

    data.push({

      contract:
        row[0],

      contract_month:
        row[1],

      contract_expiry_date:
        row[2],

      strike,

      type:
        optionType,

      open:
        nullableNumber(row[5]),

      high:
        nullableNumber(row[6]),

      low:
        nullableNumber(row[7]),

      last:
        nullableNumber(row[8]),

      settlement:
        nullableNumber(row[9]),

      change:
        nullableNumber(row[10]),

      change_percent:
        nullableNumber(row[11]),

      after_hours_volume:
        nullableNumber(row[12]),

      regular_volume:
        nullableNumber(row[13]),

      total_volume:
        nullableNumber(row[14]),

      open_interest:
        nullableNumber(row[15]),

      best_bid:
        nullableNumber(row[16]),

      best_ask:
        nullableNumber(row[17]),

      historical_high:
        nullableNumber(row[18]),

      historical_low:
        nullableNumber(row[19])
    });
  }

  return {
    found: data.length > 0,
    data
  };
}

function parseAnchors(html) {

  const links = [];
  const regex =
    /<a\b[^>]*href\s*=\s*["']([^"']+)["'][^>]*>([\s\S]*?)<\/a>/gi;

  let match;

  while ((match = regex.exec(html)) !== null) {

    links.push({
      href: match[1],
      text: cleanText(match[2])
    });
  }

  return links;
}

async function fetchTAIFEXText(url) {

  const response = await fetch(url, {
    headers: {
      "User-Agent":
        "Mozilla/5.0 (compatible; TAIFEX-Proxy/V1.0 — Production)",
      "Accept":
        "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
      "Accept-Language":
        "zh-TW,zh;q=0.9,en;q=0.8"
    }
  });

  return {
    response,
    text: await response.text()
  };
}


async function fetchTAIEXCloseForDate(requestedISO) {
  const sourceUrl =
    `${TWSE_OPENAPI}/exchangeReport/FMTQIK`;

  let response;

  try {
    response = await fetch(sourceUrl, {
      headers: {
        "User-Agent":
          "Mozilla/5.0 (compatible; TAIFEX-Proxy/V1.0 — Production)",
        "Accept":
          "application/json,text/plain,*/*"
      }
    });
  } catch (error) {
    return {
      found: false,
      reason:
        `TWSE FMTQIK fetch failed: ${error?.message || String(error)}`,
      source_url: sourceUrl
    };
  }

  if (!response.ok) {
    return {
      found: false,
      reason:
        `TWSE FMTQIK HTTP ${response.status}`,
      source_url: sourceUrl
    };
  }

  let payload;

  try {
    payload = await response.json();
  } catch (error) {
    return {
      found: false,
      reason:
        "TWSE FMTQIK response is not valid JSON",
      source_url: sourceUrl
    };
  }

  /*
   * Normalize both known TWSE OpenAPI shapes:
   *   [{...}, {...}]
   *   { fields: [...], data: [[...], [...]] }
   */
  let rows = [];

  if (Array.isArray(payload)) {
    rows = payload;
  } else if (
    payload &&
    Array.isArray(payload.fields) &&
    Array.isArray(payload.data)
  ) {
    rows = payload.data.map(values => {
      const row = {};
      payload.fields.forEach((field, index) => {
        row[field] =
          Array.isArray(values)
            ? values[index]
            : null;
      });
      return row;
    });
  }

  if (!rows.length) {
    return {
      found: false,
      reason: "TWSE FMTQIK returned no rows",
      source_url: sourceUrl
    };
  }

  const digits = value =>
    String(value ?? "").replace(/\D/g, "");

  const requestedDigits =
    digits(requestedISO);

  const normalizeDate = value => {
    const raw = digits(value);

    if (!raw) return "";

    if (raw === requestedDigits) return raw;

    // ROC 1150902 -> Gregorian 20260902
    if (raw.length === 7) {
      return (
        `${Number(raw.slice(0, 3)) + 1911}` +
        raw.slice(3)
      );
    }

    return raw;
  };

  const dateKeys = [
    "Date",
    "date",
    "日期",
    "交易日期"
  ];

  const taiexKeys = [
    "TAIEX",
    "taiex",
    "發行量加權股價指數",
    "發行量加權指數",
    "TAIEX指數",
    "Index",
    "index"
  ];

  const getField = (row, keys) => {
    for (const key of keys) {
      if (
        row &&
        Object.prototype.hasOwnProperty.call(row, key)
      ) {
        return row[key];
      }
    }
    return null;
  };

  const row =
    rows.find(item => {
      const rawDate =
        getField(item, dateKeys);

      if (
        rawDate === null ||
        rawDate === undefined ||
        rawDate === ""
      ) {
        return false;
      }

      return (
        normalizeDate(rawDate) ===
        requestedDigits
      );
    }) || null;

  if (!row) {
    return {
      found: false,
      reason:
        `TAIEX close for ${requestedISO} not found in TWSE FMTQIK`,
      source_url: sourceUrl,
      available_dates:
        rows
          .map(item =>
            getField(item, dateKeys)
          )
          .filter(
            value =>
              value !== null &&
              value !== undefined
          )
          .slice(0, 20)
    };
  }

  const close =
    nullableNumber(
      getField(row, taiexKeys)
    );

  if (
    close === null ||
    close <= 0
  ) {
    return {
      found: false,
      reason:
        "TAIEX close is missing or invalid",
      source_url: sourceUrl,
      available_fields:
        Object.keys(row)
    };
  }

  return {
    found: true,
    date: requestedISO,
    close,
    source: "TWSE FMTQIK",
    source_url: sourceUrl
  };
}

function normalCdf(x) {
  const sign = x < 0 ? -1 : 1;
  const z = Math.abs(x);
  const p = 0.2316419;
  const b1 = 0.319381530;
  const b2 = -0.356563782;
  const b3 = 1.781477937;
  const b4 = -1.821255978;
  const b5 = 1.330274429;
  const q = 1 / (1 + p * z);
  const poly =
    ((((b5 * q + b4) * q + b3) * q + b2) * q + b1) * q;
  const pdf =
    Math.exp(-0.5 * z * z) /
    Math.sqrt(2 * Math.PI);
  const cdf = 1 - pdf * poly;
  return sign > 0 ? cdf : 1 - cdf;
}

function normalPdf(x) {
  return (
    Math.exp(-0.5 * x * x) /
    Math.sqrt(2 * Math.PI)
  );
}

function bsPrice(type, S, K, T, sigma, r = 0) {
  if (
    S <= 0 ||
    K <= 0 ||
    T <= 0 ||
    sigma <= 0
  ) return null;

  const sqrtT = Math.sqrt(T);
  const d1 =
    (
      Math.log(S / K) +
      (r + 0.5 * sigma * sigma) * T
    ) /
    (sigma * sqrtT);
  const d2 = d1 - sigma * sqrtT;

  if (type === "call") {
    return (
      S * normalCdf(d1) -
      K * Math.exp(-r * T) * normalCdf(d2)
    );
  }

  return (
    K * Math.exp(-r * T) * normalCdf(-d2) -
    S * normalCdf(-d1)
  );
}

function impliedVolatilityFromPrice(
  type,
  price,
  S,
  K,
  T,
  r = 0
) {
  if (
    !Number.isFinite(price) ||
    price <= 0
  ) return null;

  const intrinsic =
    type === "call"
      ? Math.max(0, S - K)
      : Math.max(0, K - S);

  if (price + 1e-8 < intrinsic) return null;

  let lo = 0.0001;
  let hi = 5.0;

  const upper =
    bsPrice(type, S, K, T, hi, r);

  if (
    upper === null ||
    upper < price
  ) return null;

  for (let i = 0; i < 80; i++) {
    const mid = (lo + hi) / 2;
    const value =
      bsPrice(type, S, K, T, mid, r);

    if (value === null) return null;

    if (value > price) hi = mid;
    else lo = mid;
  }

  return (lo + hi) / 2;
}

function bsGamma(S, K, T, sigma, r = 0) {
  if (
    S <= 0 ||
    K <= 0 ||
    T <= 0 ||
    sigma <= 0
  ) return null;

  const d1 =
    (
      Math.log(S / K) +
      (r + 0.5 * sigma * sigma) * T
    ) /
    (sigma * Math.sqrt(T));

  return (
    normalPdf(d1) /
    (S * sigma * Math.sqrt(T))
  );
}

function daysToExpiry(expiry, requestedISO) {
  return (
    new Date(`${expiry}T00:00:00Z`).getTime() -
    new Date(`${requestedISO}T00:00:00Z`).getTime()
  ) / 86400000;
}

function dealerGexSign(type) {
  /*
   * Signed GEX convention used by this model:
   *   Call = positive
   *   Put  = negative
   *
   * This is a market-positioning convention, NOT a claim that
   * TAIFEX publishes dealer-side option positions. Therefore
   * every output is explicitly labeled "derived GEX".
   */
  return type === "call" ? 1 : -1;
}

function parseTXODeltaRows(rows) {

  const data = [];

  for (const row of rows) {

    if (row.length < 7) continue;

    if (row[0] !== "TXO") continue;

    const optionType =
      row[2] === "Call" || row[2] === "買權"
        ? "call"
        : row[2] === "Put" || row[2] === "賣權"
          ? "put"
          : null;

    if (!optionType) continue;

    const strike =
      nullableNumber(row[5]);

    const delta =
      nullableNumber(row[6]);

    if (
      strike === null ||
      delta === null
    ) {
      continue;
    }

    data.push({
      contract: row[0],
      contract_month: row[3],
      contract_expiry_date:
        isoCompactDate(row[4]),
      strike,
      type: optionType,
      delta
    });
  }

  return data;
}

async function fetchTXODeltaForDate(requestedISO) {

  /*
   * TAIFEX publishes the previous 30 trading days on the
   * Delta download page. The visible page does not expose
   * the download URL as normal anchor text; the download
   * action is generated by the page JavaScript.
   *
   * v4.7 therefore:
   * 1) fetches the historical page;
   * 2) verifies the requested date is listed;
   * 3) tries the official Excel endpoint with the historical
   *    date parameters used by TAIFEX;
   * 4) accepts either an HTML table response or a textual
   *    tabular response.
   */

  const index =
    await fetchTAIFEXText(
      `${TAIFEX}/cht/3/dlOptDailyDelta`
    );

  if (!index.response.ok) {
    const fallback = await fetchOpenAPIDeltaForDate(requestedISO);
    if (fallback.found) return fallback;
    return {
      found: false,
      reason:
        `TAIFEX Delta index HTTP ${index.response.status}; OpenAPI fallback unavailable`,
      source_url: fallback.source_url || null,
      raw_rows: 0,
      rows: []
    };
  }

  const compact =
    requestedISO.replace(/-/g, "");

  /*
   * Confirm the requested date is actually present in the
   * 30-day historical list before requesting the file.
   */
  if (!index.text.includes(compact)) {
    const fallback = await fetchOpenAPIDeltaForDate(requestedISO);
    if (fallback.found) return fallback;
    return {
      found: false,
      reason:
        `TAIFEX Delta date ${compact} is not listed; OpenAPI fallback unavailable`,
      source_url: fallback.source_url || null,
      raw_rows: 0,
      rows: []
    };
  }

  const endpoint =
    `${TAIFEX}/cht/3/optDailyDeltaExcel`;

  const bodies = [

    new URLSearchParams({
      queryDate:
        compact,
      queryDate2:
        compact,
      date:
        compact,
      scd_kind_id:
        "TXO"
    }).toString(),

    new URLSearchParams({
      queryDate:
        requestedISO,
      queryDate2:
        requestedISO,
      date:
        requestedISO,
      scd_kind_id:
        "TXO"
    }).toString(),

    new URLSearchParams({
      scd_kind_id:
        "TXO",
      date:
        compact
    }).toString()
  ];

  let lastStatus = null;

  for (const body of bodies) {

    try {

      const result =
        await fetchTAIFEXPost(
          "/cht/3/optDailyDeltaExcel",
          body
        );

      lastStatus =
        result.response.status;

      if (!result.response.ok) {
        continue;
      }

      if (!result.html) {
        continue;
      }

      const rows =
        parseRows(
          result.html
        );

      if (!rows.length) {
        continue;
      }

      const data =
        parseTXODeltaRows(rows);

      /*
       * Reject a response that is merely the download page
       * or a non-TXO table.
       */
      const txo =
        data.filter(row =>
          row.contract_month &&
          (
            String(row.contract_month)
              .startsWith("202")
          )
        );

      if (txo.length) {

        return {
          found: true,
          source_url:
            endpoint,
          raw_rows:
            rows.length,
          rows:
            txo
        };
      }

    } catch (_) {
      continue;
    }
  }

  return {
    found: false,
    reason:
      `TAIFEX historical Delta file could not be parsed (last HTTP ${lastStatus ?? "unknown"})`,
    source_url:
      endpoint,
    raw_rows: 0,
    rows: []
  };
}

function buildGammaProxy(
  chain,
  deltaRows
) {

  const primary =
    choosePrimaryTXOExpiry(
      chain,
      today()
    );

  /*
   * Gamma is estimated from the slope of TAIFEX's
   * published Delta by strike. This is intentionally
   * called a Gamma Proxy, not theoretical Gamma.
   */
  const deltaMap =
    new Map();

  for (const row of deltaRows) {

    deltaMap.set(
      `${row.contract_month}|${row.contract_expiry_date}|${row.type}|${row.strike}`,
      row.delta
    );
  }

  const expiry =
    choosePrimaryTXOExpiry(
      chain,
      today()
    );

  if (!expiry) {
    return {
      found: false,
      reason:
        "No primary TXO expiry"
    };
  }

  const filtered =
    chain.filter(row =>
      row.contract_month ===
        expiry.contract_month &&
      isoCompactDate(
        row.contract_expiry_date
      ) === expiry.expiry
    );

  const strikes =
    [...new Set(
      filtered.map(row => row.strike)
    )].sort(
      (a, b) => a - b
    );

  const deltaFor =
    (type, strike) =>
      deltaMap.get(
        `${expiry.contract_month}|${expiry.expiry}|${type}|${strike}`
      );

  const levels = [];

  for (const strike of strikes) {

    const parts = [];

    for (const type of ["call", "put"]) {

      const left =
        deltaFor(
          type,
          strike - 50
        );

      const right =
        deltaFor(
          type,
          strike + 50
        );

      if (
        left === undefined ||
        right === undefined
      ) {
        continue;
      }

      const slope =
        (right - left) / 100;

      /*
       * Call delta decreases as strike rises.
       * Put delta increases as strike rises.
       * Both therefore map to positive gamma proxy
       * through the appropriate sign.
       */
      const gammaProxy =
        type === "call"
          ? -slope
          : slope;

      if (
        Number.isFinite(gammaProxy) &&
        gammaProxy > 0
      ) {
        parts.push({
          type,
          gamma_proxy:
            gammaProxy
        });
      }
    }

    if (!parts.length) continue;

    const gammaProxy =
      parts.reduce(
        (sum, x) =>
          sum + x.gamma_proxy,
        0
      ) / parts.length;

    const rowsAtStrike =
      filtered.filter(
        row =>
          row.strike === strike &&
          Number(row.open_interest) > 0
      );

    let signedGEX = 0;

    for (const row of rowsAtStrike) {

      /*
       * OI-based GEX convention:
       * Call = positive
       * Put  = negative
       *
       * This is a positioning assumption and is
       * therefore explicitly labelled as a proxy.
       */
      const sign =
        row.type === "call"
          ? 1
          : -1;

      signedGEX +=
        sign *
        row.open_interest *
        gammaProxy;
    }

    levels.push({
      strike,
      gamma_proxy:
        gammaProxy,
      signed_gex_proxy:
        signedGEX
    });
  }

  if (!levels.length) {
    return {
      found: false,
      reason:
        "No overlapping TAIFEX Delta and TXO chain strikes"
    };
  }

  const gammaWall =
    [...levels].sort(
      (a, b) =>
        Math.abs(b.signed_gex_proxy) -
          Math.abs(a.signed_gex_proxy) ||
        a.strike - b.strike
    )[0];

  let cumulative = 0;
  let previous = null;
  let gammaFlip = null;

  for (const level of levels) {

    cumulative +=
      level.signed_gex_proxy;

    level.cumulative_gex_proxy =
      cumulative;

    if (
      previous &&
      (
        previous.cumulative_gex_proxy === 0 ||
        cumulative === 0 ||
        (
          previous.cumulative_gex_proxy < 0 &&
          cumulative > 0
        ) ||
        (
          previous.cumulative_gex_proxy > 0 &&
          cumulative < 0
        )
      )
    ) {

      const x1 =
        previous.strike;

      const x2 =
        level.strike;

      const y1 =
        previous.cumulative_gex_proxy;

      const y2 =
        cumulative;

      const ratio =
        y2 === y1
          ? 0
          : -y1 / (y2 - y1);

      gammaFlip =
        x1 +
        (x2 - x1) *
        Math.max(
          0,
          Math.min(1, ratio)
        );

      break;
    }

    previous = level;
  }

  return {

    found: true,

    primary_expiry: {
      contract_month:
        expiry.contract_month,
      expiry:
        expiry.expiry
    },

    gamma_wall: {
      strike:
        gammaWall.strike,
      signed_gex_proxy:
        gammaWall.signed_gex_proxy,
      gamma_proxy:
        gammaWall.gamma_proxy
    },

    gamma_flip:
      gammaFlip,

    methodology: {
      delta_source:
        "TAIFEX Daily Delta",
      gamma_method:
        "central Delta slope across 100-point strike span",
      gex_method:
        "OI × Gamma Proxy; Call positive / Put negative",
      caveat:
        "Gamma Wall and Gamma Flip are positioning proxies, not dealer-confirmed GEX"
    },

    levels
  };
}

/* =========================
   TXO Key Levels
   Call Wall / Put Wall / Max Pain
========================= */

function isoCompactDate(value) {

  if (!value) return null;

  const s = String(value).replace(/[^0-9]/g, "");

  if (s.length !== 8) return null;

  return `${s.slice(0, 4)}-${s.slice(4, 6)}-${s.slice(6, 8)}`;
}

function choosePrimaryTXOExpiry(data, requestedISO) {

  const requested =
    new Date(`${requestedISO}T00:00:00Z`);

  const expiryMap = new Map();

  for (const row of data) {

    const expiry =
      isoCompactDate(
        row.contract_expiry_date
      );

    if (!expiry) continue;

    const expiryDate =
      new Date(`${expiry}T00:00:00Z`);

    if (
      expiryDate >= requested
    ) {
      expiryMap.set(
        `${row.contract_month}|${expiry}`,
        {
          contract_month:
            row.contract_month,
          expiry
        }
      );
    }
  }

  const candidates =
    [...expiryMap.values()]
      .sort(
        (a, b) =>
          new Date(`${a.expiry}T00:00:00Z`) -
          new Date(`${b.expiry}T00:00:00Z`)
      );

  return candidates[0] || null;
}

function calculateTXOKeyLevels(
  data,
  requestedISO
) {

  const primary =
    choosePrimaryTXOExpiry(
      data,
      requestedISO
    );

  if (!primary) {
    return {
      found: false,
      reason:
        "No valid TXO expiry on or after requested date"
    };
  }

  const chain =
    data.filter(row =>
      row.contract_month ===
        primary.contract_month &&
      isoCompactDate(
        row.contract_expiry_date
      ) === primary.expiry
    );

  const calls =
    chain
      .filter(
        row =>
          row.type === "call" &&
          Number(row.open_interest) > 0
      );

  const puts =
    chain
      .filter(
        row =>
          row.type === "put" &&
          Number(row.open_interest) > 0
      );

  if (!calls.length || !puts.length) {
    return {
      found: false,
      reason:
        "Primary expiry does not contain both Call and Put OI"
    };
  }

  const callWall =
    [...calls].sort(
      (a, b) =>
        b.open_interest - a.open_interest ||
        a.strike - b.strike
    )[0];

  const putWall =
    [...puts].sort(
      (a, b) =>
        b.open_interest - a.open_interest ||
        a.strike - b.strike
    )[0];

  const strikes =
    [...new Set(
      chain.map(row => row.strike)
    )].sort(
      (a, b) => a - b
    );

  /*
   * Max Pain:
   * For each candidate settlement strike S,
   * calculate total intrinsic loss:
   *
   * Call: OI × max(0, S - K)
   * Put : OI × max(0, K - S)
   *
   * The strike with the minimum total pain
   * is Max Pain.
   */
  const painTable =
    strikes.map(S => {

      let callPain = 0;
      let putPain = 0;

      for (const row of calls) {

        callPain +=
          row.open_interest *
          Math.max(
            0,
            S - row.strike
          );
      }

      for (const row of puts) {

        putPain +=
          row.open_interest *
          Math.max(
            0,
            row.strike - S
          );
      }

      return {
        strike: S,
        call_pain: callPain,
        put_pain: putPain,
        total_pain:
          callPain + putPain
      };
    });

  const maxPain =
    [...painTable].sort(
      (a, b) =>
        a.total_pain - b.total_pain ||
        a.strike - b.strike
    )[0];

  return {

    found: true,

    primary_expiry: {
      contract_month:
        primary.contract_month,
      expiry:
        primary.expiry
    },

    call_wall: {
      strike:
        callWall.strike,
      open_interest:
        callWall.open_interest
    },

    put_wall: {
      strike:
        putWall.strike,
      open_interest:
        putWall.open_interest
    },

    max_pain: {
      strike:
        maxPain.strike,
      total_pain:
        maxPain.total_pain,
      call_pain:
        maxPain.call_pain,
      put_pain:
        maxPain.put_pain
    },

    chain_stats: {
      rows:
        chain.length,
      call_rows:
        calls.length,
      put_rows:
        puts.length,
      strike_count:
        strikes.length
    }
  };
}


/* =========================
   V5.0 Unified TXO Production Engine
========================= */

function expiryKey(row) {
  const expiry = isoCompactDate(row.contract_expiry_date);
  if (!expiry) return null;
  return `${row.contract_month}|${expiry}`;
}

function uniqueExpiries(rows, requestedISO) {
  const requested = new Date(`${requestedISO}T00:00:00Z`);
  const map = new Map();

  for (const row of rows) {
    const expiry = isoCompactDate(row.contract_expiry_date);
    if (!expiry) continue;

    const d = new Date(`${expiry}T00:00:00Z`);
    if (d < requested) continue;

    const key = `${row.contract_month}|${expiry}`;
    map.set(key, {
      contract_month: row.contract_month,
      expiry
    });
  }

  return [...map.values()].sort((a, b) =>
    new Date(`${a.expiry}T00:00:00Z`) -
    new Date(`${b.expiry}T00:00:00Z`)
  );
}

function findCommonExpiry(chain, deltaRows, requestedISO) {
  const chainKeys = new Map();

  for (const x of uniqueExpiries(chain, requestedISO)) {
    chainKeys.set(`${x.contract_month}|${x.expiry}`, x);
  }

  for (const x of uniqueExpiries(deltaRows, requestedISO)) {
    const key = `${x.contract_month}|${x.expiry}`;
    if (chainKeys.has(key)) {
      return chainKeys.get(key);
    }
  }

  /*
   * TAIFEX can use different contract-month labels for the
   * same expiry in different reports. Fall back to expiry
   * date only, but only when the date is unique on both sides.
   */
  const chainByDate = new Map();
  for (const x of uniqueExpiries(chain, requestedISO)) {
    const arr = chainByDate.get(x.expiry) || [];
    arr.push(x);
    chainByDate.set(x.expiry, arr);
  }

  for (const x of uniqueExpiries(deltaRows, requestedISO)) {
    const matches = chainByDate.get(x.expiry) || [];
    if (matches.length === 1) return matches[0];
  }

  return null;
}

function filterExpiry(rows, expiry, allowLabelMismatch = false) {
  if (!expiry) return [];

  return rows.filter(row => {
    const rowExpiry = isoCompactDate(row.contract_expiry_date);
    if (rowExpiry !== expiry.expiry) return false;

    if (allowLabelMismatch) return true;

    return row.contract_month === expiry.contract_month;
  });
}

function calculateKeyLevelsForExpiry(chain, expiry) {
  const rows = filterExpiry(chain, expiry, false);

  const calls = rows.filter(
    r => r.type === "call" && Number(r.open_interest) > 0
  );
  const puts = rows.filter(
    r => r.type === "put" && Number(r.open_interest) > 0
  );

  if (!calls.length || !puts.length) {
    return {
      found: false,
      reason: "Primary chain expiry does not contain both Call and Put OI"
    };
  }

  const callWall = [...calls].sort(
    (a, b) =>
      b.open_interest - a.open_interest ||
      a.strike - b.strike
  )[0];

  const putWall = [...puts].sort(
    (a, b) =>
      b.open_interest - a.open_interest ||
      a.strike - b.strike
  )[0];

  const strikes = [...new Set(rows.map(r => r.strike))].sort((a, b) => a - b);

  const painTable = strikes.map(S => {
    let callPain = 0;
    let putPain = 0;

    for (const r of calls) {
      callPain += r.open_interest * Math.max(0, S - r.strike);
    }
    for (const r of puts) {
      putPain += r.open_interest * Math.max(0, r.strike - S);
    }

    return {
      strike: S,
      call_pain: callPain,
      put_pain: putPain,
      total_pain: callPain + putPain
    };
  });

  const maxPain = [...painTable].sort(
    (a, b) =>
      a.total_pain - b.total_pain ||
      a.strike - b.strike
  )[0];

  return {
    found: true,
    call_wall: {
      strike: callWall.strike,
      open_interest: callWall.open_interest
    },
    put_wall: {
      strike: putWall.strike,
      open_interest: putWall.open_interest
    },
    max_pain: {
      strike: maxPain.strike,
      total_pain: maxPain.total_pain,
      call_pain: maxPain.call_pain,
      put_pain: maxPain.put_pain
    },
    chain_stats: {
      rows: rows.length,
      call_rows: calls.length,
      put_rows: puts.length,
      strike_count: strikes.length
    }
  };
}


function buildGammaForCommonExpiry(
  chain,
  deltaRows,
  expiry,
  underlyingPrice,
  requestedISO
) {

  const chainRows =
    filterExpiry(chain, expiry, false);

  const deltaRowsForExpiry =
    filterExpiry(deltaRows, expiry, true);

  const chainKeys =
    new Set(
      chainRows.map(
        r => `${r.strike}|${r.type}`
      )
    );

  const deltaKeys =
    new Set(
      deltaRowsForExpiry
        .filter(
          r => Number.isFinite(Number(r.delta))
        )
        .map(
          r => `${r.strike}|${r.type}`
        )
    );

  let matched = 0;
  for (const key of chainKeys) {
    if (deltaKeys.has(key)) matched++;
  }

  if (!matched) {
    return {
      found: false,
      reason: "No overlapping Chain/Delta strike keys",
      chain_rows: chainRows.length,
      delta_rows: deltaRowsForExpiry.length,
      matched_strikes: 0
    };
  }

  if (
    !Number.isFinite(underlyingPrice) ||
    underlyingPrice <= 0
  ) {
    return {
      found: false,
      reason: "Underlying TAIEX spot/index price unavailable; TX futures price is not substituted",
      chain_rows: chainRows.length,
      delta_rows: deltaRowsForExpiry.length,
      matched_strikes: matched
    };
  }

  const days =
    daysToExpiry(expiry.expiry, requestedISO);

  if (!Number.isFinite(days) || days <= 0) {
    return {
      found: false,
      reason: "Gamma expiry is not in the future",
      chain_rows: chainRows.length,
      delta_rows: deltaRowsForExpiry.length,
      matched_strikes: matched
    };
  }

  const T = days / 365;
  const modeled = [];

  /*
   * GEX Diagnostic Counters
   * -----------------------
   * These counters are observability only. They do not alter
   * the existing GEX mathematics or production thresholds.
   */
  const gammaDiagnostics = {
    chain_rows: chainRows.length,
    delta_rows: deltaRowsForExpiry.length,
    matched_strike_keys: matched,
    positive_oi_settlement_eligible: 0,
    invalid_oi: 0,
    invalid_settlement: 0,
    below_intrinsic: 0,
    iv_failed: 0,
    iv_out_of_range: 0,
    gamma_failed: 0,
    modeled_contracts: 0
  };

  for (const r of chainRows) {

    const oi = Number(r.open_interest);
    const settlement = Number(r.settlement);

    if (!Number.isFinite(oi) || oi <= 0) {
      gammaDiagnostics.invalid_oi++;
      continue;
    }

    if (!Number.isFinite(settlement) || settlement <= 0) {
      gammaDiagnostics.invalid_settlement++;
      continue;
    }

    /*
     * Eligible means positive OI + positive settlement +
     * matching Chain/Delta key. Keep this explicit so the
     * diagnostic denominator can be reconciled with the
     * modeled-contract count.
     */
    if (deltaKeys.has(`${r.strike}|${r.type}`)) {
      gammaDiagnostics.positive_oi_settlement_eligible++;
    }

    const intrinsic =
      r.type === "call"
        ? Math.max(0, underlyingPrice - r.strike)
        : Math.max(0, r.strike - underlyingPrice);

    if (settlement + 1e-8 < intrinsic) {
      gammaDiagnostics.below_intrinsic++;
      continue;
    }

    const iv =
      impliedVolatilityFromPrice(
        r.type,
        settlement,
        underlyingPrice,
        r.strike,
        T,
        0
      );

    if (!Number.isFinite(iv)) {
      gammaDiagnostics.iv_failed++;
      continue;
    }

    if (iv <= 0 || iv > 5) {
      gammaDiagnostics.iv_out_of_range++;
      continue;
    }

    const gamma =
      bsGamma(
        underlyingPrice,
        r.strike,
        T,
        iv,
        0
      );

    if (!Number.isFinite(gamma) || gamma <= 0) {
      gammaDiagnostics.gamma_failed++;
      continue;
    }

    const gex1pct =
      gamma *
      oi *
      50 *
      underlyingPrice *
      underlyingPrice *
      0.01;

    gammaDiagnostics.modeled_contracts++;

    modeled.push({
      strike: r.strike,
      type: r.type,
      open_interest: oi,
      settlement,
      implied_volatility: iv,
      gamma,
      signed_gex_1pct:
        gex1pct *
        dealerGexSign(r.type)
    });
  }

  /*
   * Production quality gate:
   * GEX is considered usable only when a meaningful portion of
   * matched positive-OI contracts can be modeled from settlement.
   * This prevents a tiny surviving subset from producing a
   * misleading "usable" GEX result.
   */
  const matchedPositiveOiRows =
    chainRows.filter(r =>
      Number(r.open_interest) > 0 &&
      deltaKeys.has(`${r.strike}|${r.type}`) &&
      Number(r.settlement) > 0
    ).length;

  const modelCoverage =
    matchedPositiveOiRows > 0
      ? modeled.length / matchedPositiveOiRows
      : 0;

  const minimumCoverage = 0.50;

  if (
    !modeled.length ||
    modelCoverage < minimumCoverage
  ) {
    return {
      found: false,
      reason:
        !modeled.length
          ? "No valid option IV/Gamma could be modeled from settlement prices"
          : "GEX model coverage below production threshold",
      chain_rows: chainRows.length,
      delta_rows: deltaRowsForExpiry.length,
      matched_strikes: matched,
      modeled_contracts: modeled.length,
      eligible_contracts: matchedPositiveOiRows,
      model_coverage: modelCoverage,
      minimum_model_coverage: minimumCoverage,
      gamma_diagnostics: {
        ...gammaDiagnostics,
        modeled_contracts: modeled.length
      }
    };
  }

  const byStrike = new Map();

  for (const r of modeled) {
    const item =
      byStrike.get(r.strike) || {
        strike: r.strike,
        call_gex_1pct: 0,
        put_gex_1pct: 0,
        net_gex_1pct: 0,
        gross_gex_1pct: 0,
        call_oi: 0,
        put_oi: 0
      };

    if (r.type === "call") {
      item.call_gex_1pct += r.signed_gex_1pct;
      item.call_oi += r.open_interest;
    } else {
      item.put_gex_1pct += r.signed_gex_1pct;
      item.put_oi += r.open_interest;
    }

    item.net_gex_1pct =
      item.call_gex_1pct +
      item.put_gex_1pct;

    item.gross_gex_1pct =
      Math.abs(item.call_gex_1pct) +
      Math.abs(item.put_gex_1pct);

    byStrike.set(r.strike, item);
  }

  const levels =
    [...byStrike.values()]
      .sort((a, b) => a.strike - b.strike);

  const gammaWall =
    [...levels].sort(
      (a, b) =>
        Math.abs(b.net_gex_1pct) -
        Math.abs(a.net_gex_1pct) ||
        a.strike - b.strike
    )[0];

  const netGexCurrent =
    levels.reduce(
      (sum, x) =>
        sum + x.net_gex_1pct,
      0
    );

  const grossGexCurrent =
    levels.reduce(
      (sum, x) =>
        sum + x.gross_gex_1pct,
      0
    );

  const loS =
    underlyingPrice * 0.90;

  const hiS =
    underlyingPrice * 1.10;

  const step =
    Math.max(
      10,
      Math.round(
        underlyingPrice * 0.00025
      )
    );

  function totalGexAt(S) {
    let total = 0;

    for (const r of modeled) {
      const gamma =
        bsGamma(
          S,
          r.strike,
          T,
          r.implied_volatility,
          0
        );

      if (!Number.isFinite(gamma)) continue;

      total +=
        gamma *
        r.open_interest *
        50 *
        S *
        S *
        0.01 *
        dealerGexSign(r.type);
    }

    return total;
  }

  let previousS = loS;
  let previousGex = totalGexAt(previousS);
  let gammaFlip = null;

  for (
    let S = loS + step;
    S <= hiS + step / 2;
    S += step
  ) {

    const currentGex =
      totalGexAt(S);

    if (
      Number.isFinite(previousGex) &&
      Number.isFinite(currentGex) &&
      (
        (previousGex < 0 && currentGex > 0) ||
        (previousGex > 0 && currentGex < 0)
      )
    ) {

      const estimated =
        previousGex === currentGex
          ? previousS
          : previousS +
            (
              -previousGex *
              (S - previousS)
            ) /
            (currentGex - previousGex);

      gammaFlip = {
        lower_underlying: previousS,
        upper_underlying: S,
        estimated_underlying: estimated,
        lower_net_gex_1pct: previousGex,
        upper_net_gex_1pct: currentGex
      };

      break;
    }

    previousS = S;
    previousGex = currentGex;
  }

  return {
    found: true,
    model:
      "Black-Scholes Gamma using TAIFEX settlement-implied volatility",
    dealer_sign_convention:
      "calls positive / puts negative; customer-long dealer-short assumption",
    underlying_price: underlyingPrice,
    time_to_expiry_days: days,

    /*
     * Source metadata from the SAME Chain/Delta universe
     * actually used by this Gamma calculation.
     * These are diagnostic counters, not additional inputs
     * and do not alter the GEX mathematics.
     */
    chain_rows: chainRows.length,
    delta_rows: deltaRowsForExpiry.length,
    matched_strikes: matched,

    option_contracts_modeled: modeled.length,
    eligible_contracts: matchedPositiveOiRows,
    model_coverage: modelCoverage,
    gamma_diagnostics: {
      ...gammaDiagnostics,
      modeled_contracts: modeled.length
    },
    model_quality:
      modelCoverage >= minimumCoverage
        ? "usable"
        : "insufficient",
    gamma_wall: {
      strike: gammaWall.strike,
      net_gex_1pct: gammaWall.net_gex_1pct,
      gross_gex_1pct: gammaWall.gross_gex_1pct
    },
    gamma_flip: gammaFlip,
    net_gex_1pct: netGexCurrent,
    gross_gex_1pct: grossGexCurrent,
    levels
  };
}

function buildDataQuality(chain, deltaRows, requestedISO, commonExpiry) {
  const chainExpiries = uniqueExpiries(chain, requestedISO);
  const deltaExpiries = uniqueExpiries(deltaRows, requestedISO);

  const deltaKeySet = new Set(
    deltaRows.map(r =>
      `${r.contract_month}|${isoCompactDate(r.contract_expiry_date)}|${r.type}|${r.strike}`
    )
  );

  let matched = 0;
  let unmatchedChain = 0;

  for (const r of chain) {
    const key =
      `${r.contract_month}|${isoCompactDate(r.contract_expiry_date)}|${r.type}|${r.strike}`;
    if (deltaKeySet.has(key)) matched++;
    else unmatchedChain++;
  }

  return {
    chain_contracts: chain.length,
    delta_rows: deltaRows.length,
    chain_expiry_count: chainExpiries.length,
    delta_expiry_count: deltaExpiries.length,
    matched_contract_keys: matched,
    unmatched_chain_contracts: unmatchedChain,
    common_expiry: commonExpiry || null,
    status:
      commonExpiry && matched > 0
        ? "usable"
        : "insufficient_overlap"
  };
}

async function fetchTXOChainForDate(taifexDate) {
  const body = new URLSearchParams({
    queryType: "2",
    marketCode: "0",
    dateaddcnt: "",
    commodity_id: "TXO",
    commodity_id2: "",
    queryDate: taifexDate,
    MarketCode: "0",
    commodity_idt: "TXO",
    commodity_id2t: "",
    commodity_id2t2: ""
  }).toString();

  const result = await fetchTAIFEXPost(
    "/cht/3/optDailyMarketReport",
    body
  );

  if (!result.response.ok) {
    return {
      found: false,
      reason: `TAIFEX option chain HTTP ${result.response.status}`,
      raw_rows: 0,
      rows: []
    };
  }

  const parsed = parseTXOOptionChain(result.rows);

  return {
    found: parsed.found,
    raw_rows: result.rows.length,
    rows: parsed.data
  };
}

function today() {
  return new Date().toISOString().slice(0, 10);
}

async function institutionalEndpoint(
  path,
  dataset,
  market,
  session,
  parser
) {

  try {

    let result =
      await fetchTAIFEX(path);

    if (!result.response.ok) {
      if (path === "/cht/3/optContractsDate") {
        const fb = await fetchOpenAPIInstitutionalOptions();
        if (fb.found) {
          result = {
            response: fallbackResponseFromRows(fb.rows),
            html: `<openapi-fallback>${JSON.stringify(fb.rows)}</openapi-fallback>`,
            rows: fb.rows,
            source: "taifex_openapi",
            fallback: true,
            source_url: "https://openapi.taifex.com.tw/v1/MarketDataOfMajorInstitutionalTradersDetailsOfOptionsContractsBytheDate"
          };
        }
      }
    }

    if (!result.response.ok) {

      return json({
        ok: false,
        source: "TAIFEX",
        status: result.response.status,
        error: "TAIFEX request failed"
      }, 502);
    }

    const parsed =
      parser(result.rows);

    return json({
      ok: true,
      source: "TAIFEX",
      dataset,
      market,
      session,
      date: today(),
      data: parsed.data,
      parser: {
        version: "4.1",
        found: parsed.found,
        row_count: result.rows.length
      }
    });

  } catch (error) {

    return json({
      ok: false,
      source: "TAIFEX",
      error: String(error)
    }, 500);
  }
}

/* =========================
   Worker
========================= */

/* =========================
   V1.4 module-level snapshot collector (used by scheduled + endpoints).
========================= */

async function collectSnapshotBundle(taipeiISO, taifexSlash) {
  const bundle = {
    version: "1.4",
    date: taipeiISO,
    collected_at: new Date().toISOString(),
    data: {}
  };

  try {
    const f = await fetchTAIFEXOpenAPI(
      "/OpenInterestOfLargeTradersFutures"
    );
    if (f.found) {
      bundle.data.top10fut = f.rows.filter(r =>
        r.Contract === "TX" &&
        String(r.TypeOfTraders) === "0"
      );
    }
    const o = await fetchTAIFEXOpenAPI(
      "/OpenInterestOfLargeTradersOptions"
    );
    if (o.found) {
      bundle.data.top10opt = o.rows.filter(r =>
        r.Contract === "TXO" &&
        String(r.TypeOfTraders) === "0"
      );
    }
  } catch (_) { /* keep partial bundle */ }

  try {
    const c = await fetchTXOChainForDate(taifexSlash);
    if (c.found) bundle.data.chain = c.rows;
  } catch (_) { /* keep partial bundle */ }

  const dayPaths = [
    ["fut_trade_day", "/cht/3/futContractsDate", parseFuturesInstitutional],
    ["fut_trade_night", "/cht/3/futContractsDateAh", parseFuturesInstitutional],
    ["opt_pos_day", "/cht/3/optContractsDate", parseOptionsInstitutional]
  ];
  for (const [key, path, parser] of dayPaths) {
    try {
      const r = await fetchTAIFEX(path);
      if (r.response.ok) {
        const parsed = parser(r.rows);
        if (parsed.found) bundle.data[key] = parsed.data;
      }
    } catch (_) { /* keep partial bundle */ }
  }

  try {
    if (bundle.data.chain) {
      const kl = calculateTXOKeyLevels(
        bundle.data.chain,
        taipeiISO
      );
      if (kl.found) {
        bundle.data.walls = {
          call_wall: kl.call_wall,
          put_wall: kl.put_wall,
          max_pain: kl.max_pain,
          primary_expiry: kl.primary_expiry
        };
      }
    }
  } catch (_) { /* keep partial bundle */ }

  return bundle;
}

function taipeiTodayISO(when = null) {
  const t = when ? new Date(when) : new Date();
  const tp = new Date(t.getTime() + 8 * 3600 * 1000);
  return tp.toISOString().slice(0, 10);
}

export default {

  /* V1.4 — daily snapshot cron (configure in wrangler.toml, e.g.
     "30 6 * * 1-5"). Requires KV binding SNAPSHOTS. */
  async scheduled(event, env, ctx) {
    try {
      const nowTaipei = new Date(Date.now() + 8 * 3600 * 1000);
      const wd = nowTaipei.getUTCDay();
      if (wd === 0 || wd === 6) return;
      const iso = nowTaipei.toISOString().slice(0, 10);
      const slash = iso.replace(/-/g, "/");
      const bundle = await collectSnapshotBundle(iso, slash);
      if (env && env.SNAPSHOTS) {
        ctx.waitUntil(
          env.SNAPSHOTS.put(`snapshot:${iso}`, JSON.stringify(bundle))
        );
      }
    } catch (e) {
      console.log("snapshot cron failed", e);
    }
  },

  async fetch(request, env) {

    const url = new URL(request.url);

    if (request.method !== "GET") {
      return json({
        ok: false,
        error: "GET only"
      }, 405);
    }

    /* HEALTH */

    if (url.pathname === "/health") {

      return json({
        ok: true,
        service: "taifex-proxy",
        taifex: true,
        version: "V1.4 — V1.3 + daily snapshots (KV) (additive)"
      });
    }

    /* TX 夜盤三大法人 */

    if (
      url.pathname ===
      "/futures-institutional-after-hours"
    ) {

      return institutionalEndpoint(
        "/cht/3/futContractsDateAh",
        "futures_institutional_after_hours",
        "TX",
        "after_hours",
        parseFuturesInstitutional
      );
    }

    /* TX 日盤三大法人 */

    if (
      url.pathname ===
      "/futures-institutional"
    ) {

      return institutionalEndpoint(
        "/cht/3/futContractsDate",
        "futures_institutional",
        "TX",
        "regular",
        parseFuturesInstitutional
      );
    }

    /* TX 行情 */

    if (
      url.pathname ===
      "/futures-price"
    ) {

      try {

        const result =
          await fetchTAIFEX(
            "/cht/3/futDailyMarketExcel?commodity_id=TX"
          );

        if (!result.response.ok) {

          return json({
            ok: false,
            source: "TAIFEX",
            status: result.response.status,
            error: "TAIFEX request failed"
          }, 502);
        }

        const data =
          parseTXMarket(result.rows);

        return json({
          ok: true,
          source: "TAIFEX",
          dataset: "futures_market",
          market: "TX",
          date: today(),
          data,
          parser: {
            version: "4.1",
            row_count: result.rows.length,
            contracts: data.length
          }
        });

      } catch (error) {

        return json({
          ok: false,
          source: "TAIFEX",
          error: String(error)
        }, 500);
      }
    }

    /* TX 夜盤行情 */

    if (
      url.pathname ===
      "/futures-price-after-hours"
    ) {

      try {

        const result =
          await fetchTAIFEX(
            "/cht/3/futDailyMarketExcel?commodity_id=TX"
          );

        if (!result.response.ok) {

          return json({
            ok: false,
            source: "TAIFEX",
            status: result.response.status,
            error: "TAIFEX request failed"
          }, 502);
        }

        const data =
          parseTXMarket(result.rows);

        return json({
          ok: true,
          source: "TAIFEX",
          dataset: "futures_market_after_hours",
          market: "TX",
          session: "after_hours",
          date: today(),

          data: data.map(x => ({
            contract_month:
              x.contract_month,
            after_hours_volume:
              x.after_hours_volume,
            settlement_price:
              x.settlement_price,
            open_interest:
              x.open_interest
          })),

          parser: {
            version: "4.1",
            row_count: result.rows.length,
            contracts: data.length
          }
        });

      } catch (error) {

        return json({
          ok: false,
          source: "TAIFEX",
          error: String(error)
        }, 500);
      }
    }

    /* TX 三大法人 OI（指定日期） */

    if (
      url.pathname ===
      "/futures-institutional-oi"
    ) {

      try {

        const requestedDate =
          url.searchParams.get("date");

        const taifexDate =
          normalizeQueryDate(requestedDate);

        if (!taifexDate) {

          return json({
            ok: false,
            error:
              "Invalid date. Use YYYY-MM-DD."
          }, 400);
        }

        const query =
          encodeURIComponent(taifexDate);

        const path =
          `/cht/3/futContractsDate?doQuery=1&queryType=1&queryDate=${query}`;

        const result =
          await fetchTAIFEX(path);

        if (!result.response.ok) {

          return json({
            ok: false,
            source: "TAIFEX",
            status: result.response.status,
            error: "TAIFEX request failed"
          }, 502);
        }

        const parsed =
          parseFuturesInstitutionalOI(
            result.rows
          );

        return json({
          ok: true,
          source: "TAIFEX",
          dataset: "futures_institutional_oi",
          market: "TX",
          session: "regular",
          date:
            queryDateToISO(taifexDate),
          data: parsed.data,
          parser: {
            version: "4.2",
            found: parsed.found,
            row_count: result.rows.length
          }
        });

      } catch (error) {

        return json({
          ok: false,
          source: "TAIFEX",
          error: String(error)
        }, 500);
      }
    }

    /* TX 三大法人 OI History：T0～T-5 */

    if (
      url.pathname ===
      "/futures-institutional-oi-history"
    ) {

      try {

        const requestedDate =
          url.searchParams.get("date");

        const taifexStartDate =
          normalizeQueryDate(requestedDate);

        if (!taifexStartDate) {

          return json({
            ok: false,
            error:
              "Invalid date. Use YYYY-MM-DD."
          }, 400);
        }

        const startISO =
          queryDateToISO(taifexStartDate);

        const history = [];
        let cursor = new Date(
          `${startISO}T00:00:00Z`
        );

        /*
         * Search backwards by calendar day and retain
         * only dates for which TAIFEX returns complete
         * TX institutional OI data.
         *
         * Safety limit: 30 calendar days, enough to
         * cover weekends and ordinary market holidays.
         */
        for (
          let attempt = 0;
          attempt < 30 && history.length < 6;
          attempt++
        ) {

          const yyyy =
            cursor.getUTCFullYear();

          const mm =
            String(
              cursor.getUTCMonth() + 1
            ).padStart(2, "0");

          const dd =
            String(
              cursor.getUTCDate()
            ).padStart(2, "0");

          const isoDate =
            `${yyyy}-${mm}-${dd}`;

          const taifexDate =
            `${yyyy}/${mm}/${dd}`;

          const query =
            encodeURIComponent(taifexDate);

          const path =
            `/cht/3/futContractsDate?doQuery=1&queryType=1&queryDate=${query}`;

          try {

            const result =
              await fetchTAIFEX(path);

            if (result.response.ok) {

              const parsed =
                parseFuturesInstitutionalOI(
                  result.rows
                );

              if (parsed.found) {

                history.push({
                  label:
                    history.length === 0
                      ? "T0"
                      : `T-${history.length}`,
                  date: isoDate,
                  data: parsed.data
                });
              }
            }

          } catch (_) {
            /* Skip an invalid/non-trading date. */
          }

          cursor.setUTCDate(
            cursor.getUTCDate() - 1
          );
        }

        return json({
          ok:
            history.length === 6,
          source: "TAIFEX",
          dataset:
            "futures_institutional_oi_history",
          market: "TX",
          session: "regular",
          requested_date: startISO,
          count: history.length,
          data: history,
          parser: {
            version: "4.3",
            found:
              history.length === 6,
            trading_days_found:
              history.length,
            search_limit_days: 30
          }
        }, history.length === 6 ? 200 : 502);

      } catch (error) {

        return json({
          ok: false,
          source: "TAIFEX",
          error: String(error)
        }, 500);
      }
    }

    /* TXO 完整 Option Chain */

    if (
      url.pathname ===
      "/futures-options-chain"
    ) {

      try {

        const requestedDate =
          url.searchParams.get("date");

        const taifexDate =
          normalizeQueryDate(requestedDate);

        if (!taifexDate) {

          return json({
            ok: false,
            error:
              "Invalid date. Use YYYY-MM-DD."
          }, 400);
        }

        const queryDate =
          taifexDate;

        const body =
          new URLSearchParams({
            queryType: "2",
            marketCode: "0",
            dateaddcnt: "",
            commodity_id: "TXO",
            commodity_id2: "",
            queryDate,
            MarketCode: "0",
            commodity_idt: "TXO",
            commodity_id2t: "",
            commodity_id2t2: ""
          }).toString();

        const result =
          await fetchTAIFEXPost(
            "/cht/3/optDailyMarketReport",
            body
          );

        if (!result.response.ok) {

          return json({
            ok: false,
            source: "TAIFEX",
            status:
              result.response.status,
            error:
              "TAIFEX request failed"
          }, 502);
        }

        const parsed =
          parseTXOOptionChain(
            result.rows
          );

        const data =
          parsed.data;

        const callCount =
          data.filter(
            x => x.type === "call"
          ).length;

        const putCount =
          data.filter(
            x => x.type === "put"
          ).length;

        return json({

          ok:
            parsed.found,

          source: "TAIFEX",

          dataset:
            "options_chain",

          market: "TXO",

          session: "regular",

          date:
            queryDateToISO(taifexDate),

          data,

          parser: {

            version: "V1.0 — Production",

            found:
              parsed.found,

            row_count:
              result.rows.length,

            contracts:
              data.length,

            call_count:
              callCount,

            put_count:
              putCount
          }

        }, parsed.found ? 200 : 502);

      } catch (error) {

        return json({
          ok: false,
          source: "TAIFEX",
          error: String(error)
        }, 500);
      }
    }

    /* TXO Daily Delta */

    if (
      url.pathname ===
      "/options-delta"
    ) {

      try {

        const requestedDate =
          url.searchParams.get("date") ||
          today();

        const taifexDate =
          normalizeQueryDate(requestedDate);

        if (!taifexDate) {

          return json({
            ok: false,
            error:
              "Invalid date. Use YYYY-MM-DD."
          }, 400);
        }

        const queryDate =
          queryDateToISO(taifexDate);

        const result =
          await fetchTXODeltaForDate(
            queryDate
          );

        return json({

          ok:
            result.found,

          source: "TAIFEX",

          dataset:
            "options_daily_delta",

          market: "TXO",

          date:
            queryDate,

          data:
            result.rows,

          parser: {

            version: "V1.0 — Production",

            found:
              result.found,

            raw_rows:
              result.raw_rows,

            delta_rows:
              result.rows.length,

            source_url:
              result.source_url ||
              null
          }

        }, result.found ? 200 : 502);

      } catch (error) {

        return json({
          ok: false,
          source: "TAIFEX",
          error: String(error)
        }, 500);
      }
    }

    /* V1.0 — Production Compact TXO Market Structure
       Production endpoint: compact analysis only. */

    if (
      url.pathname ===
      "/options-market-structure-compact"
    ) {

      try {

        const requestedDate =
          url.searchParams.get("date") ||
          today();

        const taifexDate =
          normalizeQueryDate(requestedDate);

        if (!taifexDate) {
          return json({
            ok: false,
            error: "Invalid date. Use YYYY-MM-DD."
          }, 400);
        }

        const queryDate =
          queryDateToISO(taifexDate);

        /* -------------------------
           1. Fetch TXO Chain
        ------------------------- */

        const chainResult =
          await fetchTXOChainForDate(taifexDate);

        if (!chainResult.found) {
          return json({
            ok: false,
            source: "TAIFEX",
            dataset: "options_market_structure",
            market: "TXO",
            date: queryDate,
            error:
              chainResult.reason ||
              "TXO chain not found"
          }, 502);
        }

        /* -------------------------
           2. Fetch TXO Delta
        ------------------------- */

        const deltaResult =
          await fetchTXODeltaForDate(queryDate);

        const taiexResult =
          await fetchTAIEXCloseForDate(queryDate);

        const chainExpiries =
          uniqueExpiries(
            chainResult.rows,
            queryDate
          );

        /*
         * Primary expiry is the first still-valid expiry in
         * the Chain. Key levels are calculated only from this
         * expiry.
         */
        const primaryExpiry =
          chainExpiries[0] || null;

        const keyLevels =
          primaryExpiry
            ? calculateKeyLevelsForExpiry(
                chainResult.rows,
                primaryExpiry
              )
            : {
                found: false,
                reason: "No valid TXO expiry in chain"
              };

        /* -------------------------
           3. Find common Gamma expiry
        ------------------------- */

        let gammaExpiry = null;

        let gamma = {
          status: "unavailable",
          reason:
            deltaResult.found
              ? "No common Chain/Delta expiry"
              : (
                  deltaResult.reason ||
                  "TAIFEX Delta unavailable"
                )
        };

        if (deltaResult.found) {

          gammaExpiry =
            findCommonExpiry(
              chainResult.rows,
              deltaResult.rows,
              queryDate
            );

          if (gammaExpiry) {

            const gammaRaw =
              taiexResult.found
                ? buildGammaForCommonExpiry(
                    chainResult.rows,
                    deltaResult.rows,
                    gammaExpiry,
                    taiexResult.close,
                    queryDate
                  )
                : {
                    found: false,
                    reason:
                      taiexResult.reason ||
                      "TAIEX underlying price unavailable",
                    chain_rows:
                      filterExpiry(
                        chainResult.rows,
                        gammaExpiry,
                        false
                      ).length,
                    delta_rows:
                      filterExpiry(
                        deltaResult.rows,
                        gammaExpiry,
                        true
                      ).length,
                    matched_strikes:
                      0
                  };

            if (
              gammaRaw.found &&
              gammaRaw.matched_strikes > 0
            ) {

              gamma = {

                status: "usable",

                gamma_wall:
                  gammaRaw.gamma_wall || null,

                gamma_flip:
                  gammaRaw.gamma_flip || null,

                net_gex_1pct:
                  gammaRaw.net_gex_1pct ??
                  null,

                gross_gex_1pct:
                  gammaRaw.gross_gex_1pct ??
                  null,

                underlying_price:
                  gammaRaw.underlying_price ??
                  taiexResult.close ??
                  null,

                model:
                  gammaRaw.model ??
                  null,

                dealer_sign_convention:
                  gammaRaw.dealer_sign_convention ??
                  null,

                chain_rows:
                  gammaRaw.chain_rows,

                delta_rows:
                  gammaRaw.delta_rows,

                matched_strikes:
                  gammaRaw.matched_strikes,

                gamma_diagnostics:
                  gammaRaw.gamma_diagnostics ||
                  null
              };

            } else {

              gamma = {
                status: "unavailable",
                reason:
                  gammaRaw.reason ||
                  "Insufficient Chain/Delta overlap",
                chain_rows:
                  gammaRaw.chain_rows || 0,
                delta_rows:
                  gammaRaw.delta_rows || 0,
                matched_strikes:
                  gammaRaw.matched_strikes || 0,

                gamma_diagnostics:
                  gammaRaw.gamma_diagnostics ||
                  null
              };
            }
          }
        }

        /* -------------------------
           4. Gamma-specific quality
        ------------------------- */

        let gammaChainRows = 0;
        let gammaDeltaRows = 0;
        let matchedStrikeKeys = 0;
        let unmatchedStrikeKeys = 0;

        if (gammaExpiry) {

          const c =
            filterExpiry(
              chainResult.rows,
              gammaExpiry,
              false
            );

          const d =
            filterExpiry(
              deltaResult.rows,
              gammaExpiry,
              true
            );

          gammaChainRows = c.length;
          gammaDeltaRows = d.length;

          const chainKeys =
            new Set(
              c.map(r =>
                `${r.strike}|${r.type}`
              )
            );

          const deltaKeys =
            new Set(
              d.map(r =>
                `${r.strike}|${r.type}`
              )
            );

          for (const key of chainKeys) {
            if (deltaKeys.has(key)) {
              matchedStrikeKeys++;
            } else {
              unmatchedStrikeKeys++;
            }
          }
        }

        const overallStatus =
          keyLevels.found
            ? (
                gamma.status === "usable"
                  ? "usable"
                  : "partial"
              )
            : "unavailable";

        return json({

          ok:
            keyLevels.found,

          source: "TAIFEX",

          dataset:
            "options_market_structure",

          market: "TXO",

          session: "regular",

          date: queryDate,

          data: {

            primary_expiry:
              primaryExpiry,

            call_wall:
              keyLevels.call_wall || null,

            put_wall:
              keyLevels.put_wall || null,

            max_pain:
              keyLevels.max_pain || null,

            gamma: {

              expiry:
                gammaExpiry,

              status:
                gamma.status,

              gamma_wall_proxy:
                gamma.gamma_wall?.strike ??
                null,

              gamma_flip_proxy:
                gamma.gamma_flip?.estimated_underlying ??
                null,

              net_gex_proxy:
                gamma.net_gex_1pct ??
                null
            },

            data_quality: {

              status:
                overallStatus,

              chain_rows:
                chainResult.rows.length,

              delta_rows:
                deltaResult.rows.length,

              gamma_chain_rows:
                gammaChainRows,

              gamma_delta_rows:
                gammaDeltaRows,

              matched_strike_keys:
                matchedStrikeKeys,

              unmatched_strike_keys:
                unmatchedStrikeKeys,

              gamma_contracts_modeled:
                gamma.gamma_diagnostics?.modeled_contracts ??
                0,

              gamma_diagnostics:
                gamma.gamma_diagnostics ||
                null,

              underlying_price:
                gamma.underlying_price ??
                taiexResult.close ??
                null,

              primary_expiry:
                primaryExpiry,

              gamma_expiry:
                gammaExpiry
            }
          },

          parser: {

            version:
              "V1.0 — Production",

            engine:
              "Unified TXO Chain + TAIFEX Delta + Settlement-Implied-Volatility Black-Scholes GEX",

            raw_arrays:
              false,

            fail_safe:
              true
          }

        }, keyLevels.found ? 200 : 502);

      } catch (error) {

        return json({

          ok: false,

          source: "TAIFEX",

          dataset:
            "options_market_structure",

          error:
            String(error)

        }, 500);
      }
    }

    /* V1.0 — Production Unified TXO Market Structure */

    if (
      url.pathname ===
      "/options-market-structure"
    ) {

      try {

        const requestedDate =
          url.searchParams.get("date") ||
          today();

        const taifexDate =
          normalizeQueryDate(requestedDate);

        if (!taifexDate) {
          return json({
            ok: false,
            error: "Invalid date. Use YYYY-MM-DD."
          }, 400);
        }

        const queryDate =
          queryDateToISO(taifexDate);

        const chainResult =
          await fetchTXOChainForDate(
            taifexDate
          );

        if (!chainResult.found) {
          return json({
            ok: false,
            source: "TAIFEX",
            dataset: "options_market_structure",
            market: "TXO",
            date: queryDate,
            error: chainResult.reason || "TXO chain not found"
          }, 502);
        }

        const deltaResult =
          await fetchTXODeltaForDate(
            queryDate
          );

        const taiexResult =
          await fetchTAIEXCloseForDate(
            queryDate
          );

        /*
         * Chain key levels use the nearest still-valid chain expiry.
         * Gamma deliberately uses the nearest expiry shared by both
         * Chain and Delta. This prevents an expired weekly chain from
         * being incorrectly paired with the next available Delta file.
         */
        const chainExpiries =
          uniqueExpiries(
            chainResult.rows,
            queryDate
          );

        const primaryChainExpiry =
          chainExpiries[0] || null;

        const keyLevels =
          primaryChainExpiry
            ? calculateKeyLevelsForExpiry(
                chainResult.rows,
                primaryChainExpiry
              )
            : {
                found: false,
                reason: "No valid TXO chain expiry"
              };

        let gamma = {
          found: false,
          reason: deltaResult.found
            ? "No common Chain/Delta expiry"
            : (deltaResult.reason || "TAIFEX Delta not found")
        };

        let commonExpiry = null;

        if (deltaResult.found) {
          commonExpiry =
            findCommonExpiry(
              chainResult.rows,
              deltaResult.rows,
              queryDate
            );

          if (commonExpiry) {
            gamma =
              taiexResult.found
                ? buildGammaForCommonExpiry(
                    chainResult.rows,
                    deltaResult.rows,
                    commonExpiry,
                    taiexResult.close,
                    queryDate
                  )
                : {
                    found: false,
                    reason:
                      taiexResult.reason ||
                      "TAIEX underlying price unavailable",
                    chain_rows:
                      filterExpiry(
                        chainResult.rows,
                        commonExpiry,
                        false
                      ).length,
                    delta_rows:
                      filterExpiry(
                        deltaResult.rows,
                        commonExpiry,
                        true
                      ).length,
                    matched_strikes:
                      0
                  };
          }
        }

        const quality =
          buildDataQuality(
            chainResult.rows,
            deltaResult.rows,
            queryDate,
            commonExpiry
          );

        return json({

          ok:
            keyLevels.found,

          source: "TAIFEX",

          dataset:
            "options_market_structure",

          market: "TXO",

          session: "regular",

          date:
            queryDate,

          data: {

            primary_chain_expiry:
              primaryChainExpiry,

            key_levels:
              keyLevels,

            gamma_expiry:
              commonExpiry,

            gamma:
              gamma.found
                ? {
                    status:
                      (gamma.option_contracts_modeled ?? 0) > 0
                        ? "usable"
                        : "unavailable",
                    reason:
                      (gamma.option_contracts_modeled ?? 0) > 0
                        ? null
                        : (
                            gamma.reason ||
                            "No valid option IV/Gamma could be modeled from settlement prices"
                          ),
                    gamma_wall:
                      gamma.gamma_wall || null,
                    gamma_flip:
                      gamma.gamma_flip || null,
                    net_gex_1pct:
                      gamma.net_gex_1pct ?? null,
                    gross_gex_1pct:
                      gamma.gross_gex_1pct ?? null,
                    underlying_price:
                      gamma.underlying_price ??
                      taiexResult.close ??
                      null,
                    model:
                      gamma.model ?? null,
                    dealer_sign_convention:
                      gamma.dealer_sign_convention ??
                      null,
                    chain_rows:
                      gamma.chain_rows ?? 0,
                    delta_rows:
                      gamma.delta_rows ?? 0,
                    matched_strikes:
                      gamma.matched_strikes ?? 0,
                    option_contracts_modeled:
                      gamma.option_contracts_modeled ?? 0,
                    gamma_diagnostics:
                      gamma.gamma_diagnostics || null
                  }
                : {
                    status: "unavailable",
                    reason:
                      gamma.reason ||
                      "Gamma unavailable",
                    chain_rows:
                      gamma.chain_rows ?? 0,
                    delta_rows:
                      gamma.delta_rows ?? 0,
                    matched_strikes:
                      gamma.matched_strikes ?? 0,
                    option_contracts_modeled:
                      gamma.option_contracts_modeled ?? 0,
                    gamma_diagnostics:
                      gamma.gamma_diagnostics || null
                  },

            data_quality:
              {
                ...quality,
                underlying_price:
                  taiexResult.found
                    ? taiexResult.close
                    : null,
                taiex_status:
                  taiexResult.found
                    ? "usable"
                    : "unavailable"
              }
          },

          parser: {

            version: "V1.0 — Production",

            chain_raw_rows:
              chainResult.raw_rows,

            chain_contracts:
              chainResult.rows.length,

            delta_found:
              deltaResult.found,

            delta_rows:
              deltaResult.rows.length,

            engine:
              "Unified TXO Chain + TAIFEX Delta + Settlement-Implied-Volatility Black-Scholes GEX"
          }

        }, keyLevels.found ? 200 : 502);

      } catch (error) {

        return json({
          ok: false,
          source: "TAIFEX",
          dataset: "options_market_structure",
          error: String(error)
        }, 500);
      }
    }

    /* TXO Gamma Wall / Gamma Flip */

    if (
      url.pathname ===
      "/options-gamma-levels"
    ) {

      try {

        const requestedDate =
          url.searchParams.get("date") ||
          today();

        const taifexDate =
          normalizeQueryDate(requestedDate);

        if (!taifexDate) {

          return json({
            ok: false,
            error:
              "Invalid date. Use YYYY-MM-DD."
          }, 400);
        }

        const queryDate =
          queryDateToISO(taifexDate);

        const chainBody =
          new URLSearchParams({
            queryType: "2",
            marketCode: "0",
            dateaddcnt: "",
            commodity_id: "TXO",
            commodity_id2: "",
            queryDate: taifexDate,
            MarketCode: "0",
            commodity_idt: "TXO",
            commodity_id2t: "",
            commodity_id2t2: ""
          }).toString();

        const chainResult =
          await fetchTAIFEXPost(
            "/cht/3/optDailyMarketReport",
            chainBody
          );

        if (!chainResult.response.ok) {

          return json({
            ok: false,
            source: "TAIFEX",
            status:
              chainResult.response.status,
            error:
              "TAIFEX option chain request failed"
          }, 502);
        }

        const parsedChain =
          parseTXOOptionChain(
            chainResult.rows
          );

        if (!parsedChain.found) {

          return json({
            ok: false,
            source: "TAIFEX",
            dataset:
              "options_gamma_levels",
            market: "TXO",
            date: queryDate,
            error:
              "TXO option chain not found"
          }, 502);
        }

        const deltaResult =
          await fetchTXODeltaForDate(
            queryDate
          );

        if (!deltaResult.found) {

          return json({
            ok: false,
            source: "TAIFEX",
            dataset:
              "options_gamma_levels",
            market: "TXO",
            date: queryDate,
            error:
              "TAIFEX Daily Delta not found",
            detail:
              deltaResult.reason ||
              null
          }, 502);
        }

        const taiexResult =
          await fetchTAIEXCloseForDate(
            queryDate
          );

        const gammaExpiry =
          findCommonExpiry(
            parsedChain.data,
            deltaResult.rows,
            queryDate
          );

        const gamma =
          gammaExpiry && taiexResult.found
            ? buildGammaForCommonExpiry(
                parsedChain.data,
                deltaResult.rows,
                gammaExpiry,
                taiexResult.close,
                queryDate
              )
            : {
                found: false,
                reason:
                  !gammaExpiry
                    ? "No common Chain/Delta expiry"
                    : (
                        taiexResult.reason ||
                        "TAIEX underlying price unavailable"
                      )
              };

        return json({

          ok:
            gamma.found,

          source: "TAIFEX",

          dataset:
            "options_gamma_levels",

          market: "TXO",

          session: "regular",

          date:
            queryDate,

          data:
            gamma,

          parser: {

            version: "V1.0 — Production",

            chain_contracts:
              parsedChain.data.length,

            delta_rows:
              deltaResult.rows.length,

            calculation:
              "Unified Chain + Delta + TAIEX Spot + Settlement-Implied-Volatility Black-Scholes GEX"
          }

        }, gamma.found ? 200 : 502);

      } catch (error) {

        return json({
          ok: false,
          source: "TAIFEX",
          error: String(error)
        }, 500);
      }
    }

    /* TXO Call Wall / Put Wall / Max Pain */

    if (
      url.pathname ===
      "/options-key-levels"
    ) {

      try {

        const requestedDate =
          url.searchParams.get("date");

        const taifexDate =
          normalizeQueryDate(requestedDate);

        if (!taifexDate) {

          return json({
            ok: false,
            error:
              "Invalid date. Use YYYY-MM-DD."
          }, 400);
        }

        const queryDate =
          queryDateToISO(taifexDate);

        const body =
          new URLSearchParams({
            queryType: "2",
            marketCode: "0",
            dateaddcnt: "",
            commodity_id: "TXO",
            commodity_id2: "",
            queryDate: taifexDate,
            MarketCode: "0",
            commodity_idt: "TXO",
            commodity_id2t: "",
            commodity_id2t2: ""
          }).toString();

        const result =
          await fetchTAIFEXPost(
            "/cht/3/optDailyMarketReport",
            body
          );

        if (!result.response.ok) {

          return json({
            ok: false,
            source: "TAIFEX",
            status:
              result.response.status,
            error:
              "TAIFEX request failed"
          }, 502);
        }

        const parsed =
          parseTXOOptionChain(
            result.rows
          );

        if (!parsed.found) {

          return json({
            ok: false,
            source: "TAIFEX",
            dataset:
              "options_key_levels",
            market: "TXO",
            date: queryDate,
            error:
              "TXO option chain not found"
          }, 502);
        }

        const levels =
          calculateTXOKeyLevels(
            parsed.data,
            queryDate
          );

        return json({

          ok:
            levels.found,

          source: "TAIFEX",

          dataset:
            "options_key_levels",

          market: "TXO",

          session: "regular",

          date:
            queryDate,

          data:
            levels,

          parser: {

            version: "V1.0 — Production",

            chain_rows:
              result.rows.length,

            chain_contracts:
              parsed.data.length,

            calculation:
              "OI-based Call Wall / Put Wall / intrinsic-value Max Pain"
          }

        }, levels.found ? 200 : 502);

      } catch (error) {

        return json({
          ok: false,
          source: "TAIFEX",
          error: String(error)
        }, 500);
      }
    }

    /* TXO 日盤法人 */

    if (
      url.pathname ===
      "/options-institutional"
    ) {

      return institutionalEndpoint(
        "/cht/3/optContractsDate",
        "options_institutional",
        "TXO",
        "regular",
        parseOptionsInstitutional
      );
    }

    /* TXO 夜盤法人 */

    if (
      url.pathname ===
      "/options-institutional-after-hours"
    ) {

      return institutionalEndpoint(
        "/cht/3/optContractsDateAh",
        "options_institutional_after_hours",
        "TXO",
        "after_hours",
        parseOptionsInstitutional
      );
    }

    /* =========================
       TXO 夜盤 Call / Put
    ========================= */

    if (
      url.pathname ===
      "/options-after-hours"
    ) {

      try {

        const result =
          await fetchTAIFEX(
            "/cht/3/callsAndPutsDateAh"
          );

        if (!result.response.ok) {

          return json({
            ok: false,
            source: "TAIFEX",
            status: result.response.status,
            error: "TAIFEX request failed"
          }, 502);
        }

        const rows = result.rows;

        const call = [];
        const put = [];

        let currentType = null;

        for (const row of rows) {

          /*
           * 注意：
           * 「賣權」與「自營商」可能
           * 出現在同一列。
           *
           * 因此不能在偵測權別後 continue。
           */

          if (row.includes("買權")) {
            currentType = "call";
          }

          if (row.includes("賣權")) {
            currentType = "put";
          }

          const idx = row.findIndex(x =>
            x === "自營商" ||
            x === "投信" ||
            x === "外資"
          );

          if (idx < 0 || !currentType) {
            continue;
          }

          const institution =
            institutionCode(row[idx]);

          if (!institution) {
            continue;
          }

          const v =
            row.slice(idx + 1);

          /*
           * v:
           * [買方口數,
           *  買方契約金額,
           *  賣方口數,
           *  賣方契約金額,
           *  買賣差額口數,
           *  買賣差額金額]
           */

          const item = {

            institution,

            long_volume:
              number(v[0]),

            long_amount:
              number(v[1]),

            short_volume:
              number(v[2]),

            short_amount:
              number(v[3]),

            net_volume:
              number(v[4]),

            net_amount:
              number(v[5])
          };

          if (currentType === "call") {
            call.push(item);
          }

          if (currentType === "put") {
            put.push(item);
          }
        }

        const found =
          call.length === 3 &&
          put.length === 3;

        return json({

          ok: true,

          source: "TAIFEX",

          dataset:
            "options_calls_puts_after_hours",

          market: "TXO",

          session: "after_hours",

          date: today(),

          data: {
            call,
            put
          },

          parser: {
            version: "4.1",
            found,
            call_count: call.length,
            put_count: put.length,
            row_count: rows.length
          }

        });

      } catch (error) {

        return json({
          ok: false,
          source: "TAIFEX",
          error: String(error)
        }, 500);
      }
    }

    /* 診斷 */

    if (
      url.pathname ===
      "/debug-taifex"
    ) {

      try {

        const result =
          await fetchTAIFEX(
            "/cht/3/futContractsDateAh"
          );

        return json({

          ok: true,

          source: "TAIFEX",

          http_status:
            result.response.status,

          html_length:
            result.html.length,

          row_count:
            result.rows.length,

          rows:
            result.rows.map(
              (row, index) => ({
                index,
                cells: row
              })
            )

        });

      } catch (error) {

        return json({
          ok: false,
          error: String(error)
        }, 500);
      }
    }

    /* =========================
       V1.2 ADDITIVE — Top10 Large-Traders OI (TAIFEX OpenAPI passthrough)
       Proxy primary per project policy; OpenAPI is upstream here.
       Official data lags ~1 trading day; actual date always returned.
    ========================= */

    function pickTop10Row(rows, requestedMonth) {
      const usable = rows.filter(r =>
        r && r.SettlementMonth !== "999912" && r.SettlementMonth !== "666666"
      );
      if (!usable.length) return { row: null, date: null, month: null };
      const dates = [...new Set(usable.map(r =>
        apiDateISO(r.Date || r.date)
      ).filter(Boolean))].sort();
      const latest = dates[dates.length - 1];
      const day = usable.filter(r =>
        apiDateISO(r.Date || r.date) === latest
      );
      const months = [...new Set(day.map(r =>
        String(r.SettlementMonth || "")
      ))].filter(Boolean).sort();
      const month = months.includes(requestedMonth)
        ? requestedMonth
        : months[months.length - 1];
      return {
        row: day.find(r =>
          String(r.SettlementMonth) === month
        ) || null,
        date: latest,
        month
      };
    }

    if (url.pathname === "/futures-top10") {
      try {
        const requestedDate = url.searchParams.get("date");
        const requestedMonth = url.searchParams.get("month");
        const api = await fetchTAIFEXOpenAPI(
          "/OpenInterestOfLargeTradersFutures"
        );
        if (!api.found) {
          return json({
            ok: false,
            source: "TAIFEX",
            dataset: "futures_top10",
            market: "TX",
            error: api.reason || "TAIFEX OpenAPI unavailable",
            source_url: api.source_url
          }, 502);
        }
        const tx = api.rows.filter(r =>
          r.Contract === "TX" && String(r.TypeOfTraders) === "0"
        );
        const picked = pickTop10Row(tx, requestedMonth);
        if (!picked.row) {
          return json({
            ok: false,
            source: "TAIFEX",
            dataset: "futures_top10",
            market: "TX",
            error: "No TX Top10 row"
          }, 502);
        }
        const buy = nullableNumber(picked.row.Top10Buy);
        const sell = nullableNumber(picked.row.Top10Sell);
        return json({
          ok: true,
          source: "TAIFEX",
          dataset: "futures_top10",
          market: "TX",
          date: picked.date,
          requested_date: requestedDate,
          data: {
            buy,
            sell,
            net: buy !== null && sell !== null ? buy - sell : null,
            month: picked.month,
            trader_type: "0"
          },
          parser: { version: "1.2", endpoint: "futures-top10" }
        });
      } catch (error) {
        return json({
          ok: false,
          source: "TAIFEX",
          error: String(error)
        }, 500);
      }
    }

    if (url.pathname === "/options-top10") {
      try {
        const requestedDate = url.searchParams.get("date");
        const requestedMonth = url.searchParams.get("month");
        const typeParam =
          String(url.searchParams.get("type") || "call").toLowerCase();
        const want = typeParam.startsWith("put") ? "賣權" : "買權";
        const api = await fetchTAIFEXOpenAPI(
          "/OpenInterestOfLargeTradersOptions"
        );
        if (!api.found) {
          return json({
            ok: false,
            source: "TAIFEX",
            dataset: "options_top10",
            market: "TXO",
            error: api.reason || "TAIFEX OpenAPI unavailable",
            source_url: api.source_url
          }, 502);
        }
        const txo = api.rows.filter(r =>
          r.Contract === "TXO" &&
          r.CallPut === want &&
          String(r.TypeOfTraders) === "0"
        );
        const picked = pickTop10Row(txo, requestedMonth);
        if (!picked.row) {
          return json({
            ok: false,
            source: "TAIFEX",
            dataset: "options_top10",
            market: "TXO",
            error: "No TXO Top10 row"
          }, 502);
        }
        const buy = nullableNumber(picked.row.Top10Buy);
        const sell = nullableNumber(picked.row.Top10Sell);
        return json({
          ok: true,
          source: "TAIFEX",
          dataset: "options_top10",
          market: "TXO",
          date: picked.date,
          requested_date: requestedDate,
          data: {
            buy,
            sell,
            net: buy !== null && sell !== null ? buy - sell : null,
            month: picked.month,
            call_put: want,
            trader_type: "0"
          },
          parser: { version: "1.2", endpoint: "options-top10" }
        });
      } catch (error) {
        return json({
          ok: false,
          source: "TAIFEX",
          error: String(error)
        }, 500);
      }
    }

    /* =========================
       V1.3 ADDITIVE — Night OHLC + P/C history (TAIFEX OpenAPI passthrough)
       Proxy primary per project policy. Official data lags ~1 trading day;
       actual date always returned. Existing endpoints untouched.
    ========================= */

    if (url.pathname === "/futures-night-ohlc") {
      try {
        const requestedDate = url.searchParams.get("date");
        const requestedMonth = url.searchParams.get("month");

        /* ── 1️⃣ Primary: TAIFEX website. queryDate= page date (site ignores `date=`).
           marketCode=1 → 其他交易時段 (夜盤). Client passes T0+1 for 全日, T0 for 日盤.
           GET first; if page returns no TX rows (no session cookie), retry via POST form. ── */
        let found = false;
        let target = requestedDate;
        let row = null;
        let months = [];

        const parseTx = (html) => {
          const rows = parseRows(html);
          const txRows = rows.filter(r => r[0] === "TX" && r[1] && /^\d{6}$/.test(r[1]));
          months = [...new Set(txRows.map(r => r[1]))].sort();
          const m = months.includes(requestedMonth) ? requestedMonth : months[months.length - 1];
          return txRows.find(r => r[1] === m) || null;
        };

        if (requestedDate) {
          const pageUrl = `${TAIFEX}/cht/3/futDailyMarketReport`;
          const qs = `queryDate=${requestedDate.replace(/-/g, "/")}&marketCode=1&MarketCode=1&commodity_id=TX`;
          const baseHeaders = {
            "User-Agent": "Mozilla/5.0 (compatible; TAIFEX-Proxy/V1.4)",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            "Accept-Language": "zh-TW,zh;q=0.9,en;q=0.8",
            "Referer": `${pageUrl}`
          };
          try {
            let resp = await fetch(`${pageUrl}?${qs}`, { headers: baseHeaders });
            if (resp.ok) {
              row = parseTx(await resp.text());
            }
            if (!row) {
              // Cookie-less GET sometimes returns default page — retry as POST form
              resp = await fetch(pageUrl, {
                method: "POST",
                headers: {
                  ...baseHeaders,
                  "Content-Type": "application/x-www-form-urlencoded"
                },
                body: qs
              });
              if (resp.ok) row = parseTx(await resp.text());
            }
            if (row) {
              found = true;
              target = requestedDate;
            }
          } catch (_) { /* fall through to OpenAPI */ }
        }

        /* ── 2️⃣ Fallback: OpenAPI (stale but better than nothing) ── */
        if (!found) {
          const api = await fetchTAIFEXOpenAPI("/DailyMarketReportFut");
          if (api.found) {
            const night = api.rows.filter(r =>
              r.Contract === "TX" && String(r.TradingSession) === "盤後"
            );
            if (night.length) {
              const dates = [...new Set(night.map(r => apiDateISO(r.Date)).filter(Boolean))].sort();
              target = (requestedDate && dates.includes(requestedDate))
                ? requestedDate : dates[dates.length - 1];
              const day = night.filter(r => apiDateISO(r.Date) === target);
              months = [...new Set(day.map(r => String(r["ContractMonth(Week)"] || "")))].filter(Boolean).sort();
              const m = months.includes(requestedMonth) ? requestedMonth : months[months.length - 1];
              row = day.find(r => String(r["ContractMonth(Week)"]) === m);
              if (row) {
                found = true;
                // remap OpenAPI fields to website column order
                row = {
                  0: "TX", 1: m,
                  2: String(row.Open ?? ""), 3: String(row.High ?? ""),
                  4: String(row.Low ?? ""), 5: String(row.Last ?? ""),
                  6: String(row.Change ?? ""), 7: String(row["%"] ?? ""),
                  8: String(row.Volume ?? ""), 9: String(row.SettlementPrice ?? ""),
                  10: String(row.OpenInterest ?? ""),
                  11: String(row.BestBid ?? ""), 12: String(row.BestAsk ?? ""),
                  13: String(row.HistoricalHigh ?? ""), 14: String(row.HistoricalLow ?? "")
                };
              }
            }
          }
        }

        if (!found || !row) {
          return json({
            ok: false, source: "TAIFEX", dataset: "futures_night_ohlc",
            market: "TX", error: "No TX after-hours row"
          }, 502);
        }

        return json({
          ok: true, source: "TAIFEX", dataset: "futures_night_ohlc",
          market: "TX", session: "after_hours",
          date: target, requested_date: requestedDate,
          data: {
            open: nullableNumber(row[2]), high: nullableNumber(row[3]),
            low: nullableNumber(row[4]), close: nullableNumber(row[5]),
            change: nullableNumber(String(row[6] || "").replace(/[▲▼]/g, "")),
            change_percent: nullableNumber(String(row[7] || "").replace(/[▲▼]/g, "")),
            volume: nullableNumber(row[8]),
            settlement_price: nullableNumber(row[9]),
            month: months.includes(requestedMonth) ? requestedMonth : months[months.length - 1]
          },
          parser: { version: "1.4", endpoint: "futures-night-ohlc" }
        });
      } catch (error) {
        return json({
          ok: false,
          source: "TAIFEX",
          error: String(error)
        }, 500);
      }
    }

    if (url.pathname === "/put-call-ratio-history") {
      try {
        const api = await fetchTAIFEXOpenAPI("/PutCallRatio");
        if (!api.found) {
          return json({
            ok: false,
            source: "TAIFEX",
            dataset: "put_call_ratio_history",
            market: "TXO",
            error: api.reason || "TAIFEX OpenAPI unavailable",
            source_url: api.source_url
          }, 502);
        }
        const rows = api.rows.map(r => ({
          date: apiDateISO(r.Date),
          put_volume: nullableNumber(r.PutVolume),
          call_volume: nullableNumber(r.CallVolume),
          volume_ratio: nullableNumber(r["PutCallVolumeRatio%"]),
          put_oi: nullableNumber(r.PutOI),
          call_oi: nullableNumber(r.CallOI),
          oi_ratio: nullableNumber(r["PutCallOIRatio%"])
        })).filter(r => r.date).sort((a, b) =>
          a.date < b.date ? -1 : 1
        );
        return json({
          ok: true,
          source: "TAIFEX",
          dataset: "put_call_ratio_history",
          market: "TXO",
          date: rows.length ? rows[rows.length - 1].date : null,
          count: rows.length,
          data: rows,
          parser: { version: "1.3", endpoint: "put-call-ratio-history" }
        });
      } catch (error) {
        return json({
          ok: false,
          source: "TAIFEX",
          error: String(error)
        }, 500);
      }
    }

    /* =========================
       V1.4 ADDITIVE — Daily snapshots (KV SNAPSHOTS binding)
       Covers every history-dependent input: top10, chain, day
       positions, walls. scheduled() collects daily after close;
       /snapshots/write-now triggers manually (optional key).
       (collectSnapshotBundle / taipeiTodayISO live at module level.)
    ========================= */

    if (url.pathname === "/snapshots/bundle") {
      try {
        const requested = url.searchParams.get("date");
        if (!env || !env.SNAPSHOTS) {
          return json({
            ok: false,
            error: "KV SNAPSHOTS not bound"
          }, 500);
        }
        let actual = requested;
        let raw = actual
          ? await env.SNAPSHOTS.get(`snapshot:${actual}`)
          : null;
        if (!raw) {
          const list = await env.SNAPSHOTS.list({
            prefix: "snapshot:"
          });
          const dates = list.keys
            .map(k => k.name.replace("snapshot:", ""))
            .filter(d => !requested || d <= requested)
            .sort();
          if (!dates.length) {
            return json({
              ok: false,
              error: "No snapshot available"
            }, 502);
          }
          actual = dates[dates.length - 1];
          raw = await env.SNAPSHOTS.get(`snapshot:${actual}`);
        }
        return json({
          ok: true,
          source: "TAIFEX",
          dataset: "snapshot_bundle",
          date: actual,
          requested_date: requested,
          data: JSON.parse(raw),
          parser: { version: "1.4", endpoint: "snapshots-bundle" }
        });
      } catch (error) {
        return json({
          ok: false,
          source: "TAIFEX",
          error: String(error)
        }, 500);
      }
    }

    if (url.pathname === "/snapshots/write-now") {
      try {
        const key = url.searchParams.get("key");
        if (env && env.SNAPSHOT_KEY && key !== env.SNAPSHOT_KEY) {
          return json({ ok: false, error: "Forbidden" }, 403);
        }
        if (!env || !env.SNAPSHOTS) {
          return json({
            ok: false,
            error: "KV SNAPSHOTS not bound"
          }, 500);
        }
        const iso =
          url.searchParams.get("date") || taipeiTodayISO();
        const slash = iso.replace(/-/g, "/");
        const bundle = await collectSnapshotBundle(iso, slash);
        await env.SNAPSHOTS.put(
          `snapshot:${iso}`,
          JSON.stringify(bundle)
        );
        const sizes = {};
        for (const k of Object.keys(bundle.data)) {
          const v = bundle.data[k];
          sizes[k] = Array.isArray(v) ? v.length : typeof v;
        }
        return json({
          ok: true,
          source: "TAIFEX",
          dataset: "snapshot_write",
          date: iso,
          coverage: sizes,
          parser: { version: "1.4", endpoint: "snapshots-write-now" }
        });
      } catch (error) {
        return json({
          ok: false,
          source: "TAIFEX",
          error: String(error)
        }, 500);
      }
    }

    /* 未知 endpoint */

    return json({

      ok: false,

      error: "Not found",

      endpoints: [
        "/health",
        "/futures-institutional-after-hours",
        "/futures-institutional",
        "/futures-price",
        "/futures-price-after-hours",
        "/futures-institutional-oi?date=YYYY-MM-DD",
        "/futures-institutional-oi-history?date=YYYY-MM-DD",
        "/futures-options-chain?date=YYYY-MM-DD",
        "/options-delta?date=YYYY-MM-DD",
        "/options-key-levels?date=YYYY-MM-DD",
        "/options-gamma-levels?date=YYYY-MM-DD",
        "/options-market-structure?date=YYYY-MM-DD",
        "/options-market-structure-compact?date=YYYY-MM-DD",
        "/options-institutional",
        "/options-institutional-after-hours",
        "/options-after-hours",
        "/futures-top10?date=YYYY-MM-DD",
        "/options-top10?date=YYYY-MM-DD",
        "/futures-night-ohlc?date=YYYY-MM-DD",
        "/put-call-ratio-history",
        "/snapshots/bundle?date=YYYY-MM-DD",
        "/snapshots/write-now",
        "/debug-taifex"
      ]

    }, 404);
  }
};
