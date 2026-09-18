"""視覺層 V4：五頁式戰報（總結/Daily，現貨/重要市場/期貨/選擇權/DATA章節）。

- 總結 ← Daily_REPORT 全文＋機器區圖表
- 現貨/重要市場/期貨/選擇權 ← DATA_REPORT 對應章節原表呈現＋重點圖
只讀不寫，本機執行：streamlit run dashboard/app.py
"""
from __future__ import annotations
import json
import re
from pathlib import Path

import streamlit as st
import pandas as pd
import plotly.graph_objects as go

ROOT = Path(__file__).resolve().parent.parent
REPORTS_DIR = ROOT / "reports"
DATA_DIR = ROOT / "data_reports"
LATEST = REPORTS_DIR / "latest.json"

NAVY = "#12366b"
st.set_page_config(page_title="每日盤前分析", page_icon="📈", layout="wide")
st.markdown(
    """<style>
div.block-container{padding-top:1rem;max-width:1220px}
h2{background:linear-gradient(90deg,#0b2d63,#1c4d8b);color:#fff;border-radius:6px;
padding:10px 14px;font-size:22px}
div[data-testid="stMetric"]{background:#fff;border:1px solid #aebfd6;border-top:4px solid #174b91;
border-radius:7px;padding:8px}
</style>""",
    unsafe_allow_html=True,
)

# ---------------- 解析 ----------------
def md_tables(md: str, section: str) -> list[pd.DataFrame]:
    """某節內所有 markdown 表格。"""
    m = re.search(rf"{re.escape(section)}([\s\S]*?)(?=^#{{1,4}} |\Z)", md, re.M)
    if not m:
        return []
    out = []
    for tm in re.finditer(r"((?:\|.*\n){3,})", m.group(1)):
        lines = [l.strip() for l in tm.group(1).strip().splitlines() if l.strip()]
        if len(lines) < 3:
            continue
        hdr = [c.strip() for c in lines[0].strip("|").split("|")]
        rows = [[c.strip() for c in ln.strip("|").split("|")] for ln in lines[2:]]
        try:
            out.append(pd.DataFrame(rows, columns=hdr))
        except Exception:
            pass
    return out

def md_table(md: str, section: str, idx: int = 0) -> pd.DataFrame | None:
    ts = md_tables(md, section)
    return ts[idx] if len(ts) > idx else None

def parse_blocks(md: str) -> dict:
    out: dict[str, list] = {}
    for name in ("kpi", "levels", "oidist", "scenarios"):
        m = re.search(rf"```{name}\n(.*?)```", md, re.S)
        rows = []
        if m:
            for line in m.group(1).strip().splitlines():
                parts = [c.strip() for c in line.split("|")]
                if len(parts) >= 2:
                    rows.append(parts)
        out[name] = rows
    return out

def section_text(md: str, header: str) -> str:
    m = re.search(rf"(?m)^#{{1,4}} .*?{re.escape(header)}.*?\n(.*?)(?=^#{{1,4}} |\Z)", md, re.S)
    return m.group(1).strip() if m else ""

def num(x) -> float | None:
    try:
        v = float(str(x).replace(",", "").replace("+", "").replace("%", ""))
        return v
    except (ValueError, TypeError):
        return None

def kpi_row(cols, label: str, value: str, unit: str = ""):
    cols.metric(label, f"{value} {unit}".strip())

@st.cache_data(ttl=60)
def load_latest() -> dict | None:
    try:
        return json.loads(LATEST.read_text(encoding="utf-8"))
    except Exception:
        return None

@st.cache_data(ttl=60)
def load_md(path_str: str) -> str | None:
    try:
        p = ROOT / path_str
        return p.read_text(encoding="utf-8") if p.exists() else None
    except Exception:
        return None

def list_history() -> list[str]:
    if not REPORTS_DIR.exists():
        return []
    return sorted((f.name for f in REPORTS_DIR.glob("Daily_REPORT_*.md")), reverse=True)

# ---------------- 載入 ----------------
latest = load_latest()
if latest is None:
    st.error("尚無報告：找不到 reports/latest.json。")
    st.stop()
history = list_history()
sel = st.sidebar.selectbox("歷史報告", history if history else ["(無)"])
ana_path = f"reports/{sel}" if history else latest.get("report_path", "")
md = load_md(ana_path)
if md is None:
    st.error(f"找不到分析報告：{ana_path}")
    st.stop()
