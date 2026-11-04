# RECOVERY — 最近工作與中斷恢復入口

> 本文件是新對話的第一個讀取點。
> 狀態快照：2026-11-01（Asia/Taipei）。
> 原則：先讀、再查證、後續作；未核對 GitHub 前禁止重做或 Push。

## 0. 新對話一鍵恢復指令

請先讀取同一分支上的三份文件：
1. `docs/recovery/MASTER_SPEC.md`
2. `docs/recovery/PROGRESS.md`
3. `docs/recovery/RECOVERY.md`

然後唯讀查證 GitHub：
- Repository：`grichtoyang/daily-premarket`
- 目前工作分支：`ops/recovery-handoff`
- P0 分支：`phase2-p0-data-quality`
- master：`master`

必須確認：
1. 所在 branch 與 HEAD SHA。
2. 三份交接文件是否存在、內容是否為最新。
3. P0 與 master 最新 HEAD 及 compare 結果。
4. 最近相關 GitHub Actions 狀態。
5. 工作目錄是否有未提交變更（若使用本機／IDE／OpenCode）。
6. 最後一個 Commit 實際修改了哪些檔案。

**在完成以上確認前，不得重複建立檔案、修改程式、Commit、Push 或 Merge。**

## 1. 最近工作內容

本次工作目標：建立對話中斷後可依 GitHub 交接文件快速恢復的機制。

本次已採取的隔離策略：
- 從 P0 凍結基準 Commit 建立獨立文件分支 `ops/recovery-handoff`。
- 分支起點：`031edc42791b396eb61fc32ae8c490b16d01b17c`。
- 不在 master 寫入。
- 不在 P0 原分支寫入。
- 不修改任何程式碼、workflow、Dashboard、資料或 V8 檔案。
- 本次只新增 `docs/recovery/` 下的交接文件。

## 2. 本次已寫入的交接文件

| 文件 | 用途 | 狀態 |
|---|---|---|
| `docs/recovery/MASTER_SPEC.md` | 專案總規範、不可變規則、文件權威順序 | 已建立 |
| `docs/recovery/PROGRESS.md` | Phase 進度、P0 待辦、P1 啟動條件 | 已建立 |
| `docs/recovery/RECOVERY.md` | 最近工作、Git 基準、恢復步驟、下一個明確任務 | 本文件 |

文件分支：
`ops/recovery-handoff`

已知建立文件的 Commit：
- MASTER_SPEC：`19162301dec9846d5642efb29555da7444d3dd10`
- PROGRESS：`ddad407b0151f8cd99ffbfe865c3713a65ff9427`
- RECOVERY：本文件建立後的 Commit SHA，須再查 GitHub branch HEAD 確認並補登。

## 3. 最近成功完成的工作（P0 原工作）

P0 凍結基準：
`031edc42791b396eb61fc32ae8c490b16d01b17c`

既有成功 Actions：
- Integration：`41281205671` — Success。
- Build／Deploy：`41281205639` — Success。

P0 Dashboard：
`https://grichtoyang.github.io/daily-premarket/p0/v9-pro-latest.html`

上述是既有 P0 驗收紀錄；新對話仍應確認 Actions 頁面與 HEAD 是否相符。Actions 成功不代表所有瀏覽器視覺與 CDN 測試通過。

## 4. 目前未完成／未驗證工作

### P0 Closing A — Dashboard 視覺缺陷

使用者提供畫面並指出：
1. 融資融券等圖表中數字與圖示略有重疊。
2. Call Wall／Put Wall／Gamma／Flip／MaxPain 關鍵價位圖的數字與標籤重疊。
3. 選擇權法人交易圖表／圖示異常。
4. 三劇本路徑圖表未顯示（情境文字有顯示）。
5. 相關性熱圖因日期對齊樣本不足而未計算，畫面沒有有效圖表。

修正原則：
- 先定位根因，再提出最小修改。
- 不更動 Dashboard 六個分頁及規格。
- 不使用假資料填補缺圖。
- 相關性樣本不足時，不強制繪製假熱圖；應保留誠實狀態並改善空狀態說明。
- 修改後要驗證資料正確性、圖表渲染、手機／桌面布局及既有回歸測試。
- P0 核心資料品質引擎維持功能凍結。

### P0 Closing B — 第三方 CDN 字型

狀態：NOT TESTED。
需以實際瀏覽器驗證：
- Google Fonts CSS 是否成功載入。
- Noto Sans TC 字型檔是否成功載入並實際套用。
- JetBrains Mono 字型檔是否成功載入並實際套用。
- CDN 阻擋／離線時 fallback 是否正常。
不可用 HTML 靜態引用檢查或 GitHub Actions 成功取代瀏覽器驗證。

### P0 Closing C — P0／master 整合評估

狀態：BLOCKED（尚未完成唯讀差異審查；未授權 Merge）。
已知：
- master HEAD：`d01c315a5a33d21cfd7514040700a57a66637430`
- P0 HEAD：`031edc42791b396eb61fc32ae8c490b16d01b17c`
- 先前 compare 結果：P0 ahead 265、behind 3。
- master 獨有三個 Commit；其中最新 `d01c315` 是保留 P0 Dashboard 獨立 Pages 路徑。
- 整合前須重新 compare，核對完整三個 Commit、檔案差異、workflow、DATA_REPORT、Dashboard 部署及 V8 保護。
- 只能先提出方案，不可自行 Merge、Rebase、Force Push 或覆蓋 master。

## 5. P1 狀態與邊界

- P1 尚未啟動。
- 不得只依舊對話摘要猜測 P1 工作內容。
- 先完整讀取專案架構及規格，特別是新版 Phase 2 規劃是否存在、舊 `docs/PHASE2.md` 是否過時。
- 整理 P1 工作清單、順序、依賴、資料來源、輸出及驗收條件。
- 經使用者明確確認後才開始 P1 實作。

## 6. 下一個明確執行指令

**下一步先不要進入 P1，也不要 Merge。**

請在 `ops/recovery-handoff` 分支上先完成本次交接文件遠端驗證：
1. 查詢 branch HEAD，確認三份文件已存在。
2. 讀回三份文件，確認內容完整。
3. 將 RECOVERY 文件建立 Commit SHA 補入本文件（若已建立）。
4. 確認 master 與 `phase2-p0-data-quality` HEAD 未被本次工作改動。

之後依序：
1. P0 Dashboard 五項問題的唯讀根因定位與修正方案。
2. CDN 字型實際瀏覽器測試。
3. P0／master 唯讀整合差異審查。
4. P0 最終封存。
5. Phase 2 規格盤點及 P1 工作範圍確認。

每一項都必須先呈現發現與計畫，再依使用者授權執行。

## 7. 本次執行狀態

| 項目 | 狀態 |
|---|---|
| 建立隔離文件分支 | PASS（GitHub 回傳已建立） |
| 新增 MASTER_SPEC.md | PASS（GitHub 回傳 Commit SHA） |
| 新增 PROGRESS.md | PASS（GitHub 回傳 Commit SHA） |
| 新增 RECOVERY.md | IN PROGRESS（建立後待讀回驗證） |
| 修改程式／Dashboard／Workflow | NOT DONE（本次刻意未修改） |
| Push 至 master 或 P0 | NOT DONE（本次未操作） |
| Merge P0／master | NOT DONE（未授權） |
| CDN 瀏覽器測試 | NOT TESTED |
| P0 UI 缺陷修復 | NOT STARTED |
| P1 實作 | NOT STARTED |

## 8. 交接更新鐵律

每次完成一段工作，在結束對話或切換任務前：
1. 更新 `PROGRESS.md` 的階段狀態與證據。
2. 更新 `RECOVERY.md` 的最後完成步驟、修改檔案、Commit、Push 狀態、測試 PASS／FAIL／BLOCKED／NOT TESTED。
3. 記錄下一個唯一、明確、可執行的工作指令。
4. 將文件 Commit／Push 到當前獲准的工作分支。
5. 重新查詢 GitHub branch HEAD 並讀回文件，確認遠端保存成功。
6. 不得只因為在聊天中寫了摘要，就宣稱交接點已保存。


## 9. 2026-11-01 最新進度追加：P0 視覺驗收與五個待查區塊

### 9.1 Git 狀態（本次唯讀查證）
- Recovery 文件分支：`ops/recovery-handoff`，本次查證 HEAD：`d07f384157b9ca919019a903b1b373d9ae45fb84`。
- P0 分支：`phase2-p0-data-quality`，本次查證 HEAD：`49fd5b0dfd6a9c1b89fc49bb6e4d81ae5fdc4d33`。
- P0 HEAD 的前一個程式修正 Commit：`80fb89e1a4959f242964c3f6d0891d2fb0677a46`；其後 `49fd5b0` 為每日 Dashboard 產物更新。
- 本次只更新 Recovery 文件分支；未修改 P0、master、程式、Workflow、Dashboard 或 V8。
- 本次未執行 Merge／Rebase／Force Push。

### 9.2 P0 視覺驗收狀態更新
使用者於 2026-11-01 明確確認：目前已逐頁檢查 Dashboard，所有先前指出的圖示／文字重疊均已消失。
- 先前重疊問題：PASS（使用者實際畫面驗收）。
- Build／Deploy：PASS（既有成功 Workflow Run 41297437934）。
- Integration：PASS（既有成功 Workflow Run 41297437923）。
- 17F offline self-tests：PASS（既有 Workflow log 記錄）。
- 原始 11 張基準截圖逐張像素／內容比對：NOT TESTED；但不再作為目前重疊問題的阻塞條件，因使用者已確認現行畫面無重疊。

### 9.3 使用者最新提供的五個異常區塊（新待查項目）
注意：以下是依 2026-11-01 使用者提供的五張截圖建立的初步問題紀錄，不是已確認根因。不得僅憑截圖直接修改程式。

| ID | 區塊 | 截圖觀察 | 初步調查方向 | 狀態 |
|---|---|---|---|---|
| DATA-UI-01 | 借券／券 | 上方變化值與下方餘額可能存在單位／倍率不一致；畫面同時出現 4,651,514 張、+465.2 萬張等數值 | 核對來源欄位原始單位、張／股換算、變化值與餘額是否使用同一口徑、前端 formatter | BLOCKED（尚未讀取該日 DATA_REPORT／JSON／Builder 對應欄位） |
| DATA-UI-02 | 選擇權法人交易 | 圖表區顯示外資／投信／自營商／合計均為 0 日，但明細列仍有日盤與夜盤口數 | 核對「交易日數」欄位定義、資料來源 schema、日夜盤明細與圖表 series mapping；確認是否把天數誤當口數或資料欄位缺漏 | BLOCKED（尚未讀取原始輸入與 JSON） |
| DATA-UI-03 | IV／GEX 深度 | PCR 0.61、Call/Put Vol% 有值；GEX、IV Rank、Term 顯示 unavailable | 分別追查來源可用性、計算引擎是否實作、必要輸入是否缺少；核對 PCR/Vol% 圖表單位與標籤 | BLOCKED（尚未讀取原始輸入與計算程式） |
| DATA-UI-04 | 三劇本路徑 | Bias 20／偏空及三個價格情境有顯示；機率標示未驗證，主圖區空白 | 區分「刻意不顯示未校準機率」與「路徑主圖未渲染」；檢查 chart payload、canvas／SVG 初始化及空資料分支 | BLOCKED（尚未讀取 JSON 與前端元件） |
| DATA-UI-05 | 相關性熱圖 | 顯示歷史日期對齊樣本不足，熱圖未計算 | 核對歷史序列是否取得、日期索引／交易日對齊、有效樣本數門檻、缺值剔除及 Builder 輸出 | BLOCKED（畫面提示支持樣本不足假說，但尚未查明上游原因） |

### 9.4 五區塊根因調查順序（只讀定位，不先改碼）
1. 固定 P0 分支與本次 Dashboard 對應的 T0／產物版本；確認截圖對應日期與實際 JSON。
2. 讀取同一 T0 的 DATA_REPORT、V9 Pro JSON、Dashboard HTML，建立欄位追蹤鏈。
3. 逐區塊追蹤：來源原始值 → DATA_REPORT → Builder 計算／正規化 → JSON 欄位 → 前端元件／formatter。
4. 對每項根因分類：SOURCE_MISSING、SCHEMA_MISMATCH、CALCULATION_NOT_IMPLEMENTED、DATE_ALIGNMENT、FRONTEND_MAPPING／RENDERING、UNIT_CONVERSION。
5. 先提交根因與最小修正方案，經使用者確認後才改動；不使用假資料補圖，不把 unavailable 強制轉成 0。
6. 修正後執行對應單元測試、整合 Workflow、HTML／JS 語法檢查及桌面／手機視覺驗收。

### 9.5 下一個唯一工作
先完成五個區塊的唯讀資料追蹤與根因分類；本輪不啟動 P1、不修改 P0 程式、不合併分支。五項根因及修正範圍釐清後，再更新本文件並由使用者決定是否進入修正。


## 10. 2026-11-01 五區塊唯讀根因查核（初輪）

查核對象：P0 branch `phase2-p0-data-quality`，T0 `2026-10-30`。
- `data_reports/DATA_REPORT_20261030.md` SHA：`b25266b606408615e247cdeecd7641fc52fce26b`。
- `dashboards/data-20261030.json` SHA：`9f031928b02f9b652e9ff31f0397224db2086cb4`。
- `scripts/v9_pro_builder.py` SHA：`011224e54a32ddbf52db6fc1347d2c865fa010eb`。
- `templates/v9-pro-react-template.html` SHA：`018fcff6bd49f7f796904fed47d96784aec8fe26`。

### 已確認的根因／狀態

1. **DATA-UI-01 借券／券：部分顯示是正確換算，部分欄位確實漏傳。**
   - DATA_REPORT 借券餘額為 4,651,514 張；JSON `margin.sbl=4651514`。圖表將其除以 10,000，顯示約 465.2 萬張；下方顯示 4,651,514 張，兩者數值等價，並非單位錯誤。
   - DATA_REPORT 同時有借券賣出餘額 36,178 張、增減 -1,273 張，但 JSON `margin` 僅有 `sbl`、`borrow`，缺少 `borrowedSell`。HTML 圖表讀取 `l.borrowedSell`，故顯示 unavailable／零值位置。這是 Builder parse／JSON schema 漏傳，不是上游無資料。
   - 融券 233,537 張除以 10,000 約 23.4 萬張，換算正確。
   - 狀態：單位換算 PASS；借券賣出欄位傳遞 FAIL（已定位，未修正）。

2. **DATA-UI-02 選擇權法人交易：資料存在，圖表轉數字失敗。**
   - JSON `options.instOpt` 已包含日盤淨額，例如 `+6,624`、`-4,937`、`+1,342`、`+3,029`，且夜盤欄位也有數值。
   - HTML 圖表使用 `Number(x[3]||0)`；來源字串含千分位逗號（如 `+6,624`），JavaScript `Number("+6,624")` 會得到 NaN，圖表元件再將無效值呈現為 0。因此畫面出現 0 日，但下方明細仍正常顯示。
   - 根因：前端數值正規化漏掉逗號處理；不是資料缺失。最小修正應先移除千分位逗號再轉數字，並保留正負號。
   - 狀態：FAIL（根因已定位，未修正）。

3. **DATA-UI-03 IV／GEX 深度：缺值主要來自 DATA_REPORT／Builder 未提供欄位。**
   - JSON `options` 目前只有 call/put Vol、OI、PCR、牆位、法人交易及前十大等欄位；沒有 `gex`、IV Rank、Risk Reversal、各期限 IV。
   - Builder 明確將 GEX 缺值時停用因子，並註記 IV Rank／Risk Reversal、Term 結構「DATA_REPORT 未提供」。
   - 因此 GEX、IV Rank、Term 顯示 unavailable 是誠實的缺值狀態，不是前端漏畫；PCR 0.61 與 Call/Put Vol% 可用是因為對應欄位存在。
   - 狀態：缺值呈現 PASS；資料源／計算能力是否納入後續需求 NOT TESTED（不在本次自行擴充範圍）。

4. **DATA-UI-04 三劇本路徑：目前空白區是程式明確設計的未校準機率提示，不是價格資料缺漏。**
   - React template 的「三劇本路徑」chart slot 明確渲染文字「情境機率未經回測校準，暫不顯示百分比。」；三個價格情境另於下方 table 呈現。
   - JSON `analysis.cards.三劇本` 亦明確註記尚未建立經回測校準的機率模型，不提供機率。
   - 因此空白主圖區是目前元件設計結果；是否要將其改成非機率型路徑示意圖屬需求／UX 決策，不應當成數據缺失直接補圖。
   - 狀態：防止輸出未驗證機率 PASS；圖表呈現是否符合使用者預期 BLOCKED（需先確認要不要保留提示或改成無機率路徑圖）。

5. **DATA-UI-05 相關性熱圖：根因是 Builder 目前硬編碼輸出空矩陣，且歷史樣本量極少。**
   - JSON `analysis.correlation` 為空 labels、空 matrix，描述「歷史日期對齊樣本不足，相關性未計算」。
   - JSON `analysis.db_status` 顯示 DB 共 3 筆、filled 2；歷史有效樣本不足。
   - Builder 目前直接輸出 `correlation: {'labels': [], 'matrix': [], 'desc': ...}`，沒有執行相關係數計算流程。因此不只是資料缺失，也包含相關性計算尚未實作／未接線。
   - 狀態：不捏造相關係數的空狀態 PASS；相關性計算功能 NOT IMPLEMENTED（後續需先定義資料來源、最小樣本數與計算方法）。

### 本輪結論
- 五項中，借券餘額與融券的單位換算正確；借券賣出欄位確定在 Builder→JSON 傳遞時遺漏。
- 選擇權法人圖表的 0 日是前端字串轉數字錯誤。
- GEX／IV／Term 是上游欄位未提供，現有 unavailable 顯示符合誠實資料原則。
- 三劇本空白是刻意不顯示未校準機率的 UI 設計；如要圖形化，需先確認不呈現機率的視覺方案。
- 相關性矩陣未計算：DB 僅 3 筆／有效 filled 2，且 Builder 目前硬編碼空矩陣，並非僅調整日期即可解決。

本輪僅唯讀查核；未修改程式、JSON、HTML、DATA_REPORT、P0 分支或 master。以上根因是單模型程式碼／資料追蹤審查，非獨立多模型稽核。

### 下一個工作建議
先處理兩個可明確修正的資料鏈缺陷：
1. 將 DATA_REPORT 的借券賣出餘額／增減欄位完整傳入 JSON，前端使用正確欄位顯示；不得把借券餘額存量誤標為當日增減。
2. 選擇權法人圖表解析帶逗號的數字字串，並加單元測試覆蓋正數、負數、千分位、缺值。

其餘三項先維持誠實缺值／未校準提示，待另行確認 GEX/IV 資料源、三劇本無機率圖示需求、相關性資料與樣本門檻後再規劃；不擴大本輪修正範圍。


## 11. 2026-11-01 DATA-UI-01／02 修正實作與恢復入口

> 本節為最新狀態，優先於本文件較早章節中「尚未開始修正」及「下一步唯讀根因調查」的描述。

### 11.1 最新分支與 Commit
- Repository：`grichtoyang/daily-premarket`
- 修正分支：`phase2-p0-ui-fixes`
- 修正分支 HEAD：`eb861a470ff5a90faa73ae4097c3c15d227f3d10`
- 基底分支：`phase2-p0-data-quality`
- 基底／P0 HEAD：`49fd5b0dfd6a9c1b89fc49bb6e4d81ae5fdc4d33`
- Compare：UI fixes ahead 14、behind 0；merge base 正是 P0 HEAD。
- master HEAD：`0ac95b2521e7bdcb357431cc7725da4e2c26e602`。
- Recovery 文件分支更新前 HEAD：`7e5bd237ab229a5108adb13b5200707136b4bed4`。
- P0 原分支與 master 均未修改；未 Merge／Rebase／Force Push；V8 未修改。

### 11.2 變更檔案（僅五個）
1. `.github/workflows/test-v9-ui-fixes.yml`：新增 UI 修正分支專用回歸流程，checkout 使用 `github.ref`；只執行測試及 JSON 驗證，不部署、不推送產物。
2. `scripts/v9_pro_builder.py`：解析借券賣出餘額、增減與資料範圍，將三欄傳遞至 Dashboard JSON。
3. `templates/v9-pro-react-template.html`：借券區塊顯示餘額與增減範圍；選擇權法人圖表改用 `v9ProOptionNetNumber` 解析含千分位的正負數，無效值不繪成有效 0。
4. `tests/test_builder_option_tables.py`：新增借券欄位與 scope 測試。
5. `tests/test_react_template_static.py`：新增正／負／千分位／缺值解析測試、React 內部事件函式保護及借券 UI 欄位測試。

重要修正細節：
- React template 原有 `qn(e,n)` 是 React 內部事件註冊函式，不是可任意覆寫的名稱。實作過程曾由 CI 抓出重複宣告及內部函式被誤改；最終已恢復原始 `function qn(e,n){kr(e,n),kr(e+"Capture",n)}`，並以唯一名稱 `v9ProOptionNetNumber` 作為新數字解析函式。
- Builder 遵守 `dashboards/` 唯一輸出路徑；專用 Workflow 的 JSON 驗證也使用 `dashboards/v9-ui-fixes-data.json`。

### 11.3 最新驗收證據
UI 專用 GitHub Actions：
- Run ID：`41301487409`
- Workflow：`V9 UI Fixes Regression`
- Branch：`phase2-p0-ui-fixes`
- Head SHA：`eb861a470ff5a90faa73ae4097c3c15d227f3d10`
- Conclusion：Success

逐項結果：
- V9 Builder offline self-tests：PASS。
- React template regression：10 tests，PASS；包含 inline JavaScript syntax、數字解析、缺值過濾、React 內部函式保護。
- DATA_REPORT parser regression：3 tests，PASS；包含借券餘額、借券賣出增減及範圍。
- Builder JSON 驗證：PASS；借券賣出餘額 36,178 張、增減 -1,273 張，增減範圍明確標示「上櫃（上市 TWT93U 未取得）」。
- 選擇權法人圖表解析：`+6,624 → 6624`、`-4,937 → -4937`、缺值／非數字 → null 並排除於圖表 series。
- 曾有早期 CI 失敗，分別是 helper 名稱與 React 內部函式衝突，以及測試輸出路徑不符合 Builder Output Path Rule；已修正。最終 Run `41301487409` 全步驟 Success。

### 11.4 未完成／不得誤報
- 桌面／手機瀏覽器實際視覺驗收：NOT TESTED。
- 修正分支未部署 GitHub Pages：NOT DONE。
- 未合併回 P0／master：NOT DONE。
- 本機／OpenCode 工作目錄 dirty status：NOT TESTED；本次僅查證 GitHub 遠端狀態。
- DATA-UI-03／04／05 未修改，沿用既有誠實缺值／未校準設計。
- 本次 Auditor 為單模型自我審查，沒有獨立模型或 Agent 審核。

### 11.5 下一步唯一指令
先在 `phase2-p0-ui-fixes` 建立 T0 2026-10-30 的不部署預覽 HTML（從已驗證 DATA_REPORT 建立 JSON，再注入 React template），只供檢查 DATA-UI-01／02；不得推送 Pages、不得改 P0／master／V8。預覽生成後再由使用者檢查桌面及手機顯示，未完成視覺驗收前不得宣稱 Dashboard UI 最終驗收 PASS。


## 12. 2026-11-01 非部署 HTML 預覽已產生

> 本節覆蓋第 11.5 節「下一步產生預覽」的待辦狀態。

- UI fixes branch 最新 HEAD：`2ee248dd21fa5ad9545c7c70d9e427f793721d7c`。
- Workflow Run：`41301631710`（`V9 UI Fixes Regression`），Conclusion：Success。
- 預覽生成步驟：PASS；使用 T0 2026-10-30 DATA_REPORT 產生 Builder JSON，再注入 React template。
- Artifact：`V9-UI-Fixes-Preview-20261030`。
- 檔案：`v9-pro-ui-fixes-preview-20261030.html`，88,133 bytes。
- Artifact ID：`13081122728`。
- Run URL：`https://github.com/grichtoyang/daily-premarket/actions/runs/41301631710`。
- Artifact 到期時間：2027-01-30。
- 本次只有上傳 GitHub Actions Artifact；未部署 Pages、未推送 Dashboard 產物到 P0／master、未 Merge。

### 最新狀態
- DATA-UI-01／02 程式與 JSON 回歸：PASS。
- 非部署 HTML 預覽產生及上傳：PASS。
- 桌面／手機實際瀏覽器視覺驗收：NOT TESTED，等待使用者檢查 Artifact。
- P0 原分支 HEAD：`49fd5b0dfd6a9c1b89fc49bb6e4d81ae5fdc4d33`（未變）。
- master HEAD：`0ac95b2521e7bdcb357431cc7725da4e2c26e602`（未變）。
- Recovery 文件分支更新前 HEAD：`4479bbafd893adb9bf37257a3d2e4ccb8c8ed960`。
- 本機／OpenCode 工作目錄狀態仍為 NOT TESTED。

### 下一個唯一工作
請使用者開啟上述 GitHub Actions Run，下載 Artifact `V9-UI-Fixes-Preview-20261030`，檢查借券／券區塊及選擇權法人交易區塊的數字、單位、標籤與圖表；桌面與手機各檢查一次。回報結果後再處理必要視覺調整。不要部署、不要 Merge、不要修改 P0／master／V8。


## 13. 2026-11-01 DATA-UI-01／02 手機版視覺驗收完成

> 本節為最新驗收狀態，覆蓋前文「等待使用者檢查 Artifact」的待辦敘述。

### 最新預覽版本
- Repository：`grichtoyang/daily-premarket`
- 修正分支：`phase2-p0-ui-fixes`
- HEAD：`d0f644e661fc43596bc4886ae0fd92977891db17`
- Workflow Run：`41303525878`，Success。
- Artifact：`V9-UI-Fixes-Preview-20261030`，Artifact ID：`13082301670`，88,306 bytes。
- 預覽 Run：`https://github.com/grichtoyang/daily-premarket/actions/runs/41303525878`。

