# DATA_REPORT_20261022

- 報告日期：`2026-10-22`
- T0 交易日期：`2026-10-22`
- 資料產出時間：`2026-10-22 23:46:34`
- 時區：`Asia/Taipei`
- 產出盤別：`日盤`
- 產出者：`actions`
- 排定班別：`evening`

---

## 一、現貨

### 1. 台股大盤行情

**資料來源：** `Cloudflare Worker：twse-proxy` (備援 `TWSE OpenAPI MI_INDEX`)

| 項目 | 數值 | 單位 | 資料來源 |
|---|---|---|---|
| 加權指數 | 46,041.43 | 點 | twse-proxy |
| 開盤 | 46,942.75 | 點 | FinMind TaiwanStockPrice TAIEX |
| 最高 | 47,332.18 | 點 | FinMind TaiwanStockPrice TAIEX |
| 最低 | 46,041.43 | 點 | FinMind TaiwanStockPrice TAIEX |
| 收盤 | 46,041.43 | 點 | twse-proxy |
| 漲跌點數 | -846.34 | 點 | twse-proxy |
| 漲跌幅 | -1.81 | % | twse-proxy |
| 成交金額 | 9,334.4 | 億元 | twse-proxy market_statistics |

### 2. 市場漲跌家數

#### 2.1 上市公司

**資料來源：** `Cloudflare Worker：twse-proxy` (備援 `TWSE OpenAPI twtazu_od`)

| 項目 | 家數 | 資料來源 |
|---|---|---|
| 上漲家數 | 247 | twse-proxy |
| 下跌家數 | 756 | twse-proxy |
| 平盤家數 | 74 | twse-proxy |
| 漲停家數 | 3 | twse-proxy |
| 跌停家數 | 5 | twse-proxy |

#### 2.2 上櫃公司

**資料來源：** `TPEX OpenAPI tpex_mainborad_highlight`

| 項目 | 家數 | 資料來源 |
|---|---|---|
| 上漲家數 | 146 | TPEX OpenAPI tpex_mainborad_highlight |
| 下跌家數 | 659 | TPEX OpenAPI tpex_mainborad_highlight |
| 平盤家數 | 63 | TPEX OpenAPI tpex_mainborad_highlight |
| 漲停家數 | 17 | TPEX OpenAPI tpex_mainborad_highlight |
| 跌停家數 | 11 | TPEX OpenAPI tpex_mainborad_highlight |

### 3. 三大法人現貨買賣超

**資料來源：** `TWSE RWD BFI82U`

| 法人別 | 買賣超金額 | 單位 | 資料來源 |
|---|---|---|---|
| 外資 | -815.8 | 億元 | twse-proxy /institutional |
| 投信 | +94.9 | 億元 | twse-proxy /institutional |
| 自營商 | -273.8 | 億元 | twse-proxy /institutional |
| 三大法人合計 | -994.7 | 億元 | twse-proxy /institutional |

### 4. 融資融券

**資料來源：** 上市+上櫃 `HiStock` (金額口徑)；維持率 `istock.tw`；備援官方逐股加總

| 項目 | 數值 | 單位 | 資料來源 |
|---|---|---|---|
| 融資餘額 | 8,465.1 | 億元 | HiStock 上市+上櫃融資融券 (金額口徑) |
| 融資增減 | -138.3 | 億元 | HiStock 上市+上櫃融資融券 (金額口徑) |
| 融券餘額 | 253,430 | 張 | HiStock 上市+上櫃融資融券 (金額口徑) |
| 融券增減 | 22,348 | 張 | HiStock 上市+上櫃融資融券 (金額口徑) |
| 融資維持率 | 182.90 | % | stockintelli 大盤融資維持率 (民間估算；官方無每日序列) |

### 5. 借券資料

**資料來源：** 上市 `TWSE OpenAPI TWT96U` (可借餘額)、上櫃 `TPEX OpenAPI tpex_margin_sbl`

| 項目 | 數值 | 單位 | 資料來源 |
|---|---|---|---|
| 借券餘額 | 4,575,635 | 張 | TWSE TWT93U + TPEX margin_sbl |
| 借券賣出餘額 | 36,891 | 張 | TWSE TWT93U + TPEX margin_sbl |
| 借券賣出增減 | -1,593 | 張 | TWSE TWT93U + TPEX margin_sbl |

### 6. 市場成交結構

**資料來源：** 上市 `twse-proxy market_statistics`、上櫃 `TPEX OpenAPI tpex_mainborad_highlight`

| 項目 | 成交金額 | 單位 | 資料來源 |
|---|---|---|---|
| 上市成交金額 | 9,334.4 | 億元 | twse-proxy market_statistics |
| 上櫃成交金額 | 2,255.4 | 億元 | TPEX OpenAPI tpex_mainborad_highlight |
| 上市櫃成交金額合計 | 11,589.8 | 億元 | twse-proxy market_statistics+TPEX OpenAPI tpex_mainborad_highlight |

## 二、重要市場

### 1. 美股指數

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 收盤／最新值 | 漲跌點 | 漲跌幅 | 資料來源 |
|---|---|---|---|---|---|
| S&P 500 | ^GSPC | 7,658.03 | -99.14 | -1.28 | Yahoo Finance Chart API |
| Nasdaq Composite | ^IXIC | 26,103.03 | -599.83 | -2.25 | Yahoo Finance Chart API |
| Nasdaq 100 | ^NDX | 29,093.94 | -728.58 | -2.44 | Yahoo Finance Chart API |
| Dow Jones | ^DJI | 52,744.39 | -111.70 | -0.21 | Yahoo Finance Chart API |
| 費城半導體 SOX | ^SOX | 10,810.39 | -695.17 | -6.04 | Yahoo Finance Chart API |
| VIX | ^VIX | 19.06 | 2.38 | +14.27 | Yahoo Finance Chart API |

