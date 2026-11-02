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


## 10. 2026-11-01 DATA-UI-01／02 修正分支進度

### Git 基準（最新遠端查證）
- P0 原分支 `phase2-p0-data-quality` HEAD：`49fd5b0dfd6a9c1b89fc49bb6e4d81ae5fdc4d33`（未修改）。
- UI 修正分支 `phase2-p0-ui-fixes` HEAD：`eb861a470ff5a90faa73ae4097c3c15d227f3d10`。
- UI 修正分支由上述 P0 HEAD 建立；compare：ahead 14、behind 0。
- master HEAD：`0ac95b2521e7bdcb357431cc7725da4e2c26e602`（未修改）。
- Recovery 文件分支本次更新前 HEAD：`7e5bd237ab229a5108adb13b5200707136b4bed4`。
- 本次 compare 僅有五個變更檔案：新增 UI 專用回歸 Workflow；修改 V9 Builder、React template、兩個測試檔。未修改 V8 檔案。

### 已實作項目
1. **DATA-UI-01 借券賣出**
   - Builder 解析 DATA_REPORT 的借券賣出餘額與增減，並傳遞至 JSON：`borrowedSell`、`borrowedSellDiff`、`borrowedSellDiffScope`。
   - 若報告註記「借券賣出增減僅上櫃值」，JSON／Dashboard 明確標示「上櫃（上市 TWT93U 未取得）」；不得誤標成上市櫃合計。
   - 借券賣出餘額及增減分開呈現；不把存量當成當日變化。

2. **DATA-UI-02 選擇權法人交易**
   - 新增專用數字解析函式 `v9ProOptionNetNumber`，移除千分位逗號後解析數值，保留正負號。
   - 缺值／非數字回傳 null，圖表過濾無效點，不以 0 假裝有效資料。
   - 保留 React 內部事件註冊函式 `qn` 原始宣告及呼叫，不改動 React 內部行為。

### 測試與證據
- UI 專用 Workflow Run `41301487409`：Success。
- V9 Builder offline self-tests：PASS。
- React template tests：10 tests，PASS（含 JS syntax、千分位正負數解析、缺值及 React 內部函式保護）。
- DATA_REPORT parser tests：3 tests，PASS（含借券餘額／增減／資料範圍）。
- Builder JSON 整合檢查：PASS。
  - `borrowedSell=36178.0`
  - `borrowedSellDiff=-1273.0`
  - `borrowedSellDiffScope=上櫃（上市 TWT93U 未取得）`
- 其餘 DATA-UI-03／04／05 未修改，維持既有缺值／未校準呈現。

### 尚未驗證／尚未完成
- 桌面／手機實際瀏覽器視覺驗收：NOT TESTED。
- UI 修正分支尚未部署 GitHub Pages：NOT DONE。
- 尚未 Merge／Cherry-pick 回 P0 或 master：NOT DONE；不得自行執行。
- 本機／OpenCode 工作目錄 dirty status：NOT TESTED。
- 以上為單模型程式碼與 CI 自我審查，非獨立多模型 Auditor。

### 下一個唯一工作
在 `phase2-p0-ui-fixes` 產生不部署的 T0 預覽 HTML，確認兩個修正區塊的資料注入與呈現；再交由使用者做桌面／手機畫面驗收。不得觸碰 P0 原分支、master、V8 或執行部署／合併。


## 11. 2026-11-01 非部署 HTML 預覽產物

- UI fixes branch 最新 HEAD：`2ee248dd21fa5ad9545c7c70d9e427f793721d7c`。
- UI 專用 Workflow Run `41301631710`：Success。
- 新增非部署 HTML 預覽產生與上傳步驟：PASS。
- Artifact：`V9-UI-Fixes-Preview-20261030`，檔案 `v9-pro-ui-fixes-preview-20261030.html`，88,133 bytes。
- Artifact ID：`13081122728`；GitHub Actions run：`https://github.com/grichtoyang/daily-premarket/actions/runs/41301631710`。
- Artifact 預計於 2027-01-30 到期。
- 此產物只用於預覽，沒有部署 GitHub Pages、沒有推送產物到 P0／master，也沒有 Merge。
- 使用者桌面／手機實際視覺驗收仍為 NOT TESTED；下一步由使用者下載 Artifact 檢查 DATA-UI-01／02 兩個區塊，回報結果後再決定是否需要視覺微調。
- 最新查證：P0 HEAD 仍為 `49fd5b0dfd6a9c1b89fc49bb6e4d81ae5fdc4d33`；master HEAD 仍為 `0ac95b2521e7bdcb357431cc7725da4e2c26e602`；Recovery 文件分支更新前 HEAD `4479bbafd893adb9bf37257a3d2e4ccb8c8ed960`。


## 12. 2026-11-01 DATA-UI-01／02 手機版視覺驗收

### 最新程式與預覽證據
- UI fixes branch：`phase2-p0-ui-fixes`
- 最新 UI branch HEAD：`d0f644e661fc43596bc4886ae0fd92977891db17`
- Workflow Run：`41303525878`，Conclusion：Success。
- Artifact：`V9-UI-Fixes-Preview-20261030`
- Artifact ID：`13082301670`；大小 88,306 bytes；到期時間 2027-01-30。
- Run URL：`https://github.com/grichtoyang/daily-premarket/actions/runs/41303525878`
- CI 成功且 Artifact 已上傳；本節手機截圖驗收對應此輪修正內容。

