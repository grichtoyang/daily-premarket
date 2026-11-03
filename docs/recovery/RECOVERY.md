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
