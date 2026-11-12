# DATA_REPORT_20261111

- 報告日期：`2026-11-12`
- T0 交易日期：`2026-11-11`
- 資料產出時間：`2026-11-12 12:51:43`
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
| 加權指數 | 44,257.15 | 點 | twse-proxy |
| 開盤 | 43,135.76 | 點 | FinMind TaiwanStockPrice TAIEX |
| 最高 | 44,257.15 | 點 | FinMind TaiwanStockPrice TAIEX |
| 最低 | 42,708.05 | 點 | FinMind TaiwanStockPrice TAIEX |
| 收盤 | 44,257.15 | 點 | twse-proxy |
| 漲跌點數 | 1,545.23 | 點 | twse-proxy |
| 漲跌幅 | +3.62 | % | twse-proxy |
| 成交金額 | 8,763.0 | 億元 | twse-proxy market_statistics |

### 2. 市場漲跌家數

#### 2.1 上市公司

**資料來源：** `Cloudflare Worker：twse-proxy` (備援 `TWSE OpenAPI twtazu_od`)

| 項目 | 家數 | 資料來源 |
|---|---|---|
| 上漲家數 | 634 | twse-proxy |
| 下跌家數 | 368 | twse-proxy |
| 平盤家數 | 81 | twse-proxy |
| 漲停家數 | 34 | twse-proxy |
| 跌停家數 | 3 | twse-proxy |

#### 2.2 上櫃公司

**資料來源：** `TPEX OpenAPI tpex_mainborad_highlight`

| 項目 | 家數 | 資料來源 |
|---|---|---|
| 上漲家數 | 520 | TPEX OpenAPI tpex_mainborad_highlight |
| 下跌家數 | 289 | TPEX OpenAPI tpex_mainborad_highlight |
| 平盤家數 | 63 | TPEX OpenAPI tpex_mainborad_highlight |
| 漲停家數 | 53 | TPEX OpenAPI tpex_mainborad_highlight |
| 跌停家數 | 4 | TPEX OpenAPI tpex_mainborad_highlight |

### 3. 三大法人現貨買賣超

**資料來源：** `TWSE RWD BFI82U`

| 法人別 | 買賣超金額 | 單位 | 資料來源 |
|---|---|---|---|
| 外資 | -7.7 | 億元 | twse-proxy /institutional |
| 投信 | +185.9 | 億元 | twse-proxy /institutional |
| 自營商 | +62.6 | 億元 | twse-proxy /institutional |
| 三大法人合計 | +240.8 | 億元 | twse-proxy /institutional |

### 4. 融資融券

**資料來源：** 上市+上櫃 `HiStock` (金額口徑)；維持率 `istock.tw`；備援官方逐股加總

| 項目 | 數值 | 單位 | 資料來源 |
|---|---|---|---|
| 融資餘額 | 7,129.6 | 億元 | HiStock 上市+上櫃融資融券 (金額口徑) |
| 融資增減 | +69.7 | 億元 | HiStock 上市+上櫃融資融券 (金額口徑) |
| 融券餘額 | 246,001 | 張 | HiStock 上市+上櫃融資融券 (金額口徑) |
| 融券增減 | 2,113 | 張 | HiStock 上市+上櫃融資融券 (金額口徑) |
| 融資維持率 | 174.20 | % | stockintelli 大盤融資維持率 (民間估算；官方無每日序列) |

### 5. 借券資料

**資料來源：** 上市 `TWSE OpenAPI TWT96U` (可借餘額)、上櫃 `TPEX OpenAPI tpex_margin_sbl`

| 項目 | 數值 | 單位 | 資料來源 |
|---|---|---|---|
| 借券餘額 | 2,484,682 | 張 | TWSE TWT93U + TPEX margin_sbl |
| 借券賣出餘額 | 36,982 | 張 | TWSE TWT93U + TPEX margin_sbl |
| 借券賣出增減 | 4,225 | 張 | TWSE TWT93U + TPEX margin_sbl |

### 6. 市場成交結構

**資料來源：** 上市 `twse-proxy market_statistics`、上櫃 `TPEX OpenAPI tpex_mainborad_highlight`

| 項目 | 成交金額 | 單位 | 資料來源 |
|---|---|---|---|
| 上市成交金額 | 8,763.0 | 億元 | twse-proxy market_statistics |
| 上櫃成交金額 | 2,017.0 | 億元 | TPEX OpenAPI tpex_mainborad_highlight |
| 上市櫃成交金額合計 | 10,779.9 | 億元 | twse-proxy market_statistics+TPEX OpenAPI tpex_mainborad_highlight |

## 二、重要市場

### 1. 美股指數

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 收盤／最新值 | 漲跌點 | 漲跌幅 | 資料來源 |
|---|---|---|---|---|---|
| S&P 500 | ^GSPC | 7,619.38 | 98.45 | +1.31 | Yahoo Finance Chart API |
| Nasdaq Composite | ^IXIC | 25,466.19 | 400.32 | +1.60 | Yahoo Finance Chart API |
| Nasdaq 100 | ^NDX | 28,374.25 | 633.46 | +2.28 | Yahoo Finance Chart API |
| Dow Jones | ^DJI | 52,486.50 | 254.61 | +0.49 | Yahoo Finance Chart API |
| 費城半導體 SOX | ^SOX | 10,564.11 | 565.78 | +5.66 | Yahoo Finance Chart API |
| VIX | ^VIX | 17.49 | -1.97 | -10.12 | Yahoo Finance Chart API |

