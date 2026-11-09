---
name: daily-premarket-analysis-v9-pro
description: V9 Pro 台股每日盤前分析系統操作與維護規範。涵蓋 17F 分析資料、Python Builder、React Dashboard、GitHub Actions、GitHub Pages 與六頁 Dashboard。Use when user asks for V9 Pro、每日盤前分析、V9 Pro Dashboard 或維護此專案。
---

# 台股每日盤前分析 Skill — V9 Pro

## 1. 文件適用範圍與優先原則

本 Skill 僅適用於 V9 Pro。V9 Pro 是唯一後續維護與執行版本；不得回退 V8、讀取 V8 資料庫、建立 V8 Schema，或保留 V8 相容／遷移路徑。

修改前必須先讀取並檢查當前分支的實際程式，不可只依賴本文件中的歷史描述。若本文件與程式、Workflow 不一致，以當前程式的可驗證行為為準，並回報差異；不得自行假定文件描述一定正確。

- 專案版本維持 V9 Pro，不得自行升版或改名。
- 不得任意刪除、合併或重新命名六個 Dashboard 頁籤。
- 不得把尚未實作、未測試或僅有代理估算的功能描述成已完成。
- 不得捏造市場數據、資料來源、回測結果、勝率或測試結果。
- 修改前先確認工作目錄、檔案路徑、Git 狀態及目前版本。
- 除非使用者明確要求，不要擴大修改到 V9 Pro 以外的 Skill、Workflow 或專案文件。

## 2. V9 Pro 主要檔案

| 用途 | 路徑 |
|---|---|
| 分析資料 Builder | `scripts/v9_pro_builder.py` |
| React Dashboard 母版 | `templates/v9-pro-react-template.html` |
| 每日自動化 Workflow | `.github/workflows/daily-premarket-v9-pro.yml` |
| Skill | `skills/daily-premarket-analysis-v9-pro-skill.md` |
| Dashboard 與 JSON 輸出 | `dashboards/` |
| 輸入分析報告 | `data_reports/DATA_REPORT_YYYYMMDD.md` |

歷史 Repository 內容可能仍留有 V7/V8 檔案或舊工作流程，但它們不屬於 V9 Pro 執行鏈；V9 Pro 僅使用 v9_pro_history.db 與 v9_pro_history Schema。

## 3. 目前可確認的執行流程

V9 Pro GitHub Actions Workflow 的可見流程如下：

1. 由排程、符合路徑的 Push，或 workflow_dispatch 觸發。
2. 解析指定日期或選取最新的 `DATA_REPORT_YYYYMMDD.md`。
3. 執行 `scripts/v9_pro_builder.py`，產生 `dashboards/data-YYYYMMDD.json`。
4. 驗證 JSON 可解析。
5. 讀取 `templates/v9-pro-react-template.html`。
6. Workflow 將資料 JSON 注入 HTML 的 `window.DASHBOARD_DATA`，並套用 React 資料綁定修正。
7. 產生 `dashboards/v9-pro-YYYYMMDD.html`。
8. 更新 `data-latest.json`、`v9-pro-latest.html`、`index.html` 與 `manifest.json`。
9. 將 `dashboards/` 上傳為 GitHub Pages artifact，部署至 GitHub Pages。

注意：Builder 的實際輸出、母版的資料讀取方式及 Workflow 的注入步驟，必須以三個檔案當前版本交叉核對。不可沿用舊文件中「正式環境 fetch JSON、Builder 只產 JSON、不產 HTML」等未必符合現行 Workflow 的敘述。

## 4. 執行方式

依目前 Workflow 使用的參數格式執行：

```bash
python scripts/v9_pro_builder.py \
  --data_report data_reports/DATA_REPORT_YYYYMMDD.md \
  --out dashboards/data-YYYYMMDD.json \
  --date YYYYMMDD
```

實際執行前先確認輸入報告存在、日期正確及輸出路徑正確。不得以舊日期範例或 Skill 中的歷史測試數字代替當日資料。

## 5. Dashboard 固定頁籤

V9 Pro Dashboard 保留以下六頁：

1. 總覽
2. 現貨
3. 重要市場
4. 期貨
5. 選擇權
6. 綜合分析

維護時須確認六頁均能正常切換、資料綁定正確、手機及桌面版均可閱讀。不可因重構而省略使用者原先要求的區塊。若資料缺失，應明確呈現缺失或不可用狀態，不得用虛構數值填補。

## 6. 分析資料與可信度規則

### 6.1 17F 與技術指標

舊版規格曾描述 15 個基礎因子加 RSI、MACD 為 17F，並提及 VIX 動態權重、RSI/MACD 備援與 SQLite 歷史資料。這些描述不等同於每一項功能目前都已正確實作。

