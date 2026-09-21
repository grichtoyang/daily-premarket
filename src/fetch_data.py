"""資料層主程式 V2：對齊 DATA_REPORT_TEMPLATE.md (新規範)。

用法：
    python src/fetch_data.py --date 2026-09-16 --t0 2026-09-15
    --date  報告日期 (預設今天 Asia/Taipei)
    --t0    T0 交易日期 (預設自動取 <= date 的最近平日)

產出 data_reports/DATA_REPORT_yyyymmdd.md (yyyymmdd 取自 T0)。
缺值一律 `unavailable`，不推估。
"""
from __future__ import annotations
import argparse
import sys
from datetime import date, datetime
from pathlib import Path
from zoneinfo import ZoneInfo

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from src.sources import spot, us_market, treasury, taifex, taifex_official, news, stockintelli  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
OUT_DIR = ROOT / "data_reports"
TAIPEI = ZoneInfo("Asia/Taipei")
MISSING = "unavailable"

def _f2(v) -> str:
    return f"{float(v):,.2f}" if v is not None else MISSING

def _f1s(v) -> str:  # signed 1位 (買賣超用)
    if v is None:
        return MISSING
    f = float(v)
    return f"{f:+,.1f}"

def _f1u(v) -> str:  # unsigned 1位 (成交金額用)
    return f"{float(v):,.1f}" if v is not None else MISSING

def _fi(v) -> str:
    if v is None:
        return MISSING
    try:
        return f"{int(round(float(v))):,}"
    except (ValueError, TypeError):
        return MISSING

def _f2s(v) -> str:  # signed 口數/價差 (整數無小數，其餘2位)
    if v is None:
        return MISSING
    try:
        f = float(v)
        return f"{f:+,.0f}" if f == int(f) else f"{f:+,.2f}"
    except (ValueError, TypeError):
        return MISSING

def _add3(a, b, c):
    r = _add2(a, b)
    return _add2(r, c)

def _add2(a, b):
    if a is None:
        return b
    if b is None:
        return a
    return a + b
    return f"{float(v):+.2f}" if v is not None else MISSING

def _diff2(a, b):
    return a - b if a is not None and b is not None else None

def _pct(v) -> str:
    return f"{float(v):+.2f}" if v is not None else MISSING

def _tbl(rows: list[tuple], headers: tuple) -> str:
    lines = ["| " + " | ".join(headers) + " |", "|" + "|".join(["---"] * len(headers)) + "|"]
    for r in rows:
        lines.append("| " + " | ".join(str(x) for x in r) + " |")
    return "\n".join(lines)

def last_weekday(d: date) -> date:
    """相容舊介面：T0 取今天之前的最近平日。新邏輯請用 src.t0.resolve。"""
    from datetime import timedelta
    d -= timedelta(days=1)
    while d.weekday() >= 5:
        d -= timedelta(days=1)
    return d

