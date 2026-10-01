# -*- coding: utf-8 -*-
"""本機排程入口 (Windows 工作排程器 DailyPremarket0800, 每日 07:55)。

流程: src/fetch_data.py (cwd=repo 根目錄) → git pull --ff-only →
git add/commit/push。commit 訊息沿用 T0 命名 (與 CI 一致)。
全部輸出追加至 logs/fetch.log。故意比 Actions 08:00 早 5 分鐘，
錯開推送衝突；本機住宅 IP 為主力，Actions 為備援。
"""
from __future__ import annotations

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
    LOG.parent.mkdir(exist_ok=True)
    git = shutil.which("git")
    with open(LOG, "a", encoding="utf-8") as fp:
        _log(fp, "===== local fetch start =====")
        if not git:
            _log(fp, "ERROR: git not found on PATH")
            return 2
        if _sh(fp, sys.executable, "src/fetch_data.py") != 0:
            _log(fp, "fetch FAILED, abort before git")
            return 2
        if _sh(fp, git, "pull", "--ff-only", timeout=300) != 0:
            _log(fp, "pull --ff-only FAILED, abort (avoid divergence)")
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
        if _sh(fp, git, "push", timeout=600) != 0:
            _log(fp, "git push FAILED")
            return 2
        _log(fp, "===== local fetch done =====")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
