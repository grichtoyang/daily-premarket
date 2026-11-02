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

