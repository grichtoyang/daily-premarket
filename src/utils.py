"""共用工具：HTTP 重試、數字格式化、時區時間。"""
from __future__ import annotations
import time
import requests
from datetime import datetime
from zoneinfo import ZoneInfo

TAIPEI = ZoneInfo("Asia/Taipei")
HEADERS = {"User-Agent": "daily-premarket/1.0 (+github-actions)"}

def fetch_with_retry(url: str, timeout: int = 15, retries: int = 3, params=None) -> requests.Response | None:
    last_err = None
    for i in range(retries):
        try:
            r = requests.get(url, params=params, headers=HEADERS, timeout=timeout)
            r.raise_for_status()
            return r
        except Exception as e:  # noqa: BLE001 - 容錯：記下錯誤後重試
            last_err = e
            time.sleep(2 ** (i + 1))
    print(f"[WARN] fetch failed: {url} err={last_err}")
    return None

def now_taipei() -> datetime:
    return datetime.now(TAIPEI)

def fmt_pct(v) -> str:
    if v is None:
        return "N/A"
    try:
        sign = "+" if float(v) >= 0 else ""
        return f"{sign}{float(v):.2f}%"
    except Exception:
        return "N/A"

def fmt_2(v) -> str:
    if v is None:
        return "N/A"
    try:
        return f"{float(v):,.2f}"
    except Exception:
        return "N/A"

def fmt_int(v) -> str:
    if v is None:
        return "N/A"
    try:
        return f"{int(float(v)):,}"
    except Exception:
        return "N/A"

def safe(v, suffix: str = "") -> str:
    if v is None or v == "":
        return "N/A"
    return f"{v}{suffix}"
