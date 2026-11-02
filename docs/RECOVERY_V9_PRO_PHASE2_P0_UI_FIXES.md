# v9 Pro Recovery — Phase 2 P0 UI / Unit Contract

更新日期：2026-11-02（Asia/Taipei）
Repository：`grichtoyang/daily-premarket`
工作分支：`phase2-p0-ui-fixes`
更新基準 HEAD：`45378794498c7b9144f71adee216212579e159d9`

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
| GEX | 單位尚未確認，不得推測或硬標 |

需分清楚：來源原始單位、Builder 標準化後單位、Dashboard 顯示單位。不得依數值大小猜測單位。

## 4. 目前已知的主要風險／待查項目

1. **42 區塊逐欄位覆蓋尚未完成**：需逐頁逐區塊核對資料來源欄位、Builder 解析單位、Dashboard 顯示單位與缺值呈現。
2. **Builder Regex 尚待完整複核**：確認期貨／選擇權所有數值欄位確實驗證單位後綴，沒有漏欄、重複後綴或錯誤擷取。
3. **圖表單位註記渲染尚待確認**：需檢查通用卡片元件是否實際顯示 chartNote，並確認註記位置緊鄰圖表。
4. **現貨成交額圖表 F 區塊的 `yf` 呼叫與函式簽名需重新核對**：先前曾懷疑參數不匹配，但尚不能定論。
5. **選擇權法人圖表單位需確認資料語義**：確認 `n.instOpt` 的欄位究竟是交易口數（口）或力道金額（億元），再決定圖表標示；不得只憑區塊名稱推斷。
6. **GEX 單位 BLOCKED**：需依 Worker 回傳欄位與公式定義確認 `net_gex_1pct`、`gross_gex_1pct` 的量綱；未確認前保留明確未確認註記。
7. **Desktop／Mobile 實際渲染 NOT TESTED**：需檢查圖例、數值、單位註記、文字與 icon 是否重疊、裁切或換行異常。未取得實際預覽前不得標 PASS。
8. **GitHub Actions 測試結果 BLOCKED／未取得**：雖已新增 workflow，但尚無可確認的 run ID 與成功結果。
9. **測試命令需檢查**：workflow 內 unittest 命令應採 `python -m unittest discover -s tests -p 'test_*.py' -v` 或逐檔 discover，避免 tests 目錄不是 package 時模組呼叫失敗。
10. **Builder docstring 的區塊數可能仍寫 41**：若仍存在，應依使用者確認的 42 個可見區塊修正，但需先定位確認。

## 5. 重要欄位語義提醒

- 期貨價格／高低收／價差／夜盤變化：點；成交量、OI、法人淨口數：口；漲跌幅：%。
- 選擇權 Call／Put 成交量與 OI：口；PCR 為 Put OI / Call OI，單位倍；Call Wall、Put Wall、Gamma Wall、Gamma Flip、Max Pain：點。
- PCR 卡片需分開呈現 OI PCR 與 Call／Put 成交量結構。不可把成交量占比當成 PCR。
- 殖利率水準與日變化使用不同單位（% 與 pp）。
- 混合單位圖表需對每個序列分別標示，不能用單一含糊註記涵蓋。
- GEX 的履約價可標點，但 GEX 數值單位仍未確認。
- 不得把情境權重或未校準數值包裝成統計機率。

## 6. 驗收狀態

| 項目 | 狀態 | 說明 |
|---|---|---|
| 單位標準與文件初版 | 已修改 | 文件已新增／更新，完整性仍待逐項複核 |
| Builder 單位 Regex | NOT TESTED | 已修改，尚未完整執行測試 |
| 42 區塊欄位對照 | NOT TESTED | 尚未完成逐區塊逐欄位核對 |
| 圖表單位註記程式碼 | NOT TESTED | 部分已加入，需檢查實際渲染路徑 |
| GEX 數值單位 | BLOCKED | 缺少已確認的量綱／公式契約 |
| GitHub Actions 測試 | BLOCKED | 尚無可確認的執行結果 |
| Desktop／Mobile 視覺驗收 | NOT TESTED | 尚未取得實際渲染驗證 |
| 使用者最終視覺驗收 | NOT DONE | 必須由使用者確認 |

## 7. 下一步（按順序執行，不需逐項詢問）

1. 先讀目前分支的測試檔、workflow、Builder、React template 與單位對照文件，確認實際內容與本 Recovery 一致。
2. 修正 workflow 的 unittest 執行方式；檢查是否能取得 Actions run 結果。無法取得時如實標 BLOCKED。
3. 完成 42 個區塊逐項盤點：六個分頁逐一列出區塊名稱、資料欄位、來源、單位、缺值策略、圖表註記；不得以 JSON 欄位總數代替可見區塊數。
4. 重新核對 Builder Regex 與所有敘述文字，修正漏標、錯標、重複單位與來源單位不符。
5. 逐一核對圖表函式定義與呼叫點，優先處理 `yf`、chartNote 渲染、選擇權法人圖表單位及綜合頁圖表。
6. 修正後執行可行的靜態／單元測試；每項結果記錄 PASS／FAIL／BLOCKED／NOT TESTED。
7. 在不部署、不修改其他分支的前提下，尋找可用的預覽方式；若無法取得 Desktop／Mobile 實際畫面，明確保留 NOT TESTED。
8. 完成程式與文件修正後，再交由使用者做最後 Dashboard 視覺驗收。

## 8. 工作方式

- 本對話只有單一模型；可以做 Supervisor／Worker／Auditor 分工式自我檢查，但不得宣稱已委派獨立模型。
- 發現問題後直接修正並複驗；避免每一小項都停下來要求使用者確認。
- 不擴大需求，不改資料策略或業務邏輯，除非修正單位契約必須且有明確證據。
- 所有 GitHub 寫入限定 `phase2-p0-ui-fixes`；不部署、不合併。
- 最終報告分列：已完成、已驗證、BLOCKED、NOT TESTED、尚未完成。