### 2. 亞洲主要指數

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 收盤／最新值 | 漲跌點 | 漲跌幅 | 資料來源 |
|---|---|---|---|---|---|
| 日經225 | ^N225 | 61,144.43 | -104.16 | -0.17 | Yahoo Finance Chart API |
| 韓國KOSPI | ^KS11 | 5,366.37 | -8.99 | -0.17 | Yahoo Finance Chart API |
| 香港恆生 | ^HSI | 24,092.89 | -223.03 | -0.92 | Yahoo Finance Chart API |
| 上海綜合 | 000001.SS | 3,688.05 | 7.41 | +0.20 | Yahoo Finance Chart API |
| 深圳成分 | 399001.SZ | 11,396.86 | 7.12 | +0.06 | Yahoo Finance Chart API |

### 3. 美股指數期貨

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 最新值 | 漲跌點 | 漲跌幅 | 資料來源 |
|---|---|---|---|---|---|
| S&P500期貨 | ES=F | 7,612.50 | -28.00 | -0.37 | Yahoo Finance Chart API |
| Nasdaq100期貨 | NQ=F | 28,214.75 | -258.50 | -0.91 | Yahoo Finance Chart API |
| 道瓊期貨 | YM=F | 52,643.00 | 65.00 | +0.12 | Yahoo Finance Chart API |
| Russell2000期貨 | RTY=F | 2,854.70 | 1.00 | +0.04 | Yahoo Finance Chart API |

### 4. 美國國債殖利率

**資料來源：** `U.S. Treasury Fiscal Data API` (失敗時備援 Treasury yield.xml 與 `Yahoo Finance`)

| 項目 | API 資料欄位／識別 | 殖利率 | 日變化 | 資料來源 |
|---|---|---|---|---|
| 美國 2 年期殖利率 | 2 Yr | 4.73 | 0.17 | U.S. Treasury yield.xml (網頁備援) |
| 美國 10 年期殖利率 | 10 Yr | 5.00 | 0.02 | Yahoo Finance (備援) |
| 美國 30 年期殖利率 | 30 Yr | 5.36 | 0.01 | Yahoo Finance (備援) |

### 5. 主要匯率

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 最新值 | 漲跌點 | 漲跌幅 | 資料來源 |
|---|---|---|---|---|---|
| USD/TWD | TWD=X | 32.97 | 0.02 | +0.06 | Yahoo Finance Chart API |
| DXY美元指數 | DX-Y.NYB | 102.99 | 0.08 | +0.07 | Yahoo Finance Chart API |
| USD/JPY | JPY=X | 159.68 | 0.98 | +0.61 | Yahoo Finance Chart API |
| USD/KRW | KRW=X | 1,331.08 | -10.83 | -0.81 | Yahoo Finance Chart API |

### 6. 台灣相關ADR

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 收盤／最新值 | 漲跌點 | 漲跌幅 | 資料來源 |
|---|---|---|---|---|---|
| 台積電ADR | TSM | 413.35 | 16.87 | +4.25 | Yahoo Finance Chart API |
| 聯電ADR | UMC | 16.08 | 1.04 | +6.91 | Yahoo Finance Chart API |
| 日月光ADR | ASX | 37.82 | 2.34 | +6.60 | Yahoo Finance Chart API |

### 7. 原油黃金Bitcoin

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 收盤／最新值 | 漲跌點 | 漲跌幅 | 資料來源 |
|---|---|---|---|---|---|
| WTI原油期貨 | CL=F | 85.32 | -1.21 | -1.40 | Yahoo Finance Chart API |
| 黃金期貨 | GC=F | 3,979.10 | -21.40 | -0.53 | Yahoo Finance Chart API |
| Bitcoin | BTC-USD | 73,735.79 | 15.67 | +0.02 | Yahoo Finance Chart API |

### 8. 重大經濟數據、央行事件與重大市場新聞

**資料來源：** 台股 `tw.stock.yahoo.com` (含內文摘要)；國際 `Fed 公告 RSS`＋`CNBC`＋`MarketWatch` (標題、來源、時間與連結)

- 事件1：員工領獎金得放棄爭議權？美光桃園工會爆協議疑雲
  - 來源：Yahoo 台股；發布時間：2026-11-12T04:32:01Z；台北時間：2026-11-12 12:32
  - 摘要：記憶體大廠美光（Micron）的台灣勞資爭議持續延燒！美光桃園工會最新發聲明坦言，這次為員工爭取「分潤制度」的行動宣告失敗，決定退出原訂 11 月 17 日的勞資協商，當天將直接前往民進黨中央黨部開記者會向外界發聲。工會更爆料，公司傳出打算
  - 原文連結：https://tw.stock.yahoo.com/news/%E7%8D%8E%E9%87%91%E8%A6%81%E7%94%A8%E7%B0%BD%E5%AD%97%E6%8F%9B%EF%BC%9F%E7%BE%8E%E5%85%89%E6%A1%83%E5%9C%92%E5%B7%A5%E6%9C%83%E5%8B%9E%E8%B3%87%E8%AB%87%E5%88%A4%E7%A0%B4%E5%B1%80-%E5%93%A1%E5%B7%A5%E7%88%86%E9%81%AD%E5%85%AC%E5%8F%B8%E6%96%BD%E5%A3%93-043201170.html
