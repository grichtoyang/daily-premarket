# v9 Pro Recovery — Phase 2 P0 UI / Unit Contract

更新日期：2026-11-02（Asia/Taipei）
Repository：`grichtoyang/daily-premarket`
原 P0 工作分支：`phase2-p0-ui-fixes`；目前續作分支：`fix/three-market-correlation-history`
更新基準 HEAD：`85c6fe8175517ab89237f33fd568b33ba344f26d`（2026-11-02；目前續作分支最新已知提交）

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


## 9.31 相關性熱力圖歷史資料回填與交易計畫標籤斜線修正（2026-11-02）

### 工作範圍與分支隔離
- 本輪只處理兩項指定 UI 問題：三市場圖表選擇權數據、相關性熱力圖歷史累積資料；後續另修正交易計畫圖標籤附近的斜線。
- Repository：`grichtoyang/daily-premarket`。
- 工作分支：`fix/three-market-correlation-history`。
- 最新已知提交：`85c6fe8175517ab89237f33fd568b33ba344f26d`（`85c6fe8`）。
- 不修改正式分支、不部署、不 merge、不 rebase、不修改 V8／Master；P0 已結案，不重跑 P0 總驗收。

### A. 相關性熱力圖歷史樣本不足

**根因**
- GitHub Actions 每次建置使用新的 runner，SQLite 歷史資料庫不會跨次執行持續存在。
- 先前的 5 日歷史回放測試使用暫存 SQLite DB，並不代表正式 Dashboard build 也取得相同歷史樣本。
- 另一個資料完整性問題是建置流程可能先寫入同日期的不完整舊列；回填遇到同日期既有資料時跳過，造成不完整列未被完整歷史資料取代。

**修正**
- 在 `.github/workflows/daily-premarket-v9-pro.yml` 加入建置前歷史回填，從 `data_reports/DATA_REPORT_*.md` 讀取最近 5 份報告，重建本次建置用的 `dashboards/v9_pro_history.db`。
- 回填時先刪除本次建置中相同日期的舊列，再以完整歷史報告重建，避免不完整舊列被保留。
- 日期寫入統一使用 `report_date.replace("-","")`，避免日期格式不一致。
- 加入最終輸出診斷，直接檢查 `build_final_json` 的 `analysis.correlation`，而非只驗證回填資料庫。

**CI 證據**
- Actions Run：`41419540631`。
- Commit：`85c6fe8175517ab89237f33fd568b33ba344f26d`。
- Workflow build：SUCCESS；Deploy：SKIPPED（未部署）。
- Log 確認歷史回填有效樣本 5/5。
- Log 確認最終 Dashboard JSON：Pearson 相關係數、完整有效樣本 5 筆、最近 60 筆設定、labels=8、matrix_rows=8。
- 這證明正式 build 的最終 JSON 已產生 8×8 矩陣；不是只有暫存回放測試通過。

**使用者視覺驗收**
- 使用者提供最新相關性熱力圖截圖。
- 可見 8 個指標、8×8 相關係數矩陣、對角線 1.00、正負相關色階及 -1 至 +1 圖例；數值、標籤、色塊與下方分析／判斷／操作區塊未見重疊或裁切。
- 使用者截圖視覺驗收：PASS。
- 最終 JSON／CI 證據與使用者截圖相互支持，相關性熱力圖本項結案。

### B. 交易計畫圖標籤附近斜線

**根因與修正**
- 原繪圖程式在標籤垂直移位時繪製 connector stroke；連接線可能穿過 Call Wall／Put Wall 標籤或數值區域。
- 已從 `templates/v9-pro-react-template.html` 及當前分支 `dashboards/v9-pro-20261102.html` 移除該 connector stroke 繪製語句。
- 保留價格水平線、標籤及數值。
- 另已修正 `Number(null) === 0` 的 coercion 問題：先檢查 null／undefined／空字串，再進行數字轉換，避免缺值被誤畫為 0。

**驗收**
- 程式修改已提交至目前工作分支。
- 最新 Actions build 成功，但目前尚未取得交易計畫圖修正後的使用者畫面確認。
- 狀態：程式修改已完成；實際視覺驗收 NOT TESTED。

### C. 三市場圖表選擇權數據

- 已將外資、投信、自營商選擇權日盤淨交易納入三市場圖表，圖表顯示單位為百口。
- 曾提供的數據截圖：外資 -2 百口、投信 -64 百口、自營商 +74 百口。
- 解析區域曾顯示原始口數 -167、-6,362、+7,399，與圖表百口單位的呈現方式不一致；目前沒有證據確認此單位一致性問題已修正。
- 狀態：選擇權數據已加入；圖表／解析區域單位一致性仍待確認（NOT TESTED）。

### 9.31 驗收總表

| 項目 | 狀態 | 證據／限制 |
|---|---|---|
| 相關性熱力圖歷史回填 | PASS | Actions Run 41419540631；有效樣本 5/5 |
| 相關性最終 JSON | PASS | 8 labels、8 matrix rows；完整有效樣本 5 筆 |
| 相關性熱力圖使用者畫面 | PASS | 使用者最新截圖；8×8 矩陣與版面顯示正常 |
| 交易計畫 connector 斜線程式修正 | FIXED | Template 與當前 HTML 已移除 connector stroke |
| 交易計畫修正後視覺 | NOT TESTED | 尚未取得修正後實際畫面 |
| 三市場選擇權日盤數據加入 | DONE | 外資／投信／自營商已加入，圖表單位百口 |
| 三市場圖表與解析區單位一致性 | NOT TESTED | 圖表百口與解析區原始口數顯示口徑不同，尚待確認 |
| Build workflow | PASS | Run 41419540631 SUCCESS |
| Deploy／Merge | NOT DONE | Deploy SKIPPED；未 merge、未部署 |

