# DATA_REPORT_20260922

- 報告日期：`2026-09-22`
- T0 交易日期：`2026-09-22`
- 資料產出時間：`2026-09-22 14:17:27`
- 時區：`Asia/Taipei`

---

## 一、現貨

### 1. 台股大盤行情

**資料來源：** `Cloudflare Worker：twse-proxy` (備援 `TWSE OpenAPI MI_INDEX`)

| 項目 | 數值 | 單位 | 資料來源 |
|---|---|---|---|
| 加權指數 | 47,800.17 | 點 | twse-proxy |
| 開盤 | 47,981.04 | 點 | FinMind TaiwanStockPrice TAIEX |
| 最高 | 48,601.53 | 點 | FinMind TaiwanStockPrice TAIEX |
| 最低 | 47,800.17 | 點 | FinMind TaiwanStockPrice TAIEX |
| 收盤 | 47,800.17 | 點 | twse-proxy |
| 漲跌點數 | 81.33 | 點 | twse-proxy |
| 漲跌幅 | +0.17 | % | twse-proxy |
| 成交金額 | 10,215.7 | 億元 | twse-proxy market_statistics |

### 2. 市場漲跌家數

#### 2.1 上市公司

**資料來源：** `Cloudflare Worker：twse-proxy` (備援 `TWSE OpenAPI twtazu_od`)

| 項目 | 家數 | 資料來源 |
|---|---|---|
| 上漲家數 | 330 | twse-proxy |
| 下跌家數 | 636 | twse-proxy |
| 平盤家數 | 113 | twse-proxy |
| 漲停家數 | 14 | twse-proxy |
| 跌停家數 | 2 | twse-proxy |

#### 2.2 上櫃公司

**資料來源：** `TPEX OpenAPI tpex_mainborad_highlight`

| 項目 | 家數 | 資料來源 |
|---|---|---|
| 上漲家數 | unavailable | TPEX |
| 下跌家數 | unavailable | TPEX |
| 平盤家數 | unavailable | TPEX |
| 漲停家數 | unavailable | TPEX |
| 跌停家數 | unavailable | TPEX |

### 3. 三大法人現貨買賣超

**資料來源：** `TWSE RWD BFI82U`

| 法人別 | 買賣超金額 | 單位 | 資料來源 |
|---|---|---|---|
| 外資 | +204.8 | 億元 | twse-proxy /institutional |
| 投信 | +46.0 | 億元 | twse-proxy /institutional |
| 自營商 | +227.3 | 億元 | twse-proxy /institutional |
| 三大法人合計 | +478.0 | 億元 | twse-proxy /institutional |

### 4. 融資融券

**資料來源：** 上市+上櫃 `HiStock` (金額口徑)；維持率 `istock.tw`；備援官方逐股加總

| 項目 | 數值 | 單位 | 資料來源 |
|---|---|---|---|
| 融資餘額 | unavailable | 億元 | HiStock |
| 融資增減 | unavailable | 億元 | HiStock |
| 融券餘額 | 231,582 | 張 | HiStock |
| 融券增減 | 10,189 | 張 | HiStock |
| 融資維持率 | unavailable | % | istock.tw |

### 5. 借券資料

**資料來源：** 上市 `TWSE OpenAPI TWT96U` (可借餘額)、上櫃 `TPEX OpenAPI tpex_margin_sbl`

| 項目 | 數值 | 單位 | 資料來源 |
|---|---|---|---|
| 借券餘額 | 2,437,911 | 張 | TWSE TWT93U + TPEX margin_sbl |
| 借券賣出餘額 | unavailable | 張 | TWSE TWT93U + TPEX margin_sbl |
| 借券賣出增減 | unavailable | 張 | TWSE TWT93U + TPEX margin_sbl |

### 6. 市場成交結構

**資料來源：** 上市 `twse-proxy market_statistics`、上櫃 `TPEX OpenAPI tpex_mainborad_highlight`

| 項目 | 成交金額 | 單位 | 資料來源 |
|---|---|---|---|
| 上市成交金額 | 10,215.7 | 億元 | twse-proxy market_statistics |
| 上櫃成交金額 | unavailable | 億元 | TPEX |
| 上市櫃成交金額合計 | 10,215.7 | 億元 | twse-proxy market_statistics+TPEX |

## 二、重要市場

