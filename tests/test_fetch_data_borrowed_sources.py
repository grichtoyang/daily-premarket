from pathlib import Path
import re
import tempfile
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
        self.assertIn('("整體市場借券餘額", _fi(sb["bal"]), "張", _source_if_available(sb["bal"], SRC_SBL_BAL))', source)
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
        self.assertIn('("成交量", _fi(n["vol"]), "口", _source_if_available(n["vol"], SRC_FX))', source)
        self.assertIn('("結算價", _fi(n["settle"]), "點", _source_if_available(n["settle"], SRC_FX))', source)
        self.assertIn('("未平倉量", _fi(n["oi"]), "口", _source_if_available(n["oi"], SRC_FX))', source)
        self.assertIn('_nvia = "TAIFEX Proxy" if n.get("via") == "proxy" else SRC_FX_OFF', source)
        self.assertIn('_source_if_available(_diff2(n["high"], n["low"]), _nvia)', source)
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


    def test_options_chain_source_labels_only_show_source_when_values_exist(self):
        source = (ROOT / "src/fetch_data.py").read_text(encoding="utf-8")
        expected = [
            "SRC_FX if _ot['c_vol'] is not None else MISSING",
            "SRC_FX if _ot['c_oi'] is not None else MISSING",
            "SRC_FX if _ot['p_vol'] is not None else MISSING",
            "SRC_FX if _ot['p_oi'] is not None else MISSING",
            "SRC_FX if _ot['vol_ratio'] is not None else MISSING",
            "SRC_FX if _ot['oi_ratio'] is not None else MISSING",
            "SRC_FX if _ot['pc_ratio'] is not None else MISSING",
        ]
        for expression in expected:
            with self.subTest(expression=expression):
                self.assertIn(expression, source)
        self.assertNotIn('("Call 總成交量", _fi(_ot[\'c_vol\']), SRC_FX)', source)
        self.assertNotIn('("Call 總未平倉量 OI", _fi(_ot[\'c_oi\']), SRC_FX)', source)
        self.assertNotIn('("Put 總成交量", _fi(_ot[\'p_vol\']), SRC_FX)', source)
        self.assertNotIn('("Put 總未平倉量 OI", _fi(_ot[\'p_oi\']), SRC_FX)', source)

    def test_options_institutional_day_night_source_labels_require_values(self):
        source = (ROOT / "src/fetch_data.py").read_text(encoding="utf-8")
        start = source.index("    def _full_rows(k, zh):")
        end = source.index('    A(_tbl(_full_rows("foreign"', start)
        block = source[start:end]
        self.assertIn('("日盤淨總量", _f2s(_op[k][\'net\']), _op[k][\'net\'])', block)
        self.assertIn('("Call日夜淨增減 (日－夜)", _f2s(c_diff), c_diff)', block)
        self.assertIn('("Put日夜淨增減 (日－夜)", _f2s(p_diff), p_diff)', block)
        self.assertIn("SRC_FX if raw is not None else MISSING", block)
        self.assertNotIn("return [(f\"{zh} {n}\", v, SRC_FX) for n, v in _rows]", block)


    def test_options_chain_concentration_and_walls_source_labels_require_values(self):
        source = (ROOT / "src/fetch_data.py").read_text(encoding="utf-8")
        required = [
            'SRC_FX if _ot[\'expiry\'] is not None else MISSING',
            'SRC_FX if kk is not None and vv is not None else MISSING',
            "SRC_FX if _oc['c_max'][0] is not None and _oc['c_max'][1] is not None else MISSING",
            "SRC_FX if _oc['p_max'][0] is not None and _oc['p_max'][1] is not None else MISSING",
            'SRC_FX if r.get("strike") is not None and r.get("oi") is not None else MISSING',
            "SRC_FX if _w['call'].get('strike') is not None else MISSING",
            "SRC_FX if _w['put'].get('strike') is not None else MISSING",
            "SRC_FX if _w['expiry'] is not None else MISSING",
            "SRC_FX if _w['maxpain'].get('strike') is not None else MISSING",
        ]
        for expression in required:
            with self.subTest(expression=expression):
                self.assertIn(expression, source)

    def test_options_institutional_trade_source_is_row_complete(self):
        source = (ROOT / "src/fetch_data.py").read_text(encoding="utf-8")
        self.assertIn('row_src = SRC_FX if all(v is not None for v in (*day_vals, *night_vals, diff)) else "端點未提供"', source)
        self.assertIn('_tot_src = SRC_FX if all(v is not None for v in (*_tot_day, *_tot_night, _tot_diff)) else "端點未提供"', source)
        self.assertNotIn('_f2s(_diff2(_o_tot("day", "net"), _o_tot("night", "net"))), _ot_src)', source)

    def test_market_combo_source_label_tracks_available_source_families(self):
        from src.fetch_data import _market_combo_source_label

        self.assertEqual(_market_combo_source_label(None, (None, None)), "unavailable")
        self.assertEqual(_market_combo_source_label(0, (None, None)), "twse-proxy")
        self.assertEqual(_market_combo_source_label(None, (0, None)), "TAIFEX Proxy")
        self.assertEqual(_market_combo_source_label(0, (None, 0)), "twse-proxy／TAIFEX Proxy")

        source = (ROOT / "src/fetch_data.py").read_text(encoding="utf-8")
        self.assertIn('def _market_combo_source_label(spot_value, taifex_values)', source)
        self.assertIn('if spot_value is not None:', source)
        self.assertIn('if any(value is not None for value in taifex_values):', source)
        self.assertIn('_dd["spot"], (_dd["foi"], _dd["fday"], _dd["fnight"],', source)
        self.assertIn('_dd["oday"], _dd["onight"], _dd["calld"], _dd["putd"])', source)
        self.assertIn('), _mx_src))', source)
        self.assertNotIn('_mx_combo(_dd), "twse-proxy／TAIFEX Proxy")', source)

    def test_futures_report_source_labels_require_available_values(self):
        source = (ROOT / "src/fetch_data.py").read_text(encoding="utf-8")
        self.assertIn('SRC_FX if d["open"] is not None else MISSING', source)
        self.assertIn('SRC_FX if d["close"] is not None else MISSING', source)
        self.assertIn('SRC_FX if d.get("vol_day") is not None else MISSING', source)
        self.assertIn('SRC_FX if _oi["foreign"]["long"] is not None else MISSING', source)
        self.assertIn('_t10_src if _t10["buy"] is not None else MISSING', source)
        self.assertIn('_fut_trade_rows = [(name, value, unit, src if value != MISSING else MISSING)', source)
        self.assertIn('_source_if_available(_diff2(d["close"], n["close"]),', source)
        self.assertIn('_combine_source_labels(SRC_FX, _nvia)', source)
        self.assertIn('SRC_FX if all(v != MISSING for v in _row[1:-1]) else MISSING', source)
        self.assertIn('_strength_src = SRC_FX if all(v is not None for v in _strength_values) else MISSING', source)
        self.assertIn('_pt_tot_src = SRC_FX if all(v is not None for v in (', source)
        self.assertIn('_t10c_src if _t10c["buy"] is not None else MISSING', source)
        self.assertIn('_t10p_src if _t10p["sell"] is not None else MISSING', source)
        self.assertIn("來源：{SRC_FX if fx['oi_chg'] is not None else MISSING}", source)


    def test_night_scenario_source_labels_require_available_values(self):
        source = (ROOT / "src/fetch_data.py").read_text(encoding="utf-8")
        self.assertIn(
            'f"{_nratio * 100:.2f}%" if _nratio is not None else MISSING, SRC_FX if _nratio is not None else MISSING)',
            source,
        )
        self.assertIn(
            '("夜盤漲跌點數", _f2s(_nchg), _nchg_src)',
            source,
        )
        self.assertNotIn(
            'f"{_nratio * 100:.2f}%" if _nratio is not None else MISSING, SRC_FX)',
            source,
        )
        self.assertIn('_nchg_src = (_nvia if n["change"] is not None else _night_compare_src)', source)
        self.assertIn('_source_if_available(_fgn, SRC_FX)', source)


    def test_value_gated_source_label_helpers(self):
        from src.fetch_data import _combine_source_labels, _source_if_available

        self.assertEqual(_source_if_available(None, "TAIFEX Proxy"), "unavailable")
        self.assertEqual(_source_if_available(0, "TAIFEX Proxy"), "TAIFEX Proxy")
        self.assertEqual(_combine_source_labels("TAIFEX Proxy", "unavailable", "TAIFEX Proxy"),
                         "TAIFEX Proxy")
        self.assertEqual(_combine_source_labels("unavailable", "TAIFEX OpenAPI"),
                         "TAIFEX OpenAPI")
        self.assertEqual(_combine_source_labels("unavailable", "unavailable"), "unavailable")

    def test_cash_market_source_labels_are_value_gated(self):
        source = (ROOT / "src/fetch_data.py").read_text(encoding="utf-8")
        expected = [
            '_source_if_available(tx["close"], SRC_TX)',
            '_source_if_available(tx["open"], SRC_OHLC)',
            '_source_if_available(lb["limit_up"], SRC_LB)',
            '_source_if_available(ob["limit_down"], SRC_OTC)',
            '_source_if_available(inst["total"], SRC_INST)',
            '_source_if_available(mg["fin_yi"], SRC_MG)',
            '_source_if_available(mg["ratio"], SRC_MR)',
            '_source_if_available(sb["bal"], SRC_SBL_BAL)',
            '_source_if_available(to["total"], _combine_source_labels(SRC_LTO, SRC_OTC))',
        ]
        for expression in expected:
            with self.subTest(expression=expression):
                self.assertIn(expression, source)

    def test_external_quote_source_is_unavailable_when_value_is_missing(self):
        from src.fetch_data import _market_quote_table, _treasury_yield_table

        quote_table = _market_quote_table([
            ("No quote", {"symbol": "NONE", "price": None, "change": None, "pct": None,
                          "source": "Yahoo Finance Chart API"})
        ], "最新值")
        self.assertIn("| No quote | NONE | unavailable |", quote_table)

        yields = {
            key: {"yield": None, "chg": None, "date": None, "retrieved_at": None,
                  "source": "Yahoo Finance (備援)"}
            for key in ("2Y", "10Y", "20Y", "30Y")
        }
        treasury_table = _treasury_yield_table(yields)
        self.assertIn("| 美國 10 年期殖利率 | 10 Yr | unavailable | unavailable |", treasury_table)

    def test_options_history_and_gamma_source_labels_are_field_specific(self):
        source = (ROOT / "src/fetch_data.py").read_text(encoding="utf-8")
        self.assertIn('_source_if_available(_vol_ratio_change, _pch_src)', source)
        self.assertIn('_source_if_available(_oi_ratio_change, _pch_src)', source)
        self.assertIn('_gm_flip_src = f"{SRC_FX} ({_gm.get(\'src\', \'\')})" if _gm.get("flip") is not None else MISSING', source)
        self.assertIn('_gm_date_src = f"{SRC_FX} ({_gm.get(\'src\', \'\')})" if _gm.get("date") is not None else MISSING', source)
        self.assertIn('("Gamma Flip 價位", _f2(_gm[\'flip\']), _gm_flip_src)', source)



    def test_section_source_summaries_follow_actual_field_coverage(self):
        source = (ROOT / "src/fetch_data.py").read_text(encoding="utf-8")
        self.assertIn('A(f"**資料來源：** `{_source_if_available(inst[\'foreign\'], SRC_INST)}`")', source)
        self.assertIn('_mg_src_note = SRC_MG if any(mg[k] is not None for k in ("fin_yi", "fin_chg_yi", "s_bal", "s_chg")) else MISSING', source)
        self.assertIn('_source_if_available(to["listed"], SRC_LTO)', source)
        self.assertIn('_source_if_available(to["otc"], SRC_OTC)', source)
        self.assertIn('_ratio_summary_src = "TAIFEX Proxy chain" if any(_ot[k] is not None', source)
        self.assertIn('if any(row[3] != MISSING for row in _pc_rows[3:]) else MISSING', source)
        self.assertIn('備援 TAIFEX Proxy；欄位依實際取得來源標示', source)



