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


## 13. 2026-11-03 區塊 A/B 手機版排版與選擇權力道表格修正

- 工作分支：`fix/three-market-correlation-history`。
- Template Commit：`be9c27adc3bc4491cd932930d31736f053695b2e`。
- 修改範圍僅限 `templates/v9-pro-react-template.html`，未修改資料計算引擎、資料來源、分析邏輯或其他 Dashboard 區塊。
- A/B RWD：新增 `v9-market-ab-grid`、`v9-market-a-card` 專用 CSS；viewport <=1100px 時 A/B 改單欄上下排列，>1100px 保留原桌面版 A 佔 2 欄、B 佔 1 欄。
- 區塊 B 表格：修正原本錯誤使用雙欄 key/value helper `ee` 呈現 7 欄資料的問題。原 helper 只讀取每列前兩格，導致畫面錯誤地只顯示法人與日多方第一欄數字。
- 改為 7 欄原生 HTML table：法人、日多方、日空方、日淨、夜多方、夜空方、夜淨；保留三大法人合計列。表格加上橫向捲動容器，避免手機壓縮數字。
- 區塊 B 新增定義文字：單位億元；多方／空方為來源力道分項；日淨／夜淨為來源淨額欄位；說明不是成交口數或未平倉 OI。未更動來源計算口徑。
- 依 DATA_REPORT_20261102.md 的「法人多空力道表」確認實際 9 欄資料結構；Dashboard 顯示前 7 個分析欄位，來源與日淨－夜淨欄位不塞入主表，以免混淆。
- CI Run `41478733638` 已完成 HTML build、JavaScript syntax validation、Pages artifact assembly/upload；Artifact `13157839737`（github-pages，1,782,342 bytes，未過期）。截至 recovery 更新時 GitHub Actions build job 的 post-checkout cleanup 仍顯示 in_progress，尚未把整個 Run 結果標成 completed。
- 本輪尚未取得新 Artifact 的實際手機瀏覽器截圖；RWD 目前是程式／CI 層級驗證，實體手機視覺驗收 NOT TESTED。
- 未 Merge、未部署；Master 與 V8 未修改。
- 本輪 Auditor 為單模型自我審查，非獨立多模型審核。


## 14. 2026-11-03 手機實際畫面驗收（使用者提供截圖）

- 使用者已開啟 CI Run `41478733638` 所產生的新版 `p0/v9-pro-latest.html`，並提供手機瀏覽器實際畫面截圖。
- 手機 A/B 排版：PASS。區塊 A、B 已上下排列，不再左右擠壓。
- 區塊 B 七欄力道表：PASS。法人、日多方、日空方、日淨、夜多方、夜空方、夜淨均有顯示；三大法人合計列存在。
- 表格單位／定義：PASS。億元、多空力道分項、日夜淨額，以及非成交口數／非 OI 的說明均顯示。
- 數值一致性抽查：PASS。依畫面顯示，日淨合計 +0.18 -3.01 +1.82 = -1.01；夜淨合計 -0.06 +0.00 -0.54 = -0.60，與三大法人合計列相符。
- 手機畫面未見 A/B 重疊、七欄表格文字互相覆蓋或數字被裁切。此為使用者實際手機截圖的視覺驗收，不代表所有手機型號／縮放比例均已測試。
- CI Run `41478733638` 已確認 completed / success，HEAD `be9c27adc3bc4491cd932930d31736f053695b2e`。
- A/B 本輪手機驗收：PASS。正式部署／合併：仍未執行，除非使用者另行明確授權。
- Auditor：單模型依程式差異、CI 狀態及使用者截圖自我審查，非獨立多模型審核。


## 15. 2026-11-03 區塊 B 選擇權法人多空力道動態分析升級

### 程式盤點發現
- 原始資料：DATA_REPORT 的「法人多空力道表」包含外資／投信／自營商／三大法人合計，日盤與夜盤多方金額、空方金額、淨額及日淨－夜淨差。
- 上游欄位：TAIFEX Proxy 的 long_amount／short_amount 來自買方／賣方契約金額欄位；src/fetch_data.py 的方向分類公式為：
  - 多方契約金額＝買 Call 契約金額＋賣 Put 契約金額。
  - 空方契約金額＝賣 Call 契約金額＋買 Put 契約金額。
  - 上游單位千元，除以 100,000 轉成億元。
- 這是按買賣方向與 Call／Put 分類的契約金額代理值，不是淨權利金現金流，也不是 OI／實際持倉；不得直接稱為資金流入或真實持倉。
- 原本 Builder 只解析並傳遞 instOptForce，Template 區塊 B 的 look／compass／target 為固定寫死通用句，未依當日數據改變。這是本輪真正的分析缺陷。
- 本區塊沒有呼叫 LLM；本輪新增的是可測試、可重現的規則式動態判讀，不應宣稱為即時生成式 AI 推理。

### 本輪修改
- scripts/v9_pro_builder.py：新增 build_option_force_analysis()，驗證必要法人列、欄位完整性、淨額＝多方－空方、日淨－夜淨及三法人合計；對缺值不補零、對不一致資料停止方向判讀。
- 新增日盤／夜盤主導空方與多方抵銷者分析；計算淨額佔多空雙邊契約金額合計比例；明確解釋日淨－夜淨是兩時段差，不是日對日變化。
- 將 B 區金額淨額與 A 區法人淨交易口數逐法人、逐時段交叉比較；分為同向、背離、中性，不用一種量綱覆蓋另一種量綱。
- 最終 JSON options.instOptForceAnalysis 已接入；Template 不再使用固定通用句，改讀 Builder 動態結果。
- B 區副標題／圖表備註補上多空金額分類公式及代理指標限制；圖表、七欄表格與計算引擎均保留。
- 新增 tests/test_builder_option_force_analysis.py；Workflow 加入專屬分析契約測試及既有選擇權表格回歸測試。既有一項過時測試字串（測試期待「三市場方向分歧」、程式實際輸出「跨市場訊號分歧」）已只修正測試期待，未改動原分析功能。

### 11/02 T0 範例數據判讀
- 日盤合計：多方 21.57 億、空方 22.58 億、淨額 -1.01 億；淨額／雙邊金額合計約 -2.29%。
- 夜盤合計：多方 7.70 億、空方 8.29 億、淨額 -0.60 億；淨額／雙邊金額合計約 -3.75%。
- 日盤主要空方為投信 -3.01 億，自營商 +1.82 億提供最大多方抵銷；夜盤主要空方為自營商 -0.54 億，投信為 0。
- 日淨－夜淨合計差 -0.41 億；明確說明為日盤淨額減夜盤淨額，不代表日對日變化。
- A 區口數交叉比較：4 組同向、1 組背離、1 組中性；唯一背離為外資日盤金額 +0.18 億、淨交易 -167 口。此背離被納入判斷及後續觀察條件。
- 上述比例依 DATA_REPORT 已四捨五入至小數二位的顯示金額估算；不是使用未四捨五入 raw payload 重算。

### CI／Artifact
- 最新程式 HEAD：07696e52086101692311f60d020e47c7972150d7。
- GitHub Actions Run 41481675963；截至本紀錄更新時 build job 24 個成功步驟、0 failed，仍在 post-checkout cleanup，整體 Run 尚未回報 completed。
- 專屬 options-force contract tests：PASS；既有 option table regression tests：PASS；17F offline self-tests：PASS；Dashboard JSON build：PASS；正式 HTML 與 10/30 Golden Fixture JavaScript syntax check：PASS；Pages Artifact upload：PASS。
- Artifact 13159728345（github-pages，1,785,704 bytes，未過期）。
- 已下載 Artifact，檢查 p0/data-20261102.json 的 options.instOptForceAnalysis 結果與 p0/v9-pro-latest.html 注入內容一致；預期分析字串、金額口數背離、時段差及公式備註均存在。
- 實際 Chromium 瀏覽器渲染：NOT TESTED（此執行環境對 file://／localhost 回報 ERR_BLOCKED_BY_ADMINISTRATOR；headless CLI 渲染逾時）。需由使用者開啟 Artifact 新 HTML 提供手機畫面驗收。
- Endpoint 級別的每個 options day/night API response date 未保留在法人力道表中；本輪沿用 DATA_REPORT T0／來源標籤，未修改來源擷取流程。Endpoint 級別日期獨立對帳：NOT TESTED。
- Merge／部署：NOT DONE；V8、Master 未修改。Auditor 為單模型自我審查，非獨立多模型審核。

### 下一步
1. 確認 Run 41481675963 最終 completed／success。
2. 使用者下載 Artifact 13159728345 的 p0/v9-pro-latest.html，檢查 B 區三段動態分析文字、公式說明、七欄表格及手機版是否重疊／裁切。
3. 根據實際手機畫面複驗文字可讀性；視覺驗收前 B 區分析升級不可結案。
4. 不 merge、不部署，除非使用者另行明確授權。

## 16. 2026-11-03 區塊 B 手機畫面複驗與數字格式修正

### 使用者手機截圖驗收
- 使用者提供新版區塊 B 完整手機畫面。
- 圖表、七欄表格、分析／判斷／操作區在截圖範圍內未見重疊或裁切；圖表與表格欄位對應清楚。
- 數據／敘述交叉複核：
  - 日盤合計淨額 -1.01 億；夜盤 -0.60 億；來源日淨－夜淨差 -0.41 億，算術一致。
  - 日盤淨額／多空雙邊金額合計約 -2.3%；夜盤約 -3.8%，與顯示值一致。
  - 日盤主要空方投信 -3.01 億；自營商 +1.82 億為最大多方抵銷；夜盤主要空方自營商 -0.54 億，與分法人表一致。
  - A 區口數對照 4 同向、1 背離、1 中性；外資日盤金額 +0.18 億與淨交易 -167 口背離，交叉比對成立。
- 發現一項顯示格式缺陷：投信夜淨原始字串 +0 被表格直接顯示，未統一兩位小數。

### 修正
- templates/v9-pro-react-template.html：表格數字顯示層改為統一兩位小數；多方／空方欄顯示 0.00，淨額正值加 +、負值保留 -、零值顯示 0.00；非數字內容原樣保留。未改上游數據及分析計算。
- tests/test_react_template_static.py：新增格式規則靜態契約測試。
- Template commit：fb6924901cf7700e90e9a38faaf54219b5bb02f9。
- Test commit：5a3ec0f82c23fad5122beea43f3acfa0a1db6dec。
- 新版 template CI Run 41486390048：主要 build 步驟 24/26 完成，含 options force analysis tests、17F tests、dashboard build、HTML JS syntax、artifact upload 均成功；最後 checkout cleanup 當時仍 in progress。
- 新增靜態格式測試的 CI Run 41486406787：排隊中，尚未執行／驗證。
- Run 41486390048 Artifact 13161328313（github-pages，1,786,028 bytes，未過期）。
- 本輪截圖視覺驗收：截圖範圍 PASS；修正後格式畫面尚未由使用者複驗。
- 尚未 merge／部署；V8／Master 未修改。獨立多模型 Auditor 未執行。

### 下一步
1. 確認 Run 41486390048 最終 completed／success。
2. 確認 Run 41486406787 的新增格式測試與完整 workflow PASS。
3. 交付修正後 Artifact 的新版 HTML，請使用者確認投信夜淨顯示為 0.00，並快速複查七欄表格。
4. 完成上述複驗前，區塊 B 不結案、不 merge、不部署。

## 17. 2026-11-03 區塊 B Artifact 路徑釐清與格式修正交付

- CI Run 41486390048：completed / success；Artifact 13161328313。
- CI Run 41486406787：completed / success；新增格式靜態契約測試通過；Artifact 13163070059。
- Workflow .github/workflows/daily-premarket-v9-pro.yml 明確將 Master dashboard 複製至 Pages 根目錄，並將觸發分支產物複製至 pages-site/p0/。
- 因此 Artifact 根目錄 v9-pro-latest.html 是 Master 舊版，不是本次 P0 驗收目標；正確新版是 p0/v9-pro-latest.html。先前只檢查根目錄並判 Artifact FAIL，屬驗收路徑選錯，已更正。
- 已檢查正確 P0 HTML：新版 B 標題、v9-force-table、instOptForceAnalysis、numeric.toFixed(2)、cellIndex===3||cellIndex===6 均存在。
- p0/data-20261102.json 的 options.instOptForce 資料含投信夜淨 +0；顯示層會轉為 0.00，原始資料未改。
- Node.js 對格式邏輯執行 7 組邊界案例：+0、正淨額、負淨額、一般數值、文字、null、千分位數值，7/7 PASS。另以靜態檢查確認 5 個新版 HTML 必要標記全數存在。
- 已從 Artifact 抽出正確 P0 HTML 為 /mnt/data/v9-pro-latest-format-fixed.html，供使用者手機實際複驗。
- Chromium headless 手機截圖嘗試逾時，未產生畫面；瀏覽器實際渲染／手機排版仍 NOT TESTED。
- Pages deploy job 為 skipped（本 workflow 當次未部署）；未 merge、未部署。Master 根目錄保持原版，P0 新版留在子路徑。
- 區塊 B 狀態：CI PASS；Artifact source/path PASS；格式邏輯 Node smoke test PASS；手機視覺複驗 NOT TESTED，尚未結案。

### 下一步
1. 請使用者開啟本輪交付的 v9-pro-latest-format-fixed.html，確認投信夜淨顯示 0.00，並檢查整個 B 區塊手機寬度、表格、文字是否重疊／裁切。
2. 若畫面 PASS，區塊 B 才可結案；否則依截圖修正。
3. 不合併、不部署，除非使用者明確指示。

## 18. 2026-11-03 區塊 B 手機實機畫面驗收

- 使用者提供格式修正版 HTML 的手機截圖，已直接檢查。
- 區塊 B 圖表、法人六組項目、七欄表格、分析／判斷／操作文字均完整顯示；截圖可見範圍內沒有重疊、裁切或欄位錯位。
- 投信夜盤淨額在表格正確顯示為 0.00；圖表顯示 0.0 億元，符合圖表精度與表格精度分工。
- 正負值、單位、欄位標題及表格行列對應均通過手機視覺驗收。
- 區塊 B 手機視覺驗收：PASS。結合前述 CI、HTML source/path、格式邏輯測試，B 區塊本輪格式修正可結案。
- 審核保留事項：畫面可見部分，外資日盤多方 11.36 減空方 11.17 與淨額 +0.18 存在 0.01 億元的顯示精度差；日盤各法人分項加總與合計也可能因各欄獨立四捨五入出現 0.01 差。因目前未能讀取同版原始未四捨五入數值，本次不將其判定為計算錯誤，也不宣稱精度對帳 PASS。應於下一輪資料數值稽核以原始精度確認，若屬正常四捨五入，於 UI 說明或計算規則中明確定義。
- 本次只驗收 B 區塊截圖可見內容；下方其他區塊、整頁不同手機尺寸、橫向模式與跨瀏覽器仍 NOT TESTED。
- 未 merge／部署；Master／V8 未修改。

### 下一步
1. B 區塊格式修正結案，不再反覆修改。
2. 進入下一個尚未完成的 P0 驗收項目；沿用完整驗收：資料來源／計算／HTML 注入／CI／Artifact 正確路徑／手機實機畫面。
3. 將 0.01 億元精度差列入數值對帳清單，以原始未四捨五入值確認，不阻塞本次 B 區塊版面與格式結案。


## 18. 2026-11-03 區塊 B 手機實機驗收
- 使用者提供格式修正版 HTML 手機截圖。區塊 B 圖表、法人六組指標、七欄表格、分析／判斷／操作文字完整；截圖可見範圍無重疊、裁切或欄位錯位。
- 投信夜盤淨額表格顯示 0.00；圖表顯示 0.0 億元，符合各自呈現精度。正負號、單位及欄位對應通過。
- B 區塊手機視覺 PASS；結合兩次 CI success、P0 Artifact 正確路徑及 7 組 Node 格式測試，本輪格式修正結案。
- 保留數值精度待查：外資日盤 11.36－11.17 與淨額 +0.18 差 0.01 億元，可能是各欄獨立四捨五入；尚未取得同版原始未四捨五入值，故數值精度對帳 NOT TESTED，不判定錯誤。下一輪以原始精度確認。
- 本次只驗收 B 區塊截圖範圍；其他區塊、其他手機尺寸、橫向模式、跨瀏覽器 NOT TESTED。未 merge／部署；Master／V8 未修改。
- 下一步：B 區塊不再反覆修改；進入下一個未完成 P0 驗收項目，沿用資料來源、計算、HTML 注入、CI、Artifact 正確路徑、手機實機六層驗收。0.01 億元精度差列入數值對帳清單。


## 19. 2026-11-03 下一區塊：三劇本路徑條件修正（進行中）
- B 區塊格式修正已由使用者手機截圖驗收 PASS；本節轉查截圖下方「三劇本路徑」。
- 原 Template Pth() 根因：偏多只要存在任一高於現價的 GammaWall／CallWall 即可顯示，未要求有效 Gamma Flip；偏空只要任一低於現價的 GammaWall／Flip 即可顯示，未要求現價低於 PutWall；因此觸發條件文字與路徑完整性不一致。
- 修正後條件：偏多須有有效 Gamma Flip、現價高於 Flip、且至少一個有效上方壓力；區間須 PutWall < 現價 < CallWall；偏空須現價低於有效 PutWall，且至少一個有效下方支撐。缺必要價位時不繪製路徑。
- 文案改為只陳述最新現價與關鍵位相對位置；「站穩／有效跌破」需後續價格行為確認，不冒稱單一現價已確認觸發。
- Template commit f87dad314976ad6c4d26125f7a4c37d72f92b6b4；CI 測試工作流 commit 8d0fe6f9f5ab4780facbb9fc62f130dc7b409c3c；測試修正後 HEAD dca0dc9706407b5757d747f5cd608f7419dd86b9。
- 新增 React Template／三劇本契約測試並接入 Workflow。最新 Run 41559500824：該測試步驟 PASS，含正式 inline JavaScript syntax check；實際 Pth() 六組情境案例於執行環境 6/6 PASS。
- Run 41559500824 整體 FAIL，阻斷於既有 Replay real historical DATA_REPORTs：20261027 eligible=0、cumulative=0、expected=1；同段出現 SQLite init_db missing primary-key date 訊息。這與本次 Pth() 修改無關，需獨立釐清；後續 Dashboard build／Artifact 因此 skipped。
- 三劇本修正目前：邏輯單元測試 PASS、正式 Template JS syntax PASS；整份 Workflow FAIL（歷史回放阻斷）；最新 Artifact／完整 Dashboard 注入／手機視覺 NOT TESTED，尚不可結案。
- 未修改 V8／Master；未 merge／部署。Auditor 為單模型自我審查，非獨立多模型審核。

### 下一步
1. 先查清 history replay 為何在 20261027 eligible=0 並出現 DB schema 訊息；不以 continue-on-error 或跳過測試掩蓋。
2. 修復／確認 CI 可完成後，檢查正式 Artifact 中 Pth() 是否使用 triggering branch Template，並核對 T0 現價、PutWall、CallWall、GammaWall、Flip 的來源值。
3. 用代表性 fixtures 驗證三劇本：有效偏多／缺 Flip、區間有效／價位錯側、有效偏空／缺 PutWall、缺支撐及零／缺值。
4. 再產出手機 Artifact，複驗三劇本卡片及多空條件檢查表；未完成前不結案、不部署。


## 19. 2026-11-03 三劇本路徑修正與 CI 全流程驗證
- 原 Pth() 缺陷已修正：偏多需有效 Gamma Flip 且現價高於 Flip，另需上方壓力；區間需 PutWall < 現價 < CallWall；偏空需現價低於有效 PutWall，另需下方支撐。缺必要價位不顯示路徑，並明確標示站穩／有效跌破仍待價格行為確認。
- 新增的六組實際 Pth() 執行測試已通過；測試曾因 React children 文字空白未正規化造成斷言失敗，已修正測試，不更動價格路徑條件。
- 歷史回放失敗根因已查明：Yahoo ^TWII range=1mo 對歷史 T0 過濾後只剩 14 個交易日；RSI14 至少需要 15 個收盤價，故 RSI 缺值並被品質門檻正確排除。已把抓取窗口改為 3mo，未放寬有效樣本門檻。
- 最新 commit c3a4e238e25e0f54c3c994c072c053622ac47782；CI Run 41559674941 整體 SUCCESS。
- 本次 CI PASS 項目：Template source/ref 驗證、三市場情境測試、React Template／三劇本契約測試、選擇權契約測試、17F self-test、真實 DATA_REPORT 歷史回放、Gamma fallback、歷史資料 seed、Dashboard build、Golden Master 注入、Golden Fixture inline JS syntax、Pages artifact upload。
- Pages artifact github-pages 已上傳（artifact id 13196591720，約 1.79 MB）。Deploy job SKIPPED，因本次為工作分支；未 merge／部署，Master／V8 未修改。
- 狀態：邏輯與 CI = PASS；Artifact 已產生但內部 HTML／JSON 尚未人工抽查 = NOT TESTED；手機實機三劇本與下方多空條件檢查表 = NOT TESTED；正式部署 = NOT DONE。

### 下一步
1. 下載 Run 41559674941 的 github-pages artifact，人工核對 HTML／JSON、Template branch/ref、T0 現價及 PutWall／CallWall／GammaWall／Flip。
2. 使用者手機開啟同一份 HTML，逐項驗收三劇本卡片及多空條件檢查表，特別檢查長文字換行、數字／圖表重疊及缺值狀態。
3. 手機驗收 PASS 後再更新結案狀態；未經使用者明確授權不 merge／deploy。


## 20. 2026-11-03 Artifact 實際內容抽查
- 下載 Run 41559674941 的 github-pages artifact 並解壓；確認 P0 產物在 p0/ 子目錄，p0/manifest.json 指向 20261102、data-20261102.json、v9-pro-20261102.html。artifact root HTML 是舊 Pages root，未誤用。
- p0/v9-pro-latest.html 包含更新後 Pth()；注入資料為 2026-11-02，現貨 44920.14，PutWall 44000、CallWall 48000、GammaWall／Flip 缺值。
- 對 Artifact 真正 HTML 的 Pth() 執行函式以實際資料執行 Node 檢查：偏多 blocked、區間 valid、偏空 blocked，與資料條件一致，PASS。
- 已抽取手機複驗 HTML：/mnt/data/v9-pro-20261102-scenario-fixed.html，303,448 bytes，SHA-256 e22783b01067a0de641665012c48827d4f8144b827d28b5126ce82716addec63。
- Artifact 結構／manifest／注入資料／實際路徑邏輯 PASS；手機視覺 NOT TESTED。未 merge／部署，Master／V8 未修改。

### 下一步
1. 使用者在手機瀏覽器開啟上述 HTML；應顯示偏多未成立、區間成立、偏空未成立。檢查三劇本卡片、條件表、字體換行、數字及圖表是否重疊。
2. 手機畫面 PASS 後，繼續下一個未完成 P0 區塊；不 merge／deploy，除非使用者明確授權。


## 20. 2026-11-03 三劇本修正 CI／Artifact 驗證
- Build HEAD c3a4e238e25e0f54c3c994c072c053622ac47782；branch 另含 Yahoo TWII 3mo lookback 調整，補足歷史 RSI14 回放資料，屬獨立提交。
- Actions Run 41559674941 completed / success；Artifact 13196591720；Deploy skipped。
- 三劇本契約測試、inline JS syntax、歷史 DATA_REPORT replay、correlation seed、Dashboard JSON build、Golden Fixture HTML／JS validation、Artifact upload 均 PASS。
- Artifact 正確新版 p0/v9-pro-latest.html；資料 p0/data-20261102.json；manifest 日期 20261102。HTML 內嵌 JSON 與獨立 JSON 完全一致，T0 均為 2026-11-02。
- T0 輸入：spot.close=44920.14；PutWall=44000；CallWall=48000；GammaWall=null；Flip=null。區間成立；偏多因 Flip 缺值不成立；偏空因現價高於 PutWall 不成立。舊程式會錯誤顯示偏多／偏空延伸路徑，此次已抑制。
- Chromium file:// 渲染遭 ERR_BLOCKED_BY_ADMINISTRATOR；桌面／手機實際畫面 NOT TESTED。HTML 抽取至 /mnt/data/scenario-artifact/p0/v9-pro-latest.html。
- Pth() runtime 6 案例 PASS；CI／HTML syntax／Artifact source-data consistency PASS；桌面／手機視覺待使用者驗收。
- 未 Merge／部署；Master／V8 未修改。

### 下一步
1. 使用者手機開啟新版 HTML，確認偏多與偏空條件未成立、區間路徑正常，文字沒有重疊／裁切。
2. 同時檢查多空條件檢查表的 Bias、因子權重及缺失因子是否與 JSON 一致。
3. 視覺 PASS 後再結案；B 區 0.01 億元精度差仍列後續對帳。