mdate = re.search(r"(\d{8})", sel or "")
rdate = mdate.group(1) if mdate else latest.get("report_date", "")
dpath = f"data_reports/DATA_REPORT_{rdate}.md"
dmd = load_md(dpath) or ""
ymd = f"{rdate[:4]}-{rdate[4:6]}-{rdate[6:]}" if len(rdate) == 8 else rdate
blocks = parse_blocks(md)
GH = "https://github.com/grichtoyang/daily-premarket/blob/master"
gh_data = f"{GH}/{dpath}"
gh_ana = f"{GH}/{ana_path}"

st.title("📈 每日盤前分析 Dashboard")
st.caption(f"報告日 {ymd}｜Asia/Taipei｜[原始 DATA 報告]({gh_data})")

tab_sum, tab_spot, tab_mkt, tab_fut, tab_opt = st.tabs(
    ["總結", "現貨", "重要市場", "期貨", "選擇權"])

# ================= 總結 ← Daily =================
with tab_sum:
    st.header("總結")
    oneline = re.search(r"一句話結論[：:]\s*(.+)", md)
    if oneline:
        st.info(f"💡 一句話結論：{oneline.group(1).strip()}")
    kpis = blocks["kpi"]
    if kpis:
        cols = st.columns(min(len(kpis), 5))
        for i, row in enumerate(kpis[:10]):
            kpi_row(cols[i % len(cols)], row[0], row[1], row[2] if len(row) > 2 else "")
    c1, c2 = st.columns(2)
    with c1:
        st.subheader("關鍵價位")
        lv = blocks["levels"]
        if lv:
            labels, prices, colors = [], [], []
            cmap = {"壓力": "red", "中軸": "gray", "支撐": "green"}
            for row in lv:
                if len(row) < 2:
                    continue
                p = num(row[1])
                if p is None:
                    continue
                labels.append(f"{row[0]} {row[1]}")
                prices.append(p)
                colors.append(cmap.get(row[0], "blue"))
            fig = go.Figure(go.Bar(x=prices, y=labels, orientation="h", marker_color=colors))
            fig.update_layout(height=260, margin=dict(l=10, r=10, t=10, b=10), showlegend=False)
            st.plotly_chart(fig, use_container_width=True)
    with c2:
        st.subheader("今日交易計畫")
        sc = blocks["scenarios"]
        if sc:
            hdr = sc[0] if any("情境" in c for c in sc[0]) else None
            st.table(pd.DataFrame(sc[1:] if hdr else sc, columns=hdr or ["情境", "條件", "操作"]))
    for sec in ("現貨市場分析", "重要市場環境", "國際事件與新聞解讀", "台指期分析",
                "選擇權市場分析", "整合判讀", "盤前情境分析", "盤前交易執行框架",
                "資料完整性與限制", "最終結論"):
        t = section_text(md, sec)
        if t:
            with st.expander(sec, expanded=(sec == "最終結論")):
                st.markdown(t.split("## 附錄")[0][:2500])
    with st.expander("原始 DATA 報告全文"):
        st.markdown(dmd[:20000] if dmd else "無")

# ================= 現貨 ← DATA 第一章 =================
with tab_spot:
    st.header("現貨")
    if not dmd:
        st.warning(f"找不到 {dpath}")
    else:
        t1 = md_table(dmd, "台股大盤行情")
        if t1 is not None:
            a, b = st.columns([1, 1])
            with a:
                st.subheader("台股大盤行情")
                st.table(t1.iloc[:, :3])
            with b:
                st.subheader("市場漲跌家數")
                for sec in ("上市公司", "上櫃公司"):
                    t = md_table(dmd, sec)
                    if t is not None:
                        st.markdown(f"_{sec}_")
                        st.table(t)
        t3 = md_table(dmd, "三大法人現貨買賣超")
        if t3 is not None:
            a, b = st.columns([1, 1])
            with a:
                st.subheader("三大法人現貨買賣超")
                st.table(t3)
            with b:
                try:
                    vals = [num(r[1]) or 0 for _, r in t3.iterrows()]
                    fig = go.Figure(go.Bar(
                        x=list(t3.iloc[:, 0]), y=vals,
                        marker_color=["red" if v < 0 else "green" for v in vals]))
                    fig.update_layout(height=260, margin=dict(l=10, r=10, t=10, b=10),
                                      showlegend=False, yaxis_title="億元")
                    st.plotly_chart(fig, use_container_width=True)
                except Exception:
                    pass
        a, b = st.columns(2)
        with a:
            st.subheader("融資融券")
            t = md_table(dmd, "融資融券")
            if t is not None:
                st.table(t.iloc[:, :3])
        with b:
            st.subheader("借券資料")
            t = md_table(dmd, "借券資料")
            if t is not None:
                st.table(t.iloc[:, :3])
        st.subheader("市場成交結構")
        t = md_table(dmd, "市場成交結構")
        if t is not None:
            st.table(t)

