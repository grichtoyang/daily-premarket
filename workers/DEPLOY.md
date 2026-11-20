# Cloudflare Workers 部署與驗收說明

> **版本狀態（2026-11-20）：** 正式環境目前由使用者確認部署 TAIFEX Worker **V1.7**。V1.8 為本分支 `phase2-p0-ui-fixes` 上的候選版，尚未部署。未取得使用者明確批准前，不得部署、切換正式流量或寫入 KV。

## 1. Worker 與版本

| Worker | 正式基準 | 候選版本 | 用途 |
|---|---|---|---|
| `taifex` | `workers/taifex-proxy_V1.7.js` | `workers/taifex-proxy_V1.8.js` | TAIFEX / TXO 資料代理 |
| `twse-proxy` | `workers/twse-proxy_V1.2.js` | 本次無變更 | TWSE 資料代理 |

正式網址：`https://taifex.grichtoyang.workers.dev`

V1.7 相對 V1.6 的既有新增內容：
- Compact endpoint 設定 75 秒共用 deadline。
- TXO Chain 仍保留 V1.6 的 25 秒內部 deadline。
- Delta 與 TAIEX 指數請求在 Chain 完成後平行執行，並共用 compact deadline。
- 兩項平行工作使用 `Promise.allSettled`，保留各自成功結果；單項意外失敗會留下明確的 unavailable reason / diagnostics。
- 增加 compact stage timing / outcome diagnostics。
- `/health` 版本字串更新為 V1.7。

V1.8 在保留 V1.7 行為的前提下，新增官方歷史 Delta CSV 直接下載及解析；不更改資料來源的官方性質、GEX 計算公式、expiry selection、既有端點 schema 或 KV snapshot 格式。

## 2. 部署前必要檢查（唯讀）

本 Repo 沒有 `wrangler.toml` 或其他 Wrangler 設定檔；本文件所述流程是 Cloudflare Dashboard 手動部署。不得因 Repo 缺少設定檔而建立新 Worker、KV Namespace 或 Secret。

在 Cloudflare Dashboard → Workers & Pages → 既有 `taifex` Worker，先記錄：

1. Worker 名稱與正式網址，確認目標是既有 `taifex`，不是新建 Worker。
2. 現行 Deployment / Version ID、部署時間及可回滾版本。
3. Settings / Bindings：KV binding 名稱必須仍是 `SNAPSHOTS`，並確認 Namespace ID 與目前正式環境相同。不要新建 Namespace 或更換 ID。
4. Triggers / Cron Triggers：確認既有快照排程並記錄 cron expression。過往 Dashboard 紀錄為週一至週五 08:30 UTC（`30 8 * * 1-5`，台北時間 16:30），但部署當下必須以 Dashboard 現況為準；不要新增重複排程或變更時間。
5. Variables and Secrets：必須確認 `SNAPSHOT_KEY` 存在且保留原值；只確認存在狀態，不讀取、不複製、不洩露 Secret 值。**若 `SNAPSHOT_KEY` 不存在，部署前標記 BLOCKED**：目前程式在 Secret 未設定時，`/snapshots/write-now` 不會要求 key，可能允許未授權寫入 KV。部署不得移除或清空此 Secret。
6. 記錄正式環境目前的 V1.7 版本作為 rollback target，並確認 Cloudflare Deployments / Versions 可以回滾。

任一項無法確認，標記 **BLOCKED**，停止部署。

## 3. 部署步驟（僅在使用者明確批准後）

本次只更新既有 `taifex` Worker，不部署 `twse-proxy`，不建立資源。

1. 在 Cloudflare Dashboard 開啟既有 `taifex` Worker。
2. 再次確認並記錄目前正式 V1.7 Deployment / Version ID。
3. 開啟 Edit code，將分支 `phase2-p0-ui-fixes` 中 `workers/taifex-proxy_V1.8.js` 的完整內容貼入。
4. 確認程式碼沒有截斷，且既有 `SNAPSHOTS` binding、Cron、Secret 均保留。
5. 只有在上述檢查完成且使用者已明確批准時，才執行 Save and deploy。
6. 不要在本次部署流程中呼叫 `/snapshots/write-now`、手動寫 KV、觸發 GitHub `daily-data` 或修改其他 Worker。

## 4. 部署後驗收（唯讀 GET）

所有驗收只使用 GET。先查 Health，再測端點；保留 HTTP status、完整 JSON、時間戳及 Cloudflare Deployment Version。

### 4.1 Health / 版本

```bash
curl -i https://taifex.grichtoyang.workers.dev/health
```

