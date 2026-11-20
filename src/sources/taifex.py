"""TAIFEX 期貨+選擇權：Cloudflare Proxy (主來源)。

https://taifex.grichtoyang.workers.dev/
端點：futures-price[-after-hours]、futures-institutional[-after-hours]、
  futures-institutional-oi[-history]、futures-options-chain、
  options-delta、options-gamma-levels、options-key-levels、
  options-market-structure-compact、options-institutional[-after-hours]、
  options-after-hours
(options-gamma-levels 提供 Gamma Wall/Flip 與完整 GEX；端點失敗時，
  Gamma Wall/Flip 可由 options-market-structure-compact 備援，GEX 不以 proxy 代替)

金額欄位單位：千元 (→億元 /1e5)。近月 = 日盤成交量最大契約。
前十大交易人走 taifex_official (proxy 優先)。
純數據整理，不做分析判斷。
"""
from __future__ import annotations
import sys
import requests
from src.utils import HEADERS

BASE = "https://taifex.grichtoyang.workers.dev"
DATE_EPS = {"futures-institutional-oi", "futures-institutional-oi-history", "futures-options-chain",
            "options-gamma-levels", "options-key-levels", "options-market-structure-compact",
            "options-market-structure"}
TXO_CHAIN_EPS = {"options-key-levels", "futures-options-chain", "options-market-structure-compact", "options-market-structure", "options-gamma-levels"}
FREE_EPS = ["futures-price", "futures-price-after-hours", "futures-institutional",
            "futures-institutional-after-hours", "options-institutional",
            "options-institutional-after-hours", "options-after-hours",
            "options-day-call-put"]
INST_ZH = {"foreign": "外資", "investment_trust": "投信", "dealer": "自營商"}

def _missing_night_fields(night: dict) -> list[str]:
    """Return report-visible night-session fields that have no value."""
    # TAIFEX does not publish daily settlement price or OI after the after-hours session.
    fields = ("open", "high", "low", "close", "change", "pct", "vol")
    return [f"futures.night.{field}" for field in fields if night.get(field) is None]

# F1（2026-10-19）：快照 bundle memoize。build() 的 Chain／法人部位使用 T-1 快照；
# 前十大 OpenAPI 內容落後一交易日，因此 snap_top10_change() 讀取 T0 Worker 快照。
# 同一進程內重複請求同一 (proxy, date) 只快取成功結果；
# 失敗仍每次重抓（不把一次上游故障釘成永久 unavailable）。
# 呼叫端只讀不寫（build 取 .get/.items、snap_top10_change 複製 list 後才 sort），
# 故直接回傳同一物件，不做昂貴的深拷貝。
_SNAP_CACHE: dict[tuple, dict] = {}

_LAST_FETCH_ERRORS: dict[str, dict] = {}


def _worker_error_payload(response) -> dict:
    """Extract bounded diagnostics from a Worker JSON error response."""
    try:
        payload = response.json()
    except Exception:  # noqa: BLE001
        return {}
    if not isinstance(payload, dict):
        return {}
    data = payload.get("data") if isinstance(payload.get("data"), dict) else {}
    diagnostics = payload.get("diagnostics") if isinstance(payload.get("diagnostics"), dict) else {}
    detail = (payload.get("detail") or data.get("detail") or data.get("reason")
              or diagnostics.get("primary_error") or diagnostics.get("fallback_error"))
    return {
        "error_code": payload.get("error_code") or diagnostics.get("error_code"),
        "stage": payload.get("stage") or diagnostics.get("stage"),
        "error": payload.get("error"),
        "detail": str(detail)[:400] if detail is not None else None,
        "data_reason": str(data.get("reason"))[:400] if data.get("reason") is not None else None,
    }


def _get_impl(ep: str, t0: str, timeout: int = 40) -> dict | None:
    import time
    url = f"{BASE}/{ep}?date={t0}" if ep in DATE_EPS else f"{BASE}/{ep}"
    _LAST_FETCH_ERRORS.pop(ep, None)
    for attempt in range(2):
        try:
            r = requests.get(url, headers={**HEADERS, "accept": "application/json"}, timeout=timeout)
            diagnostic = _worker_error_payload(r)
            if r.status_code == 200:
                try:
                    j = r.json()
                except Exception as e:  # noqa: BLE001
                    j = None
                    diagnostic["detail"] = f"Invalid Worker JSON: {e}"[:400]
                if isinstance(j, dict) and j.get("ok") is True and j.get("data") is not None:
                    _LAST_FETCH_ERRORS.pop(ep, None)
                    return j
                diagnostic.update({
                    "http_status": 200,
                    "error_code": diagnostic.get("error_code") or "WORKER_OK_FALSE_OR_EMPTY",
                    "stage": diagnostic.get("stage") or "worker_response",
                    "error": diagnostic.get("error") or "Worker returned ok=false or empty data",
                })
                _LAST_FETCH_ERRORS[ep] = diagnostic
                if attempt == 0:
                    print(f"[INFO] taifex {ep} ok!=true/無資料 (try {attempt + 1})，4 秒後重試",
                          file=sys.stderr, flush=True)
                    time.sleep(4)
                    continue
                print(f"[INFO] taifex {ep} 仍無資料，放棄：{diagnostic}", file=sys.stderr, flush=True)
                return None
            diagnostic.update({
                "http_status": r.status_code,
                "error_code": diagnostic.get("error_code") or f"HTTP_{r.status_code}",
                "stage": diagnostic.get("stage") or "http_request",
                "error": diagnostic.get("error") or f"Worker HTTP {r.status_code}",
            })
            _LAST_FETCH_ERRORS[ep] = diagnostic
            # F3-a：保留原有全域重試次數；僅 TXO Chain 兩端點對 502 加短暫退避，
            # 避免連續立即重打同一條 TAIFEX 共用上游路徑。其他端點行為不變。
            if r.status_code in (429, 503):
                print(f"[INFO] taifex {ep} HTTP {r.status_code} (try {attempt + 1})，退避 3 秒後重試",
                      file=sys.stderr, flush=True)
                time.sleep(3)
                continue
            if r.status_code == 502:
                if ep in TXO_CHAIN_EPS and attempt == 0:
                    print(f"[INFO] taifex {ep} HTTP 502 (try {attempt + 1})，退避 2 秒後重試",
                          file=sys.stderr, flush=True)
                    time.sleep(2)
                elif ep in TXO_CHAIN_EPS:
                    print(f"[INFO] taifex {ep} HTTP 502 (try {attempt + 1})，重試次數已用盡",
                          file=sys.stderr, flush=True)
                else:
                    print(f"[INFO] taifex {ep} HTTP 502 (try {attempt + 1})，直接重試",
                          file=sys.stderr, flush=True)
                continue
            print(f"[INFO] taifex {ep} HTTP {r.status_code}，放棄：{diagnostic}", file=sys.stderr, flush=True)
            return None
        except requests.exceptions.Timeout as e:
            _LAST_FETCH_ERRORS[ep] = {
                "error_code": "REQUEST_TIMEOUT", "stage": "http_request",
                "error": "Worker request timed out", "detail": str(e)[:400],
            }
            print(f"[INFO] taifex {ep} read timeout (try {attempt + 1})：{e}",
                  file=sys.stderr, flush=True)
            if attempt == 0:
                time.sleep(3)
        except Exception as e:  # noqa: BLE001
            _LAST_FETCH_ERRORS[ep] = {
                "error_code": "REQUEST_FAILED", "stage": "http_request",
                "error": "Worker request failed", "detail": str(e)[:400],
            }
            print(f"[WARN] taifex {ep} failed (try {attempt + 1}): {e}",
                  file=sys.stderr, flush=True)
            if attempt == 0:
                time.sleep(2)
    return None


def _get(ep: str, t0: str, timeout: int = 40) -> dict | None:
    """Measure each TAIFEX Worker endpoint call without changing retry behavior."""
    import time
    started = time.perf_counter()
    result = None
    try:
        result = _get_impl(ep, t0, timeout=timeout)
        return result
    finally:
        status = "ok" if result is not None else "unavailable"
        print(
            f"[TIMING] taifex_endpoint={ep} date={t0} status={status} "
            f"elapsed={time.perf_counter() - started:.2f}s",
            file=sys.stderr, flush=True)

def _memoized_build_fetch(fetch):
    """Memoize endpoint/date responses while allowing failed compact calls a longer retry.

    Key-level responses are deliberately not cached so the existing 90s
    fallback can retry an incomplete 40s response. Compact successes and
    failures are shared across Gamma/Wall fallback paths, but a failed result
    may be retried once at a strictly longer timeout. This preserves the
    fallback's 90s timeout without repeating successful endpoint/date calls.
    """
    cache = {}

    def _cached(ep: str, day: str, timeout: int = 40):
        key = (ep, day)
        cached = cache.get(key)
        if cached is not None:
            cached_result, cached_timeout = cached
            if cached_result is not None or timeout <= cached_timeout:
                return cached_result
        result = fetch(ep, day, timeout=timeout)
        if ep == "options-market-structure-compact":
            cache[key] = (result, timeout)
        elif result is not None and ep != "options-key-levels":
            cache[key] = (result, timeout)
        return result

    return _cached


def _sync_gamma_unavailable(unavailable: list[str], wall, flip) -> list[str]:
    """Keep unavailable flags aligned with the final resolved Gamma fields."""
    result = list(unavailable)
    if wall is not None:
        result = [field for field in result if field != "gamma_wall"]
    if flip is not None:
        result = [field for field in result if field != "gamma_flip"]
    return result