- 事件2：紡織股上演飆速秀 儒鴻登近8個月高如興逼近漲停
  - 來源：Yahoo 台股；發布時間：2026-11-12T04:13:27Z；台北時間：2026-11-12 12:13
  - 摘要：紡織族群今（12）日盤中多檔個股走揚，其中成衣大廠儒鴻（1476）盤中最高衝上372元，漲幅達5.53%，創近8個月新高；如興（4414）也一度逼近漲停，漲幅逾9%。儒鴻日前法說會釋出明年營運審慎樂觀的看法，新客戶營收占比提升，也成為近期市
  - 原文連結：https://tw.stock.yahoo.com/news/%E5%84%92%E9%B4%BB%E4%B8%80%E5%BA%A6%E6%BC%B2%E9%80%BE5%E5%89%B5%E8%BF%918%E5%80%8B%E6%9C%88%E6%96%B0%E9%AB%98%EF%BC%81%E5%A6%82%E8%88%88%E9%80%BC%E8%BF%91%E6%BC%B2%E5%81%9C-%E7%B4%A1%E7%B9%94%E8%82%A1%E8%B5%B0%E5%BC%B7-041327150.html
- 事件3：玻纖布綠一片台玻獨嗨 南亞德宏富喬齊陷賣壓
  - 來源：Yahoo 台股；發布時間：2026-11-12T04:40:00Z；台北時間：2026-11-12 12:40
  - 摘要：[FTNN新聞網]記者陳思穎／綜合報導台股今（12）日受輝達執行長黃仁勳（JensenHuang）因婚外情風波，傳出恐遭董事會撤換影響，開盤下跌76.69點，至44180.46點...
  - 原文連結：https://tw.stock.yahoo.com/news/%E7%8E%BB%E7%BA%96%E5%B8%83%E5%89%A91%E6%AA%94%E7%8D%A8%E6%92%90-%E9%BE%8D%E9%A0%AD%E5%BB%A0-%E5%89%8D%E4%B8%89%E5%AD%A3eps-1-57%E5%85%83%E8%BD%89%E8%99%A7%E7%82%BA%E7%9B%88-044000915.html
- 事件4：台玻爆量狂漲 分析師揭因：傳產股轉型電子股
  - 來源：Yahoo 台股；發布時間：2026-11-12T03:31:47Z；台北時間：2026-11-12 11:31
  - 摘要：「台玻是挖到鑽石喔」「台玻漲五天了 應該人人都有台玻了吧???????????????」「台玻要賺爛了 cc」「這次台玻權證一定要賺個10倍 cc」「雖然不知道台玻在漲什麼意思的 可是就是爽啊」
  - 原文連結：https://tw.stock.yahoo.com/news/%E3%80%90hot%E5%8F%B0%E8%82%A1%E3%80%91%E5%8F%B0%E7%8E%BB%E7%82%B840%E8%90%AC%E5%BC%B5%E5%B7%A8%E9%87%8F%E5%86%8D%E9%8E%96%E6%BC%B2%E5%81%9C%E5%AF%AB%E5%A4%A9%E5%83%B9%EF%BC%81%E7%B6%B2%E5%82%BB%E7%9C%BC%E3%80%8C%E6%98%AF%E6%8C%96%E5%88%B0%E9%91%BD%E7%9F%B3%E5%96%94%E3%80%8D-%E5%88%86%E6%9E%90%E5%B8%AB%EF%BC%9A%E9%82%84%E6%9C%89%E7%A9%BA%E9%96%93-033147588.html
- 事件5：台達電劇烈回檔 杜金龍自曝「一張沒賣」看好長線
  - 來源：Yahoo 台股；發布時間：2026-11-11T23:00:00Z；台北時間：2026-11-12 07:00
  - 摘要：台達電從高點2,500元跌到1,020元，跌幅近6成，股民哀嘆生無可戀，昨（11/11）日開高雖一度翻黑，但終場上漲20元，收在1,295元，漲幅1.57％，許多人問「還能抱嗎？」股市老先覺杜金龍直言，他手中台達電持股成本1,209元，至今
  - 原文連結：https://tw.stock.yahoo.com/news/%E5%8F%B0%E9%81%94%E9%9B%BB%E6%95%99%E6%88%B01-%E5%8F%B0%E9%81%94%E9%9B%BB%E6%9A%B4%E8%B7%8C%E8%BF%916%E6%88%90-%E6%9D%9C%E9%87%91%E9%BE%8D1%E5%BC%B5%E6%B2%92%E8%B3%A3-%E5%A4%96%E8%B3%87%E5%96%8A2400%E5%85%83-%E4%B8%8D%E7%94%A8%E6%80%95-230000780.html
- 事件6：台積電爆資安危機！暗網拍賣4.6萬筆員工個資 公司回應
  - 來源：Yahoo 台股；發布時間：2026-11-12T02:32:32Z；台北時間：2026-11-12 10:32
  - 摘要：近期台灣接連爆出多起重大資安事件，許多政府機關、知名企業遭駭客攻擊，沒想到護國神山台積電，也驚傳資安危機！有駭客在地下論壇點名「台積電（TSMC）」，拍賣詳細個資。賣家聲稱取得6.9GB共4.6萬筆員工紀錄，開價3 BTC，折合台幣 740
  - 原文連結：https://tw.stock.yahoo.com/news/%E7%8D%A8%E5%AE%B6-%E5%8F%B0%E7%A9%8D%E9%9B%BB%E8%B3%87%E5%AE%89%E9%A2%A8%E6%9A%B4-%E6%9A%97%E7%B6%B2%E6%8B%8D%E8%B3%A34-6%E8%90%AC%E7%AD%86%E5%93%A1%E5%B7%A5%E5%80%8B%E8%B3%87-%E9%A7%AD%E5%AE%A2%E9%96%8B%E5%83%B9-023001978.html