### 2. 亞洲主要指數

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 收盤／最新值 | 漲跌點 | 漲跌幅 | 資料來源 |
|---|---|---|---|---|---|
| 日經225 | ^N225 | 64,621.24 | 545.82 | +0.85 | Yahoo Finance Chart API |
| 韓國KOSPI | ^KS11 | 5,735.66 | 182.92 | +3.29 | Yahoo Finance Chart API |
| 香港恆生 | ^HSI | 22,934.68 | -717.19 | -3.03 | Yahoo Finance Chart API |
| 上海綜合 | 000001.SS | 3,658.03 | -55.00 | -1.48 | Yahoo Finance Chart API |
| 深圳成分 | 399001.SZ | 11,357.32 | -347.03 | -2.96 | Yahoo Finance Chart API |

### 3. 美股指數期貨

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 最新值 | 漲跌點 | 漲跌幅 | 資料來源 |
|---|---|---|---|---|---|
| S&P500期貨 | ES=F | 7,701.75 | -98.50 | -1.26 | Yahoo Finance Chart API |
| Nasdaq100期貨 | NQ=F | 29,305.50 | -701.50 | -2.34 | Yahoo Finance Chart API |
| 道瓊期貨 | YM=F | 52,948.00 | -111.00 | -0.21 | Yahoo Finance Chart API |
| Russell2000期貨 | RTY=F | 2,786.40 | -7.80 | -0.28 | Yahoo Finance Chart API |

### 4. 美國國債殖利率

**資料來源：** `U.S. Treasury Fiscal Data API` (失敗時備援 Treasury yield.xml 與 `Yahoo Finance`)

| 項目 | API 資料欄位／識別 | 殖利率 | 日變化 | 資料來源 |
|---|---|---|---|---|
| 美國 2 年期殖利率 | 2 Yr | 4.81 | 0.02 | U.S. Treasury yield.xml (網頁備援) |
| 美國 10 年期殖利率 | 10 Yr | 5.01 | -0.14 | Yahoo Finance (備援) |
| 美國 30 年期殖利率 | 30 Yr | 5.33 | -0.11 | Yahoo Finance (備援) |

### 5. 主要匯率

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 最新值 | 漲跌點 | 漲跌幅 | 資料來源 |
|---|---|---|---|---|---|
| USD/TWD | TWD=X | 32.60 | 0.02 | +0.06 | Yahoo Finance Chart API |
| DXY美元指數 | DX-Y.NYB | 101.78 | -0.00 | -0.00 | Yahoo Finance Chart API |
| USD/JPY | JPY=X | 157.12 | -1.15 | -0.72 | Yahoo Finance Chart API |
| USD/KRW | KRW=X | 1,325.97 | 2.03 | +0.15 | Yahoo Finance Chart API |

### 6. 台灣相關ADR

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 收盤／最新值 | 漲跌點 | 漲跌幅 | 資料來源 |
|---|---|---|---|---|---|
| 台積電ADR | TSM | 412.71 | -19.18 | -4.44 | Yahoo Finance Chart API |
| 聯電ADR | UMC | 18.52 | -1.30 | -6.56 | Yahoo Finance Chart API |
| 日月光ADR | ASX | 38.48 | -3.93 | -9.27 | Yahoo Finance Chart API |

### 7. 原油黃金Bitcoin

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 收盤／最新值 | 漲跌點 | 漲跌幅 | 資料來源 |
|---|---|---|---|---|---|
| WTI原油期貨 | CL=F | 98.28 | 1.13 | +1.16 | Yahoo Finance Chart API |
| 黃金期貨 | GC=F | 4,070.10 | -79.90 | -1.93 | Yahoo Finance Chart API |
| Bitcoin | BTC-USD | 81,389.89 | -2,622.08 | -3.12 | Yahoo Finance Chart API |

### 8. 重大經濟數據、央行事件與重大市場新聞

**資料來源：** 台股 `tw.stock.yahoo.com` (含內文摘要)；國際 `Fed 公告 RSS`＋`CNBC`＋`MarketWatch` (標題、來源、時間與連結)

- 事件1：台北股匯休市！ 薔琵颱風停班 4檔個股除權息延後到下周二
  - 來源：Yahoo 台股；發布時間：2026-10-22T12:01:18Z；台北時間：2026-10-22 20:01
  - 摘要：受颱風薔琵影響，北北基桃宣布明（23）日停止上班上課。隨著台北市停班，台股、期貨及台北外匯市場也將同步休市一日，共有 4 檔標的除權息日程順延，另有3檔興櫃掛牌案也將一併延後至下周二進行。
  - 原文連結：https://tw.stock.yahoo.com/news/%E5%8F%B0%E5%8C%97%E8%82%A1%E5%8C%AF%E4%BC%91%E5%B8%82%EF%BC%81-%E8%96%94%E7%90%B5%E9%A2%B1%E9%A2%A8%E5%81%9C%E7%8F%AD-4%E6%AA%94%E5%80%8B%E8%82%A1%E9%99%A4%E6%AC%8A%E6%81%AF%E5%BB%B6%E5%BE%8C%E5%88%B0%E4%B8%8B%E5%91%A8%E4%BA%8C-122538662.html
