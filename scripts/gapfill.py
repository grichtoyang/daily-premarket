# -*- coding: utf-8 -*-
"""缺數補登（gap-fill）：只補 unavailable／前值遞補格，不動正常值。

用法（repo 根目錄）：
    python scripts/gapfill.py --t0 20261012

設計（2026-10-13 用戶定案：Actions 主抓＋本機只補洞）：
- 本機價值 = 住宅 IP（wantgoo 等擋機房 IP 的源）＋即時重試，不是重抓全部。
- 只處理：融資融券（HiStock 上市+上櫃）、維持率（三源 T0 重試＋遞補更新）、
  借券賣出（TWT93U＋TPEX）、Yahoo 代號列的缺格。
- 其餘缺失（TAIFEX 端點類）列出請人工走 SOP 3.5，不碰。
- 未取得計數行重算；每補一格加一條註記。冪等（無洞可補時零改動）。
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))


def _t0iso(t0: str) -> str:
    t0 = t0.strip().replace("-", "")
    return f"{t0[:4]}-{t0[4:6]}-{t0[6:8]}"


def _fill_yahoo(lines, t0):
    """Yahoo 代號列缺格補登。回傳 (fills, skips)。"""
    from src.sources import us_market
    fills, skips = [], []
    cur_sec = ""
    for i, ln in enumerate(lines):
        s = ln.strip()
        if s.startswith("#"):
            cur_sec = s
            continue
        if not s.startswith("|") or "unavailable" not in s:
            continue
        if not any(k in cur_sec for k in ("美股指數", "亞洲主要", "美股指數期貨",
                                          "主要匯率", "台灣相關ADR", "原油黃金")):
            continue
        cells = [c.strip() for c in s.strip("|").split("|")]
        if len(cells) < 6:
            continue
        sym = cells[1]
        if not sym or sym == "unavailable":
            skips.append(f"L{i + 1} 無代號")
            continue
        q = us_market.quote(sym)
        if not q.get("ok") or q.get("price") is None:
            skips.append(f"L{i + 1} {sym} Yahoo 仍失敗")
            continue
        try:
            v = f"{float(q['price']):,.2f}"
            ch = (f"{float(q['change']):+,.2f}"
                  if q.get("change") is not None else cells[3])
            pc = (f"{float(q['pct']):+.2f}"
                  if q.get("pct") is not None else cells[4])
        except (ValueError, TypeError):
            skips.append(f"L{i + 1} {sym} 數值異常")
            continue
        new = [cells[0], cells[1],
               v if cells[2] == "unavailable" else cells[2],
               ch if cells[3] == "unavailable" else cells[3],
               pc if cells[4] == "unavailable" else cells[4],
               cells[5]]
        lines[i] = "| " + " | ".join(new) + " |"
        fills.append(f"L{i + 1} {cells[0]} {sym}＝{v}（Yahoo {q.get('date')}）")
    return fills, skips


def _fill_margin(lines, t0):
    """融資融券 HiStock 缺格補登。"""
    from src.sources.histock import get as histock_get
    need = any(("融資餘額" in l or "融資增減" in l or "融券餘額" in l
                or "融券增減" in l) and "unavailable" in l
               for l in lines if l.strip().startswith("|"))
    if not need:
        return [], []
    h = histock_get(_t0iso(t0))
    if not h.get("listed") or not h.get("otc"):
        return [], ["HiStock 上市/上櫃缺一（僅單邊不補，避免口徑混淆）"]
    fin = h["listed"]["fin_yi"] + h["otc"]["fin_yi"]
    finc = h["listed"]["fin_chg_yi"] + h["otc"]["fin_chg_yi"]
    sbal = h["listed"]["short_bal"] + h["otc"]["short_bal"]
    schg = h["listed"]["short_chg"] + h["otc"]["short_chg"]
    vals = {"融資餘額": f"{fin:,.1f}", "融資增減": f"{finc:+.1f}",
            "融券餘額": f"{sbal:,.0f}", "融券增減": f"{schg:+,.0f}"}
    fills = []
    for i, ln in enumerate(lines):
        s = ln.strip()
        if not s.startswith("|"):
            continue
        cells = [c.strip() for c in s.strip("|").split("|")]
        if not cells or cells[0] not in vals or len(cells) < 4:
            continue
        if cells[1] != "unavailable":
            continue
        cells[1] = vals[cells[0]]
        cells[3] = "HiStock 上市+上櫃 (gapfill 自動補登)"
        lines[i] = "| " + " | ".join(cells) + " |"
        fills.append(f"L{i + 1} {cells[0]}＝{vals[cells[0]]}")
    return fills, []


def _fill_ratio(lines, t0):
    """維持率：無條件重試 T0 真值；有比現列更新的日期就換（遞補鏈自動前進）。
    現列可能是 unavailable，也可能是舊日期 wantgoo 值（fetch-time 遞補）。"""
    from src.sources import maint_ratio
    idx = next((i for i, l in enumerate(lines)
                if l.strip().startswith("|") and "融資維持率" in l), None)
    if idx is None:
        return [], []
    cells = [c.strip() for c in lines[idx].strip("|").split("|")]
    if len(cells) < 4:
        return [], []
    m = re.search(r"資料日期 (\d{4}-\d{2}-\d{2})", cells[3])
    cur_date = m.group(1) if m else ""
    r = maint_ratio.get(_t0iso(t0))
    if not r.get("ok") or r.get("ratio") is None or not r.get("date"):
        return [], ["維持率三源皆失敗（沿用原值）"]
    if cur_date and r["date"] <= cur_date:
        return [], [f"維持率無更新（源 {r['date']} <= 現 {cur_date}）"]
    src = {"wantgoo": "wantgoo", "stockintelli": "stockintelli",
           "istock": "istock"}.get(r.get("source"), "wantgoo")
    cells[1] = f"{float(r['ratio']):.2f}"
    cells[3] = (f"{src} 大盤融資維持率 (資料日期 {r.get('date')}；"
                f"民間估算；官方無每日序列；gapfill 自動補登)")
    lines[idx] = "| " + " | ".join(cells) + " |"
    return [f"L{idx + 1} 維持率＝{cells[1]}（{src} {r.get('date')}）"], []


def _fill_sbl(lines, t0):
    """借券賣出：TWT93U＋TPEX，按 spot.py 同口徑合併。"""
    from src.sources import spot_raw
    need = any(("借券賣出餘額" in l or "借券賣出增減" in l)
               and "unavailable" in l
               for l in lines if l.strip().startswith("|"))
    if not need:
        return [], []
    roc = spot_raw.roc8(_t0iso(t0))
    tw = spot_raw.twse_twt93u_sbl(roc)
    tp = spot_raw.tpex_sbl(roc)
    if tp.get("sale_bal") is None:
        return [], ["TPEX sbl 失敗（上櫃無值不補）"]
    tw_s = tw["sale_bal"] / 1000 if tw.get("sale_bal") is not None else None
    tp_s = tp["sale_bal"] / 1000
    tw_c = tw["sale_chg"] / 1000 if tw.get("sale_chg") is not None else None
    tp_c = tp["sale_chg"] / 1000
    bal = (tw_s if tw_s is not None else 0) + tp_s
    chg = (tw_c if tw_c is not None else 0) + tp_c
    tag = ("TWSE TWT93U + TPEX margin_sbl" if tw_s is not None
           else "TPEX margin_sbl (僅上櫃值；TWT93U 未取得；gapfill 自動補登)")
    fills = []
    for i, ln in enumerate(lines):
        s = ln.strip()
        if not s.startswith("|"):
            continue
        cells = [c.strip() for c in s.strip("|").split("|")]
        if not cells or len(cells) < 4 or cells[1] != "unavailable":
            continue
        if cells[0] == "借券賣出餘額":
            cells[1] = f"{bal:,.0f}"
            cells[3] = tag
        elif cells[0] == "借券賣出增減":
            cells[1] = f"{chg:+,.0f}"
            cells[3] = tag
        else:
            continue
        lines[i] = "| " + " | ".join(cells) + " |"
        fills.append(f"L{i + 1} {cells[0]}＝{cells[1]}")
    return fills, []


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--t0", required=True, help="YYYYMMDD")
    args = ap.parse_args()
    p = ROOT / "data_reports" / f"DATA_REPORT_{args.t0}.md"
    if not p.exists():
        print(f"MISS_DATA={p}")
        return 2
    lines = p.read_text(encoding="utf-8").split("\n")
    all_fills, all_skips = [], []
    for fn in (_fill_yahoo, _fill_margin, _fill_ratio, _fill_sbl):
        try:
            f, s = fn(lines, args.t0)
        except Exception as e:  # noqa: BLE001
            f, s = [], [f"{fn.__name__} 執行異常：{e}"]
        all_fills += f
        all_skips += s
    if all_fills:
        # 未取得計數行不重寫（它是 fetch-time 基線）；只在後面追加補登註記。
        uidx = next((i for i, ln in enumerate(lines)
                     if re.match(r"^- 未取得欄位 \(\d+\)", ln.strip())), None)
        if uidx is not None:
            for n, f in enumerate(all_fills):
                lines.insert(uidx + 1 + n,
                             f"- 註記：gapfill 自動補登 {f}")
        else:
            for f in all_fills:
                lines.append(f"- 註記：gapfill 自動補登 {f}")
        p.write_text("\n".join(lines), encoding="utf-8")
    print(f"GAPFILLED={len(all_fills)}")
    for f in all_fills:
        print("FILL " + f)
    print(f"SKIPPED={len(all_skips)}")
    for s in all_skips:
        print("SKIP " + s)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
