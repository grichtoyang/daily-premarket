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
MODELS = ["gemini-2.5-flash", "gemini-2.0-flash", "gemini-2.0-flash-001", "gemini-flash-latest"]


def list_models(key: str, timeout: int = 30) -> list[str]:
    """問 API 有哪些模型可用，回傳 flash 系候選（新優先）。"""
    try:
        r = requests.get("https://generativelanguage.googleapis.com/v1beta/models",
                         params={"key": key}, timeout=timeout)
        if r.status_code != 200:
            print(f"[WARN] list models HTTP {r.status_code}")
            return []
        names = []
        for m in r.json().get("models") or []:
            name = str(m.get("name", "")).replace("models/", "")
            methods = m.get("supportedGenerationMethods") or []
            if "generateContent" in methods and "flash" in name.lower():
                names.append(name)
        names.sort(reverse=True)
        print(f"[INFO] 可用 flash 模型：{names}")
        return names
    except Exception as e:  # noqa: BLE001
        print(f"[WARN] list models failed: {e}")
        return []
SAFETY = [{"category": c, "threshold": "BLOCK_ONLY_HIGH"}
          for c in ("HARM_CATEGORY_HARASSMENT", "HARM_CATEGORY_HATE_SPEECH",
                    "HARM_CATEGORY_SEXUALLY_EXPLICIT", "HARM_CATEGORY_DANGEROUS_CONTENT")]
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
    found = list_models(key)
    models = found + [m for m in MODELS if m not in found]
    for model in models:
        url = (f"https://generativelanguage.googleapis.com/v1beta/models/{model}"
               f":generateContent?key={key}")
        body = {"contents": [{"parts": [{"text": prompt}]}],
                "safetySettings": SAFETY,
                "generationConfig": {"temperature": 0.3, "maxOutputTokens": 8192}}
        try:
            r = requests.post(url, json=body, timeout=timeout)
            if r.status_code == 404:
                print(f"[INFO] {model} 404 (model not found)")
                continue
            if r.status_code != 200:
                print(f"[WARN] {model} HTTP {r.status_code}: {r.text[:300]}")
                time.sleep(20 if r.status_code in (503, 429) else 5)
                continue
            j = r.json()
            fb = (j.get("promptFeedback") or {}).get("blockReason")
            if fb:
                print(f"[WARN] {model} blocked: {fb}")
                return None
            cands = j.get("candidates") or []
            if cands:
                parts = (cands[0].get("content") or {}).get("parts") or []
                text = "".join(p.get("text", "") for p in parts).strip()
                if text:
                    return text
                print(f"[WARN] {model} 空回應 (finish={cands[0].get('finishReason')})")
            else:
                print(f"[WARN] {model} 無 candidates: {str(j)[:300]}")
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


def audit_numbers(text: str, data: str) -> list[str]:
    """數字稽核：報告中的千分位數/百分比/小數必須能在 DATA 找到 (正規化比對)。
    回傳不匹配清單 (容忍 1 個)。"""
    def toks(s: str) -> set[str]:
        out = set()
        for m in re.finditer(r"[+-]?[\d,]+\.\d+[%％]?", s):
            out.add(m.group(0).replace(",", "").replace("％", "%").lstrip("+"))
        return out
    dt = toks(data)
    bad = sorted(t for t in toks(text) if t not in dt)
    return bad[1:] and [f"疑似虛構數字：{bad}"] or []


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
            errs = audit_numbers(text, data_text)
            if errs:
                print(f"[WARN] 數字稽核：{errs}")
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
