# Cloudflare Workers 部署與驗收說明

> **版本狀態（2026-11-24）：** 正式環境目前仍由使用者確認部署 TAIFEX Worker **V1.7**。Repo 新增的 **V1.8** 快照可靠性修正尚未部署。未取得使用者明確批准前，不得部署、切換正式流量或寫入 KV。

## 1. Worker 與版本

| Worker | 正式版本 | 本次維護狀態 | 用途 |
|---|---|---|---|
| `taifex` | V1.7 | `workers/taifex-proxy_V1.8.js` 已進版、待使用者部署 | TAIFEX / TXO 資料代理 |
| `twse-proxy` | `workers/twse-proxy_V1.2.js` | 本次無變更 | TWSE 資料代理 |

正式網址：`https://taifex.grichtoyang.workers.dev`

V1.7 既有功能（V1.8 全數保留）：
- Compact endpoint 設定 75 秒共用 deadline。
- TXO Chain 仍保留 V1.6 的 25 秒內部 deadline。
- Delta 與 TAIEX 指數請求在 Chain 完成後平行執行，並共用 compact deadline。
- 兩項平行工作使用 `Promise.allSettled`，保留各自成功結果；單項意外失敗會留下明確的 unavailable reason / diagnostics。
- 增加 compact stage timing / outcome diagnostics。
- `/health` 版本字串標示 V1.8 快照自動補抓；V1.7 direct historical Delta CSV 功能完整保留。

