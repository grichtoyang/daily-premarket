# 每日 SOP（半自動，V1 現行）

## 08:00 (無人)
GitHub Actions 自動抓資料 → commit `DATA_REPORT_yyyymmdd.md` → push。

## 早上 (用戶，10 秒)
貼 `prompts/daily_starter.md` 內容給 OpenCode，加一句「今天 T0=yyyymmdd，開工」。舊模型版存檔：`prompts/daily_starter_MiMo.md`（不再使用）。

## OpenCode 全包 (約 3 分鐘)
1. `git pull` 取最新 DATA_REPORT。
2. 用 `src/t0.py` 判定 (T0、盤別 日盤/全日、是否休市)；同 T0 文件已存在且完整就不重寫。
3. 讀 DATA，依 `docs/ANA_REPORT_TEMPLATE.md` 手寫 `reports/Daily_REPORT_yyyymmdd_日盤.md`
   或 `_全日.md` (數字只出自 DATA，N/A 不臆測，附機器區 kpi/levels/oidist/scenarios/verdict)。
   （寫作照 3.6 分段協定；驗收指令限 3.7 白名單；交付前過 3.8 清單。）
3.5 最後救援（固定慣例）：掃 DATA「未取得欄位」，逐一驗實際來源（重跑對應 `src/sources/` 函數或直查源站）；
   有值→先補登進 DATA（標「補登＋來源日期＋來源」）再寫進報告，維持「報告數字⊆DATA」；
   無值→報告寫 unavailable＋§11 揭露（前例：0924 維持率補登、夜盤節次更正）。
4. 更新 `reports/latest.json` 指向最新一份。
5. 本地驗結構 (validate PASS)。
6. `git add/commit/push` → Streamlit Cloud 1~2 分鐘自動更新 Dashboard。

## 3.6 分析層「分段寫作協定」（C1，2026-10-17 定案）
2026-10-17 實證：單次 8,000~13,000 字生成，免費 flash 模型連續空回 2 次；拆 4 段後 4/4 成功。
- 固定 4 段：(1) 首行＋§一＋§二、(2) §三＋§四＋§五、(3) §六＋§七、
  (4) §八＋§九＋§十＋§十一＋§十二＋附錄A＋附錄B（附錄B 機器可讀區塊最後貼）。
- 每段一個 worker 任務；只准 Edit 追加（取檔尾最後一行當錨點），禁止整檔重寫；
  每段落地後立刻可被檢查（檔案必須存在）。
- worker 禁跑任何檢查指令；numcheck／verify／gate 一律由 supervisor 在全部段落完成後執行。
- 修正上限 2 次，且只准 patch 出錯的那幾行；第 3 次失敗 → 停手回報原始輸出，不得繼續嘗試。
  （此上限指 worker 修段落的次數；全部段落完成後 supervisor 的 numcheck 修復迴圈仍修到零為止，兩者層級不同）
- 全段落完成後：numcheck（必帶 `--data`）→ 修正 → 更新 `latest.json` → `verify.py`。

## 3.7 驗收指令白名單＋派工前先驗（C2，2026-10-17 定案）
2026-10-17 實證：派工令寫錯指令 → worker 空轉 30 分鐘。
- 只有這三條可作為驗收：
  1. `python scripts/numcheck.py --data data_reports/DATA_REPORT_<T0>.md --report reports/Daily_REPORT_<T0>_<盤別>.md`（必帶 `--data`）
  2. `python scripts/verify.py --t0 <T0> --prev <prev> [--expect-sha <sha12>]`（權威、含 numcheck＋prior-audit＋gate）
  3. `python src/check_report.py --data data_reports/DATA_REPORT_<T0>.md --report reports/Daily_REPORT_<T0>_<盤別>.md`（gate 本體；注意在 `src/` 不是 `scripts/`；參數同 numcheck）
- supervisor 派工前必須先在「前一份已知良好報告」上實跑一次該指令，確認可執行，才寫進派工令。
- 派工令必含：目的／精確目標檔／驗收方式／不可動範圍／停手上限／回報格式。

## 3.8 交付前檢查清單（C3，2026-10-17 定案；實測抓到 2 個瑕疵）
- 附錄B：`kpi` 14 筆順序正確、`verdict` 方向/信心非空、`levels` 的 `白話` 非空且數字只用 DATA 既有價位。
- `levels` 支撐由近到遠（支撐＝較近、支撐二＝較遠），與前一份報告慣例一致。
- 首行 `- 報告日期：` ＝產出日（T0+1）；`- 資料基準：` 指向同一 T0 的 DATA。
- `reports/latest.json` 四欄齊全、`report_date`＝T0、`status=completed`。
- 交付前：`git status --porcelain` 只應出現本次預期的檔案；commit 後：`git status --porcelain` 應為空。未經批准不得 commit／push（worker／修復情境；日常全包流程仍依上方第 6 步）。

## 修復原則（2026-10-14 定案）

1. 小洞走人工：貼來源 URL＋人工讀數＋補登一行進 DATA（值＋來源＋日期，閘門只認 DATA）；不為小洞加新程式。
2. 大洞（整批抓不到）才動工具。
3. 遇到問題先找最容易的解法，不要硬修；功能凍結，只修不加。

## 用戶驗收 (手機)
開 Dashboard 網址：總結頁結論＋KPI＋交易計畫；要查數點 DATA 連結。
