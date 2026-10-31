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

def _norm_date(value: object) -> str:
    raw = str(value or "").strip().replace("/", "").replace("-", "")
    if len(raw) == 7 and raw.isdigit():
        return str(int(raw[:3]) + 1911) + raw[3:]
    return raw


def _missing_codes(margin_payload: dict, price_payload: dict, market: str) -> set[str]:
    tables = margin_payload.get("tables") or []
    price_tables = price_payload.get("tables") or []
    if not tables or not price_tables:
        raise RuntimeError(f"{market}: required tables missing during fallback discovery")
    margin_table = next((t for t in tables if "今日餘額" in (t.get("fields") or [])
                         or "資餘額" in (t.get("fields") or [])), None)
    price_table = next((t for t in price_tables if ("證券代號" in (t.get("fields") or [])
                        and "收盤價" in (t.get("fields") or []))
                        or ("代號" in (t.get("fields") or []) and "收盤" in (t.get("fields") or []))), None)
    if margin_table is None or price_table is None:
        raise RuntimeError(f"{market}: unable to identify margin/price tables for fallback")
    mf, pf = margin_table["fields"], price_table["fields"]
    balance_field = "今日餘額" if "今日餘額" in mf else "資餘額"
    margin_code_field = "代號" if "代號" in mf else "證券代號"
    price_code_field = "證券代號" if "證券代號" in pf else "代號"
    close_field = "收盤價" if "收盤價" in pf else "收盤"
    priced = set()
    for row in price_table.get("data") or []:
        if isinstance(row, list) and len(row) >= len(pf):
            item = dict(zip(pf, row))
        elif isinstance(row, dict):
            item = row
        else:
            continue
        code = str(item.get(price_code_field, "")).strip()
        try:
            close = float(str(item.get(close_field, "")).replace(",", ""))
        except (TypeError, ValueError):
            continue
        if code and close > 0:
            priced.add(code)
    missing = set()
    for row in margin_table.get("data") or []:
        if isinstance(row, list) and len(row) >= len(mf):
            item = dict(zip(mf, row))
        elif isinstance(row, dict):
            item = row
        else:
            continue
        code = str(item.get(margin_code_field, "")).strip()
        try:
            balance = float(str(item.get(balance_field, "")).replace(",", ""))
        except (TypeError, ValueError):
            continue
        if code and balance > 0 and code not in priced:
            missing.add(code)
    return missing


def fetch_prior_official_closes(market: str, missing_codes: set[str], t0_date: date,
                                max_calendar_days: int = 10) -> dict[str, dict]:
    """Resolve no-trade securities from dated official historical daily-close files."""
    unresolved = set(missing_codes)
    resolved: dict[str, dict] = {}
    for offset in range(1, max_calendar_days + 1):
        if not unresolved:
            break
        prior = date.fromordinal(t0_date.toordinal() - offset)
        date8 = prior.strftime("%Y%m%d")
        roc = f"{prior.year - 1911:03d}/{prior.month:02d}/{prior.day:02d}"
        if market == "twse":
            url = "https://www.twse.com.tw/rwd/zh/afterTrading/MI_INDEX?" + urlencode(
                {"date": date8, "type": "ALLBUT0999", "response": "json"})
            code_field, close_field = "證券代號", "收盤價"
        else:
            url = "https://www.tpex.org.tw/web/stock/aftertrading/daily_close_quotes/stk_quote_result.php?" + urlencode(
                {"l": "zh-tw", "o": "json", "d": roc, "s": "0,asc,0"})
            code_field, close_field = "代號", "收盤"
        try:
            payload = fetch_json(f"{market} prior close {date8}", url)
        except Exception as exc:  # skip non-trading dates / unavailable archive days
            print(f"[OFFICIAL-PRIOR-CLOSE] market={market} requested={date8} unavailable={type(exc).__name__}: {exc}")
            continue
        returned_date = _norm_date(payload.get("date"))
        if returned_date != date8:
            print(f"[OFFICIAL-PRIOR-CLOSE] market={market} requested={date8} returned={returned_date or 'EMPTY'}; skipped")
            continue
        for table in payload.get("tables") or []:
            fields = table.get("fields") or []
            if code_field not in fields or close_field not in fields:
                continue
            for row in table.get("data") or []:
                if isinstance(row, list) and len(row) >= len(fields):
                    item = dict(zip(fields, row))
                elif isinstance(row, dict):
                    item = row
                else:
                    continue
                code = str(item.get(code_field, "")).strip()
                if code not in unresolved:
                    continue
                try:
                    close = float(str(item.get(close_field, "")).replace(",", ""))
                except (TypeError, ValueError):
                    continue
                if close > 0:
                    resolved[code] = {"close": close, "date": date8}
                    unresolved.remove(code)
        if resolved:
            print(f"[OFFICIAL-PRIOR-CLOSE] market={market} requested={date8} newly_resolved={len(resolved)} remaining={len(unresolved)}")
    if unresolved:
        raise RuntimeError(
            f"{market}: no official close found within {max_calendar_days} calendar days "
            f"for codes={sorted(unresolved)[:50]}")
    return resolved


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

    fallback_prices = {}
    for market, margin_name, price_name in (
        ("twse", "twse_margin", "twse_prices"),
        ("tpex", "tpex_margin", "tpex_prices"),
    ):
        missing_codes = _missing_codes(payloads[margin_name], payloads[price_name], market)
        if missing_codes:
            print(f"[OFFICIAL-PRIOR-CLOSE] market={market} missing_t0_codes={sorted(missing_codes)}")
            fallback_prices[market] = fetch_prior_official_closes(market, missing_codes, d)
    result = calculate(t0, roc, payloads["twse_margin"], payloads["tpex_margin"],
                       payloads["twse_prices"], payloads["tpex_prices"], fallback_prices)
    print("[OFFICIAL-MAINT-RATIO] " + json.dumps(result, ensure_ascii=False, sort_keys=True))
    if result.get("coverage") != 1.0:
        raise SystemExit("Official maintenance ratio coverage is not 100%; refusing PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