class DataReportSemanticRepairTests(unittest.TestCase):
    def test_yahoo_quote_timestamp_is_set_after_successful_response(self):
        from src.sources import us_market
        from unittest.mock import patch
        from datetime import datetime, timezone

        class Response:
            def raise_for_status(self):
                return None
            def json(self):
                return {"chart": {"result": [{
                    "timestamp": [1793836800],
                    "meta": {"exchangeTimezoneName": "America/New_York"},
                    "indicators": {"quote": [{"close": [100.0]}]},
                }]}}

        fixed = datetime(2026, 11, 7, 12, 0, tzinfo=timezone.utc)
        with patch("requests.get", return_value=Response()), patch.object(us_market, "datetime") as clock:
            clock.now.return_value = fixed
            result = us_market.quote("TEST")
        self.assertEqual(result["retrieved_at"], "2026-11-07T12:00:00+00:00")

    def test_yahoo_quote_failure_does_not_claim_retrieval_timestamp(self):
        from src.sources import us_market
        from unittest.mock import patch

        with patch("requests.get", side_effect=RuntimeError("network down")):
            result = us_market.quote("TEST")
        self.assertIsNone(result["retrieved_at"])

    def test_treasury_missing_tenors_fallback_independently(self):
        from src.sources import treasury
        from unittest.mock import patch

        api = {
            "2Y": {"yield": 3.5, "chg": 0.1, "date": "2026-11-06", "source": "FiscalData", "ok": True},
            "10Y": {"yield": 4.1, "chg": 0.1, "date": "2026-11-06", "source": "FiscalData", "ok": True},
            "20Y": {"yield": None, "chg": None, "ok": False},
            "30Y": {"yield": None, "chg": None, "ok": False},
        }
        xml = {"yield": 4.6, "chg": 0.1, "date": "2026-11-06", "source": "Treasury XML", "ok": True}
        yahoo = {"price": 4.7, "change": 0.1, "date": "2026-11-06",
                 "retrieved_at": "2026-11-07T00:00:00+00:00", "ok": True}
        with patch.object(treasury, "_treasury", return_value=api), \
             patch.object(treasury, "_xml_yield", return_value=xml) as xml_mock, \
             patch.object(treasury, "quote", return_value=yahoo) as yahoo_mock:
            result = treasury.get_yields()
        self.assertEqual(result["2Y"]["yield"], 3.5)
        self.assertEqual(result["10Y"]["yield"], 4.1)
        self.assertEqual(result["20Y"]["yield"], 4.6)
        self.assertEqual(result["30Y"]["yield"], 4.7)
        xml_mock.assert_called_once_with("BC_20YEAR")
        yahoo_mock.assert_called_once_with("^TYX")

    def test_finmind_partial_ohlc_is_not_marked_complete(self):
        from src.sources import finmind
        from unittest.mock import patch

        class Response:
            status_code = 200
            def raise_for_status(self):
                return None
            def json(self):
                return {"data": [{
                    "date": "2026-11-06", "stock_id": "TAIEX",
                    "open": "27000", "max": None, "min": "26800",
                    "Trading_money": "1000000000",
                }]}

        with patch("requests.get", return_value=Response()):
            result = finmind.taiex_ohlc("2026-11-06", retries=1)
        self.assertEqual(result["open"], 27000.0)
        self.assertIsNone(result["high"])
        self.assertEqual(result["low"], 26800.0)
        self.assertFalse(result["ok"])

    def test_spot_ohlc_coverage_is_tracked_per_field(self):
        source = (ROOT / "src/sources/spot.py").read_text(encoding="utf-8")
        self.assertIn('for k in ("open", "high", "low"):', source)
        self.assertIn('if fm.get(k) is not None:', source)
        self.assertIn('unavailable.append(f"taiex.{k}")', source)
        self.assertNotIn('if fm["ok"]:\\n        taiex.update', source)

    def test_builder_futures_values_are_scoped_to_exact_section_and_schema(self):
        from scripts.v9_pro_builder import _extract_section_table_value

        report = """### 1．台指期近月日盤行情
| 項目 | 數值 | 資料來源 |
| --- | --- | --- |
| 開盤價 | unavailable | unavailable |
| 成交量 | 12,345 | TAIFEX Proxy |

### 2．台指期近月夜盤行情
| 項目 | 數值 | 資料來源 |
| --- | --- | --- |
| 開盤價 | 27,100 | TAIFEX Proxy |
| 成交量 | 6,789 | TAIFEX Proxy |
"""
        self.assertIsNone(_extract_section_table_value(
            report, "### 1．台指期近月日盤行情", "開盤價"))
        self.assertEqual(_extract_section_table_value(
            report, "### 2．台指期近月夜盤行情", "開盤價"), 27100.0)
        self.assertEqual(_extract_section_table_value(
            report, "### 1．台指期近月日盤行情", "成交量", True), 12345.0)
        self.assertIsNone(_extract_section_table_value(
            report, "### 1．台指期近月日盤行情", "開盤價", True))
        with self.assertRaises(ValueError):
            _extract_section_table_value(
                report, "### 1．台指期近月日盤行情", "不存在欄位", True)

    def test_builder_validates_explicit_futures_units(self):
        from scripts.v9_pro_builder import _extract_section_table_value

        report = """### 1．台指期近月日盤行情
| 項目 | 數值 | 單位 | 資料來源 |
| --- | --- | --- | --- |
| 開盤價 | 27,000 | 點 | TAIFEX Proxy |
| 漲跌幅 | -1.25 | % | TAIFEX Proxy |
| 成交量 | 12,345 | 口 | TAIFEX Proxy |
"""
        self.assertEqual(_extract_section_table_value(
            report, "### 1．台指期近月日盤行情", "開盤價", True, "點"), 27000.0)
        self.assertEqual(_extract_section_table_value(
            report, "### 1．台指期近月日盤行情", "漲跌幅", True, "%"), -1.25)
        self.assertEqual(_extract_section_table_value(
            report, "### 1．台指期近月日盤行情", "成交量", True, "口"), 12345.0)
        with self.assertRaises(ValueError):
            _extract_section_table_value(
                report, "### 1．台指期近月日盤行情", "成交量", True, "點")

    def test_futures_report_tables_declare_units(self):
        source = (ROOT / "src/fetch_data.py").read_text(encoding="utf-8")
        self.assertGreaterEqual(source.count('("項目", "數值", "單位", "資料來源")'), 2)
        self.assertIn('("成交量", _fi(n["vol"]), "口"', source)
        self.assertIn('("未平倉量", _fi(n["oi"]), "口"', source)

    def test_builder_rejects_wrong_futures_table_header(self):
        from scripts.v9_pro_builder import _extract_section_table_value

        report = """### 1．台指期近月日盤行情
| 項目 | 數值 | 單位 |
| --- | --- | --- |
| 開盤價 | 27,000 | 點 |
"""
        with self.assertRaises(ValueError):
            _extract_section_table_value(
                report, "### 1．台指期近月日盤行情", "開盤價", True)


class BuilderUnavailableFieldPropagationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.report = (ROOT / "data_reports" / "DATA_REPORT_20261030.md").read_text(encoding="utf-8")

    def replace_row_value(self, report, heading, label, value="unavailable"):
        start = report.find(heading)
        if start < 0:
            self.fail(f"fixture section not found: {heading}")
        next_heading = re.search(r"(?m)^#{2,4}\s+", report[start + len(heading):])
        end = start + len(heading) + next_heading.start() if next_heading else len(report)
        section = report[start:end]
        pattern = re.compile(rf"(?m)^(\|\s*{re.escape(label)}\s*\|)[^|\n]*(\|)")
        match = pattern.search(section)
        if not match:
            self.fail(f"fixture row not found in {heading}: {label}")
        section = section[:match.start()] + match.group(1) + " " + value + " " + match.group(2) + section[match.end():]
        return report[:start] + section + report[end:]

    def parse_modified(self, report):
        from scripts.v9_pro_builder import parse_data_report
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "DATA_REPORT.md"
            path.write_text(report, encoding="utf-8")
            return parse_data_report(path)

    def test_unavailable_spot_and_institution_fields_are_preserved(self):
        report = self.report
        for heading, label in (
            ("### 1. 台股大盤行情", "加權指數"),
            ("### 1. 台股大盤行情", "漲跌點數"),
            ("### 1. 台股大盤行情", "成交金額"),
            ("#### 2.1 上市公司", "上漲家數"),
            ("#### 2.1 上市公司", "下跌家數"),
            ("### 3. 三大法人現貨買賣超", "自營商"),
            ("### 3. 三大法人現貨買賣超", "三大法人合計"),
        ):
            report = self.replace_row_value(report, heading, label)
        parsed = self.parse_modified(report)
        self.assertIsNone(parsed["spot"]["close"])
        self.assertIsNone(parsed["spot"]["diff"])
        self.assertIsNone(parsed["spot"]["vol"])
        self.assertIsNone(parsed["spot"]["up"])
        self.assertIsNone(parsed["spot"]["down"])
        self.assertIsNone(parsed["inst"]["dealer"])
        self.assertIsNone(parsed["inst"]["all"])

    def test_unavailable_futures_fields_are_preserved(self):
        report = self.report
        for heading, label in (
            ("### 1．台指期近月日盤行情", "開盤價"),
            ("### 3．法人台指期多空未平倉部位", "投信多空淨 OI"),
            ("### 3．法人台指期多空未平倉部位", "自營商多空淨 OI"),
            ("### 4．前十大交易人多空未平倉部位", "前十大交易人多空淨 OI"),
        ):
            report = self.replace_row_value(report, heading, label)
        parsed = self.parse_modified(report)
        self.assertIsNone(parsed["tx"]["day"]["o"])
        self.assertIsNone(parsed["futures"]["trust_oi"])
        self.assertIsNone(parsed["futures"]["dealer_oi"])
        self.assertIsNone(parsed["futures"]["top10"])

    def test_unavailable_option_volume_and_oi_are_preserved(self):
        report = self.report
        for heading, label in (
            ("### 2．Call 總成交量、OI、OI 增減", "Call 總成交量"),
            ("### 2．Call 總成交量、OI、OI 增減", "Call 總未平倉量 OI"),
            ("### 3．Put 總成交量、OI、OI 增減", "Put 總成交量"),
            ("### 3．Put 總成交量、OI、OI 增減", "Put 總未平倉量 OI"),
        ):
            report = self.replace_row_value(report, heading, label)
        parsed = self.parse_modified(report)
        self.assertIsNone(parsed["options"]["callVol"])
        self.assertIsNone(parsed["options"]["callOi"])
        self.assertIsNone(parsed["options"]["putVol"])
        self.assertIsNone(parsed["options"]["putOi"])

    def test_missing_required_option_row_still_fails_closed(self):
        heading = "### 2．Call 總成交量、OI、OI 增減"
        start = self.report.find(heading)
        end_match = re.search(r"(?m)^#{2,4}\s+", self.report[start + len(heading):])
        end = start + len(heading) + end_match.start() if end_match else len(self.report)
        section = self.report[start:end]
        section = re.sub(r"(?m)^\| Call 總成交量 \|[^\n]*\n", "", section, count=1)
        report = self.report[:start] + section + self.report[end:]
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "DATA_REPORT.md"
            path.write_text(report, encoding="utf-8")
            from scripts.v9_pro_builder import parse_data_report
            with self.assertRaisesRegex(ValueError, "Call成交"):
                parse_data_report(path)


