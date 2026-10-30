# DATA_REPORT_20261029

- 報告日期：`2026-10-30`
- T0 交易日期：`2026-10-29`
- 資料產出時間：`2026-10-30 08:45:09`
- 時區：`Asia/Taipei`
- 產出盤別：`全日`
- 產出者：`actions`
- 排定班別：`manual`

---

## 一、現貨

### 1. 台股大盤行情

**資料來源：** `Cloudflare Worker：twse-proxy` (備援 `TWSE OpenAPI MI_INDEX`)

| 項目 | 數值 | 單位 | 資料來源 |
|---|---|---|---|
| 加權指數 | 46,368.33 | 點 | twse-proxy |
| 開盤 | 47,014.87 | 點 | FinMind TaiwanStockPrice TAIEX |
| 最高 | 47,015.45 | 點 | FinMind TaiwanStockPrice TAIEX |
| 最低 | 46,055.07 | 點 | FinMind TaiwanStockPrice TAIEX |
| 收盤 | 46,368.33 | 點 | twse-proxy |
| 漲跌點數 | -667.25 | 點 | twse-proxy |
| 漲跌幅 | -1.42 | % | twse-proxy |
| 成交金額 | 8,238.1 | 億元 | twse-proxy market_statistics |

### 2. 市場漲跌家數

#### 2.1 上市公司

**資料來源：** `Cloudflare Worker：twse-proxy` (備援 `TWSE OpenAPI twtazu_od`)

| 項目 | 家數 | 資料來源 |
|---|---|---|
| 上漲家數 | 232 | twse-proxy |
| 下跌家數 | 737 | twse-proxy |
| 平盤家數 | 108 | twse-proxy |
| 漲停家數 | 7 | twse-proxy |
| 跌停家數 | 3 | twse-proxy |

#### 2.2 上櫃公司

**資料來源：** `TPEX OpenAPI tpex_mainborad_highlight`

| 項目 | 家數 | 資料來源 |
|---|---|---|
| 上漲家數 | 195 | TPEX OpenAPI tpex_mainborad_highlight |
| 下跌家數 | 598 | TPEX OpenAPI tpex_mainborad_highlight |
| 平盤家數 | 75 | TPEX OpenAPI tpex_mainborad_highlight |
| 漲停家數 | 15 | TPEX OpenAPI tpex_mainborad_highlight |
| 跌停家數 | 1 | TPEX OpenAPI tpex_mainborad_highlight |

### 3. 三大法人現貨買賣超

**資料來源：** `TWSE RWD BFI82U`

| 法人別 | 買賣超金額 | 單位 | 資料來源 |
|---|---|---|---|
| 外資 | -688.2 | 億元 | twse-proxy /institutional |
| 投信 | +70.4 | 億元 | twse-proxy /institutional |
| 自營商 | -215.0 | 億元 | twse-proxy /institutional |
| 三大法人合計 | -832.7 | 億元 | twse-proxy /institutional |

### 4. 融資融券

**資料來源：** 上市+上櫃 `HiStock` (金額口徑)；維持率 `istock.tw`；備援官方逐股加總

| 項目 | 數值 | 單位 | 資料來源 |
|---|---|---|---|
| 融資餘額 | 8,438.7 | 億元 | HiStock 上市+上櫃融資融券 (金額口徑) |
| 融資增減 | +3.3 | 億元 | HiStock 上市+上櫃融資融券 (金額口徑) |
| 融券餘額 | 226,453 | 張 | HiStock 上市+上櫃融資融券 (金額口徑) |
| 融券增減 | -6,513 | 張 | HiStock 上市+上櫃融資融券 (金額口徑) |
| 融資維持率 | 178.40 | % | stockintelli 大盤融資維持率 (民間估算；官方無每日序列) |

### 5. 借券資料

**資料來源：** 上市 `TWSE OpenAPI TWT96U` (可借餘額)、上櫃 `TPEX OpenAPI tpex_margin_sbl`

| 項目 | 數值 | 單位 | 資料來源 |
|---|---|---|---|
| 借券餘額 | 4,627,918 | 張 | TWSE TWT93U + TPEX margin_sbl |
| 借券賣出餘額 | 37,451 | 張 | TWSE TWT93U + TPEX margin_sbl |
| 借券賣出增減 | -2,475 | 張 | TWSE TWT93U + TPEX margin_sbl |

### 6. 市場成交結構

**資料來源：** 上市 `twse-proxy market_statistics`、上櫃 `TPEX OpenAPI tpex_mainborad_highlight`

| 項目 | 成交金額 | 單位 | 資料來源 |
|---|---|---|---|
| 上市成交金額 | 8,238.1 | 億元 | twse-proxy market_statistics |
| 上櫃成交金額 | 2,084.2 | 億元 | TPEX OpenAPI tpex_mainborad_highlight |
| 上市櫃成交金額合計 | 10,322.3 | 億元 | twse-proxy market_statistics+TPEX OpenAPI tpex_mainborad_highlight |

## 二、重要市場

