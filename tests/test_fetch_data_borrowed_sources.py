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


    def test_market_quote_table_includes_data_and_retrieval_metadata(self):
        from src.fetch_data import _market_quote_table
        table = _market_quote_table([
            ("S&P 500", {
                "symbol": "^GSPC", "price": 6000, "change": 12, "pct": 0.2,
                "date": "2026-11-05", "retrieved_at": "2026-11-06T00:30:00+00:00",
                "exchange_timezone": "America/New_York", "source": "Yahoo Finance Chart API",
            })
        ], "收盤／最新值")
        self.assertIn("資料日期（交易所時區）", table)
        self.assertIn("擷取時間（UTC）", table)
        self.assertIn("交易所時區", table)
        self.assertIn("2026-11-05", table)
        self.assertIn("2026-11-06T00:30:00+00:00", table)
        self.assertIn("America/New_York", table)

    def test_partial_only_coverage_status(self):
        from src.fetch_data import _coverage_status_lines
        self.assertEqual(_coverage_status_lines(["spot.margin_a"], []), [
            "- 部分取得欄位 (1)：spot.margin_a",
            "- 未取得欄位 (0)：無",
        ])

    def test_unavailable_only_coverage_status(self):
        from src.fetch_data import _coverage_status_lines
        self.assertEqual(_coverage_status_lines([], ["futures.oi"]), [
            "- 部分取得欄位 (0)：無",
            "- 未取得欄位 (1)：futures.oi",
        ])

    def test_partial_and_unavailable_coverage_status(self):
        from src.fetch_data import _coverage_status_lines
        self.assertEqual(_coverage_status_lines(["spot.margin_a"], ["futures.oi"]), [
            "- 部分取得欄位 (1)：spot.margin_a",
            "- 未取得欄位 (1)：futures.oi",
        ])

    def test_neither_coverage_status(self):
        from src.fetch_data import _coverage_status_lines
        self.assertEqual(_coverage_status_lines([], []), [
            "- 部分取得欄位 (0)：無",
            "- 未取得欄位 (0)：無",
        ])


    def test_treasury_api_and_xml_records_include_utc_retrieval_timestamp(self):
        from datetime import datetime
        from src.sources import treasury
        from unittest.mock import patch

        class Response:
            status_code = 200
            text = "<ROOT><G_NEW_DATE><BID_CURVE_DATE>11/05/2026</BID_CURVE_DATE><BC_2YEAR>3.5</BC_2YEAR></G_NEW_DATE></ROOT>"

            def json(self):
                return {"data": [
                    {"record_date": "2026-11-05", "2 Yr": "3.5", "10 Yr": "4.1",
                     "20 Yr": "4.6", "30 Yr": "4.7"},
                    {"record_date": "2026-11-04", "2 Yr": "3.4", "10 Yr": "4.0",
                     "20 Yr": "4.5", "30 Yr": "4.6"},
                ]}

            def raise_for_status(self):
                return None

        with patch("requests.get", return_value=Response()):
            api = treasury._treasury()
            xml = treasury._xml_yield("BC_2YEAR")

        for item in list(api.values()) + [xml]:
            self.assertIsNotNone(datetime.fromisoformat(item["retrieved_at"]))
            self.assertIsNotNone(item["date"])

    def test_treasury_yahoo_fallback_preserves_source_retrieval_timestamp(self):
        from src.sources import treasury
        from unittest.mock import patch

        quote_data = {
            "price": 4.2, "change": 0.1, "date": "2026-11-05",
            "retrieved_at": "2026-11-06T00:30:00+00:00", "ok": True,
        }
        with patch.object(treasury, "_treasury", return_value=None), patch.object(treasury, "_xml_yield", return_value={
                 "yield": 3.5, "chg": 0.1, "date": "2026-11-05",
                 "retrieved_at": "2026-11-06T00:20:00+00:00",
                 "source": "Treasury XML", "ok": True,
             }), patch.object(treasury, "quote", return_value=quote_data):
            result = treasury.get_yields()

        self.assertEqual(result["10Y"]["retrieved_at"], quote_data["retrieved_at"])
        self.assertEqual(result["2Y"]["retrieved_at"], "2026-11-06T00:20:00+00:00")

    def test_treasury_yield_table_displays_per_tenor_retrieval_timestamp(self):
        from src.fetch_data import _treasury_yield_table
        yields = {
            key: {"yield": 4.0, "chg": 0.1, "date": "2026-11-05",
                  "retrieved_at": f"2026-11-06T00:{minute}:00+00:00",
                  "source": "U.S. Treasury FiscalData API"}
            for key, minute in (("2Y", "01"), ("10Y", "02"), ("20Y", "03"), ("30Y", "04"))
        }
        table = _treasury_yield_table(yields)
        self.assertIn("擷取時間（UTC）", table)
        for minute in ("01", "02", "03", "04"):
            self.assertIn(f"2026-11-06T00:{minute}:00+00:00", table)


    def test_futures_night_proxy_fields_only_show_source_when_available(self):
        source = (ROOT / "src/fetch_data.py").read_text(encoding="utf-8")
        self.assertIn('("成交量", _fi(n["vol"]), _nvia if n["vol"] is not None else _nmiss)', source)
        self.assertIn('("結算價", _fi(n["settle"]), _nvia if n["settle"] is not None else _nmiss)', source)
        self.assertIn('("未平倉量", _fi(n["oi"]), _nvia if n["oi"] is not None else _nmiss)', source)
        self.assertNotIn('("成交量", _fi(n["vol"]), SRC_FX)', source)
        self.assertNotIn('("結算價", _fi(n["settle"]), SRC_FX)', source)
        self.assertNotIn('("未平倉量", _fi(n["oi"]), SRC_FX)', source)


    def test_options_timestamp_is_labeled_as_report_generation_time(self):
        source = (ROOT / "src/fetch_data.py").read_text(encoding="utf-8")
        self.assertIn('("報告產製時間", now, "本機")', source)
        self.assertNotIn('("資料更新時間", now, "本機")', source)

    def test_taifex_report_generation_timestamp_label_and_legacy_freeze(self):
        from src.fetch_data import _freeze_src_time

        source = (ROOT / "src/fetch_data.py").read_text(encoding="utf-8")
        self.assertIn(
            'A(f"- 資料日期：{t0}；報告產製時間：{now}；時區：`Asia/Taipei`")',
            source,
        )
        self.assertIn("選擇權交易日期、到期日與報告產製時間", source)
        self.assertNotIn("選擇權交易日期、到期日與資料時間", source)
        old = "- 資料日期：2026-11-06；資料時間：2026-11-06 08:00:00；時區：`Asia/Taipei`"
        new = "- 資料日期：2026-11-06；報告產製時間：2026-11-06 09:00:00；時區：`Asia/Taipei`"
        frozen = _freeze_src_time(old, new)
        self.assertIn("報告產製時間：2026-11-06 08:00:00", frozen)
        self.assertNotIn("資料時間：", frozen)


if __name__ == "__main__":
    unittest.main()