- 事件7：Federal Reserve Board announces approval of two applications by Mutual Federal Bancorp, MHC, and MFB Bancorp, Inc.
  - 來源：Federal Reserve；發布時間：Mon, 9 Nov 2026 21:00:00 GMT；台北時間：2026-11-10 05:00
  - 摘要：Federal Reserve Board announces approval of two applications by Mutual Federal Bancorp, MHC, and MFB Bancorp, Inc.
  - 原文連結：https://www.federalreserve.gov/newsevents/pressreleases/orders20261109a.htm
- 事件8：Federal Reserve Board announces termination of enforcement action with Allegiant United Holdings, LLC, Nano Financial Holdings, Inc., and Nano Banc
  - 來源：Federal Reserve；發布時間：Thu, 5 Nov 2026 16:00:00 GMT；台北時間：2026-11-06 00:00
  - 摘要：Federal Reserve Board announces termination of enforcement action with Allegiant United Holdings, LLC, Nano Financial Holdings, Inc., and Nano Banc
  - 原文連結：https://www.federalreserve.gov/newsevents/pressreleases/enforcement20261105a.htm
- 事件9：Feds arrest top official of healthcare company, alleging illegal drug importation
  - 來源：CNBC；發布時間：Wed, 11 Nov 2026 22:58:11 GMT；台北時間：2026-11-12 06:58
  - 摘要：U.S. officials are accusing two top officials of a Canadian company of operating a scheme to illegally import prescription drugs, court records show.
  - 原文連結：https://www.cnbc.com/2026/11/11/canarx-official-arrested-drug-importation.html
- 事件10：Canada’s ambassador warns Trump tariffs are driving up costs, threatening U.S. investment
  - 來源：CNBC；發布時間：Wed, 11 Nov 2026 22:30:57 GMT；台北時間：2026-11-12 06:30
  - 摘要：U.S.-Canada trade tensions persist as Trump's tariffs drive up costs, threaten investment and complicate negotiations between the two countries.
  - 原文連結：https://www.cnbc.com/2026/11/11/canada-ambassador-trump-tariffs-investments.html
- 事件11：Social Security could pay full benefits until 2059 if taxable payroll kept pace with GDP: AARP report
  - 來源：CNBC；發布時間：Wed, 11 Nov 2026 19:54:27 GMT；台北時間：2026-11-12 03:54
  - 摘要：An aging work force is not the only reason Social Security's trust funds now have a looming shortfall, according to AARP Public Policy Institute resea
  - 原文連結：https://www.cnbc.com/2026/11/11/social-security-benefits-taxable-payroll-gdp.html
- 事件12：White House vows to press ahead with tariffs despite midterm backlash over rising prices
  - 來源：CNBC；發布時間：Tue, 10 Nov 2026 21:45:46 GMT；台北時間：2026-11-11 05:45
  - 摘要：Business executives warned at a Washington summit of rising costs and shifting supply chains as polls showed growing opposition to Trump's tariffs.
  - 原文連結：https://www.cnbc.com/2026/11/10/trump-tariffs-midterms-gary-cohn-inflation.html


## 三、期貨

**資料來源：**
1. Cloudflare Workers：TAIFEX Proxy — https://taifex.grichtoyang.workers.dev/
2. TAIFEX Open API — https://openapi.taifex.com.tw/

近月契約月份：202611 (日盤成交量最大者)；交易日期：2026-11-11

### 1．台指期近月日盤行情

| 項目 | 數值 | 資料來源 |
|---|---|---|
| 開盤價 | 42,942 | TAIFEX Proxy |
| 最高價 | 44,250 | TAIFEX Proxy |
| 最低價 | 42,646 | TAIFEX Proxy |
| 收盤價 | 44,091 | TAIFEX Proxy |
| 漲跌點數 | +1,445 | TAIFEX Proxy |
| 漲跌幅 | +3.39 | TAIFEX Proxy |
| 成交量 | 81,696 | TAIFEX Proxy |
| 日盤高點及低點 | 44,250 / 42,646 | TAIFEX Proxy |

### 2．台指期近月夜盤行情

| 項目 | 數值 | 資料來源 |
|---|---|---|
| 開盤價 | 44,177 | TAIFEX Proxy |
| 最高價 | 44,911 | TAIFEX Proxy |
| 最低價 | 43,957 | TAIFEX Proxy |
| 收盤價 | 44,606 | TAIFEX Proxy |
| 漲跌點數 | +470 | TAIFEX Proxy |
| 漲跌幅 | +1.06 | TAIFEX Proxy |
| 成交量 | 47,550 | TAIFEX Proxy |
| 夜盤高點及低點 | 44,911 / 43,957 | TAIFEX Proxy |
| 結算價 | unavailable | TAIFEX Proxy |
| 未平倉量 | unavailable | TAIFEX Proxy |

