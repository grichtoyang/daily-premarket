# DATA_REPORT_20261104

- 報告日期：`2026-11-05`
- T0 交易日期：`2026-11-04`
- 資料產出時間：`2026-11-05 12:11:10`
- 時區：`Asia/Taipei`
- 產出盤別：`全日`
- 產出者：`actions`
- 排定班別：`morning`

---

## 一、現貨

### 1. 台股大盤行情

**資料來源：** `Cloudflare Worker：twse-proxy` (備援 `TWSE OpenAPI MI_INDEX`)

| 項目 | 數值 | 單位 | 資料來源 |
|---|---|---|---|
| 加權指數 | 42,948.91 | 點 | twse-proxy |
| 開盤 | 43,449.45 | 點 | FinMind TaiwanStockPrice TAIEX |
| 最高 | 43,741.54 | 點 | FinMind TaiwanStockPrice TAIEX |
| 最低 | 41,855.82 | 點 | FinMind TaiwanStockPrice TAIEX |
| 收盤 | 42,948.91 | 點 | twse-proxy |
| 漲跌點數 | -358.63 | 點 | twse-proxy |
| 漲跌幅 | -0.83 | % | twse-proxy |
| 成交金額 | 11,769.3 | 億元 | twse-proxy market_statistics |

### 2. 市場漲跌家數

#### 2.1 上市公司

**資料來源：** `Cloudflare Worker：twse-proxy` (備援 `TWSE OpenAPI twtazu_od`)

| 項目 | 家數 | 資料來源 |
|---|---|---|
| 上漲家數 | 438 | twse-proxy |
| 下跌家數 | 544 | twse-proxy |
| 平盤家數 | 99 | twse-proxy |
| 漲停家數 | 20 | twse-proxy |
| 跌停家數 | 2 | twse-proxy |

#### 2.2 上櫃公司

**資料來源：** `TPEX OpenAPI tpex_mainborad_highlight`

| 項目 | 家數 | 資料來源 |
|---|---|---|
| 上漲家數 | 397 | TPEX OpenAPI tpex_mainborad_highlight |
| 下跌家數 | 416 | TPEX OpenAPI tpex_mainborad_highlight |
| 平盤家數 | 68 | TPEX OpenAPI tpex_mainborad_highlight |
| 漲停家數 | 29 | TPEX OpenAPI tpex_mainborad_highlight |
| 跌停家數 | 2 | TPEX OpenAPI tpex_mainborad_highlight |

### 3. 三大法人現貨買賣超

**資料來源：** `TWSE RWD BFI82U`

| 法人別 | 買賣超金額 | 單位 | 資料來源 |
|---|---|---|---|
| 外資 | -1,499.0 | 億元 | twse-proxy /institutional |
| 投信 | +272.6 | 億元 | twse-proxy /institutional |
| 自營商 | -375.2 | 億元 | twse-proxy /institutional |
| 三大法人合計 | -1,601.6 | 億元 | twse-proxy /institutional |

### 4. 融資融券

**資料來源：** 上市+上櫃 `HiStock` (金額口徑)；維持率 `istock.tw`；備援官方逐股加總

| 項目 | 數值 | 單位 | 資料來源 |
|---|---|---|---|
| 融資餘額 | 7,878.7 | 億元 | HiStock 上市+上櫃融資融券 (金額口徑) |
| 融資增減 | -84.7 | 億元 | HiStock 上市+上櫃融資融券 (金額口徑) |
| 融券餘額 | 281,221 | 張 | HiStock 上市+上櫃融資融券 (金額口徑) |
| 融券增減 | -15,111 | 張 | HiStock 上市+上櫃融資融券 (金額口徑) |
| 融資維持率 | 162.70 | % | 前值遞補 (DATA 2026-11-03；當日三源皆失敗；民間估算；官方無每日序列) |

### 5. 借券資料

**資料來源：** 上市 `TWSE OpenAPI TWT96U` (可借餘額)、上櫃 `TPEX OpenAPI tpex_margin_sbl`

| 項目 | 數值 | 單位 | 資料來源 |
|---|---|---|---|
| 借券餘額 | 4,824,243 | 張 | TWSE TWT93U + TPEX margin_sbl |
| 借券賣出餘額 | 34,409 | 張 | TWSE TWT93U + TPEX margin_sbl |
| 借券賣出增減 | -3,962 | 張 | TWSE TWT93U + TPEX margin_sbl |

### 6. 市場成交結構

**資料來源：** 上市 `twse-proxy market_statistics`、上櫃 `TPEX OpenAPI tpex_mainborad_highlight`

| 項目 | 成交金額 | 單位 | 資料來源 |
|---|---|---|---|
| 上市成交金額 | 11,769.3 | 億元 | twse-proxy market_statistics |
| 上櫃成交金額 | 2,400.4 | 億元 | TPEX OpenAPI tpex_mainborad_highlight |
| 上市櫃成交金額合計 | 14,169.7 | 億元 | twse-proxy market_statistics+TPEX OpenAPI tpex_mainborad_highlight |

## 二、重要市場

### 1. 美股指數

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 收盤／最新值 | 漲跌點 | 漲跌幅 | 資料來源 |
|---|---|---|---|---|---|
| S&P 500 | ^GSPC | 7,688.62 | 119.70 | +1.58 | Yahoo Finance Chart API |
| Nasdaq Composite | ^IXIC | 25,736.51 | 364.50 | +1.44 | Yahoo Finance Chart API |
| Nasdaq 100 | ^NDX | 28,437.17 | 256.91 | +0.91 | Yahoo Finance Chart API |
| Dow Jones | ^DJI | 53,356.10 | 1,569.38 | +3.03 | Yahoo Finance Chart API |
| 費城半導體 SOX | ^SOX | 10,268.65 | -331.75 | -3.13 | Yahoo Finance Chart API |
| VIX | ^VIX | 16.61 | -4.22 | -20.26 | Yahoo Finance Chart API |