- 事件2：三大法人千億賣單倒下來 台股險守4萬6資安金融扛大旗
  - 來源：Yahoo 台股；發布時間：2026-10-22T09:09:39Z；台北時間：2026-10-22 17:09
  - 摘要：連假前賣壓湧現，台股重挫846點、險守4萬6！今(22)日加權指數終場下跌846.34點、跌幅1.81%，收46,041.43點，成交金額8,815.61億元。大盤早盤一度上漲444點、重返4萬7，隨後受到美股期貨走弱，以及薔琵颱風可能拉長
  - 原文連結：https://tw.stock.yahoo.com/news/%E6%B3%95%E4%BA%BA%E6%8F%90%E6%AC%BE%E5%8D%83%E5%84%84%E5%8F%B0%E8%82%A1%E9%A2%B3%E5%A4%A7%E9%A2%A8%EF%BC%81%E9%87%8D%E6%8C%AB846%E9%BB%9E%E9%9A%AA%E5%AE%884%E8%90%AC6-%E8%B3%87%E5%AE%89%E6%8F%AA%E9%87%91%E8%9E%8D%E7%95%B6%E6%8A%97%E8%B7%8C%E9%9D%A0%E5%B1%B1%EF%BD%9Cyahoo%E8%B2%A1%E7%B6%93%E6%8E%83%E6%8F%8F-090939291.html
- 事件3：富邦台50擬1拆8 一張26萬變3萬多12月交付表決
  - 來源：Yahoo 台股；發布時間：2026-10-22T10:10:33Z；台北時間：2026-10-22 18:10
  - 摘要：71萬人開心！有「小0050」之稱的富邦台50（006208）也要加入分割行列！富邦投信今（22）日公告旗下規模最大ETF將於12月18日召開受益人會議，表決是否啟動基金分割，初步估計一拆8，屆時每股淨值剩約33元多，等於一張花3.3萬元即
  - 原文連結：https://tw.stock.yahoo.com/news/71%E8%90%AC%E4%BA%BA%E9%96%8B%E5%BF%83%EF%BC%81%E5%AF%8C%E9%82%A6%E3%80%8C%E5%B0%8F0050%E3%80%8D%E8%A6%811%E6%8B%868-%E4%B8%80%E5%BC%B5%E5%8F%AA%E8%A6%813%E8%90%AC%E5%A4%9A-101033379.html
- 事件4：台電累虧恐再破4200億 電價怎麼調點名外銷產業多負擔
  - 來源：Yahoo 台股；發布時間：2026-10-22T09:46:12Z；台北時間：2026-10-22 17:46
  - 摘要：今年10月電價暫緩調整，延至12月電價費率審議會討論，政院撥補台電711億能否到手成為關鍵。台電今（22）日說明，因中東戰爭推升天然氣價格飆漲，台電估計全年民生用電吸收逾760億元，盼爭取撥補預算挹注。至於未來電價政策方向？台電則表示，較有
  - 原文連結：https://tw.stock.yahoo.com/news/12%E6%9C%88%E9%9B%BB%E5%83%B9%E8%A6%81%E5%86%8D%E6%BC%B2%EF%BC%9F%E7%B4%AF%E8%99%A7%E4%B8%8A%E7%9C%8B4200%E5%84%84%E5%85%83-%E5%8F%B0%E9%9B%BB%EF%BC%9A%E5%A4%96%E9%8A%B7%E7%94%A2%E6%A5%AD%E5%A4%9A%E8%B2%A0%E6%93%94-095000064.html
- 事件5：網通股王連跌三天 智邦擬辦現增募資估上看142億
  - 來源：Yahoo 台股；發布時間：2026-10-22T10:28:02Z；台北時間：2026-10-22 18:28
  - 摘要：「網通股王」智邦（2345）要辦現金增資！今（22）日輸入公開資訊觀測站經董事會決議要發行一萬張新股，以股票市價每股高達1775元、一般現增打8折價來算，此次募資金額上看142億元以上，且股本56億元來看，稀釋率約1.78%，股價已連跌三天
  - 原文連結：https://tw.stock.yahoo.com/news/%E3%80%8C%E7%B6%B2%E9%80%9A%E8%82%A1%E7%8E%8B%E3%80%8D%E6%99%BA%E9%82%A6%E8%A6%81%E8%BE%A6%E7%8F%BE%E5%A2%9E1%E8%90%AC%E5%BC%B5-%E5%8B%9F%E8%B3%87%E4%B8%8A%E7%9C%8B140%E5%84%84%E5%85%83-%E8%82%A1%E5%83%B9%E5%AF%AB6%E5%80%8B%E6%9C%88%E6%96%B0%E4%BD%8E-102802029.html
- 事件6：iPhone Duo首賣撞颱風 蘋果祭彈性取貨果粉免冒風雨
  - 來源：Yahoo 台股；發布時間：2026-10-22T11:06:00Z；台北時間：2026-10-22 19:06
  - 摘要：Apple推出的首款摺疊機iPhone Duo，打開後擁有iPhone史上最大7.6吋內螢幕，可觀看內容、玩遊戲和進行多工處理；闔起後5.4吋外螢幕保持輕巧、便攜，輕鬆放入口袋。iPhone Duo搭載搭載A20 Pro晶片，採用台積電最先
  - 原文連結：https://tw.stock.yahoo.com/news/%E6%9E%9C%E7%B2%89%E5%BF%AB%E7%9C%8B-iphone-duo%E9%A6%96%E8%B3%A3%E5%BC%B7%E7%A2%B0%E8%96%94%E7%90%B5%E9%A2%B1%E9%A2%A8-%E8%98%8B%E6%9E%9C%E7%A5%AD%E5%BD%88%E6%80%A7%E5%8F%96%E8%B2%A8-100000932.html
