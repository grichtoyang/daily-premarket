"""重要市場：Yahoo Finance Chart API (免費免 Key)，API 優先、失敗標 unavailable。

每檔回傳 {price, change, pct, date, retrieved_at, source}。
優先採用帶有交易所時間戳的 meta.regularMarketPrice；只有在 meta 不完整時才退回日K。
"""
from __future__ import annotations
from datetime import datetime, timedelta, timezone
from zoneinfo import ZoneInfo, ZoneInfoNotFoundError
import requests
from src.utils import HEADERS

def _exchange_date(timestamp: int | float, timezone_name: str | None) -> str:
    """Convert Yahoo's UNIX timestamp using the instrument's exchange timezone."""
    try:
        tz = ZoneInfo(timezone_name) if timezone_name else timezone.utc
    except (ZoneInfoNotFoundError, ValueError, TypeError):
        tz = timezone.utc
    return datetime.fromtimestamp(timestamp, tz=tz).strftime("%Y-%m-%d")


GROUPS: dict[str, list[tuple[str, str]]] = {
    "美股指數": [("S&P 500", "^GSPC"), ("Nasdaq Composite", "^IXIC"), ("Nasdaq 100", "^NDX"),
             ("Dow Jones", "^DJI"), ("費城半導體 SOX", "^SOX"), ("VIX", "^VIX")],
    "亞洲主要指數": [("日經225", "^N225"), ("韓國KOSPI", "^KS11"), ("香港恆生", "^HSI"),
                ("上海綜合", "000001.SS"), ("深圳成分", "399001.SZ")],
    "美股指數期貨": [("S&P500期貨", "ES=F"), ("Nasdaq100期貨", "NQ=F"), ("道瓊期貨", "YM=F"),
                ("Russell2000期貨", "RTY=F")],
    "主要匯率": [("USD/TWD", "TWD=X"), ("DXY美元指數", "DX-Y.NYB"), ("USD/JPY", "JPY=X"),
             ("USD/KRW", "KRW=X")],
    "台灣相關ADR": [("台積電ADR", "TSM"), ("聯電ADR", "UMC"), ("日月光ADR", "ASX")],
    "原油黃金Bitcoin": [("WTI原油期貨", "CL=F"), ("黃金期貨", "GC=F"), ("Bitcoin", "BTC-USD")],
}

def quote(sym: str) -> dict:
    """Fetch the latest exchange-stamped quote from Yahoo Chart API.

    Prefer meta.regularMarketPrice when its exchange-local timestamp is at least
    as recent as the final daily bar; this avoids silently ignoring a fresher
    quote when the historical bar array is delayed.
    """
    out = {"symbol": sym, "price": None, "change": None, "pct": None, "date": None,
           "retrieved_at": None, "exchange_timezone": None,
           "source": "Yahoo Finance Chart API", "ok": False}
    try:
        r = requests.get(
            f"https://query1.finance.yahoo.com/v8/finance/chart/{sym}?interval=1d&range=1mo",
            headers={**HEADERS, "Accept": "application/json"}, timeout=20,
        )
        r.raise_for_status()
        out["retrieved_at"] = datetime.now(timezone.utc).isoformat(timespec="seconds")
        res = (r.json().get("chart", {}).get("result") or [None])[0]
        if not res:
            return out
        ts = res.get("timestamp") or []
        meta = res.get("meta") or {}
        exchange_timezone = meta.get("exchangeTimezoneName")
        out["exchange_timezone"] = exchange_timezone
        closes = ((res.get("indicators") or {}).get("quote") or [{}])[0].get("close") or []
        pts = [(t, c) for t, c in zip(ts, closes) if c is not None]

        meta_price = meta.get("regularMarketPrice")
        meta_time = meta.get("regularMarketTime")
        meta_date = (
            _exchange_date(meta_time, exchange_timezone)
            if meta_time is not None and exchange_timezone else None
        )
        bar_date = _exchange_date(pts[-1][0], exchange_timezone) if pts and exchange_timezone else None
        if meta_price is not None and meta_date and (bar_date is None or meta_date >= bar_date):
            previous = meta.get("chartPreviousClose") or meta.get("previousClose")
            if previous is None and meta_date == bar_date and len(pts) >= 2:
                previous = pts[-2][1]
            out["price"] = meta_price
            out["date"] = meta_date
            if previous not in (None, 0):
                out["change"] = float(meta_price) - float(previous)
                out["pct"] = out["change"] / float(previous) * 100
            out["source"] = "Yahoo Finance Chart API（meta.regularMarketPrice）"
            out["ok"] = out["change"] is not None and out["pct"] is not None
            if out["ok"]:
                return out

        if not pts:
            return out
        last_t, last_c = pts[-1]
        out["price"] = last_c
        out["date"] = _exchange_date(last_t, exchange_timezone)
        if len(pts) >= 2:
            prev_c = pts[-2][1]
            out["change"] = last_c - prev_c
            out["pct"] = (last_c - prev_c) / prev_c * 100 if prev_c else None
        out["ok"] = out["change"] is not None and out["pct"] is not None
    except Exception as e:  # noqa: BLE001
        print(f"[WARN] yahoo {sym} failed: {e}")
    return out