class DataReportTurnoverAndUnitContractTests(unittest.TestCase):
    def test_listed_turnover_keeps_finmind_when_proxy_field_is_missing(self):
        from src.sources.spot import _select_listed_turnover

        self.assertEqual(
            _select_listed_turnover(123456789, None),
            (123456789, "FinMind Trading_money"),
        )
        self.assertEqual(
            _select_listed_turnover(123456789, 987654321),
            (987654321, "twse-proxy market_statistics"),
        )
        self.assertEqual(_select_listed_turnover(None, None), (None, None))

        source = (ROOT / "src/sources/spot.py").read_text(encoding="utf-8")
        self.assertIn("_select_listed_turnover(\n        finmind_turnover_yuan, proxy_turnover_yuan)", source)
        self.assertNotIn(
            'listed_turnover_yuan = twse_proxy.parse_listed_turnover(payload)',
            source,
        )

    def test_futures_day_volume_never_falls_back_to_total_volume(self):
        source = (ROOT / "src/fetch_data.py").read_text(encoding="utf-8")
        self.assertIn('("成交量", _fi(d.get("vol_day")), "口",', source)
        self.assertIn('SRC_FX if d.get("vol_day") is not None else MISSING', source)
        self.assertNotIn(
            '_prefer_not_none(d.get("vol_day"), d.get("vol"))',
            source,
        )
        self.assertIn('("成交量", _fi(d["vol_day"]), _fi(n["vol"])', source)

    def test_market_quote_change_header_is_asset_neutral(self):
        from src.fetch_data import _market_quote_table

        table = _market_quote_table([
            ("USD/TWD", {"symbol": "TWD=X", "price": 32.1, "change": 0.1,
                         "pct": 0.31, "date": "2026-11-06",
                         "retrieved_at": "2026-11-07T00:00:00+00:00",
                         "exchange_timezone": "America/New_York",
                         "source": "Yahoo Finance Chart API"})
        ], "最新值")
        self.assertIn("漲跌值", table)
        self.assertNotIn("漲跌點", table)

    def test_treasury_yield_table_declares_percent_and_percentage_point_units(self):
        from src.fetch_data import _treasury_yield_table

        yields = {
            key: {"yield": 4.0, "chg": 0.1, "date": "2026-11-06",
                  "retrieved_at": "2026-11-07T00:00:00+00:00",
                  "source": "U.S. Treasury FiscalData API"}
            for key in ("2Y", "10Y", "20Y", "30Y")
        }
        table = _treasury_yield_table(yields)
        self.assertIn("殖利率（%）", table)
        self.assertIn("日變化（百分點）", table)