### 1. 美股指數

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 收盤／最新值 | 漲跌點 | 漲跌幅 | 資料來源 |
|---|---|---|---|---|---|
| S&P 500 | ^GSPC | 7,720.39 | -23.59 | -0.30 | Yahoo Finance Chart API |
| Nasdaq Composite | ^IXIC | 26,184.72 | -365.12 | -1.38 | Yahoo Finance Chart API |
| Nasdaq 100 | ^NDX | 29,402.51 | -410.65 | -1.38 | Yahoo Finance Chart API |
| Dow Jones | ^DJI | 52,342.56 | -132.54 | -0.25 | Yahoo Finance Chart API |
| 費城半導體 SOX | ^SOX | 11,518.20 | -165.80 | -1.42 | Yahoo Finance Chart API |
| VIX | ^VIX | 17.20 | 0.29 | +1.71 | Yahoo Finance Chart API |

### 2. 亞洲主要指數

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 收盤／最新值 | 漲跌點 | 漲跌幅 | 資料來源 |
|---|---|---|---|---|---|
| 日經225 | ^N225 | 63,650.45 | -303.74 | -0.47 | Yahoo Finance Chart API |
| 韓國KOSPI | ^KS11 | 5,726.35 | -286.09 | -4.76 | Yahoo Finance Chart API |
| 香港恆生 | ^HSI | 23,094.83 | 53.51 | +0.23 | Yahoo Finance Chart API |
| 上海綜合 | 000001.SS | 3,681.47 | 33.17 | +0.91 | Yahoo Finance Chart API |
| 深圳成分 | 399001.SZ | 11,473.18 | 227.45 | +2.02 | Yahoo Finance Chart API |

### 3. 美股指數期貨

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 最新值 | 漲跌點 | 漲跌幅 | 資料來源 |
|---|---|---|---|---|---|
| S&P500期貨 | ES=F | 7,701.25 | -82.00 | -1.05 | Yahoo Finance Chart API |
| Nasdaq100期貨 | NQ=F | 29,059.75 | -919.75 | -3.07 | Yahoo Finance Chart API |
| 道瓊期貨 | YM=F | 52,564.00 | -132.00 | -0.25 | Yahoo Finance Chart API |
| Russell2000期貨 | RTY=F | 2,867.90 | 28.40 | +1.00 | Yahoo Finance Chart API |

### 4. 美國國債殖利率

**資料來源：** `U.S. Treasury Fiscal Data API` (失敗時備援 Treasury yield.xml 與 `Yahoo Finance`)

| 項目 | API 資料欄位／識別 | 殖利率 | 日變化 | 資料來源 |
|---|---|---|---|---|
| 美國 2 年期殖利率 | 2 Yr | 4.61 | -0.06 | U.S. Treasury yield.xml (網頁備援) |
| 美國 10 年期殖利率 | 10 Yr | 4.99 | -0.06 | Yahoo Finance (備援) |
| 美國 30 年期殖利率 | 30 Yr | 5.33 | -0.03 | Yahoo Finance (備援) |

### 5. 主要匯率

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 最新值 | 漲跌點 | 漲跌幅 | 資料來源 |
|---|---|---|---|---|---|
| USD/TWD | TWD=X | 32.54 | 0.16 | +0.50 | Yahoo Finance Chart API |
| DXY美元指數 | DX-Y.NYB | 101.85 | -0.34 | -0.34 | Yahoo Finance Chart API |
| USD/JPY | JPY=X | 157.51 | -0.32 | -0.21 | Yahoo Finance Chart API |
| USD/KRW | KRW=X | 1,338.58 | -1.76 | -0.13 | Yahoo Finance Chart API |

### 6. 台灣相關ADR

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 收盤／最新值 | 漲跌點 | 漲跌幅 | 資料來源 |
|---|---|---|---|---|---|
| 台積電ADR | TSM | 439.51 | 2.64 | +0.60 | Yahoo Finance Chart API |
| 聯電ADR | UMC | 18.82 | -0.63 | -3.24 | Yahoo Finance Chart API |
| 日月光ADR | ASX | 43.92 | 1.86 | +4.42 | Yahoo Finance Chart API |

### 7. 原油黃金Bitcoin

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 收盤／最新值 | 漲跌點 | 漲跌幅 | 資料來源 |
|---|---|---|---|---|---|
| WTI原油期貨 | CL=F | 102.69 | -0.09 | -0.09 | Yahoo Finance Chart API |
| 黃金期貨 | GC=F | 4,018.40 | -33.20 | -0.82 | Yahoo Finance Chart API |
| Bitcoin | BTC-USD | 76,931.58 | -4,336.01 | -5.34 | Yahoo Finance Chart API |

### 8. 重大經濟數據、央行事件與重大市場新聞

**資料來源：** 台股 `tw.stock.yahoo.com` (含內文摘要)；國際 `Fed 公告 RSS`＋`CNBC`＋`MarketWatch` (標題、來源、時間與連結)

