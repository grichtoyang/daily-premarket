"""現貨正規化：twse-proxy (主) + spot_raw/FinMind/HiStock/istock (輔) → 模板可用 dict。

輸出键：
  taiex {close, open, high, low, change, pct}  (OHLC: FinMind 主、Yahoo ^TWII 備援)
  listed_breadth / otc_breadth {up, down, flat, limit_up, limit_down}
  inst {foreign, trust, dealer, total} 單位億元
  margin {fin_yi, fin_chg_yi, s_bal, s_chg, ratio} 上市+上櫃合計；融資億元、融券張、維持率%
    (HiStock 金額口徑為主；失敗則官方逐股張數備援 → 融資改 unavailable)
  sbl {bal, sale_bal, sale_chg}；借券餘額 TWT72U，借券賣出餘額 TWT93U（上市）+ TPEx S47（上櫃）
  turnover {listed, otc, total} 單位億元
  unavailable[] / notes[] / sources{}
"""
from __future__ import annotations
from src.sources import twse, twse_proxy, spot_raw, finmind, histock, listed_maint_ratio, blave_maint_ratio

def _institutional_matches_t0(inst: dict, date8: str) -> bool:
    return (
        isinstance(inst, dict)
        and inst.get("foreign") is not None
        and twse._normalize_date8(inst.get("date")) == twse._normalize_date8(date8)
        and bool(twse._normalize_date8(date8))
    )


def _add(a, b):
    if a is None:
        return b
    if b is None:
        return a
    return a + b


def _complete_market_sum(listed, otc):
    """Return a total only when both markets are present, with explicit coverage status."""
    if listed is None and otc is None:
        return None, "unavailable"
    if listed is None or otc is None:
        return None, "partial"
    return listed + otc, "complete"


def _partial_coverage_note(field: str) -> str:
    return f"[partial] {field}僅取得單一市場；不提供不完整的合計數值"


def _optional_float(value):
    """Parse a present numeric value while preserving a legitimate zero."""
    if value is None or value == "":
        return None
    try:
        return float(str(value).replace(",", ""))
    except (TypeError, ValueError):
        return None


def _margin_market_totals(listed: dict | None, otc: dict | None) -> tuple[dict, dict]:
    """Build listed+OTC margin totals; never expose a one-sided value as a combined total."""
    fields = {
        "fin_yi": ("fin_yi", "fin_yi"),
        "fin_chg_yi": ("fin_chg_yi", "fin_chg_yi"),
        "s_bal": ("short_bal", "short_bal"),
        "s_chg": ("short_chg", "short_chg"),
    }
    totals, statuses = {}, {}
    for output, (listed_key, otc_key) in fields.items():
        value, status = _complete_market_sum(
            (listed or {}).get(listed_key), (otc or {}).get(otc_key)
        )
        totals[output], statuses[output] = value, status
    return totals, statuses


SELF_BUILT_RATIO_TIMEOUT = 10
BLAVE_RATIO_TIMEOUT = 3
BLAVE_CROSS_CHECK_MAX_DIFF_PP = 1.0


def _ratio_cross_check(self_ratio: float, blave_ratio: float) -> str:
    """PASS only when two same-T0 listed-market estimates differ by <1 percentage point."""
    diff = abs(self_ratio - blave_ratio)
    status = "PASS" if diff < BLAVE_CROSS_CHECK_MAX_DIFF_PP else "FAIL"
    return (f"Blave 同 T0 交叉驗證 {blave_ratio:.4f}%；差異 {diff:.3f} 個百分點；"
            f"門檻 <{BLAVE_CROSS_CHECK_MAX_DIFF_PP:.2f} 個百分點；{status}")


def _valid_ratio(result, t0: str) -> float | None:
    if not isinstance(result, dict) or not result.get("ok") or result.get("date") != t0:
        return None
    try:
        ratio = float(result.get("ratio"))
        coverage = float(result.get("coverage", 1.0))
    except (TypeError, ValueError):
        return None
    if not (50 < ratio < 500) or coverage < 0.999999:
        return None
    return ratio