### 使用者手機截圖驗收
| 項目 | 驗收結果 | 證據／說明 |
|---|---|---|
| DATA-UI-01 借券資料欄位 | PASS | 借券餘額 4,651,514 張；借券賣出 36,178 張；增減 -1,273 張；融券 233,537 張；範圍標示「上櫃（上市 TWT93U 未取得）」。 |
| DATA-UI-01 手機排版 | PASS | 手機單欄排列；增減標籤與 -1,273 張完整同列，未見折行／重疊。 |
| DATA-UI-02 日盤解析及顯示 | PASS | 外資 +6,624、投信 -4,937、自營商 +1,342、三大法人合計 +3,029。 |
| DATA-UI-02 夜盤解析及顯示 | PASS | 外資 -94、投信 0、自營商 -1,391、三大法人合計 -1,485。 |
| DATA-UI-02 手機圖表 | PASS | 圖表呈現 8 筆日盤／夜盤資料，標籤、正負方向及數值可辨識，未見裁切／重疊。 |

### 範圍與尚未驗證事項
- DATA-UI-01／02：使用者提供手機截圖，手機實際視覺驗收 PASS。
- 桌面版實際視覺驗收：NOT TESTED（尚無桌面截圖）。
- DATA-UI-03／04／05：本輪未修改，不列入本次驗收。
- 未部署 GitHub Pages、未 Merge／Cherry-pick 回 P0 或 master；P0、master、V8 不得擅自修改。
- 本機／OpenCode 工作目錄狀態：NOT TESTED。
- Auditor 為單模型自我審查，非獨立多模型審核。
- 下一步：確認是否需要桌面版視覺驗收；之後才可討論 UI fixes 回 P0 的整合方式，需另行取得使用者明確授權。


## 13. 2026-11-01 DATA-UI-05 修正進度（最新）

> 本節覆蓋前文將 DATA-UI-05 標示為 BLOCKED／NOT IMPLEMENTED 的舊狀態；歷史紀錄保留，不回溯改寫。

- 工作分支：`phase2-p0-ui-fixes`
- 最新 Commit：`4d2ccc4769f1df819601d70742312e75e388829d`
- 變更檔案僅兩個：`scripts/v9_pro_builder.py`、`templates/v9-pro-react-template.html`。
- 實作：缺值以 NULL 儲存；T0 日期正規化；同日重複資料跳過；僅使用完整且 eligible 的歷史樣本；排除非有限值；最低樣本數 5；計算 Pearson 矩陣；樣本不足／矩陣無效時不顯示假熱圖。
- 舊歷史資料未全面重建；不合資格的舊資料不納入計算。
- GitHub Actions Run `41307754019`：Success。Builder offline self-tests、React template regression、DATA_REPORT parser regression、Dashboard JSON build／欄位檢查、非部署 HTML preview 產生及上傳均成功。

### 驗收狀態
| 項目 | 狀態 |
|---|---|
| DATA-UI-05 程式修正與 CI | PASS |
| Android／桌面實際畫面 | NOT TESTED |
| 正式部署 | NOT DONE |
| Merge／Cherry-pick | NOT DONE |
| DATA-UI-03／04 | 本輪未修改 |
| V8／Master | 未修改 |

### 下一步
由使用者檢查非部署 HTML Artifact 的相關性區塊；確認有效樣本與樣本不足兩種狀態的呈現。完成畫面驗收後再決定是否結案。不得自行部署或 Merge。


## 14. 2026-11-01 DATA-UI-05 重複提示修正與手機驗收

- UI branch：`phase2-p0-ui-fixes`
- 最新修正 Commit：`8a74e30144571413cfd2ea42bfb646500cf02214`
- 本次僅修改 `templates/v9-pro-react-template.html`，移除樣本不足時熱圖下方重複的說明文字；保留熱圖區內唯一提示及有效矩陣時的欄位標籤。
- GitHub Actions Run `41308547210`：Success；Regression job 全部步驟成功。
- Artifact：`V9-UI-Fixes-Preview-20261030`，Artifact ID `13084755255`。
- 使用者新版手機截圖驗收：樣本 `0/5` 提示只顯示一次，沒有空白矩陣／色階，說明卡片正常。樣本不足狀態手機視覺 PASS。

### 最新狀態
| 項目 | 狀態 |
|---|---|
| DATA-UI-05 樣本不足狀態手機畫面 | PASS |
| 重複提示移除 | PASS |
| CI 與非部署預覽產生 | PASS |
| 有效樣本（>=5）熱圖實際畫面 | NOT TESTED |
| 桌面視覺 | NOT TESTED |
| 部署／Merge／Cherry-pick | NOT DONE |
| DATA-UI-03／04、V8、Master | 未修改 |

- 本輪 Auditor 為單模型自我審查，非獨立多模型審核。


## 15. 2026-11-01 DATA-UI-05 手機有效樣本熱圖驗收

