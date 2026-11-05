"""現貨 raw 採集：TWSE OpenAPI + TPEX OpenAPI 直連 (twse-proxy 以外的欄位)。

端點 (皆免 Key)：
- twtazu_od      上市漲跌家數 (整體市場/股票兩列)
- MI_MARGN       上市融資融券 (逐股加總，無日期欄，視為最新)
- TWT96U         借券可借餘額 (TWSEAvailableVolume=上市, GRETAI=上櫃)
- FMTQIK         上市成交 (依 Date=ROC日期 取列)
- tpex_mainborad_highlight  上櫃成交+漲跌 (單列，須驗 Date)
- tpex_mainboard_margin_balance  上櫃融資融券 (依 Date 過濾加總)
- tpex_margin_sbl  上櫃借券 (依 Date 過濾加總)
- 三大法人金額沿用 twse.get_institutional (RWD BFI82U，單位億元)
"""
from __future__ import annotations
import requests
from src.utils import HEADERS

TWSE_API = "https://openapi.twse.com.tw/v1"
TPEX_API = "https://www.tpex.org.tw/openapi/v1"

def _num(v):
    if v is None:
        return None
    s = str(v).replace(",", "").replace("%", "").replace("－", "-").replace("—", "-").strip()
    if s in {"", "--", "---", "N/A", "null", "None", "除息", "-"}:
        return None
    try:
        return float(s)
    except ValueError:
        return None

def _get_json(url: str, timeout: int = 40):
    try:
        r = requests.get(url, headers={**HEADERS, "accept": "application/json"}, timeout=timeout)
        r.raise_for_status()
        return r.json()
    except Exception as e:  # noqa: BLE001
        print(f"[WARN] raw fetch failed {url}: {e}")
        return None

def roc8(iso_date: str) -> str:
    """2026-09-15 -> 1150915。"""
    y, m, d = iso_date.split("-")
    return f"{int(y) - 1911}{m}{d}"

# ---------- 上市漲跌 (備援 twse-proxy) ----------

def listed_breadth_raw(date8: str) -> dict:
    out = {"up": None, "down": None, "flat": None, "limit_up": None, "limit_down": None, "date_ok": False}
    j = _get_json(f"{TWSE_API}/exchangeReport/twtazu_od?date={date8}")
    if not isinstance(j, list):
        return out
    for row in j:
        if row.get("類型") == "股票":
            out = {"up": _num(row.get("上漲")), "down": _num(row.get("下跌")),
                   "flat": _num(row.get("持平")), "limit_up": _num(row.get("漲停")),
                   "limit_down": _num(row.get("跌停")),
                   "date_ok": _roc(row.get("出表日期", "")) == _roc8_from_date8(date8)}
    return out

def _roc(s: str) -> str:
    s = str(s).strip()
    if len(s) == 7 and s[:3].isdigit():
        return f"{int(s[:3]) + 1911:04d}{s[3:]}"
    return s.replace("-", "")

def _roc8_from_date8(date8: str) -> str:
    return f"{int(date8[:4]) - 1911}{date8[4:]}" if len(date8) == 8 else date8

# ---------- 上市融資融券 ----------

def margin_tw() -> dict:
    """合計單位：張。增減 = 買進-賣出。"""
    j = _get_json(f"{TWSE_API}/exchangeReport/MI_MARGN")
    out = {"bal": None, "chg": None, "sbal": None, "schg": None}
    if not isinstance(j, list):
        return out
    bal = chg_b = chg_s = sbal = sb_b = sb_s = 0.0
    has = False
    for row in j:
        b = _num(row.get("融資今日餘額"))
        if b is None:
            continue
        has = True
        bal += b
        bb, ss = _num(row.get("融資買進")), _num(row.get("融資賣出"))
        chg_b += bb or 0.0
        chg_s += ss or 0.0
        sb = _num(row.get("融券今日餘額")) or 0.0
        sbal += sb
        sb_b += _num(row.get("融券買進")) or 0.0
        sb_s += _num(row.get("融券賣出")) or 0.0
    if has:
        out = {"bal": bal, "chg": chg_b - chg_s, "sbal": sbal, "schg": sb_s - sb_b}
    return out

