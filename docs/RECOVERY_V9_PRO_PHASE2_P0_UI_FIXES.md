# v9 Pro Recovery — Phase 2 P0 UI / Unit Contract

更新日期：2026-11-02（Asia/Taipei）
Repository：`grichtoyang/daily-premarket`
工作分支：`phase2-p0-ui-fixes`
更新基準 HEAD：`8034ee36ed51c84e13a79c2753f74e8a6b5ac49e`（2026-11-02 最新 Recovery 提交）

> 本文件是本階段的續作錨點。新對話先讀本文件，再從「下一步」接續。
> 本文件只記錄可確認的狀態；未執行的測試不得標為 PASS。

## 1. 工作範圍與不可違反事項

- 本階段工作：v9 Pro Dashboard 42 個可見區塊的資料欄位／單位契約、Builder 來源單位驗證、圖表單位標示與版面風險、回歸測試。
- Dashboard 共 6 個分頁：總覽、現貨、市場、期貨、選擇權、綜合；使用者人工盤點為 **42 個可見區塊**，整組 KPI 計為 1 區塊。此數字為驗收基準。
- 只允許修改 `phase2-p0-ui-fixes`。
- 不修改 V8、Master、`phase2-p0-data-quality` 或其他分支；不 merge、不 cherry-pick、不部署。
- DATA-UI-04、DATA-UI-05 已完成，不得重做或列為待辦。
- 使用者已確認先前 11 張圖／區塊不再重疊；不要重開已確認項目。
- 使用者要求：清查完成後，發現的問題一次修正，不要每完成一小項就停下來詢問。
- 使用者接受圖表內數字不逐一加單位：若會造成擁擠，可在圖表緊鄰上方／下方標明單位；混合單位圖表必須分別標示各序列單位。
- 最終 Dashboard 是否完成，仍須使用者視覺驗收。

## 2. 已完成的修改（需以目前分支檔案為準）

- 新增 `docs/DASHBOARD_UNIT_MAP.md`：Dashboard 區塊／欄位與單位對照。
- 新增 `docs/DASHBOARD_UNIT_STANDARD.md`：單位標示原則。
- 更新 `docs/DATA_REPORT_TEMPLATE.md`：修正融資、借券、現貨金額、期貨與選擇權等資料單位文件口徑。
- 更新 `docs/ANA_REPORT_TEMPLATE.md`：分析報告單位規則。
- 更新 `skills/daily-premarket-analysis-v9-pro-skill.md`：同步 Skill 的單位規則。
- 修改 `scripts/v9_pro_builder.py`：加入部分期貨／選擇權來源單位後綴驗證，並補充部分敘述單位。
- 修改 `templates/v9-pro-react-template.html`：補充部分 KPI、表格、圖表與敘述的單位文字；處理 PCR 成交量結構與 OI PCR 的區別；部分圖表加入單位註記。
- 新增 `tests/test_dashboard_unit_contract.py`。
- 修改 `tests/test_react_template_static.py`，同步目前圖表函式簽名。
- 新增 `.github/workflows/unit-contract-audit.yml`。
- 上述為「已修改」，不等於所有內容已通過測試或視覺驗收。

## 3. 單位契約基準

| 資料類型 | 顯示／計算單位 |
|---|---|
| 台股指數、期貨價格、價差、基差、選擇權履約價與關鍵價位 | 點 |
| 漲跌幅 | % |
| 殖利率水準 | % |
| 殖利率日變化 | 百分點（pp），不可誤標為百分比變化 |
| 現貨法人買賣超、成交金額、融資餘額及增減 | 億元 |
| 融券、借券餘額／借券賣出餘額／增減 | 張；來源若為股，必須明確換算 |
| 期貨／選擇權成交量、未平倉量、法人淨交易口數 | 口 |
| 融資維持率 | % |
| PCR | Put OI / Call OI，顯示為倍；不可與 Call／Put 成交量占比混為一談 |
| Bias | 分 |
| 相關係數 | 無單位，範圍 -1 至 +1 |
| 匯率 | 必須標示貨幣對與報價方向 |
| ADR | USD／股；漲跌幅為 % |
| GEX | NT$／標的價格變動 1%；Black-Scholes 模型估值，非 TAIFEX 官方欄位 |

需分清楚：來源原始單位、Builder 標準化後單位、Dashboard 顯示單位。不得依數值大小猜測單位。

## 4. 目前已知的主要風險／待查項目

1. **42 區塊資料路徑對照已補齊**：Unit Map 新增每區塊 Dashboard JSON path、DATA_REPORT 章節與單位／缺值備註；尚有少數分析衍生卡片需以使用者最終視覺驗收為準。
2. **來源單位契約邊界已釐清**：現貨欄位 regex 明確驗證單位後綴；期貨／選擇權 DATA_REPORT 表格部分採章節／表頭 schema 定義單位，原始列未逐列提供單位欄，因此不能宣稱每列 regex 驗證單位後綴。
3. **圖表單位註記渲染已驗證**：React 卡片元件在圖表正下方顯示 chartNote；Desktop／Mobile 六頁預覽均已產生並檢查。
4. **現貨成交額圖表 F 區塊已確認**：使用 `Ol` 金額比較圖，單位億元；`yf` 僅用於 Call／Put 成交量結構，靜態測試覆蓋。
5. **選擇權法人混合單位已確認**：`options.instOpt` 為日／夜盤交易淨口數（口）；`options.instOptForce` 為法人多空力道金額（億元），Unit Map 分開標示。
6. **GEX 單位已核實並同步**：`gamma × OI × 50 元／點 × underlyingPrice² × 1%`，單位 NT$／標的價格變動 1%；DATA_REPORT 14A 明列，屬 Black-Scholes 模型估值、不是 TAIFEX 官方 GEX。Dashboard、registry、unit map、standard、Skill 已同步。
7. **Desktop／Mobile 實際渲染已完成技術檢查**：最新非部署 HTML Preview 在 Chromium headless 以 1440px Desktop、390px Mobile 檢查六個分頁；12 次切頁均無 JavaScript page error，document/body 寬度均等於 viewport，無水平溢位。已查看六頁縮圖總覽，未見明顯文字／圖示重疊或單位註記擠壓；仍須使用者最終視覺驗收。
8. **GitHub Actions 最新測試已取得 PASS**：Unit Contract Audit run `41382694778` 成功（6 項單位契約測試＋13 項 React 靜態回歸測試）；UI Fixes Regression run `41382694851` 成功（Builder self-tests、React regression、DATA_REPORT parser regression、Dashboard JSON build、借券欄位驗證、非部署 HTML preview 與 fixture artifact 均成功）。
9. **缺值顯示邏輯已修正**：市場廣度缺值不再預設為 0；融資／融券／借券缺值保留 null；圖表及文字顯示 unavailable，維持率缺值不再呈現空量條或假方向箭頭。
10. **借券賣出資料鏈已驗證**：最新 Builder 預覽 JSON 含 borrowedSell=36,178 張、borrowedSellDiff=-1,273 張及範圍註記「上櫃（上市 TWT93U 未取得）」；較舊的已提交 JSON 快照缺少這些欄位，最新產出已補正。\n11. **Builder 區塊數文件已對齊 42**：先前 41 的描述已修正；42 區塊表格編號完整性測試通過。

## 5. 重要欄位語義提醒

- 期貨價格／高低收／價差／夜盤變化：點；成交量、OI、法人淨口數：口；漲跌幅：%。
- 選擇權 Call／Put 成交量與 OI：口；PCR 為 Put OI / Call OI，單位倍；Call Wall、Put Wall、Gamma Wall、Gamma Flip、Max Pain：點。
- PCR 卡片需分開呈現 OI PCR 與 Call／Put 成交量結構。不可把成交量占比當成 PCR。
- 殖利率水準與日變化使用不同單位（% 與 pp）。
- 混合單位圖表需對每個序列分別標示，不能用單一含糊註記涵蓋。
- GEX 履約價標點；GEX 數值單位為 NT$／標的價格變動 1%，模型品質及資料日期需另列。
- 不得把情境權重或未校準數值包裝成統計機率。

## 6. 驗收狀態

| 項目 | 狀態 | 說明 |
|---|---|---|
| 單位標準與文件初版 | 已修改 | 文件已新增／更新，完整性仍待逐項複核 |
| Builder 單位／解析鏈 | PASS（主要欄位）／限制已註明 | UI Regression 的 Builder self-tests、DATA_REPORT parser regression、JSON build 與借券欄位驗證成功；期貨／選擇權部分單位依章節 schema，不是每列後綴 regex |
| 42 區塊對照表 | PASS（結構與主要 JSON path） | 1–42 區塊已補 JSON path、DATA_REPORT 來源章節、單位與缺值說明；少數分析衍生卡片依分析層欄位集合對應 |
| 圖表單位註記程式碼 | PASS（靜態＋實際渲染） | 所有實際 chart 元件相鄰 chartNote 靜態檢查通過；`V` 元件在圖表下方顯示註記，六頁桌面／手機預覽已實際檢查 |
| GEX 數值單位 | PASS（公式＋DATA_REPORT 14A） | Worker 公式量綱與 DATA_REPORT 單位欄一致：NT$／標的價格變動 1%；非 TAIFEX 官方欄位 |
| GitHub Actions 測試 | PASS | Unit Contract 5+13 項通過；UI Regression 全部步驟通過 |
| Desktop／Mobile 技術渲染 | PASS（12 個頁面狀態） | 六分頁 × Desktop 1440px／Mobile 390px；無 JS page error、無水平溢位；未見明顯標籤重疊 |
| 使用者最終視覺驗收 | NOT DONE | 必須由使用者確認 |

## 7. 下一步（按順序執行，不需逐項詢問）

1. 完成 42 區塊逐欄位矩陣：每個區塊逐一連到實際 JSON path、Builder parser、DATA_REPORT 欄位、單位、缺值策略與圖表註記。
2. 已取得成功 Actions；後續若修改程式或測試，必須重新跑兩條 workflow。
3. 完成 Desktop 六頁與 Mobile 六頁實際預覽，檢查文字、數值、圖例、單位註記、圖示重疊／裁切／換行；若 Chromium headless 不穩，改用 Actions preview artifact 的可用方式，不部署。
4. 再核對混合單位圖表（特別是綜合頁三市場法人、期貨 OI／日夜交易及選擇權法人表）之每一序列單位與縮放因子。
5. 將本次 GEX 公式量綱推導與資料來源說明納入最終稽核紀錄；若 Worker 公式未來變更，必須同步重新驗證單位。
6. 目前已確認 `yf` 僅用於 Call／Put 成交量結構，現貨成交額使用 `Ol`；Regression 測試已覆蓋此區分。
7. 保持不部署、不修改其他分支；完成以上後更新 Recovery 並請使用者作最後視覺驗收。
8. 完成程式與文件修正後，再交由使用者做最後 Dashboard 視覺驗收。

## 8. 工作方式

- 本對話只有單一模型；可以做 Supervisor／Worker／Auditor 分工式自我檢查，但不得宣稱已委派獨立模型。
- 發現問題後直接修正並複驗；避免每一小項都停下來要求使用者確認。
- 不擴大需求，不改資料策略或業務邏輯，除非修正單位契約必須且有明確證據。
- 所有 GitHub 寫入限定 `phase2-p0-ui-fixes`；不部署、不合併。
- 最終報告分列：已完成、已驗證、BLOCKED、NOT TESTED、尚未完成。

## 9. 2026-11-02 後續視覺缺陷與 GEX 修正（本節優先於舊段落）

### 9.1 三個圖表裁切

- 使用者最後確認僅有三個圖表顯示不完整：日夜法人交易、前十大選擇權、履約價 GEX 分布。
- 目前分支 React Template 的共用 Canvas `Hn` 已採動態高度：`Math.max(n,e.length*46+48)`；圖表容器使用 `minHeight:180px; overflow:visible`。
- `tests/test_react_template_static.py` 已有 `test_all_three_ranked_charts_expand_without_container_clipping`，覆蓋共用 Canvas 高度、容器、三個區塊及 GEX 前 16 筆排序。
- 上述程式／靜態測試可在目前分支確認；本次最新 Actions 預覽尚未重新完成桌面／手機實際視覺驗收，因此不可標示為最終視覺 PASS。先前截圖可能來自舊預覽，必須用本次新 Artifact 再確認。

### 9.2 Bias 卡片 GEX unavailable 根因與修正

- DATA_REPORT `data_reports/DATA_REPORT_20261030.md` 的 14A 區段包含 GEX_LEVELS_JSON：日期 2026-10-30、quality=`usable`、139 筆 levels、Net GEX 1,294,327,419.009、Gross GEX 6,320,130,202.133。
- 逐筆 Net GEX 加總與整體 Net GEX 相符；逐筆 Gross GEX 加總與整體 Gross GEX 相符。
- Builder `scripts/v9_pro_builder.py` 已具備解析 GEX_LEVELS_JSON 並映射至 `options.netGex1pct`、`grossGex1pct`、`gexLevels`、`gexDate`、`gexStatus` 的程式。
- 目前已提交的 `dashboards/data-20261030.json` 是舊快照（meta.generated_at=`2026-11-01 12:32:04`），而目前 DATA_REPORT 產出時間為 `2026-11-01 23:51:51`；舊 JSON 的 options 物件沒有 GEX 欄位。因此這是 DATA_REPORT 更新後 Dashboard JSON 未同步重建的資料快照問題。
- React Bias 卡片另有硬編碼 `GEX unavailable`（pill 與 footer），即使 options 有 GEX 欄位也不會顯示。已改為讀取 `options.gexStatus` 與 `options.netGex1pct`，available 時顯示 Net GEX 十億 NT$ 簡寫，unavailable 才保留 unavailable。
- 本次程式提交：
  - Template 動態 GEX：`86babbadf8ed63cdadd0252ecf5ba9eaaea5a512`
  - Bias GEX 靜態回歸測試：`1574e4a144f4ac55091759faadd9c020be745f70`
  - Builder→Dashboard GEX 整合驗證：`2871ed8de461dcd1345e2d2b1a6b3d41359d19c0`
- UI Regression workflow 已增加建置後驗證：GEX status/date/139 筆、Net/Gross 總額及逐筆加總。此 workflow 會以目前 DATA_REPORT 重建隔離的預覽 JSON／HTML，不直接覆寫正式 dashboard，也不部署。

### 9.3 本次狀態

| 項目 | 狀態 | 證據／限制 |
|---|---|---|
| GEX DATA_REPORT payload | PASS（資料存在） | 139 筆、quality usable、總額與逐筆加總一致 |
| 舊 Dashboard JSON | FAIL（已定位） | JSON generated_at 早於 DATA_REPORT 更新，options 缺 GEX 欄位 |
| Builder GEX parser／mapping | PASS（程式碼存在） | Parser 與輸出 mapping 已檢查；新 workflow 將實際建置後再驗證 |
| Bias 卡片硬編碼 | FIXED（程式已提交） | 兩處改為動態讀取 options GEX 欄位；CI 尚待結果 |
| 三圖表動態高度 | PASS（程式／靜態測試存在） | 最新 Artifact 的實際渲染尚未驗收 |
| 最新 UI Regression | NOT TESTED | 本次 commit 已觸發 push workflow；目前未取得 run/job 結果 |
| 新預覽手機／桌面視覺 | NOT TESTED | 待取得本次 workflow Artifact 後驗收 |
| Merge／部署 | NOT DONE | 按既定要求維持分支隔離 |

### 9.4 下一步