### 2. 亞洲主要指數

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 收盤／最新值 | 漲跌點 | 漲跌幅 | 資料來源 |
|---|---|---|---|---|---|
| 日經225 | ^N225 | 61,592.90 | -595.73 | -0.96 | Yahoo Finance Chart API |
| 韓國KOSPI | ^KS11 | 5,444.79 | -239.01 | -4.21 | Yahoo Finance Chart API |
| 香港恆生 | ^HSI | 24,654.86 | 735.36 | +3.07 | Yahoo Finance Chart API |
| 上海綜合 | 000001.SS | 3,686.17 | 78.08 | +2.16 | Yahoo Finance Chart API |
| 深圳成分 | 399001.SZ | 11,498.77 | 163.08 | +1.44 | Yahoo Finance Chart API |

### 3. 美股指數期貨

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 最新值 | 漲跌點 | 漲跌幅 | 資料來源 |
|---|---|---|---|---|---|
| S&P500期貨 | ES=F | 7,703.75 | -16.75 | -0.22 | Yahoo Finance Chart API |
| Nasdaq100期貨 | NQ=F | 28,304.00 | -262.75 | -0.92 | Yahoo Finance Chart API |
| 道瓊期貨 | YM=F | 53,628.00 | 125.00 | +0.23 | Yahoo Finance Chart API |
| Russell2000期貨 | RTY=F | 2,869.30 | 3.40 | +0.12 | Yahoo Finance Chart API |

### 4. 美國國債殖利率

**資料來源：** `U.S. Treasury Fiscal Data API` (失敗時備援 Treasury yield.xml 與 `Yahoo Finance`)

| 項目 | API 資料欄位／識別 | 殖利率 | 日變化 | 資料來源 |
|---|---|---|---|---|
| 美國 2 年期殖利率 | 2 Yr | 4.58 | -0.03 | U.S. Treasury yield.xml (網頁備援) |
| 美國 10 年期殖利率 | 10 Yr | 4.89 | -0.06 | Yahoo Finance (備援) |
| 美國 30 年期殖利率 | 30 Yr | 5.28 | -0.04 | Yahoo Finance (備援) |

### 5. 主要匯率

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 最新值 | 漲跌點 | 漲跌幅 | 資料來源 |
|---|---|---|---|---|---|
| USD/TWD | TWD=X | 32.93 | 0.20 | +0.60 | Yahoo Finance Chart API |
| DXY美元指數 | DX-Y.NYB | 101.21 | -0.30 | -0.30 | Yahoo Finance Chart API |
| USD/JPY | JPY=X | 157.88 | -0.59 | -0.37 | Yahoo Finance Chart API |
| USD/KRW | KRW=X | 1,343.18 | 0.28 | +0.02 | Yahoo Finance Chart API |

### 6. 台灣相關ADR

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 收盤／最新值 | 漲跌點 | 漲跌幅 | 資料來源 |
|---|---|---|---|---|---|
| 台積電ADR | TSM | 395.75 | -9.05 | -2.24 | Yahoo Finance Chart API |
| 聯電ADR | UMC | 16.06 | -0.34 | -2.07 | Yahoo Finance Chart API |
| 日月光ADR | ASX | 37.51 | -1.54 | -3.94 | Yahoo Finance Chart API |

### 7. 原油黃金Bitcoin

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 收盤／最新值 | 漲跌點 | 漲跌幅 | 資料來源 |
|---|---|---|---|---|---|
| WTI原油期貨 | CL=F | 86.97 | -1.15 | -1.31 | Yahoo Finance Chart API |
| 黃金期貨 | GC=F | 4,145.70 | 72.70 | +1.78 | Yahoo Finance Chart API |
| Bitcoin | BTC-USD | 80,350.45 | 3,005.41 | +3.89 | Yahoo Finance Chart API |

### 8. 重大經濟數據、央行事件與重大市場新聞

**資料來源：** 台股 `tw.stock.yahoo.com` (含內文摘要)；國際 `Fed 公告 RSS`＋`CNBC`＋`MarketWatch` (標題、來源、時間與連結)

- 事件1：｜配息基金推薦｜
  - 來源：Yahoo 台股；發布時間：2026-11-03T03:03:12Z；台北時間：2026-11-03 11:03
  - 摘要：對於習慣領月薪的上班族來說，「每月配息」的基金特別有吸引力。不過，許多人在找「月配息基金推薦」或「2026 配息基金推薦名單」時，往往只注意配息率高低、以及能否每月穩定領息。
  - 原文連結：https://tw.stock.yahoo.com/news/%E6%9C%88%E9%85%8D%E6%81%AF%E5%9F%BA%E9%87%91%E6%98%AF%E4%BB%80%E9%BA%BC%EF%BC%9F%E9%85%8D%E6%81%AF%E5%9F%BA%E9%87%91%E6%8E%A8%E8%96%A6%E6%80%8E%E9%BA%BC%E6%8C%91%EF%BC%9F4%E5%A4%A7%E6%8C%91%E9%81%B8%E9%87%8D%E9%BB%9E%E4%B8%80%E6%AC%A1%E7%9C%8B-030312577.html