def _quote_chart_meta(sym: str) -> dict | None:
    """Retry Yahoo's public v8 chart endpoint on alternate hosts for fresh meta quote.

    v7/finance/quote is deliberately not used: Yahoo now requires a session cookie
    and crumb for that endpoint. The chart endpoint remains the unauthenticated path.
    """
    for host in ("query2.finance.yahoo.com", "query1.finance.yahoo.com"):
        try:
            r = requests.get(
                f"https://{host}/v8/finance/chart/{sym}",
                params={"range": "1d", "interval": "1m", "includePrePost": "false"},
                headers={**HEADERS, "Accept": "application/json"},
                timeout=15,
            )
            r.raise_for_status()
            res = (r.json().get("chart", {}).get("result") or [None])[0]
            if not res:
                continue
            meta = res.get("meta") or {}
            price = meta.get("regularMarketPrice")
            timestamp = meta.get("regularMarketTime")
            timezone_name = meta.get("exchangeTimezoneName")
            if price is None or timestamp is None or not timezone_name:
                continue
            previous = meta.get("chartPreviousClose") or meta.get("previousClose")
            if previous in (None, 0):
                continue
            change = float(price) - float(previous)
            return {
                "symbol": sym,
                "price": price,
                "change": change,
                "pct": change / float(previous) * 100,
                "date": _exchange_date(timestamp, timezone_name),
                "retrieved_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
                "exchange_timezone": timezone_name,
                "source": f"Yahoo Finance Chart API meta fallback（{host}）",
                "ok": True,
            }
        except Exception as e:  # noqa: BLE001
            print(f"[WARN] yahoo chart-meta fallback {sym} host={host} failed: {e}")
    return None




def _apply_asia_freshness(rows: list[tuple], expected_date: str | dict | None) -> list[tuple]:
    """Validate each Asian quote against its own exchange's latest completed session.

    A mapping is keyed by Yahoo symbol. A plain date remains supported for older
    callers/tests. Missing quotes or unavailable exchange calendars fail closed.
    """
    if expected_date is None:
        return rows
    for name, q in rows:
        symbol = q.get("symbol")
        expected = expected_date.get(symbol) if isinstance(expected_date, dict) else expected_date
        actual_date = q.get("date")
        if q.get("price") is not None and expected and actual_date == expected:
            continue
        if q.get("price") is None:
            reason = f"{name}本次未取得報價；該市場最近已收盤交易日 {expected or '無法驗證'}"
        elif not expected:
            reason = f"{name}無法取得交易所最近已收盤交易日，日期驗證失敗"
        else:
            reason = f"{name}資料日期 {actual_date or '缺失'} 與該市場最近已收盤交易日 {expected} 不一致"
        q["stale"] = True
        q["stale_reason"] = reason
        q["price"] = None
        q["change"] = None
        q["pct"] = None
        q["ok"] = False
        q["source"] = f"Yahoo Finance（{reason}，已排除）"
    return rows