def _valid_gex_levels(levels) -> list[dict]:
    """Keep only computed strike-level GEX rows with finite numeric values."""
    import math
    if not isinstance(levels, list):
        return []
    valid = []
    for row in levels:
        if not isinstance(row, dict):
            continue
        try:
            strike = float(row.get("strike"))
            net_gex = float(row.get("net_gex_1pct"))
            gross_gex = float(row.get("gross_gex_1pct"))
            call_gex = float(row.get("call_gex_1pct"))
            put_gex = float(row.get("put_gex_1pct"))
        except (TypeError, ValueError):
            continue
        if not all(math.isfinite(v) for v in (strike, net_gex, gross_gex, call_gex, put_gex)) or strike <= 0:
            continue
        valid.append({**row, "strike": strike, "net_gex_1pct": net_gex, "gross_gex_1pct": gross_gex,
                      "call_gex_1pct": call_gex, "put_gex_1pct": put_gex})
    return sorted(valid, key=lambda item: item["strike"])


def _gamma_expiry_metadata(gdata: dict | None, primary_month: str | None) -> dict:
    """Preserve the exact expiry and raw OI totals used by the Worker GEX model."""
    data = gdata if isinstance(gdata, dict) else {}
    call_oi = data.get("call_oi") if isinstance(data.get("call_oi"), dict) else {}
    put_oi = data.get("put_oi") if isinstance(data.get("put_oi"), dict) else {}
    gex_month = data.get("contract_month")
    return {
        "primary_expiry_month": primary_month,
        "gex_contract_month": gex_month,
        "gex_expiry_date": data.get("expiry_date"),
        "gex_call_oi": call_oi,
        "gex_put_oi": put_oi,
        "gex_expiry_matches_primary": (
            None if not gex_month or not primary_month
            else gex_month == primary_month
        ),
    }


def _gamma_status(unavailable: list[str], endpoint_unavailable: bool,
                  wall, flip, source: str, gex_model_available: bool = False,
                  flip_diagnostics: dict | None = None,
                  wide_range_flip: dict | None = None,
                  wide_range_diagnostics: dict | None = None) -> tuple[list[str], list[str]]:
    """Resolve Gamma availability and describe formal/wide scan results accurately."""
    result = _sync_gamma_unavailable(unavailable, wall, flip)
    notes = []
    if endpoint_unavailable and (wall is not None or flip is not None):
        notes.append(f"Gamma 原始端點不可用（上游 502）；已由 {source} 備援取得"
                     f"（Wall {'有值' if wall is not None else '仍缺值'}；"
                     f"Flip {'有值' if flip is not None else '仍缺值'}）")
    for field, value, label in (
        ("gamma_wall", wall, "Gamma Wall"),
        ("gamma_flip", flip, "Gamma Flip"),
    ):
        if value is None:
            if field not in result:
                result.append(field)
            if gex_model_available and field == "gamma_flip":
                formal = flip_diagnostics or {}
                wide = wide_range_diagnostics or {}
                if wide_range_flip:
                    estimated = wide_range_flip.get("estimated_underlying")
                    notes.append(
                        f"正式 Gamma Flip 搜尋範圍未找到零交叉（±10%；"
                        f"搜尋區間 {formal.get('search_lower_underlying', '未提供')}–"
                        f"{formal.get('search_upper_underlying', '未提供')}）；"
                        f"擴大診斷範圍找到零交叉，估計價位 {estimated} "
                        "（僅供診斷，不取代正式 ±10% 結果），正式欄位維持 unavailable"
                    )
                elif wide.get("found") is True or wide.get("zero_crossings", 0):
                    notes.append(
                        "正式 Gamma Flip 搜尋範圍未找到零交叉（±10%）；"
                        "擴大診斷範圍有零交叉訊號但未提供估計價位，正式欄位維持 unavailable"
                    )
                else:
                    notes.append(
                        "正式 Gamma Flip 搜尋範圍未找到零交叉（±10%）；"
                        "擴大診斷範圍亦未找到零交叉，僅能判定在已掃描區間內無交叉，"
                        "不可推論整個價格範圍均不存在 Flip，正式欄位維持 unavailable"
                    )
            elif gex_model_available:
                notes.append(f"{label} 未找到有效價位；逐履約價 GEX 模型仍可用，標 unavailable")
            else:
                notes.append(f"{label} 原始端點與 Proxy 備援皆未取得有效價位，標 unavailable")
    return result, notes


def _gamma_proxy_fallback(
    fetch, dates: list[str], initial_wall=None, initial_flip=None
) -> dict:
    """Resolve only missing Wall/Flip fields across fallback dates.

    Primary options-gamma-levels values seed the search, so compact history
    is not fetched again for a Gamma field already resolved by the primary.
    Preserve the first useful payload and merge proxy values with provenance.
    """
    payload = None
    wall, flip = initial_wall, initial_flip
    wall_date = flip_date = None
    attempts = []
    for day in dates:
        candidate = fetch(day)
        gamma = ((((candidate or {}).get("data") or {}).get("gamma")) or {})
        candidate_wall = gamma.get("gamma_wall_proxy")
        candidate_flip = gamma.get("gamma_flip_proxy")
        fetch_error = _LAST_FETCH_ERRORS.get("options-market-structure-compact") if candidate is None else None
        attempts.append({
            "requested_date": day,
            "response": "available" if candidate is not None else "unavailable",
            "response_date": candidate.get("date") if isinstance(candidate, dict) else None,
            "gamma_status": gamma.get("status"),
            "gamma_wall_proxy": candidate_wall,
            "gamma_flip_proxy": candidate_flip,
            "error_code": (fetch_error or {}).get("error_code"),
            "error": (fetch_error or {}).get("error"),
        })
        if wall is None and candidate_wall is not None:
            wall, wall_date = candidate_wall, day
        if flip is None and candidate_flip is not None:
            flip, flip_date = candidate_flip, day
        if payload is None and (candidate_wall is not None or candidate_flip is not None):
            payload = candidate
        if wall is not None and flip is not None:
            break

    if payload is None:
        return {"payload": None, "wall": None, "wall_date": None,
                "flip": None, "flip_date": None, "attempts": attempts}

    merged = dict(payload)
    data = dict(merged.get("data") or {})
    gamma = dict(data.get("gamma") or {})
    if wall is not None:
        gamma["gamma_wall_proxy"] = wall
    if flip is not None:
        gamma["gamma_flip_proxy"] = flip
    gamma["gamma_wall_proxy_date"] = wall_date
    gamma["gamma_flip_proxy_date"] = flip_date
    data["gamma"] = gamma
    merged["data"] = data
    return {"payload": merged, "wall": wall, "wall_date": wall_date,
            "flip": flip, "flip_date": flip_date, "attempts": attempts}


def _complete_sum(values) -> int | float | None:
    """Sum only a non-empty collection of complete, non-None values; zero remains valid."""
    values = list(values)
    if not values or any(value is None for value in values):
        return None
    return sum(values)


def _complete_ratio(numerator, denominator):
    """Return a ratio only when both complete aggregates exist and denominator is non-zero."""
    return numerator / denominator if numerator is not None and denominator not in (None, 0) else None


def _oi_distribution(rows: list, limit: int = 10) -> list[dict]:
    """Preserve row OI; calculate percentages only with a complete non-empty denominator."""
    total = _complete_sum(row.get("open_interest") for row in rows)
    top = sorted(rows, key=lambda row: row.get("open_interest") if row.get("open_interest") is not None else 0,
                 reverse=True)[:limit]
    return [{"strike": row.get("strike"), "oi": row.get("open_interest"),
             "pct": round(row["open_interest"] / total * 100, 2)
             if total is not None and row.get("open_interest") is not None else None}
            for row in top]



def _options_chain_oi_change(current_chain, previous_chain, primary_month: str) -> dict | None:
    """Calculate OI deltas on valid common contracts; skip missing OI without zero-filling.

    Coverage denominator includes every unique identity in the selected month,
    including identities with missing/invalid OI. Invalid or duplicate identities
    invalidate the comparison because their contract-level values are ambiguous.
    """
    import math
    if not primary_month or not isinstance(current_chain, list) or not isinstance(previous_chain, list):
        return None

    def index(rows):
        values, seen = {}, set()
        identity_count = missing_oi = 0
        for row in rows:
            if not isinstance(row, dict) or row.get("contract_month") != primary_month:
                continue
            key = (row.get("contract_month"), row.get("contract_expiry_date"),
                   row.get("strike"), row.get("type"))
            if any(value is None for value in key) or key[3] not in ("call", "put") or key in seen:
                return None
            seen.add(key)
            identity_count += 1
            oi = row.get("open_interest")
            if isinstance(oi, bool) or not isinstance(oi, (int, float)) or not math.isfinite(float(oi)) or oi < 0:
                missing_oi += 1
                continue
            values[key] = oi
        return {"values": values, "identity_count": identity_count, "missing_oi": missing_oi}

    current, previous = index(current_chain), index(previous_chain)
    if current is None or previous is None:
        return None
    common = current["values"].keys() & previous["values"].keys()
    if not common:
        return None
    moves = [{"strike": key[2], "type": key[3],
              "d_oi": current["values"][key] - previous["values"][key]} for key in common]
    calls = [move for move in moves if move["type"] == "call"]
    puts = [move for move in moves if move["type"] == "put"]
    calls_up = sorted(calls, key=lambda move: (-move["d_oi"], move["strike"]))
    calls_down = sorted(calls, key=lambda move: (move["d_oi"], move["strike"]))
    puts_up = sorted(puts, key=lambda move: (-move["d_oi"], move["strike"]))
    puts_down = sorted(puts, key=lambda move: (move["d_oi"], move["strike"]))
    matched = len(common)
    current_total, previous_total = current["identity_count"], previous["identity_count"]
    return {
        "c_chg": sum(move["d_oi"] for move in calls) if calls else None,
        "p_chg": sum(move["d_oi"] for move in puts) if puts else None,
        "c_up": calls_up[0] if calls_up and calls_up[0]["d_oi"] > 0 else None,
        "c_dn": calls_down[0] if calls_down and calls_down[0]["d_oi"] < 0 else None,
        "p_up": puts_up[0] if puts_up and puts_up[0]["d_oi"] > 0 else None,
        "p_dn": puts_down[0] if puts_down and puts_down[0]["d_oi"] < 0 else None,
        "matched_count": matched,
        "current_count": len(current["values"]),
        "previous_count": len(previous["values"]),
        "current_identity_count": current_total,
        "previous_identity_count": previous_total,
        "current_missing_oi": current["missing_oi"],
        "previous_missing_oi": previous["missing_oi"],
        "current_coverage": matched / current_total if current_total else 0.0,
        "previous_coverage": matched / previous_total if previous_total else 0.0,
        "partial": (matched != current_total or matched != previous_total
                    or current["missing_oi"] > 0 or previous["missing_oi"] > 0),
    }


