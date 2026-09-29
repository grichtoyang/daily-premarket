# DATA_REPORT_20260929

- 報告日期：`2026-09-29`
- T0 交易日期：`2026-09-29`
- 資料產出時間：`2026-09-29 19:14:53`
- 時區：`Asia/Taipei`

---

## 一、現貨

### 1. 台股大盤行情

**資料來源：** `Cloudflare Worker：twse-proxy` (備援 `TWSE OpenAPI MI_INDEX`)

| 項目 | 數值 | 單位 | 資料來源 |
|---|---|---|---|
| 加權指數 | 47,631.96 | 點 | twse-proxy |
| 開盤 | 47,873.89 | 點 | FinMind TaiwanStockPrice TAIEX |
| 最高 | 48,045.13 | 點 | FinMind TaiwanStockPrice TAIEX |
| 最低 | 47,573.09 | 點 | FinMind TaiwanStockPrice TAIEX |
| 收盤 | 47,631.96 | 點 | twse-proxy |
| 漲跌點數 | -392.64 | 點 | twse-proxy |
| 漲跌幅 | -0.82 | % | twse-proxy |
| 成交金額 | 8,361.4 | 億元 | twse-proxy market_statistics |

### 2. 市場漲跌家數

#### 2.1 上市公司

**資料來源：** `Cloudflare Worker：twse-proxy` (備援 `TWSE OpenAPI twtazu_od`)

| 項目 | 家數 | 資料來源 |
|---|---|---|
| 上漲家數 | 374 | twse-proxy |
| 下跌家數 | 586 | twse-proxy |
| 平盤家數 | 112 | twse-proxy |
| 漲停家數 | 24 | twse-proxy |
| 跌停家數 | 0 | twse-proxy |

#### 2.2 上櫃公司

**資料來源：** `TPEX OpenAPI tpex_mainborad_highlight`

| 項目 | 家數 | 資料來源 |
|---|---|---|
| 上漲家數 | 389 | TPEX OpenAPI tpex_mainborad_highlight |
| 下跌家數 | 399 | TPEX OpenAPI tpex_mainborad_highlight |
| 平盤家數 | 80 | TPEX OpenAPI tpex_mainborad_highlight |
| 漲停家數 | 21 | TPEX OpenAPI tpex_mainborad_highlight |
| 跌停家數 | 2 | TPEX OpenAPI tpex_mainborad_highlight |

### 3. 三大法人現貨買賣超

**資料來源：** `TWSE RWD BFI82U`

| 法人別 | 買賣超金額 | 單位 | 資料來源 |
|---|---|---|---|
| 外資 | -632.0 | 億元 | twse-proxy /institutional |
| 投信 | +14.2 | 億元 | twse-proxy /institutional |
| 自營商 | -164.0 | 億元 | twse-proxy /institutional |
| 三大法人合計 | -781.9 | 億元 | twse-proxy /institutional |

### 4. 融資融券

**資料來源：** 上市+上櫃 `HiStock` (金額口徑)；維持率 `istock.tw`；備援官方逐股加總

| 項目 | 數值 | 單位 | 資料來源 |
|---|---|---|---|
| 融資餘額 | unavailable | 億元 | HiStock |
| 融資增減 | unavailable | 億元 | HiStock |
| 融券餘額 | 202,008 | 張 | HiStock |
| 融券增減 | -7,700 | 張 | HiStock |
| 融資維持率 | 193.87 | % | 前值遞補 (DATA 2026-09-24；當日三源皆失敗；民間估算；官方無每日序列) |

### 5. 借券資料

**資料來源：** 上市 `TWSE OpenAPI TWT96U` (可借餘額)、上櫃 `TPEX OpenAPI tpex_margin_sbl`

| 項目 | 數值 | 單位 | 資料來源 |
|---|---|---|---|
| 借券餘額 | 2,441,375 | 張 | TWSE TWT93U + TPEX margin_sbl |
| 借券賣出餘額 | unavailable | 張 | TWSE TWT93U + TPEX margin_sbl |
| 借券賣出增減 | unavailable | 張 | TWSE TWT93U + TPEX margin_sbl |

### 6. 市場成交結構

**資料來源：** 上市 `twse-proxy market_statistics`、上櫃 `TPEX OpenAPI tpex_mainborad_highlight`

| 項目 | 成交金額 | 單位 | 資料來源 |
|---|---|---|---|
| 上市成交金額 | 8,361.4 | 億元 | twse-proxy market_statistics |
| 上櫃成交金額 | 1,762.1 | 億元 | TPEX OpenAPI tpex_mainborad_highlight |
| 上市櫃成交金額合計 | 10,123.5 | 億元 | twse-proxy market_statistics+TPEX OpenAPI tpex_mainborad_highlight |

## 二、重要市場

### 1. 美股指數

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 收盤／最新值 | 漲跌點 | 漲跌幅 | 資料來源 |
|---|---|---|---|---|---|
| S&P 500 | ^GSPC | 7,683.69 | -59.72 | -0.77 | Yahoo Finance Chart API |
| Nasdaq Composite | ^IXIC | 26,820.38 | -248.34 | -0.92 | Yahoo Finance Chart API |
| Nasdaq 100 | ^NDX | 30,276.81 | -331.32 | -1.08 | Yahoo Finance Chart API |
| Dow Jones | ^DJI | 51,481.51 | -347.11 | -0.67 | Yahoo Finance Chart API |
| 費城半導體 SOX | ^SOX | 12,465.24 | -203.69 | -1.61 | Yahoo Finance Chart API |
| VIX | ^VIX | 15.93 | -0.14 | -0.87 | Yahoo Finance Chart API |

