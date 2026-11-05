export default {
  async fetch(request, env) {
    try {
      const url = new URL(request.url);

      // ==================================================
      // TWSE Proxy V1.2 (V1.1 + upstream date validation)
      //
      // 已驗證 Endpoint（V1.0 原樣，未動）：
      //   IND → TAIEX
      //   MS  → 大盤統計 + 漲跌家數
      //
      // V1.1 新增：
      //   /institutional?date=YYYYMMDD → 三大法人 (RWD BFI82U 金額口徑)
      //
      // 不包含：
      //   T86
      // ==================================================

      // --------------------------------------------------
      // 1. 日期
      //
      // 使用：
      // ?date=20260909
      //
      // 若沒有指定日期，使用目前日期
      // --------------------------------------------------

      let date = url.searchParams.get("date");

      if (!date) {
        const now = new Date();

        date =
          now.getUTCFullYear().toString() +
          String(now.getUTCMonth() + 1).padStart(2, "0") +
          String(now.getUTCDate()).padStart(2, "0");
      }

      // --------------------------------------------------
      // 日期格式驗證
      // --------------------------------------------------

      if (!/^\d{8}$/.test(date)) {
        return new Response(
          JSON.stringify(
            {
              ok: false,
              error: "Invalid date format. Use YYYYMMDD.",
              example: "?date=20260909"
            },
            null,
            2
          ),
          {
            status: 400,
            headers: {
              "content-type": "application/json; charset=UTF-8"
            }
          }
        );
      }

      const formattedDate =
        `${date.slice(0, 4)}-${date.slice(4, 6)}-${date.slice(6, 8)}`;

      // ==================================================
      // TWSE Proxy V1.2 ADDITIVE (2026-11-05)
      // + /institutional?date=YYYYMMDD (三大法人，RWD BFI82U 金額口徑)
      // 預設路由 (IND/MS) 以下完全未動。
      // ==================================================

      // --------------------------------------------------
      // 1b. /institutional（加法路由；預設流程不受影響）
      // --------------------------------------------------

      if (url.pathname === "/institutional") {
        const bfiUrl =
          `https://www.twse.com.tw/rwd/zh/fund/BFI82U?date=${date}&response=json`;

        const bfiResponse = await fetch(bfiUrl, {
          method: "GET",
          headers: {
            "User-Agent": "Mozilla/5.0",
            "Accept": "application/json"
          }
        });

        const bfiText = await bfiResponse.text();

        if (!bfiResponse.ok) {
          return new Response(
            JSON.stringify(
              {
                ok: false,
                source: "TWSE",
                proxy: "twse-proxy",
                version: "1.2.0",
                endpoint: "BFI82U",
                date: formattedDate,
                status: bfiResponse.status,
                body: bfiText.slice(0, 500)
              },
              null,
              2
            ),
            {
              status: 502,
              headers: {
                "content-type": "application/json; charset=UTF-8"
              }
            }
          );
        }

        let bfiData;
        try {
          bfiData = JSON.parse(bfiText);
        } catch (error) {
          return new Response(
            JSON.stringify(
              {
                ok: false,
                source: "TWSE",
                proxy: "twse-proxy",
                version: "1.2.0",
                endpoint: "BFI82U",
                date: formattedDate,
                error: "BFI82U JSON parse failed",
                detail: error.message
              },
              null,
              2
            ),
            {
              status: 502,
              headers: {
                "content-type": "application/json; charset=UTF-8"
              }
            }
          );
        }

        // 金額單位：元 → 億元
        const toYi = (v) => {
          if (v === undefined || v === null) return null;
          const n = Number(String(v).replace(/,/g, ""));
          return Number.isFinite(n) ? n / 1e8 : null;
        };

        let foreign = null;
        let trust = null;
        let dealerOwn = null;
        let dealerHedge = null;

        for (const row of bfiData.data || []) {
          if (!Array.isArray(row) || row.length < 4) continue;
          const name = String(row[0] || "");
          const net = toYi(row[3]);
          if (net === null) continue;
          if (name.includes("外資自營商")) {
            foreign = (foreign ?? 0) + net; // 與外資及陸資合併
          } else if (name.includes("外資")) {
            foreign = (foreign ?? 0) + net;
          } else if (name.includes("投信")) {
            trust = (trust ?? 0) + net;
          } else if (name.includes("自營商") && name.includes("避險")) {
            dealerHedge = (dealerHedge ?? 0) + net;
          } else if (name.includes("自營商")) {
            dealerOwn = (dealerOwn ?? 0) + net;
          }
        }

        const dealer =
          dealerOwn !== null || dealerHedge !== null
            ? (dealerOwn ?? 0) + (dealerHedge ?? 0)
            : null;
        const total =
          foreign !== null && trust !== null && dealer !== null
            ? foreign + trust + dealer
            : null;

        // RWD 會忽略 date 參數回傳最新；如實回報實際日期
        const actualDate = String(bfiData.date || "");
        const requestedCompact = date;
        const actualCompact = actualDate.replace(/-/g, "");

        return new Response(
          JSON.stringify(
            {
              ok:
                foreign !== null &&
                trust !== null &&
                dealer !== null,
              source: "TWSE",
              proxy: "twse-proxy",
              version: "1.2.0",
              endpoint: "BFI82U",
              date: formattedDate,
              actual_date: actualDate,
              date_mismatch:
                actualCompact !== requestedCompact,
              unit: "億元 (新台幣億元)",
              data: {
                foreign,
                investment_trust: trust,
                dealer,
                total
              }
            },
            null,
            2
          ),
          {
            status: 200,
            headers: {
              "content-type":
                "application/json; charset=UTF-8",
              "cache-control":
                "no-store"
            }
          }
        );
      }

      // ==================================================
      // 2. 取得 IND（以下預設流程 V1.0 原樣，未動）
      // ==================================================

      const indUrl =
        `https://www.twse.com.tw/exchangeReport/MI_INDEX?response=json&date=${date}&type=IND`;

      const indResponse = await fetch(indUrl, {
        method: "GET",
        headers: {
          "User-Agent": "Mozilla/5.0",
          "Accept": "application/json"
        }
      });

      const indText = await indResponse.text();

      if (!indResponse.ok) {
        return new Response(
          JSON.stringify(
            {
              ok: false,
              source: "TWSE",
              endpoint: "IND",
              date: formattedDate,
              status: indResponse.status,
              body: indText
            },
            null,
            2
          ),
          {
            status: 502,
            headers: {
              "content-type": "application/json; charset=UTF-8"
            }
          }
        );
      }

      // ==================================================
      // 3. 解析 IND
      // ==================================================

      let indData;

      try {
        indData = JSON.parse(indText);
      } catch (error) {
        return new Response(
          JSON.stringify(
            {
              ok: false,
              source: "TWSE",
              endpoint: "IND",
              date: formattedDate,
              error: "IND JSON parse failed",
              detail: error.message
            },
            null,
            2
          ),
          {
            status: 502,
            headers: {
              "content-type": "application/json; charset=UTF-8"
            }
          }
        );
      }

      // 驗證 IND 上游實際日期；不可用請求日期冒充資料日期
      const indActualDate = String(indData.date || "");
      const compactDate = (value) => value.replace(/[^0-9]/g, "");
      const indDateValid = compactDate(indActualDate) === date;
      if (!indDateValid) {
        return new Response(JSON.stringify({
          ok: false, source: "TWSE", proxy: "twse-proxy", version: "1.2.0",
          endpoint: "IND", date: formattedDate, actual_date: indActualDate || null,
          date_mismatch: true, error: "IND upstream date missing or mismatched"
        }, null, 2), {
          status: 502, headers: { "content-type": "application/json; charset=UTF-8", "cache-control": "no-store" }
        });
      }

      // ==================================================
      // 4. 取得 MS
      // ==================================================

      const msUrl =
        `https://www.twse.com.tw/exchangeReport/MI_INDEX?response=json&date=${date}&type=MS`;

      const msResponse = await fetch(msUrl, {
        method: "GET",
        headers: {
          "User-Agent": "Mozilla/5.0",
          "Accept": "application/json"
        }
      });

      const msText = await msResponse.text();

      if (!msResponse.ok) {
        return new Response(
          JSON.stringify(
            {
              ok: false,
              source: "TWSE",
              endpoint: "MS",
              date: formattedDate,
              status: msResponse.status,
              body: msText
            },
            null,
            2
          ),
          {
            status: 502,
            headers: {
              "content-type": "application/json; charset=UTF-8"
            }
          }
        );
      }

      // ==================================================
      // 5. 解析 MS
      // ==================================================

      let msData;

      try {
        msData = JSON.parse(msText);
      } catch (error) {
        return new Response(
          JSON.stringify(
            {
              ok: false,
              source: "TWSE",
              endpoint: "MS",
              date: formattedDate,
              error: "MS JSON parse failed",
              detail: error.message
            },
            null,
            2
          ),
          {
            status: 502,
            headers: {
              "content-type": "application/json; charset=UTF-8"
            }
          }
        );
      }

      // 驗證 MS 上游實際日期；不符時只停用 MS 衍生欄位
      const msActualDate = String(msData.date || "");
      const msDateValid = compactDate(msActualDate) === date;

      // ==================================================
      // 6. 擷取 TAIEX
      // ==================================================

      let taiex = null;

      for (const table of indData.tables || []) {
        if (!Array.isArray(table.data)) continue;

        for (const row of table.data) {
          if (row[0] === "發行量加權股價指數") {
            taiex = {
              name: row[0],
              close: row[1],
              direction: row[2],
              change: row[3],
              change_percent: row[4],
              note: row[5] || ""
            };

            break;
          }
        }

        if (taiex) break;
      }

      // ==================================================
      // 7. 擷取大盤統計資訊
      // ==================================================

      let marketStatistics = null;

      for (const table of (msDateValid ? msData.tables || [] : [])) {
        if (!Array.isArray(table.data)) continue;

        if (
          typeof table.title === "string" &&
          table.title.includes("大盤統計資訊")
        ) {
          marketStatistics = table;
          break;
        }
      }

      // ==================================================
      // 8. 擷取漲跌證券數
      // ==================================================

      let advanceDecline = null;

      for (const table of msData.tables || []) {
        if (!Array.isArray(table.data)) continue;

        if (
          typeof table.title === "string" &&
          table.title.includes("漲跌證券數合計")
        ) {
          advanceDecline = table;
          break;
        }
      }

      // ==================================================
      // 9. 建立正式標準化 JSON
      // ==================================================

      const result = {
        ok: indDateValid && !!taiex,

        source: "TWSE",

        proxy: "twse-proxy",

        version: "1.2.0",

        date: formattedDate,

        endpoints: {
          IND: {
            status: indResponse.status,
            fetch_ok: indResponse.ok,
            actual_date: indActualDate,
            date_valid: indDateValid
          },

          MS: {
            status: msResponse.status,
            fetch_ok: msResponse.ok,
            actual_date: msActualDate || null,
            date_valid: msDateValid
          }
        },

        data: {
          taiex: taiex,

          market_statistics: msDateValid ? marketStatistics : null,

          advance_decline: msDateValid ? advanceDecline : null
        }
      };

      // ==================================================
      // 10. 回傳
      // ==================================================

      return new Response(
        JSON.stringify(result, null, 2),
        {
          status: 200,
          headers: {
            "content-type":
              "application/json; charset=UTF-8",

            "cache-control":
              "no-store"
          }
        }
      );

    } catch (error) {

      // ==================================================
      // Error Handler
      // ==================================================

      return new Response(
        JSON.stringify(
          {
            ok: false,

            source: "TWSE",

            proxy: "twse-proxy",

            version: "1.2.0",

            error: error.message
          },
          null,
          2
        ),
        {
          status: 500,
          headers: {
            "content-type":
              "application/json; charset=UTF-8"
          }
        }
      );
    }
  }
};