### 3．法人台指期多空未平倉部位

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 外資多方 OI | 8,086 | TAIFEX Proxy |
| 外資空方 OI | 112,357 | TAIFEX Proxy |
| 外資多空淨 OI | -104,271 | TAIFEX Proxy |
| 投信多方 OI | 104,791 | TAIFEX Proxy |
| 投信空方 OI | 2,921 | TAIFEX Proxy |
| 投信多空淨 OI | +101,870 | TAIFEX Proxy |
| 自營商多方 OI | 4,728 | TAIFEX Proxy |
| 自營商空方 OI | 4,695 | TAIFEX Proxy |
| 自營商多空淨 OI | +33 | TAIFEX Proxy |
| 三大法人合計多方 OI | 117,605 | TAIFEX Proxy |
| 三大法人合計空方 OI | 119,973 | TAIFEX Proxy |
| 三大法人合計多空淨 OI | -2,368 | TAIFEX Proxy |
| 外資多空淨 OI 變化 | -798 | TAIFEX Proxy |
| 投信多空淨 OI 變化 | +3,351 | TAIFEX Proxy |
| 自營商多空淨 OI 變化 | -52 | TAIFEX Proxy |

### 4．前十大交易人多空未平倉部位

**資料來源：** `TAIFEX OpenAPI OpenInterestOfLargeTradersFutures` (官方資料落後約一日，標示實際日期)

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 前十大交易人多方 OI | 105,198 | TAIFEX Proxy |
| 前十大交易人空方 OI | 85,450 | TAIFEX Proxy |
| 前十大交易人多空淨 OI | +19,748 | TAIFEX Proxy |
| 多空淨 OI 變化 (2026-11-09→2026-11-11) | +6,576 | TAIFEX Proxy snapshots (2026-11-10) |
- 資料日期：2026-11-11 (TypeOfTraders=0 全部交易人；契約月份 202611)

### 5．日盤、夜盤法人交易資料

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 外資日盤多單交易量 | 80,899 | TAIFEX Proxy |
| 外資日盤空單交易量 | 81,678 | TAIFEX Proxy |
| 外資日盤多空淨交易量 | -779 | TAIFEX Proxy |
| 外資夜盤多單交易量 | 25,996 | TAIFEX Proxy |
| 外資夜盤空單交易量 | 26,994 | TAIFEX Proxy |
| 外資夜盤多空淨交易量 | -998 | TAIFEX Proxy |
| 外資日盤／夜盤交易量變化 | +219 | TAIFEX Proxy |
| 投信日盤多空淨交易量 | +3,351 | TAIFEX Proxy |
| 投信夜盤多空淨交易量 | +0 | TAIFEX Proxy |
| 投信日盤／夜盤交易量變化 | +3,351 | TAIFEX Proxy |
| 自營商日盤多空淨交易量 | -92 | TAIFEX Proxy |
| 自營商夜盤多空淨交易量 | +351 | TAIFEX Proxy |
| 自營商日盤／夜盤交易量變化 | -443 | TAIFEX Proxy |
| 三大法人日盤多空淨交易量 | +2,480 | TAIFEX Proxy |
| 三大法人夜盤多空淨交易量 | -647 | TAIFEX Proxy |
| 法人日盤交易金額淨額 (億元) | +216.1 | TAIFEX Proxy |
| 法人夜盤交易金額淨額 (億元) | -57.2 | TAIFEX Proxy |

### 6．期貨與現貨關係

| 項目 | 數值 | 資料來源 |
|---|---|---|
| 台指期近月價格 | 44,091 | TAIFEX Proxy |
| 加權指數價格 | 44,257.15 | twse-proxy |
| 台指期與加權指數價差 | -166.15 | TAIFEX Proxy+twse-proxy |
| 價差百分比 | -0.38 | TAIFEX Proxy+twse-proxy |
| 日盤基差 | -166.15 | TAIFEX Proxy+twse-proxy |
| 夜盤價格相對日盤收盤的變化 | +515 | TAIFEX Proxy |

### 7．日盤、夜盤與籌碼變化對照

#### 7.1 日夜盤價格與成交量對照 (變化 = 日盤 - 夜盤)

| 項目 | 日盤 | 夜盤 | 變化 (日-夜) | 資料來源 |
|---|---|---|---|---|
| 收盤價 | 44,091 | 44,606 | -515 | TAIFEX Proxy |
| 成交量 | 81,696 | 47,550 | +34,146 | TAIFEX Proxy |
- 台指期總 OI 前日變化：+2,501（來源：TAIFEX Proxy）


#### 7.2 法人籌碼日夜盤對照 (淨變化 = 日盤淨 - 夜盤淨；OI 為日盤收盤後總量，前日變化另列)

| 法人 | 交易量 |  |  |  |  |  |  | 未平倉量 |  |  |  | 資料來源 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|  | **日盤多單** | **日盤空單** | **日盤淨** | **夜盤多單** | **夜盤空單** | **夜盤淨** | **淨變化 (日-夜)** | **OI多方** | **OI空方** | **OI淨** | **OI前日變化** |  |
| 外資 | 80,899 | 81,678 | -779 | 25,996 | 26,994 | -998 | +219 | 8,086 | 112,357 | -104,271 | -798 | TAIFEX Proxy |
| 投信 | 4,978 | 1,627 | +3,351 | 0 | 0 | +0 | +3,351 | 104,791 | 2,921 | +101,870 | +3,351 | TAIFEX Proxy |
| 自營商 | 6,716 | 6,808 | -92 | 1,069 | 718 | +351 | -443 | 4,728 | 4,695 | +33 | -52 | TAIFEX Proxy |
| 三大法人合計 | 92,593 | 90,113 | +2,480 | 27,065 | 27,712 | -647 | +3,127 | 117,605 | 119,973 | -2,368 | +2,501 | TAIFEX Proxy |