### 1. 美股指數

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 收盤／最新值 | 漲跌點 | 漲跌幅 | 資料來源 |
|---|---|---|---|---|---|
| S&P 500 | ^GSPC | 7,764.70 | 114.20 | +1.49 | Yahoo Finance Chart API |
| Nasdaq Composite | ^IXIC | 27,122.09 | 599.55 | +2.26 | Yahoo Finance Chart API |
| Nasdaq 100 | ^NDX | 30,482.35 | 838.18 | +2.83 | Yahoo Finance Chart API |
| Dow Jones | ^DJI | 52,048.83 | 366.19 | +0.71 | Yahoo Finance Chart API |
| 費城半導體 SOX | ^SOX | 12,433.17 | 511.48 | +4.29 | Yahoo Finance Chart API |
| VIX | ^VIX | 14.87 | 0.06 | +0.41 | Yahoo Finance Chart API |

### 2. 亞洲主要指數

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 收盤／最新值 | 漲跌點 | 漲跌幅 | 資料來源 |
|---|---|---|---|---|---|
| 日經225 | ^N225 | 65,018.95 | 882.70 | +1.38 | Yahoo Finance Chart API |
| 韓國KOSPI | ^KS11 | 7,042.91 | 35.19 | +0.50 | Yahoo Finance Chart API |
| 香港恆生 | ^HSI | 25,123.10 | 80.39 | +0.32 | Yahoo Finance Chart API |
| 上海綜合 | 000001.SS | 3,955.54 | 5.63 | +0.14 | Yahoo Finance Chart API |
| 深圳成分 | 399001.SZ | 13,756.58 | 26.56 | +0.19 | Yahoo Finance Chart API |

### 3. 美股指數期貨

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 最新值 | 漲跌點 | 漲跌幅 | 資料來源 |
|---|---|---|---|---|---|
| S&P500期貨 | ES=F | 7,835.75 | 2.25 | +0.03 | Yahoo Finance Chart API |
| Nasdaq100期貨 | NQ=F | 30,790.75 | 6.00 | +0.02 | Yahoo Finance Chart API |
| 道瓊期貨 | YM=F | 52,494.00 | 19.00 | +0.04 | Yahoo Finance Chart API |
| Russell2000期貨 | RTY=F | 2,896.00 | -1.40 | -0.05 | Yahoo Finance Chart API |

### 4. 美國國債殖利率

**資料來源：** `U.S. Treasury Fiscal Data API` (失敗時備援 Treasury yield.xml 與 `Yahoo Finance`)

| 項目 | API 資料欄位／識別 | 殖利率 | 日變化 | 資料來源 |
|---|---|---|---|---|
| 美國 2 年期殖利率 | 2 Yr | 4.76 | 0.00 | U.S. Treasury yield.xml (網頁備援) |
| 美國 10 年期殖利率 | 10 Yr | 4.96 | -0.04 | Yahoo Finance (備援) |
| 美國 30 年期殖利率 | 30 Yr | 5.30 | -0.03 | Yahoo Finance (備援) |

### 5. 主要匯率

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 最新值 | 漲跌點 | 漲跌幅 | 資料來源 |
|---|---|---|---|---|---|
| USD/TWD | TWD=X | 31.72 | -0.09 | -0.30 | Yahoo Finance Chart API |
| DXY美元指數 | DX-Y.NYB | 100.43 | 0.00 | +0.00 | Yahoo Finance Chart API |
| USD/JPY | JPY=X | 157.60 | 0.56 | +0.35 | Yahoo Finance Chart API |
| USD/KRW | KRW=X | 1,358.48 | -26.38 | -1.90 | Yahoo Finance Chart API |

### 6. 台灣相關ADR

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 收盤／最新值 | 漲跌點 | 漲跌幅 | 資料來源 |
|---|---|---|---|---|---|
| 台積電ADR | TSM | 445.14 | 10.47 | +2.41 | Yahoo Finance Chart API |
| 聯電ADR | UMC | 25.43 | 0.82 | +3.33 | Yahoo Finance Chart API |
| 日月光ADR | ASX | 43.73 | 2.10 | +5.04 | Yahoo Finance Chart API |

### 7. 原油黃金Bitcoin

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 收盤／最新值 | 漲跌點 | 漲跌幅 | 資料來源 |
|---|---|---|---|---|---|
| WTI原油期貨 | CL=F | 93.68 | -2.10 | -2.19 | Yahoo Finance Chart API |
| 黃金期貨 | GC=F | 4,353.70 | -30.20 | -0.69 | Yahoo Finance Chart API |
| Bitcoin | BTC-USD | 85,281.00 | 4,138.39 | +5.10 | Yahoo Finance Chart API |

### 8. 重大經濟數據、央行事件與重大市場新聞

**資料來源：** 台股 `tw.stock.yahoo.com` (含內文摘要)；國際 `Fed 公告 RSS`＋`CNBC`＋`MarketWatch` (標題、來源、時間與連結)