- 事件2：新台幣回測32.9元 今年來已貶逾1元
  - 來源：Yahoo 台股；發布時間：2026-11-05T03:26:11Z；台北時間：2026-11-05 11:26
  - 摘要：台北股匯市場今（5）日連袂走低，新台幣兌美元匯率持續承壓，盤中一度重挫1.44角至 32.965 元，刷新逾一年半以來新低。累計今年以來，新台幣已大貶超過1元。分析師指出，外資目前仍偏向賣超匯出，短線尚未出現轉向回補的明確跡象。
  - 原文連結：https://tw.stock.yahoo.com/news/%E8%82%A1%E5%8C%AF%E9%9B%99%E6%AE%BA%EF%BC%81%E6%96%B0%E5%8F%B0%E5%B9%A3%E8%B2%B6%E9%80%BE1%E8%A7%92%E8%B7%8C%E7%A0%B4329%E5%85%83%E4%BB%8A%E5%B9%B4%E5%B7%B2%E8%B2%B61%E5%85%83-%E5%88%86%E6%9E%90%E5%B8%AB%EF%BC%9A%E5%A4%96%E8%B3%87%E9%82%84%E4%B8%8D%E6%89%93%E7%AE%97%E6%94%B6%E6%89%8B-032652450.html
- 事件3：松下湖口廠爆炸衝擊CCL供應鏈 台廠有望迎轉單
  - 來源：Yahoo 台股；發布時間：2026-11-05T02:54:33Z；台北時間：2026-11-05 10:54
  - 摘要：[NOWNEWS今日新聞]新竹縣湖口鄉台灣松下多層材料公司，在昨（4）日凌晨1時58分左右發生爆炸火警，造成5名員工受傷、2名員工失聯。爆炸造成廠房部分結構坍塌，鋼骨、鐵皮及管線嚴重扭曲變形，搜救通道...
  - 原文連結：https://tw.stock.yahoo.com/news/%E6%9D%BE%E4%B8%8B%E6%B9%96%E5%8F%A3%E5%BB%A0%E7%88%86%E7%82%B8-ai%E4%BC%BA%E6%9C%8D%E5%99%A8ccl%E4%BE%9B%E6%87%89%E9%8F%88%E8%A1%9D%E6%93%8A-025433912.html
- 事件4：富采今起暫停買賣 減資後每股退還現金超過4.5元
  - 來源：Yahoo 台股；發布時間：2026-11-05T02:58:00Z；台北時間：2026-11-05 10:58
  - 摘要：富采（3714）自今日起正式暫停股票市場買賣，為調整資本結構並提升股東權益報酬率，全面推動現金減資案。本次減資金額約33.79億元，銷除超過3.37億股，減資後實收資本額降至40億元。每仟股約減少457.95股，每股可退還現金約4.58元。
  - 原文連結：https://tw.stock.yahoo.com/news/%E9%80%99%E6%AA%94%E9%9D%A2%E6%9D%BF%E8%82%A1%E6%9A%AB%E5%81%9C%E8%B2%B7%E8%B3%A3-%E6%AF%8F%E8%82%A1%E9%80%804-5%E5%85%83-025800535.html
- 事件5：國巨一度挫逾9%探向407元 分析師：別貿然殺低
  - 來源：Yahoo 台股；發布時間：2026-11-05T02:40:30Z；台北時間：2026-11-05 10:40
  - 摘要：被動元件大廠國巨（2327）今日在大盤下挫之下，幾乎跟著所有權值股同步下跌，股價來到近半年新低點，最低觸及407元，跌幅達到9.3%。運達投顧分析師陳石輝指出，如今市場擔心美國AI放緩，訂單外溢效應淡化，因此漲價概念股挫跌，不過回歸基本面，
  - 原文連結：https://tw.stock.yahoo.com/news/65%E8%90%AC%E8%82%A1%E6%9D%B1%E6%8F%AA%E5%BF%83%E5%9C%8B%E5%B7%A8%E6%8C%AB9%E8%A7%B8%E3%80%8C%E5%8D%8A%E5%B9%B4%E4%BD%8E%E9%BB%9E%E3%80%8D-%E5%88%86%E6%9E%90%E5%B8%AB%E5%8B%B8%EF%BC%9A%E5%88%A5%E8%B2%BF%E7%84%B6%E6%AE%BA%E4%BD%8E-024030698.html
- 事件6：金融股成避風港  玉山金領34檔類股抗跌
  - 來源：Yahoo 台股；發布時間：2026-11-05T02:16:40Z；台北時間：2026-11-05 10:16
  - 摘要：大盤、電子全倒，金融股今（5）日成資金避風港，上市櫃34檔都呈現紅盤演出，為今日八大類股中表現最整齊的類股。截至10點為止，玉山金（2884）一度漲4%最強是多頭司令，新產（2850）、聯邦銀（2838）、公勝保經（6028）漲逾2%最多，
  - 原文連結：https://tw.stock.yahoo.com/news/%E9%87%91%E8%9E%8D%E8%82%A1%E6%88%90%E9%81%BF%E9%A2%A8%E6%B8%AF-%E7%8E%89%E5%B1%B1%E9%87%91%E9%A0%9834%E6%AA%94%E7%B4%85%E8%8A%B1%E6%9C%B5%E6%9C%B5%E9%96%8B-021656789.html
- 事件7：Federal Reserve Board announces approval of application by The Bank of Nova Scotia
  - 來源：Federal Reserve；發布時間：Thu, 29 Oct 2026 20:30:00 GMT；台北時間：2026-10-30 04:30
  - 摘要：Federal Reserve Board announces approval of application by The Bank of Nova Scotia
  - 原文連結：https://www.federalreserve.gov/newsevents/pressreleases/orders20261029a.htm