#### 7.3 前十大交易人日夜盤對照 (OI 無日夜拆分，列收盤後總量)

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 前十大交易人多方 OI | 105,198 | TAIFEX Proxy |
| 前十大交易人空方 OI | 85,450 | TAIFEX Proxy |
| 前十大交易人多空淨 OI | +19,748 | TAIFEX Proxy |
| 前十大交易人多空淨 OI 變化 (2026-11-09→2026-11-11) | +6,576 | TAIFEX Proxy snapshots (2026-11-10) |

#### 7.4 夜盤劇本分類 (規則對應：夜盤漲跌 × 外資夜盤偏多空)

| 項目 | 數值 | 資料來源 |
|---|---|---|
| 夜盤成交量占比 (夜盤量／(夜盤量＋日盤量)) | 36.79% | TAIFEX Proxy |
| 夜盤漲跌點數 | +470 | TAIFEX Proxy |
| 外資夜盤多空淨交易量 | -998 | TAIFEX Proxy |
| 劇本分類 | 劇本二 | 規則對應 |
| 劇本條件 | 夜盤上漲＋外資偏空 | 規則對應 |
| 劇本特徵 | 先漲、小心開高走低 | 規則對應 |

## 四、選擇權

**資料來源：** 主要 TAIFEX 經 Cloudflare Worker Proxy；時區 `Asia/Taipei`

### 1．選擇權交易日期、到期日與資料時間

| 項目 | 數值 | 資料來源 |
|---|---|---|
| 交易日期 | 2026-11-11 | TAIFEX Proxy |
| 到期月份／到期日 | 202611W2 | TAIFEX Proxy |
| 資料更新時間 | 2026-11-12 12:51:43 | 本機 |
| 日盤／夜盤標記 | 日盤收盤後資料 | TAIFEX Proxy |

### 2．Call 總成交量、OI、OI 增減

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Call 總成交量 | 366,892 | TAIFEX Proxy |
| Call 總未平倉量 OI | 85,471 | TAIFEX Proxy |
| Call OI 增減 (2026-11-10→2026-11-11) | +8,846 | TAIFEX Proxy snapshots (2026-11-10) |

### 3．Put 總成交量、OI、OI 增減

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Put 總成交量 | 394,841 | TAIFEX Proxy |
| Put 總未平倉量 OI | 109,230 | TAIFEX Proxy |
| Put OI 增減 (2026-11-10→2026-11-11) | +51,977 | TAIFEX Proxy snapshots (2026-11-10) |

### 4．Call／Put 比例與變化

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Call／Put 成交量比例 | 0.93 | TAIFEX Proxy |
| Call／Put 未平倉量比例 | 0.78 | TAIFEX Proxy |
| Put／Call Ratio | 1.28 | TAIFEX Proxy |
| Call／Put 比例變化 (量比 2026-11-10→2026-11-11) | -11.28 | TAIFEX Proxy |
| 與前一交易日比較 (OI 比 2026-11-10→2026-11-11) | -1.37 | TAIFEX Proxy |
**資料來源：** 比例 `TAIFEX Proxy chain`；變化 `TAIFEX Proxy PutCallRatio`

### 5．外資 Call／Put 部位

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 外資 Call日買 | 130,690 | TAIFEX Proxy |
| 外資 Call日賣 | 128,536 | TAIFEX Proxy |
| 外資 Call日淨 | +2,154 | TAIFEX Proxy |
| 外資 Put日買 | 132,850 | TAIFEX Proxy |
| 外資 Put日賣 | 136,794 | TAIFEX Proxy |
| 外資 Put日淨 | -3,944 | TAIFEX Proxy |
| 外資 Call夜買 | 22,289 | TAIFEX Proxy |
| 外資 Call夜賣 | 22,047 | TAIFEX Proxy |
| 外資 Call夜淨 | +242 | TAIFEX Proxy |
| 外資 Put夜買 | 24,796 | TAIFEX Proxy |
| 外資 Put夜賣 | 24,617 | TAIFEX Proxy |
| 外資 Put夜淨 | +179 | TAIFEX Proxy |
| 外資 日盤淨總量 | +6,098 | TAIFEX Proxy |
| 外資 Call日夜淨增減 (日－夜) | +1,912 | TAIFEX Proxy |
| 外資 Put日夜淨增減 (日－夜) | -4,123 | TAIFEX Proxy |