### 2. 亞洲主要指數

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 收盤／最新值 | 漲跌點 | 漲跌幅 | 資料來源 |
|---|---|---|---|---|---|
| 日經225 | ^N225 | 65,481.27 | -396.35 | -0.60 | Yahoo Finance Chart API |
| 韓國KOSPI | ^KS11 | 6,870.81 | -18.93 | -0.27 | Yahoo Finance Chart API |
| 香港恆生 | ^HSI | 24,523.57 | -118.94 | -0.48 | Yahoo Finance Chart API |
| 上海綜合 | 000001.SS | 3,830.45 | 6.83 | +0.18 | Yahoo Finance Chart API |
| 深圳成分 | 399001.SZ | 12,901.95 | 43.20 | +0.34 | Yahoo Finance Chart API |

### 3. 美股指數期貨

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 最新值 | 漲跌點 | 漲跌幅 | 資料來源 |
|---|---|---|---|---|---|
| S&P500期貨 | ES=F | 7,756.25 | 9.50 | +0.12 | Yahoo Finance Chart API |
| Nasdaq100期貨 | NQ=F | 30,657.00 | 90.75 | +0.30 | Yahoo Finance Chart API |
| 道瓊期貨 | YM=F | 51,898.00 | 61.00 | +0.12 | Yahoo Finance Chart API |
| Russell2000期貨 | RTY=F | 2,847.90 | 7.80 | +0.27 | Yahoo Finance Chart API |

### 4. 美國國債殖利率

**資料來源：** `U.S. Treasury Fiscal Data API` (失敗時備援 Treasury yield.xml 與 `Yahoo Finance`)

| 項目 | API 資料欄位／識別 | 殖利率 | 日變化 | 資料來源 |
|---|---|---|---|---|
| 美國 2 年期殖利率 | 2 Yr | 4.92 | 0.11 | U.S. Treasury yield.xml (網頁備援) |
| 美國 10 年期殖利率 | 10 Yr | 5.24 | 0.06 | Yahoo Finance (備援) |
| 美國 30 年期殖利率 | 30 Yr | 5.56 | 0.06 | Yahoo Finance (備援) |

### 5. 主要匯率

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 最新值 | 漲跌點 | 漲跌幅 | 資料來源 |
|---|---|---|---|---|---|
| USD/TWD | TWD=X | 31.80 | 0.02 | +0.07 | Yahoo Finance Chart API |
| DXY美元指數 | DX-Y.NYB | 101.35 | 0.15 | +0.15 | Yahoo Finance Chart API |
| USD/JPY | JPY=X | 157.26 | -0.21 | -0.13 | Yahoo Finance Chart API |
| USD/KRW | KRW=X | 1,354.98 | 0.47 | +0.03 | Yahoo Finance Chart API |

### 6. 台灣相關ADR

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 收盤／最新值 | 漲跌點 | 漲跌幅 | 資料來源 |
|---|---|---|---|---|---|
| 台積電ADR | TSM | 452.88 | 2.27 | +0.50 | Yahoo Finance Chart API |
| 聯電ADR | UMC | 23.85 | -0.46 | -1.89 | Yahoo Finance Chart API |
| 日月光ADR | ASX | 43.79 | -0.52 | -1.17 | Yahoo Finance Chart API |

### 7. 原油黃金Bitcoin

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 收盤／最新值 | 漲跌點 | 漲跌幅 | 資料來源 |
|---|---|---|---|---|---|
| WTI原油期貨 | CL=F | 91.81 | -0.79 | -0.85 | Yahoo Finance Chart API |
| 黃金期貨 | GC=F | 4,186.80 | -134.40 | -3.11 | Yahoo Finance Chart API |
| Bitcoin | BTC-USD | 83,991.32 | 488.71 | +0.59 | Yahoo Finance Chart API |

### 8. 重大經濟數據、央行事件與重大市場新聞

**資料來源：** 台股 `tw.stock.yahoo.com` (含內文摘要)；國際 `Fed 公告 RSS`＋`CNBC`＋`MarketWatch` (標題、來源、時間與連結)

- 事件1：台股節後失守4萬8！聯發科重挫7%四寶來救場
  - 來源：Yahoo 台股；發布時間：2026-09-29T09:15:47Z；台北時間：2026-09-29 17:15
  - 摘要：中秋連假後賣壓湧現，台股跌破4萬8！今（29）日加權指數盤中短暫翻紅，最高觸及48,045.13點，隨後在大型電子權值股拖累下走低，終場下跌392.64點或0.82%，收47,631.96點，成交金額7,868.16億元。電子指數下跌1.0
  - 原文連結：https://tw.stock.yahoo.com/news/%E5%A4%96%E8%B3%87%E6%94%B6%E5%81%87%E5%85%88%E7%A0%8D632%E5%84%84%E5%8F%B0%E8%82%A1%E5%A4%B1%E5%AE%884%E8%90%AC8%EF%BC%81%E6%AC%8A%E5%80%BC%E8%82%A1%E7%B6%A0%E6%88%90%E4%B8%80%E7%89%87%E8%81%AF%E7%99%BC%E7%A7%91%E8%B7%8C%E5%9B%9E5%E5%8D%83%E5%85%83-%E5%8F%B0%E5%A1%91%E5%9B%9B%E5%AF%B6%E6%8C%BA%E8%BA%AB%E6%95%91%E5%A0%B4%EF%BD%9Cyahoo%E8%B2%A1%E7%B6%93%E6%8E%83%E6%8F%8F-085851253.html
