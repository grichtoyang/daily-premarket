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
   （長文分 4 段寫作照下方第 7 條；驗收指令白名單見第 8 條。）

4. 更新 reports/latest.json（report_date/report_path/generated_at/status），指向最新一份。
5. 先跑數字稽核 `python scripts/numcheck.py --data data_reports/DATA_REPORT_yyyymmdd.md --report reports/Daily_REPORT_yyyymmdd_日盤.md`（檔名按盤別），[ERROR] 就地修到零為止；再跑閘門 `python src/check_report.py`（同參數），[PASS] 才可 git add/commit/push；[FAIL] 就地修到過為止。
6. 開工鐵律（2026-10-07 起，避免手填數字錯誤重演）：
   - 先記 DATA sha256（numcheck 首行 DATA_SHA）；寫報告途中若 DATA 被改寫（sha 變了），以新 DATA 為準重對一次。
   - 表格數字一律從起草機輸出貼上：kpi/oidist/Top3/Top10全表/OI增減/VIX/§5.5前十大/§6.4比較表/§6.2流向/§4事件清單/預填verdict/levels/scenarios/關鍵數字速查（含區間與資料日期）照貼不手改（§6.4 全表整張貼，不手排；§4 只寫清單內事件，數字抄摘要原文，不憑記憶加；§4.1/§4.2每條須對應DATA事件號，逐條比對_news_list；verdict/levels/scenarios 只改字不改數；敘述行數字只准從速查表複貼）；只手寫解讀、verdict 理由取捨、levels 白話、scenarios 條件。
   - 貼之前先對錨：draft 首行加權收盤必須等於 DATA §1 收盤（防貼到舊版起草或憑記憶填數；2026-10-16 教訓：力道合計夜半列＋舊新聞殘留，verify 首輪抓 5 處）。
   - 驗證只做單輪：numcheck 一次列出全部問題→一次修完→重跑確認零 ERROR→gate。若稽核輸出與已驗證狀態矛盾，先重跑該檢查，不連坐推翻之前結論。
7. 分段寫作協定（C1，2026-10-17 定案；實證：單次 8,000~13,000 字生成，免費 flash 模型連續空回 2 次，拆 4 段後 4/4 成功）：
   - 2026-10-21 修正：上限放寬至 20,000（不含附錄），且**不得為字數重寫或壓縮**（見 `prompts/report_dispatch.md` 第 5 條）；字數僅供觀測。
   - 固定 4 段：(1) 首行＋§一＋§二、(2) §三＋§四＋§五、(3) §六＋§七、(4) §八＋§九＋§十＋§十一＋§十二＋附錄A＋附錄B（附錄B 機器可讀區塊最後貼）。
   - 每段一個 worker 任務；只准 Edit 追加（取檔尾最後一行當錨點），禁止整檔重寫；每段落地後立刻可被檢查（檔案必須存在）。
   - worker 禁跑任何檢查指令；numcheck／verify／gate 一律由 supervisor 在全部段落完成後執行。
   - 修正上限 2 次，且只准 patch 出錯的那幾行；第 3 次失敗 → 停手回報原始輸出，不得繼續嘗試。
     （此上限指 worker 修段落的次數；全部段落完成後 supervisor 的 numcheck 修復迴圈仍修到零為止，兩者層級不同）
   - 全段落完成後：numcheck（必帶 --data）→ 修正 → 更新 latest.json → verify.py。