# ---------- 借券 ----------

def sbl_tw() -> dict:
    """TWT96U 可借餘額加總。單位：股數 (API 原值)。"""
    j = _get_json(f"{TWSE_API}/SBL/TWT96U")
    out = {"tw": None, "otc": None}
    if not isinstance(j, list):
        return out
    tw = otc = 0.0
    has = False
    for row in j:
        a, b = _num(row.get("TWSEAvailableVolume")), _num(row.get("GRETAIAvailableVolume"))
        if a is not None or b is not None:
            has = True
            tw += a or 0.0
            otc += b or 0.0
    if has:
        out = {"tw": tw, "otc": otc}
    return out


def _twse_date8(date_value: str) -> str | None:
    """Normalize an ISO (YYYY-MM-DD), AD (YYYYMMDD), or ROC (YYYMMDD) date to YYYYMMDD."""
    value = str(date_value or "").strip().replace("-", "").replace("/", "")
    if len(value) == 8 and value.isdigit():
        return value
    if len(value) == 7 and value.isdigit():
        return f"{int(value[:3]) + 1911:04d}{value[3:]}"
    return None



def _borrowed_short_field_pair(fields):
    """Resolve previous/current borrowed-short balances from unique or grouped labels."""
    names = [str(name).strip().replace(" ", "") for name in fields]
    prev_unique = ("借券賣出前日餘額", "前日借券賣出餘額股數", "借券前日餘額")
    curr_unique = ("借券賣出當日餘額", "本日借券賣出餘額股數", "借券當日餘額")
    prev_idx = next((names.index(name) for name in prev_unique if name in names), None)
    curr_idx = next((names.index(name) for name in curr_unique if name in names), None)
    if prev_idx is not None and curr_idx is not None and prev_idx != curr_idx:
        return prev_idx, curr_idx

    prev_candidates = [i for i, name in enumerate(names) if name == "前日餘額"]
    curr_candidates = [i for i, name in enumerate(names) if name == "當日餘額"]
    marker_names = {"當日還券", "當日調整", "當日調整數額", "借券賣出當日還券", "借券賣出當日調整數額"}
    marker_indices = [i for i, name in enumerate(names) if name in marker_names]
    pairs = [
        (p, q) for p in prev_candidates for q in curr_candidates
        if p < q and any(p < marker < q for marker in marker_indices)
    ]
    if not pairs:
        return None, None
    # The borrowed-short section follows the margin section; the pair that
    # encloses the SBL return/adjustment columns is the intended pair.
    return max(pairs, key=lambda pair: (pair[0], pair[1]))