- UI branch：`phase2-p0-ui-fixes`，Commit `98df6c782346b01dc6f66d3b4692786c32e133e1`。
- 僅修改 `templates/v9-pro-react-template.html` 熱圖繪製函式：欄名改由左側標籤呈現，儲存格依手機畫布寬高縮放，保留右側色階空間；未改相關性數值及色彩映射。
- GitHub Actions Run `41309915998`：Success；Regression、Fixture 產生與 Artifact 上傳皆成功。
- 隔離 Artifact `V9-Correlation-Heatmap-Test-Fixture`（ID `13084587818`），使用合成矩陣，不得部署。
- 使用者新版 Android 截圖確認 8×8 矩陣、標籤、數值及色階可讀，手機有效矩陣 UI PASS。

### 狀態
| 項目 | 狀態 |
|---|---|
| 0/5 樣本不足手機畫面 | PASS |
| 合成 8×8 有效矩陣手機畫面 | PASS |
| CI／隔離 Fixture | PASS |
| 真實歷史數據相關係數準確性 | NOT TESTED |
| 桌面視覺 | NOT TESTED |
| 部署／合併 | NOT DONE |
| DATA-UI-03／04、V8、Master | 未修改 |

- Auditor：單模型自我審查，非獨立多模型審核。


## 16. 2026-11-01 DATA-UI-05 真實資料樣本數盤點

- 檢查 `dashboards/data-latest.json`（UI branch，SHA `9f031928b02f9b652e9ff31f0397224db2086cb4`）：T0 `2026-10-30`、`db_mode=db`、`db_rows=3`。
- correlation `labels=[]`、`matrix=[]`，desc 為「歷史日期對齊樣本不足，相關性未計算」。最低門檻 5 筆有效樣本；DB 目前僅 3 列，故真實歷史相關性驗證 BLOCKED，待資料自然累積，禁止以合成資料填入正式 DB。
- 手機兩種 UI 狀態（0/5 與合成 8×8）PASS；桌面視覺 NOT TESTED。
- 本輪未修改程式、正式資料庫、Dashboard 資料；未部署／合併。


## 17. 2026-11-01 DATA-UI-05 寬版畫面驗收

- 使用者提供 911×1536 寬版 Dashboard 截圖；雙欄排列中的 8×8 相關性熱圖完整顯示，標籤／數值無明顯重疊，色彩與色階刻度可辨，卡片排列正常。
- 寬版雙欄視覺 PASS；大型桌面寬度（如 1440px）NOT TESTED，不過度推論。
- 本輪無程式／正式資料修改，無部署／合併。


## 18. 2026-11-01 UI branch 與 P0 基底差異審查

- Compare `phase2-p0-data-quality`（`49fd5b0d`）→ `phase2-p0-ui-fixes`（`98df6c78`）：ahead 31、behind 0，P0 為共同基底。
- 僅變更 5 檔：UI 專用 Workflow、`scripts/v9_pro_builder.py`、`templates/v9-pro-react-template.html`、兩個對應測試檔。涵蓋 DATA-UI-01／02 與 DATA-UI-05，無額外檔案變更。
- Workflow 靜態審查 PASS：只對 UI branch 執行，contents read；離線測試、JSON 驗證、非部署 HTML preview、Artifact 上傳；沒有 Pages deploy 或正式產物推送步驟。
- P0 HEAD 維持 `49fd5b0dfd6a9c1b89fc49bb6e4d81ae5fdc4d33`；master HEAD 維持 `0ac95b2521e7bdcb357431cc7725da4e2c26e602`。
- 未 Merge／Rebase／Cherry-pick／Deploy。DATA-UI-05 真實資料驗證仍 BLOCKED；1440px 視覺 NOT TESTED；本機工作目錄 NOT TESTED。
- Auditor：單模型自我審查，非獨立多模型審核。


## 19. 2026-11-01 DATA-UI-04 三劇本路徑完成手機驗收

- UI branch：`phase2-p0-ui-fixes`。
- 區間路徑修正 Commit：`9a4ca2ce4a646badedbc98ab1469c3e8fb9995a8`；回歸斷言 Commit：`d303ac600c17fc275b690ae183d0d67b7bf3cf8e`。
- 區間情境改為「現價 位於 Put Wall ↔ Call Wall」，避免用單向箭頭造成先後目標誤讀。偏多／偏空方向路徑、機率未校準聲明及 MaxPain 磁吸參考規則保留。
- GitHub Actions Run `41312758676`：Success；React template regression、JavaScript parser、DATA_REPORT parser、JSON build、非部署預覽及 Artifact 產生／上傳均成功。
- 使用者提供新版 Android 截圖，三情境價格路徑與區間上下界語意均清楚，無明顯重疊或裁切；DATA-UI-04 手機視覺 PASS。

### 狀態
| 項目 | 狀態 |
|---|---|
| 三情境條件式價格路徑 | PASS |
| 區間上下界語意 | PASS |
| MaxPain／未校準機率防誤導 | PASS |
| CI／回歸測試 | PASS |
| Android 手機畫面 | PASS |
| 桌面（含 1440px） | NOT TESTED |
| 真實回測／機率校準 | NOT TESTED |
| Merge／Cherry-pick／Deploy | NOT DONE |

- Auditor：單模型自我審查，非獨立多模型審核。


## 20. 2026-11-01 DATA-UI-03 第二輪資料鏈調查