1. 查收本次 `V9 UI Fixes Regression` Actions；確認 Builder self-test、React static regression、DATA_REPORT parser regression、GEX pipeline assertions 全部 PASS。
2. 下載本次新產生的 `V9-UI-Fixes-Preview-20261030` Artifact；確認 Bias pill 顯示實際 Net GEX，不再硬編碼 unavailable。
3. 以新 Artifact 檢查手機／桌面三個圖表是否完整呈現；若仍裁切，根據實際 DOM／Canvas 尺寸定位，不再只調整猜測高度。
4. 將最終 Actions 證據與視覺驗收結果更新本 Recovery；不修改 Master／V8，不 Merge、不部署。
### 9.5 Template 完整性複驗與顯示單位調整

- Template 已重建為單一完整 HTML 文件，檢查結果：242,532 字元、僅 1 個 `<!DOCTYPE html>`；Canvas 動態高度與 Bias GEX 動態欄位均存在。
- Bias GEX 值改用台灣常用億元單位顯示，例如本次 DATA_REPORT 的 Net GEX 約 `+12.94 億 NT$`；避免顯示過長的 1,294,327,419 數字或不直觀的 B 單位。
- Template 完整性修復提交：`bd5b0c10ba0af2085b7b15a47c394770115c02ad`。
- GEX 顯示單位回歸測試提交：`c2ec5fc12ff91750c7e91ff46e2ad3d1c64ade94`。
- 以上只完成程式與靜態結構檢查；仍待 Actions 執行結果與最新 Artifact 的實際渲染驗收。

## 9.6 2026-11-02 最終修正與回歸驗收（歷史狀態；目前以 9.7 為準）

### 修正內容
- GitHub Actions 首次執行失敗並非圖表 runtime error，而是新增靜態測試與實際模板不一致：
  - 測試錯誤要求 style:{minHeight:"180px",overflow:"visible"}。
  - 實際共用卡片元件 V 使用 style:{minHeight:"180px"}；卡片高度由內容自然撐開。
  - 測試另錯誤要求模板中存在兩句不存在的 GEX 圖表說明文字。
- 已修正 tests/test_react_template_static.py：改驗證真實存在的卡片容器、Canvas 動態高度 Math.max(n,e.length*46+48)、GEX 圖表真實單位註記與高度設定，不再檢查不存在的文字。
- 最新測試修正提交：8506e5f9dbe8e891124937b9d63ad009788e3c00。

### GitHub Actions 最終結果
| Workflow | Run ID | 結果 | 關鍵步驟 |
|---|---:|---|---|
| V9 Pro Unit Contract Audit | 41386619948 | PASS | Python compile、Dashboard unit contract、React template regression |
| V9 UI Fixes Regression | 41386620098 | PASS | Builder self-test、React regression、DATA_REPORT parser regression、JSON build、borrowed securities assertions、GEX pipeline assertions、non-deploy HTML preview、fixture artifact |

- UI Regression Artifact：V9-UI-Fixes-Preview-20261030，Artifact ID 13114794682。
- Build 後 GEX 驗證：status available、date 2026-10-30、139 levels；Net GEX 約 1,294,327,419.01 NT$；Gross GEX 約 6,320,130,202.13 NT$；逐筆加總與總額相符。
- 先前失敗 run 已定位為靜態測試契約錯誤；最後修正後兩條 workflow 均 PASS。

### 預覽實際渲染檢查
- 從本次 Actions Artifact 下載 HTML，使用 Chromium headless 實際載入。
- Desktop 1440px：
  - 期貨頁「日夜法人交易」圖表可完整顯示。
  - 選擇權頁「前十大選擇權」及「履約價 GEX 分布」圖表可完整顯示；GEX 前 16 筆圖表高度 784px，卡片高度 1149px，無垂直裁切。
  - GEX 數值顯示 Net 1,294,327,419 NT$ / 1%、Gross 6,320,130,202 NT$ / 1%；不再顯示 unavailable。
- Mobile 390px：
  - 期貨頁「日夜法人交易」與選擇權頁兩張目標圖表均完整呈現；GEX 前 16 筆 Canvas 高度 784px，卡片高度 1276px，無垂直裁切。
  - 390px viewport 的主內容寬度與 viewport 相同，未發現水平溢位。
  - Overview Bias 卡片顯示 GEX +12.94億 NT$，不再顯示 GEX unavailable。
- 本次 Chromium 檢查的已載入頁面未發生 JavaScript page error。
- 視覺驗收範圍限本次三張目標圖表及 Overview GEX Bias；未宣稱六頁全部完成全量人工視覺驗收，其他頁仍可由使用者最後確認。

### 仍需保留的限制
- 分支內舊快照 dashboards/data-20261030.json 仍是較早產出的版本（generated_at=2026-11-01 12:32:04），缺少 GEX 欄位；本次 Actions 以最新 DATA_REPORT 建立的隔離預覽 JSON／HTML 已正確，但未覆寫正式快照。
- 正式 dashboard build workflow 目前只在 master 與 phase2-p0-data-quality 的 push／schedule 執行；本階段明確不 merge、不部署、不改其他分支，因此不能宣稱目前正式發布頁面已更新。
- 目前已完成的是修正後分支程式、測試與隔離預覽；正式頁面更新需依使用者後續批准的正常 build／發布流程進行。

### 最終狀態
| 項目 | 狀態 |
|---|---|
| 三張指定圖表動態高度／卡片容器 | PASS（程式、CI、Desktop／Mobile 實際渲染） |
| Bias GEX 動態顯示 | PASS（Builder JSON、CI、Desktop／Mobile 預覽） |
| GEX 139 筆資料與總額驗證 | PASS |
| Unit Contract Audit | PASS |
| UI Fixes Regression | PASS |
| 本次指定區塊 JavaScript runtime | PASS（無 page error） |
| 六頁全部完整視覺驗收 | NOT TESTED |
| 舊 committed JSON snapshot 更新 | NOT DONE |
| Merge／部署／正式頁面更新 | NOT DONE（遵守不 merge、不部署） |


## 9.7 2026-11-02 舊快照重建、K 線單位標籤缺陷修正與全頁複驗（目前最新）

### A. 舊 JSON／HTML 快照已重新建置
- 已修改 .github/workflows/daily-premarket-v9-pro.yml：
  - 增加 phase2-p0-ui-fixes push 分支允許清單。
  - 生成 dashboard 歷史檔的 commit guard 只允許 phase2-p0-data-quality 與 phase2-p0-ui-fixes。
  - deploy job 條件未放寬；本分支建置後 deploy 仍為 skipped，不會部署。
- 最新成功完整建置 Workflow：Run ID 41390676168，Commit SHA 8ec4fb28a28c113a418ead43bad3d631cd11a6c4；build job PASS，deploy job SKIPPED。
- Builder 使用最新 DATA_REPORT_20261030.md（產出時間 2026-11-01 23:51:51）重新產生：
  - dashboards/data-20261030.json
  - dashboards/data-latest.json
  - dashboards/v9-pro-20261030.html
  - dashboards/v9-pro-latest.html
  - dashboards/index.html
  - dashboards/manifest.json
- 新 JSON 的 meta.generated_at 已更新為 2026-11-01 23:51:51；options.gexStatus=available、gexDate=2026-10-30、gexLevels=139。
- Net GEX = 1,294,327,419.0091748 NT$；Gross GEX = 6,320,130,202.132608 NT$；兩組逐履約價加總與總額完全一致。
- 借券欄位同時已生成：borrowedSell=36,178 張、borrowedSellDiff=-1,273 張、scope 為 上櫃（上市 TWT93U 未取得）。
- 最新 HTML 的資料注入存在，且 GEX 動態欄位可用；程式碼中仍保留 unavailable fallback 字串是正常條件分支，實際渲染不顯示 unavailable。

### B. 新發現並修正：K 線成交量單位變數遮蔽
- 最新完整建置 HTML 的實際畫面發現，期貨／現貨 K 線圖成交量標籤錯誤，例如手機顯示 VOL 73,987149.4、桌面顯示 VOL 73,987301.5，未顯示應有的「口」。
- 根因：Canvas 元件 Pt 的 props 將 volUnit 別名為 a，但繪圖 callback 又宣告局部變數 a=d*0.45 作為 K 線 x 座標，覆蓋了外層單位標籤。成交量標籤因此拼接 Canvas 座標，而不是單位。
- 修正：props 改用 volUnit:unitLabel="口"，繪圖時使用 unitLabel；座標變數維持獨立。
- 新增回歸測試：
  - tests/test_react_template_static.py：test_candlestick_volume_unit_is_not_shadowed_by_canvas_coordinate
  - tests/test_dashboard_unit_contract.py：增加相同契約斷言。
- 最新模板已由完整建置 Workflow 重建進 HTML；Desktop／Mobile 截圖已確認期貨日盤成交量標籤顯示 VOL 73,987 口，不再出現 301.5／149.4 座標數字。夜盤亦正確顯示口數單位。

### C. 42 區塊單位對照表修訂
- docs/DASHBOARD_UNIT_MAP.md 更新至 1.1：
  - 修正區塊 9 上櫃欄位路徑為 spot.otc.up/down/flat/limit_up/limit_down，不再使用錯誤的 spot.otc_*。
  - 修正區塊 36、37 對選擇權法人交易口數與法人多空力道金額的欄位／單位界線。
  - GEX 單位不再標 BLOCKED；統一為 NT$／標的價格變動 1%。
  - 明確區分 parse_data_report()、build_final_json()、build_41_cards() 三層資料處理責任。
  - 明列市場匯率報價方向、商品報價單位、殖利率 % 與 pp、缺值與相關性樣本不足的顯示策略。
- tests/test_dashboard_unit_contract.py 增加對區塊 9 正確 JSON path、Parser 層級及 GEX 單位狀態的文件回歸斷言。

### D. 最新 GitHub Actions 結果
| Workflow | Run ID | Commit | 結果 |
|---|---:|---|---|
| V9 Pro Unit Contract Audit | 41390676026 | 8ec4fb28a28c113a418ead43bad3d631cd11a6c4 | PASS |
| V9 UI Fixes Regression | 41390676167 | 8ec4fb28a28c113a418ead43bad3d631cd11a6c4 | PASS |
| Daily Premarket V9 Pro | 41390676168 | 8ec4fb28a28c113a418ead43bad3d631cd11a6c4 | Build PASS；Deploy SKIPPED |

- 另有相同最新模板修正後的 Unit Contract run 41390259701 PASS、UI Regression run 41390259678 PASS、完整 Build run 41390259700 PASS；最新一輪 413906* 已包含 42 區塊文件修正並再次通過。
- 先前 41390201664 失敗原因為舊單位測試仍期待舊變數別名 volUnit:a；已同步更新兩份測試，後續 41390259701 與 41390676026 均 PASS。

### E. 最新完整 HTML 技術渲染驗證
- 使用最新完整 Pages Artifact 的 p0/v9-pro-20261030.html，Chromium headless 實際載入。
- Desktop 1440px 六頁均已切頁檢查；各頁主內容非空、畫布數量符合預期、document/body scrollWidth 均為 1440px。
- Mobile 390px 六頁均已檢查；各頁主內容非空、document/body scrollWidth 均為 390px。六頁 Canvas 數量與 Desktop 相同：
  - 總覽 14
  - 現貨 6
  - 重要市場 7
  - 期貨 6
  - 選擇權 8
  - 綜合分析 7
- 指定三張圖表最新完整建置版實際高度：期貨日夜法人圖表正常；選擇權前十大圖表依資料列展開；GEX 前 16 筆 Canvas 高度 784px，未裁切。
- GEX Overview Bias 顯示 GEX +12.94億 NT$；選擇權 GEX 區塊顯示 139 筆及正確總額。
- K 線成交量標籤 Desktop／Mobile 均顯示正確單位，不再輸出 Canvas 寬度座標。
- 已檢查的頁面無水平溢位；Browser pageerror 未觀察到 JavaScript runtime error。
- 本節為技術渲染驗證，不代替使用者最終人工視覺驗收。

### F. 目前狀態
| 項目 | 狀態 |
|---|---|
| 舊 JSON 快照重建 | PASS |
| 最新 HTML／latest alias／index／manifest | PASS（分支已提交） |
| GEX 資料 139 筆、總額、逐筆加總 | PASS |
| 借券賣出餘額與增減欄位 | PASS |
| 三張指定圖表高度與裁切 | PASS |
| K 線成交量單位標籤變數遮蔽 | FIXED + PASS（回歸測試、Desktop／Mobile 實際畫面） |
| 42 區塊結構及主要路徑 | PASS（文件與測試） |
| 六頁 Desktop／Mobile 技術渲染 | PASS（12 個分頁狀態） |
| 六頁每一個欄位逐欄人工語義審查 | NOT TESTED（單位矩陣及自動契約已覆蓋主要欄位；仍需針對新資料來源變更持續審核） |
| 使用者最終視覺驗收 | NOT DONE |
| Merge／正式部署 | NOT DONE（deploy job 已明確 SKIPPED；未修改 Master／V8） |

## 9.8 2026-11-02 完整 42 區塊欄位語義稽核（目前最新）

### A. 稽核交付文件
- docs/DASHBOARD_UNIT_MAP.md：升級至 1.2，新增 42 區塊逐項語義稽核矩陣、缺陷清單與模型限制。
- docs/DASHBOARD_UNIT_STANDARD.md：升級至 1.1，新增正負號、存量／流量、GEX 模型假設、T0 as-of 與歷史相似結果語義。
- docs/DASHBOARD_UNIT_REGISTRY.json：升級至 1.2，補充 GEX、OI／flow、歷史相似結果、技術指標來源與時間邊界。
- docs/DATA_REPORT_TEMPLATE.md：修正現貨 OHLC 來源註記；收盤／漲跌／成交金額由 twse-proxy，開高低由 FinMind TAIEX，分別保留來源。
- 42 區塊表格為程式契約與樣本資料的語義核對結果；不代表上游供應商原始資料正確性或交易策略預測力已通過獨立驗證。

### B. 已修正的欄位／分析語義缺陷
1. **T0 look-ahead leakage**：
   - Yahoo 歷史 K 線以 Asia/Taipei 日期過濾至 DATA_REPORT T0。
   - FinMind 查詢 end_date 改為 T0，並再次過濾日期。
   - SQLite 技術資料只讀 date <= T0。
   - RSI、MACD、KD、SMA 與 spot5 使用同一份 T0 截斷序列。
   - 歷史因子學習與相似樣本只讀 date < T0；相關性只讀 date <= T0。
2. **GEX 欄位路徑與方向性**：
   - 分析器原先讀取不存在的 options.gex；改讀 options.netGex1pct。
   - GEX 數值仍顯示於卡片，但因 OI-based Black-Scholes GEX 的 Call／Put 正負是模型假設，且不是已知造市商實際庫存，正負不等於市場多空方向；因此暫不納入 Bias。
3. **美股廣度與來源缺值**：
   - VIX 排除於股票指數全漲／全跌統計。
   - SOX 缺值不再預設為 0。
   - DXY 獨立顯示，不混入股票指數廣度。
4. **Regime 敘述**：
   - 原程式依單日漲跌幅、外資現貨與 OI PCR 判斷，文字卻稱跌破／站上月線；已改為列出實際判斷條件。
5. **存量／流量量綱**：
   - 前十大淨 OI 是部位存量，外資日盤淨交易是區間流量；取消兩者直接相減與「對作差額」敘述。
   - 現貨、期貨、選擇權三市場一致性只比較方向，不比較不同量綱絕對值。
6. **固定多空文字**：
   - 現貨三法人、外資選擇權日夜盤、三市場一致性及外資期貨描述改依實際數值產生。
   - 資料缺漏時顯示資料不足，不補造中性或方向。
7. **歷史相似分析**：
   - 原 win_rate 實際計算隔日負報酬比例，非策略勝率。
   - 改為 positive_rate／negative_rate，卡片顯示隔日上漲比例及下跌比例。