- 事件1：台股盤中創高後外資反手賣 萬點行情只留81點漲幅
  - 來源：Yahoo 台股；發布時間：2026-09-22T05:50:57Z；台北時間：2026-09-22 13:50
  - 摘要：台股22日開高走低，台積電紅翻黑，台股也拉出801點的上影線，最後收在47800.17...
  - 原文連結：https://tw.stock.yahoo.com/news/%E8%81%AF%E7%99%BC%E7%A7%91-%E5%89%B5%E6%84%8F%E8%82%A1%E5%83%B9%E7%B9%BC%E7%BA%8C%E5%89%B5%E6%96%B0%E9%AB%98-%E4%BD%86%E5%8F%B0%E8%82%A1%E8%A6%8B4%E8%90%AC8%E5%BE%8C%E5%A4%96%E8%B3%87%E5%8F%8D%E6%89%8B%E8%B3%A3%E8%B6%85-%E5%8F%B0%E7%A9%8D%E9%9B%BB%E6%94%B6%E7%9B%A4%E5%8F%8D%E8%B7%8C-055057217.html
- 事件2：「三角飯糰」突現身IG 宏達電神祕新品準備揭曉
  - 來源：Yahoo 台股；發布時間：2026-09-22T01:58:15Z；台北時間：2026-09-22 09:58
  - 摘要：hTC宏達電（2498）今日正式發出新品預告，即將推出全新神祕新商品，並首度公開疑似吉祥物的「VIVEE」，為新產品搶先預熱。不過，根據先前hTC全球副總裁黃昭穎受訪時曾透露「手機將退居二線」，這次的新品高機率將是手機之外的其他產品，也吸引
  - 原文連結：https://tw.stock.yahoo.com/news/htc%E5%AE%8F%E9%81%94%E9%9B%BB%E5%86%8D%E7%99%BC%E5%B8%83%E3%80%8C%E6%96%B0%E5%93%81%E9%A0%90%E5%91%8A%E3%80%8D%EF%BC%81%E6%96%B0%E7%B2%89%E5%B0%88%E3%80%8Cvivee%E3%80%8D%E5%90%8C%E6%AD%A5%E5%85%AC%E9%96%8B-015815800.html
- 事件3：聯發科把戰線拉到PC 3奈米晶片搶進Google供應鏈
  - 來源：Yahoo 台股；發布時間：2026-09-22T05:32:00Z；台北時間：2026-09-22 13:32
  - 摘要：IC設計龍頭聯發科近日股價強勢攻高，盤中一度逼近5500元大關，創下歷史新高。市場聚焦於聯發科正式發表全新個人運算旗艦晶片Dimensity CX C10 Max，該晶片採用台積電3奈米先進製程，並具備高達55 TOPS的AI運算效能，專為
  - 原文連結：https://tw.stock.yahoo.com/news/3%E5%A5%88%E7%B1%B3%E6%99%B6%E7%89%87%E5%88%87%E5%85%A5googlebook-%E8%81%AF%E7%99%BC%E7%A7%91-%E5%BA%A6%E9%80%B2%E9%80%BC5500%E9%97%9C%E5%8D%A1-%E5%86%8D%E5%89%B5%E6%AD%B7%E5%8F%B2%E6%96%B0%E9%AB%98-053200716.html
- 事件4：健康幣怎麼拿又怎麼花 五大任務與兌換門檻一次看懂
  - 來源：Yahoo 台股；發布時間：2026-09-22T05:45:07Z；台北時間：2026-09-22 13:45
  - 摘要：[NOWNEWS今日新聞]衛福部推出「健康幣」，盼讓民眾從預防保健延伸至日常生活的健康行動。而「健康幣」自10月1日起，只要年滿18歲的民眾，完成健檢、癌症篩檢或打疫苗等指定健康任務，就可累積。但有哪...
  - 原文連結：https://tw.stock.yahoo.com/news/%E5%81%A5%E5%BA%B7%E5%B9%A3%E6%95%88%E6%9C%9F2%E5%B9%B4-%E6%96%87%E7%9C%8B%E6%87%82%E7%94%A8%E6%B3%95-%E5%85%8C%E6%8F%9B%E6%96%B9%E5%BC%8F-054507367.html
- 事件5：熬過10年虧損寒冬 漢測蜜月大噴發衝出50倍身價
  - 來源：Yahoo 台股；發布時間：2026-09-22T04:23:39Z；台北時間：2026-09-22 12:23
  - 摘要：漢測曾連虧十年、減資還債，直到工程服務救回公司，再跨入探針卡與AI測試市場，如今更寫下台股最高IPO承銷價紀錄。
  - 原文連結：https://tw.stock.yahoo.com/news/%E6%BC%A2%E6%B8%AC%E8%9C%9C%E6%9C%88%E8%A1%8C%E6%83%85%E5%A4%A7%E5%99%B4%E7%99%BC-%E6%9B%BE%E9%80%A3%E8%99%A710%E5%B9%B4-%E5%85%AC%E5%8F%B8%E5%89%A920%E5%A4%9A%E4%BA%BA-%E5%A6%82%E4%BB%8A%E7%82%BA%E4%BD%95%E8%82%A1%E5%83%B9-%E5%B9%B4%E7%BF%BB50%E5%80%8D-042339931.html
