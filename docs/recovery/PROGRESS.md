# PROGRESS — 盤前分析 V9 Pro 進度總表

> 狀態基準：2026-11-01（Asia/Taipei）。
> 本文件是進度索引；最新中斷點與下一步以 `RECOVERY.md` 為準。

## 1. Repository／分支基準

| 項目 | 已查證狀態 |
|---|---|
| Repository | `grichtoyang/daily-premarket` |
| master HEAD | `d01c315a5a33d21cfd7514040700a57a66637430` |
| P0 branch | `phase2-p0-data-quality` |
| P0 HEAD／凍結基準 | `031edc42791b396eb61fc32ae8c490b16d01b17c` |
| Recovery 文件工作分支 | `ops/recovery-handoff`，由 P0 凍結 Commit 建立 |
| P0／master 關係 | 已知分歧；先前比對為 P0 ahead 265、behind 3。禁止未經批准整合。 |

P0 與 master 分歧期間，master 獨有的三個 Commit（先前查證）：
- `df5f5dc09fb57badff6fdcdba6abd39791e5a286` — 更新 2026-10-30 DATA_REPORT。
- `dd84528` — 刪除 2026-10-30 DATA_REPORT（完整 SHA 待重新查證）。
- `d01c315a5a33d21cfd7514040700a57a66637430` — 保留 P0 Dashboard 獨立 Pages 路徑。

以上分歧數字與 Commit 清單在正式整合前必須重新執行 compare 驗證；本文件不構成 Merge 授權。

## 2. Phase 2 階段狀態

| 階段 | 定位 | 狀態 | 備註 |
|---|---|---|---|
| P0 | 資料品質、V9 Pro 基礎 Dashboard／流程隔離 | 核心功能完成；結案收尾未完成 | 不重開發核心；處理已知缺陷與未測項 |
| P1 | 尚待正式規格盤點 | NOT STARTED | 不可從舊聊天摘要推定完整範圍 |
| P2 | 尚待正式規格盤點 | NOT STARTED | 依新版 Phase 2 規劃確認 |
| P3 | 尚待正式規格盤點 | NOT STARTED | 依新版 Phase 2 規劃確認 |
| P4 | 尚待正式規格盤點 | NOT STARTED | 依新版 Phase 2 規劃確認 |
| P5 | 尚待正式規格盤點 | NOT STARTED | 依新版 Phase 2 規劃確認 |

注意：既有 `docs/PHASE2.md` 內容仍有早期選擇權改版待辦，不能視為完整且最新的 P0～P5 規劃。P1 啟動前必須先盤點正式規格與歷史決策。

## 3. P0 已完成且有紀錄的項目

以下為 P0 結案摘要（依既有交接資訊及指定 Actions 紀錄）：
- 自建上市融資維持率計算引擎。
- Blave 同 T0 交叉驗證及備援。
- 同日人工輸入最後備援，禁止沿用舊資料。
- DATA_REPORT T0 歸屬及資料品質處理。
- V9 Pro Dashboard 建置、資料注入及既有回歸測試。
- V8 與 V9 執行路徑分離。
- P0 Fetch／Build／Deploy 工作流程隔離。
- P0 GitHub Actions 整合測試。

既有 Actions：
- Integration：Run `41281205671`，Success（使用者提供並已於前一工作階段查核）。
- Build／Deploy：Run `41281205639`，Success（使用者提供並已於前一工作階段查核）。

P0 Dashboard URL：
`https://grichtoyang.github.io/daily-premarket/p0/v9-pro-latest.html`

Actions Success 僅證明該次 workflow 工作成功，不代表 CDN 字型或所有瀏覽器圖表視覺均已驗收。

## 4. P0 結案前未完成工作

### 4.1 CDN 字型載入

- Dashboard template 使用 Google Fonts CDN；需確認 CSS 及字型檔實際載入。
- 驗收項目：CSS 回應、字型檔回應、Noto Sans TC 套用、JetBrains Mono 套用、CDN 失敗時 fallback。
- 狀態：NOT TESTED（尚無實際瀏覽器測試證據）。

### 4.2 Dashboard 已發現缺陷

| ID | 區塊 | 使用者觀察 | 待查／驗收 |
|---|---|---|---|
| UI-01 | 圖表（融資融券儀表等） | 數字與圖示略有重疊 | 定位／間距修正後檢查桌面與手機尺寸 |
| UI-02 | Call Wall／Put Wall／Gamma／Flip／MaxPain 關鍵價位圖 | 數字及標籤互相重疊 | 標籤避讓、定位及不同價位接近時的顯示 |
| UI-03 | 選擇權法人交易 | 圖示／圖表呈現異常 | 檢查資料 schema、series mapping、渲染元件 |
| UI-04 | 三劇本路徑 | 圖表區域空白，文字情境有呈現 | 檢查資料是否產生、圖表元件是否掛載、空資料狀態 |
| UI-05 | 相關性熱圖 | 歷史日期對齊樣本不足，圖表未產生 | 檢查日期對齊與樣本門檻；不得捏造資料；樣本不足時顯示清楚空狀態 |

程式初步查核曾在 `scripts/v9_pro_builder.py` 約第 1080 行看到相關性資料輸出為空 labels／matrix。行號可能隨版本變動，修正前必須以目標 Commit 重新定位。
UI-01～UI-05 尚未完成根因確認及修正，不能標示 PASS。

### 4.3 P0／master 整合評估

- 狀態：BLOCKED（等待差異審查與使用者決策）。
- 不可直接 Merge；不可直接覆蓋 master 正式 Dashboard。
- 下一步是唯讀 compare、逐檔分類、提出整合方案；不執行 Merge。

## 5. P1 啟動條件

P1 尚未開始。啟動前必須：
1. 完成 P0 必要結案工作，或由使用者明確決定未完成項目的處置。
2. 讀取完整架構與相關規格，確認新版 Phase 2 的 P1 範圍。
3. 對照舊文件、Master 規格、既有程式與歷史決策，列出衝突。
4. 提出 P1 清單、執行順序、依賴關係、資料需求及逐項驗收標準。
5. 取得使用者明確批准後，才開始 P1 程式實作。

## 6. 禁止事項

- 不修改／刪除／搬移 V8。
- 不未經批准 Merge P0 與 master。
- 不覆蓋 master 正式 Dashboard。
- 不合併 Fetch 與 Build workflow。
- 不擅改 Dashboard 六個分頁及規格。
- 不重新開發已凍結的 P0 核心功能。
- 不將未測試、未執行或推測結果標示為 PASS。
- 不在新對話未查 GitHub 實際狀態前重做、覆蓋或 Push。

## 7. 更新紀錄

| 日期 | 更新 |
|---|---|
| 2026-11-01 | 建立專案進度基準；記錄 P0 結案待辦、Dashboard 缺陷、CDN NOT TESTED、分支整合 BLOCKED、P1 未啟動。 |
