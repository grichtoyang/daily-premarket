"""重要市場：Yahoo Finance Chart API (免費免 Key)，API 優先、失敗標 unavailable。

每檔回傳 {price, change, pct, date, retrieved_at, source}，
change/pct 由最近兩根日K收盤計算 (不依賴 meta 漲跌欄)。
"""
from __future__ import annotations
from datetime import datetime, timezone
import requests
from src.utils import HEADERS

GROUPS: dict[str, list[tuple[str, str]]] = {
    "美股指數": [("S&P 500", "^GSPC"), ("Nasdaq Composite", "^IXIC"), ("Nasdaq 100", "^NDX"),
             ("Dow Jones", "^DJI"), ("費城半導體 SOX", "^SOX"), ("VIX", "^VIX")],
    "亞洲主要指數": [("日經225", "^N225"), ("韓國KOSPI", "^KS11"), ("香港恆生", "^HSI"),
                ("上海綜合", "000001.SS"), ("深圳成分", "399001.SZ")],
    "美股指數期貨": [("S&P500期貨", "ES=F"), ("Nasdaq100期貨", "NQ=F"), ("道瓊期貨", "YM=F"),
                ("Russell2000期貨", "RTY=F")],
    "主要匯率": [("USD/TWD", "TWD=X"), ("DXY美元指數", "DX-Y.NYB"), ("USD/JPY", "JPY=X"),
             ("USD/KRW", "KRW=X")],
    "台灣相關ADR": [("台積電ADR", "TSM"), ("聯電ADR", "UMC"), ("日月光ADR", "ASX")],
    "原油黃金Bitcoin": [("WTI原油期貨", "CL=F"), ("黃金期貨", "GC=F"), ("Bitcoin", "BTC-USD")],
}

def quote(sym: str) -> dict:
    out = {"symbol": sym, "price": None, "change": None, "pct": None, "date": None,
           "retrieved_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
           "source": "Yahoo Finance Chart API", "ok": False}
    try:
        r = requests.get(f"https://query1.finance.yahoo.com/v8/finance/chart/{sym}?interval=1d&range=1mo",
                         headers={**HEADERS, "Accept": "application/json"}, timeout=20)
        r.raise_for_status()
        res = (r.json().get("chart", {}).get("result") or [None])[0]
        if not res:
            return out
        ts = res.get("timestamp") or []
        closes = ((res.get("indicators") or {}).get("quote") or [{}])[0].get("close") or []
        pts = [(t, c) for t, c in zip(ts, closes) if c is not None]
        if len(pts) < 1:
            return out
        last_t, last_c = pts[-1]
        out["price"] = last_c
        out["date"] = datetime.fromtimestamp(last_t, tz=timezone.utc).strftime("%Y-%m-%d")
        if len(pts) >= 2:
            prev_c = pts[-2][1]
            out["change"] = last_c - prev_c
            out["pct"] = (last_c - prev_c) / prev_c * 100 if prev_c else None
        out["ok"] = True
    except Exception as e:  # noqa: BLE001
        print(f"[WARN] yahoo {sym} failed: {e}")
    return out

def get_all() -> dict:
    """{group: [(name, quote)]}。"""
    return {g: [(name, quote(sym)) for name, sym in items] for g, items in GROUPS.items()}

def ohlc(sym: str) -> dict:
    """最近一根日K的 open/high/low/close/date。失敗回 ok=False。"""
    out = {"open": None, "high": None, "low": None, "close": None, "date": None, "ok": False}
    try:
        r = requests.get(f"https://query1.finance.yahoo.com/v8/finance/chart/{sym}?interval=1d&range=5d",
                         headers={**HEADERS, "Accept": "application/json"}, timeout=20)
        r.raise_for_status()
        res = (r.json().get("chart", {}).get("result") or [None])[0]
        if not res:
            return out
        ts = res.get("timestamp") or []
        q = ((res.get("indicators") or {}).get("quote") or [{}])[0]
        n = len(ts)
        for i in range(n - 1, -1, -1):
            c = (q.get("close") or [None] * n)[i]
            if c is None:
                continue
            import datetime as _dt
            out = {"open": (q.get("open") or [None] * n)[i], "high": (q.get("high") or [None] * n)[i],
                   "low": (q.get("low") or [None] * n)[i], "close": c,
                   "date": _dt.datetime.fromtimestamp(ts[i], tz=_dt.timezone.utc).strftime("%Y-%m-%d"),
                   "ok": True}
            break
    except Exception as e:  # noqa: BLE001
        print(f"[WARN] yahoo ohlc {sym} failed: {e}")
    return out
# ---- 相容舊介面 (分析層/舊報表用) ----
_LEGACY = {"SP500": "^GSPC", "Nasdaq": "^IXIC", "DOW": "^DJI", "SOX": "^SOX", "VIX": "^VIX",
           "TSM_ADR": "TSM", "US10Y": "^TNX", "DXY": "DX-Y.NYB", "USDTWD": "TWD=X",
           "GOLD": "GC=F", "WTI": "CL=F"}

def get_legacy() -> dict:
    out = {}
    for name, sym in _LEGACY.items():
        q = quote(sym)
        out[name] = {"symbol": sym, "close": q["price"], "pct": q["pct"], "date": q["date"]}
    return out
