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
            "options-gamma-levels", "options-key-levels", "options-market-structure-compact"}
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

# F1（2026-10-19）：快照 bundle memoize。build() 與 snap_top10_change() 取的是同一份
# T-1 快照（報表多處引用），同一進程內重複請求同一 (proxy, date) 只快取成功結果；
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
    detail = payload.get("detail") or data.get("detail") or data.get("reason")
    return {
        "error_code": payload.get("error_code"),
        "stage": payload.get("stage"),
        "error": payload.get("error"),
        "detail": str(detail)[:400] if detail is not None else None,
        "data_reason": str(data.get("reason"))[:400] if data.get("reason") is not None else None,
    }


def _get(ep: str, t0: str, timeout: int = 40) -> dict | None:
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
            # F3-a（2026-10-19）：退避只留給真的會自己好的狀況（限流 429／上游忙碌 503／
            # read timeout）；502 上游閘道錯誤直接重試，不再每次固定睡 3 秒。
            # 重試次數（2 次）與「失敗即 None」的語意完全不變。
            if r.status_code in (429, 503):
                print(f"[INFO] taifex {ep} HTTP {r.status_code} (try {attempt + 1})，退避 3 秒後重試",
                      file=sys.stderr, flush=True)
                time.sleep(3)
                continue
            if r.status_code == 502:
                print(f"[INFO] taifex {ep} HTTP 502 (try {attempt + 1})，直接重試", file=sys.stderr, flush=True)
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


def _gamma_status(unavailable: list[str], endpoint_unavailable: bool,
                  wall, flip, source: str) -> tuple[list[str], list[str]]:
    """Resolve Gamma availability and provenance notes after primary/proxy fallback."""
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
            notes.append(f"{label} 無資料（原始端點與 Proxy 備援皆未取得），標 unavailable")
    return result, notes


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
    """Calculate daily OI deltas only when both primary-expiry chains align completely."""
    import math

    if not primary_month or not isinstance(current_chain, list) or not isinstance(previous_chain, list):
        return None

    def _index(rows):
        indexed = {}
        for row in rows:
            if not isinstance(row, dict) or row.get("contract_month") != primary_month:
                continue
            identity = (row.get("contract_month"), row.get("contract_expiry_date"),
                        row.get("strike"), row.get("type"))
            if any(value is None for value in identity):
                return None
            if identity in indexed:
                return None
            oi = row.get("open_interest")
            if isinstance(oi, bool) or not isinstance(oi, (int, float)):
                return None
            if not math.isfinite(float(oi)) or oi < 0:
                return None
            indexed[identity] = oi
        return indexed

    current = _index(current_chain)
    previous = _index(previous_chain)
    if not current or not previous or current.keys() != previous.keys():
        return None

    moves = []
    for key, oi in current.items():
        kind = key[3]
        if kind not in ("call", "put"):
            return None
        moves.append({"strike": key[2], "type": kind, "d_oi": oi - previous[key]})

    calls = sorted((move for move in moves if move["type"] == "call"),
                   key=lambda move: move["d_oi"], reverse=True)
    puts = sorted((move for move in moves if move["type"] == "put"),
                  key=lambda move: move["d_oi"], reverse=True)
    return {
        "c_chg": sum(move["d_oi"] for move in calls),
        "p_chg": sum(move["d_oi"] for move in puts),
        "c_up": calls[0] if calls and calls[0]["d_oi"] > 0 else None,
        "c_dn": calls[-1] if calls and calls[-1]["d_oi"] < 0 else None,
        "p_up": puts[0] if puts and puts[0]["d_oi"] > 0 else None,
        "p_dn": puts[-1] if puts and puts[-1]["d_oi"] < 0 else None,
    }