- 事件8：White House panel delays hearing on Fed's Lisa Cook to Dec. 14
  - 來源：CNBC；發布時間：Thu, 05 Nov 2026 01:11:26 GMT；台北時間：2026-11-05 09:11
  - 摘要：President Donald Trump first tried to fire Lisa Cook in August 2025, but the Supreme Court in June blocked him from doing so, for now.
  - 原文連結：https://www.cnbc.com/2026/11/04/trump-federal-reserve-lisa-cook-hearing.html
- 事件9：What Wall Street billionaires are saying about Democrats' midterm sweep
  - 來源：CNBC；發布時間：Wed, 04 Nov 2026 23:17:56 GMT；台北時間：2026-11-05 07:17
  - 摘要：Billionaire political spending met criticism from ... billionaires in the wake of Tuesday's blue wave election.
  - 原文連結：https://www.cnbc.com/2026/11/04/billionaires-musk-branson-democrats-midterms-ai-wall-street.html
- 事件10：Jim Cramer warns investors may be reading too much into Wall Street's post-election rally
  - 來源：CNBC；發布時間：Wed, 04 Nov 2026 23:18:56 GMT；台北時間：2026-11-05 07:18
  - 摘要：Cramer warned that Wall Street may be getting ahead of itself following the midterm elections.
  - 原文連結：https://www.cnbc.com/2026/11/04/cramer-midterms-ai-stocks.html
- 事件11：Crude oil prices fall below $90 a barrel as Vance blames GOP election defeat on Iran war
  - 來源：CNBC；發布時間：Wed, 04 Nov 2026 20:14:52 GMT；台北時間：2026-11-05 04:14
  - 摘要：Crude oil prices tumbled Wednesday after Vice President JD Vance blamed the Republicans' steep midterm election losses on the Iran war.
  - 原文連結：https://www.cnbc.com/2026/11/04/oil-price-iran-war-us-election-strait-hormuz.html
- 事件12：This year's worst-performing S&P 500 stock is finally seeing some major relief
  - 來源：MarketWatch；發布時間：Thu, 05 Nov 2026 01:05:00 GMT；台北時間：2026-11-05 09:05
  - 摘要：AppLovin&#x2019;s stock is popping after &#x201c;clearly positive&#x201d; earnings results.
  - 原文連結：https://www.marketwatch.com/story/this-years-worst-performing-s-p-500-stock-is-finally-seeing-some-major-relief-fff3fa85?mod=mw_rss_topstories


## 三、期貨

**資料來源：**
1. Cloudflare Workers：TAIFEX Proxy — https://taifex.grichtoyang.workers.dev/
2. TAIFEX Open API — https://openapi.taifex.com.tw/

近月契約月份：202611 (日盤成交量最大者)；交易日期：2026-11-04

### 1．台指期近月日盤行情

| 項目 | 數值 | 資料來源 |
|---|---|---|
| 開盤價 | 43,450 | TAIFEX Proxy |
| 最高價 | 43,774 | TAIFEX Proxy |
| 最低價 | 42,050 | TAIFEX Proxy |
| 收盤價 | 43,204 | TAIFEX Proxy |
| 漲跌點數 | -149 | TAIFEX Proxy |
| 漲跌幅 | -0.34 | TAIFEX Proxy |
| 成交量 | 113,674 | TAIFEX Proxy |
| 日盤高點及低點 | 43,774 / 42,050 | TAIFEX Proxy |

### 2．台指期近月夜盤行情

| 項目 | 數值 | 資料來源 |
|---|---|---|
| 開盤價 | 43,430 | TAIFEX Proxy |
| 最高價 | 44,274 | TAIFEX Proxy |
| 最低價 | 43,141 | TAIFEX Proxy |
| 收盤價 | 43,404 | TAIFEX Proxy |
| 漲跌點數 | +201 | TAIFEX Proxy |
| 漲跌幅 | +0.47 | TAIFEX Proxy |
| 成交量 | 66,939 | TAIFEX Proxy |
| 夜盤高點及低點 | 44,274 / 43,141 | TAIFEX Proxy |
| 結算價 | unavailable | TAIFEX Proxy |
| 未平倉量 | unavailable | TAIFEX Proxy |

### 3．法人台指期多空未平倉部位

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 外資多方 OI | 11,103 | TAIFEX Proxy |
| 外資空方 OI | 104,750 | TAIFEX Proxy |
| 外資多空淨 OI | -93,647 | TAIFEX Proxy |
| 投信多方 OI | 92,491 | TAIFEX Proxy |
| 投信空方 OI | 2,991 | TAIFEX Proxy |
| 投信多空淨 OI | +89,500 | TAIFEX Proxy |
| 自營商多方 OI | 6,858 | TAIFEX Proxy |
| 自營商空方 OI | 3,897 | TAIFEX Proxy |
| 自營商多空淨 OI | +2,961 | TAIFEX Proxy |
| 三大法人合計多方 OI | 110,452 | TAIFEX Proxy |
| 三大法人合計空方 OI | 111,638 | TAIFEX Proxy |
| 三大法人合計多空淨 OI | -1,186 | TAIFEX Proxy |
| 外資多空淨 OI 變化 | -1,835 | TAIFEX Proxy |
| 投信多空淨 OI 變化 | +2,502 | TAIFEX Proxy |
| 自營商多空淨 OI 變化 | -1,015 | TAIFEX Proxy |

### 4．前十大交易人多空未平倉部位

