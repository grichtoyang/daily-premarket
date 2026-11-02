import unittest
from pathlib import Path

from scripts.v9_pro_builder import validate_data_report_consistency


ROOT = Path(__file__).resolve().parents[1]


class MissingSpotOhlcTests(unittest.TestCase):
    def test_missing_spot_ohlc_is_optional_and_not_imputed(self):
        source = (ROOT / "scripts/v9_pro_builder.py").read_text(encoding="utf-8")
        self.assertIn('spot_open=optional_get(r"開盤', source)
        self.assertIn('spot_high=optional_get(r"最高', source)
        self.assertIn('spot_low=optional_get(r"最低', source)
        self.assertIn('gamma_wall=optional_get(r"Gamma Wall', source)
        self.assertIn('gamma_flip=optional_get(r"Gamma Flip', source)
        self.assertIn('call_wall=optional_get(r"Call Wall', source)
        self.assertIn('max_pain=optional_get(r"Max Pain', source)
        self.assertIn("if all(spot.get(k) is not None for k in ('high','low','close'))", source)
        self.assertIn("'levels': key_levels", source)
        warnings = validate_data_report_consistency(
            {"open": None, "high": None, "low": None, "close": "44920.14"},
            {"foreign": None, "trust": None, "dealer": "0", "all": None},
            {"listed": None, "otc": None, "total": None},
            {"day": {"o": "45000", "h": "45100", "l": "44900", "c": "45020", "basis": None}},
            {"callOi": None, "putOi": None, "pcr": None},
        )
        self.assertEqual(warnings, [])


if __name__ == "__main__":
    unittest.main()