## 21. 2026-11-03 手機驗收與 Bias 因子圖表修正
- 手機截圖視覺初步 PASS：區塊 C、三劇本、因子圖、相關性熱圖、交易計畫未見明顯重疊／裁切；截圖範圍未見橫向溢出。三劇本「機率未校準」標籤正確。現價 44,920.14 位於 PutWall 44,000 與 CallWall 48,000 之間，區間成立；偏多缺 Flip、偏空未跌破 PutWall，兩者不成立。
- 發現多空圖表誤用 u.weights 作為方向貢獻，造成正值綠色權重柱與 Bias 24 偏空語意相反，且顯示英文程式 key。已改用 factor_details.active 的 contribution，按絕對值排序取前 8，使用中文名稱及正負顏色；標題改「多空因子方向貢獻」，明示正值推升 Bias、負值壓低 Bias，非權重。
- 新增靜態契約測試；第一次因測試字串跳脫錯誤 FAIL，修正後 Run 41560578070 整體 SUCCESS，React template tests 19/19、inline JS 4 scripts、Artifact upload PASS；deploy SKIPPED。
- Artifact 13196638130 已下載抽查；新 HTML p0/v9-pro-20261102.html，date 2026-11-02，Bias 24 偏空，14/17 有效因子。前 8 貢獻值：外資現貨 -7.1429、美股費半 -7.1429、夜盤 -4.7619、PCR -3.3333、現貨趨勢 -1.9345、投信 +1.7857、MACD -1.7857、Put Wall +0.8929。
- 手機複驗檔 /mnt/data/v9-pro-20261102-factor-contrib-fixed.html，303,829 bytes，SHA-256 d82b30b923d70538570163febf80764ca5fc57b91551786d8cee570cf430843d。
- 狀態：舊版手機排版初步 PASS；舊版因子語意 FAIL 已修正；新版 CI／Artifact／HTML data PASS；新版手機視覺 NOT TESTED；未 merge／部署；B 區 0.01 億元精度差仍未結案。

### 下一步
1. 手機驗收新版因子貢獻圖：中文名稱、紅負綠正、Bias 24 偏空語意一致，無重疊。
2. 通過後處理 B 區 0.01 億元精度差，再做全頁最終驗收。
3. 未經使用者明確授權不 merge／deploy。

 
## 22. 2026-11-03 因子方向貢獻圖空白修正
- 手機驗收上一版因子圖空白，FAIL。根因：綜合分析頁 y2 解構 `options:l`、`analysis:u`，圖表卻讀 `l.factor_details`；正確來源是 `u.factor_details`，導致空陣列。
- Template 已修正圖表資料 filter 及缺失因子名稱 lookup 均讀 `u.factor_details`；靜態測試改為明確斷言正確來源。
- CI Run 41561549286 / commit c97b970dd29fc05664fbdb2b251b7f4ef6735f3e SUCCESS；JS 4 scripts PASS；React template 因子圖測試 PASS；Artifact 13196699558 上傳成功，deploy skipped。
- Artifact 實際 HTML 已抽查，確認使用 `u.factor_details`；注入資料 14 個有效因子，前 8 貢獻值：外資現貨 -7.1429、美股費半 -7.1429、夜盤 -4.7619、PCR -3.3333、現貨趨勢 -1.9345、投信 +1.7857、MACD -1.7857、Put Wall +0.8929。
- 新 HTML `/mnt/data/v9-pro-20261102-factor-contrib-fixed-v2.html`，303,829 bytes，SHA-256 `0dc550e7a6adb19e324fa1ed7af7308605a614092c061d9beda8ce1dc886bf72`。
- 狀態：程式／CI／Artifact 靜態資料來源核對 PASS；手機視覺 NOT TESTED；未 merge/deploy；Master/V8 未修改；B 區 0.01 億元精度差未結案。
 
### 下一步
1. 手機複驗 fixed-v2 因子圖是否實際出現 8 條正負貢獻。
2. 通過後處理 B 區 0.01 億元精度差，再執行 42 區塊最終驗收。
3. 未授權不 merge/deploy。

 
## 23. 2026-11-03 因子圖 8 列顯示高度修正
- 手機截圖顯示因子圖只有 7 列；根因是 Canvas 高度 240px，繪圖公式每列 30px、起始餘量 2px，最多繪製 7 列。
- 已將因子圖高度調整為 260px，新增靜態測試鎖定此設定。未改變因子值、Bias 或排序。
- CI Run 41562071919 SUCCESS；React template tests、因子圖測試、JS syntax、Golden Fixture build PASS；Artifact 13197570937 已上傳，deploy skipped。
- 新版 260px 高度的手機畫面仍 NOT TESTED；尚未 merge/deploy。B 區精度差與 42 區塊總驗收仍未完成。
 
### 下一步
1. 從 Artifact 13197570937 取得新版 HTML並確認 260px。
2. 手機確認 8 列均顯示。
3. 處理 B 區精度差，再進行 42 區塊總驗收。

 
## 24. 2026-11-03 八列因子圖新版 HTML 已從 CI Artifact 抽取
- Artifact 13197570937 / Run 41562071919 中抽取 `p0/v9-pro-20261102.html`，輸出 `/mnt/data/v9-pro-20261102-factor-chart-8rows-v3.html`（303,829 bytes；SHA-256 `a0cc47e5a566f272438d48fdcae03f5a4dfa837affdf29b54f9a3626e15e7bba`）。
- 實際 HTML 已確認高度 260px；對應 data JSON 有 14 個有效因子，前 8 名第 8 項為 Put Wall +0.8929。
- 手機驗收仍 NOT TESTED；B 區精度差與 42 區塊總驗收未完成；未 merge/deploy。
 
### 下一步
1. 手機確認 8 條（含 Put Wall +0.9）完整顯示且無重疊。
2. 修正 B 區 0.01 億元精度差，進行 42 區塊總驗收。

 
## 25. 2026-11-03 因子圖 V3 手機實機驗收 PASS
- 使用者手機截圖確認 8 列全部顯示，含 Put Wall +0.9；無裁切，中文標籤與正負顏色正常。因子圖 8 列顯示問題結案。
- 下一項：追查區塊 B 外資日盤多方 11.36、空方 11.17、淨額 +0.18 億元的 0.01 差異。先取 TAIFEX Proxy 原始千元 long_amount / short_amount 未格式化值，重算並確認是否獨立四捨五入；目前僅有格式化 JSON 字串，原因仍 NOT TESTED。
- 不得未查原始值就判定 rounding；若屬正常獨立四捨五入，補註而非強制改算式；若不符，修正資料鏈與測試。
- 未 merge／部署；42 區塊總驗收未完成。


## 26. 2026-11-03 其他區塊解析文字動態化（進行中，尚未手機驗收）
- 使用者要求延續 A／B 區塊解析文字修正經驗，全面檢查其餘區塊解析；解析必須由當日 Dashboard data 推導，與圖表、價位及缺值狀態一致。
- 工作分支：`fix/three-market-correlation-history`；目前 HEAD：`0a397dc3e2c4e13e1bdb5149c6e1a679e206a284`。
- 變更檔案：`templates/v9-pro-react-template.html`、`tests/test_react_template_static.py`。新增 `v9ProSynthesisAnalysis()`，將五組解析改為動態推導：C 日夜盤劇本、三劇本路徑、多空因子方向貢獻、相關性熱圖、交易計畫。
- 日夜盤解析交叉判讀日夜收盤、成交量占比、外資夜盤淨交易及 OI；三劇本依現價與 Put／Call Wall、Gamma Flip／Wall 有效性列出條件成立與否；因子解析計算正負及淨貢獻、主要因子與缺失因子；相關性解析辨識最強正負配對並說明不代表因果；交易計畫依價格位置及關鍵位給出條件式觀察，不單靠 Bias 產生追價指令。
- 修改 commits：Template `bfafaec57521744d91e52a2dc49d87a2175350a1`；解析測試 `57166c2b92a5baae030ced64eca43a321ed145dd`；Template 修正 `0b3f51959a7b93590ca178e5f8e2fd5bbca3e2a8`；最新測試修正 `0a397dc3e2c4e13e1bdb5149c6e1a679e206a284`。
- CI Run `41563655940`，HEAD 與工作分支一致，整體 SUCCESS。Build job 中 Template source/ref、資料來源與分類測試、三市場情境、React Template／三劇本契約、選擇權法人力道、17F self-test、歷史 DATA_REPORT correlation replay、Gamma fallback、Dashboard build、Golden Master 注入、Golden Fixture HTML JavaScript 驗證、Pages artifact upload 均 SUCCESS；deploy job SKIPPED（工作分支）。
- CI PASS 不等於解析內容與畫面已驗收：最新 Artifact 的五組解析實際注入值、HTML 內容及手機畫面仍 NOT TESTED。不得宣告完成。
- 先前 Run `41563482857`、`41563515516`、`41563640245` 曾 FAIL；最新 HEAD `0a397dc...` 的 Run `41563655940` 已 SUCCESS。
- 未 merge／部署；Master／V8 未修改。Auditor 為單模型自我審查，非獨立多模型審核。

### 下一步
1. 抽查 Run `41563655940` Pages Artifact，確認最新 HTML 使用 triggering branch Template，五組解析的 data binding 正確，並以當日 JSON 執行解析函式，測試缺值、零值及反向情境。
2. 核對解析文字與圖表同源，檢查正負號、單位、關鍵位、Bias、有效因子數及相關性配對。
3. 以最新 Artifact 進行手機驗收：解析可讀性、換行、重疊、裁切及圖表一致性。
4. 通過後再進入 42 區塊全頁驗收；B 區 0.01 億元精度差仍待查。未經使用者明確授權不 merge／deploy。


## 2026-11-03 Artifact 驗收與解析邊界修正
- 舊版 Artifact Run 41563655940 / Artifact 13197767563 已抽查：正確 P0 路徑 `p0/`、manifest 日期 20261102、HTML 內嵌 JSON 與獨立 JSON 完全一致。
- 五組解析以真實 JSON 執行並與數據核對：日夜盤 -868 點、夜盤量占比 37.45%、外資夜盤 +1,365 口；現價 44,920.14／PutWall 44,000／CallWall 48,000，區間成立；Bias 24、有效因子 14/17、淨貢獻 -26.04；相關矩陣 8×8，最強正／負相關 +0.85／-0.89；交易計畫區間內不追價。
- 邊界測試審查發現缺值觸發文案、零值關鍵價位判斷、相關矩陣維度／係數驗證三項缺陷。已修正 Template 與新增測試。
- Template commit `a0212f191a96a918c4e96e0eb0ff7b787a496cbc`；tests commit `0e59d8cc4350137facdb6924300ad0f25c42928a`；工作分支檔案已讀回確認。
- 新修正版本 CI 尚無可查證 Run ID；狀態 BLOCKED／NOT TESTED，舊 Run 41563655940 不可當成新版本 PASS。新 Artifact／手機驗收 NOT TESTED。
- 未 merge／deploy；Master／V8 未修改；B 區 0.01 億元精度差未解；42 區塊總驗收未開始。

### 下一步
1. 取得並核對 HEAD `0e59d8cc4350137facdb6924300ad0f25c42928a` 的新 CI Run，完整 build 必須 SUCCESS。
2. 抽查新 Artifact 與實際 JSON，重跑缺值／零值／反向測試。
3. 交付新版手機驗收；通過後進入 42 區塊完整驗收。


## 2026-11-03 夜盤反向情境修正追加
- 五組解析反向稽核發現 C 區交易觀察句固定偏空，夜盤上漲時仍可能輸出「夜盤弱勢訊號延續」。已改為依夜盤相對日盤收盤的正／負／零方向分別產生偏強、偏弱、中性觀察；必要價格缺值時不提供價位觸發句。
- 新增測試覆蓋夜盤上漲／下跌反向情境。Template commit `a3a49002c31646b29906b970ac4c1170647636f0`；test commit `882227d153007c7429833c011f826dadd6b8cb99`。
- 工作分支最新已知 HEAD `882227d153007c7429833c011f826dadd6b8cb99`；兩檔已讀回確認。
- 最新修正版本 CI 仍 NOT TESTED／BLOCKED（目前可用 GitHub 連線無法查詢 push-triggered run 清單或手動 dispatch；combined status 空值不代表 PASS）。新 Artifact／手機驗收 NOT TESTED。
- 未 merge／deploy；Master／V8 未修改；B 區 0.01 億元精度差未解；42 區塊總驗收未開始。

### 下一步
1. 取得 HEAD `882227d153007c7429833c011f826dadd6b8cb99` 的新 CI Run ID，完整 build 必須 SUCCESS。
2. 抽查新 Artifact 並重跑五組解析實際 JSON、缺值／零值／反向測試。
3. 交付手機驗收；通過後進入 42 區塊完整驗收。


## 2026-11-03 五組解析 Artifact 驗收進度
- GitHub 工作分支 HEAD 已從交接快照的 `0a397dc3...` 前進至 `6aa7ac665a5f47cbc6f1634d3e8988f26c848d58`；最新測試 commit 增加反向價位情境斷言。
- 最新 CI Run `41564828844` 對應最新 HEAD，整體 SUCCESS；Build 全步驟 PASS、Artifact `13197918949` 上傳 PASS，deploy SKIPPED。
- 已抽查正確 P0 Artifact：`p0/v9-pro-20261102.html` + `p0/data-20261102.json`，manifest 日期 20261102；HTML 內嵌 JSON 與獨立 JSON 完全一致。
- 五組解析已以 Artifact 真實 JSON 執行；日夜盤、三劇本、因子貢獻、相關性配對、交易計畫數值及邏輯與圖表資料源核對 PASS。
- 缺值、零值、夜盤上漲／下跌反向、錯誤相關矩陣、反向價位情境 runtime 測試 PASS。
- 最新手機驗收檔：`/mnt/data/v9-pro-20261102-synthesis-verified.html`；SHA-256 `c0104af557a855d9ddf8b024c7166a0d17d225208ad62c867f5b281ab4b24f29`。
- 手機畫面 NOT TESTED；B 區 0.01 億元原始精度對帳 NOT TESTED；42 區塊全頁驗收 NOT STARTED。
- 未 Merge／Deploy；Master／V8 未修改。單模型自我審查，非獨立多模型 Auditor。
- 下一步：使用者手機驗收最新 HTML；通過後查 B 區原始金額精度，再進入 42 區塊總驗收。


## 2026-11-03 手機截圖審查與 C 區單位修正
- 使用者提供的五區塊截圖未見明顯重疊／裁切；視覺初步 PASS。長文字及熱圖小字仍可改善。
- 發現 C 區日夜量圖顯示 74.0／44.3，但缺少千口縮放標示；已在 template 為兩個圖表項目增加 `extra:"千口"`，chartNote 同步解釋右側圖表以千口顯示。原始數據卡口數不變。
- 修正 Commit `ca4fe9d1a044f802182e10f74b3fdac45251c9c5`；CI Run `41566032790` SUCCESS，Build PASS、Artifact upload PASS、Deploy SKIPPED。
- Artifact ID `13199196057`；manifest date 20261102；HTML 內嵌 JSON 與獨立 JSON 一致。
- 新 HTML SHA-256 `2aca4c218351d1c0759d2099bea0087e9e6e5ed83daf29403881950ccfd0cea1`；手機驗收檔 `/mnt/data/v9-pro-20261102-synthesis-unitfix.html`。
- 修正後版本手機重驗 NOT TESTED；B 區 0.01 億元精度差 NOT TESTED；42 區塊驗收 NOT STARTED。
- 未 Merge／Deploy；Master／V8 未修改。Auditor 為單模型自我審查。
- 下一步：手機重驗修正後 C 區單位及五區塊版面，通過後對帳 B 區精度差，再進入 42 區塊總驗收。


## 2026-11-03 五區塊主動稽核與 MaxPain 分類修正
- 最新使用者截圖中 C 區顯示 74.0／44.3 千口，原始卡片仍為 73,987／44,305 口；可見範圍無明顯重疊。
- 釐清資料版本：根目錄 `dashboards/data-20261102.json` 並非此次手機截圖所用 P0 Artifact。正確 P0 Artifact `p0/data-20261102.json` 為 Bias 24、14/17、8×8 correlation、樣本 5/5；內嵌 JSON 與外部 JSON 一致。最強正／負相關 +0.854／-0.9053，顯示 +0.85／-0.91。
- 主動發現交易計畫原本將 Put Wall 與 MaxPain 同列「支撐」，與 MaxPain 僅磁吸參考的規格矛盾。已修改為支撐只列 Put Wall、另列「磁吸參考」MaxPain；新增靜態測試防回歸。
- Template commit `e923f2dde34b011407263a4831b2e58a363bb354`；test commit／最新 HEAD `d335c755644840f61e7ca7f386900126f5cd17da`。
- CI Run `41566885386` SUCCESS；Build 全步驟 PASS、React template 測試 PASS、Artifact upload PASS、deploy SKIPPED。
- Artifact ID `13199517282`；digest `ddc9e03e52f44bf0c669dc93d6108c307f2a966c390aae68f130a705b0b86aab`；P0 HTML SHA-256 `a0ceeb82731a98c33947cc5c9ed7e911dd977dd6869228f4c536e3842f7a066c`；P0 JSON SHA-256 `aaf5cc488a2d86f7abadbe3c9ed0ab05417863ba726c6bcf30dde2caed25a980`。
- 新手機驗收檔 `/mnt/data/v9-pro-20261102-maxpain-fix.html`，314,009 bytes。Artifact 已確認包含「千口」及獨立「磁吸參考」列。
- 五組數據／解析核對 PASS；最新版本手機重驗 NOT TESTED；B 區 0.01 億元精度差 NOT TESTED；42 區塊驗收 NOT STARTED。
- 未 Merge／Deploy；Master／V8 未修改。Auditor 為單模型自我審查。
- 下一步：手機重驗最新版五區塊，尤其交易計畫新增列；通過後對帳 B 區精度，再進入 42 區塊總驗收。


## 2026-11-03 最新手機截圖複驗
- 使用者已在手機實際開啟 MaxPain 修正版並提供截圖。
- 截圖可見範圍無卡片重疊、文字／圖表覆蓋或千口單位碰撞；交易計畫的 Call Wall、現價、MaxPain（磁吸參考）、Put Wall（支撐）分列正確。
- 可見範圍結構排版 PASS；手機雙欄縮放導致文字偏小，列為可讀性改善項目。交易計畫下半部及全頁底部未完整呈現在截圖，故完整手機全頁驗收 PARTIAL／NOT COMPLETE。
- 下一步：取得交易計畫下半部及頁面底部手機截圖，確認裁切／溢出；再處理 B 區 0.01 億元精度差。不得把本次可見範圍 PASS 擴張為全頁手機 PASS。


## 2026-11-03 五區塊手機驗收與 B 區精度對帳
- 使用者追加手機向下捲動截圖，與前一張合併覆蓋五個目標區塊完整內容；五區塊手機直向結構驗收 PASS。未見重疊、覆蓋、裁切、價位／單位碰撞。手機雙欄縮放字偏小列為可讀性改善項目。
- 交易計畫支撐 Put Wall 44,000、磁吸參考 MaxPain 44,400、壓力 Call Wall 48,000 分列正確。
- TAIFEX 官方 2026-11-02 原始值（千元）：Call 買 479,793、Call 賣 466,820、Put 買 650,588、Put 賣 655,894。
- 多方=(479,793+655,894)/100,000=11.35687→11.36 億；空方=(466,820+650,588)/100,000=11.17408→11.17 億；淨額=(1,135,687-1,117,408)/100,000=0.18279→+0.18 億。0.01 億差異由各欄獨立四捨五入造成，非錯誤。
- B 區模板備註已加入獨立四捨五入說明；template commit `ac75f9ba1d1bc4c48f8c8c7ec5b56b3516733df6`。新增靜態測試，最新 HEAD `e678877bc076e157c948483d40f136e0f504303e`。
- CI Run `41568199233` 與 `41568208858` 已觸發；最新 HEAD Run `41568208858` 當時 pending，尚未 PASS。
- B 區原始精度對帳 PASS；UI 新備註的 CI／Artifact／手機驗收 PENDING；42 區塊總驗收 NOT STARTED。
- 未 Merge／Deploy；V8／Master 未修改。Auditor 為單模型自我審查。
- 下一步：確認 Run `41568208858` 結果及 Artifact，檢查 B 區備註與資料 JSON 不變，再手機確認備註可讀性；之後進入 42 區塊總驗收。


## 2026-11-03 B 區精度說明 CI／Artifact 結果
- 最新 HEAD `e678877bc076e157c948483d40f136e0f504303e`；CI Run `41568208858` SUCCESS，HEAD 精確相符。Build PASS、React template 測試 PASS（含新備註斷言）、option force analysis 測試 PASS、Artifact upload PASS、Deploy SKIPPED。
- Artifact ID `13200545155`，size 1,807,354 bytes，digest `c80d9596a33f77d8f87d9997f50238dcdf5e0cad93ec2725546d2409b8b3f654`。
- Artifact P0 HTML 314,159 bytes，SHA-256 `d98eec6560462a21d63d4df03f8d3bdf950b2442a0d8f1f8de6190b37af28839`；P0 JSON 62,774 bytes，SHA-256 `aaf5cc488a2d86f7abadbe3c9ed0ab05417863ba726c6bcf30dde2caed25a980`，與原版一致；HTML 內嵌 JSON = 外部 P0 JSON。
- 新版 HTML 確認有四捨五入說明；手機驗收檔 `v9-pro-20261102-rounding-note.html`。
- B 區原始數據對帳 PASS；備註／CI／Artifact PASS；最新備註手機可讀性 NOT TESTED；42 區塊總驗收 NOT STARTED。
- 未 Merge／Deploy；Master／V8 未修改。下一步請使用者手機確認新增備註排版，通過後開始 42 區塊總驗收。


## 2026-11-03 最新手機驗收與 42 區塊總稽核
- B 區四捨五入說明手機可讀性：PASS；文字完整、無截斷／重疊／遮蓋。字體偏小但放大可辨識，列為非阻斷改善項。
- 本輪五區塊（B 精度說明、C 夜盤劇本、三劇本路徑、多空因子方向貢獻、相關性熱圖、交易計畫）手機畫面未見重疊、裁切或單位碰撞：PASS。
- CI Run 41568208858、Artifact 13200545155、資料 JSON 未變更之核對結果沿用前節：PASS；Deploy SKIPPED。
- 42 區塊全頁稽核：IN PROGRESS（尚未逐項完成）。不可將五區塊驗收擴張為 42 區塊 PASS。
- 下一步：固定最新 P0 Artifact／T0，盤點 42 區塊，逐一完成來源、DATA_REPORT、Builder／JSON、圖表、解析文字與缺值／反向情境驗證；所有缺陷修正後需重新回歸。
- 未 Merge／Deploy；Master／V8 未修改。Auditor 為單模型自我審查，非獨立多模型審核。


## 2026-11-03 42 區塊稽核基準固定
- 工作分支 HEAD：`fix/three-market-correlation-history` / `e678877bc076e157c948483d40f136e0f504303e`；Recovery branch HEAD 更新後：待本次寫入後查證。
- Run `41568208858` completed / success，head_sha 精確匹配；Artifact `13200545155` 已重新下載。
- 固定稽核資料：P0 Artifact `p0/data-20261102.json` SHA-256 `aaf5cc488a2d86f7abadbe3c9ed0ab05417863ba726c6bcf30dde2caed25a980`；HTML SHA-256 `d98eec6560462a21d63d4df03f8d3bdf950b2442a0d8f1f8de6190b37af28839`；T0 DATA_REPORT SHA `8ccd0dfc0f86f80e23253781bf923a533566df96`。
- Template SHA `513ecee347f8df931196b46dd7a0f798902fc576`；Builder SHA `c4e49dfcf047cb86bd1592bf2ffdeb3e6121581f`。
- 防錯：工作分支根目錄 `dashboards/data-20261102.json` SHA `9e2c50907535d6f070a353eca50722d8c5e98aa1`，不是 P0 Artifact JSON，禁止混用。
- 結構盤點：Artifact JSON 有 48 個 `analysis.cards` 解析鍵；Template 初步找到 34 個主要卡片元件呼叫點及 8 個 KPI 格。與使用者確認的 42 個可見區塊尚未逐項對映，不能以此粗略相加／替代完整清單。
- 狀態：T0／Artifact／程式版本固定 PASS；42 個可見區塊對映與逐項資料鏈驗證 IN PROGRESS／NOT YET TESTED。
- 下一步：對照四頁實際 render tree 建立精確 42 項清單，再逐項追蹤 source → DATA_REPORT → Builder → Artifact JSON → chart/table → analysis/judgment/action，測試缺值、零值、反向及單位邊界。


