# OpenCode supervisor × worker（本專案設定）

## 角色
- `supervisor`（primary）：模型 `opencode/deepseek-v4.1-flash-free`。只讀稽核／調度，**不改檔**（`edit: deny`）；任何檔案修改一律派給 `worker`。
- `worker`（subagent）：模型 `opencode/big-pickle`。唯一動檔者，`edit: allow`、`bash: ask`。

## 位置
- `.opencode/agents/supervisor.md`
- `.opencode/agents/worker.md`
- `opencode.json`（`default_agent: supervisor`）

## 用法
- 新對話預設即 `supervisor`；用 Tab 可切換主代理。
- 可直接與 supervisor 對話；要叫 worker 可 `@worker`，或由 supervisor 派工。
- 對 supervisor 說一句「產出今日盤前分析」→ 依 `prompts/daily_starter.md` 與 `docs/SOP.md` 執行完整開工流程。

## 生效條件
- 設定只於啟動時載入、**不熱重載**；任何改動後需**完全關閉並重啟 opencode**。

## 還原
- 刪除 `.opencode/` 與 `opencode.json`，重啟即可。

## 注意
- `*-contributor-free` 為 Zen 免費 SKU：免 key、免綁卡，但限時／可能限流／地區受限，且**對話內容可能被供應商用於訓練**（供應商依 SKU 而異）。
- 若 SKU 下架，改 agent 檔的 `model:` 欄位；可用模型查 `https://opencode.ai/zen/v1/models`。
- supervisor 的 `bash`：既定指令（open/verify/numcheck/test/check_report 與 git 唯讀）已放行，其餘仍需人工核可。
- **免費 SKU 會被撤**：實例 2026-10-17，Zen 下架 `muse-spark-1.3-contributor-free`，worker 派工直接報 `Model ... has been deprecated`。解法：改該 agent 檔的 `model:` 一行 → **完全重啟**（見上「生效條件」）。
- 2026-10-17：worker 改用 `opencode/big-pickle`；備援 `opencode/space-bunny-free`（ctx 1M／out 512k）。原 `opencode/glm-5.3-flash-free` 在單次 8,000~13,000 字長文生成連續空回 2 次（該 SKU out 上限僅 32k）；`minimax-m3-free` 曾評估但否決（棄用、命短、知識舊）。**換 model 需完全重啟 opencode 才生效**（見上「生效條件」）；重啟後先跑一次「3,000~4,000 字探針」確認輸出非空，再上正式日。（本機快取對 `big-pickle` 標示 out=32k，該欄位對新代號未必準，仍以 runtime 為準。）
- 判斷模型能不能用**以 runtime 為準**：opencode 本機模型目錄有快取（`~/.cache/opencode/models.json`），UI 選單可能仍列出已下架的模型；實際呼叫失敗才是事實。

## 派工模板與驗收白名單（2026-10-17）
- 派工令必含六項：目的／精確目標檔／驗收方式／不可動範圍／**停手上限**／回報格式。
- 驗收指令白名單（只有三條）：
  1. `python scripts/numcheck.py --data data_reports/DATA_REPORT_<T0>.md --report reports/Daily_REPORT_<T0>_<盤別>.md`（**必帶 `--data`**）
  2. `python scripts/verify.py --t0 <T0> --prev <prev> [--expect-sha <sha12>]`
  3. `python src/check_report.py --data data_reports/DATA_REPORT_<T0>.md --report reports/Daily_REPORT_<T0>_<盤別>.md`（gate 本體；在 `src/` 不是 `scripts/`；參數同 numcheck）
- supervisor 派工前**必須先在前一份已知良好報告上實跑該指令**確認可執行（2026-10-17 實證：錯誤指令導致 worker 空轉 30 分鐘）。
- supervisor 只讀稽核、所有檔案修改一律派 worker；複核不採信 worker 敘述（以實跑輸出為準）。

## 移植到其他專案
複製下列三項到新專案，再改內文：
1. `.opencode/agents/supervisor.md`：把 body 的本專案路徑換成該專案的（`prompts/daily_starter_*`、`scripts/open.py`、`docs/SOP.md`、`docs/ANA_REPORT_TEMPLATE.md`、`reports/latest.json`），並調整 `permission.bash` 的放行指令。
2. `.opencode/agents/worker.md`：把自測指令改成該專案的驗證方式。
3. `opencode.json`（`default_agent: supervisor`）。
最後**完全關閉並重啟 opencode** 才生效。