- 事件2：景氣燈號連9紅 學者提醒發現金也別漏了還國債
  - 來源：Yahoo 台股；發布時間：2026-09-29T09:28:26Z；台北時間：2026-09-29 17:28
  - 摘要：國發會8月景氣對策信號綜合判斷分數為41分，與上月持平，燈號續呈紅燈，也追平史上最長的連9紅紀錄，9項構成項目燈號均維持不變。文化大學經濟系退休教授柏雲昌指出，連9紅追平史上最長，後續還有望繼續延續熱潮，但他也指出，民間企業是否因此願意調漲
  - 原文連結：https://tw.stock.yahoo.com/news/%E7%B6%93%E6%BF%9F%E7%81%AB%E7%86%B1%E3%80%8C%E6%99%AF%E6%B0%A3%E7%87%88%E8%99%9F%E9%80%A39%E7%B4%85%E3%80%8D%E8%BF%BD%E5%B9%B3%E5%8F%B2%E4%B8%8A%E6%9C%80%E9%95%B7%EF%BC%81%E5%AD%B8%E8%80%85%E5%8D%BB%E5%8B%B8%EF%BC%9A%E5%88%A5%E5%8F%AA%E7%99%BC%E7%8F%BE%E9%87%91%E4%B9%9F%E8%A6%81%E9%82%84%E5%9C%8B%E5%82%B5-092826416.html
- 事件3：馬斯克狂催AI算力 美超微拚速度預告「聖誕驚喜」
  - 來源：Yahoo 台股；發布時間：2026-09-29T10:23:17Z；台北時間：2026-09-29 18:23
  - 摘要：AI競賽全面加速，決勝關鍵正從「擁有多少晶片」延伸至「多快讓算力上線」。SpaceX執行長馬斯克近日在社群平台X揭露Colossus超級電腦擴建計畫，並直言，讓龐大算力迅速投入運作極為困難。美超微（Supermicro）執行長梁見後也發文表
  - 原文連結：https://tw.stock.yahoo.com/news/%E9%A6%AC%E6%96%AF%E5%85%8B%E6%8B%9A%E5%85%A8%E9%80%9F%E6%93%B4%E5%BC%B5ai%E7%AE%97%E5%8A%9B-%E7%BE%8E%E8%B6%85%E5%BE%AE%E9%9D%A0%E4%BA%A4%E4%BB%98%E9%80%9F%E5%BA%A6%E6%90%B6%E5%8D%A0%E5%85%88%E6%A9%9F-%E9%A0%90%E5%91%8A%E5%B9%B4%E5%BA%95%E5%B0%87%E6%9C%89-%E8%81%96%E8%AA%95%E9%A9%9A%E5%96%9C-102317584.html
- 事件4：對手還是好夥伴？陳立武親揭英特爾與台積電關係
  - 來源：Yahoo 台股；發布時間：2026-09-29T09:55:00Z；台北時間：2026-09-29 17:55
  - 摘要：英特爾（Intel）近年力拼追上第一線晶圓製造的腳步，追趕台灣的全球第一巨頭台積電，被市場看作是潛在競爭對手之一，不過英特爾執行長陳立武近日在接受Podcast專訪時強調，英特爾仍將台積電視為「合作夥伴」，未來更依然會是台積電的十大客戶之一
  - 原文連結：https://tw.stock.yahoo.com/news/%E5%8F%B0%E7%A9%8D%E9%9B%BB%E6%98%AF%E5%90%88%E4%BD%9C%E5%A4%A5%E4%BC%B4-%E4%B8%8D%E6%98%AF%E5%B0%8D%E6%89%8B-%E8%8B%B1%E7%89%B9%E7%88%BEceo%E9%99%B3%E7%AB%8B%E6%AD%A6%E6%9B%9D%E9%AB%98%E5%B1%A4%E5%A5%BD%E4%BA%A4%E6%83%85-%E7%89%B9%E5%88%A5%E9%A3%9B%E5%8F%B0%E7%81%A3%E6%89%BE%E5%BC%B5%E5%BF%A0%E8%AC%80-095500444.html
- 事件5：房貸補貼最後倒數 符合資格利率最低1.187%
  - 來源：Yahoo 台股；發布時間：2026-09-29T09:57:00Z；台北時間：2026-09-29 17:57
  - 摘要：房貸族把握最後時間。內政部115年度自購及修繕住宅貸款利息補貼，將於9月30日下午5時截止申請，今年規劃6,000戶受惠。自購住宅優惠貸款利率最低1.187%，台北最高250萬元、新北230萬元，且可與青安3.0搭配，2年內已買房並符合資格
  - 原文連結：https://tw.stock.yahoo.com/news/%E6%88%BF%E8%B2%B8%E5%88%A9%E6%81%AF%E8%A3%9C%E8%B2%BC%E6%98%8E%E6%88%AA%E6%AD%A2-%E9%9D%92%E5%AE%89%E5%8F%AF%E6%90%AD-%E6%9C%80%E4%BD%8E%E5%88%A9%E7%8E%871-187-095700910.html
- 事件6：明年EPS直逼1股本！「晶圓代工大廠」獲法人喊價185元　投信投14.7億元買近萬張
  - 來源：Yahoo 台股；發布時間：2026-09-29T11:00:00Z；台北時間：2026-09-29 19:00
  - 摘要：[FTNN新聞網]記者陳献朋／綜合報導台股加權指數今（29）日來到47631.96點，下跌392.64點，跌幅0.82%，成交量達7868億元。根據證交所資料，投信買超14.16億元...
  - 原文連結：https://tw.stock.yahoo.com/news/%E6%98%8E%E5%B9%B4eps%E7%9B%B4%E9%80%BC1%E8%82%A1%E6%9C%AC-%E6%99%B6%E5%9C%93%E4%BB%A3%E5%B7%A5%E5%A4%A7%E5%BB%A0-%E7%8D%B2%E6%B3%95%E4%BA%BA%E5%96%8A%E5%83%B9185%E5%85%83-%E6%8A%95%E4%BF%A1%E6%8A%9514-7%E5%84%84%E5%85%83%E8%B2%B7%E8%BF%91%E8%90%AC%E5%BC%B5-110000248.html