### 6．自營商 Call／Put 部位

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 自營商 Call日買 | 85,562 | TAIFEX Proxy |
| 自營商 Call日賣 | 88,582 | TAIFEX Proxy |
| 自營商 Call日淨 | -3,020 | TAIFEX Proxy |
| 自營商 Put日買 | 94,874 | TAIFEX Proxy |
| 自營商 Put日賣 | 112,565 | TAIFEX Proxy |
| 自營商 Put日淨 | -17,691 | TAIFEX Proxy |
| 自營商 Call夜買 | 17,288 | TAIFEX Proxy |
| 自營商 Call夜賣 | 16,821 | TAIFEX Proxy |
| 自營商 Call夜淨 | +467 | TAIFEX Proxy |
| 自營商 Put夜買 | 17,043 | TAIFEX Proxy |
| 自營商 Put夜賣 | 19,073 | TAIFEX Proxy |
| 自營商 Put夜淨 | -2,030 | TAIFEX Proxy |
| 自營商 日盤淨總量 | +14,671 | TAIFEX Proxy |
| 自營商 Call日夜淨增減 (日－夜) | -3,487 | TAIFEX Proxy |
| 自營商 Put日夜淨增減 (日－夜) | -15,661 | TAIFEX Proxy |

### 7．主要 Call OI 集中區

| 項目 | 履約價 | OI | 資料來源 |
|---|---|---|---|
| Call OI 第1大履約價 | 46,000 | 7,773 | TAIFEX Proxy |
| Call OI 第2大履約價 | 44,000 | 5,370 | TAIFEX Proxy |
| Call OI 第3大履約價 | 45,000 | 3,386 | TAIFEX Proxy |
| Call OI 最大履約價 | 46,000 | 7,773 | TAIFEX Proxy |

#### Call OI 分布明細 Top10 (機器可讀，到期月份 202611W2)

| # | 履約價 | OI | 佔比 | 資料來源 |
|---|---|---|---|---|
| C1 | 46,000 | 7,773 | 9.09% | TAIFEX Proxy |
| C2 | 44,000 | 5,370 | 6.28% | TAIFEX Proxy |
| C3 | 45,000 | 3,386 | 3.96% | TAIFEX Proxy |
| C4 | 48,300 | 2,774 | 3.25% | TAIFEX Proxy |
| C5 | 43,000 | 2,276 | 2.66% | TAIFEX Proxy |
| C6 | 43,500 | 2,247 | 2.63% | TAIFEX Proxy |
| C7 | 43,800 | 1,557 | 1.82% | TAIFEX Proxy |
| C8 | 41,000 | 1,386 | 1.62% | TAIFEX Proxy |
| C9 | 46,500 | 1,351 | 1.58% | TAIFEX Proxy |
| C10 | 45,500 | 1,292 | 1.51% | TAIFEX Proxy |


### 8．主要 Put OI 集中區

| 項目 | 履約價 | OI | 資料來源 |
|---|---|---|---|
| Put OI 第1大履約價 | 35,700 | 3,777 | TAIFEX Proxy |
| Put OI 第2大履約價 | 43,500 | 3,738 | TAIFEX Proxy |
| Put OI 第3大履約價 | 40,000 | 3,614 | TAIFEX Proxy |
| Put OI 最大履約價 | 35,700 | 3,777 | TAIFEX Proxy |

#### Put OI 分布明細 Top10 (機器可讀，到期月份 202611W2)

| # | 履約價 | OI | 佔比 | 資料來源 |
|---|---|---|---|---|
| P1 | 35,700 | 3,777 | 3.46% | TAIFEX Proxy |
| P2 | 43,500 | 3,738 | 3.42% | TAIFEX Proxy |
| P3 | 40,000 | 3,614 | 3.31% | TAIFEX Proxy |
| P4 | 42,000 | 3,202 | 2.93% | TAIFEX Proxy |
| P5 | 43,000 | 3,134 | 2.87% | TAIFEX Proxy |
| P6 | 41,000 | 3,048 | 2.79% | TAIFEX Proxy |
| P7 | 38,000 | 2,659 | 2.43% | TAIFEX Proxy |
| P8 | 43,100 | 2,535 | 2.32% | TAIFEX Proxy |
| P9 | 42,500 | 2,424 | 2.22% | TAIFEX Proxy |
| P10 | 41,500 | 2,405 | 2.2% | TAIFEX Proxy |


### 9．Call OI 增減集中區

| 項目 | 履約價 (增減口數) | 資料來源 |
|---|---|---|
| Call OI 增加最多的履約價 | 44,000 (+3,018) | TAIFEX Proxy snapshots (2026-11-10) |
| Call OI 減少最多的履約價 | 46,000 (-1,068) | TAIFEX Proxy snapshots (2026-11-10) |

### 10．Put OI 增減集中區

| 項目 | 履約價 (增減口數) | 資料來源 |
|---|---|---|
| Put OI 增加最多的履約價 | 43,500 (+3,653) | TAIFEX Proxy snapshots (2026-11-10) |
| Put OI 減少最多的履約價 | 35,700 (-410) | TAIFEX Proxy snapshots (2026-11-10) |

### 11．Call Wall

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Call Wall 價位 | 46,000 | TAIFEX Proxy |
| 對應到期月份 | 202611W2 | TAIFEX Proxy |
| 與前一交易日的變化 (2026-11-10→2026-11-11) | +0 | TAIFEX Proxy snapshots (2026-11-10) |

### 12．Put Wall

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Put Wall 價位 | 35,700 | TAIFEX Proxy |
| 對應到期月份 | 202611W2 | TAIFEX Proxy |
| 與前一交易日的變化 (2026-11-10→2026-11-11) | +0 | TAIFEX Proxy snapshots (2026-11-10) |

