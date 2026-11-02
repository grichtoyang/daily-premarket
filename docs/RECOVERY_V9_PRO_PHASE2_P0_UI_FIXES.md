# v9 Pro Recovery — Phase 2 P0 UI / Unit Contract

更新日期：2026-11-02（Asia/Taipei）
Repository：`grichtoyang/daily-premarket`
工作分支：`phase2-p0-ui-fixes`
更新基準 HEAD：`c2ec5fc12ff91750c7e91ff46e2ad3d1c64ade94`（2026-11-02 最新 GEX 顯示單位測試提交；Recovery 由本次文件 Commit 接續）

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
| V9 Pro Unit Contract Audit | 41390676026 | 65c560f642a0bc6fd5e59b3709200870f9d7e1a7 | PASS |
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