- 已唯讀檢查 TAIFEX source、DATA_REPORT template／實際報告、V9 Builder、Dashboard JSON 與 React 卡片。
- 根因：options chain 目前只用履約價、Call/Put、成交量、OI；DATA_REPORT／JSON 沒有 IV Rank、Risk Reversal、期限 IV、逐履約價 Gamma／GEX 欄位。
- 現有卡片標題「IV / GEX 深度」，實際圖表只畫 PCR、Call Vol%、Put Vol%，標題與內容不一致；GEX／IV Rank／Term unavailable 是正確缺值，不應填 0。
- 官方 TAIFEX 有每日選擇權行情、每日 Delta、Put/Call Ratio、TAIWAN VIX；VIX 可作 30 日預期波動率歷史排名基礎，但需以「TAIWAN VIX Rank」命名，不等同單一履約價 IV Rank。
- 期限 ATM IV 可評估由有效 Bid/Ask、到期時間、標的價格與利率／股利假設反解；GEX 可計算 gross exposure，但 OI 不提供持倉方向，signed/dealer GEX 需額外模型與驗證。Delta 不等於 Gamma。

| 項目 | 狀態 |
|---|---|
| 缺值根因追查 | PASS |
| 現有缺值誠實呈現 | PASS |
| 卡片標題／內容一致性 | FAIL（已定位，待修正） |
| TAIWAN VIX Rank 接入 | NOT TESTED |
| 期限 ATM IV 計算 | NOT IMPLEMENTED |
| Gross GEX 計算 | NOT IMPLEMENTED |
| Signed／Dealer GEX | BLOCKED（方向估計方法未定） |
| DATA-UI-03 完成 | NOT DONE |

- 本輪唯讀；未改程式、資料或部署設定。Auditor 為單模型自我審查，非獨立多模型審核。


## 21. 2026-11-01 DATA-UI-03 GEX 資料鏈第一階段

- UI branch `phase2-p0-ui-fixes` 完成來源欄位保留、DATA_REPORT GEX 摘要／衍生履約價 JSON、Builder JSON 輸出及選擇權頁 GEX 分布卡片。
- GEX 僅承接既有 Gamma endpoint 計算結果，未重寫 Gamma 模型；逐履約價數值驗證、排序，T0 日期不符拒收；compact proxy 不冒充 GEX。
- 主要 Commit：source `613ce0146b19db70859560c430ae470e81d267b6`、schema fix `dfba4b6bd6074551330fe8e24c8139f0f4f62f32`、test `4c95cdefa92db010e47c023a7196c639242b3c6c`、DATA_REPORT `0c2f6aa8c7b038664959ae8c93b92121e6ab5091`、Builder `5125d66613b8e2ee21d09e914a299bac43779241`、UI `833b0220ad87d768a6805d68f47e5447f590fcc9`。
- GitHub Actions Run `41316484376`：Success；offline self-test、React regression、DATA_REPORT parser regression、Dashboard JSON build、非部署 HTML preview 通過。
- Recovery docs 僅記錄狀態；未 Merge／Deploy，未修改 Master／P0 baseline／V8。

| 項目 | 狀態 |
|---|---|
| Gamma payload 欄位保留與逐履約價基本驗證 | PASS（程式與 CI） |
| DATA_REPORT GEX 摘要／明細 JSON | PASS（程式與 CI build） |
| Builder 將 GEX 傳至 Dashboard JSON | PASS（CI build；真實 GEX 有值情境尚未驗證） |
| 選擇權頁 GEX 卡片接線 | PASS（靜態回歸）；實際視覺 NOT TESTED |
| 當日 Gamma endpoint 與 GEX 數據 | NOT TESTED |
| IV Rank／VIX Rank／期限 IV | NOT IMPLEMENTED |
| Signed／Dealer GEX | BLOCKED |
| Actions 增量耗時 <10 秒 | NOT TESTED |
| Merge／Deploy | NOT DONE |

- Auditor：單模型自我審查，非獨立多模型審核。


## 22. 2026-11-01 DATA-UI-03 GEX 第一階段交接狀態（最新）

- UI branch phase2-p0-ui-fixes HEAD：833b0220ad87d768a6805d68f47e5447f590fcc9。
- 已提交：Gamma source 保留並驗證逐履約價 GEX；DATA_REPORT 輸出 Net／Gross GEX 摘要與衍生履約價 JSON；Builder 將日期相符的 GEX 資料傳至 Dashboard JSON；選擇權頁接上逐履約價 GEX 分布卡片。
- 關鍵 commits：613ce0146b19db70859560c430ae470e81d267b6、dfba4b6bd6074551330fe8e24c8139f0f4f62f32、4c95cdefa92db010e47e023a7196c639242b3c6c、0c2f6aa8c7b038664959ae8c93b92121e6ab5091、5125d66613b8e2ee21d09e914a299bac43779241、833b0220ad87d768a6805d68f47e5447f590fcc9。
- GitHub Actions Run 41316484376：completed / success；head SHA 與 UI branch HEAD 相同。

