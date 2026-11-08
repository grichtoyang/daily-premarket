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

from src.sources.taifex import _options_chain_oi_change


class OptionsChainOICoverageTests(unittest.TestCase):
    def test_daily_change_uses_only_common_contracts_and_discloses_coverage(self):
        current = [
            {"contract_month": "202611F1", "contract_expiry_date": "2026-11-11",
             "strike": 40000, "type": "call", "open_interest": 120},
            {"contract_month": "202611F1", "contract_expiry_date": "2026-11-11",
             "strike": 40000, "type": "put", "open_interest": 80},
            {"contract_month": "202611F1", "contract_expiry_date": "2026-11-11",
             "strike": 40500, "type": "call", "open_interest": 50},
        ]
        previous = [
            {"contract_month": "202611F1", "contract_expiry_date": "2026-11-11",
             "strike": 40000, "type": "call", "open_interest": 100},
            {"contract_month": "202611F1", "contract_expiry_date": "2026-11-11",
             "strike": 40000, "type": "put", "open_interest": 90},
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

    def test_no_common_contracts_remains_unavailable(self):
        current = [{"contract_month": "202611F1", "contract_expiry_date": "2026-11-11",
                    "strike": 40500, "type": "call", "open_interest": 50}]
        previous = [{"contract_month": "202611F1", "contract_expiry_date": "2026-11-11",
                     "strike": 40000, "type": "call", "open_interest": 100}]
        self.assertIsNone(_options_chain_oi_change(current, previous, "202611F1"))

    def test_invalid_or_duplicate_contract_identity_remains_unavailable(self):
        row = {"contract_month": "202611F1", "contract_expiry_date": "2026-11-11",
               "strike": 40000, "type": "call", "open_interest": 100}
        self.assertIsNone(_options_chain_oi_change([row, dict(row)], [row], "202611F1"))


if __name__ == "__main__":
    unittest.main()