- 事件6：ABF載板三雄滿血復活 法人上調欣興目標價
  - 來源：Yahoo 台股；發布時間：2026-09-22T04:09:56Z；台北時間：2026-09-22 12:09
  - 摘要：AI伺服器需求持續升溫，帶動ABF載板族群走強，PCB及IC載板大廠欣興（3037）今（22）日股價強勢攻上漲停，來到1,120元，盤中仍有超過5,000張買單排隊。南電（8046）也同步攻上漲停價1,165元，景碩（3189）同步走強、盤
  - 原文連結：https://tw.stock.yahoo.com/news/%E6%AC%A3%E8%88%88-%E5%8D%97%E9%9B%BB%E5%BC%B7%E6%94%BB%E6%BC%B2%E5%81%9C-abf%E8%BC%89%E6%9D%BF%E6%97%8F%E7%BE%A4%E9%9C%80%E6%B1%82%E7%88%86%E7%99%BC-%E6%B3%95%E4%BA%BA%E6%9C%80%E6%96%B0%E7%9B%AE%E6%A8%99%E5%83%B9%E6%9B%9D%E5%85%89-%E5%BE%8C%E9%9D%A2%E9%82%84%E6%9C%89%E5%93%AA%E4%BA%9B%E8%A3%9C%E6%BC%B2%E8%82%A1-040956455.html
- 事件7：Federal Reserve Board announces termination of enforcement action with SNB Bancshares and Bank of Eufaula
  - 來源：Federal Reserve；發布時間：Fri, 18 Sep 2026 15:00:00 GMT；台北時間：2026-09-18 23:00
  - 摘要：Federal Reserve Board announces termination of enforcement action with SNB Bancshares and Bank of Eufaula
  - 原文連結：https://www.federalreserve.gov/newsevents/pressreleases/enforcement20260918b.htm
- 事件8：Federal Reserve Board issues enforcement actions with former employee of Northstar Bank, former employee of American Express Travel Related Services Company, Inc., and former employee of Regions Bank
  - 來源：Federal Reserve；發布時間：Fri, 18 Sep 2026 15:00:00 GMT；台北時間：2026-09-18 23:00
  - 摘要：Federal Reserve Board issues enforcement actions with former employee of Northstar Bank, former employee of American Express Travel Related Services C
  - 原文連結：https://www.federalreserve.gov/newsevents/pressreleases/enforcement20260918a.htm
- 事件9：Federal Reserve issues FOMC statement
  - 來源：Federal Reserve；發布時間：Wed, 16 Sep 2026 18:00:00 GMT；台北時間：2026-09-17 02:00
  - 摘要：Federal Reserve issues FOMC statement
  - 原文連結：https://www.federalreserve.gov/newsevents/pressreleases/monetary20260916a.htm
- 事件10：Federal Reserve Board and Federal Open Market Committee release economic projections from the September 15-16 FOMC meeting
  - 來源：Federal Reserve；發布時間：Wed, 16 Sep 2026 18:00:00 GMT；台北時間：2026-09-17 02:00
  - 摘要：Federal Reserve Board and Federal Open Market Committee release economic projections from the September 15-16 FOMC meeting
  - 原文連結：https://www.federalreserve.gov/newsevents/pressreleases/monetary20260916b.htm
- 事件11：Trump, Xi seek trade stability and deals, but AI, tariffs and Iran loom large. What to watch
  - 來源：CNBC；發布時間：Mon, 21 Sep 2026 22:25:33 GMT；台北時間：2026-09-22 06:25
  - 摘要：Trump, facing low approval on the economy ahead of the midterm election, has an added incentive to emerge from the summit with China's Xi touting trad
  - 原文連結：https://www.cnbc.com/2026/09/21/trump-xi-china-summit-trade-tariffs.html
- 事件12：Investors rush into India’s National Stock Exchange IPO at valuation multiple above Nasdaq
  - 來源：CNBC；發布時間：Tue, 22 Sep 2026 04:00:28 GMT；台北時間：2026-09-22 12:00
  - 摘要：The $2.3 billion NSE IPO, India's largest public share sale issue so far this year, has drawn strong interest from investors, with bids of more than $
  - 原文連結：https://www.cnbc.com/2026/09/22/india-nse-ipo-billion-nasdaq.html