- 事件7：Federal Reserve Board announces approval of application by Peoples Bancorp Inc.
  - 來源：Federal Reserve；發布時間：Fri, 25 Sep 2026 20:30:00 GMT；台北時間：2026-09-26 04:30
  - 摘要：Federal Reserve Board announces approval of application by Peoples Bancorp Inc.
  - 原文連結：https://www.federalreserve.gov/newsevents/pressreleases/orders20260925a.htm
- 事件8：Federal Reserve Board requests public comment on two proposals related to establishing a regulatory framework for Board-supervised payment stablecoin issuers under the GENIUS Act
  - 來源：Federal Reserve；發布時間：Thu, 24 Sep 2026 18:30:00 GMT；台北時間：2026-09-25 02:30
  - 摘要：Federal Reserve Board requests public comment on two proposals related to establishing a regulatory framework for Board-supervised payment stablecoin 
  - 原文連結：https://www.federalreserve.gov/newsevents/pressreleases/bcreg20260924a.htm
- 事件9：Federal Reserve Board issues enforcement action with former employee of Sandy Spring Bank
  - 來源：Federal Reserve；發布時間：Thu, 24 Sep 2026 15:00:00 GMT；台北時間：2026-09-24 23:00
  - 摘要：Federal Reserve Board issues enforcement action with former employee of Sandy Spring Bank
  - 原文連結：https://www.federalreserve.gov/newsevents/pressreleases/enforcement20260924a.htm
- 事件10：Federal Reserve Board announces approval of application by BancFirst Corporation
  - 來源：Federal Reserve；發布時間：Tue, 22 Sep 2026 20:30:00 GMT；台北時間：2026-09-23 04:30
  - 摘要：Federal Reserve Board announces approval of application by BancFirst Corporation
  - 原文連結：https://www.federalreserve.gov/newsevents/pressreleases/orders20260922a.htm
- 事件11：U.S., Iran hold separate mediator talks as Mideast oil exports hit war-time high
  - 來源：CNBC；發布時間：Tue, 29 Sep 2026 04:02:47 GMT；台北時間：2026-09-29 12:02
  - 摘要：Iranian and U.S. officials reportedly met separately with mediators Monday to push for a ceasefire, as Middle Eastern crude exports rebounded to war-t
  - 原文連結：https://www.cnbc.com/2026/09/29/us-iran-war-trump-hormuz-.html
- 事件12：Morgan Stanley's Mike Wilson says an S&P 500 correction may be exactly what the market needs
  - 來源：MarketWatch；發布時間：Tue, 29 Sep 2026 11:03:00 GMT；台北時間：2026-09-29 19:03
  - 摘要：The chief U.S. equity strategist at the investment bank favors large-capitalization quality companies.
  - 原文連結：https://www.marketwatch.com/story/morgan-stanleys-mike-wilson-says-an-s-p-500-correction-may-be-exactly-what-the-market-needs-a6baf54e?mod=mw_rss_topstories


## 三、期貨

**資料來源：**
1. Cloudflare Workers：TAIFEX Proxy — https://taifex.grichtoyang.workers.dev/
2. TAIFEX Open API — https://openapi.taifex.com.tw/

近月契約月份：202610 (日盤成交量最大者)；交易日期：2026-09-29

### 1．台指期近月日盤行情

| 項目 | 數值 | 資料來源 |
|---|---|---|
| 開盤價 | 48,098 | TAIFEX Proxy |
| 最高價 | 48,194 | TAIFEX Proxy |
| 最低價 | 47,630 | TAIFEX Proxy |
| 收盤價 | 47,767 | TAIFEX Proxy |
| 漲跌點數 | -358 | TAIFEX Proxy |
| 漲跌幅 | -0.74 | TAIFEX Proxy |
| 成交量 | 73,240 | TAIFEX Proxy |
| 日盤高點及低點 | 48,194 / 47,630 | TAIFEX Proxy |

### 2．台指期近月夜盤行情

| 項目 | 數值 | 資料來源 |
|---|---|---|
| 開盤價 | 47,915 | TAIFEX Proxy |
| 最高價 | 48,296 | TAIFEX Proxy |
| 最低價 | 47,769 | TAIFEX Proxy |
| 收盤價 | 47,956 | TAIFEX Proxy |
| 漲跌點數 | -169 | TAIFEX Proxy |
| 漲跌幅 | -0.35 | TAIFEX Proxy |
| 成交量 | 29,428 | TAIFEX Proxy |
| 夜盤高點及低點 | 48,296 / 47,769 | TAIFEX Proxy |
| 結算價 | 47,781 | TAIFEX Proxy |
| 未平倉量 | 102,023 | TAIFEX Proxy |

### 3．法人台指期多空未平倉部位

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 外資多方 OI | 8,788 | TAIFEX Proxy |
| 外資空方 OI | 87,817 | TAIFEX Proxy |
| 外資多空淨 OI | -79,029 | TAIFEX Proxy |
| 投信多方 OI | 75,767 | TAIFEX Proxy |
| 投信空方 OI | 2,955 | TAIFEX Proxy |
| 投信多空淨 OI | +72,812 | TAIFEX Proxy |
| 自營商多方 OI | 3,465 | TAIFEX Proxy |
| 自營商空方 OI | 3,953 | TAIFEX Proxy |
| 自營商多空淨 OI | -488 | TAIFEX Proxy |
| 三大法人合計多方 OI | 88,020 | TAIFEX Proxy |
| 三大法人合計空方 OI | 94,725 | TAIFEX Proxy |
| 三大法人合計多空淨 OI | -6,705 | TAIFEX Proxy |
| 外資多空淨 OI 變化 | -1,998 | TAIFEX Proxy |
| 投信多空淨 OI 變化 | -52 | TAIFEX Proxy |
| 自營商多空淨 OI 變化 | +1,032 | TAIFEX Proxy |

