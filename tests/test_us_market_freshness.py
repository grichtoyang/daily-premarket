import unittest
from datetime import datetime, timezone
from unittest.mock import patch

import pandas as pd

from src.sources.us_market import (
    _apply_asia_freshness, _apply_adr_freshness, _expected_us_session_date,
    _expected_asia_session_dates, _quote_chart_meta, _refresh_stale_market_quotes,
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


    def test_asia_freshness_uses_exchange_specific_expected_dates(self):
        rows = self._rows([
            ("日經225", "^N225", 56000.0, "2026-11-26"),
            ("香港恆生", "^HSI", 22000.0, "2026-11-27"),
        ])
        expected = {"^N225": "2026-11-26", "^HSI": "2026-11-27"}
        result = _apply_asia_freshness(rows, expected)
        self.assertTrue(result[0][1]["ok"])
        self.assertFalse(result[0][1].get("stale", False))
        self.assertTrue(result[1][1]["ok"])
        self.assertFalse(result[1][1].get("stale", False))

    def test_missing_asia_quote_is_marked_stale(self):
        rows = self._rows([("日經225", "^N225", None, None)])
        result = _apply_asia_freshness(rows, {"^N225": "2026-11-27"})
        quote = result[0][1]
        self.assertTrue(quote["stale"])
        self.assertFalse(quote["ok"])
        self.assertIsNone(quote["price"])
        self.assertIn("本次未取得報價", quote["stale_reason"])

    def test_asia_calendar_dates_are_resolved_per_exchange(self):
        expected = {"JPX": "2026-11-27", "XKRX": "2026-11-27",
                    "HKEX": "2026-11-27", "SSE": "2026-11-27"}
        with patch(
            "src.sources.us_market._expected_exchange_session_date",
            side_effect=lambda calendar, timezone_name, now: expected[calendar],
        ):
            result = _expected_asia_session_dates(
                datetime(2026, 11, 28, 1, 45, tzinfo=timezone.utc)
            )
        self.assertEqual(result, {
            "^N225": "2026-11-27", "^KS11": "2026-11-27",
            "^HSI": "2026-11-27", "000001.SS": "2026-11-27",
            "399001.SZ": "2026-11-27",
        })


    def test_quote_prefers_fresher_meta_timestamp_over_stale_daily_bars(self):
        meta_time = int(datetime(2026, 11, 27, 6, 30, tzinfo=timezone.utc).timestamp())
        old_bar_time = int(datetime(2026, 11, 26, 6, 30, tzinfo=timezone.utc).timestamp())
        response = unittest.mock.Mock()
        response.raise_for_status.return_value = None
        response.json.return_value = {"chart": {"result": [{
            "meta": {
                "regularMarketPrice": 60000.0, "chartPreviousClose": 59000.0,
                "regularMarketTime": meta_time, "exchangeTimezoneName": "Asia/Tokyo",
            },
            "timestamp": [old_bar_time],
            "indicators": {"quote": [{"close": [58000.0]}]},
        }]}}
        with patch("requests.get", return_value=response):
            from src.sources.us_market import quote
            result = quote("^N225")
        self.assertEqual(result["price"], 60000.0)
        self.assertEqual(result["date"], "2026-11-27")
        self.assertEqual(result["change"], 1000.0)
        self.assertAlmostEqual(result["pct"], 1000 / 59000 * 100)
        self.assertIn("meta.regularMarketPrice", result["source"])

    def test_quote_does_not_use_stale_daily_close_as_meta_previous_close(self):
        meta_time = int(datetime(2026, 11, 27, 6, 30, tzinfo=timezone.utc).timestamp())
        bar_times = [
            int(datetime(2026, 11, 25, 6, 30, tzinfo=timezone.utc).timestamp()),
            int(datetime(2026, 11, 26, 6, 30, tzinfo=timezone.utc).timestamp()),
        ]
        response = unittest.mock.Mock()
        response.raise_for_status.return_value = None
        response.json.return_value = {"chart": {"result": [{
            "meta": {
                "regularMarketPrice": 60000.0,
                "regularMarketTime": meta_time, "exchangeTimezoneName": "Asia/Tokyo",
            },
            "timestamp": bar_times,
            "indicators": {"quote": [{"close": [57000.0, 58000.0]}]},
        }]}}
        with patch("requests.get", return_value=response):
            from src.sources.us_market import quote
            result = quote("^N225")
        self.assertEqual(result["price"], 58000.0)
        self.assertEqual(result["date"], "2026-11-26")

    def test_chart_meta_fallback_requires_a_previous_close(self):
        timestamp = int(datetime(2026, 11, 27, 21, 0, tzinfo=timezone.utc).timestamp())
        response = unittest.mock.Mock()
        response.raise_for_status.return_value = None
        response.json.return_value = {"chart": {"result": [{
            "meta": {
                "regularMarketPrice": 353.34, "regularMarketTime": timestamp,
                "exchangeTimezoneName": "America/New_York",
            },
            "timestamp": [timestamp],
            "indicators": {"quote": [{"close": [353.34]}]},
        }]}}
        with patch("requests.get", return_value=response):
            self.assertIsNone(_quote_chart_meta("TSM"))

    def test_chart_meta_fallback_parses_exchange_timestamp_without_v7_quote(self):
        timestamp = int(datetime(2026, 11, 27, 21, 0, tzinfo=timezone.utc).timestamp())
        response = unittest.mock.Mock()
        response.raise_for_status.return_value = None
        response.json.return_value = {"chart": {"result": [{
            "meta": {
                "regularMarketPrice": 353.34, "chartPreviousClose": 342.34,
                "regularMarketTime": timestamp, "exchangeTimezoneName": "America/New_York",
            },
            "indicators": {"quote": [{"close": [342.34, 353.34]}]},
        }]}}
        with patch("requests.get", return_value=response):
            result = _quote_chart_meta("TSM")
        self.assertEqual(result["date"], "2026-11-27")
        self.assertEqual(result["price"], 353.34)
        self.assertAlmostEqual(result["change"], 11.0)
        self.assertAlmostEqual(result["pct"], 11.0 / 342.34 * 100)
        self.assertIn("Chart API meta fallback", result["source"])

    def test_stale_chart_quote_is_replaced_only_by_matching_fallback_date(self):
        chart_quote = {
            "symbol": "^N225", "price": 59000.0, "change": 10.0, "pct": 0.1,
            "date": "2026-11-26", "source": "Yahoo Finance Chart API", "ok": True,
        }
        fresh_quote = {
            "symbol": "^N225", "price": 60000.0, "change": 1000.0, "pct": 1.69,
            "date": "2026-11-27", "retrieved_at": "2026-11-28T01:45:00+00:00",
            "exchange_timezone": "Asia/Tokyo",
            "source": "Yahoo Finance Chart API meta fallback", "ok": True,
        }
        data = {"亞洲主要指數": [("日經225", chart_quote)]}
        with patch("src.sources.us_market._quote_chart_meta", return_value=fresh_quote):
            _refresh_stale_market_quotes(data, {"^N225": "2026-11-27"}, None)
        self.assertEqual(chart_quote["price"], 60000.0)
        self.assertEqual(chart_quote["date"], "2026-11-27")
        self.assertTrue(chart_quote["fallback_used"])

    def test_stale_fallback_quote_is_not_used(self):
        chart_quote = {
            "symbol": "^N225", "price": 59000.0, "change": 10.0, "pct": 0.1,
            "date": "2026-11-26", "source": "Yahoo Finance Chart API", "ok": True,
        }
        stale_fallback = {
            "symbol": "^N225", "price": 58000.0, "change": -1000.0, "pct": -1.7,
            "date": "2026-11-25", "source": "Yahoo Finance Quote API v7", "ok": True,
        }
        data = {"亞洲主要指數": [("日經225", chart_quote)]}
        with patch("src.sources.us_market._quote_chart_meta", return_value=stale_fallback):
            _refresh_stale_market_quotes(data, {"^N225": "2026-11-27"}, None)
        self.assertEqual(chart_quote["price"], 59000.0)
        self.assertNotIn("fallback_used", chart_quote)

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
