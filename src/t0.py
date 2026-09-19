"""T0 與交易日共用邏輯 (台指期全定義)。

- 日盤收盤：當日 13:45；夜盤 15:00~隔日 05:00，歸屬開盤當日。
- 交易日 = 週一~五 且非 TWSE 休市日 (holidaySchedule：僅「開始交易/最後交易」視為開市)。
- resolve(now)：平日 13:45 前 → 前一交易日/全日；平日 13:45 後 → 今天(若交易日)/日盤；
  週末假日 → 前一交易日/全日＋休市標示。
"""
from __future__ import annotations
from datetime import date, datetime, timedelta
from zoneinfo import ZoneInfo
import requests

TAIPEI = ZoneInfo("Asia/Taipei")
HOL_URL = "https://openapi.twse.com.tw/v1/holidaySchedule/holidaySchedule"
UA = {"User-Agent": "daily-pre-market-analysis/1.0", "accept": "application/json"}


def _roc_to_iso(roc: str) -> str:
    roc = str(roc).strip()
    if len(roc) == 7 and roc[:3].isdigit():
        return f"{int(roc[:3]) + 1911:04d}-{roc[3:5]}-{roc[5:7]}"
    return roc


def load_closed(year: int, timeout: int = 20) -> set[str]:
    """回傳該年休市日 ISO set。API 失敗回空集 (退為週末判斷)。"""
    try:
        r = requests.get(HOL_URL, headers=UA, timeout=timeout)
        r.raise_for_status()
        closed = set()
        for row in r.json():
            name = str(row.get("Name", ""))
            if "開始交易" in name or "最後交易" in name:
                continue
            d = _roc_to_iso(row.get("Date", ""))
            if len(d) == 10 and d.startswith(str(year)):
                closed.add(d)
        return closed
    except Exception as e:  # noqa: BLE001
        print(f"[WARN] 休市日曆失敗，退為週末判斷：{e}")
        return set()


def is_trading_day(d: date, closed: set[str] | None = None) -> bool:
    if d.weekday() >= 5:
        return False
    if closed is None:
        return True
    return d.isoformat() not in closed


def prev_trading_day(d: date, closed: set[str]) -> date:
    while True:
        d -= timedelta(days=1)
        if is_trading_day(d, closed):
            return d


def resolve(now: datetime | None = None) -> dict:
    """回傳 {t0, session(日盤/全日), today_holiday, report_date}。"""
    now = now or datetime.now(TAIPEI)
    today = now.date()
    closed = load_closed(today.year)
    today_open = is_trading_day(today, closed)
    day_closed = now.hour > 13 or (now.hour == 13 and now.minute >= 45)
    if not today_open:
        t0 = prev_trading_day(today, closed)
        return {"t0": t0.isoformat(), "session": "全日", "today_holiday": True,
                "report_date": today.isoformat()}
    if day_closed:
        return {"t0": today.isoformat(), "session": "日盤", "today_holiday": False,
                "report_date": today.isoformat()}
    t0 = prev_trading_day(today, closed)
    return {"t0": t0.isoformat(), "session": "全日", "today_holiday": False,
            "report_date": today.isoformat()}


def daily_filename(t0: str, session: str) -> str:
    return f"Daily_REPORT_{t0.replace('-', '')}_{session}.md"