| 驗收項目 | 狀態 |
|---|---|
| 程式接線與 CI 自動化檢查 | PASS |
| 真實當日 Gamma endpoint／GEX 有值資料 | NOT TESTED |
| 手機／桌面 GEX 圖表視覺 | NOT TESTED |
| GEX 模型獨立正確性驗證 | NOT TESTED |
| IV Rank／VIX Rank／期限 IV | NOT IMPLEMENTED |
| Signed／Dealer GEX | BLOCKED |
| Actions 新增耗時低於 10 秒 | NOT TESTED |
| Merge／Cherry-pick／正式部署 | NOT DONE |

### 下一步
1. 用當日 T0 真實資料驗證 DATA_REPORT → Builder → Dashboard JSON 完整資料鏈及日期一致性。
2. 產生非部署 HTML Artifact，完成手機與桌面 GEX 圖表視覺驗收。
3. 量測 Actions 實際增量耗時。

- 未修改 Master、P0 baseline、V8；未部署、未合併。Auditor 為單模型自我審查，非獨立多模型審核。


## 23. 2026-11-02 P0 正式結案狀態校正

> 本節依最新 P0 結案 Commit 與使用者交接截圖更新；覆蓋本文件較早章節中 P0 尚未結案、UI-01～UI-05 尚未完成的歷史狀態。歷史紀錄保留，不回溯改寫。

### 遠端查證基準
- Repository：`grichtoyang/daily-premarket`
- P0 凍結基準分支 `phase2-p0-data-quality` HEAD：`49fd5b0dfd6a9c1b89fc49bb6e4d81ae5fdc4d33`。
- P0 UI 修正／結案分支 `phase2-p0-ui-fixes` HEAD：`a791e4f3a2a15e46cc670b163b2160651df070c3`。
- P0 UI 修正分支相對 P0 基準：ahead 272、behind 0；merge base 為 P0 基準。這不構成 Merge 授權。
- `master` HEAD：`136eb43ebbfd0a59dc2bb715238d5fb9eae42cad`。
- P0 基準與 master 已分歧；compare 顯示 master 相對 P0 ahead 8、behind 290。不得自行 Merge／Rebase／Force Push。
- Recovery 文件分支 `ops/recovery-handoff` 本次更新前 HEAD：`227bcf862d03613d66eff7368886282edadc5c3f`。

### P0 結案證據（沿用既有 PASS，不重跑）
- Unit Contract Audit #106：PASS。
- V9 UI Fixes Regression #136：PASS。
- Daily Premarket V9 Pro #173：PASS。
- Browser Audit #41400089885：PASS；六個分頁 Desktop／Mobile 共 12 次檢查通過。
- P0 結案 Commit：`a791e4f3a2a15e46cc670b163b2160651df070c3`，訊息 `docs(recovery): close Phase 2 P0 semantic audit`。
- P0 結論：目前沒有已知且尚未修正的 P0 程式或 Dashboard 欄位語義缺陷。
- V8、Master、P0 baseline 均未由該結案 Commit 修改；未 Merge、未部署。

### 非 P0 阻斷的後續稽核
| 工作 | 狀態 | 邊界 |
|---|---|---|
| 2026-10-30 TAIFEX／TWSE／TPEX 原始 API payload 逐筆獨立重算 | NOT TESTED | 必須取得原始 payload；不可由 DATA_REPORT 衍生值冒充原始資料 |
| 2026-10-30 GEX 原始 IV／OI 輸入重建 | NOT TESTED | 現有 139 筆 GEX_LEVELS_JSON 只證明模型輸出內部公式與彙總一致，不代表原始輸入已外部對帳 |
| 因子預測力與 walk-forward | NOT TESTED | 需先固定因子定義、時間切分及避免 look-ahead 的驗證方法 |

### 目前資料版本
- `phase2-p0-ui-fixes/data_reports/DATA_REPORT_20261030.md` SHA：`665ae0ce957cbda372a1d70e1f06f0eea124ba11`。
- `phase2-p0-ui-fixes/data_reports/DATA_REPORT_20261102.md` SHA：`8ccd0dfc0f86f80e23253781bf923a533566df96`。
- `phase2-p0-ui-fixes/dashboards/data-20261102.json` SHA：`9e2c50907535d6f070a353eca50722d8c5e98aa1`；T0 2026-11-02，產出時間 14:35:26，GEX 狀態 unavailable。這是當日資料快照，不作為 10/30 原始輸入重建依據。

### 後續工作順序
1. 先做 10/30 原始 API payload 逐筆對帳，確認哪些原始資料可取得、哪些已無法回溯；產出差異清單，不修改 P0 程式。
2. 以已確認的原始輸入重建 10/30 GEX；若原始 IV／OI／結算價／到期資訊不足，明確標 BLOCKED，不用衍生 JSON 反推原始資料。
3. 最後再做因子預測力與 walk-forward，先定義樣本、時間切分、基準、交易成本及評估指標。
4. 這些均屬 P0 結案後的獨立資料稽核／模型驗證，不重新開啟 P0。



## 24. 2026-11-02 10/30 原始 API 對帳：來源盤點（第一輪）