8. **新聞解析**：
   - 修正從事件 1 標記開始解析，避免第一則新聞被跳過。
   - 支援「原文連結」欄位，保留新聞時間與 URL。
9. **技術水位命名**：
   - 當日最高／最低不再錯標 R3／S1；改為當日高點／當日低點。
10. **缺值與來源描述**：
   - 基差比例與夜盤變化缺值改保留 None/null，不再預設 0。
   - JSON data_source 改輸出實際技術歷史來源。
   - 內部分析卡數量新增 analysis_card_count；42 個可見區塊另以 visible_block_count 表示；舊 cards_41_count 僅保留相容性。

### C. 回歸測試新增
tests/test_builder_option_tables.py 新增：
- 第一則新聞、12 則新聞數量、原文連結與時間。
- T0 截斷測試：未來日期不得進入歷史序列。
- 缺少基差比例／夜盤變化時保留 None。
- GEX 有值但不應被當成方向性 Bias 因子。
- VIX 不得混入股票指數廣度；SOX unavailable 不得默認 0；DXY 獨立。
- 三市場方向及選擇權日夜盤方向依真實 flow 產生。
- 前十大 OI 與外資日盤 flow 不直接相減。
- 歷史學習、相似樣本與相關性排除 T0 之後資料。
- 歷史相似結果顯示上漲／下跌比例，不再標勝率。

tests/test_dashboard_unit_contract.py 新增：
- 42 區塊稽核矩陣數量與狀態。
- GEX、歷史結果、技術指標語義註冊表契約。
- T0 與 GEX 非方向性規則文件契約。

.github/workflows/unit-contract-audit.yml 已納入 test_builder_option_tables.py。

### D. 最新 GitHub Actions（2026-11-02）
- V9 Pro Unit Contract Audit Run 41393233848：PASS（Commit 8d08df0504d378c2d3f2592802062e83bd37c8fa）。
- V9 UI Fixes Regression Run 41393233879：PASS（同一 commit）。
- Daily Premarket V9 Pro Run 41393233928：Build PASS（同一 commit）；Deploy SKIPPED。
- 先前 commit 86fdc41f99b001d4989cdbb378137ee009b825b6 的 Unit Contract、UI Regression 與 Daily Premarket Build 均 PASS；其中新增的語義測試已包含在該輪 UI Regression。
- Commit 2f272eacaf1a2017ef61709c69979d63b1a75f5e 的 Unit Contract 曾因測試 regex 過度跳脫而 FAIL；已修正 regex，commit 9db471be1a18086d3e472ffc228ab463a4abb489 的 Unit Contract 已 PASS。

### E. 仍需明確保留的限制
- **上游資料真實性：NOT TESTED**。已驗證欄位、日期、單位與可檢查的算術關係；未逐筆向每一個供應商原始 API 獨立對帳。
- **策略預測力：NOT TESTED**。PCR、RSI、外資 OI 等因子門檻屬既定啟發式規則；須累積無前視偏誤樣本並進行 walk-forward 回測，才能評估有效性。
- **GEX 造市商真實庫存：NOT TESTED／不可由現有 OI 推定**。本模組僅是 OI-based Black-Scholes 模型曝險估值。
- **最終 42 區塊使用者視覺驗收：NOT DONE**。
- **Merge／正式部署：NOT DONE**。未修改 Master／V8，未合併及部署。

### F. 本階段驗收狀態
| 項目 | 狀態 |
|---|---|
| 42 區塊欄位／單位／正負號／存量流量語義矩陣 | PASS（文件與程式契約） |
| T0 技術資料及歷史資料防前視 | PASS（新增回歸測試、最新 UI／Build 均通過） |
| GEX 非方向性與資料路徑 | PASS（新增回歸測試） |
| 新聞、缺值、法人／三市場敘述 | PASS（新增回歸測試） |
| Unit Contract Audit 最新 commit | PASS |
| UI Regression 最新 commit | PASS（41393233879） |
| Daily Premarket V9 Pro 最新 commit | PASS（41393233928；Deploy SKIPPED） |
| 上游 API 每筆原始資料獨立對帳 | NOT TESTED |
| 因子策略預測力／walk-forward 回測 | NOT TESTED |
| 使用者最終視覺驗收 | NOT DONE |
| Merge／正式部署 | NOT DONE |

### G. 最終複驗補充（2026-11-02；Commit 8d08df0504d378c2d3f2592802062e83bd37c8fa）
- 先前 41393146802／41393146823 失敗原因是 Builder self-test 仍檢查舊字串「缺失」；因摘要改成區分「缺值」與「有值停用」，已同步修正 self-test，沒有略過或停用測試。
- 最新三個 Workflow：
  - Unit Contract Audit 41393233848：PASS。
  - UI Fixes Regression 41393233879：PASS；Builder offline self-tests、React template regression、DATA_REPORT parser regression、JSON／借券欄位驗證、非部署 HTML 預覽及相關性 fixture 均 PASS。
  - Daily Premarket V9 Pro 41393233928：Build PASS；deploy job SKIPPED。
- 最新非部署 artifact 已實際解壓與核對：
  - p0/v9-pro-20261030.html（317,862 bytes）。
  - p0/data-20261030.json（91,810 bytes）。
  - T0=2026-10-30；技術序列 18 筆，spot5Dates 最後日期 10/30；沒有 11/02 未來日期。
  - technical_history=yahoo (T0 filtered)；historical_learning=SQLite db。
  - 新聞 12 則，首則及原文 URL 正確。
  - GEX available、139 levels；Net GEX 1,294,327,419.009 NT$／1%；Gross GEX 6,320,130,202.133 NT$／1%。
  - factor_quality active=12/17；missing_factors 為 yield、volume、ma_bias、macd；disabled_factors 僅 gex。GEX 有數值但不納入方向性 Bias，狀態不再誤標為缺值。
  - 前十大 OI 與外資日盤淨交易不再直接相減；選擇權外資日盤 +6,624 口、夜盤 -94 口，卡片正確顯示日夜分歧。
  - analysis_card_count=48 是內部分析敘述卡數；visible_block_count=42 是使用者定義的可見 Dashboard 區塊數；cards_41_count 僅為相容舊版的 alias。
- 最新 artifact 的本輪實際瀏覽器截圖驗收：NOT TESTED（目前執行環境阻擋 localhost／file 頁面導航）；最新 CI 的靜態、Builder、資料解析與 HTML 預覽測試均 PASS。此前版本的六頁 Desktop／Mobile 技術渲染紀錄仍保留於 9.7。
- 最新 Recovery 文件更新後，分支 head 會再前進一個文件提交；上述程式驗證均對應 8d08df0504d378c2d3f2592802062e83bd37c8fa。
## 9.9 最終欄位語義抽樣複核與交付（2026-11-02）

### A. 最新 CI 狀態確認
- V9 UI Fixes Regression Run **41393233879**：completed / success，job regression PASS。
- V9 Pro Unit Contract Audit Run **41393233848**：completed / success。
- Daily Premarket V9 Pro Run **41393233928**：completed / success；Build PASS，Deploy SKIPPED（本分支不正式部署）。
- 三者對應 commit：8d08df0504d378c2d3f2592802062e83bd37c8fa。

### B. 最新 artifact 實際資料複核
- 由 Run 41393233928 的 github-pages artifact（ID 13117683797）下載並解壓，實際複核 p0/data-20261030.json 與 p0/v9-pro-20261030.html。
- HTML：317,862 bytes；JSON：91,941 bytes；T0=2026-10-30；報告產出時間 2026-11-01 23:51:51（Asia/Taipei）。
- 42 個可見區塊；內部 analysis cards 為 48，兩者用途不同，不能將 48 當成可見區塊數。
- 技術歷史來源 Yahoo；18 筆收盤序列；spot5 最後日期 10/30，沒有 T0 之後日期。
- MACD／MACD signal／hist 為 null，因可用歷史序列不足；相應 MACD 因子列入 missing，不以 0 代替。RSI=32.85、K=20.98、D=20.46。
- PCR：Put OI 59,945 ÷ Call OI 98,551 = 0.6083，顯示 0.61，符合定義。
- GEX：139 個履約價；Net GEX 1,294,327,419.009 NT$／1%；Gross GEX 6,320,130,202.133 NT$／1%。逐履約價 Net 加總與總值差約 0.0000012 NT$（浮點加總誤差）；Gross 加總差 0。
- 法人現貨：外資 -1,124.7 億、投信 +236.2 億、自營商 -513.7 億，合計 -1,402.2 億，算術一致。
- 成交金額：上市 9,396.1 億 + 上櫃 1,987.7 億 = 11,383.8 億；顯示總額 11,383.7 億，差 0.1 億，屬各欄位先四捨五入後再顯示造成的精度差。這不是精確相等；若後續需要嚴格對帳，應以未四捨五入原始值計算總額，再統一顯示精度。
- 新聞 12 則；第一則新聞有標題、發布時間與原文 URL。
- 因子品質：active 12/17；missing 為 yield、volume、ma_bias、macd；disabled 僅 gex；有效權重正規化總和 100%。GEX 有數值但不參與方向評分，未被誤列為缺值。
- 融資維持率顯示 171.75%，狀態 estimated_t0；來源說明上市自建估算 1,238 檔，4 檔使用最近有效收盤價，並有 Blave 同 T0 交叉驗證。此為估算口徑，不宣稱全市場逐檔當日價格完整。
- 借券賣出 36,178 張、增減 -1,273 張，明確註記上櫃範圍；上市 TWT93U 未取得，不冒稱全市場。

### C. 最終驗收分類
| 項目 | 狀態 | 說明 |
|---|---|---|
| 42 區塊欄位／單位／來源／正負號文件矩陣 | PASS | 文件及自動契約測試通過 |
| Builder／JSON 主要欄位與公式 | PASS | 最新 artifact 實值抽樣複核 |
| T0 防前視邊界 | PASS | 日期序列截至 2026-10-30 |
| GEX、PCR、法人合計、新聞、因子狀態 | PASS | 最新 JSON 實值核對 |
| 成交金額分項與合計 | PASS with rounding note | 顯示值差 0.1 億；需保留原始精度才能精確核對 |
| 上游供應商逐筆原始 API 對帳 | NOT TESTED | 本次未逐筆對外部供應商原始端做獨立對帳 |
| 因子預測力／walk-forward | NOT TESTED | 語義正確不等於策略有預測力 |
| 最新 artifact 的實際瀏覽器六頁 Desktop／Mobile 完整人工視覺驗收 | NOT TESTED | 最新 artifact 已核對檔案與 JSON；本次未完成可靠的瀏覽器互動全頁複驗 |
| 使用者最後視覺確認 | NOT DONE | 需由使用者開啟最新 HTML 確認 |
| Merge／正式部署 | NOT DONE | Deploy SKIPPED；未碰 Master／V8 |

### D. 交付檔
- 最新 Dashboard HTML：p0/v9-pro-20261030.html（317,862 bytes）。
- 同版 JSON：p0/data-20261030.json（91,941 bytes）。
- 下載交付使用者的獨立 HTML 檔以本次對話提供的下載連結為準；它是 Run 41393233928 的 artifact 原檔，不是重新拼裝或手動改寫版本。


## 9.10 六頁瀏覽器自動驗收工作流（2026-11-02）

### A. 已新增的自動化
- 新增 `.github/workflows/dashboard-browser-audit.yml`，限定 `phase2-p0-ui-fixes` 分支，支援 push 與 workflow_dispatch；不部署、不修改 Master／V8。
- 新增 `tests/browser_dashboard_audit.mjs`，使用 Playwright + Chromium：
  - Desktop 1440×1000 與 Mobile 390×844。
  - 逐一點擊總覽、現貨、重要市場、期貨、選擇權、綜合分析六頁。
  - 每頁檢查主內容非空、至少一個可見 Canvas、document/body 不得水平溢位。
  - 收集 pageerror；輸出 12 張截圖及 report.json 作為 Actions artifact。
- Workflow 會自動挑選 dashboards/ 中最新日期版 `v9-pro-*.html`，不再固定寫死 2026-10-30。

### B. 本次提交
- Browser audit script：commit `217b4d2de4da7528bed6af86a236d8c59519ad92`。
- 初版 workflow：commit `5a317fe9c500e52a9ecf12f73b35d476cfe7d28f`。
- 動態選取最新 Dashboard HTML：commit `d0ef8ed3a31d4aadf34e7d09f9cff0f5dcd127a0`。
- 分支：`phase2-p0-ui-fixes`。

### C. 驗收狀態（務必區分）
| 項目 | 狀態 | 說明 |
|---|---|---|
| Playwright 測試程式已提交 | PASS | GitHub fetch_file 已讀回確認 |
| Actions workflow 已提交 | PASS | GitHub fetch_file 已讀回確認 |
| 六頁 × Desktop/Mobile 實際 Chromium 執行 | NOT TESTED | 本次工具環境未提供 workflow dispatch／run listing；不得宣稱 CI 已執行 |
| 12 張新截圖與 report.json | NOT GENERATED | 等待 workflow 真正執行成功 |
| 使用者視覺驗收 | NOT DONE | 仍待使用者確認 |

### D. 執行注意事項
- Workflow 自動由分支 push 觸發；若未觸發，可在 GitHub Actions 手動執行「V9 Dashboard Browser Audit」。
- 若失敗，優先查看 artifact 中的 report.json、Actions log 與頁面截圖；不得因 workflow 檔存在就視為瀏覽器驗收通過。
- 目前 workflow 使用最新日期版 HTML；未來每日新 Dashboard 提交到該分支時，會納入相同瀏覽器檢查。


## 9.11 上游來源語義抽查（2026-11-02）

### A. 已確認的來源定義
- TWSE 官方 TWT93U「融券借券賣出餘額」資料表同時列出融券欄與借券賣出欄；借券賣出欄包含前日餘額、當日賣出、當日還券、當日調整、當日餘額及次一營業日可限額，數值單位為股。不能把它與「借券成交／借券餘額（尚未返還借入證券）」混為一談。
- TPEX 官方 OpenAPI 的 `tpex_margin_sbl` 是上櫃股票融券借券賣出餘額資料；其網頁說明借券賣出餘額依前日餘額＋當日賣出－當日還券＋當日調整計算。
- TWSE 官方說明明確區分「借券餘額」與「借券賣出餘額」：借入證券未返還，不等同已賣出尚未回補。外部來源：TWSE TWT93U、TWSE 借券資訊說明、TPEX OpenAPI／借券賣出餘額說明。

### B. 發現的文件／報表口徑風險
- 舊版 `docs/DATA_SOURCES.md` 把上市 TWT96U 寫成可借餘額，並稱上市借券賣出無機器接口；但 TWT93U 官方資料表本身包含借券賣出欄。原規範易讓維護者誤判上市欄位不可用，或把不同存量口徑混用。
- DATA_REPORT_20261030 的借券表將借券餘額、借券賣出餘額、借券賣出增減三欄共用 `TWSE TWT93U + TPEX margin_sbl` 來源標示；同一報告又註明「借券賣出增減僅上櫃值（TWSE TWT93U 未取得）」。兩者在欄位層級不一致，來源欄不能共用一個合併標籤。
- 報告顯示借券賣出餘額 36,178 張、增減 -1,273 張；目前只能確認報告註明增減僅上櫃，尚未取得原始 TWSE/TPEX 回應逐檔重算證據。因此該兩欄的跨市場範圍／總額不得標為已完成獨立對帳。
- 融資維持率報告實際採 TWSE 上市逐檔自建估算（1,238 檔、4 檔最近有效價）並以 Blave 同 T0 交叉驗證；這與舊資料來源規範中「上市櫃整體 iStock」的敘述不一致。已將規範更新為上市估算口徑，禁止標示成上市櫃合計。

