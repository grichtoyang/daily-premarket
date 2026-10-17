# OpenCode supervisor × Muse worker（本專案設定）

## 角色
- `supervisor`（primary）：模型 `opencode/deepseek-v4.1-flash-free`。只讀稽核／調度，**不改檔**（`edit: deny`）；任何檔案修改一律派給 `muse-worker`。
- `muse-worker`（subagent）：模型 `opencode/glm-5.3-flash-free`。唯一動檔者，`edit: allow`、`bash: ask`。

## 位置
- `.opencode/agents/supervisor.md`
- `.opencode/agents/muse-worker.md`
- `opencode.json`（`default_agent: supervisor`）

## 用法
- 新對話預設即 `supervisor`；用 Tab 可切換主代理。
- 可直接與 supervisor 對話；要叫 Muse 可 `@muse-worker`，或由 supervisor 派工。
- 對 supervisor 說一句「產出今日盤前分析」→ 依 `prompts/daily_starter_Muse.md` 與 `docs/SOP.md` 執行完整開工流程。

## 生效條件
- 設定只於啟動時載入、**不熱重載**；任何改動後需**完全關閉並重啟 opencode**。

## 還原
- 刪除 `.opencode/` 與 `opencode.json`，重啟即可。

## 注意
- `*-contributor-free` 為 Zen 免費 SKU：免 key、免綁卡，但限時／可能限流／地區受限，且**對話內容可能被供應商（Meta）用於訓練**。
- 若 SKU 下架，改 agent 檔的 `model:` 欄位；可用模型查 `https://opencode.ai/zen/v1/models`。
- supervisor 的 `bash`：既定指令（open/verify/numcheck/test/check_report 與 git 唯讀）已放行，其餘仍需人工核可。
- **免費 SKU 會被撤**：實例 2026-10-17，Zen 下架 `muse-spark-1.3-contributor-free`，worker 派工直接報 `Model ... has been deprecated`。解法：改該 agent 檔的 `model:` 一行 → **完全重啟**（見上「生效條件」）。
- 判斷模型能不能用**以 runtime 為準**：opencode 本機模型目錄有快取（`~/.cache/opencode/models.json`），UI 選單可能仍列出已下架的模型；實際呼叫失敗才是事實。

## 移植到其他專案
複製下列三項到新專案，再改內文：
1. `.opencode/agents/supervisor.md`：把 body 的本專案路徑換成該專案的（`prompts/daily_starter_*`、`scripts/open.py`、`docs/SOP.md`、`docs/ANA_REPORT_TEMPLATE.md`、`reports/latest.json`），並調整 `permission.bash` 的放行指令。
2. `.opencode/agents/muse-worker.md`：把自測指令改成該專案的驗證方式。
3. `opencode.json`（`default_agent: supervisor`）。
最後**完全關閉並重啟 opencode** 才生效。