class OptionsChainOiChangeContractTests(unittest.TestCase):
    def setUp(self):
        from src.sources.taifex import _options_chain_oi_change
        self.calculate = _options_chain_oi_change
        self.previous = [
            {"contract_month": "202611W2", "contract_expiry_date": "2026-11-11",
             "strike": 27000, "type": "call", "open_interest": 100},
            {"contract_month": "202611W2", "contract_expiry_date": "2026-11-11",
             "strike": 27000, "type": "put", "open_interest": 200},
            {"contract_month": "202611W2", "contract_expiry_date": "2026-11-11",
             "strike": 27100, "type": "call", "open_interest": 50},
        ]
        self.current = [
            {"contract_month": "202611W2", "contract_expiry_date": "2026-11-11",
             "strike": 27000, "type": "call", "open_interest": 110},
            {"contract_month": "202611W2", "contract_expiry_date": "2026-11-11",
             "strike": 27000, "type": "put", "open_interest": 180},
            {"contract_month": "202611W2", "contract_expiry_date": "2026-11-11",
             "strike": 27100, "type": "call", "open_interest": 45},
        ]

    def test_complete_aligned_chains_calculate_call_put_deltas_and_concentrations(self):
        result = self.calculate(self.current, self.previous, "202611W2")
        self.assertEqual(result["c_chg"], 5)
        self.assertEqual(result["p_chg"], -20)
        self.assertEqual(result["c_up"], {"strike": 27000, "type": "call", "d_oi": 10})
        self.assertEqual(result["c_dn"], {"strike": 27100, "type": "call", "d_oi": -5})
        self.assertEqual(result["p_dn"], {"strike": 27000, "type": "put", "d_oi": -20})

    def test_missing_current_or_previous_oi_is_unavailable_not_zero(self):
        current_missing = [dict(row) for row in self.current]
        current_missing[0]["open_interest"] = None
        previous_missing = [dict(row) for row in self.previous]
        previous_missing[1]["open_interest"] = None
        self.assertIsNone(self.calculate(current_missing, self.previous, "202611W2"))
        self.assertIsNone(self.calculate(self.current, previous_missing, "202611W2"))

    def test_missing_or_extra_contract_is_unavailable(self):
        self.assertIsNone(self.calculate(self.current[:-1], self.previous, "202611W2"))
        extra = self.current + [{
            "contract_month": "202611W2", "contract_expiry_date": "2026-11-11",
            "strike": 27200, "type": "call", "open_interest": 0,
        }]
        self.assertIsNone(self.calculate(extra, self.previous, "202611W2"))

    def test_duplicate_contract_identity_is_unavailable(self):
        duplicate = self.current + [dict(self.current[0])]
        self.assertIsNone(self.calculate(duplicate, self.previous, "202611W2"))

    def test_zero_oi_is_valid_and_other_expiries_are_excluded(self):
        current = [dict(row) for row in self.current]
        previous = [dict(row) for row in self.previous]
        current[0]["open_interest"] = 0
        previous[0]["open_interest"] = 0
        current.append({
            "contract_month": "202612W3", "contract_expiry_date": "2026-12-16",
            "strike": 27000, "type": "call", "open_interest": 999,
        })
        previous.append({
            "contract_month": "202612W3", "contract_expiry_date": "2026-12-16",
            "strike": 27000, "type": "call", "open_interest": 1,
        })
        result = self.calculate(current, previous, "202611W2")
        self.assertIsNotNone(result)
        self.assertEqual(result["c_chg"], -5)