### C. 已修改
- `docs/DATA_SOURCES.md` 已更新：
  - 融資維持率明確標為 TWSE 上市自建估算；Blave 僅同 T0 交叉驗證，不冒稱上市櫃合計。
  - 借券拆分存量定義、TWSE TWT93U 欄位、TPEX tpex_margin_sbl 範圍，要求每欄分別標示上市／上櫃可得性；未確認前不把 TWT96U 當 TWT93U 替代。
- Commit：`c9f11c27bd7fce0976d09e5a31f68d5308d2235f`。

### D. 驗收狀態
| 項目 | 狀態 | 說明 |
|---|---|---|
| TWSE/TPEX 借券欄位定義 | PASS | 官方網頁／OpenAPI 說明核對 |
| DATA_SOURCES 維持率與借券規範更新 | PASS | GitHub 讀回確認 |
| DATA_REPORT 借券各欄來源標示 | FAIL | 同一來源標籤與「僅上櫃」註記互相矛盾，需修正產生器 |
| TWT93U/TPEX 原始回應逐檔加總與報表數字 | NOT TESTED | 尚未取得同 T0 原始回應及重算結果 |
| BFI82U / TPEX / TWSE 其他欄位原始值逐筆對帳 | NOT TESTED | 後續逐來源執行 |
| 六頁瀏覽器實際執行 | NOT TESTED | 仍待 Actions 結果 |


## 9.12 2026-11-02 借券來源標籤修正

### 根因
- `src/sources/spot.py` 原本將借券餘額、借券賣出餘額、借券賣出增減共用 `sources["sbl"]`，但三者實際來源與市場涵蓋範圍不同。
- `src/fetch_data.py` 將同一個來源標籤套用至三列，當上市 TWT93U 未取得時，仍可能把上櫃數值標示成上市＋上櫃，造成來源範圍誤導。

### 已提交修正
- `src/sources/spot.py` 改為分別輸出 `sbl_bal`、`sbl_sale_bal`、`sbl_sale_chg` 來源標籤；只把實際非空的市場來源列入標籤。
- `src/fetch_data.py` 借券表格三列各自使用對應來源標籤，並說明缺值市場不納入加總。
- Commit：`58df9767f6dcdffbb82dabb2262ff0b4292793d3`（spot source mapping）；`c0d2e2f44bdec7509c3540025ae853e052425052`（report output）。

### 驗收
| 項目 | 狀態 | 證據／限制 |
|---|---|---|
| 欄位來源標籤拆分 | PASS（程式已提交） | 三個獨立 source keys 已寫入 spot builder，報告表格逐列讀取 |
| Regression test | NOT TESTED | 正在新增欄位來源契約測試；尚未執行 CI |
| 2026-10-30 原始 TWT93U／TPEX 數據重新核算 | NOT TESTED | 尚未取得同 T0 完整原始逐股回應並重算 |
| 新 DATA_REPORT 產出驗證 | NOT TESTED | 尚未重新執行 data workflow |
| Browser audit workflow | NOT TESTED | 尚未取得 Actions run 結果 |
| Merge／部署 | NOT DONE | 僅限 phase2-p0-ui-fixes，不合併、不部署 |


### 9.12.1 CI 複驗結果（2026-11-02）
- 新增 `tests/test_fetch_data_borrowed_sources.py`，檢查三個欄位使用獨立來源鍵，且 DATA_REPORT 表格逐列取用對應標籤。
- `.github/workflows/daily-premarket-v9-pro.yml` 已新增執行該測試的步驟。
- Workflow Run **41399740450**：`success`；Commit `6eeec5a759532de0fd5d34a0e07ad53994ea992b`。
- 新增測試步驟 PASS；既有融資維持率／DATA_REPORT merge 測試、17F self-tests、Gamma fallback tests、Dashboard JSON build、HTML injection、Pages artifact upload 均 PASS。
- Artifact：`github-pages`，ID `13120833006`。本 workflow 的 deploy job 未執行（本分支 deploy 條件不成立），不代表正式 Pages 已更新。
- **重要限制**：本次為 Dashboard builder workflow，讀取既有 DATA_REPORT 並重建 Dashboard；它沒有重新執行 `src/fetch_data.py`，因此不能據此宣稱新的 DATA_REPORT 已產出正確的借券逐欄來源標籤。須待 daily-data workflow 下一次執行或可用的手動觸發，檢查新報告的三列來源欄位。
- 本次程式／測試狀態：來源欄位拆分 PASS（CI）；新 DATA_REPORT 實際產出與欄位標籤 PASS 尚未驗證；TWT93U／TPEX 原始逐股數據核算 NOT TESTED；browser audit workflow NOT TESTED。


## 9.13 2026-11-02 Browser Audit 修正與驗證

### 發現與修正
- 首次 Browser Audit Run `41398676067` FAIL，根因是 workflow 使用 `find -printf '%f\\\\n'`，將多個檔名以字面 `\\n` 串成單一環境變數，導致 Playwright 找不到 HTML。此為 workflow 檔名解析 bug，非 Dashboard 本身錯誤。
- 已修正 `.github/workflows/dashboard-browser-audit.yml` 為真正換行分隔，commit `03050c048b041669bb9f086ab09ddf80c33d57ce`。

### 複驗結果
- Browser Audit Run **41400089885**：SUCCESS。
- 實際檢查檔案：`dashboards/v9-pro-20261030.html`。
- Desktop 1440×1000：六個分頁全部 PASS；Mobile 390×844：六個分頁全部 PASS。
- 共 12 組分頁／裝置檢查、12 張截圖；pageErrors = 0；每頁根節點文字長度超過最低門檻；沒有水平溢位；每頁均有可見 canvas。
- 各頁 canvas 數：總覽 14、現貨 6、重要市場 7、期貨 6、選擇權 8、綜合分析 7（Desktop／Mobile 相同）。
- Artifact：`v9-dashboard-browser-audit`，ID `13121281035`，包含 12 張截圖與 `report.json`；已下載並讀取 report.json 確認 PASS。

### 驗收狀態
| 項目 | 狀態 | 備註 |
|---|---|---|
| Browser Audit workflow 檔案解析 | PASS | 已修正 double-escaped newline |
| 六分頁 Desktop | PASS | 6/6 |
| 六分頁 Mobile | PASS | 6/6 |
| JavaScript page errors | PASS | 0 |
| 水平溢位 | PASS | 12/12 無溢位 |
| Dashboard 截圖 | PASS | 12 張已產生並封存 |
| DATA_REPORT 借券來源標籤實際新產出 | NOT TESTED | 本輪尚未執行 daily_data workflow |
| TWT93U／TPEX 原始資料重新核算 | NOT TESTED | 尚未取得同 T0 原始回應做逐股重算 |


## 9.14 2026-11-02 daily_data 手動執行與新報告實測

### A. 執行證據
- 使用者提供 GitHub Actions 截圖：Workflow `daily-data` Run **#95**，手動觸發，分支 `phase2-p0-ui-fixes`，執行 commit 短 SHA `9c40f2b`，狀態 **Success**，總耗時 3m42s；Job `fetch` 成功。
- 已由 GitHub `fetch_file` 讀取分支新產物 `data_reports/DATA_REPORT_20261102.md`。
- 新報告標示：T0 `2026-11-02`、產出時間 `2026-11-02 14:35:26`（Asia/Taipei）、產出者 `actions`、排定班別 `manual`。因此已確認本次不只是 Dashboard 重建，而是 daily_data 的 Fetch job 真正執行並產生新 DATA_REPORT。

### B. 借券三欄實測
| 欄位 | 本次新報告 | 驗收 |
|---|---|---|
| 借券餘額 | 2,525,241 張；來源標示 `TWSE TWT96U + TWSE TWT96U OTC` | 數值及來源標籤已產出；標籤的 OTC 命名仍可改善，應明確對應 TWT96U 的 GRETAIAvailableVolume（上櫃） |
| 借券賣出餘額 | unavailable；來源「端點未提供」 | FAIL（資料未取得） |
| 借券賣出增減 | unavailable；來源「端點未提供」 | FAIL（資料未取得） |

### C. 程式鏈初步定位
- `spot.py` 對借券賣出餘額／增減分別嘗試上市 TWSE TWT93U 與上櫃 TPEX `tpex_margin_sbl`；僅將非 None 的市場資料納入加總及來源標籤。
- `spot_raw.py` 中 TWT93U 請求使用 TWSE 網站 `exchangeReport/TWT93U?response=json&date=...`；TPEX 請求使用 `/openapi/v1/tpex_margin_sbl`，並以 ROC T0 日期篩選。
- 本次報告兩欄皆為 unavailable，表示該次資料鏈沒有回傳可用的上市或上櫃值；目前沒有原始 API response／Actions log 可判定是 HTTP/端點失敗、資料日期不符或欄位解析失敗。不得直接判定是程式加總錯誤，也不得把 unavailable 說成零。
- 借券餘額來源中的 `TWSE TWT96U OTC` 實際對應同一 TWT96U 回應欄位 `GRETAIAvailableVolume`，建議將顯示名稱改為 `TWT96U GRETAI（上櫃）`，避免讓人誤以為它是另一個 TWSE OTC API。

### D. 本輪狀態
| 項目 | 狀態 | 證據／限制 |
|---|---|---|
| daily_data Run #95 | PASS | 使用者截圖顯示 Success、fetch job 綠勾 |
| Fetch job 產出新 DATA_REPORT | PASS | GitHub 讀回 DATA_REPORT_20261102.md；Actions 產出時間與 T0 明確 |
| 三欄來源標籤分流程式 | PASS | spot.py / fetch_data.py 已讀回確認 |
| 借券餘額 TWT96U 數值 | PASS（產出層） | 有非空值；原始逐股／欄位加總尚未獨立對帳 |
| 借券賣出餘額 | FAIL | 本次上市、上櫃均無可用值 |
| 借券賣出增減 | FAIL | 本次上市、上櫃均無可用值 |
| TWT93U／TPEX 原始回應及逐筆重算 | NOT TESTED | 本次尚未取得原始回應及對應 Actions log |
| GEX、Gamma Wall／Flip | FAIL（本次資料產出） | DATA_REPORT_20261102 明確為 unavailable |
| 合併／部署 | NOT DONE | 仍只在 phase2-p0-ui-fixes；Master／V8 不動 |

### E. 後續工作順序
1. 先取得 Run #95 的 fetch job log（確認 TWT93U 與 TPEX API 的實際錯誤／回傳筆數），不要先改解析器猜原因。
2. 針對失敗端點以實際回應修復；補測 TWT93U 欄位索引、TPEX 日期欄位及非空欄位判斷。
3. 將 TWT96U OTC 來源顯示名稱改為 `TWT96U GRETAI（上櫃）`，並補回歸測試。
4. 再跑 daily_data，確認三欄新報告結果與來源標籤；若上游端點仍不可用，保留 unavailable 並清楚標示，不得虛構數值。


## 9.15 TWT96U 上櫃來源標籤精確化（2026-11-02）

- 依 DATA_REPORT_20261102 的實際輸出，發現 `TWSE TWT96U OTC` 容易誤解為獨立的 TWSE OTC 端點。
- 已核對 `src/sources/spot_raw.py`：TWT96U API 的 `TWSEAvailableVolume` 對應上市，`GRETAIAvailableVolume` 對應上櫃；兩者都來自同一個 TWSE TWT96U 回應。
- 已將來源顯示名稱改為 `TWT96U GRETAI（上櫃）`，保留上市來源名稱 `TWSE TWT96U`。
- 已在 `tests/test_fetch_data_borrowed_sources.py` 加入精確標籤契約斷言。
- Commits：
  - `d83903d1111e78026ec4f31fdde0ef85160d641d`（source label）
  - `75d97a5d8b8136d9d95032ee50f63d467f2f739d`（regression assertion）
- 驗收：程式修改已提交並讀回可確認；該 commit 的 combined status 查詢目前沒有回傳 status checks，因此測試執行狀態 **NOT TESTED**，不得標為 PASS。等待 Actions 自動執行／後續手動確認。


## 9.16 Run #95 借券端點診斷日誌補強（2026-11-02）

- 使用者在 Run #95 的 Fetch daily data 步驟中搜尋 `TWT93U` 與 `tpex_margin_sbl` 均無結果。
- 原因已由程式控制流程確認：`spot_raw.py` 的兩個解析器在 HTTP 回應成功但格式／狀態／日期／資料列／欄位不符合預期時，原先會靜默回傳 None；只有 requests 例外會由 `_get_json` 輸出 `raw fetch failed`。
- 已補診斷：
  - TWT93U：回應型別、stat/欄位、空資料、可解析列數、短列數及無效餘額列數。
  - TPEX margin_sbl：回應型別、總列數、T0 日期匹配列數、可解析列數。
- 已提交：
  - `3b56e2206a4c0ea8edf7f4b430db6c22e9babcf2`（parser diagnostics）
  - `a03f69ca85a7c6751c53639c667ff6b6a958d23e`（diagnostic regression assertion）
- 驗收狀態：程式修改已提交；本次尚未有新 daily_data run，因此新診斷輸出及測試執行狀態 **NOT TESTED**。下一次手動執行 daily_data 後，直接搜尋 `TWT93U`、`TPEX margin_sbl` 即可辨別 HTTP 失敗、回應結構錯誤、日期不符或資料欄位解析失敗。


## 9.17 10/30 DATA_REPORT 借券來源沿用標籤錯置：根因定位與修正（2026-11-02）

### A. 根因定位（由實際報告與程式碼交叉確認）
- 10/30 報告的借券區塊表格仍標示 `TWSE TWT93U + TPEX margin_sbl`，但同報告來源摘要已標示借券餘額使用 `TWSE OpenAPI TWT96U` + `TPEX OpenAPI tpex_margin_sbl`；另註記明確寫「借券賣出增減僅上櫃值 (TWSE TWT93U 未取得)」。
- 現行 `spot.py` 的語義已明確分流：借券餘額由 TWT96U TWSE + TWT96U GRETAI + TPEX margin_sbl；借券賣出餘額／增減由 TWT93U + TPEX margin_sbl，來源標籤依各市場實際非 None 值組成。
- 根因在 `fetch_data.merge_same_t0()`：當新抓取欄位為 unavailable、沿用前版舊數值時，會將來源欄位也直接改回舊來源（原程式第 374-375 行）。因此報告表格可能顯示舊來源，掩蓋本次實際來源；這也解釋為何同一報告的總來源摘要與表格來源標籤不同。
- 10/30 報告借券賣出增減 -1,273 張雖有值，但同報告明確註記 TWT93U 未取得，故不能解讀為上市櫃合計；它是上櫃來源的值或同 T0 沿用值，需以本次標籤修正後的未來報告明確區分。未重新抓取歷史原始 API，逐筆數值仍 NOT TESTED。

### B. 已提交修正
- `src/fetch_data.py`：當新值為 unavailable、由同 T0 舊報告填補時，來源格改顯示 `沿用前版（原來源：...）`，不再偽裝成本次即時來源。
- 新增 `tests/test_fetch_data_same_t0_source.py`：以同 T0 舊有 -1,273、新抓取 unavailable 且新來源只有 TPEX 的 fixture，驗證數值沿用時來源標籤會清楚標示沿用前版。
- Commits：
  - `23e74f9c088b7f04f395f12eb5616e765be95b5f`（merge source attribution fix）
  - `96f63baa6c3736a82928d9f7ada59325446e9c2b`（regression test）
- Unit Contract Audit Run **#94**（commit 23e74f9）已完成 **SUCCESS**。
- V9 UI Fixes Regression Run **#126**（commit 23e74f9）仍 in_progress；新測試 commit 96f63ba 觸發 Daily Premarket V9 Pro Run **#157**，截至本記錄仍 in_progress。不得提前宣稱新測試 PASS。

