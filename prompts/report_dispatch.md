# 報告派工令範本（Daily_REPORT）

用途：給 worker 寫 `reports/Daily_REPORT_{T0}_{SESSION}.md` 的標準派工令；每天填完佔位符後，把「派工令本文」整段複製貼進 Task 即可。

## 佔位符

| 佔位符 | 意義 | 範例 |
|---|---|---|
| `{T0}` | T0 交易日（8 碼、無破折號） | `20261020` |
| `{REPORT_DATE}` | 報告產出日（T0+1，ISO 格式） | `2026-10-21` |
| `{SESSION}` | 盤別（`全日`／`日盤`／`夜盤`），決定檔名後綴 | `全日` |
| `{DATA_SHA}` | DATA 基線 sha（`numcheck` 印出的 `DATA_SHA=` 前 12 碼） | `7a72214e1312` |
| `{REPORT}` | 目標報告路徑 | `reports/Daily_REPORT_20261020_全日.md` |
| `{DATA}` | 對應 DATA 檔 | `data_reports/DATA_REPORT_20261020.md` |
| `{FRAGMENTS}` | 片段包（已算好的表格片段，`python src/draft_blocks.py --data {DATA} --out <path>` 產出） | `<path>` |

## 派工令本文（整段複製，填值後貼上）

你是本專案（每日盤前分析）的 worker。只做本派工指派的事，範圍外一律不動。

**任務**：寫 `{REPORT}`（若該檔已存在且是壞檔，直接整檔覆寫）。

**輸入（只讀）**
1. 模板：`docs/ANA_REPORT_TEMPLATE.md`（章節順序、各節該寫什麼以它為準）。
2. 數據：`{DATA}`（DATA_SHA={DATA_SHA}；數字唯一來源）。
3. 片段包：`{FRAGMENTS}`。

**硬規則**
1. **片段包不是骨架**：它只含已算好的表格片段（表格 bytes 照貼），不含章節結構與解讀。全文須自己依模板寫；片段該出現的位置整段照貼，不要重排、不要改數值。
2. **數字只能出自 DATA**，且緊接標註 `（DATA Lxxx）`（Lxxx＝該數值在 DATA 的行號）。禁止自創、重算、換算、改值；DATA 標 `unavailable`／`N/A` 者照留，不得補值或推估。
3. **標題層級（最易錯）**：
   - 主章節用**單井號**：`# 一、` … `# 十二、`（不可用 `##`）。
   - 子節用兩井號：`## 1.1`、`## 6.2` …。
   - `## 附錄A`、`## 附錄B` 用兩井號。
   - §六 必須是 `# 六、`（`numcheck._split_sec6()` 只認這個前綴，寫成 `## 六、` 會讓 §6 檢查整段失效）。
4. **維持率**：若為前值遞補，內文與表格註記都要寫「前值遞補（DATA <日期>）」；`unavailable` 照留，不得補值。
5. **篇幅**：約 8,000–20,000 字（不含空白；表格與出處不計入目標，僅供觀測）。
   **一次成稿**：不得為了字數重寫、壓縮或刪減表格／出處；寫完就交，字數超出只在回報註明即可。
6. **另更新** `reports/latest.json`，只 4 欄、`report_date` 用 8 碼無破折號：
   `{"generated_at": "<ISO8601+08:00>", "report_date": "{T0}", "report_path": "{REPORT}", "status": "completed"}`
7. **收尾必跑**：`python scripts/gate.py --t0 {T0} [--prev <prev>]`，須見 `GATE_PASS`（exit 0）。FAIL 就照錯誤訊息修，不要改 gate／numcheck／check_report。
8. **禁止**：修改 `data_reports/`、`src/`、`scripts/`、`docs/`；`git commit`／`git push`；抓取任何外部資料。
9. **回報 ≤10 行**：改了哪些檔（路徑）→ 為何改 → gate 實際輸出（RC／NUMCHECK_ERRORS／FAILS／末行）→ 殘留風險。

## 常見失敗（先檢查這四項）

1. **把片段包當骨架**：直接貼片段包就交件 → 章節缺漏、字數不足、無解讀。片段包只是表格素材，結構照模板寫。
2. **標題層級錯**：主章節誤用 `## 一、`（應為 `# 一、`）、子節誤用 `# 1.1`（應為 `## 1.1`）、§六 寫成 `## 六、` 導致 §6 檢查失效。
3. **`latest.json` 格式錯**：多加 `updated_at` 等欄位、`report_date` 帶破折號（`2026-10-20`）、`report_path` 不一致。
4. **自行重算數字**：把 DATA 的數值換算／加總／四捨五入後寫入，或缺 `（DATA Lxxx）` 出處 → numcheck token 稽核不過。