### 9. 產業資金流向 (股市智投)

**資料來源：** `StockIntelli API` — https://www.stockintelli.com/market/industry-flow

- unavailable (StockIntelli API 速率限制或回應異常)

## 三、期貨

**資料來源：**
1. Cloudflare Workers：TAIFEX Proxy — https://taifex.grichtoyang.workers.dev/
2. TAIFEX Open API — https://openapi.taifex.com.tw/

近月契約月份：202610 (日盤成交量最大者)；交易日期：2026-09-22

### 1．台指期近月日盤行情

| 項目 | 數值 | 資料來源 |
|---|---|---|
| 開盤價 | 47,607 | TAIFEX Proxy |
| 最高價 | 48,091 | TAIFEX Proxy |
| 最低價 | 47,496 | TAIFEX Proxy |
| 收盤價 | 48,077 | TAIFEX Proxy |
| 漲跌點數 | +649 | TAIFEX Proxy |
| 漲跌幅 | +1.37 | TAIFEX Proxy |
| 成交量 | 59,264 | TAIFEX Proxy |
| 日盤高點及低點 | 48,091 / 47,496 | TAIFEX Proxy |

### 2．台指期近月夜盤行情

| 項目 | 數值 | 資料來源 |
|---|---|---|
| 開盤價 | 48,121 | proxy |
| 最高價 | 48,805 | proxy |
| 最低價 | 48,105 | proxy |
| 收盤價 | 48,781 | proxy |
| 漲跌點數 | +728 | proxy |
| 漲跌幅 | +1.51 | proxy |
| 成交量 | 21,514 | TAIFEX Proxy |
| 夜盤高點及低點 | 48,805 / 48,105 | proxy |
| 結算價 | 48,053 | TAIFEX Proxy |
| 未平倉量 | 101,502 | TAIFEX Proxy |

### 3．法人台指期多空未平倉部位

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 外資多方 OI | 0 | TAIFEX Proxy |
| 外資空方 OI | 0 | TAIFEX Proxy |
| 外資多空淨 OI | +0 | TAIFEX Proxy |
| 投信多方 OI | 0 | TAIFEX Proxy |
| 投信空方 OI | 0 | TAIFEX Proxy |
| 投信多空淨 OI | +0 | TAIFEX Proxy |
| 自營商多方 OI | 0 | TAIFEX Proxy |
| 自營商空方 OI | 0 | TAIFEX Proxy |
| 自營商多空淨 OI | +0 | TAIFEX Proxy |
| 三大法人合計多方 OI | 0 | TAIFEX Proxy |
| 三大法人合計空方 OI | 0 | TAIFEX Proxy |
| 三大法人合計多空淨 OI | +0 | TAIFEX Proxy |
| 外資多空淨 OI 變化 | +74,081 | TAIFEX Proxy |
| 投信多空淨 OI 變化 | -74,019 | TAIFEX Proxy |
| 自營商多空淨 OI 變化 | +3,354 | TAIFEX Proxy |

### 4．前十大交易人多空未平倉部位

**資料來源：** `TAIFEX OpenAPI OpenInterestOfLargeTradersFutures` (官方資料落後約一日，標示實際日期)

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 前十大交易人多方 OI | 80,066 | TAIFEX Proxy |
| 前十大交易人空方 OI | 69,303 | TAIFEX Proxy |
| 前十大交易人多空淨 OI | +10,763 | TAIFEX Proxy |
| 多空淨 OI 變化 | unavailable | 端點未提供 |
- 資料日期：2026-09-21 (TypeOfTraders=0 全部交易人；契約月份 202610)

### 5．日盤、夜盤法人交易資料

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 外資日盤多單交易量 | 33,568 | TAIFEX Proxy |
| 外資日盤空單交易量 | 35,050 | TAIFEX Proxy |
| 外資日盤多空淨交易量 | -1,482 | TAIFEX Proxy |
| 外資夜盤多單交易量 | 11,094 | TAIFEX Proxy |
| 外資夜盤空單交易量 | 10,839 | TAIFEX Proxy |
| 外資夜盤多空淨交易量 | +255 | TAIFEX Proxy |
| 外資日盤／夜盤交易量變化 | -1,737 | TAIFEX Proxy |
| 投信日盤多空淨交易量 | -42 | TAIFEX Proxy |
| 投信夜盤多空淨交易量 | +0 | TAIFEX Proxy |
| 投信日盤／夜盤交易量變化 | -42 | TAIFEX Proxy |
| 自營商日盤多空淨交易量 | -106 | TAIFEX Proxy |
| 自營商夜盤多空淨交易量 | +73 | TAIFEX Proxy |
| 自營商日盤／夜盤交易量變化 | -179 | TAIFEX Proxy |
| 三大法人日盤多空淨交易量 | -1,630 | TAIFEX Proxy |
| 三大法人夜盤多空淨交易量 | +328 | TAIFEX Proxy |
| 法人日盤交易金額淨額 (億元) | -157.9 | TAIFEX Proxy |
| 法人夜盤交易金額淨額 (億元) | +31.8 | TAIFEX Proxy |