預期：
- HTTP 200
- `ok: true`
- `service: "taifex-proxy"`
- `version` 以 `V1.8` 開頭，且明確包含 direct historical Delta CSV。

若仍回報 V1.7，表示新版本尚未生效或部署目標錯誤；立即停止後續驗收並評估回滾。

### 4.2 Compact endpoint（核心驗收）

以已知可查詢的交易日替換日期：

```bash
curl -i "https://taifex.grichtoyang.workers.dev/options-market-structure-compact?date=YYYY-MM-DD"
```

驗收：
- HTTP 200 時，確認回應日期與請求日期一致。
- 確認 Chain、Delta、TAIEX 的 found / reason / diagnostics 狀態能分辨成功與失敗。
- 確認有 V1.8 compact stage timing 診斷，能分辨 `chain_fetch` 與 `delta_taiex_parallel`。
- 單一 Delta 或 TAIEX 失敗時，另一項成功結果仍應保留；不可因單項例外而丟棄另一項成功結果。
- 若 Chain 不可用，應回傳明確錯誤，不得偽裝成成功或以 0 代替缺值。
- 上游暫時性錯誤可造成明確 unavailable / 非 2xx；須區分上游故障與 Worker runtime exception，不可只因一次上游故障判定程式部署失敗。
- 75 秒是 endpoint deadline，不代表每次都會耗滿 75 秒，也不保證整體 daily-data 一定低於 3 分鐘。

### 4.3 既有端點抽查

```bash
curl -i "https://taifex.grichtoyang.workers.dev/options-key-levels?date=YYYY-MM-DD"
curl -i "https://taifex.grichtoyang.workers.dev/futures-options-chain?date=YYYY-MM-DD"
curl -i "https://taifex.grichtoyang.workers.dev/options-gamma-levels?date=YYYY-MM-DD"
```

確認 HTTP 狀態、日期、欄位及既有錯誤診斷語意沒有回歸。若上游不可用，記錄其明確錯誤，不得把缺值當成 0。

### 4.4 Snapshot KV（唯讀）

只有確認原有 `SNAPSHOTS` binding 仍存在且 Namespace ID 相同後才執行：

```bash
curl -i "https://taifex.grichtoyang.workers.dev/snapshots/bundle?date=YYYY-MM-DD"
```

確認既有快照可讀、日期與內容符合預期。本驗收絕不呼叫 `/snapshots/write-now`，避免新增或覆寫 KV 資料。

### 4.5 上線判定

- **PASS**：Health 回報 V1.8；compact endpoint 的 stage 診斷及資料狀態合理；既有端點抽查無回歸；KV bundle 唯讀正常；Cron / binding / Secret 保留。
- **FAIL**：版本錯誤、Worker runtime exception、既有端點回歸、KV binding 遺失或資料 schema 被破壞。
- **BLOCKED**：Cloudflare 設定或 rollback target 無法確認。
- **NOT TESTED**：尚未執行的上游情境、單項失敗保留測試或未能觸發的市場資料情境。不得以靜態測試取代真實環境驗收。

正式上線驗收 PASS 前，不得宣稱 V1.8 已完成部署驗證。部署 Worker 與觸發 `daily-data` 是兩個不同操作；後者仍須使用者自行手動觸發。

## 5. 回滾

若 Health、Worker Runtime、compact endpoint 或既有端點出現部署引入的異常：

1. 停止後續驗收與其他變更。
2. 在 Cloudflare Dashboard → Deployments / Versions，選擇部署前記錄的正式 V1.7 Deployment / Version 執行 Rollback。
3. 若需手動貼回程式碼，使用已確認的 V1.7 正式版本來源；不要以 Repo 最新檔案推斷線上版本。
4. 回滾後重新查詢 `/health)，確認回報 V1.7。
5. 記錄錯誤時間、HTTP status、回應內容、Deployment Version 與回滾結果。

## 6. 相關版本

- `workers/taifex-proxy_V1.8.js`：候選版，尚未部署。
- `workers/taifex-proxy_V1.7.js`：目前正式版本程式碼基準。\n- `workers/taifex-proxy_V1.6.js`：歷史版本程式碼基準。
- `workers/taifex-proxy_V1.5.js`、`V1.4.js`：歷史版本。
- `workers/twse-proxy_V1.2.js`：本次不變更。

Python 仍使用既有 `TAIFEX_PROXY_BASE_URL`；本次 V1.8 不變更 Python URL、資料 schema、其他資料來源或 daily-data workflow。
