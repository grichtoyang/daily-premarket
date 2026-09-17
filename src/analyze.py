"""分析層全自動：DATA_REPORT → Gemini API → Daily_REPORT + latest.json。

用法：
    GEMINI_API_KEY=xxx python src/analyze.py --date 2026-09-17 --t0 2026-09-16
    --t0 缺省取最近平日 (與 fetch_data 一致)

流程：組 prompt → 調 API (最多 3 次，含 1 次格式修正重試) → 結構校驗 →
      寫 reports/Daily_REPORT_yyyymmdd.md + reports/latest.json。
Key 只從環境變數讀，不進 repo。
"""
from __future__ import annotations
import argparse
import json
import os
import re
import sys
import time
from datetime import date, datetime
from pathlib import Path
from zoneinfo import ZoneInfo

import requests

ROOT = Path(__file__).resolve().parent.parent
TAIPEI = ZoneInfo("Asia/Taipei")
MODELS = ["gemini-2.5-flash", "gemini-2.0-flash"]
SECTIONS = ["關鍵數據一覽", "國際市場解讀", "台股籌碼解讀", "期貨選擇權解讀",
            "關鍵價位與今日交易計畫", "資料限制聲明"]
BLOCKS = ("kpi", "levels", "oidist", "scenarios")


def last_weekday(d: date) -> date:
    from datetime import timedelta
    d -= timedelta(days=1)
    while d.weekday() >= 5:
        d -= timedelta(days=1)
    return d


def call_gemini(prompt: str, key: str, timeout: int = 180) -> str | None:
    for model in MODELS:
        url = (f"https://generativelanguage.googleapis.com/v1beta/models/{model}"
               f":generateContent?key={key}")
        body = {"contents": [{"parts": [{"text": prompt}]}],
                "generationConfig": {"temperature": 0.3, "maxOutputTokens": 8192}}
        try:
            r = requests.post(url, json=body, timeout=timeout)
            if r.status_code == 404:
                continue
            r.raise_for_status()
            cands = r.json().get("candidates") or []
            if cands:
                parts = (cands[0].get("content") or {}).get("parts") or []
                text = "".join(p.get("text", "") for p in parts).strip()
                if text:
                    return text
        except Exception as e:  # noqa: BLE001
            print(f"[WARN] {model} failed: {e}")
            time.sleep(5)
    return None


def validate(text: str) -> list[str]:
    """回傳錯誤清單，空 = 通過。"""
    errs = []
    for s in SECTIONS:
        if s not in text:
            errs.append(f"缺章節：{s}")
    if "一句話結論" not in text:
        errs.append("缺一句話結論")
    for b in BLOCKS:
        m = re.search(rf"```{b}\n(.*?)```", text, re.S)
        if not m:
            errs.append(f"缺機器區：{b}")
            continue
        rows = [l for l in m.group(1).strip().splitlines() if l.strip()]
        if b == "oidist":
            calls = [r for r in rows if r.startswith("call|")]
            puts = [r for r in rows if r.startswith("put|")]
            if len(calls) < 5 or len(puts) < 5:
                errs.append(f"oidist 不足 (call {len(calls)}/put {len(puts)})")
        elif len(rows) < 2:
            errs.append(f"機器區過短：{b}")
    if not (800 <= len(text) <= 6000):
        errs.append(f"字數異常：{len(text)}")
    return errs


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--date", default="")
    ap.add_argument("--t0", default="")
    ap.add_argument("--prompt", default=str(ROOT / "prompts" / "analyze.md"))
    args = ap.parse_args()
    key = os.getenv("GEMINI_API_KEY", "")
    if not key:
        print("[ERROR] 缺少 GEMINI_API_KEY", file=sys.stderr)
        return 2
    today = datetime.now(TAIPEI).date()
    report_date = args.date.strip() or today.isoformat()
    t0 = args.t0.strip() or last_weekday(date.fromisoformat(report_date)).isoformat()
    ymd = t0.replace("-", "")

    data_path = ROOT / "data_reports" / f"DATA_REPORT_{ymd}.md"
    if not data_path.exists():
        print(f"[ERROR] 找不到 {data_path}", file=sys.stderr)
        return 2
    data_text = data_path.read_text(encoding="utf-8")
    template = Path(args.prompt).read_text(encoding="utf-8")
    base_prompt = (f"{template}\n\n---\n以下為 DATA_REPORT_{ymd}.md 全文 (T0={t0})：\n\n{data_text}")

    text, errs = None, ["not run"]
    for attempt in range(1, 4):
        prompt = base_prompt
        if attempt > 1:
            prompt += ("\n\n【格式修正】上一版未通過校驗："
                       + "；".join(errs) + "。請重出全文並修正。")
        print(f"[INFO] API attempt {attempt}")
        text = call_gemini(prompt, key)
        if text is None:
            errs = ["API 無回應"]
            continue
        errs = validate(text)
        if not errs:
            break
        print(f"[WARN] 校驗失敗：{errs}")
    if errs:
        print(f"[ERROR] 3 次皆未通過：{errs}", file=sys.stderr)
        return 1

    out = ROOT / "reports" / f"Daily_REPORT_{ymd}.md"
    out.write_text(text + "\n", encoding="utf-8")
    latest = {"report_date": ymd,
              "report_path": f"reports/Daily_REPORT_{ymd}.md",
              "generated_at": datetime.now(TAIPEI).isoformat(timespec="seconds"),
              "status": "completed"}
    (ROOT / "reports" / "latest.json").write_text(
        json.dumps(latest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"[OK] wrote {out} ({len(text)} 字)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