### 6．期貨與現貨關係

| 項目 | 數值 | 資料來源 |
|---|---|---|
| 台指期近月價格 | 48,077 | TAIFEX Proxy |
| 加權指數價格 | 47,800.17 | twse-proxy |
| 台指期與加權指數價差 | +276.83 | TAIFEX Proxy+twse-proxy |
| 價差百分比 | +0.58 | TAIFEX Proxy+twse-proxy |
| 日盤基差 | +276.83 | TAIFEX Proxy+twse-proxy |
| 夜盤價格相對日盤收盤的變化 | +704 | proxy |

### 7．日盤、夜盤與籌碼變化對照

#### 7.1 日夜盤價格與成交量對照 (變化 = 日盤 - 夜盤)

| 項目 | 日盤 | 夜盤 | 變化 (日-夜) | 資料來源 |
|---|---|---|---|---|
| 收盤價 | 48,077 | 48,781 | -704 | TAIFEX Proxy |
| 成交量 | 37,750 | 21,514 | +16,236 | TAIFEX Proxy |
- 台指期總 OI 前日變化：+3,416（來源：TAIFEX Proxy）


#### 7.2 法人籌碼日夜盤對照 (淨變化 = 日盤淨 - 夜盤淨；OI 為日盤收盤後總量，前日變化另列)

| 法人 | 交易量 |  |  |  |  |  |  | 未平倉量 |  |  |  | 資料來源 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|  | **日盤多單** | **日盤空單** | **日盤淨** | **夜盤多單** | **夜盤空單** | **夜盤淨** | **淨變化 (日-夜)** | **OI多方** | **OI空方** | **OI淨** | **OI前日變化** |  |
| 外資 | 33,568 | 35,050 | -1,482 | 11,094 | 10,839 | +255 | -1,737 | 0 | 0 | +0 | +74,081 | TAIFEX Proxy |
| 投信 | 75 | 117 | -42 | 0 | 0 | +0 | -42 | 0 | 0 | +0 | -74,019 | TAIFEX Proxy |
| 自營商 | 3,128 | 3,234 | -106 | 441 | 368 | +73 | -179 | 0 | 0 | +0 | +3,354 | TAIFEX Proxy |
| 三大法人合計 | 36,771 | 38,401 | -1,630 | 11,535 | 11,207 | +328 | -1,958 | 0 | 0 | +0 | +3,416 | TAIFEX Proxy |

#### 7.3 前十大交易人日夜盤對照 (OI 無日夜拆分，列收盤後總量)

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 前十大交易人多方 OI | 80,066 | TAIFEX Proxy |
| 前十大交易人空方 OI | 69,303 | TAIFEX Proxy |
| 前十大交易人多空淨 OI | +10,763 | TAIFEX Proxy |
| 前十大交易人多空淨 OI 變化 | unavailable | 端點未提供 |

#### 7.4 夜盤劇本分類 (規則對應：夜盤漲跌 × 外資夜盤偏多空)

| 項目 | 數值 | 資料來源 |
|---|---|---|
| 夜盤成交量占比 (夜盤量／(夜盤量＋日盤量)) | 36.30% | TAIFEX Proxy |
| 夜盤漲跌點數 | +728 | TAIFEX Proxy |
| 外資夜盤多空淨交易量 | +255 | TAIFEX Proxy |
| 劇本分類 | 劇本一 | 規則對應 |
| 劇本條件 | 夜盤上漲＋外資偏多 | 規則對應 |
| 劇本特徵 | 開高、續漲機率高 | 規則對應 |

## 四、選擇權

**資料來源：** 主要 TAIFEX 經 Cloudflare Worker Proxy；時區 `Asia/Taipei`

### 1．選擇權交易日期、到期日與資料時間

| 項目 | 數值 | 資料來源 |
|---|---|---|
| 交易日期 | 2026-09-22 | TAIFEX Proxy |
| 到期月份／到期日 | 202609W4 | TAIFEX Proxy |
| 資料更新時間 | 2026-09-22 14:17:27 | 本機 |
| 日盤／夜盤標記 | 日盤收盤後資料 | TAIFEX Proxy |

### 2．Call 總成交量、OI、OI 增減

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Call 總成交量 | 115,764 | TAIFEX Proxy |
| Call 總未平倉量 OI | 30,570 | TAIFEX Proxy |
| Call OI 增減 | unavailable | 端點未提供 |