### 13．Gamma Wall

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Gamma Wall 價位 | 45,000.00 | TAIFEX Proxy (options-market-structure-compact (proxy)) |
| 對應到期月份 | 202611W2 | TAIFEX Proxy |
| 資料日期 | 2026-11-11 | TAIFEX Proxy (options-market-structure-compact (proxy)) |

### 14．Gamma Flip

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Gamma Flip 價位 | 43,546.87 | TAIFEX Proxy (options-market-structure-compact (proxy)) |
| 對應到期月份 | 202611W2 | TAIFEX Proxy |
| 資料日期 | 2026-11-11 | TAIFEX Proxy (options-market-structure-compact (proxy)) |

### 15．Max Pain

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Max Pain 價位 | 42,950 | TAIFEX Proxy |
| 對應到期月份 | 202611W2 | TAIFEX Proxy |
| 與前一交易日的變化 (2026-11-10→2026-11-11) | +1,950 | TAIFEX Proxy snapshots (2026-11-10) |

### 17．選擇權法人日盤、夜盤交易

| 法人 | 日盤多單 | 日盤空單 | 日盤淨 | 夜盤多單 | 夜盤空單 | 夜盤淨 | 淨變化 (日-夜) | 資料來源 |
|---|---|---|---|---|---|---|---|---|
| 外資 | 267,484 | 261,386 | +6,098 | 46,906 | 46,843 | +63 | +6,035 | TAIFEX Proxy |
| 投信 | 240 | 3,147 | -2,907 | 0 | 0 | +0 | -2,907 | TAIFEX Proxy |
| 自營商 | 198,127 | 183,456 | +14,671 | 36,361 | 33,864 | +2,497 | +12,174 | TAIFEX Proxy |
| 三大法人合計 | 465,851 | 447,989 | +17,862 | 83,267 | 80,707 | +2,560 | +15,302 | TAIFEX Proxy |
- 方法論：多方＝買Call＋賣Put（看多），空方＝賣Call＋買Put（看空），淨額＝看多－看空（已用 Call／Put 拆分頁交叉驗算一致）
- 公式：多方(買)－空方(賣)＝（買call＋賣put）－（賣call＋買put）＝看多－看空
- 速記：多＝BC＋SP、空＝SC＋BP

#### 法人多空力道表（金額・億元；上游千元／1e5）

| 法人 | 日多方力道 | 日空方力道 | 日淨多空力道 | 夜多方力道 | 夜空方力道 | 夜淨多空力道 | 日淨－夜淨 | 資料來源 |
|---|---|---|---|---|---|---|---|---|
| 外資 | 19.77 | 19.07 | +0.70 | 5.76 | 5.95 | -0.19 | +0.88 | TAIFEX Proxy |
| 投信 | 0.00 | 2.06 | -2.05 | 0.00 | 0.00 | +0 | -2.05 | TAIFEX Proxy |
| 自營商 | 18.54 | 15.39 | +3.15 | 4.48 | 4.05 | +0.43 | +2.72 | TAIFEX Proxy |
| 三大法人合計 | 38.31 | 36.51 | +1.80 | 10.25 | 10.00 | +0.25 | +1.55 | TAIFEX Proxy |

### 18．選擇權前十大

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 買權多方 OI | 23,549 | TAIFEX Proxy |
| 買權空方 OI | 28,526 | TAIFEX Proxy |
| 買權多空淨 OI | -4,977 | TAIFEX Proxy |
| 買權多空淨 OI 變化 | unavailable | 端點未提供 |

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 賣權多方 OI | 14,352 | TAIFEX Proxy |
| 賣權空方 OI | 16,859 | TAIFEX Proxy |
| 賣權多空淨 OI | -2,507 | TAIFEX Proxy |
| 賣權多空淨 OI 變化 | unavailable | 端點未提供 |
- 資料日期：買權 2026-11-11／賣權 2026-11-11 (TypeOfTraders=0 全部交易人；契約月份 202611)

#### 大戶流向（全日；前十大無日夜拆分）

| 項目 | 淨變化 | 區間 | 資料來源 |
|---|---|---|---|
| 期貨前十大 | +6,576 | 2026-11-09→2026-11-11 | TAIFEX Proxy snapshots (2026-11-10) |
| 買權前十大 | unavailable | — | 端點未提供 |
| 賣權前十大 | unavailable | — | 端點未提供 |

### 16．資料來源、時間、時區與狀態

- 資料來源：TAIFEX 經 Cloudflare Worker Proxy
- 資料日期：2026-11-11；資料時間：2026-11-12 12:51:43；時區：`Asia/Taipei`
- 日盤／夜盤標記：日盤收盤後 + 夜盤盤後
- 未取得欄位 (3)：futures.gamma_wall, futures.gamma_flip, options.top10_change
- 註記：futures-price-after-hours 日期 2026-11-11 非今日 2026-11-12，視為無新節次，不採用
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
| 外資 | -7.7 | -104,271 | -779 | -998 | +6,098 | +63 | 避險／對沖 | 分歧 | twse-proxy／TAIFEX Proxy |
| 投信 | +185.9 | +101,870 | +3,351 | +0 | -2,907 | +0 | 避險／對沖 | 分歧 | twse-proxy／TAIFEX Proxy |
| 自營商 | +62.6 | +33 | -92 | +351 | +14,671 | +2,497 | 趨勢偏多 | 分歧 | twse-proxy／TAIFEX Proxy |