### 手機實際畫面驗收
1. DATA-UI-01 借券／券：借券餘額、借券賣出、借券賣出增減、資料範圍及融券均正確顯示；手機版改為單欄排列，`-1,273 張` 與資料範圍標籤完整同列，沒有截圖可見的折行或重疊。PASS。
2. DATA-UI-02 選擇權法人交易：圖表呈現日盤與夜盤各四筆資料；日盤為外資 +6,624、投信 -4,937、自營商 +1,342、合計 +3,029；夜盤為外資 -94、投信 0、自營商 -1,391、合計 -1,485。明細與圖表數值一致，手機畫面無明顯裁切或重疊。PASS。

### 總驗收狀態
- DATA-UI-01 手機視覺：PASS。
- DATA-UI-02 手機視覺：PASS。
- DATA-UI-01／02 程式與 CI：PASS（Run `41303525878`）。
- 桌面視覺驗收：NOT TESTED。
- DATA-UI-03／04／05：未修改，非本輪驗收範圍。
- 尚未部署、尚未 Merge／Cherry-pick；P0 原分支、master、V8 未修改。
- 本機／OpenCode 工作目錄狀態：NOT TESTED。
- 本輪 Auditor 為單模型自我審查，非獨立多模型審核。

### 下一步
桌面版視覺驗收尚未提供截圖；若使用者希望完整跨裝置驗收，需在桌面瀏覽器開啟同一 Artifact 並檢查 DATA-UI-01／02。未取得桌面證據前，不得宣稱桌面視覺 PASS。部署或合併仍須使用者另行明確授權。


## 14. 2026-11-01 DATA-UI-05 修正與 CI 驗收

> 本節為最新工作狀態，優先於前文將 DATA-UI-05 標示為未實作／待唯讀調查的舊紀錄。此輪只處理 DATA-UI-05；DATA-UI-03／04、V8、Master、部署均未觸碰。

### 14.1 分支與變更
- Repository：`grichtoyang/daily-premarket`
- 工作分支：`phase2-p0-ui-fixes`
- 最新 Commit：`4d2ccc4769f1df819601d70742312e75e388829d`
- 基準 Commit：`d0f644e661fc43596bc4886ae0fd92977891db17`
- 相對基準新增 5 個 Commit；Compare 顯示僅修改兩個檔案：
  1. `scripts/v9_pro_builder.py`
  2. `templates/v9-pro-react-template.html`
- 未修改 DATA-UI-03／04、V8、Master、部署設定；未 Merge／Cherry-pick。

### 14.2 DATA-UI-05 實作摘要
- 歷史資料新增 `correlation_eligible` 品質資格欄位；缺失值以 NULL 儲存，不再以 0 假造。
- 使用 T0 日期正規化；同日期已存在資料則跳過，不覆寫既有紀錄。
- 相關性採 8 個有效欄位，僅讀取明確標記 eligible 的完整樣本；排除非有限值，依日期排序後計算 Pearson 相關係數。
- 最低樣本數預設 5；樣本不足或有效欄位不足時回傳空矩陣與明確說明。
- 前端只有在 matrix 與 labels 均有效時才建立熱圖；否則顯示資料不足描述，不再渲染空白格與色階。
- 舊歷史資料未全面重建；既有不符合資格的舊列不會被納入本次計算。

### 14.3 CI 證據
- Workflow：`V9 UI Fixes Regression`
- Run ID：`41307754019`
- Run URL：`https://github.com/grichtoyang/daily-premarket/actions/runs/41307754019`
- Head SHA：`4d2ccc4769f1df819601d70742312e75e388829d`
- Conclusion：Success；regression job 全部步驟成功。
- 通過項目：V9 Builder offline self-tests、React template regression、DATA_REPORT parser regression、Dashboard JSON build／借券欄位檢查、非部署 HTML preview 產生及 Artifact 上傳。

### 14.4 驗收狀態與限制
| 項目 | 狀態 |
|---|---|
| 缺值 NULL／eligible 資料篩選 | PASS（CI 自我測試） |
| T0 日期正規化／重複日期跳過 | PASS（程式與既有測試查核） |
| 最低樣本數與 Pearson 矩陣 | PASS（CI 自我測試） |
| 無有效矩陣時隱藏熱圖 | PASS（React regression） |
| Android／桌面實際視覺 | NOT TESTED |
| 正式 Pages 部署 | NOT DONE |
| Merge／Cherry-pick | NOT DONE |
| Recovery 工作目錄 dirty status | NOT TESTED |

### 14.5 下一步唯一指令
DATA-UI-05 程式與 CI 驗收已完成。若要繼續，先由使用者檢查非部署 HTML Artifact 的相關性區塊（有效樣本時的熱圖，以及樣本不足時的空狀態）；取得實際畫面驗收後，再決定是否結案及是否授權後續整合。不得自行部署或 Merge。


## 15. 2026-11-01 DATA-UI-05 手機畫面驗收與重複提示修正

> 本節更新第 14 節的最新狀態；只記錄 DATA-UI-05，不代表已部署或整合。

### 最新修正
- UI branch：`phase2-p0-ui-fixes`
- 修正 Commit：`8a74e30144571413cfd2ea42bfb646500cf02214`
- 變更檔案：`templates/v9-pro-react-template.html`。
- 修正前使用者截圖顯示資料不足說明重複兩次；已移除熱圖區塊下方重複的描述，只保留熱圖區內的狀態提示。
- 新版模板已從 GitHub 遠端讀回，確認重複描述片段已移除，條件式欄位標籤仍保留。

### CI 與實際畫面證據
- Workflow Run `41308547210`：Conclusion Success。
- Regression job 全部步驟成功，包括 Builder offline self-tests、React template regression、DATA_REPORT parser regression、JSON build、非部署 HTML preview 產生及 Artifact 上傳。
- Run URL：`https://github.com/grichtoyang/daily-premarket/actions/runs/41308547210`。
- Artifact：`V9-UI-Fixes-Preview-20261030`，Artifact ID `13084755255`，未過期。
- 使用者提供新版手機截圖：`0/5` 樣本提示只出現一次；未顯示空白矩陣／色階；原有分析、判斷、操作說明卡片正常呈現。手機畫面驗收 PASS。

### 最新驗收狀態
| 項目 | 狀態 |
|---|---|
| DATA-UI-05 樣本不足狀態（手機） | PASS |
| 重複提示移除 | PASS |
| 無效矩陣不顯示熱圖 | PASS |
| Builder／React／DATA_REPORT CI | PASS |
| 有效樣本達 5 筆時的實際熱圖視覺 | NOT TESTED（目前截圖為 0/5） |
| 桌面視覺 | NOT TESTED |
| 正式部署／Merge／Cherry-pick | NOT DONE |
| DATA-UI-03／04、V8、Master | 本輪未修改 |

### 下一步
DATA-UI-05 樣本不足狀態的手機視覺驗收已完成。有效樣本矩陣與桌面畫面仍未驗證；不得將其標示為 PASS。部署或合併須另行取得使用者明確授權。


## 16. 2026-11-01 DATA-UI-05 手機有效樣本熱圖驗收

### 修正內容
- UI branch：`phase2-p0-ui-fixes`
- Commit：`98df6c782346b01dc6f66d3b4692786c32e133e1`
- 僅修改 `templates/v9-pro-react-template.html` 的 `t2` 熱圖繪製函式。
- 手機版取消矩陣上方擠壓的欄名，改由左側列標籤辨識欄位；依畫布寬高動態縮放儲存格，並預留右側色階空間。
- 相關性數值、矩陣資料及色彩映射邏輯未更動。

### 測試證據
- GitHub Actions Run `41309915998`：Success；Builder offline self-tests、React template regression、DATA_REPORT parser regression、JSON build、非部署預覽及隔離有效矩陣 Fixture 均成功。
- Run URL：`https://github.com/grichtoyang/daily-premarket/actions/runs/41309915998`。
- 隔離 Artifact：`V9-Correlation-Heatmap-Test-Fixture`，Artifact ID `13084587818`；只含合成測試資料，標示不得部署。
- 使用者提供最新版 Android 手機截圖：8×8 矩陣完整顯示；列標籤清楚、數值可讀、色階與 1.0／-1.0 刻度可見；未見先前欄名重疊問題。手機有效樣本熱圖視覺 PASS。

### 最新狀態
| 項目 | 狀態 |
|---|---|
| 樣本不足 0/5 手機狀態 | PASS |
| 有效樣本 8×8 熱圖手機渲染（合成資料） | PASS |
| 手機矩陣標籤／數值／色階排版 | PASS |
| CI 回歸測試與隔離 Fixture 產生 | PASS |
| 真實歷史資料達標時的矩陣內容與統計正確性 | NOT TESTED（合成資料僅驗證 UI 渲染） |
| 桌面視覺 | NOT TESTED |
| 正式部署／Merge／Cherry-pick | NOT DONE |
| DATA-UI-03／04、V8、Master | 本輪未修改 |

### 下一步
DATA-UI-05 的兩種手機 UI 狀態（樣本不足與合成有效矩陣）已驗收。若要進一步驗證真實歷史資料相關係數，須使用正式資料自然累積的有效樣本；不得將合成 Fixture 寫入正式歷史資料。桌面視覺仍未測試。部署或合併須另行取得使用者明確授權。


## 17. 2026-11-01 DATA-UI-05 真實歷史資料驗證盤點

- 檢查 UI branch `phase2-p0-ui-fixes` 的 `dashboards/data-latest.json`，SHA `9f031928b02f9b652e9ff31f0397224db2086cb4`。
- 資料快照 T0 `2026-10-30`，產出時間 `2026-11-01 12:32:04`（Asia/Taipei）。
- `meta.db_mode=db`、`meta.db_rows=3`；相關性欄位為 `labels=[]`、`matrix=[]`，描述為「歷史日期對齊樣本不足，相關性未計算」。
- DATA-UI-05 最低門檻為 5 筆有效完整樣本；目前 DB 總列數只有 3，且不能據此推定 3 筆均為有效樣本。真實歷史相關性數值驗證目前 BLOCKED，原因是有效樣本不足，需待正式歷史資料自然累積，不得注入合成資料。
- 手機樣本不足 UI 與合成 8×8 熱圖 UI 已 PASS；本輪未修改程式、正式資料庫或 Dashboard 資料。
- 桌面瀏覽器實際視覺仍 NOT TESTED；目前未執行正式部署、合併或 cherry-pick。


## 18. 2026-11-01 DATA-UI-05 寬版 Dashboard 熱圖視覺驗收

- 使用者提供寬版 Dashboard 截圖（911×1536）。畫面採雙欄配置，相關性熱圖位於左下區塊。
- 觀察結果：8×8 矩陣完整顯示；列標籤與數值無明顯重疊；正負相關色彩可辨；右側色階及上下限刻度可見；熱圖卡片未破壞雙欄排列。
- 寬版／雙欄畫面視覺驗收 PASS。因截圖寬度為 911px，不將此結果擴大宣稱為大型桌面螢幕（例如 1440px）驗收；大型桌面視覺 NOT TESTED。
- 本次僅依使用者截圖驗收，未修改程式、正式資料或部署狀態。


## 19. 2026-11-01 UI 修正分支與 P0 基底差異審查

- Repository：`grichtoyang/daily-premarket`。
- Base：`phase2-p0-data-quality`，HEAD `49fd5b0dfd6a9c1b89fc49bb6e4d81ae5fdc4d33`。
- Head：`phase2-p0-ui-fixes`，HEAD `98df6c782346b01dc6f66d3b4692786c32e133e1`。
- Compare：ahead 31、behind 0；merge base 即 P0 HEAD。
- 僅 5 個檔案變更：`.github/workflows/test-v9-ui-fixes.yml`、`scripts/v9_pro_builder.py`、`templates/v9-pro-react-template.html`、`tests/test_builder_option_tables.py`、`tests/test_react_template_static.py`。
- 變更範圍涵蓋先前 DATA-UI-01／02（借券欄位、選擇權法人數字解析）及 DATA-UI-05（歷史相關性計算與熱圖呈現），沒有發現額外檔案變更。
- Workflow 已讀取完整內容：僅對 `phase2-p0-ui-fixes` 觸發；`contents: read`；執行離線測試、JSON 驗證、非部署 HTML 預覽及 Artifact 上傳；未見 Pages 部署、正式產物推送或合併步驟。
- P0 branch HEAD 維持 `49fd5b0dfd6a9c1b89fc49bb6e4d81ae5fdc4d33`；master HEAD 維持 `0ac95b2521e7bdcb357431cc7725da4e2c26e602`；V8 備份分支未修改（本次未比較其內容）。
- 差異審查結果 PASS（檔案範圍及 Workflow 靜態審查）；未執行 Merge／Rebase／Cherry-pick／Deploy。
- DATA-UI-05 真實歷史相關性仍 BLOCKED（有效樣本不足）；大尺寸桌面 1440px 視覺 NOT TESTED；本機／OpenCode 工作目錄狀態 NOT TESTED。
- Auditor 為單模型自我審查，非獨立多模型審核。


## 20. 2026-11-01 DATA-UI-04 三劇本路徑修正與手機視覺驗收

### 修正內容
- UI branch：`phase2-p0-ui-fixes`。
- 修正 Commit：`9a4ca2ce4a646badedbc98ab1469c3e8fb9995a8`（區間路徑語意）；回歸測試 Commit：`d303ac600c17fc275b690ae183d0d67b7bf3cf8e`。
- 區間情境不再以連續單向箭頭暗示先後目標；現價至 Put Wall 顯示「位於」，Put Wall 至 Call Wall 顯示「↔」，表示價格位於上下界之間。
- 偏多／偏空價格節點篩選、機率未校準聲明及 MaxPain 僅作磁吸參考的規則維持不變。
- 僅修改 UI template 與對應靜態回歸測試；未修改 P0、Master、V8、正式資料或部署設定。

### 測試與視覺證據
- GitHub Actions Run `41312758676`：Success；Builder offline self-tests、JavaScript parser、React template regression、DATA_REPORT parser、JSON build、非部署 HTML preview、隔離 heatmap fixture 及 Artifact 上傳皆成功。
- Run URL：`https://github.com/grichtoyang/daily-premarket/actions/runs/41312758676`。
- 非部署預覽 Artifact：`V9-UI-Fixes-Preview-20261030`，Artifact ID `13085608534`。
- 使用者提供新版 Android 手機截圖：偏多、區間、偏空三條路徑均顯示實際有效價格節點；區間情境已呈現「現價 位於 Put Wall ↔ Call Wall」；未見卡片重疊或裁切。DATA-UI-04 手機視覺驗收 PASS。

### 最新狀態
| 項目 | 狀態 |
|---|---|
| 三劇本價格節點條件式呈現 | PASS |
| 區間上下界語意與箭頭修正 | PASS |
| MaxPain 不作下跌目標 | PASS |
| 機率未校準、不輸出虛構機率 | PASS |
| CI／回歸測試／非部署預覽 | PASS |
| Android 手機畫面 | PASS |
| 桌面視覺（含 1440px） | NOT TESTED |
| 真實市場情境回測與機率校準 | NOT TESTED（本功能不宣稱已回測） |
| Merge／Cherry-pick／正式部署 | NOT DONE |

- Auditor：單模型自我審查，非獨立多模型審核。


## 21. 2026-11-01 DATA-UI-03 IV／GEX 深度資料鏈第二輪調查

### 查核範圍（唯讀）
- Repo：`grichtoyang/daily-premarket`；程式查核分支：`phase2-p0-ui-fixes`。
- 查核檔案：`src/sources/taifex.py`、`scripts/v9_pro_builder.py`、`docs/DATA_SOURCES.md`、`docs/DATA_REPORT_TEMPLATE.md`、`data_reports/DATA_REPORT_20261030.md`、`dashboards/data-latest.json`、`templates/v9-pro-react-template.html`。
- 本次未修改任何程式、資料或部署設定。

### 根因確認
1. Builder 的 TAIFEX options chain 流程目前只使用合約月份、Call/Put、履約價、成交量及 OI，計算 Call/Put Vol、OI 與 PCR；沒有將隱含波動率、Bid/Ask、Gamma 等欄位納入 DATA_REPORT／JSON。
2. DATA_REPORT 選擇權章節目前列有成交量、OI、PCR、Wall、Gamma Wall／Flip、Max Pain、法人與前十大資料，沒有 IV Rank、Risk Reversal、期限 IV 序列或逐履約價 Greeks。
3. JSON `options` 無 `gex`、`ivRank`、`riskReversal`、`ivTerm` 等欄位。Builder 的 GEX 因子只接受來源直接提供且可驗證的值；IV／Term 分析卡明確註記 DATA_REPORT 未提供。
4. React 卡片標題為「IV / GEX 深度」，但圖表實際只繪 PCR、Call Vol%、Put Vol%；表格另列 GEX、IV Rank、Term 為 unavailable。這造成標題與圖表內容不完全一致，屬 UI 語意問題；PCR／成交量比例本身有來源資料，不應描述為 IV／GEX 圖。
5. TAIFEX 官方公開資料目錄可查到選擇權每日行情、每日 Delta、Put/Call Ratio 與 TAIEX Options Volatility Index（TAIWAN VIX）；官方 FAQ 說明 VIX 代表市場預期未來 30 日波動率，並提供歷史資料下載。官方公開目錄未列出直接供應的 GEX 或 IV Rank 欄位。

### 可行性與限制（不得把推導值冒充官方原始值）
- **TAIWAN VIX／波動率歷史排名：** 可評估使用官方 VIX 歷史序列計算 rolling 52-week percentile／rank；必須將名稱標示為「TAIWAN VIX Rank／30D 波動率歷史排名」，不能未經定義直接稱為單一履約價 IV Rank。
- **期限結構：** 可評估由各到期月份的選擇權報價（優先有效 Bid/Ask mid，無效／零報價排除）、標的價格、到期時間及利率／股利假設反解 ATM IV，再插值為固定期限（如 7D／14D／30D／60D）。必須保存輸入、報價時間、到期日、方法與品質旗標；不可用成交量／OI 代替 IV。
- **GEX：** 可由逐履約價 OI、Gamma、合約乘數與標的價格計算 gross gamma exposure；但 OI 本身不帶多空持有人方向，不能直接推導做市商淨 Gamma 正負。若要 signed/dealer GEX，必須先定義並驗證持倉方向估計方法；否則只可呈現 unsigned/gross GEX 或明確標為模型估計。
- **TAIFEX DailyOptionsDelta：** Delta 不等於 Gamma；不能直接把 Delta 當 Gamma，也不能單靠每日 Delta 直接得到 GEX。

### UI／資料處理建議（待實作）
1. 將現有圖表標題改為「PCR／成交量結構」，避免把成交比例誤稱 IV／GEX 深度。
2. GEX、IV Rank、Term 仍維持 unavailable，直到資料源、公式、日期對齊與品質檢查通過。
3. 後續若實作，先定義 gross GEX、TAIWAN VIX Rank 與期限 ATM IV 的欄位 schema、單位、時間基準、到期範圍及回歸測試，再接入 DATA_REPORT／Builder／JSON／Dashboard。

### 狀態
| 項目 | 狀態 |
|---|---|
| 上游欄位缺漏根因 | PASS（已追到來源／DATA_REPORT／Builder／JSON） |
| 現有缺值不造假 | PASS |
| 卡片標題與圖表內容不一致 | FAIL（已定位，尚未修正） |
| TAIFEX VIX 歷史序列接入 | NOT TESTED |
| 各期限 ATM IV 計算 | NOT IMPLEMENTED |
| Gross GEX 計算 | NOT IMPLEMENTED |
| Signed／Dealer GEX 方法驗證 | BLOCKED（OI 無方向資訊，需另定估計方法） |
| DATA-UI-03 完整結案 | NOT DONE |

- 官方參考：TAIFEX OpenAPI `https://openapi.taifex.com.tw/`；TAIFEX VIX／歷史資料說明 `https://www.taifex.com.tw/enl/eng9/tradersQAProducts`；TAIFEX 選擇權歷史行情下載 `https://www.taifex.com.tw/enl/eng3/optDailyMarketView?menuid1=03`。
- 本次 Auditor 為單模型自我審查，非獨立多模型審核。


## 22. 2026-11-01 DATA-UI-03 GEX 資料鏈第一階段實作

### 實作範圍
- 實作分支：`phase2-p0-ui-fixes`；未修改 Master、P0 baseline 或 V8。
- `src/sources/taifex.py`：保留既有 Gamma endpoint 已計算的 `levels`、`net_gex_1pct`、`gross_gex_1pct`、`gamma_diagnostics`、模型與品質欄位；逐履約價欄位依實際來源 schema（`call_gex_1pct`、`put_gex_1pct`、`net_gex_1pct`、`gross_gex_1pct`）驗證數值、有限值及正履約價，並排序。
- Gamma 主端點回傳日期不符 T0 時拒收；compact proxy 只保留 Wall／Flip，不將 proxy 值冒充 GEX。GEX 明細不完整時狀態為 unavailable。
- `src/fetch_data.py`：DATA_REPORT 新增 Net／Gross GEX、模型品質、履約價筆數、正負 Net GEX Top 5；附加衍生後逐履約價 GEX JSON 區塊，不包含原始報價。
- `scripts/v9_pro_builder.py`：只接受日期與 DATA_REPORT T0 相符的 GEX JSON 區塊，並將摘要、日期、狀態及逐履約價資料輸出至 Dashboard JSON。
- `templates/v9-pro-react-template.html`：原「IV / GEX 深度」卡改為「履約價 GEX 分布」，繪製逐履約價 Net GEX；缺資料時明確顯示 unavailable。
- 新增逐履約價來源欄位驗證測試。

### Commit／驗證
- Source validation：`613ce0146b19db70859560c430ae470e81d267b6`；欄位 schema 修正：`dfba4b6bd6074551330fe8e24c8139f0f4f62f32`。
- 測試：`4c95cdefa92db010e47c023a7196c639242b3c6c`。
- DATA_REPORT：`0c2f6aa8c7b038664959ae8c93b92121e6ab5091`。
- Builder JSON：`5125d66613b8e2ee21d09e914a299bac43779241`。
- Dashboard UI：`833b0220ad87d768a6805d68f47e5447f590fcc9`。
- GitHub Actions Run `41316484376`：Success；17F offline self-test、React template regression、DATA_REPORT parser regression、Dashboard JSON build、非部署 HTML preview 均通過。

### 未完成／風險
- **Live Gamma endpoint／當日 GEX 明細：NOT TESTED**；CI 的 DATA_REPORT／JSON build 成功不代表當日 Gamma endpoint 有資料。
- Gamma payload 日期是否在正式端點穩定等於 T0，仍需以實際當日回應確認；不符時目前採 fail-closed。
- Dashboard 真實 GEX 圖表視覺（手機／桌面）：NOT TESTED；尚待使用者實際畫面驗收。
- IV Rank／TAIWAN VIX Rank／IV Term：NOT IMPLEMENTED。
- Signed／Dealer GEX：BLOCKED；本次沒有新增方向估計模型，也沒有把 gross/net model output 宣稱為 dealer positioning。
- Actions 增量耗時是否低於 10 秒：NOT TESTED。
- 未 Merge／Rebase／Cherry-pick／Deploy；本次 Auditor 為單模型自我審查，非獨立多模型審核。


## 23. 2026-11-01 DATA-UI-03 GEX 第一階段狀態複核（交接基準）

> 本節為目前交接的最新狀態；與第 22 節重複的實作細節以第 22 節為準。本節補上遠端分支與 Actions 的即時查證結果。

- Repo：grichtoyang/daily-premarket。
- UI branch：phase2-p0-ui-fixes，查證 HEAD：833b0220ad87d768a6805d68f47e5447f590fcc9。
- HEAD commit message：Render actual per-strike GEX distribution in options card；其 parent 為 Builder commit 5125d66613b8e2ee21d09e914a299bac43779241。
- GitHub Actions Run 41316484376 已由 GitHub API 查證：completed / success，head SHA 與 UI branch HEAD 相同；Workflow 為 V9 UI Fixes Regression。
- 第 22 節記錄的 Dashboard GEX 卡片接線與該輪 CI 成功有遠端 commit／run 證據；但 CI 成功只代表該 workflow 的自動化檢查通過，不等同真實當日 Gamma 端點有資料，也不等同使用者實際畫面驗收。

### 最新驗收狀態
| 項目 | 狀態 |
|---|---|
| 來源 Gamma GEX 欄位保留及格式驗證 | PASS（程式提交；CI run success） |
| DATA_REPORT GEX 摘要及衍生履約價資料區塊 | PASS（程式提交；CI run success） |
| Builder 日期檢查及 Dashboard JSON 欄位接線 | PASS（程式提交；CI run success；真實有值資料情境仍待確認） |
| React 選擇權頁 GEX 分布卡片接線 | PASS（程式提交；CI run success） |
| 真實當日 Gamma endpoint 回應及逐履約價 GEX 有值 | NOT TESTED |
| 手機／桌面實際 GEX 圖表視覺 | NOT TESTED |
| GEX 計算模型獨立正確性／與外部基準交叉驗證 | NOT TESTED（沿用既有模型，本輪未重算） |
| IV Rank／TAIWAN VIX Rank／期限 IV | NOT IMPLEMENTED |
| Signed／Dealer GEX | BLOCKED（持倉方向估計方法未定） |
| Actions 增量耗時是否低於 10 秒 | NOT TESTED |
| Merge／Cherry-pick／正式部署 | NOT DONE |

### 下一個工作（唯一順序）
1. 先以當日 T0 真實資料跑完整 DATA_REPORT → Builder → Dashboard JSON，確認 options.gexStatus、gexLevels、Net／Gross GEX 日期一致且非空；若來源失敗則確認明確 unavailable，不能沿用舊日期。
2. 取得非部署 HTML Artifact，驗收手機及桌面 GEX 圖表；完成前 DATA-UI-03 不結案。
3. 最後量測 Actions 執行時間，確認新增處理耗時；不可預先宣稱低於 10 秒。

- 本次交接文件更新不改動程式、正式資料或部署設定。Auditor 為單模型自我審查，非獨立多模型審核。


## 24. 2026-11-02 新對話恢復校正：P0 已正式結案

