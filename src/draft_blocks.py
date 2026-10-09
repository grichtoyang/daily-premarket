# -*- coding: utf-8 -*-
"""報告起草機：從 DATA_REPORT 產出附錄B五區塊＋§6/§5.5 表格草稿。

用法：
    python src/draft_blocks.py --data data_reports/DATA_REPORT_20261005.md [--out /tmp/draft.md]

原則：數字全自動（只出自 DATA，當前檔案 bytes，刷新也不怕抄錯版；
比較表/流向/前十大含區間與資料日期，一律照貼不手改）；
解讀全人工（verdict 理由、levels 價位選擇、scenarios 條件一律留白手寫）。
輸出直接貼進報告對應位置再補解讀。
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path


def _tables(md: str, section: str) -> list:
    """回傳 [{\"cols\": [...], \"rows\": [[...]]}]；起點須為標題行。"""
    m = re.search(rf"(?m)^#+ .*?{re.escape(section)}.*?$", md)
    if not m:
        return []
    seg = md[m.end():]
    m2 = re.search(r"(?m)^#{1,4} ", seg)
    seg = seg[:m2.start()] if m2 else seg
    out = []
    for tm in re.finditer(r"((?:\|.*\n){3,})", seg):
        lines = [l.strip() for l in tm.group(1).strip().splitlines() if l.strip()]
        if len(lines) < 3:
            continue
        hdr = [c.strip() for c in lines[0].strip("|").split("|")]
        rows = [[c.strip() for c in ln.strip("|").split("|")] for ln in lines[2:]]
        out.append({"cols": hdr, "rows": rows})
    return out


def _first_table(md: str, section: str):
    ts = _tables(md, section)
    return ts[0] if ts else None


def _cell(t, label: str, col: int = 1) -> str:
    """首欄含 label 的第一列取 col 欄；找不到回 '—'。"""
    if t is None:
        return "—"
    for r in t["rows"]:
        if label in str(r[0]):
            return str(r[col]) if col < len(r) else "—"
    return "—"


def _num(s: str) -> str:
    """kpi/oidist 格式：去逗號，保留正負號；整數位小數 (.00) 去尾（Gamma Wall 慣例取整）。"""
    v = str(s).replace(",", "").strip()
    if v.endswith(".00"):
        v = v[:-3]
    return v


def _kpi(data: str) -> list[str]:
    def _mkt(sec: str, rowkey: str, col: int):
        t = _first_table(data, sec)
        if t is None:
            return "unavailable"
        for r in t["rows"]:
            if str(r[0]).strip() == rowkey:
                return str(r[col]) if col < len(r) else "unavailable"
        return "unavailable"

    us = _first_table(data, "美股指數")
    sox = _mkt_us(us, "費城半導體 SOX")
    vix_close = "unavailable"
    if us is not None:
        for r in us["rows"]:
            if str(r[0]).strip() == "VIX" and len(r) > 2:
                vix_close = str(r[2])
    tsm = _mkt_us(_first_table(data, "台灣相關ADR"), "台積電ADR")
    night = _first_table(data, "台指期近月夜盤行情")
    day_price = _cell(_first_table(data, "期貨與現貨關係"), "台指期近月價格")
    inst = _first_table(data, "三大法人現貨買賣超")
    foi = _first_table(data, "法人台指期多空未平倉部位")
    ftr = _first_table(data, "日盤、夜盤法人交易資料")
    walls = {}
    for sec, lbl in (("Call Wall", "cw"), ("Put Wall", "pw"), ("Gamma Wall", "gw")):
        t = _first_table(data, sec)
        v = "unavailable"
        if t is not None:
            for r in t["rows"]:
                if "價位" in str(r[0]) and "變化" not in str(r[0]):
                    v = str(r[1])
        walls[lbl] = v
    tx_close = _cell(_first_table(data, "台股大盤行情"), "收盤")
    # 夜盤成交量占比（7.1 在 #### 子節下，直接定位子節）
    ratio = "unavailable"
    t71 = _tables(data, "日夜盤價格與成交量對照")
    if t71:
        for r in t71[0]["rows"]:
            if str(r[0]).strip() == "成交量" and len(r) >= 3:
                try:
                    dv = float(str(r[1]).replace(",", ""))
                    nv = float(str(r[2]).replace(",", ""))
                    ratio = f"{nv / (nv + dv) * 100:.2f}" if (nv + dv) else "unavailable"
                except (ValueError, TypeError):
                    pass
    return [
        f"加權收盤|{_num(tx_close)}|點",
        f"台指夜盤成交量占比|{ratio}|%",
        f"外資現貨|{_num(_cell(inst, '外資'))}|億元",
        f"外資期貨淨OI|{_num(_cell(foi, '外資多空淨 OI'))}|口",
        f"費半|{sox}|%",
        f"Call Wall|{_num(walls['cw'])}|點",
        f"Gamma Wall|{_num(walls['gw'])}|點",
        f"台指期收盤|{_num(day_price)}|點",
        f"台指夜盤漲跌|{_num(_cell(night, '漲跌點數'))}|點",
        f"投信現貨|{_num(_cell(inst, '投信'))}|億元",
        f"外資夜盤淨|{_num(_cell(ftr, '外資夜盤多空淨交易量'))}|口",
        f"台積電ADR|{tsm}|%",
        f"Put Wall|{_num(walls['pw'])}|點",
        f"VIX|{_num(vix_close)}|",
    ]


def _mkt_us(us, name: str) -> str:
    if us is None:
        return "unavailable"
    for r in us["rows"]:
        if str(r[0]).strip() == name:
            return str(r[4]) if len(r) > 4 else "unavailable"
    return "unavailable"


def _oidist(data: str) -> list[str]:
    out = []
    for sec, tag in (("Call OI 分布明細", "call"), ("Put OI 分布明細", "put")):
        ts = _tables(data, sec)
        if not ts:
            continue
        for r in ts[0]["rows"][:10]:
            if len(r) >= 3 and str(r[1]).replace(",", "").replace("+", "").replace("-", "").strip().isdigit():
                out.append(f"{tag}|{_num(r[1])}|{_num(r[2])}")
    return out


def _top10_merge(data: str) -> list[str]:
    """§6.4 Top10 全表並排（markdown 表格行；整張照貼進 6.4，下加備查註記）。"""
    lines = ["| # | Call 履約價 | Call OI | Call 佔比 | Put 履約價 | Put OI | Put 佔比 |",
             "|---|---|---|---|---|---|---|"]
    try:
        cc = _tables(data, "Call OI 分布明細")[0]["rows"][:10]
        pp = _tables(data, "Put OI 分布明細")[0]["rows"][:10]
        for i in range(min(10, len(cc), len(pp))):
            c, p = cc[i], pp[i]
            lines.append(f"| {i + 1} | {c[1]} | {c[2]} | "
                         f"{c[3] if len(c) > 3 else '—'} | {p[1]} | {p[2]} | "
                         f"{p[3] if len(p) > 3 else '—'} |")
    except (IndexError, KeyError):
        pass
    return lines


def _top3_merge(data: str) -> list[str]:
    """§6.1 Top3 並排表（markdown 表格行）。"""
    lines = ["| 排名 | Call 履約價 | Call OI | Call 佔比 | Put 履約價 | Put OI | Put 佔比 |",
             "|---|---|---|---|---|---|---|"]
    try:
        cc = _tables(data, "Call OI 分布明細")[0]["rows"][:3]
        pp = _tables(data, "Put OI 分布明細")[0]["rows"][:3]
        for i in range(min(3, len(cc), len(pp))):
            c, p = cc[i], pp[i]
            lines.append(f"| 第 {i + 1} 大 | {c[1]} | {c[2]} | "
                         f"{c[3] if len(c) > 3 else '—'} | {p[1]} | {p[2]} | "
                         f"{p[3] if len(p) > 3 else '—'} |")
    except (IndexError, KeyError):
        pass
    return lines


def _oi_moves(data: str) -> list[str]:
    """§6 OI 增減並排表（含最大 OI 列；缺值標 —）。"""
    def _mv(sec: str):
        t = _first_table(data, sec)
        up = dn = mx = "—"
        if t is not None:
            for r in t["rows"]:
                c0 = str(r[0])
                if "增加" in c0:
                    up = str(r[1])
                elif "減少" in c0:
                    dn = str(r[1])
                elif "最大" in c0:
                    mx = str(r[1])
        return up, dn, mx

    def _tot(sec: str):
        t = _first_table(data, sec)
        return _cell(t, "增減") if t is not None else "—"

    # 總增減列藏在 Call/Put 總量表（§§2/3 的增減列）
    _cup, _cdn, _cmx = _mv("Call OI 增減集中區")
    _pup, _pdn, _pmx = _mv("Put OI 增減集中區")
    return ["| 項目 | Call | Put |", "|---|---|---|",
            f"| 總 OI 增減 | {_tot('Call 總成交量')} | {_tot('Put 總成交量')} |",
            f"| 增加最多 | {_cup} | {_pup} |",
            f"| 減少最多 | {_cdn} | {_pdn} |",
            f"| 最大OI增減 | {_cmx} | {_pmx} |"]


def _seg(data: str, section: str) -> str:
    """取 section 標題起至下一個同級以上標題止的文字段（找資料日期註記用）。"""
    m = re.search(rf"(?m)^#+ .*?{re.escape(section)}.*?$", data)
    if not m:
        return ""
    seg = data[m.end():]
    m2 = re.search(r"(?m)^#{1,4} ", seg)
    return seg[:m2.start()] if m2 else seg


def _date_note(seg: str) -> str:
    m = re.search(r"(?m)^\s*-\s*資料日期.*?$", seg)
    if not m:
        return ""
    return re.sub(r"^\s*-\s*", "- ", m.group(0).strip())


def _interval(label: str) -> str:
    m = re.search(r"\(([^)]*→[^)]*)\)", str(label))
    return m.group(1) if m else ""


def _t10_fut(data: str) -> list[str]:
    """§5.5 期貨前十大草稿（貼進 5.5，數字直接用，下加解讀）。"""
    t = _first_table(data, "前十大交易人多空未平倉部位")
    vals = {"多方": "—", "空方": "—", "淨": "—", "變化": "—", "區間": ""}
    if t is not None:
        for r in t["rows"]:
            c0 = str(r[0])
            v = str(r[1]) if len(r) > 1 else "—"
            if "變化" in c0:
                vals["變化"] = v
                vals["區間"] = _interval(c0)
            elif "淨" in c0:
                vals["淨"] = v
            elif "多方" in c0:
                vals["多方"] = v
            elif "空方" in c0:
                vals["空方"] = v
    iv = f"（{vals['區間']}）" if vals["區間"] else ""
    lines = ["| 項目 | 口數 |", "|---|---|",
             f"| 多方 OI | {vals['多方']} |",
             f"| 空方 OI | {vals['空方']} |",
             f"| 多空淨 OI | {vals['淨']} |",
             f"| 多空淨 OI 變化{iv} | {vals['變化']} |"]
    note = _date_note(_seg(data, "前十大交易人多空未平倉部位"))
    if note:
        lines.append(note)
    return lines


def _opt_comps(data: str) -> list[str]:
    """§6.4 選擇權前十大比較表草稿（買權/賣權欄，貼進 6.4，數字直接用）。"""
    ts = _tables(data, "選擇權前十大")
    buy = sell = None
    if len(ts) >= 2:
        buy, sell = ts[0], ts[1]
    def _pick(t, key: str) -> str:
        if t is None:
            return "—"
        for r in t["rows"]:
            if key in str(r[0]):
                return str(r[1]) if len(r) > 1 else "—"
        return "—"
    def _pick_iv(t, key: str) -> tuple:
        if t is None:
            return "—", ""
        for r in t["rows"]:
            if key in str(r[0]):
                return (str(r[1]) if len(r) > 1 else "—"), _interval(r[0])
        return "—", ""
    b_long, s_long = _pick(buy, "多方"), _pick(sell, "多方")
    b_short, s_short = _pick(buy, "空方"), _pick(sell, "空方")
    b_net, s_net = _pick(buy, "淨 OI"), _pick(sell, "淨 OI")
    b_chg, b_iv = _pick_iv(buy, "變化")
    s_chg, s_iv = _pick_iv(sell, "變化")
    b_ivt = f"（{b_iv}）" if b_iv else ""
    s_ivt = f"（{s_iv}）" if s_iv else ""
    lines = ["| 項目 | 買權 | 賣權 |", "|---|---|---|",
             f"| 多方 OI | {b_long} | {s_long} |",
             f"| 空方 OI | {b_short} | {s_short} |",
             f"| 多空淨 OI | {b_net} | {s_net} |",
             f"| 多空淨 OI 變化 | {b_chg}{b_ivt} | {s_chg}{s_ivt} |"]
    note = _date_note(_seg(data, "選擇權前十大"))
    if note:
        lines.append(note)
    return lines


def _news_list(data: str) -> list[str]:
    """§4 事件清單草稿（只寫清單內事件，不憑記憶加；數字抄摘要原文）。"""
    seg = _seg(data, "重大經濟數據")
    lines = ["| # | 事件 | 摘要先60字 | 來源 |", "|---|---|---|---|"]
    titles = list(re.finditer(r"(?m)^\s*-\s*事件(\d+)：(.*)$", seg))
    sums = re.findall(r"(?m)^\s*-\s*摘要：(.*)$", seg)
    srcs = re.findall(r"(?m)^\s*-\s*來源：(.*?)[；;]", seg)
    for i, m in enumerate(titles):
        no, title = m.group(1), m.group(2).strip()[:36]
        s = sums[i].strip()[:60] if i < len(sums) else ""
        src = srcs[i].strip() if i < len(srcs) else ""
        lines.append(f"| {no} | {title} | {s} | {src} |")
    return lines


def _flow(data: str) -> list[str]:
    """§6.2 大戶流向草稿（貼進 6.2，數值＋區間直接用，下加解讀）。"""
    t = _first_table(data, "大戶流向")
    lines = ["| 項目 | 淨變化 | 區間 |", "|---|---|---|"]
    if t is not None:
        for r in t["rows"]:
            if len(r) >= 3:
                lines.append(f"| {r[0]} | {r[1]} | {r[2]} |")
    return lines


def _vix_block(data: str) -> list[str]:
    us = _first_table(data, "美股指數")
    vx = vxp = ""
    if us is not None:
        for r in us["rows"]:
            if str(r[0]).strip() == "VIX" and len(r) > 4:
                vx, vxp = str(r[2]), str(r[4])
    nt = _first_table(data, "台指期近月夜盤行情")
    hi = _cell(nt, "最高價") if nt is not None else ""
    lo = _cell(nt, "最低價") if nt is not None else ""
    amp = ""
    try:
        amp = f"{int(float(hi.replace(',', '')) - float(lo.replace(',', ''))):,} 點"
    except (ValueError, TypeError, AttributeError):
        pass
    if amp:
        amp += f"（算式：{hi}－{lo}）"
    return ["| 市場 | 數值 |", "|---|---|",
            f"| 美股 VIX | {vx}（{vxp}%） |" if vx else "| 美股 VIX | — |",
            "| 台股 VIX | 見玩股網連結（人工讀數） |",
            f"| 台指夜盤振幅 | {amp if amp else '—'} |"]


def build(data_path: str) -> str:
    data = Path(data_path).read_text(encoding="utf-8")
    L: list[str] = []
    A = L.append
    A("# DRAFT-附錄B（貼進報告附錄B，verdict/levels/scenarios 理由手寫）")
    A("```kpi")
    A("\n".join(_kpi(data)))
    A("```")
    A("```verdict")
    A("方向|\n信心|\n理由1|\n理由2|\n理由3|\n注意|")
    A("```")
    A("```levels")
    A("壓力|\n壓力二|\n中軸|\n支撐|\n支撐二|\n白話|")
    A("```")
    A("```oidist")
    A("\n".join(_oidist(data)))
    A("```")
    A("```scenarios")
    A("開高續攻|||\n開平震盪|||\n開低測撐|||\n破支撐走弱|||")
    A("```")
    A("")
    A("# DRAFT-§6.1 Top3 並排（貼進 6.1，下加解讀）")
    A("\n".join(_top3_merge(data)))
    A("")
    A("# DRAFT-§6.4 Top10 全表（整張照貼進 6.4，下加備查註記，不手排）")
    A("\n".join(_top10_merge(data)))
    A("")
    A("# DRAFT-§6 OI 增減並排（貼進 6.1，下加解讀）")
    A("\n".join(_oi_moves(data)))
    A("")
    A("# DRAFT-§6.3 VIX 三列（貼進 6.3，下加解讀）")
    A("\n".join(_vix_block(data)))
    A("")
    A("# DRAFT-§5.5 期貨前十大（貼進 5.5，數字直接用，下加解讀）")
    A("\n".join(_t10_fut(data)))
    A("")
    A("# DRAFT-§6.4 選擇權前十大比較表（貼進 6.4，買權/賣權欄＋區間直接用）")
    A("\n".join(_opt_comps(data)))
    A("")
    A("# DRAFT-§6.2 大戶流向（貼進 6.2，數值＋區間直接用，下加解讀）")
    A("\n".join(_flow(data)))
    A("")
    A("# DRAFT-§4 事件清單（只寫清單內事件，不憑記憶加；數字抄摘要原文）")
    A("\n".join(_news_list(data)))
    return "\n".join(L) + "\n"


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--data", required=True)
    ap.add_argument("--out", default="")
    args = ap.parse_args()
    text = build(args.data)
    if args.out:
        Path(args.out).write_text(text, encoding="utf-8")
        print(f"[OK] wrote {args.out} ({len(text)} chars)")
    else:
        print(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
