"""TWSE 證交所：加權指數 (OpenAPI) + 三大法人 (RWD JSON)，免 Key。"""
from __future__ import annotations
from datetime import datetime
from src.utils import fetch_with_retry as _fetch

MI_INDEX_URL = "https://openapi.twse.com.tw/v1/exchangeReport/MI_INDEX"
BFI82U_URL = "https://www.twse.com.tw/rwd/zh/fund/BFI82U"
TWSE_PROXY = "https://twse-proxy.grichtoyang.workers.dev"

def _proxy_institutional(date8: str) -> dict | None:
    """twse-proxy /institutional (V1.1+)。未部署/失敗回 None，由呼叫端走 RWD 備援。"""
    import os
    base = os.getenv("TWSE_PROXY_BASE_URL", TWSE_PROXY).rstrip("/")
    try:
        import requests
        from src.utils import HEADERS
        r = requests.get(f"{base}/institutional", params={"date": date8},
                         headers={**HEADERS, "accept": "application/json"}, timeout=20)
        if r.status_code != 200:
            return None
        j = r.json()
        if not isinstance(j, dict) or j.get("ok") is not True:
            return None
        d = j.get("data") or {}
        if d.get("foreign") is None:
            return None
        return {"date": str(j.get("actual_date", "")).replace("-", ""), "foreign": d.get("foreign"),
                "trust": d.get("investment_trust"), "dealer": d.get("dealer"),
                "total": d.get("total"), "via": "proxy"}
    except Exception as e:  # noqa: BLE001
        print(f"[INFO] twse-proxy institutional 不可用，改 RWD 備援：{e}")
        return None

def get_taiex() -> dict:
    """回傳 {date, close, change_sign, change_pts, pct}，失敗回 {}。"""
    r = _fetch(MI_INDEX_URL)
    if r is None:
        return {}
    try:
        data = r.json()
        # TAIEX 本體 = 發行量加權股價指數
        rows = [d for d in data if d.get("指數") == "發行量加權股價指數"]
        if not rows:
            # 退路：找名稱含加權的第一筆
            rows = [d for d in data if "加權" in str(d.get("指數", ""))]
        if not rows:
            return {}
        rows = sorted(rows, key=lambda x: x.get("日期", ""))
        row = rows[-1]
        return {
            "date": row.get("日期", ""),
            "close": row.get("收盤指數", ""),
            "change_sign": row.get("漲跌", ""),
            "change_pts": row.get("漲跌點數", ""),
            "pct": row.get("漲跌百分比", ""),
            "raw": row,
        }
    except Exception as e:  # noqa: BLE001
        print(f"[WARN] TWSE MI_INDEX parse failed: {e}")
        return {}

def get_institutional(query_date: str = "") -> dict:
    """三大法人買賣超 (億元)。Proxy 優先 (/institutional, V1.1+)，RWD BFI82U 備援。
    query_date 格式 yyyymmdd，空字串=最新。回傳 {date, foreign, trust, dealer, total, via}。"""
    if query_date:
        proxy = _proxy_institutional(query_date)
        if proxy is not None:
            return proxy
    params = {}
    if query_date:
        # RWD API 要 yyyyMMdd (西元)，傳入 yyyymmdd (如 20260915) 直接可用
        params = {"date": query_date, "response": "json"}
    r = _fetch(BFI82U_URL, params=params or None)
    if r is None:
        return {}
    try:
        j = r.json()
        if j.get("stat") != "OK":
            print(f"[WARN] BFI82U stat={j.get('stat')}")
            return {}
        # fields: 證券商..., data rows: 自營商/投信/外資...
        date = j.get("date", "")
        foreign = trust = dealer = None
        for row in j.get("data", []):
            name = row[0] if row else ""
            # 買賣超 = row[3]，格式 "1,234,567,890"，單位元 → 億元
            try:
                val_yi = float(str(row[3]).replace(",", "")) / 1e8
            except Exception:
                continue
            if "外資" in name:
                # 外資有兩列：外資及陸資 + 外資自營商，需加總
                foreign = val_yi if foreign is None else foreign + val_yi
            elif "投信" in name:
                trust = val_yi if trust is None else trust + val_yi
            elif "自營商" in name and dealer is None:
                # 自營商有 (自行買賣) 與 (避險) 兩列，需加總
                dealer = val_yi
            elif "自營商" in name and dealer is not None:
                dealer += val_yi
        # 若有合計列直接用，否則加總
        total = None
        for row in j.get("data", []):
            if "合計" in str(row[0]):
                try:
                    total = float(str(row[3]).replace(",", "")) / 1e8
                except Exception:
                    pass
        if total is None and None not in (foreign, trust, dealer):
            total = foreign + trust + dealer
        return {"date": date, "foreign": foreign, "trust": trust, "dealer": dealer, "total": total}
    except Exception as e:  # noqa: BLE001
        print(f"[WARN] TWSE BFI82U parse failed: {e}")
        return {}