> 本節優先於本文件第 4、6、9～23 節中任何「P0 尚未結案」或「DATA-UI 尚待修正」的舊狀態。舊紀錄保留作為歷史追溯，不得照舊重做。

### 最新權威結案紀錄
- 以 `phase2-p0-ui-fixes` HEAD `a791e4f3a2a15e46cc670b163b2160651df070c3` 為 P0 結案紀錄；Commit 訊息：`docs(recovery): close Phase 2 P0 semantic audit`。
- P0：PASS／CLOSED。沒有已知未修正的 P0 程式或 Dashboard 欄位語義缺陷。
- 沿用既有驗收：Unit Contract #106、UI Regression #136、Daily Build #173、Browser Audit #41400089885（12 次 Desktop／Mobile 畫面檢查）；不為了結案重跑未受影響的測試。
- V8 保留不動；Master 與 P0 baseline 不修改；未 Merge、未部署。
- 10/30 原始 API 逐筆對帳、GEX 原始輸入重建、因子預測力／walk-forward 均為 NOT TESTED 的後續獨立稽核，不是 P0 blocker。

### 本次重新查證的分支
| 分支 | HEAD |
|---|---|
| `ops/recovery-handoff`（本文件分支，更新前） | `227bcf862d03613d66eff7368886282edadc5c3f` |
| `phase2-p0-ui-fixes` | `a791e4f3a2a15e46cc670b163b2160651df070c3` |
| `phase2-p0-data-quality` | `49fd5b0dfd6a9c1b89fc49bb6e4d81ae5fdc4d33` |
| `master` | `136eb43ebbfd0a59dc2bb715238d5fb9eae42cad` |

- P0 UI fixes 相對 P0 baseline：ahead 272、behind 0。
- P0 baseline 與 master：分歧；compare 顯示 master 相對 P0 ahead 8、behind 290。
- 不得 Merge／Rebase／Force Push；任何整合須另行提出方案並取得明確授權。

### 最新工作資料觀察（唯讀）
- 10/30 DATA_REPORT SHA：`665ae0ce957cbda372a1d70e1f06f0eea124ba11`；含 139 筆 GEX_LEVELS_JSON 衍生結果，但不含足以獨立重建的原始 IV／OI payload。
- 10/30 GEX 139 筆內部檢查曾確認 Net = Call + Put、Gross = |Call| + |Put|，逐筆及總計差異為 0；這只證明內部一致性，不是外部原始輸入對帳。
- 11/02 DATA_REPORT SHA：`8ccd0dfc0f86f80e23253781bf923a533566df96`；產出時間 14:35:26，Gamma／GEX 原始端點未取得時如實標 unavailable。
- 11/02 Dashboard JSON SHA：`9e2c50907535d6f070a353eca50722d8c5e98aa1`；GEX status unavailable。不可將 11/02 當日快照混作 10/30 歷史原始輸入。

### 下一個唯一工作
**開始 P0 結案後的 10/30 原始 API 資料稽核（唯讀）。**
1. 盤點 TAIFEX／TWSE／TPEX 各欄位的原始端點、請求參數、資料日期、來源欄位與報告輸出欄位。
2. 確認 10/30 原始 payload 是否仍可由官方 API／Proxy 歷史查詢取得；取得者保存可重現證據，無法取得者標 BLOCKED。
3. 對可取得欄位逐筆重算並與 DATA_REPORT 比較，輸出差異表及來源日期／單位問題。
4. 完成來源對帳後，再獨立重建 GEX 原始 IV／OI 輸入；最後才評估因子預測力與 walk-forward。
5. 本輪不修改 P0 程式、不更新正式 Dashboard、不部署、不 Merge；V8、Master、P0 baseline 維持不動。

### 本次狀態
- 讀取三份 recovery 文件：PASS。
- GitHub branch／HEAD／compare 唯讀查證：PASS。
- 讀取 P0 結案 Commit 與結案報告：PASS。
- 本次 Recovery／Progress 文件校正：IN PROGRESS（完成遠端寫入與讀回驗證後才可標 PASS）。
- 原始 API 逐筆對帳：NOT STARTED。
- GEX 原始輸入重建：NOT STARTED。
- 因子預測力／walk-forward：NOT STARTED。
- 本次未修改程式、正式資料、Dashboard、Workflow、V8、Master 或 P0 baseline。



## 25. 2026-11-02 接續進度：10/30 API 來源追查第一輪

### 最新分支／資料 Commit 更正
- P0 結案錨點仍為 `a791e4f3a2a15e46cc670b163b2160651df070c3`。
- P0 結案後，`phase2-p0-ui-fixes` 有一筆 Actions 產出 Commit：`d5443eacb29b7b0824306de4d1b126b9281210b5`（父提交即 P0 結案 Commit）。此提交只更新 10/30 Dashboard 資料／呈現與 manifest，不代表 P0 程式碼有新變更。
- 10/30 DATA_REPORT SHA：`665ae0ce957cbda372a1d70e1f06f0eea124ba11`，產出時間 2026-11-01 23:51:51。

### 第一輪唯讀盤點結論
1. `daily_data.yml` 沒有保存原始 API response 的 artifact 步驟；`src/fetch_data.py` 產出正規化報告。Git 中目前只有衍生結果，沒有可直接獨立重算的 raw response 封存。
2. 現貨主要歷史來源可指定 T0：TWSE MI_INDEX、FinMind TAIEX、TWSE 自建維持率使用的 MI_MARGN／MI_INDEX、TWT93U（但 10/30 報告註記 TWT93U 未取得）。
3. TWSE BFI82U proxy 程式註明 RWD 忽略 date 參數、只回最新日期並提供 actual_date；因此不能只憑 `?date=20261030` 宣稱可回查歷史。
4. TWSE MI_MARGN、TWT96U 主報表欄位無日期，報告已註明採最新可得；不能將其直接當成 10/30 歷史 raw。
5. TPEX highlight 沒有 date query，程式只檢查回傳第一列 Date；歷史可用性尚未實際驗證。
6. TAIFEX Worker 支援指定歷史日期的 TXO daily market chain；Delta 歷史下載先檢查最近 30 交易日清單，再下載指定日 Excel。10/30 應優先驗證這條路徑；OpenAPI fallback 不能先假設有完整歷史資料。
7. 10/30 DATA_REPORT 已註明 TWSE TWT93U 未取得，借券賣出增減僅上櫃值；報告來源標籤需在對帳時核實，不能當作上市櫃完整合計。

### 執行結果與限制
- 程式碼、Worker 路由、日期參數及 DATA_REPORT 來源註記盤點：PASS。
- 原始 API response 實際擷取：BLOCKED（本次執行介面無法直接取回指定 Cloudflare Worker／TWSE／TPEX API payload）。
- 逐筆對帳：NOT TESTED。
- GEX 原始輸入重建：NOT TESTED；但 TAIFEX 歷史 chain／Delta 的程式路徑已確認，尚待實際請求。
- 本次未修改正式程式、Dashboard、資料報告、Workflow、V8、Master 或 P0 baseline。

### 下一個工作
使用具備直接 HTTP GET/POST 的環境，逐一保存 10/30 原始 API request／response（含 URL、POST body、HTTP status、回傳日期、原始檔及 SHA-256），再逐欄重算。優先順序：
1. TAIFEX TXO chain + Delta + TWSE FMTQIK（為 GEX 重建準備原始資料）。
2. TWSE MI_INDEX、FinMind TAIEX、TWSE 自建維持率、TWT93U。
3. BFI82U、TPEX、HiStock 等可能只有最新資料或有限歷史窗口的來源，先確認可回查性。
4. 對 10/30 TWT96U／MI_MARGN 最新值的日期不匹配及 TWT93U 缺值，分別列出，不用當前資料替代歷史數據。



### GEX 重建輸入與模型細節（TAIFEX Worker V1.4 程式碼）
- Chain 必要欄位：到期月份／到期日、履約價、Call/Put、結算價、OI。
- Delta 必要欄位：到期月份／到期日、履約價、Call/Put、有限數值 Delta；目前實作僅用有限 Delta 建立 Chain/Delta 匹配鍵，Delta 數值本身不直接代入 Gamma 公式。
- 標的價格必須是同 T0 的 TWSE TAIEX close（FMTQIK），不能以 TX 期貨價替代。
- IV 由結算價反解 Black-Scholes implied volatility（r=0）；Gamma 使用 Black-Scholes；單筆 GEX = Gamma × OI × 50 × S² × 0.01。
- 符號約定為 Call 正、Put 負；Worker 說明此為 customer-long/dealer-short 假設，不是官方 Dealer 實際部位資料。
- Gamma Wall 為絕對 Net GEX 最大履約價；Gamma Flip 在標的價格 ±10% 掃描總 GEX，取第一個符號跨越並線性插值。
- 模型有效門檻為可計算筆數／符合正 OI、正結算價及 Chain/Delta 匹配條件的筆數 >= 50%。
- 獨立重建必須保存 Chain、Delta 原始列及標的收盤價；不能由 GEX_LEVELS_JSON 反推原始 IV／OI。


## 26. 2026-11-02 最終收尾決策

本節為目前有效的收尾指令，優先於第23～25節要求重新逐筆對帳或建立原始 API 擷取流程的舊待辦；舊紀錄保留為歷史，不再執行。

- 使用者確認：10/30 TAIFEX／TWSE／TPEX 逐筆比對已多次驗收，沿用既有結果，不重跑、不再總驗收。
- 直接使用現有 DATA_REPORT 與既有驗收紀錄；不新增 Raw API Audit Runner、Fetch Data 機制或 Worker。
- P0 保持 PASS／CLOSED；不修改正式資料鏈、Dashboard、P0 baseline、Master 或 V8；不 Merge／Rebase／Force Push／部署。
- 10/30 DATA_REPORT SHA：665ae0ce957cbda372a1d70e1f06f0eea124ba11。報告含 139 筆衍生 GEX_LEVELS_JSON；underlying=45,211.83；Net GEX=1,294,327,419.01；Gross GEX=6,320,130,202.13；quality=usable。
- 沿用既有 139 筆內部一致性驗收：Net=Call+Put、Gross=abs(Call)+abs(Put)，差異為 0；不重算。
- GEX_LEVELS_JSON 不含原始 Chain、完整 Delta payload 與原始報價，因此 DATA_REPORT 足以保留既有 GEX 結果與內部一致性證據，但不足以獨立重建原始 IV／Gamma。標記 BLOCKED；本階段不新增抓取工具，將限制記錄後收尾。
- 因子預測力／walk-forward 不屬本次 P0 收尾範圍，不列入待辦。新增 Fetch Data／Runner／Worker 均 NOT IN SCOPE。

最終狀態：P0 結案後稽核收尾完成；GEX 原始輸入重建保留 BLOCKED 限制。不得因該限制重新啟動本階段或重複既有驗收。Auditor 為單模型自我審查，非獨立多模型審核。


## 27. 2026-11-02 區塊 A/B Template 與建置來源一致性收尾

### 最新工作基準
- 工作分支：`fix/three-market-correlation-history`。
- 最新 Commit：`38162c1b84ac8f309f618a69d8e9606c82eb737c`。
- A 三市場圖表分流：`7c00dcd5cb95e4b892d2fd73f705630afbffc2e0`；B 選擇權多空力道金額定義：`dc09cb7332f7c5290fc478cd78187a1ebeeccb33`；選擇權法人表格口數單位：`8eace1b368816ae65016c9890166aab6b48139d2`。
- 先前大範圍 React 替換造成語法失敗（Runs `41466664463`、`41466690791`）已由 `81f146714de08f0d0de6299a49427ca490eab69d` 還原至語法通過版本，再以小範圍修改完成 A/B；歷史 FAIL 不代表目前仍 FAIL。

### 建置來源查證與防呆
- Workflow 第一個 checkout 指向觸發分支；V9 Pro Build 與 Golden Fixture 均讀取 repo root 的 `templates/v9-pro-react-template.html`。
- `master-site` 是第二個獨立 checkout，僅用於 Pages 根目錄；新版分支輸出複製到 Pages `p0/`，不會以 Master Template 產生新版 V9 Pro HTML。
- Commit `38162c1b84ac8f309f618a69d8e9606c82eb737c` 將第一個 checkout pin 到 `github.sha`，新增驗證：HEAD 必須等於 triggering SHA，Template worktree blob 必須等於該 commit 內的 Template blob；Master checkout 明確標示僅供 Pages root。
- GitHub Actions Run `41475229916`：completed / success；來源驗證步驟 PASS，Golden Fixture 與正式 HTML inline JavaScript syntax check PASS，Pages artifact assembly/upload PASS。
- Artifact `13156417750`（github-pages，1,780,599 bytes，未過期）。
- Deploy job skipped；沒有部署到正式 Pages。

### 最新驗收狀態
| 項目 | 狀態 |
|---|---|
| A 三市場圖表分流與單位 | PASS（CI／Artifact 靜態輸出） |
| B 選擇權法人多空力道金額定義 | PASS（CI／Artifact 靜態輸出） |
| 選擇權法人交易表格口數單位 | PASS |
| 建置 checkout 固定觸發 Commit | PASS |
| Template blob 與觸發 Commit 一致 | PASS（Run 41475229916） |
| 正式 HTML inline JavaScript 語法 | PASS |
| 10/30 Golden Fixture 語法與建置 | PASS |
| Pages Artifact 組裝／上傳 | PASS |
| 實際瀏覽器／手機畫面與排版 | NOT TESTED |
| Merge／正式部署 | NOT DONE |

### 下一步
1. 使用者開啟 Artifact `13156417750` 內的 `p0/test-fixtures/v9-pro-20261030-full-day.html`，驗收區塊 A/B 的實際圖表、文字、單位及手機排版。
2. 若畫面驗收通過，才更新本分支的 A/B 視覺驗收狀態；不得以 CI／Golden Fixture 語法通過代替使用者畫面驗收。
3. 不執行 Merge／部署；後續範圍由使用者另行確認。

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


## 28. 2026-11-03 區塊 A/B RWD 與選擇權法人多空力道表修正

### 修改
- 工作分支：`fix/three-market-correlation-history`；Template Commit：`be9c27adc3bc4491cd932930d31736f053695b2e`。
- 手機／窄版 RWD：A/B 主 grid 在 viewport <=1100px 強制單欄；區塊 A 跨滿整列；桌面 >1100px 保留原本 A 2/3、B 1/3 配置。
- 區塊 B 表格原先錯誤呼叫雙欄 helper `ee`，而資料列實際為 7 個顯示欄位，導致只顯示每列前兩欄。已改成真正 7 欄表格，完整顯示法人、日多方、日空方、日淨、夜多方、夜空方、夜淨，包含三大法人合計列。
- 表格新增橫向捲動，手機不壓縮欄位；新增單位及欄位定義文字，明確區分來源力道分項／淨額、交易口數與 OI。
- 修改僅涉及 Template 呈現，不更動資料來源與計算引擎。
- DATA_REPORT_20261102.md 原始法人力道表有 9 欄；Dashboard 顯示前 7 個核心分析欄位。來源欄與日淨－夜淨欄位不混入主表。

### CI 與驗收
- Commit：`be9c27adc3bc4491cd932930d31736f053695b2e`。
- Run `41478733638`：HTML build、JS syntax validation、Pages artifact assembly/upload 步驟成功；Artifact `13157839737`（github-pages，1,782,342 bytes，未過期）。
- 截至更新時 build job post-checkout cleanup 尚顯示 in_progress；不能將整個 Run 宣告 completed。
- 實際新 Artifact 手機畫面驗收：NOT TESTED；RWD 程式規則已加入，但須以新 Artifact 開啟後確認手機 A/B 是否上下排列、表格是否能橫向捲動。
- Merge／部署：NOT DONE；Master、V8 未修改。
- Auditor：單模型自我審查，非獨立多模型審核。

### 下一步
1. 取得 Artifact `13157839737` 的 `p0/v9-pro-latest.html`。
2. 在手機實際開啟，確認 A/B 上下排列；區塊 B 表格七欄完整且可水平捲動。
3. 若畫面通過，更新手機視覺驗收為 PASS；若不通過，只修正 RWD CSS，不動資料邏輯。
4. 不 Merge、不部署，除非使用者另行明確授權。


## 29. 2026-11-03 手機實際畫面驗收完成

- 使用者提供新版 `p0/v9-pro-latest.html` 手機瀏覽器實際截圖。
- A/B 手機上下排列：PASS。
- 區塊 B 七欄表格完整呈現，含三大法人合計；單位與欄位定義清楚：PASS。
- 日淨合計抽查：+0.18 -3.01 +1.82 = -1.01；夜淨合計抽查：-0.06 +0.00 -0.54 = -0.60，與合計列一致：PASS。
- 截圖未見 A/B 重疊、表格欄位互相覆蓋或數字裁切：PASS。此視覺驗收只涵蓋使用者提供的手機／瀏覽器／縮放條件，不外推至所有裝置。
- CI Run `41478733638` 已確認 completed / success；建置 Commit `be9c27adc3bc4491cd932930d31736f053695b2e`。
- 本輪 A/B 手機畫面驗收可結案。正式 merge／部署仍 NOT DONE，未獲使用者授權不得執行。
- Auditor 為單模型自我審查，非獨立多模型審核。


## 30. 後續工作統一採用全面驗收門檻（2026-11-03 使用者要求）

使用者明確要求後續驗收必須全面，不得只看畫面或 CI。往後每個修正區塊／功能，交付前均須依下列層次驗收，並留下可追溯證據：

1. **需求與規格**：對照 Master/當前分支適用規格、欄位定義、單位、方向、資料時間窗及例外狀態；先確認本次修改範圍及不得觸碰的檔案。
2. **資料來源與新鮮度**：核對來源、官方資料日期、取得時間、原始值、缺值／延遲／休市狀態及 fallback；尚未到公布時間的資料應標示待更新／NOT TESTED，不得誤判為程式缺陷或假造即時值。
3. **計算與資料契約**：逐欄位核對解析、型別、單位、正負號、精度、千分位、加總、邊界條件；必要時以原始資料獨立重算，並使用正常、零值、負值、缺值及極端值 fixtures。
4. **圖表與視覺**：核對圖表系列、軸、單位、標籤、圖例、動態高度、數字與單位是否重疊／裁切；桌面與手機實際畫面均需檢查，不能以 CSS 存在或單一 viewport 推定所有裝置 PASS。
5. **AI 分析品質**：檢查是否真正解讀數據而非重述；是否比較主導者、強弱、時段變化、方向一致／分歧及不確定性；分析、判斷、操作條件須引用同一組數據、邏輯一致，不得超出資料可支持的結論。以代表性案例人工審核。
6. **整合與回歸**：驗證相關上下游資料鏈、同頁其他區塊及 42 個 Dashboard 區塊的既有功能；11 張圖表依專案清單逐一檢查；確認無因局部修改造成的版面、資料或 JS regression。
7. **正式產物與來源一致性**：確認 workflow checkout 的 branch/ref、實際使用 Template、commit SHA、build inputs、Artifact 路徑與 HTML 內呈現一致；檢查正式 HTML 語法與 JS、Golden Fixture 及 CI。不得用單獨通過的 fixture 代替正式 HTML 驗收。
8. **交付與證據**：提供 CI run、commit、artifact、實際截圖／測試結果及 Recovery 記錄；逐項標示 PASS、FAIL、BLOCKED、NOT TESTED。只有必要驗收項目全部 PASS 才可結案；任何 BLOCKED／NOT TESTED 必須明確保留，不得包裝成完成。

### Supervisor / Worker / Auditor 執行要求
- Supervisor 先盤點、定義驗收標準與修改邊界；Worker 集中完成修正；Auditor 依證據逐項獨立檢查並要求修正／複驗。
- 若本環境無法呼叫獨立模型或 Agent，必須明確標示為單模型自我審查，不得稱為獨立審核。
- 不得每完成一個小項就中斷要求使用者逐項指揮；應先完成全盤清查、集中修正、完整回歸後再交付。
- 除非使用者另行明確授權，不得修改 V8、Master 或其他未授權分支，不得 merge、部署或覆蓋正式版本。
- 本要求適用於後續所有 V9 Pro 區塊，不因 A/B 本輪已結案而降低標準。


## 31. 2026-11-03 區塊 B 選擇權法人多空力道動態分析升級

### 問題根因
- DATA_REPORT 原本已提供完整七欄金額表，含日／夜多方、空方、淨額及來源日淨－夜淨差。
- Builder 原本僅解析並輸出 instOptForce，沒有建立區塊 B 專屬分析邏輯；React Template 的 look／compass／target 是固定寫死的通用句，因此即使數據改變，分析也不會跟著更新。
- 本輪未接入 LLM。新增的是 deterministic／rule-based data interpretation；不可稱為即時生成式 AI 分析。
- TAIFEX 金額資料定義：上游 long_amount／short_amount 是買方／賣方契約金額。src/fetch_data.py 方向分類：多方＝買 Call＋賣 Put；空方＝賣 Call＋買 Put；上游千元 ÷ 100,000 = 億元。這是方向分類代理指標，不等於淨權利金現金流或 OI／實際持倉。

### 修改範圍
- scripts/v9_pro_builder.py 新增 build_option_force_analysis()：
  - 檢查外資／投信／自營商／三大法人合計列及七欄數值。
  - 驗證多方－空方＝淨額、日淨－夜淨、三法人淨額加總；允許兩位小數獨立四捨五入造成的有限差異；發現超出容差則停止方向結論。
  - 缺值保持 unavailable，不得視為 0。
  - 輸出日／夜盤主要空方、最大多方抵銷者、合計淨額、淨額相對雙邊金額比例。
  - 將日淨－夜淨解釋為兩個時段淨額相減，不宣稱日對日變化。
  - 與 A 區口數逐法人逐時段對照，分類同向／背離／中性；背離不得互相覆蓋。
- Dashboard JSON 增加 options.instOptForceAnalysis；Template 區塊 B 改讀動態分析結果，不再使用固定通用句。
- B 區副標題及圖表備註補上公式與「契約金額代理值」限制；未改變資料來源、資料計算引擎、圖表及七欄表格。
- 新增 tests/test_builder_option_force_analysis.py；Workflow 加入該測試及既有 option table regression。原測試中一條舊用語斷言與現行程式文案不一致，僅修正測試期待值。

### 11/02 T0 樣本驗算
- 日盤多方 21.57 億、空方 22.58 億、淨額 -1.01 億；淨額／多空雙邊金額合計 -2.29%。
- 夜盤多方 7.70 億、空方 8.29 億、淨額 -0.60 億；淨額／多空雙邊金額合計 -3.75%。
- 日盤主空方投信 -3.01 億，最大多方抵銷自營商 +1.82 億；夜盤主空方自營商 -0.54 億，投信 0。
- 日淨－夜淨合計差 -0.41 億，為日盤淨額減夜盤淨額，不代表日對日變化。
- A 區淨交易口數對照：4 組同向、1 組背離、1 組中性；外資日盤金額 +0.18 億與口數 -167 口背離。已寫入 compass／target。
- 百分比是根據 DATA_REPORT 顯示到小數二位的金額估算，非 raw payload 未四捨五入值重算。

### CI／產物
- HEAD：07696e52086101692311f60d020e47c7972150d7。
- Run 41481675963；build job 24 個成功步驟、0 failed，最後 post-checkout cleanup 尚未回報完成。
- Options-force analysis contract tests：PASS；option table regression：PASS；17F self-tests：PASS；Dashboard JSON build：PASS；正式 HTML／Golden Fixture JS syntax：PASS；Artifact upload：PASS。
- Artifact 13159728345（github-pages，1,785,704 bytes，未過期）。
- 已下載 Artifact 並檢查 p0/data-20261102.json 的 options.instOptForceAnalysis，及 p0/v9-pro-latest.html 的注入文字；分析、背離與公式字串均存在。
- Chromium 實際渲染：NOT TESTED（執行環境 file://／localhost 被管理政策阻擋，headless CLI 逾時）；需使用者實際手機截圖驗收。
- 每個 options day/night API response 的 endpoint-level date 未保留於此法人力道表；本輪沿用 DATA_REPORT T0／來源標籤，未修改來源擷取流程。Endpoint 級日期獨立對帳：NOT TESTED。
- Merge／部署：NOT DONE；V8／Master 未修改。Auditor 為單模型自我審查，非獨立多模型審核。

### 下一步
1. 等待 Run 41481675963 回報 completed／success。
2. 使用者下載 github-pages Artifact 13159728345，開啟 p0/v9-pro-latest.html。
3. 檢查 B 區動態分析、公式備註、七欄表格、手機排版及文字裁切；未完成使用者實際畫面驗收前不得結案。
4. 不 merge／部署，除非另行取得使用者明確授權。

## 32. 2026-11-03 區塊 B 手機畫面複驗與數字格式修正

### 使用者截圖複驗
- 使用者提供新版手機畫面；截圖範圍內圖表、七欄表格及分析／判斷／操作文字沒有明顯重疊或裁切。
- 算術及分析核對：
  - 日盤合計淨額 -1.01 億，夜盤 -0.60 億，日淨－夜淨差 -0.41 億，計算一致。
  - 日盤淨額相對雙邊契約金額 -2.3%；夜盤 -3.8%，依顯示數據計算一致。
  - 日盤主空方投信 -3.01 億、最大正淨額抵銷自營商 +1.82 億；夜盤主空方自營商 -0.54 億，正確。
  - A/B 交叉比對 4 同向、1 背離、1 中性；外資日盤金額 +0.18 億與口數 -167 口背離，正確。
- 發現投信夜淨在七欄表格顯示 +0，為原始來源字串未格式化，不是計算錯誤。

### 程式修正
- templates/v9-pro-react-template.html：七欄表格統一兩位小數；多空分項固定兩位小數，淨額正值加正號、負值保留負號、零值顯示 0.00；非數值文字原樣保留。只修顯示層，不改數據。
- tests/test_react_template_static.py：新增數字格式契約測試。
- Template commit fb6924901cf7700e90e9a38faaf54219b5bb02f9；測試 commit 5a3ec0f82c23fad5122beea43f3acfa0a1db6dec。
- Run 41486390048：截至更新時 24/26 步驟完成，options analysis tests、17F、dashboard build、HTML syntax、artifact upload 成功；最後 cleanup 仍在執行。
- Artifact 13161328313，github-pages，1,786,028 bytes，未過期。
- Run 41486406787（含新增格式測試）當時仍 pending，尚未驗證。
- 修正後手機畫面尚未由使用者複驗。
- 未 merge／部署；V8／Master 未修改；未執行獨立多模型審核。