### 3．Put 總成交量、OI、OI 增減

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Put 總成交量 | 144,629 | TAIFEX Proxy |
| Put 總未平倉量 OI | 36,042 | TAIFEX Proxy |
| Put OI 增減 | unavailable | 端點未提供 |

### 4．Call／Put 比例與變化

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Call／Put 成交量比例 | 0.80 | TAIFEX Proxy |
| Call／Put 未平倉量比例 | 0.85 | TAIFEX Proxy |
| Put／Call Ratio | 1.18 | TAIFEX Proxy |
| Call／Put 比例變化 (量比 2026-09-18→2026-09-21) | 25.75 | TAIFEX OpenAPI |
| 與前一交易日比較 (OI 比 2026-09-18→2026-09-21) | 19.88 | TAIFEX OpenAPI |
**資料來源：** 比例 `TAIFEX Proxy chain`；變化 `TAIFEX OpenAPI PutCallRatio`

### 5．外資 Call／Put 部位

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 外資 Call 部位 (夜盤淨口數) | +25 | TAIFEX Proxy |
| 外資 Put 部位 (夜盤淨口數) | +372 | TAIFEX Proxy |
| 外資 Call／Put 淨部位 (日盤淨口數) | -3,098 | TAIFEX Proxy |
| 外資部位增減 (日盤淨 2026-09-21→2026-09-22) | -2,704 | TAIFEX Proxy snapshots (2026-09-21) |

### 6．自營商 Call／Put 部位

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 自營商 Call 部位 (夜盤淨口數) | -1,148 | TAIFEX Proxy |
| 自營商 Put 部位 (夜盤淨口數) | -1,464 | TAIFEX Proxy |
| 自營商 Call／Put 淨部位 (日盤淨口數) | -1,381 | TAIFEX Proxy |
| 自營商部位增減 (日盤淨 2026-09-21→2026-09-22) | -2,232 | TAIFEX Proxy snapshots (2026-09-21) |

### 7．主要 Call OI 集中區

| 項目 | 履約價 | OI | 資料來源 |
|---|---|---|---|
| Call OI 第1大履約價 | 48,500 | 1,485 | TAIFEX Proxy |
| Call OI 第2大履約價 | 48,000 | 1,336 | TAIFEX Proxy |
| Call OI 第3大履約價 | 47,500 | 1,163 | TAIFEX Proxy |
| Call OI 最大履約價 | 48,500 | 1,485 | TAIFEX Proxy |

#### Call OI 分布明細 Top10 (機器可讀，到期月份 202609W4)

| # | 履約價 | OI | 佔比 | 資料來源 |
|---|---|---|---|---|
| C1 | 48,500 | 1,485 | 4.86% | TAIFEX Proxy |
| C2 | 48,000 | 1,336 | 4.37% | TAIFEX Proxy |
| C3 | 47,500 | 1,163 | 3.8% | TAIFEX Proxy |
| C4 | 50,000 | 1,086 | 3.55% | TAIFEX Proxy |
| C5 | 48,600 | 1,062 | 3.47% | TAIFEX Proxy |
| C6 | 52,000 | 1,049 | 3.43% | TAIFEX Proxy |
| C7 | 50,500 | 985 | 3.22% | TAIFEX Proxy |
| C8 | 47,200 | 926 | 3.03% | TAIFEX Proxy |
| C9 | 46,900 | 912 | 2.98% | TAIFEX Proxy |
| C10 | 48,400 | 837 | 2.74% | TAIFEX Proxy |


### 8．主要 Put OI 集中區

| 項目 | 履約價 | OI | 資料來源 |
|---|---|---|---|
| Put OI 第1大履約價 | 47,000 | 1,760 | TAIFEX Proxy |
| Put OI 第2大履約價 | 46,000 | 1,507 | TAIFEX Proxy |
| Put OI 第3大履約價 | 45,000 | 1,419 | TAIFEX Proxy |
| Put OI 最大履約價 | 47,000 | 1,760 | TAIFEX Proxy |

#### Put OI 分布明細 Top10 (機器可讀，到期月份 202609W4)

