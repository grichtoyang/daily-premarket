import unittest
from datetime import datetime
from unittest.mock import patch
import sys
import tempfile
from pathlib import Path

from src import t0, fetch_data


class _CalendarResponse:
    def __init__(self, rows):
        self._rows = rows

    def raise_for_status(self):
        return None

    def json(self):
        return self._rows


class T0CalendarFailClosedTests(unittest.TestCase):
    def setUp(self):
        t0._CLOSED_CACHE.clear()
        t0._LAST_CAL_ERROR = ""

    def tearDown(self):
        t0._CLOSED_CACHE.clear()
        t0._LAST_CAL_ERROR = ""

    @patch("src.t0.requests.get", side_effect=RuntimeError("calendar API unavailable"))
    def test_resolve_stops_when_calendar_load_fails(self, _get):
        with self.assertRaisesRegex(RuntimeError, "拒絕自動判定 T0"):
            t0.resolve(datetime(2026, 11, 5, 14, 0, tzinfo=t0.TAIPEI))

    @patch("src.t0.requests.get", side_effect=RuntimeError("calendar API unavailable"))
    def test_slot_params_stops_when_calendar_load_fails(self, _get):
        with self.assertRaisesRegex(RuntimeError, "拒絕自動判定 slot=evening"):
            t0.slot_params("evening", "2026-11-05")

    @patch("src.t0.requests.get", return_value=_CalendarResponse([]))
    def test_resolve_uses_current_date_on_open_day_after_day_session(self, _get):
        result = t0.resolve(datetime(2026, 11, 5, 14, 0, tzinfo=t0.TAIPEI))
        self.assertEqual(result["t0"], "2026-11-05")
        self.assertEqual(result["session"], "日盤")
        self.assertFalse(result["today_holiday"])

    @patch(
        "src.t0.requests.get",
        return_value=_CalendarResponse([{"Name": "國定假日", "Date": "1151106"}]),
    )
    def test_resolve_uses_previous_trading_day_on_calendar_holiday(self, _get):
        result = t0.resolve(datetime(2026, 11, 6, 14, 0, tzinfo=t0.TAIPEI))
        self.assertEqual(result["t0"], "2026-11-05")
        self.assertEqual(result["session"], "全日")
        self.assertTrue(result["today_holiday"])

    def test_slot_params_evening_open_day(self):
        result = t0.slot_params("evening", "2026-11-05", closed=set())
        self.assertEqual(result, {
            "t0": "2026-11-05", "session": "日盤", "slot": "evening"
        })

    def test_slot_params_evening_holiday_uses_previous_trading_day(self):
        result = t0.slot_params("evening", "2026-11-06", closed={"2026-11-06"})
        self.assertEqual(result, {
            "t0": "2026-11-05", "session": "全日", "slot": "evening"
        })


    @patch("src.t0.resolve", side_effect=RuntimeError("calendar API unavailable"))
    def test_fetch_data_stops_before_creating_report_when_calendar_fails(self, _resolve):
        with tempfile.TemporaryDirectory() as tmp:
            report_dir = Path(tmp) / "data_reports"
            with patch.object(fetch_data, "OUT_DIR", report_dir), \
                 patch.object(fetch_data, "build") as build, \
                 patch.object(sys, "argv", ["fetch_data.py"]):
                with self.assertRaisesRegex(RuntimeError, "calendar API unavailable"):
                    fetch_data.main()
            self.assertFalse(report_dir.exists())
            build.assert_not_called()



if __name__ == "__main__":
    unittest.main()
