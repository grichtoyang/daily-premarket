# MASTER_SPEC — 盤前分析 V9 Pro 專案總規範

> 文件定位：專案最高層級的架構、需求與不可變規則索引。
> 本文件不取代既有技術規格；細部實作以對應文件及已驗證程式碼為準。
> 最後整理：2026-11-01（Asia/Taipei）。

## 1. 專案目標與版本定位

- Repository：`grichtoyang/daily-premarket`
- V9 Pro：目前唯一維護及運行版本。
- V8：歷史／相容保留版本，禁止修改、刪除、搬移或以 V9 檔案覆蓋。
- Phase 2：分階段改善資料品質、籌碼分析、圖表與分析能力；各階段須依正式規格與使用者批准推進。
- GitHub 是專案狀態、程式碼與交接證據的唯一可信來源；聊天紀錄不是 Git 狀態的替代品。

## 2. 文件權威順序

遇到文件矛盾時，不可自行猜測或把舊文件當成最新決策。依序處理：

1. 使用者在目前對話明確確認的最新決策。
2. 本文件記錄的不可變規則及經確認的架構決策。
3. 對應模組的最新正式規格文件／模板。
4. `PROGRESS.md` 的進度紀錄。
5. `RECOVERY.md` 的最近工作快照（只描述狀態，不可推翻規格）。
6. 舊 HANDOFF、舊對話及歷史文件（僅供追溯，必須辨識是否已過期）。
7. 程式碼現況（可用來驗證實作，不可單方面取代需求）。

現有主要文件索引：
- `docs/PHASE2.md`：現存 Phase 2 文件；目前內容仍有早期選擇權改版待辦，不能直接視為完整新版 P0～P5 路線圖。
- `docs/DASHBOARD_SPEC.md`：Dashboard 詳細規格；未經使用者同意不得改動六個分頁及其規格。
- `docs/DATA_SOURCES.md`：資料來源與擷取方式。
- `docs/DATA_SCHEMA.md`：資料結構與欄位規範。
- `docs/AUTO_FLOW.md`：自動化流程。
- `docs/SOP.md`：操作及品質控管程序。
- `docs/HANDOFF.md`、`docs/AUDIT_HANDOFF.md`、`docs/AUDIT_FIX_HANDOFF.md`：歷史交接／稽核材料；閱讀時須確認日期與是否已被後續決策取代。

## 3. 不可變更規則（除非使用者明確批准）

1. V8 檔案全部保留：不修改、不刪除、不搬移。
2. V9 Pro 是唯一維護及運行版本。
3. P0 核心資料品質功能已功能凍結；不得重新開發已完成的引擎或擴大需求。只有使用者已指出、且經確認的 P0 Dashboard 缺陷可提出最小修正。
4. 不得未經確認就合併 P0 與 master。
5. 不得直接覆蓋 master 正式 Dashboard。
6. Fetch 與 Build 工作流程維持分離。
7. 不得擅自修改 Dashboard 六個分頁、既定規格或整體設計；缺陷修復限於必要最小範圍。
8. 不得虛構資料、引用、測試、瀏覽器驗證、Actions 結果、Git 操作或完成狀態。
9. 未檢查目前 Git branch、HEAD、工作目錄及遠端狀態前，不得開始修改或 Push。
10. 未確認 GitHub 實際狀態前，不得重複修改或 Push；中斷後先讀取 `RECOVERY.md` 並重新查證。
11. 每次修改需說明檔案、目的、分支、Commit、測試證據及未驗證事項。
12. 所有新工作優先使用獨立工作分支；不得把文件交接工作混入 P0 功能分支或 master。

## 4. 系統架構概覽

目前 Repository 同時保留既有每日盤前分析資料管線與 V9 Pro Dashboard／Phase 2 工作。

- 資料層：GitHub Actions／Python fetch 程式，產生標準化 DATA_REPORT。
- 分析層：依正式分析模板使用 DATA_REPORT 產出分析報告及結構化資料。
- 視覺層：Dashboard 讀取建置資料並呈現；V9 Pro Dashboard 有獨立建置與部署路徑。
- Fetch 與 Build 必須分離；部署路徑須維持 V8 與 V9 Pro 隔離。
- 詳細執行方式以 `docs/AUTO_FLOW.md`、`docs/DATA_SOURCES.md`、`docs/DATA_SCHEMA.md`、`docs/DASHBOARD_SPEC.md` 及 workflow 實際內容為準。

## 5. Phase 2 管理原則

- P0：資料品質與 V9 Pro 基礎建置。既有 P0 核心功能凍結；目前僅有結案前待驗證／缺陷收尾項目。
- P1～P5：不得只依聊天摘要或推測開發。必須先核對最新正式規劃、依賴、資料可用性及驗收條件，再由使用者確認工作範圍。
- 目前已知舊版 `docs/PHASE2.md` 並非完整新版 Phase 2 規劃，必須在啟動 P1 前完成規格盤點與衝突清理。
- 任何階段均須先定義輸入、輸出、資料日期、計算方式、失敗／缺值行為及驗收證據。

## 6. 變更與驗收流程

Supervisor／Worker／Auditor 思維：
1. Supervisor：拆解任務、界定變更邊界、確認依賴與驗收條件。
2. Worker：執行最小必要修改，提供 diff、Commit 及可重現證據。
3. Auditor：逐項獨立檢查需求符合度、程式差異、測試及文件一致性。
4. 有缺陷則退回修正並複驗；必要項目未通過不得宣稱完成。

若只有單一模型，必須標示為單模型自我審查，不得宣稱獨立多模型協作。

狀態只能使用：
- PASS：有可查證證據且符合驗收標準。
- FAIL：已執行且不符合標準。
- BLOCKED：因依賴、權限或缺少條件而無法執行。
- NOT TESTED：尚未執行測試。
- IN PROGRESS：正在處理；不得等同 PASS。

## 7. Git 與交付規範

- 工作開始：確認 repository、branch、HEAD SHA、工作樹／未提交變更、遠端分支及最近 Actions。
- 工作中：先建立或切換到獲准的隔離分支；一次只處理明確範圍。
- 工作結束：更新 `docs/recovery/PROGRESS.md` 與 `docs/recovery/RECOVERY.md`。
- Commit／Push：只在使用者授權的分支執行；Push 後必須重新讀取 GitHub branch SHA 確認。
- 不得以「工具呼叫成功」代替遠端內容驗證。
- 不得在未經批准下 Merge、Rebase、Force Push、刪除分支或覆蓋正式部署路徑。

## 8. 對話中斷恢復規則

新對話必須依 `docs/recovery/RECOVERY.md` 指示恢復，並讀取：
1. `docs/recovery/MASTER_SPEC.md`
2. `docs/recovery/PROGRESS.md`
3. `docs/recovery/RECOVERY.md`

接著重新查詢 GitHub 實際分支、HEAD、最近 Commit、未完成 Actions 及文件版本。若文件與 GitHub 現況不一致，以最新可查證的 GitHub 狀態為準，並先修正交接紀錄，不得直接猜測或重做。

## 9. 規格變更紀錄

| 日期 | 變更 |
|---|---|
| 2026-11-01 | 建立 V9 Pro 專案總規範索引、不可變更規則、驗收狀態及中斷恢復規則。 |