def build(report_date: str, t0: str) -> str:
    now = datetime.now(TAIPEI).strftime("%Y-%m-%d %H:%M:%S")
    s = spot.build(t0)
    tx, lb, ob = s["taiex"], s["listed_breadth"], s["otc_breadth"]
    inst, mg, sb, to = s["inst"], s["margin"], s["sbl"], s["turnover"]
    _src = s["sources"]
    SRC_TX = _src.get("taiex", "twse-proxy")
    SRC_OHLC = _src.get("taiex_ohlc", "FinMind")
    SRC_LB = _src.get("listed_breadth", "twse-proxy")
    SRC_LTO = _src.get("listed_turnover", "twse-proxy")
    SRC_OTC = _src.get("otc", "TPEX")
    SRC_INST = _src.get("institutional", "TWSE BFI82U")
    SRC_MG = _src.get("margin", "HiStock")
    SRC_MR = _src.get("margin_ratio", "istock.tw")
    SRC_SBL = _src.get("sbl", "TWSE/TPEX")

    L: list[str] = []
    A = L.append
    A(f"# DATA_REPORT_{t0.replace('-', '')}")
    A("")
    A(f"- 報告日期：`{report_date}`")
    A(f"- T0 交易日期：`{t0}`")
    A(f"- 資料產出時間：`{now}`")
    A("- 時區：`Asia/Taipei`")
    A("")
    A("---")
    A("")
    A("## 一、現貨")
    A("")
    A("### 1. 台股大盤行情")
    A("")
    A("**資料來源：** `Cloudflare Worker：twse-proxy` (備援 `TWSE OpenAPI MI_INDEX`)")
    A("")
    A(_tbl([("加權指數", _f2(tx["close"]), "點", SRC_TX), ("開盤", _f2(tx["open"]), "點", SRC_OHLC),
            ("最高", _f2(tx["high"]), "點", SRC_OHLC), ("最低", _f2(tx["low"]), "點", SRC_OHLC),
            ("收盤", _f2(tx["close"]), "點", SRC_TX),
            ("漲跌點數", _f2(tx["change"]), "點", SRC_TX), ("漲跌幅", _pct(tx["pct"]), "%", SRC_TX),
            ("成交金額", _f1u(to["listed"]), "億元", SRC_LTO)], ("項目", "數值", "單位", "資料來源")))
    A("")
    A("### 2. 市場漲跌家數")
    A("")
    A("#### 2.1 上市公司")
    A("")
    A("**資料來源：** `Cloudflare Worker：twse-proxy` (備援 `TWSE OpenAPI twtazu_od`)")
    A("")
    A(_tbl([("上漲家數", _fi(lb["up"]), SRC_LB), ("下跌家數", _fi(lb["down"]), SRC_LB),
            ("平盤家數", _fi(lb["flat"]), SRC_LB),
            ("漲停家數", _fi(lb["limit_up"]), SRC_LB), ("跌停家數", _fi(lb["limit_down"]), SRC_LB)],
           ("項目", "家數", "資料來源")))
    A("")
    A("#### 2.2 上櫃公司")
    A("")
    A("**資料來源：** `TPEX OpenAPI tpex_mainborad_highlight`")
    A("")
    A(_tbl([("上漲家數", _fi(ob["up"]), SRC_OTC), ("下跌家數", _fi(ob["down"]), SRC_OTC),
            ("平盤家數", _fi(ob["flat"]), SRC_OTC),
            ("漲停家數", _fi(ob["limit_up"]), SRC_OTC), ("跌停家數", _fi(ob["limit_down"]), SRC_OTC)],
           ("項目", "家數", "資料來源")))
    A("")
    A("### 3. 三大法人現貨買賣超")
    A("")
    A("**資料來源：** `TWSE RWD BFI82U`")
    A("")
    A(_tbl([("外資", _f1s(inst["foreign"]), "億元", SRC_INST), ("投信", _f1s(inst["trust"]), "億元", SRC_INST),
            ("自營商", _f1s(inst["dealer"]), "億元", SRC_INST),
            ("三大法人合計", _f1s(inst["total"]), "億元", SRC_INST)],
           ("法人別", "買賣超金額", "單位", "資料來源")))
    A("")
    A("### 4. 融資融券")
    A("")
    A("**資料來源：** 上市+上櫃 `HiStock` (金額口徑)；維持率 `istock.tw`；備援官方逐股加總")
    A("")
    A(_tbl([("融資餘額", _f1u(mg["fin_yi"]), "億元", SRC_MG),
            ("融資增減", _f1s(mg["fin_chg_yi"]), "億元", SRC_MG),
            ("融券餘額", _fi(mg["s_bal"]), "張", SRC_MG), ("融券增減", _fi(mg["s_chg"]), "張", SRC_MG),
            ("融資維持率", _f2(mg["ratio"]), "%", SRC_MR)], ("項目", "數值", "單位", "資料來源")))
    A("")
    A("### 5. 借券資料")
    A("")
    A("**資料來源：** 上市 `TWSE OpenAPI TWT96U` (可借餘額)、上櫃 `TPEX OpenAPI tpex_margin_sbl`")
    A("")
    A(_tbl([("借券餘額", _fi(sb["bal"]), "張", SRC_SBL),
            ("借券賣出餘額", _fi(sb["sale_bal"]), "張", SRC_SBL),
            ("借券賣出增減", _fi(sb["sale_chg"]), "張", SRC_SBL)], ("項目", "數值", "單位", "資料來源")))
    A("")
    A("### 6. 市場成交結構")
    A("")
    A("**資料來源：** 上市 `twse-proxy market_statistics`、上櫃 `TPEX OpenAPI tpex_mainborad_highlight`")
    A("")
    A(_tbl([("上市成交金額", _f1u(to["listed"]), "億元", SRC_LTO),
            ("上櫃成交金額", _f1u(to["otc"]), "億元", SRC_OTC),
            ("上市櫃成交金額合計", _f1u(to["total"]), "億元", f"{SRC_LTO}+{SRC_OTC}")],
           ("項目", "成交金額", "單位", "資料來源")))
    A("")
    A("## 二、重要市場")
    A("")
    mk = us_market.get_all()
    titles = {"美股指數": ("美股指數", "收盤／最新值"), "亞洲主要指數": ("亞洲主要指數", "收盤／最新值"),
              "美股指數期貨": ("美股指數期貨", "最新值"), "主要匯率": ("主要匯率", "最新值"),
              "台灣相關ADR": ("台灣相關ADR", "收盤／最新值"), "原油黃金Bitcoin": ("原油黃金Bitcoin", "收盤／最新值")}
    order = ["美股指數", "亞洲主要指數", "美股指數期貨"]
    num = 0
    for group in order:
        num += 1
        title, col = titles[group]
        rows = mk[group]
        A(f"### {num}. {title}")
        A("")
        A("**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)")
        A("")
        A(_tbl([(n, q["symbol"], _f2(q["price"]), _f2(q["change"]), _pct(q["pct"]), "Yahoo Finance Chart API") for n, q in rows],
               ("項目", "Yahoo Finance 代號", col, "漲跌點", "漲跌幅", "資料來源")))
        A("")
    y = treasury.get_yields()
    num += 1
    A(f"### {num}. 美國國債殖利率")
    A("")
    A("**資料來源：** `U.S. Treasury Fiscal Data API` (失敗時備援 Treasury yield.xml 與 `Yahoo Finance`)")
    A("")
    A(_tbl([("美國 2 年期殖利率", "2 Yr", _f2(y["2Y"]["yield"]), _f2(y["2Y"]["chg"]), y["2Y"]["source"]),
            ("美國 10 年期殖利率", "10 Yr", _f2(y["10Y"]["yield"]), _f2(y["10Y"]["chg"]), y["10Y"]["source"]),
            ("美國 30 年期殖利率", "30 Yr", _f2(y["30Y"]["yield"]), _f2(y["30Y"]["chg"]), y["30Y"]["source"])],
           ("項目", "API 資料欄位／識別", "殖利率", "日變化", "資料來源")))
    A("")
    for group in ["主要匯率", "台灣相關ADR", "原油黃金Bitcoin"]:
        num += 1
        title, col = titles[group]
        rows = mk[group]
        A(f"### {num}. {title}")
        A("")
        A("**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)")
        A("")
        A(_tbl([(n, q["symbol"], _f2(q["price"]), _f2(q["change"]), _pct(q["pct"]), "Yahoo Finance Chart API") for n, q in rows],
               ("項目", "Yahoo Finance 代號", col, "漲跌點", "漲跌幅", "資料來源")))
        A("")
    num += 1
    A(f"### {num}. 重大經濟數據、央行事件與重大市場新聞")
    A("")
    A("**資料來源：** 台股 `tw.stock.yahoo.com` (含內文摘要)；國際 `Fed 公告 RSS`＋`CNBC`＋`MarketWatch` (標題、來源、時間與連結)")
    A("")
    _nw = news.get()
    if _nw["items"]:
        for _i, it in enumerate(_nw["items"], 1):
            A(f"- 事件{_i}：{it['title']}")
            A(f"  - 來源：{it['source']}；發布時間：{it['pub']}；台北時間：{it['taipei']}")
            A(f"  - 摘要：{it.get('summary', MISSING)}")
            A(f"  - 原文連結：{it['link']}")
    else:
        A(_tbl([("TBD", "TBD", "TBD", "TBD", "TBD", "TBD")],
               ("事件／新聞", "來源", "發布時間", "台北時間", "摘要", "原文連結")))
    A("")
    _news_note = _nw["note"]
    A("")
    num += 1
    A(f"### {num}. 產業資金流向 (股市智投)")
    A("")
    A("**資料來源：** `StockIntelli API` — https://www.stockintelli.com/market/industry-flow")
    A("")
    _si = stockintelli.industry_flow(limit=5)
    if _si["ok"]:
        _si_sum = _si.get("summary", {})
        if _si_sum:
            A(f"- 交易日：{_si_sum.get('trade_date', MISSING)}")
            A(f"- 總流入：{_si_sum.get('total_inflow', 0) / 1e8:.1f} 億；總流出：{_si_sum.get('total_outflow', 0) / 1e8:.1f} 億；淨流入：{_si_sum.get('net_flow', 0) / 1e8:.1f} 億")
        for _direction, _label in [("inflow", "資金流入前5"), ("outflow", "資金流出前5")]:
            _items = _si.get(_direction, [])
            if _items:
                A(f"- **{_label}：**")
                for _s in _items[:5]:
                    _name = _s.get("security_name", "?")
                    _code = _s.get("stock_code", "?")
                    _net = _s.get("net_flow_value", 0)
                    _chg = _s.get("price_change_percent", 0)
                    _sign = "+" if _net > 0 else ""
                    A(f"  - {_code} {_name}：{_sign}{_net / 1e8:.1f}億 ({_chg:+.2f}%)")
    else:
        A("- unavailable (StockIntelli API 速率限制或回應異常)")
    A("")
    A("## 三、期貨")
    A("")
    A("**資料來源：**")
    A("1. Cloudflare Workers：TAIFEX Proxy — https://taifex.grichtoyang.workers.dev/")
    A("2. TAIFEX Open API — https://openapi.taifex.com.tw/")
    A("")
    fx = taifex.build(t0, taiex_close=tx["close"])
    d, n = fx["day"], fx["night"]
    SRC_FX = "TAIFEX Proxy"
    SRC_FX_OFF = "TAIFEX OpenAPI"
    _sg = fx.get("snapchg") or {}
    _sdate = _sg.get("date")
    SRC_SNAP = f"TAIFEX Proxy snapshots ({_sdate})" if _sdate else "端點未提供"
    A(f"近月契約月份：{d['month'] or MISSING} (日盤成交量最大者)；交易日期：{t0}")
    A("")
    A("### 1．台指期近月日盤行情")
    A("")
    A(_tbl([("開盤價", _fi(d["open"]), SRC_FX), ("最高價", _fi(d["high"]), SRC_FX),
            ("最低價", _fi(d["low"]), SRC_FX),
            ("收盤價", _fi(d["close"]), SRC_FX), ("漲跌點數", _f2s(d["change"]), SRC_FX),
            ("漲跌幅", _pct(d["pct"]), SRC_FX),
            ("成交量", _fi(d["vol"]), SRC_FX),
            ("日盤高點及低點", f"{_fi(d['high'])} / {_fi(d['low'])}", SRC_FX)],
           ("項目", "數值", "資料來源")))
    A("")
    A("### 2．台指期近月夜盤行情")
    A("")
    _nvia = n.get("via", "proxy") if n.get("close") is not None else "端點未提供"
    _nmiss = "端點未提供"
    A(_tbl([("開盤價", _fi(n["open"]), _nvia if n["open"] is not None else _nmiss),
            ("最高價", _fi(n["high"]), _nvia if n["high"] is not None else _nmiss),
            ("最低價", _fi(n["low"]), _nvia if n["low"] is not None else _nmiss),
            ("收盤價", _fi(n["close"]), _nvia if n["close"] is not None else _nmiss),
            ("漲跌點數", _f2s(n["change"]), _nvia if n["change"] is not None else _nmiss),
            ("漲跌幅", _pct(n["pct"]), _nvia if n["pct"] is not None else _nmiss),
            ("成交量", _fi(n["vol"]), SRC_FX), ("夜盤高點及低點", f"{_fi(n['high'])} / {_fi(n['low'])}", _nvia if n["high"] is not None else _nmiss),
            ("結算價", _fi(n["settle"]), SRC_FX), ("未平倉量", _fi(n["oi"]), SRC_FX)],
           ("項目", "數值", "資料來源")))
    A("")
    A("### 3．法人台指期多空未平倉部位")
    A("")
    _oi = fx["fut_oi"]
    A(_tbl([("外資多方 OI", _fi(_oi["foreign"]["long"]), SRC_FX),
            ("外資空方 OI", _fi(_oi["foreign"]["short"]), SRC_FX),
            ("外資多空淨 OI", _f2s(_oi["foreign"]["net"]), SRC_FX),
            ("投信多方 OI", _fi(_oi["investment_trust"]["long"]), SRC_FX),
            ("投信空方 OI", _fi(_oi["investment_trust"]["short"]), SRC_FX),
            ("投信多空淨 OI", _f2s(_oi["investment_trust"]["net"]), SRC_FX),
            ("自營商多方 OI", _fi(_oi["dealer"]["long"]), SRC_FX),
            ("自營商空方 OI", _fi(_oi["dealer"]["short"]), SRC_FX),
            ("自營商多空淨 OI", _f2s(_oi["dealer"]["net"]), SRC_FX),
            ("三大法人合計多方 OI", _fi(_oi["total"]["long"]), SRC_FX),
            ("三大法人合計空方 OI", _fi(_oi["total"]["short"]), SRC_FX),
            ("三大法人合計多空淨 OI", _f2s(_oi["total"]["net"]), SRC_FX),
            ("外資多空淨 OI 變化", _f2s(_oi["foreign"]["d_net"]), SRC_FX),
            ("投信多空淨 OI 變化", _f2s(_oi["investment_trust"]["d_net"]), SRC_FX),
            ("自營商多空淨 OI 變化", _f2s(_oi["dealer"]["d_net"]), SRC_FX)],
           ("項目", "口數", "資料來源")))
    A("")
    A("### 4．前十大交易人多空未平倉部位")
    A("")
    A("**資料來源：** `TAIFEX OpenAPI OpenInterestOfLargeTradersFutures` (官方資料落後約一日，標示實際日期)")
    A("")
    _t10 = taifex_official.top10_fut(d["month"] or "", t0)
    _t10_src = "TAIFEX Proxy" if _t10.get("via") == "proxy" else SRC_FX_OFF
    _t10chg = taifex.snap_top10_change(d["month"] or "", t0, _t10.get("net"))
    A(_tbl([("前十大交易人多方 OI", _fi(_t10["buy"]), _t10_src),
            ("前十大交易人空方 OI", _fi(_t10["sell"]), _t10_src),
            ("前十大交易人多空淨 OI", _f2s(_t10["net"]), _t10_src),
            ("多空淨 OI 變化" + (f" ({_t10chg['date']}→{t0})" if _t10chg else ""),
             _f2s(_t10chg["chg"]) if _t10chg else MISSING,
             SRC_SNAP if _t10chg else "端點未提供")],
           ("項目", "口數", "資料來源")))
    A(f"- 資料日期：{_t10['date'] or MISSING} (TypeOfTraders=0 全部交易人；契約月份 {_t10['month'] or MISSING})")
    A("")
    A("### 5．日盤、夜盤法人交易資料")
    A("")
    _tr = fx["fut_trade"]
    def _t(sess, k):
        v = _tr[(sess, k)]
        return v
    A(_tbl([("外資日盤多單交易量", _fi(_t("day", "foreign")["long"]), SRC_FX),
            ("外資日盤空單交易量", _fi(_t("day", "foreign")["short"]), SRC_FX),
            ("外資日盤多空淨交易量", _f2s(_t("day", "foreign")["net"]), SRC_FX),
            ("外資夜盤多單交易量", _fi(_t("night", "foreign")["long"]), SRC_FX),
            ("外資夜盤空單交易量", _fi(_t("night", "foreign")["short"]), SRC_FX),
            ("外資夜盤多空淨交易量", _f2s(_t("night", "foreign")["net"]), SRC_FX),
            ("外資日盤／夜盤交易量變化", _f2s(_diff2(_t("day", "foreign")["net"], _t("night", "foreign")["net"])), SRC_FX),
            ("投信日盤多空淨交易量", _f2s(_t("day", "investment_trust")["net"]), SRC_FX),
            ("投信夜盤多空淨交易量", _f2s(_t("night", "investment_trust")["net"]), SRC_FX),
            ("投信日盤／夜盤交易量變化", _f2s(_diff2(_t("day", "investment_trust")["net"], _t("night", "investment_trust")["net"])), SRC_FX),
            ("自營商日盤多空淨交易量", _f2s(_t("day", "dealer")["net"]), SRC_FX),
            ("自營商夜盤多空淨交易量", _f2s(_t("night", "dealer")["net"]), SRC_FX),
            ("自營商日盤／夜盤交易量變化", _f2s(_diff2(_t("day", "dealer")["net"], _t("night", "dealer")["net"])), SRC_FX),
            ("三大法人日盤多空淨交易量", _f2s(_add3(_t("day", "foreign")["net"], _t("day", "investment_trust")["net"], _t("day", "dealer")["net"])), SRC_FX),
            ("三大法人夜盤多空淨交易量", _f2s(_add3(_t("night", "foreign")["net"], _t("night", "investment_trust")["net"], _t("night", "dealer")["net"])), SRC_FX),
            ("法人日盤交易金額淨額 (億元)", _f1s(_add3(_t("day", "foreign")["net_amt_yi"], _t("day", "investment_trust")["net_amt_yi"], _t("day", "dealer")["net_amt_yi"])), SRC_FX),
            ("法人夜盤交易金額淨額 (億元)", _f1s(_add3(_t("night", "foreign")["net_amt_yi"], _t("night", "investment_trust")["net_amt_yi"], _t("night", "dealer")["net_amt_yi"])), SRC_FX)],
           ("項目", "口數", "資料來源")))
    A("")
    A("### 6．期貨與現貨關係")
    A("")
    _night_vs_day = _diff2(n["close"], d["close"])
    A(_tbl([("台指期近月價格", _fi(d["close"]), SRC_FX),
            ("加權指數價格", _f2(tx["close"]), SRC_TX),
            ("台指期與加權指數價差", _f2s(fx["basis"]), f"{SRC_FX}+{SRC_TX}"),
            ("價差百分比", _pct(fx["basis_pct"]), f"{SRC_FX}+{SRC_TX}"),
            ("日盤基差", _f2s(fx["basis"]), f"{SRC_FX}+{SRC_TX}"),
            ("夜盤價格相對日盤收盤的變化", _f2s(_night_vs_day),
             _nvia if _night_vs_day is not None else "端點未提供")],
           ("項目", "數值", "資料來源")))
    A("")
    A("### 7．日盤、夜盤與籌碼變化對照")
    A("")
    A("#### 7.1 日夜盤價格與成交量對照 (變化 = 日盤 - 夜盤)")
    A("")
    A(_tbl([("收盤價", _fi(d["close"]), _fi(n["close"]), _f2s(_diff2(d["close"], n["close"])), SRC_FX),
            ("成交量", _fi(d["vol_day"]), _fi(n["vol"]), _f2s(_diff2(d["vol_day"], n["vol"])), SRC_FX)],
           ("項目", "日盤", "夜盤", "變化 (日-夜)", "資料來源")))
    A(f"- 台指期總 OI 前日變化：{_f2s(fx['oi_chg'])}（來源：{SRC_FX}）")
    A("")
    A("")
    A("#### 7.2 法人籌碼日夜盤對照 (淨變化 = 日盤淨 - 夜盤淨；OI 為日盤收盤後總量，前日變化另列)")
    A("")
    _rows72 = [(("", "**日盤多單**", "**日盤空單**", "**日盤淨**", "**夜盤多單**", "**夜盤空單**",
                 "**夜盤淨**", "**淨變化 (日-夜)**", "**OI多方**", "**OI空方**", "**OI淨**",
                 "**OI前日變化**", ""))]
    for _k, _zh in (("foreign", "外資"), ("investment_trust", "投信"), ("dealer", "自營商")):
        _rows72.append((_zh, _fi(_t("day", _k)["long"]), _fi(_t("day", _k)["short"]),
                        _f2s(_t("day", _k)["net"]), _fi(_t("night", _k)["long"]),
                        _fi(_t("night", _k)["short"]), _f2s(_t("night", _k)["net"]),
                        _f2s(_diff2(_t("day", _k)["net"], _t("night", _k)["net"])),
                        _fi(_oi[_k]["long"]), _fi(_oi[_k]["short"]), _f2s(_oi[_k]["net"]),
                        _f2s(_oi[_k]["d_net"]), SRC_FX))
    _rows72.append(("三大法人合計", _fi(_add3(_t("day", "foreign")["long"], _t("day", "investment_trust")["long"], _t("day", "dealer")["long"])),
                    _fi(_add3(_t("day", "foreign")["short"], _t("day", "investment_trust")["short"], _t("day", "dealer")["short"])),
                    _f2s(_add3(_t("day", "foreign")["net"], _t("day", "investment_trust")["net"], _t("day", "dealer")["net"])),
                    _fi(_add3(_t("night", "foreign")["long"], _t("night", "investment_trust")["long"], _t("night", "dealer")["long"])),
                    _fi(_add3(_t("night", "foreign")["short"], _t("night", "investment_trust")["short"], _t("night", "dealer")["short"])),
                    _f2s(_add3(_t("night", "foreign")["net"], _t("night", "investment_trust")["net"], _t("night", "dealer")["net"])),
                    _f2s(_diff2(_add3(_t("day", "foreign")["net"], _t("day", "investment_trust")["net"], _t("day", "dealer")["net"]),
                                _add3(_t("night", "foreign")["net"], _t("night", "investment_trust")["net"], _t("night", "dealer")["net"]))),
                    _fi(_oi["total"]["long"]), _fi(_oi["total"]["short"]), _f2s(_oi["total"]["net"]),
                    _f2s(_oi["total"]["d_net"]), SRC_FX))
    A(_tbl(_rows72, ("法人", "交易量", "", "", "", "", "", "", "未平倉量", "", "", "", "資料來源")))
    A("")
    A("#### 7.3 前十大交易人日夜盤對照 (OI 無日夜拆分，列收盤後總量)")
    A("")
    A(_tbl([("前十大交易人多方 OI", _fi(_t10["buy"]), _t10_src),
            ("前十大交易人空方 OI", _fi(_t10["sell"]), _t10_src),
            ("前十大交易人多空淨 OI", _f2s(_t10["net"]), _t10_src),
            ("前十大交易人多空淨 OI 變化", MISSING, "端點未提供")],
           ("項目", "口數", "資料來源")))
    A("")
    A("#### 7.4 夜盤劇本分類 (規則對應：夜盤漲跌 × 外資夜盤偏多空)")
    A("")
    _nv, _dv = n["vol"], d["vol_day"]
    _nratio = (_nv / (_nv + _dv)) if _nv is not None and _dv is not None and (_nv + _dv) else None
    _nchg = n["change"] if n["change"] is not None else _night_vs_day
    _fgn = _tr[("night", "foreign")]["net"]
    _play, _cond, _feat = MISSING, MISSING, MISSING
    if _nchg is not None and _fgn is not None and _nchg != 0 and _fgn != 0:
        _up, _bull = _nchg > 0, _fgn > 0
        _play = ("劇本一" if _up and _bull else "劇本二" if _up else "劇本三" if not _bull else "劇本四")
        _cond = f"夜盤{'上漲' if _up else '下跌'}＋外資偏{'多' if _bull else '空'}"
        _feat = {"劇本一": "開高、續漲機率高", "劇本二": "先漲、小心開高走低",
                 "劇本三": "開低、續跌機率高", "劇本四": "先跌、開低反彈"}[_play]
    A(_tbl([("夜盤成交量占比 (夜盤量／(夜盤量＋日盤量))",
             f"{_nratio * 100:.2f}%" if _nratio is not None else MISSING, SRC_FX),
            ("夜盤漲跌點數", _f2s(_nchg), SRC_FX if n["change"] is not None else f"{SRC_FX}+{SRC_TX}"),
            ("外資夜盤多空淨交易量", _f2s(_fgn), SRC_FX),
            ("劇本分類", _play, "規則對應"),
            ("劇本條件", _cond, "規則對應"),
            ("劇本特徵", _feat, "規則對應")],
           ("項目", "數值", "資料來源")))
    A("")
    A("## 四、選擇權")
    A("")
    A("**資料來源：** 主要 TAIFEX 經 Cloudflare Worker Proxy；時區 `Asia/Taipei`")
    A("")
    _ot, _oc, _op, _w = fx["opt_tot"], fx["opt_conc"], fx["opt_pos"], fx["walls"]
    _od = fx.get("opt_dist") or {"call": [], "put": []}
    A("### 1．選擇權交易日期、到期日與資料時間")
    A("")
    A(_tbl([("交易日期", fx['trade_date'], SRC_FX),
            ("到期月份／到期日", _ot['expiry'] or MISSING, SRC_FX),
            ("資料更新時間", now, "本機"),
            ("日盤／夜盤標記", "日盤收盤後資料", SRC_FX)],
           ("項目", "數值", "資料來源")))
    A("")
    A("### 2．Call 總成交量、OI、OI 增減")
    A("")
    _ch = (_sg.get("chain") or {})
    A(_tbl([("Call 總成交量", _fi(_ot['c_vol']), SRC_FX),
            ("Call 總未平倉量 OI", _fi(_ot['c_oi']), SRC_FX),
            ("Call OI 增減" + (f" ({_sdate}→{t0})" if _ch.get("c_chg") is not None else ""),
             _f2s(_ch.get("c_chg")), SRC_SNAP if _ch.get("c_chg") is not None else "端點未提供")],
           ("項目", "數值", "資料來源")))
    A("")
    A("### 3．Put 總成交量、OI、OI 增減")
    A("")
    A(_tbl([("Put 總成交量", _fi(_ot['p_vol']), SRC_FX),
            ("Put 總未平倉量 OI", _fi(_ot['p_oi']), SRC_FX),
            ("Put OI 增減" + (f" ({_sdate}→{t0})" if _ch.get("p_chg") is not None else ""),
             _f2s(_ch.get("p_chg")), SRC_SNAP if _ch.get("p_chg") is not None else "端點未提供")],
           ("項目", "數值", "資料來源")))
    A("")
    A("### 4．Call／Put 比例與變化")
    A("")
    _pch = taifex_official.putcall_history()
    _pc_rows = [("Call／Put 成交量比例", _f2(_ot['vol_ratio']), SRC_FX),
                ("Call／Put 未平倉量比例", _f2(_ot['oi_ratio']), SRC_FX),
                ("Put／Call Ratio", _f2(_ot['pc_ratio']), SRC_FX)]
    if len(_pch) >= 2:
        _a, _b = _pch[-2], _pch[-1]
        _pc_rows += [(f"Call／Put 比例變化 (量比 {_a['date']}→{_b['date']})",
                      _f2(_diff2(_b['vol_ratio'], _a['vol_ratio'])), SRC_FX_OFF),
                     (f"與前一交易日比較 (OI 比 {_a['date']}→{_b['date']})",
                      _f2(_diff2(_b['oi_ratio'], _a['oi_ratio'])), SRC_FX_OFF)]
    else:
        _pc_rows += [("Call／Put 比例變化", MISSING, "端點未提供"),
                     ("與前一交易日比較", MISSING, "端點未提供")]
    A(_tbl(_pc_rows, ("項目", "數值", "資料來源")))
    A("**資料來源：** 比例 `TAIFEX Proxy chain`；變化 `TAIFEX OpenAPI PutCallRatio`")
    A("")
    A("### 5．外資 Call／Put 部位")
    A("")
    _ps = (_sg.get("pos") or {})
    _pf, _pd = _ps.get("foreign") or {}, _ps.get("dealer") or {}
    A(_tbl([("外資 Call 部位 (夜盤淨口數)", _f2s(_op['foreign']['ah_c_net']), SRC_FX),
            ("外資 Put 部位 (夜盤淨口數)", _f2s(_op['foreign']['ah_p_net']), SRC_FX),
            ("外資 Call／Put 淨部位 (日盤淨口數)", _f2s(_op['foreign']['net']), SRC_FX),
            ("外資部位增減" + (f" (日盤淨 {_sdate}→{t0})" if _pf.get("opt_chg") is not None else ""),
             _f2s(_pf.get("opt_chg")), SRC_SNAP if _pf.get("opt_chg") is not None else "端點未提供")],
           ("項目", "口數", "資料來源")))
    A("")
    A("### 6．自營商 Call／Put 部位")
    A("")
    A(_tbl([("自營商 Call 部位 (夜盤淨口數)", _f2s(_op['dealer']['ah_c_net']), SRC_FX),
            ("自營商 Put 部位 (夜盤淨口數)", _f2s(_op['dealer']['ah_p_net']), SRC_FX),
            ("自營商 Call／Put 淨部位 (日盤淨口數)", _f2s(_op['dealer']['net']), SRC_FX),
            ("自營商部位增減" + (f" (日盤淨 {_sdate}→{t0})" if _pd.get("opt_chg") is not None else ""),
             _f2s(_pd.get("opt_chg")), SRC_SNAP if _pd.get("opt_chg") is not None else "端點未提供")],
           ("項目", "口數", "資料來源")))
    A("")
    A("### 7．主要 Call OI 集中區")
    A("")
    _crows = [("Call OI 第%d大履約價" % (i + 1), _fi(kk), _fi(vv), SRC_FX)
              for i, (kk, vv) in enumerate(_oc["c_top"][:3])]
    _crows.append(("Call OI 最大履約價", _fi(_oc['c_max'][0]), _fi(_oc['c_max'][1]), SRC_FX))
    A(_tbl(_crows, ("項目", "履約價", "OI", "資料來源")))
    A("")
    A("#### Call OI 分布明細 Top10 (機器可讀，到期月份 {})".format(_od.get("expiry") or MISSING))
    A("")
    if _od["call"]:
        A(_tbl([(f"C{i + 1}", _fi(r["strike"]), _fi(r["oi"]),
                 f"{r['pct']}%" if r["pct"] is not None else MISSING, SRC_FX)
                for i, r in enumerate(_od["call"])],
               ("#", "履約價", "OI", "佔比", "資料來源")))
    else:
        A(_tbl([("TBD", MISSING, MISSING, MISSING, "端點未提供")],
               ("#", "履約價", "OI", "佔比", "資料來源")))
    A("")
    A("")
    A("### 8．主要 Put OI 集中區")
    A("")
    _prows = [("Put OI 第%d大履約價" % (i + 1), _fi(kk), _fi(vv), SRC_FX)
              for i, (kk, vv) in enumerate(_oc["p_top"][:3])]
    _prows.append(("Put OI 最大履約價", _fi(_oc['p_max'][0]), _fi(_oc['p_max'][1]), SRC_FX))
    A(_tbl(_prows, ("項目", "履約價", "OI", "資料來源")))
    A("")
    A("#### Put OI 分布明細 Top10 (機器可讀，到期月份 {})".format(_od.get("expiry") or MISSING))
    A("")
    if _od["put"]:
        A(_tbl([(f"P{i + 1}", _fi(r["strike"]), _fi(r["oi"]),
                 f"{r['pct']}%" if r["pct"] is not None else MISSING, SRC_FX)
                for i, r in enumerate(_od["put"])],
               ("#", "履約價", "OI", "佔比", "資料來源")))
    else:
        A(_tbl([("TBD", MISSING, MISSING, MISSING, "端點未提供")],
               ("#", "履約價", "OI", "佔比", "資料來源")))
    A("")
    A("")
    A("### 9．Call OI 增減集中區")
    A("")
    def _mv(x, kind):
        if not x:
            return MISSING
        return f"{_fi(x['strike'])} ({_f2s(x['d_oi'])})"
    A(_tbl([("Call OI 增加最多的履約價", _mv(_ch.get("c_up"), 1),
             SRC_SNAP if _ch.get("c_up") else "端點未提供"),
            ("Call OI 減少最多的履約價", _mv(_ch.get("c_dn"), 1),
             SRC_SNAP if _ch.get("c_dn") else "端點未提供")],
           ("項目", "履約價 (增減口數)", "資料來源")))
    A("")
    A("### 10．Put OI 增減集中區")
    A("")
    A(_tbl([("Put OI 增加最多的履約價", _mv(_ch.get("p_up"), 1),
             SRC_SNAP if _ch.get("p_up") else "端點未提供"),
            ("Put OI 減少最多的履約價", _mv(_ch.get("p_dn"), 1),
             SRC_SNAP if _ch.get("p_dn") else "端點未提供")],
           ("項目", "履約價 (增減口數)", "資料來源")))
    A("")
    A("### 11．Call Wall")
    A("")
    _wl = (_sg.get("walls") or {})
    A(_tbl([("Call Wall 價位", _fi(_w['call'].get('strike')), SRC_FX),
            ("對應到期月份", _w['expiry'] or MISSING, SRC_FX),
            ("與前一交易日的變化" + (f" ({_sdate}→{t0})" if _wl.get("call") is not None else ""),
             _f2s(_wl.get("call")), SRC_SNAP if _wl.get("call") is not None else "端點未提供")],
           ("項目", "數值", "資料來源")))
    A("")
    A("### 12．Put Wall")
    A("")
    A(_tbl([("Put Wall 價位", _fi(_w['put'].get('strike')), SRC_FX),
            ("對應到期月份", _w['expiry'] or MISSING, SRC_FX),
            ("與前一交易日的變化" + (f" ({_sdate}→{t0})" if _wl.get("put") is not None else ""),
             _f2s(_wl.get("put")), SRC_SNAP if _wl.get("put") is not None else "端點未提供")],
           ("項目", "數值", "資料來源")))
    A("")
    A("### 13．Gamma Wall")
    A("")
    _gm = fx["gamma"]
    _gm_src = f"{SRC_FX} ({_gm.get('src', '')})" if _gm.get("wall") is not None else "端點未提供"
    A(_tbl([("Gamma Wall 價位", _f2(_gm['wall']), _gm_src),
            ("對應到期月份", _w['expiry'] or MISSING, SRC_FX),
            ("資料日期", _gm['date'] or MISSING, _gm_src)],
           ("項目", "數值", "資料來源")))
    A("")
    A("### 14．Gamma Flip")
    A("")
    A(_tbl([("Gamma Flip 價位", _f2(_gm['flip']), _gm_src),
            ("對應到期月份", _w['expiry'] or MISSING, SRC_FX),
            ("資料日期", _gm['date'] or MISSING, _gm_src)],
           ("項目", "數值", "資料來源")))
    A("")
    A("### 15．Max Pain")
    A("")
    A(_tbl([("Max Pain 價位", _fi(_w['maxpain'].get('strike')), SRC_FX),
            ("對應到期月份", _w['expiry'] or MISSING, SRC_FX),
            ("與前一交易日的變化" + (f" ({_sdate}→{t0})" if _wl.get("maxpain") is not None else ""),
             _f2s(_wl.get("maxpain")), SRC_SNAP if _wl.get("maxpain") is not None else "端點未提供")],
           ("項目", "數值", "資料來源")))
    A("")
    A("### 16．資料來源、時間、時區與狀態")
    A("")
    A("- 資料來源：TAIFEX 經 Cloudflare Worker Proxy")
    A(f"- 資料日期：{t0}；資料時間：{now}；時區：`Asia/Taipei`")
    A("- 日盤／夜盤標記：日盤收盤後 + 夜盤盤後")
    _snap = fx.get("snapchg", {})
    _snap_unav = []
    if not _snap.get("chain"):
        _snap_unav.append("options.chain_oi_change")
    if not _snap.get("pos"):
        _snap_unav.append("options.pos_change")
    if not _snap.get("walls"):
        _snap_unav.append("options.wall_change")
    if not _t10chg:
        _snap_unav.append("futures.top10_change")
    _all_unav = s["unavailable"] + [f"futures.{x}" for x in fx["unavailable"]] + _snap_unav
    A(f"- 未取得欄位 ({len(_all_unav)})：{', '.join(_all_unav) if _all_unav else '無'}")
    for nn in fx["notes"]:
        A(f"- 註記：{nn}")
    A("")
    A("## 五、資料來源、時間與完整性")
    A("")
    A("- 期貨/匯率為最新報價，其餘為 T0 收盤資料；時間皆為 `Asia/Taipei`。")
    for k, v in s["sources"].items():
        A(f"- {k}：`{v}`")
    A("- 期貨選擇權：`TAIFEX Proxy`")
    A(f"- 新聞：台股 Yahoo／國際 Fed＋CNBC＋MarketWatch；{_news_note}")
    A(f"- 美股/亞股/期貨/匯率/ADR/商品：`Yahoo Finance Chart API`；美債：`{y['10Y']['source']}`")
    for n in s["notes"]:
        A(f"- 註記：{n}")
    A("- 本報告僅整理資料，不提供交易判斷。")
    return "\n".join(L) + "\n"

def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--date", default="", help="報告日期 YYYY-MM-DD，預設今天 (Asia/Taipei)")
    ap.add_argument("--t0", default="", help="T0 交易日期 YYYY-MM-DD，預設最近平日")
    args = ap.parse_args()
    today = datetime.now(TAIPEI).date()
    report_date = args.date.strip() or today.isoformat()
    if args.t0.strip():
        t0 = args.t0.strip()
    else:
        try:
            from src.t0 import resolve as _resolve
            t0 = _resolve().get("t0") or last_weekday(date.fromisoformat(report_date)).isoformat()
        except Exception:
            t0 = last_weekday(date.fromisoformat(report_date)).isoformat()
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    out = OUT_DIR / f"DATA_REPORT_{t0.replace('-', '')}.md"
    out.write_text(build(report_date, t0), encoding="utf-8")
    print(f"[OK] wrote {out} (report_date={report_date}, t0={t0})")

if __name__ == "__main__":
    main()