- 事件7：Federal Reserve Board announces termination of enforcement actions with Gardner Bancshares, Inc. and Small Business Bank
  - 來源：Federal Reserve；發布時間：Fri, 16 Oct 2026 15:00:00 GMT；台北時間：2026-10-16 23:00
  - 摘要：Federal Reserve Board announces termination of enforcement actions with Gardner Bancshares, Inc. and Small Business Bank
  - 原文連結：https://www.federalreserve.gov/newsevents/pressreleases/enforcement20261016a.htm
- 事件8：CoreWeave’s market confidence erodes as bond yields spike and stock sinks
  - 來源：CNBC；發布時間：Thu, 22 Oct 2026 15:35:55 GMT；台北時間：2026-10-22 23:35
  - 摘要：CoreWeave shares are down 35% in October, and the spreads in its credit default swaps are widening.
  - 原文連結：https://www.cnbc.com/2026/10/21/coreweaves-market-confidence-erodes-as-bond-yields-spike-stock-sinks.html
- 事件9：Trump’s tariffs loom over Maine Senate race between Collins and Jackson
  - 來源：CNBC；發布時間：Thu, 22 Oct 2026 13:53:23 GMT；台北時間：2026-10-22 21:53
  - 摘要：The Maine Senate race between Republican incumbent Susan Collins and Democrat Troy Jackson presents a laboratory for public sentiment on Trump's Canad
  - 原文連結：https://www.cnbc.com/2026/10/22/maine-senate-election-trump-tariffs.html
- 事件10：Under-the-radar stocks to play the next leg of the energy trade with oil prices jumping again
  - 來源：CNBC；發布時間：Thu, 22 Oct 2026 15:16:05 GMT；台北時間：2026-10-22 23:16
  - 摘要：Iran is going to grow more desperate as oil money dries up, which makes the country even more dangerous.
  - 原文連結：https://www.cnbc.com/2026/10/22/under-the-radar-stocks-to-play-the-next-leg-of-the-energy-trade-with-oil-prices-jumping-again.html
- 事件11：Two big reasons Micron and other chip stocks are falling on Thursday
  - 來源：MarketWatch；發布時間：Thu, 22 Oct 2026 15:33:00 GMT；台北時間：2026-10-22 23:33
  - 摘要：Investors are spooked by Tesla&#x2019;s cut to its near-term spending target and Lam Research&#x2019;s weaker-than-expected forecast,
  - 原文連結：https://www.marketwatch.com/story/two-big-reasons-micron-and-other-chip-stocks-are-falling-on-thursday-312f1fb2?mod=mw_rss_topstories
- 事件12：Oil is now flowing out of the Persian Gulf like before the Iran war. Why prices may still not come down anytime soon.
  - 來源：MarketWatch；發布時間：Thu, 22 Oct 2026 12:35:00 GMT；台北時間：2026-10-22 20:35
  - 摘要：Oil flows out of the Persian Gulf in October nearly returned to levels seen before the start of the Iran war, but traders remain wary about a fragile 
  - 原文連結：https://www.marketwatch.com/story/oil-is-now-flowing-out-of-the-persian-gulf-like-before-the-iran-war-why-prices-may-still-not-come-down-anytime-soon-56df2f48?mod=mw_rss_topstories


## 三、期貨

**資料來源：**
1. Cloudflare Workers：TAIFEX Proxy — https://taifex.grichtoyang.workers.dev/
2. TAIFEX Open API — https://openapi.taifex.com.tw/

近月契約月份：202611 (日盤成交量最大者)；交易日期：2026-10-22

### 1．台指期近月日盤行情

| 項目 | 數值 | 資料來源 |
|---|---|---|
| 開盤價 | 47,164 | TAIFEX Proxy |
| 最高價 | 47,337 | TAIFEX Proxy |
| 最低價 | 46,217 | TAIFEX Proxy |
| 收盤價 | 46,272 | TAIFEX Proxy |
| 漲跌點數 | -741 | TAIFEX Proxy |
| 漲跌幅 | -1.58 | TAIFEX Proxy |
| 成交量 | 55,226 | TAIFEX Proxy |
| 日盤高點及低點 | 47,337 / 46,217 | TAIFEX Proxy |

### 2．台指期近月夜盤行情

| 項目 | 數值 | 資料來源 |
|---|---|---|
| 開盤價 | 46,991 | TAIFEX Proxy |
| 最高價 | 47,555 | TAIFEX Proxy |
| 最低價 | 46,983 | TAIFEX Proxy |
| 收盤價 | 47,482 | TAIFEX Proxy |
| 漲跌點數 | +469 | TAIFEX Proxy |
| 漲跌幅 | +1.00 | TAIFEX Proxy |
| 成交量 | 35,753 | TAIFEX Proxy |
| 夜盤高點及低點 | 47,555 / 46,983 | TAIFEX Proxy |
| 結算價 | 46,234 | TAIFEX Proxy |
| 未平倉量 | 115,258 | TAIFEX Proxy |