def _options_chain_oi_change_diagnostic(current_chain, previous_chain, primary_month: str) -> dict:
    """Explain why primary-expiry OI deltas cannot be calculated; never infer zero OI."""
    import math
    result = {"primary_month": primary_month, "current_count": 0, "previous_count": 0,
              "current_only": 0, "previous_only": 0, "current_missing_oi": 0,
              "previous_missing_oi": 0, "invalid_identity": 0, "duplicate_identity": 0, "reason": None}
    if not primary_month:
        result["reason"] = "primary_expiry_missing"
        return result
    if not isinstance(current_chain, list) or not isinstance(previous_chain, list):
        result["reason"] = "chain_payload_missing"
        return result
    def index(rows, side):
        out = {}
        for row in rows:
            if not isinstance(row, dict) or row.get("contract_month") != primary_month:
                continue
            key = (row.get("contract_month"), row.get("contract_expiry_date"), row.get("strike"), row.get("type"))
            if any(value is None for value in key):
                result["invalid_identity"] += 1
                continue
            if key in out:
                result["duplicate_identity"] += 1
                continue
            oi = row.get("open_interest")
            if isinstance(oi, bool) or not isinstance(oi, (int, float)) or not math.isfinite(float(oi)) or oi < 0:
                result[side + "_missing_oi"] += 1
                continue
            out[key] = oi
        result[side + "_count"] = len(out)
        return out
    current = index(current_chain, "current")
    previous = index(previous_chain, "previous")
    result["current_only"] = len(current.keys() - previous.keys())
    result["previous_only"] = len(previous.keys() - current.keys())
    if result["invalid_identity"]: reason = "invalid_contract_identity"
    elif result["duplicate_identity"]: reason = "duplicate_contract_identity"
    elif result["current_missing_oi"] or result["previous_missing_oi"]: reason = "open_interest_missing_or_invalid"
    elif not current or not previous: reason = "primary_expiry_chain_empty"
    elif result["current_only"] or result["previous_only"]: reason = "contract_set_mismatch"
    else: reason = "aligned"
    result["reason"] = reason
    return result

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
    if month:
        try:
            r = requests.get(f"{base}/futures-night-ohlc", params={"date": query_date, "month": month},
                             headers={**HEADERS, "accept": "application/json"}, timeout=30)
            if r.status_code == 200:
                j = r.json()
                if isinstance(j, dict) and j.get("ok") is True and isinstance(j.get("data"), dict):
                    d = j["data"]
                    if d.get("close") is not None and (j.get("date") or "") == query_date:
                        return {"open": d.get("open"), "high": d.get("high"), "low": d.get("low"),
                                "close": d.get("close"), "change": d.get("change"),
                                "pct": _pct(d.get("change_percent")),
                                "volume": d.get("volume"),
                                "via": "proxy", "date": query_date,
                                "qdate": query_date}
                    print(f"[INFO] proxy night-ohlc 回退 (查 {query_date} 得 {j.get('date')})，改官方備援")
        except Exception as e:  # noqa: BLE001
            print(f"[INFO] proxy night-ohlc 不可用，改官方備援：{e}")
    try:
        from src.sources import taifex_official as _off
        rows = [x for x in _off._get("/DailyMarketReportFut")
                if x.get("Contract") == "TX" and x.get("TradingSession") == "盤後"
                and x.get("ContractMonth(Week)") == month
                and _off._iso(x.get("Date", "")) == query_date]
        if not rows:
            return None
        rows.sort(key=lambda x: x.get("Date", ""), reverse=True)
        r0 = rows[0]
        def _n(v):
            try:
                return float(str(v).replace(",", "")) if v not in (None, "", "-", "NULL") else None
            except (ValueError, TypeError):
                return None
        chg, close = _n(r0.get("Change")), _n(r0.get("Last"))
        return {"open": _n(r0.get("Open")), "high": _n(r0.get("High")), "low": _n(r0.get("Low")),
                "close": close, "change": chg,
                "pct": (chg / (close - chg) * 100) if chg is not None and close else None,
                "via": "official", "date": _off._iso(r0.get("Date", "")),
                "qdate": query_date}
    except Exception as e:  # noqa: BLE001
        print(f"[INFO] official night-ohlc 不可用：{e}")
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
    unav: list[str] = []
    notes: list[str] = []
    _content = dateless_content_date()
    if _content != t0:
        notes.append(f"無日期端點為最新盤勢快照 (判定資料日期 {_content}，非 T0 {t0})，"
                     "適用：日盤價／法人交易／夜盤／選擇權法人；T0 相符時不另標註")
    P = {ep: _get(ep, t0) for ep in list(FREE_EPS) + sorted(DATE_EPS - {"options-gamma-levels", "options-market-structure-compact", "futures-options-chain"})}
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
    _p = _get("options-gamma-levels", t0)
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
    # Market-structure-compact 仍保留 T-1/T-2 遞補（Gamma Wall proxy 來源）
    c_pay, c_date = None, None
    for _d in _prev_dates(t0, 2):
        if c_pay is None:
            _p = _get("options-market-structure-compact", _d)
            _cg = (((_p or {}).get("data") or {}).get("gamma") or {})
            _w = _cg.get("gamma_wall_proxy")
            _f = _cg.get("gamma_flip_proxy")
            if _w is not None or _f is not None:
                c_pay, c_date = _p, _d
        if c_pay is not None:
            break
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
                _p = _get("options-key-levels", _d, timeout=90)
                if (((_p or {}).get("data") or {}).get("call_wall") or {}).get("strike") is not None:
                    kl_pay, kl_date = _p, _d
            if cp_pay is None:
                _p = P["options-market-structure-compact"] if _d == t0 else _get("options-market-structure-compact", _d, timeout=90)
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
    hist = (_get("futures-institutional-oi-history", t0) or {}).get("data") or []
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
    notes.append("法人交易量變化無昨日交易端點，標 unavailable")

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
        _p = _get("futures-options-chain", _d, timeout=90)
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
    if wall is None and cgamma.get("gamma_wall_proxy") is not None:
        wall, wall_src = cgamma.get("gamma_wall_proxy"), "options-market-structure-compact (proxy)"
    if flip is None and cgamma.get("gamma_flip_proxy") is not None:
        flip, flip_src = cgamma.get("gamma_flip_proxy"), "options-market-structure-compact (proxy)"
    gsrc = " + ".join(dict.fromkeys(x for x in (wall_src, flip_src) if x)) or "TAIFEX Gamma endpoints"
    # Reconcile field-level availability only after primary + proxy resolution.
    # Primary endpoint failure is provenance, not final unavailability when proxy recovered values.
    unav, _gamma_notes = _gamma_status(unav, gamma_endpoint_unavailable, wall, flip, gsrc)
    notes.extend(_gamma_notes)
    _gex_levels = _valid_gex_levels(gdata.get("levels")) if g_pay is not None else []
    _net_gex = gdata.get("net_gex_1pct") if g_pay is not None else None
    _gross_gex = gdata.get("gross_gex_1pct") if g_pay is not None else None
    gamma = {"wall": wall, "flip": flip,
             "model": gdata.get("model") if g_pay is not None else None,
             "quality": gdata.get("model_quality") if g_pay is not None else None,
             "underlying": gdata.get("underlying_price") if g_pay is not None else None,
             "net_gex_1pct": _net_gex, "gross_gex_1pct": _gross_gex,
             "levels": _gex_levels, "levels_count": len(_gex_levels),
             "diagnostics": gdata.get("gamma_diagnostics") if g_pay is not None else None,
             "gex_status": "available" if _gex_levels and _net_gex is not None and _gross_gex is not None else "unavailable",
             "date": gamma_date, "src": gsrc, "wall_src": wall_src, "flip_src": flip_src}
    if gamma["gex_status"] == "unavailable":
        notes.append("逐履約價 GEX／Net GEX／Gross GEX 未取得或資料不完整，標 unavailable（不以 Wall/Flip proxy 代替）")
    if gamma_date and gamma_date != t0:
        notes.append(f"Gamma Wall/Flip 資料日期 {gamma_date} (來源 {gsrc})")

    # ---------- 快照差值 (V1.4+；無快照則維持 unavailable) ----------
    from datetime import date as _dd, timedelta as _td
    _t1 = (_dd.fromisoformat(t0) - _td(days=1)).isoformat()
    _sb = snapshot_bundle(_t1)
    _sdate = (_sb or {}).get("date")
    _sd = (_sb or {}).get("data") or {}
    snapchg = {"date": _sdate}
    if not _sdate:
        snapchg["chain_diagnostic"] = {"reason": "previous_snapshot_unavailable"}
        notes.append("選擇權 OI 日對日變化 unavailable：前一日快照不存在或無法讀取（previous_snapshot_unavailable）")
    # C2 跨到期換月檢查：快照主力到期 vs 當前主力到期不同 → 日對日差值無意義
    # （實證：10-14 快照主力 202610W2，當前 202610F3；舊寫法會拿 F3 今值減 W2 舊值）。
    # 注意：不能只比到期集合是否相交（兩邊常同時含新舊合約），必須比主力。
    _roll, _roll_old = _chain_rollover(
        _sd.get("chain", []),
        ((_sd.get("walls") or {}).get("primary_expiry") or {}).get("contract_month"),
        prim_month)
    if _sdate and _roll is True:
        snapchg["chain"] = None
        snapchg["walls"] = None
        notes.append(f"跨到期換月（舊{_roll_old}→新{prim_month}），日對日 OI/Walls 變化不適用")
    elif _sdate and _roll is None:
        snapchg["chain"] = None
        snapchg["walls"] = None
        notes.append(f"前一日主力到期月份無法確認（快照值：{_roll_old or '缺失'}），日對日 OI/Walls 變化 unavailable")
    elif _sdate and _roll is False:
        # 只有前後日主力到期合約集合完整一致，且每筆 OI 都有效，才計算日對日差值。
        _previous_chain = _sd.get("chain", [])
        snapchg["chain_diagnostic"] = _options_chain_oi_change_diagnostic(chain, _previous_chain, prim_month)
        snapchg["chain"] = _options_chain_oi_change(chain, _previous_chain, prim_month)
        if snapchg["chain"] is None:
            _diag = snapchg["chain_diagnostic"]
            notes.append("選擇權 OI 日對日變化 unavailable：reason={}; 主力={}; 本日/前日有效合約={}/{}; 僅本日/僅前日={}/{}; 本日/前日 OI 缺值={}/{}; 無效/重複識別={}/{}".format(
                _diag["reason"], prim_month or "missing", _diag["current_count"], _diag["previous_count"],
                _diag["current_only"], _diag["previous_only"], _diag["current_missing_oi"],
                _diag["previous_missing_oi"], _diag["invalid_identity"], _diag["duplicate_identity"]))
        # 部位：日盤淨差值 (僅快照當日收集才可信)
        _sfd = {x.get("institution"): x for x in _sd.get("fut_trade_day", [])} \
            if (_sb or {}).get("trust_pos") else {}
        _sod = {x.get("institution"): x for x in _sd.get("opt_pos_day", [])} \
            if (_sb or {}).get("trust_pos") else {}
        _pos = {}
        for _k in ("foreign", "dealer"):
            _cf = (fut_trade.get(("day", _k)) or {}).get("net")
            _sf = (_sfd.get(_k) or {}).get("net_volume")
            _co = (opt_pos.get(_k) or {}).get("net")
            _so = (_sod.get(_k) or {}).get("net_volume")
            _pos[_k] = {"fut_chg": _diff(_cf, _sf), "opt_chg": _diff(_co, _so)}
        snapchg["pos"] = _pos
        _sw = _sd.get("walls") or {}
        snapchg["walls"] = {
            "call": _diff((walls["call"] or {}).get("strike"), (_sw.get("call_wall") or {}).get("strike")),
            "put": _diff((walls["put"] or {}).get("strike"), (_sw.get("put_wall") or {}).get("strike")),
            "maxpain": _diff((walls["maxpain"] or {}).get("strike"), (_sw.get("max_pain") or {}).get("strike"))}

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
    """前十大淨變化 (快照 T-1)。dataset: top10fut (期貨) / top10opt (選擇權，需 callput)。
    上游 OpenAPI 落後約一日 (最新 = T-1)，取指定契約月份最新內容日期；
    指定月份或買賣方資料不完整時回傳 None，不跨月份、不將缺值補零。
    回傳 {chg, prev_date, cur_date, snap_date} 或 None。"""
    import math
    from datetime import date as _dd, timedelta as _td

    _t1 = (_dd.fromisoformat(t0) - _td(days=1)).isoformat()
    _sb = snapshot_bundle(_t1)
    if not _sb:
        return None
    rows = [r for r in (_sb["data"].get(dataset) or []) if isinstance(r, dict)]
    if callput:
        rows = [r for r in rows if str(r.get("CallPut", "")) == str(callput)]
    if month:
        rows = [r for r in rows if str(r.get("SettlementMonth", "")) == str(month)]
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
    return {"chg": current_net - prev, "prev_date": prev_date,
            "cur_date": _iso8(cur_date) or t0, "snap_date": _sb["date"]}


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
