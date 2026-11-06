"""美國國債殖利率：Treasury FiscalData API (主) → Treasury XML / Yahoo (備援)。

- 主：FiscalData 候選端點 (波動大，失敗即備援，不中斷)
- 備援：Treasury yield.xml 支援 2Y／20Y；Yahoo ^TNX (10Y)、^TYX (30Y)
- 日變化單位：百分點
"""
from __future__ import annotations
from datetime import datetime, timezone
from src.sources.us_market import quote


def _retrieved_at() -> str:
    """Return the UTC timestamp when the upstream response was received."""
    return datetime.now(timezone.utc).isoformat(timespec="seconds")

CANDIDATES = [
    "https://api.fiscaldata.treasury.gov/services/api/fiscal_service/v2/accounting/od/daily_treasury_yield_curve?sort=-record_date&page[size]=3",
    "https://api.fiscaldata.treasury.gov/services/api/fiscal_service/v1/accounting/od/daily_treasury_yield_curve?sort=-record_date&page[size]=3",
]
YIELD_XML = "https://home.treasury.gov/sites/default/files/interest-rates/yield.xml"

def _treasury() -> dict | None:
    import requests
    from src.utils import HEADERS
    for url in CANDIDATES:
        try:
            r = requests.get(url, headers={**HEADERS, "Accept": "application/json"}, timeout=20)
            if r.status_code != 200:
                continue
            retrieved_at = _retrieved_at()
            rows = r.json().get("data") or []
            if len(rows) < 1:
                continue
            last, prev = rows[0], rows[1] if len(rows) > 1 else rows[0]
            def y(row, *keys):
                for k in keys:
                    for kk in (k, k.replace(" ", "_"), k.lower()):
                        if row.get(kk) not in (None, ""):
                            try:
                                return float(row[kk])
                            except (ValueError, TypeError):
                                pass
                return None
            out = {}
            for label, keys in (
                ("2Y", ("2 Yr", "2yr", "bc_2year")),
                ("10Y", ("10 Yr", "10yr", "bc_10year")),
                ("20Y", ("20 Yr", "20yr", "bc_20year")),
                ("30Y", ("30 Yr", "30yr", "bc_30year")),
            ):
                v, p = y(last, *keys), y(prev, *keys)
                out[label] = {"yield": v, "chg": (v - p) if v is not None and p is not None else None,
                              "date": last.get("record_date"), "retrieved_at": retrieved_at,
                              "source": "U.S. Treasury FiscalData API", "ok": v is not None}
            if any(v["ok"] for v in out.values()):
                return out
        except Exception as e:  # noqa: BLE001
            print(f"[WARN] treasury {url[:60]} failed: {e}")
            continue
    return None

def _xml_yield(field: str):
    """Treasury yield.xml 備援：指定 BC_* 欄位，取最新與前一筆有效值。"""
    import re
    from src.utils import HEADERS
    import requests
    try:
        r = requests.get(YIELD_XML, headers={**HEADERS, "Accept": "application/xml"}, timeout=30)
        r.raise_for_status()
        retrieved_at = _retrieved_at()
        bodies = re.findall(r"<G_NEW_DATE>(.*?)</G_NEW_DATE>", r.text, re.S)
        rows = []
        for b in bodies:
            d = re.search(r"<BID_CURVE_DATE>(.*?)</BID_CURVE_DATE>", b)
            v = re.search(rf"<{re.escape(field)}>(.*?)</{re.escape(field)}>", b)
            if d and v:
                try:
                    rows.append((d.group(1).strip(), float(v.group(1).strip())))
                except ValueError:
                    pass
        if rows:
            first = rows[-1]
            prev = rows[-2] if len(rows) > 1 else rows[-1]
            return {"yield": first[1], "chg": first[1] - prev[1], "date": first[0],
                    "retrieved_at": retrieved_at,
                    "source": f"U.S. Treasury yield.xml（{field} 備援）", "ok": True}
    except Exception as e:  # noqa: BLE001
        print(f"[WARN] treasury xml {field} failed: {e}")
    return {"yield": None, "chg": None, "date": None, "retrieved_at": None,
            "source": "unavailable", "ok": False}

def get_yields() -> dict:
    """{2Y/10Y/20Y/30Y: {yield, chg(百分點), date, source, ok}}。"""
    t = _treasury()
    if t is not None:
        return t
    print("[INFO] Treasury API 不可用，改用 Treasury XML + Yahoo 備援")
    out = {"2Y": _xml_yield("BC_2YEAR"), "20Y": _xml_yield("BC_20YEAR")}
    for label, sym in (("10Y", "^TNX"), ("30Y", "^TYX")):
        q = quote(sym)
        out[label] = {"yield": q["price"], "chg": q["change"], "date": q["date"],
                      "retrieved_at": q.get("retrieved_at"),
                      "source": "Yahoo Finance (備援)", "ok": q["ok"]}
    return out