- 事件1：威剛前3季淨利超過25年總和 董座：DRAM缺貨將更嚴重
  - 來源：Yahoo 台股；發布時間：2026-10-29T17:31:49Z；台北時間：2026-10-30 01:31
  - 摘要：記憶體景氣轉強，威剛科技（3260）前3季獲利寫下成立以來新紀錄。威剛今（29）日公布第三季財報，單季歸屬母公司業主淨利達126.1億元，EPS 38.69元，雙雙改寫單季新高；累計前三季EPS更達101.47元、首度突破百元，稅後淨利33
  - 原文連結：https://tw.stock.yahoo.com/news/%E5%A8%81%E5%89%9B%E5%89%8D3%E5%AD%A3eps%E7%AA%81%E7%A0%B4%E7%99%BE%E5%85%83-q3%E6%AF%8F%E8%82%A1%E8%B3%BA38-69%E5%85%83%E5%86%8D%E5%89%B5%E6%96%B0%E9%AB%98-%E9%99%B3%E7%AB%8B%E7%99%BD-2027%E5%B9%B4dram%E7%BC%BA%E8%B2%A8%E6%9B%B4%E5%9A%B4%E9%87%8D-173149322.html
- 事件2：國巨第三季淨利成長近9成 決議不分派上半年盈餘
  - 來源：Yahoo 台股；發布時間：2026-10-29T23:13:18Z；台北時間：2026-10-30 07:13
  - 摘要：國巨第三季營運來自於 AI 相關應用需求的強勁動能，單季營收創歷史新高。
  - 原文連結：https://tw.stock.yahoo.com/news/%E5%9C%8B%E5%B7%A8q3%E5%96%AE%E5%AD%A3%E7%87%9F%E6%94%B6495-32%E5%84%84%E6%AD%B7%E5%8F%B2%E6%96%B0%E9%AB%98-%E5%89%8D%E4%B8%89%E5%AD%A3eps%E9%81%9414-32%E5%85%83-%E4%BD%86%E4%B8%8D%E5%88%86%E6%B4%BE%E4%B8%8A%E5%8D%8A%E5%B9%B4%E5%BA%A6%E7%9B%88%E9%A4%98-231318456.html
- 事件3：美股受創 Alphabet瀉12%、Marvell跌逾13%
  - 來源：Yahoo 台股；發布時間：2026-10-29T21:30:08Z；台北時間：2026-10-30 05:30
  - 摘要：美股週四收黑，那指、費半跌逾1%，Marvell暴跌逾13%；開拓重工也創2020年3月以來最差日 Alphabet 第三季財報失色，營收與EPS不如預期，自由現金流連續2季陷入負值，股價暴跌逾12% 美國Q3經濟創一年最快，9月PCE月增
  - 原文連結：https://tw.stock.yahoo.com/news/%E7%BE%8E%E8%82%A1%E7%9B%A4%E5%BE%8C-alphabet%E7%8B%82%E7%80%8912-marvell%E6%9A%B4%E8%B7%8C%E9%80%BE13-%E6%8B%96%E7%B4%AF%E9%82%A3%E6%8C%87%E8%B2%BB%E5%8D%8A-%E6%A8%99%E6%99%AE%E7%B5%82%E6%AD%A2%E9%80%A3%E4%B8%89%E7%B4%85-213008863.html
- 事件4：華碩傳將結束手機業務 庫存賣光、已無通訊行報價
  - 來源：Yahoo 台股；發布時間：2026-10-29T22:47:29Z；台北時間：2026-10-30 06:47
  - 摘要：PC品牌大廠華碩今年初證實，2026年暫無推出手機新機種的計畫，如今市場傳出，華碩手機庫存到了第4季已幾乎銷售一空，上周已無通訊行提供報價，顯示現貨已經售罄，產品走入下市階段。
  - 原文連結：https://tw.stock.yahoo.com/news/%E8%8F%AF%E7%A2%A9%E5%82%B3%E5%8F%AF%E8%83%BD%E7%B5%90%E6%9D%9F%E6%89%8B%E6%A9%9F%E6%A5%AD%E5%8B%99-%E7%8F%BE%E6%9C%89%E7%94%A2%E5%93%81%E7%B4%9B%E4%B8%8B%E5%B8%82-%E5%B7%B2%E7%84%A1%E9%80%9A%E8%A8%8A%E8%A1%8C%E6%8F%90%E4%BE%9B%E5%A0%B1%E5%83%B9-224729577.html
- 事件5：momo併購foodpanda？總座回應
  - 來源：Yahoo 台股；發布時間：2026-10-29T09:08:48Z；台北時間：2026-10-29 17:08
  - 摘要：隨著Grab併購foodpanda台灣案遭公平會否決，外界關注是否有其他業者接手。電商龍頭momo富邦媒（8454）總經理谷元宏今（29）日出席雙11記者會，會後被問及是否考慮併購foodpanda時表示，公司過去確實曾評估相關機會，目前仍
  - 原文連結：https://tw.stock.yahoo.com/news/momo%E6%9C%89%E6%84%8F%E4%BD%B5%E8%B3%BCfoodpanda%EF%BC%9F%E7%B8%BD%E5%BA%A7%EF%BC%9A%E4%B8%8D%E6%8E%92%E9%99%A4%E4%BB%BB%E4%BD%95%E6%A9%9F%E6%9C%83-%E7%9C%8B%E9%87%8D%E6%A5%AD%E5%8B%99%E7%B6%9C%E6%95%88-090848544.html
