# -*- coding: utf-8 -*-
"""報告數字稽核：報告所有數字必須出自 DATA（常駐版，單輪驗證用）。

用法：
    python scripts/numcheck.py --data data_reports/DATA_REPORT_yyyymmdd.md \
        --report reports/Daily_REPORT_yyyymmdd_全日.md

三層檢查：
1. token 稽核：報告數字 token（去逗號＋數值比對）必須存在於 DATA；
   豁免：前值引用行（前/昨/上週/→）、算式行、情境條件行、§8/§9/§10/結論/檢查表。
2. 結構檢查：§5.5 前十大表＋ narrative、§6.4 比較表（買權/賣權欄位語義）、
   §6.2 大戶流向（數值＋區間），逐格對 DATA。
3. 輸出 DATA sha256（開工凍結基線用；gate 前比對，不一致代表 DATA 被改寫過）。

結束碼：0 全過；1 有 ERROR。
"""
from __future__ import annotations

import argparse
import hashlib
import re
import sys

EXEMPT_WORDS = ["前", "昨", "上週", "上周", "→", "算式", "振幅",
                "站穩", "跌破", "觸發", "目標", "條件", "停損", "失效"]
SKIP_SECTIONS = ["情境分析", "執行框架", "盤中對應", "最終結論", "快速檢查表"]
NUM_RE = re.compile(r"\d[\d,]*(?:\.\d+)?%?")
FROM_PRIOR_RE = re.compile(r"由\s*[＋+－\-]?[\d,]")


def _keep(tok: str) -> bool:
    """2 位以下純整數（年份/時間/家數小數）跳過；但 5.8% 這類帶 % 小數保留；
    無 % 的微小小數（如 V3.0 的 3.0）跳過；8 碼日期跳過。"""
    core = tok.rstrip("%")
    digits = re.sub(r"[^0-9]", "", core)
    if re.fullmatch(r"\d{8}", core):
        return False
    if len(digits) <= 2 and not ("%" in tok and "." in core):
        return False
    return True


def _norm(tok: str):
    t = tok.replace(",", "").strip().rstrip("%").lstrip("+").strip()
    try:
        return ("f", float(t))
    except ValueError:
        return ("s", t)


def _tables_after(text: str, key: str):
    """回傳 key 標題行之後第一個連續 | 表格區塊（去掉分隔列；
    跳過標題與表格之間的空行/來源註記行）。"""
    lines = text.split("\n")
    out, hit, started = [], False, False
    for ln in lines:
        if not hit:
            if key in ln and ln.strip().startswith("#"):
                hit = True
            continue
        s = ln.strip()
        if s.startswith("|"):
            started = True
            if re.match(r"^\|[\s\-\:|]+\|$", s):
                continue
            out.append([c.strip() for c in s.strip("|").split("|")])
        elif s == "":
            if started:
                break
            continue
        else:
            if started:
                break
            continue
    return out


def _data_keyvals(rows):
    d = {}
    for r in rows:
        if r:
            d[str(r[0])] = str(r[1]) if len(r) > 1 else ""
    return d


def _interval(label: str) -> str:
    m = re.search(r"[（(]([^)）]*→[^)）]*)[）)]", str(label))
    return m.group(1) if m else ""


def _split_sec6(rtext: str):
    """以 '# 六' 標題為界切報告：前段（§5 前十大）／後段（§6 比較表/流向）。"""
    lines = rtext.split("\n")
    idx = next((i for i, ln in enumerate(lines)
                if ln.strip().startswith("# 六")), len(lines))
    return "\n".join(lines[:idx]), "\n".join(lines[idx:])