### 4．前十大交易人多空未平倉部位

**資料來源：** `TAIFEX OpenAPI OpenInterestOfLargeTradersFutures` (官方資料落後約一日，標示實際日期)

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 前十大交易人多方 OI | 78,199 | TAIFEX Proxy |
| 前十大交易人空方 OI | 70,805 | TAIFEX Proxy |
| 前十大交易人多空淨 OI | +7,394 | TAIFEX Proxy |
| 多空淨 OI 變化 (2026-09-24→2026-09-24) | +0 | TAIFEX Proxy snapshots (2026-09-28) |
- 資料日期：2026-09-24 (TypeOfTraders=0 全部交易人；契約月份 202610)

### 5．日盤、夜盤法人交易資料

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 外資日盤多單交易量 | 42,631 | TAIFEX Proxy |
| 外資日盤空單交易量 | 43,640 | TAIFEX Proxy |
| 外資日盤多空淨交易量 | -1,009 | TAIFEX Proxy |
| 外資夜盤多單交易量 | 16,603 | TAIFEX Proxy |
| 外資夜盤空單交易量 | 16,638 | TAIFEX Proxy |
| 外資夜盤多空淨交易量 | -35 | TAIFEX Proxy |
| 外資日盤／夜盤交易量變化 | -974 | TAIFEX Proxy |
| 投信日盤多空淨交易量 | -52 | TAIFEX Proxy |
| 投信夜盤多空淨交易量 | +0 | TAIFEX Proxy |
| 投信日盤／夜盤交易量變化 | -52 | TAIFEX Proxy |
| 自營商日盤多空淨交易量 | +981 | TAIFEX Proxy |
| 自營商夜盤多空淨交易量 | +389 | TAIFEX Proxy |
| 自營商日盤／夜盤交易量變化 | +592 | TAIFEX Proxy |
| 三大法人日盤多空淨交易量 | -80 | TAIFEX Proxy |
| 三大法人夜盤多空淨交易量 | +354 | TAIFEX Proxy |
| 法人日盤交易金額淨額 (億元) | -7.4 | TAIFEX Proxy |
| 法人夜盤交易金額淨額 (億元) | +34.0 | TAIFEX Proxy |

### 6．期貨與現貨關係

| 項目 | 數值 | 資料來源 |
|---|---|---|
| 台指期近月價格 | 47,767 | TAIFEX Proxy |
| 加權指數價格 | 47,631.96 | twse-proxy |
| 台指期與加權指數價差 | +135.04 | TAIFEX Proxy+twse-proxy |
| 價差百分比 | +0.28 | TAIFEX Proxy+twse-proxy |
| 日盤基差 | +135.04 | TAIFEX Proxy+twse-proxy |
| 夜盤價格相對日盤收盤的變化 | +189 | TAIFEX Proxy |

### 7．日盤、夜盤與籌碼變化對照

#### 7.1 日夜盤價格與成交量對照 (變化 = 日盤 - 夜盤)

| 項目 | 日盤 | 夜盤 | 變化 (日-夜) | 資料來源 |
|---|---|---|---|---|
| 收盤價 | 47,767 | 47,956 | -189 | TAIFEX Proxy |
| 成交量 | 43,812 | 29,428 | +14,384 | TAIFEX Proxy |
- 台指期總 OI 前日變化：-1,018（來源：TAIFEX Proxy）


#### 7.2 法人籌碼日夜盤對照 (淨變化 = 日盤淨 - 夜盤淨；OI 為日盤收盤後總量，前日變化另列)

| 法人 | 交易量 |  |  |  |  |  |  | 未平倉量 |  |  |  | 資料來源 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|  | **日盤多單** | **日盤空單** | **日盤淨** | **夜盤多單** | **夜盤空單** | **夜盤淨** | **淨變化 (日-夜)** | **OI多方** | **OI空方** | **OI淨** | **OI前日變化** |  |
| 外資 | 42,631 | 43,640 | -1,009 | 16,603 | 16,638 | -35 | -974 | 8,788 | 87,817 | -79,029 | -1,998 | TAIFEX Proxy |
| 投信 | 68 | 120 | -52 | 0 | 0 | +0 | -52 | 75,767 | 2,955 | +72,812 | -52 | TAIFEX Proxy |
| 自營商 | 4,255 | 3,274 | +981 | 872 | 483 | +389 | +592 | 3,465 | 3,953 | -488 | +1,032 | TAIFEX Proxy |
| 三大法人合計 | 46,954 | 47,034 | -80 | 17,475 | 17,121 | +354 | -434 | 88,020 | 94,725 | -6,705 | -1,018 | TAIFEX Proxy |

#### 7.3 前十大交易人日夜盤對照 (OI 無日夜拆分，列收盤後總量)

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 前十大交易人多方 OI | 78,199 | TAIFEX Proxy |
| 前十大交易人空方 OI | 70,805 | TAIFEX Proxy |
| 前十大交易人多空淨 OI | +7,394 | TAIFEX Proxy |
| 前十大交易人多空淨 OI 變化 (2026-09-24→2026-09-24) | +0 | TAIFEX Proxy snapshots (2026-09-28) |

