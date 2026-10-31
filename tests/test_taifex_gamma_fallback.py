import unittest

from src.sources.taifex import _sync_gamma_unavailable


class GammaFallbackAvailabilityTests(unittest.TestCase):
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


if __name__ == "__main__":
    unittest.main()