def _options_chain_oi_change_diagnostic(current_chain, previous_chain, primary_month: str) -> dict:
    """Report the same valid/invalid identity sets used by _options_chain_oi_change."""
    import math
    result = {"primary_month": primary_month, "current_count": 0, "previous_count": 0,
              "current_identity_count": 0, "previous_identity_count": 0,
              "current_only": 0, "previous_only": 0, "current_missing_oi": 0,
              "previous_missing_oi": 0, "invalid_identity": 0, "duplicate_identity": 0,
              "reason": None}
    if not primary_month:
        result["reason"] = "primary_expiry_missing"
        return result
    if not isinstance(current_chain, list) or not isinstance(previous_chain, list):
        result["reason"] = "chain_payload_missing"
        return result

    def index(rows, side):
        values, seen = {}, set()
        for row in rows:
            if not isinstance(row, dict) or row.get("contract_month") != primary_month:
                continue
            key = (row.get("contract_month"), row.get("contract_expiry_date"),
                   row.get("strike"), row.get("type"))
            if any(value is None for value in key) or key[3] not in ("call", "put"):
                result["invalid_identity"] += 1
                continue
            if key in seen:
                result["duplicate_identity"] += 1
                continue
            seen.add(key)
            result[side + "_identity_count"] += 1
            oi = row.get("open_interest")
            if isinstance(oi, bool) or not isinstance(oi, (int, float)) or not math.isfinite(float(oi)) or oi < 0:
                result[side + "_missing_oi"] += 1
                continue
            values[key] = oi
        result[side + "_count"] = len(values)
        return values

    current, previous = index(current_chain, "current"), index(previous_chain, "previous")
    result["current_only"] = len(current.keys() - previous.keys())
    result["previous_only"] = len(previous.keys() - current.keys())
    if result["invalid_identity"]:
        reason = "invalid_contract_identity"
    elif result["duplicate_identity"]:
        reason = "duplicate_contract_identity"
    elif not result["current_identity_count"] or not result["previous_identity_count"]:
        reason = "primary_expiry_chain_empty"
    elif result["current_missing_oi"] or result["previous_missing_oi"]:
        reason = "open_interest_missing_or_invalid"
    elif not current or not previous:
        reason = "primary_expiry_chain_empty"
    elif not (current.keys() & previous.keys()):
        reason = "no_common_valid_contracts"
    elif result["current_only"] or result["previous_only"]:
        reason = "contract_set_mismatch"
    else:
        reason = "aligned"
    result["reason"] = reason
    return result


def _options_chain_key_levels_for_month(chain, primary_month: str, expiry_date: str | None = None) -> dict:
    """Recalculate TAIFEX Walls/Max Pain for one expiry; require complete unique OI."""
    import math

    def unavailable(reason, **extra):
        return {"found": False, "reason": reason, **extra}

    if not primary_month or not isinstance(chain, list):
        return unavailable("primary_expiry_or_chain_missing")
    rows = [row for row in chain if isinstance(row, dict)
            and row.get("contract_month") == primary_month]
    if not rows:
        return unavailable("primary_expiry_chain_empty")

    def norm_date(value):
        value = str(value or "").strip().replace("-", "")
        return value if len(value) == 8 and value.isdigit() else None

    wanted = norm_date(expiry_date) if expiry_date else None
    expiry_values = {norm_date(row.get("contract_expiry_date")) for row in rows}
    if None in expiry_values:
        return unavailable("invalid_contract_expiry")
    if wanted:
        rows = [row for row in rows if norm_date(row.get("contract_expiry_date")) == wanted]
        if not rows:
            return unavailable("requested_expiry_not_found", expiry_date=expiry_date)
        actual_expiry = wanted
    elif len(expiry_values) == 1:
        actual_expiry = next(iter(expiry_values))
    else:
        return unavailable("multiple_expiry_dates")

    seen, calls, puts, strikes = set(), [], [], set()
    for row in rows:
        kind, strike, oi = row.get("type"), row.get("strike"), row.get("open_interest")
        identity = (row.get("contract_month"), norm_date(row.get("contract_expiry_date")), strike, kind)
        if kind not in ("call", "put") or strike is None or isinstance(strike, bool):
            return unavailable("invalid_contract_identity", expiry_date=actual_expiry)
        if not isinstance(strike, (int, float)) or not math.isfinite(float(strike)):
            return unavailable("invalid_strike", expiry_date=actual_expiry)
        if identity in seen:
            return unavailable("duplicate_contract_identity", expiry_date=actual_expiry)
        seen.add(identity)
        if isinstance(oi, bool) or not isinstance(oi, (int, float)) or not math.isfinite(float(oi)) or oi < 0:
            return unavailable("open_interest_missing_or_invalid", expiry_date=actual_expiry)
        strikes.add(strike)
        if oi > 0:
            (calls if kind == "call" else puts).append((strike, oi))
    if not calls or not puts:
        return unavailable("call_or_put_side_empty", expiry_date=actual_expiry)

    call_wall = sorted(calls, key=lambda item: (-item[1], item[0]))[0]
    put_wall = sorted(puts, key=lambda item: (-item[1], item[0]))[0]
    pains = []
    for settlement in sorted(strikes):
        call_pain = sum(oi * max(0, settlement - strike) for strike, oi in calls)
        put_pain = sum(oi * max(0, strike - settlement) for strike, oi in puts)
        pains.append((settlement, call_pain + put_pain, call_pain, put_pain))
    max_pain = sorted(pains, key=lambda item: (item[1], item[0]))[0]
    return {"found": True, "expiry_date": actual_expiry[:4] + "-" + actual_expiry[4:6] + "-" + actual_expiry[6:],
            "call_wall": {"strike": call_wall[0], "open_interest": call_wall[1]},
            "put_wall": {"strike": put_wall[0], "open_interest": put_wall[1]},
            "max_pain": {"strike": max_pain[0], "total_pain": max_pain[1],
                         "call_pain": max_pain[2], "put_pain": max_pain[3]},
            "chain_stats": {"rows": len(rows), "call_rows": len(calls),
                            "put_rows": len(puts), "strike_count": len(strikes)}}


def _previous_trading_day_iso(t0: str) -> str | None:
    """Resolve prior trading day with shared TWSE calendar, including year rollover."""
    from datetime import date as _date, timedelta as _td
    import src.t0 as _cal

    try:
        cursor = _date.fromisoformat(t0)
    except (TypeError, ValueError):
        return None
    loaded = {}
    for _ in range(370):
        cursor -= _td(days=1)
        year = cursor.year
        if year not in loaded:
            try:
                closed = _cal.load_closed(year)
            except Exception as exc:  # noqa: BLE001
                print("[WARN] 前一交易日曆載入失敗（{}）：{}".format(year, exc))
                return None
            if _cal._LAST_CAL_ERROR:
                print("[WARN] 前一交易日曆不可用（{}）：{}".format(year, _cal._LAST_CAL_ERROR))
                return None
            loaded[year] = closed
        if _cal.is_trading_day(cursor, loaded[year]):
            return cursor.isoformat()
    return None

def _rows(payload: dict | None) -> list:
    d = (payload or {}).get("data")
    return d if isinstance(d, list) else []

def _by_inst(rows: list) -> dict:
    return {r.get("institution"): r for r in rows if isinstance(r, dict) and r.get("institution")}

def _get_dates(ep: str, dates: list[str], timeout: int = 40) -> tuple[dict | None, str | None]:
    """依序嘗試多個日期 (Gamma FMTQIK 落後時遞補 T-1…)。回傳 (payload, 實際日期)。"""
    for d in dates:
        p = _get(ep, d, timeout)
        if p is not None and (p.get("date") or d) == d:
            return p, d
        if p is not None:
            return p, p.get("date") or d
    return None, None

def _next_trading_day(d):
    """T0 的下一個交易日。期交所報表把「T0 15:00 → T0+1 05:00」的夜盤掛在 T0 的下一個交易日
    （不是日曆 T0+1）。2026-10-17 實證：查 2026-10-19 得 10/16 夜盤 47269/47380/46107/46140/-1144
    （漲跌基準 47,284 = 10/16 結算價）；查 2026-10-17 全空。週五 T0 若用日曆 T0+1 必抓不到。
    日曆不可用（load_closed 失敗，src.t0._LAST_CAL_ERROR 非空）→ 回 None（B3 fail-loud）：
    舊行為退週末判斷會把假日當交易日，夜盤查詢日靜默偏一節。"""
    import src.t0 as _cal
    from datetime import timedelta as _tdd

    def _load(y):
        """載入休市日曆；失敗（例外或 _LAST_CAL_ERROR 非空）→ 警告並回 None。"""
        try:
            closed = _cal.load_closed(y)
        except Exception as e:  # noqa: BLE001
            print(f"[WARN] 交易日曆不可用（load_closed 例外：{e}），不退週末判斷（fail-loud）")
            return None
        if _cal._LAST_CAL_ERROR:
            print(f"[WARN] 交易日曆不可用（{_cal._LAST_CAL_ERROR}），不退週末判斷（fail-loud）")
            return None
        return closed

    _y = d.year
    closed = _load(_y)
    if closed is None:
        return None
    for _ in range(14):
        d = d + _tdd(days=1)
        if d.year != _y:
            _y = d.year
            closed = _load(_y)
            if closed is None:
                return None
        if _cal.is_trading_day(d, closed):
            return d
    return d