V1.8 快照修正：
- 快照 Chain 必須通過指定日期、來源 TXO 列與解析合約數一致、至少 100 筆且 Call/Put 各至少 30 筆、每個到期月份 Call/Put 履約價集合一致、合約唯一性及至少 95% OI 完整度驗證。
- Chain 未通過驗證時明確標記 pending，保留一般快照，並建立同一 KV Namespace 內的待補 key。 初次寫入不完整快照時，pending 先寫入；Snapshot bundle 寫入最多 3 次（首次加 2 次重試，間隔 500ms／1,500ms），每次重送同一份序列化內容與同一 key，不重新抓取市場資料。三次仍失敗會 best-effort 記錄 `snapshot_bundle_write_failed`，並保留後續確認 Snapshot 是否實際存在的資格；若確認 bundle 確實遺失，才標記人工檢查。不會以即時資料重建遺失的歷史 bundle。 完整 Chain 分支也使用相同的最多 3 次 Snapshot bundle 寫入（同一份序列化內容、同一 key，間隔 500／1,500ms）；三次仍失敗才回報寫入失敗。完整 bundle 寫入成功後才刪除 pending；若刪除失敗只記錄 `snapshot completed pending cleanup failed`，不把已成功保存的快照判為失敗，後續 Cron 可再清理。同日與歷史 Chain 補抓成功後，也統一使用相同的 Snapshot bundle 最多 3 次寫入機制（同一份序列化 payload、同一 key，間隔 500／1,500ms）；寫入成功後才清理 pending，清理失敗只記錄錯誤，不把已保存的 Chain 當成補抓失敗或消耗額外抓取次數。 不完整 Chain 分支在讀取既有 Snapshot 以保護先前有效 Chain 時，最多嘗試 3 次（間隔 500／1,500ms）；若三次仍讀取失敗，會停止本次持久化並保留原 Snapshot key，不冒險以不完整 Chain 覆蓋未知內容。此時當日一般快照也可能未更新，需依錯誤 log 待 KV 恢復後人工確認；不會假裝已保存。
- 原定每日 Cron 只建立一次當日快照；首次 Chain 抓取最多 1 次，每次共用 25 秒 deadline。若失敗，建立 pending 並安排同日定時恢復。
- 必須在既有每日 Cron 之外，於同一個 Worker 增加一個 `*/30 * * * *` Cron Trigger（每 30 分鐘）。此 Trigger 只檢查當日 Chain pending 是否到期，不重新建立每日快照，也不處理歷史日期。
- 當日最多額外重試 **4 次**，每次最多 1 次抓取、25 秒 deadline；相對於前一次失敗，排程等待時間依序為 **30／30／60／60 分鐘**。任何一次取得通過完整性驗證的 Chain，立即更新原日期快照並刪除 pending；四次額外重試仍失敗則停止當日重試，保留 pending。
- 每 30 分鐘 Trigger 不會等待或 sleep；透過 KV 的 `next_retry_at` 控制實際重試時間。每日快照 Cron（既有排程 `30 8 * * 1-5` UTC）與 `*/30` Trigger 同在 08:30 UTC 觸發時，程式會跳過該次重試 Trigger，避免它與每日快照的 pending / Snapshot 寫入競態；當日首次重試最早在下一個 30 分鐘 Trigger 執行。考量 Cron 固定在每小時的 :00／:30 執行，程式允許在 `next_retry_at` 前最多 5 分鐘進入重試，避免因排程啟動早於時間戳而整整錯過一個週期；因此 30／30／60／60 分鐘是目標排程間隔，實際執行以 Cron 觸發時點為準。原定每日 Cron 才會執行歷史 pending 恢復：以台北日期為基準，從今天往前最多檢查 45 個日曆日的 pending key，不使用 KV list、分頁 Cursor 或跨日掃描位置；每次都從相同日期窗口重新檢查，因此不會因舊 Cursor 失效或中途跳頁而漏掉窗口內的 pending。歷史掃描對單一日期讀取 pending marker 或 Snapshot bundle、建立／更新 pending 狀態，或清除已完成的 pending marker 時若發生 KV 例外，只記錄該日期錯誤並跳過該日期，繼續掃描其他日期；不會因單一日期 KV 操作失敗中止整個 45 日掃描，也不會在讀取失敗時改寫該日期狀態。快照完整性發現仍只驗證最新 10 筆既有快照；達到 10 筆驗證上限後，沒有 pending marker 的日期會直接略過 Snapshot 讀取，但已有 pending marker 的日期仍會讀取快照，以檢查 bundle 是否遺失並保留歷史補救資格；每次最多恢復 1 個歷史日期，每日期最多 2 次 Chain 抓取。若歷史恢復發生例外，程式會 best-effort 更新該 pending 的 `updated_at`，避免同一日期因反覆例外持續佔用下一次恢復名額；若 KV 寫入也失敗，則只能記錄 log。超過最近 45 個日曆日的 pending 不會由此機制自動掃描，需人工處理。初次建立不完整快照時，pending marker 最多嘗試寫入 3 次（間隔 500／1,500ms）；若讀取舊 pending 或 3 次寫入仍失敗，不會因此放棄一般 Snapshot bundle，仍會嘗試以最多 3 次寫入保存 bundle，並記錄「無 pending marker」狀態。此情況無法啟動當日定時重試，需由下一次每日歷史掃描在最新 10 筆快照範圍內重新發現並建立 pending；若 Snapshot bundle 寫入也失敗，則只能留下錯誤 log，待 KV 恢復後處理。當日重試若發現快照本體遺失或 pending JSON 損壞，會 best-effort 將重試次數設為 4、清除下一次重試時間並標記人工檢查；若 pending JSON 損壞時狀態更新本身也遇到 KV 寫入失敗，會記錄錯誤並停止該次重試，不會讓單一狀態寫入例外逸出排程函式；排程重試執行例外（包含讀取快照本體時的例外）會消耗一個重試名額並更新下一次時間；若 Chain 已驗證有效、或 Chain 更新已成功寫入 Snapshot，但刪除 pending marker 失敗，只記錄清理錯誤，不消耗 Chain 重試名額；後續 Cron 可再次嘗試清理，且不會重新抓取已有效的 Chain；若 pending marker 本身讀取失敗，因無法可靠得知既有重試次數，程式會 best-effort 將當日重試終止並標記人工檢查。若 KV 本身不可寫入，狀態更新仍可能失敗，只能留下錯誤 log，待 KV 恢復後再處理。若 pending 對應的歷史快照本體不存在，程式不會重建整份 bundle（避免把未驗證日期的即時資料寫入歷史日期），只保留 pending 並標記 `snapshot_bundle_missing`，需人工檢查。
- `/snapshots/bundle?date=...` 改為**純讀取**：只驗證並回報 `chain_status` / `chain_diagnostics`，不發出 Chain 上游請求、不重試、不等待、不寫入 KV。daily-data 不再負責補抓，也不增加等待時間。
- 已驗證的舊 Chain 不會被失敗的新抓取覆蓋。
- 不新增 Cloudflare 服務、Namespace、Binding 或 Secret；沿用既有 `SNAPSHOTS` KV，並在同一 Worker 增加一個 30 分鐘 Cron Trigger。
- Python 既有 `/snapshots/bundle` schema 保持相容；未完成狀態透過 bundle 的 `chain_status` / `chain_diagnostics` 明確呈現。

本次不更改資料來源、GEX 計算公式、expiry selection、其他資料端點或 daily-data workflow。

