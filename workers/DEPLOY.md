# Cloudflare Workers 部署與驗收說明

本文件描述 TAIFEX Proxy V1.6 的部署準備、既有設定保留、部署後驗證及回滾程序。

## 版本與檔案

| Worker | 原始碼 | 用途 |
|---|---|---|
| `taifex` | `workers/taifex-proxy_V1.6.js` | TAIFEX 資料代理；V1.6 加入 TXO Chain 共用期限、受控重試及一致錯誤診斷 |
| `twse-proxy` | `workers/twse-proxy_V1.1.js` | TWSE 資料代理；本次 V1.6 不涉及此 Worker |

正式網址：`https://taifex.grichtoyang.workers.dev`

V1.6 相對 V1.5 的新增內容：
- TXO Chain Primary TAIFEX POST timeout：12 秒。
- OpenAPI fallback timeout：8 秒。
- TXO Chain 單次請求總 deadline：25 秒。
- TXO Chain 路徑共用 fetch helper，並保留 Primary / Fallback 錯誤診斷。
- Snapshot Chain retry 最多兩次，兩次間隔 3 秒。
- Python TXO Chain 502 retry 增加 2 秒 backoff；其他端點的既有 retry 行為不變。

## 部署前檢查（不得重複建立資源）

部署前先在 Cloudflare Dashboard 確認既有 `taifex` Worker 設定。不要因為看不到設定就直接建立新 Worker、KV Namespace 或 Secret。

1. 確認目標是既有 Worker `taifex`，正式網址仍為上方網址。
2. 在 Settings / Bindings 確認既有 KV Namespace binding 名稱為 `SNAPSHOTS`，並確認它指向原本使用的 Namespace。不要新建 Namespace 或更換 ID。
3. 在 Triggers / Cron Triggers 確認既有快照排程。程式註解中的預期排程為 `30 6 * * 1-5`（UTC，即台北時間週一至週五 14:30）。若現有設定不同，先查明原因，不要自行新增重複排程。
4. 確認目前 `SNAPSHOT_KEY` Secret 的設定狀態並予以保留。它是選用設定：若已設定，`/snapshots/write-now` 需提供正確 key；若未設定，該端點不會因 key 缺少而拒絕請求。不要在本次部署中更換或洩露 Secret。
5. 記錄目前已部署版本，並確認可透過 Cloudflare Deployments / Versions 回滾。專案先前記錄 V1.5 為已部署版本，但部署前仍應以 Cloudflare Dashboard 顯示為準。

若上述 binding、排程或回滾資訊無法確認，部署狀態應標記 BLOCKED，先不要部署。

## 部署步驟（需經使用者明確批准後執行）

本次只更新既有 `taifex` Worker，不部署 `twse-proxy`，也不建立新 Worker。

1. 開啟 Cloudflare Dashboard → Workers & Pages → 選擇既有 `taifex` Worker。
2. 先記錄目前 Deployment / Version，確認回滾目標。
3. 開啟 Edit code，將本 Repo 的 `workers/taifex-proxy_V1.6.js` 完整內容貼入。
4. 確認程式碼完整後才執行 Save and deploy。
5. 不要在本次部署流程中觸發 GitHub Actions、執行 `daily-data` 或修改其他 Worker。

## 部署後驗證

以下為唯讀 GET 驗證。部署後逐項執行，保留完整 HTTP 狀態碼與 JSON 回應。

### 1. Health 與版本

```bash
curl -i https://taifex.grichtoyang.workers.dev/health
```

預期：
- HTTP 200
- `ok: true`
- `service: "taifex-proxy"`
- `version: "V1.6 — V1.5 + bounded TXO Chain fetch + unified failure diagnostics (additive)"`

若仍回報 V1.4 / V1.5，代表正式環境版本尚未更新或部署目標錯誤。

### 2. TXO Chain 路由

將 `YYYY-MM-DD` 換成已知可查詢的交易日期：

```bash
curl -i "https://taifex.grichtoyang.workers.dev/options-key-levels?date=YYYY-MM-DD"
curl -i "https://taifex.grichtoyang.workers.dev/futures-options-chain?date=YYYY-MM-DD"
curl -i "https://taifex.grichtoyang.workers.dev/options-market-structure-compact?date=YYYY-MM-DD"
curl -i "https://taifex.grichtoyang.workers.dev/options-market-structure?date=YYYY-MM-DD"
curl -i "https://taifex.grichtoyang.workers.dev/options-gamma-levels?date=YYYY-MM-DD"
```

驗收原則：
- HTTP 200 時，確認回應 `ok: true`、日期符合請求，且資料欄位存在。
- 上游暫時故障時，允許回傳明確的非 2xx 錯誤；確認有 `error_code` 及來源診斷，不得把錯誤偽裝成成功、零值或空資料。
- 單次失敗不能直接判定部署失敗；先區分 TAIFEX / OpenAPI 上游可用性與 Worker Runtime 錯誤。

### 3. Snapshot KV（唯讀）

只有在確認既有 `SNAPSHOTS` binding 後，才執行：

```bash
curl -i "https://taifex.grichtoyang.workers.dev/snapshots/bundle?date=YYYY-MM-DD"
```

這是讀取既有快照的檢查。本驗收不呼叫 `/snapshots/write-now`，避免在驗收時新增或覆寫快照資料。

## 回滾

若 Health、Worker Runtime 或既有端點出現部署引入的異常：

1. 停止後續驗證與其他變更。
2. 在 Cloudflare Dashboard 的 Deployments / Versions 選擇部署前記錄的穩定版本執行 Rollback。
3. 若需手動貼回程式碼，使用部署前保存的正式版本原始碼；不要假設 Repo 中最新檔案就是目前正式環境的前一版。
4. 回滾後重新查詢 `/health`，確認版本回到預期值。
5. 記錄錯誤時間、HTTP 狀態、回應內容及部署版本，再決定是否修正 V1.6。

## 相關歷史版本

- `workers/taifex-proxy_V1.5.js`：V1.6 的前一版程式碼基準。
- `workers/taifex-proxy_V1.4.js`：加入每日快照（Cron + KV）的歷史版本。
- `workers/taifex-proxy_V1.3.js`：加入夜盤 OHLC 與 Put/Call Ratio 歷史端點。
- `workers/taifex-proxy_V1.2.js`：加入期貨及選擇權 Top 10 端點。

Python 對接設定使用 `TAIFEX_PROXY_BASE_URL` 指向既有 TAIFEX Worker；本次 V1.6 不變更 Python URL、資料 schema 或其他資料來源。
