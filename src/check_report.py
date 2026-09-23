"""Daily_REPORT 發布前閘門：數字稽核＋V3.0 結構＋附錄B 機器區。

用法：
    python src/check_report.py --data data_reports/DATA_REPORT_20260922.md \
        --report reports/Daily_REPORT_20260922_日盤.md

結束碼 0=通過；1=失敗（列出所有錯誤）。警告不影響結束碼。
規則來源：docs/ANA_REPORT_TEMPLATE.md V3.0。
"""
from __future__ import annotations
import argparse
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

# 數字稽核：錨點法。V3.0 報告含大量衍生百分比，逐數精確比對誤殺太多；
# 改抽 DATA 關鍵錨點（指數收盤、ADR、法人、Walls 等），報告內必須出現（正規化比對）。
# MiMo 式幻覺（S&P 6996 vs 7764）必在此被攔下。
_FW = str.maketrans({"＋": "+", "－": "-", "％": "%", "，": ",", "｜": "|"})


def _norm_num(s: str) -> str:
    s = s.translate(_FW).replace(",", "").replace(" ", "")
    if "." in s:
        s = s.rstrip("0").rstrip(".")
    return s.lstrip("+")


def _anchor_row(data: str, label: str) -> str | None:
    m = re.search(rf"\|\s*{re.escape(label)}\s*\|[^|]*\|\s*([+-]?[\d,]+(?:\.\d+)?)",
                  data)
    return _norm_num(m.group(1)) if m else None


def data_anchors(data: str) -> list[tuple[str, str]]:
    out: list[tuple[str, str]] = []
    simple = ["加權指數價格", "融資維持率", "S&P 500", "Dow Jones",
              "Nasdaq Composite", "Nasdaq 100", "費城半導體 SOX", "VIX",
              "台積電ADR", "Call Wall 價位", "Put Wall 價位",
              "Gamma Wall 價位", "Max Pain 價位"]
    for lb in simple:
        v = _anchor_row(data, lb)
        if v is not None:
            out.append((lb, v))
    m = re.search(r"\|\s*外資\s*\|\s*([+-]?[\d,]+\.\d+)", data)
    if m:
        out.append(("外資現貨買賣超", _norm_num(m.group(1))))
    for sec, lb in (("日盤行情", "台指日盤收"), ("夜盤行情", "台指夜盤收")):
        ms = re.search(sec, data)
        if ms:
            m2 = re.search(r"收盤價\s*\|\s*([+-]?[\d,]+(?:\.\d+)?)",
                           data[ms.end():ms.end() + 2000])
            if m2:
                out.append((lb, _norm_num(m2.group(1))))
    return out

CHAPTERS = ["一、", "二、", "三、", "四、", "五、", "六、",
            "七、", "八、", "九、", "十、", "十一、", "十二、"]
KPI_ORDER = ["加權收盤", "台指夜盤成交量占比", "外資現貨", "外資期貨淨OI", "費半",
             "Call Wall", "Gamma Wall", "台指期收盤", "台指夜盤漲跌", "投信現貨",
             "外資夜盤淨", "台積電ADR", "Put Wall", "VIX"]


def _block(text: str, name: str) -> list[str]:
    m = re.search(rf"```{name}\n(.*?)```", text, re.S)
    if not m:
        return []
    return [l.strip() for l in m.group(1).strip().splitlines() if l.strip()]


