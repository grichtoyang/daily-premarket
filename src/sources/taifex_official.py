"""TAIFEX OpenAPI 官方 (第一優先)：前十大 + P/C 歷史。

https://openapi.taifex.com.tw/v1/ (servers 欄位確認)
注意：官方端點資料落後約一日 (最新 = T-1)，取用時必須標示實際日期。
TypeOfTraders=0 (全部交易人)；999912/666666 為合計列，取指定月份列。
"""
from __future__ import annotations
import requests
from src.utils import HEADERS

BASE = "https://openapi.taifex.com.tw/v1"
PROXY = "https://taifex.grichtoyang.workers.dev"
_cache: dict = {}

def _proxy_top10(kind: str, t0: str, month: str) -> dict | None:
    """Proxy 優先 (V1.2+)。kind: futures|call|put。失敗回 None，由呼叫端走官方備援。"""
    import os
    base = os.getenv("TAIFEX_PROXY_BASE_URL", PROXY).rstrip("/")
    ep = "futures-top10" if kind == "futures" else "options-top10"
    params = {"date": t0}
    if month:
        params["month"] = month
    if kind != "futures":
        params["type"] = kind
    try:
        r = requests.get(f"{base}/{ep}", params=params,
                         headers={**HEADERS, "accept": "application/json"}, timeout=30)
        if r.status_code != 200:
            return None
        j = r.json()
        if not isinstance(j, dict) or j.get("ok") is not True:
            return None
        d = j.get("data") or {}
        if d.get("buy") is None:
            return None
        return {"date": (j.get("date") or "").replace("-", ""),
                "buy": d.get("buy"), "sell": d.get("sell"), "net": d.get("net"),
                "month": d.get("month"), "via": "proxy"}
    except Exception as e:  # noqa: BLE001
        print(f"[INFO] proxy top10 不可用 ({kind})，改官方備援：{e}")
        return None

def _get(path: str, timeout: int = 60):
    if path not in _cache:
        _cache[path] = []
        import time
        for attempt in range(3):
            try:
                r = requests.get(BASE + path, headers={**HEADERS, "accept": "application/json"}, timeout=timeout)
                r.raise_for_status()
                j = r.json()
                if isinstance(j, list) and j:
                    _cache[path] = j
                    break
                time.sleep(3)
            except Exception as e:  # noqa: BLE001
                print(f"[WARN] taifex official {path} failed (try {attempt + 1}): {e}")
                time.sleep(2 ** (attempt + 1))
    return _cache[path]

def _num(v):
    try:
        return float(str(v).replace(",", "")) if v not in (None, "") else None
    except (ValueError, TypeError):
        return None

def _pick(rows: list, month: str) -> dict:
    """取最新日期列；月份優先指定，無則取當日最大月份 (排除合計列)。"""
    rows = [r for r in rows if r.get("SettlementMonth") not in ("999912", "666666")]
    if not rows:
        return {}
    latest = max(r.get("Date", "") for r in rows)
    cands = [r for r in rows if r.get("Date") == latest]
    for r in cands:
        if r.get("SettlementMonth") == month:
            return r
    return max(cands, key=lambda r: r.get("SettlementMonth", ""))

def top10_fut(month: str, t0: str = "") -> dict:
    """TX 前十大 (TypeOfTraders=0)。Proxy 優先，官方備援。月份無資料時取最新日最大月份。"""
    if t0 and month:
        p = _proxy_top10("futures", t0, month)
        if p is not None:
            b, s = p["buy"], p["sell"]
            return {"date": _iso(p["date"]), "buy": b, "sell": s, "net": p["net"],
                    "month": p["month"], "via": "proxy"}
    out = {"date": None, "buy": None, "sell": None, "net": None, "month": None, "via": "official"}
    rows = [r for r in _get("/OpenInterestOfLargeTradersFutures")
            if r.get("Contract") == "TX" and r.get("TypeOfTraders") == "0"]
    r = _pick(rows, month)
    if not r:
        return out
    b, s = _num(r.get("Top10Buy")), _num(r.get("Top10Sell"))
    return {"date": _iso(r.get("Date", "")), "buy": b, "sell": s,
            "net": (b - s) if b is not None and s is not None else None,
            "month": r.get("SettlementMonth")}

def top10_opt(month: str, callput: str, t0: str = "") -> dict:
    """TXO 買權/賣權前十大。callput: '買權'/'賣權'。Proxy 優先，官方備援。"""
    out = {"date": None, "buy": None, "sell": None, "net": None, "month": None,
           "via": "official", "callput": callput}
    if t0 and month:
        kind = "call" if callput == "買權" else "put"
        p = _proxy_top10(kind, t0, month)
        if p is not None:
            b, s = p["buy"], p["sell"]
            return {"date": _iso(p["date"]), "buy": b, "sell": s, "net": p["net"],
                    "month": p["month"], "via": "proxy", "callput": callput}
    rows = [r for r in _get("/OpenInterestOfLargeTradersOptions")
            if r.get("Contract") == "TXO" and r.get("CallPut") == callput
            and r.get("TypeOfTraders") == "0"]
    r = _pick(rows, month)
    if not r:
        return out
    b, s = _num(r.get("Top10Buy")), _num(r.get("Top10Sell"))
    return {"date": _iso(r.get("Date", "")), "buy": b, "sell": s,
            "net": (b - s) if b is not None and s is not None else None,
            "month": r.get("SettlementMonth"), "via": "official", "callput": callput}

def putcall_history() -> list:
    """依日期排序的 P/C 歷史 [(date, vol_ratio, oi_ratio)]。Proxy 優先，官方備援。"""
    import os
    base = os.getenv("TAIFEX_PROXY_BASE_URL", PROXY).rstrip("/")
    try:
        import requests
        from src.utils import HEADERS
        r = requests.get(f"{base}/put-call-ratio-history",
                         headers={**HEADERS, "accept": "application/json"}, timeout=30)
        if r.status_code == 200:
            j = r.json()
            if isinstance(j, dict) and j.get("ok") is True and isinstance(j.get("data"), list):
                return [{"date": x.get("date"), "vol_ratio": x.get("volume_ratio"),
                         "oi_ratio": x.get("oi_ratio")} for x in j["data"] if x.get("date")]
    except Exception as e:  # noqa: BLE001
        print(f"[INFO] proxy put-call-ratio 不可用，改官方備援：{e}")
    rows = sorted(_get("/PutCallRatio"), key=lambda r: r.get("Date", ""))
    out = []
    for r in rows:
        d = _iso(r.get("Date", ""))
        out.append({"date": d, "vol_ratio": _num(r.get("PutCallVolumeRatio%")),
                    "oi_ratio": _num(r.get("PutCallOIRatio%"))})
    return out

def _iso(d8: str) -> str:
    d8 = str(d8).strip()
    return f"{d8[:4]}-{d8[4:6]}-{d8[6:8]}" if len(d8) == 8 and d8.isdigit() else d8