### 下一步
1. 確認兩個 CI Run 最終狀態；尤其 Run 41486406787 新增格式測試。
2. 交付最新 Artifact HTML，確認投信夜淨為 0.00 及整張七欄表格。
3. 修正後畫面複驗完成才結案；未經使用者授權不 merge／部署。

## 33. 2026-11-03 Artifact 路徑釐清與區塊 B 格式修正交付

- CI Run 41486390048 與 41486406787 均 completed / success；後者包含新增格式靜態測試。
- Artifact 13163070059 中，根目錄 v9-pro-latest.html 是 Master dashboard；Workflow 會把本次觸發分支產物放在 p0/。正確驗收目標為 p0/v9-pro-latest.html。先前只檢查根目錄而判定 Artifact 不含新版，是路徑選錯，已更正。
- 正確 P0 HTML 確認新版 B 標題、v9-force-table、instOptForceAnalysis、numeric.toFixed(2)、cellIndex===3||cellIndex===6 均存在。
- p0/data-20261102.json 的 options.instOptForce 中，投信夜淨原始值為 +0；顯示層轉為 0.00，不修改原始資料。
- Node.js 格式邏輯 7 組案例全部 PASS（+0、正值、負值、一般數值、文字、null、千分位數值）；HTML 5 個必要標記全數存在。
- 正確 P0 HTML 已抽取至 /mnt/data/v9-pro-latest-format-fixed.html，供手機複驗。
- Chromium headless 截圖逾時，無畫面產出；瀏覽器實際渲染及手機排版仍 NOT TESTED。
- Pages deploy job skipped，未部署；未 merge；Master root 保持不動。
- 區塊 B 尚未結案，待使用者實際手機檢查修正後 HTML。

### 下一步
1. 使用者開啟交付 HTML，確認投信夜淨顯示 0.00，並檢查手機表格及分析文字。
2. 畫面 PASS 後才結案；FAIL 則修正。
3. 未經明確授權不 merge／deploy。


## 34. 2026-11-03 區塊 B 手機驗收
- 修正版 HTML 手機截圖已由使用者提供。B 區塊圖表、六組法人指標、七欄表格及分析／判斷／操作文字完整；截圖範圍沒有重疊、裁切或欄位錯位。
- 投信夜盤淨額表格顯示 0.00；圖表顯示 0.0 億元。手機視覺 PASS。
- 結合兩次 CI success、正確 P0 Artifact 路徑及 7 組格式測試，本輪 B 區塊格式修正結案。
- 數值精度保留待查：外資日盤顯示多方 11.36、空方 11.17、淨額 +0.18，差 0.01 億元。原始未四捨五入值未取得，故精度對帳 NOT TESTED，後續以原始值確認。
- 本次未驗收其他區塊、其他手機尺寸、橫向模式及跨瀏覽器。未 merge／部署；Master／V8 未修改。
- 下一步：進入下一個未完成 P0 項目，沿用資料來源、計算、HTML、CI、Artifact、手機畫面完整驗收；0.01 億元差異列入對帳清單。


## 35. 2026-11-03 三劇本路徑條件修正（進行中）
- 區塊 B 格式修正已由使用者手機截圖驗收 PASS。本節開始檢查其下方三劇本路徑。
- 原 Pth() 缺陷：偏多只需任一上方 GammaWall／CallWall，未要求有效 Gamma Flip；偏空只需任一下方 GammaWall／Flip，未要求現價低於 PutWall。顯示路徑可能與觸發文字不一致。
- 修正條件：偏多＝有效 Flip 且現價高於 Flip，另需至少一個上方壓力；區間＝PutWall < 現價 < CallWall；偏空＝現價低於有效 PutWall，另需至少一個下方支撐。必要條件缺失即不顯示路徑。
- 文案不再把單一現價位置當成已確認「站穩／有效跌破」；明確說明仍須後續價格行為確認。
- Template commit f87dad314976ad6c4d26125f7a4c37d72f92b6b4；Workflow 增加 Template contract tests commit 8d0fe6f9f5ab4780facbb9fc62f130dc7b409c3c；最新測試修正 HEAD dca0dc9706407b5757d747f5cd608f7419dd86b9。
- 最新 Run 41559500824：React Template／三劇本契約測試 PASS，正式 inline JavaScript syntax PASS；Pth() 代表性六案例由執行環境抽取實際函式測試 6/6 PASS。
- Workflow 整體 FAIL：Replay real historical DATA_REPORTs 在 20261027 eligible=0（expected 1）失敗，且同段出現 SQLite init_db missing primary-key date 訊息。下游 Dashboard build／Artifact skipped。不得將其包裝為完整 CI PASS。
- 三劇本修正狀態：邏輯測試 PASS、Template JS syntax PASS；完整 Workflow FAIL（歷史回放阻斷）；Artifact／完整資料注入／手機畫面 NOT TESTED。
- 未修改 V8／Master；未 merge／部署。Auditor 為單模型自我審查，非獨立多模型審核。

### 下一步
1. 釐清 history replay 20261027 eligible=0 及 SQLite schema 訊息，不跳過或弱化測試。
2. Workflow 完成後，核對 Artifact Template branch/ref、T0 現價與五個關鍵價位來源。
3. 用有效偏多、缺 Flip、區間有效／價位錯側、有效偏空、缺 PutWall／支撐、缺值等 fixtures 驗證。
4. 產出新 Artifact 後由使用者複驗手機三劇本及多空條件檢查表；完成前不得結案或部署。


## 36. 2026-11-03 三劇本路徑與完整 CI 修復驗證
- 根據 Run 41559500824 日誌，新增的 Pth() 六組執行情境測試原先因測試斷言未正規化 React children 文字空白而 FAIL；非路徑計算錯誤。修正測試文字空白正規化後，React Template／三劇本路徑契約測試 PASS。
- 歷史回放失敗根因：fetch_yahoo_twii_30d() 僅取 range=1mo，對較早 T0 過濾後僅剩 14 個交易日；calc_rsi(period=14) 需要至少 15 個收盤價，故 RSI=None，correlation_eligible=0。資料品質門檻正確，不應降低。
- 已將 Yahoo ^TWII 技術指標歷史擷取窗口由 1mo 擴大至 3mo（commit c3a4e238e25e0f54c3c994c072c053622ac47782），維持 RSI14 完整資料要求。
- 最新 CI Run 41559674941：整體 SUCCESS。Template source/ref 驗證、三市場情境測試、React Template／三劇本 18 tests、選擇權契約測試、17F self-test、真實 DATA_REPORT 歷史累積回放、Gamma fallback、歷史資料 seed、Dashboard build、React Golden Master 注入、Golden Fixture inline JavaScript syntax、Pages artifact upload 全部 PASS。
- Run 41559674941 的 deploy job SKIPPED（工作分支，不等同正式部署）；Commit generated dashboard history 亦 SKIPPED。未 merge／部署，Master／V8 未修改。
- Artifact：Run 41559674941 的 github-pages（artifact id 13196591720，約 1.79 MB）。Artifact 已成功上傳，但本輪尚未下載／抽查其中 HTML 及手機實機畫面，故 Artifact 內容抽查、手機三劇本視覺仍 NOT TESTED。
- 歷史回放由 CI 步驟 PASS，表示 20261027→20261102 五日有效樣本累積檢查通過；但本摘要未取得逐日 console 輸出，故不額外宣稱每個樣本的原始數值已人工覆核。

### 下一步
1. 從 Run 41559674941 下載 github-pages artifact，確認內含正確分支產生的最新 HTML／data JSON，檢查 Pth() 注入與關鍵位來源。
2. 將該 HTML 交由使用者手機開啟，驗收三劇本：有效偏多／缺 Flip、區間有效／價位錯側、有效偏空／缺 PutWall／缺支撐／缺值；並檢查多空條件檢查表、文字換行、數字與圖表不重疊。
3. 只有 Artifact source、資料值、手機視覺均 PASS 才結案；未經授權不 merge／deploy。


## 37. 2026-11-03 CI Artifact 實際內容抽查
- 已下載 Run 41559674941 的 github-pages artifact（artifact id 13196591720），解開 ZIP／TAR 後確認 `p0/manifest.json` 指向 date=20261102、data-20261102.json、v9-pro-20261102.html；本次 V9 Pro 正式產物位於 p0 子目錄，不能誤拿 artifact root 的舊版 Pages root HTML。
- 已核對 p0/v9-pro-latest.html 含本次修正後 Pth()；注入資料日期 2026-11-02，現貨收盤 44920.14，PutWall 44000、CallWall 48000、GammaWall／Gamma Flip 均為 null。
- 將 Artifact 實際 HTML 中 Pth() 函式抽出，以 2026-11-02 實際注入資料執行：偏多因 Flip 缺值而阻擋、區間因 44000 < 44920.14 < 48000 而成立、偏空因現價未低於 PutWall 而阻擋。Node runtime check PASS。
- 已抽取正確 HTML 至 /mnt/data/v9-pro-20261102-scenario-fixed.html（303,448 bytes；SHA-256 e22783b01067a0de641665012c48827d4f8144b827d28b5126ce82716addec63），可供使用者手機複驗。
- Artifact 內容／日期／資料注入／實際 Pth() 對照 PASS；手機實機畫面仍 NOT TESTED。未 merge／部署；Master／V8 未修改。

### 下一步
1. 使用者下載並以手機瀏覽器開啟 v9-pro-20261102-scenario-fixed.html，檢查三劇本及多空條件檢查表的文字、卡片、換行、圖表／數字重疊。
2. 依本次資料，應看到偏多未成立（Gamma Flip 缺值）、區間成立（PutWall 44000 < 現價 44920.14 < CallWall 48000）、偏空未成立（現價未跌破 PutWall）。若畫面與此不符即 FAIL，提供截圖修正。
3. 手機 PASS 後再檢查下一個未完成 P0 區塊；未經授權不 merge／deploy。


## 36. 2026-11-03 三劇本修正 CI／Artifact 驗證
- Build HEAD c3a4e238e25e0f54c3c994c072c053622ac47782；branch 另含 Yahoo TWII 3mo lookback 調整，補足歷史 RSI14 回放資料，屬獨立提交。
- Actions Run 41559674941 completed / success；Artifact 13196591720；Deploy skipped。
- 三劇本契約測試、inline JS syntax、歷史 DATA_REPORT replay、correlation seed、Dashboard JSON build、Golden Fixture HTML／JS validation、Artifact upload 均 PASS。
- Artifact 正確新版 p0/v9-pro-latest.html；資料 p0/data-20261102.json；manifest 日期 20261102。HTML 內嵌 JSON 與獨立 JSON 完全一致，T0 均為 2026-11-02。
- T0：spot.close 44920.14；PutWall 44000；CallWall 48000；GammaWall、Flip 缺值。區間成立；偏多因 Flip 缺值不成立；偏空因現價仍高於 PutWall 不成立。舊程式可能顯示不符合觸發條件的路徑，已修正。
- Chromium file:// 渲染遭 ERR_BLOCKED_BY_ADMINISTRATOR；桌面／手機實際畫面 NOT TESTED。HTML 抽取至 /mnt/data/scenario-artifact/p0/v9-pro-latest.html。
- Pth() runtime 6 案例 PASS；CI／HTML syntax／Artifact data consistency PASS；手機視覺待使用者驗收。
- 未 Merge／部署；Master／V8 未修改。

### 下一步
1. 使用者手機開啟新版 HTML，驗收三劇本條件顯示及排版。
2. 檢查多空條件檢查表 Bias、因子權重及缺失因子與 JSON 一致。
3. 手機視覺 PASS 後才結案；B 區 0.01 億元精度差仍列後續對帳。


## 38. 2026-11-03 手機驗收與 Bias 因子圖表語意修正
- 使用者提供手機實機截圖（v9-pro-20261102）。版面檢查：區塊 C 日夜盤劇本、三劇本卡片、多空圖表、相關性熱圖、交易計畫未見明顯重疊或裁切；截圖範圍未見橫向溢出。視覺初步 PASS。
- 三劇本顯示「機率未校準」屬正確狀態，不是條件未成立。實際區間情境：現價 44,920.14，PutWall 44,000，CallWall 48,000，區間條件成立；偏多因 Flip 缺值不成立，偏空因現價仍高於 PutWall 不成立。
- 截圖發現多空條件圖表實際把 u.weights（正規化因子權重）當成方向貢獻畫圖，並直接顯示 spot_trend、foreign_spot 等程式 key；全正綠色長條會造成全部偏多的錯誤印象。此為內容語意 FAIL，非單純視覺問題。
- 已修正 templates/v9-pro-react-template.html：改讀 factor_details 中 status=active 的 contribution，依絕對值排序顯示前 8 項；使用中文 name；正值綠色推升 Bias、負值紅色壓低 Bias；標題改為「多空因子方向貢獻」，清楚標示不是權重；缺失因子名稱也轉為中文。
- 新增測試 test_bias_chart_uses_signed_factor_contributions_and_chinese_names；第一次 CI 因測試 assertion 的反引號跳脫寫法錯誤而 FAIL，修正測試後通過，非產品程式錯誤。
- 最新 CI Run 41560578070（commit 0034eb9155857db2a869709b8b64b4e13a547586）整體 SUCCESS；React template tests 19/19 PASS；新因子圖表測試 PASS；inline JS 4 scripts PASS；Pages artifact upload PASS；deploy job SKIPPED（工作分支）。
- Artifact 13196638130 已下載抽查，正確檔案 p0/v9-pro-20261102.html。實際 HTML 包含新圖表程式；資料 date=2026-11-02、Bias=24 偏空、有效因子 14/17。前 8 方向貢獻：外資現貨 -7.1429、美股費半 -7.1429、夜盤 -4.7619、PCR -3.3333、現貨趨勢 -1.9345、投信 +1.7857、MACD -1.7857、Put Wall +0.8929。新圖表已正確混合呈現正負貢獻。
- 新手機複驗檔：/mnt/data/v9-pro-20261102-factor-contrib-fixed.html，303,829 bytes，SHA-256 d82b30b923d70538570163febf80764ca5fc57b91551786d8cee570cf430843d。此檔由 Run 41560578070 Artifact 的 p0/v9-pro-20261102.html 抽出。
- 狀態：手機原截圖排版初步 PASS；舊版因子語意 FAIL 已修正；新版 CI／HTML／注入資料 PASS；新版手機視覺 NOT TESTED。未 merge／部署，Master／V8 未修改。區塊 B 0.01 億元精度差仍未結案。

### 下一步
1. 使用者手機開啟 v9-pro-20261102-factor-contrib-fixed.html，確認圖表顯示中文因子名稱、紅綠正負方向貢獻，且 Bias 24 偏空不再搭配全正綠色權重圖。
2. 新版手機 PASS 後，回頭對帳區塊 B 0.01 億元精度差及完整來源／單位；之後再做全頁最終驗收。
3. 未經使用者明確授權不 merge／deploy。

 
## 39. 2026-11-03 因子方向貢獻圖空白根因修正
- 使用者實機驗收上一版 HTML：區塊標題、Bias 24 偏空及正負方向說明顯示正確，但因子圖繪圖區完全空白，手機驗收 FAIL。
- 根因已定位：綜合分析頁 y2({data:e}) 解構為 `options:l`、`analysis:u`，但新因子圖仍從 `l.factor_details` 讀取；該欄位實際位於 `u.factor_details`。因此 filter 得到空陣列，Canvas 只畫背景網格，沒有因子列。
- 已修正 `templates/v9-pro-react-template.html`：圖表 filter 改讀 `u.factor_details`；缺失因子中文名稱查找亦改讀 `u.factor_details`。不改變權重或 Bias 計算。
- 更新 `tests/test_react_template_static.py`：測試明確要求圖表資料來源為 `u.factor_details`，避免再次錯用 options 物件。
- 最新 CI Run 41561549286，commit c97b970dd29fc05664fbdb2b251b7f4ef6735f3e，整體 SUCCESS；新 HTML 產生成功，4 個 inline JS scripts 語法檢查 PASS，React template 靜態測試中的 test_bias_chart_uses_signed_factor_contributions_and_chinese_names PASS；Artifact 13196699558 上傳成功，Deploy job SKIPPED（工作分支）。
- 已從本次 CI Artifact 13196699558 抽取 `p0/v9-pro-20261102.html`，確認生成 HTML 圖表程式讀取 `u.factor_details`，不再讀取錯誤的 `l.factor_details`。注入資料中有 14 個 active 且 contribution 為有限數值的因子；按絕對值排序前 8 項為：外資現貨 -7.1429、美股費半 -7.1429、夜盤 -4.7619、PCR -3.3333、現貨趨勢 -1.9345、投信 +1.7857、MACD -1.7857、Put Wall +0.8929。
- 新版 HTML：`/mnt/data/v9-pro-20261102-factor-contrib-fixed-v2.html`，303,829 bytes，SHA-256 `0dc550e7a6adb19e324fa1ed7af7308605a614092c061d9beda8ce1dc886bf72`。
- 狀態：程式根因修正 PASS；CI PASS；Artifact 內實際 HTML 取值來源與注入因子資料核對 PASS；實際手機新版畫面 NOT TESTED；未 merge／正式部署；Master／V8 未修改。
 
### 下一步
1. 請使用者手機開啟 fixed-v2 HTML，確認 8 個因子長條、中文標籤、正負顏色及數值均出現，且不重疊。
2. 手機 PASS 後處理區塊 B 0.01 億元精度差，再進行完整 42 區塊最終驗收。
3. 未經使用者明確授權不 merge／deploy。

 
## 40. 2026-11-03 因子圖第 8 列被 Canvas 高度裁掉：修正與驗收
- 使用者手機實機回報截圖：新版因子圖可見 7 列，非預期 8 列；其他可見 UI（正負顏色、中文標籤、數值）正常。
- 根因定位於模板 `mf({items,height=160,...})`：每列高度 m=18、間距 k=12、起始 y=14；可畫列數 N=Math.min(items.length, Math.floor((height-14+12)/30))。當高度 240px 時 N=floor(238/30)=7，故第 8 個有效因子資料雖存在，未被 Canvas 繪製。
- 已將「多空因子方向貢獻」圖表高度從 240px 提高至 260px，保留 8 項排序及「顯示 8 項」說明；未改變因子計算、權重、Bias。
- 新增靜態測試，斷言該圖表高度維持 260px（目前繪圖列距條件下足以容納 8 列）。
- Template commit `cc9ca65bfef14f0908b8f44bdae803640ef5da83`；test commit `642fd0c4f14e27652c3b859ff48b5ca901368612`。
- CI Run 41562071919 SUCCESS；React template and three-scenario path contract tests PASS；`test_bias_chart_uses_signed_factor_contributions_and_chinese_names` PASS；inline JavaScript syntax PASS；Golden Fixture build PASS；GitHub Pages artifact 13197570937 uploaded; deploy job SKIPPED（工作分支）。
- 狀態：高度根因確認 PASS；程式修正 PASS；CI PASS；使用者上一版手機截圖只驗證 7 列可見，修正版 260px 的實際手機 8 列畫面 NOT TESTED；尚未 merge/deploy；區塊 B 精度差仍未結案；42 區塊總驗收未完成。
 
### 下一步
1. 從本次 CI Artifact 13197570937 取得新 HTML，確認輸出模板高度為 260px。
2. 交付新 HTML，請使用者手機確認 8 列均顯示（尤其 Put Wall +0.9）。
3. 通過後再處理區塊 B 精度差及 42 區塊完整驗收；未授權不 merge/deploy。

 
## 41. 2026-11-03 八列因子圖新版 Artifact 抽取完成
- 已下載 CI Run 41562071919 的 Artifact 13197570937，從 `p0/v9-pro-20261102.html` 抽取新版 HTML。
- 新檔：`/mnt/data/v9-pro-20261102-factor-chart-8rows-v3.html`，303,829 bytes；SHA-256 `a0cc47e5a566f272438d48fdcae03f5a4dfa837affdf29b54f9a3626e15e7bba`。
- 抽查實際 Artifact HTML：因子圖設定為 `height:260`，原 `height:240` 已不存在；確認新版 build 使用修正後 Template。
- 同一 Artifact 的 `p0/data-20261102.json` 核對：17 個 factor_details，其中 14 個 active 且 contribution 為有限數字。依絕對值排序前 8：外資現貨 -7.1429、美股費半 -7.1429、夜盤 -4.7619、PCR -3.3333、現貨趨勢 -1.9345、投信 +1.7857、MACD -1.7857、Put Wall +0.8929。新版 260px 高度依 mf 列高公式可容納 8 列。
- 下載 HTML 已可交使用者手機驗收；實際手機視覺仍 NOT TESTED。未 merge/deploy；B 區精度差與 42 區塊總驗收仍未完成。
 
### 下一步
1. 使用者手機開啟 `v9-pro-20261102-factor-chart-8rows-v3.html`，確認 8 列包含 Put Wall +0.9 全部可見、無重疊。
2. 通過後處理區塊 B 0.01 億元精度差，接著執行 42 區塊總驗收。
3. 未經授權不 merge/deploy。

 
## 42. 2026-11-03 因子圖 V3 手機實機驗收完成
- 使用者提供 V3 手機截圖；「多空因子方向貢獻」完整顯示 8 列：外資現貨 -7.1、美股費半 -7.1、夜盤 -4.8、PCR -3.3、現貨趨勢 -1.9、投信 +1.8、MACD -1.8、Put Wall +0.9。
- 第 8 列 Put Wall 已可見，無裁切；正負顏色、中文標籤、數值均正常。此項手機實機驗收 PASS，因子圖 8 列顯示問題正式結案。
- 此 PASS 僅限本張手機截圖與當前直向 viewport，不代表 42 區塊總驗收或其他裝置／橫向／瀏覽器驗收完成。
- 下一工作回到 B 區 0.01 億元精度差：日盤外資多方 11.36、空方 11.17、淨額 +0.18。顯示值相減為 +0.19，可能是各欄獨立四捨五入造成，但目前 artifact JSON 只有格式化字串，原始未四捨五入值尚未取得，不能先判定為單純 rounding。
- 先追溯 TAIFEX Proxy options-day-call-put 原始 long_amount / short_amount（千元）及金額彙總路徑，使用未格式化值重算：多方、空方、淨額各自獨立換算億元與四捨五入；核對淨額是否以原始多方－空方計算。若原始值可支持 +0.18，記錄為正常四捨五入差異並補充 UI 註記；若不能，修正資料計算鏈及測試。不得為了讓顯示相減相等而把淨額改成顯示值相減。
- 未 merge／部署；Master／V8 未修改；42 區塊總驗收未完成。


## 2026-11-03 工作快照：其他區塊解析文字動態化
- 使用者要求延續 A／B 區塊解析文字的處理方式，檢查其餘區塊解析是否能接受；不可只潤飾文字，必須由同一份當日 Dashboard data 推導，與圖表、價位、單位及缺值狀態一致。
- 工作分支 `fix/three-market-correlation-history`，HEAD `0a397dc3e2c4e13e1bdb5149c6e1a679e206a284`。修改 Template `templates/v9-pro-react-template.html` 及測試 `tests/test_react_template_static.py`。
- Template 新增 `v9ProSynthesisAnalysis()`，動態產生五組解析：C 日夜盤劇本、三劇本路徑、多空因子方向貢獻、相關性熱圖、交易計畫。內容包括日夜價格與外資流量同向／背離、三劇本價位條件狀態、正負因子貢獻加總與缺失因子、最強正負相關配對及相關不代表因果、交易計畫按有效關鍵位與價格確認而非只靠 Bias。
- 相關 commits：`bfafaec57521744d91e52a2dc49d87a2175350a1`、`57166c2b92a5baae030ced64eca43a321ed145dd`、`0b3f51959a7b93590ca178e5f8e2fd5bbca3e2a8`、`0a397dc3e2c4e13e1bdb5149c6e1a679e206a284`。
- 最新 CI Run `41563655940` 對應 HEAD `0a397dc...`，整體 SUCCESS；build job 的 React Template／三劇本契約、資料流程、歷史 DATA_REPORT correlation replay、Dashboard build、Golden Master 注入、Golden Fixture inline JavaScript 驗證及 Pages Artifact upload 均 SUCCESS。Deploy job SKIPPED，因工作分支未部署。
- 最新 CI 成功只代表自動化檢查通過；Artifact 五組解析實際注入值／最終 HTML 抽查與手機畫面驗收尚未執行，狀態 NOT TESTED。先前三次 CI failure 是中間 commits；最新 HEAD 的 CI 已成功。
- 未 merge／部署；Master／V8 未修改。Auditor 為單模型自我審查，非獨立多模型審核。

### 恢復後下一步
1. 抽查 Run `41563655940` Artifact，核對 Template ref、資料注入、五組解析與當日 JSON 一致；用實際資料及缺值／零值／反向 fixtures 驗證。
2. 修正發現的 schema 或推論錯誤，重跑 CI。
3. 交付最新 Artifact 給使用者手機驗收五組解析文字、圖表一致性、換行及重疊。
4. 通過後再進行 42 區塊全頁總驗收；B 區 0.01 億元精度差仍待原始值對帳。未經使用者明確授權不得 merge／deploy。


