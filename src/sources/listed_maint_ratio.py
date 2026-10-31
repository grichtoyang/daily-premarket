"""TWSE listed-only market-wide margin maintenance ratio estimate."""
from __future__ import annotations
import math
import time
import ast
from concurrent.futures import ThreadPoolExecutor, as_completed, TimeoutError as FuturesTimeoutError
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


def _month_start(date8, offset):
    year, month = int(date8[:4]), int(date8[4:6])
    month -= offset
    while month <= 0:
        year -= 1
        month += 12
    return f"{year:04d}{month:02d}01"


def _last_valid_close(code, date8, timeout=2, max_months=12, deadline=None):
    """Return the most recent TWSE traded close on/before date8 within the shared deadline."""
    for offset in range(max_months):
        remaining = (deadline - time.monotonic()) if deadline is not None else timeout
        if remaining <= 0:
            return None
        month_date = _month_start(date8, offset)
        url = BASE + "/afterTrading/STOCK_DAY?" + urlencode(
            {"date": month_date, "stockNo": code, "response": "json"})
        try:
            response = requests.get(url, headers=HEADERS, timeout=min(float(timeout), remaining))
            response.raise_for_status()
            payload = response.json()
        except Exception:
            continue
        rows = payload.get("data") or []
        fields = payload.get("fields") or []
        date_idx = fields.index("日期") if "日期" in fields else 0
        close_idx = fields.index("收盤價") if "收盤價" in fields else 6
        valid = []
        for row in rows:
            if not isinstance(row, list) or len(row) <= max(date_idx, close_idx):
                continue
            try:
                close = _num(row[close_idx])
            except ValueError:
                continue
            roc_date = str(row[date_idx]).strip()
            try:
                y, m, d = roc_date.split("/")
                row_date = f"{int(y) + 1911:04d}{int(m):02d}{int(d):02d}"
            except Exception:
                continue
            if row_date <= date8 and close > 0:
                valid.append((row_date, close))
        if valid:
            return max(valid, key=lambda item: item[0])
    return None

def calculate(t0, margin_payload, price_payload, historical_prices=None):
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
                          and (t.get("fields") or []).count("今日餘額") >= 2), None)
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
    # MI_MARGN repeats "今日餘額": first is financing, second is short.
    financing_balance_idx = [i for i, field in enumerate(balance_fields)
                             if field == "今日餘額"][0]
    code_idx = balance_fields.index("代號")
    historical_prices = historical_prices or {}
    collateral = 0.0
    financed = 0
    missing = []
    price_dates = {}
    stale_price_codes = []
    for raw_row in balance_table.get("data") or []:
        if isinstance(raw_row, dict):
            code = str(raw_row.get("代號", "")).strip()
            raw_lots = raw_row.get("融資今日餘額", raw_row.get("今日餘額"))
        elif isinstance(raw_row, list) and len(raw_row) > max(code_idx, financing_balance_idx):
            code = str(raw_row[code_idx]).strip()
            raw_lots = raw_row[financing_balance_idx]
        else:
            continue
        try:
            lots = _num(raw_lots)
        except ValueError:
            continue
        if not code or lots <= 0:
            continue
        financed += 1
        close = prices.get(code)
        price_date = _date(t0)
        if close is None:
            historical = historical_prices.get(code)
            if historical:
                price_date, close = historical
                stale_price_codes.append(code)
        if close is None:
            missing.append(code)
        else:
            collateral += lots * 1000 * close
            price_dates[code] = price_date

    if financed == 0:
        raise ValueError("no positive listed financing balance rows")
    if missing:
        raise ValueError(f"listed securities missing T0 close: {missing}")
    ratio = collateral / financing_amount * 100
    return {
        "ok": True, "date": t0, "ratio": round(ratio, 4),
        "numerator_collateral_value_ntd": round(collateral, 2),
        "denominator_financing_amount_ntd": round(financing_amount, 2),
        "financed_security_count": financed, "priced_security_count": financed,
        "coverage": 1.0, "market": "listed",
        "stale_price_security_count": len(stale_price_codes),
        "stale_price_security_codes": stale_price_codes,
        "price_date_min": min(price_dates.values()) if price_dates else None,
        "price_date_max": max(price_dates.values()) if price_dates else None,
        "method": "TWSE listed financing balance lots x latest available close on/before T0 / TWSE listed financing amount",
        "classification": "listed_market_estimate_not_individual_account_ratio",
    }


def get(t0, timeout=6):
    """Fetch and calculate the TWSE listed ratio under one total wall-clock budget.

    The two primary TWSE requests and any historical-close lookups share this
    deadline. Historical lookups run concurrently and are capped at 20 symbols;
    if the complete listed universe cannot be valued, the caller uses fallback.
    """
    date8 = _date(t0)
    deadline = time.monotonic() + max(0.1, float(timeout))
    urls = (
        BASE + "/marginTrading/MI_MARGN?" + urlencode(
            {"date": date8, "selectType": "ALL", "response": "json"}),
        BASE + "/afterTrading/MI_INDEX?" + urlencode(
            {"date": date8, "type": "ALLBUT0999", "response": "json"}),
    )
    try:
        payloads = []
        for url in urls:
            remaining = deadline - time.monotonic()
            if remaining <= 0:
                raise TimeoutError("TWSE self-built ratio total time budget exceeded")
            response = requests.get(url, headers=HEADERS, timeout=min(3.0, remaining))
            response.raise_for_status()
            payloads.append(response.json())

        try:
            return calculate(t0, payloads[0], payloads[1])
        except ValueError as exc:
            marker = "listed securities missing T0 close: "
            if marker not in str(exc):
                raise
            missing_codes = ast.literal_eval(str(exc).split(marker, 1)[1].strip())
            if not missing_codes:
                raise
            if len(missing_codes) > 20:
                raise ValueError(
                    f"historical close lookup cap exceeded ({len(missing_codes)} symbols); "
                    "skip self-built result and use fallback"
                )
            remaining = deadline - time.monotonic()
            if remaining <= 0:
                raise TimeoutError("TWSE self-built ratio time budget exhausted before historical prices")

            historical = {}
            executor = ThreadPoolExecutor(max_workers=min(8, len(missing_codes)))
            futures = {
                executor.submit(
                    _last_valid_close, code, date8, timeout=2.0,
                    max_months=12, deadline=deadline
                ): code
                for code in missing_codes
            }
            try:
                for future in as_completed(futures, timeout=max(0.05, remaining)):
                    code = futures[future]
                    try:
                        found = future.result()
                        if found:
                            historical[code] = found
                    except Exception:
                        continue
            except FuturesTimeoutError:
                pass
            finally:
                # Do not block the caller after the shared deadline has expired.
                # Each worker's HTTP request is itself capped by that deadline.
                executor.shutdown(wait=False, cancel_futures=True)

            return calculate(t0, payloads[0], payloads[1], historical_prices=historical)
    except Exception as exc:
        return {"ok": False, "date": t0, "ratio": None,
                "reason": f"{type(exc).__name__}: {exc}"}
