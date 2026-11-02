import unittest

from src.sources.taifex import _missing_night_fields


class NightUnavailableSummaryTests(unittest.TestCase):
    def test_missing_settlement_and_oi_are_reported(self):
        night = {
            "open": 45395, "high": 45420, "low": 44052, "close": 44433,
            "change": -867, "pct": -1.91, "vol": 44305,
            "settle": None, "oi": None,
        }
        self.assertEqual(
            _missing_night_fields(night),
            ["futures.night.settle", "futures.night.oi"],
        )

    def test_available_night_fields_do_not_appear_as_missing(self):
        night = {
            "open": 45395, "high": 45420, "low": 44052, "close": 44433,
            "change": -867, "pct": -1.91, "vol": 44305,
            "settle": 44433, "oi": 123456,
        }
        self.assertEqual(_missing_night_fields(night), [])

    def test_missing_night_ohlc_and_volume_are_each_listed(self):
        self.assertEqual(
            _missing_night_fields({}),
            [f"futures.night.{field}" for field in
             ("open", "high", "low", "close", "change", "pct", "vol", "settle", "oi")],
        )


if __name__ == "__main__":
    unittest.main()