8. 驗收指令白名單（C2，2026-10-17 定案；實證：派工令寫錯指令 → worker 空轉 30 分鐘）——只有這三條可作為驗收：
   - `python scripts/numcheck.py --data data_reports/DATA_REPORT_<T0>.md --report reports/Daily_REPORT_<T0>_<盤別>.md`（必帶 --data）
   - `python scripts/verify.py --t0 <T0> --prev <prev> [--expect-sha <sha12>]`（權威、含 numcheck＋prior-audit＋gate）
   - `python src/check_report.py --data data_reports/DATA_REPORT_<T0>.md --report reports/Daily_REPORT_<T0>_<盤別>.md`（gate 本體；注意在 src/ 不是 scripts/；參數同 numcheck）
   - supervisor 派工前必須先在「前一份已知良好報告」上實跑一次該指令，確認可執行，才寫進派工令；派工令必含：目的／精確目標檔／驗收方式／不可動範圍／停手上限／回報格式。　（驗收必含數字對照：派工令中出現的任何數字，**必須附 DATA 出處**＝檔名＋欄位／行號；**嚴禁 supervisor 自創、憑記憶或沿用舊值**。測試與樣本任務亦同。違者視同違反鐵律「數字只出自 DATA」。）
9. 交付前檢查清單（C3，2026-10-17 定案；實測抓到 2 個瑕疵）：
   - 附錄B：kpi 14 筆順序正確、verdict 方向/信心非空、levels 的 白話 非空且數字只用 DATA 既有價位。
   - levels 支撐由近到遠（支撐＝較近、支撐二＝較遠），與前一份報告慣例一致。
   - 首行 `- 報告日期：`＝產出日（T0+1）；`- 資料基準：`指向同一 T0 的 DATA。
   - reports/latest.json 四欄齊全、report_date＝T0、status=completed。
   - 交付前：`git status --porcelain` 只應出現本次預期的檔案；commit 後：`git status --porcelain` 應為空。未經批准不得 commit／push（worker／修復情境；日常全包流程仍依上方第 5 步）。
   - 節號格式一致：各節標題樣式相同且連續（例「## 五、交易計畫」；錯例「## 五 交易計畫」漏頓號）。
   - 派工紀律（零成本）：
     - 派工令只寫差異，既有規範不重述。
     - 長輸出／diff／比對明細一律導向 temp 檔，回覆精簡（≤25 行，只貼原始輸出）。
     - 一個派工最多 1-2 項修正、最多 3 個檔案。
     - 驗證指令只跑一次，貼原始輸出（不重跑、不改寫產物硬過檢查）。
     - 執行超過 20 分鐘先回報現況，不要靜默。
     - supervisor 自身回報亦同此紀律。
10. DATA 穩定性協定（2026-10-22 定案；實證：bot 於 10:28~10:40 連推 3 版 DATA，報告寫完後被迫重對，多花 14 分鐘）：
   - 開跑前：`git fetch` 後查最後一筆 DATA commit 的時間（`git log -1 --format=%cd origin/master -- data_reports/DATA_REPORT_<T0>.md`）；距今 < 5 分鐘 → 先等 bot 推完再動工，不要開跑（成本約 3 秒，換掉整批重對）。
   - 收尾前：重算 `sha256` 前 12 碼，與 `open.py` 印出的 `DATA_SHA=` 比對；不一致 → 立即以新 DATA 重對，不要等 push 被拒才發現。
完成後回報：T0＋盤別＋一句話結論＋關鍵價位＋push 的 commit＋Dashboard 更新時間。

固定指令（勿用臨時腳本）：
- 開工：`python scripts/open.py --t0 yyyymmdd --fetch`（先 gapfill 補洞再凍結＋起草，DATA 缺失才全量抓取；失敗自動退回已 pull 的 DATA；本機 07:55 排程已取消，on-demand 取代之，Actions 照跑；跨日補跑加 `--slot morning/evening/weekend --date 排定日` 釘死盤別）
- 驗證：`python scripts/verify.py --t0 yyyymmdd --prev yyyymmdd`（numcheck＋prior-audit＋gate 一次完成；`--expect-sha` 可鎖基線）

定義（台指期全為準）：
- 日盤收盤當日 13:45；夜盤 15:00~隔日 05:00，歸屬開盤當日。
- 平日 13:45 前→T0＝前一交易日／全日；平日 13:45 後→T0＝今天／日盤；
  週末假日→T0＝往前最近交易日／全日（＋休市標示）。
- 交易日＝週一~五且非 TWSE 休市日曆休市日。

註：國定假日後第一天若 T0 對不上，我會先跟你確認再動工。
