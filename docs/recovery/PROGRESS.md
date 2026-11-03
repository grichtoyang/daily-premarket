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