每次修改分析引擎時，必須逐項核對：
- 因子清單、輸入欄位及資料來源。
- 基礎權重採相對權重點數（目前總和 104），不是百分比；動態調整後只對有效因子重新正規化至 100%。缺值因子有效權重為 0。輸出須明確標示 `base_weight_total`、`base_weight_unit=relative_points` 與 `weight_normalization=active_factors_rescaled_to_100_percent`。
- 權重總和、動態權重調整公式及缺值處理。
- RSI、MACD 的資料期間、計算方式及備援來源。
- 缺值時是否停用因子、重新正規化權重，或採取其他策略。
- SQLite schema、歷史資料筆數及回測計算是否真實可用。

不得只根據頁面標示「17F」或 Builder 註解宣稱 17 個因子完整有效。若尚未逐項測試，應標示 NOT TESTED。

### 6.2 真實值、推算值與缺失值

所有重要數據應盡可能保留來源、資料日期、擷取時間及計算方法。呈現時須區分：
- 來源直接提供的真實數據。
- 由來源數據計算出的衍生數據。
- 代理指標或估算值。
- 缺失、過期或無法驗證的數據。

Gamma、GEX、IV、相關性、歷史勝率等項目，只有在資料來源與計算方式可驗證時才能標示為實際計算結果。不可將 fallback、placeholder、預設矩陣或硬編碼值包裝成即時真實數據。

### 6.3 歷史統計

SQLite 檔案存在不代表歷史樣本充足。使用歷史相似度、因子績效或勝率前，必須檢查資料表、日期範圍、有效樣本數、標籤定義及計算程式。樣本不足時明確顯示不足，不得推論為可靠勝率。

## 7. 圖表與 UI 維護規範

- 保留目前 V9 Pro 深色視覺設計與六頁資訊架構，除非使用者明確要求改版。
- Canvas 圖表需處理 Resize、DPR、容器尺寸及手機版顯示。
- 防止文字、數值、圖例及軸標籤重疊；長文字應截斷或換行。
- 圖表數值必須來自 Dashboard data payload，不得在 UI 內另放互相矛盾的硬編碼市場數字。
- 台股慣例：上漲／多方使用紅色，下跌／空方使用綠色。不得套用美股顏色慣例。
- 空資料、錯誤資料及載入失敗必須有清楚狀態，不得留下空白畫面或假資料。

## 8. Phase 2 已確認方向（規劃，不代表已實作）

Phase 2 定位為「台股市場情報與短線交易決策輔助系統」，方向已確認，但以下項目仍須依實際盤點、規格及測試逐步開發，不可宣稱已完成：

1. Data Quality：資料來源、時間戳、完整度、異常與交叉驗證。
2. Analysis Engine：完整核實 17F、跨市場分析、多空一致性及市場情境辨識。
3. Historical Intelligence：持續累積歷史資料、技術指標、相似情境及統計驗證。
4. Options Intelligence：選擇權籌碼、關鍵履約價、部位變化及壓力分析。
5. Trading Decision Support：盤前情境、關鍵價位、成立／失效條件及風險提示。
6. Dashboard Integration：整合至既有六頁，不任意推倒重做。
7. Performance Review：保存盤前快照並以盤後結果驗證。

Phase 2 應採增量開發。先確認現況與驗收標準，再修改程式；不得一次擴張成與本專案無關的工作。

## 9. 開發與驗收流程

複雜修改採 Supervisor / Worker / Auditor 工作流程；若實際只有單一模型，必須稱為自我審查，不得宣稱獨立多模型審核。

每次任務至少完成：
1. 需求與影響檔案確認。
2. 修改前檢查及備份／Git diff。
3. Worker 實作並回報修改檔案。
4. 執行適用的語法、資料、建置及 UI 測試。
5. Auditor 對照需求、程式與測試證據。
6. 缺陷修正後重新驗收。

狀態只能使用：
- PASS：有可檢查證據通過。
- FAIL：測試或需求不符合。
- BLOCKED：受外部條件阻擋。
- NOT TESTED：尚未測試。

不得將「程式已修改」等同於「功能已驗證」，也不得只因 GitHub Actions 成功就宣稱數據分析正確。

## 10. GitHub Pages 部署檢查

部署前至少檢查：
- Builder 成功產生 JSON，且 JSON 可解析。
- HTML 正確注入 `window.DASHBOARD_DATA`。
- React 資料變數確實讀取注入資料。
- HTML 不含意外的字面 `\\n` 或其他注入殘留。
- 六頁標籤存在。
- `dashboards/index.html` 非空且為預期日期版本。
- Actions Build 與 Deploy job 成功。
- 最後以實際瀏覽器確認頁面可正常顯示。

若無法實際瀏覽器驗證，必須標示 NOT TESTED，不可宣稱端到端通過。

## 11. 回覆與交付要求

