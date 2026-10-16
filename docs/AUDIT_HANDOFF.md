# 稽核交接包（給外部模型審查用，2026-10-16）

> 目的：用户請第三方模型審查本專案＋審查我（OpenCode/Muse Spark）經手的改動。
> 本文件只陳述事實與不確定處，不辯護。時間皆 Asia/Taipei。

## 1. 專案一句話

每日台股盤前報告流水線：GitHub Actions 定時抓資料 → `data_reports/DATA_REPORT_*.md`
→ AI（我）寫 `reports/Daily_REPORT_*_日盤/全日.md` → `verify.py`（numcheck＋prior-audit＋gate）
全過才發布 → Streamlit Dashboard 讀 `reports/latest.json` 顯示。

## 2. 當前架構（2026-10-16 現況）

- 寫手只剩 Actions（三班：平日 08:00／19:00、週六 08:00；UTC cron 見
  `.github/workflows/daily_data.yml`）。本機排程已刪除（10-14）。
- 本機只走 `scripts/open.py --fetch`（gapfill 補洞；DATA 缺失才全量）。
- 同 T0 重跑 fill-only（`fetch_data.merge_same_t0`）：新缺沿用舊、皆有值沿用舊值。
- 起草機 `src/draft_blocks.py` 產出數字貼塊；驗證 `scripts/verify.py --t0 X --prev Y
  [--expect-sha S]`；發布閘門 `src/check_report.py`。
- TAIFEX 經 Cloudflare Workers 代理（`workers/taifex-proxy_V1.4.js`，已部署驗收）。

## 3. 期交所夜盤語義（已實證，審查基準）

- 官網「期貨每日交易行情查詢」：**查日期 D 的盤後時段 → D-1 15:00~D 05:00 那一節**。
  證據：用户 10-16 官網截圖（查 10/16 盤後，標題寫 2026/10/15 15:00~次日05:00，
  TX 202610：開46,926／高47,417／低46,456／收47,366／+435／+0.93%／量41,283）。
- 推論：T0 全日版要的當晚節（15:00 T0 → 05:00 T0+1）必須**查 T0+1**；
  日盤版要前一夜，查 T0 當天。收盤前（T0+1 05:00 前）查到的都是半成品。
- 線上交叉驗證：`futures-night-ohlc?date=2026/10/16` 回上述終值；
  `?date=2026/10/15` 回開48,801／收47,945／-853（前一節）。

## 4. 我經手的改動（10-14～10-16，含驗證狀態）

| commit | 改動 | 驗證 |
|---|---|---|
| 6aa493f | 封存本機排程入口（guard＋docstring）；t0 日曆失敗 flag；open 帶 --from-open | 裸執行拒絕 RC=2 實測 |
| 7295981 | 起草機補 9 表（§5.1/5.3/5.4/6.1/6.2） | 真實 DATA 實測＋10-14/10-16 兩份報告實戰 |
| 8cbd266 | ANA 模板兩處過期修正 | 文字 |
| 4ffb36f | open.py subprocess None-safe（gapfill stdout=None 崩潰） | 重跑 RC=0；**根因未明（疑 Windows pipe 瞬斷，僅發生一次）** |
| c7743fc／0b83df8 | gapfill 維持率補登（189.94／191.61） | 之後報告採用，gate 通過 |
| 2eb687a／ea5bb93 | 兩份全日報告（1013／1015），皆 RC=0＋GATE_PASS | verify 日誌見對話；1015 後來重發（見下） |
| 5977a9f | SOP 修復三原則（小洞人工／大洞才動工具／功能凍結） | 文字（用户定案） |
| 8d739c6 | open.py pull --ff-only＋分歧 abort | 實測 pull 正常、sha 不變 |
| 19b76ee | fetch_data 死碼＋TBD→unavailable（3 處） | compile＋import＋單元行為實測 |
| e4c5384 | Actions 遲到根因（GitHub 10-12 事故 backlog，官方狀態頁實證） | 時間線對齊；遲到仍持續（~7h，未改善） |
| b7c3e98 | worker V1.4 部署線上驗收（date=page） | live 端點實測通過 |
| 185f378 | **夜盤改回查 T0+1＋05:00 完整性 gate**（見 §5 認錯） | 规则單元實測（全日→T0+1、日盤→今天、23:32 拒收）；待一次真實早班實戰 |
| 321bef4 | DATA_1015 夜盤手動補登官網終值 | 與截圖＋proxy 交叉一致 |
| 29207d5 | 1015 報告夜盤重發 PASS | verify RC=0＋GATE_PASS（新 sha 227210ebb47f） |
| 0fefd29／94fc714／ae087c1 | HANDOFF＋喚醒 prompt 防火牆（一行錨規則） | 文字 |

