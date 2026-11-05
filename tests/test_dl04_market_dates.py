import unittest
from datetime import datetime, timezone
from unittest.mock import patch

from src.sources import us_market
from src.fetch_data import _market_quote_table, _treasury_yield_table


class _Response:
    status_code = 200

    def __init__(self, payload):
        self.payload = payload

    def raise_for_status(self):
        return None

    def json(self):
        return self.payload


def yahoo_payload(timestamp, exchange_timezone):
    return {
        "chart": {
            "result": [{
                "meta": {"exchangeTimezoneName": exchange_timezone},
                "timestamp": [timestamp],
                "indicators": {"quote": [{
                    "open": [100.0], "high": [102.0], "low": [99.0], "close": [101.0]
                }]}
            }]
        }
    }


class YahooExchangeTimezoneTests(unittest.TestCase):
    def test_quote_uses_exchange_timezone_not_utc_date(self):
        timestamp = int(datetime(2026, 11, 5, 0, 30, tzinfo=timezone.utc).timestamp())
        with patch("src.sources.us_market.requests.get",
                   return_value=_Response(yahoo_payload(timestamp, "America/New_York"))):
            result = us_market.quote("^GSPC")
        self.assertTrue(result["ok"])
        self.assertEqual(result["date"], "2026-11-04")
        self.assertEqual(result["exchange_timezone"], "America/New_York")

    def test_ohlc_uses_exchange_timezone_not_utc_date(self):
        timestamp = int(datetime(2026, 11, 5, 0, 30, tzinfo=timezone.utc).timestamp())
        with patch("src.sources.us_market.requests.get",
                   return_value=_Response(yahoo_payload(timestamp, "America/New_York"))):
            result = us_market.ohlc("^GSPC")
        self.assertTrue(result["ok"])
        self.assertEqual(result["date"], "2026-11-04")
        self.assertEqual(result["exchange_timezone"], "America/New_York")

    def test_unknown_exchange_timezone_falls_back_to_utc(self):
        timestamp = int(datetime(2026, 11, 5, 0, 30, tzinfo=timezone.utc).timestamp())
        with patch("src.sources.us_market.requests.get",
                   return_value=_Response(yahoo_payload(timestamp, "Invalid/Zone"))):
            result = us_market.quote("TEST")
        self.assertEqual(result["date"], "2026-11-05")
        self.assertEqual(result["exchange_timezone"], "Invalid/Zone")


class MarketReportDateTests(unittest.TestCase):
    def test_yahoo_report_table_includes_exchange_local_data_date(self):
        table = _market_quote_table([
            ("S&P 500", {"symbol": "^GSPC", "price": 6000, "change": 10,
                         "pct": 0.1, "date": "2026-11-04"})
        ], "收盤／最新值")
        self.assertIn("資料日期（交易所時區）", table)
        self.assertIn("2026-11-04", table)

    def test_missing_yahoo_date_is_explicitly_unavailable(self):
        table = _market_quote_table([
            ("S&P 500", {"symbol": "^GSPC", "price": None, "change": None,
                         "pct": None, "date": None})
        ], "收盤／最新值")
        self.assertIn("| S&P 500 | ^GSPC | unavailable | unavailable | unavailable | unavailable |", table)

    def test_treasury_report_table_shows_each_tenor_date(self):
        yields = {
            "2Y": {"yield": 3.5, "chg": 0.01, "date": "2026-11-04", "source": "FiscalData"},
            "10Y": {"yield": 4.1, "chg": 0.02, "date": "2026-11-04", "source": "FiscalData"},
            "20Y": {"yield": 4.5, "chg": 0.03, "date": "2026-11-03", "source": "Treasury XML"},
            "30Y": {"yield": 4.7, "chg": 0.04, "date": None, "source": "unavailable"},
        }
        table = _treasury_yield_table(yields)
        self.assertIn("資料日期", table)
        self.assertEqual(table.count("2026-11-04"), 2)
        self.assertIn("2026-11-03", table)
        self.assertIn("unavailable", table)


if __name__ == "__main__":
    unittest.main()