### 3．法人台指期多空未平倉部位

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 外資多方 OI | 8,126 | TAIFEX Proxy |
| 外資空方 OI | 95,423 | TAIFEX Proxy |
| 外資多空淨 OI | -87,297 | TAIFEX Proxy |
| 投信多方 OI | 86,375 | TAIFEX Proxy |
| 投信空方 OI | 2,774 | TAIFEX Proxy |
| 投信多空淨 OI | +83,601 | TAIFEX Proxy |
| 自營商多方 OI | 6,399 | TAIFEX Proxy |
| 自營商空方 OI | 3,139 | TAIFEX Proxy |
| 自營商多空淨 OI | +3,260 | TAIFEX Proxy |
| 三大法人合計多方 OI | 100,900 | TAIFEX Proxy |
| 三大法人合計空方 OI | 101,336 | TAIFEX Proxy |
| 三大法人合計多空淨 OI | -436 | TAIFEX Proxy |
| 外資多空淨 OI 變化 | -1,225 | TAIFEX Proxy |
| 投信多空淨 OI 變化 | -177 | TAIFEX Proxy |
| 自營商多空淨 OI 變化 | +1,544 | TAIFEX Proxy |

### 4．前十大交易人多空未平倉部位

**資料來源：** `TAIFEX OpenAPI OpenInterestOfLargeTradersFutures` (官方資料落後約一日，標示實際日期)

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 前十大交易人多方 OI | 90,479 | TAIFEX Proxy |
| 前十大交易人空方 OI | 82,789 | TAIFEX Proxy |
| 前十大交易人多空淨 OI | +7,690 | TAIFEX Proxy |
| 多空淨 OI 變化 (2026-10-20→2026-10-21) | +2,787 | TAIFEX Proxy snapshots (2026-10-21) |
- 資料日期：2026-10-21 (TypeOfTraders=0 全部交易人；契約月份 202611)

### 5．日盤、夜盤法人交易資料

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 外資日盤多單交易量 | 50,162 | TAIFEX Proxy |
| 外資日盤空單交易量 | 51,383 | TAIFEX Proxy |
| 外資日盤多空淨交易量 | -1,221 | TAIFEX Proxy |
| 外資夜盤多單交易量 | 18,496 | TAIFEX Proxy |
| 外資夜盤空單交易量 | 19,414 | TAIFEX Proxy |
| 外資夜盤多空淨交易量 | -918 | TAIFEX Proxy |
| 外資日盤／夜盤交易量變化 | -303 | TAIFEX Proxy |
| 投信日盤多空淨交易量 | -177 | TAIFEX Proxy |
| 投信夜盤多空淨交易量 | +0 | TAIFEX Proxy |
| 投信日盤／夜盤交易量變化 | -177 | TAIFEX Proxy |
| 自營商日盤多空淨交易量 | +1,565 | TAIFEX Proxy |
| 自營商夜盤多空淨交易量 | +536 | TAIFEX Proxy |
| 自營商日盤／夜盤交易量變化 | +1,029 | TAIFEX Proxy |
| 三大法人日盤多空淨交易量 | +167 | TAIFEX Proxy |
| 三大法人夜盤多空淨交易量 | -382 | TAIFEX Proxy |
| 法人日盤交易金額淨額 (億元) | +14.1 | TAIFEX Proxy |
| 法人夜盤交易金額淨額 (億元) | -36.1 | TAIFEX Proxy |

### 6．期貨與現貨關係

| 項目 | 數值 | 資料來源 |
|---|---|---|
| 台指期近月價格 | 46,272 | TAIFEX Proxy |
| 加權指數價格 | 46,041.43 | twse-proxy |
| 台指期與加權指數價差 | +230.57 | TAIFEX Proxy+twse-proxy |
| 價差百分比 | +0.50 | TAIFEX Proxy+twse-proxy |
| 日盤基差 | +230.57 | TAIFEX Proxy+twse-proxy |
| 夜盤價格相對日盤收盤的變化 | +1,210 | TAIFEX Proxy |

### 7．日盤、夜盤與籌碼變化對照

#### 7.1 日夜盤價格與成交量對照 (變化 = 日盤 - 夜盤)

| 項目 | 日盤 | 夜盤 | 變化 (日-夜) | 資料來源 |
|---|---|---|---|---|
| 收盤價 | 46,272 | 47,482 | -1,210 | TAIFEX Proxy |
| 成交量 | 55,226 | 35,753 | +19,473 | TAIFEX Proxy |
- 台指期總 OI 前日變化：+142（來源：TAIFEX Proxy）


#### 7.2 法人籌碼日夜盤對照 (淨變化 = 日盤淨 - 夜盤淨；OI 為日盤收盤後總量，前日變化另列)

| 法人 | 交易量 |  |  |  |  |  |  | 未平倉量 |  |  |  | 資料來源 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|  | **日盤多單** | **日盤空單** | **日盤淨** | **夜盤多單** | **夜盤空單** | **夜盤淨** | **淨變化 (日-夜)** | **OI多方** | **OI空方** | **OI淨** | **OI前日變化** |  |
| 外資 | 50,162 | 51,383 | -1,221 | 18,496 | 19,414 | -918 | -303 | 8,126 | 95,423 | -87,297 | -1,225 | TAIFEX Proxy |
| 投信 | 568 | 745 | -177 | 0 | 0 | +0 | -177 | 86,375 | 2,774 | +83,601 | -177 | TAIFEX Proxy |
| 自營商 | 5,489 | 3,924 | +1,565 | 1,231 | 695 | +536 | +1,029 | 6,399 | 3,139 | +3,260 | +1,544 | TAIFEX Proxy |
| 三大法人合計 | 56,219 | 56,052 | +167 | 19,727 | 20,109 | -382 | +549 | 100,900 | 101,336 | -436 | +142 | TAIFEX Proxy |

#### 7.3 前十大交易人日夜盤對照 (OI 無日夜拆分，列收盤後總量)

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 前十大交易人多方 OI | 90,479 | TAIFEX Proxy |
| 前十大交易人空方 OI | 82,789 | TAIFEX Proxy |
| 前十大交易人多空淨 OI | +7,690 | TAIFEX Proxy |
| 前十大交易人多空淨 OI 變化 (2026-10-20→2026-10-21) | +2,787 | TAIFEX Proxy snapshots (2026-10-21) |