def _get_margin_ratio(t0: str, env=None) -> dict:
    """TWSE self-built primary -> Blave cross-check/fallback -> exact-T0 manual input."""
    import os
    values = os.environ if env is None else env

    try:
        self_result = listed_maint_ratio.get(t0, timeout=SELF_BUILT_RATIO_TIMEOUT)
    except Exception as exc:
        self_result = {"ok": False, "date": None, "ratio": None,
                       "reason": f"{type(exc).__name__}: {exc}"}
    self_ratio = _valid_ratio(self_result, t0)
    self_reason = (self_result or {}).get("reason", "invalid result/date/coverage")

    try:
        blave_result = blave_maint_ratio.get(t0, timeout=BLAVE_RATIO_TIMEOUT)
    except Exception as exc:
        blave_result = {"ok": False, "date": None, "ratio": None,
                        "reason": f"{type(exc).__name__}: {exc}"}
    blave_ratio = _valid_ratio(blave_result, t0)
    blave_reason = (blave_result or {}).get("reason", "invalid result/date")

    if self_ratio is not None:
        financed_count = int(self_result.get("financed_security_count") or 0)
        stale_count = int(self_result.get("stale_price_security_count") or 0)
        price_min = self_result.get("price_date_min")
        price_max = self_result.get("price_date_max")
        if blave_ratio is not None:
            diff = abs(self_ratio - blave_ratio)
            cross_check = _ratio_cross_check(self_ratio, blave_ratio)
        else:
            cross_check = f"Blave 交叉驗證未取得（{blave_reason}）；不影響自建值"
        price_note = (
            f"{stale_count} 檔採最近有效收盤價"
            + (f"（價格日期 {price_min} 至 {price_max}）" if stale_count and price_min and price_max else "")
        )
        source = (
            f"TWSE 上市自建估算（當日暫估；資料日期：{t0}；估值 {financed_count} 檔；"
            f"{price_note}；{cross_check}）"
        )
        return {
            "ratio": round(self_ratio, 4),
            "source": source,
            "note": (
                f"上市市場維持率為當日暫估，以 TWSE 自建計算為主；{price_note}。"
                f"{cross_check}。Blave 不可用不影響 DATA_REPORT 產出。"
            ),
        }

    if blave_ratio is not None:
        return {
            "ratio": round(blave_ratio, 4),
            "source": f"Blave 上市市場融資維持率估算（當日暫估；資料日期：{t0}；自建計算備援）",
            "note": f"上市市場維持率為當日暫估；TWSE 自建計算未成功（{self_reason}）；改用 Blave 同 T0 數值（{t0}）。",
        }

    manual_date = str(values.get("MANUAL_LISTED_MARGIN_RATIO_DATE", "")).strip()
    manual_value = str(values.get("MANUAL_LISTED_MARGIN_RATIO", "")).strip()
    try:
        manual_ratio = float(manual_value)
    except (TypeError, ValueError):
        manual_ratio = None
    if manual_date == t0 and manual_ratio is not None and 50 < manual_ratio < 500:
        return {
            "ratio": round(manual_ratio, 4),
            "source": f"人工輸入（當日暫估；MANUAL_LISTED_MARGIN_RATIO；資料日期：{t0}）",
            "note": (
                f"上市市場維持率為當日暫估；TWSE 自建計算未成功（{self_reason}）；Blave 備援未取得（{blave_reason}）；"
                f"最後採用同 T0 人工輸入（資料日期：{t0}）。"
            ),
        }

    return {
        "ratio": None,
        "source": "unavailable（TWSE 自建、Blave、同 T0 人工輸入皆不可用）",
        "note": (
            f"上市融資維持率 unavailable；自建計算：{self_reason}；Blave：{blave_reason}。"
            "不影響其他融資融券欄位、DATA_REPORT、JSON 與 Dashboard 產出。"
        ),
    }