#### 7.4 夜盤劇本分類 (規則對應：夜盤漲跌 × 外資夜盤偏多空)

| 項目 | 數值 | 資料來源 |
|---|---|---|
| 夜盤成交量占比 (夜盤量／(夜盤量＋日盤量)) | 40.18% | TAIFEX Proxy |
| 夜盤漲跌點數 | -169 | TAIFEX Proxy |
| 外資夜盤多空淨交易量 | -35 | TAIFEX Proxy |
| 劇本分類 | 劇本三 | 規則對應 |
| 劇本條件 | 夜盤下跌＋外資偏空 | 規則對應 |
| 劇本特徵 | 開低、續跌機率高 | 規則對應 |

## 四、選擇權

**資料來源：** 主要 TAIFEX 經 Cloudflare Worker Proxy；時區 `Asia/Taipei`

### 1．選擇權交易日期、到期日與資料時間

| 項目 | 數值 | 資料來源 |
|---|---|---|
| 交易日期 | 2026-09-29 | TAIFEX Proxy |
| 到期月份／到期日 | 202609F4 | TAIFEX Proxy |
| 資料更新時間 | 2026-09-29 19:14:53 | 本機 |
| 日盤／夜盤標記 | 日盤收盤後資料 | TAIFEX Proxy |

### 2．Call 總成交量、OI、OI 增減

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Call 總成交量 | 259,809 | TAIFEX Proxy |
| Call 總未平倉量 OI | 65,523 | TAIFEX Proxy |
| Call OI 增減 | unavailable | 端點未提供 |

### 3．Put 總成交量、OI、OI 增減

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Put 總成交量 | 246,986 | TAIFEX Proxy |
| Put 總未平倉量 OI | 44,870 | TAIFEX Proxy |
| Put OI 增減 | unavailable | 端點未提供 |

### 4．Call／Put 比例與變化

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Call／Put 成交量比例 | 1.05 | TAIFEX Proxy |
| Call／Put 未平倉量比例 | 1.46 | TAIFEX Proxy |
| Put／Call Ratio | 0.68 | TAIFEX Proxy |
| Call／Put 比例變化 (量比 2026-09-23→2026-09-24) | 25.27 | TAIFEX Proxy |
| 與前一交易日比較 (OI 比 2026-09-23→2026-09-24) | 5.50 | TAIFEX Proxy |
**資料來源：** 比例 `TAIFEX Proxy chain`；變化 `TAIFEX Proxy PutCallRatio`

### 5．外資 Call／Put 部位

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 外資 Call日買 | 95,546 | TAIFEX Proxy |
| 外資 Call日賣 | 98,706 | TAIFEX Proxy |
| 外資 Call日淨 | -3,160 | TAIFEX Proxy |
| 外資 Put日買 | 103,371 | TAIFEX Proxy |
| 外資 Put日賣 | 104,254 | TAIFEX Proxy |
| 外資 Put日淨 | -883 | TAIFEX Proxy |
| 外資 Call夜買 | 18,103 | TAIFEX Proxy |
| 外資 Call夜賣 | 18,219 | TAIFEX Proxy |
| 外資 Call夜淨 | -116 | TAIFEX Proxy |
| 外資 Put夜買 | 20,577 | TAIFEX Proxy |
| 外資 Put夜賣 | 20,634 | TAIFEX Proxy |
| 外資 Put夜淨 | -57 | TAIFEX Proxy |
| 外資 日盤淨總量 | -2,277 | TAIFEX Proxy |
| 外資 Call日夜淨增減 (日－夜) | -3,044 | TAIFEX Proxy |
| 外資 Put日夜淨增減 (日－夜) | -826 | TAIFEX Proxy |

### 6．自營商 Call／Put 部位

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 自營商 Call日買 | 81,161 | TAIFEX Proxy |
| 自營商 Call日賣 | 93,074 | TAIFEX Proxy |
| 自營商 Call日淨 | -11,913 | TAIFEX Proxy |
| 自營商 Put日買 | 77,282 | TAIFEX Proxy |
| 自營商 Put日賣 | 83,291 | TAIFEX Proxy |
| 自營商 Put日淨 | -6,009 | TAIFEX Proxy |
| 自營商 Call夜買 | 10,032 | TAIFEX Proxy |
| 自營商 Call夜賣 | 12,257 | TAIFEX Proxy |
| 自營商 Call夜淨 | -2,225 | TAIFEX Proxy |
| 自營商 Put夜買 | 12,328 | TAIFEX Proxy |
| 自營商 Put夜賣 | 12,245 | TAIFEX Proxy |
| 自營商 Put夜淨 | +83 | TAIFEX Proxy |
| 自營商 日盤淨總量 | -5,904 | TAIFEX Proxy |
| 自營商 Call日夜淨增減 (日－夜) | -9,688 | TAIFEX Proxy |
| 自營商 Put日夜淨增減 (日－夜) | -6,092 | TAIFEX Proxy |

### 7．主要 Call OI 集中區

| 項目 | 履約價 | OI | 資料來源 |
|---|---|---|---|
| Call OI 第1大履約價 | 48,000 | 4,407 | TAIFEX Proxy |
| Call OI 第2大履約價 | 50,500 | 3,828 | TAIFEX Proxy |
| Call OI 第3大履約價 | 47,900 | 3,707 | TAIFEX Proxy |
| Call OI 最大履約價 | 48,000 | 4,407 | TAIFEX Proxy |

#### Call OI 分布明細 Top10 (機器可讀，到期月份 202609F4)