def twse_twt93u_sbl(date_value: str) -> dict:
    """TWT93U 上市借券賣出餘額與當日增減；依 API fields 欄名定位，不使用固定欄位索引。

    回傳 {sale_bal, sale_chg, prev_bal, date_ok}。單位：股數 (API 原值)。
    """
    date8 = _twse_date8(date_value)
    out = {"sale_bal": None, "sale_chg": None, "prev_bal": None, "date_ok": False}
    if date8 is None:
        print(f"[WARN] TWT93U invalid requested date: {date_value!r}")
        return out
    url = f"https://www.twse.com.tw/rwd/zh/marginTrading/TWT93U?response=json&date={date8}"
    j = _get_json(url)
    if not isinstance(j, dict):
        print(f"[WARN] TWT93U invalid response type: {type(j).__name__}")
        return out
    if j.get("stat") != "OK":
        print(f"[WARN] TWT93U stat not OK: {j.get('stat')!r}; date={date8}")
        return out

    actual_date = _twse_date8(j.get("date"))
    if actual_date != date8:
        print(f"[WARN] TWT93U date mismatch: requested={date8} actual={j.get('date')!r}")
        return out
    fields = j.get("fields") or []
    data = j.get("data") or []
    if not fields or not data:
        print(f"[WARN] TWT93U missing fields/data: date={date8}")
        return out

    # API field labels vary slightly between display versions; only accept explicit
    # semantic labels. Never fall back to positional indices.
    normalized = {str(name).strip().replace(" ", ""): i for i, name in enumerate(fields)}
    symbol_idx = next((normalized[name] for name in ("證券代號", "股票代號", "代號") if name in normalized), None)
    name_idx = normalized.get("名稱")
    prev_idx, bal_idx = _borrowed_short_field_pair(fields)
    sell_idx = next((normalized[k] for k in ("當日賣出", "借券賣出當日賣出") if k in normalized), None)
    return_idx = next((normalized[k] for k in ("當日還券", "借券賣出當日還券") if k in normalized), None)
    adjust_idx = next((normalized[k] for k in ("當日調整", "當日調整數額", "借券賣出當日調整") if k in normalized), None)
    if symbol_idx is None or prev_idx is None or bal_idx is None or sell_idx is None or return_idx is None or adjust_idx is None:
        print(f"[WARN] TWT93U required lending fields absent: fields={fields!r}")
        return out

    # Use the official final "合計" row only. Individual securities are detail rows
    # and must never be summed together with (or instead of) the market aggregate.
    total_row = next((
        row for row in reversed(data)
        if isinstance(row, (list, tuple))
        and max(symbol_idx, prev_idx, sell_idx, return_idx, adjust_idx, bal_idx) < len(row)
        and (
            str(row[symbol_idx] or "").strip() == "合計"
            or (name_idx is not None and str(row[name_idx] or "").strip() == "合計")
        )
    ), None)
    if total_row is None:
        print(f"[WARN] TWT93U official 合計 row absent: date={date8}")
        return out

    prev = _num(total_row[prev_idx])
    sold = _num(total_row[sell_idx])
    returned = _num(total_row[return_idx])
    adjusted = _num(total_row[adjust_idx])
    bal = _num(total_row[bal_idx])
    if any(value is None for value in (prev, sold, returned, adjusted, bal)):
        print(f"[WARN] TWT93U official 合計 row contains invalid values: date={date8} row={total_row!r}")
        return out
    if abs((prev + sold - returned + adjusted) - bal) > 1e-6:
        print(f"[WARN] TWT93U official 合計 row roll-forward mismatch: date={date8}")
        return out

    print(f"[INFO] TWT93U official 合計 row accepted date={date8}")
    return {
        "sale_bal": bal,
        "sale_chg": bal - prev,
        "prev_bal": prev,
        "date_ok": True,
    }