- 事件6：連8紅、漲逾47%登強勢股王 誠美材上季仍虧損
  - 來源：Yahoo 台股；發布時間：2026-10-30T00:00:00Z；台北時間：2026-10-30 08:00
  - 摘要：[FTNN新聞網]記者黃詩雯／綜合報導台股加權指數29日收盤46,368.33點，跌667.25點，跌幅1.42%，觀察昨日強勢個股表現，偏光板廠誠美材（4960）連續8個交易日收...
  - 原文連結：https://tw.stock.yahoo.com/news/%E8%82%A1%E5%83%B9%E9%80%A38%E7%B4%85-%E7%8B%82%E9%A3%8647-68-%E7%99%BB%E5%BC%B7%E5%8B%A2%E8%82%A1%E7%8E%8B-%E5%81%8F%E5%85%89%E6%9D%BF%E5%BB%A0-000000273.html
- 事件7：Federal Reserve Board announces approval of application by The Bank of Nova Scotia
  - 來源：Federal Reserve；發布時間：Thu, 29 Oct 2026 20:30:00 GMT；台北時間：2026-10-30 04:30
  - 摘要：Federal Reserve Board announces approval of application by The Bank of Nova Scotia
  - 原文連結：https://www.federalreserve.gov/newsevents/pressreleases/orders20261029a.htm
- 事件8：Federal Reserve issues FOMC statement
  - 來源：Federal Reserve；發布時間：Wed, 28 Oct 2026 18:00:00 GMT；台北時間：2026-10-29 02:00
  - 摘要：Federal Reserve issues FOMC statement
  - 原文連結：https://www.federalreserve.gov/newsevents/pressreleases/monetary20261028a.htm
- 事件9：Third-quarter U.S. GDP increases a better-than-expected 3.4% as September inflation accelerates
  - 來源：CNBC；發布時間：Thu, 29 Oct 2026 18:06:31 GMT；台北時間：2026-10-30 02:06
  - 摘要：The personal consumption expenditures price index was projected to increase 0.5% in September for an annual rate of 3.7%, according to the Dow Jones c
  - 原文連結：https://www.cnbc.com/2026/10/29/pce-inflation-report-september-2026-.html
- 事件10：The politics of President Lagarde's European Central Bank early exit  — and who could replace her
  - 來源：CNBC；發布時間：Thu, 29 Oct 2026 14:53:06 GMT；台北時間：2026-10-29 22:53
  - 摘要：European Central Bank President Christine Lagarde will step down on Feb. 7 next year, she announced Thursday.
  - 原文連結：https://www.cnbc.com/2026/10/29/lagarde-ecb-stand-down.html
- 事件11：European Central Bank keeps key interest rate on hold at 2.5%
  - 來源：CNBC；發布時間：Thu, 29 Oct 2026 14:48:01 GMT；台北時間：2026-10-29 22:48
  - 摘要：Markets saw the decision as a hawkish pause and were last pricing in a 67% chance of a December rate hike.
  - 原文連結：https://www.cnbc.com/2026/10/29/european-central-bank-interest-rates.html
- 事件12：Our church has a $1.5 million bequest earning 3.75% in a bank account. Is inflation eroding it?
  - 來源：MarketWatch；發布時間：Fri, 30 Oct 2026 00:05:00 GMT；台北時間：2026-10-30 08:05
  - 摘要：&#x201c;Given the size and long-term nature of this gift, we want to make sure the funds are managed prudently.&#x201d;
  - 原文連結：https://www.marketwatch.com/story/there-may-be-better-investment-options-my-church-received-1-5-million-from-a-parishioner-is-3-75-interest-enough-5164d790?mod=mw_rss_topstories


## 三、期貨

**資料來源：**
1. Cloudflare Workers：TAIFEX Proxy — https://taifex.grichtoyang.workers.dev/
2. TAIFEX Open API — https://openapi.taifex.com.tw/

近月契約月份：202611 (日盤成交量最大者)；交易日期：2026-10-29

### 1．台指期近月日盤行情

| 項目 | 數值 | 資料來源 |
|---|---|---|
| 開盤價 | 47,187 | TAIFEX Proxy |
| 最高價 | 47,218 | TAIFEX Proxy |
| 最低價 | 46,310 | TAIFEX Proxy |
| 收盤價 | 46,577 | TAIFEX Proxy |
| 漲跌點數 | -672 | TAIFEX Proxy |
| 漲跌幅 | -1.42 | TAIFEX Proxy |
| 成交量 | 56,666 | TAIFEX Proxy |
| 日盤高點及低點 | 47,218 / 46,310 | TAIFEX Proxy |

### 2．台指期近月夜盤行情

| 項目 | 數值 | 資料來源 |
|---|---|---|
| 開盤價 | 46,400 | TAIFEX Proxy |
| 最高價 | 46,637 | TAIFEX Proxy |
| 最低價 | 45,850 | TAIFEX Proxy |
| 收盤價 | 45,926 | TAIFEX Proxy |
| 漲跌點數 | -643 | TAIFEX Proxy |
| 漲跌幅 | -1.38 | TAIFEX Proxy |
| 成交量 | 34,357 | TAIFEX Proxy |
| 夜盤高點及低點 | 46,637 / 45,850 | TAIFEX Proxy |
| 結算價 | unavailable | TAIFEX Proxy |
| 未平倉量 | unavailable | TAIFEX Proxy |

