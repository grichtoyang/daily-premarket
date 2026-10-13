# -*- coding: utf-8 -*-
"""開工固定指令：判定→pull→凍結→起草，一次輸出開工簡報。

用法（repo 根目錄）：
    python scripts/open.py --t0 20261012

取代臨時腳本 step1/frz/draft piecemeal，不在 repo 外留狀態。
"""
from __future__ import annotations

import argparse
import glob
import hashlib
import os
import runpy
import subprocess
import sys
import tempfile
from datetime import datetime, timedelta, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--t0", required=True, help="YYYYMMDD")
    args = ap.parse_args()
    now = datetime.now(timezone(timedelta(hours=8)))
    print("NOW=" + now.strftime("%Y-%m-%d %H:%M %A"))
    from src.t0 import resolve
    r = resolve()
    print("T0=" + str(r.get("t0")) + " SESSION=" + str(r.get("session"))
          + " HOL=" + str(r.get("today_holiday")))
    p = subprocess.run(["git", "pull"], capture_output=True, text=True,
                       cwd=ROOT)
    print("PULL=" + (p.stdout.strip() + p.stderr.strip())[-100:])
    dp = ROOT / "data_reports" / f"DATA_REPORT_{args.t0}.md"
    if not dp.exists():
        print("MISS_DATA=" + str(dp))
        return 2
    d = dp.read_text(encoding="utf-8")
    sha = hashlib.sha256(d.encode("utf-8")).hexdigest()[:12]
    print(f"DATA_SHA={sha}")
    un = [i + 1 for i, l in enumerate(d.split("\n")) if "unavailable" in l]
    print(f"UNAVAIL_LINES={un}")
    rps = sorted(glob.glob(str(ROOT / "reports" / f"Daily_REPORT_{args.t0}_*.md")))
    print("RPT=" + str([Path(x).name for x in rps]))
    sys.argv = ["draft", "--data", str(dp),
                "--out", str(Path(tempfile.gettempdir())
                              / f"draft_{args.t0}.md")]
    runpy.run_path(str(ROOT / "src" / "draft_blocks.py"),
                   run_name="__main__")
    print(f"NEXT=scripts/verify.py --t0 {args.t0} --expect-sha {sha}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