**資料來源：** `TAIFEX OpenAPI OpenInterestOfLargeTradersFutures` (官方資料落後約一日，標示實際日期)

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 前十大交易人多方 OI | 97,829 | TAIFEX Proxy |
| 前十大交易人空方 OI | 84,567 | TAIFEX Proxy |
| 前十大交易人多空淨 OI | +13,262 | TAIFEX Proxy |
| 多空淨 OI 變化 (2026-11-02→2026-11-04) | -977 | TAIFEX Proxy snapshots (2026-11-03) |
- 資料日期：2026-11-04 (TypeOfTraders=0 全部交易人；契約月份 202611)

### 5．日盤、夜盤法人交易資料

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 外資日盤多單交易量 | 93,663 | TAIFEX Proxy |
| 外資日盤空單交易量 | 95,523 | TAIFEX Proxy |
| 外資日盤多空淨交易量 | -1,860 | TAIFEX Proxy |
| 外資夜盤多單交易量 | 38,711 | TAIFEX Proxy |
| 外資夜盤空單交易量 | 39,180 | TAIFEX Proxy |
| 外資夜盤多空淨交易量 | -469 | TAIFEX Proxy |
| 外資日盤／夜盤交易量變化 | -1,391 | TAIFEX Proxy |
| 投信日盤多空淨交易量 | +2,502 | TAIFEX Proxy |
| 投信夜盤多空淨交易量 | +0 | TAIFEX Proxy |
| 投信日盤／夜盤交易量變化 | +2,502 | TAIFEX Proxy |
| 自營商日盤多空淨交易量 | -991 | TAIFEX Proxy |
| 自營商夜盤多空淨交易量 | -310 | TAIFEX Proxy |
| 自營商日盤／夜盤交易量變化 | -681 | TAIFEX Proxy |
| 三大法人日盤多空淨交易量 | -349 | TAIFEX Proxy |
| 三大法人夜盤多空淨交易量 | -779 | TAIFEX Proxy |
| 法人日盤交易金額淨額 (億元) | -26.1 | TAIFEX Proxy |
| 法人夜盤交易金額淨額 (億元) | -69.7 | TAIFEX Proxy |

### 6．期貨與現貨關係

| 項目 | 數值 | 資料來源 |
|---|---|---|
| 台指期近月價格 | 43,204 | TAIFEX Proxy |
| 加權指數價格 | 42,948.91 | twse-proxy |
| 台指期與加權指數價差 | +255.09 | TAIFEX Proxy+twse-proxy |
| 價差百分比 | +0.59 | TAIFEX Proxy+twse-proxy |
| 日盤基差 | +255.09 | TAIFEX Proxy+twse-proxy |
| 夜盤價格相對日盤收盤的變化 | +200 | TAIFEX Proxy |

### 7．日盤、夜盤與籌碼變化對照

#### 7.1 日夜盤價格與成交量對照 (變化 = 日盤 - 夜盤)

| 項目 | 日盤 | 夜盤 | 變化 (日-夜) | 資料來源 |
|---|---|---|---|---|
| 收盤價 | 43,204 | 43,404 | -200 | TAIFEX Proxy |
| 成交量 | 113,674 | 66,939 | +46,735 | TAIFEX Proxy |
- 台指期總 OI 前日變化：-348（來源：TAIFEX Proxy）


#### 7.2 法人籌碼日夜盤對照 (淨變化 = 日盤淨 - 夜盤淨；OI 為日盤收盤後總量，前日變化另列)

| 法人 | 交易量 |  |  |  |  |  |  | 未平倉量 |  |  |  | 資料來源 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|  | **日盤多單** | **日盤空單** | **日盤淨** | **夜盤多單** | **夜盤空單** | **夜盤淨** | **淨變化 (日-夜)** | **OI多方** | **OI空方** | **OI淨** | **OI前日變化** |  |
| 外資 | 93,663 | 95,523 | -1,860 | 38,711 | 39,180 | -469 | -1,391 | 11,103 | 104,750 | -93,647 | -1,835 | TAIFEX Proxy |
| 投信 | 2,514 | 12 | +2,502 | 0 | 0 | +0 | +2,502 | 92,491 | 2,991 | +89,500 | +2,502 | TAIFEX Proxy |
| 自營商 | 12,388 | 13,379 | -991 | 1,328 | 1,638 | -310 | -681 | 6,858 | 3,897 | +2,961 | -1,015 | TAIFEX Proxy |
| 三大法人合計 | 108,565 | 108,914 | -349 | 40,039 | 40,818 | -779 | +430 | 110,452 | 111,638 | -1,186 | -348 | TAIFEX Proxy |

#### 7.3 前十大交易人日夜盤對照 (OI 無日夜拆分，列收盤後總量)

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 前十大交易人多方 OI | 97,829 | TAIFEX Proxy |
| 前十大交易人空方 OI | 84,567 | TAIFEX Proxy |
| 前十大交易人多空淨 OI | +13,262 | TAIFEX Proxy |
| 前十大交易人多空淨 OI 變化 (2026-11-02→2026-11-04) | -977 | TAIFEX Proxy snapshots (2026-11-03) |

#### 7.4 夜盤劇本分類 (規則對應：夜盤漲跌 × 外資夜盤偏多空)

| 項目 | 數值 | 資料來源 |
|---|---|---|
| 夜盤成交量占比 (夜盤量／(夜盤量＋日盤量)) | 37.06% | TAIFEX Proxy |
| 夜盤漲跌點數 | +201 | TAIFEX Proxy |
| 外資夜盤多空淨交易量 | -469 | TAIFEX Proxy |
| 劇本分類 | 劇本二 | 規則對應 |
| 劇本條件 | 夜盤上漲＋外資偏空 | 規則對應 |
| 劇本特徵 | 先漲、小心開高走低 | 規則對應 |

## 四、選擇權

**資料來源：** 主要 TAIFEX 經 Cloudflare Worker Proxy；時區 `Asia/Taipei`

