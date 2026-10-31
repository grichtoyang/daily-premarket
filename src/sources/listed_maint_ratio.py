"""TWSE listed-only market-wide margin maintenance ratio estimate."""
from __future__ import annotations
import math
from urllib.parse import urlencode
import requests

HEADERS = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 Chrome/120 Safari/537.36",
    "Accept": "application/json,text/plain,*/*",
    "Referer": "https://www.twse.com.tw/",
}
BASE = "https://www.twse.com.tw/rwd/zh"


def _date(value):
    return str(value or "").strip().replace("/", "").replace("-", "")


def _num(value):
    raw = str(value if value is not None else "").strip().replace(",", "").replace("%", "")
    if raw in {"", "--", "---", "-", "N/A", "null", "None"}:
        raise ValueError("missing numeric value")
    value = float(raw)
    if not math.isfinite(value):
        raise ValueError("non-finite numeric value")
    return value


def _records(table):
    fields, data = table.get("fields"), table.get("data")
    if not isinstance(fields, list) or not isinstance(data, list):
        raise ValueError("TWSE table fields/data missing")
    return [row if isinstance(row, dict) else dict(zip(fields, row))
            for row in data if isinstance(row, dict) or
            (isinstance(row, list) and len(row) >= len(fields))]


def calculate(t0, margin_payload, price_payload):
    """T0 listed collateral market value / T0 listed financing amount."""
    expected = _date(t0)
    for label, payload in (("TWSE margin", margin_payload), ("TWSE prices", price_payload)):
        if not isinstance(payload, dict) or _date(payload.get("date")) != expected:
            got = _date(payload.get("date")) if isinstance(payload, dict) else ""
            raise ValueError(f"{label} date mismatch: {got or 'missing'} != {expected}")
        if not isinstance(payload.get("tables"), list):
            raise ValueError(f"{label} tables missing")

    mtables, ptables = margin_payload["tables"], price_payload["tables"]
    balance_table = next((t for t in mtables if "代號" in (t.get("fields") or [])
                          and ("融資今日餘額" in (t.get("fields") or [])
                               or "融資餘額" in (t.get("fields") or []))), None)
    price_table = next((t for t in ptables if "證券代號" in (t.get("fields") or [])
                        and "收盤價" in (t.get("fields") or [])), None)
    if balance_table is None or price_table is None:
        raise ValueError("required TWSE listed balance/close table missing")

    financing_amount = None
    for table in mtables:
        fields = table.get("fields") or []
        if "項目" not in fields or "今日餘額" not in fields:
            continue
        for row in _records(table):
            if str(row.get("項目", "")).strip() == "融資金額(仟元)":
                financing_amount = _num(row.get("今日餘額")) * 1000
                break
    if financing_amount is None or financing_amount <= 0:
        raise ValueError("TWSE listed financing amount missing/non-positive")

    prices = {}
    for row in _records(price_table):
        code = str(row.get("證券代號", "")).strip()
        try:
            close = _num(row.get("收盤價"))
        except ValueError:
            continue
        if code and close > 0:
            prices[code] = close

    balance_fields = balance_table.get("fields") or []
    balance_key = ("融資今日餘額" if "融資今日餘額" in balance_fields
                   else "融資餘額")
    collateral = 0.0
    financed = 0
    missing = []
    for row in _records(balance_table):
        code = str(row.get("代號", "")).strip()
        try:
            lots = _num(row.get(balance_key))
        except ValueError:
            continue
        if not code or lots <= 0:
            continue
        financed += 1
        close = prices.get(code)
        if close is None:
            missing.append(code)
        else:
            collateral += lots * 1000 * close

    if financed == 0:
        raise ValueError("no positive listed financing balance rows")
    if missing:
        raise ValueError(f"listed securities missing T0 close: {missing[:30]}")
    ratio = collateral / financing_amount * 100
    return {
        "ok": True, "date": t0, "ratio": round(ratio, 4),
        "numerator_collateral_value_ntd": round(collateral, 2),
        "denominator_financing_amount_ntd": round(financing_amount, 2),
        "financed_security_count": financed, "priced_security_count": financed,
        "coverage": 1.0, "market": "listed",
        "method": "TWSE listed financing balance lots x same-day close / TWSE listed financing amount",
        "classification": "listed_market_estimate_not_individual_account_ratio",
    }


def get(t0, timeout=4):
    """Fetch exactly two TWSE T0 endpoints, once each; fail fast to caller fallback."""
    date8 = _date(t0)
    urls = (
        BASE + "/marginTrading/MI_MARGN?" + urlencode(
            {"date": date8, "selectType": "ALL", "response": "json"}),
        BASE + "/afterTrading/MI_INDEX?" + urlencode(
            {"date": date8, "type": "ALLBUT0999", "response": "json"}),
    )
    try:
        payloads = []
        for url in urls:
            response = requests.get(url, headers=HEADERS, timeout=timeout)
            response.raise_for_status()
            payloads.append(response.json())
        return calculate(t0, payloads[0], payloads[1])
    except Exception as exc:
        return {"ok": False, "date": t0, "ratio": None,
                "reason": f"{type(exc).__name__}: {exc}"}