def _expected_exchange_session_date(
    calendar_name: str, timezone_name: str, now: datetime | None = None
) -> str:
    """Return the latest fully closed session for one exchange calendar."""
    import pandas as pd
    import pandas_market_calendars as mcal

    now_utc = now or datetime.now(timezone.utc)
    if now_utc.tzinfo is None:
        raise ValueError("now must be timezone-aware")
    now_utc = now_utc.astimezone(timezone.utc)
    local_date = now_utc.astimezone(ZoneInfo(timezone_name)).date()
    calendar = mcal.get_calendar(calendar_name)
    schedule = calendar.schedule(
        start_date=(local_date - timedelta(days=30)).isoformat(),
        end_date=local_date.isoformat(),
    )
    if schedule.empty:
        raise RuntimeError(f"{calendar_name} calendar returned no sessions")
    close_column = "market_close" if "market_close" in schedule.columns else "close"
    closed = schedule[schedule[close_column] <= pd.Timestamp(now_utc)]
    if closed.empty:
        raise RuntimeError(f"No completed {calendar_name} session found in calendar window")
    return closed.index[-1].date().isoformat()


def _expected_asia_session_dates(now: datetime | None = None) -> dict[str, str | None]:
    """Resolve latest completed session independently for each Asian exchange."""
    exchanges = {
        "^N225": ("JPX", "Asia/Tokyo"),
        "^KS11": ("XKRX", "Asia/Seoul"),
        "^HSI": ("HKEX", "Asia/Hong_Kong"),
        "000001.SS": ("SSE", "Asia/Shanghai"),
        "399001.SZ": ("SSE", "Asia/Shanghai"),
    }
    result: dict[str, str | None] = {}
    for symbol, (calendar_name, timezone_name) in exchanges.items():
        try:
            result[symbol] = _expected_exchange_session_date(calendar_name, timezone_name, now)
        except Exception as e:  # noqa: BLE001
            print(f"[WARN] {calendar_name} calendar unavailable for {symbol}: {e}")
            result[symbol] = None
    return result


def _expected_us_session_date(now: datetime | None = None) -> str:
    """Return the latest fully closed NYSE session, including holidays/early closes."""
    return _expected_exchange_session_date("NYSE", "America/New_York", now)


def _apply_adr_freshness(rows: list[tuple], expected_session: str | None) -> list[tuple]:
    """Reject ADR quotes not dated on the latest fully closed US equity session."""
    for name, q in rows:
        actual_date = q.get("date")
        if q.get("price") is None:
            # A missing quote is also authoritative unavailable. Mark it stale so
            # same-T0 merge cannot silently refill an older ADR value.
            if expected_session is None:
                reason = f"{name}本次未取得報價，且無法驗證美國交易日（交易日曆不可用）"
            else:
                reason = f"{name}本次未取得可驗證報價（美國最近已收盤交易日 {expected_session}）"
        elif expected_session and actual_date == expected_session:
            continue
        elif expected_session is None:
            reason = f"{name}無法驗證美國交易日（交易日曆不可用）"
        else:
            reason = f"{name}資料日期 {actual_date or '缺失'} 與美國最近已收盤交易日 {expected_session} 不一致"
        q["stale"] = True
        q["stale_reason"] = reason
        q["price"] = None
        q["change"] = None
        q["pct"] = None
        q["ok"] = False
        q["source"] = f"Yahoo Finance Chart API（{reason}，已排除）"
    return rows



def _refresh_stale_market_quotes(
    market_data: dict,
    expected_asia: dict[str, str | None],
    expected_us_session: str | None,
) -> None:
    """Try Yahoo Quote API v7 before rejecting stale/missing Asia and ADR Chart bars."""
    pending: dict[str, str] = {}
    for group, rows in market_data.items():
        for _, q in rows:
            symbol = q.get("symbol")
            if group == "亞洲主要指數":
                expected = expected_asia.get(symbol)
            elif group == "台灣相關ADR":
                expected = expected_us_session
            else:
                continue
            if expected and (q.get("price") is None or q.get("date") != expected):
                pending[symbol] = expected
    if not pending:
        return

    from concurrent.futures import ThreadPoolExecutor

    started = datetime.now(timezone.utc)
    with ThreadPoolExecutor(max_workers=4) as executor:
        fetched = list(executor.map(_quote_chart_meta, pending.keys()))
    fallback = dict(zip(pending.keys(), fetched))
    accepted = 0
    for group, rows in market_data.items():
        for name, q in rows:
            symbol = q.get("symbol")
            expected = pending.get(symbol)
            if not expected:
                continue
            candidate = fallback.get(symbol)
            if (
                candidate
                and candidate.get("price") is not None
                and candidate.get("date") == expected
                and candidate.get("change") is not None
                and candidate.get("pct") is not None
            ):
                q.update(candidate)
                q["fallback_used"] = True
                accepted += 1
                print(f"[INFO] yahoo chart-meta fallback accepted {symbol} date={expected}")
            else:
                actual = candidate.get("date") if candidate else "no_quote"
                print(
                    f"[WARN] yahoo chart-meta fallback not accepted {symbol} "
                    f"expected={expected} actual={actual}"
                )
    elapsed = (datetime.now(timezone.utc) - started).total_seconds()
    print(
        f"[TIMING] source=us_market.chart_meta_fallback elapsed={elapsed:.2f}s "
        f"requested={len(pending)} accepted={accepted}"
    )