def token_audit(dtext: str, rtext: str):
    dkeys = set()
    for tok in NUM_RE.findall(dtext):
        if not _keep(tok):
            continue
        k = _norm(tok)
        dkeys.add(k)
        if k[0] == "f":
            dkeys.add(("f", float(int(k[1]))))
    errs = []
    in_skip = False
    for i, ln in enumerate(rtext.split("\n"), 1):
        s = ln.strip()
        if s.startswith("#"):
            in_skip = any(k in s for k in SKIP_SECTIONS)
            continue
        if not s or s.startswith("```") or s.startswith("|---") or \
                s.startswith("| ---") or s.startswith("---") or "http" in s:
            continue
        if in_skip:
            continue
        if any(w in s for w in EXEMPT_WORDS):
            continue
        if FROM_PRIOR_RE.search(s):
            continue
        for tok in NUM_RE.findall(s):
            if not _keep(tok):
                continue
            if _norm(tok) not in dkeys:
                errs.append((i, tok))
    return errs


def struct_t10(dtext: str, rtext: str):
    errs = []
    drows = _data_keyvals(_tables_after(dtext, "前十大交易人多空未平倉部位"))
    d_net = d_chg = d_iv = ""
    for k, v in drows.items():
        if "變化" in k:
            d_chg, d_iv = v, _interval(k)
        elif "淨" in k:
            d_net = v
    if not d_net:
        return ["DATA 缺前十大淨值"]
    pat = re.compile(r"^\|\s*(多空淨 OI 變化[^|]*|多方 OI|空方 OI|多空淨 OI)\|\s*([^|]+)\|")
    got = {}
    pre, _post = _split_sec6(rtext)
    for ln in pre.split("\n"):
        m = pat.match(ln.strip())
        if m:
            got[m.group(1)] = m.group(2).strip()
    exp = {"多方 OI": drows.get("前十大交易人多方 OI", ""),
           "空方 OI": drows.get("前十大交易人空方 OI", ""),
           "多空淨 OI": d_net}
    for k, v in exp.items():
        if k in got and _norm(got[k]) != _norm(v):
            errs.append(f"T10表 {k} 報告={got[k]} DATA={v}")
    for k in got:
        if "變化" in k:
            if _norm(got[k]) != _norm(d_chg):
                errs.append(f"T10表 變化 報告={got[k]} DATA={d_chg}")
            if _interval(k) != d_iv:
                errs.append(f"T10表 區間 報告={_interval(k)} DATA={d_iv}")
    for i, ln in enumerate(rtext.split("\n"), 1):
        if "前十大淨多" in ln and "變化" not in ln and "→" not in ln:
            m = re.search(r"前十大淨多[^\d＋+－\-]*([＋+－\-]?[\d,]+)", ln)
            if m and _norm(m.group(1)) != _norm(d_net):
                errs.append(f"L{i} 前十大敘述 {m.group(1)} DATA淨={d_net}")
    return errs


