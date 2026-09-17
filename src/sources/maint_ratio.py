"""愛玩股 (第三優先)：大盤融資維持率。

https://www.istock.tw/post/twmarginrequirement
頁面含「更新日期: YYYY-MM-DD」+ 最新維持率數值。
注意：官方無每日維持率序列，此為民間估算值，來源須透明標示。
"""
from __future__ import annotations
import re
import requests

UA = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"}
URL = "https://www.istock.tw/post/twmarginrequirement"

def get(t0: str, timeout: int = 30) -> dict:
    """回傳 {ratio(%), date}；日期不符/失敗回 {ratio: None}。"""
    out = {"ratio": None, "date": None, "ok": False}
    try:
        r = requests.get(URL, headers=UA, timeout=timeout)
        r.raise_for_status()
        t = re.sub(r"<script.*?</script>", "", r.text, flags=re.S)
        t = re.sub(r"<style.*?</style>", "", t, flags=re.S)
        tx = re.sub(r"<[^>]+>", "|", t)
        # 以卡片標題錨定 (跳過 <title> 等非卡片出現)，避免抓到其他卡片日期
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