#### 7.4 夜盤劇本分類 (規則對應：夜盤漲跌 × 外資夜盤偏多空)

| 項目 | 數值 | 資料來源 |
|---|---|---|
| 夜盤成交量占比 (夜盤量／(夜盤量＋日盤量)) | 39.30% | TAIFEX Proxy |
| 夜盤漲跌點數 | +469 | TAIFEX Proxy |
| 外資夜盤多空淨交易量 | -918 | TAIFEX Proxy |
| 劇本分類 | 劇本二 | 規則對應 |
| 劇本條件 | 夜盤上漲＋外資偏空 | 規則對應 |
| 劇本特徵 | 先漲、小心開高走低 | 規則對應 |

## 四、選擇權

**資料來源：** 主要 TAIFEX 經 Cloudflare Worker Proxy；時區 `Asia/Taipei`

### 1．選擇權交易日期、到期日與資料時間

| 項目 | 數值 | 資料來源 |
|---|---|---|
| 交易日期 | 2026-10-22 | TAIFEX Proxy |
| 到期月份／到期日 | 202610F4 | TAIFEX Proxy |
| 資料更新時間 | 2026-10-22 23:46:34 | 本機 |
| 日盤／夜盤標記 | 日盤收盤後資料 | TAIFEX Proxy |

### 2．Call 總成交量、OI、OI 增減

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Call 總成交量 | 178,535 | TAIFEX Proxy |
| Call 總未平倉量 OI | 55,024 | TAIFEX Proxy |
| Call OI 增減 | unavailable | 端點未提供 |

### 3．Put 總成交量、OI、OI 增減

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Put 總成交量 | 155,316 | TAIFEX Proxy |
| Put 總未平倉量 OI | 31,411 | TAIFEX Proxy |
| Put OI 增減 | unavailable | 端點未提供 |

### 4．Call／Put 比例與變化

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Call／Put 成交量比例 | 1.15 | TAIFEX Proxy |
| Call／Put 未平倉量比例 | 1.75 | TAIFEX Proxy |
| Put／Call Ratio | 0.57 | TAIFEX Proxy |
| Call／Put 比例變化 (量比 2026-10-20→2026-10-21) | -17.18 | TAIFEX Proxy |
| 與前一交易日比較 (OI 比 2026-10-20→2026-10-21) | -3.31 | TAIFEX Proxy |
**資料來源：** 比例 `TAIFEX Proxy chain`；變化 `TAIFEX Proxy PutCallRatio`

### 5．外資 Call／Put 部位

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 外資 Call日買 | 45,172 | TAIFEX Proxy |
| 外資 Call日賣 | 45,054 | TAIFEX Proxy |
| 外資 Call日淨 | +118 | TAIFEX Proxy |
| 外資 Put日買 | 52,064 | TAIFEX Proxy |
| 外資 Put日賣 | 52,245 | TAIFEX Proxy |
| 外資 Put日淨 | -181 | TAIFEX Proxy |
| 外資 Call夜買 | 18,352 | TAIFEX Proxy |
| 外資 Call夜賣 | 18,236 | TAIFEX Proxy |
| 外資 Call夜淨 | +116 | TAIFEX Proxy |
| 外資 Put夜買 | 20,801 | TAIFEX Proxy |
| 外資 Put夜賣 | 21,125 | TAIFEX Proxy |
| 外資 Put夜淨 | -324 | TAIFEX Proxy |
| 外資 日盤淨總量 | +299 | TAIFEX Proxy |
| 外資 Call日夜淨增減 (日－夜) | +2 | TAIFEX Proxy |
| 外資 Put日夜淨增減 (日－夜) | +143 | TAIFEX Proxy |

### 6．自營商 Call／Put 部位

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 自營商 Call日買 | 65,292 | TAIFEX Proxy |
| 自營商 Call日賣 | 64,470 | TAIFEX Proxy |
| 自營商 Call日淨 | +822 | TAIFEX Proxy |
| 自營商 Put日買 | 52,508 | TAIFEX Proxy |
| 自營商 Put日賣 | 54,441 | TAIFEX Proxy |
| 自營商 Put日淨 | -1,933 | TAIFEX Proxy |
| 自營商 Call夜買 | 15,497 | TAIFEX Proxy |
| 自營商 Call夜賣 | 16,186 | TAIFEX Proxy |
| 自營商 Call夜淨 | -689 | TAIFEX Proxy |
| 自營商 Put夜買 | 18,128 | TAIFEX Proxy |
| 自營商 Put夜賣 | 14,336 | TAIFEX Proxy |
| 自營商 Put夜淨 | +3,792 | TAIFEX Proxy |
| 自營商 日盤淨總量 | +2,755 | TAIFEX Proxy |
| 自營商 Call日夜淨增減 (日－夜) | +1,511 | TAIFEX Proxy |
| 自營商 Put日夜淨增減 (日－夜) | -5,725 | TAIFEX Proxy |

### 7．主要 Call OI 集中區

| 項目 | 履約價 | OI | 資料來源 |
|---|---|---|---|
| Call OI 第1大履約價 | 49,000 | 2,444 | TAIFEX Proxy |
| Call OI 第2大履約價 | 47,000 | 2,275 | TAIFEX Proxy |
| Call OI 第3大履約價 | 51,000 | 1,993 | TAIFEX Proxy |
| Call OI 最大履約價 | 49,000 | 2,444 | TAIFEX Proxy |

