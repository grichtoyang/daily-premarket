import sys
import types
import unittest

try:
    import requests  # noqa: F401
except ImportError:
    class _Timeout(Exception):
        pass
    _requests_stub = types.ModuleType("requests")
    _requests_stub.exceptions = types.SimpleNamespace(Timeout=_Timeout)
    sys.modules["requests"] = _requests_stub

from src.sources.taifex import _missing_night_fields


class NightUnavailableSummaryTests(unittest.TestCase):
    def test_night_settlement_and_oi_are_not_missing_because_exchange_does_not_publish_them(self):
        night = {
            "open": 45395, "high": 45420, "low": 44052, "close": 44433,
            "change": -867, "pct": -1.91, "vol": 44305,
            "settle": None, "oi": None,
        }
        self.assertEqual(_missing_night_fields(night), [])

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
             ("open", "high", "low", "close", "change", "pct", "vol")],
        )


if __name__ == "__main__":
    unittest.main()
