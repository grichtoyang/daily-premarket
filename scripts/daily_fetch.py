# -*- coding: utf-8 -*-
"""全量抓取＋推送（已封存排程入口，2026-10-14 定案）。

現況：Windows 工作排程器 DailyPremarket0800 已刪除；日常資料主抓為
GitHub Actions，本機只走 gapfill 補洞（見 scripts/gapfill.py）。
本檔僅保留給 `scripts/open.py` 在 DATA 完全缺失時的 NO_DATA 全量路徑，
或人工明確執行。直接裸執行一律拒絕（防舊排程命令復活造成雙寫手）。

流程: src/fetch_data.py (cwd=repo 根目錄，盤別/T0 一律顯式傳參，不看牆鐘)
→ git pull --rebase → git add/commit/push（push 失敗重試 3 次；rebase 衝突不自動解）。
commit 訊息沿用 T0 命名 (與 CI 一致)。
全部輸出追加至 logs/fetch.log。
"""
from __future__ import annotations

import argparse
import shutil
import subprocess
import sys
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo

ROOT = Path(__file__).resolve().parent.parent
LOG = ROOT / "logs" / "fetch.log"
TAIPEI = ZoneInfo("Asia/Taipei")


def _log(fp, msg: str) -> None:
    line = f"[{datetime.now(TAIPEI).isoformat(timespec='seconds')}] {msg}"
    print(line, flush=True)
    fp.write(line + "\n")
    fp.flush()


def _sh(fp, *args: str, timeout: int = 1500) -> int:
    fp.write("$ " + " ".join(args) + "\n")
    fp.flush()
    try:
        p = subprocess.run(
            list(args), cwd=ROOT, stdout=fp, stderr=subprocess.STDOUT,
            timeout=timeout,
        )
        return p.returncode
    except subprocess.TimeoutExpired:
        fp.write("TIMEOUT after %ds\n" % timeout)
        fp.flush()
        return 3


def main() -> int:
    ap = argparse.ArgumentParser(description="全量抓取（僅 open.py 缺 DATA 時或人工明確呼叫）")
    ap.add_argument("--from-open", action="store_true",
                    help="由 scripts/open.py NO_DATA 路徑呼叫")
    ap.add_argument("--manual", action="store_true",
                    help="人工明確執行（已知會全量抓取＋推送）")
    ap.add_argument("--slot", default="", choices=["morning", "evening", "weekend"],
                    help="排定班別（釘死盤別/T0；需搭配 --date）")
    ap.add_argument("--date", default="", help="排定日期 YYYY-MM-DD（同 fetch_data --date）")
    ap.add_argument("--t0", default="", help="手動覆寫 T0（供 SOP 3.5 補登）")
    ap.add_argument("--session", default="", choices=["日盤", "全日"], help="手動覆寫盤別")
    args = ap.parse_args()
    if not (args.from_open or args.manual):
        print("REFUSE: 本機排程已取消（2026-10-14），裸執行拒絕；"
              "如確需全量抓取，請加 --manual（人工）或走 open.py（自動）。")
        return 2
    if not args.slot.strip() and not (args.t0.strip() and args.session.strip()):
        print("REFUSE: 需顯式盤別（--slot＋--date，或 --t0＋--session），不依牆鐘判定。")
        return 2
    LOG.parent.mkdir(exist_ok=True)
    git = shutil.which("git")
    with open(LOG, "a", encoding="utf-8") as fp:
        _log(fp, "===== local fetch start =====")
        if not git:
            _log(fp, "ERROR: git not found on PATH")
            return 2
        _fargs = [sys.executable, "src/fetch_data.py"]
        if args.slot.strip():
            if not args.date.strip():
                _log(fp, "ERROR: --slot 需搭配 --date")
                return 2
            _fargs += ["--slot", args.slot.strip(), "--date", args.date.strip()]
        elif args.date.strip():
            _fargs += ["--date", args.date.strip()]
        if args.t0.strip():
            _fargs += ["--t0", args.t0.strip()]
        if args.session.strip():
            _fargs += ["--session", args.session.strip()]
        if _sh(fp, *_fargs) != 0:
            _log(fp, "fetch FAILED, abort before git")
            return 2
        if _sh(fp, git, "pull", "--rebase", timeout=300) != 0:
            _log(fp, "pull --rebase FAILED（有分歧請人工解，不自動合併），abort")
            return 2
        if _sh(fp, git, "add", "data_reports", timeout=120) != 0:
            _log(fp, "git add FAILED")
            return 2
        files = sorted((ROOT / "data_reports").glob("DATA_REPORT_*.md"))
        t0 = files[-1].stem.replace("DATA_REPORT_", "") if files else "unknown"
        chk = subprocess.run([git, "diff", "--staged", "--quiet"], cwd=ROOT)
        if chk.returncode != 0:
            if _sh(fp, git, "commit", "-m", f"chore(data): DATA_REPORT_{t0}",
                   timeout=300) != 0:
                _log(fp, "git commit FAILED")
                return 2
        else:
            _log(fp, "no changes, skip commit")
        _pushed = False
        for _try in range(3):
            if _sh(fp, git, "push", timeout=600) == 0:
                _pushed = True
                break
            _log(fp, f"push retry {_try + 1}/3：先 rebase 再推")
            if _sh(fp, git, "pull", "--rebase", timeout=300) != 0:
                break
        if not _pushed:
            _log(fp, "git push FAILED after retries")
            return 2
        _log(fp, "===== local fetch done =====")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
