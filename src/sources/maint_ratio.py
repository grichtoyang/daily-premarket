"""大盤融資維持率。

1) 玩股網 API (免費、穩定，但延遲 ~3 天)
   https://www.wantgoo.com/stock/0000A/margin-trading/historical-lending-balance
2) 股市智投 stockintelli.com (SSR 頁面爬蟲，通常有當天資料)
   https://www.stockintelli.com/market/margin-trading
3) 愛玩股 istock.tw 網頁爬蟲 (最後備援)。
注意：官方無每日維持率序列，此為民間估算值，來源須透明標示。
"""
from __future__ import annotations
from datetime import datetime, timezone, timedelta
import re
import requests

TAIPEI = timezone(timedelta(hours=8))


UA = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Referer": "https://www.wantgoo.com/stock/margin-trading/market-price/taiex",
}

# ---------- 主力：玩股網 API ----------

WANTGOO_URL = "https://www.wantgoo.com/stock/0000A/margin-trading/historical-lending-balance"


def _wantgoo(t0: str, timeout: int = 20) -> dict:
    """玩股網 API，回傳 {ratio, date, ok}。延遲 1~3 天，取最接近 T0 的資料。"""
    out = {"ratio": None, "date": None, "ok": False}
    try:
        r = requests.get(WANTGOO_URL, headers=UA, timeout=timeout)
        r.raise_for_status()
        data = r.json()
        if not data:
            return out
        best = None
        for item in data:
            ts = item.get("date", 0)
            dt = datetime.fromtimestamp(ts / 1000, tz=TAIPEI)
            date_str = dt.strftime("%Y-%m-%d")
            mr = item.get("marginRatio")
            if mr is not None and date_str <= t0:
                best = (date_str, round(mr * 100, 2))
                break  # API 已按日期降序，第一筆 <= T0 即為最接近
        if best:
            out = {"ratio": best[1], "date": best[0], "ok": True}
            if best[0] != t0:
                print(f"[INFO] wantgoo 維持率日期 {best[0]} 非 T0 ({t0})，取最接近")
    except Exception as e:  # noqa: BLE001
        print(f"[WARN] wantgoo margin ratio failed: {e}")
    return out


# ---------- 備援一：股市智投 stockintelli.com ----------

STOCKINTELLI_URL = "https://www.stockintelli.com/market/margin-trading"


def _stockintelli(t0: str, timeout: int = 20) -> dict:
    """stockintelli.com SSR 頁面爬蟲，回傳 {ratio, date, ok}。"""
    out = {"ratio": None, "date": None, "ok": False}
    try:
        r = requests.get(STOCKINTELLI_URL, headers=UA, timeout=timeout)
        r.raise_for_status()
        html = r.text
        # T0 "2026-09-18" → "09/18"
        mm_dd = t0[5:].replace("-", "/")  # "09/18"
        # 找整個表格列，取最後一個百分比（維持率在最後一欄）
        # 格式：<td...>09/18</td>...<td...>189.81%</td></tr>
        row_pattern = re.compile(
            rf'{re.escape(mm_dd)}.*?</tr>',
            re.S,
        )
        rm = row_pattern.search(html)
        if rm:
            row = rm.group(0)
            # 取最後一個 XX.XX%
            pcts = re.findall(r'(\d{2,3}\.\d{1,2})%', row)
            if pcts:
                ratio = float(pcts[-1])  # 最後一個百分比 = 維持率
                if 50 < ratio < 500:  # 合理範圍
                    out = {"ratio": ratio, "date": t0, "ok": True}
                else:
                    print(f"[INFO] stockintelli 維持率數值異常: {ratio}")
        else:
            # 備用：找 sr-only 區塊裡的「大盤融資維持率目前 XX.X%」
            m2 = re.search(
                r'大盤融資維持率目前\s*(\d{2,3}\.\d)%', html
            )
            if m2:
                ratio = float(m2.group(1))
                # sr-only 區塊只有最新日期，無法指定 T0，保守檢查
                if 50 < ratio < 500:
                    # 從同一區塊抓日期
                    dm = re.search(r'(\d{4}-\d{2}-\d{2})', html[m2.start() - 300:m2.start()])
                    date_str = dm.group(1) if dm else None
                    if date_str == t0:
                        out = {"ratio": ratio, "date": t0, "ok": True}
                    else:
                        print(f"[INFO] stockintelli sr-only 日期 {date_str} 非 T0 ({t0})")
    except Exception as e:  # noqa: BLE001
        print(f"[WARN] stockintelli margin ratio failed: {e}")
    return out


# ---------- 備援二：愛玩股 istock.tw ----------

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
    """回傳 {ratio(%), date, ok, source}。依序嘗試 wantgoo → stockintelli → istock。"""
    # 1) 玩股網 API
    result = _wantgoo(t0, timeout=min(timeout, 20))
    if result["ok"]:
        result["source"] = "wantgoo"
        return result
    # 2) 股市智投 (SSR，通常有當天資料)
    print("[INFO] wantgoo 維持率不可用，嘗試 stockintelli")
    result = _stockintelli(t0, timeout=min(timeout, 15))
    if result["ok"]:
        result["source"] = "stockintelli"
        return result
    # 3) 愛玩股 istock.tw
    print("[INFO] stockintelli 維持率不可用，嘗試 istock 備援")
    result = _istock(t0, timeout=timeout)
    if result["ok"]:
        result["source"] = "istock"
    return result