## 2. 部署前必要檢查（唯讀）

本 Repo 沒有 `wrangler.toml` 或其他 Wrangler 設定檔；本文件所述流程是 Cloudflare Dashboard 手動部署。不得因 Repo 缺少設定檔而建立新 Worker、KV Namespace 或 Secret。

在 Cloudflare Dashboard → Workers & Pages → 既有 `taifex` Worker，先記錄：

1. Worker 名稱與正式網址，確認目標是既有 `taifex`，不是新建 Worker。
2. 現行 Deployment / Version ID、部署時間及可回滾版本。
3. Settings / Bindings：KV binding 名稱必須仍是 `SNAPSHOTS`，並確認 Namespace ID 與目前正式環境相同。不要新建 Namespace 或更換 ID。
4. Triggers / Cron Triggers：確認既有每日快照排程並記錄 cron expression。過往 Dashboard 紀錄為週一至週五 08:30 UTC（`30 8 * * 1-5`，台北時間 16:30），但部署當下必須以 Dashboard 現況為準。保留該每日排程，另外增加 `*/30 * * * *`（每 30 分鐘）作為 Chain 同日恢復 Trigger；不得以新排程取代原每日快照排程。
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
- `version` 應回報 `V1.8 — validated Chain snapshots with automatic recovery`。

若 `version` 未回報 V1.8，表示尚未部署正確版本；停止後續驗收並評估回滾。

### 4.2 Compact endpoint（核心驗收）

以已知可查詢的交易日替換日期：

```bash
curl -i "https://taifex.grichtoyang.workers.dev/options-market-structure-compact?date=YYYY-MM-DD"
```

驗收：
- HTTP 200 時，確認回應日期與請求日期一致。
- 確認 Chain、Delta、TAIEX 的 found / reason / diagnostics 狀態能分辨成功與失敗。
- 確認有 V1.7 compact stage timing 診斷，能分辨 `chain_fetch` 與 `delta_taiex_parallel`。
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

確認既有快照可讀、日期與內容符合預期；若該日期 Chain 曾缺失，觀察 Cron 自動補抓後 `chain_status` 是否變成 `complete`。本驗收絕不呼叫 `/snapshots/write-now`，避免手動新增或覆寫 KV 資料。

### 4.5 上線判定

- **PASS**：Health 回報 V1.8；既有端點抽查無回歸；KV bundle 可讀；缺失 Chain 能由後續 Cron 自動補回並通過驗證；Cron / binding / Secret 保留。
- **FAIL**：版本錯誤、Worker runtime exception、既有端點回歸、KV binding 遺失或資料 schema 被破壞。
- **BLOCKED**：Cloudflare 設定或 rollback target 無法確認。
- **NOT TESTED**：尚未執行的上游情境、單項失敗保留測試或未能觸發的市場資料情境。不得以靜態測試取代真實環境驗收。

正式上線驗收 PASS 前，不得宣稱 V1.8 已完成部署驗證。部署 Worker 與觸發 `daily-data` 是兩個不同操作；後者仍須使用者自行手動觸發。

## 5. 回滾

若 Health、Worker Runtime、compact endpoint 或既有端點出現部署引入的異常：

1. 停止後續驗收與其他變更。
2. 在 Cloudflare Dashboard → Deployments / Versions，選擇部署前記錄的正式 V1.7 Deployment / Version 執行 Rollback。
3. 若需手動貼回程式碼，使用已確認的 V1.7 正式版本來源；不要以 Repo 最新檔案推斷線上版本。
4. 回滾後重新查詢 `/health`，確認回報 V1.7。
5. 記錄錯誤時間、HTTP status、回應內容、Deployment Version 與回滾結果。

## 6. 相關版本

- `workers/taifex-proxy_V1.8.js`：V1.8 快照可靠性版本，保留 V1.7 原有功能；目前待使用者部署。
- `workers/taifex-proxy_V1.7.js`：保留的 V1.7 原始版本，不覆寫。
- 正式環境目前仍是使用者先前確認部署的 V1.7；未部署前不能假設線上程式與 Repo 檔案相同。
- `workers/taifex-proxy_V1.6.js`：歷史版本程式碼基準。
- `workers/taifex-proxy_V1.5.js`、`V1.4.js`：歷史版本。
- `workers/twse-proxy_V1.2.js`：本次不變更。

Python 仍使用既有 `TAIFEX_PROXY_BASE_URL`；本次 V1.8 不變更 Python URL、資料 schema、其他資料來源或 daily-data workflow。