### 下一步（只處理未結項）
1. 取得交易計畫圖最新建置產物或使用者截圖，確認 Call Wall／Put Wall 標籤與數值不再被斜線穿越；只做此區塊視覺驗收。
2. 核對三市場圖表與解析區的選擇權法人淨交易單位；若解析區維持原始口數，須清楚標示「口」，不得與圖表百口混淆。只修改必要標籤／格式。
3. 不重跑 P0、不做全 Dashboard 無差別回歸、不部署、不 merge。完成以上兩項後再更新 Recovery 並結案本輪指定工作。

### 工作方式
- 本輪只有單一模型；Auditor 為同模型自我複核，不宣稱獨立多模型審核。
- 不把 build PASS 等同使用者端視覺 PASS；不把未取得的 Artifact 或截圖描述成已檢查。
- 僅修改明確指定問題，保留其他已驗收區塊。


## 9.32 P4 核心分析引擎提前執行（2026-11-02）

- 使用者確認：分析、判斷、操作引擎原屬 Phase 2 的 P4，現因解析品質重大缺失，提前作為 P0 結案前必要改善；不新增階段、不改變六階段原始定義與 P1～P5 後續順序。
- 已建立規格文件：`docs/P4_EARLY_ANALYSIS_ENGINE_PLAN.md`。
- 規格定義 17F 僅負責量化因子、權重、貢獻與資料覆蓋；逐區塊 AI 分析負責數據關係、推理、反證、風險與操作觀察；程式驗證負責數據、單位、日期、來源及 schema。
- 已確認 Builder 的 `build_41_cards()` 存在不同卡片共用同一段分析文字的情形，例如「KPI 8宮格」、「開盤前必核」、「AI 5面向」共用 look／compass／target；部分期貨及選擇權卡亦共用摘要。這與使用者指出的空泛解析相符。
- 已確認目前 Workflow 未見 LLM provider secret 注入或模型呼叫設定。因此真正的 LLM runtime 尚未具備可確認的執行設定；不得宣稱已完成 AI 分析。規格採可替換 provider adapter，API key 僅由 GitHub Actions Secrets 注入。
- 品質目標：各適用可見區塊逐一評分，目標 >=95/100；數字、單位、日期或來源錯誤為硬性 FAIL。必須測試資料充足、部分缺值、訊號矛盾三種情境。
- 目前狀態：規格文件已提交；42 區塊完整 ID／欄位／profile 對照、LLM provider 設定、runtime、試點分析及 95% 評分均尚未完成。
- 本次文件提交：`846754d7d60b3dc5a1c849b4dcb8f8f5b69cdc5d`。
- 不重做已 PASS 的 P0 資料／圖表項目；只做分析引擎必要的局部測試與整合。維持不部署、不 merge、不修改正式分支。

### 下一步
1. 盤點 React template 六頁全部可見區塊，建立 42 區塊 ID、資料欄位、分析 profile 對照表。
2. 確認並設定可用 LLM provider（Workflow 目前無可確認的模型 API secret 設定）；未設定前 AI runtime 維持 BLOCKED。
3. 先完成三市場法人、期貨籌碼、選擇權結構、相關性、交易計畫五個核心試點，再逐步擴展。


## 9.33 修正 P4 分析引擎方向：Master 品質作為基準（2026-11-02）

- 使用者提供 Master 產出的 v9 pro Dashboard 截圖，指出 Master 解析文字尚可，而目前工作分支的解析明顯退化。此回饋成立，先前「全面重建 AI／立即導入 LLM」的方向過度擴張，已修正。
- 已直接比較 `master` 與 `fix/three-market-correlation-history` 的 `scripts/v9_pro_builder.py`：
  - Master SHA：`76c742ac0d0cd7ff310f587e980f963c7acd192b`
  - 工作分支 SHA（比較當時）：`41cc7e720b24e46325914ebff7e3079773eb39ad`
  - Master 的 `build_41_cards()` 有較多具體情境解讀（法人三市場分歧、前十大與外資部位對照、三劇本條件等）。
  - 工作分支增加缺值防護、存量／流量區分及選擇權日夜盤拆分，但部分分析文字被改成中性摘要／限制聲明，造成分析深度退化；部分卡片仍共用 KPI 文字。
- 修正後原則：以 Master 分析深度作為最低保留基準；保留工作分支的資料真實性、缺值防護與單位／存量流量區分；清除 Master 中可能存在的硬編碼假設、無來源數值或不當機率；逐區塊增量改善。不是推倒重寫，也不把 LLM 導入當成先決條件。
- 已修訂 `docs/P4_EARLY_ANALYSIS_ENGINE_PLAN.md`，明定 Master 基準與漸進改善路徑。
- 最新規格文件提交：`acf8b933c6459e2f220a12cc71c541f470808651`。
- 目前只完成 Master／工作分支程式層比較及規格修正；尚未恢復或修改任何分析程式碼，亦未執行 Dashboard 產出驗收。
- 下一步：盤點 42 個可見區塊的 Master／branch 分析差異，建立「保留／恢復／修正」清單；先修復五個核心區塊，再逐步擴展。維持不部署、不 merge、不修改 master。