def struct_comps(dtext: str, rtext: str):
    errs = []
    dtabs = []
    lines = dtext.split("\n")
    hit = False
    cur = []
    for ln in lines:
        if not hit:
            if "選擇權前十大" in ln and ln.strip().startswith("#"):
                hit = True
            continue
        s = ln.strip()
        if s.startswith("|"):
            if re.match(r"^\|[\s\-\:|]+\|$", s):
                continue
            cur.append([c.strip() for c in s.strip("|").split("|")])
        elif s == "":
            if cur:
                dtabs.append(cur)
                cur = []
        else:
            if cur:
                dtabs.append(cur)
                cur = []
            if s.startswith("#"):
                break
    if cur:
        dtabs.append(cur)
    if len(dtabs) < 2:
        return ["DATA 缺選擇權前十大雙表"]
    buy, sell = _data_keyvals(dtabs[0]), _data_keyvals(dtabs[1])

    def pick(d, *keys):
        for kk in keys:
            for k, v in d.items():
                if kk in k and "變化" not in k:
                    return v
        return ""

    def pick_chg(d):
        for k, v in d.items():
            if "變化" in k:
                return v, _interval(k)
        return "", ""

    b_chg, b_iv = pick_chg(buy)
    s_chg, s_iv = pick_chg(sell)
    exp = {
        "多方 OI": (pick(buy, "多方"), pick(sell, "多方")),
        "空方 OI": (pick(buy, "空方"), pick(sell, "空方")),
        "多空淨 OI": (pick(buy, "淨"), pick(sell, "淨")),
        "多空淨 OI 變化": (b_chg, s_chg),
    }
    exp_iv = (b_iv, s_iv)
    rpat = re.compile(r"^\|\s*(多空淨 OI 變化|多方 OI|空方 OI|多空淨 OI)\s*([^|]*)\|\s*([^|]*)\|\s*([^|]*)\|")
    got = {}
    _pre, post = _split_sec6(rtext)
    for ln in post.split("\n"):
        m = rpat.match(ln.strip())
        if m and "買權" not in m.group(1):
            got[m.group(1).strip()] = (m.group(3).strip(), m.group(4).strip())
    for k, (eb, es) in exp.items():
        if k not in got:
            errs.append(f"比較表 缺{k}列")
            continue
        gb, gs = got[k]
        gbv = re.sub(r"（[^）]*）", "", gb).strip()
        gsv = re.sub(r"（[^）]*）", "", gs).strip()
        if _norm(gbv) != _norm(eb):
            errs.append(f"比較表 {k}-買權 報告={gbv} DATA={eb}")
        if _norm(gsv) != _norm(es):
            errs.append(f"比較表 {k}-賣權 報告={gsv} DATA={es}")
    if "多空淨 OI 變化" in got:
        gb, gs = got["多空淨 OI 變化"]
        if _interval(gb) != exp_iv[0]:
            errs.append(f"比較表 變化-買權區間 報告={_interval(gb)} DATA={exp_iv[0]}")
        if _interval(gs) != exp_iv[1]:
            errs.append(f"比較表 變化-賣權區間 報告={_interval(gs)} DATA={exp_iv[1]}")
    return errs


def struct_flow(dtext: str, rtext: str):
    errs = []
    drows = _data_keyvals(_tables_after(dtext, "大戶流向"))
    dmap = {}
    for k, v in drows.items():
        if "前十大" in k:
            dmap[k] = v
    rpat = re.compile(r"^\|\s*((?:期貨|買權|賣權)前十大)\s*\|\s*([^|]+)\|\s*([^|]+)\|")
    for ln in rtext.split("\n"):
        m = rpat.match(ln.strip())
        if not m:
            continue
        name, val, iv = m.group(1), m.group(2).strip(), m.group(3).strip()
        if name not in dmap:
            continue
        dval = dmap[name]
        dtab = _tables_after(dtext, "大戶流向")
        div = ""
        for r in dtab:
            if r and r[0] == name and len(r) > 2:
                div = r[2]
        if _norm(val) != _norm(dval):
            errs.append(f"流向 {name} 報告={val} DATA={dval}")
        if iv != div:
            errs.append(f"流向 {name}區間 報告={iv} DATA={div}")
    return errs


def ascii_only(s: str) -> str:
    return "".join(c if ord(c) < 128 else "?" for c in s)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--data", required=True)
    ap.add_argument("--report", required=True)
    args = ap.parse_args()
    with open(args.data, encoding="utf-8") as f:
        dtext = f.read()
    with open(args.report, encoding="utf-8") as f:
        rtext = f.read()
    sha = hashlib.sha256(dtext.encode("utf-8")).hexdigest()[:12]
    print(f"DATA_SHA={sha}")
    errs = []
    for i, tok in token_audit(dtext, rtext):
        ctx = ""
        for ln in rtext.split("\n"):
            if tok in ln:
                ctx = ascii_only(ln.strip()[:60])
                break
        errs.append(f"TOKEN L{i} [{tok}] :: {ctx}")
    for e in struct_t10(dtext, rtext):
        errs.append("STRUCT " + e)
    for e in struct_comps(dtext, rtext):
        errs.append("STRUCT " + e)
    for e in struct_flow(dtext, rtext):
        errs.append("STRUCT " + e)
    print(f"NUMCHECK_ERRORS={len(errs)}")
    for e in errs:
        print(e)
    return 1 if errs else 0


if __name__ == "__main__":
    raise SystemExit(main())