### 1．選擇權交易日期、到期日與資料時間

| 項目 | 數值 | 資料來源 |
|---|---|---|
| 交易日期 | 2026-11-04 | TAIFEX Proxy |
| 到期月份／到期日 | 202611W1 | TAIFEX Proxy |
| 資料更新時間 | 2026-11-05 12:11:10 | 本機 |
| 日盤／夜盤標記 | 日盤收盤後資料 | TAIFEX Proxy |

### 2．Call 總成交量、OI、OI 增減

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Call 總成交量 | 438,164 | TAIFEX Proxy |
| Call 總未平倉量 OI | 123,799 | TAIFEX Proxy |
| Call OI 增減 (2026-11-03→2026-11-04) | +27,305 | TAIFEX Proxy snapshots (2026-11-03) |

### 3．Put 總成交量、OI、OI 增減

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Put 總成交量 | 387,135 | TAIFEX Proxy |
| Put 總未平倉量 OI | 65,804 | TAIFEX Proxy |
| Put OI 增減 (2026-11-03→2026-11-04) | +25,669 | TAIFEX Proxy snapshots (2026-11-03) |

### 4．Call／Put 比例與變化

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Call／Put 成交量比例 | 1.13 | TAIFEX Proxy |
| Call／Put 未平倉量比例 | 1.88 | TAIFEX Proxy |
| Put／Call Ratio | 0.53 | TAIFEX Proxy |
| Call／Put 比例變化 (量比 2026-11-03→2026-11-04) | 5.01 | TAIFEX Proxy |
| 與前一交易日比較 (OI 比 2026-11-03→2026-11-04) | 1.60 | TAIFEX Proxy |
**資料來源：** 比例 `TAIFEX Proxy chain`；變化 `TAIFEX Proxy PutCallRatio`

### 5．外資 Call／Put 部位

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 外資 Call日買 | 146,103 | TAIFEX Proxy |
| 外資 Call日賣 | 147,099 | TAIFEX Proxy |
| 外資 Call日淨 | -996 | TAIFEX Proxy |
| 外資 Put日買 | 144,973 | TAIFEX Proxy |
| 外資 Put日賣 | 149,598 | TAIFEX Proxy |
| 外資 Put日淨 | -4,625 | TAIFEX Proxy |
| 外資 Call夜買 | 39,947 | TAIFEX Proxy |
| 外資 Call夜賣 | 40,962 | TAIFEX Proxy |
| 外資 Call夜淨 | -1,015 | TAIFEX Proxy |
| 外資 Put夜買 | 34,664 | TAIFEX Proxy |
| 外資 Put夜賣 | 34,763 | TAIFEX Proxy |
| 外資 Put夜淨 | -99 | TAIFEX Proxy |
| 外資 日盤淨總量 | +3,629 | TAIFEX Proxy |
| 外資 Call日夜淨增減 (日－夜) | +19 | TAIFEX Proxy |
| 外資 Put日夜淨增減 (日－夜) | -4,526 | TAIFEX Proxy |

### 6．自營商 Call／Put 部位

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 自營商 Call日買 | 113,663 | TAIFEX Proxy |
| 自營商 Call日賣 | 117,752 | TAIFEX Proxy |
| 自營商 Call日淨 | -4,089 | TAIFEX Proxy |
| 自營商 Put日買 | 96,474 | TAIFEX Proxy |
| 自營商 Put日賣 | 101,454 | TAIFEX Proxy |
| 自營商 Put日淨 | -4,980 | TAIFEX Proxy |
| 自營商 Call夜買 | 25,062 | TAIFEX Proxy |
| 自營商 Call夜賣 | 26,325 | TAIFEX Proxy |
| 自營商 Call夜淨 | -1,263 | TAIFEX Proxy |
| 自營商 Put夜買 | 19,833 | TAIFEX Proxy |
| 自營商 Put夜賣 | 20,869 | TAIFEX Proxy |
| 自營商 Put夜淨 | -1,036 | TAIFEX Proxy |
| 自營商 日盤淨總量 | +891 | TAIFEX Proxy |
| 自營商 Call日夜淨增減 (日－夜) | -2,826 | TAIFEX Proxy |
| 自營商 Put日夜淨增減 (日－夜) | -3,944 | TAIFEX Proxy |

### 7．主要 Call OI 集中區

| 項目 | 履約價 | OI | 資料來源 |
|---|---|---|---|
| Call OI 第1大履約價 | 46,000 | 5,405 | TAIFEX Proxy |
| Call OI 第2大履約價 | 43,000 | 5,041 | TAIFEX Proxy |
| Call OI 第3大履約價 | 48,000 | 4,681 | TAIFEX Proxy |
| Call OI 最大履約價 | 46,000 | 5,405 | TAIFEX Proxy |

#### Call OI 分布明細 Top10 (機器可讀，到期月份 202611W1)

| # | 履約價 | OI | 佔比 | 資料來源 |
|---|---|---|---|---|
| C1 | 46,000 | 5,405 | 4.37% | TAIFEX Proxy |
| C2 | 43,000 | 5,041 | 4.07% | TAIFEX Proxy |
| C3 | 48,000 | 4,681 | 3.78% | TAIFEX Proxy |
| C4 | 44,000 | 3,694 | 2.98% | TAIFEX Proxy |
| C5 | 44,500 | 3,580 | 2.89% | TAIFEX Proxy |
| C6 | 45,000 | 3,430 | 2.77% | TAIFEX Proxy |
| C7 | 49,400 | 3,028 | 2.45% | TAIFEX Proxy |
| C8 | 44,200 | 2,889 | 2.33% | TAIFEX Proxy |
| C9 | 43,500 | 2,867 | 2.32% | TAIFEX Proxy |
| C10 | 46,200 | 2,809 | 2.27% | TAIFEX Proxy |


