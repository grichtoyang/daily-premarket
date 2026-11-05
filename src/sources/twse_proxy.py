"""twse-proxy 用戶端 (現貨主要來源) + TWSE MI_INDEX 官方備援。

proxy: https://twse-proxy.grichtoyang.workers.dev?date=yyyymmdd
回傳 data.taiex / data.market_statistics / data.advance_decline
"""
from __future__ import annotations
import re
import requests
from src.utils import HEADERS

BASE = "https://twse-proxy.grichtoyang.workers.dev"
MI_INDEX = "https://openapi.twse.com.tw/v1/exchangeReport/MI_INDEX"

def _num(v):
    if v is None:
        return None
    s = re.sub(r"<[^>]+>", "", str(v)).replace(",", "").replace("%", "").strip()
    if s in {"", "--", "---", "N/A", "null", "None", "－", "—"}:
        return None
    try:
        return float(s)
    except ValueError:
        return None

def fetch(date8: str, timeout: int = 30) -> dict | None:
    """date8 = yyyymmdd。成功回傳 proxy payload dict，失敗回 None。"""
    try:
        r = requests.get(f"{BASE}?date={date8}", headers={**HEADERS, "accept": "application/json"}, timeout=timeout)
        r.raise_for_status()
        j = r.json()
        if isinstance(j, dict) and j.get("ok") is True:
            def compact(value):
                return re.sub(r"[^0-9]", "", str(value or ""))
            endpoints = j.get("endpoints") or {}
            ind = endpoints.get("IND") or {}
            # V1.2 才提供上游實際日期；舊版或缺日期一律不接受。
            if (
                ind.get("date_valid") is not True
                or compact(ind.get("actual_date")) != date8
            ):
                print("[WARN] twse-proxy IND upstream date missing or mismatched")
                return None
            data = j.get("data") or {}
            ms = endpoints.get("MS") or {}
            if (
                ms.get("date_valid") is not True
                or compact(ms.get("actual_date")) != date8
            ):
                # IND/TAIEX 可用，但 MS 衍生資料必須獨立標為不可用。
                data["market_statistics"] = None
                data["advance_decline"] = None
                j["data"] = data
                print("[WARN] twse-proxy MS upstream date missing or mismatched")
            return j
    except Exception as e:  # noqa: BLE001
        print(f"[WARN] twse-proxy failed: {e}")
    return None

def parse_taiex(payload: dict) -> dict:
    t = (payload.get("data") or {}).get("taiex") or {}
    direction = str(t.get("direction", ""))
    change = _num(t.get("change"))
    pct = _num(t.get("change_percent"))
    if change is not None:
        if "-" in direction and "color:green" in direction:
            change = -abs(change)
        elif "+" in direction or "color:red" in direction:
            change = abs(change)
    if change is not None and pct is not None:
        pct = abs(pct) if change >= 0 else -abs(pct)
    return {"close": _num(t.get("close")), "change": change, "pct": pct}

def _split_paren(text: str) -> tuple:
    """'207(5)' -> (207.0, 5.0)。"""
    m = re.match(r"\s*([\d,\.]+)\s*(?:\(\s*([\d,\.]+)\s*\))?", str(text))
    if not m:
        return None, None
    return _num(m.group(1)), _num(m.group(2))

def parse_listed_breadth(payload: dict) -> dict:
    """從 advance_decline 取 類型=股票 的上漲(漲停)/下跌(跌停)/持平。"""
    out = {"up": None, "down": None, "flat": None, "limit_up": None, "limit_down": None}
    adv = (payload.get("data") or {}).get("advance_decline") or {}
    fields = adv.get("fields") or []
    data = adv.get("data") or []
    if not fields or not data:
        return out
    try:
        ti = fields.index("類型")
        si = fields.index("股票")
    except ValueError:
        return out
    for row in data:
        if len(row) <= max(ti, si):
            continue
        label = str(row[ti]).strip()
        val, paren = _split_paren(row[si])
        if label == "上漲(漲停)":
            out["up"], out["limit_up"] = val, paren
        elif label == "下跌(跌停)":
            out["down"], out["limit_down"] = val, paren
        elif label == "持平":
            out["flat"] = val
    return out

def parse_listed_turnover(payload: dict) -> float | None:
    """market_statistics 總計(1~15) 成交金額(元)。"""
    ms = (payload.get("data") or {}).get("market_statistics") or {}
    fields = ms.get("fields") or []
    data = ms.get("data") or []
    if not fields or not data:
        return None
    try:
        si = fields.index("成交統計")
        ai = fields.index("成交金額(元)")
    except ValueError:
        return None
    for row in data:
        if row and str(row[si]).strip().startswith("總計"):
            return _num(row[ai])
    return None

def official_ind_taiex(date8: str, timeout: int = 20) -> dict:
    """備援：MI_INDEX?date=&type=IND。回傳 {close, change, pct} (無開高低)。"""
    out = {"close": None, "change": None, "pct": None}
    try:
        url = f"https://www.twse.com.tw/exchangeReport/MI_INDEX?response=json&date={date8}&type=IND"
        r = requests.get(url, headers={**HEADERS, "accept": "application/json"}, timeout=timeout)
        r.raise_for_status()
        payload = r.json()
        actual_date = re.sub(r"[^0-9]", "", str(payload.get("date") or "")) if isinstance(payload, dict) else ""
        if actual_date != date8:
            print(f"[WARN] MI_INDEX fallback date mismatch: actual={actual_date or 'missing'} requested={date8}")
            return out
        for table in payload.get("tables") or []:
            for row in table.get("data") or []:
                if row and row[0] == "發行量加權股價指數":
                    sign = str(row[2] if len(row) > 2 else "").strip()
                    chg = _num(row[3] if len(row) > 3 else None)
                    pct = _num(row[4] if len(row) > 4 else None)
                    if chg is not None and "-" in sign:
                        chg = -abs(chg)
                    if chg is not None and pct is not None:
                        pct = abs(pct) if chg >= 0 else -abs(pct)
                    out = {"close": _num(row[1] if len(row) > 1 else None), "change": chg, "pct": pct}
                    return out
    except Exception as e:  # noqa: BLE001
        print(f"[WARN] MI_INDEX fallback failed: {e}")
    return out
