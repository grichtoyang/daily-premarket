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


## 8. 2026-11-01 最新狀態追加

### P0 視覺與自動化驗收
- 使用者確認目前 Dashboard 所有先前指出的圖示／文字重疊均已消失：PASS（使用者畫面驗收）。
- Build／Deploy Run `41297437934`：PASS。
- Integration Run `41297437923`：PASS。
- 17F offline self-tests：PASS（以該次 Workflow log 為證）。
- 原始 11 張基準截圖逐張比對：NOT TESTED；不阻擋目前重疊問題結案。

### 五個新異常區塊
以下僅為使用者截圖觀察，尚未讀取相同 T0 的 DATA_REPORT／JSON／HTML／來源資料，故根因均未確認：

| ID | 區塊 | 初步假說／待查 | 狀態 |
|---|---|---|---|
| DATA-UI-01 | 借券／券 | 單位換算、餘額與變化值口徑、張／股倍率 | BLOCKED：待查來源欄位與 Builder formatter |
| DATA-UI-02 | 選擇權法人交易 | 圖表的 0 日與明細日夜盤口數不一致；查 schema／series mapping／欄位定義 | BLOCKED：待查原始輸入與 JSON |
| DATA-UI-03 | IV／GEX 深度 | PCR、Vol% 可用但 GEX／IV Rank／Term unavailable；查來源與計算是否實作 | BLOCKED：待查原始輸入與計算程式 |
| DATA-UI-04 | 三劇本路徑 | 未校準機率不顯示可能符合規則，但主圖空白仍須查 payload／rendering | BLOCKED：待查 JSON 與前端元件 |
| DATA-UI-05 | 相關性熱圖 | 畫面提示日期對齊樣本不足；查歷史資料、日期對齊及樣本門檻 | BLOCKED：上游原因未確認 |

### Git 基準（2026-11-01 查證）
- P0 branch `phase2-p0-data-quality` HEAD：`49fd5b0dfd6a9c1b89fc49bb6e4d81ae5fdc4d33`。
- Recovery branch `ops/recovery-handoff` 更新前 HEAD：`d07f384157b9ca919019a903b1b373d9ae45fb84`。
- 本次 Recovery 文件更新 Commit：`2432be63f7afa6bcf4d2ba74a2cecc16630fb21d`（RECOVERY.md）；PROGRESS.md 本次更新後續 Commit 待補。
- 未修改 P0／master／V8／程式／Dashboard／Workflow；未 Merge。

### 下一步
1. 先對五個區塊做唯讀根因追蹤：同一 T0 的 DATA_REPORT → V9 Pro JSON → Builder → HTML 元件。
2. 分類根因並提出最小修正方案；未經確認不改程式。
3. 五項問題釐清後再決定 P0 收尾／P1 啟動順序；P1 尚未開始。


## 9. 五個 Dashboard 區塊初輪根因結果（T0 2026-10-30）

查核依據：
- DATA_REPORT SHA `b25266b606408615e247cdeecd7641fc52fce26b`
- Dashboard JSON SHA `9f031928b02f9b652e9ff31f0397224db2086cb4`
- Builder SHA `011224e54a32ddbf52db6fc1347d2c865fa010eb`
- React template SHA `018fcff6bd49f7f796904fed47d96784aec8fe26`

| ID | 初輪查核結論 | 狀態 |
|---|---|---|
| DATA-UI-01 借券／券 | 借券餘額 4,651,514 張與 465.2 萬張為等值換算；融券 233,537 張換算正確。但 DATA_REPORT 有借券賣出餘額 36,178 張、增減 -1,273 張，JSON 缺少 `borrowedSell`，前端讀取不到。 | 單位換算 PASS；借券賣出欄位傳遞 FAIL |
| DATA-UI-02 選擇權法人交易 | JSON 明確有法人日夜盤口數；前端 `Number(x[3]||0)` 遇到 `+6,624` 這類含逗號字串轉成 NaN，圖表顯示 0。 | FAIL：前端數字解析錯誤 |
| DATA-UI-03 IV／GEX 深度 | JSON options 沒有 GEX／IV Rank／Term；Builder 也註明 DATA_REPORT 未提供。Unavailable 屬正確缺值呈現。 | 缺值呈現 PASS；補資料源／計算 NOT TESTED |
| DATA-UI-04 三劇本路徑 | Template 明確以「情境機率未經回測校準，暫不顯示百分比」取代 chart；三種價格情境已在下方列出。不是資料缺漏。 | 防止未驗證機率 PASS；替代圖形需求待確認 |
| DATA-UI-05 相關性熱圖 | JSON matrix／labels 為空；SQLite 3 筆、有效 filled 2；Builder 直接輸出硬編碼空矩陣，尚未執行相關係數計算。 | 空狀態 PASS；相關性計算 NOT IMPLEMENTED |

### 建議最小修正順序
1. 修正借券賣出餘額／增減由 DATA_REPORT 到 JSON 的欄位傳遞。
2. 修正選擇權法人圖表對千分位字串的解析，補上正／負／逗號／缺值測試。
3. 其餘三項先不造假資料、不把 unavailable 轉 0；另行定義資料源、三劇本呈現方式及相關性樣本門檻。

本輪為單模型唯讀自我審查，未修改程式或執行修正測試；P0 程式修正尚未開始，P1 尚未啟動。
- Recovery 文件更新 Commit：`2432be63f7afa6bcf4d2ba74a2cecc16630fb21d`（RECOVERY 初次更新）；`4dbd7fbe11363fb672a182d03fc1d042aec55fa7`（RECOVERY 根因追加）。
- 本次 PROGRESS 更新 Commit：待遠端寫入後補登。

- PROGRESS 初輪根因結果更新 Commit：`cf09ba27d1a66c404052cdf2833cdb397382ea83`。
- 本次交接文件更新完成；最新 Recovery branch HEAD 請以 GitHub 查詢結果為準。
