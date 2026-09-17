# 每日喚醒 Prompt（每天早上貼給 OpenCode 執行，記得改 T0 日期）

開工，T0=yyyymmdd。
照 docs/SOP.md 全包：git pull 取最新 DATA_REPORT_yyyymmdd.md，
依 docs/ANA_REPORT_TEMPLATE.md 手寫 reports/Daily_REPORT_yyyymmdd.md
（數字只出自 DATA，N/A 不臆測，附機器區 kpi/levels/oidist/scenarios），
更新 reports/latest.json（report_date/report_path/generated_at/status），
本地驗結構後 git add/commit/push。
完成後回報：一句話結論＋關鍵價位＋push 的 commit＋Dashboard 更新時間。

註：yyyymmdd = 當日 T0（DATA 檔名那串數字，如 20260917）。
