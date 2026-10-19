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

_LAST_CAL_ERROR: str = ""
# F2（2026-10-19）：load_closed 成功結果 memoize。同一份年度休市日曆在一次抓取中
# 會被重複請求（taifex._next_trading_day 逐年載入 + t0.resolve + slot_params），
# 但失敗不得快取，否則一次網路故障會把該年份永久釘成空日曆（退週末判斷）。
_CLOSED_CACHE: dict[int, set[str]] = {}


def _roc_to_iso(roc: str) -> str:
    roc = str(roc).strip()
    if len(roc) == 7 and roc[:3].isdigit():
        return f"{int(roc[:3]) + 1911:04d}-{roc[3:5]}-{roc[5:7]}"
    return roc


def load_closed(year: int, timeout: int = 20) -> set[str]:
    """回傳該年休市日 ISO set。API 失敗回空集 (退為週末判斷)。
    失敗原因記在 _LAST_CAL_ERROR，resolve() 轉為 cal_fail 大聲揭露。
    F2：同 year 命中快取時直接回傳（回傳副本，維持「每次拿到新 set」的舊語意），
    並同樣把 _LAST_CAL_ERROR 清空——否則前一次失敗的錯誤字串會外洩到這次呼叫者。"""
    global _LAST_CAL_ERROR
    if year in _CLOSED_CACHE:
        _LAST_CAL_ERROR = ""
        return set(_CLOSED_CACHE[year])
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
        _LAST_CAL_ERROR = ""
        _CLOSED_CACHE[year] = closed
        return closed
    except Exception as e:  # noqa: BLE001
        _LAST_CAL_ERROR = str(e)[:160]
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
    """回傳 {t0, session(日盤/全日), today_holiday, report_date,
    cal_fail(日曆是否抓失敗), cal_error}。"""
    now = now or datetime.now(TAIPEI)
    today = now.date()
    closed = load_closed(today.year)
    cal_fail = bool(_LAST_CAL_ERROR)
    today_open = is_trading_day(today, closed)
    day_closed = now.hour > 13 or (now.hour == 13 and now.minute >= 45)
    if not today_open:
        t0 = prev_trading_day(today, closed)
        return {"t0": t0.isoformat(), "session": "全日", "today_holiday": True,
                "report_date": today.isoformat(), "cal_fail": cal_fail,
                "cal_error": _LAST_CAL_ERROR}
    if day_closed:
        return {"t0": today.isoformat(), "session": "日盤", "today_holiday": False,
                "report_date": today.isoformat(), "cal_fail": cal_fail,
                "cal_error": _LAST_CAL_ERROR}
    t0 = prev_trading_day(today, closed)
    return {"t0": t0.isoformat(), "session": "全日", "today_holiday": False,
            "report_date": today.isoformat(), "cal_fail": cal_fail,
            "cal_error": _LAST_CAL_ERROR}


def slot_params(slot: str, sched_iso: str, closed: set[str] | None = None) -> dict:
    """班別→(T0, session)，純函式：只吃排定日期，不讀牆鐘（備援半夜跑也不會判錯盤別）。
    morning：T0＝排定日前一交易日／全日；evening：排定日開市→T0＝當日／日盤，
      休市→退為前一交易日／全日；weekend：T0＝排定日前一交易日／全日（週六即週五）。
    closed 缺省時載入 sched 年份日曆（與 resolve 同口徑）；測試時傳 set() 即不碰網路。"""
    if slot not in ("morning", "evening", "weekend"):
        raise ValueError(f"unknown slot: {slot}")
    sched = date.fromisoformat(sched_iso)
    if closed is None:
        closed = load_closed(sched.year)
    if slot == "evening" and is_trading_day(sched, closed):
        return {"t0": sched.isoformat(), "session": "日盤", "slot": slot}
    t0 = prev_trading_day(sched, closed)
    return {"t0": t0.isoformat(), "session": "全日", "slot": slot}


def daily_filename(t0: str, session: str) -> str:
    return f"Daily_REPORT_{t0.replace('-', '')}_{session}.md"
