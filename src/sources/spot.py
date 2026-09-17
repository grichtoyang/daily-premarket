"""現貨正規化：twse-proxy (主) + spot_raw/FinMind/HiStock/istock (輔) → 模板可用 dict。

輸出键：
  taiex {close, open, high, low, change, pct}  (OHLC: FinMind 主、Yahoo ^TWII 備援)
  listed_breadth / otc_breadth {up, down, flat, limit_up, limit_down}
  inst {foreign, trust, dealer, total} 單位億元
  margin {fin_yi, fin_chg_yi, s_bal, s_chg, ratio} 上市+上櫃合計；融資億元、融券張、維持率%
    (HiStock 金額口徑為主；失敗則官方逐股張數備援 → 融資改 unavailable)
  sbl {bal, sale_bal, sale_chg} bal 股數；sale 上櫃值+上市缺註記
  turnover {listed, otc, total} 單位億元
  unavailable[] / notes[] / sources{}
"""
from __future__ import annotations
from src.sources import twse, twse_proxy, spot_raw, finmind, histock, maint_ratio

def _add(a, b):
    if a is None:
        return b
    if b is None:
        return a
    return a + b

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
        ob = {"up": float(row["PriceRiseCompanyNumbers"]) if row.get("PriceRiseCompanyNumbers") else None,
              "down": float(row["PriceDeclineCompanyNumbers"]) if row.get("PriceDeclineCompanyNumbers") else None,
              "flat": float(row["PriceFlatCompanyNumbers"]) if row.get("PriceFlatCompanyNumbers") else None,
              "limit_up": float(row["LimitUpCompanyNumbers"]) if row.get("LimitUpCompanyNumbers") else None,
              "limit_down": float(row["LimitDownCompanyNumbers"]) if row.get("LimitDownCompanyNumbers") else None}
        if row.get("DailyTradingValue"):
            otc_turnover_yi = float(str(row["DailyTradingValue"]).replace(",", "")) / 100  # 百萬元→億元
        sources["otc"] = "TPEX OpenAPI tpex_mainborad_highlight"
    else:
        notes.append(f"上櫃 highlight 日期不符或缺值 (回傳 {(hl['row'] or {}).get('Date')}, T0={roc})")
    for k in ("up", "down", "flat", "limit_up", "limit_down"):
        if ob[k] is None:
            unavailable.append(f"otc_breadth.{k}")

    # ---- 三大法人 (億元) ----
    inst = twse.get_institutional(query_date=date8)
    if inst.get("foreign") is None:
        notes.append("三大法人未取得")
        for k in ("foreign", "trust", "dealer", "total"):
            unavailable.append(f"institutional.{k}")
    else:
        sources["institutional"] = "twse-proxy /institutional" if inst.get("via") == "proxy" else "TWSE RWD BFI82U"
        if inst.get("date") and inst["date"] != date8:
            notes.append(f"三大法人回傳日期 {inst['date']} (T0 {date8})，採用最新可得")

    # ---- 融資融券 (HiStock 金額口徑為主：融資億元/融券張) ----
    hs = histock.get(t0)
    mtw = spot_raw.margin_tw()
    mtp = spot_raw.tpex_margin(roc)
    margin = {"fin_yi": None, "fin_chg_yi": None, "s_bal": None, "s_chg": None, "ratio": None}
    if hs["listed"] is not None and hs["otc"] is not None:
        L, O = hs["listed"], hs["otc"]
        margin = {"fin_yi": (L["fin_yi"] or 0) + (O["fin_yi"] or 0),
                  "fin_chg_yi": _add(L["fin_chg_yi"], O["fin_chg_yi"]),
                  "s_bal": _add(L["short_bal"], O["short_bal"]),
                  "s_chg": _add(L["short_chg"], O["short_chg"]), "ratio": None}
        sources["margin"] = "HiStock 上市+上櫃融資融券 (金額口徑)"
    elif hs["listed"] is not None or hs["otc"] is not None:
        one = hs["listed"] or hs["otc"]
        margin = {"fin_yi": one["fin_yi"], "fin_chg_yi": one["fin_chg_yi"],
                  "s_bal": one["short_bal"], "s_chg": one["short_chg"], "ratio": None}
        sources["margin"] = "HiStock (僅上市或上櫃)"
        notes.append("HiStock 僅取上市/上櫃單邊，另一邊日期不符")
    else:
        notes.append("HiStock 未取得，融資餘額/增減標 unavailable (官方逐股加總僅有張數)")
        if mtw["sbal"] is not None or mtp["sbal"] is not None:
            margin["s_bal"] = _add(mtw["sbal"], mtp["sbal"])
            margin["s_chg"] = _add(mtw["schg"], mtp["schg"])
            notes.append("融券沿用官方逐股加總 (張)")
            sources["margin_short"] = "TWSE MI_MARGN + TPEX margin_balance (張)"
    mr = maint_ratio.get(t0)
    if mr["ok"]:
        margin["ratio"] = mr["ratio"]
        sources["margin_ratio"] = "istock.tw 大盤融資維持率 (民間估算；官方無每日序列)"
    else:
        notes.append("融資維持率未取得 (istock 失敗；官方無每日序列)")
    notes.append("上市 MI_MARGN / TWT96U 無日期欄，採用最新可得")
    for k in ("fin_yi", "fin_chg_yi", "s_bal", "s_chg", "ratio"):
        if margin[k] is None:
            unavailable.append(f"margin.{k}")

    # ---- 借券 (TWT96U/TPEX 原值為股數 → 張，1張=1000股) ----
    stw = spot_raw.sbl_tw()
    stp = spot_raw.tpex_sbl(roc)
    sbl_bal = _add(_add(stw["tw"], stw["otc"]), stp["bal"])
    if sbl_bal is not None:
        sbl_bal /= 1000
    _sale = stp["sale_bal"] / 1000 if stp["sale_bal"] is not None else None
    _schg = stp["sale_chg"] / 1000 if stp["sale_chg"] is not None else None
    sbl = {"bal": sbl_bal, "sale_bal": _sale, "sale_chg": _schg}
    if sbl_bal is None:
        notes.append("借券餘額未取得")
        unavailable.append("sbl.bal")
    if sbl["sale_bal"] is None:
        unavailable.append("sbl.sale_bal")
    if sbl["sale_chg"] is None:
        unavailable.append("sbl.sale_chg")
    if stp["sale_bal"] is not None:
        notes.append("借券賣出餘額/增減為上櫃值 (上市 TWT93U 無機器接口)")
    sources["sbl"] = "TWSE TWT96U + TPEX margin_sbl"

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
            "unavailable": unavailable, "notes": notes, "sources": sources}