#### Call OI 分布明細 Top10 (機器可讀，到期月份 202610F4)

| # | 履約價 | OI | 佔比 | 資料來源 |
|---|---|---|---|---|
| C1 | 49,000 | 2,444 | 4.44% | TAIFEX Proxy |
| C2 | 47,000 | 2,275 | 4.13% | TAIFEX Proxy |
| C3 | 51,000 | 1,993 | 3.62% | TAIFEX Proxy |
| C4 | 48,000 | 1,851 | 3.36% | TAIFEX Proxy |
| C5 | 47,500 | 1,600 | 2.91% | TAIFEX Proxy |
| C6 | 48,350 | 1,591 | 2.89% | TAIFEX Proxy |
| C7 | 47,600 | 1,555 | 2.83% | TAIFEX Proxy |
| C8 | 48,500 | 1,424 | 2.59% | TAIFEX Proxy |
| C9 | 45,100 | 1,401 | 2.55% | TAIFEX Proxy |
| C10 | 47,200 | 1,139 | 2.07% | TAIFEX Proxy |


### 8．主要 Put OI 集中區

| 項目 | 履約價 | OI | 資料來源 |
|---|---|---|---|
| Put OI 第1大履約價 | 46,000 | 1,829 | TAIFEX Proxy |
| Put OI 第2大履約價 | 46,500 | 1,537 | TAIFEX Proxy |
| Put OI 第3大履約價 | 45,500 | 1,531 | TAIFEX Proxy |
| Put OI 最大履約價 | 46,000 | 1,829 | TAIFEX Proxy |

#### Put OI 分布明細 Top10 (機器可讀，到期月份 202610F4)

| # | 履約價 | OI | 佔比 | 資料來源 |
|---|---|---|---|---|
| P1 | 46,000 | 1,829 | 5.82% | TAIFEX Proxy |
| P2 | 46,500 | 1,537 | 4.89% | TAIFEX Proxy |
| P3 | 45,500 | 1,531 | 4.87% | TAIFEX Proxy |
| P4 | 45,000 | 1,478 | 4.71% | TAIFEX Proxy |
| P5 | 44,000 | 1,106 | 3.52% | TAIFEX Proxy |
| P6 | 45,800 | 956 | 3.04% | TAIFEX Proxy |
| P7 | 45,900 | 854 | 2.72% | TAIFEX Proxy |
| P8 | 46,450 | 819 | 2.61% | TAIFEX Proxy |
| P9 | 45,400 | 768 | 2.45% | TAIFEX Proxy |
| P10 | 47,000 | 756 | 2.41% | TAIFEX Proxy |


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
| Call Wall 價位 | 49,000 | TAIFEX Proxy |
| 對應到期月份 | 202610F4 | TAIFEX Proxy |
| 與前一交易日的變化 | unavailable | 端點未提供 |

### 12．Put Wall

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Put Wall 價位 | 46,000 | TAIFEX Proxy |
| 對應到期月份 | 202610F4 | TAIFEX Proxy |
| 與前一交易日的變化 | unavailable | 端點未提供 |

### 13．Gamma Wall

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Gamma Wall 價位 | 47,000.00 | TAIFEX Proxy (options-market-structure-compact (proxy)) |
| 對應到期月份 | 202610F4 | TAIFEX Proxy |
| 資料日期 | 2026-10-21 | TAIFEX Proxy (options-market-structure-compact (proxy)) |

### 14．Gamma Flip

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Gamma Flip 價位 | 46,174.50 | TAIFEX Proxy (options-market-structure-compact (proxy)) |
| 對應到期月份 | 202610F4 | TAIFEX Proxy |
| 資料日期 | 2026-10-21 | TAIFEX Proxy (options-market-structure-compact (proxy)) |

### 15．Max Pain

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Max Pain 價位 | 46,000 | TAIFEX Proxy |
| 對應到期月份 | 202610F4 | TAIFEX Proxy |
| 與前一交易日的變化 | unavailable | 端點未提供 |

### 17．選擇權法人日盤、夜盤交易

| 法人 | 日盤多單 | 日盤空單 | 日盤淨 | 夜盤多單 | 夜盤空單 | 夜盤淨 | 淨變化 (日-夜) | 資料來源 |
|---|---|---|---|---|---|---|---|---|
| 外資 | 97,417 | 97,118 | +299 | 39,477 | 39,037 | +440 | -141 | TAIFEX Proxy |
| 投信 | 0 | 2,000 | -2,000 | 0 | 0 | +0 | -2,000 | TAIFEX Proxy |
| 自營商 | 119,733 | 116,978 | +2,755 | 29,833 | 34,314 | -4,481 | +7,236 | TAIFEX Proxy |
| 三大法人合計 | 217,150 | 216,096 | +1,054 | 69,310 | 73,351 | -4,041 | +5,095 | TAIFEX Proxy |
- 方法論：多方＝買Call＋賣Put（看多），空方＝賣Call＋買Put（看空），淨額＝看多－看空（已用 Call／Put 拆分頁交叉驗算一致）
- 公式：多方(買)－空方(賣)＝（買call＋賣put）－（賣call＋買put）＝看多－看空
- 速記：多＝BC＋SP、空＝SC＋BP

#### 法人多空力道表（金額・億元；上游千元／1e5）

