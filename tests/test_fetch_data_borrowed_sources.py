from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]


class BorrowedSecuritiesSourceContractTests(unittest.TestCase):
    def test_spot_source_tracks_each_borrowed_field_independently(self):
        source = (ROOT / "src/sources/spot.py").read_text(encoding="utf-8")
        self.assertIn('sources["sbl_bal"]', source)
        self.assertIn('sources["sbl_sale_bal_listed"]', source)
        self.assertIn('sources["sbl_sale_bal_otc"]', source)
        self.assertIn('sources["sbl_sale_chg_listed"]', source)
        self.assertIn('sources["sbl_sale_chg_otc"]', source)
        self.assertIn('sources["sbl_sale_bal"]', source)
        self.assertIn('sources["sbl_sale_chg"]', source)
        self.assertNotIn('sources["sbl"] =', source)
        self.assertIn('twse_twt72u_sbl(roc)', source)
        self.assertIn('twse_twt93u_sbl(roc)', source)
        self.assertIn('tpex_sbl(roc)', source)
        self.assertNotIn('_add(_add(stw["tw"], stw["otc"]), stp["bal"])', source)
        self.assertIn('TWT96U 是當日可借券賣出股數', source)

    def test_raw_borrowed_parsers_emit_diagnostics_when_unavailable(self):
        source = (ROOT / "src/sources/spot_raw.py").read_text(encoding="utf-8")
        self.assertIn("[WARN] TWT93U", source)
        self.assertIn("TWT93U official 合計 row accepted", source)
        self.assertIn("[WARN] TPEX margin_sbl", source)
        self.assertIn("[INFO] TPEX margin_sbl parsed rows=", source)

    def test_report_uses_field_specific_source_labels(self):
        source = (ROOT / "src/fetch_data.py").read_text(encoding="utf-8")
        self.assertIn('SRC_SBL_BAL = _src.get("sbl_bal"', source)
        self.assertIn('SRC_SBL_SALE_BAL = _src.get("sbl_sale_bal"', source)
        self.assertIn('SRC_SBL_SALE_CHG = _src.get("sbl_sale_chg"', source)
        self.assertIn('("整體市場借券餘額", _fi(sb["bal"]), "張", SRC_SBL_BAL)', source)
        self.assertIn('def _sbl_market_table(sb: dict)', source)
        self.assertIn('sb.get("listed_sale_bal")', source)
        self.assertIn('sb.get("otc_sale_bal")', source)
        self.assertIn('sb.get("sale_bal")', source)
        self.assertIn('sb.get("listed_sale_chg")', source)
        self.assertIn('sb.get("otc_sale_chg")', source)
        self.assertIn('sb.get("sale_chg")', source)
        self.assertIn('("項目", "上市", "上櫃", "兩者合計", "單位")', source)
        self.assertNotIn("SRC_SBL)", source)


if __name__ == "__main__":
    unittest.main()
