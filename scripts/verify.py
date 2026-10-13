# -*- coding: utf-8 -*-
"""單輪驗證固定指令：numcheck（含 prior-audit）＋gate，一次輸出。

用法（repo 根目錄）：
    python scripts/verify.py --t0 20261012 --prev 20261008
    python scripts/verify.py --t0 20261012 --prev 20261008 --expect-sha abc123

--prev 缺省時跳過 prior-audit。--expect-sha 不符直接失敗
（DATA 中途被改寫就重跑 open，不在舊基準上修）。
結束碼：0 全過；1 有 ERROR。
"""
from __future__ import annotations

import argparse
import glob
import hashlib
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
sys.path.insert(0, str(ROOT))

import numcheck
from src.check_report import check as gate_check


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--t0", required=True, help="YYYYMMDD")
    ap.add_argument("--prev", default="", help="前一版 YYYYMMDD")
    ap.add_argument("--expect-sha", default="")
    args = ap.parse_args()
    dps = sorted((ROOT / "data_reports").glob(f"DATA_REPORT_{args.t0}.md"))
    rps = sorted((ROOT / "reports").glob(f"Daily_REPORT_{args.t0}_*.md"))
    if not dps or not rps:
        print(f"MISS files data={len(dps)} report={len(rps)}")
        return 2
    dp, rp = dps[-1], rps[-1]
    dtext = dp.read_text(encoding="utf-8")
    rtext = rp.read_text(encoding="utf-8")
    sha = hashlib.sha256(dtext.encode("utf-8")).hexdigest()[:12]
    print(f"DATA_SHA={sha}")
    if args.expect_sha and sha != args.expect_sha:
        print(f"SHA_MISMATCH expect={args.expect_sha} got={sha}："
              "DATA 被改寫，重跑 open 再驗")
        return 1
    errs: list[str] = []
    for i, tok in numcheck.token_audit(dtext, rtext):
        errs.append(f"TOKEN L{i} [{tok}]")
    for e in numcheck.struct_t10(dtext, rtext):
        errs.append("STRUCT " + e)
    for e in numcheck.struct_comps(dtext, rtext):
        errs.append("STRUCT " + e)
    for e in numcheck.struct_flow(dtext, rtext):
        errs.append("STRUCT " + e)
    if args.prev:
        pps = sorted((ROOT / "data_reports").glob(
            f"DATA_REPORT_{args.prev}.md"))
        if not pps:
            print(f"MISS prev DATA {args.prev}")
            return 2
        ptext = pps[-1].read_text(encoding="utf-8")
        for i, tok in numcheck.prior_audit(rtext, ptext, dtext):
            errs.append(f"PRIOR L{i} [{tok}]")
    print(f"NUMCHECK_ERRORS={len(errs)}")
    for e in errs:
        print(e)
    gerrs, gwarns = gate_check(dtext, rtext)
    for w in gwarns:
        print(f"GATE_WARN {w}"[:160])
    if gerrs:
        print(f"GATE_FAIL {len(gerrs)}")
        for e in gerrs:
            print(f"GATE {e}"[:200])
        return 1
    print("GATE_PASS")
    return 1 if errs else 0


if __name__ == "__main__":
    raise SystemExit(main())
