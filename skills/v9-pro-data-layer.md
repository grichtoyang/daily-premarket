---
name: v9-pro-data-layer
description: V9 Pro 資料層正式規範；目前為凍結狀態，預設只讀。
---

# V9 Pro — Data Layer Skill（正式版）

版本：1.0｜定版日期：2026-11-14
狀態：DATA LAYER FROZEN

## 1. 職責與輸出

資料層只負責來源擷取、欄位解析、日期／時段歸屬、標準化、單位轉換、缺值標記及 DATA_REPORT 產出。資料層不負責主觀市場方向、交易判斷或 Dashboard 版面。

正式資料流：
\`Fetch Workflow → DATA_REPORT_YYYYMMDD.md → Builder → dashboards/data-YYYYMMDD.json\`

分析層與視覺層只能使用既有、已產出的欄位；不得在 UI 中暗中補抓資料或自行創造替代數值。

## 2. 凍結政策（最高優先）

資料層於 2026-11-09 宣告完成。未取得使用者事前明確授權，不得：

- 修改資料來源、API／端點、Proxy／Worker、擷取程式、解析器、清洗、轉換、公式、合併及 fallback。
- 修改 DATA_REPORT schema、欄位、單位、產出格式或缺值語義。
- 修改／執行會重跑資料層的 Workflow、排程、觸發參數、重試、timeout、依賴或發布流程。
- 執行資料層測試、DL 檢查或任何已結案資料層驗收流程。
- 以 UI 改進為由新增資料欄位或要求 Builder 改寫。

只讀檢查、閱讀既有 DATA_REPORT、比對現有 Dashboard JSON、檢查程式碼及提出修正建議不構成修改授權。發現疑似錯誤時，先提交證據、影響範圍與最小方案，等待使用者批准。

## 3. 日期、時段與報告語義

- 所有日期／時段解讀以 DATA_REPORT 的 T0、產出盤別及來源日期為準；不得僅依檔名或系統當日猜測。
- 日盤、夜盤及全日資料的統計範圍不可混用；夜盤歸屬、查詢日期與交易日邊界應以當前資料規格及已驗證實作為準。
- 新聞與市場資料必須保留來源日期／時間；無法確認時區或時間時，不得自行補造時間。
- 單日快照不能冒充連續序列；沒有多日同口徑資料時，不得推論增減趨勢。
- 來源未提供或解析失敗的欄位應保留 unavailable／null 等原有缺值語義，不得以 0、前值或其他欄位替代，除非既有規格明確允許。

## 4. 單位與資料口徑

權威對照：
- \`docs/DASHBOARD_UNIT_STANDARD.md\`
- \`docs/DASHBOARD_UNIT_MAP.md\`
- \`docs/DATA_SCHEMA.md\`
- \`docs/DATA_SOURCES.md\`

基本區分：
- 指數、期貨價格、價差、基差、履約價與關鍵價位：點。
- 漲跌幅與殖利率水準：%；殖利率日變化：百分點（pp）。
- 現貨法人金額、成交金額及融資餘額：億元。
- 融券、借券餘額、借券賣出餘額及增減：張。
- 期貨／選擇權成交量、OI、法人淨交易口數：口。
- PCR：Put OI ÷ Call OI，單位倍；不可用成交量占比代替。
- GEX：NT$／標的價格變動 1%，屬模型估值，非 TAIFEX 官方欄位。

必須分清來源原始單位、Builder 標準化單位與 Dashboard 顯示單位。不可按數字大小猜單位。

## 5. 存量、流量、代理值及缺值

- OI 是某一時點未平倉部位存量；日盤／夜盤淨交易是區間流量，不能直接相減並解讀成新增部位。
- 選擇權成交量、OI、買賣淨口數、法人力道金額及契約金額代理值是不同口徑，不可互換。
- GEX、Gamma Wall、Gamma Flip、Max Pain 等模型估算須標示其模型屬性及限制，不可稱為官方持倉或確定支撐／壓力。
- 缺值、零值、未取得、來源失敗及有值但不參與方向評分是不同狀態，必須保留差異。
- 任何代理／估算值都必須清楚標示，不得寫成真實現金流、實際 Delta／Gamma 曝險或官方數據。

## 6. Builder 與資料契約邊界

目前主要檔案：
- \`scripts/v9_pro_builder.py\`
- \`dashboards/data-YYYYMMDD.json\`
- \`docs/DASHBOARD_UNIT_MAP.md\`

Builder 將 DATA_REPORT 解析與標準化後輸出 Dashboard JSON。React Template 只消費 JSON，不應重新實作資料擷取或在 UI 層默默改變來源口徑。

不得宣稱所有原始列都經逐列單位 regex 驗證；實際驗證範圍依 parser、schema 與測試覆蓋而定。

## 7. 驗收與狀態

- 只讀核對可標示為「只讀檢查 PASS」，不可據此宣稱資料來源或資料層重新驗證 PASS。
- 沒有使用者授權時，資料層修改／測試狀態應標示 BLOCKED 或 NOT TESTED。
- DL-07 已結案，不得重開。
- 如獲得明確授權，仍須限定授權範圍，逐項提供來源證據、程式差異、測試結果及回歸影響；授權不自動延伸到其他資料層項目。

## 8. 前十大交易人 OI：契約換月比較規則（2026-11-19 補充）

- 前十大 OI 是特定契約月份的持倉快照；不得將舊月份與新主力月份的 OI 直接相減。
- 當前一交易日快照只有舊契約月份，而當日新主力月份 OI 有效時，狀態為 `rollover_baseline_reset`：新月份重新建立比較基準，當日只呈現 OI 存量，不產生跨月份變化值、不補零。
- 同一契約月份且前後快照完整時，才計算日變化。
- 快照真正缺失、指定 Call／Put 無資料或當日淨值不完整，仍是 unavailable／missing；不得誤標為換月。
- 期貨、買權、賣權各自判斷；DATA_REPORT 與 Dashboard 都要清楚顯示換月原因。
- Section 7.3 即使變化值 unavailable，仍應列出可用的當日多方 OI、空方 OI、淨 OI 與來源。OI 是存量，不可與日／夜盤交易流量混用。
- 測試：`tests/test_taifex_top10_rollover.py`（4 個案例：月份不一致、Call／Put 分流、同月份計算、真正缺少快照）。

## 9. TAIFEX TXO Chain 請求快取與重試邊界（2026-11-19 補充）

- `src/sources/taifex.py` 的 `_memoized_build_fetch(fetch)` 在單次 build 內快取，key 為 `(endpoint, date)`；不跨 build 或 workflow run 共用。
- 成功的非 Key Levels 端點回應會快取。
- `options-market-structure-compact` 的結果（包括失敗）會快取，因 Gamma 與 Wall fallback 可能對同一日期重複掃描；其原始 `_get()` 重試先行執行。
- `options-key-levels` 不快取，保留原本較長 timeout（90 秒）備援重新查詢的機會。
- 其他非 compact 端點的失敗不一律快取，允許後續以較長 timeout 再試。
- 不可為了速度移除既有 retry、timeout fallback 或資料品質判斷；快取的目的在避免同一 build 內重複等待，不是降低資料完整性標準。
- 相關測試位於 `tests/test_taifex_gamma_fallback.py`，涵蓋 compact failure reuse、Key Levels long-timeout retry 與其他端點較長 timeout retry。

## 10. 2026-11-19 效能驗收與觀察狀態

- 本機：`src/sources/taifex.py` py_compile PASS；Gamma fallback 41/41 PASS；前十大 OI rollover 4/4 PASS，合計 45/45。
- GitHub Actions：`daily-data #185`（run ID `44471987470`）completed／success；Fetch Job 約 2m36s，Fetch daily data step 約 2m13s。
- 內部 Fetch 計時：改善前 #184 為 399.3 秒，#185 為 132.8 秒，單次實測約改善 66.7%。
- 單次低於 180 秒已 PASS；長期穩定性尚未驗證。後續觀察 3–5 次使用者手動執行，逐次檢查耗時、502／timeout、Gamma fallback 與 DATA_REPORT 缺值。
- 2026-11-19 這次有限授權修正不解除 DATA LAYER FROZEN 政策；未來任何資料層程式、來源、Worker、Workflow、測試或產出格式變更，仍須先取得使用者明確授權。