### 程式／資料基準校正
- P0 語義結案 Commit 仍為 `a791e4f3a2a15e46cc670b163b2160651df070c3`，作為 P0 驗收證據錨點。
- `phase2-p0-ui-fixes` 後續另有 GitHub Actions 產生的資料／Dashboard Commit `d5443eacb29b7b0824306de4d1b126b9281210b5`（2026-11-02 07:48Z），其父提交為 P0 結案 Commit；變更只涉及 `dashboards/data-20261030.json`、`data-latest.json`、HTML、manifest 等產出物，未見程式檔變更。不可把這個資料更新 Commit 誤認為新的 P0 修正。
- 10/30 DATA_REPORT：`665ae0ce957cbda372a1d70e1f06f0eea124ba11`；T0=2026-10-30，Actions 產出時間 2026-11-01 23:51:51 Asia/Taipei。
- 主要程式證據：`src/sources/spot_raw.py` SHA `f5d95898b327b9243ee586ad4dd528d4502d7500`；`twse.py` SHA `64964bcc0db7670d49ae3d204ffb7bf5ff647764`；`twse_proxy.py` SHA `6245e8209ce4c54ec14a24d9e9215a112b82bb68`；`spot.py` SHA `92f4f90241c91ec5f1a46570bad439ba9aa3d7f0`；`taifex.py` SHA `d741115b488e8e3c241773d6fcf82d4edda0ba38`；`taifex_official.py` SHA `2fdc4ea61f40078fc35ab3b5f2246becb7de93de`。
- Worker 證據：`workers/twse-proxy_V1.1.js` SHA `1cb3e0a7ac6de4809fb606f73eb09e10da112a0b`；`workers/taifex-proxy_V1.4.js` SHA `f6406554393f57b71f88eaf6fdb75ee73ae2803c`。

### 原始資料保存檢查
- `.github/workflows/daily_data.yml` 只執行 `src/fetch_data.py` 並提交 `data_reports/`、`reports/`；沒有 `upload-artifact` 步驟。
- `src/fetch_data.py` 產出正規化 Markdown DATA_REPORT；本次讀取的版本未見將每個來源 HTTP 原始 response body 寫入檔案／artifact 的流程。
- 因此目前 Git 內的 DATA_REPORT 與 Dashboard JSON 是正規化／衍生結果，不是可直接逐筆重算的原始 API 封存。
- 這是原始 API 稽核的證據保存缺口；不是 P0 程式缺陷，不回頭修改 P0。

### 10/30 現貨來源矩陣（依程式碼與報告註記）
| 欄位 | 來源／端點 | 日期能力（程式可證） | 10/30 原始 payload 狀態 |
|---|---|---|---|
| 加權指數收盤／漲跌 | twse-proxy → TWSE RWD MI_INDEX IND | Worker 帶 `date=20261030` | NOT TESTED；未封存 raw response |
| 上市成交金額／上市漲跌家數 | twse-proxy → TWSE RWD MI_INDEX MS；備援 `twtazu_od?date=` | 帶 T0 日期 | NOT TESTED；未封存 raw response |
| 加權 OHLC | FinMind TaiwanStockPrice，`start_date=2026-10-30` | 可指定起始日期並篩 T0 | NOT TESTED；未封存 raw response |
| 上櫃漲跌／成交金額 | TPEX `tpex_mainborad_highlight` | 無 date query；程式只取第一列並驗證 Date | BLOCKED 待確認歷史列是否仍可取得 |
| 三大法人現貨 | TWSE RWD BFI82U／twse-proxy `/institutional?date=` | Worker 明確註記 RWD 忽略 date、回傳最新日，並回報 actual_date | BLOCKED；目前無原始封存，端點不是可保證歷史回查 |
| 融資融券金額口徑 | HiStock 上市／上櫃 HTML | 程式抓網頁並按 MM/DD 比對列 | NOT TESTED；需檢查頁面是否仍保留 10/30 |
| 自建上市融資維持率 | TWSE RWD `marginTrading/MI_MARGN?date=20261030` + `afterTrading/MI_INDEX?date=20261030&type=ALLBUT0999`，另查缺價股票歷史月資料 | 明確帶 T0；程式要求 payload date 必須等於 T0 | NOT TESTED；可重取性待實際 API 回應確認 |
| 借券餘額 | TWSE TWT96U + TPEX margin_sbl | TWSE TWT96U 無日期參數；TPEX 依回傳 Date 篩選 | BLOCKED/NOT TESTED；報告明確註記 MI_MARGN/TWT96U 無日期欄、採最新可得 |
| 借券賣出餘額／增減 | TWSE TWT93U + TPEX margin_sbl | TWT93U 帶 ROC 日期 1151030；TPEX 依 Date 篩選 | 10/30 報告註記 TWT93U 未取得，賣出增減僅上櫃值；不能視為上市櫃完整值 |

