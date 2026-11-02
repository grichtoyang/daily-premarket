from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]


class BorrowedSecuritiesSourceContractTests(unittest.TestCase):
    def test_spot_source_tracks_each_borrowed_field_independently(self):
        source = (ROOT / "src/sources/spot.py").read_text(encoding="utf-8")
        self.assertIn('sources["sbl_bal"]', source)
        self.assertIn('sources["sbl_sale_bal"]', source)
        self.assertIn('sources["sbl_sale_chg"]', source)
        self.assertNotIn('sources["sbl"] =', source)
        self.assertIn('("TWT96U GRETAI（上櫃）", stw.get("otc"))', source)

    def test_report_uses_field_specific_source_labels(self):
        source = (ROOT / "src/fetch_data.py").read_text(encoding="utf-8")
        self.assertIn('SRC_SBL_BAL = _src.get("sbl_bal"', source)
        self.assertIn('SRC_SBL_SALE_BAL = _src.get("sbl_sale_bal"', source)
        self.assertIn('SRC_SBL_SALE_CHG = _src.get("sbl_sale_chg"', source)
        self.assertIn('("借券餘額", _fi(sb["bal"]), "張", SRC_SBL_BAL)', source)
        self.assertIn('("借券賣出餘額", _fi(sb["sale_bal"]), "張", SRC_SBL_SALE_BAL)', source)
        self.assertIn('("借券賣出增減", _fi(sb["sale_chg"]), "張", SRC_SBL_SALE_CHG)', source)
        self.assertNotIn("SRC_SBL)", source)


if __name__ == "__main__":
    unittest.main()