| 法人 | 日多方力道 | 日空方力道 | 日淨多空力道 | 夜多方力道 | 夜空方力道 | 夜淨多空力道 | 日淨－夜淨 | 資料來源 |
|---|---|---|---|---|---|---|---|---|
| 外資 | 11.44 | 11.58 | -0.14 | 4.38 | 4.35 | +0.03 | -0.17 | TAIFEX Proxy |
| 投信 | 0.00 | 1.10 | -1.10 | 0.00 | 0.00 | +0 | -1.10 | TAIFEX Proxy |
| 自營商 | 12.75 | 14.01 | -1.26 | 3.19 | 5.02 | -1.83 | +0.57 | TAIFEX Proxy |
| 三大法人合計 | 24.18 | 26.69 | -2.51 | 7.56 | 9.37 | -1.80 | -0.70 | TAIFEX Proxy |

### 18．選擇權前十大

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 買權多方 OI | 5,000 | TAIFEX Proxy |
| 買權空方 OI | 6,459 | TAIFEX Proxy |
| 買權多空淨 OI | -1,459 | TAIFEX Proxy |
| 買權多空淨 OI 變化 (2026-10-20→2026-10-21) | +17,189 | TAIFEX Proxy snapshots (2026-10-21) |

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 賣權多方 OI | 7,216 | TAIFEX Proxy |
| 賣權空方 OI | 8,501 | TAIFEX Proxy |
| 賣權多空淨 OI | -1,285 | TAIFEX Proxy |
| 賣權多空淨 OI 變化 (2026-10-20→2026-10-21) | -8,081 | TAIFEX Proxy snapshots (2026-10-21) |
- 資料日期：買權 2026-10-21／賣權 2026-10-21 (TypeOfTraders=0 全部交易人；契約月份 202611)

#### 大戶流向（全日；前十大無日夜拆分）

| 項目 | 淨變化 | 區間 | 資料來源 |
|---|---|---|---|
| 期貨前十大 | +2,787 | 2026-10-20→2026-10-21 | TAIFEX Proxy snapshots (2026-10-21) |
| 買權前十大 | +17,189 | 2026-10-20→2026-10-21 | TAIFEX Proxy snapshots (2026-10-21) |
| 賣權前十大 | -8,081 | 2026-10-20→2026-10-21 | TAIFEX Proxy snapshots (2026-10-21) |

### 16．資料來源、時間、時區與狀態

- 資料來源：TAIFEX 經 Cloudflare Worker Proxy
- 資料日期：2026-10-22；資料時間：2026-10-22 23:46:34；時區：`Asia/Taipei`
- 日盤／夜盤標記：日盤收盤後 + 夜盤盤後
- 未取得欄位 (2)：options.chain_oi_change, options.wall_change
- 註記：Gamma 資料日期 2026-10-21 (T0 2026-10-22 尚無，上游 FMTQIK 落後，採最新可得)
- 註記：法人交易量變化無昨日交易端點，標 unavailable
- 註記：Gamma Wall/Flip 資料日期 2026-10-21 (來源 options-market-structure-compact (proxy))
- 註記：跨到期換月（舊202610→新202610F4），日對日 OI/Walls 變化不適用

## 五、資料來源、時間與完整性

- 期貨/匯率為最新報價，其餘為 T0 收盤資料；時間皆為 `Asia/Taipei`。
- taiex：`twse-proxy`
- taiex_ohlc：`FinMind TaiwanStockPrice TAIEX`
- listed_turnover：`twse-proxy market_statistics`
- listed_breadth：`twse-proxy`
- otc：`TPEX OpenAPI tpex_mainborad_highlight`
- institutional：`twse-proxy /institutional`
- margin：`HiStock 上市+上櫃融資融券 (金額口徑)`
- margin_ratio：`stockintelli 大盤融資維持率 (民間估算；官方無每日序列)`
- sbl：`TWSE TWT93U + TPEX margin_sbl`
- 期貨選擇權：`TAIFEX Proxy`
- 新聞：台股 Yahoo／國際 Fed＋CNBC＋MarketWatch；台股 Yahoo（不足時財訊快報備援）/ 國際 Fed 公告＋CNBC＋MarketWatch RSS；Fed 無摘要；investing 港股為主已退役；cnyes CSR、wantgoo JS 算繪、中央社/台灣央行路徑待查，未採用
- 美股/亞股/期貨/匯率/ADR/商品：`Yahoo Finance Chart API`；美債：`Yahoo Finance (備援)`
- 註記：上市 MI_MARGN / TWT96U 無日期欄，採用最新可得
- 註記：借券賣出增減僅上櫃值 (TWSE TWT93U 未取得)
- 本報告僅整理資料，不提供交易判斷。

## 六、期現選方向對照

**規則：** 趨勢偏多／空＝現貨、期貨OI、選擇權日淨三者同向；避險／對沖＝現貨與期選反向；日內反轉＝日淨與夜淨反向；缺值標示，不推估。選擇權多空為看多看空口徑。

| 法人 | 現貨買賣超(億) | 期貨OI淨(口) | 期貨日淨 | 期貨夜淨 | 選擇權日淨 | 選擇權夜淨 | 判定 | 期選組合 | 資料來源 |
|---|---|---|---|---|---|---|---|---|---|
| 外資 | -815.8 | -87,297 | -1,221 | -918 | +299 | +440 | 避險／對沖 | 分歧 | twse-proxy／TAIFEX Proxy |
| 投信 | +94.9 | +83,601 | -177 | +0 | -2,000 | +0 | 避險／對沖 | 分歧 | twse-proxy／TAIFEX Proxy |
| 自營商 | -273.8 | +3,260 | +1,565 | +536 | +2,755 | -4,481 | 避險／對沖 | 趨勢偏多 | twse-proxy／TAIFEX Proxy |
