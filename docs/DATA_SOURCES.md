# DATA_SOURCES.md — 資料來源規範 (資料層 Rule 1/4)

版本： V2.0 (對齊 DATA_REPORT_TEMPLATE.md 新規範) | 原則：API 優先、失敗備援、缺值標 `unavailable`、不推估

## 一、現貨

| 模板章節 | 主要來源 | 備援 | 狀態 |
|---|---|---|---|
| 1. 台股大盤行情 | `twse-proxy` (收盤/漲跌) + `FinMind TaiwanStockPrice TAIEX` (開高低/成交金額，免 token) | `TWSE OpenAPI MI_INDEX` + `Yahoo ^TWII` | ✅ (MI_INDEX 無開高低) |
| 2.1 上市漲跌 | `twse-proxy` advance_decline (股票欄) | `TWSE OpenAPI twtazu_od?date=` | ✅ (注意：twtazu_od 會忽略 date，回最新) |
| 2.2 上櫃漲跌 | `TPEX OpenAPI tpex_mainborad_highlight` (注意拼字) | 無 (缺值 unavailable) | ✅ (忽略 date，須驗 Date==T0) |
| 3. 三大法人 | `TWSE RWD BFI82U?date=` (金額→億元；外資兩列加總；注意會忽略 date，回最新→註記) | 無 | ✅ |
| 4. 融資融券 | `HiStock` 上市 `three.aspx?m=mg` + 上櫃 `&no=TWOI` (融資餘額/增減億元、融券張)；大盤維持率採 `TWSE` 上市逐檔自建估算，必須標示上市範圍、T0、價格日期覆蓋數及最近有效價檔數；`Blave` 僅同 T0 交叉驗證，不作主要來源；此值不得標成上市櫃合計。官方無每日整體維持率序列。 | 官方逐股加總 (僅張數) | ⚠️ 估算口徑需揭露 |
| 5. 借券 | 必須拆開三種欄位：①上市借券餘額（尚未返還的借入證券存量）與借券賣出餘額（已賣出尚未回補存量）不可混稱；②上市 `TWT93U` 官方表同時含融券欄與借券賣出欄，借券賣出欄位為前日餘額／當日賣出／當日還券／當日調整／當日餘額，原值股數→張 (÷1000)；③上櫃 `tpex_margin_sbl` 為上櫃借券賣出餘額及前日變化。每個輸出欄位須分別標示上市／上櫃是否取得；若上市 TWT93U 未取得，借券賣出增減只能標「上櫃」不可將來源欄泛寫成上市+上櫃。`TWT96U` 是當日可借券賣出股數，不是借券餘額，禁止寫入 `sbl.bal`。真正借券餘額應使用 `TWT72U`；官方 E-Shop 顯示該日檔按月訂閱，公開歷史頁自動化取得方式及授權尚未驗證，因此未驗證前 `sbl.bal=unavailable`。`TWT93U` API 日期參數使用西元 `YYYYMMDD`；欄位需由 response `fields` 名稱定位，禁止固定 index。上市借券賣出餘額可用 TWT93U 欄位計算；TPEX `tpex_margin_sbl` 欄位 mapping 未完成官方 JSON/CSV 同日對照前，不與上市值相加。 | 上櫃值+註記 | ⚠️ 需分市場標示來源範圍 |
| 6. 成交結構 | 上市 proxy market_statistics 總計 (元) / 備援 `FMTQIK` (依 Date 取列)；上櫃 highlight DailyTradingValue (百萬元→億元) | FinMind Trading_money 交叉 | ✅ |

## 二、重要市場 (Yahoo Finance Chart API，API 優先、爬蟲備援 Phase 2)

美股 `^GSPC ^IXIC ^NDX ^DJI ^SOX ^VIX` / 亞股 `^N225 ^KS11 ^HSI 000001.SS 399001.SZ` /
期貨 `ES=F NQ=F YM=F RTY=F` / 匯率 `TWD=X DX-Y.NYB JPY=X KRW=X` /
ADR `TSM UMC ASX` / 商品 `CL=F GC=F BTC-USD` — 全部已驗 200。
漲跌點/幅由最近兩根日K收盤計算；期貨匯率保留報價時間，不得誤當現貨收盤。

美債：主 `U.S. Treasury FiscalData API` (yield curve 端點 404) → 2Y 用 `Treasury yield.xml`
(網頁備援，模板允許)；10Y/30Y 用 Yahoo `^TNX`/`^TYX`。
重大新聞：台股 `tw.stock.yahoo.com/news` (列表＋內文 datePublished/og:description，前 6 筆) 優先，
財訊快報 `TodayNews.asp` 備援 (Big5 解碼＋articleNo 日期過濾＋內文全標題，Yahoo 不足時補位)，
國際 `Fed 公告 RSS`＋`CNBC 要聞 RSS`＋`MarketWatch` 備援 (總經優先兩級＋7日窗＋去重＋分源配額；
Fed/CNBC/MW 有 description 者取摘要，Fed 無)。
cnyes (tw_stock_news/wd_stock) CSR、wantgoo 新聞 JS 算繪，無機器接口未採用；
investing 港股為主已退役；中央社/台灣央行路徑待查 (Phase 2：官方 RSS＋GDELT)。

## 三、期貨 / 四、選擇權 (Proxy 主、OpenAPI 備援)

`TAIFEX Proxy https://taifex.grichtoyang.workers.dev/` V1.3 (部署後；部署前 Python 自動走備援)：
既有 15 端點不變 ＋ `/futures-top10`、`/options-top10`、`/futures-night-ohlc`、`put-call-ratio-history`
(worker 內轉接官方，日期驗證，實際日期回傳)。
夜盤 OHLC：proxy 優先 → 官方 `DailyMarketReportFut` 盤後列備援。
P/C 比例變化：proxy 優先 → 官方 `PutCallRatio` 歷史備援。
前十大 Python 對接：proxy 優先 → 官方 OpenAPI (`OpenInterestOfLargeTradersFutures`，TypeOfTraders=0) 備援，來源欄如實標示。
`options-gamma-levels` 需 FMTQIK 當日收盤 (落後約一日)，T0 無值向 T-1…遞補；
重端點 (chain/key-levels) 不穩時向 T-1…遞補並標示日期。
P/C 比例變化走官方 `PutCallRatio` 歷史序列。
`twse-proxy` V1.1：既有 IND/MS 不變 ＋ `/institutional` (RWD BFI82U 金額口徑，附 actual_date)；
三大法人 Python 對接：proxy 優先 → RWD 直連備援。
金額欄位單位千元；近月取日盤成交量最大契約並標示月份。
缺口 (誠實標 unavailable)：夜盤開高低收、交易量/價格變化 (無昨日交易端點)、
chain/OI增減集中 (無昨日 chain)、前十大變化 (官方僅最新日)。

## 通則

- timeout 15~40s (TPEX 大檔 45s)，重試 3 次；單來源失敗不中斷全流程。
- 保留 `data_source`、`retrieved_at`、`timezone`，寫入報告第五節。