### 3．法人台指期多空未平倉部位

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 外資多方 OI | 8,362 | TAIFEX Proxy |
| 外資空方 OI | 97,884 | TAIFEX Proxy |
| 外資多空淨 OI | -89,522 | TAIFEX Proxy |
| 投信多方 OI | 89,920 | TAIFEX Proxy |
| 投信空方 OI | 2,702 | TAIFEX Proxy |
| 投信多空淨 OI | +87,218 | TAIFEX Proxy |
| 自營商多方 OI | 5,606 | TAIFEX Proxy |
| 自營商空方 OI | 4,095 | TAIFEX Proxy |
| 自營商多空淨 OI | +1,511 | TAIFEX Proxy |
| 三大法人合計多方 OI | 103,888 | TAIFEX Proxy |
| 三大法人合計空方 OI | 104,681 | TAIFEX Proxy |
| 三大法人合計多空淨 OI | -793 | TAIFEX Proxy |
| 外資多空淨 OI 變化 | -4,605 | TAIFEX Proxy |
| 投信多空淨 OI 變化 | +39 | TAIFEX Proxy |
| 自營商多空淨 OI 變化 | +1,028 | TAIFEX Proxy |

### 4．前十大交易人多空未平倉部位

**資料來源：** `TAIFEX OpenAPI OpenInterestOfLargeTradersFutures` (官方資料落後約一日，標示實際日期)

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 前十大交易人多方 OI | 92,810 | TAIFEX Proxy |
| 前十大交易人空方 OI | 81,120 | TAIFEX Proxy |
| 前十大交易人多空淨 OI | +11,690 | TAIFEX Proxy |
| 多空淨 OI 變化 (2026-10-27→2026-10-29) | +888 | TAIFEX Proxy snapshots (2026-10-28) |
- 資料日期：2026-10-29 (TypeOfTraders=0 全部交易人；契約月份 202611)

### 5．日盤、夜盤法人交易資料

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 外資日盤多單交易量 | 48,741 | TAIFEX Proxy |
| 外資日盤空單交易量 | 53,346 | TAIFEX Proxy |
| 外資日盤多空淨交易量 | -4,605 | TAIFEX Proxy |
| 外資夜盤多單交易量 | 19,301 | TAIFEX Proxy |
| 外資夜盤空單交易量 | 18,842 | TAIFEX Proxy |
| 外資夜盤多空淨交易量 | +459 | TAIFEX Proxy |
| 外資日盤／夜盤交易量變化 | -5,064 | TAIFEX Proxy |
| 投信日盤多空淨交易量 | +39 | TAIFEX Proxy |
| 投信夜盤多空淨交易量 | +0 | TAIFEX Proxy |
| 投信日盤／夜盤交易量變化 | +39 | TAIFEX Proxy |
| 自營商日盤多空淨交易量 | +992 | TAIFEX Proxy |
| 自營商夜盤多空淨交易量 | -5 | TAIFEX Proxy |
| 自營商日盤／夜盤交易量變化 | +997 | TAIFEX Proxy |
| 三大法人日盤多空淨交易量 | -3,574 | TAIFEX Proxy |
| 三大法人夜盤多空淨交易量 | +454 | TAIFEX Proxy |
| 法人日盤交易金額淨額 (億元) | -335.0 | TAIFEX Proxy |
| 法人夜盤交易金額淨額 (億元) | +42.1 | TAIFEX Proxy |

### 6．期貨與現貨關係

| 項目 | 數值 | 資料來源 |
|---|---|---|
| 台指期近月價格 | 46,577 | TAIFEX Proxy |
| 加權指數價格 | 46,368.33 | twse-proxy |
| 台指期與加權指數價差 | +208.67 | TAIFEX Proxy+twse-proxy |
| 價差百分比 | +0.45 | TAIFEX Proxy+twse-proxy |
| 日盤基差 | +208.67 | TAIFEX Proxy+twse-proxy |
| 夜盤價格相對日盤收盤的變化 | -651 | TAIFEX Proxy |

### 7．日盤、夜盤與籌碼變化對照

#### 7.1 日夜盤價格與成交量對照 (變化 = 日盤 - 夜盤)

| 項目 | 日盤 | 夜盤 | 變化 (日-夜) | 資料來源 |
|---|---|---|---|---|
| 收盤價 | 46,577 | 45,926 | +651 | TAIFEX Proxy |
| 成交量 | 56,666 | 34,357 | +22,309 | TAIFEX Proxy |
- 台指期總 OI 前日變化：-3,538（來源：TAIFEX Proxy）


#### 7.2 法人籌碼日夜盤對照 (淨變化 = 日盤淨 - 夜盤淨；OI 為日盤收盤後總量，前日變化另列)