### C. 其他 10/30 報告稽核
- 成交金額顯示：上市 9,396.1 + 上櫃 1,987.7 = 11,383.8 億，但總計顯示 11,383.7 億。程式以原始精度先加總、最後各自四捨五入到 0.1 億；顯示值不必然可直接相加。此項目前屬顯示精度差異，需以未四捨五入原值才能判斷是否錯誤，NOT TESTED，暫不改成「先四捨五入再相加」以免損失精度。
- 「未取得欄位 (0)」與期貨表格中的 unavailable 欄位存在口徑落差。摘要目前只彙總 `s["unavailable"]`、`fx["unavailable"]` 與少數快照項目；部分期貨表格缺值未加入 fx["unavailable"]。需再盤點期貨表格必填欄位及其 unavailable 收集邏輯，未修正前此摘要不能當成全報告完整性總數。
- 10/30 報告原始 API 逐筆對帳未做；夜盤期間不重跑資料抓取，避免覆寫日盤／全日報告。


## 9.18 11/02 DATA_REPORT 缺少現貨 OHLC 時 Dashboard 建置失敗：修正（2026-11-02）

- 新增借券沿用來源標籤修正後，Daily Premarket V9 Pro Run **#157**（commit `96f63ba`）執行時，前置借券合約測試、17F self-tests、Gamma fallback tests 均成功；Dashboard builder 在解析現貨「開盤」欄位時失敗。
- Run #157 的實際錯誤：`[NO-FALLBACK] DATA_REPORT missing 開盤`。讀取 `DATA_REPORT_20261102.md` 確認現貨開盤／最高／最低三欄為 `unavailable`，收盤值仍有資料。這是合法缺值，不應阻斷 Dashboard 建置，也絕不可用收盤價填補 OHLC。
- 已修改 `scripts/v9_pro_builder.py`：收盤維持必要欄位；開盤、最高、最低改為 optional_get，缺值保留 None；既有一致性檢查只有在 OHLC 四值齊全時才檢查，不做推估。
- 新增 `tests/test_builder_missing_spot_ohlc.py`，檢查三欄採 optional_get，且 None OHLC 不產生虛假一致性錯誤。
- Commits：
  - `6d696aab0898d346f18c29db3949579d527f7ff7`（builder accepts missing OHLC）
  - `a82156e8ca9715f76200486108708dca0e6b6a94`（regression test）
- 驗收：上述修改已提交；新 commit 對應的 CI 尚待完成，狀態 **NOT TESTED**。Run #157 的 Dashboard build 已確認 FAIL，原因不是借券修正，而是當日報告 OHLC 合法缺值未被 parser 容忍。


## 9.19 Dashboard 缺值容忍補強：Gamma Wall／Flip 等欄位（2026-11-02）

- Run #160（commit `6d696aa`）在 OHLC parser 修正後繼續往下執行，下一個實際錯誤是 `[NO-FALLBACK] DATA_REPORT missing Gamma Wall`。
- 已讀取 `DATA_REPORT_20261102.md`，確認 Gamma Wall、Gamma Flip、GEX 等欄位明確為 `unavailable`，不是報告格式遺失。
- 因此同步修正 `scripts/v9_pro_builder.py`：Call Wall、Put Wall、Gamma Wall、Gamma Flip、Max Pain 全部改採 optional_get；缺值傳 None，不互相代填、不阻斷整份 Dashboard 建置。
- 擴充 `tests/test_builder_missing_spot_ohlc.py`，斷言上述 key-level parser 均為 optional。
- Commits：
  - `209efae90ae3bc4cc0af4d692402021449ed31cc`（optional option key levels）
  - `7aa13aacb082abfed7c33659a721228d21ec8891`（regression assertions）
- Unit Contract Audit Run **#96**（commit 209efae）已 **SUCCESS**；V9 UI Fixes Regression Run **#128** 與 Daily Premarket V9 Pro Run **#162** 當時仍在執行／排隊，尚未驗證最終 builder 結果。
- 本次僅修正解析器對合法 unavailable 的容忍，不修改 DATA_REPORT 數值、不以其他數據補值、不部署。


## 9.20 缺值容忍的第二層：不產生不存在的現貨樞紐價（2026-11-02）

- Run #162（commit `209efae`）已能通過 DATA_REPORT parser，並完成 17F 分析；接著在 `build_final_json()` 產生支撐壓力位時，因 `spot.high/low` 為 None 而發生 `TypeError`。
- 已修正 `scripts/v9_pro_builder.py`：僅在 high、low、close 三值齊全時才產生當日高點／P 樞紐／當日低點；缺值時省略這三個衍生價位。Put Wall／Gamma Flip 仍各自依實際數值獨立顯示。
- 新增回歸斷言，確保 OHLC 缺值時不計算樞紐位。
- Commits：
  - `0af34d23991ccf3ed6bd39b28ca7e5797d27ea0d`（safe key-level generation）
  - `46f26b020f9e7d62defab6728323d68459d54fec`（regression assertion）
- Run #162 實際驗證：DATA_REPORT parse PASS、17F self-tests PASS、技術指標及歷史分析執行完成；最終 JSON 仍因 OHLC 衍生價位 None 而 FAIL。修正後的新 builder run 尚未完成，NOT TESTED。


## 9.21 最新 CI 驗收結果（2026-11-02）

- Daily Premarket V9 Pro Run **#165**（commit `46f26b0`）：**SUCCESS**。借券來源合約測試、17F offline self-tests、Gamma fallback regression、Dashboard JSON build、React Golden Master data injection、Pages entrypoint、dashboard history commit、Pages artifact upload 全部成功；deploy job 按 workflow 設定為 skipped，未部署。
- V9 UI Fixes Regression Run **#129**（commit `0af34d2`）：**SUCCESS**。包含 builder offline self-tests、React template regression、DATA_REPORT parser regression、Dashboard JSON、non-deploy HTML preview 與 correlation fixture。
- V9 Pro Unit Contract Audit Run **#97**（commit `0af34d2`）：**SUCCESS**。
- 因此，OHLC 合法缺值、Gamma Wall／Flip 合法缺值及缺 OHLC 時省略樞紐價的修正已通過 CI build／regression。Dashboard 產物成功建置，但 deploy skipped，沒有推送正式部署。

## 9.22 釐清 10/30 借券來源標籤錯誤的實際根因（更正 9.17）

- 更正 9.17：10/30 報告本身標記「同 T0 覆蓋」且註明當時無既有報告，故不能將 10/30 表格來源錯誤歸因於同 T0 merge 沿用舊來源格。
- 10/30 報告的全域來源摘要仍使用舊的單一 `sbl` 來源鍵（`TWSE TWT93U + TPEX margin_sbl`），同一來源被套用到借券餘額、借券賣出餘額及增減三列；這與當時實際欄位來源分流不一致。報告本身又註記 TWT93U 未取得，足以證明至少「借券賣出增減」的上市來源標籤錯誤。
- 正確根因是舊版「三個借券欄位共用一個來源標籤」，不是 10/30 報告的 merge carry-forward。該問題已由 9.12／9.12.1 的欄位來源分流修正；新報告會分別使用 `sbl_bal`、`sbl_sale_bal`、`sbl_sale_chg`。
- 9.17 修正的 merge source attribution 是另一個獨立防護：當未來同 T0 重跑時，若新值 unavailable 而沿用舊值，來源標籤需明示「沿用前版」，避免被誤認為本次新取得。該修正仍保留，不應視為 10/30 問題的原始根因。
- 10/30 原始 API 逐筆資料尚未取得，不能對 4,651,514 張、36,178 張、-1,273 張做逐筆重算；該三筆數值仍 NOT TESTED。


## 9.23 daily-data #95 為何輸出 20261102（手動觸發、t0 留白）— 根因確認（2026-11-02）

- 檢查 `.github/workflows/daily_data.yml`：手動觸發不會因 `inputs.t0` 空白而省略報告日期。workflow 一律先以 `TZ=Asia/Taipei date +%F` 設定 `TODAY`，再執行 `src/fetch_data.py --date "$TODAY" --t0 "${{ inputs.t0 }}"`。因此報告日期固定採執行當天台灣日期。
- 檢查 `src/fetch_data.py`：`report_date = args.date.strip() or today.isoformat()`；輸出檔名則由 `t0` 產生：`DATA_REPORT_{t0}`。空白 T0 會呼叫 `src.t0.resolve()` 自動判定。
- 檢查 `src/t0.py`：平日 13:45（含）後且當日為交易日，resolve 回傳當日 T0、session=日盤；13:45 前則回前一交易日、全日。
- #95 實際報告 metadata：報告日期 2026-11-02、T0 2026-11-02、產出時間 2026-11-02 14:35:26、session=日盤、排定班別=manual。與上述程式規則完全一致。
- 結論：#95 的 20261102 是因為手動觸發時空白 T0 代表自動解析，而 workflow 仍明確傳入當日 `--date`；執行時點又已過 13:45 日盤收盤，因此自動判定 T0=當日。不是 GitHub 把空白輸入自動填成日期，也不是報告日期錯置。
- 重要邊界：目前自動判定使用 Python 開始執行時的牆鐘，不是按下 Run workflow 的精確時間；若在 13:45 前觸發但工作排隊到 13:45 後才執行，T0/session 可能依執行時點而非點擊時點判定。#95 並未遇到此邊界。
- 本項為原因調查與規格確認，未修改 workflow 或日期邏輯。


## 9.24 10/30 DATA_REPORT 完整性欄位摘要漏列夜盤缺值：已修正（2026-11-02）

### 實際矛盾
- `DATA_REPORT_20261030.md` 夜盤行情列明確顯示「結算價 unavailable」「未平倉量 unavailable」（報告第 265–266 行），但選擇權章節的資料完整性摘要卻顯示「未取得欄位 (0)：無」（第 629 行）。
- 根因：`src/sources/taifex.py` 的 `unavailable` 清單只在部分選擇權 Gamma／快照路徑維護；夜盤行情欄位雖為 None 並在表格顯示 unavailable，卻沒有加入 `fx["unavailable"]`。因此 `src/fetch_data.py` 彙總的 `_all_unav` 漏掉夜盤欄位。
- 這是資料完整性摘要程式缺陷，不是 10/30 夜盤資料真的齊全。

### 已提交修正
- 新增純函式 `_missing_night_fields(night)`，逐欄檢查夜盤 open/high/low/close/change/pct/vol/settle/oi，將缺值以 `futures.night.<field>` 加入 unavailable 清單。
- 在 TAIFEX data builder 完成夜盤欄位解析後呼叫該函式，確保表格與完整性摘要一致；不補 0、不推估。
- 新增 `tests/test_taifex_night_unavailable_summary.py`，覆蓋：
  1. 僅結算價與 OI 缺值時，準確列出兩欄；
  2. 全部有值時回傳空清單；
  3. 夜盤所有欄位缺值時逐欄列出。

### Commits
- `1e2b0282749c49598ab52e613b0697df5e993c30`（missing night fields in completeness list）
- `d86d331852315b83f7b35e6faf3eb652b4f60359`（pure helper）
- `1dd378631afd979b266864d2de113985959f50fc`（regression tests）

### 驗收
- 程式與測試檔已提交並可由 GitHub 讀回；新測試及 CI 尚待執行，狀態 NOT TESTED。
- 10/30 舊報告是歷史產物，不會因程式修正自動重寫；新產生的 DATA_REPORT 才會使用修正後摘要。


## 9.25 10/30 DATA_REPORT 期貨法人交易表混用單位：已修正（2026-11-02）

### 發現
- 10/30 報告「三、期貨／5．日盤、夜盤法人交易資料」原表格欄頭使用「口數」，但最後兩列是法人日盤／夜盤交易金額淨額，數值單位實際為「億元」。
- 這是明確的單位語義錯誤：同一欄不能同時代表「口」與「億元」，會讓讀者誤讀金額欄位。

### 修正
- `src/fetch_data.py` 將該表格改成逐列四欄：項目、數值、單位、資料來源。
- 15 個交易量／淨交易量／日夜差值列標示「口」；兩個交易金額淨額列標示「億元」。
- 金額列名稱移除括號內重複單位，單位統一放入單位欄。
- `tests/test_dashboard_unit_contract.py` 新增單位契約測試，鎖定交易口數與交易金額的不同單位。

### Commits
- `ccff53c6af7b597ddc0aba0ff1cfb29625f6644e`（report per-row units）
- `a9c8a214e8667fbbd3303e38778f9d43699766c4`（unit contract regression）

### 驗收
- 修改與測試已提交；Unit Contract Audit CI 待執行，狀態 NOT TESTED。
- 舊的 10/30 DATA_REPORT 不會自動重寫；需未來重新產出該 T0 報告才會呈現修正後表格。未在夜盤中重跑 10/30 歷史抓取。


## 9.26 10/30 GEX_LEVELS_JSON 數值內部一致性複核（2026-11-02）

- 從 `DATA_REPORT_20261030.md` 的 GEX_LEVELS_JSON 直接解析 139 個履約價紀錄。
- 資料日期：2026-10-30；模型品質：usable；履約價範圍 41,400–51,600。
- 逐筆驗證 139 筆：每個履約價 `Net GEX = Call GEX + Put GEX`；`Gross GEX = |Call GEX| + |Put GEX|`。公式不一致筆數 **0**。
- 139 筆加總 Net GEX = 1,294,327,419.0091748，與報告宣告值完全相同（差異 0）。
- 139 筆加總 Gross GEX = 6,320,130,202.132608，與報告宣告值完全相同（差異 0）。
- 驗收：**PASS（報告內部數學一致性）**。此項只證明產出 JSON 的公式與彙總一致；不代表已獨立取得 TAIFEX 原始 IV／OI 逐筆重算 Black-Scholes 模型，也不代表 GEX 是造市商實際持倉。外部原始輸入對帳仍 NOT TESTED。


## 9.27 10/30 報告修正後 CI 驗收（2026-11-02）

- Unit Contract Audit Run **#98**（commit `822d4eb`）：SUCCESS。從 job log 確認新增 `test_taifex_night_unavailable_summary.py` 的 3 個測試均執行且通過（結算價／OI 缺值、全欄位正常、所有欄位缺值）。
- Unit Contract Audit Run **#99**（commit `ccff53c`）：SUCCESS。期貨交易表改為逐列單位欄的變更已通過 unit contract。
- Unit Contract Audit Run **#100**（commit `a9c8a21`）：SUCCESS。新增期貨交易口數／金額單位契約測試後仍通過。
- Daily Premarket V9 Pro Run **#168**（commit `1dd3786`）：SUCCESS；Run **#169**（commit `00dc48f`）：SUCCESS；Run **#170**（commit `a9c8a21`）：SUCCESS。這些是 Dashboard build／artifact workflows，不代表重新產出 10/30 DATA_REPORT。
- V9 UI Fixes Regression Run **#130**（commit `ccff53c`）：SUCCESS；Run **#131**（commit `a9c8a21`）當時仍 in_progress，待最終狀態。
- 上述修正仍只在 `phase2-p0-ui-fixes`；deploy jobs skipped，沒有部署或合併。


- V9 UI Fixes Regression Run **#131**（commit `a9c8a21`）：SUCCESS。期貨交易表逐列單位修正及其契約測試後，整體 UI／資料回歸流程通過。


## 9.28 10/30 報告缺少 20 年期美債殖利率：確認需求並補齊資料鏈（2026-11-02）