def _night_query_date(t0=None, session="全日", now=None) -> str | None:
    """夜盤查詢日（期交所語義：查日期 D → D-1 15:00~D 05:00 節，2026-10-16 官網截圖實證）。
    全日版要 T0 當晚節（15:00 T0 → 05:00 T0+1）→ 查 T0 的下一個交易日
    （報表把該節掛在下一個交易日，不是日曆 T0+1；2026-10-17 實證：查 2026-10-19
    得 10/16 夜盤，查 2026-10-17 全空；週五 T0 用日曆 T0+1 必失效）；
    日盤版要前一夜（今晨收盤節）→ 查今天（此時 T0 即今天）。
    10-12 改查今天是誤診（假日無節次的回退被當成規則錯），此次改回；
    嚴格把關（回傳日期不符視為無新節次）保留，假日照樣安全。
    交易日曆不可用時回 None（B3 fail-loud，不猜測）。"""
    from datetime import date as _date
    from datetime import datetime as _dt
    from datetime import timedelta as _td
    from zoneinfo import ZoneInfo as _ZI
    now = now or _dt.now(_ZI("Asia/Taipei"))
    if session != "日盤" and t0:
        _nxt = _next_trading_day(_date.fromisoformat(t0))
        if _nxt is None:
            return None
        return _nxt.isoformat()
    return now.date().isoformat()


def _night_ohlc(t0: str, month: str | None, session: str = "全日", now=None) -> dict | None:
    """夜盤 OHLC：proxy /futures-night-ohlc (V1.4+) 優先，官方 DailyMarketReportFut 備援。
    回傳含 via/date/qdate，或 None。
    期交所規則：查日期 D + Session=F → D-1 15:00~D 05:00（查詢日為節次收盤日）。
    全日查 T0 的下一個交易日、日盤查今天（_night_query_date）；回傳 date 必須等於查詢日，否則視為無新節次。
    節次完整性：全日節在 T0+1（日曆）05:00 收盤，此前查詢只抓得到半成品，一律不採用。
    官方備援同理，只收查詢日當天列。"""
    import os
    from datetime import datetime as _dt2
    from datetime import timedelta as _td2
    from zoneinfo import ZoneInfo as _ZI2
    now = now or _dt2.now(_ZI2("Asia/Taipei"))
    query_date = _night_query_date(t0, session, now)
    if query_date is None:
        import src.t0 as _cal
        print(f"[WARN] 夜盤 OHLC 不採用：交易日曆不可用（{_cal._LAST_CAL_ERROR or 'load_closed 失敗'}），"
              f"夜盤查詢日無法判定（T0 {t0}，session {session}），不猜測（B3 fail-loud）")
        return None
    if session != "日盤":
        _end_src = (_dt2.fromisoformat(t0) + _td2(days=1)) if t0 else _dt2.fromisoformat(query_date)
        _end = _end_src.replace(
            tzinfo=_ZI2("Asia/Taipei")).replace(hour=5, minute=0)
        if now < _end:
            print(f"[INFO] 夜盤節未收盤（T0 {t0} 節次 {_end} 才收），不採用半成品")
            return None
    base = os.getenv("TAIFEX_PROXY_BASE_URL", BASE).rstrip("/")
    print(f"[NIGHT_OHLC] start t0={t0} session={session} query_date={query_date} month={month}")
    if month:
        try:
            r = requests.get(f"{base}/futures-night-ohlc", params={"date": query_date, "month": month},
                             headers={**HEADERS, "accept": "application/json"}, timeout=30)
            print(f"[NIGHT_OHLC] proxy status={r.status_code} query_date={query_date} month={month}")
            if r.status_code == 200:
                j = r.json()
                d = j.get("data") if isinstance(j, dict) else None
                print(f"[NIGHT_OHLC] proxy payload ok={j.get('ok') if isinstance(j, dict) else None} "
                      f"date={j.get('date') if isinstance(j, dict) else None} "
                      f"data_keys={sorted(d.keys()) if isinstance(d, dict) else []} "
                      f"close={d.get('close') if isinstance(d, dict) else None} "
                      f"volume={d.get('volume') if isinstance(d, dict) else None}")
                if isinstance(j, dict) and j.get("ok") is True and isinstance(d, dict):
                    if d.get("close") is not None and (j.get("date") or "") == query_date:
                        print(f"[NIGHT_OHLC] selected=proxy date={query_date}")
                        return {"open": d.get("open"), "high": d.get("high"), "low": d.get("low"),
                                "close": d.get("close"), "change": d.get("change"),
                                "pct": _pct(d.get("change_percent")),
                                "volume": d.get("volume"),
                                "via": "proxy", "date": query_date,
                                "qdate": query_date}
                    print(f"[NIGHT_OHLC] proxy rejected: expected_date={query_date} actual_date={j.get('date')} "
                          f"close_present={d.get('close') is not None}; try official")
                else:
                    print("[NIGHT_OHLC] proxy rejected: payload shape/ok flag invalid; try official")
            else:
                print(f"[NIGHT_OHLC] proxy rejected: HTTP {r.status_code}; try official")
        except Exception as e:  # noqa: BLE001
            print(f"[NIGHT_OHLC] proxy exception={type(e).__name__}: {e}; try official")
    try:
        from src.sources import taifex_official as _off
        official_all = _off._get("/DailyMarketReportFut")
        official_candidates = [x for x in official_all
                               if x.get("Contract") == "TX" and x.get("TradingSession") == "盤後"
                               and x.get("ContractMonth(Week)") == month]
        rows = [x for x in official_candidates
                if _off._iso(x.get("Date", "")) == query_date]
        print(f"[NIGHT_OHLC] official rows_total={len(official_all)} "
              f"tx_after_hours_month_rows={len(official_candidates)} "
              f"matching_date_rows={len(rows)} query_date={query_date} "
              f"candidate_dates={sorted({_off._iso(x.get('Date', '')) for x in official_candidates})[-5:]}")
        if not rows:
            print(f"[NIGHT_OHLC] result=unavailable query_date={query_date} month={month}")
            return None
        rows.sort(key=lambda x: x.get("Date", ""), reverse=True)
        r0 = rows[0]
        def _n(v):
            try:
                return float(str(v).replace(",", "")) if v not in (None, "", "-", "NULL") else None
            except (ValueError, TypeError):
                return None
        chg, close = _n(r0.get("Change")), _n(r0.get("Last"))
        result = {"open": _n(r0.get("Open")), "high": _n(r0.get("High")), "low": _n(r0.get("Low")),
                  "close": close, "change": chg,
                  "pct": (chg / (close - chg) * 100) if chg is not None and close else None,
                  "via": "official", "date": _off._iso(r0.get("Date", "")),
                  "qdate": query_date}
        print(f"[NIGHT_OHLC] selected=official date={result['date']} close={result['close']} volume={_n(r0.get('Volume'))}")
        return result
    except Exception as e:  # noqa: BLE001
        print(f"[NIGHT_OHLC] official exception={type(e).__name__}: {e}")
        return None

def snapshot_bundle(date: str, timeout: int = 40) -> dict | None:
    """讀 worker 快照 (V1.4+ /snapshots/bundle)。未部署/無資料回 None。
    日盤部位類僅當 collected_at 與標示日期同日才可信 (cron 當日收盤後收集；
    手動回填舊日期時其無日期源實為抓取當下值，不可採用)。
    F1：同 (proxy, date) 命中 _SNAP_CACHE 直接回傳（只快取成功結果）。"""
    import os, time
    base = os.getenv("TAIFEX_PROXY_BASE_URL", BASE).rstrip("/")
    _ck = (base, date)
    if _ck in _SNAP_CACHE:
        return _SNAP_CACHE[_ck]
    for _try in range(2):
        try:
            r = requests.get(f"{base}/snapshots/bundle", params={"date": date},
                             headers={**HEADERS, "accept": "application/json"}, timeout=60)
            if r.status_code != 200:
                print(f"[WARN] snapshot http {r.status_code} (try {_try + 1})")
                time.sleep(5)
                continue
            j = r.json()
            if isinstance(j, dict) and j.get("ok") is True and isinstance(j.get("data"), dict):
                b = j["data"]
                inner = b.get("data") if isinstance(b.get("data"), dict) else b
                trust_pos = str(b.get("collected_at", ""))[:10] == j.get("date")
                _res = {"date": j.get("date"), "data": inner, "trust_pos": trust_pos}
                _SNAP_CACHE[_ck] = _res
                return _res
            print(f"[WARN] snapshot ok!=true (try {_try + 1})")
            time.sleep(5)
        except Exception as e:  # noqa: BLE001
            print(f"[INFO] snapshot 不可用 (try {_try + 1})：{e}")
            time.sleep(5)
    return None

def _prev_dates(t0: str, n: int = 5) -> list[str]:
    from datetime import date as _d, timedelta as _td
    base = _d.fromisoformat(t0)
    return [(base - _td(days=i)).isoformat() for i in range(n + 1)]

def dateless_content_date(now=None) -> str:
    """無日期端點的內容日期判定 (日盤 08:45 開、13:45 收；僅平日)。
    08:00 正式跑時回傳 T0；盤中跑回傳今日。"""
    from datetime import datetime as _dt
    from zoneinfo import ZoneInfo as _ZI
    now = now or _dt.now(_ZI("Asia/Taipei"))
    d = now.date()
    if now.hour < 13 or (now.hour == 13 and now.minute < 45):
        from datetime import timedelta as _td
        d -= _td(days=1)
    while d.weekday() >= 5:
        from datetime import timedelta as _td
        d -= _td(days=1)
    return d.isoformat()