## 2026-11-03 Artifact 抽查與解析邊界修正（CI 待確認）
- 已下載 Run 41563655940 / Artifact 13197767563，解壓後確認驗收目標為 `p0/v9-pro-20261102.html` 與 `p0/data-20261102.json`；manifest 日期 20261102。HTML 內嵌 `window.DASHBOARD_DATA` 與獨立 JSON 完全相同；Artifact 來源 HEAD 為 `0a397dc3e2c4e13e1bdb5149c6e1a679e206a284`。
- 以 Artifact 真實 JSON 執行原版 `v9ProSynthesisAnalysis()`，五組實際解析與資料核對：日收 45,301、夜收 44,433、夜盤變化 -868 點、夜盤量占比 37.45%、外資夜盤 +1,365 口；現價 44,920.14 位於 PutWall 44,000／CallWall 48,000 之間；Bias 24、14/17 有效因子、淨貢獻 -26.04；相關矩陣 8×8，最強正相關 +0.85、負相關 -0.89；交易計畫為區間內不追價。
- Artifact 邊界情境檢查發現三個問題並已在工作分支修正：①夜盤低點／日收缺值時，舊解析仍輸出包含「缺值」的價位觸發句；②零值 PutWall 可能在敘述／交易計畫中被當成有效牆位，與 Pth() 的正值有效性規則不一致；③相關矩陣非方陣或係數超出 [-1,1] 時，舊邏輯仍可能宣稱 NxN 並讓圖表嘗試繪製。
- 已修改 `templates/v9-pro-react-template.html`：價格欄位以正值有效性判斷，零值流量／OI 仍保留為有效 0；缺少夜盤低點或日盤收盤時停止產生價位觸發句；情境位置、交易計畫與 Pth() 使用一致的有效價位規則；新增共用 `v9ProCorrelationMatrixReady()`，熱圖與解析文字共用方陣／有限值／[-1,1] 驗證。
- 已修改 `tests/test_react_template_static.py`：增加缺值、零值、錯誤相關矩陣及圖表／文字共用驗證條件。
- 修正 commits：Template `a0212f191a96a918c4e96e0eb0ff7b787a496cbc`；測試 `0e59d8cc4350137facdb6924300ad0f25c42928a`。兩檔已讀回 GitHub 工作分支確認新內容存在。
- **新修正版本 CI：NOT TESTED／BLOCKED**。目前可用 GitHub 連線只提供 PR-triggered workflow runs 查詢，不提供 push-triggered run 清單或 workflow dispatch；新 commit 的 combined status 回傳空 statuses，不能視為 PASS。不得用舊 Run 41563655940 代替新版本 CI 證據。
- 新修正版本 Artifact 與手機畫面：NOT TESTED。舊 Artifact 僅用於發現問題，不可交付作為修正版手機驗收。
- 未 merge／deploy；Master／V8 未修改。Auditor 為單模型自我審查，非獨立多模型審核。

### 下一步（唯一工作）
1. 先確認工作分支 HEAD `0e59d8cc4350137facdb6924300ad0f25c42928a` 是否已有新的 GitHub Actions run；若有，檢查完整 build job，必須 SUCCESS。
2. 若未觸發或無法查詢，需取得該 HEAD 對應的新 Run ID；不可用舊 Run 41563655940 代替。
3. 新 CI PASS 後下載新 Artifact，重新核對 HTML／JSON、五組解析及缺值／零值／反向情境；再交付手機驗收。
4. 手機 PASS 後才進入 42 區塊全頁驗收；B 區 0.01 億元精度差仍待原始值對帳。未經明確授權不 merge／deploy。


## 2026-11-03 反向夜盤情境文案修正（CI 待確認）
- 對五組解析進一步做反向情境稽核時，發現舊版 C 區 `cTarget` 固定使用偏空措辭；即使夜盤收盤高於日盤收盤，也會寫成「夜盤弱勢訊號延續」，與反向價格情境不一致。
- 已修正 Template：夜盤日收差為負時採偏弱確認條件；為正時改為守住日盤收盤、夜盤低點作第二層防守參考的偏強確認條件；價差接近零時採中性觀察；日收／夜收／夜低缺值或無效時不產生價位觸發句。
- 新增反向夜盤情境測試，檢查上漲情境不得出現偏空目標、下跌情境須輸出跌勢確認條件。
- 最新修正 commits：Template `a3a49002c31646b29906b970ac4c1170647636f0`；測試 `882227d153007c7429833c011f826dadd6b8cb99`。目前工作分支最新已知 commit：`882227d153007c7429833c011f826dadd6b8cb99`；Template／測試均已讀回確認。
- 新版 CI 仍無可查證 Run ID；最新 commit combined status 回傳空 statuses，且可用 workflow-run 查詢僅限 PR-triggered runs。故新修正版本 CI = NOT TESTED／BLOCKED，不能引用舊 Run 41563655940 作為修正後驗收證據。
- 新修正版本 Artifact、手機畫面 = NOT TESTED；未 merge／deploy；Master／V8 未修改。Auditor 為單模型自我審查，非獨立多模型審核。

### 下一步（唯一工作）
1. 取得最新 HEAD `882227d153007c7429833c011f826dadd6b8cb99` 對應的新 GitHub Actions Run ID，核對所有 build 步驟及新增加的缺值／零值／反向測試。
2. CI SUCCESS 後下載新 Artifact，重新核對五組解析、HTML 內嵌 JSON、圖表同源與 edge fixtures。
3. 再交付手機驗收；通過後進入 42 區塊全頁驗收。B 區 0.01 億元精度差仍待原始值對帳；未授權不 merge／deploy。


## 2026-11-03 最新工作續接：五組解析 Artifact 驗收完成，待手機驗收

### Git／CI 最新查證
- Repository：`grichtoyang/daily-premarket`。
- 工作分支：`fix/three-market-correlation-history`。
- 本次恢復時使用者提供 HEAD `0a397dc3e2c4e13e1bdb5149c6e1a679e206a284`；重新查詢 GitHub 後，實際分支 HEAD 已前進至 `6aa7ac665a5f47cbc6f1634d3e8988f26c848d58`。最新 commit 為 `test(v9): assert synthesis reverse scenario consistency`，只擴充反向價位情境測試。
- 最新 CI Run `41564828844`，HEAD `6aa7ac665a5f47cbc6f1634d3e8988f26c848d58`，completed／success。Build job 所有步驟 SUCCESS；Pages artifact upload SUCCESS；deploy job SKIPPED（工作分支）。
- Artifact：`13197918949`（github-pages，1,806,890 bytes，SHA-256 digest `5005dad2f050397a00ac903d2b2972eb9089d8b6fa784bba4728e3497ea9545c`）。

### Artifact／實際 JSON 驗收
- 已下載並解壓最新 Artifact；驗收目標確認為 `p0/v9-pro-20261102.html`、`p0/data-20261102.json`，manifest 日期 `20261102`。
- HTML 內嵌 `window.DASHBOARD_DATA` 與獨立 JSON 完全相同；HTML SHA-256 `c0104af557a855d9ddf8b024c7166a0d17d225208ad62c867f5b281ab4b24f29`。
- 五組解析以最新 Artifact 實際 JSON 執行：日夜盤日收 45,301、夜收 44,433、差 -868 點、夜盤量占比 37.45%、外資夜盤 +1,365 口、OI 0 口；現價 44,920.14 位於 Put Wall 44,000／Call Wall 48,000 之間，區間成立，偏多／偏空路徑因必要價位缺失或條件不符而不成立；Bias 24、有效因子 14/17、正向 +2.6786、負向 -28.7203、淨貢獻 -26.0417；相關矩陣 8×8，最強正相關 +0.854、最強負相關 -0.8892；交易計畫為區間內不追價。
- 實際 Artifact 的 `v9ProSynthesisAnalysis()` 與 `Pth()` 已在 Node runtime 執行；缺值、零值、夜盤上漲／下跌反向、非方陣相關矩陣、係數超出 [-1,1]、反向價位情境測試全部 PASS。
- 圖表與解析資料來源已核對：夜盤摘要使用 tx.day／tx.night／futures；三劇本 Pth 與解析使用同一現價及 Put／Call／Gamma／Flip；因子圖與摘要使用同一 factor_details；相關性熱圖與摘要共用矩陣有效性檢查；交易計畫圖與文字使用同一現價及關鍵位。
- 已抽取最新手機驗收 HTML：`/mnt/data/v9-pro-20261102-synthesis-verified.html`，313,917 bytes；SHA-256 同上。

### 狀態與限制
- 最新 HEAD CI：PASS。
- Artifact 路徑／manifest／HTML 與 JSON 一致：PASS。
- 五組解析實際值／圖表資料來源一致性：PASS（依實際 JSON 與 Artifact 程式執行核對）。
- 缺值／零值／反向／錯誤相關矩陣 runtime cases：PASS。
- 手機實際畫面：NOT TESTED，必須由使用者開啟上述 HTML 驗收；CI PASS 不可替代手機驗收。
- B 區 0.01 億元精度差：NOT TESTED，仍需回查 TAIFEX Proxy 原始未格式化 long_amount／short_amount。
- 42 個區塊全頁驗收：NOT STARTED。
- 未 Merge／Deploy；Master／V8 未修改。Auditor 為單模型自我審查，非獨立多模型審核。

### 下一個唯一工作
1. 使用者手機開啟 `v9-pro-20261102-synthesis-verified.html`，驗收五組解析的文字可讀性、換行、重疊、裁切及圖表同源一致性。
2. 手機 PASS 後，依 Recovery 原定順序處理 B 區 0.01 億元原始精度對帳，再進入 42 區塊全頁驗收。
3. 未經使用者明確授權不得 Merge／Deploy；不得修改 Master／V8。


## 2026-11-03 手機截圖審查與 C 區成交量單位修正

### 使用者提供的手機截圖審查
- 五個區塊均未見明顯卡片重疊、文字互相覆蓋或區塊裁切；三劇本價位、因子方向、相關性矩陣及交易計畫主要內容可辨識。
- 手機截圖視覺檢查：版面初步 PASS；較長解析文字與熱圖小字仍有可讀性改善空間。
- 發現 C 區右側日夜成交量圖將 73,987／44,305 口縮放為 74.0／44.3，但圖表未標示縮放單位；chartNote 卻僅寫成交量單位為「口」，容易誤讀。

### 修正與最新 CI
- 僅修改 `templates/v9-pro-react-template.html`：右側日量／夜量圖增加 `extra:"千口"`；說明同步標示「右側圖表以千口顯示」。保留原始數據卡的精確口數，不改計算值。
- 修正 Commit：`ca4fe9d1a044f802182e10f74b3fdac45251c9c5`。
- CI Run：`41566032790`，HEAD 與修正 Commit 相同，completed／success；Build PASS，Artifact upload PASS，Deploy SKIPPED（工作分支）。
- Artifact ID：`13199196057`，github-pages，1,807,051 bytes，digest `fdfed15d248f2f900da5e68de4288f5a4cfefe1b7a42a4c40b20846cb126e488`。
- 最新 Artifact 重新抽查：`p0/v9-pro-20261102.html`、`p0/data-20261102.json`、manifest date `20261102`；HTML 內嵌 DASHBOARD_DATA 與獨立 JSON 完全相同。
- 修正後 HTML SHA-256：`2aca4c218351d1c0759d2099bea0087e9e6e5ed83daf29403881950ccfd0cea1`。
- 已輸出手機重新驗收檔：`/mnt/data/v9-pro-20261102-synthesis-unitfix.html`，313,992 bytes。

### 驗收狀態
- 原使用者截圖版面：未見重疊／裁切，視覺初步 PASS。
- C 區成交量單位問題：程式修正 PASS，最新 Artifact 含「千口」標示。
- 最新修正 Artifact／HTML-JSON 一致：PASS。
- 最新修正版本手機重新截圖：NOT TESTED；仍需確認「74.0 千口／44.3 千口」不造成手機畫面擠壓或重疊，故整體手機驗收尚未結案。
- B 區 0.01 億元原始精度對帳：NOT TESTED。
- 42 區塊總驗收：NOT STARTED。
- 未 Merge／Deploy；Master／V8 未修改。Auditor 為單模型自我審查，非獨立多模型審核。

### 下一步
1. 使用者在手機開啟 `v9-pro-20261102-synthesis-unitfix.html`，確認 C 區成交量顯示「74.0 千口／44.3 千口」可讀且沒有重疊；五區塊版面重新確認。
2. 手機確認通過後，查 B 區 0.01 億元差異的 TAIFEX Proxy 原始未格式化金額。
3. 再開始 42 區塊完整驗收。不得 Merge／Deploy，除非使用者另行明確授權。


## 2026-11-03 主動五區塊數據稽核、MaxPain 分類修正與新版 Artifact

### 使用者截圖及資料版本釐清
- 使用者最新手機截圖確認 C 區日量／夜量顯示 `74.0 千口`／`44.3 千口`，原始數據卡仍為 73,987／44,305 口；可見範圍沒有因單位標籤造成重疊。五區塊版面可見範圍初步 PASS，整體手機驗收仍待最新版完整複驗。
- 曾發現 GitHub 根目錄 `dashboards/data-20261102.json` 為 Bias 25、active 12/17、相關性樣本不足；該檔不是此次驗收的 P0 Artifact 資料。已下載正確 CI Artifact 並確認 `p0/data-20261102.json` 才是手機截圖對應資料：Bias 24、active 14/17、8×8 correlation，樣本 5/5（最近 60 筆）。兩者不可混用；後續所有 P0 驗收以同一 Run 的 `p0/v9-pro-20261102.html` + `p0/data-20261102.json` + manifest 為準。
- 正確 P0 JSON 核對：現貨 44,920.14；日盤收 45,301、夜盤收 44,433、差 -868 點；日／夜成交量 73,987／44,305 口，夜盤占比 37.45%；外資夜盤淨交易 +1,365 口、外資期貨 OI 0 口；Put Wall 44,000、Call Wall 48,000、MaxPain 44,400、Gamma Wall／Flip 缺值。
- 因子 14/17；正向合計 +2.6786、負向合計 -28.7203、淨貢獻 -26.0417；Bias 24（50 中性基準，計算後四捨五入）。相關矩陣 8×8，最強正相關 +0.854（顯示 +0.85），最強負相關 -0.9053（顯示 -0.91）；不可將其他歷史截圖的 -0.89 數字沿用至本版。
- HTML 內嵌 DASHBOARD_DATA 與同一 P0 Artifact 獨立 JSON 完全相同。

### 主動發現並修正的邏輯分類缺陷
- 原交易計畫表將 Put Wall 與 MaxPain 一起列在「支撐」欄；但旁邊說明明確規定 MaxPain 僅作磁吸參考，不當作跌破後下跌目標。這會使使用者把 MaxPain 誤讀成實際支撐，屬於圖表／文字分類不一致。
- Template 已最小修改：支撐列只顯示 Put Wall；MaxPain 獨立列為「磁吸參考」。未更改數值、策略條件或其他區塊。
- 新增測試 `test_trade_plan_keeps_max_pain_separate_from_support`，防止 MaxPain 再被列為支撐。
- Template commit：`e923f2dde34b011407263a4831b2e58a363bb354`；測試 commit：`d335c755644840f61e7ca7f386900126f5cd17da`。

### 新版 CI／Artifact 驗證
- 工作分支：`fix/three-market-correlation-history`；最新 HEAD：`d335c755644840f61e7ca7f386900126f5cd17da`。
- CI Run：`41566885386`，HEAD 精確相符，completed／success。Build 所有步驟 PASS；React template／three-scenario contract test step PASS；Artifact upload PASS；deploy job SKIPPED（未部署）。
- Artifact ID：`13199517282`，github-pages，1,807,081 bytes，digest `ddc9e03e52f44bf0c669dc93d6108c307f2a966c390aae68f130a705b0b86aab`。
- 新 Artifact P0 HTML：314,009 bytes；SHA-256 `a0ceeb82731a98c33947cc5c9ed7e911dd977dd6869228f4c536e3842f7a066c`。P0 JSON 62,774 bytes；SHA-256 `aaf5cc488a2d86f7abadbe3c9ed0ab05417863ba726c6bcf30dde2caed25a980`。
- 已從實際 Artifact 解壓並驗證：manifest date 20261102；內嵌 JSON 與 `p0/data-20261102.json` 完全一致；新 HTML 包含「千口」單位與「磁吸參考」獨立列，不再包含舊的 Put Wall／MaxPain 合併支撐列。
- 已輸出新版手機驗收檔：`/mnt/data/v9-pro-20261102-maxpain-fix.html`，314,009 bytes。

### 五區塊主動稽核結果
- C 日夜盤劇本：價格／流量背離描述與 -868 點、+1,365 口一致；量能占比 37.45% 計算正確；零 OI 明確顯示 0 口；價位確認條件使用日盤收盤及夜盤低點。數據／邏輯 PASS。
- 三劇本：現價 44,920.14 位於 Put Wall 44,000 與 Call Wall 48,000 之間，區間條件成立；Gamma Flip 缺值使偏多條件不成立；偏空條件不成立。數據／邏輯 PASS。
- 多空因子：14/17、正負合計及淨貢獻一致；Bias 24 與 50 中性基準及 -26.0417 淨貢獻一致；圖表只顯示貢獻絕對值較大的 8 項，其他有效因子仍納入 Bias。PASS。
- 相關性：8×8、樣本 5/5；最大正負配對及四捨五入顯示與矩陣一致（+0.85／-0.91）；說明限制為歷史共變、不作因果／預測。PASS。
- 交易計畫：區間內不追價；Put Wall 作下方參考、Call Wall 作上方壓力，MaxPain 已獨立標為磁吸參考。新分類修正已進 Artifact；程式／CI PASS。

### 狀態
- 最新 CI／Build／Artifact upload：PASS。
- P0 Artifact／JSON 一致：PASS。
- 五組資料計算與圖表來源核對：PASS（以 Run 41566885386 的 P0 Artifact 為準）。
- MaxPain 支撐分類缺陷：已修正，測試／CI PASS。
- 最新版本手機驗收：NOT TESTED（需使用者開啟新檔，檢查新增列是否影響手機排版及五區塊可讀性）。
- B 區 0.01 億元原始精度對帳：NOT TESTED。
- 42 區塊全頁驗收：NOT STARTED。
- 未 Merge／Deploy；Master／V8 未修改。Auditor 為單模型自我審查，非獨立多模型審核。

### 下一步
1. 使用者手機開啟 `v9-pro-20261102-maxpain-fix.html`，重驗五區塊，尤其交易計畫表新增「磁吸參考」列的可讀性、換行、重疊及裁切。
2. 手機 PASS 後，追查 B 區 0.01 億元差異的 TAIFEX Proxy 原始未格式化 long_amount／short_amount。
3. 完成 B 區對帳後，開始 42 區塊全頁驗收。未經明確授權不得 Merge／Deploy；不得修改 Master／V8。


## 2026-11-03 最新手機截圖複驗（MaxPain 修正版）
- 使用者已提供手機實際瀏覽器截圖，對象為 `v9-pro-20261102-maxpain-fix.html`。
- 截圖可見範圍：C 區日夜盤劇本、三劇本路徑、多空因子、相關性熱圖、交易計畫。可見卡片未見互相重疊、圖表與文字覆蓋或單位標籤碰撞；C 區日量／夜量顯示 +74.0／+44.3 千口，原始數字卡為 73,987／44,305 口。
- 交易計畫可辨識 Call Wall 48,000、現價 44,920、MaxPain 44,400、Put Wall 44,000；MaxPain 已獨立於 Put Wall 支撐呈現，分類修正手機截圖確認 PASS。
- 可見範圍的結構排版檢查 PASS；但手機目前仍以雙欄縮放呈現，文字偏小，影響閱讀效率，記為可讀性改善項目。交易計畫下方內容在截圖底部未完整顯示，且未取得完整向下捲動截圖，因此完整手機全頁驗收仍為 PARTIAL／NOT COMPLETE，不得宣稱全部手機驗收完成。
- 待辦：評估是否需要獨立手機單欄／字級改善（不得擅自擴大本次修正範圍）；另須取得交易計畫下半部及頁面底部的手機截圖，確認沒有裁切、溢出或重疊。B 區 0.01 億元精度差仍待查；42 區塊總驗收尚未開始。


## 2026-11-03 五區塊手機驗收結案與 B 區精度對帳

### 五區塊手機實機驗收
- 使用者追加手機向下捲動截圖，補足交易計畫下半部及 C 區分析／判斷／操作文字。與前一張手機截圖合併覆蓋五個目標區塊的完整內容。
- C 區、三劇本路徑、多空因子（8 項）、相關性熱圖、交易計畫均可辨識；未發現卡片重疊、文字覆蓋、裁切、價位／單位碰撞。交易計畫支撐 44,000、磁吸參考 MaxPain 44,400、壓力 48,000 分列正確。
- 五區塊手機實機驗收：PASS／結案（限使用者提供的手機直向截圖與該五區塊；不代表其他裝置／橫向或 42 區塊驗收）。手機雙欄縮放文字偏小列為可讀性改善項目，不阻擋本次結構驗收。

### B 區 0.01 億元精度差原始值對帳
- 對帳日期：2026-11-02。來源為 TAIFEX 官方「選擇權買賣權分計－依日期」頁面（https://www.taifex.com.tw/cht/3/callsAndPutsDate），頁面日期 2026/11/02，契約金額單位千元；官方定義為每筆權利金 × 契約乘數 × 交易口數後加總。
- 臺指選擇權外資原始值：Call 買方 479,793；Call 賣方 466,820；Put 買方 650,588；Put 賣方 655,894（均為千元）。
- 依現有方向分類：多方＝買 Call＋賣 Put＝1,135,687 千元＝11.35687 億元→11.36；空方＝賣 Call＋買 Put＝1,117,408 千元＝11.17408 億元→11.17；淨額＝原始多方－原始空方＝18,279 千元＝0.18279 億元→+0.18。
- 因多方、空方、淨額各自從未四捨五入原始金額換算億元後獨立四捨五入至小數二位，顯示 11.36－11.17＝0.19 與淨額顯示 +0.18 相差 0.01 億元，屬正常獨立四捨五入，不是資料或計算錯誤。不可用已顯示值相減覆寫原始精度淨額。
- 源碼路徑已核對：`src/sources/taifex.py` 以千元／1e5 換算億元；`scripts/v9_pro_builder.py` 依 Call／Put 分類並以未四捨五入分項差計算淨額；模板表格以兩位小數顯示。原始官方表格與專案方向分類公式一致。

### UI 透明度補充與 CI
- 為避免使用者將獨立四捨五入誤認為算術錯誤，已在 B 區七欄表格備註加入說明：各欄由原始千元金額獨立換算並四捨五入至小數二位，顯示多方減空方可能與淨額相差 0.01 億元；淨額以未四捨五入原始值計算。
- Template commit：`ac75f9ba1d1bc4c48f8c8c7ec5b56b3516733df6`。
- 靜態測試新增對上述說明文字的斷言，test commit／最新工作 HEAD：`e678877bc076e157c948483d40f136e0f504303e`。
- CI Run `41568199233`（template commit）及 `41568208858`（含測試 commit）已觸發；截至本次記錄查詢時仍執行中／pending，尚不可宣稱 PASS。需確認最新 HEAD 對應 Run `41568208858` 最終結果與 Artifact。

### 狀態與下一步
- 五區塊手機實機驗收：PASS／結案。
- B 區 0.01 億元原始精度對帳：PASS；根因為獨立四捨五入。
- B 區 UI 說明文字與靜態回歸測試：已提交，CI PENDING。
- 最新 template 變更的 CI／Artifact／手機新增說明文字檢查：PENDING／NOT TESTED。
- 42 區塊完整總驗收：NOT STARTED。
- 未 Merge／Deploy；V8／Master 未修改。Auditor 為單模型自我審查，非獨立多模型審核。
- 下一步：等待並檢查 Run `41568208858`；若 PASS，抽查新 Artifact 的 B 區備註及 JSON 不變性，再交付使用者手機確認備註可讀性。通過後進入 42 區塊總驗收。


## 2026-11-03 B 區精度說明 CI／Artifact 驗收
- 最新工作 HEAD：`e678877bc076e157c948483d40f136e0f504303e`。
- 最新 CI Run：`41568208858`，completed／success，HEAD 精確相符。Build job PASS；React template／scenario contract tests PASS（含新增獨立四捨五入說明斷言）；option force analysis contract tests PASS；Artifact upload PASS；deploy job SKIPPED；Commit generated dashboard history SKIPPED（沒有需要提交的生成歷史變更）。
- 測試 log 明確顯示 `test_option_force_table_normalizes_amounts_and_signed_net_values ... ok`，React template 測試共 21 tests，OK；其他工作流測試亦均 OK。
- Artifact ID：`13200545155`，size 1,807,354 bytes，digest `c80d9596a33f77d8f87d9997f50238dcdf5e0cad93ec2725546d2409b8b3f654`。
- 已下載並解壓 Artifact；P0 HTML `p0/v9-pro-20261102.html` 314,159 bytes，SHA-256 `d98eec6560462a21d63d4df03f8d3bdf950b2442a0d8f1f8de6190b37af28839`；P0 JSON `p0/data-20261102.json` 62,774 bytes，SHA-256 `aaf5cc488a2d86f7abadbe3c9ed0ab05417863ba726c6bcf30dde2caed25a980`（與先前 P0 JSON SHA 相同，資料未被 UI 說明修正改動）。
- 實際 Artifact HTML 已確認含獨立四捨五入說明；HTML 內嵌 DASHBOARD_DATA 與外部 P0 JSON 完全相同。新手機驗收檔：`/mnt/data/v9-pro-20261102-rounding-note.html`，314,159 bytes。
- 狀態：B 區原始金額精度對帳 PASS；備註程式／靜態測試／CI／Artifact PASS；最新備註手機可讀性 NOT TESTED。五區塊先前版本手機結構驗收 PASS，但因 B 區新增說明文字，最新 Artifact 的 B 區備註仍需手機複驗。42 區塊總驗收 NOT STARTED。
- 未 Merge／Deploy；Master／V8 未修改。Auditor 為單模型自我審查，非獨立多模型審核。
- 下一步：使用者手機開啟最新 `v9-pro-20261102-rounding-note.html`，檢查 B 區新增備註字級、換行、裁切及是否與圖表／表格重疊。通過後開始 42 區塊完整總驗收。


