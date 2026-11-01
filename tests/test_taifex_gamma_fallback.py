import unittest

from src.sources.taifex import _gamma_status, _sync_gamma_unavailable, _valid_gex_levels


class GammaFallbackAvailabilityTests(unittest.TestCase):
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


if __name__ == "__main__":
    unittest.main()