回報時聚焦使用者指定的 V9 Pro 範圍，不擴張到 Repository 其他專案。清楚列出：
- 已修改檔案。
- 已執行測試與證據。
- PASS / FAIL / BLOCKED / NOT TESTED。
- 尚未完成及風險。
- Commit 或備份檔案位置（只有確實產生後才能提供）。

## 12. 歷史資訊處理

舊版文件中的市場數字、日期、測試結果、檔案大小、卡片數、圖表數及勝率均屬歷史紀錄，不可當作目前狀態。使用前必須重新檢查當前程式、資料及執行結果。

## 10. Dashboard 數字單位與圖表版面驗收（強制）

修改 Dashboard、Builder、DATA_REPORT 或分析模板前，必須先讀取 `docs/DASHBOARD_UNIT_STANDARD.md`。該文件是 V9 Pro 單位顯示標準。

### 10.1 三層單位契約
- 每個數值欄位必須確認來源單位、Builder 標準單位、Dashboard 顯示單位。
- 不得依數字大小推測單位；來源定義不明確時標 BLOCKED。
- 任何單位轉換必須寫出公式並以測試驗證倍率、正負值及缺值。
- DATA_REPORT 解析器不可只擷取數字而忽略單位字串；來源單位驗證未完成不得標 PASS。

### 10.2 呈現規則
- KPI、表格、一般分析文字：數字旁須有單位；若表頭已明確定義單位，欄內可不重複。
- 圖表優先在軸標題、圖例或數列名稱標示單位。
- 若每個圖內數值都加單位會造成擠壓、裁切、遮擋或可讀性下降，允許省略逐筆單位，改在圖表緊鄰上方或下方加清楚備註，例如「單位：口」或「價位單位：點」。
- 混合單位圖表必須逐數列標示單位；不可用單一備註涵蓋不同量綱。
- 圖表縮放須標示原始數值、轉換倍率及方向；不可只寫 x10。
- 不得為了塞入單位而造成文字、圖例、數值標籤或圖示重疊。

### 10.3 驗收
- 42 個可見 Dashboard 區塊逐一對照資料欄位、來源單位、Builder 單位及顯示單位；整組 KPI 群依使用者定義計為一個區塊。
- 六個頁籤均須檢查：總覽、現貨、重要市場、期貨、選擇權、綜合分析。
- 桌面與手機實際渲染均須檢查換行、裁切、圖例、數值標籤及文字／圖示重疊。
- 靜態程式檢查不等於實際渲染 PASS。未實際渲染一律 NOT TESTED。
- GEX 的公式、Worker 回傳 schema 與量綱未核實前，單位狀態維持 BLOCKED。
- 驗收結果必須逐項使用 PASS、FAIL、BLOCKED、NOT TESTED；不得把未測試寫成通過。


## 13. 資料層完成與嚴格凍結規則（2026-11-09 起生效）

使用者已確認 V9 Pro 資料層改進全部完成。自 2026-11-09 起，資料層進入 **DATA LAYER FROZEN** 狀態。除非使用者事前明確同意特定變更，否則一律禁止修改、增加、刪除、重構或調整任何資料層內容。

### 13.1 凍結範圍

- 資料擷取、來源端點、解析器、清洗、轉換、計算、合併、fallback、缺值處理、驗證與輸出程式碼。
- 所有資料層 GitHub Actions Workflow，包括 `.github/workflows/daily_data.yml`、排程、觸發輸入、執行參數、重試、timeout、依賴安裝及 commit/push 流程。
- DATA_REPORT 欄位、指標、章節、格式、單位、來源標示、產出與覆寫規則。
- Worker、Proxy、API、資料來源設定及任何會改變資料內容或取得方式的設定。
- 資料層測試、fixture、schema、設定檔及相關自動化。

### 13.2 未經同意禁止事項

不得以效能優化、修 bug、清理、重構、依賴更新、穩定性改善或「小幅調整」為由自行變更上述內容。不得自行提交資料層程式碼或 Workflow commit，不得部署 Worker／Proxy，也不得執行會改變資料層設定或產物的操作。

### 13.3 允許事項與授權流程

- 只讀檢查、讀取日誌、分析報告、比對資料及提出風險說明，不等於取得修改授權。
- 發現疑似問題時，先提出可驗證證據、根因假設、影響範圍及最小修正方案；等待使用者明確同意後才能動手。
- 使用者同意某一項變更，只授權該項明確範圍，不得擴張到其他檔案或資料層項目。
- 更新 Skill／Recovery／交接文件以記錄本凍結規則，不視為資料層程式碼或 Workflow 變更。

### 13.4 解除凍結

只有使用者明確要求解除或調整凍結範圍，才可恢復相應資料層修改。未取得明確授權時，預設狀態永遠是凍結。