def twse_twt72u_sbl(date_value: str) -> dict:
    """TWT72U（SLBNLB）借券餘額；直接採用「整體市場」合計列。"""
    date8 = _twse_date8(date_value)
    out = {"bal": None, "prev_bal": None, "chg": None, "date_ok": False}
    if date8 is None:
        print(f"[WARN] TWT72U invalid requested date: {date_value!r}")
        return out
    url = (
        "https://www.twse.com.tw/rwd/zh/lending/TWT72U"
        f"?response=json&date={date8}"
    )
    j = _get_json(url)
    if not isinstance(j, dict) or j.get("stat") != "OK":
        print(f"[WARN] TWT72U stat/type not OK: {j.get('stat') if isinstance(j, dict) else type(j).__name__!r}")
        return out

    actual_date = _twse_date8(j.get("date"))
    if actual_date != date8:
        print(f"[WARN] TWT72U date mismatch: requested={date8} actual={j.get('date')!r}")
        return out
    fields = j.get("fields") or []
    data = j.get("data") or []
    normalized = {str(name).strip().replace(" ", ""): i for i, name in enumerate(fields)}
    symbol_idx = next((normalized[k] for k in ("證券代號", "股票代號", "代號") if k in normalized), None)
    prev_idx = next((normalized[k] for k in ("前日借券餘額(1)股", "昨日借券餘額(股數)") if k in normalized), None)
    borrow_idx = next((normalized[k] for k in ("本日異動股借券(2)", "今日新增借券股數") if k in normalized), None)
    return_idx = next((normalized[k] for k in ("本日異動股還券(3)", "今日還券了結股數") if k in normalized), None)
    bal_idx = next((normalized[k] for k in ("本日借券餘額股(4)=(1)+(2)-(3)", "今日借券餘額(股數)") if k in normalized), None)
    market_idx = normalized.get("市場別")
    if symbol_idx is None or prev_idx is None or borrow_idx is None or return_idx is None or bal_idx is None or market_idx is None or not data:
        print(f"[WARN] TWT72U required fields/data absent: fields={fields!r}")
        return out

    # The official "整體市場" 合計 row is the all-market source of truth.
    # Do not reconstruct it by adding individual securities or market subtotals.
    overall_row = next((
        row for row in reversed(data)
        if isinstance(row, (list, tuple))
        and max(symbol_idx, prev_idx, borrow_idx, return_idx, bal_idx, market_idx) < len(row)
        and str(row[market_idx] or "").strip() == "整體市場"
    ), None)
    if overall_row is None:
        print(f"[WARN] TWT72U 整體市場合計 row absent: date={date8}")
        return out

    total_prev = _num(overall_row[prev_idx])
    borrowed = _num(overall_row[borrow_idx])
    returned = _num(overall_row[return_idx])
    total_bal = _num(overall_row[bal_idx])
    if any(value is None for value in (total_prev, borrowed, returned, total_bal)):
        print(f"[WARN] TWT72U 整體市場合計 row contains invalid values: date={date8}")
        return out
    if abs((total_prev + borrowed - returned) - total_bal) > 1e-6:
        print(f"[WARN] TWT72U 整體市場合計 row roll-forward mismatch: date={date8}")
        return out

    print(f"[INFO] TWT72U official 整體市場合計 row accepted date={date8}")
    return {
        "bal": total_bal,
        "prev_bal": total_prev,
        "chg": total_bal - total_prev,
        "date_ok": True,
    }


# ---------- 上市成交 ----------

def turnover_tw(roc: str) -> float | None:
    """FMTQIK 依 Date 取 TradeValue (元)。"""
    j = _get_json(f"{TWSE_API}/exchangeReport/FMTQIK")
    if not isinstance(j, list):
        return None
    for row in j:
        if str(row.get("Date", "")) == roc:
            return _num(row.get("TradeValue"))
    return None

# ---------- 上櫃 ----------

def tpex_highlight(roc: str) -> dict:
    """單列 + Date 驗證。DailyTradingValue 單位：百萬元。"""
    j = _get_json(f"{TPEX_API}/tpex_mainborad_highlight")
    out = {"row": None, "date_ok": False}
    if isinstance(j, list) and j:
        row = j[0]
        out = {"row": row, "date_ok": str(row.get("Date", "")) == roc}
    return out

def tpex_margin(roc: str) -> dict:
    out = {"bal": None, "chg": None, "sbal": None, "schg": None, "date_ok": False}
    j = _get_json(f"{TPEX_API}/tpex_mainboard_margin_balance")
    if not isinstance(j, list):
        return out
    bal = chg = sbal = schg = 0.0
    n = 0
    for row in j:
        if str(row.get("Date", "")) != roc:
            continue
        b = _num(row.get("MarginPurchaseBalance"))
        if b is None:
            continue
        n += 1
        bal += b
        chg += (_num(row.get("MarginPurchase")) or 0.0) - (_num(row.get("MarginSales")) or 0.0)
        sbal += _num(row.get("ShortSaleBalance")) or 0.0
        schg += (_num(row.get("ShortSale")) or 0.0) - (_num(row.get("ShortConvering")) or 0.0)
    if n:
        out = {"bal": bal, "chg": chg, "sbal": sbal, "schg": schg, "date_ok": True}
    return out