## 2026-11-03 B 區說明手機驗收 PASS／42 區塊稽核啟動
- 使用者提供三張手機截圖，涵蓋 B 區精度說明、C 區夜盤劇本、三劇本路徑、多空因子方向貢獻、相關性熱圖及交易計畫。
- B 區新增四捨五入說明已在手機畫面完整呈現；無截斷、重疊、遮蓋或異常擠壓。字體偏小但放大可辨識，列為可讀性改善項，不阻斷驗收。
- B 區最新 Artifact 的新增說明手機可讀性：PASS。五個目標區塊的手機直向版面／文字圖表無重疊、裁切及單位碰撞：PASS。
- B 區原始值對帳、UI 備註、CI Run 41568208858、Artifact 13200545155 均維持 PASS；部署 job SKIPPED，未部署。
- 五區塊驗收僅代表本輪指定五區，不等同 42 區塊全 Dashboard 驗收。42 區塊總驗收自本日開始列為 IN PROGRESS；尚未完成逐區塊資料鏈稽核，不得宣稱全頁 PASS。
- 下一步：以最新 P0 Artifact／對應 DATA_REPORT 為固定 T0，建立 42 區塊清單，逐項追蹤原始來源 → DATA_REPORT → Builder／JSON → 圖表 → 分析／判斷／操作；每區標示 PASS／FAIL／BLOCKED／NOT TESTED，發現缺陷先定位再最小修正並回歸測試。
- 未 Merge／Deploy；Master／V8 未修改。Auditor 為單模型自我審查，非獨立多模型審核。


## 2026-11-03 42 區塊稽核：T0 基準固定與盤點差異待釐清
- 工作分支唯讀查證：`fix/three-market-correlation-history` HEAD `e678877bc076e157c948483d40f136e0f504303e`；Recovery 文件分支 HEAD `77de89fe1834fd72c44f61ca1eadd0d7e2d3fda5`。
- CI Run `41568208858` 已重新查證為 completed / success，head_sha 與工作分支 HEAD 完全相符；Artifact `13200545155` 已重新下載，確認 ZIP 內含 `p0/data-20261102.json`（62,774 bytes，SHA-256 `aaf5cc488a2d86f7abadbe3c9ed0ab05417863ba726c6bcf30dde2caed25a980`）及 `p0/v9-pro-20261102.html`（314,159 bytes，SHA-256 `d98eec6560462a21d63d4df03f8d3bdf950b2442a0d8f1f8de6190b37af28839`）。此 Artifact 是本輪 42 區塊稽核的 UI／資料固定基準。
- 同一分支的程式基準：React template SHA `513ecee347f8df931196b46dd7a0f798902fc576`；Builder SHA `c4e49dfcf047cb86bd1592bf2ffdeb3e6121581f`；T0 DATA_REPORT `data_reports/DATA_REPORT_20261102.md` SHA `8ccd0dfc0f86f80e23253781bf923a533566df96`。
- **重要防錯：**工作分支根目錄 `dashboards/data-20261102.json` SHA `9e2c50907535d6f070a353eca50722d8c5e98aa1`，不是此次 P0 Artifact 的 JSON（SHA `aaf5cc...`）。不得拿根目錄 JSON 代替 Artifact P0 JSON 做畫面／數值驗收；所有後續稽核需固定讀取 Artifact 的 `p0/data-20261102.json`。
- 初步盤點發現 Artifact JSON 的 `analysis.cards` 有 48 個解析卡片鍵；目前 template 靜態掃描找到 34 個主要卡片元件呼叫點，另有 8 個 KPI 格。此數量不直接等於使用者確認的 42 個可見區塊（動態 map／隱藏／跨頁渲染仍待核對），不得直接把 48 個解析鍵當成 48 個 UI 區塊，也不得只憑 34 個靜態呼叫點結案。
- 42 區塊總稽核：IN PROGRESS；目前只完成 T0／Artifact／程式基準固定及初步盤點差異辨識，尚未逐區塊驗證資料鏈。不得宣稱全頁資料或解析 PASS。
- 下一步：以實際四頁 React render tree 對照使用者確認的 42 個可見區塊，建立唯一 42 項清單；每項再核對來源欄位、DATA_REPORT、Builder 計算、Artifact JSON、圖表／表格與分析／判斷／操作文字。先完成清單與資料鏈映射，再逐項測試缺值、零值、反向及單位邊界。


## 2026-11-03 42 區塊清單對映完成（修正前一筆頁數判讀）
- 重新以固定 Artifact `13200545155` 的實際 HTML React render tree 逐頁切分檢查；確認此版本不是四頁，而是 **六頁**：總覽、現貨、重要市場、期貨、選擇權、綜合分析。這與工作分支 Builder 的版頭規格「6頁結構」一致。前一筆「四頁」是舊上下文沿用錯誤，已在本筆更正；不應為了符合舊描述而刪併頁面。
- 六頁可見卡片清單（34 張）逐頁計數：總覽 5、現貨 6、重要市場 2、期貨 6、選擇權 8、綜合分析 7，合計 34。
- 總覽另有 8 格 KPI：加權收盤、外資現貨、台指日盤、台指夜盤、外資期貨、PCR、Call Wall、Bias。故可見區塊總數為 34 張卡片 + 8 格 KPI = **42**；與 Artifact JSON `analysis.visible_block_count=42` 及 Builder 明確設定 `visible_block_count: 42` 一致。
- Artifact JSON 的 `analysis.cards` 48 個鍵及 `cards_41_count`／`analysis_card_count` 是內部 AI 解析卡片／敘述卡片數，不是 UI 可見區塊數；Builder 原始碼註解明確標示這是 legacy alias，不能拿 48 取代 42。
- 本次完成的是 42 個可見區塊的**結構盤點與計數對帳**，不是 42 項資料鏈品質驗收。結構對映：PASS；逐項 source → DATA_REPORT → Builder → JSON → chart/table → analysis/judgment/action：仍 IN PROGRESS。
- 此次僅修正 Recovery／Progress 的頁數與區塊數判讀，未修改 Builder、Template、DATA_REPORT、Artifact 或 Dashboard UI；未 Merge／Deploy，Master／V8 未修改。
- 下一步依六頁 42 項清單逐一進行資料鏈核驗；先從總覽 8 KPI 與現貨頁 6 區塊開始，保留已 PASS 區塊不動，只在有原始證據的缺陷上提出最小修正。


## 2026-11-03 首輪 KPI 資料鏈核驗：期貨 OI 零值被 Bias 因子誤納（確認缺陷，暫不改碼）
- 以 Artifact `13200545155` P0 JSON、T0 `DATA_REPORT_20261102.md`、Builder `c4e49dfcf047cb86bd1592bf2ffdeb3e6121581f` 交叉核對總覽 8 KPI。
- 六個直接資料 KPI 對帳 PASS：加權收盤 44,920.14 點、外資現貨 -1,124.7 億、台指期日盤收 45,301 點、夜盤收 44,433 點、OI PCR 0.57、Call Wall 48,000 點；均與 DATA_REPORT／P0 JSON 對應欄位一致。
- 外資期貨淨 OI 0 口：原始 DATA_REPORT 及 JSON 都是 0，但同一份資料中三法人 OI 全為 0，Builder 的 `classify_futures_oi()` 已明確判定「三法人淨 OI 全為 0，視為可疑快照，不納入方向判斷」。因此此值不可當成已驗證有效的真實持倉數字；UI／KPI 仍顯示 0 口，屬需修正的狀態傳遞／標示問題。
- 已確認的邏輯矛盾：`build_41_cards()` 產生的「三法人 OI 可疑、不納入方向判斷」文字存在；但 `V9Analyzer._evaluate_factors()` 仍直接將 `futures.foreign_oi=0` 當作有效值，建立 `foreign_fut` active factor（score 0、base weight 8），且 `calculate_weights()` 將它納入有效權重正規化。P0 JSON 亦顯示此因子 status=active、effective_weight=9.52381；factor_quality confidence=high、bias_reliable=true。
- 影響量化（只做離線反事實試算，未修改任何檔案）：依 P0 JSON 既有 adaptive weights，若排除可疑 foreign_fut 因子並重新正規化其餘有效權重，Bias 約由 24 降至 21（未重新跑全套 optimizer，屬影響估算，不是修正後正式值）；base weight coverage 約由 85.6% 降至 77.9%，品質等級會由 high 降為 medium。故目前 Bias 24 的程式重現性可確認，但因納入可疑 OI 因子，Bias 的可靠度標示與方向解讀 FAIL。
- 狀態：總覽六個直接行情／籌碼 KPI 映射 PASS；期貨 OI 值有效性／狀態傳遞 FAIL；Bias 現行輸出可重現 PASS、其輸入有效性與 confidence 標示 FAIL。此為一個已定位的根因群，不拆成多個重複修正任務。
- 保護措施：本輪只讀查證與 Recovery／Progress 記錄，沒有修改 Builder、Template、DATA_REPORT、JSON、Artifact、Dashboard；沒有 Merge／Deploy。已通過的 B 區精度、五區手機版面與 42 區塊結構對映全部凍結。
- 後續處置：先完成 42 區塊其餘資料鏈清查，彙整缺陷後再一次提出最小修正方案；修正時須讓「全零可疑 OI」狀態同步影響 KPI 顯示、Bias 因子 active/disabled、權重覆蓋率／confidence、相關分析文字，並加回歸測試，禁止只改單一文案。


## 2026-11-03 現貨頁 6 區塊首輪資料鏈稽核：3 組確認缺陷（只記錄、不改碼）
- 稽核依固定 T0 DATA_REPORT `2026-11-02`、Artifact P0 JSON 與實際 React component source；本次只讀，未改程式。
- 現貨 A「大盤行情」：DATA_REPORT 明確標示 open/high/low unavailable；P0 JSON 對應為 null。但 React 分析文字直接執行 `n.open>n.close`、`n.close>n.open`、`n.high-Math.max(...)`、`Math.min(...)-n.low`，未先檢查 OHLC 是否完整，會把 null 強制轉成 0，產生「開低走高／收盤高於開盤」及不合理影線／實體數字；Candlestick `Pt` 亦直接用 null 計算座標範圍。狀態 FAIL（缺值被當成數值運算）。
- 現貨 B「漲跌家數」：上市家數 518／447／116 與 DATA_REPORT 一致；上櫃欄位 null。Canvas `u2` 對上櫃任一欄位缺值會明確顯示 unavailable，分析 compass 亦在上市漲跌家數缺失時停判。此區目前可見缺值防護 PASS（上櫃缺值未被補成 0）。
- 現貨 C「三大法人現貨」：外資 -1,124.7 億、投信 +236.2 億、自營 -513.7 億、合計 -1,402.2 億與 DATA_REPORT 對帳一致；此組數值與方向敘述 PASS。
- 現貨 D「融資融券」：融資餘額／增減及維持率 null，UI 表格與 Canvas `i2` 有 unavailable 防護；融券 197,359 張、借券餘額 2,525,241 張有值。缺值防護目前 PASS；維持率未取得不得當作 0%。
- 現貨 E「借券／券」：借券賣出餘額與增減為 null，表格有顯示 unavailable；但共用 Lollipop Canvas `Ol` 將 `Number(null)||0`，故圖表會把借券賣出畫成 0，而不是 unavailable。狀態 FAIL（表格與圖表語意不一致）。
- 現貨 F「成交結構」：上櫃成交金額 DATA_REPORT／JSON 為 unavailable／null，但 Lollipop Canvas `Ol` 會把 null 畫成 0；表格字串插值可能顯示 `null億`。更重要的是 `turnover.total=7,588.8` 等於上市金額，卻仍標為「上市櫃成交金額合計」，因上櫃值缺失而不是完整總額。Builder 的 consistency check 僅在上市與上櫃皆非 null 時才檢查合計，因此本案例被跳過。狀態 FAIL（缺值顯示與總額完整性兩個問題，根因屬同一欄位缺值未向下游正確傳遞）。
- 本輪現貨頁狀態：A FAIL、B PASS、C PASS、D PASS、E FAIL、F FAIL。此為資料鏈與 UI 缺值處理稽核，不是手機版面驗收；未因本次發現而修改任何既有 PASS 區塊。
- 後續修正原則（尚未執行）：A 僅在 OHLC 完整時才畫 K 棒並計算開高低、影線及實體；否則明確顯示 OHLC unavailable 並取消方向判讀。E/F 圖表通用 renderer 必須保留 null 與 0 的區別；F 的上市櫃總額只有在兩市場皆有有效數據時才可標示完整合計，否則標示部分／不可計算並同步處理 DATA_REPORT、JSON、圖表、表格與解析文字。需加 regression tests 覆蓋 null 與真 0。
- 未 Merge／Deploy；Master／V8、Builder、Template、DATA_REPORT、Artifact 均未修改。既有 PASS（B、C、D）凍結保留。


## 2026-11-03 42 區塊計數方法再校正（以實際渲染邏輯計數）
- 補充更正上一筆的計數拆法：不能把 34 個靜態元件呼叫點 + 8 個 KPI tile 當成 42，因為這忽略了總覽的 Bias 卡、KPI 群組計數方式，以及重要市場頁的動態 map 展開。
- 以使用者「一個邏輯分析區塊／一個卡片群組」為單位，實際 42 區塊分頁對映為：總覽 7（KPI 八格合併計 1 個 KPI 區塊、Bias 盤前偏向 1、五張側欄卡 5）；現貨 6；重要市場 8（美股指數、亞洲指數、美股期貨、美債殖利率、主要匯率、台灣 ADR、原油黃金 Bitcoin、重大新聞）；期貨 6；選擇權 8；綜合分析 7。合計 42。
- 重要市場頁在 React render 中由 map 產生 7 張市場卡，另加重大新聞 1 張；不可把 map 呼叫點只算成一張。總覽的 KPI 八個 tile 按邏輯群組計為一個區塊，Bias 卡另計一個。
- 以上六頁 7+6+8+6+8+7=42，與 Builder `visible_block_count=42`、Artifact JSON 相符，也符合使用者確認的 42 區塊口徑。上一筆「總覽 5+8 KPI、重要市場 2」的計數方法已作廢，不可引用。
- 此為 42 區塊結構映射 PASS；不代表每個區塊資料鏈已 PASS。程式仍未修改。


## 2026-11-03 重要市場頁 8 區塊首輪資料鏈稽核
- 固定 T0 DATA_REPORT／P0 JSON 對帳：美股指數 6 項、亞洲指數 5 項、美股期貨 4 項、美債殖利率 3 項、主要匯率 4 項、台灣 ADR 3 項、商品 3 項及重大新聞 12 則，所有本次列出的市場數值均可在 DATA_REPORT 與 JSON 的 `markets`／`marketPct`／`news` 找到對應，未發現本輪逐項對帳差異。數值映射 PASS。
- 美債欄位需保留不同來源註記：2Y 來自 Treasury yield.xml 網頁備援；10Y／30Y 來自 Yahoo Finance 備援。UI 顯示殖利率水準（%）與日變化（pp），單位標示目前一致；不可將 pp 誤標為 %。
- UI 分析文字接線問題：React `h2()` 對每個市場卡在 map 內建立空物件 `i={}`，後續 `compass:i[o.key]?.compass||"連動觀察"`、`target:i[o.key]?.target||"等待資料與價格確認"` 因空物件而全部落入泛用 fallback。雖然 P0 JSON 的 `analysis.cards` 已包含「美股指數／亞洲指數／美股期貨／美債殖利率／匯率／商品」各自的 compass／target，畫面未接入這些內容。七個市場子卡的方向判讀／下一步觀察未使用已產生的專屬解析，狀態 FAIL（分析輸出未接線；不是數值來源錯誤）。
- 市場子卡的 look 目前由 UI 依 markets 數值動態組成，避免直接輸出 JSON 內部分卡片的原始 Python list；此呈現方式保留，不因本次發現而改動。
- 重大新聞卡目前顯示 12 則標題／摘要／時間，資料數量與 T0 DATA_REPORT 相符；分析／判斷／操作為來源可信度與價格反應的通用提醒，暫不列為數據缺陷。
- 重要市場頁狀態：7 組市場數值映射 PASS；7 張市場卡專屬 compass／target 接線 FAIL；重大新聞資料呈現 PASS。尚未完成新聞逐則品質／時間戳稽核。
- 僅唯讀查證並更新 Recovery／Progress，未改動 Template／Builder／JSON／DATA_REPORT／Artifact；未 Merge／Deploy。後續修正待全部 42 區塊稽核完成後統一處理。


## 2026-11-03 期貨頁 6 區塊首輪資料鏈稽核
- 台指期日盤：開高低收 45,410／45,597／44,908／45,301，成交量 73,987 口、漲跌 -2.72%、基差 +380.86 點；DATA_REPORT 與 P0 JSON 對帳一致，圖表 OHLC 欄位有效，PASS。
- 台指期夜盤：開高低收 45,395／45,420／44,052／44,433，成交量 44,305 口、漲跌 -1.91%、夜盤相對日盤收盤變化 -868 點；資料值對帳 PASS，但 UI 把 `n.night.change` 傳入共用 Candlestick `Pt` 的 `basis` 參數，該元件固定將其標成「基差」，故夜盤圖上會把 -868 點錯標為基差。狀態 FAIL（圖表標籤語意錯誤）；表格的「夜盤變化」欄位定義正確。
- 期現貨價差：基差 +380.86 點、正價差 0.85%、夜盤變化 -868 點；圖表將夜盤變化除以 10，並在 chartNote 說明需乘 10 還原，表格保留原值；目前縮放與定義說明一致，PASS。
- 法人 OI：外資／投信／自營淨 OI 均為 0，前十大 +11,622；來源數值與 DATA_REPORT 一致，但三法人全零已由 Builder 自身分類為可疑快照。畫面仍將三法人 0 口當作一般 OI，未把可疑狀態同步至圖表／表格；0 值色彩也被指定為紅色（>=0），可能被誤讀為偏多。狀態 FAIL（沿用 OI 狀態傳遞缺陷群）。
- 日夜法人交易：外資日盤 +2,801、夜盤 +1,365；投信日盤 -72、夜盤 0；自營商日盤 -457、夜盤 +246；三大合計日盤 +2,272、夜盤 +1,611。與 DATA_REPORT 一致；UI 圖表與表格分列 OI 存量及日夜淨交易流量，單位口數，方法註記區分統計口徑，數值呈現 PASS；但 OI 可疑狀態仍未顯示，納入 OI 狀態缺陷群。
- 夜盤劇本：夜盤量占比 44,305／(73,987+44,305)=37.45%，夜盤收盤低於日盤 868 點，外資夜盤淨交易 +1,365 口；計算與來源一致。UI 文案明確表示不預設續漲機率、需現貨開盤確認，PASS。
- 期貨頁 6 區塊狀態：日盤 PASS；夜盤 FAIL（圖表標籤錯）；期現價差 PASS；法人 OI FAIL（可疑狀態未傳遞）；日夜法人交易 PASS（數值與口徑分離正確，但 OI 警示缺失，併入同一 OI 缺陷群）；夜盤劇本 PASS。
- 未修改 Template／Builder／DATA_REPORT／JSON／Artifact；已 PASS 區塊凍結；未 Merge／Deploy。修正待全頁稽核完成後統一進行。


## 2026-11-03 選擇權頁 8 區塊首輪資料鏈稽核
- PCR／成交量結構：Call Vol 140,350、Put Vol 135,722、Call OI 61,578、Put OI 34,887、OI PCR 0.57 與 DATA_REPORT／P0 JSON 對帳一致；成交量占比圖與 PCR 分開標示，PASS。
- 主要 OI 集中：Call／Put Top4 合併傳入同一 `Ct` 圖表，但呼叫固定 `type:"call"`；`Ct` 依 type 對整條曲線統一套 Call 紅色，故 Put OI 點也以 Call 色彩呈現，無法在圖上區分 Call 與 Put。表格標籤仍有 Call／Put 區分。狀態 FAIL（混合資料集被單一側別著色）。
- Call OI Top10、Put OI Top10：各 10 筆履約價／OI 與 DATA_REPORT／JSON 對應；標籤與單位點／口一致，PASS。
- Call Wall／Put Wall／Gamma Wall／Flip／MaxPain：Call Wall 48,000、Put Wall 44,000、MaxPain 44,400 與來源一致；Gamma Wall／Flip 為 null，UI 表格與標題顯示 unavailable，圖表不繪製缺值價位，缺值防護 PASS。
- 選擇權法人交易：四列法人日盤／夜盤淨口數與 DATA_REPORT 一致；圖表過濾非有限值，表格呈現原值，PASS。
- 前十大選擇權：買權／賣權多空 OI 與變化數值對應 DATA_REPORT；以標籤保留多空類型，未將淨 OI 變化當作單日流量，PASS。
- 履約價 GEX 分布：gexStatus unavailable、gexLevels 空陣列、Net/Gross GEX null；標題與表格顯示 unavailable，不以 0 代替，資料缺值傳遞 PASS；Canvas 無資料時目前呈現空白座標區，缺少圖內 unavailable 提示，列為非阻斷可讀性改善（不列數值錯誤）。
- 選擇權法人力道 B 區精度說明與前次獨立驗收一致，保留原始精度算法及手機 PASS，不再改動。
- 選擇權頁狀態：6 個區塊資料／缺值映射 PASS；主要 OI 集中圖側別顏色 FAIL；GEX 空圖提示為非阻斷改善。沒有修改程式／資料／Artifact；未 Merge／Deploy。


## 2026-11-03 綜合分析頁 7 區塊首輪資料鏈稽核
- 區塊 A 三市場法人：現貨、期貨日夜盤交易流量、選擇權日夜盤淨口數分欄呈現；敘述明確指出三市場方向分歧，並警告三法人 OI 全零為可疑快照、不納入方向判斷。內容口徑正確；但 OI 圖／數值仍顯示 0，納入既有 OI 狀態傳遞缺陷群。
- 區塊 B 選擇權法人多空力道：原始千元換算、日夜盤、淨額及多空雙邊分類與前次已核對；獨立四捨五入說明及手機版面 PASS，凍結不動。
- 區塊 C 日夜盤劇本：日盤收 45,301、夜盤收 44,433、相對變化 -868、夜盤量占比 37.45%、外資夜盤淨交易 +1,365；價格走弱與外資流量偏多的背離判讀合理，操作條件要求現貨開盤價格確認，PASS。
- 三劇本路徑：現價 44,920.14 位於 Put Wall 44,000 與 Call Wall 48,000 之間；Flip／Gamma 缺值時不成立偏多確認，偏空條件亦未成立；以區間觀察、不追價呈現，PASS。
- 多空因子方向貢獻：正負貢獻加總及 Bias 24 與 P0 JSON 對應；但因 `foreign_fut=0` 可疑因子仍 active，且 confidence=high，圖表／文字把錯誤有效因子集合當成可信來源。狀態 FAIL，併入 OI 狀態傳遞缺陷群。
- 相關性熱圖：SQLite 中 T0 2026-11-02 的 `foreign_fut=0` 被 `save_today_to_db()` 的 `correlation_eligible` 條件接受（目前只檢查非 null／有限數字，沒有排除可疑全零 OI）；故 8×8 Pearson 矩陣以 5 筆樣本計算，包含該可疑列。獨立重算「大盤漲跌幅 vs 外資期貨」係數：含 T0 可疑列 n=5 時 r=0.0146；排除 T0 後 n=4 時 r=0.9590，但低於 min_samples=5，應不顯示矩陣。數值對比證明可疑零值大幅扭曲相關性；狀態 FAIL（無效樣本進入歷史資料及熱圖）。另 JSON `analysis.cards[相關性熱圖]` 說未計算，但 `analysis.correlation` 有矩陣，屬內部敘述卡與實際矩陣狀態不一致，需一併清理。
- 交易計畫：現價 44,920、Bias 24 偏空、Put Wall 44,000 支撐、MaxPain 44,400 磁吸參考、Call Wall 48,000 壓力；Gamma／Flip 缺值以 unavailable 呈現，圖表與表格沒有把 MaxPain 誤作跌破目標；PASS。
- 綜合分析頁狀態：A 口徑敘述 PASS（OI 數值顯示沿用缺陷）；B PASS；C PASS；三劇本 PASS；因子貢獻 FAIL（OI 因子）；相關性 FAIL（可疑樣本污染）；交易計畫 PASS。手機版面先前驗收 PASS，不因資料邏輯問題重做版面。
- 本輪只讀及 Recovery／Progress 記錄，沒有修改程式、SQLite、JSON、Template 或 Artifact；未 Merge／Deploy。所有已 PASS 區塊凍結。


## 2026-11-03 總覽頁 7 區塊首輪資料鏈稽核
- KPI 群組：加權 44,920.14／-0.65%、外資現貨 -1,124.7 億、TX 日盤 45,301、夜盤 44,433、PCR 0.57、Call Wall 48,000、Bias 24 均與對應 P0 JSON／DATA_REPORT 欄位一致；外資期貨 OI 0 口仍屬可疑快照，顯示需沿用 OI 狀態傳遞 FAIL，不可當成有效部位。
- Bias 盤前偏向：Bias 24、偏空、Put Wall 44,000 與 JSON 一致；但該分數由 active foreign_fut 零值因子參與權重正規化，confidence=high 失真，沿用 OI／Bias 缺陷群 FAIL。
- 加權 5 日走勢＋關鍵水位：5 日序列 10/27–11/02 為 46,096／47,036／46,368／45,212／44,920，T0 收盤 44,920.14；歷史來源標示 technical_history=yahoo（T0 filtered），圖表以 5 日序列呈現；levels 僅有 Put Wall 44,000，未虛構其他水位。資料映射 PASS；外部 Yahoo 歷史序列原始 API 本輪未獨立重抓，來源原始回應 NOT TESTED。
- 三大法人快照：外資 -1,124.7、投信 +236.2、自營 -513.7、合計 -1,402.2 億與 DATA_REPORT／JSON 一致，PASS。
- 期選結構快照：PCR 0.57、Net GEX unavailable、關鍵價位依有效值顯示；Gamma Wall／Flip／GEX 缺值未補 0，PASS。
- 美股連動：SOX -7.20%、VIX 19.42 點等值與重要市場資料對應；美股數值映射 PASS。
- 重大新聞：12 則，首則標示 UTC 05:53:37Z／台北 13:53:37，時區換算 +8 小時正確；數量與 DATA_REPORT 對應 PASS。其餘 11 則逐則來源／內容品質未逐項查證，NOT TESTED。
- 總覽頁狀態：5 日圖／法人快照／期選快照／美股連動／新聞資料映射 PASS（來源原始回應及其餘新聞品質仍有 NOT TESTED）；KPI 與 Bias 卡因可疑 OI 因子狀態未傳遞 FAIL。Bias 8 格已合併視為一個 KPI 群組區塊，維持 42 區塊計數口徑。
- 本輪唯讀；沒有修改程式／資料／UI／Artifact；未 Merge／Deploy。


