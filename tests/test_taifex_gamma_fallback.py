import unittest
from unittest.mock import Mock, patch

from src.sources.taifex import (
    BASE, DATE_EPS, _LAST_FETCH_ERRORS, _get, _gamma_status, _chain_rollover,
    _sync_gamma_unavailable, _valid_gex_levels, _complete_sum, _complete_ratio, _oi_distribution,
)


class GammaFallbackAvailabilityTests(unittest.TestCase):
    def test_gamma_levels_fetch_uses_requested_t0_date(self):
        response = Mock(status_code=200)
        response.json.return_value = {
            "ok": True,
            "date": "2026-10-30",
            "data": {"levels": []},
        }
        with patch("src.sources.taifex.requests.get", return_value=response) as get:
            payload = _get("options-gamma-levels", "2026-10-30")

        self.assertIsNotNone(payload)
        self.assertIn("options-gamma-levels", DATE_EPS)
        self.assertEqual(
            get.call_args.args[0],
            f"{BASE}/options-gamma-levels?date=2026-10-30",
        )

    def test_worker_http_502_preserves_stage_and_detail(self):
        response = Mock(status_code=502)
        response.json.return_value = {
            "ok": False,
            "error_code": "TAIEX_SPOT_UNAVAILABLE",
            "stage": "taiex_underlying",
            "error": "TAIEX underlying price unavailable",
            "detail": "TWSE FMTQIK HTTP 503",
            "data": {"reason": "TWSE FMTQIK HTTP 503"},
        }
        with patch("src.sources.taifex.requests.get", return_value=response):
            with patch("time.sleep", return_value=None):
                payload = _get("options-gamma-levels", "2026-10-30")

        self.assertIsNone(payload)
        diagnostic = _LAST_FETCH_ERRORS["options-gamma-levels"]
        self.assertEqual(diagnostic["error_code"], "TAIEX_SPOT_UNAVAILABLE")
        self.assertEqual(diagnostic["stage"], "taiex_underlying")
        self.assertEqual(diagnostic["detail"], "TWSE FMTQIK HTTP 503")
        self.assertEqual(diagnostic["http_status"], 502)

    def test_worker_http_200_ok_false_preserves_data_reason(self):
        response = Mock(status_code=200)
        response.json.return_value = {
            "ok": False,
            "error_code": "GEX_NO_COMMON_EXPIRY",
            "stage": "gex_input_match",
            "error": "GEX unavailable",
            "data": {"reason": "No common Chain/Delta expiry"},
        }
        with patch("src.sources.taifex.requests.get", return_value=response):
            with patch("time.sleep", return_value=None):
                payload = _get("options-gamma-levels", "2026-10-30")

        self.assertIsNone(payload)
        diagnostic = _LAST_FETCH_ERRORS["options-gamma-levels"]
        self.assertEqual(diagnostic["error_code"], "GEX_NO_COMMON_EXPIRY")
        self.assertEqual(diagnostic["stage"], "gex_input_match")
        self.assertEqual(diagnostic["data_reason"], "No common Chain/Delta expiry")

    def test_validates_source_schema_and_sorts_levels(self):
        rows = [
            {"strike": 45600, "call_gex_1pct": 20, "put_gex_1pct": -5,
             "net_gex_1pct": 15, "gross_gex_1pct": 25},
            {"strike": 45500, "call_gex_1pct": 10, "put_gex_1pct": -8,
             "net_gex_1pct": 2, "gross_gex_1pct": 18},
            {"strike": 0, "call_gex_1pct": 1, "put_gex_1pct": -1,
             "net_gex_1pct": 0, "gross_gex_1pct": 2},
            {"strike": 45700, "call_gex_1pct": "bad", "put_gex_1pct": -1,
             "net_gex_1pct": 0, "gross_gex_1pct": 2},
        ]
        result = _valid_gex_levels(rows)
        self.assertEqual([row["strike"] for row in result], [45500.0, 45600.0])
        self.assertEqual(result[0]["net_gex_1pct"], 2.0)

    def test_missing_levels_returns_empty_list(self):
        self.assertEqual(_valid_gex_levels(None), [])
    def test_proxy_success_clears_recovered_gamma_fields(self):
        unavailable = ["gamma_wall", "gamma_flip", "gex"]
        result = _sync_gamma_unavailable(unavailable, 44500, 44049.22)
        self.assertEqual(result, ["gex"])

    def test_partial_proxy_keeps_missing_gamma_field_unavailable(self):
        unavailable = ["gamma_wall", "gamma_flip"]
        result = _sync_gamma_unavailable(unavailable, 44500, None)
        self.assertEqual(result, ["gamma_flip"])

    def test_no_gamma_values_keeps_both_unavailable(self):
        unavailable = ["gamma_wall", "gamma_flip"]
        result = _sync_gamma_unavailable(unavailable, None, None)
        self.assertEqual(result, unavailable)

    def test_primary_502_with_proxy_values_is_not_unavailable(self):
        unavailable, notes = _gamma_status(
            [], True, 44500, 44049.22, "options-market-structure-compact (proxy)"
        )
        self.assertEqual(unavailable, [])
        self.assertEqual(len(notes), 1)
        self.assertIn("原始端點不可用", notes[0])
        self.assertIn("備援取得", notes[0])
        self.assertNotIn("unavailable", notes[0])

    def test_partial_proxy_marks_only_missing_field_unavailable(self):
        unavailable, notes = _gamma_status([], True, 44500, None, "compact proxy")
        self.assertEqual(unavailable, ["gamma_flip"])
        self.assertEqual(len(notes), 2)
        self.assertIn("Wall 有值", notes[0])
        self.assertIn("Gamma Flip 無資料", notes[1])

    def test_primary_and_proxy_failure_marks_both_unavailable(self):
        unavailable, notes = _gamma_status([], True, None, None, "compact proxy")
        self.assertEqual(unavailable, ["gamma_wall", "gamma_flip"])
        self.assertEqual(len(notes), 2)
        self.assertTrue(all("unavailable" in note for note in notes))