## 2026-11-03 42 個可見區塊結構盤點結果（已對帳）
- 固定 Artifact `13200545155` 實際 render tree 確認本版為六頁：總覽／現貨／重要市場／期貨／選擇權／綜合分析；舊筆記「四頁」判讀錯誤，已更正。Builder 規格亦為六頁，禁止為遷就舊筆記改動頁面架構。
- 可見卡片 34 張：總覽 5、現貨 6、重要市場 2、期貨 6、選擇權 8、綜合分析 7；總覽另有 8 KPI 格，總計 42。
- 8 KPI：加權收盤、外資現貨、台指日盤、台指夜盤、外資期貨、PCR、Call Wall、Bias。
- JSON `analysis.visible_block_count=42`，Builder `visible_block_count=42`；48 個 `analysis.cards`／`analysis_card_count` 是內部敘述卡，不是可見 UI 區塊。結構計數 PASS。
- 42 區塊逐項資料鏈稽核仍 IN PROGRESS；本次沒有改動任何 Builder／Template／資料／UI 程式，也沒有 Merge／Deploy。
- 下一步：按六頁清單逐項核對來源、DATA_REPORT、Builder、JSON、圖表與分析／判斷／操作；已驗收正確者凍結不動。


## 2026-11-03 總覽 KPI 首輪資料鏈結果：期貨 OI 狀態矛盾
- 六個直接資料 KPI（加權收盤 44,920.14、外資現貨 -1,124.7 億、TX 日盤 45,301、夜盤 44,433、OI PCR 0.57、Call Wall 48,000）DATA_REPORT → P0 JSON 對帳 PASS。
- 外資期貨淨 OI 0 口為可疑值：三法人 OI 全 0，Builder 的 classify_futures_oi 已判定不納入方向判斷；但 V9Analyzer 仍把 foreign_fut 當 active factor，P0 JSON effective_weight=9.52381，confidence=high。
- 確認 FAIL：可疑 OI 狀態沒有傳遞到 Bias 因子引擎，Bias 24 雖可由現行程式重現，但輸入有效性／confidence 標示不一致。離線反事實估算排除該因子後 Bias 約 21、coverage 約 77.9%（僅估算，非修正後正式輸出）。
- 僅讀取與記錄，沒有改動程式／資料／UI。已 PASS 的區塊凍結，不重做。
- 後續先完成其餘區塊稽核，最後彙整缺陷一次提出最小修正，避免反覆修補造成迴圈。


## 2026-11-03 現貨頁 6 區塊稽核結果
- A 大盤行情：FAIL。T0 OHLC open/high/low 為 null；React 分析文字及 Candlestick `Pt` 未做 null guard，null 被 JS coercion 成 0，會生成錯誤開低走高／影線／實體與無效圖形。
- B 漲跌家數：PASS。上市家數與報告一致；上櫃 null 由 Canvas 明確顯示 unavailable，分析文字不對缺值作方向推論。
- C 三大法人現貨：PASS。外資 -1,124.7、投信 +236.2、自營 -513.7、合計 -1,402.2 億與報告一致。
- D 融資融券：PASS（缺值防護）。融資及維持率 null 由 UI 顯示 unavailable；融券與借券餘額對應有效值。
- E 借券／券：FAIL。表格顯示借券賣出 unavailable，但共用 Canvas `Ol` 將 null 轉成 0 畫圖。
- F 成交結構：FAIL。上櫃成交金額 null 被 `Ol` 畫成 0；表格可能顯示 null億；total 7,588.8 仍標成上市櫃合計，實際僅等於上市成交額。資料一致性檢查因 OTC null 而跳過合計驗證。
- 現貨頁合計：3 PASS（B/C/D）、3 FAIL（A/E/F）。僅記錄缺陷，沒有修改程式／報告／JSON／HTML。修正待 42 區塊清查彙總後一次執行。


## 2026-11-03 42 區塊清單計數方法校正
- 正確邏輯區塊分布：總覽 7（KPI 群組 1 + Bias 盤前偏向 1 + 側欄五卡 5）、現貨 6、重要市場 8（七市場卡 + 新聞）、期貨 6、選擇權 8、綜合分析 7；合計 42。
- 重要市場 map 會展開成七張獨立卡，不能只算一個呼叫點；總覽八個 KPI tile 是一個 KPI 區塊，不是八個獨立分析區塊。上一筆錯誤拆法已作廢。
- 六頁 42 區塊結構映射 PASS；逐項資料鏈驗收仍 IN PROGRESS。未修改程式。


## 2026-11-03 重要市場頁首輪結果
- 7 組市場資料（美股、亞洲、美股期貨、美債、匯率、ADR、商品）共 28 個值均與 DATA_REPORT／P0 JSON 對應；來源日期與單位欄位目前一致。數值映射 PASS。
- 美債水準用 %、日變化用 pp；2Y Treasury XML 備援、10Y／30Y Yahoo 備援，UI 單位標示正確。
- FAIL：React h2() 將市場卡的分析物件 i 初始化為空物件，故 7 張市場子卡的 compass／target 全部使用泛用 fallback，沒有接入 JSON analysis.cards 已產生的專屬判讀。look 仍由 UI 正確組出原始市場數值。
- 重大新聞 12 則數量對應 DATA_REPORT，資料呈現 PASS；逐則時效與內容稽核 NOT TESTED。
- 本輪唯讀，沒有程式或資料修改。


## 2026-11-03 期貨頁首輪結果
- 日盤 OHLC／量／基差與 DATA_REPORT 對帳 PASS。
- 夜盤 OHLC／量／漲跌與 DATA_REPORT 對帳 PASS；FAIL：夜盤變化 -868 被傳入 Pt(basis=...)，圖表固定印「基差 -868」，表格定義則正確為夜盤變化。
- 期現價差圖將夜盤變化 ÷10 並標示還原方式，表格保留原值，PASS。
- 法人 OI：FAIL，可疑三法人全零仍當一般數字顯示並以紅色標示 0；沿用 OI 狀態傳遞缺陷群。
- 日夜法人交易流量與 OI 存量分列，日夜淨額對帳 PASS；但 OI 可疑狀態未顯示，納入同一缺陷群。
- 夜盤劇本量占比 37.45% 算式與報告一致；不預設方向，PASS。
- 本頁無程式修改。


## 2026-11-03 選擇權頁首輪結果
- PCR／成交量結構：成交量與 OI 對帳 PASS；PCR 0.57 = Put OI 34,887 / Call OI 61,578 四捨五入；成交量占比與 PCR 分開呈現。
- 主要 OI 集中：FAIL。Call Top4 + Put Top4 混合資料送入 Ct(type="call")，整條曲線套 Call 紅色，Put 點未以 Put 綠色區分。
- Call OI Top10、Put OI Top10：各 10 筆對帳 PASS。
- 關鍵價位：Call Wall 48,000、Put Wall 44,000、MaxPain 44,400 對帳 PASS；Gamma Wall／Flip null，UI 顯示 unavailable，不補 0，PASS。
- 選擇權法人交易與前十大選擇權數值對帳 PASS。
- GEX unavailable 狀態正確傳遞，空圖欠缺圖內提示列為非阻斷改善。
- B 區金額精度說明維持既有 PASS，不改動。
- 本頁僅記錄，無程式修改。


## 2026-11-03 綜合分析頁首輪結果
- A 三市場法人：方向分歧及 OI 可疑警示敘述正確；OI 0 值顯示沿用既有缺陷群。
- B 選擇權法人金額：資料／算法／四捨五入備註／手機驗收 PASS，凍結不動。
- C 日夜盤劇本：價格、量占比、外資夜盤流量對帳 PASS；背離解讀與開盤確認條件 PASS。
- 三劇本路徑：現價在 Put／Call Wall 之間，缺少 Flip/Gamma 時不宣稱偏多／偏空確認，區間觀察 PASS。
- 多空因子貢獻：FAIL，外資期貨 OI 零值被納入 active factor，confidence high 失真。
- 相關性熱圖：FAIL，T0 可疑 OI=0 被標記 correlation_eligible 並納入 5 筆 Pearson 樣本；外資期貨 vs 大盤漲跌 r 含該列=0.0146，排除後 n=4、r=0.9590（不足 min_samples=5，不應顯示）。JSON 內部相關性文字另與 matrix 狀態矛盾。
- 交易計畫：價位、支撐／磁吸／壓力分工及缺值呈現 PASS。
- 本頁無程式修改；既有手機版面 PASS 凍結。


## 2026-11-03 總覽頁首輪結果
- KPI 群組：除外資期貨 OI 0 口可疑外，其餘直接值與 T0 JSON／DATA_REPORT 對帳 PASS；OI 狀態沿用 FAIL。
- Bias 卡：24 分與 JSON 重現一致，但 confidence high 受可疑 OI 因子污染，FAIL。
- 加權 5 日序列與 Put Wall 44,000 映射 PASS；Yahoo 原始 API 回應未獨立重抓，NOT TESTED。
- 三大法人快照 PASS；期選結構快照 PASS（GEX／Gamma 缺值有顯示 unavailable）；美股連動數值映射 PASS。
- 新聞 12 則數量 PASS，首則 UTC／台北時間換算正確；其餘 11 則逐則品質 NOT TESTED。
- 總覽 7 區塊首輪盤點完成；無程式修改。


## 2026-11-03 上游根因定位與避免誤傷的修正邊界
- OI：Worker 通用 number() 將空白／dash 轉 0，OI parser 未驗證欄位有效性；原始 2026-11-02 TAIFEX HTML 未成功取得，故該日是否 dash 被轉 0 NOT TESTED。不可改通用 number()，應限縮 OI nullable parser。
- OI downstream：必須同步處理 Bias factor、coverage/confidence、KPI、OI 卡及 correlation eligibility；P0 DB 已把 T0 零值列為 eligible，save_today_to_db 對既有日期 skip，需另有明確 T0 eligibility 修正步驟。
- turnover：spot.py 通用 _add 同時用於融券／借券，不能全域改；僅 turnover.total 改為兩市場皆有效才計算完整合計。
- UI：Ol null→0、Pt 缺 OHLC 仍運算；需保留 null/0 差異並加測試。其他精確點：夜盤圖標籤、h2() 專屬市場解析接線、Call/Put OI 顏色區分。
- 尚未改碼；先固定修正邊界，避免改到其他共用來源語意。


## 2026-11-03 daily-data 手動觸發日期準則（強制）

- 手動觸發 GitHub Actions 的 `daily-data` workflow 時，`T0 交易日期（t0）` 輸入欄必須留空；**不得直接填入當日日期**。
- 留空後由 `src/fetch_data.py` 呼叫 `src.t0.resolve()`，自動判定 T0 與盤別（日盤／全日），避免手動指定 T0 使程式走入「手動 T0 預設全日」分支，造成資料日期／夜盤查詢節次不符合預期。
- `report_date`（報告產出日期）與 `t0`（交易資料日期）是不同參數。不得因為要產出當日報告，就把當日日期填入 `t0`。
- 排定班別 workflow 若有明確 `slot`／`date` 參數，依該 workflow 的排程契約執行；本規則針對一般手動觸發 `daily-data`，不可混用排程班別參數。
- 若需要指定歷史 T0 進行重抓／回補，必須先確認目標盤別及夜盤查詢日，再使用明確的受控回補流程；不得把一般手動觸發的留空規則自行改成填日期。
- 驗證 11/02 等報告的夜盤缺失時，先查 workflow dispatch 輸入與執行紀錄；若當次手動輸入了 T0 日期，應先視為可能的操作／參數原因，不得直接判定資料源或程式退化。
- 比對資料完整性時，以已確認的完整全日版 DATA_REPORT（目前指定 2026-10-30）作為基準。未確認目標報告是日盤版或全日版前，不得把其缺欄位直接列為資料遺失。

**程式依據（已讀取工作分支原始碼）：** `src/fetch_data.py` 的 CLI 說明指出手動 `--t0` 未指定 `--session` 時預設「全日」；未指定 `--t0` 時呼叫 `src.t0.resolve()` 自動判斷。全日夜盤查詢使用 T0 的下一個交易日。這確認了參數分支差異；但 2026-11-02 當次 dispatch 是否真的填入日期，仍須以該次 workflow run 的實際輸入／紀錄查證，不能僅憑報告缺夜盤推定。


## 2026-11-03 1030／1102 DATA_REPORT 實檔與 Actions 複核
- `phase2-p0-ui-fixes` 的 10/30 全日報告 SHA `665ae0ce957cbda372a1d70e1f06f0eea124ba11`：夜盤、三大法人 OI、前十大 OI 均有值。
- `phase2-p0-ui-fixes` 的 11/02 全日報告 SHA `4add0443546bde87309fc1f13396f3a478e60bb0`（2026-11-03 08:55:11）：夜盤、三大法人 OI、前十大 OI 均有值。
- `master` 的 11/02 全日報告 SHA `38fc2e8a5fe2578e6779ffc11e157fed3e76a8ee`（2026-11-03 12:32:18）：夜盤、OI 均有值；Actions run #98 `41578655028` success。
- Actions run #97 `41556173914` 在 `phase2-p0-ui-fixes` 以 workflow_dispatch 執行，log 證實 `--t0 ""`，自動解析 T0=2026-11-02、session=全日；不能據此推定 11/02 14:35 舊日盤版 run #95 的輸入。
- 舊分支 `fix/three-market-correlation-history` 的 11/02 14:35 日盤版 SHA `8ccd0dfc0f86f80e23253781bf923a533566df96` 有三法人 OI 全零及期貨行情沿用 10/30 數值。該版本不是 11/03 產出的全日版，不能混版比較。
- 結論：目前 10/30／11/02 全日 DATA_REPORT 並未缺夜盤／OI；舊日盤版的 OI 零值仍是資料完整性缺陷。Worker `number()` 將空白／dash 轉 0 的風險已確認，但 11/02 原始 HTML 未取到，當次直接成因仍 NOT TESTED。
- 本輪只讀驗證，無程式／DB／報告／Dashboard 修改，無 Merge／Deploy。下一步：在允許的工作分支對 OI parser 做局部 nullable 修正，並驗證 OI 有效性狀態能阻止零值污染 Bias、confidence 與 correlation；先不動通用 `number()`。



## 2026-11-03 GEX Worker V1.5 診斷修正進度（本次交接更新）

- 工作 repo：`grichtoyang/daily-premarket`。
- 程式工作分支：`phase2-p0-ui-fixes`。
- Recovery 文件分支：`ops/recovery-handoff`。
- 本次核對三個程式檔案遠端內容，確認它們已包含 GEX Worker V1.5 診斷修改（不是只停留在聊天草稿）：
  - `workers/taifex-proxy_V1.4.js` blob SHA：`3f5fdfe3442a106aa21a74706e911f7970258056`；檔案路徑依既有部署引用保留 V1.4 名稱，程式標頭／GEX parser 版本已標示 V1.5。
  - `src/sources/taifex.py` blob SHA：`aebb590370105937c0ad86506c7e8f66d9b8118c`。
  - `tests/test_taifex_gamma_fallback.py` blob SHA：`ff7f83c0a1081f27781eb3dbf2ae08da840e8c08`。
- Worker 已新增 GEX 失敗診斷分類：TXO Chain fetch／parse、TXO Delta fetch、Chain/Delta expiry 配對、TAIEX underlying、GEX internal error；回應增加 `error_code`、`stage`、`detail`，成功回應欄位及 GEX 計算公式不應改變。
- Python 呼叫端新增 Worker error payload 解析與 `_LAST_FETCH_ERRORS` 記錄；HTTP 502、HTTP 200 但 `ok=false` 及 request timeout／failure 不再只留下狀態碼。GEX unavailable 時將錯誤摘要寫入 DATA_REPORT notes；不把失敗值當成有效 GEX。
- 測試檔已新增 HTTP 502 階段／細節保留，以及 HTTP 200 `ok=false` 的 data.reason 保留測試。
- **本次遠端內容核對：PASS**（三檔均讀回且含預期診斷修改）。
- **測試執行：NOT TESTED**（本次尚未取得 GitHub Actions／本機測試結果；不得宣稱測試通過）。
- **Worker 部署：NOT DONE**；未觸發 Worker deploy。
- **DATA_REPORT 實際診斷輸出：NOT TESTED**；尚未以新 Worker 實際產出報告驗證 notes。
- 本次僅更新 Recovery 文件；不改 master、V8、原始 P0 分支，不 Merge／Rebase／Deploy。
- 下一步唯一工作：對照這三個遠端檔案的實際 diff 與測試內容，修正任何審查發現，再執行對應測試；測試通過後才部署 Worker，最後用一次真實 GEX endpoint 呼叫確認錯誤階段能被 Python／DATA_REPORT 接收。



## 2026-11-03 GEX Worker V1.5 CI 審查結果追加

- 程式分支最新查證 HEAD：`e852ee6d8eaab4225b563b2b856ce1f76ad7cb41`（GitHub Actions 自動產生的 `V9 Pro 20261102 Bias 25分` commit；不是 Worker 部署 commit）。
- V1.5 相關三個程式檔案 blob SHA 維持：
  - Worker `3f5fdfe3442a106aa21a74706e911f7970258056`
  - Python `aebb590370105937c0ad86506c7e8f66d9b8118c`
  - Tests `ff7f83c0a1081f27781eb3dbf2ae08da840e8c08`
- CI 首次執行 Run `41626557631` FAIL，原因是新增測試的 Python 多行 with 語法有多餘反斜線；不是產品程式測試斷言失敗。已由 commit `82796f958b3cedd62e077e11a59ac4cd680e5c06` 修正為巢狀 context manager。
- 修正後 Run `41626627855` SUCCESS；Gamma fallback regression step PASS，執行 11 tests，輸出 OK。Builder／其餘工作流程步驟亦成功；Deploy job SKIPPED。
- CI 成功流程另執行 Build、注入、產生 Dashboard history commit 並上傳 Pages artifact；**沒有部署**。該 workflow 的一般 Build／artifact 行為與 Worker 部署不同。
- 程式碼審查：Worker Chain parser 的回傳結構只有 `found/data`，沒有 `reason`，所以新增的 Chain parse detail 會採用固定 fallback 文案；不影響分類，但無法提供更細解析錯誤。其他 Chain／Delta／TAIEX／GEX failure stage 與 Python response parser 欄位名稱目前吻合。
- **Python regression tests：PASS**（Run `41626627855`，11 tests）。
- **Worker JavaScript runtime／Wrangler validation：NOT TESTED**。
- **真實 Worker endpoint 與 DATA_REPORT notes：NOT TESTED**。
- **Worker deploy：NOT DONE**。
- 下一步：補做 Worker JavaScript 語法／部署前驗證；檢查通過後才部署 Worker，部署後再以受控 GEX endpoint 呼叫驗證錯誤階段與 DATA_REPORT notes。不得因 Python tests PASS 就宣稱 Worker 已上線。



## 2026-11-03 Worker V1.5 source-level audit / syntax validation checkpoint

- Re-read Worker, Python source and tests on `phase2-p0-ui-fixes`; the three blob SHAs remain unchanged from the previous checkpoint.
- Source-level audit confirms:
  - Worker classifies Chain fetch/parse, Delta fetch, Chain-Delta expiry mismatch, TAIEX underlying and internal GEX failures.
  - Python `_get()` extracts Worker `error_code`, `stage`, `error`, `detail`, `data.reason`; preserves HTTP status and retries under existing rules.
  - `build()` clears diagnostics at start and appends GEX diagnostics to `notes` only when the T0 Gamma endpoint is unavailable.
  - Existing T0 date check and GEX unavailable behavior remain present.
- **Source-level contract review：PASS** (code inspection only; not runtime validation).
- Attempted to obtain Worker source for local `node --check`, but the execution environment cannot resolve `raw.githubusercontent.com`; GitHub connector is read-only and exposes no workflow-dispatch action. No Wrangler/package config or Worker-specific validation workflow was found in the repository root/workflow listing.
- **Worker JavaScript syntax/runtime validation：BLOCKED** (not executed; do not mark PASS).
- **Real endpoint / DATA_REPORT notes integration：NOT TESTED**.
- **Worker deployment：NOT DONE**.
- Next step: obtain an execution path with repository checkout and Node/Wrangler (e.g. user-run local command or authorized CI workflow); run syntax check before any deployment. No source changes made in this checkpoint.


## 2026-11-03 Worker V1.5 語法驗證阻塞複核

- 再查 .github/workflows/：目前分支現有 workflows 中，daily_data.yml 只有 Python 執行流程；unit-contract-audit.yml 僅執行 Python compile／測試；test-v9-ui-fixes.yml 的 Node／Acorn 步驟只檢查 React template，沒有檢查 Worker 原始檔。
- 上述既有 workflows 均不能在不改 workflow 的情況下驗證 Worker V1.5。此次修改授權僅限三個程式檔案，不擴大修改 CI workflow。
- GitHub connector 可讀取 workflow／檔案，但目前可用工具沒有 workflow_dispatch 或遠端 shell；本地執行環境亦無法取得 exact Worker source，故沒有可執行 node --check 的途徑。
- Worker syntax/runtime validation：**BLOCKED（未執行）**；真實 endpoint／DATA_REPORT notes：**NOT TESTED**；Worker deploy：**NOT DONE**。
- 未修改任何程式、workflow 或部署設定。下一步需在可 checkout repo 且有 Node.js 的環境，對 workers/taifex-proxy_V1.4.js 執行 node --check；通過後才考慮 Wrangler validation／部署。


## 2026-11-03 Worker V1.5 V8 語法解析結果

- 直接由 GitHub 讀取 `phase2-p0-ui-fixes` 的 exact Worker source：`workers/taifex-proxy_V1.4.js`，blob SHA `3f5fdfe3442a106aa21a74706e911f7970258056`，檔案長度 132,720 characters。
- 原始碼只有一個 `export default`，沒有 static import。使用本環境 V8 parser 對完整 source 解析；為相容 script parser，僅在記憶體副本將唯一 `export default` 改成等價的 `const __worker_default__ =`，原始碼與 GitHub 檔案均未修改。
- V8 parser syntax validation：**PASS**。此結果確認完整程式本文可被 V8 parser 解析，但不是 `node --check`，亦不是 Cloudflare Workers runtime／Wrangler validation。
- 本地 Node.js 22.16.0 已確認存在，但因 DNS 無法解析 raw.githubusercontent.com，無法把 exact source 下載到本地執行 `node --check`。
- Worker `node --check`：**BLOCKED（未執行）**；V8 syntax parse：**PASS**；Wrangler／Cloudflare runtime：**NOT TESTED**；真實 endpoint／DATA_REPORT notes：**NOT TESTED**；Worker deploy：**NOT DONE**。
- 未修改任何程式檔案、workflow、Worker 設定或部署狀態。


## 2026-11-03 Worker 驗證環境完整性複核

- 重新讀取 `phase2-p0-ui-fixes` 完整 Git tree（recursive，200 entries，`truncated=false`）。未發現 `wrangler.toml`、`wrangler.json`、`wrangler.jsonc`、`package.json`、Node package lockfile、Vitest/Jest 設定或 Worker 專用測試檔。
- 現有 repository 缺少可直接執行 Wrangler bundle/dev/test 的專案設定與依賴宣告；目前工具亦無 Cloudflare Workers runtime／Wrangler 執行器。
- 因此在目前 repo 結構及工具權限下，無法安全地做 Wrangler validation；不應臨時新增設定或 workflow，因這會超出本輪三檔程式授權範圍並引入部署環境假設。
- 最新驗證狀態維持：V8 full-source syntax parse **PASS**；Python GEX fallback 11 tests **PASS**；Node `--check` **BLOCKED**；Wrangler/runtime **BLOCKED／NOT TESTED**；真實 endpoint／DATA_REPORT notes **NOT TESTED**；deploy **NOT DONE**。
- 本輪只讀 Git tree；未修改任何程式、設定、workflow 或部署。


## 2026-11-03 Worker 版本管理修復：V1.4 還原、V1.5 獨立

### 修復原因
- 前次將 GEX failure diagnostics 修改直接提交到既有路徑 `workers/taifex-proxy_V1.4.js`，造成穩定版本路徑被新版內容佔用；此版本管理方式錯誤。
- 正確策略是保留原 V1.4，另建 `workers/taifex-proxy_V1.5.js`，不得以 V1.5 覆蓋 V1.4。

### GitHub 修復結果（branch: phase2-p0-ui-fixes）
- 原始 V1.4 從 V1.5 修改前的歷史 commit `4f3a9afbaf48fe4c9ee6bd73804ef78e382a3291` 還原。
- V1.4 路徑：`workers/taifex-proxy_V1.4.js`
  - 已讀回 Blob SHA：`f6406554393f57b71f88eaf6fdb75ee73ae2803c`
  - 與歷史版本 Blob SHA 完全一致；內容長度 131,250 characters。
- V1.5 路徑：`workers/taifex-proxy_V1.5.js`
  - 已讀回 Blob SHA：`3f5fdfe3442a106aa21a74706e911f7970258056`
  - 與原先診斷版內容 Blob SHA 完全一致；內容長度 132,720 characters。