## 2026-11-03 已定位缺值／可疑值缺陷的上游根因與安全修正邊界（尚未改碼）
- 期貨 OI 上游解析：`workers/taifex-proxy_V1.4.js` 的通用 `number()` 對空字串、`-`、`--` 回傳 0；`parseFuturesInstitutionalOI()` 對 OI 欄位直接呼叫此函式，且只以三法人列數是否足夠判定 `found`，沒有驗證 OI 欄位本身是否有效。這可把來源缺值轉成 0。**原始 2026-11-02 TAIFEX HTML 欄位本身本輪未成功取得，故「該日三法人 0 是否由 dash 轉成 0」仍 NOT TESTED；已確認的是 parser 具有此風險路徑。**
- 安全邊界：不可直接改通用 `number()`，它被其他 TAIFEX endpoint 共用，空值／dash 在交易量等欄位可能具有不同語意。修正應限定在 OI parser，使用保留真數字 0、但將空白／dash 轉為 null 的 OI 專用 nullable parser，並檢查完整性。
- OI 狀態下游：需以三法人 OI 快照狀態同步控制外資期貨 Bias 因子 active/disabled、factor coverage／confidence、KPI／期貨 OI 卡片及 correlation eligibility。不能只在文字上加警告。
- 歷史 DB：P0 SQLite 已把 2026-11-02 的 OI=0 列存為 `correlation_eligible=1`；`save_today_to_db()` 遇到已存在 T0 會直接 skip，不會自動重寫。修正後若要排除該列，需以明確、限縮到該 T0 的 eligibility 修正／重建步驟處理，不能只改 eligibility 計算函式就宣稱歷史矩陣已修復。
- 成交金額合計上游：`src/sources/spot.py` 的通用 `_add(a,b)` 設計為一邊缺值時回傳另一邊，並同時用於融券／借券等跨市場可用部分加總；因此不可全域改寫 `_add`。成交結構目前 `total=_add(listed_yi,otc_turnover_yi)`，造成 OTC null 時 total 仍等於上市值。安全修正應只對 turnover total 採嚴格完整性規則（兩市場皆有效才計算完整合計），並同步 DATA_REPORT、Builder、JSON、圖表／表格。
- UI null 處理：`Ol` 將 `Number(null)||0`，應保留 null 與真 0 的區別；`Pt` 在 OHLC 缺值時仍執行座標與影線計算，應在缺值時停止 K 棒及相關分析計算。修正需增加 null 與真 0 的獨立回歸案例。
- 其餘精確修正點：夜盤 `Pt` 的圖表參數標籤應可指定為「夜盤變化」而非沿用「基差」；重要市場 h2() 的 `i={}` 空物件造成七張市場卡不讀 JSON 專屬 compass／target；Call+Put 合併 OI 圖不可全套 Call 紅色，須保留 Call／Put 側別。
- 以上是已確認的程式風險／缺陷定位與修正邊界，不代表修正已執行。當前工作分支程式碼維持原樣；未 Merge／Deploy；V8／Master 未修改。


## 2026-11-03 daily-data 手動觸發日期準則（強制）

- 手動觸發 GitHub Actions 的 `daily-data` workflow 時，`T0 交易日期（t0）` 輸入欄必須留空；**不得直接填入當日日期**。
- 留空後由 `src/fetch_data.py` 呼叫 `src.t0.resolve()`，自動判定 T0 與盤別（日盤／全日），避免手動指定 T0 使程式走入「手動 T0 預設全日」分支，造成資料日期／夜盤查詢節次不符合預期。
- `report_date`（報告產出日期）與 `t0`（交易資料日期）是不同參數。不得因為要產出當日報告，就把當日日期填入 `t0`。
- 排定班別 workflow 若有明確 `slot`／`date` 參數，依該 workflow 的排程契約執行；本規則針對一般手動觸發 `daily-data`，不可混用排程班別參數。
- 若需要指定歷史 T0 進行重抓／回補，必須先確認目標盤別及夜盤查詢日，再使用明確的受控回補流程；不得把一般手動觸發的留空規則自行改成填日期。
- 驗證 11/02 等報告的夜盤缺失時，先查 workflow dispatch 輸入與執行紀錄；若當次手動輸入了 T0 日期，應先視為可能的操作／參數原因，不得直接判定資料源或程式退化。
- 比對資料完整性時，以已確認的完整全日版 DATA_REPORT（目前指定 2026-10-30）作為基準。未確認目標報告是日盤版或全日版前，不得把其缺欄位直接列為資料遺失。

**程式依據（已讀取工作分支原始碼）：** `src/fetch_data.py` 的 CLI 說明指出手動 `--t0` 未指定 `--session` 時預設「全日」；未指定 `--t0` 時呼叫 `src.t0.resolve()` 自動判斷。全日夜盤查詢使用 T0 的下一個交易日。這確認了參數分支差異；但 2026-11-02 當次 dispatch 是否真的填入日期，仍須以該次 workflow run 的實際輸入／紀錄查證，不能僅憑報告缺夜盤推定。


## 2026-11-03 1030／1102 DATA_REPORT 實檔與 Actions 執行紀錄複核（新增證據）

### 已確認的報告版本
- `phase2-p0-ui-fixes` 分支的 `data_reports/DATA_REPORT_20261030.md`：blob SHA `665ae0ce957cbda372a1d70e1f06f0eea124ba11`；T0=2026-10-30、全日版。期貨日盤／夜盤、三大法人 OI、前十大 OI、日夜盤法人交易均有值。
- `phase2-p0-ui-fixes` 分支的 `data_reports/DATA_REPORT_20261102.md`：blob SHA `4add0443546bde87309fc1f13396f3a478e60bb0`；產出時間 2026-11-03 08:55:11、T0=2026-11-02、全日版。期貨日盤／夜盤、三大法人 OI、前十大 OI、日夜盤法人交易均有值；例如 TX 夜盤收盤 44,310、外資 OI 淨額 -89,379、三法人 OI 淨額 +1,067。
- `master` 分支的 `data_reports/DATA_REPORT_20261102.md`：blob SHA `38fc2e8a5fe2578e6779ffc11e157fed3e76a8ee`；產出時間 2026-11-03 12:32:18、T0=2026-11-02、全日版，夜盤及 OI 同樣有值。
- 舊工作分支 `fix/three-market-correlation-history` 的 `DATA_REPORT_20261102.md`：blob SHA `8ccd0dfc0f86f80e23253781bf923a533566df96`；產出時間 2026-11-02 14:35:26、盤別為日盤。該版三法人 OI 全零，且期貨行情數值與 10/30 報告相同；不得拿這份日盤版與 11/03 早上／中午的全日版當成同一資料版本比較。
- 因此，**目前可讀取的 10/30 全日版與 11/02 全日版都沒有缺少夜盤／OI**。異常集中在 11/02 14:35 的舊日盤版及 OI 零值狀態；尚不能把它描述成目前 master／phase2-p0-ui-fixes 的全日 DATA_REPORT 遺失。

### Actions 執行輸入已查證
- Run #97：`41556173914`，分支 `phase2-p0-ui-fixes`，event=`workflow_dispatch`，2026-11-03 08:54（台北）。Job log 明確顯示 `SCHED=''`、命令 `--t0 ""`，程式輸出 `slot` 未指定、T0=2026-11-02、session=全日，產生上述 08:55 全日版。
- Run #98：`41578655028`，分支 `master`，event=`schedule`，2026-11-03 12:31（台北）。Job log 顯示 morning slot，T0=2026-11-02、session=全日，產生上述 12:32 全日版；run success。
- 這兩次執行均不能代表 2026-11-02 14:35 的舊日盤版當次輸入；該次 run 的 dispatch input／完整 log 仍需另找歷史 run #95 證據。不可將 #97 的空白輸入反推為 #95 的輸入。

### 仍待處理的根因與界線
- Worker 的通用 `number()` 將空字串、`-`、`--` 轉為 0；`parseFuturesInstitutionalOI()` 對 OI 欄位直接呼叫該函式。這是已確認的程式風險，但 2026-11-02 14:35 當時原始 TAIFEX HTML 未取得，故不能宣稱已證實當次 0 一定由 dash 轉換造成。
- 最小安全修正仍限定在 OI parser：採 OI 專用 nullable parser（保留真實數字 0；空白／dash → null），並讓 parser 完整性狀態能被 Python／DATA_REPORT 下游辨識；不可改通用 `number()`。
- 下游 Bias、confidence／coverage、KPI／OI 卡、correlation eligibility 及已污染的 2026-11-02 SQLite row，仍按本文件前述修正邊界處理。修正及回歸測試尚未執行。
- 本次只讀 GitHub 文件、分支報告與 Actions logs；沒有修改程式、資料庫、報告或 Dashboard；沒有 Merge／Deploy。



## 2026-11-03 最新中斷恢復點：GEX Worker V1.5 診斷修改

> 本節為目前 GEX Worker 診斷工作的最新狀態；早期章節中的下一步如與本節衝突，以本節為準。

### 工作位置
- Repository：`grichtoyang/daily-premarket`
- 程式分支：`phase2-p0-ui-fixes`
- Recovery 文件分支：`ops/recovery-handoff`
- 修改範圍僅三檔：
  1. `workers/taifex-proxy_V1.4.js`（程式版本升為 V1.5；檔名保留既有 V1.4 路徑）
  2. `src/sources/taifex.py`
  3. `tests/test_taifex_gamma_fallback.py`

### 已讀回確認的程式內容
- Worker blob：`3f5fdfe3442a106aa21a74706e911f7970258056`。
- Python blob：`aebb590370105937c0ad86506c7e8f66d9b8118c`。
- Tests blob：`ff7f83c0a1081f27781eb3dbf2ae08da840e8c08`。
- Worker GEX endpoint 已加入 `error_code`／`stage`／`detail` 診斷欄位，區分 Chain fetch／parse、Delta fetch、共同到期月份配對、TAIEX underlying 及 GEX internal error。
- Python `_get()` 已解析 Worker JSON error payload，保存 HTTP status、error code、stage、error、detail／data.reason；GEX endpoint unavailable 時將摘要加入 DATA_REPORT notes。
- 測試檔已加入 HTTP 502 與 HTTP 200 + `ok=false` 診斷資訊保留測試。
- 保留 P0 fixes 的 T0 日期檢查、GEX unavailable 語意及既有 GEX 計算公式；不以 Gamma Wall／Flip proxy 假造 GEX。

### 驗收狀態
| 項目 | 狀態 |
|---|---|
| 三個遠端程式檔案讀回及診斷修改存在 | PASS |
| Worker V1.5 程式測試 | NOT TESTED |
| Python GEX fallback 測試 | NOT TESTED |
| DATA_REPORT notes 真實輸出驗證 | NOT TESTED |
| Worker 部署 | NOT DONE |
| master／V8／原始 P0 分支未被本次修改 | 本次未操作 |
| Merge／Rebase | NOT DONE |

### 已知背景與限制
- 2026-11-03 的 daily-data run `41621794469` 成功產生 T0=2026-10-30 報告，但 `options-gamma-levels` 連續兩次 HTTP 502，`options-market-structure-compact` 備援 read timeout；報告中的舊 GEX 值是沿用前版，不代表本輪成功重新取得。
- 原始 P0 與 P0 fixes 使用相同 Worker blob，但 Python 呼叫端版本不同；原始 P0 也曾出現 GEX endpoint 502。
- Worker route 已知依賴 TXO Chain、TXO Delta、TWSE FMTQIK TAIEX close；FMTQIK 沒有第二資料源備援。此次新增診斷的目的在於下次能識別實際失敗階段，不代表已修復上游 502／timeout 根因。
- 本輪尚未測試新 Worker 是否能在真實 Cloudflare 執行環境回傳預期 JSON，也未部署。

### 下一個唯一工作
先做三檔 diff／程式審查，確認 Worker response schema 與 Python parser 完全吻合，並檢查測試可執行；修正後執行測試。測試 PASS 後再另行部署 Worker，並用實際 endpoint 驗證 GEX error diagnostics 能進入 DATA_REPORT。不得先部署再測，也不得擴大修改到其他模組。



## 2026-11-03 GEX Worker V1.5 CI 審查結果追加

### 最新 Git／CI 證據
- `phase2-p0-ui-fixes` 最新 HEAD：`e852ee6d8eaab4225b563b2b856ce1f76ad7cb41`；此為 GitHub Actions 產生的 Dashboard history commit，並非 Worker deploy。
- V1.5 三檔 blob SHA：Worker `3f5fdfe3442a106aa21a74706e911f7970258056`；Python `aebb590370105937c0ad86506c7e8f66d9b8118c`；Tests `ff7f83c0a1081f27781eb3dbf2ae08da840e8c08`。
- 首輪 Run `41626557631` FAIL：新增測試檔的多行 `with` 語法有多餘反斜線，導致 SyntaxError。Commit `82796f958b3cedd62e077e11a59ac4cd680e5c06` 已改成巢狀 context manager。
- 修正後 Run `41626627855` SUCCESS；`test_taifex_gamma_fallback.py` 執行 11 tests，全部 OK；Deploy job SKIPPED。該 run 的一般 V9 build、資料注入及 artifact upload 成功，但不等同 Worker 已部署。

### 程式審查補充
- Worker 的 `parseTXOOptionChain()` 失敗回傳只有 `found/data`，沒有 `reason`；Chain parse failure 會使用固定 detail fallback。分類可辨識，但 parser 本身沒有更細的錯誤原因。
- Worker 回應的 `error_code`／`stage`／`detail` 與 Python `_worker_error_payload()` 的讀取欄位相符；GEX calculation failure 亦會由 `data.reason` 保留原因。
- Python notes 的診斷摘要在 `build()` 回傳的 `notes` 陣列中；尚未用真實 Worker error response 跑完整 DATA_REPORT 產生流程驗證。

### 狀態更新
| 項目 | 狀態 |
|---|---|
| Python GEX fallback regression（11 tests） | PASS |
| 修正新增測試語法錯誤 | PASS |
| Worker JavaScript runtime／Wrangler validation | NOT TESTED |
| 真實 GEX endpoint 診斷回應 | NOT TESTED |
| DATA_REPORT notes 實際輸出 | NOT TESTED |
| Worker deploy | NOT DONE |
| Pages deploy | 本次 Deploy job SKIPPED |

### 下一個唯一工作
先完成 Worker JavaScript 語法／部署前驗證；若通過，再部署 Worker。部署後使用受控 GEX endpoint 呼叫，確認 Worker 的 stage／error_code 能被 Python 解析並寫入 DATA_REPORT notes。不可把 Python 測試成功當作 Worker runtime 或部署成功。



## 2026-11-03 Worker V1.5 source-level audit checkpoint

### Source review
- Re-read the Worker route, Python `_get()`, `build()` and regression tests on `phase2-p0-ui-fixes`.
- Worker diagnostic stages and Python parser keys are aligned: `error_code`, `stage`, `error`, `detail`, and `data.reason`.
- Python resets `_LAST_FETCH_ERRORS` at `build()` start; when the T0 Gamma endpoint is unavailable it appends the diagnostic summary to returned `notes`.
- P0 T0-date guard and GEX unavailable handling remain in place.
- Source-level review only: **PASS**.

### Syntax/runtime check
- Local `node --check` could not be run because the environment cannot resolve `raw.githubusercontent.com` to retrieve the exact repository file.
- GitHub connector provides read-only fetch and no workflow-dispatch action; repository listing showed no Wrangler config or Worker-specific syntax-validation workflow.
- **Worker JavaScript syntax/runtime validation: BLOCKED** (not executed; no PASS claim).
- Real Worker endpoint and DATA_REPORT notes integration: **NOT TESTED**.
- Worker deployment: **NOT DONE**.
- No source files changed in this checkpoint.

### Next action
Use an execution environment with the repository checked out and Node/Wrangler available to run syntax validation against the exact Worker file. Only after that passes should deployment be considered. Do not treat source review or Python regression tests as Worker runtime validation.


## 2026-11-03 Worker V1.5 語法驗證途徑複核（本輪）

### 既有 CI 能力盤點
- .github/workflows/daily_data.yml：執行 Python daily-data fetch，沒有 Node／Worker syntax check。
- .github/workflows/unit-contract-audit.yml：Python compileall 與 Python unittest，沒有 Worker syntax check。
- .github/workflows/test-v9-ui-fixes.yml：雖安裝 Acorn／使用 Node 相關工具，但檢查對象是 React template；workflow paths 亦未包含 workers/taifex-proxy_V1.4.js，不能據此認定 Worker 已通過語法檢查。
- 目前授權範圍只允許三個既定程式檔案；本輪不新增／修改 workflow 以擴大範圍。

### 工具限制與狀態
- 目前 GitHub connector 僅提供讀取／檔案更新等動作，沒有 workflow_dispatch 或遠端 shell 執行能力。
- 本地環境無法解析 raw.githubusercontent.com，不能下載 exact Worker source，因此無法在本地對該檔執行 node --check。
- Worker JavaScript syntax/runtime validation：**BLOCKED（未執行）**。
- 真實 Worker endpoint 與 DATA_REPORT notes 整合：**NOT TESTED**。
- Worker deployment：**NOT DONE**。
- 本輪只讀 workflow 清單及內容；沒有修改任何程式、workflow、設定或部署。

### 下一步（唯一）
在可 checkout phase2-p0-ui-fixes 並有 Node.js 的環境，對 exact file workers/taifex-proxy_V1.4.js 執行 node --check。通過後才進行 Wrangler／部署前驗證；未通過前不得部署。


## 2026-11-03 Worker V1.5 V8 語法解析補充驗證

### 驗證方法與結果
- 透過 GitHub connector 讀取 `phase2-p0-ui-fixes` 的 `workers/taifex-proxy_V1.4.js` exact source，blob SHA：`3f5fdfe3442a106aa21a74706e911f7970258056`；長度 132,720 characters。
- source 只有一個 `export default`，沒有 static import。使用 V8 parser 對完整 source 進行語法解析；僅在記憶體副本將唯一 `export default` 改寫成等價的 `const __worker_default__ =`，以符合 script parser 入口。原始檔未修改。
- V8 syntax parse：**PASS**。這是完整 source 的 V8 語法解析結果，但不得等同宣稱 `node --check`、ES module 原生檢查或 Cloudflare Workers runtime 已通過。

### 仍未完成的驗證
- 本地 Node.js 22.16.0 存在，但無法從 raw.githubusercontent.com 下載 exact source（DNS resolution failure），故 `node --check`：**BLOCKED／NOT EXECUTED**。
- Wrangler／Cloudflare Workers runtime：**NOT TESTED**。
- 真實 Worker endpoint 與 Python DATA_REPORT notes 整合：**NOT TESTED**。
- Worker deploy：**NOT DONE**。
- 本輪沒有修改任何程式、workflow、Worker 設定或部署。

### 下一步
在不部署的前提下，若可取得 Wrangler／Cloudflare 相容 runtime，先執行 Worker bundle／runtime validation；其後才可安排受控部署與 endpoint 整合驗證。不得把 V8 syntax parse PASS 當作 runtime PASS。


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


## 2026-11-03 最新中斷恢復點：歷史 DATA_REPORT 日期混用

> 本節是目前最新工作中斷點，優先於前面 GEX Worker V1.5 的「下一個唯一工作」。GEX Worker V1.5 的程式版本與部署狀態仍按前文保留；目前工作焦點已切回 DATA_REPORT 日期一致性。

### 目標與範圍
- Repository：`grichtoyang/daily-premarket`
- 程式分支：`phase2-p0-ui-fixes`
- Recovery 文件分支：`ops/recovery-handoff`
- 目標 T0：2026-10-30。
- 問題：2026-11-03 21:26 手動重跑後，歷史報告混入非 T0 快照，部分欄位 unavailable，部分欄位沿用舊報告。
- 不碰 master、V8、原始 P0 分支；未經批准不修改程式、不 commit 程式、不 deploy、不 merge、不重跑 workflow。

### 最新報告與比較證據
- 新報告：`data_reports/DATA_REPORT_20261030.md`，phase2-p0-ui-fixes blob SHA `61b5a8799bec62762a60d5efb3f1099c18084fc5`；報告產出時間 2026-11-03 21:26:27；workflow Run `41644283168`，Job `125945406903`。
- 舊報告：fix/three-market-correlation-history blob SHA `665ae0ce957cbda372a1d70e1f06f0eea124ba11`；產出時間 2026-11-01 23:51:51。
- 新報告註記：50 格沿用前版有值；73 格以本次新抓取覆蓋。兩者是不同計數，不能合併解讀成報告完整重建。
- 新舊報告逐欄比對已見到三大法人、台指期日盤、日盤法人等新值與舊報告不同，但新值日期未被一致證明為 T0；部分夜盤欄位因日期檢核而 unavailable；GEX／Gamma Wall／Gamma Flip 仍有 10/30 值。
- 新報告借券欄位：借券餘額 2,525,111 張（TWT96U + GRETAI，無日期欄最新快照）；借券賣出餘額 36,178 張、增減 -1,273 張均沿用前版，原來源註記 TWT93U + TPEX margin_sbl。舊報告借券餘額為 4,651,514 張。

### 已確認的程式根因

1. **歷史日期隔離不一致**
   - TAIFEX 的部分無日期端點回傳最新快照；目前程式有些欄位只加 note 仍採用最新資料，有些夜盤欄位則會因日期不符拒絕。
   - TWSE 三大法人日期不符時只新增 note，仍採用最新可得資料。
   - TWT96U 無日期欄，程式直接使用最新快照。
   - 這會使同一份歷史 T0 報告混合 T0 原始值、較新快照、沿用舊值及 unavailable。
   - 狀態：程式行為已定位 **PASS**；逐一修正及回歸測試尚未做。

2. **同 T0 protect 判斷漏查 DATA_REPORT**
   - `src/fetch_data.py` 的 `main()` 在輸出檔已存在時，使用 `reports/Daily_REPORT_{T0}_*.md` 判斷 `has_report`。
   - 沒有將 `data_reports/DATA_REPORT_{T0}.md` 本身納入判斷。
   - 因此同 T0 DATA_REPORT 已存在，但 reports 目錄沒有符合檔案時，會被錯誤判為 `protect=False`，進入「同 T0 覆蓋模式」。
   - `merge_same_t0()` 已讀取確認：protect=True 時新舊不同實值傾向沿用舊值；新值 unavailable 時可回填舊值；protect=False 時新舊不同實值保留本次新值並計入 overwritten；缺值回填仍會發生。50 格 filled 與 73 格 overwritten 是不同計數。
   - 狀態：程式缺陷已定位 **PASS**；修正及測試尚未做。

3. **TWSE TWT93U 日期參數**
   - `spot_raw.roc8("2026-10-30")` 產生 `1151030`。
   - `twse_twt93u_sbl(roc)` 將該民國日期直接放入 `https://www.twse.com.tw/exchangeReport/TWT93U?response=json&date={roc}`。
   - 本次 workflow log 曾回報「查詢日期小於 94 年 7 月 1 日」。
   - 已確認程式把民國年格式傳入 API；但尚未以官方文件或實際成功請求確認正確 query date 格式，故不可直接把「改成西元 YYYYMMDD」當作已驗證修法。
   - 狀態：民國格式傳入 **PASS（程式事實）**；正確格式／端點回應 **BLOCKED，待查**。

4. **TPEX margin_sbl 日期匹配**
   - `tpex_sbl(roc)` 呼叫 `tpex_margin_sbl`，沒有日期 query parameter。
   - 逐列只接受 `str(row["Date"]).strip() == roc`。
   - 本次回應 932 rows，但 matched_date_rows=0。
   - 尚未取得原始 Date 欄位樣本，無法確認資料實際格式或是否包含 2026-10-30。
   - 狀態：比對邏輯 **PASS（程式事實）**；格式根因 **BLOCKED**。

### 下一步（請嚴格依序）
1. 查證 TWT93U 官方／實際 endpoint 的正確日期格式，取得修正前後可重現的 response；不要只憑錯誤訊息猜格式。
2. 取得 TPEX `tpex_margin_sbl` 原始資料的 Date 欄位樣本，確認 932 rows 是否包含 2026-10-30，並核對日期表示方式。
3. 查核舊報告 11/1 當次原始 API response 或可追溯 log，區分 API 當時提供歷史值、同 T0 沿用值、最新快照。
4. 提出最小修正清單與測試矩陣：相同 T0 白天／晚上重跑、舊報告存在、缺值回填、錯日期拒收、無日期端點拒收、明示 force rewrite。
5. 取得使用者批准後才修改程式；修正後先跑測試，再以同一 T0 白天及晚上重跑做日期一致性驗收，最後才回到 Dashboard 階段。

### 明確驗收原則
- 同一 T0 的報告不得因產出時間不同而混入其他交易日資料。
- 無日期欄位的最新快照不得冒充歷史 T0 值；若無法證明日期，應標示 unavailable 或採明確可追溯的同 T0 舊值。
- 沿用值必須標示「沿用前版」、原始來源與可得的資料日期；不得偽裝成當次抓取成功。
- 不可將 workflow SUCCESS 當作 DATA_REPORT 日期正確性或完整性 PASS。
- 不可把 50 格 filled 與 73 格 overwritten 混為一談。
- 本輪為單模型自我審查，非獨立多模型 Auditor。

### 本輪狀態
| 項目 | 狀態 |
|---|---|
| 歷史 T0 日期混用的程式行為定位 | PASS |
| 同 T0 protect 判斷漏查 DATA_REPORT | PASS |
| TWT93U 民國日期被直接傳入 query | PASS |
| TWT93U 正確日期格式及實際成功 response | BLOCKED |
| TPEX Date 原始格式／目標日期是否存在 | BLOCKED |
| 舊報告 11/1 原始 API response 追溯 | NOT TESTED |
| 程式修正／測試／commit | NOT DONE |
| DATA_REPORT 重跑／Dashboard workflow | NOT DONE |
| Deploy／Merge | NOT DONE |