## 5. 我承認的錯誤（請重點審查是否還有殘留）

1. **10-12 夜盤改錯（最大的一件）**：把「假日無節次的正常回退」誤診成規則錯，
   將驗證無誤的「全日查 T0+1」改成查今天，錯了四天（10-12～10-15 夜盤可能整節偏移）。
   10-16 已改回。**问题：之前在錯誤地基上疊了 strict-gate／worker 標籤等四層，
   請審查這些層在改回後是否仍自洽、有無互相打架。**
2. **10-16 報告憑記憶填數**：力道合計夜半列混入昨日值、格芯金額跨事件混搭等 5 處，
   verify 首輪全抓到並修完。**问题：verify 抓不到「數字對但語義錯」的巧合
   （如 Top10 的 49,000 在新舊 DATA 都存在），請審查是否有此類漏網。**
3. **draft 首讀異常（未破案）**：10-16 早班第一次讀起草檔得到昨日數字，
   重跑即正常，生成器本身無辜。現象一次、無復現、無解釋。**请判断是否需追查。**

## 6. 已知未解／沒把握清單（不推論，只列出）

- 法人夜盤交易拆分（外資夜淨 -2,103 等）無日期可驗 session 歸屬，維持＋§11 揭露。
- DATA_1014 夜盤與 1013 一字相同，疑似 fill-only 凍結舊值；1014 無報告，按不動歷史原則未處理。
- fill-only 對「天天會變的列」（夜盤、7.1 對照列）是否會永久凍結舊值，未做系統性證明。
- GitHub 排程仍遲到 ~7h（外部問題，持續中）；10-15 19:00 那班至今無 commit（可能無變化跳過，無法從本地確認）。
- repo 內零常駐測試（用户定案：小洞人工、不為此加碼）。
- `open.py` 的 `git pull` 已改 --ff-only；bot 的中途改寫仍可能造成開工當下 sha 變化（流程要求重凍結，但靠人工記得）。

## 7. 請第三方重點審查（用户原話：怕我稽核後再次改錯）

1. `src/sources/taifex.py` 的夜盤規則（§3 語義下全日→T0+1、日盤→T0、05:00 gate、附屬端點同口徑）有無漏洞，特別是假日／延遲班次／日盤傍晚等邊界。
2. `merge_same_t0` 在夜盤與 7.x 對照列上的行為：是否會把舊節次凍成正式值。
3. `Daily_REPORT_20261015_全日.md`（sha 227210ebb47f 版）有無數字與 DATA 不符、
   語義與數字矛盾之處（verify 已過，找機器抓不到的）。
4. 唤醒 prompt（`prompts/daily_starter_Muse.md`）與實際腳本行為是否一致，有無 drift。
5. 只讀審查、逐項列清單；要改任何東西之前，先經用户批准（鐵律）。

## 8. 重現驗證的方法

- 開工：`python scripts/open.py --t0 yyyymmdd --fetch`（先看 DATA 在不在）。
- 驗證：`python scripts/verify.py --t0 yyyymmdd --prev yyyymmdd [--expect-sha s]`，
  要 RC=0＋NUMCHECK_ERRORS=0＋GATE_PASS。
- 夜盤：对照官網「期貨每日交易行情查詢」（日期選 T0+1、盤後交易時段），
  标题应为「T0 15:00~次日05:00」；或打
  `https://taifex.grichtoyang.workers.dev/futures-night-ohlc?date=YYYY/MM/DD&month=202610`
  （D 对应 D-1 起那一节）。