# ================= 重要市場 ← DATA 第二章 =================
with tab_mkt:
    st.header("重要市場")
    if not dmd:
        st.warning(f"找不到 {dpath}")
    else:
        for sec in ("美股指數", "亞洲主要指數", "美股指數期貨", "美國國債殖利率",
                    "主要匯率", "台灣相關ADR", "原油黃金Bitcoin"):
            t = md_table(dmd, sec)
            if t is not None:
                st.subheader(sec)
                st.table(t)
        st.subheader("重大經濟數據、央行事件與重大市場新聞")
        news = section_text(dmd, "重大經濟數據")
        evts = re.findall(r"^- 事件\d+：(.+)$", news, re.M)[:10]
        if evts:
            st.table(pd.DataFrame({"事件": evts}))
        with st.expander("新聞明細"):
            st.markdown(news[:4000] if news else "無")

# ================= 期貨 ← DATA 第三章 =================
with tab_fut:
    st.header("期貨")
    if not dmd:
        st.warning(f"找不到 {dpath}")
    else:
        for sec in ("台指期近月日盤行情", "台指期近月夜盤行情", "法人台指期多空未平倉部位",
                    "前十大交易人多空未平倉部位", "日盤、夜盤法人交易資料",
                    "期貨與現貨關係", "日盤、夜盤與籌碼變化對照"):
            ts = md_tables(dmd, sec)
            if not ts:
                continue
            st.subheader(sec)
            for t in ts:
                st.table(t)
        with st.expander("夜盤劇本分類"):
            st.markdown(section_text(dmd, "夜盤劇本分類")[:1500])

# ================= 選擇權 ← DATA 第四章 =================
with tab_opt:
    st.header("選擇權")
    if not dmd:
        st.warning(f"找不到 {dpath}")
    else:
        oi = blocks["oidist"]
        calls = [(int(r[1].replace(",", "")), int(r[2].replace(",", "")))
                 for r in oi if len(r) >= 3 and r[0] == "call"
                 and r[1].replace(",", "").isdigit()]
        puts = [(int(r[1].replace(",", "")), int(r[2].replace(",", "")))
                for r in oi if len(r) >= 3 and r[0] == "put"
                and r[1].replace(",", "").isdigit()]
        if calls or puts:
            st.subheader("選擇權 OI 分布")
            fig = go.Figure()
            if calls:
                fig.add_bar(x=[c[0] for c in calls], y=[c[1] for c in calls],
                            name="Call OI", marker_color="indianred")
            if puts:
                fig.add_bar(x=[c[0] for c in puts], y=[c[1] for c in puts],
                            name="Put OI", marker_color="steelblue")
            lvmap = {}
            for row in blocks["levels"]:
                if len(row) >= 2 and num(row[1]) is not None:
                    lvmap[row[0]] = num(row[1])
            for name, color in (("壓力", "red"), ("中軸", "gray"), ("支撐", "green")):
                if name in lvmap:
                    fig.add_vline(x=lvmap[name], line_color=color, line_dash="dash",
                                  annotation_text=name)
            fig.update_layout(barmode="group", height=380,
                              margin=dict(l=10, r=10, t=10, b=10),
                              xaxis_title="履約價", yaxis_title="OI")
            st.plotly_chart(fig, use_container_width=True)
            st.caption("⚠️ Walls 為模型結果，非 TAIFEX 官方公布")
        for sec in ("選擇權交易日期", "Call 總成交量", "Put 總成交量", "Call／Put 比例",
                    "外資 Call", "自營商 Call", "Call OI 集中", "Put OI 集中",
                    "Call OI 增減", "Put OI 增減", "Call Wall", "Put Wall",
                    "Gamma Wall", "Gamma Flip", "Max Pain"):
            for t in md_tables(dmd, sec):
                st.subheader(sec)
                st.table(t)

st.divider()
st.caption(f"分析報告：[{ana_path}]({gh_ana})｜原始數據：[{dpath}]({gh_data})｜"
           "非投資建議，僅供參考")
