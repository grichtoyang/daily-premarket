---
name: v9-pro-build-release
description: V9 Pro Build、UI-only Browser Audit、GitHub Pages 部署與交付驗收流程。
---

# V9 Pro — Build & Release Skill（正式版）

版本：1.0｜定版日期：2026-11-14
工作分支：\`phase2-p0-ui-fixes\`
Dashboard Pages：\`https://grichtoyang.github.io/daily-premarket/p0/v9-pro-latest.html\`

## 1. 建置與發布責任

Build／Release 層負責：
1. 依指定 DATA_REPORT／既有 Dashboard JSON 準備建置輸入。
2. 執行 Template／HTML／JavaScript 驗證。
3. 產生日期版與 latest Dashboard HTML。
4. 執行 Browser Audit。
5. 產生 Pages artifact 並部署。
6. 提供 commit、Actions run 與 Pages 網址供使用者驗收。

實際步驟以當前 Workflow 為準，不得只依本文件推測執行結果。

## 2. 兩種 Workflow 必須區分

### 2.1 完整 Build + Deploy

Workflow：\`.github/workflows/daily-premarket-v9-pro.yml\`

目前 workflow 不只是 UI 渲染：它會執行部分資料來源／資料契約測試、Builder self-tests、讀取 DATA_REPORT、執行 Builder 產生 JSON、注入 Template、產生 Dashboard HTML、執行測試並部署 Pages。

因此在 DATA LAYER FROZEN 狀態下：
- 不得自行手動觸發完整 Workflow。
- 修改 Template 或相關檔案前，必須檢查 push path filter 是否會自動觸發完整 Workflow。
- 只有使用者明確授權該次 Build／Deploy 時，才可執行或安排會觸發完整 Workflow 的變更。
- 若本輪僅需 UI 技術驗收，優先使用 UI-only Audit；不可把 UI-only Audit 稱為正式 Build 或 Pages 部署。

### 2.2 UI-only Browser Audit

Workflow：\`.github/workflows/v9-pro-ui-only-audit.yml\`

其目的為在不執行 Builder／資料來源／資料層測試、不修改 DATA_REPORT／Dashboard JSON／Worker／Proxy／API、不部署 Pages 的前提下，使用既有日期版 Dashboard JSON 注入最新 Template，進行：
- HTML inline JavaScript 驗證。
- Playwright Chromium 瀏覽器測試。
- 六分頁切換與內容載入檢查。
- Desktop／Tablet／Mobile 測試。
- 重要市場新聞來源、T0 分類、全寬卡片等專項檢查（以目前 Browser Audit 實作為準）。
- 資料層與既有 Dashboard source artifacts 未變更檢查。
- 上傳臨時 HTML、測試報告與截圖 artifact。

UI-only Audit 不產生正式 Pages 部署，也不驗證新 Builder 輸出或資料來源真實性。

## 3. Git 與分支紀律

- 目前工作分支為 \`phase2-p0-ui-fixes\`；未經使用者指示不得切換到其他分支。
- 不擅自建立多餘分支、PR、merge、cherry-pick 或 release tag。
- 修改前讀取 branch HEAD、檔案 SHA、Git 狀態與差異。
- 只提交授權範圍的檔案；文件更新不得夾帶 Template 或資料層修改。
- 產生 Dashboard HTML 的自動 commit 必須與原始 Template commit 分開記錄。
- Push 前確認會觸發的 Actions；不得以文件提交成功推定部署成功。

## 4. 驗收證據鏈

逐層回報，不得跨層推論：

| 層級 | 可支持的結論 |
|---|---|
| 文件／程式 diff | 指定內容已修改 |
| HTML／JS validation | 語法與注入結構通過 |
| Builder self-test | Builder 內建測試通過；不等於外部資料正確 |
| Browser Audit | 指定瀏覽器、視窗尺寸及測試斷言通過 |
| Build artifact | 指定輸入已產生 HTML／JSON artifact |
| Pages Deploy | 指定版本已部署到 Pages |
| 使用者截圖驗收 | 實際畫面與分析內容經使用者確認 |

每次報告應提供：
- Branch、Template commit、generated artifact commit。
- Workflow run ID／URL 與各 Job／Step 結果。
- 測試尺寸、分頁範圍及已驗證的斷言。
- Pages URL 與對應版本。
- 尚未測試項目與風險。

## 5. 發布前檢查

- Template 是觸發該次 Workflow 的 commit 內容。
- 使用指定日期或最新 DATA_REPORT 的解析結果有明確記錄。
- 六分頁均存在；Dashboard data version 符合 V9 Pro 17F。
- 缺值、PCR、Flip／GEX 等欄位契約符合目前規格。
- HTML／JavaScript validation 通過。
- Browser Audit 六分頁 Desktop／Tablet／Mobile 通過。
- Pages artifact 存在且 Deploy job 成功。
- 對比自動生成的 Dashboard 檔案，確認沒有未預期資料層或其他檔案改動。

若完整 Workflow 執行資料層測試或 Builder，必須先有使用者明確授權；不得以「只改 UI」作為略過此限制的理由。

## 6. 最終交付

使用者偏好直接提供最新 Pages URL 及必要 Actions 證據。交付時明確區分：
- 已修改。
- 自動化測試已通過。
- 已部署。
- 使用者實際畫面已驗收。
- 尚未驗證／尚未完成。

沒有成功部署證據時，不得稱為已上線；只有 UI-only Audit 通過時，不得稱為 Pages 已更新。