| 法人 | 交易量 |  |  |  |  |  |  | 未平倉量 |  |  |  | 資料來源 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|  | **日盤多單** | **日盤空單** | **日盤淨** | **夜盤多單** | **夜盤空單** | **夜盤淨** | **淨變化 (日-夜)** | **OI多方** | **OI空方** | **OI淨** | **OI前日變化** |  |
| 外資 | 48,741 | 53,346 | -4,605 | 19,301 | 18,842 | +459 | -5,064 | 8,362 | 97,884 | -89,522 | -4,605 | TAIFEX Proxy |
| 投信 | 578 | 539 | +39 | 0 | 0 | +0 | +39 | 89,920 | 2,702 | +87,218 | +39 | TAIFEX Proxy |
| 自營商 | 5,353 | 4,361 | +992 | 877 | 882 | -5 | +997 | 5,606 | 4,095 | +1,511 | +1,028 | TAIFEX Proxy |
| 三大法人合計 | 54,672 | 58,246 | -3,574 | 20,178 | 19,724 | +454 | -4,028 | 103,888 | 104,681 | -793 | -3,538 | TAIFEX Proxy |

#### 7.3 前十大交易人日夜盤對照 (OI 無日夜拆分，列收盤後總量)

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 前十大交易人多方 OI | 92,810 | TAIFEX Proxy |
| 前十大交易人空方 OI | 81,120 | TAIFEX Proxy |
| 前十大交易人多空淨 OI | +11,690 | TAIFEX Proxy |
| 前十大交易人多空淨 OI 變化 (2026-10-27→2026-10-29) | +888 | TAIFEX Proxy snapshots (2026-10-28) |

#### 7.4 夜盤劇本分類 (規則對應：夜盤漲跌 × 外資夜盤偏多空)

| 項目 | 數值 | 資料來源 |
|---|---|---|
| 夜盤成交量占比 (夜盤量／(夜盤量＋日盤量)) | 37.75% | TAIFEX Proxy |
| 夜盤漲跌點數 | -643 | TAIFEX Proxy |
| 外資夜盤多空淨交易量 | +459 | TAIFEX Proxy |
| 劇本分類 | 劇本四 | 規則對應 |
| 劇本條件 | 夜盤下跌＋外資偏多 | 規則對應 |
| 劇本特徵 | 先跌、開低反彈 | 規則對應 |

## 四、選擇權

**資料來源：** 主要 TAIFEX 經 Cloudflare Worker Proxy；時區 `Asia/Taipei`

### 1．選擇權交易日期、到期日與資料時間

| 項目 | 數值 | 資料來源 |
|---|---|---|
| 交易日期 | 2026-10-29 | TAIFEX Proxy |
| 到期月份／到期日 | 202610F5 | TAIFEX Proxy |
| 資料更新時間 | 2026-10-30 08:45:09 | 本機 |
| 日盤／夜盤標記 | 日盤收盤後資料 | TAIFEX Proxy |

### 2．Call 總成交量、OI、OI 增減

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Call 總成交量 | 197,738 | TAIFEX Proxy |
| Call 總未平倉量 OI | 62,516 | TAIFEX Proxy |
| Call OI 增減 | unavailable | 端點未提供 |

### 3．Put 總成交量、OI、OI 增減

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Put 總成交量 | 159,516 | TAIFEX Proxy |
| Put 總未平倉量 OI | 35,052 | TAIFEX Proxy |
| Put OI 增減 | unavailable | 端點未提供 |

### 4．Call／Put 比例與變化

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Call／Put 成交量比例 | 1.24 | TAIFEX Proxy |
| Call／Put 未平倉量比例 | 1.78 | TAIFEX Proxy |
| Put／Call Ratio | 0.56 | TAIFEX Proxy |
| Call／Put 比例變化 (量比 2026-10-28→2026-10-29) | -11.33 | TAIFEX Proxy |
| 與前一交易日比較 (OI 比 2026-10-28→2026-10-29) | -4.92 | TAIFEX Proxy |
**資料來源：** 比例 `TAIFEX Proxy chain`；變化 `TAIFEX Proxy PutCallRatio`

### 5．外資 Call／Put 部位

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 外資 Call日買 | 48,121 | TAIFEX Proxy |
| 外資 Call日賣 | 48,611 | TAIFEX Proxy |
| 外資 Call日淨 | -490 | TAIFEX Proxy |
| 外資 Put日買 | 54,731 | TAIFEX Proxy |
| 外資 Put日賣 | 54,418 | TAIFEX Proxy |
| 外資 Put日淨 | +313 | TAIFEX Proxy |
| 外資 Call夜買 | 38,791 | TAIFEX Proxy |
| 外資 Call夜賣 | 38,648 | TAIFEX Proxy |
| 外資 Call夜淨 | +143 | TAIFEX Proxy |
| 外資 Put夜買 | 46,616 | TAIFEX Proxy |
| 外資 Put夜賣 | 46,506 | TAIFEX Proxy |
| 外資 Put夜淨 | +110 | TAIFEX Proxy |
| 外資 日盤淨總量 | -803 | TAIFEX Proxy |
| 外資 Call日夜淨增減 (日－夜) | -633 | TAIFEX Proxy |
| 外資 Put日夜淨增減 (日－夜) | +203 | TAIFEX Proxy |

