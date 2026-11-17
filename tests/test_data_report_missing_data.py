import unittest
from unittest.mock import patch

from src.fetch_data import _asia_stale_note, _history_pair_for_t0
from src.sources import taifex, taifex_official


class DataReportMissingDataTests(unittest.TestCase):
    def test_position_deltas_are_available_independent_of_expiry_rollover(self):
        snapshot = {
            "fut_trade_day": [
                {"institution": "foreign", "net_volume": 100},
                {"institution": "dealer", "net_volume": -20},
            ],
            "opt_pos_day": [
                {"institution": "foreign", "net_volume": 30},
                {"institution": "dealer", "net_volume": -5},
            ],
        }
        fut_trade = {
            ("day", "foreign"): {"net": 125},
            ("day", "dealer"): {"net": -10},
        }
        opt_pos = {
            "foreign": {"net": 40},
            "dealer": {"net": -8},
        }

        result = taifex._snapshot_position_change(snapshot, True, fut_trade, opt_pos)

        self.assertEqual(result["foreign"], {"fut_chg": 25, "opt_chg": 10})
        self.assertEqual(result["dealer"], {"fut_chg": 10, "opt_chg": -3})

    def test_untrusted_position_snapshot_stays_unavailable(self):
        result = taifex._snapshot_position_change({}, False, {}, {})
        self.assertEqual(result["foreign"], {"fut_chg": None, "opt_chg": None})
        self.assertEqual(result["dealer"], {"fut_chg": None, "opt_chg": None})

    def test_pcr_pair_requires_exact_t0_and_previous_trading_day(self):
        rows = [
            {"date": "2026-11-12", "vol_ratio": 80, "oi_ratio": 90},
            {"date": "2026-11-13", "vol_ratio": 82, "oi_ratio": 91},
        ]
        self.assertIsNone(_history_pair_for_t0(rows, "2026-11-16", "2026-11-13"))

        rows.append({"date": "2026-11-16", "vol_ratio": 84, "oi_ratio": 93})
        pair = _history_pair_for_t0(rows, "2026-11-16", "2026-11-13")
        self.assertEqual([row["date"] for row in pair], ["2026-11-13", "2026-11-16"])

    def test_pcr_pair_rejects_missing_or_duplicate_previous_date(self):
        rows = [
            {"date": "2026-11-13", "vol_ratio": 82, "oi_ratio": 91},
            {"date": "2026-11-13", "vol_ratio": 83, "oi_ratio": 92},
            {"date": "2026-11-16", "vol_ratio": 84, "oi_ratio": 93},
        ]
        self.assertIsNone(_history_pair_for_t0(rows, "2026-11-16", "2026-11-13"))

    def test_asia_quote_date_mismatch_is_explicitly_flagged(self):
        mk = {
            "亞洲主要指數": [
                ("日經225", {"symbol": "^N225", "date": "2026-11-13", "price": 50000}),
                ("韓國KOSPI", {"symbol": "^KS11", "date": "2026-11-13", "price": 4000}),
            ]
        }
        note = _asia_stale_note(mk, "2026-11-16")
        self.assertIn("日期與 T0", note)
        self.assertIn("2026-11-13", note)
        self.assertIn("不可當成當日同步訊號", note)

    def test_empty_taifex_response_is_not_cached_for_later_retry(self):
        class BadResponse:
            def raise_for_status(self):
                return None

            def json(self):
                raise ValueError("non-JSON response")

        class GoodResponse:
            def raise_for_status(self):
                return None

            def json(self):
                return [{"Date": "20261116"}]

        taifex_official._cache.pop("/OpenInterestOfLargeTradersOptions", None)
        with patch("src.sources.taifex_official.requests.get",
                   side_effect=[BadResponse(), BadResponse(), GoodResponse()]) as get:
            with patch("time.sleep", return_value=None):
                first = taifex_official._get("/OpenInterestOfLargeTradersOptions")
                second = taifex_official._get("/OpenInterestOfLargeTradersOptions")
        self.assertEqual(first, [])
        self.assertEqual(second, [{"Date": "20261116"}])
        self.assertEqual(get.call_count, 3)
        taifex_official._cache.pop("/OpenInterestOfLargeTradersOptions", None)


if __name__ == "__main__":
    unittest.main()