class CompleteAggregateContractTests(unittest.TestCase):
    def test_futures_institutional_oi_requires_all_three_values(self):
        self.assertEqual(_complete_sum([100, 20, 3]), 123)
        self.assertIsNone(_complete_sum([100, None, 3]))
        self.assertIsNone(_complete_sum([None, None, None]))

    def test_zero_is_a_valid_oi_or_volume_value(self):
        self.assertEqual(_complete_sum([0, 2, 3]), 5)
        self.assertEqual(_complete_sum([0, 0]), 0)

    def test_option_chain_empty_side_is_unavailable(self):
        self.assertIsNone(_complete_sum([]))
        self.assertIsNone(_complete_ratio(100, None))

    def test_option_chain_partial_row_invalidates_only_that_aggregate(self):
        self.assertIsNone(_complete_sum([10, None, 5]))
        self.assertEqual(_complete_sum([10, 0, 5]), 15)

    def test_ratios_require_complete_nonzero_denominator(self):
        self.assertEqual(_complete_ratio(20, 10), 2)
        self.assertIsNone(_complete_ratio(20, 0))
        self.assertIsNone(_complete_ratio(None, 10))
        self.assertIsNone(_complete_ratio(20, None))

    def test_oi_distribution_uses_complete_denominator(self):
        rows = [{"strike": 100, "open_interest": 25},
                {"strike": 110, "open_interest": 75}]
        result = _oi_distribution(rows)
        self.assertEqual([row["pct"] for row in result], [75.0, 25.0])

    def test_partial_oi_distribution_preserves_values_but_hides_percentages(self):
        rows = [{"strike": 100, "open_interest": 25},
                {"strike": 110, "open_interest": None},
                {"strike": 120, "open_interest": 75}]
        result = _oi_distribution(rows)
        self.assertEqual([row["oi"] for row in result], [75, 25, None])
        self.assertTrue(all(row["pct"] is None for row in result))

    def test_empty_oi_distribution_is_empty(self):
        self.assertEqual(_oi_distribution([]), [])


class ChainRolloverThreeStateTests(unittest.TestCase):
    def test_explicit_same_primary_month_means_no_rollover(self):
        result = _chain_rollover(
            [{"type": "call", "contract_month": "202611", "open_interest": 100}],
            "202611", "202611")
        self.assertEqual(result, (False, "202611"))

    def test_explicit_different_primary_month_means_rollover(self):
        result = _chain_rollover([], "202611", "202612")
        self.assertEqual(result, (True, "202611"))

    def test_missing_prior_primary_is_unknown_even_if_chain_looks_populated(self):
        # Chain may be partial; its OI ranking cannot establish the prior primary expiry.
        rows = [
            {"type": "call", "contract_month": "202611", "open_interest": 10000},
            {"type": "call", "contract_month": "202612", "open_interest": 100},
            {"type": "put", "contract_month": "202611", "open_interest": 9000},
        ]
        self.assertEqual(_chain_rollover(rows, None, "202611"), (None, None))

    def test_missing_current_primary_is_unknown(self):
        self.assertEqual(_chain_rollover([], "202611", None), (None, "202611"))

    def test_empty_or_invalid_snapshot_chain_does_not_infer_old_primary(self):
        for rows in ([], None, [{"type": "call", "contract_month": "202611",
                                 "open_interest": None}]):
            with self.subTest(rows=rows):
                self.assertEqual(_chain_rollover(rows, None, "202611"), (None, None))


if __name__ == "__main__":
    unittest.main()