### 6．自營商 Call／Put 部位

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 自營商 Call日買 | 61,592 | TAIFEX Proxy |
| 自營商 Call日賣 | 67,754 | TAIFEX Proxy |
| 自營商 Call日淨 | -6,162 | TAIFEX Proxy |
| 自營商 Put日買 | 45,946 | TAIFEX Proxy |
| 自營商 Put日賣 | 45,783 | TAIFEX Proxy |
| 自營商 Put日淨 | +163 | TAIFEX Proxy |
| 自營商 Call夜買 | 27,222 | TAIFEX Proxy |
| 自營商 Call夜賣 | 28,359 | TAIFEX Proxy |
| 自營商 Call夜淨 | -1,137 | TAIFEX Proxy |
| 自營商 Put夜買 | 25,797 | TAIFEX Proxy |
| 自營商 Put夜賣 | 24,669 | TAIFEX Proxy |
| 自營商 Put夜淨 | +1,128 | TAIFEX Proxy |
| 自營商 日盤淨總量 | -6,325 | TAIFEX Proxy |
| 自營商 Call日夜淨增減 (日－夜) | -5,025 | TAIFEX Proxy |
| 自營商 Put日夜淨增減 (日－夜) | -965 | TAIFEX Proxy |

### 7．主要 Call OI 集中區

| 項目 | 履約價 | OI | 資料來源 |
|---|---|---|---|
| Call OI 第1大履約價 | 48,500 | 4,246 | TAIFEX Proxy |
| Call OI 第2大履約價 | 49,200 | 3,912 | TAIFEX Proxy |
| Call OI 第3大履約價 | 47,000 | 2,685 | TAIFEX Proxy |
| Call OI 最大履約價 | 48,500 | 4,246 | TAIFEX Proxy |

#### Call OI 分布明細 Top10 (機器可讀，到期月份 202610F5)

| # | 履約價 | OI | 佔比 | 資料來源 |
|---|---|---|---|---|
| C1 | 48,500 | 4,246 | 6.79% | TAIFEX Proxy |
| C2 | 49,200 | 3,912 | 6.26% | TAIFEX Proxy |
| C3 | 47,000 | 2,685 | 4.29% | TAIFEX Proxy |
| C4 | 46,300 | 1,948 | 3.12% | TAIFEX Proxy |
| C5 | 46,600 | 1,876 | 3.0% | TAIFEX Proxy |
| C6 | 47,500 | 1,799 | 2.88% | TAIFEX Proxy |
| C7 | 48,000 | 1,643 | 2.63% | TAIFEX Proxy |
| C8 | 46,800 | 1,604 | 2.57% | TAIFEX Proxy |
| C9 | 48,200 | 1,555 | 2.49% | TAIFEX Proxy |
| C10 | 47,300 | 1,533 | 2.45% | TAIFEX Proxy |


### 8．主要 Put OI 集中區

| 項目 | 履約價 | OI | 資料來源 |
|---|---|---|---|
| Put OI 第1大履約價 | 46,000 | 2,822 | TAIFEX Proxy |
| Put OI 第2大履約價 | 45,000 | 2,366 | TAIFEX Proxy |
| Put OI 第3大履約價 | 45,500 | 1,826 | TAIFEX Proxy |
| Put OI 最大履約價 | 46,000 | 2,822 | TAIFEX Proxy |

#### Put OI 分布明細 Top10 (機器可讀，到期月份 202610F5)

| # | 履約價 | OI | 佔比 | 資料來源 |
|---|---|---|---|---|
| P1 | 46,000 | 2,822 | 8.05% | TAIFEX Proxy |
| P2 | 45,000 | 2,366 | 6.75% | TAIFEX Proxy |
| P3 | 45,500 | 1,826 | 5.21% | TAIFEX Proxy |
| P4 | 45,600 | 1,446 | 4.13% | TAIFEX Proxy |
| P5 | 45,700 | 1,360 | 3.88% | TAIFEX Proxy |
| P6 | 45,800 | 1,308 | 3.73% | TAIFEX Proxy |
| P7 | 45,900 | 1,304 | 3.72% | TAIFEX Proxy |
| P8 | 46,500 | 1,160 | 3.31% | TAIFEX Proxy |
| P9 | 46,200 | 1,118 | 3.19% | TAIFEX Proxy |
| P10 | 45,400 | 1,048 | 2.99% | TAIFEX Proxy |


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
| 對應到期月份 | 202610F5 | TAIFEX Proxy |
| 與前一交易日的變化 | unavailable | 端點未提供 |

### 12．Put Wall

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Put Wall 價位 | 46,000 | TAIFEX Proxy |
| 對應到期月份 | 202610F5 | TAIFEX Proxy |
| 與前一交易日的變化 | unavailable | 端點未提供 |

### 13．Gamma Wall

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Gamma Wall 價位 | 46,300.00 | TAIFEX Proxy (options-market-structure-compact (proxy)) |
| 對應到期月份 | 202610F5 | TAIFEX Proxy |
| 資料日期 | 2026-10-29 | TAIFEX Proxy (options-market-structure-compact (proxy)) |

### 14．Gamma Flip

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Gamma Flip 價位 | 46,131.40 | TAIFEX Proxy (options-market-structure-compact (proxy)) |
| 對應到期月份 | 202610F5 | TAIFEX Proxy |
| 資料日期 | 2026-10-29 | TAIFEX Proxy (options-market-structure-compact (proxy)) |

### 15．Max Pain

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Max Pain 價位 | 46,000 | TAIFEX Proxy |
| 對應到期月份 | 202610F5 | TAIFEX Proxy |
| 與前一交易日的變化 | unavailable | 端點未提供 |