class Top10OiSnapshotChangeContractTests(unittest.TestCase):
    def setUp(self):
        from unittest.mock import patch
        from src.sources import taifex
        self.taifex = taifex
        self.patch_snapshot = patch("src.sources.taifex.snapshot_bundle", return_value={
            "date": "2026-11-06",
            "data": {
                "top10fut": [
                    {"Date": "20261105", "SettlementMonth": "202611",
                     "Top10Buy": "1,000", "Top10Sell": "700"},
                    {"Date": "20261106", "SettlementMonth": "202611",
                     "Top10Buy": "1,200", "Top10Sell": "800"},
                    {"Date": "20261106", "SettlementMonth": "202612",
                     "Top10Buy": "9,000", "Top10Sell": "1,000"},
                ],
                "top10opt": [
                    {"Date": "20261106", "SettlementMonth": "202611",
                     "CallPut": "買權", "Top10Buy": "500", "Top10Sell": "300"},
                    {"Date": "20261106", "SettlementMonth": "202611",
                     "CallPut": "賣權", "Top10Buy": "700", "Top10Sell": "400"},
                ],
            },
        })
        self.mock_snapshot = self.patch_snapshot.start()
        self.addCleanup(self.patch_snapshot.stop)

    def test_uses_latest_record_of_requested_month_only(self):
        result = self.taifex.snap_top10_change(
            "202611", "2026-11-07", 450, cur_date="20261107")
        self.assertEqual(result["chg"], 50)
        self.assertEqual(result["prev_date"], "2026-11-06")

    def test_missing_requested_month_is_unavailable_not_another_month(self):
        result = self.taifex.snap_top10_change(
            "202610", "2026-11-07", 450, cur_date="20261107")
        self.assertIsNone(result)

    def test_missing_buy_or_sell_is_unavailable_not_zero(self):
        for missing_field in ("Top10Buy", "Top10Sell"):
            with self.subTest(field=missing_field):
                self.mock_snapshot.return_value["data"]["top10fut"][-2].pop(missing_field)
                result = self.taifex.snap_top10_change(
                    "202611", "2026-11-07", 450, cur_date="20261107")
                self.assertIsNone(result)
                self.mock_snapshot.return_value["data"]["top10fut"][-2][missing_field] = (
                    "1,200" if missing_field == "Top10Buy" else "800")

    def test_invalid_or_non_finite_snapshot_values_are_unavailable(self):
        for value in ("", "not-a-number", "NaN", "Infinity"):
            with self.subTest(value=value):
                self.mock_snapshot.return_value["data"]["top10fut"][-2]["Top10Buy"] = value
                result = self.taifex.snap_top10_change(
                    "202611", "2026-11-07", 450, cur_date="20261107")
                self.assertIsNone(result)
        self.mock_snapshot.return_value["data"]["top10fut"][-2]["Top10Buy"] = "1,200"

    def test_zero_is_valid_and_option_callput_is_filtered(self):
        row = self.mock_snapshot.return_value["data"]["top10fut"][-2]
        row["Top10Buy"] = "0"
        row["Top10Sell"] = "0"
        result = self.taifex.snap_top10_change(
            "202611", "2026-11-07", 10, cur_date="20261107")
        self.assertEqual(result["chg"], 10)

        call_result = self.taifex.snap_top10_change(
            "202611", "2026-11-07", 250, cur_date="20261107",
            dataset="top10opt", callput="買權")
        put_result = self.taifex.snap_top10_change(
            "202611", "2026-11-07", 250, cur_date="20261107",
            dataset="top10opt", callput="賣權")
        self.assertEqual(call_result["chg"], 50)
        self.assertEqual(put_result["chg"], -50)