### TAIFEX／GEX 原始來源矩陣
| 欄位 | 原始來源／路徑 | 日期能力（程式可證） | 10/30 狀態 |
|---|---|---|---|
| TXO 行情、履約價、Call/Put、結算價、OI | TAIFEX 網站 `/cht/3/optDailyMarketReport`，POST queryDate | Worker 支援指定歷史日期 | 有可行歷史重取路徑；尚未取得 10/30 原始 response |
| TXO Delta | TAIFEX `/cht/3/dlOptDailyDelta` 歷史清單 + `/cht/3/optDailyDeltaExcel` | Worker 先確認日期在最近 30 交易日清單，再下載指定日期 | 10/30 位於理論回查窗口內；尚未實際驗證清單及下載 |
| TAIFEX OpenAPI fallback | `DailyMarketReportOpt`、`DailyOptionsDelta` | Worker 明確將其視為 latest/current fallback，並要求回傳日期吻合 | 不可先假定能回查 10/30；需以實際日期清單判斷 |
| GEX 標的收盤價 | TWSE FMTQIK | Worker 下載後按日期欄位尋找 T0 | NOT TESTED；尚未取得 10/30 raw response |
| GEX 計算 | Settlement-implied IV → Black-Scholes Gamma；Call 正、Put 負；GEX 乘數公式見 Worker | 可用原始 chain + Delta + TAIEX close 重算 | 尚未重建；現有 139 筆 GEX_LEVELS_JSON 只是衍生輸出 |
| OI 日變化／快照 | TAIFEX Proxy KV snapshots | `/snapshots/bundle?date=` 讀取指定日期，找不到時退回較早 snapshot | DATA_REPORT 取用 2026-10-29 snapshot；10/30 當日 snapshot 是否存在未驗證 |

### 已識別的報告資料品質／來源註記
- 10/30 DATA_REPORT 明確註記「上市 MI_MARGN / TWT96U 無日期欄，採用最新可得」；因此這兩項不可直接宣稱是 10/30 歷史原始值。
- 10/30 DATA_REPORT 明確註記「借券賣出增減僅上櫃值 (TWSE TWT93U 未取得)」；相關欄位不得解讀為上市櫃完整合計。
- DATA_REPORT 的借券來源摘要列與該註記需在逐筆對帳時一起核對，避免來源標籤看似包含 TWSE，但實際僅有 TPEX 值。
- 10/30 現貨三大法人值為外資 -1,124.7 億、投信 +236.2 億、自營商 -513.7 億；因 BFI82U proxy 會回報 actual_date，本次仍需 raw actual_date 證據才能確認值日期。
- 10/30 GEX 139 筆的既有內部公式一致性，不代表原始 chain／Delta／標的價格已獨立重取或對帳。

### 本輪執行限制與狀態
- 已完成程式碼／端點／日期參數／資料保存方式的唯讀追查。
- 嘗試透過目前可用的外部讀取介面直接讀取 Cloudflare Worker、TWSE、TPEX API JSON；這些 API URL 未能在本次執行環境取回有效 payload。因此沒有虛報 HTTP 狀態、raw row count 或 API 數值。
- 10/30 raw API payload 逐筆對帳：NOT TESTED（實際 response 尚未取得）。
- TAIFEX TXO chain／Delta 歷史回查：可行路徑已由程式碼確認，實際取回 BLOCKED（本次無法直接呼叫來源 API）。
- 下一步應使用能直接發送 HTTP GET/POST 的執行環境，按上述 endpoint 與參數擷取原始 response，保存 request URL/body、HTTP status、response date、raw JSON/HTML/Excel 及 SHA-256，再進行逐欄位重算；不需要修改正式程式或重跑 P0。


### GEX 重建輸入契約（Worker V1.4 程式碼確認）
- Chain 每筆必要欄位：`contract_month`、`contract_expiry_date`、`strike`、`type`、`settlement`、`open_interest`。
- Delta 每筆必要欄位：`contract_month`、`contract_expiry_date`、`strike`、`type`、有限數值 `delta`。目前模型用 Delta 數值的有限性建立匹配鍵（strike/type）；Delta 數值本身不直接進入 Gamma 公式。
- 標的輸入：同 T0 的 TWSE TAIEX close（Worker 使用 FMTQIK；不得用 TX futures price 代替）。
- 到期時間：由 Chain 到期日與 T0 計算 days/365。
- IV：以 Chain settlement 作為 Black-Scholes option price，反解 implied volatility（r=0）；不以 last trade／bid／ask IV 取代。
- Gamma：Black-Scholes Gamma；每筆 GEX 公式為 `Gamma × OI × 50 × S² × 0.01`。
- 符號慣例：Call 正、Put 負；Worker 明確標示這是 customer-long/dealer-short 假設，不是 TAIFEX 發布的 Dealer 實際部位。
- Gamma Wall：逐履約價絕對 Net GEX 最大者；Gamma Flip：標的價 ±10% 區間掃描總 GEX，取第一個正負跨越並線性插值。
- 生產品質門檻：模型成功計算筆數／正 OI、正結算價且 Chain/Delta key 匹配筆數至少 50%。
- 因此原始重建必須保留 Chain 與 Delta 的原始完整列、日期、下載 URL／POST body、標的收盤價；只保留 GEX_LEVELS_JSON 不足以獨立重建。


## 26. 2026-11-02 最終收尾決策

本節優先於第23～25節的舊待辦；舊紀錄保留作歷史，不再照舊執行。

