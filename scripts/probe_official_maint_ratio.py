#!/usr/bin/env python3
"""Probe official TWSE/TPEx historical margin endpoints without calculating a ratio.

This is a schema/date diagnostic only. It deliberately does not write dashboard data.
"""
from __future__ import annotations

import argparse
import json
from datetime import date
from typing import Any
from urllib.parse import urlencode

import requests

HEADERS = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 Chrome/120 Safari/537.36",
    "Accept": "application/json,text/plain,*/*",
    "Referer": "https://www.twse.com.tw/",
}
ROC = lambda d: f"{d.year - 1911:03d}/{d.month:02d}/{d.day:02d}"


def fetch(label: str, url: str, timeout: int = 30) -> Any:
    print(f"\n[OFFICIAL-PROBE] {label}")
    print(f"URL={url}")
    try:
        response = requests.get(url, headers=HEADERS, timeout=timeout)
        print(f"HTTP={response.status_code} bytes={len(response.content)} content_type={response.headers.get('content-type')}")
        response.raise_for_status()
        payload = response.json()
        if isinstance(payload, dict):
            print("TOP_KEYS=" + json.dumps(list(payload.keys()), ensure_ascii=False))
            tables = payload.get("tables")
            if isinstance(tables, list):
                for index, table in enumerate(tables):
                    if not isinstance(table, dict):
                        continue
                    fields = table.get("fields") or []
                    rows = table.get("data") or []
                    print(f"TABLE[{index}] title={table.get('title')} fields={json.dumps(fields, ensure_ascii=False)} rows={len(rows)} sample={json.dumps(rows[:2], ensure_ascii=False)}")
            for key in ("aaData", "tfootData_one", "tfootData_two", "data", "fields"):
                value = payload.get(key)
                if value is not None:
                    sample = value[:2] if isinstance(value, list) else value
                    print(f"{key}={json.dumps(sample, ensure_ascii=False)[:5000]}")
        elif isinstance(payload, list):
            print(f"ROWS={len(payload)}")
            if payload:
                print("FIRST_ROW_KEYS=" + json.dumps(list(payload[0].keys()) if isinstance(payload[0], dict) else [], ensure_ascii=False))
                print("SAMPLE=" + json.dumps(payload[:2], ensure_ascii=False)[:5000])
        else:
            print(f"PAYLOAD_TYPE={type(payload).__name__} VALUE={str(payload)[:1000]}")
        return payload
    except Exception as exc:  # noqa: BLE001
        print(f"[OFFICIAL-PROBE-ERROR] {label}: {type(exc).__name__}: {exc}")
        return None


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--date", required=True, help="Trading date YYYYMMDD")
    args = parser.parse_args()
    if len(args.date) != 8 or not args.date.isdigit():
        raise SystemExit("--date must be YYYYMMDD")
    d = date(int(args.date[:4]), int(args.date[4:6]), int(args.date[6:8]))
    date8 = args.date
    roc = ROC(d)

    twse_margin = (
        "https://www.twse.com.tw/rwd/zh/marginTrading/MI_MARGN?"
        + urlencode({"date": date8, "selectType": "ALL", "response": "json"})
    )
    tpex_margin = (
        "https://www.tpex.org.tw/web/stock/margin_trading/margin_bal_result.php?"
        + urlencode({"l": "zh-tw", "o": "json", "d": roc, "s": "0,asc"})
    )
    # Historical daily market quote endpoints are probed separately from margin.
    twse_prices = (
        "https://www.twse.com.tw/rwd/zh/afterTrading/MI_INDEX?"
        + urlencode({"date": date8, "type": "ALLBUT0999", "response": "json"})
    )
    tpex_prices = (
        "https://www.tpex.org.tw/web/stock/aftertrading/daily_trading_info/st43_result.php?"
        + urlencode({"l": "zh-tw", "o": "json", "d": roc, "s": "0,asc"})
    )

    results = {
        "twse_margin": fetch("TWSE margin detail", twse_margin),
        "tpex_margin": fetch("TPEx margin detail + totals", tpex_margin),
        "twse_prices": fetch("TWSE historical prices", twse_prices),
        "tpex_prices": fetch("TPEx historical prices", tpex_prices),
    }
    ok = all(results[name] is not None for name in ("twse_margin", "tpex_margin", "twse_prices", "tpex_prices"))
    print("\n[OFFICIAL-PROBE-SUMMARY] " + json.dumps({
        "date": date8, "roc_date": roc, "all_four_endpoints_responded": ok,
        "responded": {key: value is not None for key, value in results.items()},
    }, ensure_ascii=False))
    # Diagnostic probe is non-blocking initially; endpoint payloads must be reviewed before production use.
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