| # | 履約價 | OI | 佔比 | 資料來源 |
|---|---|---|---|---|
| P1 | 47,000 | 1,760 | 4.88% | TAIFEX Proxy |
| P2 | 46,000 | 1,507 | 4.18% | TAIFEX Proxy |
| P3 | 45,000 | 1,419 | 3.94% | TAIFEX Proxy |
| P4 | 46,500 | 1,409 | 3.91% | TAIFEX Proxy |
| P5 | 46,400 | 1,316 | 3.65% | TAIFEX Proxy |
| P6 | 44,000 | 1,045 | 2.9% | TAIFEX Proxy |
| P7 | 46,600 | 985 | 2.73% | TAIFEX Proxy |
| P8 | 46,700 | 970 | 2.69% | TAIFEX Proxy |
| P9 | 46,800 | 931 | 2.58% | TAIFEX Proxy |
| P10 | 45,700 | 915 | 2.54% | TAIFEX Proxy |


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
| Call Wall 價位 | 48,500 | TAIFEX Proxy |
| 對應到期月份 | 202609W4 | TAIFEX Proxy |
| 與前一交易日的變化 | unavailable | 端點未提供 |

### 12．Put Wall

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Put Wall 價位 | 47,000 | TAIFEX Proxy |
| 對應到期月份 | 202609W4 | TAIFEX Proxy |
| 與前一交易日的變化 | unavailable | 端點未提供 |

### 13．Gamma Wall

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Gamma Wall 價位 | 48,000.00 | TAIFEX Proxy (options-market-structure-compact (proxy)) |
| 對應到期月份 | 202609W4 | TAIFEX Proxy |
| 資料日期 | 2026-09-21 | TAIFEX Proxy (options-market-structure-compact (proxy)) |

### 14．Gamma Flip

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Gamma Flip 價位 | 47,530.33 | TAIFEX Proxy (options-market-structure-compact (proxy)) |
| 對應到期月份 | 202609W4 | TAIFEX Proxy |
| 資料日期 | 2026-09-21 | TAIFEX Proxy (options-market-structure-compact (proxy)) |

### 15．Max Pain

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Max Pain 價位 | 47,000 | TAIFEX Proxy |
| 對應到期月份 | 202609W4 | TAIFEX Proxy |
| 與前一交易日的變化 | unavailable | 端點未提供 |

### 16．資料來源、時間、時區與狀態

- 資料來源：TAIFEX 經 Cloudflare Worker Proxy
- 資料日期：2026-09-22；資料時間：2026-09-22 14:17:27；時區：`Asia/Taipei`
- 日盤／夜盤標記：日盤收盤後 + 夜盤盤後
- 未取得欄位 (13)：otc_breadth.up, otc_breadth.down, otc_breadth.flat, otc_breadth.limit_up, otc_breadth.limit_down, margin.fin_yi, margin.fin_chg_yi, margin.ratio, sbl.sale_bal, sbl.sale_chg, turnover.otc, options.chain_oi_change, futures.top10_change
- 註記：Call/Put Wall 與 Max Pain 資料日期 2026-09-21 (T0 2026-09-22 端點不穩，採最新可得)
- 註記：Gamma 資料日期 2026-09-21 (T0 2026-09-22 尚無，上游 FMTQIK 落後，採最新可得)
- 註記：法人交易量變化無昨日交易端點，標 unavailable
- 註記：選擇權 chain 資料日期 2026-09-21 (T0 2026-09-22 端點不穩，採最新可得)
- 註記：Gamma Wall/Flip 資料日期 2026-09-21 (來源 options-market-structure-compact (proxy))

## 五、資料來源、時間與完整性

- 期貨/匯率為最新報價，其餘為 T0 收盤資料；時間皆為 `Asia/Taipei`。
- taiex：`twse-proxy`
- taiex_ohlc：`FinMind TaiwanStockPrice TAIEX`
- listed_breadth：`twse-proxy`
- listed_turnover：`twse-proxy market_statistics`
- institutional：`twse-proxy /institutional`
- margin_short：`TWSE MI_MARGN + TPEX margin_balance (張)`
- sbl：`TWSE TWT93U + TPEX margin_sbl`
- 期貨選擇權：`TAIFEX Proxy`
- 新聞：台股 Yahoo／國際 Fed＋CNBC＋MarketWatch；台股 Yahoo / 國際 Fed 公告＋CNBC＋MarketWatch RSS；Fed 無摘要；investing 港股為主已退役；cnyes CSR、wantgoo JS 算繪、中央社/央行路徑待查，未採用
- 美股/亞股/期貨/匯率/ADR/商品：`Yahoo Finance Chart API`；美債：`Yahoo Finance (備援)`
- 註記：上櫃 highlight 日期不符或缺值 (回傳 None, T0=1150922)
- 註記：三大法人回傳日期 20260921 (T0 20260922)，採用最新可得
- 註記：HiStock 未取得，融資餘額/增減標 unavailable (官方逐股加總僅有張數)
- 註記：融券沿用官方逐股加總 (張)
- 註記：融資維持率未取得 (wantgoo+istock 均失敗；官方無每日序列)
- 註記：上市 MI_MARGN / TWT96U 無日期欄，採用最新可得
- 本報告僅整理資料，不提供交易判斷。
