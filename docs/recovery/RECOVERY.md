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