| # | 履約價 | OI | 佔比 | 資料來源 |
|---|---|---|---|---|
| C1 | 48,000 | 4,407 | 6.73% | TAIFEX Proxy |
| C2 | 50,500 | 3,828 | 5.84% | TAIFEX Proxy |
| C3 | 47,900 | 3,707 | 5.66% | TAIFEX Proxy |
| C4 | 47,800 | 3,510 | 5.36% | TAIFEX Proxy |
| C5 | 48,200 | 2,752 | 4.2% | TAIFEX Proxy |
| C6 | 47,750 | 2,684 | 4.1% | TAIFEX Proxy |
| C7 | 51,900 | 2,455 | 3.75% | TAIFEX Proxy |
| C8 | 47,700 | 2,107 | 3.22% | TAIFEX Proxy |
| C9 | 48,100 | 2,106 | 3.21% | TAIFEX Proxy |
| C10 | 47,850 | 1,985 | 3.03% | TAIFEX Proxy |


### 8．主要 Put OI 集中區

| 項目 | 履約價 | OI | 資料來源 |
|---|---|---|---|
| Put OI 第1大履約價 | 47,700 | 3,785 | TAIFEX Proxy |
| Put OI 第2大履約價 | 47,600 | 3,307 | TAIFEX Proxy |
| Put OI 第3大履約價 | 47,500 | 2,692 | TAIFEX Proxy |
| Put OI 最大履約價 | 47,700 | 3,785 | TAIFEX Proxy |

#### Put OI 分布明細 Top10 (機器可讀，到期月份 202609F4)

| # | 履約價 | OI | 佔比 | 資料來源 |
|---|---|---|---|---|
| P1 | 47,700 | 3,785 | 8.44% | TAIFEX Proxy |
| P2 | 47,600 | 3,307 | 7.37% | TAIFEX Proxy |
| P3 | 47,500 | 2,692 | 6.0% | TAIFEX Proxy |
| P4 | 47,550 | 2,674 | 5.96% | TAIFEX Proxy |
| P5 | 47,650 | 1,952 | 4.35% | TAIFEX Proxy |
| P6 | 43,000 | 1,617 | 3.6% | TAIFEX Proxy |
| P7 | 47,000 | 1,345 | 3.0% | TAIFEX Proxy |
| P8 | 47,800 | 1,223 | 2.73% | TAIFEX Proxy |
| P9 | 46,000 | 1,203 | 2.68% | TAIFEX Proxy |
| P10 | 47,400 | 1,138 | 2.54% | TAIFEX Proxy |


### 9．Call OI 增減集中區

| 項目 | 履約價 (增減口數) | 資料來源 |
|---|---|---|
| Call OI 增加最多的履約價 | unavailable | 端點未提供 |
| Call OI 減少最多的履約價 | unavailable | 端點未提供 |

### 10．Put OI 增減集中區

| 項目 | 履約價 (增減口數) | 資料來源 |
|---|---|---|
| Put OI 增加最多的履約價 | unavailable | 端點未提供 |
| Put OI 減少最多的履約價 | unavailable | 端點未提供 |

### 11．Call Wall

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Call Wall 價位 | 48,000 | TAIFEX Proxy |
| 對應到期月份 | 202609F4 | TAIFEX Proxy |
| 與前一交易日的變化 | unavailable | 端點未提供 |

### 12．Put Wall

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Put Wall 價位 | 47,700 | TAIFEX Proxy |
| 對應到期月份 | 202609F4 | TAIFEX Proxy |
| 與前一交易日的變化 | unavailable | 端點未提供 |

### 13．Gamma Wall

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Gamma Wall 價位 | unavailable | 端點未提供 |
| 對應到期月份 | 202609F4 | TAIFEX Proxy |
| 資料日期 | unavailable | 端點未提供 |

### 14．Gamma Flip

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Gamma Flip 價位 | unavailable | 端點未提供 |
| 對應到期月份 | 202609F4 | TAIFEX Proxy |
| 資料日期 | unavailable | 端點未提供 |

### 15．Max Pain

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Max Pain 價位 | 47,700 | TAIFEX Proxy |
| 對應到期月份 | 202609F4 | TAIFEX Proxy |
| 與前一交易日的變化 | unavailable | 端點未提供 |

### 17．選擇權法人日盤、夜盤交易

| 法人 | 日盤多單 | 日盤空單 | 日盤淨 | 夜盤多單 | 夜盤空單 | 夜盤淨 | 淨變化 (日-夜) | 資料來源 |
|---|---|---|---|---|---|---|---|---|
| 外資 | 199,800 | 202,077 | -2,277 | 38,737 | 38,796 | -59 | -2,218 | TAIFEX Proxy |
| 投信 | 0 | 4,500 | -4,500 | 0 | 0 | +0 | -4,500 | TAIFEX Proxy |
| 自營商 | 164,452 | 170,356 | -5,904 | 22,277 | 24,585 | -2,308 | -3,596 | TAIFEX Proxy |
| 三大法人合計 | 364,252 | 376,933 | -12,681 | 61,014 | 63,381 | -2,367 | -10,314 | TAIFEX Proxy |
- 方法論：多方＝買Call＋賣Put（看多），空方＝賣Call＋買Put（看空），淨額＝看多－看空（已用 Call／Put 拆分頁交叉驗算一致）
- 公式：多方(買)－空方(賣)＝（買call＋賣put）－（賣call＋買put）＝看多－看空
- 速記：多＝BC＋SP、空＝SC＋BP

#### 法人多空力道表（金額・億元；上游千元／1e5）