### 8．主要 Put OI 集中區

| 項目 | 履約價 | OI | 資料來源 |
|---|---|---|---|
| Put OI 第1大履約價 | 42,000 | 3,334 | TAIFEX Proxy |
| Put OI 第2大履約價 | 41,000 | 3,186 | TAIFEX Proxy |
| Put OI 第3大履約價 | 43,000 | 2,909 | TAIFEX Proxy |
| Put OI 最大履約價 | 42,000 | 3,334 | TAIFEX Proxy |

#### Put OI 分布明細 Top10 (機器可讀，到期月份 202611W1)

| # | 履約價 | OI | 佔比 | 資料來源 |
|---|---|---|---|---|
| P1 | 42,000 | 3,334 | 5.07% | TAIFEX Proxy |
| P2 | 41,000 | 3,186 | 4.84% | TAIFEX Proxy |
| P3 | 43,000 | 2,909 | 4.42% | TAIFEX Proxy |
| P4 | 42,800 | 2,445 | 3.72% | TAIFEX Proxy |
| P5 | 42,500 | 2,223 | 3.38% | TAIFEX Proxy |
| P6 | 41,500 | 2,166 | 3.29% | TAIFEX Proxy |
| P7 | 42,300 | 2,066 | 3.14% | TAIFEX Proxy |
| P8 | 42,900 | 1,982 | 3.01% | TAIFEX Proxy |
| P9 | 40,600 | 1,859 | 2.83% | TAIFEX Proxy |
| P10 | 40,400 | 1,807 | 2.75% | TAIFEX Proxy |


### 9．Call OI 增減集中區

| 項目 | 履約價 (增減口數) | 資料來源 |
|---|---|---|
| Call OI 增加最多的履約價 | 43,000 (+3,982) | TAIFEX Proxy snapshots (2026-11-03) |
| Call OI 減少最多的履約價 | 49,400 (-1,350) | TAIFEX Proxy snapshots (2026-11-03) |

### 10．Put OI 增減集中區

| 項目 | 履約價 (增減口數) | 資料來源 |
|---|---|---|
| Put OI 增加最多的履約價 | 41,000 (+2,468) | TAIFEX Proxy snapshots (2026-11-03) |
| Put OI 減少最多的履約價 | 44,000 (-559) | TAIFEX Proxy snapshots (2026-11-03) |

### 11．Call Wall

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Call Wall 價位 | 46,000 | TAIFEX Proxy |
| 對應到期月份 | 202611W1 | TAIFEX Proxy |
| 與前一交易日的變化 (2026-11-03→2026-11-04) | +0 | TAIFEX Proxy snapshots (2026-11-03) |

### 12．Put Wall

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Put Wall 價位 | 42,000 | TAIFEX Proxy |
| 對應到期月份 | 202611W1 | TAIFEX Proxy |
| 與前一交易日的變化 (2026-11-03→2026-11-04) | -1,000 | TAIFEX Proxy snapshots (2026-11-03) |

### 13．Gamma Wall

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Gamma Wall 價位 | 44,000.00 | TAIFEX Proxy (options-market-structure-compact (proxy)) |
| 對應到期月份 | 202611W1 | TAIFEX Proxy |
| 資料日期 | 2026-11-04 | TAIFEX Proxy (options-market-structure-compact (proxy)) |

### 14．Gamma Flip

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Gamma Flip 價位 | 39,901.34 | TAIFEX Proxy (options-market-structure-compact (proxy)) |
| 對應到期月份 | 202611W1 | TAIFEX Proxy |
| 資料日期 | 2026-11-04 | TAIFEX Proxy (options-market-structure-compact (proxy)) |

### 15．Max Pain

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Max Pain 價位 | 43,100 | TAIFEX Proxy |
| 對應到期月份 | 202611W1 | TAIFEX Proxy |
| 與前一交易日的變化 (2026-11-03→2026-11-04) | -900 | TAIFEX Proxy snapshots (2026-11-03) |

### 17．選擇權法人日盤、夜盤交易

| 法人 | 日盤多單 | 日盤空單 | 日盤淨 | 夜盤多單 | 夜盤空單 | 夜盤淨 | 淨變化 (日-夜) | 資料來源 |
|---|---|---|---|---|---|---|---|---|
| 外資 | 295,701 | 292,072 | +3,629 | 74,710 | 75,626 | -916 | +4,545 | TAIFEX Proxy |
| 投信 | 202 | 15,585 | -15,383 | 0 | 0 | +0 | -15,383 | TAIFEX Proxy |
| 自營商 | 215,117 | 214,226 | +891 | 45,931 | 46,158 | -227 | +1,118 | TAIFEX Proxy |
| 三大法人合計 | 511,020 | 521,883 | -10,863 | 120,641 | 121,784 | -1,143 | -9,720 | TAIFEX Proxy |
- 方法論：多方＝買Call＋賣Put（看多），空方＝賣Call＋買Put（看空），淨額＝看多－看空（已用 Call／Put 拆分頁交叉驗算一致）
- 公式：多方(買)－空方(賣)＝（買call＋賣put）－（賣call＋買put）＝看多－看空
- 速記：多＝BC＋SP、空＝SC＋BP

#### 法人多空力道表（金額・億元；上游千元／1e5）