def check(data: str, report: str) -> tuple[list[str], list[str]]:
    errs, warns = [], []

    # 1. 錨點稽核：DATA 關鍵數必須在報告出現
    rnorm = _norm_num(report)
    missing = [(lb, v) for lb, v in data_anchors(data) if v not in rnorm]
    if missing:
        errs.append("錨點數缺失（疑似虛構/抄錯）: " +
                    "；".join(f"{lb}={v}" for lb, v in missing[:12]))

    # 2. V3.0 章節（一〜十二＋附錄A/B）
    for c in CHAPTERS:
        if f"# {c}" not in report:
            errs.append(f"缺章節：# {c}")
    if "附錄A" not in report:
        errs.append("缺附錄A：盤中快速檢查表")
    if "附錄B" not in report:
        errs.append("缺附錄B：機器可讀數據")

    # 3. 附錄B 機器區
    kpi = _block(report, "kpi")
    if len(kpi) != 14:
        errs.append(f"kpi 須 14 筆，實得 {len(kpi)} 筆")
    else:
        names = [r.split("|")[0].strip() for r in kpi]
        if names != KPI_ORDER:
            errs.append(f"kpi 順序不符：{names}")
        for r in kpi:
            if len(r.split("|")) < 2:
                errs.append(f"kpi 格式錯誤：{r}")
    verdict = _block(report, "verdict")
    for k in ("方向", "信心", "理由1", "理由2", "理由3", "注意"):
        if not any(r.startswith(k + "|") or r.startswith(k + "：") for r in verdict):
            errs.append(f"verdict 缺鍵：{k}")
    levels = _block(report, "levels")
    for k in ("壓力", "壓力二", "中軸", "支撐", "支撐二", "白話"):
        if not any(r.startswith(k + "|") or r.startswith(k + "：") for r in levels):
            errs.append(f"levels 缺鍵：{k}")
    oid = _block(report, "oidist")
    nc = sum(1 for r in oid if r.startswith("call|"))
    np_ = sum(1 for r in oid if r.startswith("put|"))
    if nc < 5 or np_ < 5:
        errs.append(f"oidist 不足 (call {nc}/put {np_}，需各>=5)")
    # oidist 每筆履約價+OI 必須能在 DATA 同一行找到（防抄錯到期月份；
    # 2026-09-23 日盤曾誤貼整段 Put 分布而閘門放行，特加此條）
    dlines = [_norm_num(l) for l in data.splitlines()]
    bad_oid = []
    for r in oid:
        p = [c.strip() for c in r.split("|")]
        if len(p) < 3 or p[0] not in ("call", "put"):
            continue
        sk, oi = _norm_num(p[1]), _norm_num(p[2])
        if not sk.replace(".", "").isdigit() or not oi.replace(".", "").isdigit():
            continue
        if not any(sk in dl and oi in dl for dl in dlines):
            bad_oid.append(f"{p[0]}|{p[1]}|{p[2]}")
    if bad_oid:
        errs.append("oidist 數字在 DATA 找不到（疑似抄錯列/錯月份）: " +
                    "; ".join(bad_oid[:10]))
    scen = _block(report, "scenarios")
    if len(scen) < 2:
        errs.append(f"scenarios 過少 ({len(scen)} 列，需>=2)")

    # 4. 字數（正文 2500~4500，不含附錄；僅警告，表格多時易超）
    body = report.split("附錄A")[0] if "附錄A" in report else report
    n = len(re.sub(r"\s", "", body))
    if not (2000 <= n <= 6000):
        warns.append(f"正文字數 {n}（模板 2500~4500，供參考）")

    # 5. 整數千分位抽查（警告性：DATA 沒有的整數可能是臆測或衍生目標價，人工複核）
    def itoks(s: str) -> set[str]:
        return {m.group(0).translate(_FW).replace(",", "").lstrip("+-")
                for m in re.finditer(r"[+-]?[\d,，]{2,}", s)
                if "," in m.group(0) or "，" in m.group(0)}
    missing_ints = sorted(t for t in itoks(report) if t not in itoks(data))
    # 排除年/月日/檔號常見雜訊：4 位年份、8 位日期
    missing_ints = [t for t in missing_ints
                    if not (len(t) == 4 and t.startswith("20"))
                    and len(t.lstrip("+-")) != 8]
    if missing_ints:
        warns.append(f"DATA 無此整數（人工複核是否為衍生/目標價）：{missing_ints[:12]}")

    return errs, warns


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--data", required=True)
    ap.add_argument("--report", required=True)
    args = ap.parse_args()
    data = Path(args.data).read_text(encoding="utf-8")
    report = Path(args.report).read_text(encoding="utf-8")
    errs, warns = check(data, report)
    for w in warns:
        print(f"[WARN] {w}")
    if errs:
        print(f"[FAIL] {len(errs)} 項未通過：")
        for e in errs:
            print(f"  - {e}")
        return 1
    print("[PASS] 數字稽核＋結構＋機器區全通過")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