### 發現與確認
- 10/30 DATA_REPORT 的美債表只有 2Y、10Y、30Y，缺少 20Y。
- 專案原先 `src/sources/treasury.py` 的 FiscalData 主來源解析器只解析 2Y／10Y／30Y；API 失敗備援亦只有 2Y Treasury XML、10Y／30Y Yahoo，因此並非單日缺值，而是資料鏈根本沒有 20Y 欄位。
- DATA_REPORT_TEMPLATE 原規格同樣只列 2／10／30 年，與本專案盤前分析需求應涵蓋 2／10／20／30 年的要求不一致。
- 官方 Treasury yield curve 包含 20 年期 tenor；Treasury 官方 XML feed 提供每日 yield curve 資料。參考：Data.gov Treasury yield curve dataset、Treasury XML feed 說明（見對話引用）。

### 已提交修正
- `src/sources/treasury.py`：
  - FiscalData 主解析新增 `bc_20year`／`20 Yr`。
  - API 失敗時 Treasury XML 新增 `BC_20YEAR` 備援。
  - 20Y 缺值維持 None/unavailable，不以 10Y 或 30Y 推估。
- `src/fetch_data.py`：美債表新增「美國 20 年期殖利率」列。
- `docs/DATA_REPORT_TEMPLATE.md`：需求欄位更新為 2／10／20／30 年。
- `tests/test_dashboard_unit_contract.py`：新增 20Y source/parser/report row contract test。

### Commits
- `6a5ee98115af478a7564cc75b88fb484a1281111`（20Y Treasury source）
- `005912bced4801287b25e727ee233bdeb163fde7`（DATA_REPORT 20Y row）
- `334eb88b91d4c8c27f9945d2a247ebe475129396`（template requirement）
- `722dd0f15e30df0831021bf75d9bad5b61405ec0`（20Y unit contract test）

### 驗收
- 程式、模板及測試檔已提交；新 Unit Contract Audit 尚待完成，NOT TESTED。
- 10/30 歷史報告不會自動重寫；本修正供後續新報告使用。若要補 10/30 歷史數值，需另行取得該日官方 20Y 原始值，不可用目前值回填。


- Unit Contract Audit Run **#103**（commit `a30325e`）：SUCCESS。Job log 確認 `test_treasury_yield_curve_includes_20_year`、`test_futures_trade_table_has_per_row_units` 均 PASS；本次 unit contract 共 8 tests，全部 OK。
- Daily Premarket V9 Pro Run **#172**（commit `a30325e`）：SUCCESS；deploy skipped。這是 Dashboard build，不代表 20Y 已由 live Treasury API 實際取回並寫入新 DATA_REPORT。
- 20Y parser／報表欄位契約：PASS；實際 FiscalData／XML 20Y 回應、來源日期及新報告值：NOT TESTED。


- 補充歷史資料查證：美國財政部 2026-10-30 Daily Treasury Par Yield Curve 的 20Y 值為 **5.34%**；前一交易日 10/29 為 5.35%，日變化 **-0.01 個百分點**。此值由美國財政部官方 2026-10 月 Daily Treasury Rates 頁面查得（官方來源：`home.treasury.gov/resource-center/data-chart-center/interest-rates/TextView?field_tdr_date_value=202610&type=daily_treasury_yield_curve`）。因此 10/30 DATA_REPORT 缺少 20Y 是欄位遺漏，不是官方沒有公布。歷史報告尚未手動改寫，保留原始自動產物；後續新報告由修正後程式自動納入。


## 9.29 10/30 選擇權比例變化單位不明確：修正（2026-11-02）

### 發現
- 10/30 報告 Call／Put 比例與變化表中，Call／Put 成交量比、OI 比、PCR 是比值（倍）；但兩個歷史變化值 9.95 與 -1.87 來自 TAIFEX `PutCallRatio` 歷史欄位 `PutCallVolumeRatio%`／`PutCallOIRatio%`，其差值量綱是百分點，而非倍或百分比變化。
- 原表沒有單位欄，將比值與百分點差值混列，語義不完整。

### 修正
- `src/fetch_data.py`：Call／Put 成交量比、OI 比、PCR 各標「倍」；歷史成交量比變化與 OI 比變化各標「百分點（pp）」；表格新增單位欄。
- `docs/DASHBOARD_UNIT_STANDARD.md`：明訂 TAIFEX 歷史比例欄位的日變化用百分點，不得標成 % 或倍。
- `tests/test_dashboard_unit_contract.py`：新增 ratio 與 percentage-point 分離的契約測試。
- Commits：
  - `d09a5140e6491f44f7e79e56ead64c4a0de99182`（ratio table unit fix）
  - `c6081bfcefcf95976b88039cfedb64c2d8cf219c`（unit standard）
  - `29936a7a1daf7bd433bfedf532782811e217e1cc`（regression test）
- 驗收：程式、標準與測試已提交；最新 Unit Contract Audit 待執行，NOT TESTED。舊 10/30 DATA_REPORT 不自動改寫。

### 10/30 歷史值核對
- 10/30 報告歷史變化值 +9.95、-1.87 是百分點差值（非百分比變動率）；本次修正只補單位語義，不改動數值或公式。


- Unit Contract Audit Run **#106**（commit `72ee9c4`）：SUCCESS。Job log 確認新增 `test_option_ratio_changes_use_percentage_points` PASS；本次 Dashboard unit contract 共 9 tests，全部 OK。
- V9 UI Fixes Regression Run **#136**（commit `72ee9c4`）當時 queued；Daily Premarket V9 Pro Run **#173** in_progress，待最終狀態。這兩個 workflow 不會重跑歷史 DATA_REPORT 抓取。


## 9.30 P0 收尾：10/30 DATA_REPORT 欄位語義審查與結案（2026-11-02）

### 最後一輪語義核對結論

- **現貨法人買賣超**：外資 -1,124.7 億、投信 +236.2 億、自營商 -513.7 億，合計 -1,402.2 億；加總正確。
- **融資維持率**：報告明確標示上市自建估算、資料日期、估值檔數、4 檔沿用最近有效收盤價及 Blave 同 T0 交叉驗證差異；不是官方全市場逐檔即時值，現有註記足以揭露估算口徑。
- **借券欄位**：10/30 歷史報告仍保留舊版共用來源標籤，不能視為已回寫修正；欄位來源分流已在後續程式修正。10/30 原始 API 逐筆資料未取回，三個借券數值無法逐筆重算，標記 NOT TESTED，不列為目前程式 P0。
- **期貨法人 OI**：外資 -92,241、投信 +89,211、自營商 +1,736，合計 -1,294 口；前日淨 OI 變化 -2,719 +1,993 +225 = -501 口，算術一致。OI 是部位存量；日／夜盤淨交易量是交易流量，報告分欄呈現，不應互相當成同一口徑。
- **前十大交易人**：報告註明 TAIFEX OpenAPI、TypeOfTraders=0（全部交易人）、契約月份 202611、資料日期；前十大淨 OI 由多方 OI 減空方 OI（93,812 - 82,190 = +11,622）。日對日變化另受官方資料落後與快照日期限制，報告已列明快照日期。未取得 10/30 原始 API payload 逐筆重算，外部來源對帳 NOT TESTED。
- **選擇權比率**：Put OI / Call OI = 59,945 / 98,551 = 0.6083 倍；Call/Put 成交量比約 1.056 倍、OI 比約 1.643 倍。歷史比例欄位差值 +9.95、-1.87 的單位為百分點（pp），已修正產生器與單位契約；歷史報告本體保留原始值。
- **GEX**：139 個履約價的 Net/Gross GEX 逐筆公式及彙總內部一致，差異 0；只代表模型輸出內部一致，不代表已用 TAIFEX 原始 IV/OI 逐筆重建 Black-Scholes。原始輸入外部對帳 NOT TESTED；GEX 定義為模型估值，非交易所官方欄位或造市商真實持倉。
- **美債 20Y**：10/30 歷史報告原本缺列；官方 Treasury 歷史資料已確認當日 20Y 為 5.34%。產生器、模板及測試已補上 20Y；舊歷史報告不直接改寫。
- **成交金額合計**：上市 9,396.1 億 + 上櫃 1,987.7 億 = 11,383.8 億，報告總計 11,383.7 億，差 0.1 億，屬各來源先四捨五入至小數一位後再加總的顯示差，不構成計算 P0。
- **夜盤缺值摘要**：10/30 夜盤結算價與 OI 缺值曾未列入完整性摘要；已修正 unavailable 欄位收集邏輯並通過專項測試。

### P0 結案判定

- **PASS**：既有 Unit Contract Audit #106、V9 UI Fixes Regression #136、Daily Premarket V9 Pro #173、Browser Audit #41400089885 均沿用已取得的 SUCCESS 證據；Browser Audit 六分頁 Desktop/Mobile 共 12 次檢查通過。沒有為了結案重跑未受影響的總驗收。
- **PASS**：本輪已識別且屬程式／欄位語義範圍的缺陷，均已修正並有對應 CI 覆蓋：夜盤缺值摘要、期貨交易表混合單位、20Y 美債欄位、選擇權比例變化單位、借券來源欄位分流。
- **P0 CLOSED**：目前沒有已知且尚未修正的 P0 程式／Dashboard 欄位語義缺陷。
- **NOT TESTED（非 P0 阻斷）**：10/30 TAIFEX／TWSE／TPEX 原始 API 逐筆 payload 獨立重算；GEX 原始 IV/OI 外部重建；因子預測力與 walk-forward。這些是來源稽核／模型效能工作，不得宣稱已驗證。
- **使用者驗收待辦**：Dashboard 最終視覺接受仍由使用者確認；不影響本次程式 P0 結案。
- **分支狀態**：只更新 `phase2-p0-ui-fixes`；不 merge、不部署；V8 與 Master 未修改。

### 後續處理原則

P0 階段結束。後續若要處理 NOT TESTED 項目，另開資料來源稽核／模型驗證工作，不再把它們混入 P0，也不重跑本次已通過的總驗收。


---

# 2026-11-09 補記：V9 Pro 資料層完成與凍結

更新基準：`phase2-p0-ui-fixes`，當時已確認分支 HEAD：`3cb3cd65026abc0c607f3cf98e7dd4cda0f63ee1`。

## A. 最終狀態

使用者已確認：**V9 Pro 資料層改進全部完成，進入 DATA LAYER FROZEN 狀態。** 後續任何資料層變更，必須先取得使用者明確同意。不得將本文件更新解讀為修改資料層程式碼或 Workflow 的授權。

## B. 嚴格凍結範圍

未經使用者明確同意，禁止修改、增加、刪除、重構或調整：

1. 資料來源、端點、抓取順序、解析、清洗、轉換、計算、合併、fallback、缺值處理、驗證及輸出程式碼。
2. GitHub Actions Workflow，尤其是 `.github/workflows/daily_data.yml`；包括排程、觸發輸入、參數、timeout、重試、等待、依賴安裝及 commit/push 流程。
3. DATA_REPORT 欄位、指標、章節、格式、單位、來源標示、產出與同 T0 保護／覆寫規則。
4. Worker、Proxy、API、資料來源設定，以及任何會影響資料內容或取得方式的設定。
5. 資料層測試、schema、fixture、設定檔及相關自動化。

不得以效能改善、修 bug、清理程式碼、重構、依賴更新或小幅優化為理由自行變更。不得擅自提交資料層程式碼／Workflow commit 或部署 Worker／Proxy。

## C. 允許的只讀工作與必要授權程序

- 可以只讀檢查程式、Workflow、執行日誌及 DATA_REPORT，進行稽核、分析與比對；只讀檢查不構成修改授權。
- 發現疑似問題時，先提供可驗證證據、影響範圍及最小修正方案，等待使用者明確同意。
- 使用者對單一項目的同意，只涵蓋該明確項目；不得擴張修改範圍。
- Skill、Recovery、交接文件可以依使用者要求更新，以記錄凍結規則；文件更新不得連帶修改資料層程式碼或 Workflow。
- 只有使用者明確解除或調整凍結規則後，才可恢復對應範圍的修改。

## D. 最近一次 daily-data 執行與覆寫選項釐清

- Run：`daily-data #136`，Run ID：`42547562440`，分支：`phase2-p0-ui-fixes`，執行結果：success。
- Workflow commit：`f3c25d0882525e756218213577cb48de40f2511c`（最終失敗時略過不必要的 90 秒等待；保留第一次失敗後的重試等待）。
- 本次執行日誌明確記錄 `FORCE_REWRITE='false'`，且印出「同 T0 保護模式：DATA_REPORT 已存在」。因此本次**沒有啟用強制覆蓋**。
- 同 T0 保護合併仍允許依既有規則補入新值或特定優先級資料；所以報告檔案仍可能產生新 commit／新版本。這不等同於啟用 `--force-rewrite` 無條件覆蓋舊值。
- 報告更新 commit：`3cb3cd65026abc0c607f3cf98e7dd4cda0f63ee1`。
- `force_rewrite` 手動輸入選項保留作為特殊修正的安全閥；平常執行不勾選。只有使用者明確決定要讓本次抓取值取代同 T0 已發布的既有值時才勾選。

## E. 後續交接第一優先規則

新對話或新執行者開始工作時，必須先讀本補記及 V9 Pro Skill 的「資料層完成與嚴格凍結規則」。若任務涉及資料層，預設只能只讀檢查與提出方案；沒有使用者明確授權不得修改。任何不確定是否屬於資料層的檔案或設定，一律先視為凍結範圍並詢問，不得自行判斷為可改。

---
# 2026-11-09 補記：資料層凍結後，綜合分析分頁第一輪改善與區塊 B 結案

更新分支：phase2-p0-ui-fixes。
本補記優先於本 Recovery 中較早的「不部署／不 merge」歷史階段敘述；該敘述只適用當時任務，不可套用到本次已獲使用者授權的 Dashboard Build + Deploy 工作。資料層凍結規則持續有效且優先級最高。

## 1. 工作範圍邊界

- 使用者已確認 V9 Pro 資料層改進全部完成。未經使用者明確同意，嚴禁修改、增加、刪除或重構任何資料層內容，尤其是資料來源、資料擷取／轉換程式、Builder、DATA_REPORT、daily-data workflow、Worker／Proxy／API、資料層測試與設定。
- 本輪授權範圍是分析層、視覺層及 Dashboard Build + Deploy Workflow；不得把此授權擴張到 daily-data workflow 或資料層程式。
- DL-07 是資料層 issue，定義為對產出的 DATA_REPORT_20261106.md 做最後完整總檢查；已 PASS／CLOSE。不得把任何 GitHub Actions workflow/job 名稱含有 DL-07 字樣的項目混同此 issue，也不得因此重開 DL-07。
- 本次不修改 scripts/v9_pro_builder.py，不修改任何 DATA_REPORT、Worker、Proxy 或 daily-data workflow。

## 2. 本輪目標與已確認基準

目標是讓目前 phase2-p0-ui-fixes 分支產出的 V9 Pro Dashboard「綜合分析」分頁，達到先前三市場參考分支的分析呈現水準；不是整體合併參考分支，也不是重新設計 Dashboard。

參考分支主要分析結構包含：
1. 三市場法人籌碼（現貨、期貨 OI／日夜盤交易流量、選擇權日夜盤交易流量），明確分離 OI 存量與交易流量。
2. 選擇權法人多空力道金額（日夜盤分開），明確揭露契約金額代理值不等於淨權利金現金流、成交口數或 OI。
3. 條件式日夜盤劇本；未經回測校準的情境不得包裝成統計機率。
4. 三劇本條件路徑；Max Pain 只作磁吸參考，不當作支撐壓力或下跌目標。
5. 有效多空因子方向貢獻（前 8 項）。
6. 有足夠歷史樣本才呈現的相關性熱圖；矩陣缺值／維度不符時不得硬畫。
7. 交易計畫與 Bias、Put Wall、Gamma Wall、Call Wall、Flip、Max Pain 等價位及條件。
8. 解析文字使用觀察（look）、判讀（compass）、應對／觀察條件（target）結構。

