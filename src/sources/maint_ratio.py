"""大盤融資維持率。

主力來源：玩股網 API (免費、穩定)
  https://www.wantgoo.com/stock/0000A/margin-trading/historical-lending-balance
  回傳 JSON 陣列，第一筆為最新；marginRatio 為小數 (1.89922 = 189.92%)。

備援：愛玩股 istock.tw 網頁爬蟲。
注意：官方無每日維持率序列，此為民間估算值，來源須透明標示。
"""
from __future__ import annotations
from datetime import datetime, timezone
import re
import requests


UA = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Referer": "https://www.wantgoo.com/stock/margin-trading/market-price/taiex",
}

# ---------- 主力：玩股網 API ----------

WANTGOO_URL = "https://www.wantgoo.com/stock/0000A/margin-trading/historical-lending-balance"


def _wantgoo(t0: str, timeout: int = 20) -> dict:
    """玩股網 API，回傳 {ratio, date, ok}。"""
    out = {"ratio": None, "date": None, "ok": False}
    try:
        r = requests.get(WANTGOO_URL, headers=UA, timeout=timeout)
        r.raise_for_status()
        data = r.json()
        if not data:
            return out
        latest = data[0]
        ts = latest.get("date", 0)
        dt = datetime.fromtimestamp(ts / 1000, tz=timezone.utc)
        date_str = dt.strftime("%Y-%m-%d")
        mr = latest.get("marginRatio")
        if mr is not None and date_str == t0:
            out = {"ratio": round(mr * 100, 2), "date": t0, "ok": True}
        elif mr is not None:
            print(f"[INFO] wantgoo 維持率日期 {date_str} 非 T0 ({t0})")
    except Exception as e:  # noqa: BLE001
        print(f"[WARN] wantgoo margin ratio failed: {e}")
    return out


# ---------- 備援：愛玩股 istock.tw ----------

ISTOCK_URL = "https://www.istock.tw/post/twmarginrequirement"


def _istock(t0: str, timeout: int = 30) -> dict:
    """istock.tw 爬蟲，回傳 {ratio, date, ok}。"""
    out = {"ratio": None, "date": None, "ok": False}
    try:
        istock_headers = {"User-Agent": UA["User-Agent"]}
        r = requests.get(ISTOCK_URL, headers=istock_headers, timeout=timeout)
        r.raise_for_status()
        t = re.sub(r"<script.*?</script>", "", r.text, flags=re.S)
        t = re.sub(r"<style.*?</style>", "", t, flags=re.S)
        tx = re.sub(r"<[^>]+>", "|", t)
        seg0 = tx
        for mm in re.finditer("大盤融資維持率", tx):
            cand = tx[mm.start():mm.start() + 2500]
            if "更新日期" in cand:
                seg0 = cand
                break
        m = re.search(r"更新日期:\s*(\d{4}-\d{2}-\d{2})", seg0)
        if m and m.group(1) == t0:
            seg = seg0[m.end():m.end() + 500].split("看更多")[0]
            v = re.search(r"(\d{2,3}\.\d+)", seg)
            if v and float(v.group(1)) < 1000:
                out = {"ratio": float(v.group(1)), "date": t0, "ok": True}
            else:
                print("[INFO] istock 維持率數值解析失敗")
        elif m:
            print(f"[INFO] istock 維持率日期 {m.group(1)} 非 T0 ({t0})")
        else:
            print("[INFO] istock 找不到維持率更新日期")
    except Exception as e:  # noqa: BLE001
        print(f"[WARN] istock failed: {e}")
    return out


# ---------- 對外介面 ----------

def get(t0: str, timeout: int = 30) -> dict:
    """回傳 {ratio(%), date, ok}。先嘗試玩股網，失敗再用 istock。"""
    result = _wantgoo(t0, timeout=min(timeout, 20))
    if result["ok"]:
        result["source"] = "wantgoo"
        return result
    print("[INFO] wantgoo 維持率不可用，嘗試 istock 備援")
    result = _istock(t0, timeout=timeout)
    if result["ok"]:
        result["source"] = "istock"
    return result