### 17．選擇權法人日盤、夜盤交易

| 法人 | 日盤多單 | 日盤空單 | 日盤淨 | 夜盤多單 | 夜盤空單 | 夜盤淨 | 淨變化 (日-夜) | 資料來源 |
|---|---|---|---|---|---|---|---|---|
| 外資 | 102,539 | 103,342 | -803 | 85,297 | 85,264 | +33 | -836 | TAIFEX Proxy |
| 投信 | 0 | 2,776 | -2,776 | 0 | 0 | +0 | -2,776 | TAIFEX Proxy |
| 自營商 | 107,375 | 113,700 | -6,325 | 51,891 | 54,156 | -2,265 | -4,060 | TAIFEX Proxy |
| 三大法人合計 | 209,914 | 219,818 | -9,904 | 137,188 | 139,420 | -2,232 | -7,672 | TAIFEX Proxy |
- 方法論：多方＝買Call＋賣Put（看多），空方＝賣Call＋買Put（看空），淨額＝看多－看空（已用 Call／Put 拆分頁交叉驗算一致）
- 公式：多方(買)－空方(賣)＝（買call＋賣put）－（賣call＋買put）＝看多－看空
- 速記：多＝BC＋SP、空＝SC＋BP

#### 法人多空力道表（金額・億元；上游千元／1e5）

| 法人 | 日多方力道 | 日空方力道 | 日淨多空力道 | 夜多方力道 | 夜空方力道 | 夜淨多空力道 | 日淨－夜淨 | 資料來源 |
|---|---|---|---|---|---|---|---|---|
| 外資 | 9.19 | 9.33 | -0.14 | 5.96 | 6.00 | -0.04 | -0.10 | TAIFEX Proxy |
| 投信 | 0.00 | 0.75 | -0.75 | 0.00 | 0.00 | +0 | -0.75 | TAIFEX Proxy |
| 自營商 | 8.11 | 8.38 | -0.27 | 3.40 | 3.53 | -0.12 | -0.15 | TAIFEX Proxy |
| 三大法人合計 | 17.30 | 18.47 | -1.17 | 9.37 | 9.53 | -0.16 | -1.00 | TAIFEX Proxy |

### 18．選擇權前十大

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 買權多方 OI | 8,476 | TAIFEX Proxy |
| 買權空方 OI | 10,073 | TAIFEX Proxy |
| 買權多空淨 OI | -1,597 | TAIFEX Proxy |
| 買權多空淨 OI 變化 (2026-10-27→2026-10-29) | +145 | TAIFEX Proxy snapshots (2026-10-28) |

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 賣權多方 OI | 7,922 | TAIFEX Proxy |
| 賣權空方 OI | 10,180 | TAIFEX Proxy |
| 賣權多空淨 OI | -2,258 | TAIFEX Proxy |
| 賣權多空淨 OI 變化 (2026-10-27→2026-10-29) | -404 | TAIFEX Proxy snapshots (2026-10-28) |
- 資料日期：買權 2026-10-29／賣權 2026-10-29 (TypeOfTraders=0 全部交易人；契約月份 202611)

#### 大戶流向（全日；前十大無日夜拆分）

| 項目 | 淨變化 | 區間 | 資料來源 |
|---|---|---|---|
| 期貨前十大 | +888 | 2026-10-27→2026-10-29 | TAIFEX Proxy snapshots (2026-10-28) |
| 買權前十大 | +145 | 2026-10-27→2026-10-29 | TAIFEX Proxy snapshots (2026-10-28) |
| 賣權前十大 | -404 | 2026-10-27→2026-10-29 | TAIFEX Proxy snapshots (2026-10-28) |

### 16．資料來源、時間、時區與狀態

- 資料來源：TAIFEX 經 Cloudflare Worker Proxy
- 資料日期：2026-10-29；資料時間：2026-10-30 08:45:09；時區：`Asia/Taipei`
- 日盤／夜盤標記：日盤收盤後 + 夜盤盤後
- 註記：同 T0 保護：33 格沿用前版有值（本次抓取缺失不覆寫）
- 註記：同 T0 覆蓋：37 格以本次新抓取覆蓋（該 T0 尚無報告，無凍結對象）
- 未取得欄位 (4)：futures.gamma_wall, futures.gamma_flip, options.chain_oi_change, options.wall_change
- 註記：futures-price-after-hours 日期 2026-10-29 非今日 2026-10-30，視為無新節次，不採用
- 註記：Gamma Wall/Flip 端點不可用（上游 502），標 unavailable
- 註記：法人交易量變化無昨日交易端點，標 unavailable
- 註記：跨到期換月（舊202610W4→新202610F5），日對日 OI/Walls 變化不適用

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
| 外資 | -688.2 | -89,522 | -4,605 | +459 | -803 | +33 | 趨勢偏空 | 對沖避險 | twse-proxy／TAIFEX Proxy |
| 投信 | +70.4 | +87,218 | +39 | +0 | -2,776 | +0 | 避險／對沖 | 分歧 | twse-proxy／TAIFEX Proxy |
| 自營商 | -215.0 | +1,511 | +992 | -5 | -6,325 | -2,265 | 避險／對沖 | 分歧 | twse-proxy／TAIFEX Proxy |
