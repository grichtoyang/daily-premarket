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


def twse_twt93u_sbl(roc: str) -> dict:
    """TWT93U 信用額度總量管制餘額表 — 上市借券賣出餘額與增減。

    回傳 {sale_bal, sale_chg, prev_bal, date_ok}。單位：股數 (API 原值)。
    借券欄位在 data[i][7..13]：前日餘額/當日賣出/當日還券/當日調整/當日餘額/次一營業日可限額
    """
    url = f"https://www.twse.com.tw/exchangeReport/TWT93U?response=json&date={roc}"
    j = _get_json(url)
    out = {"sale_bal": None, "sale_chg": None, "prev_bal": None, "date_ok": False}
    if not isinstance(j, dict) or j.get("stat") != "OK":
        return out
    data = j.get("data") or []
    if not data:
        return out
    total_prev = 0.0
    total_bal = 0.0
    n = 0
    for row in data:
        if len(row) < 12:
            continue
        prev = _num(row[7])   # 前日餘額 (借券)
        bal = _num(row[11])   # 當日餘額 (借券)
        if prev is not None and bal is not None:
            total_prev += prev
            total_bal += bal
            n += 1
    if n:
        out = {
            "sale_bal": total_bal,
            "sale_chg": total_bal - total_prev,
            "prev_bal": total_prev,
            "date_ok": True,
        }
    return out

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
    out = {"bal": None, "sale_bal": None, "sale_chg": None, "date_ok": False}
    j = _get_json(f"{TPEX_API}/tpex_margin_sbl")
    if not isinstance(j, list):
        return out
    bal = sale = sale_prev = 0.0
    n = 0
    for row in j:
        if str(row.get("Date", "")) != roc:
            continue
        b = _num(row.get("SecuritiesBorrowingBalanceOfTheMarketDay"))
        if b is None:
            continue
        n += 1
        bal += b
        sale += _num(row.get("SaleBalanceOfTheMarketDay")) or 0.0
        sale_prev += _num(row.get("SaleBalancePreviousDay")) or 0.0
    if n:
        out = {"bal": bal, "sale_bal": sale, "sale_chg": sale - sale_prev, "date_ok": True}
    return out
