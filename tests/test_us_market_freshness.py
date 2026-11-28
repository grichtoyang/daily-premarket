import unittest
from datetime import datetime, timezone
from unittest.mock import patch

import pandas as pd

from src.sources.us_market import (
    _apply_asia_freshness, _apply_adr_freshness, _expected_us_session_date,
)


class AsianMarketFreshnessTests(unittest.TestCase):
    def _rows(self, dates):
        return [
            (name, {
                "symbol": symbol,
                "price": price,
                "change": 10.0,
                "pct": 1.0,
                "date": day,
                "source": "Yahoo Finance Chart API",
                "ok": True,
            })
            for name, symbol, price, day in dates
        ]

    def test_entire_asia_batch_older_than_t0_is_marked_unavailable(self):
        rows = self._rows([
            ("日經225", "^N225", 59444.21, "2026-11-19"),
            ("韓國KOSPI", "^KS11", 5137.89, "2026-11-19"),
            ("香港恆生", "^HSI", 22841.62, "2026-11-19"),
        ])

        result = _apply_asia_freshness(rows, "2026-11-20")

        for _, quote in result:
            self.assertTrue(quote["stale"])
            self.assertFalse(quote["ok"])
            self.assertIsNone(quote["price"])
            self.assertIsNone(quote["change"])
            self.assertIsNone(quote["pct"])
            self.assertEqual(quote["date"], "2026-11-19")
            self.assertIn("早於或無法核對報告 T0", quote["stale_reason"])

    def test_batch_with_t0_data_is_not_rejected(self):
        rows = self._rows([
            ("日經225", "^N225", 56000.0, "2026-11-20"),
            ("韓國KOSPI", "^KS11", 48000.0, "2026-11-20"),
        ])

        result = _apply_asia_freshness(rows, "2026-11-20")

        for _, quote in result:
            self.assertNotIn("stale", quote)
            self.assertTrue(quote["ok"])
            self.assertIsNotNone(quote["price"])

    def test_older_single_market_is_rejected_when_another_market_has_t0(self):
        # Freshness is evaluated per index; another market's T0 quote cannot
        # make this older quote appear current.
        rows = self._rows([
            ("日經225", "^N225", 56000.0, "2026-11-20"),
            ("香港恆生", "^HSI", 22841.62, "2026-11-19"),
        ])

        result = _apply_asia_freshness(rows, "2026-11-20")

        self.assertFalse(result[0][1].get("stale", False))
        self.assertEqual(result[0][1]["price"], 56000.0)
        self.assertTrue(result[1][1]["stale"])
        self.assertFalse(result[1][1]["ok"])
        self.assertIsNone(result[1][1]["price"])
        self.assertIsNone(result[1][1]["change"])
        self.assertIsNone(result[1][1]["pct"])

    def test_missing_expected_date_preserves_legacy_behavior(self):
        rows = self._rows([
            ("日經225", "^N225", 59444.21, "2026-11-19"),
        ])

        result = _apply_asia_freshness(rows, None)

        self.assertEqual(result[0][1]["price"], 59444.21)
        self.assertNotIn("stale", result[0][1])



class ADRMarketFreshnessTests(unittest.TestCase):
    def _rows(self, dates):
        return [
            (name, {
                "symbol": symbol, "price": price, "change": 1.5, "pct": 1.0,
                "date": day, "source": "Yahoo Finance Chart API", "ok": True,
            })
            for name, symbol, price, day in dates
        ]

    def test_each_adr_must_match_latest_closed_us_session(self):
        rows = self._rows([
            ("台積電ADR", "TSM", 353.34, "2026-11-27"),
            ("聯電ADR", "UMC", 13.19, "2026-11-25"),
            ("日月光ADR", "ASX", 31.34, "2026-11-27"),
        ])
        result = _apply_adr_freshness(rows, "2026-11-27")
        self.assertTrue(result[0][1]["ok"])
        self.assertTrue(result[0][1]["price"])
        self.assertTrue(result[1][1]["stale"])
        self.assertFalse(result[1][1]["ok"])
        self.assertIsNone(result[1][1]["price"])
        self.assertIsNone(result[1][1]["change"])
        self.assertIsNone(result[1][1]["pct"])
        self.assertEqual(result[1][1]["date"], "2026-11-25")
        self.assertTrue(result[2][1]["ok"])

    def test_missing_date_is_rejected(self):
        rows = self._rows([("台積電ADR", "TSM", 353.34, None)])
        result = _apply_adr_freshness(rows, "2026-11-27")
        self.assertTrue(result[0][1]["stale"])
        self.assertIsNone(result[0][1]["price"])

    def test_missing_price_is_marked_stale_to_block_same_t0_carry_forward(self):
        rows = self._rows([("台積電ADR", "TSM", None, None)])
        result = _apply_adr_freshness(rows, "2026-11-27")
        quote = result[0][1]
        self.assertTrue(quote["stale"])
        self.assertFalse(quote["ok"])
        self.assertIsNone(quote["price"])
        self.assertIsNone(quote["change"])
        self.assertIsNone(quote["pct"])
        self.assertIn("本次未取得可驗證報價", quote["stale_reason"])

    def test_unavailable_calendar_fails_closed(self):
        rows = self._rows([("台積電ADR", "TSM", 353.34, "2026-11-27")])
        result = _apply_adr_freshness(rows, None)
        self.assertTrue(result[0][1]["stale"])
        self.assertIn("無法驗證美國交易日", result[0][1]["stale_reason"])
        self.assertIsNone(result[0][1]["price"])

    def test_nyse_calendar_uses_last_fully_closed_session_and_holiday_schedule(self):
        schedule = pd.DataFrame(
            {"market_close": pd.to_datetime([
                "2026-11-25T21:00:00Z", "2026-11-27T18:00:00Z"
            ], utc=True)},
            index=pd.to_datetime(["2026-11-25", "2026-11-27"]),
        )
        calendar = unittest.mock.Mock()
        calendar.schedule.return_value = schedule
        with patch("pandas_market_calendars.get_calendar", return_value=calendar):
            # Friday's early close has passed; the calendar skips Thanksgiving.
            actual = _expected_us_session_date(
                datetime(2026, 11, 27, 19, 0, tzinfo=timezone.utc)
            )
        self.assertEqual(actual, "2026-11-27")

    def test_before_market_close_uses_previous_completed_session(self):
        schedule = pd.DataFrame(
            {"market_close": pd.to_datetime([
                "2026-11-25T21:00:00Z", "2026-11-27T18:00:00Z"
            ], utc=True)},
            index=pd.to_datetime(["2026-11-25", "2026-11-27"]),
        )
        calendar = unittest.mock.Mock()
        calendar.schedule.return_value = schedule
        with patch("pandas_market_calendars.get_calendar", return_value=calendar):
            actual = _expected_us_session_date(
                datetime(2026, 11, 27, 17, 0, tzinfo=timezone.utc)
            )
        self.assertEqual(actual, "2026-11-25")


if __name__ == "__main__":
    unittest.main()
