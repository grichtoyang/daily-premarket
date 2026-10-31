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


def _tpex_footer_totals(table: dict[str, Any]) -> dict[str, Any]:
    """Extract TPEx market totals from the official JSON table's footers."""
    footers = table.get("footers")
    if not isinstance(footers, list):
        return {"available": False, "reason": "tables[0].footers missing"}
    result: dict[str, Any] = {"available": False, "raw_footers": footers}
    for row in footers:
        if not isinstance(row, list):
            continue
        if len(row) > 6 and str(row[1]).strip() == "融資金(仟元)":
            result.update({
                "available": True,
                "label": str(row[1]).strip(),
                "previous_financing_amount_thousand_ntd": row[2],
                "financing_buy_thousand_ntd": row[3],
                "financing_sell_thousand_ntd": row[4],
                "cash_repayment_thousand_ntd": row[5],
                "current_financing_amount_thousand_ntd": row[6],
            })
            break
    if not result["available"]:
        result["reason"] = "融資金(仟元) row not found in tables[0].footers"
    return result


def fetch(label: str, url: str, timeout: int = 30) -> Any:
    print(f"\\n[OFFICIAL-PROBE] {label}")
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
                    sample_rows = rows if label.startswith("TWSE margin") and index == 0 else rows[:2]
                    print(f"TABLE[{index}] title={table.get('title')} fields={json.dumps(fields, ensure_ascii=False)} rows={len(rows)} sample={json.dumps(sample_rows, ensure_ascii=False)}")
                    if label.startswith("TPEx legacy margin") and index == 0:
                        print("TPEX_OFFICIAL_TOTALS=" + json.dumps(
                            _tpex_footer_totals(table), ensure_ascii=False
                        )[:12000])
            for key in ("stat", "aaData", "tfootData_one", "tfootData_two", "data", "fields"):
                value = payload.get(key)
                if value is not None:
                    sample = value[:2] if isinstance(value, list) and key not in ("stat", "tfootData_one", "tfootData_two") else value
                    print(f"{key}={json.dumps(sample, ensure_ascii=False)[:12000]}")
            if label.startswith("TPEx legacy margin"):
                print("TPEx_PAYLOAD_META=" + json.dumps({
                    "date": payload.get("date"),
                    "stat_type": type(payload.get("stat")).__name__,
                    "stat_keys": list(payload.get("stat", {}).keys()) if isinstance(payload.get("stat"), dict) else None,
                    "table_count": len(payload.get("tables", [])) if isinstance(payload.get("tables"), list) else None,
                    "table_meta": [
                        {"title": table.get("title"), "keys": list(table.keys()),
                         "fields": table.get("fields"),
                         "rows": len(table.get("data") or []),
                         "last_rows": (table.get("data") or [])[-2:],
                         "footer": table.get("footer"), "footers": table.get("footers"),
                         "summary": table.get("summary"), "tfoot": table.get("tfoot")}
                        for table in (payload.get("tables") or []) if isinstance(table, dict)
                    ],
                }, ensure_ascii=False)[:20000])
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
        "https://www.tpex.org.tw/web/stock/margin_trading/margin_balance/margin_bal_result.php?"
        + urlencode({"l": "zh-tw", "o": "json", "d": roc, "s": "0,asc"})
    )
    tpex_margin_html = (
        "https://www.tpex.org.tw/web/stock/margin_trading/margin_balance/margin_bal_result.php?"
        + urlencode({"l": "zh-tw", "o": "htm", "d": roc, "s": "0,asc"})
    )
    tpex_margin_csv = (
        "https://www.tpex.org.tw/web/stock/margin_trading/margin_balance/margin_bal_result.php?"
        + urlencode({"l": "zh-tw", "o": "csv", "d": roc, "s": "0,asc"})
    )
    twse_prices = (
        "https://www.twse.com.tw/rwd/zh/afterTrading/MI_INDEX?"
        + urlencode({"date": date8, "type": "ALLBUT0999", "response": "json"})
    )
    tpex_prices = (
        "https://www.tpex.org.tw/web/stock/aftertrading/daily_trading_info/st43_result.php?"
        + urlencode({"l": "zh-tw", "o": "json", "d": roc, "s": "0,asc"})
    )
    tpex_openapi_margin = "https://www.tpex.org.tw/openapi/v1/tpex_mainboard_margin_balance"
    tpex_openapi_prices = "https://www.tpex.org.tw/openapi/v1/tpex_mainboard_daily_close_quotes"
    tpex_openapi_marginspot = "https://www.tpex.org.tw/openapi/v1/tpex_mainboard_margin_trading_marginspot"

    results = {
        "twse_margin": fetch("TWSE margin detail", twse_margin),
        "tpex_margin": fetch("TPEx legacy margin detail + totals", tpex_margin),
        "tpex_margin_html": fetch("TPEx margin HTML export (footer totals)", tpex_margin_html),
        "tpex_margin_csv": fetch("TPEx margin CSV export (footer totals)", tpex_margin_csv),
        "twse_prices": fetch("TWSE historical prices", twse_prices),
        "tpex_prices": fetch("TPEx legacy historical prices", tpex_prices),
        "tpex_openapi_margin": fetch("TPEx OpenAPI latest margin snapshot", tpex_openapi_margin),
        "tpex_openapi_prices": fetch("TPEx OpenAPI latest price snapshot", tpex_openapi_prices),
        "tpex_openapi_marginspot": fetch("TPEx OpenAPI margin trading balance overview", tpex_openapi_marginspot),
    }
    ok = all(results[name] is not None for name in ("twse_margin", "tpex_margin", "twse_prices", "tpex_prices"))
    openapi_meta = {}
    for name in ("tpex_openapi_margin", "tpex_openapi_prices"):
        payload = results[name]
        if isinstance(payload, list):
            dates = sorted({str(row.get("Date", "")).strip() for row in payload if isinstance(row, dict) and row.get("Date")})
            keys = list(payload[0].keys()) if payload and isinstance(payload[0], dict) else []
            openapi_meta[name] = {"rows": len(payload), "dates": dates[:5], "first_row_keys": keys}
        else:
            openapi_meta[name] = {"valid_list": False}
    marginspot_payload = results["tpex_openapi_marginspot"]
    marginspot_meta = {
        "is_list": isinstance(marginspot_payload, list),
        "rows": len(marginspot_payload) if isinstance(marginspot_payload, list) else None,
        "sample": marginspot_payload[:5] if isinstance(marginspot_payload, list) else None,
        "is_dict": isinstance(marginspot_payload, dict),
        "keys": list(marginspot_payload.keys()) if isinstance(marginspot_payload, dict) else None,
    }
    print("\\n[OFFICIAL-PROBE-SUMMARY] " + json.dumps({
        "date": date8, "roc_date": roc,
        "historical_four_endpoints_responded": ok,
        "responded": {key: value is not None for key, value in results.items()},
        "tpex_openapi_snapshot": openapi_meta,
        "tpex_openapi_marginspot": marginspot_meta,
    }, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