保留 P0 分支較嚴謹的缺值檢查、期貨 OI 完整性檢查、OI／流量分離及動態 factorTarget 描述；不複製參考分支的舊日期或舊數值。

## 3. 已完成修改

### 3.1 Dashboard Template

檔案：templates/v9-pro-react-template.html

- 新增外層 .v9-market-ab-grid 與 A 卡 .v9-market-a-card 標記。
- 加入 @media (max-width: 1100px)，使區塊 A／C 在平板寬度改為單欄，避免 768～1100px 範圍仍並排造成擠壓。
- v9ProSynthesisAnalysis() 使用既有 night.l 作第二層價格確認；有效時引用夜盤低點，缺值時明確 fallback 至日／夜收盤價，不填造數值。
- 共用圖表元件 Hn 新增 decimals 顯示參數，選擇權法人多空力道區塊 B 指定 decimals:2；正負號與零值格式明確，且加寬數值標籤保留區，避免標籤遭裁切。
- 其他呼叫 Hn 的圖表維持預設精度，不應因區塊 B 修正而全部改成兩位小數。
- 保留 P0 原有動態 factorTarget、缺值保護及既有分析邏輯。

### 3.2 Dashboard Build + Deploy Workflow

檔案：.github/workflows/daily-premarket-v9-pro.yml

- Deploy job 的 branch condition 加入 refs/heads/phase2-p0-ui-fixes。
- 這是 Dashboard Build + Deploy workflow，不是 daily-data workflow；不可混淆兩者。
- 首次 Deploy 失敗根因不是程式或 artifact，而是 GitHub Repository Settings → Environments → github-pages → Deployment branches and tags 未允許 phase2-p0-ui-fixes。
- 使用者自行調整 Environment 設定後，Deploy 重跑成功。

### 3.3 Browser Audit

檔案：tests/browser_dashboard_audit.mjs

- 加入 1024×900 tablet viewport。
- 綜合分析頁加入主要區塊存在性檢查。
- 加入 tablet 下 .v9-market-ab-grid 必須為單欄的檢查。
- 首次修改後曾發現 helper 分號及 regex escape 兩項缺陷，已分別修正並回讀確認。

## 4. 相關 commits

| Commit | 內容 |
|---|---|
| 7ee409e890da982c9556793418b7f107e76c74ed | 綜合分析平板版面與夜盤低點確認 |
| 91d62e3a1285c6508d270c9519f45f30ed4a5198 | Dashboard Build + Deploy 分支條件 |
| 12d56a0bb4b7a0432502f28a591c152f4f1e46b3 | Browser Audit tablet 與綜合分析檢查 |
| 84f0be6332a622b46941ae6a10a4b7cacaadad2f | 修正 helper 分號 |
| 179f538f4a1bdef4ad1037fa80c32dbd1a5f0921 | 修正 tablet regex escape |
| 61b77527a2c259d1a83bf530555563cdab42a0fe | 區塊 B 圖表標籤兩位小數 |

## 5. Actions／部署驗證證據

### 5.1 第一輪綜合分析修改部署

- Workflow：Daily Premarket V9 Pro。
- Run ID：42551931616，Run #537，branch：phase2-p0-ui-fixes。
- 第一次 Deploy 失敗：GitHub Pages Environment branch protection 拒絕該分支；Build 已成功，Deploy 在 step 開始前被拒。
- 使用者調整 Environment 設定後，attempt 2：Build、Browser Audit、Pages Artifact、Deploy 均 SUCCESS。

### 5.2 區塊 B 精度修正部署

- Commit：61b77527a2c259d1a83bf530555563cdab42a0fe。
- Workflow Run ID：42556853022，Run #538。
- Run conclusion：SUCCESS；Build、Browser Audit、Pages Artifact、GitHub Pages Deploy 均成功。
- Browser Audit 覆蓋六分頁 Desktop／Mobile；這是自動化驗證，不替代使用者手機實際畫面驗收。

## 6. 區塊 B 手機實際畫面最終驗收

使用者先提供第一次部署後截圖，發現圖表標籤仍將 -0.11、+0.46 顯示成 -0、+0。表格原始顯示仍正確。其後以版本參數重新載入：

https://grichtoyang.github.io/daily-premarket/p0/v9-pro-latest.html?v=61b77527

使用者最新手機截圖確認圖表六列標籤已正確顯示兩位小數，且與表格、分析文字一致：

| 項目 | 圖表顯示 | 結果 |
|---|---:|---|
| 外資日淨 | +1.06 億元 | PASS |
| 外資夜淨 | -0.11 億元 | PASS |
| 投信日淨 | -10.86 億元 | PASS |
| 投信夜淨 | 0.00 億元 | PASS |
| 自營商日淨 | +7.59 億元 | PASS |
| 自營商夜淨 | +0.46 億元 | PASS |

因此區塊 B 的小數精度、正負號、零值呈現及手機實際畫面均 PASS，該項正式結案。不得再把此項列為待辦，除非後續有新的回歸證據。

## 7. 當前驗收狀態與後續工作

| 項目 | 狀態 | 證據／限制 |
|---|---|---|
| 區塊 A／C 平板單欄版面 | PASS（程式與 Browser Audit） | 1024px tablet audit 已納入；本補記未宣稱使用者逐尺寸人工驗收 |
| 夜盤低點第二層價格確認 | PASS（程式存在） | 使用既有分析層欄位；缺值有明確 fallback；未修改資料層 |
| Build／Browser Audit／Deploy | PASS | Run 42551931616 attempt 2 及 Run 42556853022 均成功 |
| 區塊 B 六筆圖表數值精度 | PASS | 使用者手機截圖確認兩位小數，並與表格／分析文字一致 |
| 綜合分析分頁所有分析邏輯全量驗收 | NOT TESTED | 七個主要區塊已呈現，但尚未完成所有數值推導、情境合理性及各區塊手機細節的全量稽核 |
| 資料層 | FROZEN | 本輪未修改任何資料層程式、Workflow、DATA_REPORT、Worker／Proxy／API |
| DL-07 | CLOSED | 不得重開或與 workflow/job 名稱混淆 |

### 下一步

1. 繼續只針對綜合分析其他區塊，逐項比對三市場參考分支的分析品質與視覺呈現；只修正有明確證據的差異。
2. 不重做區塊 B 精度修正，不重新調查已結案項目。
3. 每次修改僅限分析層／視覺層及 Dashboard Build + Deploy 相關檔案；先列精確檔案範圍。
4. 不執行、不修改 daily-data workflow；不修改 Builder、資料來源、DATA_REPORT、Worker／Proxy／API。
5. Actions PASS 後，若需驗收實際手機視覺，仍請使用者提供部署後截圖；不得以 Browser Audit 代替人工視覺驗收。
6. 本輪只有單一模型進行 Supervisor／Worker／Auditor 分工式自我審查；沒有獨立多模型委派。


## 8. 2026-11-09 綜合分析決策鏈第二輪改善（CI／視覺驗收待完成）

### 8.1 使用者確認的改善方向

使用者要求先改善五項分析問題，特別優先處理：
1. Gamma Flip 缺值與 0 的視覺矛盾。
2. Bias 分數與多空因子貢獻的解釋鏈。
3. 相關性熱圖有效樣本數與可信度提示。
4. 三市場籌碼、選擇權力道的交叉判讀。
5. 交易計畫明確連結前述分析，具備觸發、取消及觀望條件。

並要求依使用者提供的流程圖，建立四階段決策鏈：
「三市場籌碼與選擇權力道 → 多空因子與市場關係 → Bias 與日夜盤情境 → 交易計畫與風險條件」。

### 8.2 本輪實際修改範圍

只修改以下兩個程式檔案：
- `templates/v9-pro-react-template.html`
- `tests/browser_dashboard_audit.mjs`

另更新本 Recovery 文件及 Skill 文件。沒有修改 Builder、資料來源、DATA_REPORT、daily-data workflow、Worker／Proxy／API 或其他資料層內容。

Template 改善：
- 增加四階段決策鏈導覽卡片，桌面四欄、窄螢幕自動換行。
- 新增「三市場交叉判讀」卡：現貨三法人合計、期貨外資日夜淨交易流量、選擇權三法人日夜淨交易口數；另列選擇權契約金額代理值方向交叉核對。
- OI 明確定義為存量，不納入日夜交易流量方向投票；契約金額代理值不等同權利金現金流。
- 當選擇權淨交易口數與契約金額代理值方向相反時，顯示背離提醒。
- 三市場方向不一致時降低方向信心；交易計畫候選條件要求至少兩個市場同向且沒有反向市場訊號，並等待關鍵價位突破／跌破後回測確認。
- 交易計畫列出市場狀態、執行前提、觸發／取消、支撐／壓力失效條件；Bias 僅為背景評分。
- Gamma Flip 僅在有效正價位時繪製；0／缺值不當成價位標記，表格顯示缺值／不畫價位。
- Bias 解釋補上 50 分中性基準、有效因子數及前 8 項圖表限制；不把前 8 項合計當作全部 17 項因子總貢獻，也不把 Bias 當勝率。
- 相關性說明解析既有描述中的有效樣本數，對少於 10 筆標示探索性觀察、10 至 29 筆標示有限樣本；不更動歷史資料或相關性計算。

Browser Audit 改善：
- 成功切換至綜合分析後，檢查三市場交叉判讀及決策鏈等必要區塊是否實際渲染。
- Tablet 1024px 維持 A／C 單欄檢查；regex 使用正確的 whitespace pattern。

### 8.3 本輪 commits

| Commit | 內容 |
|---|---|
| `f4b9018585bfcd11ac73eb9e23fe56e1c7c33644` | 初版三市場交叉判讀、交易計畫條件、樣本警示與 Bias 解釋 |
| `e193c0606d645d2b5d0b12b5ec4f9d711841a753` | 綁定既有 institutional 資料並新增四階段決策鏈導覽 |
| `1fe9405d00a2b082786dcba6360b5f9d707b85ea` | 加入兩市場同向且無反向訊號條件、選擇權口數／金額背離提示及交易計畫前提 |
| `abab35be096159a8aaf9ed1774d8f27a7600ee92` | 修正交易計畫 Gamma Flip 缺值顯示，避免區塊內引用未定義 helper |
| `5ed957b9f6651d73cde1586ec3cbbd0074f18640` | Browser Audit 增加決策鏈及交叉判讀區塊檢查 |
| `15792b820fda27e46f48abfd9f4439da11341686` | 修正 tablet grid regex |
| `18162d781d1e180964056ce7f47f7f0ecdea9749` | Skill 文件補記本輪改善規範 |

### 8.4 驗收狀態

| 項目 | 狀態 | 說明 |
|---|---|---|
| Template 修改 | PASS（已提交／回讀） | 尚未等同瀏覽器執行驗證 |
| Browser Audit 修改 | PASS（已提交／回讀） | 尚待 CI 實際執行 |
| 三市場交叉數值邏輯 | NOT TESTED | 需以實際 Dashboard JSON 與畫面核對 |
| Gamma Flip 0／缺值顯示 | NOT TESTED | 需瀏覽器實際渲染驗證 |
| Bias 與因子說明 | NOT TESTED | 需核對輸出文字與有效因子數 |
| 相關性樣本警示 | NOT TESTED | 需核對 5、10、30 筆邊界情況 |
| 交易計畫條件鏈 | NOT TESTED | 需核對多空同向、背離、資料不足等案例 |
| 手機／平板實際畫面 | NOT TESTED | 等待 Browser Audit 及部署後畫面確認 |
| 資料層 | FROZEN | 本輪未修改任何資料層程式或 Workflow |
| DL-07 | CLOSED | 不得重開 |

注意：本輪多個連續 commits 會觸發多次 Dashboard workflow；只以最新 head SHA 對應的最終 run 判定，不將舊 commit 的取消或失敗誤認為最新成果狀態。不可執行或修改 daily-data。


### 8.5 Dashboard Build／Browser Audit／Deploy 自動驗收結果

- 最終 Dashboard Workflow Run：`42561211616`（Run #546），head SHA：`ce11f3c428f08eaadd18858b846683325411a7ac`。
- Build：SUCCESS。
- HTML／JavaScript validation：SUCCESS。
- Browser Audit：SUCCESS；六分頁 Desktop／Tablet／Mobile 測試通過，且新增的三市場交叉判讀、交易前提、觸發／取消及決策鏈必要文字均通過。
- Browser Audit 證據上傳：SUCCESS。
- Dashboard Pages artifact：SUCCESS。
- GitHub Pages Deploy：SUCCESS。
- Workflow URL：https://github.com/grichtoyang/daily-premarket/actions/runs/42561211616
- 預期部署頁：https://grichtoyang.github.io/daily-premarket/p0/v9-pro-latest.html?v=ce11f3c4
- Build workflow 在成功完成後自動更新三個 Dashboard HTML 輸出檔（`dashboards/index.html`、`dashboards/v9-pro-20261106.html`、`dashboards/v9-pro-latest.html`）；未變更 Builder、DATA_REPORT 或任何資料層程式／Workflow。

### 8.6 最終驗收狀態更新

| 項目 | 狀態 | 說明 |
|---|---|---|
| Dashboard Build | PASS | Run 42561211616 |
| HTML／JavaScript validation | PASS | Run 42561211616 |
| Browser Audit | PASS | Desktop／Tablet／Mobile、六分頁及新增決策鏈內容檢查 |
| Pages Artifact | PASS | Run 42561211616 |
| GitHub Pages Deploy | PASS | Run 42561211616 |
| 實際手機畫面人工驗收 | NOT TESTED | 仍需使用者開啟部署頁並確認畫面、數值及文字 |
| 三市場交叉判讀的案例正確性 | NOT TESTED | 自動化檢查確認渲染，不代表各種市場多空／背離案例均已逐筆驗證 |
| 資料層 | FROZEN | 未修改資料層程式、來源、DATA_REPORT、daily-data workflow、Worker／Proxy／API |
| DL-07 | CLOSED | 維持結案 |

在使用者完成實際手機畫面驗收前，不得宣稱本輪視覺與交易案例全量驗收完成。


---

# 2026-11-09 補記：綜合分析 01～04 動態決策導航與三市場口徑修正

## 1. 使用者驗收發現
使用者指出綜合分析置頂 01～04 不清楚用途。檢查實際程式確認原本只是四張靜態說明卡，沒有顯示當日結論，也沒有頁內導覽功能。另發現不同區塊的方向結論混用了外資與全體法人資料，導致「外資跨市場分歧」與「三市場同向偏空」可能同時出現而未交代統計範圍。

## 2. 本輪修改範圍
只修改：
- `templates/v9-pro-react-template.html`
- `tests/browser_dashboard_audit.mjs`
- 本 Skill 文件
- 本 Recovery 文件

未修改 Builder、資料來源、DATA_REPORT、daily-data Workflow、Worker／Proxy／API、資料層測試或設定。Dashboard Build + Deploy Workflow 本身未修改。

## 3. 實際改善內容
### 3.1 01～04 轉為動態決策導航
- 01：顯示外資現貨、外資期貨日夜流量、外資選擇權日夜流量的同法人群跨市場判讀；另列全體法人現貨／選擇權背景。
- 02：顯示 Bias、有效因子數、圖表前 8 項限制及相關性有效樣本數。
- 03：顯示現價相對 Put／Call Wall 的位置及日夜盤價格變化。
- 04：顯示當前交易計畫狀態及等待的觸發／確認條件。
- 四張卡均改為可點擊頁內導覽，分別跳轉到下方對應分析區塊；目標元素使用穩定 id。
- 導覽卡摘要由當日分析結果產生，不再只顯示固定說明文字。

