# V9 Pro 專案工作規則（正式版）

版本：1.0｜2026-11-14（Asia/Taipei）
Repository：\`grichtoyang/daily-premarket\`
工作分支：\`phase2-p0-ui-fixes\`

## 1. 專案狀態

- V9 Pro 17F 六分頁 UI／分析改進已完成使用者驗收。
- 資料層於 2026-11-09 完成並凍結；未經使用者明確授權不得修改、重跑或部署。
- DL-07 已結案，不得重開。
- 六個分頁：總覽、現貨、重要市場、期貨、選擇權、綜合分析。已驗收分頁不得主動重做。
- 保留原 V9 Pro 視覺風格，不另建模板，不恢復已被否決的版型。

## 2. 工作開始前

1. 讀取 Master Skill：\`skills/daily-premarket-analysis-v9-pro-skill.md\`。
2. 依任務讀取四份專項 Skill：data／analysis／visual／build-release。
3. 確認 branch、HEAD、檔案狀態、差異與 Workflow path filter。
4. 確認使用者授權的分頁、檔案與可執行測試範圍。
5. 不把歷史 Recovery 文字當成高於目前程式的現行規格；遇到矛盾先查證。

## 3. 工作範圍

- 僅修改使用者明確指定範圍。
- 不順手重構、不擴大範圍、不碰已鎖定頁面。
- 不修改 Builder、DATA_REPORT、資料來源、Worker／Proxy／API、daily-data Workflow 或資料層測試，除非使用者明確授權。
- UI-only 工作若會觸發完整 Build + Deploy（其中含 Builder／資料層測試），必須先檢查並取得該次執行授權。
- 不擅自建立分支、PR、merge、cherry-pick 或 tag；沿用指定工作分支。

## 4. 分析與呈現

- 所有分析區塊維持「分析／判斷／操作」。
- 數據、單位、基準與時間範圍清楚。
- 交代支持與反向證據；缺值不當零，存量不當流量。
- Bias 是背景評分，不是勝率或進場訊號。
- 交易計畫必須有觸發、確認、失效及風險條件。
- 保留原 V9 Pro 六分頁視覺語言與使用者已驗收的配置。

## 5. 驗收與交付

狀態使用 PASS／FAIL／BLOCKED／NOT TESTED。
自動化測試、Browser Audit、Pages Deploy、使用者實際畫面驗收分開記錄。
只提供可核實的 commit、Actions run、artifact 與 Pages URL。
若只有單一模型審查，必須稱為自我審查，不得宣稱獨立多模型審核。

## 6. 文件優先順序

1. 使用者在當前任務的明確授權與限制。
2. Master Skill 與四份正式專項 Skill。
3. Unit Standard／Unit Map 等現行契約文件。
4. 目前 branch 的程式、測試與 Workflow 實際行為（用來核實文件）。
5. Recovery／HANDOFF 等歷史交接文件。

若文件與程式不一致，不得自行選擇有利版本；先查證並記錄差異。