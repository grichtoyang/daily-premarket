# 每日喚醒 Prompt（每天早上貼給 OpenCode 執行，不用改日期）

開工，今天。
照 docs/SOP.md 全包：
1. 用 src/t0.py 判定 (T0、盤別 日盤/全日、是否休市)：檔名取自 T0。
2. git pull 取最新 DATA_REPORT_yyyymmdd.md。
3. 同 T0 文件已存在且完整就不重寫；否則依 docs/ANA_REPORT_TEMPLATE.md 手寫
   reports/Daily_REPORT_yyyymmdd_日盤.md 或 _全日.md
   （數字只出自 DATA，N/A 不臆測，附機器區 kpi/levels/oidist/scenarios/verdict）。
4. 更新 reports/latest.json（report_date/report_path/generated_at/status），指向最新一份。
5. 本地驗結構後 git add/commit/push。
完成後回報：T0＋盤別＋一句話結論＋關鍵價位＋push 的 commit＋Dashboard 更新時間。

定義（台指期全為準）：
- 日盤收盤當日 13:45；夜盤 15:00~隔日 05:00，歸屬開盤當日。
- 平日 13:45 前→T0＝前一交易日／全日；平日 13:45 後→T0＝今天／日盤；
  週末假日→T0＝往前最近交易日／全日（＋休市標示）。
- 交易日＝週一~五且非 TWSE 休市日曆休市日。

註：國定假日後第一天若 T0 對不上，我會先跟你確認再動工。