def build(t0: str) -> dict:
    date8 = t0.replace("-", "")
    roc = spot_raw.roc8(t0)
    unavailable: list[str] = []
    notes: list[str] = []
    sources: dict = {}

    # ---- twse-proxy ----
    listed_turnover_yuan = None  # 後續 FinMind/proxy/FMTQIK 依序填入
    payload = twse_proxy.fetch(date8)
    if payload is None:
        notes.append("twse-proxy 連線失敗，TAIEX 改用 MI_INDEX 備援")
        t = twse_proxy.official_ind_taiex(date8)
        sources["taiex"] = "TWSE OpenAPI MI_INDEX (備援)"
    else:
        t = twse_proxy.parse_taiex(payload)
        sources["taiex"] = "twse-proxy"
        if t["close"] is None:
            notes.append("twse-proxy taiex 缺值，改用 MI_INDEX 備援")
            t = twse_proxy.official_ind_taiex(date8)
            sources["taiex"] = "TWSE OpenAPI MI_INDEX (備援)"
    taiex = {"close": t["close"], "open": None, "high": None, "low": None,
             "change": t["change"], "pct": t["pct"]}
    # ---- 大盤 OHLC：FinMind 主、Yahoo ^TWII 備援 ----
    fm = finmind.taiex_ohlc(t0)
    if fm["ok"]:
        taiex.update({"open": fm["open"], "high": fm["high"], "low": fm["low"]})
        sources["taiex_ohlc"] = "FinMind TaiwanStockPrice TAIEX"
        if fm["money_yuan"] and listed_turnover_yuan is None:
            listed_turnover_yuan = fm["money_yuan"]
            sources["listed_turnover"] = "FinMind Trading_money"
    else:
        # 不用 Yahoo 盤中值備援：FinMind 日線收盤後才有列，缺值即 unavailable，避免盤中混充收盤
        notes.append("大盤開高低未取得 (FinMind 失敗；MI_INDEX 無此欄)")
        for k in ("open", "high", "low"):
            unavailable.append(f"taiex.{k}")
    if fm["ok"]:
        pass  # OHLC 齊全，不標 unavailable

    # ---- 上市漲跌/成交 ----
    lb = {"up": None, "down": None, "flat": None, "limit_up": None, "limit_down": None}
    if payload is not None:
        lb = twse_proxy.parse_listed_breadth(payload)
        listed_turnover_yuan = twse_proxy.parse_listed_turnover(payload)
        sources["listed_breadth"] = "twse-proxy"
        sources["listed_turnover"] = "twse-proxy market_statistics"
    if lb["up"] is None:
        raw = spot_raw.listed_breadth_raw(date8)
        if raw["up"] is not None and raw.get("date_ok"):
            lb = raw
            sources["listed_breadth"] = "TWSE OpenAPI twtazu_od (備援)"
        elif raw["up"] is not None:
            notes.append("twtazu_od 備援日期不符 (回傳舊資料)，上市漲跌標 unavailable")
        else:
            notes.append("上市漲跌家數未取得 (proxy 與 twtazu_od 皆無)")
    if listed_turnover_yuan is None:
        v = spot_raw.turnover_tw(roc)
        if v is not None:
            listed_turnover_yuan = v
            sources["listed_turnover"] = "TWSE OpenAPI FMTQIK (備援)"
    for k in ("up", "down", "flat", "limit_up", "limit_down"):
        if lb[k] is None:
            unavailable.append(f"listed_breadth.{k}")

    # ---- 上櫃漲跌/成交 ----
    ob = {"up": None, "down": None, "flat": None, "limit_up": None, "limit_down": None}
    otc_turnover_yi = None
    hl = spot_raw.tpex_highlight(roc)
    if hl["row"] is not None and hl["date_ok"]:
        row = hl["row"]
        ob = {"up": _optional_float(row.get("PriceRiseCompanyNumbers")),
              "down": _optional_float(row.get("PriceDeclineCompanyNumbers")),
              "flat": _optional_float(row.get("PriceFlatCompanyNumbers")),
              "limit_up": _optional_float(row.get("LimitUpCompanyNumbers")),
              "limit_down": _optional_float(row.get("LimitDownCompanyNumbers"))}
        otc_turnover_value = _optional_float(row.get("DailyTradingValue"))
        if otc_turnover_value is not None:
            otc_turnover_yi = otc_turnover_value / 100  # 百萬元→億元
        sources["otc"] = "TPEX OpenAPI tpex_mainborad_highlight"
    else:
        notes.append(f"上櫃 highlight 日期不符或缺值 (回傳 {(hl['row'] or {}).get('Date')}, T0={roc})")
    for k in ("up", "down", "flat", "limit_up", "limit_down"):
        if ob[k] is None:
            unavailable.append(f"otc_breadth.{k}")

    # ---- 三大法人 (億元) ----
    inst = twse.get_institutional(query_date=date8)
    if inst.get("foreign") is not None and not _institutional_matches_t0(inst, date8):
        notes.append(f"三大法人資料日期缺失或不符 T0（回傳 {inst.get('date') or 'missing'}，要求 {date8}），拒絕採用")
        inst = {}
    if inst.get("foreign") is None:
        notes.append("三大法人未取得")
        for k in ("foreign", "trust", "dealer", "total"):
            unavailable.append(f"institutional.{k}")
    else:
        sources["institutional"] = "twse-proxy /institutional" if inst.get("via") == "proxy" else "TWSE RWD BFI82U"

    # ---- 融資融券 (HiStock 金額口徑為主：融資億元/融券張) ----
    hs = histock.get(t0)
    mtw = spot_raw.margin_tw()
    mtp = spot_raw.tpex_margin(roc)
    margin = {"fin_yi": None, "fin_chg_yi": None, "s_bal": None, "s_chg": None, "ratio": None}
    L, O = hs.get("listed"), hs.get("otc")
    margin_totals, margin_status = _margin_market_totals(L, O)
    margin = {**margin_totals, "ratio": None}
    if L is not None or O is not None:
        sources["margin"] = "HiStock 上市+上櫃融資融券 (金額口徑；合計需雙市場欄位完整)"
        if L is None or O is None:
            notes.append("HiStock 僅取得單一市場；不將單邊值冒充上市+上櫃合計")
    else:
        notes.append("HiStock 未取得，融資餘額/增減標 unavailable (官方逐股加總僅有張數)")
        if mtw["sbal"] is not None or mtp["sbal"] is not None:
            margin["s_bal"] = _add(mtw["sbal"], mtp["sbal"])
            margin["s_chg"] = _add(mtw["schg"], mtp["schg"])
            notes.append("融券沿用官方逐股加總 (張)")
            sources["margin_short"] = "TWSE MI_MARGN + TPEX margin_balance (張)"
    for field, status in margin_status.items():
        if status == "partial":
            partial.append(f"margin.{field}")
            notes.append(_partial_coverage_note(f"融資融券 {field}"))
        elif status == "unavailable":
            unavailable.append(f"margin.{field}")
    # ---- 上市大盤融資維持率：TWSE 自建主引擎 → Blave 交叉驗證／備援 → 同 T0 人工最後備援 ----
    ratio_result = _get_margin_ratio(t0)
    margin["ratio"] = ratio_result["ratio"]
    sources["margin_ratio"] = ratio_result["source"]
    notes.append(ratio_result["note"])

    notes.append("上市 MI_MARGN 無日期欄，採用最新可得")
    for k in ("fin_yi", "fin_chg_yi", "s_bal", "s_chg", "ratio"):
        if margin[k] is None:
            unavailable.append(f"margin.{k}")

    # ---- 借券：借券餘額與借券賣出餘額分開取自官方歷史資料 ----
    # TWT96U 是當日可借券賣出股數，不屬於借券餘額；完全不納入此區。
    tw72 = spot_raw.twse_twt72u_sbl(roc)
    tw93 = spot_raw.twse_twt93u_sbl(roc)
    tp_sbl = spot_raw.tpex_sbl(roc)
    sbl_bal = tw72["bal"] / 1000 if tw72["bal"] is not None else None
    _tw_sale = tw93["sale_bal"] / 1000 if tw93["sale_bal"] is not None else None
    _tp_sale = tp_sbl["sale_bal"] / 1000 if tp_sbl["sale_bal"] is not None else None
    _tw_schg = tw93["sale_chg"] / 1000 if tw93["sale_chg"] is not None else None
    _tp_schg = tp_sbl["sale_chg"] / 1000 if tp_sbl["sale_chg"] is not None else None
    _sale, _sale_status = _complete_market_sum(_tw_sale, _tp_sale)
    _schg, _schg_status = _complete_market_sum(_tw_schg, _tp_schg)
    sbl = {
        "bal": sbl_bal,
        "listed_sale_bal": _tw_sale, "otc_sale_bal": _tp_sale, "sale_bal": _sale,
        "listed_sale_chg": _tw_schg, "otc_sale_chg": _tp_schg, "sale_chg": _schg,
        "status": {"sale_bal": _sale_status, "sale_chg": _schg_status},
        "publication": {"twse_twt93u": tw93.get("publication"), "tpex_s47": tp_sbl.get("publication")},
    }
    partial: list[str] = []

    def _sbl_scope(*parts):
        available = [name for name, value in parts if value is not None]
        return " + ".join(available) if available else "unavailable"
    sources["sbl_bal"] = "TWSE TWT72U（SLBNLB；上市+上櫃）" if sbl_bal is not None else "unavailable"
    sources["sbl_sale_bal_listed"] = "TWSE TWT93U（上市）" if _tw_sale is not None else "unavailable"
    sources["sbl_sale_bal_otc"] = "TPEx S47（上櫃）" if _tp_sale is not None else "unavailable"
    sources["sbl_sale_chg_listed"] = "TWSE TWT93U（上市）" if _tw_schg is not None else "unavailable"
    sources["sbl_sale_chg_otc"] = "TPEx S47（上櫃）" if _tp_schg is not None else "unavailable"
    sources["sbl_sale_bal"] = _sbl_scope(
        ("TWSE TWT93U（上市）", _tw_sale), ("TPEX S47（上櫃）", _tp_sale))
    sources["sbl_sale_chg"] = _sbl_scope(
        ("TWSE TWT93U（上市）", _tw_schg), ("TPEX S47（上櫃）", _tp_schg))
    if sbl_bal is None:
        unavailable.append("sbl.bal")
        notes.append("借券餘額未取得：TWSE TWT72U（SLBNLB）資料日期或欄位驗證失敗")
    if _tw_sale is None or _tp_sale is None:
        notes.append("借券賣出餘額市場覆蓋不完整；來源欄已明確標示實際取得市場")
    if _tw_schg is None or _tp_schg is None:
        notes.append("借券賣出增減市場覆蓋不完整；來源欄已明確標示實際取得市場")
    if _sale_status == "partial":
        partial.append("sbl.sale_bal")
        notes.append(_partial_coverage_note("借券賣出餘額"))
    elif _sale_status == "unavailable":
        unavailable.append("sbl.sale_bal")
    if _schg_status == "partial":
        partial.append("sbl.sale_chg")
        notes.append(_partial_coverage_note("借券賣出增減"))
    elif _schg_status == "unavailable":
        unavailable.append("sbl.sale_chg")

    # ---- 成交結構 (億元) ----
    listed_yi = listed_turnover_yuan / 1e8 if listed_turnover_yuan else None
    turnover = {"listed": listed_yi, "otc": otc_turnover_yi,
                "total": _add(listed_yi, otc_turnover_yi)}
    for k in ("listed", "otc", "total"):
        if turnover[k] is None:
            unavailable.append(f"turnover.{k}")

    return {"taiex": taiex, "listed_breadth": lb, "otc_breadth": ob,
            "inst": {"foreign": inst.get("foreign"), "trust": inst.get("trust"),
                     "dealer": inst.get("dealer"), "total": inst.get("total")},
            "margin": margin, "sbl": sbl, "turnover": turnover,
            "unavailable": unavailable, "partial": partial,
            "notes": notes, "sources": sources}
