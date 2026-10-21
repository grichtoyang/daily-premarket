# -*- coding: utf-8 -*-
"""薄殼彙總器：一條指令跑完 numcheck → check_report → verify（可選）。

用法（repo 根目錄）：
    python scripts/gate.py --t0 20261020
    python scripts/gate.py --t0 20261020 --prev 2026-10-19
    python scripts/gate.py --t0 20261020 --data data_reports/DATA_REPORT_20261020.md \
        --report reports/Daily_REPORT_20261020_盤前.md

本檔只做「呼叫＋抓結果＋印摘要」，不含任何驗證邏輯；純唯讀，不寫／不改任何檔案。
結束碼：0 = GATE_PASS；1 = GATE_FAIL；2 = 找不到報告／資料。
"""
from __future__ import annotations

import argparse
import os
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

NUM_ERR_RE = re.compile(r"NUMCHECK_ERRORS=(\d+)")
FAIL_CNT_RE = re.compile(r"\[FAIL\]\s*(\d+)")
GATE_PASS_RE = re.compile(r"GATE_PASS")

MAX_LINES = 25      # 總輸出上限
TAIL_LINES = 12     # 失敗時原樣印出的最後行數


def _run(argv: list[str]) -> subprocess.CompletedProcess:
    """以本支解譯器跑子檢查；強制 UTF-8 讀取，避免管線編碼炸掉。"""
    env = dict(os.environ)
    env["PYTHONIOENCODING"] = "utf-8"
    return subprocess.run(
        [sys.executable, *argv],
        cwd=str(ROOT),
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
        env=env,
    )


def _tail(res: subprocess.CompletedProcess, n: int = TAIL_LINES) -> list[str]:
    """取子檢查輸出最後 n 行（stdout 為主，stderr 附在後面）。"""
    text = res.stdout or ""
    if res.stderr:
        text = text + ("\n" if text and not text.endswith("\n") else "") + res.stderr
    lines = text.replace("\r\n", "\n").split("\n")
    while lines and lines[-1].strip() == "":
        lines.pop()
    return lines[-n:]


def _pick_report(t0: str) -> tuple[str, str]:
    """自動挑 reports/Daily_REPORT_<t0>_*.md，多個取 mtime 最新。

    回傳 (報告相對路徑, 挑選說明)；找不到回傳 ("", "")。
    """
    cand = list((ROOT / "reports").glob(f"Daily_REPORT_{t0}_*.md"))
    if not cand:
        return "", ""
    cand.sort(key=lambda p: p.stat().st_mtime)
    rel = cand[-1].relative_to(ROOT).as_posix()
    note = f"（mtime 最新，共 {len(cand)} 個候選）" if len(cand) > 1 else ""
    return rel, note


def _check_rows(args: argparse.Namespace, data: str, report: str):
    """依序跑檢查，回傳 [(標籤行, 是否通過, CompletedProcess)]。"""
    total = 3 if args.prev else 2
    rows: list[tuple[str, bool, subprocess.CompletedProcess]] = []

    # 1) numcheck：token 稽核（錯誤數以 NUMCHECK_ERRORS= 為準）
    r1 = _run(["scripts/numcheck.py", "--data", data, "--report", report])
    m1 = NUM_ERR_RE.search(r1.stdout or "")
    n1 = m1.group(1) if m1 else "?"
    ok1 = r1.returncode == 0 and n1 == "0"
    rows.append((f"[1/{total}] numcheck RC={r1.returncode} "
                 f"NUMCHECK_ERRORS={n1}", ok1, r1))

    # 2) check_report：結構／機器閘（數 [FAIL]／[WARN]）
    r2 = _run(["src/check_report.py", "--data", data, "--report", report])
    out2 = r2.stdout or ""
    m2 = FAIL_CNT_RE.search(out2)
    fails = int(m2.group(1)) if m2 else out2.count("[FAIL]")
    warns = out2.count("[WARN]")
    ok2 = r2.returncode == 0 and fails == 0
    rows.append((f"[2/{total}] check_report RC={r2.returncode} "
                 f"FAILS={fails} WARNS={warns}", ok2, r2))

    # 3) verify：numcheck＋prior-audit＋gate 一次跑（有 --prev 才跑）
    if args.prev:
        r3 = _run(["scripts/verify.py", "--t0", args.t0, "--prev", args.prev])
        out3 = r3.stdout or ""
        m3 = NUM_ERR_RE.search(out3)
        n3 = m3.group(1) if m3 else "?"
        gate_ok = bool(GATE_PASS_RE.search(out3))
        ok3 = r3.returncode == 0 and gate_ok and n3 == "0"
        rows.append((f"[3/{total}] verify RC={r3.returncode} "
                     f"{'GATE_PASS' if gate_ok else 'GATE_FAIL'} "
                     f"NUMCHECK_ERRORS={n3}", ok3, r3))

    return rows


def main() -> int:
    ap = argparse.ArgumentParser(description="numcheck／check_report／verify 一次跑")
    ap.add_argument("--t0", required=True, help="YYYYMMDD")
    ap.add_argument("--prev", default="", help="前一交易日（YYYY-MM-DD 或 YYYYMMDD），給了才跑 verify")
    ap.add_argument("--data", default="", help="預設 data_reports/DATA_REPORT_<t0>.md")
    ap.add_argument("--report", default="", help="預設自動找 reports/Daily_REPORT_<t0>_*.md")
    args = ap.parse_args()
    args.prev = args.prev.replace("-", "").strip()

    report = args.report
    head: list[str] = []
    if not report:
        picked, note = _pick_report(args.t0)
        if not picked:
            print("NO_REPORT")
            return 2
        report = picked
        head.append(f"REPORT={picked}{note}")

    data = args.data or f"data_reports/DATA_REPORT_{args.t0}.md"
    if not (ROOT / data).is_file():
        print("NO_DATA")
        return 2

    rows = _check_rows(args, data, report)
    all_ok = all(ok for _, ok, _ in rows)

    # 組輸出：標頭＋各檢查摘要；失敗者附尾段（總行數壓在 25 行內）
    out: list[str] = list(head)
    dumps: list[list[str]] = []
    for label, ok, res in rows:
        out.append(label)
        if not ok:
            dumps.append(_tail(res))

    budget = MAX_LINES - len(out) - 1  # 留一行給 GATE_PASS／GATE_FAIL
    merged: list[str] = []
    for d in dumps:
        merged.extend(d)
    if budget < 0:
        budget = 0
    if len(merged) > budget:
        merged = merged[len(merged) - budget:] if budget else []

    for ln in merged:
        out.append(ln)
    out.append("GATE_PASS" if all_ok else "GATE_FAIL")
    print("\n".join(out))
    return 0 if all_ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
