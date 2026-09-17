"""HiStock (第三優先)：上市/上櫃融資融券金額口徑。

- 上市：https://histock.tw/stock/three.aspx?m=mg
- 上櫃：https://histock.tw/stock/three.aspx?m=mg&no=TWOI
表列：日期(MM/DD) / 融資餘額(億) / 融資增加(億) / 融券餘額(張) / 融券增加(張) / 價格 / 比例 / 成交量(億)
官方逐股加總僅有張數；金額口徑以此為主來源，失敗則回 None 由呼叫端標 unavailable。
"""
from __future__ import annotations
import re
import requests
from src.utils import HEADERS

UA = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"}
URLS = {"listed": "https://histock.tw/stock/three.aspx?m=mg",
        "otc": "https://histock.tw/stock/three.aspx?m=mg&no=TWOI"}

def _num(s: str):
    try:
        return float(str(s).replace(",", "").replace("%", "").strip() or "nan")
    except ValueError:
        return None

def _table(url: str, mmdd: str, timeout: int = 30) -> dict | None:
    try:
        r = requests.get(url, headers=UA, timeout=timeout)
        r.raise_for_status()
        rows = re.findall(r"<tr[^>]*>(.*?)</tr>", r.text, re.S)
        for rw in rows:
            if "<td" not in rw:
                continue
            cells = [re.sub(r"<[^>]+>", "", c).strip()
                     for c in re.findall(r"<td[^>]*>(.*?)</td>", rw, re.S)]
            if len(cells) >= 5 and cells[0] == mmdd:
                v = [_num(c) for c in cells[1:5]]
                if v[0] is None:
                    return None
                return {"fin_yi": v[0], "fin_chg_yi": v[1], "short_bal": v[2], "short_chg": v[3]}
    except Exception as e:  # noqa: BLE001
        print(f"[WARN] histock failed {url}: {e}")
    return None

def get(t0: str) -> dict:
    """{listed: {...}|None, otc: {...}|None}。mmdd 取自 T0。"""
    mmdd = f"{int(t0[5:7]):02d}/{int(t0[8:10]):02d}"
    return {"listed": _table(URLS["listed"], mmdd), "otc": _table(URLS["otc"], mmdd)}