- 使用者確認：10/30 TAIFEX／TWSE／TPEX 逐筆比對已多次驗收，沿用既有結果，不重跑、不再總驗收。
- 不新增 Raw API Audit Runner、Fetch Data 機制或 Worker；直接使用現有 DATA_REPORT 與既有驗收紀錄。
- P0 維持 PASS／CLOSED；不修改 P0 baseline、Master、V8、正式 Dashboard 或資料鏈；不 Merge／Rebase／Force Push／部署。
- 10/30 DATA_REPORT（SHA 665ae0ce957cbda372a1d70e1f06f0eea124ba11）含 139 筆衍生 GEX_LEVELS_JSON；underlying=45,211.83；Net GEX=1,294,327,419.01；Gross GEX=6,320,130,202.13；quality=usable。
- 沿用既有 139 筆內部一致性驗收：Net=Call+Put、Gross=abs(Call)+abs(Put)，差異為 0；不重算。
- GEX_LEVELS_JSON 不含原始 Chain、完整 Delta payload 與原始報價，故不能獨立重建原始 IV／Gamma。狀態 BLOCKED，原因為 DATA_REPORT 不含原始輸入；本階段不建抓取工具，將限制記錄後收尾。
- 因子預測力／walk-forward 不屬本次 P0 收尾範圍，不列入待辦。新增 Fetch Data／Runner／Worker 均 NOT IN SCOPE。

結案定義：P0 結案後稽核收尾完成；GEX 原始輸入重建保留 BLOCKED 限制。Auditor 為單模型自我審查，非獨立多模型審核。


## 11. 2026-11-02 法人三市場區塊 A/B Template 與建置來源一致性驗收

- 工作分支：`fix/three-market-correlation-history`。
- 最新程式／Workflow Commit：`38162c1b84ac8f309f618a69d8e9606c82eb737c`（`fix(ci): pin V9 Pro build to triggering branch template`）。
- 區塊 A：現貨法人（億元）、期貨 OI／日夜盤交易流量（口）、選擇權法人日夜盤交易流量（口）拆分獨立圖表；明確區分 OI 存量與交易流量。
- 區塊 B：選擇權法人多空力道標示金額單位（億元），並明確說明非淨交易口數或 OI。
- 選擇權法人表格：標示淨交易口數及日盤／夜盤單位。
- 建置來源防呆：第一個 checkout 固定使用觸發本次 workflow 的 `github.sha`；新增來源驗證，確認工作目錄 HEAD 與觸發 SHA 一致，且 Template worktree blob SHA 與該 Commit 內的 Template blob SHA 相同。
- Master checkout 改名為「Checkout master dashboard source for Pages root only」；只用於 Pages 根目錄，V9 Pro 新版產物仍放在 `p0/`。
- GitHub Actions Run `41475229916`：completed / success；build job 成功，Deploy 依分支保護條件 skipped（未部署）。
- Run Artifact `13156417750`（`github-pages`，1,780,599 bytes，未過期）。
- 本次新增來源驗證步驟 PASS；10/30 Golden Fixture 與正式建置 HTML inline JavaScript syntax check PASS；Pages artifact 組裝與上傳 PASS。
- Master、V8、P0 baseline 未修改；未 Merge／Rebase／Force Push／部署。
- 實際瀏覽器／手機視覺驗收：NOT TESTED；Golden Fixture 語法通過不等於畫面驗收。
- 本輪 Auditor 為單模型自我審查，非獨立多模型審核。


## 12. 2026-11-02 A/B 實際 Artifact 視覺檢查與金額精度修正

- 實際下載並解壓 Run `41475229916` Pages Artifact，使用 Chromium + Playwright 在桌面 1440px 與手機尺寸 390px 渲染 `p0/v9-pro-20261102.html`。
- DOM bounding-box 檢查：A/B 標題與副標題沒有幾何重疊；390px viewport 的 body scrollWidth=390，無水平溢出。
- 視覺檢查發現 Hn 共用圖表格式器將金額一律以整數顯示，造成 +0.18 億元顯示成 +0 億元、現貨 -1124.7 億元顯示成 -1125 億元；這是數值精度缺陷，不是排版重疊。
- 已修正 `templates/v9-pro-react-template.html` 的 Hn：單位為「億元」時，絕對值小於 1 的非零數值顯示 2 位小數，其餘顯示 1 位小數；口數等非金額仍顯示整數。文字寬度測量與實際繪製共用同一 formatter，避免加上單位後超出預留文字寬度。
- 修正 Commit：`a320c876ccb9dfdac909df5cb68f61d4bf051437`。
- GitHub Actions Run `41476324893`：completed / success；build job 25 steps success、無 failed steps；Deploy job skipped（未部署）。
- Artifact `13157138161`（github-pages，1,780,850 bytes，未過期）。
- 已下載新 Artifact 並檢查實際產出的 `p0/v9-pro-20261102.html` 確實含新 formatter。
- 新 Artifact 手機 390px Chromium 視覺檢查：區塊 A 金額顯示 -1,124.7 億元、+236.2 億元、-513.7 億元；區塊 B 顯示 +0.18、-0.06、-3.0、+1.8、-0.54 億元，精度保留且文字未與圖示重疊；body scrollWidth=390。
- 桌面 Chromium 視覺檢查曾以舊 Artifact `41475229916` 確認版面結構；新版本桌面截圖尚未另行重拍。
- 狀態：CI／正式 HTML／Golden Fixture PASS；新 Artifact 手機尺寸 Chromium 模擬 PASS；實體手機及使用者手機瀏覽器 NOT TESTED；正式 Pages 部署 NOT DONE。
- 本輪 Auditor 為單模型自我審查，非獨立多模型審核。