def tpex_sbl(roc: str) -> dict:
    """TPEx 官方信用額度總量管制餘額：依 S47 欄名取借券賣出前日／當日餘額。"""
    out = {"bal": None, "sale_bal": None, "sale_chg": None, "date_ok": False}
    date8 = _twse_date8(roc)
    if date8 is None:
        print(f"[WARN] TPEX margin_sbl invalid requested date: {roc!r}")
        return out
    date_iso = f"{date8[:4]}/{date8[4:6]}/{date8[6:8]}"
    url = f"https://www.tpex.org.tw/www/zh-tw/margin/sbl?response=json&date={date_iso}"
    j = _get_json(url)
    if not isinstance(j, dict):
        print(f"[WARN] TPEX margin_sbl invalid response type: {type(j).__name__}")
        return out
    tables = j.get("tables") or []
    table = next((t for t in tables if isinstance(t, dict) and isinstance(t.get("fields"), list) and isinstance(t.get("data"), list)), None)
    if table is None:
        print(f"[WARN] TPEX margin_sbl missing tables/fields/data: keys={list(j)[:10]}")
        return out
    actual = _twse_date8(table.get("date") or j.get("date"))
    if actual != date8:
        print(f"[WARN] TPEX margin_sbl date mismatch: requested={date8} actual={table.get('date') or j.get('date')!r}")
        return out
    fields = table["fields"]
    data = table["data"]
    normalized = {str(name).strip().replace(" ", ""): i for i, name in enumerate(fields)}
    symbol_idx = next((normalized[k] for k in ("股票代號", "證券代號", "代號") if k in normalized), None)
    prev_idx, bal_idx = _borrowed_short_field_pair(fields)
    sell_idx = next((normalized[k] for k in ("當日賣出", "借券賣出當日賣出") if k in normalized), None)
    return_idx = next((normalized[k] for k in ("當日還券", "借券賣出當日還券") if k in normalized), None)
    adjust_idx = next((normalized[k] for k in ("當日調整數額", "當日調整", "借券賣出當日調整數額") if k in normalized), None)
    if symbol_idx is None or prev_idx is None or bal_idx is None or sell_idx is None or return_idx is None or adjust_idx is None:
        print(f"[WARN] TPEX margin_sbl required S47 fields absent: fields={fields!r}")
        return out
    import re
    total_prev = total_bal = 0.0
    parsed = invalid = 0
    for row in data:
        # A structurally malformed row cannot safely be classified as a non-stock
        # summary row, so reject the market aggregate instead of silently skipping it.
        if not isinstance(row, (list, tuple)) or max(symbol_idx, prev_idx, sell_idx, return_idx, adjust_idx, bal_idx) >= len(row):
            invalid += 1
            continue
        code = str(row[symbol_idx] or "").strip().upper()
        if not re.fullmatch(r"[0-9A-Z]{4,6}", code):
            continue
        prev = _num(row[prev_idx])
        sold = _num(row[sell_idx])
        returned = _num(row[return_idx])
        adjusted = _num(row[adjust_idx])
        bal = _num(row[bal_idx])
        if prev is None or sold is None or returned is None or adjusted is None or bal is None or abs((prev + sold - returned + adjusted) - bal) > 1e-6:
            invalid += 1
            continue
        total_prev += prev
        total_bal += bal
        parsed += 1
    if not parsed or invalid:
        print(f"[WARN] TPEX margin_sbl rejected incomplete stock rows: date={date8} parsed={parsed} total={len(data)} invalid={invalid}")
        return out
    print(f"[INFO] TPEX margin_sbl parsed rows={parsed}/{len(data)} date={date8}")
    return {"bal": None, "sale_bal": total_bal, "sale_chg": total_bal - total_prev, "date_ok": True}
