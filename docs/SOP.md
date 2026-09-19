# 每日 SOP（半自動，V1 現行）

## 08:00 (無人)
GitHub Actions 自動抓資料 → commit `DATA_REPORT_yyyymmdd.md` → push。

## 早上 (用戶，10 秒)
叫醒 OpenCode：「今天 T0=yyyymmdd，開工」。

## OpenCode 全包 (約 3 分鐘)
1. `git pull` 取最新 DATA_REPORT。
2. 用 `src/t0.py` 判定 (T0、盤別 日盤/全日、是否休市)；同 T0 文件已存在且完整就不重寫。
3. 讀 DATA，依 `docs/ANA_REPORT_TEMPLATE.md` 手寫 `reports/Daily_REPORT_yyyymmdd_日盤.md`
   或 `_全日.md` (數字只出自 DATA，N/A 不臆測，附機器區 kpi/levels/oidist/scenarios/verdict)。
4. 更新 `reports/latest.json` 指向最新一份。
5. 本地驗結構 (validate PASS)。
6. `git add/commit/push` → Streamlit Cloud 1~2 分鐘自動更新 Dashboard。

## 用戶驗收 (手機)
開 Dashboard 網址：總結頁結論＋KPI＋交易計畫；要查數點 DATA 連結。