| 法人 | 日多方力道 | 日空方力道 | 日淨多空力道 | 夜多方力道 | 夜空方力道 | 夜淨多空力道 | 日淨－夜淨 | 資料來源 |
|---|---|---|---|---|---|---|---|---|
| 外資 | 9.97 | 10.09 | -0.12 | 3.68 | 3.73 | -0.05 | -0.07 | TAIFEX Proxy |
| 投信 | 0.00 | 0.99 | -0.99 | 0.00 | 0.00 | +0 | -0.99 | TAIFEX Proxy |
| 自營商 | 8.64 | 8.20 | +0.44 | 1.82 | 2.33 | -0.52 | +0.96 | TAIFEX Proxy |
| 三大法人合計 | 18.62 | 19.28 | -0.67 | 5.50 | 6.06 | -0.57 | -0.10 | TAIFEX Proxy |

### 18．選擇權前十大

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 買權多方 OI | 12,023 | TAIFEX Proxy |
| 買權空方 OI | 10,907 | TAIFEX Proxy |
| 買權多空淨 OI | +1,116 | TAIFEX Proxy |
| 買權多空淨 OI 變化 (2026-09-24→2026-09-24) | +0 | TAIFEX Proxy snapshots (2026-09-28) |

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 賣權多方 OI | 7,486 | TAIFEX Proxy |
| 賣權空方 OI | 8,368 | TAIFEX Proxy |
| 賣權多空淨 OI | -882 | TAIFEX Proxy |
| 賣權多空淨 OI 變化 (2026-09-24→2026-09-24) | +0 | TAIFEX Proxy snapshots (2026-09-28) |
- 資料日期：買權 2026-09-24／賣權 2026-09-24 (TypeOfTraders=0 全部交易人；契約月份 202610)

#### 大戶流向（全日；前十大無日夜拆分）

| 項目 | 淨變化 | 區間 | 資料來源 |
|---|---|---|---|
| 期貨前十大 | +0 | 2026-09-24→2026-09-24 | TAIFEX Proxy snapshots (2026-09-28) |
| 買權前十大 | +0 | 2026-09-24→2026-09-24 | TAIFEX Proxy snapshots (2026-09-28) |
| 賣權前十大 | +0 | 2026-09-24→2026-09-24 | TAIFEX Proxy snapshots (2026-09-28) |

### 16．資料來源、時間、時區與狀態

- 資料來源：TAIFEX 經 Cloudflare Worker Proxy
- 資料日期：2026-09-29；資料時間：2026-09-29 19:14:53；時區：`Asia/Taipei`
- 日盤／夜盤標記：日盤收盤後 + 夜盤盤後
- 未取得欄位 (7)：margin.fin_yi, margin.fin_chg_yi, sbl.sale_bal, sbl.sale_chg, futures.gamma_wall, futures.gamma_flip, options.chain_oi_change
- 註記：法人交易量變化無昨日交易端點，標 unavailable
- 註記：Gamma Wall/Flip 無資料 (proxy 端點上游無資料)，標 unavailable

## 五、資料來源、時間與完整性

- 期貨/匯率為最新報價，其餘為 T0 收盤資料；時間皆為 `Asia/Taipei`。
- taiex：`twse-proxy`
- taiex_ohlc：`FinMind TaiwanStockPrice TAIEX`
- listed_turnover：`twse-proxy market_statistics`
- listed_breadth：`twse-proxy`
- otc：`TPEX OpenAPI tpex_mainborad_highlight`
- institutional：`twse-proxy /institutional`
- margin_short：`TWSE MI_MARGN + TPEX margin_balance (張)`
- margin_ratio：`前值遞補 (DATA 2026-09-24；當日三源皆失敗；民間估算；官方無每日序列)`
- sbl：`TWSE TWT93U + TPEX margin_sbl`
- 期貨選擇權：`TAIFEX Proxy`
- 新聞：台股 Yahoo／國際 Fed＋CNBC＋MarketWatch；台股 Yahoo / 國際 Fed 公告＋CNBC＋MarketWatch RSS；Fed 無摘要；investing 港股為主已退役；cnyes CSR、wantgoo JS 算繪、中央社/央行路徑待查，未採用
- 美股/亞股/期貨/匯率/ADR/商品：`Yahoo Finance Chart API`；美債：`Yahoo Finance (備援)`
- 註記：HiStock 未取得，融資餘額/增減標 unavailable (官方逐股加總僅有張數)
- 註記：融券沿用官方逐股加總 (張)
- 註記：融資維持率未取得 (三源皆失敗；官方無每日序列)
- 註記：融資維持率採前值遞補 (DATA 2026-09-24)，非 T0 2026-09-29
- 註記：上市 MI_MARGN / TWT96U 無日期欄，採用最新可得
- 本報告僅整理資料，不提供交易判斷。

## 六、期現選方向對照

**規則：** 趨勢偏多／空＝現貨、期貨OI、選擇權日淨三者同向；避險／對沖＝現貨與期選反向；日內反轉＝日淨與夜淨反向；缺值標示，不推估。選擇權多空為看多看空口徑。

| 法人 | 現貨買賣超(億) | 期貨OI淨(口) | 期貨日淨 | 期貨夜淨 | 選擇權日淨 | 選擇權夜淨 | 判定 | 期選組合 | 資料來源 |
|---|---|---|---|---|---|---|---|---|---|
| 外資 | -632.0 | -79,029 | -1,009 | -35 | -2,277 | -59 | 趨勢偏空 | 趨勢偏空 | twse-proxy／TAIFEX Proxy |
| 投信 | +14.2 | +72,812 | -52 | +0 | -4,500 | +0 | 避險／對沖 | 分歧 | twse-proxy／TAIFEX Proxy |
| 自營商 | -164.0 | -488 | +981 | +389 | -5,904 | -2,308 | 趨勢偏空 | 趨勢偏空 | twse-proxy／TAIFEX Proxy |