### 3.2 三市場比較口徑統一
- 外資跨市場投票採同一法人群：現貨外資、期貨外資日夜淨交易、選擇權外資日夜淨交易。
- 全體法人現貨／選擇權合計另作背景資訊，不與期貨外資資料混成同一個法人群投票。
- 選擇權口數與契約金額代理值比較時，使用同一法人列；契約金額缺值時明確顯示無法交叉確認。
- OI 持續作為存量獨立觀察，不納入日夜交易流量投票。
- 交易方向至少需要兩個外資市場訊號同向且沒有反向訊號；即使符合，仍必須等待關鍵價位突破／跌破及回測確認。資料不足或背離時維持低信心／觀望。
- 相關性樣本數解析兼容「有效樣本僅 N 筆」文字格式，避免導覽摘要錯誤顯示樣本數未提供。

## 4. 本輪程式 commits
- `c24d9db4943ef03bb1544b5bb4dbea6cef8a1d2a`：初版動態決策導航、跨市場同法人群判讀及頁內錨點。
- `3ec7bbe38f5118ff6d5e807e76b3b715b83a2036`：修正交叉判讀文字及交易狀態動態摘要。
- `bcb792f695838c2cc29dff83aea8b1b4921f293c`：調整兩個以上同向訊號門檻，確保選擇權口數／契約金額代理值同法人比較，清除重複敘事鍵。
- `6a8661ca09f49425ef8f7aaeb39cea48cef79097`：修正相關性樣本數解析與金額代理缺值提示。
- `ff19356bb6c27c6e990ad7f254db7035a1d53200`：統一區間交易條件的外資跨市場確認口徑。
- Browser Audit：`e57bdc67f38b23de5aaf104739e5cf29a139c6af`，檢查 4 張決策卡、動態摘要、頁內目標存在及法人範圍文字。

## 5. 最終自動化與部署驗證
- Dashboard Workflow Run：`42568580304`（Run #552）。
- Head SHA：`ff19356bb6c27c6e990ad7f254db7035a1d53200`。
- Build：PASS。
- HTML／JavaScript validation：PASS。
- Browser Audit（Desktop／Tablet／Mobile 六分頁）：PASS；新增的決策卡與目標檢查通過。
- Pages Artifact：PASS。
- GitHub Pages Deploy：PASS。
- Workflow URL：https://github.com/grichtoyang/daily-premarket/actions/runs/42568580304
- Workflow 自動提交的產出只有 `dashboards/index.html`、`dashboards/v9-pro-20261106.html`、`dashboards/v9-pro-latest.html`；相對於 template commit 的 compare 僅顯示這三個 Dashboard HTML 產出檔，未變更資料層程式／Workflow。

## 6. 驗收狀態
| 項目 | 狀態 | 說明 |
|---|---|---|
| 01～04 動態摘要 | PASS（自動化） | 四張卡內容依當日分析結果產生 |
| 01～04 頁內導覽目標 | PASS（自動化） | Browser Audit 確認四個 href 對應目標存在 |
| 外資同法人群跨市場口徑 | PASS（程式／自動化） | 現貨、期貨、選擇權均取外資欄位 |
| 全體法人背景與外資方向區分 | PASS（程式／自動化） | 不再混成同一方向投票 |
| 選擇權口數／契約金額代理值核對 | PASS（程式檢查） | 同一法人列比較；缺值明確提示 |
| Build／Browser Audit／Deploy | PASS | Run #552 |
| 實際手機視覺 | NOT TESTED | 等待使用者開啟新部署並提供畫面 |
| 多種市場組合案例合理性 | NOT TESTED | 尚未逐一驗證多空一致、背離、資料不足等情境 |
| 資料層 | FROZEN | 未修改資料層內容 |
| DL-07 | CLOSED | 維持結案，不重開 |

## 7. 最新 Dashboard
https://grichtoyang.github.io/daily-premarket/p0/v9-pro-latest.html?v=ff19356b

使用者需實際確認手機上 01～04 是否易讀、動態摘要是否正確，以及點擊各卡是否跳到正確區塊。自動化測試通過不能取代人工畫面與真實市場案例驗收。


---

# 2026-11-09 補記：三劇本與交易計畫連動（第二輪）

## 1. 本輪發現
檢查 v9ProSynthesisAnalysis() 發現外資跨市場方向共識的文字門檻不一致：交易候選可接受至少兩個可用市場同向且無反向訊號，但交叉判讀文字在部分分支要求三市場全數可用。這會使同一份 Dashboard 對兩個已知同向、第三市場缺值的情況產生矛盾敘述。

## 2. 修改範圍與 commits
僅修改：
- templates/v9-pro-react-template.html
- tests/browser_dashboard_audit.mjs
- 本 Skill 與本 Recovery 文件

Commits：
- 151118b8302fa5f0bb584d7ed83ac27f200acdad：統一 2-of-3 可用市場共識文字；選擇權口數與契約金額代理值方向背離時，阻止交易流量確認；新增多方／空方觸發、流量門檻、劇本失效及風險控制文字；移除不分情境的固定支撐／壓力失效描述。
- f369c1959d7acd9527fa27b38c458aa5313e3462：Browser Audit 新增交易計畫五項欄位的渲染檢查。
- Skill／Recovery 文件補記本輪決策規則及限制。

## 3. 新交易計畫規則
- 多方候選：現價須有效站上 Call Wall 並回測守穩；外資至少兩個可用市場同向偏多、沒有反向訊號；選擇權口數與契約金額代理值不得背離。
- 空方候選：現價須有效跌破 Put Wall 並反抽無法收復；外資至少兩個可用市場同向偏空、沒有反向訊號；選擇權口數與契約金額代理值不得背離。
- 區間內：以區間觀察為主，不追價；等待邊界突破／跌破及回測確認。
- 方向確認少於兩個可用市場、出現反向市場訊號，或選擇權口數／金額方向背離時，不提供方向確認。
- 未有波動停損依據時，不虛構固定停損點數；僅列出劇本失效條件，並提示實際停損距離需按商品波動及風險額度設定。

## 4. 驗收狀態
| 項目 | 狀態 | 說明 |
|---|---|---|
| Template 更新 | PASS（提交） | Commit 151118b |
| Browser Audit 更新 | PASS（提交） | Commit f369c19 |
| 2-of-3 與缺值文字一致性 | PASS（靜態檢查） | 已統一為至少兩個可用市場且無反向訊號 |
| 口數／金額背離阻擋交易確認 | PASS（靜態檢查） | tradeBullConfirm／tradeBearConfirm 加入背離 gate |
| 多空觸發／流量門檻／失效／風險欄位 | PASS（靜態檢查） | 已接入交易計畫表格 |
| Dashboard Build／Browser Audit／Deploy | NOT TESTED | 等待 GitHub Actions 結果 |
| 實際手機畫面 | NOT TESTED | 等待部署後人工驗收 |
| 多種市場情境案例測試 | NOT TESTED | 尚未完成獨立案例測試 |
| 資料層 | FROZEN | 未修改資料來源、Builder、DATA_REPORT、daily-data、Worker／Proxy／API |
| DL-07 | CLOSED | 維持結案 |

## 5. 風險與限制
- 目前交易觸發使用既有 Put Wall／Call Wall，不新增資料欄位，也不產生固定停損點數。
- Bias 仍為背景評分，不作勝率或單獨進場依據。
- 這輪審查為單一模型自我覆核，並非獨立多模型審核。


## 2026-11-09 追加：因子與日夜盤證據連動交易計畫
- Template commit：7959367b7b5aefa8f88c122572d22bb9a3c69595。
- Browser Audit commit：48742e8d31d5a3b6f62923991f1cdcede87e2e0b。
- 交易計畫新增「因子交叉檢查」：對照 Bias 與圖表前 8 項可見因子淨貢獻方向；明確指出前 8 項僅為可見子集合，不代表全部因子。
- 交易計畫新增「日夜盤確認」：依日夜收盤差及日盤收盤價提供開盤後守住／收復觀察；夜盤低點缺值時不產生替代數值。
- 上述因子與日夜盤資訊是交叉檢查，不取代外資至少兩個可用市場同向且無反向訊號，以及 Put／Call Wall 突破／跌破後回測確認。
- Browser Audit 增加「因子交叉檢查」「日夜盤確認」必要欄位。
- 此輪自動化尚待最新 workflow 結果；實際手機畫面及多情境案例仍未驗證。


## 2026-11-09 第二輪交易計畫連動最終 CI／部署結果
- 最終 Dashboard Workflow：Run #557，ID 42570499929，head SHA 68c38c38a0d256eb364650d19f9773d5fbb7e40a。
- Build：PASS；HTML／JavaScript validation：PASS。
- Browser Audit：PASS；Desktop／Tablet／Mobile 六分頁及交易計畫新增欄位檢查通過。
- Generated dashboard history commit：PASS。
- Pages Artifact：PASS；GitHub Pages Deploy：PASS。
- Workflow URL：https://github.com/grichtoyang/daily-premarket/actions/runs/42570499929
- 本輪先前 Run #554 曾因更新文件時遠端分支前進，導致「Commit generated dashboard history」push rejected；該次 Browser Audit 已 PASS，但部署未執行。其後將文件與程式提交固定，最終 Run #557 成功完成 Build／Audit／Artifact／Deploy。不可把 Run #554 記為部署成功。
- 最新 Template／Audit／Skill／Recovery 均已回讀確認。Workflow 自動產出的 Dashboard HTML 已由成功部署流程發布。
- 資料層凍結維持不變；本輪沒有修改資料來源、Builder、DATA_REPORT、daily-data Workflow、Worker／Proxy／API。DL-07 維持 CLOSED。
- 實際手機畫面與多種市場組合下的人工分析合理性：NOT TESTED，仍需使用者查看新版畫面。


---

# 2026-11-11 補記：期貨分頁分析文字易讀性與判斷流程改善

## 1. 本輪目標與範圍
使用者要求期貨分頁的分析文字必須讓一般使用者容易理解，知道如何判斷及後續觀察／操作，同時保留專業深度、完整性與風險限制。

本輪只修改：
- `templates/v9-pro-react-template.html`
- `tests/browser_dashboard_audit.mjs`
- 本 Recovery 文件
- 本 Skill 文件

資料層持續凍結；未修改 Builder、資料來源、DATA_REPORT、daily-data workflow、Worker／Proxy／API 或資料層測試。

## 2. 本輪新增／修正的分析語義
### 2.1 OI 淨部位變化必須同時看正負號與變化量
原操作說明以「數字增加＝部位擴大、數字減少＝部位收斂」概括，對帶正負號的淨部位容易造成反向理解。

修正後：
- 淨部位數值往正方向移動：部位往多方移動，可能是淨多擴大，也可能是淨空縮小。
- 淨部位數值往負方向移動：部位往空方移動，可能是淨空擴大，也可能是淨多縮小。
- 必須同時比較正負號與變化量；不可只看絕對數字大小。
- OI 仍是持倉存量，不是當日買賣口數；前十大與三大法人仍分開比較。

### 2.2 外資交易流量操作建議依價格與流量實際關係動態生成
原操作建議只依外資夜盤淨買／淨賣方向選擇固定背離例子，沒有完整對應當日實際價格方向。

修正後涵蓋：
- 價格上升＋外資淨買超：方向一致，但只屬初步呼應；下一交易日仍須確認日盤流量延續及價格守穩。
- 價格下降＋外資淨賣超：方向一致，但仍須確認，不可直接當成趨勢已確立。
- 價格上升＋外資淨賣超：價格與流量背離；確認前不追多或追空。
- 價格下降＋外資淨買超：價格與流量背離；確認前不追多或追空。
- 夜盤流量為零、日夜流量缺值、價格資料不足，均有獨立文字分支，不推定方向、不補零。
- 明確重申 OI 存量與日／夜盤交易流量不可相加或相減。

## 3. Browser Audit 補強
- 期貨頁原有術語說明、OI／交易流量區分、基差正逆價差說明及三步驟劇本檢查保留。
- 新增動態流量判讀狀態檢查：方向一致、方向背離、夜盤流量為零、流量缺值、價格缺值等分支至少須有一種符合當日資料的文字實際渲染。
- 新增 OI 正負方向解釋文字檢查，避免回歸成只看數字增減的錯誤敘述。

## 4. 本輪 commits
- `60d93396b39818a3a437c281dd351c04f470421a`：外資流量操作建議改為依價格／流量方向動態判斷。
- `4876cc7943f5605eb91985b3c3bf30f9844d8557`：新增價格／流量背離與一致的分支操作文字。
- `7f074b226bbeb9a616a2bc412f375cdee5ec77bb`：Browser Audit 加入流量判讀狀態斷言。
- `66733e35219e4897dd4ce6d46bac9b267d379f9b`：修正帶正負號 OI 淨部位的變化解讀。
- `6f7036cb4cfb4783085102d4cae273f3c8b47e41`：Browser Audit 加入 OI 正負方向文字斷言。
- `003d34ac84a9cb4fc7eba26175aa0fe02c5a1b9b`：OI 缺值時仍保留正負方向解讀提示。

## 5. 驗收狀態
| 項目 | 狀態 | 證據／限制 |
|---|---|---|
| Template JavaScript 語法 | PASS | 以目前分支 Template module script 編譯檢查 |
| Browser Audit JavaScript 語法 | PASS | 移除 import 後檢查 async 主體語法 |
| 價格上升／外資淨賣超背離 | PASS（合成案例） | 實際呼叫分析函式，輸出正確背離文字 |
| 價格下降／外資淨買超背離 | PASS（合成案例） | 實際呼叫分析函式，輸出正確背離文字 |
| 價格上升／外資淨買超一致 | PASS（合成案例） | 實際呼叫分析函式，輸出一致但仍需確認的文字 |
| 夜盤流量為零、流量缺值 | PASS（合成案例） | 分別輸出中性／缺值提示 |
| OI 缺值時的正負方向說明 | PASS（合成案例） | 缺值分支仍保留方向教學 |
| Browser Audit 實際瀏覽器執行 | NOT TESTED | 尚未執行 Playwright |
| Dashboard Build／Pages Deploy | NOT TESTED | 尚未執行 |
| 手機／桌面實際畫面 | NOT TESTED | 尚未取得新版本實際畫面 |
| 真實市場資料下的分析合理性 | NOT TESTED | 本輪為合成案例，不代表真實行情驗證 |
| 資料層 | FROZEN | 本輪未修改資料層任何程式、Workflow 或產物 |
| DL-07 | CLOSED | 維持結案，不重開 |

## 6. 執行限制與下一步
- 目前 Dashboard Build workflow 內含資料層來源與回歸測試步驟；在使用者未授權執行任何資料層相關工作前，不以該完整 workflow 作為本輪 UI-only 驗收方式。
- 現有隔離 Browser Visual Audit workflow 固定下載舊的 Pages artifact run ID（`42436118367`），並非本輪最新 Template 的產物；不能把該 workflow 的結果當成新版本驗收。
- 本輪尚未取得可用的 UI-only 最新版本 Build／Browser Audit／Deploy 執行證據。不得宣稱部署完成。
- 下一步應建立／使用不執行資料層程式與測試、直接針對最新 UI Template 與既有 Dashboard JSON 產生頁面的 UI-only 驗收路徑；任何 Workflow 修改仍須先確認不會觸及資料層凍結範圍。


### 2026-11-11 期貨跨盤操作文字邊界補充
- 若夜盤收盤高於日盤收盤，次日觀察能否守在日盤收盤之上；若低於，觀察能否重新站回；若兩者相等，文字改為等待有效站上或跌破，不再錯寫成「守在日盤收盤之上」。
- Template commit：`7d0823e1815639fcde5177b7abb00a20d0e73850`。
- Skill 文件補充：`9e915ebca21ff51581f50c06cdd348d68276cc3f`。
- 此邊界已納入本輪分析邏輯；瀏覽器實際渲染仍為 NOT TESTED。