- 建立 V1.5 commit：`2156f917eaf38af09fee110a4566e7b4c872ae26`。
- 還原 V1.4 commit：`240d88a21d939daa94a63064f40ea0c12ca1711c`。
- 修復後 branch head：`240d88a21d939daa94a63064f40ea0c12ca1711c`。
- 兩個檔案已從 GitHub 重新讀回核對，版本內容與 Blob SHA 均符合預期。

### 驗收狀態
- 原始 V1.4 歷史版本還原：**PASS**（Blob SHA exact match）。
- V1.5 診斷版獨立保存：**PASS**（Blob SHA exact match）。
- V1.4／V1.5 路徑分離：**PASS**。
- 本次沒有部署 Worker，沒有修改 Cloudflare Worker 線上版本。
- V1.5 V8 syntax parse：沿用先前結果 **PASS**；Node `--check`：**BLOCKED／NOT EXECUTED**；Wrangler／Cloudflare runtime：**NOT TESTED**；真實 endpoint：**NOT TESTED**。
- 部署前應明確選擇 V1.5 檔案；不得再以 V1.4 路徑作為新版部署來源。

### 版本連結
- [V1.4 原始穩定版](https://github.com/grichtoyang/daily-premarket/blob/phase2-p0-ui-fixes/workers/taifex-proxy_V1.4.js)
- [V1.5 GEX 診斷版](https://github.com/grichtoyang/daily-premarket/blob/phase2-p0-ui-fixes/workers/taifex-proxy_V1.5.js)


## 2026-11-03 V1.5 TAIEX historical fetch patch (supersedes temporary V1.6 entry)

- V1.5 production endpoint test (user screenshot): Worker reports `V1.5 - Production`; TXO Chain contracts=3,102 and Delta rows=3,030; GEX stops at `TAIEX_SPOT_UNAVAILABLE` / `taiex_underlying` because 2026-10-30 close is not found by the OpenAPI FMTQIK source.
- Root cause narrowed to TAIEX historical-close fetch path, not Chain/Delta acquisition or GEX calculation. The previous V1.5 used `https://openapi.twse.com.tw/v1/exchangeReport/FMTQIK`, which does not provide the required date-scoped historical lookup.
- Per user direction, do NOT introduce a V1.6 release. The date-scoped TWSE RWD change was applied directly to `workers/taifex-proxy_V1.5.js`; V1.4 remains unchanged.
- V1.5 now requests `https://www.twse.com.tw/rwd/zh/afterTrading/FMTQIK?date=YYYYMMDD&response=json`. Existing row/date normalization and GEX calculation semantics are retained.
- Updated V1.5 commit: `b45a694cea424958b4b90033f615853e3c7d7f04`; Blob SHA: `1af35533028ca1f3163c7fd346ec8c781f743d4c`; file re-read and V8 syntax parse PASS.
- Temporary `workers/taifex-proxy_V1.6.js` was removed to avoid version ambiguity (delete commit `585a0e97f6140f6fe0d9375474d642ad16444c3d`).
- Live TWSE RWD request could not be exercised from the current execution environment. Therefore exact 2026-10-30 response parsing, Cloudflare Worker runtime, real endpoint and GEX calculation remain NOT TESTED. Updated V1.5 is not deployed yet; deployed Worker remains whatever version is currently active until user deploys this patched V1.5.


### V1.5 follow-up: date-regex escaping defect (2026-11-03)

- User's post-deployment endpoint screenshot showed `Invalid TAIEX query date: 2026-10-30`, while Worker reported `V1.5 - Production` and Chain/Delta counts remained 3,102 / 3,030.
- Root cause: the newly added date normalization regexes were over-escaped in the committed JavaScript: `/\\\\D/g` and `/^\\\\d{8}$/`. They therefore matched literal backslash sequences rather than stripping non-digits / validating eight digits.
- Fixed directly in `workers/taifex-proxy_V1.5.js`: regexes now are `/\\D/g` and `/^\\d{8}$/`.
- Fix commit: `ddc516f11840605c7bb704024298bbc395de0b73`; Blob SHA: `b8d09e461175839e178dab30de405c43b14fa7b7`.
- GitHub file re-read SHA matches; V8 syntax parse PASS; local date-normalization check for `2026-10-30` produces `20261030` and passes eight-digit validation.
- This is a source-level fix only. The updated V1.5 must be redeployed to Cloudflare and the real endpoint retested. TWSE RWD response parsing and full GEX success remain NOT TESTED.


## 2026-11-03 DATA_REPORT 歷史 T0 重跑日期混用調查（最新中斷點）

- 最新調查分支：`phase2-p0-ui-fixes`；Recovery 文件分支：`ops/recovery-handoff`。
- 目標：釐清 2026-10-30 DATA_REPORT 在 2026-11-03 晚間手動重跑後，為何混入其他日期快照、部分欄位 unavailable、部分欄位沿用前版。
- 11/03 新報告 workflow Run：`41644283168`；Job：`125945406903`；產出時間 2026-11-03 21:26:27；T0=2026-10-30。
- 新報告檔案 blob SHA（phase2-p0-ui-fixes）：`61b5a8799bec62762a60d5efb3f1099c18084fc5`。舊報告（fix/three-market-correlation-history）blob SHA：`665ae0ce957cbda372a1d70e1f06f0eea124ba11`。
- 新報告含 50 格沿用前版、73 格以本次新抓取覆蓋的註記；欄位值比較證明有部分最新快照日期未對齊 T0。GEX／Gamma Wall／Gamma Flip 仍有 10/30 值，但不得據此認定整份報告日期正確。
- `merge_same_t0()` 的規則已讀取：`protect=True` 時同欄新舊實值不同會沿用舊值；新值 unavailable 時舊值有值則填回；`protect=False` 時新舊實值不同會保留本次新值並計入 overwritten；缺值回填仍會發生。回傳的 filled count 與 overwritten count 是不同計數。
- `main()` 的 protect 判斷已確認只查 `reports/Daily_REPORT_{T0}_*.md`；沒有查同 T0 的 `data_reports/DATA_REPORT_{T0}.md`。因此，即使目標 DATA_REPORT 已存在，只要 reports 目錄沒有符合檔案，就會進入 `protect=False`。這是已定位的程式缺陷。
- TWT93U：`spot_raw.roc8("2026-10-30")` 產生 `1151030`；`twse_twt93u_sbl(roc)` 將此字串直接放入 `TWT93U?response=json&date={roc}`。Log 曾回報「查詢日期小於 94 年 7 月 1 日」。已確認程式傳入民國年格式；但官方端點要求的正確日期格式及修正後真實回應尚未驗證，不能直接宣稱已修好。
- TPEX `tpex_sbl(roc)` 呼叫不帶日期參數的 `tpex_margin_sbl`，逐列要求 `str(row["Date"]).strip() == roc`。本次 932 rows、matched_date_rows=0；尚未取得原始 Date 值樣本，無法確認應如何正規化。
- 舊報告的借券賣出餘額 36,178 張、增減 -1,273 張；新報告同值但來源註記「沿用前版（原來源：TWSE TWT93U + TPEX margin_sbl）」。因此新報告這兩值不是本次 API 成功取得。借券餘額則由 4,651,514 張變成 2,525,111 張，來源為無日期欄位的 TWT96U／GRETAI 最新快照。
- 修正原則：歷史 T0 報告不得混入其他日期快照；無日期 API 必須有日期證據或拒絕納入；同 T0 有效舊值可依明確規則沿用並保留原始來源／日期；protect 判斷須涵蓋 DATA_REPORT 本身。
- 狀態：日期混用根因（無日期端點缺少一致 T0 gate）PASS；protect 判斷漏查 DATA_REPORT PASS；TWT93U 日期格式根因已定位到民國格式傳入，但官方正確格式驗證 BLOCKED；TPEX Date 格式 BLOCKED；舊報告當次原始 API 回應 NOT TESTED。
- 本輪未修改程式、報告、workflow 或資料庫；未 commit 程式、未 deploy、未重跑 workflow、未 merge。
- 下一步唯一工作：先取得 TWT93U 正確日期格式的官方／實際端點證據及 TPEX 原始 Date 值，再提出最小修正與測試清單；未經使用者批准不得修改程式。


## 2026-11-03 歷史 DATA_REPORT 重跑問題：第二輪實檔／程式根因稽核（22:xx）

### 分支與版本固定
- 本次 GitHub compare 同 ref 核對：`phase2-p0-ui-fixes` HEAD `581a808d6db6bea50a971f74a00b695ffbe8b509`；`ops/recovery-handoff` HEAD（本次更新前）`416f69317d658d51267bf9186c984e7f2598e849`；`master` HEAD `9f88de0bd92294df0051f706a0af1018e439bf6f`。
- 程式只讀查核；未改程式、DATA_REPORT、workflow、DB，未 Merge／Deploy。

### Run／報告交叉核對
- 手動歷史重跑 Run `41644283168` / Job `125945406903`，log 明確顯示執行參數 `--date 2026-11-03 --t0 20261030`；因手動指定 T0 且未指定 session，程式判定 `session=全日`。本次目標 T0／盤別選擇正確，不能把本次資料混用單純歸因於 T0 參數。
- Run log 明確顯示：`TWT93U stat not OK: 查詢日期小於94年7月1日`；`TPEX margin_sbl total_rows=932 matched_date_rows=0`；同時印出「同 T0 覆蓋模式：尚無報告，以本次抓取為準」及「同 T0 保護：沿用前版 50 格有值」。
- 本次產出 `data_reports/DATA_REPORT_20261030.md` blob `61b5a8799bec62762a60d5efb3f1099c18084fc5`。舊版已知完整報告在 `fix/three-market-correlation-history`，blob `665ae0ce957cbda372a1d70e1f06f0eea124ba11`。兩份不可混稱同一版。
- 2026-11-02 全日報告在 `phase2-p0-ui-fixes` blob `4add0443546bde87309fc1f13396f3a478e60bb0`，夜盤及三法人 OI 有值；`master` 同日全日報告 blob `38fc2e8a5fe2578e6779ffc11e157fed3e76a8ee` 亦有值。另有舊分支 11/02 日盤版，不得拿來與全日版直接比較。

### 已確認程式缺陷／風險
1. **同 T0 protect 判斷錯誤（CONFIRMED FAIL）**：`src/fetch_data.py` 在 `out.exists()` 後，`has_report` 只搜尋 `reports/Daily_REPORT_{T0}_*.md`，沒有把已存在的 `data_reports/DATA_REPORT_{T0}.md` 本身納入保護條件。若沒有 Daily_REPORT，即使 DATA_REPORT 已存在仍會進入 `protect=False`。本次 Run 因此以新抓取覆蓋既有實值；log 顯示 50 格沿用舊值、其餘 73 格被本次抓取覆蓋。這是報告混版的直接程式根因。
2. **TWT93U 日期格式錯誤（CONFIRMED）**：`spot.build()` 傳入民國日期 `1151030`；`spot_raw.twse_twt93u_sbl()` 直接作為 API `date` 參數。該端點日期參數使用西元 `YYYYMMDD`（例如 `20250829`），故本次被官方拒絕。應改傳 `20261030`，並以真實回應驗證。
3. **TPEX 日期字串比對（ROOT CAUSE LIKELY；RAW SAMPLE NOT TESTED）**：`tpex_sbl()` 以 `str(row['Date']) == '1151030'` 嚴格比較；本次 932 rows、0 matched。尚未取得本次原始 Date 值樣本，不能猜定它是 `115/10/30` 或其他格式。應先取樣，再用明確正規化後比對 ISO T0；無法解析／日期不符時 fail closed。
4. **無日期 TWT96U 最新快照混入歷史 T0（CONFIRMED RISK）**：`spot_raw.sbl_tw()` 讀取 TWT96U 的 `AvailableVolume`，端點沒有日期欄，`spot.build()` 卻在歷史 T0 重跑時照樣採用最新值。10/30 報告的該欄從舊版 4,651,514 變為 2,525,111，來源註記由舊來源變成 TWT96U/TWT96U GRETAI/TPEX 最新快照。官方定義 TWT96U 是「當日可借券賣出股數／限額」，不是「借券餘額」；官方亦區分「借券餘額」與「借券賣出餘額」。此處有日期混用與欄位語義問題，必須先決定正確指標／來源，不能只把最新值硬塞回歷史 T0。
5. **TWT93U parser index 尚待原始 JSON 核驗（NOT TESTED）**：程式目前使用 `row[7]`、`row[11]`；官方 TWT93U 表頭順序與 API list index 需以實際 JSON `fields`／data row 對齊，不能僅憑 HTML 表格推定 index。未核對前不得改 index。

### 目前狀態
- T0=2026-10-30、session=全日：PASS（Run log 已證實）。
- protect 判斷漏查 DATA_REPORT：FAIL／根因已確認。
- TWT93U 日期參數：FAIL／根因已確認；修正後真實 endpoint 尚未測試。
- TPEX Date 格式：BLOCKED（缺原始 Date 樣本）。
- TWT96U 無日期快照歷史隔離與指標語義：FAIL／修正設計待定。
- TWT93U row index：NOT TESTED。
- 11/02 全日報告夜盤／OI 缺失：未由目前實檔證據支持；不可將舊日盤版誤認為全日版。
- 本次未改碼／未跑測試／未重跑 workflow／未部署。

### 下一個唯一工作（不擴大到 42 區塊）
1. 在 `phase2-p0-ui-fixes` 先修正 DATA_REPORT 自身 protect 判斷，並新增同 T0 重跑 regression：既有 DATA_REPORT 無 Daily_REPORT 時仍 protect；只有明確 `--force-rewrite` 才允許覆寫。
2. 以原始 API response fixture 核對 TWT93U 的 `fields`、row 長度與欄位 index；將查詢日期改為西元 `YYYYMMDD`，測試日期與欄位對應。
3. 擷取 TPEX `tpex_margin_sbl` 真實 Date 值樣本，再實作可辨識格式的日期正規化；同時檢查 TPEX highlight／margin 的 Date 比對是否同類問題。
4. 對無日期 TWT96U／MI_MARGN 歷史回補設 fail-closed 規則；TWT96U 指標名稱需與官方「當日可借券賣出限額」一致，不得稱為借券餘額。保留舊 T0 已驗證值時，來源與日期必須明確標註。
5. 完成後只在工作分支執行 CI／實際 endpoint 驗證；先抽查 10/30 與 11/02 全日報告，再決定是否需要歷史報告重建。未經明確授權不 Merge／Deploy；Master／V8 不動。


## 2026-11-03 DATA_REPORT protect 第一階段修正已提交（CI 待確認）
- 工作分支 phase2-p0-ui-fixes：先前 HEAD 581a808d6db6bea50a971f74a00b695ffbe8b509；最新 HEAD 1e15691a1c0964f626786779561e702fde3c7bee。
- src/fetch_data.py commit 9a576b97bfbc9030308a68eac07546abad9f1cc2，blob SHA cd33a860f27d4d7d3bd3a7289174c42e8e9fadf6：新增 _should_protect_existing_data_report(data_report_exists, force_rewrite)；只要 DATA_REPORT 已存在且未指定 --force-rewrite 就進入 protect，不再依賴 reports/Daily_REPORT 是否存在。更新模式 log 明確標示需 --force-rewrite 才可覆蓋。
- tests/test_dashboard_unit_contract.py commit／最新 HEAD 1e15691a1c0964f626786779561e702fde3c7bee，blob SHA 0b9a6142aebfafc7f5e9f1b2bcc6f7a3f101fae9：新增測試覆蓋既有 DATA_REPORT、無 force → protect；有 force → 不 protect；沒有既有 DATA_REPORT → 不 protect。
- GitHub compare 581a808... → 1e15691... 僅兩檔變更：src/fetch_data.py、tests/test_dashboard_unit_contract.py。兩檔均從 GitHub 讀回，確認 helper／測試存在，舊 has_report = bool(...reports/Daily_REPORT...) 判斷已移除。
- CI：GitHub combined status 查詢回傳空 statuses；目前可用 GitHub 工具無 push-triggered workflow run 清單／dispatch 能力。故新 commit CI = NOT TESTED／BLOCKED，不能宣稱測試 PASS。
- 尚未修正 TWT93U 日期、TPEX Date、TWT96U 歷史快照／指標語義；10/30 報告未重跑；未 Merge／Deploy；Master／V8 未修改。
- 下一步：取得 commit 1e15691... 對應 CI Run 並核對 unit-contract-audit／test-v9-ui-fixes；PASS 後再進行 TWT93U／TPEX 日期修正與無日期快照隔離。


## 2026-11-03 資料層第二輪：借券指標語義與歷史日期可用性稽核

### 新增確認的重大資料模型錯誤
1. **TWT96U 被當成借券餘額：CONFIRMED FAIL。** TWSE 官方商品頁明確定義 TWT96U 為「當日可借券賣出股數」，每交易日約 22:30 產出，欄位是「本日可借券賣出限額」，不是已借入尚未返還的借券餘額。官方來源：https://eshop.twse.com.tw/zh/product/detail/57d33ebcf0e54c2187d06dd23e793096 。目前 `spot_raw.sbl_tw()` 讀取 `/SBL/TWT96U` 的 `TWSEAvailableVolume`／`GRETAIAvailableVolume`；`spot.build()` 卻把它們加上 TPEX `SecuritiesBorrowingBalanceOfTheMarketDay`，輸出為 `sbl.bal`／「借券餘額」。這是不同指標混加，必須停止這種計算。
2. **TWT96U 沒有歷史 T0 參數：CONFIRMED。** 目前 `sbl_tw()` URL 固定 `/SBL/TWT96U`，無 date 參數；官方資料為每日 22:30 產生的當日可借券賣出限額。歷史重跑 2026-10-30 時取到的是執行當下最新快照，不能回填歷史日期。
3. **TWSE 正確「借券餘額」資料產品是 TWT72U：官方定義已確認，程式接入尚未測試。** TWSE 官方商品頁說明 TWT72U 是「借券餘額表」，包含前日餘額、今日新增借券、今日還券、今日借券餘額及資料日期；每日約 20:30 產出。官方來源：https://eshop.twse.com.tw/zh/product/detail/8247357531294f4ab139f64c96394096 。這與 TWT96U 完全不同。TWT72U 可作為上市／上櫃借券餘額候選正確來源，但需先確認 RWD 歷史查詢路徑、selectType 市場分類及授權／回傳結構，不能直接假設可用。
4. **借券賣出餘額與借券餘額亦不同。** TWSE 官方定義借券餘額是已借入未返還；借券賣出餘額是已借入並賣出、尚未回補。TWT93U 是融券／借券賣出餘額總量管制資料，不是 TWT72U 借券餘額。官方定義：https://wwwc.twse.com.tw/zh/products/sbl/disclosures/info.html 。TPEX 的 Margin_SBL 文件亦明列融券與借券賣出欄位，借券賣出餘額公式為前日餘額＋當日賣出－當日還券＋當日調整：https://www.tpex.org.tw/storage/regular_system/新版收市後交易資訊格式說明(V1.33版).pdf 。
5. **10/30 報告欄位值與來源註記不可信任：CONFIRMED provenance mismatch。** 舊版 10/30 報告（blob `665ae0ce957cbda372a1d70e1f06f0eea124ba11`）列「借券餘額」4,651,514 張，來源註記 `TWSE TWT93U + TPEX margin_sbl`；重跑版（blob `61b5a8799bec62762a60d5efb3f1099c18084fc5`）列 2,525,111 張，來源註記 `TWSE TWT96U + TWT96U GRETAI（上櫃）`。前者來源註記本身也不是正確的借券餘額來源（TWT93U 為借券賣出餘額類），後者則明確是可借券賣出限額。不能把任一數值直接視為正確歷史借券餘額；此欄應標為資料模型錯誤，先撤除錯誤混算，再選定正確來源。

### TWT93U parser 需升級為高優先待核項
- 官方 TWT93U 商品欄位順序包含：代號、名稱、融券前日餘額、融券賣出、融券買進、融券現券、融券當日餘額、融券限額、借券賣出前日餘額、借券賣出當日賣出、借券賣出當日還券、借券賣出當日調整、借券賣出當日餘額、次一營業日可借券賣出限額、備註／狀態。官方商品說明：https://eshop.twse.com.tw/zh/product/detail/000000006e0bbe8d016f181acc1f0321 。
- 目前 `twse_twt93u_sbl()` 註解稱借券欄位在 `data[i][7..13]`，程式實際使用 `row[7]` 當前日借券餘額、`row[11]` 當日借券餘額。若 API data row 依 15 欄 `fields` 原順序回傳，這兩個 index 很可能偏移一欄（正確借券前日餘額應在 index 8，借券當日餘額應在 index 12）。但本次尚未取得有效 JSON `fields`／data row，故 **INDEX OFF-BY-ONE = HIGH RISK / NOT CONFIRMED**；不可直接修 index，必須先保存實際 response 並依 `fields.index()` 對欄名取值。
- 日期參數已由 Run log 證實傳入 ROC `1151030` 被拒絕（stat: 查詢日期小於94年7月1日）；應測試西元 `YYYYMMDD` `20261030`，並核對回傳 `date` 是否等於請求日期。

### 其他歷史 T0 日期污染面盤點
- `spot_raw.margin_tw()`：TWSE MI_MARGN URL 無日期參數，程式註解明確標記無日期欄、採最新；不能用於歷史 T0。
- `spot_raw.sbl_tw()`：TWT96U 無日期參數、最新快照；歷史 T0 禁用。
- `spot_raw.tpex_highlight()`：只取 TPEX API 回傳 `j[0]`，再與指定 ROC T0 比較；歷史 T0 若 API 只供最新日，將無法回補。需檢查回傳日期與歷史端點。
- `spot_raw.tpex_margin()`、`tpex_sbl()`：只抓當前 OpenAPI 列表並嚴格比較 `str(Date) == roc`。Run log 已顯示 tpex_margin_sbl 932 rows、matched_date_rows=0。必須取得原始 `Date` 樣本，確認其格式（例如是否含斜線）後做標準化；若 API 只回最新日期，不能靠正規化解決歷史查詢，需改用 TPEX 歷史 afterTrading 查詢或可信歷史資料。
- `spot_raw.turnover_tw()`：FMTQIK 無日期參數，僅掃描回傳列表找指定 ROC 日期；若回傳月份資料集合可正常找到，否則需記錄其實際覆蓋範圍；不得在缺列時採最新值。
- `twse.get_institutional(query_date)`：Proxy 與 RWD BFI82U 均傳西元日期，這條路徑有歷史日期參數；`spot.build()` 在回傳 date 不等於 T0 時仍註記「採用最新可得」，這個 fallback 對歷史報告不可接受，應改成 date mismatch -> unavailable。
- `twse_proxy.fetch(date8)`、`histock.get(t0)`、`finmind.taiex_ohlc(t0)` 已見明確傳入 T0 的日期型介面；仍須以 response 日期／資料列日期核對，不能僅因參數存在就當成歷史命中。

### 下一步決策（先資料契約，不先亂改 API）
1. 將借券欄位拆成三個獨立語義：`sbl_borrow_balance`（借入未還，候選 TWT72U）、`sbl_short_sale_balance`（借券賣出未回補，TWSE TWT93U + TPEX Margin_SBL）、`sbl_shortable_limit`（當日可借券賣出限額，TWT96U）。禁止跨指標相加。
2. 先驗證 TWT72U 歷史 API：日期參數、`selectType`、資料日期、上市／上櫃範圍、欄位名稱及資料授權；若 API 無法取得歷史，借券餘額欄不得填入假值，應 unavailable。
3. 修 TWT93U 時先取得 `fields`／`data` 真實 response；用欄名對 index，不使用硬編碼猜測。日期改西元 YYYYMMDD 後確認 2026-10-30 回傳日期。
4. 取得 TPEX `tpex_margin_sbl` 原始 Date 與欄位 sample；確認 endpoint 是否只供最新日，再決定 historical route。對 `tpex_margin`、`tpex_highlight` 同步檢查。
5. 歷史資料來源無日期／日期不匹配，一律 fail closed，不得用最新快照冒充 T0。完成上述資料契約前，不重跑 10/30 DATA_REPORT，不把任何借券欄位標 PASS。

### 狀態更新
- TWT96U 語義及歷史無日期污染：FAIL／CONFIRMED。
- TWT96U 與 TPEX 借券餘額混加：FAIL／CONFIRMED。
- TWT72U 為官方借券餘額產品：PASS（官方定義），API 接入 NOT TESTED。
- TWT93U 日期參數 ROC 錯誤：FAIL／CONFIRMED by run log；西元修正後未測。
- TWT93U row index：HIGH RISK／NOT CONFIRMED。
- TPEX Date 0 matched：CONFIRMED by run log；具體格式／歷史查詢能力 BLOCKED。
- MI_MARGN 歷史 T0 無日期：FAIL／CONFIRMED。
- 本輪僅程式／報告唯讀稽核及官方文件查核；未改程式、DATA_REPORT、workflow、DB，未 Merge／Deploy。


## 2026-11-03 資料層第三輪：TWT93U 欄位索引確認與 TWT72U 歷史來源查核

### 新增證據與狀態
1. **TWT93U parser 欄位索引錯誤：CONFIRMED FAIL（欄位順序交叉核對）。**
   - 目前工作分支 `phase2-p0-ui-fixes` 的 `src/sources/spot_raw.py` 中，`twse_twt93u_sbl()` 使用 `row[7]` 作為借券前日餘額、`row[11]` 作為借券當日餘額。
   - 15 欄順序為：0代號、1名稱、2融券前日餘額、3融券賣出、4融券買進、5融券現券、6融券當日餘額、7融券限額、8借券賣出前日餘額、9借券賣出當日賣出、10借券賣出當日還券、11借券賣出當日調整、12借券賣出當日餘額、13次一營業日可借券賣出限額、14備註。
   - 獨立欄位文件列出相同的 15 欄順序：https://github.com/twcs-analysis/tw-stock-collector/blob/main/data/README.md；TWSE 官方 TWT93U 說明亦確認「借券賣出當日餘額＝前日餘額＋當日賣出－當日還券＋當日調整」及調整欄位存在：https://www.twse.com.tw/exchangeReport/TWT93U?date=20220316&response=html 。
   - 因此現行 row[7] 實為融券限額、row[11] 實為借券賣出當日調整；正確欄位位置應為 8 與 12（前提是實際 JSON data row 與 fields 順序一致）。現行 parser 會將錯誤欄位加總，故 TWT93U sale_bal／sale_chg = FAIL，不可使用。
   - 修正方式不得只硬改 index；應先取得真實 JSON response，使用 `fields.index("借券賣出前日餘額")`、`fields.index("借券賣出當日餘額")` 等欄名定位，並驗證 row 長度、日期及欄位存在。
2. **TWT72U 歷史查詢頁存在：官方頁面 PASS；RWD API NOT TESTED。**
   - TWSE 官方 TWT72U 歷史查詢頁可選日期及分類，頁面標示資料自 2004-11-22 起：https://www.twse.com.tw/zh/products/sbl/disclosures/twt72u.html 。
   - 官方 TWT72U 產品欄位包含前日借券餘額、今日新增借券、今日還券、今日借券餘額及資料日期；官方投資人知識網將借券餘額定義為借入尚未返還數量：https://eshop.twse.com.tw/zh/product/detail/8247357531294f4ab139f64c96394096 、https://investoredu.twse.com.tw/Pages/TWSE_InvestmentQA.aspx?ID=8 。
   - TWSE Data E-Shop 亦將 TWT72U 列為訂閱商品，故公開網頁可查詢不等於 workflow 可無條件使用其資料檔/API；需分別確認 RWD API 的實際回應、歷史日期、分類、可用性及授權條件：https://eshop.twse.com.tw/en/product/detail/790d45d2b28b4f50a52a951ec0723150 。
   - 嘗試讀取候選 RWD URL `/rwd/zh/sbl/TWT72U?date=20261030&selectType=SLBNLB&response=json`，本次查詢工具回傳不可存取；此結果不是 API 失效證明。狀態仍為 API NOT TESTED／BLOCKED。
3. **TWT96U 的資料定義再次由官方 OpenAPI 文件確認：**
   - TWSE OpenAPI 將 `/SBL/TWT96U` 定義為「上市上櫃股票當日可借券賣出股數」，Data E-Shop 產品頁亦明列為當日可借券賣出股數，22:30 產出；不得映射成借券餘額：https://openapi.twse.com.tw/ 、https://eshop.twse.com.tw/en/product/detail/6206e910508c4f2c96c9d38f0a53b715 。
4. **TPEX tpex_margin_sbl 的歷史資料語義仍需原始 API response 才能最後定案。**
   - TPEX 官方 OpenAPI 將 `tpex_margin_sbl` 命名為「上櫃股票融券借券賣出餘額」；官方頁明確說明借券賣出餘額公式為前日餘額＋當日賣出－當日還券＋當日調整，且含融券及借券賣出欄位：https://www.tpex.org.tw/openapi/ 、https://www.tpex.org.tw/zh-tw/mainboard/trading/margin-trading/sbl.html 。
   - TPEX 官方歷史查詢頁可指定日期並下載 CSV：https://www.tpex.org.tw/web/stock/margin_trading/margin_sbl/margin_sbl_result.php 。官方文件頁在本次工具環境部分回傳 403；不能把工具 403 說成官方服務不可用。
   - 現行 `tpex_sbl()` 把 `SecuritiesBorrowingBalanceOfTheMarketDay` 填入 `bal`，又把 `SaleBalanceOfTheMarketDay`／`SaleBalancePreviousDay` 當成借券賣出餘額與前日值。從 endpoint 名稱與官方欄位組成看，這很可能把「融券餘額」與「借券賣出餘額」映射反了；但尚未取得實際 OpenAPI fields／row 樣本，標記 **HIGH RISK / NOT CONFIRMED**，不可直接改 mapping。
   - OpenAPI endpoint 呼叫不帶日期參數；現有 Run log 932 rows、0 matched_date_rows。歷史 T0 應改走官方歷史查詢／可驗證日期參數來源，不能把 latest-only OpenAPI 回應當成歷史值。
5. **TWSE／TPEX 官方借券賣出餘額可按相同語義分市場加總，但必須先修正各自欄位映射與日期。**
   - TWSE 官方說明借券賣出餘額為已借券賣出尚未回補；TPEX 官方公式亦包含前日餘額、當日賣出、當日還券與調整。市場分開統計後，若單位同為股數且日期相同，才可換算張數後合併；不可混入 TWT72U 借券餘額或 TWT96U 可借限額。

### 本輪狀態表
- TWT93U row[7]/row[11] 對應錯誤欄位：**FAIL / CONFIRMED**（依官方欄位定義及 15 欄順序交叉核對；尚待 raw JSON fixture 做 parser regression）。
- TWT93U 西元日期 20261030 真實 API response：**NOT TESTED**。
- TWT72U 官方歷史查詢頁與欄位定義：**PASS**；RWD API、分類及授權：**NOT TESTED / BLOCKED**。
- TWT96U 可借券賣出限額語義：**PASS / OFFICIAL**。
- TPEX 欄位 mapping（融券餘額 vs 借券賣出餘額）：**HIGH RISK / NOT CONFIRMED**。
- TPEX OpenAPI Date／歷史查詢：**BLOCKED**，尚缺 raw sample。
- 本輪未修改程式、DATA_REPORT、workflow 或 DB；未重跑 10/30；未 Merge／Deploy；Master／V8 未動。
- Auditor：單一模型自我稽核，非獨立多模型審核。

### 下一個窄範圍工作
1. 取得 TWT93U 2026-10-30 真實 JSON response，保存 fields/data fixture，依欄名定位並測試 date equality。
2. 取得 TPEX `tpex_margin_sbl` 原始 JSON 樣本，逐欄對照官方歷史 CSV 欄位，確認 `SecuritiesBorrowingBalanceOfTheMarketDay`、`SaleBalanceOfTheMarketDay`、`SaleBalancePreviousDay` 的真實中文語義。
3. 驗證 TWT72U 歷史查詢 API 的資料日期、selectType、回傳欄位及授權可用性；若無法在 workflow 中合法穩定取得，`sbl_borrow_balance` 保持 unavailable。
4. 以上三項完成前，不改報告 mapping、不重跑 10/30。


## 2026-11-03 資料層第四輪：TWT93U 日期／欄位實測佐證補強，重新收斂 TPEX mapping

### TWT93U：日期格式及欄位索引已有真實 API 輸出範例佐證
- 找到公開的 Python 實測紀錄，實際請求 `https://www.twse.com.tw/exchangeReport/TWT93U?response=json&date=20250829`，輸入日期為西元 `YYYYMMDD`，成功回傳 stat OK、title、15 個 fields 與 data rows。來源：https://yhhuang1966.blogspot.com/2025/08/python_3.html 。
- 該實測的 fields 原序為：`代號`、`名稱`、融券前日餘額、融券賣出、融券買進、融券現券、融券當日餘額、融券限額、借券賣出前日餘額、借券賣出當日賣出、借券賣出當日還券、借券賣出當日調整、借券賣出當日餘額、次一營業日可借券賣出限額、備註。
- 因此 index 7 = 融券限額、index 8 = 借券賣出前日餘額、index 11 = 借券賣出當日調整、index 12 = 借券賣出當日餘額。現行 `twse_twt93u_sbl()` 使用 row[7]/row[11]，錯誤已由實際 API response 範例交叉確認：**FAIL / CONFIRMED**。
- 日期格式使用西元 YYYYMMDD 亦有成功實測佐證；本專案 2026-10-30 的真實 endpoint response 尚未取得，故目標日期命中仍是 **NOT TESTED**。程式目前仍傳 ROC 日期，修正後需檢查 response `date` 等於 20261030。
- 正式修正需檢查 `fields` 存在且唯一、data row 長度與 fields 一致、以欄名定位 index，並排除總計列／空代號列；不可僅改成 row[8]/row[12] 而不加結構驗證。

### TPEX：將先前「欄位可能對調」收斂為具體待核對的欄位語義
- TPEX 官方 EDIS S47「Margin_SBL.csv」格式文件列出 15 欄：資料日期、證券代號、融券前日餘額、融券賣出、融券買進、融券現券、融券當日餘額、融券限額、借券賣出前日餘額、借券賣出當日賣出、借券賣出當日還券、借券賣出當日調整數額、借券賣出當日餘額、次一營業日可借券賣出限額、備註。來源：https://www.tpex.org.tw/storage/regular_system/新版收市後交易資訊格式說明(V1.33版).pdf 。
- 官方 OpenAPI Swagger 將 `tpex_margin_sbl` 描述為「上櫃股票融券借券賣出餘額」；官方歷史頁也說明借券賣出餘額公式為前日餘額＋當日賣出－當日還券＋當日調整。來源：https://www.tpex.org.tw/openapi/ 、https://www.tpex.org.tw/zh-tw/mainboard/trading/margin-trading/sbl.html 。
- 現行程式 mapping：`SecuritiesBorrowingBalanceOfTheMarketDay` -> `bal`；`SaleBalanceOfTheMarketDay` -> `sale_bal`；`SaleBalancePreviousDay` -> `sale_prev`。依 S47 15 欄資料模型，**更可能的語義**是 `SecuritiesBorrowingBalanceOfTheMarketDay` 對應第 13 欄「借券賣出當日餘額」，而 `SaleBalanceOfTheMarketDay`／`SaleBalancePreviousDay` 對應第 7／3 欄「融券當日／前日餘額」。若此推斷成立，現行程式把借券賣出餘額放入 `bal`、把融券餘額放入 `sale_bal`，正好對調了用途。
- 上述為依官方欄位架構推導的 **HIGH RISK / NOT CONFIRMED**，不是已取得 OpenAPI JSON schema 的直接證據。必須取得 Swagger schema 或原始 JSON key-value + 官方同日 CSV，逐證券代號對照後才可確認；在此之前，不得將 `bal` 當借券餘額，也不得將 `sale_bal` 當借券賣出餘額。
- 日期方面，官方 S47 檔案格式明示資料日期是西元 YYYYMMDD；但目前 OpenAPI 回傳的 Date 原始值與歷史日期覆蓋仍未取得，Run log 932 rows / 0 matched 仍待原始樣本解釋。

### TWT72U：公開歷史查詢頁與付費 E-Shop 商品必須區分
- TWSE 官方 TWT72U 網頁提供日期、分類選擇及 CSV 下載按鈕，資料頁標示自 2004-11-22 提供：https://www.twse.com.tw/zh/products/sbl/disclosures/twt72u.html 。
- TWSE Data E-Shop 的 TWT72U 產品頁則標示資料起始日 2017-03-15、每日 20:30 產製、訂閱單位按月；內部使用 NT$1,500/月、外部使用 NT$3,000/月，並有使用限制。來源：https://eshop.twse.com.tw/zh/product/detail/8247357531294f4ab139f64c96394096 。
- 因此不能籠統宣稱「TWT72U API 免費可用」；應先驗證公開歷史查詢頁的 CSV 下載請求是否可供自動化合法使用，以及它與 E-Shop 訂閱商品的授權邊界。RWD API 仍 NOT TESTED；若要使用訂閱資料檔，須先有合法訂閱／授權。
- TWT72U 內容欄位明確是前日借券餘額、當日新增借券、當日還券、當日借券餘額，且涵蓋 TWSE／TPEx 市場別；這仍是 `sbl_borrow_balance` 的正確候選語義，不應以 TWT93U/TWT96U 代替。

### 本輪狀態修正
- TWT93U 日期格式 YYYYMMDD：**PASS / 實際 API 範例**；本專案 T0=20261030 實際 response：**NOT TESTED**。
- TWT93U row[7]/row[11] mapping：**FAIL / CONFIRMED**。
- TWT93U parser 以 fields 欄名定位、row length/date validation：**NOT IMPLEMENTED**。
- TPEX OpenAPI mapping：**HIGH RISK / NOT CONFIRMED**；最優先核對 SecuritiesBorrowingBalanceOfTheMarketDay 與 SaleBalanceOfTheMarketDay 的對應欄位。
- TPEX 日期欄位實際格式及 20261030 歷史資料：**BLOCKED / NOT TESTED**。
- TWT72U 官方公開查詢頁：**PASS**；自動化 CSV 請求及授權界線：**NOT TESTED**；E-Shop 訂閱商品價格與限制：**PASS / OFFICIAL**。
- 本輪未修改程式、DATA_REPORT、workflow 或 DB；未重跑 10/30；未 Merge／Deploy；Master／V8 未動。


## 2026-11-03 資料層第五輪：TPEX S47 官方格式與現行 build mapping 對照

### 新增確認
- 已直接讀取 TPEX 官方 V1.33 EDIS 格式 PDF，定位到 S47「Margin_SBL.csv」規格（PDF 第 122 頁／文件 lines 5043–5068）。其 15 欄依序為：
  0 資料日期、1 證券代號、2 融券前日餘額、3 融券賣出、4 融券買進、5 融券現券、6 融券當日餘額、7 融券限額、8 借券賣出前日餘額、9 借券賣出當日賣出、10 借券賣出當日還券、11 借券賣出當日調整數額、12 借券賣出當日餘額、13 次一營業日可借券賣出限額、14 備註。官方 PDF：https://www.tpex.org.tw/storage/regular_system/新版收市後交易資訊格式說明(V1.33版).pdf 。
- 官方 OpenAPI 把 `tpex_margin_sbl` 命名為「上櫃股票融券借券賣出餘額」；其官方資料表即 S47，內容不是「一般借券餘額表」，而是融券餘額與借券賣出餘額兩組不同欄位。
- 對照現行 `tpex_sbl()` 與 `spot.build()`：
  - parser 把 `SecuritiesBorrowingBalanceOfTheMarketDay` 放進 `stp["bal"]`，build 又將它與 TWSE TWT96U（可借券賣出限額）相加，輸出為 `sbl.bal`「借券餘額」。
  - parser 把 `SaleBalanceOfTheMarketDay` 放進 `stp["sale_bal"]`，build 又將它與 TWSE TWT93U 的借券賣出餘額相加，輸出為 `sbl.sale_bal`。
  - 依 S47 欄位結構與 property 命名，最合理對應是 `SecuritiesBorrowingBalanceOfTheMarketDay` = index 12「借券賣出當日餘額」；`SaleBalanceOfTheMarketDay`／`SaleBalancePreviousDay` = index 6／2「融券當日／前日餘額」。若同日 JSON schema 對照確認此 mapping，現行程式就是把「借券賣出餘額」放入 `sbl.bal`，並把「融券餘額」放入 `sbl.sale_bal`，兩欄用途完全顛倒。
  - 因此現行兩項 TPEX 輸出均不得使用：`sbl.bal` 還額外混入 TWT96U 可借限額；`sbl.sale_bal` 還把融券餘額與 TWT93U 借券賣出餘額相加。此為 **FAIL / HIGH CONFIDENCE, exact OpenAPI property-to-S47 field mapping awaits same-date raw schema/CSV confirmation**。
- 官方 S47 15 欄本身沒有「借入尚未返還的借券餘額」這個欄位；只有借券賣出未回補餘額。真正借券餘額應另用 TWT72U（官方 TWT72U 同時涵蓋市場別），不能從 S47/TWT93U/TWT96U 拼湊。
- TWT96U 仍是可借券賣出限額，不應出現在 `sbl.bal`。
- TWSE TWT93U + TPEX S47 的「借券賣出當日餘額」在同日、同單位股數、逐市場完整資料時可作為跨市場借券賣出餘額合計；不能把 TPEX 的融券餘額加進去。

### 本輪狀態
- TWT93U 日期格式 YYYYMMDD／15 欄順序：**PASS / 實際 API 範例**；目標日期 20261030 response：**NOT TESTED**。
- TWT93U row[7]/row[11]：**FAIL / CONFIRMED**。
- TPEX S47 欄位順序與語義：**PASS / OFFICIAL**。
- TPEX OpenAPI property-to-S47 exact mapping：**HIGH CONFIDENCE / NOT TESTED**（需取得 JSON schema 或同日 CSV 對照）。
- 現行 TPEX `bal`、`sale_bal` 的 build 用途：**FAIL / HIGH CONFIDENCE**；不得用於 DATA_REPORT。
- TWT72U 作為真正借券餘額來源：官方定義 PASS；workflow 自動化取得及授權：NOT TESTED。
- 本輪只讀程式與官方 PDF／頁面；未改程式、DATA_REPORT、workflow、DB；未重跑 10/30；未 Merge／Deploy。

## 2026-11-03｜P0 Quality「數據真實性全面清查」回溯稽核

### 本輪查核範圍與證據
- 唯讀檢查 phase2-p0-data-quality 分支，當前 HEAD：49fd5b0dfd6a9c1b89fc49bb6e4d81ae5fdc4d33（GitHub branch API）。
- 該分支 src/sources/spot_raw.py blob 53664aeeeb40032290c7bc895f3c79c217f573fc：sbl_tw() 仍將 TWT96U 當成「可借餘額」；twse_twt93u_sbl() 仍以 row[7]／row[11] 取借券前日／當日餘額。
- 該分支 src/sources/spot.py blob f38d2e49994d48eeb4c58b191d0ebf08b7c751ae：build 將 TWT96U TWSE/OTC 值與 TPEX stp[bal] 合併為 sbl.bal；借券賣出餘額則將 TWT93U 與 stp[sale_bal] 合併。
- docs/DATA_SOURCES.md blob 748e1ab43073219663650a6ca67d55642d50f6d1 仍明確寫「上市 TWT96U（可借餘額）＋上櫃 tpex_margin_sbl（賣出餘額/前日→增減）」並標記狀態「✅」。此文件本身把 TWT96U 指標語義寫錯。
- P0 branch tests/ 目錄包含維持率、Builder、workflow isolation、Gamma 等測試；未見 spot_raw／TWT93U／TWT96U／TPEX S47 的 parser fixture 或欄位 mapping 測試。這是對該分支當前 tree 的檢查結果，不代表外部對話或未入庫材料不存在。
- docs/DATA_SCHEMA.md blob fa422f250bfb41dab23241986e4756b215482b9e 對部分無日期端點允許採最新可得／標示最新值；但缺少能保證「歷史 T0 不會誤用最新快照」的全來源端到端契約。

### 結論（針對 P0 Quality 清查品質）
- FAIL：資料來源定義層未完成有效驗收。TWT96U 的錯誤語義不只留在程式，還被 DATA_SOURCES.md 正式文件標為正確並打勾。
- FAIL：借券 parser 欄位 mapping 未有對應測試證據。現有測試目錄沒有 TWT93U／TPEX S47／TWT96U 專項測試；程式錯誤因此未被 regression 攔截。
- FAIL：資料真實性驗收深度不足。至少未能證明每個欄位均完成「官方定義→原始 response/schema→欄位 mapping→日期/T0→計算→DATA_REPORT」逐段核對。
- NOT ESTABLISHED：當初清查實際執行內容。本輪未取得當時完整清查工單、對話及逐欄簽核紀錄；不能斷言完全沒做，而是目前 repo 留存證據不足以支持「數據真實性全面 PASS」的結論。

### 本輪邊界
- 僅唯讀查核 phase2-p0-data-quality 的 branch HEAD、spot source、DATA_SOURCES／DATA_SCHEMA、docs 及 tests tree。
- 未修改 phase2-p0-data-quality、phase2-p0-ui-fixes、DATA_REPORT、workflow 或 DB；未重跑 10/30；未 merge／deploy；master／V8 未動。
- Auditor 為單一模型自我稽核，非獨立多模型審核。

### 下一步（維持窄範圍）
1. 不再抽象討論「全面清查」；先完成 TWT93U 20261030 真實 response、TPEX S47 同日 JSON/CSV 對照、TWT72U 歷史取得與授權確認。
2. 以上證據齊備後，修正資料契約、parser、build mapping 與專項 fixture tests；來源日期不符或未取得時 fail closed。
3. 測試通過後才重建 20261030 DATA_REPORT；目前仍禁止重跑。
## 2026-11-03｜資料來源取得可行性補查

- 嘗試讀取 TWSE TWT93U 目標日期 JSON：`https://www.twse.com.tw/exchangeReport/TWT93U?response=json&date=20261030`。Web 讀取回 Internal Error，容器端請求遇 DNS resolution failure；此為目前查詢環境 BLOCKED，不可據此宣稱官方 API 失效。20261030 原始 response 仍 NOT TESTED。
- TPEX 官方歷史查詢頁 `sbl_hist10110.html` 提供日期查詢及「另存 CSV」介面（官方頁面搜尋結果可確認）；但 TPEX E-Shop 對 `Margin_SBL.csv` 列有每日訂閱商品，產製時間 22:00，內部 NT$1,000/月、外部 NT$1,500/月，且用途／再揭露限制依訂閱條款。公開查詢頁的 CSV 按鈕與訂閱商品授權邊界仍未釐清；不能直接把訂閱檔當成可免費自動化使用的來源。
- 因此 TPEX S47 的官方欄位結構已確認，但 API property-to-column 精確 mapping 及 20261030 原始 CSV/JSON 同日對照仍 NOT TESTED；不得只憑 property 名稱改 parser。
- 本輪沒有修改程式、DATA_REPORT 或 workflow，沒有重跑 10/30，沒有 merge/deploy。
## 2026-11-03｜TWT72U 指標範圍補充

- TWSE 投資人知識網明確定義「借券餘額」為借入證券尚未返還數量；並明確區分「借券賣出餘額」（已賣出尚未回補）及「融券餘額」。來源：https://investoredu.twse.com.tw/Pages/TWSE_InvestmentQA.aspx?ID=8 。
- 官方 TWT72U 商品欄位包含系統別、證券代號、昨日借券餘額、今日新增借券、今日還券、今日借券餘額、市場別及資料日期；資料頁提供日期／分類選擇與 CSV 下載。但 TWT72U E-Shop 商品本身為月訂閱（內部 NT$1,500/月、外部 NT$3,000/月）。
- TWSE 官方儀表板將借券餘額拆示證交所借券系統、證商／證金營業處所及借券餘額合計。故在接入 TWT72U 前，還需核實分類 selectType 的涵蓋範圍、各系統別是否都在同一下載檔、是否有重複計算，以及「合計」口徑如何組成；不能未核對就將單一分類當成全市場總借券餘額。
- 結論：TWT72U 的指標語義正確，但「單一端點／單一分類即涵蓋 dashboard 所需全市場合計」尚未確認；資料取得方式與授權亦未確認。
## 2026-11-03｜現貨籌碼欄位投資人語義對照（唯讀）

- 依 phase2-p0-ui-fixes 的 DATA_REPORT_TEMPLATE.md（blob 334eb88b91d4c8c27f9945d2a247ebe475129396）及 DASHBOARD_UNIT_MAP.md（blob ee8e8cde6b6629c5ab70931e2d739def8b745a2f），現貨籌碼區應以投資人名稱呈現：融資餘額／增減、融券餘額、上市維持率、借券餘額、借券賣出餘額、借券賣出增減；單位分別依億元、張、%標示。
- `margin.s_bal`／`margin.s_chg` 是融券餘額／增減（張），不是借券餘額；`sbl.bal` 是借券餘額（張）；`sbl.sale_bal`／`sbl.sale_chg` 是借券賣出餘額／增減（張）。三者語義必須分開。
- 目前 DATA_SOURCES.md（blob ded0fc727dc716f3859b70f68b25f131d51e2ca7）已警告 TWT96U 不得作 TWT93U 替代來源；但現行 spot_raw.py（blob f5d95898b327b9243ee586ad4dd528d4502d7500）仍將 TWT96U 定義為可借餘額，spot.py（blob 92f4f90241c91ec5f1a46570bad439ba9aa3d7f0）仍把 TWT96U TWSE/OTC 與 TPEX stp.bal 加總輸出 sbl.bal。文件與程式矛盾，sbl.bal 不可信。
- 現行 spot_raw.py 的 TWT93U parser 仍以 row[7]、row[11] 讀取借券前日／當日餘額；已知官方欄位排列顯示應依欄名取借券賣出前日餘額及借券賣出當日餘額，故上市借券賣出資料仍 FAIL。
- DASHBOARD_UNIT_MAP.md 的 2026-11-02 區塊 12 曾將借券欄位標 PASS；該 PASS 僅能代表顯示欄位／單位及 scope 樣本契約，不能代表上游來源定義及原始 mapping 真實性。此項驗收標準需要更正，不能沿用舊 PASS 作資料真實性證明。
- 本輪只盤點現貨融資融券／借券語義，不擴展至期貨與選擇權內部欄位；未改程式、DATA_REPORT、workflow，未重跑 10/30，未 merge/deploy。

### 使用者可見名稱標準（建議資料契約）
- 融資餘額／融資增減（億元）。
- 融券餘額／融券增減（張）。
- 上市融資維持率（%；明確標示上市估算範圍、T0、來源）。
- 借券餘額（張；借入尚未返還）。
- 借券賣出餘額／借券賣出增減（張；已借券賣出尚未回補／當日淨變化）。
- 來源代碼 TWT72U／TWT93U／S47 只留在技術來源註記，不作 Dashboard 主標題。

## 2026-11-03｜借券資料鏈修正與官方 T0 live 驗證（最新）

### 程式修正（僅 phase2-p0-ui-fixes）
- TWT96U 已完全排除借券餘額與借券賣出餘額／增減計算；TWT96U 只代表當日可借券賣出限額。
- TWT72U：新增歷史查詢 parser，使用西元 YYYYMMDD + selectType=SLBNLB；依 fields 取欄位、檢查 response date，逐列驗證「前日餘額＋新增借券－還券＝當日餘額」。個股分上市／上櫃加總，並核對兩市場小計與整體市場合計，防止總計重複加總。
- TWT93U：改用 RWD 歷史 endpoint 與西元 YYYYMMDD；欄位名稱有重複時依欄位群組及中間「當日賣出／當日還券／當日調整」辨識借券賣出欄，不再使用 row[7]/row[11]；逐股驗證「前日＋賣出－還券＋調整＝當日」。
- TPEx S47：改用官方日期查詢 endpoint；針對重複「前日餘額／當日餘額」欄名，以欄位群組結構辨識後段借券賣出欄，逐股驗證同一遞推公式。
- spot.build() 分別使用 TWT72U 借券餘額、TWT93U 上市借券賣出、TPEx S47 上櫃借券賣出；只有同一 T0 兩市場都有效才可視為完整合計，否則 source label 明示市場範圍。
- Builder 不再由舊報告的模糊來源註記推斷市場範圍；不能判定時輸出「範圍未註明」。
- 更新 DATA_SOURCES.md、DATA_SCHEMA.md、DASHBOARD_UNIT_MAP.md；區塊 12 驗收明確區分 UI、source parser、舊 DATA_REPORT 數值三個層級。

### 2026-10-30 官方端點 live 驗證（GitHub Actions）
- Run 41671847081 / Job 126042001585，live-borrowed-sources：**PASS**。
- TWT72U：response date 20261030，2,075 rows；市場分類為集中市場 1,238、櫃檯買賣中心 836、整體市場 1；其中個股 1,237 + 835 = 2,072。上市小計、上櫃小計及整體市場合計完全一致，subtotal_checks=PASS。
- TWT93U：response date 20261030，1,308 rows；解析 1,307 個股，invalid_rows=0，逐股餘額遞推檢查通過。
- TPEx S47：response/table date 20261030，932 rows；live parser 成功解析資料，逐股餘額遞推檢查通過。
- 這是官方端點實際 live response，不是 mock fixture；但 E-Shop 訂閱商品的授權／自動化使用邊界仍需依官方條款確認。

### CI／Builder 驗證
- 最新修正分支 HEAD：899900c017ef036f808b4843ed85f6e29ca383e1（phase2-p0-ui-fixes）。
- Unit Contract Audit Run 41671847081：**PASS**（borrowed source tests、Dashboard unit contract、DATA_REPORT/Builder regression、React template regression、TAIFEX night unavailable summary 等皆通過）。
- V9 UI Fixes Regression Run 41671995742：**PASS**。GEX pipeline 2026-10-30、139 levels、GEX totals 驗證通過；Builder JSON 借券欄位輸出通過；非部署 HTML preview 318,829 bytes；獨立 correlation fixture 319,438 bytes。
- Daily Premarket V9 Pro Run 41671847060：build **PASS**、deploy **SKIPPED**；workflow 使用既有 DATA_REPORT_20261102.md，沒有重跑或修改 DATA_REPORT_20261030。
- Unit Contract Audit 曾因舊 UI regression 將模糊來源註記錯誤推斷為「上櫃（上市未取得）」而 FAIL；已修正為「範圍未註明」，符合 fail-closed 原則。舊 DATA_REPORT_20261030 借券賣出餘額 36,178 張、增減 -1,273 張尚未由新 parser 重建，不能宣稱數值已驗證。

### 重要 Git commits（phase2-p0-ui-fixes）
- TWT93U／TWT72U／TPEx S47 source parser 與 spot mapping 修正已提交；相關測試、live probe workflow、Builder scope parser、測試 expectation 也已提交。
- 最新 HEAD 899900c017ef036f808b4843ed85f6e29ca383e1。
- 主要檔案最新 SHA：spot_raw.py 937ea000d0b81b90fda46720d92ae88095df661a；spot.py 3c20c84bcc50d539741caa61b0f2cb544c33af97；v9_pro_builder.py 982bdf87884dce83aba54dbdb48e7f1b96122a32；test_spot_borrowed_semantics.py aac26ccc808caf08f9a950b346eaa22be76ff867。
- 文件更新 commits：DATA_SOURCES c98cbc34f46d81af7efaee17c4e91a624ad5ad01；DATA_SCHEMA b14b18238b368fac73d1d22b9820b4c9bb8c6f46；DASHBOARD_UNIT_MAP 3e83b1649cebfd91d8cb2218bbfb896593ede2b6。

### 尚未完成／限制
- **NOT DONE**：尚未以修正後 fetch pipeline 重建 DATA_REPORT_20261030。
- **NOT VERIFIED**：舊 DATA_REPORT_20261030 的借券餘額／借券賣出餘額／增減數值與市場範圍；Builder 對舊模糊 provenance 顯示「範圍未註明」是正確行為。
- **NOT TESTED**：TWT72U／TWT93U／TPEx S47 的 E-Shop 訂閱／公開 API workflow 自動化授權界線；不可將 live endpoint 可讀取等同授權確認。
- 未 Merge／Deploy；master、P0 base、V8 未修改；data_reports 樣本未修改。
- Auditor 為單一模型自我稽核，非獨立多模型審核。

### 下一步（只做收尾）
1. 先確認官方公開 endpoint 與 E-Shop 商品授權邊界；若無需訂閱授權或已具合法授權，才進行歷史報告重建。
2. 在使用者指定／已批准的方式下，僅重建 20261030 DATA_REPORT，逐欄核對借券餘額、上市借券賣出、上櫃借券賣出、跨市場增減及來源 scope。
3. 驗收 DATA_REPORT 後再跑 Builder 與 dashboard preview；不部署，除非使用者明確授權。


## 2026-11-03｜最新驗收更新（HEAD 01d8d6e）

- phase2-p0-ui-fixes 最新 HEAD：01d8d6e82810b13ce617feff18f142189cb9c14a。
- Unit Contract Audit Run 41672806366：**PASS**。live-borrowed-sources、借券 source semantic tests、42 區塊 unit contract、DATA_REPORT／Builder tests、React template tests、TAIFEX night unavailable tests 均通過。
- V9 UI Fixes Regression Run 41672806450：**PASS**。Builder self-tests、React regression、DATA_REPORT parser regression、借券 JSON 欄位與 scope 驗證、GEX 139 levels／總量、non-deploy HTML preview、correlation fixture 均通過。
- Daily Premarket V9 Pro Run 41672806998：build **PASS**、deploy **SKIPPED**；使用既有 DATA_REPORT_20261102.md，沒有修改 data_reports 樣本，也沒有重建 20261030。
- 先前 Unit Contract Audit 因 42 區塊表格的驗收 regex 不接受 UI PASS 標籤而失敗；已修正測試，使其同時接受 PASS 與 UI PASS，最新 Run 41672806366 已通過。這是驗收測試 regex 修正，不是放寬資料來源驗收。
- 最新 docs/DATA_SOURCES.md、DATA_SCHEMA.md、DASHBOARD_UNIT_MAP.md 已提交於 phase2-p0-ui-fixes；區塊 12 明確區分 UI PASS／新來源 parser PASS／舊 DATA_REPORT 數值 NOT VERIFIED。
- 最新 tests/test_dashboard_unit_contract.py commit：01d8d6e82810b13ce617feff18f142189cb9c14a。
- 尚未完成：DATA_REPORT_20261030 尚未使用新 parser 重建；舊 36,178 張／-1,273 張數值仍 NOT VERIFIED；E-Shop／公開 endpoint 自動化授權界線仍 NOT TESTED。
- 未 merge/deploy；master、P0 base、V8 未修改；data_reports 樣本未修改。Auditor 為單一模型自我稽核，非獨立多模型審核。


## 2026-11-03｜TWSE／TPEx 資料授權邊界查證（阻止未授權報告重建）

- TWSE E-Shop 官方商品頁顯示 TWT72U「借券餘額表」為月訂閱：內部 NT$1,500/月、外部 NT$3,000/月；資料每日產製，含系統別、借券前日餘額、今日新增借券、今日還券、今日借券餘額、市場別與資料日期。來源：https://eshop.twse.com.tw/zh/product/detail/8247357531294f4ab139f64c96394096 。
- TWSE E-Shop 官方商品頁顯示 TWT93U「信用額度總量管制餘額檔」為月訂閱：內部 NT$1,000/月、外部 NT$1,500/月；含融券與借券賣出兩組餘額欄。來源：https://eshop.twse.com.tw/zh/product/detail/000000006e0bbe8d016f181acc1f0321 。
- TWSE OpenAPI Swagger 搜尋結果列出 TWT96U（當日可借券賣出股數），但未見 TWT72U／TWT93U；不能把 RWD 網頁端點可匿名讀取等同已取得開放資料授權。
- TPEx S47 對應政府資料開放平臺 dataset 11632「上櫃股票融券借券賣出餘額」，官方 metadata 標示每日更新、政府資料開放授權條款第 1 版、免費，欄位含融券與借券賣出兩組。來源：https://data.gov.tw/dataset/11632 。
- 因此：TPEx S47 有免費開放資料授權證據；TWSE TWT72U／TWT93U 的 RWD live endpoint 已通過技術驗證，但 production 自動化授權尚無證據，應標 **BLOCKED / LICENSE NOT CONFIRMED**。不得重建 20261030 DATA_REPORT，也不得把 live test 成功當成可合法自動化使用的證據。
- TWSE E-Shop 頁面提供價格與用途條款；本專案尚未取得使用者已訂購／授權證明。待使用者確認是否有 TWT72U、TWT93U 訂閱，或取得官方書面授權後，才能決定啟用上市借券餘額及上市借券賣出來源。若沒有授權，兩欄應 unavailable；TPEx S47 仍可依政府開放資料授權單獨呈現上櫃借券賣出值，並明確標示「上櫃」而非全市場。
- 最新 phase2-p0-ui-fixes 文件 DATA_SOURCES.md 授權註記 commit：8317dcb359b5629cf073c144068339322e89884a。


## 2026-11-04 最新補充｜TWSE TWT93U／TWT72U 新版 RWD JSON 使用者實測

### 使用者提供的端點與實測
- 使用者於 2026-11-04 明確確認兩支官方新版 RWD API 的 JSON 回應均可正常取得：
  - 借券賣出餘額 TWT93U：`https://www.twse.com.tw/rwd/zh/marginTrading/TWT93U?response=json&date=20261030`
  - 借券餘額 TWT72U：`https://www.twse.com.tw/rwd/zh/lending/TWT72U?response=json&date=20261030`
- 這是新版 `/rwd/zh/` 路徑；後續以此為優先候選，不再把舊 `/exchangeReport/` 路徑當作必要條件，也不應因 Swagger 未列出就否定端點可用性。
- 使用者提供兩支 JSON 最後合計列截圖。以下數值是使用者實測截圖證據，不是本助手獨立 HTTP 抓取結果。

### 2026-10-30 TWT93U 合計列
- 最後一列名稱為「合計」，借券賣出欄位：
  - 前日餘額：16,691,222,049 股
  - 當日賣出：323,013,000 股
  - 當日還券：218,375,860 股
  - 當日調整：0 股
  - 借券賣出當日餘額：**16,795,859,189 股**（約 1,679.59 萬張）
- 遞推驗算：16,691,222,049 + 323,013,000 - 218,375,860 = 16,795,859,189。
- 取值規則：以最後「合計」列的借券賣出當日餘額為全上市市場彙總；不可再加總個股明細，避免重複計算。
- 注意：截圖未包含完整 fields 標題；實作時仍須依新版 JSON 的欄名定位，不可盲用舊版 row index。

### 2026-10-30 TWT72U 合計列
- JSON 最後可見市場合計列：
  - 集中市場：今日借券餘額 **26,717,413,000 股**
  - 櫃檯買賣中心：今日借券餘額 **3,320,272,000 股**
  - 整體市場：今日借券餘額 **30,037,685,000 股**（約 3,003.77 萬張）
- 整體市場遞推：29,828,535,000 + 813,411,000 - 604,261,000 = 30,037,685,000。
- 取值規則：全市場欄位直接取「整體市場」合計列；若要拆市場則各取集中市場／櫃檯買賣中心合計列。不得再加總個股明細，也不得把個股列與市場合計列混加。
- 借券餘額定義為借入尚未返還；與借券賣出餘額、融券餘額、TWT96U 可借券賣出限額是不同指標。

### 對先前恢復紀錄的狀態修正
- 先前記錄「TWT93U／TWT72U 目標日 response 未取得」已被使用者本輪實測補足：端點 JSON 可取得、合計列數值可讀，以上兩項應更新為 PASS（使用者證據）。
- 助手執行環境對這些 URL 的直接讀取曾回傳 DisabledError；助手獨立 HTTP 抓取仍為 BLOCKED。不可把使用者實測寫成助手獨立抓取。
- TWT93U 完整新版 fields／data schema 與欄位標題對照仍需程式實際讀取驗證；截圖只足以驗證合計列的關鍵數值及遞推。
- 本次只更新 Recovery 文件；沒有修改 fetch 程式、DATA_REPORT、Builder、workflow、資料樣本或 Dashboard；沒有重跑 2026-10-30 報告；沒有 Merge／Deploy。
- 官方 E-Shop 商品／自動化使用授權條款仍需依官方授權邊界審慎處理；技術上可取得 JSON 不等於已證明可供 GitHub Actions 無限制自動化使用。使用者已明確要求不採任何付費方案；不得推薦或採購付費資料商品。不得擅自把授權疑慮解讀成要求使用者付費。

### 下一個唯一工作
1. 在 `phase2-p0-ui-fixes` 先唯讀檢查目前 branch HEAD、相關 fetch/parser、DATA_REPORT schema 及測試；不改 master、P0 base、V8 或 data_reports 樣本。
2. 將新版 JSON 的 `fields`／`data` 真實欄名映射納入解析設計：TWT72U 取「整體市場」合計列；TWT93U 取最後「合計」列；兩者均不逐筆加總。
3. 加入原始 JSON fixture／欄位 mapping／合計列／遞推測試後，才執行程式修改及 CI；先不重建歷史 DATA_REPORT，直到 parser、來源範圍及使用條款邊界確認。
4. 任何變更均需記錄 commit SHA、GitHub reread、測試 Run ID；不得 Merge／Deploy，除非使用者另行明確授權。

### 本次驗收標記
- TWT93U 新版 RWD JSON 可取得：**PASS（使用者實測）**
- TWT72U 新版 RWD JSON 可取得：**PASS（使用者實測）**
- TWT93U 合計餘額與遞推：**PASS（使用者截圖）**
- TWT72U 整體市場合計與遞推：**PASS（使用者截圖）**
- 新版完整欄位 schema／parser mapping：**NOT TESTED**
- 助手獨立 HTTP 抓取：**BLOCKED（工具限制）**
- 程式接入／CI／DATA_REPORT 重建：**NOT DONE**
- 免費自動化授權邊界：**BLOCKED／待確認；不得因此推薦付費方案**


## 2026-11-04｜分支策略確認與三市場成果移植盤點（唯讀）

### 分支關係（GitHub compare 實測）
- 維持原案：以 `phase2-p0-ui-fixes` 為主線，選擇性移植 `fix/three-market-correlation-history` 的已完成成果；不整條 merge。
- P0 fixes HEAD：`8317dcb359b5629cf073c144068339322e89884a`。
- 三市場分支 HEAD：`e678877bc076e157c948483d40f136e0f504303e`。
- 共同祖先：`d5443eacb29b7b0824306de4d1b126b9281210b5`。
- P0 fixes 相對共同祖先 ahead 59 commits；三市場分支 ahead 105 commits；兩分支已 diverged。
- 兩分支 HEAD 的 combined status 均回傳空 statuses；本輪不能據此宣稱 HEAD CI PASS。既有 CI run 證據仍按各自歷史 commit／Run ID 記錄，不可轉嫁成最新 HEAD 的 CI 結果。

### 三市場分支應保留評估的功能群
- 三市場法人方向一致性／分歧解讀、四個分析卡深化及主力意圖證據界線（例如 commit `9c907d1b3919e24c3a62f87702197905e3f5e9c1`）。
- 三劇本價位觸發、方向衝突防護、夜盤方向判斷及合成情境資料有效性（例如 `7fd3e2d4e91acde2ecf587938c4432723f360b41`、`caa6eab52d26e4642ee69bfc9382427b405d8625`）。
- 選擇權法人力道分析端到端資料流與 UI（例如 `d7bf6ef0828172254fa02c296ee12fc7f3813dbd`、`aeb8fdb16f`、`ce55c9b013`）。
- 即時 Dashboard 資料衍生的 synthesis narrative（`bfafaec57521744d91e52a2dc49d87a2175350a1`）。
- 三市場圖表單位、金額精度、夜盤成交量單位、Max Pain 與支撐位語義修正。
- 相關性歷史資料 seed 與 workflow build 前執行（`32566de3a79b7f2f69acb4e0bf4d1cfe5f43c9db`）；此群會觸及 workflow／SQLite，需獨立驗收，不與 UI patch 綁定。
- 上述僅是移植候選功能群，不代表已移植或已在 P0 branch 驗證。

### 為何不以三市場分支為新 base
- 三市場分支的 `src/sources/spot_raw.py` 仍使用舊 TWT93U `/exchangeReport/TWT93U` 路徑及固定 row index，並逐筆加總；其 `spot.py` 仍將 TWT96U 可借券賣出限額與 TPEx 欄位併入借券餘額。這與目前已確認的借券指標定義及 P0 fixes 已完成的資料層修正不相容。
- P0 fixes 的 `spot.py` 已分離 TWT72U 借券餘額、TWT93U 上市借券賣出餘額、TPEx S47 上櫃借券賣出餘額，並排除 TWT96U；應保留這條資料層主線。
- P0 fixes 的 `spot_raw.py` 已使用新版 RWD 路徑、response date 驗證與 fields 欄名定位；但目前 parser／測試仍以個股列加總及小計對帳為主要邏輯，尚未落實使用者 2026-11-04 最新指定的合計列取值規則。TWT93U 應直接取最後「合計」列；TWT72U 應直接取「整體市場」合計列，不再逐筆加總。故借券 parser 仍需後續最小修正及真實 JSON fixture 驗證。
- 現有 P0 tests 的 TWT93U fixture 以個股列作為預期；TWT72U test 名稱及 fixture 明確測試 stock rows sum + subtotal reconciliation。這些測試契約需跟著最新合計列語義更新，不能沿用舊測試作 PASS。

### 移植執行順序（尚未寫入程式）
1. 保留 P0 fixes 資料層、Worker、DATA_REPORT 保護及授權註記。
2. 先移植／重做三市場分析卡、三劇本、選擇權法人力道及 synthesis narrative；每一功能群連同必要測試一起移植，並確認分析文字只引用圖表可見或可追溯的數值。
3. 單獨處理 correlation history seed／workflow／SQLite，不與前述 UI 功能一併改動。
4. 最後做完整 React template syntax、42 區塊、版面重疊、Builder JSON、DATA_REPORT 相容性回歸。
5. data_reports 樣本不修改；不 merge／deploy；master、P0 base、V8 不動。

### 本輪驗收標記
- 分支 HEAD／共同祖先／ahead 數：**PASS（GitHub compare）**。
- 三市場功能群識別：**PASS（commit message + 部分關鍵 diff/file read）**；完整逐檔依賴盤點仍未結束。
- 三市場分支不適合作為資料層 base：**PASS（spot_raw.py、spot.py 實際程式檢查）**。
- P0 借券 parser 符合最新合計列規則：**FAIL（目前仍以個股列加總／對帳）**。
- 兩分支最新 HEAD CI：**NOT VERIFIED（combined statuses 為空）**。
- 本輪未修改任何產品程式、DATA_REPORT、workflow、樣本或 Dashboard；未 merge／deploy。Recovery 文件更新除外。
- Auditor 為單一模型自我稽核，非獨立多模型審核。


## 2026-11-04｜借券 parser 合計列修正已提交（尚待執行測試）

### 工作主線與修改範圍
- 唯一產品工作分支：`phase2-p0-ui-fixes`；修改前確認 HEAD 為 `8317dcb359b5629cf073c144068339322e89884a`。
- 未建立、切換、合併或刪除任何分支；未修改 master、P0 base、V8、workflow、DATA_REPORT、data_reports 樣本或 Dashboard。
- 本次只修改 `src/sources/spot_raw.py` 與借券 parser 相關測試。

### 實際修改
- TWT93U：改為依既有 fields 欄名 mapping 定位最後一筆「合計」列，驗證該列前日餘額 + 當日賣出 - 當日還券 + 當日調整 = 當日餘額；直接回傳合計列，不再加總個股明細。
- TWT72U：改為直接定位「市場別=整體市場」列，驗證前日餘額 + 本日借券 - 本日還券 = 今日餘額；直接回傳整體市場合計列，不再加總個股或市場小計。
- TWT72U URL 改為使用者實測成功的原始 query：`/rwd/zh/lending/TWT72U?response=json&date=YYYYMMDD`，不再額外附加 `selectType=SLBNLB`。
- 更新語義測試 fixture：TWT93U 使用使用者提供的 2026-10-30 合計數值；TWT72U 使用使用者提供的整體市場餘額及遞推數值。這些是合成測試 fixture，並非完整原始 JSON fixture；完整 fields/data 原始回應尚未取得。
- 更新來源契約測試的 parser 診斷字串，以及 live probe 的 TWT72U URL。

### Commits（均在既定主線）
- Parser 合計列邏輯：`818cf6a80ff879f3d6f879370773758197d1bc02`
- TWT93U/TWT72U semantic tests：`428b8ec18737766988976b536fc09851c3fab981`
- TWT72U fixture 精簡為整體市場列：`ce9d746b9f2d74299f42bbf562d9458a6052938a`
- 借券來源契約測試更新：`dc0150eef8fb8a7a264ad3b677907ff10cdb72c0`
- TWT72U URL 對齊使用者實測 query：`f0515a798dc85526f307966f53fc120d4f280dd7`
- semantic/live test URL 更新：`c0cc0754b5bc7974358a6ad906f0beec5faaeb6d`、`3c246660355aa01697b2f29d6256248ef32f5ea7`
- TWT72U aggregate selector 放寬為只依「整體市場」標籤定位：`b0b9e2cb5140653062b8a7d03f23ca7fb5867562`
- 最終工作分支 HEAD：`b0b9e2cb5140653062b8a7d03f23ca7fb5867562`。

### 回讀與驗收
- GitHub 回讀已確認 parser 與三份測試檔案包含預期修改；最終 parser blob SHA：`9ed97c220bfc69595c2b883b8bb24fcaed5201bf`。
- TWT93U 合計列程式邏輯：**CODE REVIEW PASS**；實際新版 JSON fields 名稱對應：**NOT TESTED**。
- TWT72U 整體市場列程式邏輯：**CODE REVIEW PASS**；實際新版 JSON fields/data 完整 schema：**NOT TESTED**。
- 合成 fixture 的預期值與使用者截圖數值：**PASS（算術核對）**。
- Python unit tests／live API tests：**NOT TESTED**（目前本輪未執行測試環境）。
- 最新 HEAD combined status：空 statuses，CI **NOT VERIFIED**。
- DATA_REPORT 重建、GitHub Actions 自動化授權邊界：**NOT DONE／BLOCKED**；不得因 parser 修改就啟動歷史報告重建。
- Auditor：單一模型自我稽核，非獨立多模型審核。

### 下一步（保持收斂）
1. 執行 `tests/test_spot_borrowed_semantics.py` 與 `tests/test_fetch_data_borrowed_sources.py`，修正任何失敗。
2. 若可取得使用者原始 JSON 檔，將完整 fields/data 作為真實 fixture，驗證 parser mapping；不可把合成 fixture 當成原始 JSON。
3. 通過後再進入既定的三市場分析／選擇權法人力道成果移植；不重做已驗證的 P0 資料層。


### 2026-11-04｜CI 失敗修正與重跑結果（追加）
- 首次驗收在 commit `b0b9e2cb5140653062b8a7d03f23ca7fb5867562` 發現兩個實際缺陷：
  1. TWT93U live payload 的「合計」標籤位於 `名稱` 欄，不在 `代號` 欄；parser 原先只查代號欄，導致 live test FAIL。
  2. TWT72U 測試預期值手算錯誤；正確淨增減為 813,411,000 - 604,261,000 = **209,150,000 股**，不是 208,150,000。
- 修正：TWT93U 現可在「代號」或「名稱」欄辨識「合計」；semantic fixture 改為覆蓋「名稱」欄合計標籤；TWT72U 測試改為正確淨增減。
- 修正 commits：`dcacecdeeb214f7069af02cecc483cb56be10656`（TWT93U label mapping）、`00a5adb2ca6b55f7728b88b7ae182fa4b81a05de`（semantic fixture／TWT72U arithmetic assertion）。
- 最終工作分支 HEAD：`00a5adb2ca6b55f7728b88b7ae182fa4b81a05de`。
- Unit Contract Audit Run **41754077116 SUCCESS**：Python compile、borrowed source semantic tests、Dashboard unit contract、DATA_REPORT／field semantics、React template、TAIFEX night unavailable regressions 全部成功。
- Live borrowed sources job（同一 Run 41754077116）**SUCCESS**：TWT72U、TWT93U、TPEx S47 2026-10-30 live probe 全部通過。
- Daily Premarket V9 Pro Run **41754077121 SUCCESS**：build 成功、artifact 上傳成功；deploy job **SKIPPED**。Workflow log 顯示產生的 dashboard 沒有變更（No dashboard changes to commit），沒有對 master push；生成 commit 的保護條件只允許 P0 branches。
- 因為前一輪已存在失敗 Run（41753942232），不可刪除或隱藏失敗歷史；最終 HEAD 的最新驗收以 Run 41754077116／41754077121 為準。
- 最終狀態：TWT93U/TWT72U parser 語義與 live source probe **PASS**；DATA_REPORT 歷史重建與資料自動化授權仍 **NOT DONE／BLOCKED**；完整原始 JSON fixture 仍 **NOT TESTED**。


## 2026-11-04｜選擇權法人力道分析歷史成果恢復

### 恢復內容與來源
- 從 `fix/three-market-correlation-history` 的歷史實作選擇性恢復，沒有整條 merge：
  - Builder 分析函式來源：`aeb8fdb16fdfcbeeabc909db45ecdd76e2fa6b97`（後續以歷史分支最終版本為準）。
  - UI 區塊來源：`d7bf6ef0828172254fa02c296ee12fc7f3813dbd`；資料 JSON 映射來源：`ce55c9b013e9ef0efc9ec4dfbcbad281e65b687c`。
- `scripts/v9_pro_builder.py` 恢復 `build_option_force_analysis`，含缺值保護、金額欄位遞推／合計一致性檢查、日夜盤法人主導者、雙邊金額失衡率，以及與獨立淨口數資料的方向背離檢查。
- Builder 的 parsed options 與 final JSON 均新增 `instOptForceAnalysis`。
- `templates/v9-pro-react-template.html` 恢復原區塊 B 的選擇權法人金額力道表、可橫向捲動樣式及資料驅動分析文字；沒有新增 Dashboard layout 或改動 42 區塊 registry。
- 新增 `tests/test_builder_option_force_analysis.py`，涵蓋正常分析、金額／口數背離、缺值不轉零、不一致時停止方向結論、日淨－夜淨語義，以及既有 2026-11-02 DATA_REPORT 實際解析。
- 更新 `.github/workflows/unit-contract-audit.yml`，將此測試納入正式 Unit Contract Audit。

### 修正測試預期值的證據
- 歷史測試原先預期夜盤失衡率 -3.75%，但 P0 fixes 的既有 `DATA_REPORT_20261102.md` 法人力道表為夜盤多方 7.00、空方 7.41、淨額 -0.41 億元；依公式 `-0.41 / (7.00 + 7.41) * 100`，正確值為 **-2.85%**。
- 已按 P0 fixes 現有 DATA_REPORT 實際值調整測試預期；沒有修改 DATA_REPORT 樣本。

### Commits 與最終分支狀態
- Builder 分析邏輯與 JSON：`a8984267718f0c39f840500a1b849b07bfcabb29`。
- React UI 區塊與 CSS：`7f1d5edca0033f980da503163fa1b2508c8317a4`。
- 恢復分析測試：`ed8d4ee652b021a0f5177a67bea4c61476184b7e`。
- CI 加入測試：`0a8e36bcecbc6c819560746b09614215f35d3f22`。
- 測試預期值修正：`ab53d93020f4a3d5b225521fb81a1bff95dcd482`。
- Daily Premarket build 自動產生 dashboard commit：`466182c83e861f94e5696115308e215da9bf829c`（parent 為 ab53d930；僅修改 `dashboards/index.html`、`dashboards/v9-pro-20261102.html)、`dashboards/v9-pro-latest.html)，未修改 DATA_REPORT。
- 目前分支 HEAD：`466182c83e861f94e5696115308e215da9bf829c`。

### 驗收證據
- Unit Contract Audit Run **41754523955 SUCCESS**（含新 option-force 測試、borrowed parser tests、42 區塊 contract、DATA_REPORT tests、React template tests、TAIFEX night unavailable tests）。
- Live borrowed sources job 同一 Run **SUCCESS**。
- Daily Premarket V9 Pro Run **41754523920 SUCCESS**；build／artifact upload 成功，deploy **SKIPPED**。
- V9 UI Fixes Regression Run **41754377688 SUCCESS**；V9 Dashboard Browser Audit Run **41754377599 SUCCESS**（針對恢復後的 React template commit）。
- 生成的 `dashboards/data-20261102.json` GitHub 回讀 blob SHA `53a44f7552f787079643cd7dcc72a96280fe0597`；其中 `options.instOptForceAnalysis.status=available`，分析文字包含可追溯至法人金額表及法人淨口數表的值。
- 生成 HTML 回讀 blob SHA `512da9759071c2d19ec5092211f6036acd1a65d9`；確認包含恢復後區塊標題及動態分析文字。
- Browser/UI test 已通過，但本輪沒有人工逐像素檢查所有 42 區塊；完整全版面人工驗收 **NOT TESTED**。
- 歷史 P0 fixes 版本的 2026-11-02 dashboard 由 Builder 重新產生，這是既有報告的 build 測試，不代表重建或修改 DATA_REPORT 樣本。

### 狀態
- 選擇權法人力道 Builder 資料鏈：**PASS**。
- 選擇權法人力道 UI／分析文字：**PASS（template regression + browser audit）**。
- 新增分析單元測試：**PASS**。
- 生成 JSON／HTML 含分析結果：**PASS（GitHub readback）**。
- 全 42 區塊人工視覺逐一驗收：**NOT TESTED**。
- 未完成的下一組歷史成果：三市場分析卡深化與三劇本條件／資料有效性恢復；之後再處理相關性歷史 seed／workflow。


## 2026-11-04｜三市場分析卡與情境條件恢復

### Builder（三市場四張分析卡）
- 由歷史分支 commit `9c907d1b3919e24c3a62f87702197905e3f5e9c1` 選擇性恢復，未整條 merge。
- 新增／恢復四個分類 helper：`classify_three_market`、`classify_futures_oi`、`classify_option_sessions`、`classify_spot_institutions`。
- 恢復四張卡的證據與條件式解讀：`三市一致性`、`期現選方向對照`、`籌碼三市矩陣`、`主力意圖解碼`。
- 明確區分現貨億元（買賣超金額）、期貨／選擇權口數（交易流量）、期貨 OI（部位存量）；不跨單位加總、不將單一 OI 快照當成新增交易、不從資料不足推定主力控盤意圖。
- 新增 `tests/test_spot_institution_classification.py`、`tests/test_three_market_scenarios.py` 並納入 Unit Contract Audit。

### React synthesis／三劇本條件
- 從歷史 template 恢復 `v9ProCorrelationMatrixReady` 與 `v9ProSynthesisAnalysis`，只移植分析 helper 與既有區塊的 analysis 綁定，沒有替換整個 `y2` component，也沒有改變 Dashboard layout。
- 恢復日夜盤價格／成交量與外資夜盤流量對照、三劇本價格條件（偏多／區間／偏空）、相關性矩陣品質檢查、交易計畫的條件式觀察。
- 三劇本不輸出未回測機率；偏多條件要求現價高於有效 Flip 且上方有有效價位，偏空要求現價低於 Put Wall 且有下方有效參考位；區間需有效 Put／Call Wall 與現價關係成立。
- 相關性矩陣須維度一致、數值有效且落在 -1 至 +1，否則不顯示熱圖。

### Commits 與驗收
- Builder 三市場 helpers／四張卡：`bc3348522fd827dbde8f95a64ce22c727138e7af`。
- 三市場測試：`89e5e952a6efb7870aa9b25952258093e91d87c5`、`9d7432e84517b5378231ca937ea5adf739573294`。
- Unit Contract workflow 納入測試：`df2e5d59467966454e18eeaa0bda8ae2379fd8bb`。
- React synthesis／scenario helper：`df783b964a6289e578bb1d176391c5c5c0e05d0a`。
- 最終程式 Unit Contract Audit Run **41755176208 SUCCESS**；內含三市場分類／scenario tests、option force analysis tests、borrowed parser tests、42 block contract、DATA_REPORT、React template 與 TAIFEX night regressions。
- V9 Dashboard Browser Audit Run **41755176320 SUCCESS**；六分頁 Desktop／Mobile audit。
- V9 UI Fixes Regression Run **41755176398 SUCCESS**。
- Daily Premarket V9 Pro Run **41755176415 SUCCESS**；build、artifact upload 成功，deploy **SKIPPED**。
- 自動 build commit：`a658dd90d073a8d84fb07afd229a781407dc6ebd`（parent `df783b9`），只修改三個 dashboard HTML aliases/index，沒有修改 DATA_REPORT 樣本、Builder、template 或 master。
- 最終產品分支 HEAD：`a658dd90d073a8d84fb07afd229a781407dc6ebd`。
- 生成的 `dashboards/data-20261102.json` blob SHA `57efd362922948cfd662f9e0564e952ad28e2474`；`dashboards/v9-pro-20261102.html` blob SHA `85605a2eb66ac3d43952da5d835343ccd8b47f24`，均已 GitHub 回讀。
- JSON 顯示 `visible_block_count=42`；沒有增加 Dashboard 區塊或更換 layout。人工逐一檢查所有 42 區塊仍 **NOT TESTED**。

### 下一步
- 選擇權法人力道分析、三市場四卡、三市場分類與三劇本／synthesis 已恢復並通過目前自動測試。
- 尚待恢復／整合：相關性歷史資料 seed／workflow／SQLite（單獨處理），以及歷史分支其餘 UI／分析修正候選。
- 不要重做以上已通過測試的項目；若後續修改觸及相關檔案才做 targeted regression。保持唯一主線、不開新分支、不整條 merge。


## 2026-11-04｜Correlation history seed 已恢復並通過 P0 實際報告驗收

### 實際問題與修正
- 首輪 P0 Unit Contract Audit Run `41755904315` **FAIL**：`fetch_yahoo_twii_30d` 在 P0 分支使用 Yahoo `range=1mo`，部分歷史日期僅取得 14 筆，RSI=None，導致第一筆歷史樣本 `correlation_eligible=0)，五筆 replay 無法累積。
- 比對歷史分支後確認該函式差異只有 Yahoo range：歷史版本為 `3mo`，P0 版本為 `1mo`。已將 P0 恢復為 `range=3mo&interval=1d`，不降低 correlation eligibility 門檻。
- 修正 commit：`1a49f9a15dc45dddb6c0c7a1a322d1d79ad832e8`。
- 已恢復 `seed_correlation_history_for_dashboard`、`run_historical_correlation_replay)、CLI `--seed-correlation-history`／`--history-replay`。
- Daily workflow 在 Builder 前 seed 最近五份已提交、日期不晚於 T0 的 DATA_REPORT；seed 不可用時只發 warning，dashboard 繼續建置並保持 heatmap unavailable，不讓單一分析欄位阻斷整份 dashboard。
- Unit Contract Audit 執行 `--history-replay`：用暫存 DB、實際 P0 branch 五份歷史 DATA_REPORT 驗證逐日累積；不寫入正式 DB、不修改 data_reports。
- `.gitignore` 加入 `dashboards/v9_pro_history.db`；確認 DB 由每次 build 從 DATA_REPORT 重建，不應作為持久化輸出。曾由 build 自動 commit 的 tracked DB 已從 P0 branch 刪除，避免後續生成 commit 持續改動 SQLite；刪除 commit：`4fb002951f463d5964f3c88970ddf78497ecaba9`。

