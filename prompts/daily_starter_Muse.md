# 每日喚醒 Prompt（每天早上貼給 OpenCode 執行，不用改日期）

我的角色是專業的分析師與工程師
開工，今天。
照 docs/SOP.md 全包：
1. 用 src/t0.py 判定 (T0、盤別 日盤/全日、是否休市)：檔名取自 T0。
2. git pull 取最新 DATA_REPORT_yyyymmdd.md。
3. 同 T0 文件已存在且完整就不重寫；否則依 docs/ANA_REPORT_TEMPLATE.md 手寫
   reports/Daily_REPORT_yyyymmdd_日盤.md 或 _全日.md
   （數字只出自 DATA，N/A 不臆測，附機器區 kpi/levels/oidist/scenarios/verdict；
   DATA 有 unavailable 先做最後救援：驗源站→有值先補登 DATA 再寫報告，詳 docs/SOP.md 3.5）。

4. 更新 reports/latest.json（report_date/report_path/generated_at/status），指向最新一份。
5. 先跑數字稽核 `python scripts/numcheck.py --data data_reports/DATA_REPORT_yyyymmdd.md --report reports/Daily_REPORT_yyyymmdd_日盤.md`（檔名按盤別），[ERROR] 就地修到零為止；再跑閘門 `python src/check_report.py`（同參數），[PASS] 才可 git add/commit/push；[FAIL] 就地修到過為止。
6. 開工鐵律（2026-10-07 起，避免手填數字錯誤重演）：
   - 先記 DATA sha256（numcheck 首行 DATA_SHA）；寫報告途中若 DATA 被改寫（sha 變了），以新 DATA 為準重對一次。
   - 表格數字一律從 `python src/draft_blocks.py --data ... --out ...` 的輸出貼上：kpi/oidist/Top3/Top10全表/OI增減/VIX/§5.5前十大/§6.4比較表/§6.2流向（含區間與資料日期）照貼不手改（§6.4 全表整張貼，不手排）；只手寫解讀、verdict 理由、levels 白話、scenarios 條件。
   - 驗證只做單輪：numcheck 一次列出全部問題→一次修完→重跑確認零 ERROR→gate。若稽核輸出與已驗證狀態矛盾，先重跑該檢查，不連坐推翻之前結論。
完成後回報：T0＋盤別＋一句話結論＋關鍵價位＋push 的 commit＋Dashboard 更新時間。

定義（台指期全為準）：
- 日盤收盤當日 13:45；夜盤 15:00~隔日 05:00，歸屬開盤當日。
- 平日 13:45 前→T0＝前一交易日／全日；平日 13:45 後→T0＝今天／日盤；
  週末假日→T0＝往前最近交易日／全日（＋休市標示）。
- 交易日＝週一~五且非 TWSE 休市日曆休市日。

註：國定假日後第一天若 T0 對不上，我會先跟你確認再動工。
