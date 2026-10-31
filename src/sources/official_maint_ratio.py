"""Official TWSE + TPEx market-wide margin maintenance ratio estimator.

All inputs must be same-day T0 official payloads. This is a market-wide
collateral-value / financing-amount estimate, not an individual account ratio.
"""
from __future__ import annotations

from typing import Any


def _normalize_date(value: Any) -> str:
    """Normalize Gregorian YYYYMMDD and ROC YYYMMDD dates to Gregorian YYYYMMDD."""
    raw = str(value or "").strip().replace("/", "").replace("-", "").replace(".", "")
    if len(raw) == 7 and raw.isdigit():
        return str(int(raw[:3]) + 1911) + raw[3:]
    if len(raw) == 8 and raw.isdigit():
        return raw
    return raw


def _number(value: Any) -> float:
    text = str(value).strip().replace(",", "").replace("%", "")
    if text in {"", "--", "---", "-", "N/A", "null", "None"}:
        raise ValueError("missing numeric value")
    return float(text)


def _tables(payload: dict, expected_date: str, label: str) -> list[dict]:
    if not isinstance(payload, dict):
        raise ValueError(f"{label}: payload is not an object")
    got = _normalize_date(payload.get("date", ""))
    expected = _normalize_date(expected_date)
    if got and got != expected:
        raise ValueError(f"{label}: date mismatch {got} != {expected}")
    tables = payload.get("tables")
    if not isinstance(tables, list):
        raise ValueError(f"{label}: tables missing")
    return [t for t in tables if isinstance(t, dict)]


def _records(table: dict) -> list[dict]:
    fields, data = table.get("fields"), table.get("data")
    if not isinstance(fields, list) or not isinstance(data, list):
        raise ValueError("table fields/data missing")
    names = [str(x).strip() for x in fields]
    result = []
    for row in data:
        if isinstance(row, dict):
            result.append({str(k).strip(): v for k, v in row.items()})
        elif isinstance(row, list) and len(row) >= len(names):
            result.append(dict(zip(names, row)))
    return result


def _find_table(tables: list[dict], *required_fields: str) -> dict:
    for table in tables:
        fields = [str(x).strip() for x in (table.get("fields") or [])]
        if all(field in fields for field in required_fields):
            return table
    raise ValueError(f"table containing fields {required_fields!r} not found")


def _sum_market_value(margin_table: dict, price_table: dict, balance_field: str,
                      code_field: str, close_field: str, market: str) -> dict:
    balances = _records(margin_table)
    prices = _records(price_table)
    price_map = {}
    for row in prices:
        code = str(row.get(code_field, "")).strip()
        if code:
            try:
                price_map[code] = _number(row.get(close_field))
            except ValueError:
                continue

    total = 0.0
    positive_count = 0
    missing = []
    for row in balances:
        code = str(row.get("代號", row.get("證券代號", ""))).strip()
        if not code:
            continue
        try:
            lots = _number(row.get(balance_field))
        except ValueError:
            continue
        if lots <= 0:
            continue
        positive_count += 1
        close = price_map.get(code)
        if close is None or close <= 0:
            missing.append(code)
            continue
        total += lots * 1000.0 * close

    return {
        "market": market,
        "financed_security_count": positive_count,
        "priced_security_count": positive_count - len(missing),
        "missing_price_codes": missing,
        "collateral_value_ntd": total,
    }


def _twse_financing_amount(payload: dict, t0: str) -> float:
    tables = _tables(payload, t0, "TWSE margin")
    for table in tables:
        fields = [str(x).strip() for x in (table.get("fields") or [])]
        rows = table.get("data") or []
        if "項目" not in fields or "今日餘額" not in fields:
            continue
        idx_label, idx_today = fields.index("項目"), fields.index("今日餘額")
        for row in rows:
            if isinstance(row, list) and len(row) > max(idx_label, idx_today):
                if str(row[idx_label]).strip() == "融資金額(仟元)":
                    return _number(row[idx_today]) * 1000.0
    raise ValueError("TWSE current financing amount row not found")


def _tpex_financing_amount(payload: dict, t0_roc: str) -> float:
    if not isinstance(payload, dict):
        raise ValueError("TPEx margin payload is not an object")
    got = _normalize_date(payload.get("date", ""))
    expected = _normalize_date(t0_roc)
    if got and got != expected:
        raise ValueError(f"TPEx margin date mismatch {got} != {expected}")
    tables = payload.get("tables") or []
    if not tables:
        raise ValueError("TPEx margin tables missing")
    summary = tables[0].get("summary")
    if not isinstance(summary, list):
        raise ValueError("TPEx margin summary missing")
    for row in summary:
        if isinstance(row, list) and len(row) > 6 and str(row[1]).strip() == "融資金(仟元)":
            return _number(row[6]) * 1000.0
    raise ValueError("TPEx current financing amount summary missing")


