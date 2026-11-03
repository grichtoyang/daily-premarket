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
| 5. 借券 | 三種指標嚴格分離：①借券餘額＝借入尚未返還，使用 TWSE TWT72U selectType=SLBNLB；②借券賣出餘額＝借券賣出尚未回補，上市用 TWSE TWT93U、上櫃用 TPEx S47；③融券餘額屬另一指標，不能混入前兩者。TWT96U 是當日可借券賣出限額，禁止寫入任何餘額。TWT72U 依 fields 取前日／新增借券／還券／當日餘額，逐列驗證前日+新增-還券=當日，分別加總集中市場與櫃檯買賣中心個股，並核對兩市場小計及整體市場合計，避免重複計算。TWT93U 使用西元日期 YYYYMMDD，依欄名辨識重複欄位中的借券賣出欄組，逐股驗證前日+賣出-還券+調整=當日。TPEx S47 使用 GET /www/zh-tw/margin/sbl?date=YYYY/MM/DD&response=json，回傳欄位有重複「前日餘額／當日餘額」標籤；依欄位順序及其間的「當日還券／當日調整」標記辨識借券賣出欄組，逐股驗證相同餘額遞推公式。每個來源均驗證回傳日期與 row 完整性；來源缺失時欄位 unavailable，僅在同一 T0 上市、上櫃均有效時合併，否則來源欄明確標示實際市場範圍。2026-10-30 live workflow 已驗證三個官方端點與日期；TWT72U 上市／上櫃小計及整體合計一致，TWT93U／S47 逐列餘額遞推檢查通過。資料授權／官方 E-Shop 訂閱商品的自動化使用邊界仍需依官方條款確認。 | TWT72U（借券餘額）；TWT93U（上市借券賣出）；TPEx S47（上櫃借券賣出） | ⚠️ 來源 parser／T0 驗證 PASS；歷史 DATA_REPORT 需重建後再驗 |
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
