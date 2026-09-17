# Workers 部署說明 (Cloudflare)

版本：
- `taifex-proxy_V1.4.js` — V1.3 ＋ 每日快照 (cron＋KV)：`/snapshots/bundle`、`/snapshots/write-now`
- `taifex-proxy_V1.3.js` — V1.2 ＋ `/futures-night-ohlc`、`/put-call-ratio-history`
- `taifex-proxy_V1.2.js` — V1.1 Final_V2 原樣 ＋ `/futures-top10`、`/options-top10`
- `twse-proxy_V1.1.js` — V1.0 FINAL 原樣 ＋ `/institutional`

## 部署前置 (V1.4 快照需要，僅一次)

```bash
npx wrangler kv:namespace create SNAPSHOTS
# 將回傳的 id 填入 wrangler.toml：
# [[kv_namespaces]]
# binding = "SNAPSHOTS"
# id = "<kv-id>"
#
# [triggers]
# crons = ["30 6 * * 1-5"]   # 06:30 UTC = 14:30 Taipei (日盤收盤後，週一~五)
#
# 可選：npx wrangler secret put SNAPSHOT_KEY   # write-now 保護 key
```

## 部署步驟 (Cloudflare Dashboard)

1. Workers & Pages → 選擇 `taifex` worker → Edit code
2. 全選貼上 `workers/taifex-proxy_V1.4.js` 全部內容 → Save and deploy
3. 同上部署 `twse-proxy` ← `workers/twse-proxy_V1.1.js` (若上次已部署可略過)

## 部署後：手動觸發首次快照 (否則變化欄位維持 unavailable 直到隔日 cron)

```bash
curl -s "https://taifex.grichtoyang.workers.dev/snapshots/write-now?date=2026-09-16"
# ok:true, coverage 各鍵筆數
curl -s "https://taifex.grichtoyang.workers.dev/snapshots/bundle?date=2026-09-16"
# ok:true, date=2026-09-16
```

## 驗證 (部署後依序執行)

```bash
curl -s https://taifex.grichtoyang.workers.dev/health
# version 應為 "V1.3 — V1.2 + night-ohlc & put-call-ratio-history (additive)"

curl -s "https://taifex.grichtoyang.workers.dev/futures-night-ohlc?date=2026-09-16&month=202610"
# ok:true, data.open/high/low/close

curl -s "https://taifex.grichtoyang.workers.dev/put-call-ratio-history"
# ok:true, data 陣列 (date/volume_ratio/oi_ratio)
```

## 部署步驟 (Cloudflare Dashboard)

1. Workers & Pages → 選擇 `taifex` worker → Edit code
2. 全選貼上 `workers/taifex-proxy_V1.2.js` 全部內容 → Save and deploy
3. 同上部署 `twse-proxy` ← `workers/twse-proxy_V1.1.js`

## 驗證 (部署後依序執行)

```bash
curl -s https://taifex.grichtoyang.workers.dev/health
# version 應為 "V1.2 — V1.1 Production + Top10 endpoints (additive)"

curl -s "https://taifex.grichtoyang.workers.dev/futures-top10?date=2026-09-16&month=202610"
# ok:true, data.buy/sell/net

curl -s "https://taifex.grichtoyang.workers.dev/options-top10?date=2026-09-16&type=call"
# ok:true

curl -s "https://twse-proxy.grichtoyang.workers.dev/institutional?date=20260916"
# ok:true, data.foreign/investment_trust/dealer/total (億元)

curl -s "https://twse-proxy.grichtoyang.workers.dev?date=20260916"
# 舊 IND/MS 行為不變 (ok:true, version 1.0.0)
```

## 回滾

- 任一新端點異常：Python 端自動走舊備援 (RWD/官方直連)，報告不受影響。
- Worker 回滾：貼回前一版重 deploy 即可 (原檔在 `D:\Chatgpt 正式文件\每日盤前分析\Proxy\`)。

## 待辦批次 (已併入 V1.4，部署後結案)

1. ~~前十大歷史快照~~ → V1.4 cron＋KV 快照已實作 (top10/chain/部位/walls)。
2. 變化欄自動回填 → Python 已接線 (快照缺失時維持 unavailable)。

## Python 對接 (已完成，未部署也可用)

- 前十大：`TAIFEX_PROXY_BASE_URL` → `/futures-top10` 優先，官方 OpenAPI 備援。
- 三大法人：`TWSE_PROXY_BASE_URL` → `/institutional` 優先，RWD BFI82U 備援。
- 來源欄會如實標示 `TAIFEX Proxy` / `twse-proxy /institutional` 或備援來源。