def build(t0: str, taiex_close=None, session: str = "全日") -> dict:
    _LAST_FETCH_ERRORS.clear()
    _fetch = _memoized_build_fetch(_get)
    unav: list[str] = []
    notes: list[str] = []
    _content = dateless_content_date()
    if _content != t0:
        notes.append(f"無日期端點為最新盤勢快照 (判定資料日期 {_content}，非 T0 {t0})，"
                     "適用：日盤價／法人交易／夜盤／選擇權法人；T0 相符時不另標註")
    P = {ep: _fetch(ep, t0) for ep in list(FREE_EPS) + sorted(DATE_EPS - {"options-gamma-levels", "options-market-structure-compact", "futures-options-chain"})}
    # 夜盤附屬端點（量/結算/法人夜交易）同口徑把關：payload 日期必須等於今天，
    # 否則視為無新節次，不採用（回退舊值曾靜默混入，2026-10-08 全日版教訓）。
    # options-after-hours 不在此列（它供日盤買賣權拆分，非純夜盤歸屬）。
    _today = _night_query_date(t0, session)
    if _today is None:
        import src.t0 as _cal0
        notes.append(f"交易日曆不可用（{_cal0._LAST_CAL_ERROR or 'load_closed 失敗'}），"
                     "夜盤查詢日無法判定，夜盤附屬端點一律不採用（B3 fail-loud）")
    for _ep in ("futures-price-after-hours", "futures-institutional-after-hours",
                "options-institutional-after-hours"):
        _p = P.get(_ep)
        _d = (_p or {}).get("date")
        if _p is None:
            continue
        if _today is None:
            P[_ep] = None
        elif _d is not None and _d != _today:
            notes.append(f"{_ep} 日期 {_d} 非今日 {_today}，視為無新節次，不採用")
            P[_ep] = None
    # Gamma 端點需 TAIEX 收盤 (FMTQIK 落後約一日)：僅查詢 T0 一次，上游 502 則標 unavailable，不再跑 T-1/T-2
    g_pay, g_date = None, None
    _p = _fetch("options-gamma-levels", t0)
    _w, _f = None, None
    if _p is not None and (_p.get("date") or t0) == t0:
        _gd = (_p or {}).get("data") or {}
        _w = (_gd.get("gamma_wall") or {}).get("strike")
        _f = (_gd.get("gamma_flip") or {}).get("estimated_underlying")
        if _w is not None or _f is not None:
            g_pay, g_date = _p, t0
    elif _p is not None:
        notes.append(f"Gamma 端點日期 {_p.get('date')} 非 T0 {t0}，拒絕採用（避免舊值混入）")
    gamma_endpoint_unavailable = g_pay is None
    if gamma_endpoint_unavailable and _LAST_FETCH_ERRORS.get("options-gamma-levels"):
        _diag = _LAST_FETCH_ERRORS["options-gamma-levels"]
        _parts = [
            f"code={_diag.get('error_code')}",
            f"stage={_diag.get('stage')}",
            f"HTTP={_diag.get('http_status')}",
            _diag.get("error"),
            _diag.get("detail"),
            _diag.get("data_reason"),
        ]
        _summary = "；".join(str(x) for x in _parts if x)
        notes.append(f"GEX Worker 診斷：{_summary[:900]}")
    # Market-structure-compact 的 Wall/Flip 必須分欄位遞補：
    # T-1 只有 Wall 時，仍須繼續查 T-2 的 Flip，不能因任一欄有值就停止。
    # Only query compact history for Gamma fields missing from the primary endpoint.
    # If both are present, compact data is not needed here; the later Wall fallback
    # still requests it when Key Levels themselves are unavailable.
    _gamma_proxy_dates = _prev_dates(t0, 2) if (_w is None or _f is None) else []
    _gamma_proxy = _gamma_proxy_fallback(
        lambda _d: _fetch("options-market-structure-compact", _d),
        _gamma_proxy_dates, initial_wall=_w, initial_flip=_f)
    if _gamma_proxy["flip"] is None:
        _proxy_diag = []
        for _attempt in _gamma_proxy.get("attempts", []):
            _proxy_diag.append(
                "{}: response={}, response_date={}, status={}, wall={}, flip={}, error={}".format(
                    _attempt["requested_date"], _attempt["response"], _attempt["response_date"],
                    _attempt["gamma_status"], _attempt["gamma_wall_proxy"],
                    _attempt["gamma_flip_proxy"], _attempt["error_code"] or _attempt["error"] or "none"))
        notes.append("Gamma Flip Proxy 查詢診斷：" + "；".join(_proxy_diag))
    c_pay = _gamma_proxy["payload"]
    c_date = next((d for d in (_gamma_proxy["wall_date"], _gamma_proxy["flip_date"]) if d), None)
    P["options-gamma-levels"] = g_pay
    P["options-market-structure-compact"] = c_pay
    gamma_date = g_date or c_date
    # Walls 端點 (key-levels/compact) 工人偶發 503：有 Call Wall 才算命中，否則遞補並標示日期
    kl_pay, kl_date = None, None
    cp_pay, cp_date = None, None
    # 初始批次已抓過 options-key-levels，若有效直接複用，避免重複請求 T0
    _existing_kl = P.get("options-key-levels")
    if _existing_kl is not None and (((_existing_kl.get("data") or {}).get("call_wall") or {}).get("strike") is not None):
        kl_pay, kl_date = _existing_kl, t0
    else:
        for _d in _prev_dates(t0, 2):
            if kl_pay is None:
                _p = _fetch("options-key-levels", _d, timeout=90)
                if (((_p or {}).get("data") or {}).get("call_wall") or {}).get("strike") is not None:
                    kl_pay, kl_date = _p, _d
            if cp_pay is None:
                _p = P["options-market-structure-compact"] if _d == t0 else _fetch("options-market-structure-compact", _d, timeout=90)
                if (((_p or {}).get("data") or {}).get("call_wall") or {}).get("strike") is not None:
                    cp_pay, cp_date = _p, _d
            if kl_pay is not None and cp_pay is not None:
                break
    if kl_pay is not None:
        P["options-key-levels"] = kl_pay
    if cp_pay is not None and (P["options-market-structure-compact"] is None):
        P["options-market-structure-compact"] = cp_pay
    walls_date = kl_date or cp_date
    if walls_date and walls_date != t0:
        notes.append(f"Call/Put Wall 與 Max Pain 資料日期 {walls_date} (T0 {t0} 端點不穩，採最新可得)")
    if gamma_date and gamma_date != t0:
        notes.append(f"Gamma 資料日期 {gamma_date} (T0 {t0} 尚無，上游 FMTQIK 落後，採最新可得)")

    # ---------- 期貨 1/2：近月日夜盤 ----------
    prices = _rows(P["futures-price"])
    ahp = _rows(P["futures-price-after-hours"])
    near = max(prices, key=lambda r: (r.get("regular_volume") or 0)) if prices else {}
    ah = next((r for r in ahp if r.get("contract_month") == near.get("contract_month")), {})
    day = {"month": near.get("contract_month"), "open": near.get("open"), "high": near.get("high"),
           "low": near.get("low"), "close": near.get("close"), "change": near.get("change"),
           "pct": _pct(near.get("change_percent")), "vol": near.get("total_volume"),
           "vol_day": near.get("regular_volume"), "oi": near.get("open_interest")}
    # TAIFEX 不公布夜盤結算價與 OI；night 僅保留可用的成交量及 OHLC 行情。
    night = {"month": ah.get("contract_month"), "vol": ah.get("after_hours_volume"),
             "open": None, "high": None, "low": None, "close": None, "change": None, "pct": None,
             "via": "proxy"}
    # 夜盤 OHLC：proxy V1.4+ /futures-night-ohlc 優先，官方 DailyMarketReportFut 備援
    # 全日查 T0+1、日盤查今天（今晨收盤節）；回傳非查詢日一律視為無新節次（_night_ohlc 內部把關＋完整性檢查）
    _nh = _night_ohlc(t0, day["month"], session=session)
    if _nh is not None:
        night.update({k: _nh.get(k) for k in ("open", "high", "low", "close", "change", "pct")})
        # 量取 OHLC 端點（同節次聚合；after-hours 端點量口徑常不一致，2026-10-12 教訓）
        if _nh.get("volume") is not None:
            night["vol"] = _nh.get("volume")
        night["via"] = _nh.get("via", "proxy")
        _q = _nh.get("qdate") or t0
        if _nh.get("date") and _nh["date"] != _q:
            notes.append(f"夜盤 OHLC 回退：查 {_q} 得 {_nh['date']} (T0 {t0})，來源 {_nh.get('via')}，無新節次")
    else:
        import src.t0 as _cal1
        # 全日節 _night_ohlc 內必經 load_closed：_LAST_CAL_ERROR 非空 ⟺ 本次曆失敗，歸因準確
        if session != "日盤" and _cal1._LAST_CAL_ERROR:
            notes.append(f"夜盤開高低收未取得（交易日曆不可用：{_cal1._LAST_CAL_ERROR}），僅有夜盤成交量")
        else:
            notes.append("夜盤開高低收未取得 (proxy 與官方皆無)，僅有夜盤成交量")

    # 完整性清單只追蹤 DATA_REPORT 實際顯示的夜盤行情欄位；夜盤結算價與 OI 不列入資料模型。
    unav.extend(_missing_night_fields(night))

    # ---------- 期貨 3：法人 OI + 變化 ----------
    oi = _by_inst(_rows(P["futures-institutional-oi"]))
    hist = (_fetch("futures-institutional-oi-history", t0) or {}).get("data") or []
    prev = {}
    if len(hist) >= 2:
        for r in hist[1].get("data") or []:
            prev[r.get("institution")] = r
    fut_oi = {}
    for k in ("foreign", "investment_trust", "dealer"):
        cur = oi.get(k, {})
        pr = prev.get(k, {})
        net = cur.get("net_oi")
        fut_oi[k] = {"long": cur.get("long_oi"), "short": cur.get("short_oi"), "net": net,
                     "d_long": _diff(cur.get("long_oi"), pr.get("long_oi")),
                     "d_short": _diff(cur.get("short_oi"), pr.get("short_oi")),
                     "d_net": _diff(net, pr.get("net_oi"))}
    _inst_oi = [fut_oi[k] for k in ("foreign", "investment_trust", "dealer")]
    fut_oi["total"] = {
        field: _complete_sum(row[field] for row in _inst_oi)
        for field in ("long", "short", "net", "d_long", "d_short", "d_net")
    }
    if any(value is None for row in _inst_oi for value in row.values()):
        notes.append("期貨三大法人 OI 部分欄位缺值；對應合計標 unavailable")

    # ---------- 期貨 5：日夜盤法人交易 ----------
    day_t = _by_inst(_rows(P["futures-institutional"]))
    night_t = _by_inst(_rows(P["futures-institutional-after-hours"]))
    fut_trade = {}
    for sess, src in (("day", day_t), ("night", night_t)):
        for k in ("foreign", "investment_trust", "dealer"):
            r = src.get(k, {})
            fut_trade[(sess, k)] = {"long": r.get("long_volume"), "short": r.get("short_volume"),
                                    "net": r.get("net_volume"),
                                    "long_amt_yi": _yi(r.get("long_amount")), "short_amt_yi": _yi(r.get("short_amount")),
                                    "net_amt_yi": _yi(r.get("net_amount"))}
    notes.append("法人交易量未提供前日變化端點；日盤、夜盤交易量及日夜淨額差仍照常列示")

    # ---------- 期貨 6：期現關係 ----------
    basis = None
    basis_pct = None
    if day["close"] is not None and taiex_close is not None:
        basis = day["close"] - taiex_close
        basis_pct = basis / taiex_close * 100 if taiex_close else None

    # ---------- 期貨 7：對照 (量/OI/籌碼變化；價格變化無昨日價格端點) ----------
    oi_chg = fut_oi["total"]["d_net"]

    # ---------- 選擇權 chain (失敗向 T-1…遞補並標示日期) ----------
    chain, chain_date = [], None
    for _d in _prev_dates(t0, 2):
        _p = _fetch("futures-options-chain", _d, timeout=90)
        if _p is not None:
            chain, chain_date = _rows(_p), _d
            break
    if chain_date and chain_date != t0:
        notes.append(f"選擇權 chain 資料日期 {chain_date} (T0 {t0} 端點不穩，採最新可得)")
    kl = (P["options-key-levels"] or {}).get("data") or {}
    prim = (kl.get("primary_expiry") or {}) if isinstance(kl, dict) else {}
    prim_month = prim.get("contract_month")
    pc = [r for r in chain if r.get("contract_month") == prim_month] if prim_month else chain
    calls = [r for r in pc if r.get("type") == "call"]
    puts = [r for r in pc if r.get("type") == "put"]
    c_vol = _complete_sum(r.get("total_volume") for r in calls)
    p_vol = _complete_sum(r.get("total_volume") for r in puts)
    c_oi = _complete_sum(r.get("open_interest") for r in calls)
    p_oi = _complete_sum(r.get("open_interest") for r in puts)
    opt_tot = {"expiry": prim_month, "c_vol": c_vol, "p_vol": p_vol, "c_oi": c_oi, "p_oi": p_oi,
               "vol_ratio": _complete_ratio(c_vol, p_vol),
               "oi_ratio": _complete_ratio(c_oi, p_oi),
               "pc_ratio": _complete_ratio(p_oi, c_oi)}
    if any(value is None for value in (c_vol, p_vol, c_oi, p_oi)):
        notes.append("選擇權 chain 總量或 OI 缺值／不完整；對應合計與比例標 unavailable")
    def top_oi(rows, n=3):
        return sorted(rows, key=lambda r: r.get("open_interest") or 0, reverse=True)[:n]
    tc, tp = top_oi(calls), top_oi(puts)
    opt_conc = {"c_top": [(r.get("strike"), r.get("open_interest")) for r in tc],
                "p_top": [(r.get("strike"), r.get("open_interest")) for r in tp],
                "c_max": (tc[0].get("strike"), tc[0].get("open_interest")) if tc else (None, None),
                "p_max": (tp[0].get("strike"), tp[0].get("open_interest")) if tp else (None, None)}
    # OI 分布明細 Top10 (機器可讀，Dashboard 繪圖用)
    opt_dist = {"expiry": prim_month, "call": _oi_distribution(calls), "put": _oi_distribution(puts)}
    if not chain:
        notes.append("選擇權 chain 未取得，總量/OI/集中區 unavailable")

    # ---------- 選擇權法人 ----------
    oi_inst = _by_inst(_rows(P["options-institutional"]))
    ah_inst = (P["options-after-hours"] or {}).get("data") or {}
    ah_c = _by_inst(ah_inst.get("call") or [])
    ah_p = _by_inst(ah_inst.get("put") or [])
    opt_pos = {}
    for k in ("foreign", "dealer"):
        r = oi_inst.get(k, {})
        opt_pos[k] = {"long": r.get("long_volume"), "short": r.get("short_volume"), "net": r.get("net_volume"),
                      "ah_c_net": (ah_c.get(k) or {}).get("net_volume"),
                      "ah_p_net": (ah_p.get(k) or {}).get("net_volume")}
    if opt_pos["foreign"]["long"] is None:
        notes.append("選擇權法人部位未取得")

    # ---------- 選擇權買賣權拆分 (日盤新端點＋夜盤；口數金額供完整版/力道表) ----------
    _dcp = (P.get("options-day-call-put") or {}).get("data") or {}
    _dcp_c = _by_inst(_dcp.get("call") or [])
    _dcp_p = _by_inst(_dcp.get("put") or [])
    _ncp = (P.get("options-after-hours") or {}).get("data") or {}
    _ncp_c = _by_inst(_ncp.get("call") or [])
    _ncp_p = _by_inst(_ncp.get("put") or [])
    opt_split = {}
    for sess, src in (("day", {"call": _dcp_c, "put": _dcp_p}),
                      ("night", {"call": _ncp_c, "put": _ncp_p})):
        for k in ("foreign", "investment_trust", "dealer"):
            c = (src["call"].get(k) or {})
            p = (src["put"].get(k) or {})
            opt_split[(sess, k)] = {
                "c_long": c.get("long_volume"), "c_short": c.get("short_volume"),
                "c_net": c.get("net_volume"),
                "c_lamt": c.get("long_amount"), "c_samt": c.get("short_amount"),
                "p_long": p.get("long_volume"), "p_short": p.get("short_volume"),
                "p_net": p.get("net_volume"),
                "p_lamt": p.get("long_amount"), "p_samt": p.get("short_amount")}
    if opt_split[("day", "foreign")]["c_net"] is None:
        unav.append("opt_split")
        notes.append("選擇權日盤買賣權拆分未取得")

    # ---------- 選擇權法人日夜盤交易 (同 期貨 5；夜盤為晨收已結算節) ----------
    opt_night_t = _by_inst(_rows(P["options-institutional-after-hours"]))
    opt_trade = {}
    for sess, src in (("day", oi_inst), ("night", opt_night_t)):
        for k in ("foreign", "investment_trust", "dealer"):
            r = src.get(k, {})
            opt_trade[(sess, k)] = {"long": r.get("long_volume"), "short": r.get("short_volume"),
                                    "net": r.get("net_volume")}
    if opt_trade[("day", "foreign")]["long"] is None:
        unav.append("opt_trade")
        notes.append("選擇權法人日夜盤交易未取得")

    # ---------- Walls ----------
    def _wall(v):
        return v if isinstance(v, dict) else {}
    walls = {"call": _wall(kl.get("call_wall")), "put": _wall(kl.get("put_wall")),
             "maxpain": _wall(kl.get("max_pain")), "expiry": prim_month}
    # ---------- Gamma (T0 缺時已遞補，g_date 為實際日期) ----------
    gdata = (P["options-gamma-levels"] or {}).get("data") or {}
    cdata = (P["options-market-structure-compact"] or {}).get("data") or {}
    cgamma = cdata.get("gamma") or {}
    wall = (gdata.get("gamma_wall") or {}).get("strike")
    flip = (gdata.get("gamma_flip") or {}).get("estimated_underlying")
    wall_src = "options-gamma-levels" if wall is not None else None
    flip_src = "options-gamma-levels" if flip is not None else None
    wall_date = g_date if wall is not None else None
    flip_date = g_date if flip is not None else None
    if wall is None and _gamma_proxy["wall"] is not None:
        wall = _gamma_proxy["wall"]
        wall_date = _gamma_proxy["wall_date"]
        wall_src = "options-market-structure-compact (proxy)"
    if flip is None and _gamma_proxy["flip"] is not None:
        flip = _gamma_proxy["flip"]
        flip_date = _gamma_proxy["flip_date"]
        flip_src = "options-market-structure-compact (proxy)"
    gsrc = " + ".join(dict.fromkeys(x for x in (wall_src, flip_src) if x)) or "TAIFEX Gamma endpoints"
    # Reconcile field-level availability only after primary + proxy resolution.
    # Primary endpoint failure is provenance, not final unavailability when proxy recovered values.
    unav, _gamma_notes = _gamma_status(
        unav, gamma_endpoint_unavailable, wall, flip, gsrc,
        gex_model_available=bool(g_pay is not None and gdata.get("levels")),
        flip_diagnostics=gdata.get("gamma_flip_diagnostics"),
        wide_range_flip=gdata.get("gamma_flip_wide_range"),
        wide_range_diagnostics=gdata.get("gamma_flip_wide_range_diagnostics"))
    notes.extend(_gamma_notes)
    _gex_levels = _valid_gex_levels(gdata.get("levels")) if g_pay is not None else []
    _net_gex = gdata.get("net_gex_1pct") if g_pay is not None else None
    _gross_gex = gdata.get("gross_gex_1pct") if g_pay is not None else None
    _gamma_expiry = _gamma_expiry_metadata(gdata if g_pay is not None else cgamma, prim_month)
    if _gamma_expiry["gex_expiry_matches_primary"] is False:
        notes.append(
            "Gamma GEX 實際使用到期月份 {}（到期日 {}）與 Options Key Levels 主到期月份 {} 不同；"
            "GEX 數值應以實際使用到期月份為準".format(
                _gamma_expiry["gex_contract_month"],
                _gamma_expiry["gex_expiry_date"] or "未提供",
                prim_month
            )
        )
    gamma = {"wall": wall, "flip": flip, **_gamma_expiry,
             "model": gdata.get("model") if g_pay is not None else None,
             "sign_convention_note": (
                 "Call 正／Put 負為模型假設；Aggregate OI 不揭露 Dealer 實際淨部位，"
                 "此值不可視為實際 Dealer GEX"
             ) if g_pay is not None else None,
             "quality": gdata.get("model_quality") if g_pay is not None else None,
             "underlying": gdata.get("underlying_price") if g_pay is not None else None,
             "net_gex_1pct": _net_gex, "gross_gex_1pct": _gross_gex,
             "levels": _gex_levels, "levels_count": len(_gex_levels),
             "diagnostics": gdata.get("gamma_diagnostics") if g_pay is not None else cgamma.get("gamma_diagnostics"),
             "flip_diagnostics": (gdata.get("gamma_flip_diagnostics") if g_pay is not None else None) or cgamma.get("gamma_flip_diagnostics"),
             "wide_range_flip_diagnostics": (gdata.get("gamma_flip_wide_range_diagnostics") if g_pay is not None else None) or cgamma.get("gamma_flip_wide_range_diagnostics"),
             "wide_range_flip": (gdata.get("gamma_flip_wide_range") if g_pay is not None else None) or cgamma.get("gamma_flip_wide_range"),
             "expiry_selection_diagnostics": (gdata.get("expiry_selection_diagnostics") if g_pay is not None else None) or cgamma.get("expiry_selection_diagnostics"),
             "delta_fetch_diagnostics": (cdata.get("data_quality") or {}).get("delta_fetch_diagnostics"),
             "gex_status": "available" if _gex_levels and _net_gex is not None and _gross_gex is not None else "unavailable",
             "date": gamma_date, "wall_date": wall_date, "flip_date": flip_date,
             "src": gsrc, "wall_src": wall_src, "flip_src": flip_src}
    if gamma["gex_status"] == "unavailable":
        notes.append("逐履約價 GEX／Net GEX／Gross GEX 未取得或資料不完整，標 unavailable（不以 Wall/Flip proxy 代替）")
    if gamma_date and gamma_date != t0:
        notes.append(f"Gamma Wall/Flip 資料日期 {gamma_date} (來源 {gsrc})")

    # ---------- 快照差值：嚴格核對前一交易日，選擇權按當日主力月份獨立比較 ----------
    _expected_snapshot_date = _previous_trading_day_iso(t0)
    _t1 = _expected_snapshot_date
    _sb = snapshot_bundle(_t1) if _t1 else None
    _sdate = (_sb or {}).get("date")
    _sd = (_sb or {}).get("data") or {}
    snapchg = {"date": _sdate, "expected_date": _expected_snapshot_date}
    _roll, _roll_old = _chain_rollover(
        _sd.get("chain", []),
        ((_sd.get("walls") or {}).get("primary_expiry") or {}).get("contract_month"),
        prim_month)

    if not _sdate:
        snapchg["chain"] = None
        snapchg["walls"] = None
        snapchg["chain_diagnostic"] = {"reason": "previous_snapshot_unavailable"}
        snapchg["walls_diagnostic"] = {"reason": "previous_snapshot_unavailable"}
        notes.append("選擇權 OI／Walls 前日比較 unavailable：前一日快照不存在或無法讀取")
    elif not _expected_snapshot_date:
        snapchg["chain"] = None
        snapchg["walls"] = None
        snapchg["chain_diagnostic"] = {"reason": "previous_trading_day_calendar_unavailable"}
        snapchg["walls_diagnostic"] = {"reason": "previous_trading_day_calendar_unavailable"}
        notes.append("選擇權 OI／Walls 前日比較 unavailable：無法可靠取得前一交易日（交易日曆不可用）")
    elif _sdate != _expected_snapshot_date:
        snapchg["chain"] = None
        snapchg["walls"] = None
        snapchg["chain_diagnostic"] = {
            "reason": "snapshot_date_mismatch", "expected_date": _expected_snapshot_date,
            "actual_date": _sdate}
        snapchg["walls_diagnostic"] = {
            "reason": "snapshot_date_mismatch", "expected_date": _expected_snapshot_date,
            "actual_date": _sdate}
        notes.append(
            "選擇權 OI／Walls 前日比較 unavailable：快照實際日期 {}，正確前一交易日應為 {}；"
            "不以跨日資料冒充日對日".format(_sdate, _expected_snapshot_date))
    else:
        _previous_chain = _sd.get("chain", [])
        if chain_date != t0:
            snapchg["chain"] = None
            snapchg["chain_diagnostic"] = {
                "reason": "current_chain_date_mismatch", "expected_date": t0,
                "actual_date": chain_date}
            notes.append(
                "選擇權 OI 前日變化 unavailable：本日 Chain 實際日期 {}，T0 應為 {}；"
                "不以遞補舊資料冒充當日資料".format(chain_date or "missing", t0))
        else:
            snapchg["chain_diagnostic"] = _options_chain_oi_change_diagnostic(
                chain, _previous_chain, prim_month)
            snapchg["chain"] = _options_chain_oi_change(chain, _previous_chain, prim_month)
            if snapchg["chain"] is not None:
                snapchg["chain"].update({
                    "snapshot_date": _sdate, "current_date": t0,
                    "source": "Cloudflare Worker KV snapshot bundle"})
            if snapchg["chain"] is None:
                _diag = snapchg["chain_diagnostic"]
                notes.append(
                    "選擇權 OI 前日變化 unavailable：reason={}; 主力={}; 本日/前日有效合約={}/{}; "
                    "本日/前日合約識別數={}/{}; 僅本日/僅前日有效合約={}/{}; "
                    "本日/前日 OI 缺值或無效={}/{}; 無效/重複識別={}/{}".format(
                        _diag["reason"], prim_month or "missing",
                        _diag["current_count"], _diag["previous_count"],
                        _diag["current_identity_count"], _diag["previous_identity_count"],
                        _diag["current_only"], _diag["previous_only"],
                        _diag["current_missing_oi"], _diag["previous_missing_oi"],
                        _diag["invalid_identity"], _diag["duplicate_identity"]))
            elif snapchg["chain"].get("partial"):
                _diag, _chg = snapchg["chain_diagnostic"], snapchg["chain"]
                notes.append(
                    "選擇權 OI 前日變化採共同有效合約計算：主力={}; 共同合約={}; "
                    "本日有效/識別合約={}/{}（覆蓋率 {:.1%}，OI 缺值/無效 {}）；"
                    "前日有效/識別合約={}/{}（覆蓋率 {:.1%}，OI 缺值/無效 {}）；"
                    "僅本日/僅前日有效合約={} / {}，未補零".format(
                        prim_month or "missing", _chg["matched_count"],
                        _chg["current_count"], _chg["current_identity_count"], _chg["current_coverage"],
                        _chg["current_missing_oi"], _chg["previous_count"],
                        _chg["previous_identity_count"], _chg["previous_coverage"],
                        _chg["previous_missing_oi"], _diag["current_only"], _diag["previous_only"]))

        if _roll is True:
            notes.append(
                "主力到期月份已由 {} 換至 {}；僅比較前後快照中相同主力月份的共同合約，不跨月份相減".format(
                    _roll_old, prim_month))
        elif _roll is None:
            notes.append(
                "前日快照主力月份無法確認（快照值：{}）；選擇權比較仍僅按當日主力月份及共同合約判定".format(
                    _roll_old or "缺失"))

        if chain_date != t0:
            snapchg["walls"] = None
            snapchg["walls_diagnostic"] = {
                "reason": "current_chain_date_mismatch", "expected_date": t0,
                "actual_date": chain_date}
        elif walls_date != t0:
            snapchg["walls"] = None
            snapchg["walls_diagnostic"] = {
                "reason": "current_key_levels_date_mismatch", "expected_date": t0,
                "actual_date": walls_date}
        else:
            _cur_levels = _options_chain_key_levels_for_month(chain, prim_month, prim.get("expiry"))
            if not _cur_levels.get("found"):
                snapchg["walls"] = None
                snapchg["walls_diagnostic"] = {
                    "reason": "current_chain_incomplete", "detail": _cur_levels.get("reason")}
            else:
                _prev_levels = _options_chain_key_levels_for_month(
                    _previous_chain, prim_month, _cur_levels["expiry_date"])
                _current_levels_match = (
                    walls.get("expiry") == prim_month
                    and (walls.get("call") or {}).get("strike") == _cur_levels["call_wall"]["strike"]
                    and (walls.get("put") or {}).get("strike") == _cur_levels["put_wall"]["strike"]
                    and (walls.get("maxpain") or {}).get("strike") == _cur_levels["max_pain"]["strike"])
                if not _current_levels_match:
                    snapchg["walls"] = None
                    snapchg["walls_diagnostic"] = {"reason": "current_key_levels_mismatch"}
                elif not _prev_levels.get("found"):
                    snapchg["walls"] = None
                    snapchg["walls_diagnostic"] = {
                        "reason": "previous_chain_incomplete", "detail": _prev_levels.get("reason")}
                else:
                    snapchg["walls"] = {
                        "call": _diff(_cur_levels["call_wall"]["strike"], _prev_levels["call_wall"]["strike"]),
                        "put": _diff(_cur_levels["put_wall"]["strike"], _prev_levels["put_wall"]["strike"]),
                        "maxpain": _diff(_cur_levels["max_pain"]["strike"], _prev_levels["max_pain"]["strike"]),
                        "expiry_date": _cur_levels["expiry_date"]}
                    snapchg["walls_diagnostic"] = {
                        "reason": "aligned", "contract_month": prim_month,
                        "expiry_date": _cur_levels["expiry_date"],
                        "current_rows": _cur_levels["chain_stats"]["rows"],
                        "previous_rows": _prev_levels["chain_stats"]["rows"]}
        if not snapchg["walls"]:
            _wd = snapchg["walls_diagnostic"]
            notes.append("選擇權 Call Wall／Put Wall／Max Pain 前日變化 unavailable：reason={}; detail={}".format(
                _wd.get("reason"), _wd.get("detail") or "n/a"))

    # 法人部位差值獨立於選擇權 Chain/Walls 換月；只要求前一交易日快照可信。
    if _sdate == _expected_snapshot_date and (_sb or {}).get("trust_pos") is True:
        _sfd = {x.get("institution"): x for x in _sd.get("fut_trade_day", [])} if (_sb or {}).get("trust_pos") else {}
        _sod = {x.get("institution"): x for x in _sd.get("opt_pos_day", [])} if (_sb or {}).get("trust_pos") else {}
        _pos = {}
        for _k in ("foreign", "dealer"):
            _cf = (fut_trade.get(("day", _k)) or {}).get("net")
            _sf = (_sfd.get(_k) or {}).get("net_volume")
            _co = (opt_pos.get(_k) or {}).get("net")
            _so = (_sod.get(_k) or {}).get("net_volume")
            _pos[_k] = {"fut_chg": _diff(_cf, _sf), "opt_chg": _diff(_co, _so)}
        snapchg["pos"] = _pos

    return {"day": day, "night": night, "fut_oi": fut_oi, "fut_trade": fut_trade,
            "basis": basis, "basis_pct": basis_pct, "oi_chg": oi_chg,
            "opt_tot": opt_tot, "opt_conc": opt_conc, "opt_dist": opt_dist, "opt_pos": opt_pos,
            "opt_trade": opt_trade, "opt_split": opt_split, "walls": walls,
            "gamma": gamma, "trade_date": t0, "opt_expiry": prim_month, "snapchg": snapchg,
            "unavailable": unav, "notes": notes}