### P0 實際驗收
- Unit Contract Audit Run **41756154308 SUCCESS**：Replay 五筆實際 P0 DATA_REPORT（20261027、20261028、20261029、20261030、20261102），五筆皆 `correlation_eligible=1)，最終有限值、對稱的 **8×8 Pearson matrix**，PASS。
- Daily Premarket V9 Pro Run **41756154307 SUCCESS**：seed 最近五份報告成功；輸出 `Pearson 相關係數｜完整有效樣本 5 筆｜最近 5 筆`；Builder／JSON／HTML build 成功；Deploy **SKIPPED**。
- V9 UI Fixes Regression Run **41756154315 SUCCESS**。
- 2026-11-02 dashboard JSON 回讀 blob SHA：`556a9d076a8eb83ca974a2199bf496ef1c24cca2`；`analysis.correlation.labels` 8 項、matrix 8×8，`visible_block_count=42`。
- Daily build 產生 commit：`d298ff039a463d94b8740f48f60d11064cf9c4e3`；只修改 dashboards JSON／HTML aliases 及當時被追蹤的 SQLite DB。其後 DB 移除 commit `4fb002951f463d5964f3c88970ddf78497ecaba9`；最新 tree 確認 `dashboards/v9_pro_history.db` 不再追蹤，下一次 build 仍可由 seed 重建。
- 最新產品分支 HEAD：`4fb002951f463d5964f3c88970ddf78497ecaba9`。
- 目前 correlation heatmap 只有 5 筆有效樣本；係數僅作探索性歷史共變參考，不代表因果或下一交易日預測。增加樣本需後續 DATA_REPORT 累積。
- DATA_REPORT 樣本均未修改；seed/replay 僅讀取資料。

### 本輪恢復項目狀態
- TWT93U／TWT72U 合計列 parser：PASS。
- 選擇權法人力道 Builder／UI／分析：PASS。
- 三市場分類／四張分析卡：PASS。
- 三劇本／synthesis／交易條件：PASS。
- Correlation replay／seed／8×8 matrix：PASS。
- 全 42 區塊人工逐一視覺檢查：NOT TESTED；自動六分頁 Desktop／Mobile browser audit 已 PASS。
- 後續只需針對剩餘歷史 UI／分析修正候選做選擇性恢復，不重做以上已通過項目。

## 2026-11-04｜歷史分支差異收斂與因子分析 CI 修正

### 歷史分支差異稽核
- 比較產品主線 phase2-p0-ui-fixes（修正前 HEAD dc73d21cbaff9ca1802999a515ccbc0f1d27fad8）與歷史分支 fix/three-market-correlation-history（HEAD e678877bc076e157c948483d40f136e0f504303e）：tree 共 35 個路徑不同，其中程式／測試／workflow／文件 25 個。
- Builder 關鍵函式 build_option_force_analysis、三市場四個 classifier、seed_correlation_history_for_dashboard、session_leaders、V9Analyzer、find_historical_similarity 均相同或只有空白差異；build_41_cards() 只有主線增加「跨市場訊號分歧」說明，未發現需整段移植的歷史 Builder 邏輯。
- Template 比對：三劇本 Pth、圖表 mf、共用卡片 V 等核心元件相同；主線 y2／v2 已有動態 synthesis 分析、區塊樣式及資料缺值保護。歷史分支的因子文字計算 17 個有效因子總和，但圖表只顯示前 8 項；不能直接移植，否則會再次出現分析文字引用圖表看不到的數字。
- 歷史分支來源層 src/fetch_data.py、src/sources/spot.py、spot_raw.py、taifex.py 與主線不同；歷史版仍有舊 TWT93U endpoint／固定列索引及 TWT96U 借券欄位混用風險。保留 P0 主線較新的資料來源與借券語義，不回退。
- 主線獨有 workers/taifex-proxy_V1.5.js、借券 live／semantics tests 及 P0 parser 保護均保留。
- 結論：已知歷史 UI／分析成果大多已選擇性吸收；本輪未發現值得整條 merge 或回退資料層的候選。後續不重做已 PASS 項目。

### 因子貢獻敘述與 CI 缺陷
- 主線 commit dc73d21cbaff9ca1802999a515ccbc0f1d27fad8 的 Unit Contract Audit Run 41759852834、UI Fixes Regression Run 41759852808 均 FAIL，原因是 synthesis runtime test 仍期待「正向貢獻合計」，但 template 已改成只列圖表前 8 項主要正負因素，造成測試契約與實際輸出不一致。
- 修正 commit：243bc10952731450f69f773021d6a7dc656a1005。
- 修改 templates/v9-pro-react-template.html 與 tests/test_react_template_static.py：正向／負向／淨貢獻合計只計算圖表實際顯示的有效前 8 項，且先依圖表顯示精度四捨五入至 1 位小數再加總；主要正負因素與最大絕對貢獻因素亦只引用圖表可見項。明確聲明可見子集合計不等於完整 17F 總貢獻，避免隱藏數字與過度推論。
- 新增 runtime assertions：以 fixture 驗證正向合計 +1.8、負向合計 -9.0、可見淨貢獻 -7.2，均與圖表一位小數標籤一致；並驗證不得把可見子集合計說成全部 17 因子總貢獻。

### 修正後驗收
- Unit Contract Audit Run 41761016184 SUCCESS；test_synthesis_narratives_are_derived_from_live_data PASS；相關性 replay 以五份真實 DATA_REPORT 累積 5/5，輸出有限值、對稱 8×8 matrix；所有列出的單元測試均 OK。
- UI Fixes Regression Run 41761016206 SUCCESS；21 tests 與 12 tests 均 OK，V9 17F／42 visible blocks contract OK。
- Daily Premarket V9 Pro Run 41761016255 SUCCESS；seed 五份報告成功，JSON／HTML build 成功，browser audit gate=True；六頁 Desktop／Mobile 共 12 個 viewport 全部 PASS，Browser audit artifact ID 13290800310；Deploy SKIPPED。
- 程式 commit 243bc10952731450f69f773021d6a7dc656a1005；自動 build commit b7153a3199494a4f8004bea2dd23afbc828c25b9（只更新 dashboards HTML aliases/index，沒有修改 DATA_REPORT）。
- GitHub readback：template blob d5fc77bc3d524a320e27f3107597db87077c3173；test blob 8ca29acdfcd8004d3f26149f547848e8d84cedf0；JSON blob 99df8ced5b412b00c22149d1bfeb66e1601f0102；HTML blob 6432e70a575358498d1febb7f9024c6db05d4e97。
- 產品主線最新 HEAD b7153a3199494a4f8004bea2dd23afbc828c25b9。未切換／建立分支，未 merge、未 deploy，未修改 DATA_REPORT。

### 尚未完成
- 42 個可見區塊人工逐一評分／視覺檢查仍 NOT TESTED；自動 Browser Audit 六頁 Desktop／Mobile 12 viewport PASS 不等於人工 42 區塊分析品質驗收。
- docs/P4_EARLY_ANALYSIS_ENGINE_PLAN.md 已明確記錄：42 區塊完整 ID／資料欄位／profile 映射 BLOCKED／待完成；LLM analysis runtime NOT IMPLEMENTED；95% 分析品質目標 NOT TESTED。不可宣稱目前已達 95% AI 分析品質。
- 下一步依 P4 計畫先完成 42 區塊對照表及分析 profile 盤點，再逐區塊改善；保留既有 17F 量化層、資料真實性及缺值防護，不推倒重寫，也不直接移植歷史分支引用全 17 因子隱藏總和的文字。

## 2026-11-04｜P4 42 區塊 Profile 盤點啟動

- 重新檢查發現 42 區塊的結構資料映射並非空白：現有 docs/DASHBOARD_UNIT_MAP.md 已列出 1–42 的頁籤、JSON path、DATA_REPORT 來源、單位及缺值規則。因此修正 P4 計畫原先「42 區塊完整映射 BLOCKED」的過時狀態。
- 新增 docs/P4_ANALYSIS_PROFILE_MAP.md，建立 42 個獨立分析 profile 草案；每個 profile 都有必答分析問題、交叉驗證／反證、操作觀察與禁止推論。程式檢查確認 42 rows、42 unique IDs、無缺號。
- 更新 docs/P4_EARLY_ANALYSIS_ENGINE_PLAN.md：結構映射 PASS；42 個 profile 草案 DRAFTED；Profile → Builder／React 綁定 NOT IMPLEMENTED；LLM provider BLOCKED；AI runtime NOT IMPLEMENTED；42 區塊逐一評分及 95% 品質目標 NOT TESTED。
- 文件 commits：profile map 4e32c32855665a0b1475753bd4777eea9756fe48；P4 plan status 8ecc6d334f6df9196883b2274abb611852c36cbd。產品分支最新 HEAD 8ecc6d334f6df9196883b2274abb611852c36cbd。
- 本輪僅新增／更新規格文件，尚未把 42 profiles 接入 Builder 或 React；不可宣稱分析 runtime 已完成，也不可宣稱 95% 達標。
- 下一步：逐項對照 profile 與目前 React template／Builder 的實際資料綁定，先選核心區塊（三市場法人、期貨籌碼、選擇權結構、相關性、交易計畫）作 profile-to-output 試點；不得一次改版或改動 42 區塊 layout。

 
## 2026-11-04｜P4 期貨頁六區塊分析 Profile 試點

- 依 docs/P4_ANALYSIS_PROFILE_MAP.md，先完成期貨頁六區塊中的五個獨立敘述（台指期日盤、台指期夜盤、期現貨價差、法人 OI、日夜法人交易）；既有「夜盤劇本」保留 v9ProSynthesisAnalysis 的價格／外資夜盤流量交叉判讀。未改六頁版面、圖表、資料來源或 Builder JSON schema。
- 新增 template helper v9ProFuturesAnalysis，將日盤／夜盤 OHLC、前結算漲跌、基差、正逆價差、法人 OI 存量、外資日／夜盤淨交易流量分開分析。
- 實際 2026-11-02 fixture 驗證：
  - 日盤收盤高於開盤，但相較前結算仍下跌 44 點；分析明確區分兩種比較基準。
  - 夜盤收盤低於日盤收盤，且收在夜盤區間下緣；不把夜盤走勢當作現貨開盤預測。
  - 日盤正價差與夜盤跌勢同時存在；敘述明確禁止以正價差抵銷夜盤跌勢。
  - 外資 OI -89,379 口、投信 +89,139 口、自營 +1,307 口、三大法人合計 +1,067 口、前十大 +14,239 口；明確指出法人分歧及前十大與外資方向相反。
  - 外資日盤淨交易 +2,801 口、夜盤 -1,349 口；明確指出日夜流量反轉，且與 OI 存量分開解讀。
- 所有分析數值取自該卡可見的圖表／表格欄位；OI 合計對應同卡表格「三大合計」列；缺值不補零，0 口仍是有效數值。若日盤收盤缺值，不建立夜盤收復日盤收盤的觸發條件。
- 程式 commits：3b86ca1f182f407decb11de291d0eac2bc14c493（helper＋runtime test）、7a8b35b71dd2de2c659bb6ed7c4b13018eeac133（缺值 fallback 與測試修正）、aaee46124d6688e4cbef32fca34c69e9f693d8d7（fixture newline test fix）。
- 驗收：UI Regression Run 41762406835 SUCCESS（React template 22 tests OK、17F contract OK）；Unit Contract Audit Run 41762406842 SUCCESS（含相關性 replay 5/5、template 22 tests OK）；Daily Premarket Run 41762406847 SUCCESS、Deploy SKIPPED。
- Browser audit：Template commit 7a8b35b 的 Daily Run 41762276445 gate=True，六頁 Desktop／Mobile 共 12 viewport 全 PASS；Futures 頁可見文字已顯示日盤 OHLC 與「日內收高於開盤、相對前結算仍下跌」的動態敘述。後續 aaee commit 只改測試，不改 template；其 Daily Run browser audit gate=False 為預期。
- 最新 template blob 47ae47f39b24fe4f7e4e4989ec1b592a71333136；test blob 0a5c14d635b87b9a5e586cbb046fcfaf25876c9d；JSON blob 99df8ced5b412b00c22149d1bfeb66e1601f0102；HTML blob bfd9a3cd299336469e6d781f363953cfd427b128。
- 產品主線最新 HEAD aaee46124d6688e4cbef32fca34c69e9f693d8d7；無 deploy、無 merge、未修改 DATA_REPORT。

### 下一個 P4 試點
- 期貨頁試點已完成自動化驗收；下一個核心試點為選擇權結構（PCR／OI 分布／Wall、Flip、Max Pain／法人交易／GEX）。
- 仍未接入 LLM runtime；本次是可重現的資料驅動分析，不得稱為 AI 模型已完成或 95% 品質達標。

 
## 2026-11-04｜P4 選擇權頁八區塊 Profile 試點

- 新增 v9ProOptionsAnalysis，將選擇權頁 8 張卡全部改為資料驅動分析：PCR／成交量結構、主要 OI 集中、Call OI Top10、Put OI Top10、Wall／Flip／Max Pain、法人日夜交易、前十大交易人 OI、履約價 GEX。
- PCR：以實際 Call／Put 成交量計算占比，與 OI PCR 分開解讀；核對 PCR 欄位與 Put OI／Call OI 重算值。
- OI 分布：引用圖表前三大履約價、口數及占比，並比較現價位置；不把集中 OI 直接當支撐／壓力，不在缺少同到期月份前值時推論增減。
- Wall／Flip／Max Pain：區分各價位；Max Pain 明確只作到期損益分布磁吸參考，不作支撐、壓力或價格目標。
- 法人交易：分開日盤／夜盤淨交易口數與法人分項；不與契約金額或 OI 存量混算。
- 前十大交易人 OI：分別呈現 Call／Put 多方、空方、淨 OI；說明淨 OI 是未平倉部位差，不是當日流量，跨到期月份不得直接比較變化。
- GEX：敘述只取圖表顯示的前 16 大絕對值履約價，指出最大正／負曝險與 Net／Gross GEX；明確說明模型估值不等於造市商真實持倉或市場方向預測。
- 2026-11-02 fixture 實測：Call／Put 成交量占比 50.8%／49.2%，OI PCR 0.57；Call OI 最大 48,000 點 4,503 口（7.31%），Put OI 最大 44,000 點 2,661 口（7.63%）；現價 44,920.14；法人日盤合計 +870 口、夜盤 -4,222 口；前十大 Call／Put 淨 OI -2,873／-2,040 口；Net／Gross GEX +3,510,697,648／+16,362,020,679 NT$；圖表最大正曝險 46,000 點 +458,793,202 NT$、最大負曝險 44,000 點 -271,383,835 NT$。
- Runtime tests 覆蓋實際 fixture、缺值及零值，確認缺值不補零、零值不誤判缺值、GEX／OI／成交量不跨語義。
- 程式 commit 8782ff2a0aac3d5867d4d4752553c750943b887c；PCR／Top10 文案及測試契約修正 commit 7e7fa9d6009edefae6cef5e2a675982d13dce457、5ed470d40a4cbd0ccdf7afa2fbeeff873ee5e847。
- 驗收：Unit Contract Audit 41763494591 SUCCESS（含 options runtime test、23 template tests、correlation replay 5/5）；UI Fixes Regression 41763494945 SUCCESS（23 tests、12 tests、17F／42 visible blocks contract OK）；Daily Premarket 41763494658 SUCCESS，Deploy SKIPPED。
- Browser Audit：template commit 7e7fa9d 的 Daily Run 41763372720 gate=True，六頁 Desktop／Mobile 共 12 viewport 全 PASS；選擇權頁 Desktop／Mobile 均 PASS，畫面文字已呈現動態 PCR 成交量占比。
- GitHub readback：template blob 9790c9564163f554261443efd2a678cca5dd967a；test blob 5b8dd9a02e84e3ceabfe4510f361ed5c38b1aea2；JSON blob 99df8ced5b412b00c22149d1bfeb66e1601f0102；HTML blob 62120258c9578b46f8e762b0711f839c85679192。
- P4 profile binding 現況更新為 20/42：22–27、28–35、36–37、39–42 已接入；01–21 與 38 尚待接入。profile map 與 P4 plan 已更新。
- 產品主線最新 HEAD 5b31daf471ec44a505d9055291d54b6f1290a5cb。未 merge、未 deploy、未修改 DATA_REPORT。

### P4 後續工作
- 下一步處理 ID 01–21（總覽／現貨／重要市場）及 ID 38（日夜盤劇本），先做資料綁定盤點再逐頁接入。
- LLM analysis runtime 仍 NOT IMPLEMENTED；42 區塊人工品質評分及 95% 目標仍 NOT TESTED。


## 2026-11-04｜P4 ID 38 日夜盤劇本接入完成

- 產品主線：`phase2-p0-ui-fixes`；程式提交：template `a434451ec354a53521d26bd055ca05041c37752d`、runtime test `f1b00a81ab42aaca980a5b39a63d917903a33c82`；後續 P4 文件提交：plan `e75682484342a5c16949d7c75701d8066063f723`、profile map `9a22d56a4963680608d2aea591fcaa0589f6c941`。
- ID 38「綜合分析／日夜盤劇本」由原本固定文字改接既有 `v9ProSynthesisAnalysis.night`。分析取日盤／夜盤收盤、日夜成交量、外資夜盤淨交易及外資 OI；依日夜收盤差與外資流量辨識同向／背離，提供開盤收復／守住日盤收盤的條件觀察。
- 移除原敘述引用但卡片未顯示的夜盤低點；新敘述不再使用 `night.l`，避免分析出現圖表／表格看不到的數字。日盤或夜盤收盤缺值／無效時不產生價位觸發；零值價格仍視為無效，外資流量／OI 的 0 仍是有效值。
- 測試新增 ID 38 區塊綁定斷言，並更新實際、missing、zero、夜盤上漲／下跌 fixture 的 target 預期。
- 驗收：Unit Contract Audit Run `41768827082` SUCCESS（React template regression tests completed SUCCESS；live borrowed sources SUCCESS）；UI Fixes Regression Run `41768827095` SUCCESS；Daily Premarket Run `41768827031` SUCCESS，20261102 Dashboard build 與 20261030 full-day fixture JavaScript validation SUCCESS，Deploy SKIPPED。
- Browser Audit：template commit `a434451` 對應 Daily Run `41768820962`，gate=True，六頁 Desktop／Mobile 共 12 viewport 全 PASS、pageErrors=[]。該 run 最終因同時提交造成 generated dashboard push non-fast-forward 而整體 FAILURE；後續 Run `41768827031` build／history push SUCCESS，但因觸發 commit 只改 tests，browser gate 按 workflow 規則 SKIPPED。Browser PASS 與 workflow push failure 分開記錄，不混為整體 PASS。
- 初次 Unit Audit Run `41768820878` 因測試仍期待舊 target 文案而 FAIL；已更新測試契約，後續 Run `41768827082` SUCCESS。初次 Daily Run `41768820962` 的 build/browser 成功，僅 generated dashboard push 因並行 commit 被拒；後續 Run `41768827031` 已成功推送生成檔。
- 自動生成 dashboard commit：`83bbc1c2e1052161aad0aeb1950f3d6e6b48b76d`，只修改 dashboards/index.html、v9-pro-20261102.html、v9-pro-latest.html；未修改 DATA_REPORT。最新產品主線 HEAD 隨 P4 文件更新為 `9a22d56a4963680608d2aea591fcaa0589f6c941`。
- Template blob `281843f8727a76f3b14394b6ba2465b8bfba6626`；test blob `267ca92425b429b8fa22c5494132efda0f2eaef1`。已 GitHub 回讀確認 ID 38 綁定及舊固定文字移除。
- P4 runtime binding 更新為 21/42：原 20 個已驗收區塊不重做；ID 38 新增完成。下一步只處理 ID 01–21（總覽／現貨／重要市場），不重做 ID 22–42。
- 未 merge、未 deploy；未修改 master、P0 base、V8 或 data_reports 樣本。LLM runtime NOT IMPLEMENTED；42 區塊人工品質評分與 95/100 目標仍 NOT TESTED。


## 2026-11-07｜DL-01～DL-07 最新進度（DL-05 結案）

> 本節為最新狀態索引，若與前文歷史紀錄衝突，以本節及 GitHub 最新可查證狀態為準。DL-06／DL-07 尚未取得可核對的正式範圍與驗收證據，不推定其狀態。

| DL | 主題／目前判定 | 狀態 | 最新說明 |
|---|---|---|---|
| DL-01 | 交易日期正確性 | **PASS／CLOSE** | 已完成；不重開。 |
| DL-02 | 現貨／借券資料品質 | **PASS／CLOSE** | 已完成；不重開。 |
| DL-03 | 期貨／選擇權資料品質 | **PASS／CLOSE** | 已完成；不重開。 |
| DL-04 | 維持率及外部市場資料 | **PASS／CLOSE** | 已完成；自建上市維持率為主、Blave 交叉驗證／備援，差異小於 1% 可接受；不重開。 |
| DL-05 | DATA_REPORT data contract | **PASS／CLOSE** | 本日完成最後一項 Builder unavailable 缺值傳遞修正及回歸測試，詳見下節。 |
| DL-06 | 報告產生安全性／錯誤處理 | **NOT ESTABLISHED** | 目前交接資料未提供可核對的正式範圍、逐項驗收或結案證據；不得標示 PASS／CLOSE，也不在本次擅自擴大清查。 |
| DL-07 | 測試與最終驗收 | **NOT ESTABLISHED** | 目前交接資料未提供可核對的正式範圍、逐項驗收或結案證據；不得標示 PASS／CLOSE。DL-05 的 CI 測試不等同 DL-07 整體結案。 |

### DL-05 最後修正（2026-11-07）

- 工作分支：phase2-p0-ui-fixes。
- 最終產品分支 HEAD：1f5202003c3969ecca2dddadcdd479dafc134e5e。
- 只修改 scripts/v9_pro_builder.py：DATA_REPORT 明確標示 unavailable 的欄位轉成 None，不再因單一欄位缺值而使 Builder 解析中止；必要欄位列或章節不存在仍維持 fail-closed。
- 只修改 tests/test_fetch_data_borrowed_sources.py：新增現貨、期貨、選擇權缺值傳遞測試，以及必要欄位列缺失仍報錯的反向測試。
- 獨立測試檔 tests/test_builder_unavailable_fields.py 曾短暫建立，之後已刪除；最終變更範圍不包含該檔。
- GitHub Actions Run #431 / Run ID 42377949845：SUCCESS。
- CI log 驗證：回歸測試共 53 tests passed；Dashboard data build、React template injection、2026-10-30 full-day fixture build、HTML JavaScript validation、Pages artifact upload 均 PASS。
- GitHub 回讀確認上述兩檔已包含修正；最終 branch HEAD 與該次 CI head SHA 一致。
- 與前一個已驗證產品 HEAD 889c1c980c452e1d9c00992f66e1c303fe0290cf 比較，僅上述兩個檔案有差異；沒有修改 data_reports 樣本、Worker、V8、P0 base 或 master。
- 未執行正式 DATA_REPORT 重新抓取；Browser 桌面／手機視覺驗證 NOT TESTED；Pages 實際部署 NOT TESTED／未執行。artifact upload 不代表 Pages deploy。
- DL-05 結案條件已達成：契約允許的明確缺值可傳遞，必要結構缺失仍會失敗，針對性測試及 CI 通過。未測項目保留標記，不再延長 DL-05 或追加清查。

### DL 最新接續原則

1. DL-01～DL-05 不重開；若未來出現新的可重現證據，才針對該具體缺陷另案處理。
2. DL-06／DL-07 暫列 NOT ESTABLISHED；在找到正式定義及現存證據前，不臆測其完成度。
3. 不把 DL-05 的局部 CI 通過擴張解讀成 DL-06／DL-07 全面通過。
4. 本次只更新 Recovery 文件分支；不修改產品程式、DATA_REPORT、Workflow、Dashboard，不 Merge／Deploy。


## 2026-11-07 最新進度｜DL-06 重試驗收完成；DL-07 離線驗收第一階段完成

### DL-06
- 產品分支：`phase2-p0-ui-fixes`。
- DL-06 隔離重試 Workflow：`.github/workflows/dl06-retry-tests.yml`。
- 最終隔離測試 commit：`0980de4edce4a0ccea5260e28fad43a0b89850eb`；Actions Run ID `42381174670` SUCCESS。
- 以現有 production retry shell 搭配 mock Fetch／mock validator 驗證三情境：第一次 Fetch 失敗後第二次成功、第一次報告驗證失敗後第二次成功、連續兩次失敗最終非零退出；三項均 PASS。
- 測試只使用 TemporaryDirectory，不呼叫正式 Fetch、不寫正式 DATA_REPORT、不 commit、不 deploy。
- DL-06 程式安全及隔離重試驗收：**PASS／CLOSE**。正式市場 API Fetch／正式 daily_data Workflow 實際重跑：**NOT TESTED**，不包含在隔離重試結案聲明內。

### DL-07 第一階段
- 新增唯讀離線驗收 Workflow：`.github/workflows/dl07-offline-validation.yml`。
- 最終產品分支 HEAD／CI head SHA：`a52ce7800e155d51da3e4091269089cd53c1d8fe`。
- 本次與 DL-06 最終 HEAD `0980de4edce4a0ccea5260e28fad43a0b89850eb` 比較，**只有新增上述一個 Workflow 檔案**；沒有修改產品程式、DATA_REPORT 樣本或 Dashboard 版面。
- Actions Run ID `42381892154` SUCCESS： [DL-07 Offline Unit and Integration Validation](https://github.com/grichtoyang/daily-premarket/actions/runs/42381892154)。
- 驗收證據：
  - **282 個離線單元測試 PASS**。
  - DL-06／DL-07 Workflow 唯讀權限、無 commit／push／deploy side effect 檢查 PASS。
  - 更新後 DATA_REPORT 必要／選填欄位解析、比例變化百分點單位、Treasury 20Y 備援語義契約 PASS。
  - V9 Pro 17F offline self-test PASS。
  - 使用 `git archive` 建立 runner temp workspace，對 `DATA_REPORT_20261030.md` 與 `DATA_REPORT_20261102.md` 重建 Builder JSON；兩份 T0／版本檢查 PASS。
  - 在 temp workspace 注入 React HTML；兩份 HTML 各 4 個 executable inline scripts，JavaScript validation PASS。
  - `git diff --exit-code -- data_reports/ dashboards/` PASS；正式 Checkout 的 DATA_REPORT 樣本與 Dashboard 輸出未變更。
- 10 個測試案例未納入 282 個測試數：
  - `test_spot_borrowed_live` 3 個 live API probe：避免離線測試碰外部市場 API，**NOT TESTED**。
  - `test_p0_workflow_isolation` 4 個測試：仍引用目前 UI fixes 分支不存在的 `.github/workflows/test-data-report-margin-ratio.yml`；該舊測試未執行。DL-07 另有針對現存 DL-06／DL-07 Workflow 的唯讀及 side-effect 檢查 PASS，但不等同舊 P0 workflow isolation 測試全數驗證。
  - `test_dashboard_unit_contract.py` 3 個舊 source-text assertions：期待舊 Builder／Fetch／Treasury 寫法，與目前等價實作不一致；未執行原 assertions。Workflow 已以目前實作語義重新驗證 required/optional parser、pp 單位及 Treasury 20Y fallback，PASS。原測試檔未修改。
- DL-07 尚未結案。以下項目仍明確保留：
  - 正式 Fetch／歷史日期重新抓取：**NOT TESTED**。
  - 正式 `daily_data.yml` Workflow：**NOT TESTED**；不得手動觸發此正式資料流程作為離線測試。
  - Browser Desktop／Mobile 視覺稽核：**NOT TESTED**；本次只驗證 HTML inline JavaScript 語法。
  - DL-07 整體：**IN PROGRESS**，不得標示 PASS／CLOSE。

### 後續接續範圍（不擴張）
1. 先處理上述 7 個舊測試案例的測試契約整理：4 個 stale workflow reference、3 個 stale source-text assertions；修改前先確認不會不必要觸發既有 Dashboard build／history commit。
2. 再規劃安全的正式 Workflow／歷史 Fetch 驗收；先設計可隔離資料目錄、mock 外部端點及禁止 commit/push 的執行方式。未建立安全隔離前，不觸發正式 `daily_data.yml`。
3. Browser Desktop／Mobile 視覺驗收另列，不可把 HTML JavaScript syntax PASS 當成視覺 PASS。
4. 不重做已 PASS 的 282 個離線測試、17F self-test、兩份歷史 Builder fixture；只有程式或 fixture 有新變更時才針對性回歸。
5. 不修改 `master`、P0 base、V8、Worker、DATA_REPORT 樣本或 Dashboard layout；不 merge／deploy。


## 2026-11-08｜DL-07 Workflow isolation guard strengthening

- 產品分支：`phase2-p0-ui-fixes`；最新驗證 commit：`9ada66a4841502b5e1e443fdad9652ef3cb32e3d`。
- 只修改 `.github/workflows/dl07-offline-validation.yml`（2 additions／1 deletion）；GitHub commit changed-files API 確認只有此檔案。Workflow blob 已回讀、產品分支 HEAD 與 CI head SHA 一致。
- Actions Run ID `42435737830`：SUCCESS。Workflow isolation、branch guards、deployment boundaries 檢查 PASS；282 個離線單元測試 PASS；DATA_REPORT／ratio／Treasury 語義契約 PASS；17F offline self-tests PASS；兩份歷史 fixture Builder、React injection／JS syntax、正式樣本及 dashboards 未變更檢查 PASS。
- 本次 isolation guard 檢查涵蓋 DL-06／DL-07 唯讀權限與禁止副作用、DL-06 mock/temp 測試模式、DL-07 workflow_dispatch／checkout SHA pin、Dashboard checkout SHA pin、生成檔 commit branch guard、Pages deploy gate，以及禁止 DL-07 呼叫正式 Fetch／daily_data 流程。
- 注意：這些是新增的現存 Workflow 靜態邊界檢查；不代表舊 `test_p0_workflow_isolation.py` 中引用缺失 Workflow 的 4 個測試已執行或通過。該 4 個舊測試仍 **NOT TESTED**。3 個 stale source-text assertions 與 3 個 live API probes 的排除狀態亦不變。
- DL-07 整體仍 **IN PROGRESS**：正式 Fetch／正式 `daily_data.yml` 執行及 Browser Desktop／Mobile 視覺稽核仍 **NOT TESTED**。本次未執行正式 Fetch、未寫入 DATA_REPORT、未部署 Pages、未 merge。
- 後續不再擴充此靜態檢查清單；除非有新的可重現缺陷，不重跑本次已 PASS 的 282 tests、17F self-test 或歷史 fixture builds。

## 2026-11-08｜DL-07 Fetch main isolated success-path test added（CI pending）

- 產品分支：`phase2-p0-ui-fixes`。
- 新增測試 `DataReportWriteSafetyTests.test_main_writes_valid_report_in_isolated_output_dir`，位於 `tests/test_fetch_data_borrowed_sources.py`。
- 測試直接呼叫 `fetch_data.main()`，但以 mock `build()` 阻斷所有外部資料來源，並將 `OUT_DIR` 指向 `TemporaryDirectory`；驗證報告路徑、內容、正式檔案驗證器、成功輸出及暫存目錄內容。
- 新增唯讀 Workflow：`.github/workflows/dl07-fetch-isolated-tests.yml`。只執行上述單一測試，checkout 釘選觸發 SHA，`contents: read`，並檢查 `data_reports/` 與 `dashboards/` 無變更；不呼叫正式 Fetch API、不執行 `daily_data.yml`、不 commit／push／deploy。
- 產品 commits：測試 `71bc3a85579f68dfd506bdc7f215e72c500fcec2`；Workflow `aa4cba71b838bcf878de0cf3de53cd00736cfc0c`。各 commit changed-files API 分別確認只修改測試檔及 Workflow 檔。
- 測試檔、Workflow 檔均已從產品分支回讀；`src/fetch_data.py` Blob SHA 維持 `6d8eb13004ab6273525b28b2d7396a7eaa24d61e`，沒有修改正式 Fetch 程式。
- **CI 狀態：PENDING／尚未取得可驗證的 Actions run ID 與結果。** 因此新增測試尚未標記 PASS；不得推定 Workflow 已成功執行。
- 本次未觸發正式 Fetch、未寫入正式 DATA_REPORT、未執行正式 `daily_data.yml`、未部署 Pages、未 merge。
- DL-07 仍 **IN PROGRESS**。本項待獨立 Workflow CI 成功後才能標記 PASS；正式 API Fetch 與 Browser Desktop／Mobile 視覺稽核仍 **NOT TESTED**。

## 2026-11-08｜DL-07 Fetch main 隔離成功路徑 CI 驗證完成

> 本節取代前一節的 CI pending 狀態；保留前一節作為當時紀錄。

- Actions Run ID：`42436125303`，[Run 詳細紀錄](https://github.com/grichtoyang/daily-premarket/actions/runs/42436125303)，Conclusion：**SUCCESS**。
- Workflow：`.github/workflows/dl07-fetch-isolated-tests.yml`；Run head SHA：`aa4cba71b838bcf878de0cf3de53cd00736cfc0c`。
- 產品分支 `phase2-p0-ui-fixes` 最新 HEAD 已回讀核對，與 Run head SHA 完全一致。
- Job `fetch-main-isolated` 全部步驟 SUCCESS：checkout triggering commit、Python／dependencies、指定測試、`data_reports/` 與 `dashboards/` 未變更檢查。
- Job log 明確顯示 `test_main_writes_valid_report_in_isolated_output_dir ... ok`、`Ran 1 test`、`OK`。
- **DL-07 Fetch main 隔離成功路徑：PASS**。測試執行真正的 `fetch_data.main()`，但以 mock `build()` 阻斷外部 API，並寫入 TemporaryDirectory；只證明隔離環境的成功寫檔路徑及報告驗證，不代表正式 API Fetch／正式 DATA_REPORT 產製通過。
- 本次未執行正式 Fetch、未寫入正式 DATA_REPORT、未執行正式 `daily_data.yml`、未部署 Pages、未 merge；`src/fetch_data.py` 未修改。
- DL-07 整體仍 **IN PROGRESS**。正式市場 API Fetch／正式 workflow 及 Browser Desktop／Mobile 視覺稽核仍 **NOT TESTED**；不得標示 DL-07 整體 PASS／CLOSE。
- 下一步只進入 DL-07 尚未完成的 Browser Desktop／Mobile 視覺驗收規劃／執行；不可將此隔離測試擴大解讀為正式資料流程驗收。


## 2026-11-08｜DL-07 Browser Artifact 取得完成；實際瀏覽器稽核 BLOCKED

- Dashboard workflow run：`42436118367`；Artifact ID：`13599433688`（`github-pages`）。已透過 GitHub Artifact 下載，並在工作目錄解壓縮，取得 `p0/test-fixtures/v9-pro-20261030-full-day.html`（約 353 KB）等 Pages 產物。
- Artifact 內容檢查確認 HTML 內含六個分頁定義：總覽、現貨、重要市場、期貨、選擇權、綜合分析。這只是靜態 HTML／程式內容確認，**不代表六個分頁已實際點擊或渲染驗收**。
- 執行環境雖有 Chromium 與 Playwright 套件，但 Playwright 導航本機 HTML／HTTP 頁面均回報 `net::ERR_BLOCKED_BY_ADMINISTRATOR`；Chromium headless CLI 亦未能在限定時間內完成頁面載入。未取得有效 DOM、畫面截圖或瀏覽器互動結果。
- 因此 Desktop 1440×1000、Mobile 390×844 六分頁的視覺、溢位、圖表可見性及 console error 驗收均為 **BLOCKED／NOT TESTED**；不可標記 PASS。不是產品頁面測試失敗，而是目前執行環境阻擋瀏覽器導航。
- 下一步需要使用者在可正常開啟該 HTML 的桌面及手機瀏覽器提供六分頁畫面（或提供可用的瀏覽器執行環境）。在取得實際渲染證據前，不修改產品程式、不擴大測試、不部署 Pages。
- DL-07 整體維持 **IN PROGRESS**；正式市場 API Fetch、正式 `daily_data.yml` 仍 **NOT TESTED**。本次未執行正式 Fetch、未寫入正式 DATA_REPORT、未部署 Pages、未 merge。
