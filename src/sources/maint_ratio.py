"""大盤融資維持率。

1) 愛玩股 iStock：明確提供上市櫃整體維持率與資料日期，作為合計值主來源。
2) WantGoo API / StockIntelli SSR：計算範圍尚未證實為上市櫃合計，只作交叉參考，不可替代上市櫃合計值。
注意：官方無每日維持率序列，此為民間估算值，來源須透明標示。
"""
from __future__ import annotations
from datetime import datetime, timezone, timedelta
import re
from html import unescape
import requests

TAIPEI = timezone(timedelta(hours=8))


UA = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Referer": "https://www.wantgoo.com/stock/margin-trading/market-price/taiex",
}

# ---------- 主力：玩股網 API ----------

WANTGOO_URL = "https://www.wantgoo.com/stock/0000A/margin-trading/historical-lending-balance"


def _wantgoo(t0: str, timeout: int = 20) -> dict:
    """玩股網 API；只接受資料日期精確等於 T0 的數值。較舊資料視為不可用。"""
    out = {"ratio": None, "date": None, "ok": False}
    code = None
    try:
        r = requests.get(WANTGOO_URL, headers=UA, timeout=timeout)
        code = r.status_code
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
            if mr is not None and date_str == t0:
                best = (date_str, round(mr * 100, 2))
                break  # API 已按日期降序；只接受精確 T0
        if best:
            out = {"ratio": best[1], "date": best[0], "ok": True}

    except Exception as e:  # noqa: BLE001
        print(f"[WARN] wantgoo margin ratio failed (HTTP {code}): {e}")
    return out


# ---------- 備援一：股市智投 stockintelli.com ----------

STOCKINTELLI_URL = "https://www.stockintelli.com/market/margin-trading"


def _stockintelli(t0: str, timeout: int = 20) -> dict:
    """stockintelli.com SSR 頁面爬蟲，回傳 {ratio, date, ok}。"""
    out = {"ratio": None, "date": None, "ok": False}
    code = None
    try:
        r = requests.get(STOCKINTELLI_URL, headers=UA, timeout=timeout)
        code = r.status_code
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
        print(f"[WARN] stockintelli margin ratio failed (HTTP {code}): {e}")
    return out


# ---------- 備援二：愛玩股 istock.tw ----------

ISTOCK_URL = "https://www.istock.tw/post/twmarginrequirement"


def _parse_istock_html(t0: str, html: str) -> dict:
    """解析 iStock 頁面；只取「上市櫃整體維持率」，並要求資料日期精確等於 T0。"""
    out = {"ratio": None, "date": None, "ok": False}
    text = re.sub(r"<script.*?</script>", " ", html, flags=re.S | re.I)
    text = re.sub(r"<style.*?</style>", " ", text, flags=re.S | re.I)
    text = unescape(re.sub(r"<[^>]+>", " ", text))
    text = re.sub(r"\s+", " ", text)

    date_match = re.search(r"(?:資料日期|更新日期)\s*[:：]?\s*(\d{4}-\d{2}-\d{2})", text)
    if not date_match:
        print("[INFO] istock 找不到資料日期")
        return out
    source_date = date_match.group(1)
    if source_date != t0:
        print(f"[INFO] istock 維持率日期 {source_date} 非 T0 ({t0})")
        return out

    # 頁面同時列上市、上櫃與上市櫃整體數值；不可誤取第一個（上市）百分比。
    total_marker = re.search(r"上市櫃整體維持率", text)
    if not total_marker:
        print("[INFO] istock 找不到上市櫃整體維持率欄位")
        return out
    segment = text[total_marker.end():date_match.start()]
    ratio_match = re.search(r"(\d{2,3}(?:\.\d+)?)\s*%", segment)
    if not ratio_match:
        print("[INFO] istock 上市櫃整體維持率數值解析失敗")
        return out
    ratio = float(ratio_match.group(1))
    if not 50 < ratio < 500:
        print(f"[INFO] istock 維持率數值異常: {ratio}")
        return out
    return {"ratio": ratio, "date": source_date, "ok": True}


def _istock(t0: str, timeout: int = 30) -> dict:
    """iStock SSR/HTML 備援；只回傳 T0 上市櫃整體維持率。"""
    out = {"ratio": None, "date": None, "ok": False}
    code = None
    try:
        istock_headers = {"User-Agent": UA["User-Agent"]}
        r = requests.get(ISTOCK_URL, headers=istock_headers, timeout=timeout)
        code = r.status_code
        r.raise_for_status()
        out = _parse_istock_html(t0, r.text)
    except Exception as e:  # noqa: BLE001
        print(f"[WARN] istock failed (HTTP {code}): {e}")
    return out


# ---------- 對外介面 ----------

def get(t0: str, timeout: int = 30) -> dict:
    """回傳上市櫃合計維持率；只接受 iStock 明確標示的「上市櫃整體維持率」與精確 T0 日期。

    WantGoo / StockIntelli 僅作上市單邊交叉參考，不得替代上市櫃合計值。
    """
    from concurrent.futures import ThreadPoolExecutor
    with ThreadPoolExecutor(max_workers=3) as ex:
        f_wg = ex.submit(_wantgoo, t0, timeout=min(timeout, 20))
        f_si = ex.submit(_stockintelli, t0, timeout=min(timeout, 15))
        f_is = ex.submit(_istock, t0, timeout=timeout)
        wg = f_wg.result()
        si = f_si.result()
        ist = f_is.result()

    # 這兩個來源的計算範圍尚未證實為上市櫃合計，只能交叉參考。
    if wg.get("ok") and wg.get("date") == t0:
        print(f"[INFO] wantgoo T0 參考值 {wg.get('ratio')}% (口徑未確認，不作上市櫃合計)")
    if si.get("ok") and si.get("date") == t0:
        print(f"[INFO] stockintelli T0 參考值 {si.get('ratio')}% (不作上市櫃合計)")

    if ist.get("ok") and ist.get("date") == t0:
        ist["source"] = "istock_combined"
        return ist

    print("[WARN] iStock 上市櫃整體維持率無精確 T0 值；不以上市單邊來源代替")
    return {"ratio": None, "date": None, "ok": False, "source": "unavailable"}