def calculate(t0: str, t0_roc: str, twse_margin: dict, tpex_margin: dict,
              twse_prices: dict, tpex_prices: dict) -> dict:
    """Calculate only when all four sources are present, same-day and fully priced."""
    date8 = t0.replace("-", "")
    twm = _tables(twse_margin, date8, "TWSE margin")
    twp = _tables(twse_prices, date8, "TWSE prices")
    txp = _tables(tpex_prices, date8, "TPEx prices")
    tw_margin_table = _find_table(twm, "代號", "今日餘額")
    tw_price_table = _find_table(twp, "證券代號", "收盤價")
    tx_margin_tables = _tables(tpex_margin, t0_roc, "TPEx margin")
    tx_margin_table = _find_table(tx_margin_tables, "代號", "資餘額")
    tx_price_table = _find_table(txp, "代號", "收盤")

    # Diagnose market-universe mismatches before calculating. Do not silently
    # cross-map prices: that could double-count a security across exchanges.
    tw_margin_rows = _records(tw_margin_table)
    tx_margin_rows = _records(tx_margin_table)
    tw_price_rows = _records(tw_price_table)
    tx_price_rows = _records(tx_price_table)

    def _code(row: dict) -> str:
        return str(row.get("代號", row.get("證券代號", ""))).strip()

    def _positive_codes(rows: list[dict], balance_field: str) -> set[str]:
        codes = set()
        for row in rows:
            code = _code(row)
            try:
                balance = _number(row.get(balance_field))
            except ValueError:
                continue
            if code and balance > 0:
                codes.add(code)
        return codes

    tw_price_codes = {_code(row) for row in tw_price_rows if _code(row)}
    tx_price_codes = {_code(row) for row in tx_price_rows if _code(row)}
    tw_margin_codes = _positive_codes(tw_margin_rows, "今日餘額")
    tx_margin_codes = _positive_codes(tx_margin_rows, "資餘額")
    tw_missing = tw_margin_codes - tw_price_codes
    tx_missing = tx_margin_codes - tx_price_codes
    margin_overlap = tw_margin_codes & tx_margin_codes

    def _describe_missing(rows: list[dict], missing_codes: set[str],
                          other_price_codes: set[str], other_margin_codes: set[str],
                          balance_field: str) -> list[dict]:
        details = []
        for row in rows:
            code = _code(row)
            if code in missing_codes:
                details.append({
                    "code": code,
                    "name": str(row.get("名稱", row.get("證券名稱", ""))).strip(),
                    "balance_lots": str(row.get(balance_field, "")).strip(),
                    "exists_in_other_market_prices": code in other_price_codes,
                    "exists_in_other_market_margin": code in other_margin_codes,
                })
        return details[:50]

    if tw_missing or tx_missing or margin_overlap:
        raise ValueError(
            "market-universe mismatch; "
            f"TWSE_margin_rows={len(tw_margin_rows)} "
            f"TPEx_margin_rows={len(tx_margin_rows)} "
            f"TWSE_price_codes={len(tw_price_codes)} "
            f"TPEx_price_codes={len(tx_price_codes)} "
            f"TWSE_margin_missing_own_prices={_describe_missing(tw_margin_rows, tw_missing, tx_price_codes, tx_margin_codes, '今日餘額')} "
            f"TPEx_margin_missing_own_prices={_describe_missing(tx_margin_rows, tx_missing, tw_price_codes, tw_margin_codes, '資餘額')} "
            f"TWSE_TPEx_margin_code_overlap={sorted(margin_overlap)[:50]}"
        )

    listed = _sum_market_value(tw_margin_table, tw_price_table, "今日餘額",
                               "證券代號", "收盤價", "上市")
    otc = _sum_market_value(tx_margin_table, tx_price_table, "資餘額",
                            "代號", "收盤", "上櫃")
    denominator = (_twse_financing_amount(twse_margin, date8)
                   + _tpex_financing_amount(tpex_margin, t0_roc))
    missing = listed["missing_price_codes"] + otc["missing_price_codes"]
    priced = listed["priced_security_count"] + otc["priced_security_count"]
    count = listed["financed_security_count"] + otc["financed_security_count"]
    coverage = priced / count if count else 0.0
    if denominator <= 0:
        raise ValueError("combined financing amount must be positive")
    if missing:
        raise ValueError(f"positive financing balance has no same-day close: {missing[:30]}")
    if count == 0:
        raise ValueError("no positive financing balance rows")
    numerator = listed["collateral_value_ntd"] + otc["collateral_value_ntd"]
    return {
        "ok": True, "date": t0, "ratio": round(numerator / denominator * 100, 4),
        "numerator_collateral_value_ntd": round(numerator, 2),
        "denominator_financing_amount_ntd": round(denominator, 2),
        "coverage": round(coverage, 6), "financed_security_count": count,
        "priced_security_count": priced, "listed": listed, "otc": otc,
        "method": "official_same_day_financing_balance_x_close_over_official_same_day_financing_amount",
        "classification": "market_wide_estimate_not_individual_account_ratio",
    }
