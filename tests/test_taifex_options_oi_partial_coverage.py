import sys
import types
import unittest
from unittest.mock import patch

try:
    import requests  # noqa: F401
except ImportError:
    class _Timeout(Exception):
        pass
    _requests_stub = types.ModuleType("requests")
    _requests_stub.exceptions = types.SimpleNamespace(Timeout=_Timeout)
    sys.modules["requests"] = _requests_stub

from src.sources.taifex import (
    _options_chain_oi_change,
    _options_chain_oi_change_diagnostic,
    _options_chain_key_levels_for_month,
    _previous_trading_day_iso,
)


def contract(month, expiry, strike, kind, oi):
    return {"contract_month": month, "contract_expiry_date": expiry,
            "strike": strike, "type": kind, "open_interest": oi}


class OptionsChainOICoverageTests(unittest.TestCase):
    def test_daily_change_uses_only_common_contracts_and_discloses_coverage(self):
        current = [
            contract("202611F1", "2026-11-11", 40000, "call", 120),
            contract("202611F1", "2026-11-11", 40000, "put", 80),
            contract("202611F1", "2026-11-11", 40500, "call", 50),
        ]
        previous = [
            contract("202611F1", "2026-11-11", 40000, "call", 100),
            contract("202611F1", "2026-11-11", 40000, "put", 90),
        ]
        result = _options_chain_oi_change(current, previous, "202611F1")
        self.assertIsNotNone(result)
        self.assertEqual(result["c_chg"], 20)
        self.assertEqual(result["p_chg"], -10)
        self.assertEqual(result["matched_count"], 2)
        self.assertEqual(result["current_count"], 3)
        self.assertEqual(result["previous_count"], 2)
        self.assertAlmostEqual(result["current_coverage"], 2 / 3)
        self.assertEqual(result["previous_coverage"], 1.0)
        self.assertTrue(result["partial"])

    def test_compact_and_iso_expiry_dates_match_as_same_contracts(self):
        current = [
            contract("202611F3", "20261120", 42000, "call", 3369),
            contract("202611F3", "20261120", 42000, "put", 1992),
        ]
        previous = [
            contract("202611F3", "2026-11-20", 42000, "call", 0),
            contract("202611F3", "2026-11-20", 42000, "put", 0),
        ]
        result = _options_chain_oi_change(current, previous, "202611F3")
        diagnostic = _options_chain_oi_change_diagnostic(current, previous, "202611F3")
        self.assertIsNotNone(result)
        self.assertEqual(result["matched_count"], 2)
        self.assertEqual(result["c_chg"], 3369)
        self.assertEqual(result["p_chg"], 1992)
        self.assertEqual(diagnostic["reason"], "aligned")
        self.assertEqual(diagnostic["current_only"], 0)
        self.assertEqual(diagnostic["previous_only"], 0)

    def test_different_expiry_dates_do_not_match_after_normalization(self):
        current = [contract("202611F3", "20261120", 42000, "call", 120)]
        previous = [contract("202611F3", "2026-11-21", 42000, "call", 100)]
        self.assertIsNone(_options_chain_oi_change(current, previous, "202611F3"))
        diagnostic = _options_chain_oi_change_diagnostic(current, previous, "202611F3")
        self.assertEqual(diagnostic["reason"], "no_common_valid_contracts")
        self.assertEqual(diagnostic["current_only"], 1)
        self.assertEqual(diagnostic["previous_only"], 1)

    def test_normalized_expiry_keeps_strike_and_option_type_distinct(self):
        current = [
            contract("202611F3", "20261120", 42000, "call", 120),
            contract("202611F3", "20261120", 42000, "put", 80),
        ]
        previous = [
            contract("202611F3", "2026-11-20", 42000, "call", 100),
            contract("202611F3", "2026-11-20", 42100, "put", 70),
        ]
        result = _options_chain_oi_change(current, previous, "202611F3")
        self.assertIsNotNone(result)
        self.assertEqual(result["matched_count"], 1)
        self.assertEqual(result["c_chg"], 20)
        self.assertIsNone(result["p_chg"])


    def test_missing_oi_is_skipped_without_zero_fill_and_coverage_uses_all_identities(self):
        current = [
            contract("202611", "2026-11-18", 40000, "call", 110),
            contract("202611", "2026-11-18", 40000, "put", None),
            contract("202611", "2026-11-18", 40500, "call", 50),
        ]
        previous = [
            contract("202611", "2026-11-18", 40000, "call", 100),
            contract("202611", "2026-11-18", 40000, "put", 70),
        ]
        result = _options_chain_oi_change(current, previous, "202611")
        diagnostic = _options_chain_oi_change_diagnostic(current, previous, "202611")
        self.assertIsNotNone(result)
        self.assertEqual(result["c_chg"], 10)
        self.assertIsNone(result["p_chg"])
        self.assertEqual(result["matched_count"], 1)
        self.assertEqual(result["current_count"], 2)
        self.assertEqual(result["current_identity_count"], 3)
        self.assertEqual(result["current_missing_oi"], 1)
        self.assertAlmostEqual(result["current_coverage"], 1 / 3)
        self.assertAlmostEqual(result["previous_coverage"], 1 / 2)
        self.assertTrue(result["partial"])
        self.assertEqual(diagnostic["current_count"], result["current_count"])
        self.assertEqual(diagnostic["current_identity_count"], result["current_identity_count"])
        self.assertEqual(diagnostic["current_missing_oi"], result["current_missing_oi"])
        self.assertEqual(diagnostic["reason"], "open_interest_missing_or_invalid")

    def test_rollover_still_compares_common_contracts_in_current_primary_month(self):
        current = [
            contract("202611F2", "2026-11-13", 40000, "call", 1000),
            contract("202611", "2026-11-18", 40000, "call", 120),
        ]
        previous = [
            contract("202611F2", "2026-11-13", 40000, "call", 900),
            contract("202611", "2026-11-18", 40000, "call", 100),
        ]
        result = _options_chain_oi_change(current, previous, "202611")
        self.assertIsNotNone(result)
        self.assertEqual(result["c_chg"], 20)
        self.assertEqual(result["matched_count"], 1)

    def test_no_common_contracts_remains_unavailable(self):
        current = [contract("202611F1", "2026-11-11", 40500, "call", 50)]
        previous = [contract("202611F1", "2026-11-11", 40000, "call", 100)]
        self.assertIsNone(_options_chain_oi_change(current, previous, "202611F1"))

    def test_invalid_or_duplicate_contract_identity_remains_unavailable(self):
        row = contract("202611F1", "2026-11-11", 40000, "call", 100)
        self.assertIsNone(_options_chain_oi_change([row, dict(row)], [row], "202611F1"))

    def test_walls_and_max_pain_recalculate_for_requested_expiry(self):
        chain = [
            contract("202611", "2026-11-18", 100, "call", 10),
            contract("202611", "2026-11-18", 110, "call", 20),
            contract("202611", "2026-11-18", 100, "put", 15),
            contract("202611", "2026-11-18", 110, "put", 5),
            contract("202611F2", "2026-11-13", 100, "call", 999),
        ]
        result = _options_chain_key_levels_for_month(chain, "202611", "2026-11-18")
        self.assertTrue(result["found"])
        self.assertEqual(result["call_wall"]["strike"], 110)
        self.assertEqual(result["put_wall"]["strike"], 100)
        self.assertEqual(result["max_pain"]["strike"], 100)
        self.assertEqual(result["expiry_date"], "2026-11-18")
        self.assertEqual(result["chain_stats"]["rows"], 4)

    def test_walls_refuse_missing_oi_or_duplicate_identity(self):
        missing = [
            contract("202611", "2026-11-18", 100, "call", 10),
            contract("202611", "2026-11-18", 100, "put", None),
        ]
        self.assertFalse(_options_chain_key_levels_for_month(missing, "202611")["found"])
        duplicate = [
            contract("202611", "2026-11-18", 100, "call", 10),
            contract("202611", "2026-11-18", 100, "call", 11),
            contract("202611", "2026-11-18", 100, "put", 10),
        ]
        self.assertEqual(
            _options_chain_key_levels_for_month(duplicate, "202611")["reason"],
            "duplicate_contract_identity")

    def test_previous_trading_day_uses_shared_calendar(self):
        import src.t0 as calendar
        with patch.object(calendar, "_LAST_CAL_ERROR", ""), patch.object(
            calendar, "load_closed", return_value=set()
        ):
            self.assertEqual(_previous_trading_day_iso("2026-11-16"), "2026-11-13")

    def test_previous_trading_day_loads_prior_year_calendar_when_crossing_year(self):
        import src.t0 as calendar
        calls = []
        def load(year):
            calls.append(year)
            return {"2027-01-01"} if year == 2027 else set()
        with patch.object(calendar, "_LAST_CAL_ERROR", ""), patch.object(
            calendar, "load_closed", side_effect=load
        ):
            self.assertEqual(_previous_trading_day_iso("2027-01-04"), "2026-12-31")
        self.assertIn(2026, calls)


if __name__ == "__main__":
    unittest.main()