def get_all(expected_date: str | None = None) -> dict:
    """{group: [(name, quote)]}; stale Asia/ADR Chart bars get a timestamped quote-API fallback."""
    from concurrent.futures import ThreadPoolExecutor
    out: dict = {}
    with ThreadPoolExecutor(max_workers=5) as ex:
        for g, items in GROUPS.items():
            out[g] = list(ex.map(lambda it: (it[0], quote(it[1])), items))

    now_utc = datetime.now(timezone.utc)
    expected_asia = _expected_asia_session_dates(now_utc)
    try:
        expected_us_session = _expected_us_session_date(now_utc)
    except Exception as e:  # noqa: BLE001
        print(f"[WARN] NYSE calendar unavailable; ADR freshness fails closed: {e}")
        expected_us_session = None

    _refresh_stale_market_quotes(out, expected_asia, expected_us_session)
    if "亞洲主要指數" in out:
        out["亞洲主要指數"] = _apply_asia_freshness(out["亞洲主要指數"], expected_asia)
    if "台灣相關ADR" in out:
        out["台灣相關ADR"] = _apply_adr_freshness(out["台灣相關ADR"], expected_us_session)
    return out

def ohlc(sym: str) -> dict:
    """最近一根日K的 open/high/low/close/date。失敗回 ok=False。"""
    out = {"open": None, "high": None, "low": None, "close": None, "date": None,
           "exchange_timezone": None, "ok": False}
    try:
        r = requests.get(f"https://query1.finance.yahoo.com/v8/finance/chart/{sym}?interval=1d&range=5d",
                         headers={**HEADERS, "Accept": "application/json"}, timeout=20)
        r.raise_for_status()
        res = (r.json().get("chart", {}).get("result") or [None])[0]
        if not res:
            return out
        ts = res.get("timestamp") or []
        meta = res.get("meta") or {}
        exchange_timezone = meta.get("exchangeTimezoneName")
        q = ((res.get("indicators") or {}).get("quote") or [{}])[0]
        n = len(ts)
        for i in range(n - 1, -1, -1):
            c = (q.get("close") or [None] * n)[i]
            if c is None:
                continue
            out = {"open": (q.get("open") or [None] * n)[i], "high": (q.get("high") or [None] * n)[i],
                   "low": (q.get("low") or [None] * n)[i], "close": c,
                   "date": _exchange_date(ts[i], exchange_timezone),
                   "exchange_timezone": exchange_timezone, "ok": True}
            break
    except Exception as e:  # noqa: BLE001
        print(f"[WARN] yahoo ohlc {sym} failed: {e}")
    return out
# ---- 相容舊介面 (分析層/舊報表用) ----
_LEGACY = {"SP500": "^GSPC", "Nasdaq": "^IXIC", "DOW": "^DJI", "SOX": "^SOX", "VIX": "^VIX",
           "TSM_ADR": "TSM", "US10Y": "^TNX", "DXY": "DX-Y.NYB", "USDTWD": "TWD=X",
           "GOLD": "GC=F", "WTI": "CL=F"}

def get_legacy() -> dict:
    out = {}
    for name, sym in _LEGACY.items():
        q = quote(sym)
        out[name] = {"symbol": sym, "close": q["price"], "pct": q["pct"], "date": q["date"]}
    return out
