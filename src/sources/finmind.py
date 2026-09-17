"""FinMind (第二優先)：大盤 OHLC + 成交金額。

dataset=TaiwanStockPrice, data_id=TAIEX，免 token 可取近期資料。
失敗時由呼叫端改用 Yahoo ^TWII 備援。
"""
from __future__ import annotations
import requests
from src.utils import HEADERS

API = "https://api.finmindtrade.com/api/v4/data"

def taiex_ohlc(t0: str, timeout: int = 20, retries: int = 3) -> dict:
    """回傳 {open, high, low, money_yuan, date}，取不到回全 None。"""
    import time
    out = {"open": None, "high": None, "low": None, "money_yuan": None, "date": None, "ok": False}
    for attempt in range(retries):
        try:
            r = requests.get(API, params={"dataset": "TaiwanStockPrice", "data_id": "TAIEX",
                                          "start_date": t0},
                             headers={**HEADERS, "Accept": "application/json"}, timeout=timeout)
            if r.status_code == 429:
                time.sleep(2 ** (attempt + 1))
                continue
            r.raise_for_status()
            for row in r.json().get("data") or []:
                if row.get("date") != t0 or row.get("stock_id") != "TAIEX":
                    continue
                return {"open": _f(row.get("open")), "high": _f(row.get("max")), "low": _f(row.get("min")),
                        "money_yuan": _f(row.get("Trading_money")), "date": t0, "ok": True}
            return out  # 有回應但無 T0 列，不必重試
        except Exception as e:  # noqa: BLE001
            print(f"[WARN] finmind TAIEX failed (try {attempt + 1}): {e}")
            time.sleep(2 ** (attempt + 1))
    return out

def _f(v):
    try:
        return float(v) if v is not None else None
    except (ValueError, TypeError):
        return None
