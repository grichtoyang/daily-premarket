#!/usr/bin/env python3
"""Fetch same-day official TWSE/TPEx margin and close data, then calculate market-wide estimate."""
from __future__ import annotations

import argparse
import json
from datetime import date
from urllib.parse import urlencode

import requests

from src.sources.official_maint_ratio import calculate

HEADERS = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 Chrome/120 Safari/537.36",
    "Accept": "application/json,text/plain,*/*",
    "Referer": "https://www.twse.com.tw/",
}


def fetch_json(label: str, url: str, timeout: int = 45) -> dict:
    response = requests.get(url, headers=HEADERS, timeout=timeout)
    response.raise_for_status()
    try:
        payload = response.json()
    except ValueError as exc:
        raise RuntimeError(f"{label}: response is not JSON (HTTP {response.status_code})") from exc
    if not isinstance(payload, dict):
        raise RuntimeError(f"{label}: expected JSON object, got {type(payload).__name__}")
    return payload


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--date", required=True, help="T0 date YYYYMMDD")
    args = parser.parse_args()
    if len(args.date) != 8 or not args.date.isdigit():
        raise SystemExit("--date must be YYYYMMDD")
    d = date(int(args.date[:4]), int(args.date[4:6]), int(args.date[6:8]))
    t0 = d.isoformat()
    roc = f"{d.year - 1911:03d}/{d.month:02d}/{d.day:02d}"

    urls = {
        "twse_margin": "https://www.twse.com.tw/rwd/zh/marginTrading/MI_MARGN?" + urlencode(
            {"date": args.date, "selectType": "ALL", "response": "json"}),
        "tpex_margin": "https://www.tpex.org.tw/web/stock/margin_trading/margin_balance/margin_bal_result.php?" + urlencode(
            {"l": "zh-tw", "o": "json", "d": roc, "s": "0,asc"}),
        "twse_prices": "https://www.twse.com.tw/rwd/zh/afterTrading/MI_INDEX?" + urlencode(
            {"date": args.date, "type": "ALLBUT0999", "response": "json"}),
        "tpex_prices": "https://www.tpex.org.tw/web/stock/aftertrading/daily_close_quotes/stk_quote_result.php?" + urlencode(
            {"l": "zh-tw", "o": "json", "d": roc, "s": "0,asc,0"}),
    }

    payloads = {}
    for name, url in urls.items():
        payloads[name] = fetch_json(name, url)
        tables = payloads[name].get("tables")
        row_count = sum(len(t.get("data") or []) for t in tables if isinstance(t, dict)) if isinstance(tables, list) else 0
        print(f"[OFFICIAL-DATA] {name}: date={payloads[name].get('date')} tables={len(tables) if isinstance(tables, list) else 0} rows={row_count}")

    result = calculate(t0, roc, payloads["twse_margin"], payloads["tpex_margin"],
                       payloads["twse_prices"], payloads["tpex_prices"])
    print("[OFFICIAL-MAINT-RATIO] " + json.dumps(result, ensure_ascii=False, sort_keys=True))
    if result.get("coverage") != 1.0:
        raise SystemExit("Official maintenance ratio coverage is not 100%; refusing PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