| 法人 | 日多方力道 | 日空方力道 | 日淨多空力道 | 夜多方力道 | 夜空方力道 | 夜淨多空力道 | 日淨－夜淨 | 資料來源 |
|---|---|---|---|---|---|---|---|---|
| 外資 | 21.05 | 20.57 | +0.47 | 8.79 | 8.93 | -0.14 | +0.61 | TAIFEX Proxy |
| 投信 | 0.05 | 14.56 | -14.51 | 0.00 | 0.00 | +0 | -14.51 | TAIFEX Proxy |
| 自營商 | 33.99 | 21.10 | +12.89 | 7.45 | 6.28 | +1.18 | +11.72 | TAIFEX Proxy |
| 三大法人合計 | 55.09 | 56.23 | -1.14 | 16.25 | 15.21 | +1.04 | -2.18 | TAIFEX Proxy |

### 18．選擇權前十大

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 買權多方 OI | 11,926 | TAIFEX Proxy |
| 買權空方 OI | 16,052 | TAIFEX Proxy |
| 買權多空淨 OI | -4,126 | TAIFEX Proxy |
| 買權多空淨 OI 變化 (2026-11-02→2026-11-04) | -1,253 | TAIFEX Proxy snapshots (2026-11-03) |

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 賣權多方 OI | 8,715 | TAIFEX Proxy |
| 賣權空方 OI | 11,434 | TAIFEX Proxy |
| 賣權多空淨 OI | -2,719 | TAIFEX Proxy |
| 賣權多空淨 OI 變化 (2026-11-02→2026-11-04) | -679 | TAIFEX Proxy snapshots (2026-11-03) |
- 資料日期：買權 2026-11-04／賣權 2026-11-04 (TypeOfTraders=0 全部交易人；契約月份 202611)

#### 大戶流向（全日；前十大無日夜拆分）

| 項目 | 淨變化 | 區間 | 資料來源 |
|---|---|---|---|
| 期貨前十大 | -977 | 2026-11-02→2026-11-04 | TAIFEX Proxy snapshots (2026-11-03) |
| 買權前十大 | -1,253 | 2026-11-02→2026-11-04 | TAIFEX Proxy snapshots (2026-11-03) |
| 賣權前十大 | -679 | 2026-11-02→2026-11-04 | TAIFEX Proxy snapshots (2026-11-03) |

### 16．資料來源、時間、時區與狀態

- 資料來源：TAIFEX 經 Cloudflare Worker Proxy
- 資料日期：2026-11-04；資料時間：2026-11-05 12:11:10；時區：`Asia/Taipei`
- 日盤／夜盤標記：日盤收盤後 + 夜盤盤後
- 未取得欄位 (2)：futures.gamma_wall, futures.gamma_flip
- 註記：futures-price-after-hours 日期 2026-11-04 非今日 2026-11-05，視為無新節次，不採用
- 註記：Gamma Wall/Flip 端點不可用（上游 502），標 unavailable
- 註記：法人交易量變化無昨日交易端點，標 unavailable

## 五、資料來源、時間與完整性

- 期貨/匯率為最新報價，其餘為 T0 收盤資料；時間皆為 `Asia/Taipei`。
- taiex：`twse-proxy`
- taiex_ohlc：`FinMind TaiwanStockPrice TAIEX`
- listed_turnover：`twse-proxy market_statistics`
- listed_breadth：`twse-proxy`
- otc：`TPEX OpenAPI tpex_mainborad_highlight`
- institutional：`twse-proxy /institutional`
- margin：`HiStock 上市+上櫃融資融券 (金額口徑)`
- margin_ratio：`前值遞補 (DATA 2026-11-03；當日三源皆失敗；民間估算；官方無每日序列)`
- sbl：`TWSE TWT93U + TPEX margin_sbl`
- 期貨選擇權：`TAIFEX Proxy`
- 新聞：台股 Yahoo／國際 Fed＋CNBC＋MarketWatch；台股 Yahoo（不足時財訊快報備援）/ 國際 Fed 公告＋CNBC＋MarketWatch RSS；Fed 無摘要；investing 港股為主已退役；cnyes CSR、wantgoo JS 算繪、中央社/台灣央行路徑待查，未採用
- 美股/亞股/期貨/匯率/ADR/商品：`Yahoo Finance Chart API`；美債：`Yahoo Finance (備援)`
- 註記：融資維持率未取得 (三源皆失敗；官方無每日序列)
- 註記：融資維持率採前值遞補 (DATA 2026-11-03)，非 T0 2026-11-04
- 註記：上市 MI_MARGN / TWT96U 無日期欄，採用最新可得
- 註記：借券賣出增減僅上櫃值 (TWSE TWT93U 未取得)
- 本報告僅整理資料，不提供交易判斷。

## 六、期現選方向對照

**規則：** 趨勢偏多／空＝現貨、期貨OI、選擇權日淨三者同向；避險／對沖＝現貨與期選反向；日內反轉＝日淨與夜淨反向；缺值標示，不推估。選擇權多空為看多看空口徑。

| 法人 | 現貨買賣超(億) | 期貨OI淨(口) | 期貨日淨 | 期貨夜淨 | 選擇權日淨 | 選擇權夜淨 | 判定 | 期選組合 | 資料來源 |
|---|---|---|---|---|---|---|---|---|---|
| 外資 | -1,499.0 | -93,647 | -1,860 | -469 | +3,629 | -916 | 避險／對沖 | 趨勢偏空 | twse-proxy／TAIFEX Proxy |
| 投信 | +272.6 | +89,500 | +2,502 | +0 | -15,383 | +0 | 避險／對沖 | 分歧 | twse-proxy／TAIFEX Proxy |
| 自營商 | -375.2 | +2,961 | -991 | -310 | +891 | -227 | 避險／對沖 | 分歧 | twse-proxy／TAIFEX Proxy |