class DataReportWriteSafetyTests(unittest.TestCase):
    def valid_report(self, t0="2026-11-06"):
        from src.fetch_data import _validate_data_report_text
        return "\n".join([
            f"# DATA_REPORT_{t0.replace('-', '')}",
            f"- T0 交易日期：`{t0}`",
            "## 一、現貨", "## 二、重要市場", "## 三、期貨",
            "## 四、選擇權", "## 五、資料來源、時間與完整性",
            "## 六、期現選方向對照", "內容" * 600,
        ])

    def test_atomic_write_replaces_only_after_validation(self):
        from src.fetch_data import _atomic_write_data_report
        with tempfile.TemporaryDirectory() as directory:
            target = Path(directory) / "DATA_REPORT_20261106.md"
            target.write_text("舊報告", encoding="utf-8")
            _atomic_write_data_report(target, self.valid_report(), "2026-11-06")
            self.assertTrue(target.read_text(encoding="utf-8").startswith("# DATA_REPORT_20261106"))
            self.assertEqual(list(Path(directory).glob("*.tmp")), [])

    def test_merge_failure_stops_before_touching_existing_report(self):  # regression
        import sys
        from unittest.mock import patch
        from src import fetch_data

        with tempfile.TemporaryDirectory() as directory:
            out_dir = Path(directory)
            target = out_dir / "DATA_REPORT_20261106.md"
            old_text = self.valid_report()
            target.write_text(old_text, encoding="utf-8")
            with patch.object(fetch_data, "OUT_DIR", out_dir), \
                 patch.object(fetch_data, "build", return_value=self.valid_report()), \
                 patch.object(fetch_data, "merge_same_t0", side_effect=ValueError("merge failed")), \
                 patch.object(sys, "argv", ["fetch_data.py", "--date", "2026-11-07", "--t0", "2026-11-06"]):
                with self.assertRaisesRegex(RuntimeError, "為保護既有報告"):
                    fetch_data.main()
            self.assertEqual(target.read_text(encoding="utf-8"), old_text)
            self.assertEqual(list(out_dir.glob(".*.tmp")), [])

    def test_invalid_report_keeps_previous_file_and_cleans_temp(self):
        from src.fetch_data import _atomic_write_data_report
        with tempfile.TemporaryDirectory() as directory:
            target = Path(directory) / "DATA_REPORT_20261106.md"
            target.write_text("舊報告", encoding="utf-8")
            with self.assertRaises(ValueError):
                _atomic_write_data_report(target, "# DATA_REPORT_20261106\n不完整", "2026-11-06")
            self.assertEqual(target.read_text(encoding="utf-8"), "舊報告")
            self.assertEqual(list(Path(directory).glob(".*.tmp")), [])

    def test_replace_failure_keeps_previous_file_and_cleans_temp(self):
        from unittest.mock import patch
        from src.fetch_data import _atomic_write_data_report
        with tempfile.TemporaryDirectory() as directory:
            target = Path(directory) / "DATA_REPORT_20261106.md"
            target.write_text("舊報告", encoding="utf-8")
            with patch("src.fetch_data.os.replace", side_effect=OSError("simulated")):
                with self.assertRaises(OSError):
                    _atomic_write_data_report(target, self.valid_report(), "2026-11-06")
            self.assertEqual(target.read_text(encoding="utf-8"), "舊報告")
            self.assertEqual(list(Path(directory).glob(".*.tmp")), [])

    def test_report_validator_rejects_wrong_t0_and_missing_sections(self):
        from src.fetch_data import _validate_data_report_text
        with self.assertRaises(ValueError):
            _validate_data_report_text(self.valid_report(), "2026-11-07")
        incomplete = self.valid_report().replace("## 四、選擇權\n", "")
        with self.assertRaises(ValueError):
            _validate_data_report_text(incomplete, "2026-11-06")

    def test_workflow_requires_success_exit_and_validated_report_path(self):
        from pathlib import Path
        workflow = (ROOT / ".github" / "workflows" / "daily_data.yml").read_text(encoding="utf-8")
        self.assertIn('if [ "$FETCH_RC" -eq 0 ]', workflow)
        self.assertIn("validate_data_report_file", workflow)
        self.assertIn("grep -F", workflow)
        self.assertIn("tail -1 || true", workflow)
        self.assertNotIn("find data_reports -name 'DATA_REPORT_*.md' -newermt", workflow)


if __name__ == "__main__":
    unittest.main()