def _chain_rollover(snap_rows, snap_walls_primary, cur_primary):
    """快照主力到期 vs 當前主力到期是否換月。

    只有快照明確記錄舊主力到期月份時才判斷；缺少舊／新主力月份時回傳 None，
    不從可能不完整的 chain OI 分布推估主力月份。
    回傳 (True=已換月, False=未換月, None=未知；舊主力月份)。
    """
    old = snap_walls_primary
    if not old or not cur_primary:
        return None, old
    return old != cur_primary, old


def _iso8(v: str | None) -> str | None:
    """yyyymmdd / yyyy-mm-dd → yyyy-mm-dd；無法解析回 None。"""
    s = str(v or "").strip().replace("-", "")
    if len(s) == 8 and s.isdigit():
        return f"{s[:4]}-{s[4:6]}-{s[6:8]}"
    s2 = str(v or "").strip()
    if len(s2) == 10 and s2[4] == "-" and s2[7] == "-":
        return s2
    return None


def snap_top10_change(month: str, t0: str, cur_net, cur_date: str | None = None,
                      dataset: str = "top10fut", callput: str | None = None) -> dict | None:
    """前十大淨變化 (Worker T0 快照；Top10 內容日期 T-1)。dataset: top10fut (期貨) / top10opt (選擇權，需 callput)。
    上游 OpenAPI 落後約一日 (最新 = T-1)，取指定契約月份最新內容日期；
    若快照只有其他契約月份，回傳換月基準重建狀態；不跨月份、不將缺值補零。
    快照不存在、指定買賣方資料不存在或數值不完整時回傳 None。
    同月份有效比較回傳 {chg, status=available, prev_date, cur_date, snap_date}；
    前快照只有其他契約月份時回傳 status=rollover_baseline_reset，不跨月相減；
    快照不存在或資料無法驗證時回傳 None。"""
    import math

    # Worker 每個交易日收盤後寫入當日 KV 快照；TAIFEX Top10 OpenAPI 內容落後
    # Worker 收集日一個交易日。因此 T0 報告應讀取 snapshot:T0，並驗證內容日期為 T-1。
    _snapshot_date = str(t0 or "").strip()
    _expected_content_date = _previous_trading_day_iso(_snapshot_date)
    if not _snapshot_date or not _expected_content_date:
        return None
    _sb = snapshot_bundle(_snapshot_date)
    if not isinstance(_sb, dict):
        return None

    # Top10 自身以 Worker key 日期及 OpenAPI 內容日期驗證；
    # trust_pos 僅代表無日期法人部位是否可信，不應阻擋有日期可驗證的 Top10。
    if _sb.get("date") != _snapshot_date:
        print(
            f"[WARN] top10 snapshot rejected: requested={_snapshot_date} "
            f"returned={_sb.get('date')}"
        )
        return None

    _snapshot_data = _sb.get("data")
    if not isinstance(_snapshot_data, dict):
        return None
    _raw_rows = _snapshot_data.get(dataset)
    if not isinstance(_raw_rows, list) or not _raw_rows:
        return None
    rows = [r for r in _raw_rows if isinstance(r, dict)]
    if len(rows) != len(_raw_rows) or not rows:
        return None

    # The TAIFEX top10 endpoint is one trading day behind the Worker
    # collection date. Require that exact source date; a consistently stale
    # payload must not be accepted as a valid rollover baseline.
    _row_dates = [_iso8(r.get("Date")) for r in rows]
    if any(d is None for d in _row_dates) or set(_row_dates) != {_expected_content_date}:
        return None

    if callput:
        rows = [r for r in rows if str(r.get("CallPut", "")) == str(callput)]
    month_rows = rows
    if month:
        rows = [r for r in month_rows if str(r.get("SettlementMonth", "")) == str(month)]
    if not rows and month and month_rows and cur_net is not None:
        # A rollover is valid only when the current contract month is strictly
        # later than the latest contract month in the trusted prior snapshot.
        # Reverse or malformed month relationships are unavailable, not rollover.
        # SettlementMonth may contain TAIFEX sentinel/non-delivery codes
        # (for example 666666 or 999912). Only real YYYYMM calendar months
        # may establish a rollover baseline; never infer from row ordering.
        def _valid_contract_month(value):
            value = str(value or "").strip()
            if len(value) != 6 or not value.isdigit():
                return False
            year, month_num = int(value[:4]), int(value[4:])
            return 2000 <= year <= 2100 and 1 <= month_num <= 12

        current_month = str(month).strip()
        if not _valid_contract_month(current_month):
            return None
        prior_rows = [
            row for row in month_rows
            if _valid_contract_month(row.get("SettlementMonth"))
        ]
        if not prior_rows:
            return None
        prior_month = max(
            str(row.get("SettlementMonth")).strip() for row in prior_rows
        )
        prior = next(
            row for row in prior_rows
            if str(row.get("SettlementMonth")).strip() == prior_month
        )
        if int(current_month) <= int(prior_month):
            return None
        return {
            "chg": None,
            "status": "rollover_baseline_reset",
            "reason": "前一交易日快照只有舊契約月份，無新主力月份可比基準；換月建立新基準，不跨月相減",
            "prev_month": prior_month,
            "current_month": current_month,
            "prev_date": _iso8(prior.get("Date")),
            "cur_date": _iso8(cur_date) or t0,
            "snap_date": _sb.get("date"),
        }
    if not rows or cur_net is None:
        return None
    rows.sort(key=lambda r: str(r.get("Date", "")))
    r0 = rows[-1]
    prev_date = _iso8(r0.get("Date"))
    if prev_date is None:
        return None

    def _valid_number(value):
        if value is None or value == "" or isinstance(value, bool):
            return None
        try:
            number = float(str(value).replace(",", ""))
        except (ValueError, TypeError):
            return None
        return number if math.isfinite(number) else None

    prev_buy = _valid_number(r0.get("Top10Buy"))
    prev_sell = _valid_number(r0.get("Top10Sell"))
    current_net = _valid_number(cur_net)
    if prev_buy is None or prev_sell is None or current_net is None:
        return None
    prev = prev_buy - prev_sell
    return {"chg": current_net - prev, "status": "available", "prev_date": prev_date,
            "cur_date": _iso8(cur_date) or t0, "snap_date": _sb["date"],
            "prev_month": str(month) if month else None, "current_month": str(month) if month else None}


def _pct(v):
    try:
        return float(v) if v is not None else None
    except (ValueError, TypeError):
        return None

def _diff(a, b):
    return a - b if a is not None and b is not None else None

def _yi(v):
    """千元 → 億元。"""
    try:
        return float(v) / 1e5 if v is not None else None
    except (ValueError, TypeError):
        return None