### 本輪 GitHub 文件更新紀錄
- 僅更新 `docs/recovery/RECOVERY.md` 與 `docs/recovery/PROGRESS.md`。
- 程式分支 `phase2-p0-ui-fixes`、master、V8、DATA_REPORT、Dashboard、Worker 均未修改。


## 2026-11-03 最新接手狀態：歷史 DATA_REPORT 重跑混版（22:xx）

### 目前工作焦點
- 暫停擴大 42 區塊 Dashboard 稽核；先處理 2026-10-30 歷史 DATA_REPORT 重跑造成的欄位覆蓋／資料日期混用。
- 目前工作分支 `phase2-p0-ui-fixes` HEAD：`581a808d6db6bea50a971f74a00b695ffbe8b509`；Recovery 分支：`ops/recovery-handoff`。Master HEAD `9f88de0bd92294df0051f706a0af1018e439bf6f`，禁止修改。
- 最新調查與完整證據已追加至 `PROGRESS.md` 的「2026-11-03 歷史 DATA_REPORT 重跑問題：第二輪實檔／程式根因稽核」段落；本節為新對話快速接手摘要。

### 最重要的已確認事實
1. Run `41644283168`（Job `125945406903`）確實執行 `--date 2026-11-03 --t0 20261030`，session=全日。這次指定歷史 T0 的日期／盤別本身正確。
2. Run log 顯示 TWT93U 因傳入民國日期 `1151030` 被拒絕；TPEX margin_sbl 取得 932 rows 但日期比對 0 rows。
3. `src/fetch_data.py` 的 protect 判斷只搜尋 `reports/Daily_REPORT_{T0}_*.md`，沒有把已存在的 `data_reports/DATA_REPORT_{T0}.md` 本身視為保護對象。因此既有 DATA_REPORT 在沒有 Daily_REPORT 時仍以 `protect=False` 重跑；本次 50 格沿用舊值、73 格被新抓取覆蓋，造成混版。
4. 無日期 TWT96U 最新快照被用在歷史 T0；官方定義 TWT96U 為「當日可借券賣出股數／限額」，不是「借券餘額」。此欄同時有日期污染與指標語義問題，不能直接用最新值覆寫舊 T0。
5. 11/02 全日 DATA_REPORT（phase2 branch blob `4add0443546bde87309fc1f13396f3a478e60bb0`）夜盤及 OI 有值；舊分支 11/02 日盤版不可拿來比較。10/30 舊完整報告 blob `665ae0ce957cbda372a1d70e1f06f0eea124ba11` 位於 `fix/three-market-correlation-history`；本次重跑後報告 blob `61b5a8799bec62762a60d5efb3f1099c18084fc5` 位於 `phase2-p0-ui-fixes`。

### 尚未完成／不可宣稱 PASS
- DATA_REPORT protect 程式修正與 regression tests：NOT STARTED。
- TWT93U 西元日期修正及真實 endpoint：NOT TESTED。
- TWT93U raw JSON fields／row index 對齊：NOT TESTED。
- TPEX Date 原始值樣本與日期正規化：BLOCKED／NOT TESTED。
- TWT96U／MI_MARGN 無日期來源的歷史回補隔離：NOT STARTED。
- 10/30 報告修復後重跑與完整性驗收：NOT TESTED。
- 本次只有 Recovery 文件更新，未改程式、資料、workflow、DB；未 Merge／Deploy。

### 接續執行順序
1. 只在 `phase2-p0-ui-fixes` 修正 `src/fetch_data.py`：只要同 T0 的 DATA_REPORT 已存在，預設必須 protect；只有明確 `--force-rewrite` 才允許覆寫。加入 regression tests，驗證沒有 Daily_REPORT 仍會保護 DATA_REPORT。
2. 修正 TWT93U 查詢日期使用西元 `YYYYMMDD`；先核對原始 JSON `fields`／row 長度再決定 index，不能猜。
3. 取得 TPEX `Date` 原始樣本，實作嚴格日期正規化；同查 highlight／margin 的日期比對。
4. 歷史 T0 不得採用無日期最新快照；TWT96U 名稱／來源必須反映「當日可借券賣出限額」，不能冒稱借券餘額。
5. 完成 code + tests + CI + endpoint validation 後，先核對 10/30、11/02 全日報告。未經明確授權不 Merge／Deploy；Master／V8 不動。

**Auditor 狀態：** 目前由單一模型依 GitHub 檔案、workflow log 及官方公開文件做自我稽核，並非獨立多模型審核。  


## 2026-11-03 接手續作：DATA_REPORT protect 修正已提交、CI 待確認
- 工作分支 phase2-p0-ui-fixes 最新 HEAD：1e15691a1c0964f626786779561e702fde3c7bee。
- 已修正 src/fetch_data.py：既有 DATA_REPORT 本身就是 T0 保護對象；除非明確傳入 --force-rewrite，否則重跑必須 protect，不再看 reports/Daily_REPORT 是否存在。程式 commit：9a576b97bfbc9030308a68eac07546abad9f1cc2。
- 已新增 tests/test_dashboard_unit_contract.py regression test，覆蓋 existing DATA_REPORT + no force、force rewrite、no existing report 三種狀態；最新測試 commit：1e15691a1c0964f626786779561e702fde3c7bee。
- GitHub 讀回驗證：src/fetch_data.py blob cd33a860f27d4d7d3bd3a7289174c42e8e9fadf6；test blob 0b9a6142aebfafc7f5e9f1b2bcc6f7a3f101fae9。Compare 顯示僅上述兩檔修改。
- CI 狀態：combined status 空 statuses；可用 GitHub 工具目前無 push-triggered workflow run listing／dispatch，因此 CI NOT TESTED／BLOCKED，不能標 PASS。
- TWT93U／TPEX 日期修正、TWT96U 歷史快照隔離、指標語義修正、10/30 報告重建均尚未完成。未 Merge／Deploy；Master／V8 未修改。
- 下一步：先取得 HEAD 1e15691... 的 CI Run ID 並核對 build／regression；CI PASS 後再修正日期來源與歷史快照混用問題。完整調查與分支／blob 證據見 PROGRESS.md 最新段落。


## 2026-11-03 資料層最新調查：借券指標模型存在錯誤（先不要重跑 10/30）
- **重大發現：TWT96U 不是借券餘額。** TWSE 官方定義 TWT96U 為「當日可借券賣出股數／限額」，每日約 22:30 產出。現行 `spot.build()` 卻將 TWT96U 上市／上櫃可借額度與 TPEX `SecuritiesBorrowingBalanceOfTheMarketDay` 相加，填入 DATA_REPORT「借券餘額」。這是跨指標混加，確定錯誤。
- 正確借券餘額候選官方來源是 TWSE TWT72U（每日約 20:30，包含前日餘額、今日新增借券、今日還券、今日借券餘額、資料日期）。但程式接入及歷史 API 參數尚未驗證，不能直接宣稱已可用。
- TWT93U 是融券／借券賣出餘額總量管制資料，應用於「借券賣出餘額」，不是借券餘額。官方資料欄位有 15 個；現行 parser 用 `row[7]`、`row[11]` 取借券前日／當日餘額，若 data row 保持 fields 原順序，可能 off-by-one。尚未拿到有效 response fields/data，列 HIGH RISK / NOT CONFIRMED，禁止猜 index。
- Run log 已證實 TWT93U 使用 ROC `1151030` 被拒絕（stat: 查詢日期小於94年7月1日）；日期參數需改測西元 `20261030`，再核對回傳日期。
- TPEX `tpex_margin_sbl` 本次 932 rows、0 matched；目前 `Date == roc` 嚴格比對。需取得原始 Date sample，確認格式及 endpoint 是否只回最新日。不能在未確認歷史能力前用日期正規化掩蓋資料缺失。
- 其他已確認歷史風險：MI_MARGN 無日期參數、TWT96U 無日期參數；TPEX highlight 只讀第一列最新資料；TPEX margin/SBL 僅在當前 OpenAPI 結果中比對 T0；歷史回補時可能無資料或拿到最新快照。三大法人若日期不符，目前仍註記「採用最新可得」，歷史報告必須改為 fail-closed。
- 因此先不要重跑 10/30。完整證據、各 source 的程式位置、官方資料定義及接續方案均已記錄在 PROGRESS.md 最新的「資料層第二輪：借券指標語義與歷史日期可用性稽核」段落。
- 後續先訂資料契約：`sbl_borrow_balance`（TWT72U 借入未還）、`sbl_short_sale_balance`（TWT93U + TPEX Margin_SBL 借券賣出未回補）、`sbl_shortable_limit`（TWT96U 當日可借券賣出限額）；三者絕不可混加。歷史來源缺日期或日期不符即 unavailable。
- 本輪僅唯讀稽核及官方文件查核；未改程式、報告、workflow、DB，未 Merge／Deploy。

## 2026-11-03 資料層第三輪接手摘要：TWT93U 索引錯誤已確認

### 目前最重要結論
- **TWT93U parser 現行欄位索引錯誤，已確認。** `src/sources/spot_raw.py` 用 `row[7]` 當借券前日餘額、`row[11]` 當借券當日餘額；但 15 欄原始順序中，index 7 是融券限額、index 11 是借券賣出當日調整，借券賣出前日餘額／當日餘額分別在 index 8／12。這會使現行 TWT93U sale_bal／sale_chg 不可信。欄位順序依獨立資料欄位整理與 TWSE 官方 TWT93U 欄位說明交叉核對。修正時必須先取得真實 JSON `fields`／`data`，以欄名定位，不可只硬改 index。
- **TWT72U 是官方借券餘額資料產品，且官方歷史查詢頁存在。** 頁面可選日期及分類，資料自 2004-11-22 起；官方欄位包含前日借券餘額、今日新增借券、今日還券、今日借券餘額。可是 Data E-Shop 同時把 TWT72U 列為訂閱商品，因此 RWD API 的實際可用性、分類、授權及 workflow 可否穩定使用尚未確認。不得先把它當成可用資料源。
- **TWT96U 只代表當日可借券賣出限額**，不是借券餘額，也不是借券賣出餘額。
- **TPEX `tpex_margin_sbl` 的欄位映射可能也反了。** endpoint 是「融券借券賣出餘額」，官方歷史表同時包含融券餘額與借券賣出餘額。現行程式把 `SecuritiesBorrowingBalanceOfTheMarketDay` 寫入 `bal`，把 `SaleBalanceOfTheMarketDay` 寫入 `sale_bal`，疑似把借券賣出餘額與融券餘額對調；但未取得真實 JSON 欄位樣本，仍列 HIGH RISK / NOT CONFIRMED，不可猜 mapping。
- TWSE／TPEX 的借券賣出餘額在市場分開、日期一致、單位確認為股數後，才可合併；絕不能和 TWT72U 借券餘額或 TWT96U 可借限額混加。

### 接續工作（嚴格限縮）
1. 取得 TWT93U 2026-10-30 真實 JSON response，核對 `fields`、row 長度、date，加入 fixture；依欄名取 index。
2. 取得 TPEX `tpex_margin_sbl` 真實 JSON sample，對照官方歷史 CSV 欄位，確認三個欄位 `SecuritiesBorrowingBalanceOfTheMarketDay`、`SaleBalanceOfTheMarketDay`、`SaleBalancePreviousDay` 的中文意義及單位。
3. 驗證 TWT72U 歷史 RWD 查詢路徑、selectType、日期回傳及授權可用性；若不能穩定合法使用，真正借券餘額欄保持 unavailable。
4. 上述未完成前，不修改 DATA_REPORT 借券 mapping、不重跑 10/30、不 Merge／Deploy。只在 `phase2-p0-ui-fixes` 工作；master、P0 base、V8 不動。

### 本輪狀態
- TWT93U index mapping：**FAIL / CONFIRMED**。
- TWT93U date=20261030 raw response：**NOT TESTED**。
- TWT72U 官方產品定義及歷史查詢頁：**PASS**；API／授權：**NOT TESTED**。
- TWT96U 語義：**PASS / OFFICIAL**（當日可借券賣出限額）。
- TPEX field mapping：**HIGH RISK / NOT CONFIRMED**。
- 程式、DATA_REPORT、workflow、DB：本輪未修改；未重跑歷史報告。
- Auditor：單一模型自我稽核，非獨立多模型審核。

Recovery 最新詳細證據記錄於 `PROGRESS.md` 的「2026-11-03 資料層第三輪：TWT93U 欄位索引確認與 TWT72U 歷史來源查核」。


## 2026-11-03 接手補充：TWT93U 真實欄位範例已找到；TPEX mapping 待精確對照

- TWT93U 已找到實際 API response 範例（2025-08-29），確認 endpoint query 日期格式為西元 `YYYYMMDD`，成功回傳 15 欄 fields 與 data。index 7=融券限額、8=借券賣出前日餘額、11=借券賣出當日調整、12=借券賣出當日餘額。現行 parser row[7]/row[11] 是確定錯誤；需依 fields 欄名定位、檢查 row 長度及 response date。來源與詳細內容見 PROGRESS.md「資料層第四輪」。
- 目前尚未取得本專案目標日期 2026-10-30 的真實 response；ROC 日期已由 workflow log 證實被拒絕，修正後應傳 `20261030` 並確認 response date。
- TPEX 官方 S47 Margin_SBL.csv 的 15 欄格式已取得：融券欄位在前 8 欄，借券賣出欄位在後 7 欄。現行 OpenAPI mapping 的兩個名稱 `SecuritiesBorrowingBalanceOfTheMarketDay` 與 `SaleBalanceOfTheMarketDay` 很可能分別落在借券賣出當日餘額與融券當日餘額，但還沒有直接 JSON schema／同日逐代號對照，故仍列 HIGH RISK / NOT CONFIRMED；不可先改 mapping。
- TWT72U 官方歷史頁有日期／分類查詢及 CSV 下載，但 E-Shop 訂閱產品標示月費及使用限制。不能假定 RWD API 可免費自動化使用；需先驗證公開頁 CSV 請求與授權邊界。TWT72U 仍是「借入未還」的正確官方候選來源。
- 本輪未修改程式、資料或 workflow，未重跑 10/30，未 Merge／Deploy。


## 2026-11-03 最新補充：TPEX S47 官方規格揭露現行 build 兩欄用途顛倒

- 已直接核對 TPEX 官方 V1.33 EDIS PDF 的 S47 Margin_SBL.csv（第 122 頁）：欄位 2–7 是融券前日餘額、融券交易、融券當日餘額及融券限額；欄位 8–13 是借券賣出前日餘額、當日賣出、當日還券、當日調整、借券賣出當日餘額及次日可借券賣出限額。
- 現行 `tpex_sbl()` 把 `SecuritiesBorrowingBalanceOfTheMarketDay` 當成 `bal`，再由 build 與 TWT96U 相加成「借券餘額」；把 `SaleBalanceOfTheMarketDay` 當成 `sale_bal`，再與 TWSE TWT93U 相加成「借券賣出餘額」。
- 依 OpenAPI 欄位命名與官方 S47 15 欄資料結構，最合理對應是 `SecuritiesBorrowingBalanceOfTheMarketDay` = 借券賣出當日餘額（S47 index 12），`SaleBalanceOfTheMarketDay`／`SaleBalancePreviousDay` = 融券當日／前日餘額（S47 index 6／2）。這代表目前 build 把兩個指標放反：借券賣出餘額被拿去當借券餘額，融券餘額被加進跨市場借券賣出餘額。仍需同日 OpenAPI JSON + 官方 CSV 逐代號對照確認 property mapping，因此不把這項推論寫成已完全驗證，但目前兩個輸出均應視為不可信。
- 官方 S47 不含「借入未返還」的借券餘額欄；真正借券餘額要另用 TWT72U。TWT96U 是可借券賣出限額，不能用於任何餘額欄。
- 這項發現比單純修 TWT93U 更重要：即使把 TWT93U 修正，現行 TPEX 的 `sbl.bal`／`sbl.sale_bal` mapping 仍會污染兩個彙總值。因此在 TPEX schema 對照完成前，不能重建 10/30 DATA_REPORT。
- 本輪未修改程式／資料／workflow，未重跑報告，未 Merge／Deploy。詳細證據見 PROGRESS.md「資料層第五輪」。

## 2026-11-03 P0 Quality 清查回溯稽核補充

- phase2-p0-data-quality HEAD 49fd5b0dfd6a9c1b89fc49bb6e4d81ae5fdc4d33 的 spot_raw.py／spot.py 仍有 TWT96U 指標誤用及 TWT93U row[7]/row[11] 欄位錯誤；DATA_SOURCES.md 甚至將 TWT96U 寫為「可借餘額」並標示通過。
- 該分支 tests/ tree 未見 TWT93U、TWT96U、TPEX S47 的原始 response fixture／欄位 mapping 專項測試；現有專項測試集中於維持率、Builder、workflow isolation、Gamma 等。
- 因此「P0 Quality 已完成數據真實性全面清查」目前無法由 repo 證據支持；更精確的結論是資料可用性／維持率／workflow 等部分品質工作確有實作，但資料來源定義、借券欄位語義及端到端日期真實性驗收存在重大缺口。
- 本結論是對 repo 留存證據的回溯稽核，不代表已取得當初所有外部稽核紀錄；不得宣稱已還原所有歷史驗收活動。
- 未改程式或報告，未重跑 10/30，未 merge／deploy，master／V8 未動。
## 2026-11-03 資料源取得性補查

- TWSE TWT93U 20261030 JSON 嘗試讀取遭查詢環境 Internal Error／DNS resolution failure；標記 BLOCKED（環境限制），不是官方 API 失效結論。目標日 response 尚未取得。
- TPEX 官方歷史 SBL 查詢頁提供日期選擇及 CSV 下載介面；但 E-Shop 對 Margin_SBL.csv 列為每日訂閱商品（22:00 產製；內部 NT$1,000/月、外部 NT$1,500/月，並有使用限制）。公開網頁 CSV 下載是否可合法供 workflow 自動化，以及與訂閱商品的授權界線，仍未確認。
- TPEX S47 exact JSON property mapping 及 20261030 同日 CSV/JSON 對照仍 NOT TESTED；禁止依欄位名稱推測直接改 mapping。
## 2026-11-03 TWT72U 範圍口徑補查

- TWSE 投資人教育資料定義借券餘額＝借入尚未返還，並將借券賣出餘額、融券餘額列為不同指標。
- TWT72U 欄位含系統別及市場別；TWSE 官方儀表板又分別呈現證交所借券系統、證商／證金營業處所及借券餘額合計。因此必須核對分類 selectType、系統別覆蓋與合計規則，不能未經對照便認定單一 TWT72U 分類可代表全市場合計。
- TWT72U 指標定義正確，但資料覆蓋範圍、分類參數、重複列風險、workflow 取得方式與授權仍 NOT TESTED。
## 2026-11-03 現貨籌碼投資人語義與文件／程式矛盾

- 投資人可見欄位應為融資餘額／增減（億元）、融券餘額／增減（張）、上市融資維持率（%）、借券餘額（張）、借券賣出餘額／增減（張）。`margin.s_bal` 是融券餘額；`sbl.bal` 是借券餘額；`sbl.sale_bal` 是借券賣出餘額，三者不可混用。
- phase2-p0-ui-fixes 的 DATA_SOURCES.md 已寫明 TWT96U 不得當 TWT93U 替代來源；但 spot_raw.py 仍把 TWT96U 當可借餘額，spot.py 仍將 TWT96U + TPEX stp.bal 填入 sbl.bal。文件與程式矛盾，sbl.bal FAIL。
- TWT93U parser 仍使用 row[7]/row[11]，上市借券賣出餘額 parser FAIL。
- DASHBOARD_UNIT_MAP 的區塊 12 舊 PASS 只能代表 UI 欄位／單位／scope 顯示契約，不能視為來源定義與原始 mapping 的真實性 PASS；必須修正驗收語義。
- 本輪僅盤點現貨融資融券及借券欄位，未改程式或報告，未重跑 10/30，未 merge/deploy。

## 2026-11-03 最新接手狀態｜借券資料鏈已修正並完成來源 live 驗證

- 活躍分支：phase2-p0-ui-fixes；最新 HEAD：899900c017ef036f808b4843ed85f6e29ca383e1。master、P0 base、V8 未修改；未 merge/deploy。
- 三個官方歷史端點已在 GitHub Actions 對 2026-10-30 實際查詢成功：TWT72U（2,072 個股，上市 1,237、上櫃 835，兩市場小計及整體總計一致）；TWT93U（1,307 個股，逐股遞推檢查通過）；TPEx S47（932 rows，逐股遞推檢查通過）。
- 借券三指標已分離：TWT72U＝借入未還的借券餘額；TWT93U＝上市借券賣出餘額；TPEx S47＝上櫃借券賣出餘額；TWT96U＝當日可借券賣出限額，已排除於餘額欄位。
- TWT93U／TPEx S47 重複欄名以欄位群組辨識；所有來源均驗 response date、欄位、逐列餘額遞推。缺資料 fail-closed。
- Unit Contract Audit Run 41671847081 PASS；V9 UI Fixes Regression Run 41671995742 PASS；Daily Premarket build Run 41671847060 PASS、deploy skipped。
- 區塊 12 的舊 DATA_REPORT 數值尚未由新 parser 重建；舊來源註記無法證明市場範圍，Builder 現正顯示「範圍未註明」。不可把舊 DATA_REPORT 的 36,178 張／-1,273 張當成新來源驗證通過。
- 尚未重建 DATA_REPORT_20261030。E-Shop 訂閱商品與公開 endpoint 的自動化授權邊界仍 NOT TESTED，確認前不要進行報告重建。
- Recovery 完整證據、commit、CI Run IDs、檔案 SHA、限制及下一步見 PROGRESS.md 本節。
- Auditor 為單一模型自我稽核，非獨立多模型審核。


## 2026-11-03 最新驗收覆核｜目前可接續狀態

- 活躍分支 phase2-p0-ui-fixes HEAD：01d8d6e82810b13ce617feff18f142189cb9c14a。
- Unit Contract Audit Run 41672806366 **PASS**；V9 UI Fixes Regression Run 41672806450 **PASS**；Daily Premarket V9 Pro Run 41672806998 build **PASS**、deploy **SKIPPED**。
- 三個官方借券端點 2026-10-30 live 驗證通過；TWT72U 市場小計與整體合計一致，TWT93U／TPEx S47 逐股餘額遞推檢查通過。
- 42 區塊 unit contract、DATA_REPORT／Builder、React、TAIFEX night unavailable regression 均通過。
- 2026-11-02 既有報告 Builder build 成功；未修改 data_reports 樣本。2026-10-30 報告仍未重建。
- 目前唯一直接阻止收尾的事項：先確認官方端點自動化使用授權／E-Shop 商品條款邊界；確認可用後，再重建並驗收 20261030 DATA_REPORT。舊報告借券數字不可當作新 parser 驗證結果。
- 詳細實作、數據列數、測試結果及 commit 證據見 PROGRESS.md 最新兩節。
- 未 merge/deploy；master、P0 base、V8 未修改；Auditor 為單一模型自我稽核。


## 2026-11-03｜新增授權阻擋（接手時必讀）

- TWSE TWT72U／TWT93U 雖已實際 live 查詢成功，但官方 E-Shop 將其列為月訂閱商品；目前未取得使用者訂閱／書面授權證據。技術可讀取 ≠ 可免費自動化使用。
- TWT72U：內部 NT$1,500/月、外部 NT$3,000/月；TWT93U：內部 NT$1,000/月、外部 NT$1,500/月。官方商品連結及欄位內容見 PROGRESS.md 最新授權查證段。
- TPEx S47 dataset 11632 則明確標示政府資料開放授權第 1 版、每日更新、免費。
- 所以目前不得重建 DATA_REPORT_20261030，除非先確認使用者已訂購 TWT72U／TWT93U 或取得 TWSE 授權。若沒有，上市借券餘額及上市借券賣出欄應 unavailable；TPEx S47 可單獨顯示上櫃借券賣出值並標示 scope。
- 最新 phase2-p0-ui-fixes HEAD 因 DATA_SOURCES 授權註記更新而變更；重新查詢 branch HEAD，不要沿用前一節的 HEAD。


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


## 2026-11-04 最新接手補充｜分支主線與移植決策

- 維持原案：主線 `phase2-p0-ui-fixes`，三市場分支 `fix/three-market-correlation-history` 作選擇性移植來源，不整條 merge。
- P0 HEAD `8317dcb359b5629cf073c144068339322e89884a`；三市場 HEAD `e678877bc076e157c948483d40f136e0f504303e`；共同祖先 `d5443eacb29b7b0824306de4d1b126b9281210b5`。P0 ahead 59、三市場 ahead 105；兩分支 diverged。
- 三市場分支已完成多項值得移植的工作：三市場分析卡、三劇本條件觸發、選擇權法人力道、live synthesis narrative、方向一致性與資料有效性判斷、單位／精度修正、相關性歷史 seed。詳見 PROGRESS.md 的 2026-11-04 分支盤點。
- 不以三市場分支為 base 的關鍵理由：該分支仍有舊 TWT93U endpoint／固定索引／逐股加總，且舊 spot mapping 將 TWT96U 與 TPEx 值併入借券餘額；P0 fixes 已有較正確的資料指標分離與新版 RWD parser，應保留。
- 但 P0 fixes 借券 parser 尚未符合使用者最新指定：TWT93U 直接取最後「合計」列；TWT72U 直接取「整體市場」合計列。現有測試仍以個股加總為契約，必須修正並加入真實 JSON fixture；不可宣稱此項 PASS。
- 下一步：先完成 P0 借券 parser 合計列 mapping／fixture／測試，再按功能群將三市場 UI／分析成果移植到 P0 fixes；correlation history workflow／SQLite 獨立處理。全程不改 master、P0 base、V8 或 data_reports 樣本，不 merge/deploy。
- 最新 HEAD combined statuses 均空白，故兩分支最新 HEAD CI **NOT VERIFIED**；既有歷史 CI run 不可直接當作目前 HEAD 驗收。
- 本輪未修改產品程式或資料，只更新 Recovery 文件；Auditor 為單一模型自我稽核，非獨立多模型審核。
