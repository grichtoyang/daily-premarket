# DATA_REPORT_20260924

- 報告日期：`2026-09-28`
- T0 交易日期：`2026-09-24`
- 資料產出時間：`2026-09-28 08:09:09`
- 時區：`Asia/Taipei`

---

## 一、現貨

### 1. 台股大盤行情

**資料來源：** `Cloudflare Worker：twse-proxy` (備援 `TWSE OpenAPI MI_INDEX`)

| 項目 | 數值 | 單位 | 資料來源 |
|---|---|---|---|
| 加權指數 | 48,024.60 | 點 | twse-proxy |
| 開盤 | 48,075.39 | 點 | FinMind TaiwanStockPrice TAIEX |
| 最高 | 48,117.54 | 點 | FinMind TaiwanStockPrice TAIEX |
| 最低 | 47,754.72 | 點 | FinMind TaiwanStockPrice TAIEX |
| 收盤 | 48,024.60 | 點 | twse-proxy |
| 漲跌點數 | -132.69 | 點 | twse-proxy |
| 漲跌幅 | -0.28 | % | twse-proxy |
| 成交金額 | 7,755.9 | 億元 | twse-proxy market_statistics |

### 2. 市場漲跌家數

#### 2.1 上市公司

**資料來源：** `Cloudflare Worker：twse-proxy` (備援 `TWSE OpenAPI twtazu_od`)

| 項目 | 家數 | 資料來源 |
|---|---|---|
| 上漲家數 | 386 | twse-proxy |
| 下跌家數 | 546 | twse-proxy |
| 平盤家數 | 140 | twse-proxy |
| 漲停家數 | 11 | twse-proxy |
| 跌停家數 | 1 | twse-proxy |

#### 2.2 上櫃公司

**資料來源：** `TPEX OpenAPI tpex_mainborad_highlight`

| 項目 | 家數 | 資料來源 |
|---|---|---|
| 上漲家數 | 389 | TPEX OpenAPI tpex_mainborad_highlight |
| 下跌家數 | 380 | TPEX OpenAPI tpex_mainborad_highlight |
| 平盤家數 | 101 | TPEX OpenAPI tpex_mainborad_highlight |
| 漲停家數 | 12 | TPEX OpenAPI tpex_mainborad_highlight |
| 跌停家數 | 1 | TPEX OpenAPI tpex_mainborad_highlight |

### 3. 三大法人現貨買賣超

**資料來源：** `TWSE RWD BFI82U`

| 法人別 | 買賣超金額 | 單位 | 資料來源 |
|---|---|---|---|
| 外資 | -329.6 | 億元 | twse-proxy /institutional |
| 投信 | -128.2 | 億元 | twse-proxy /institutional |
| 自營商 | +13.4 | 億元 | twse-proxy /institutional |
| 三大法人合計 | -444.5 | 億元 | twse-proxy /institutional |

### 4. 融資融券

**資料來源：** 上市+上櫃 `HiStock` (金額口徑)；維持率 `istock.tw`；備援官方逐股加總

| 項目 | 數值 | 單位 | 資料來源 |
|---|---|---|---|
| 融資餘額 | 8,268.3 | 億元 | HiStock 上市+上櫃融資融券 (金額口徑) |
| 融資增減 | +96.2 | 億元 | HiStock 上市+上櫃融資融券 (金額口徑) |
| 融券餘額 | 235,966 | 張 | HiStock 上市+上櫃融資融券 (金額口徑) |
| 融券增減 | -10,767 | 張 | HiStock 上市+上櫃融資融券 (金額口徑) |
| 融資維持率 | 193.87 | % | wantgoo 大盤融資維持率 (資料日期 2026-09-24；補登；民間估算；官方無每日序列) |

### 5. 借券資料

**資料來源：** 上市 `TWSE OpenAPI TWT96U` (可借餘額)、上櫃 `TPEX OpenAPI tpex_margin_sbl`

| 項目 | 數值 | 單位 | 資料來源 |
|---|---|---|---|
| 借券餘額 | 4,554,957 | 張 | TWSE TWT93U + TPEX margin_sbl |
| 借券賣出餘額 | 33,958 | 張 | TWSE TWT93U + TPEX margin_sbl |
| 借券賣出增減 | 284 | 張 | TWSE TWT93U + TPEX margin_sbl |

### 6. 市場成交結構

**資料來源：** 上市 `twse-proxy market_statistics`、上櫃 `TPEX OpenAPI tpex_mainborad_highlight`

| 項目 | 成交金額 | 單位 | 資料來源 |
|---|---|---|---|
| 上市成交金額 | 7,755.9 | 億元 | twse-proxy market_statistics |
| 上櫃成交金額 | 1,950.1 | 億元 | TPEX OpenAPI tpex_mainborad_highlight |
| 上市櫃成交金額合計 | 9,706.1 | 億元 | twse-proxy market_statistics+TPEX OpenAPI tpex_mainborad_highlight |

## 二、重要市場

### 1. 美股指數

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 收盤／最新值 | 漲跌點 | 漲跌幅 | 資料來源 |
|---|---|---|---|---|---|
| S&P 500 | ^GSPC | 7,743.41 | 39.28 | +0.51 | Yahoo Finance Chart API |
| Nasdaq Composite | ^IXIC | 27,068.72 | 129.35 | +0.48 | Yahoo Finance Chart API |
| Nasdaq 100 | ^NDX | 30,608.13 | 129.27 | +0.42 | Yahoo Finance Chart API |
| Dow Jones | ^DJI | 51,828.62 | 478.64 | +0.93 | Yahoo Finance Chart API |
| 費城半導體 SOX | ^SOX | 12,668.93 | 176.39 | +1.41 | Yahoo Finance Chart API |
| VIX | ^VIX | 14.87 | -0.80 | -5.11 | Yahoo Finance Chart API |

### 2. 亞洲主要指數

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 收盤／最新值 | 漲跌點 | 漲跌幅 | 資料來源 |
|---|---|---|---|---|---|
| 日經225 | ^N225 | 66,364.20 | 850.21 | +1.30 | Yahoo Finance Chart API |
| 韓國KOSPI | ^KS11 | 7,080.92 | 63.01 | +0.90 | Yahoo Finance Chart API |
| 香港恆生 | ^HSI | 24,510.09 | -251.04 | -1.01 | Yahoo Finance Chart API |
| 上海綜合 | 000001.SS | 3,888.37 | -48.15 | -1.22 | Yahoo Finance Chart API |
| 深圳成分 | 399001.SZ | 13,316.97 | -319.10 | -2.34 | Yahoo Finance Chart API |

### 3. 美股指數期貨

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 最新值 | 漲跌點 | 漲跌幅 | 資料來源 |
|---|---|---|---|---|---|
| S&P500期貨 | ES=F | 7,784.00 | -19.75 | -0.25 | Yahoo Finance Chart API |
| Nasdaq100期貨 | NQ=F | 30,846.25 | -43.00 | -0.14 | Yahoo Finance Chart API |
| 道瓊期貨 | YM=F | 51,978.00 | -185.00 | -0.35 | Yahoo Finance Chart API |
| Russell2000期貨 | RTY=F | 2,847.70 | -11.60 | -0.41 | Yahoo Finance Chart API |

### 4. 美國國債殖利率

**資料來源：** `U.S. Treasury Fiscal Data API` (失敗時備援 Treasury yield.xml 與 `Yahoo Finance`)

| 項目 | API 資料欄位／識別 | 殖利率 | 日變化 | 資料來源 |
|---|---|---|---|---|
| 美國 2 年期殖利率 | 2 Yr | 4.81 | -0.06 | U.S. Treasury yield.xml (網頁備援) |
| 美國 10 年期殖利率 | 10 Yr | 5.18 | 0.02 | Yahoo Finance (備援) |
| 美國 30 年期殖利率 | 30 Yr | 5.50 | 0.04 | Yahoo Finance (備援) |

### 5. 主要匯率

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 最新值 | 漲跌點 | 漲跌幅 | 資料來源 |
|---|---|---|---|---|---|
| USD/TWD | TWD=X | 31.78 | -0.03 | -0.09 | Yahoo Finance Chart API |
| DXY美元指數 | DX-Y.NYB | 100.97 | -0.32 | -0.32 | Yahoo Finance Chart API |
| USD/JPY | JPY=X | 157.63 | -1.18 | -0.75 | Yahoo Finance Chart API |
| USD/KRW | KRW=X | 1,358.08 | -9.28 | -0.68 | Yahoo Finance Chart API |

### 6. 台灣相關ADR

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 收盤／最新值 | 漲跌點 | 漲跌幅 | 資料來源 |
|---|---|---|---|---|---|
| 台積電ADR | TSM | 450.61 | -0.54 | -0.12 | Yahoo Finance Chart API |
| 聯電ADR | UMC | 24.31 | 0.21 | +0.87 | Yahoo Finance Chart API |
| 日月光ADR | ASX | 44.31 | 0.81 | +1.86 | Yahoo Finance Chart API |

### 7. 原油黃金Bitcoin

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 收盤／最新值 | 漲跌點 | 漲跌幅 | 資料來源 |
|---|---|---|---|---|---|
| WTI原油期貨 | CL=F | 93.28 | 0.87 | +0.94 | Yahoo Finance Chart API |
| 黃金期貨 | GC=F | 4,295.00 | -26.20 | -0.61 | Yahoo Finance Chart API |
| Bitcoin | BTC-USD | 84,377.65 | -28.80 | -0.03 | Yahoo Finance Chart API |

### 8. 重大經濟數據、央行事件與重大市場新聞

**資料來源：** 台股 `tw.stock.yahoo.com` (含內文摘要)；國際 `Fed 公告 RSS`＋`CNBC`＋`MarketWatch` (標題、來源、時間與連結)

- 事件1：美債殖利率飆破5%、通膨正在失控？甲骨文突傳警訊 　阮慕驊揭「3大未爆彈」盯緊了
  - 來源：Yahoo 台股；發布時間：2026-09-28T00:00:00Z；台北時間：2026-09-28 08:00
  - 摘要：[FTNN新聞網]記者周雅琦／綜合報導美股多頭行情延續之際，財經專家阮慕驊提醒，自己並不看空市場，但仍有3大變數值得投資人留意，包括實際利率升高、AI產業融...
  - 原文連結：https://tw.stock.yahoo.com/news/%E7%BE%8E%E5%82%B5%E6%AE%96%E5%88%A9%E7%8E%87%E9%A3%86%E7%A0%B45-%E9%80%9A%E8%86%A8%E6%AD%A3%E5%9C%A8%E5%A4%B1%E6%8E%A7-%E7%94%B2%E9%AA%A8%E6%96%87%E7%AA%81%E5%82%B3%E8%AD%A6%E8%A8%8A-%E9%98%AE%E6%85%95%E9%A9%8A%E6%8F%AD-3%E5%A4%A7%E6%9C%AA%E7%88%86%E5%BD%88-000000570.html
- 事件2：群創摔破50元關卡！1張已虧2.3萬元　股民手握7張嘆「要繼續做夢嗎？」
  - 來源：Yahoo 台股；發布時間：2026-09-27T23:30:00Z；台北時間：2026-09-28 07:30
  - 摘要：[FTNN新聞網]記者陳宣穎／綜合報導台股近期多頭氣勢連發多次刷新歷史高點，不過面板大廠群創（3481）股價卻反向疲軟，一路從今年6月波段高點72.6元下滑，25日...
  - 原文連結：https://tw.stock.yahoo.com/news/%E7%BE%A4%E5%89%B5%E6%91%94%E7%A0%B450%E5%85%83%E9%97%9C%E5%8D%A1-1%E5%BC%B5%E5%B7%B2%E8%99%A72-3%E8%90%AC%E5%85%83-%E8%82%A1%E6%B0%91%E6%89%8B%E6%8F%A17%E5%BC%B5%E5%98%86-%E8%A6%81%E7%B9%BC%E7%BA%8C%E5%81%9A%E5%A4%A2%E5%97%8E-233000621.html
- 事件3：嫌定期定額太無聊、明牌才刺激？李勛用「82配置」兼顧穩健與操作！
  - 來源：Yahoo 台股；發布時間：2026-09-27T23:09:00Z；台北時間：2026-09-28 07:09
  - 摘要：雜誌官方line＠財經資訊不漏接 多數投資人渴望一夕致富，容易在獲利了結後轉向頻繁追逐明牌，忽略複利的長期效益。建議投資人應將8成資金持續扣款、2成資金操作個股，兼顧複利效果與投資樂趣。 前些日子和認識超過14年的大學同學吃飯，在台灣只要超
  - 原文連結：https://tw.stock.yahoo.com/news/%E5%AB%8C%E5%AE%9A%E6%9C%9F%E5%AE%9A%E9%A1%8D%E5%A4%AA%E7%84%A1%E8%81%8A-%E6%98%8E%E7%89%8C%E6%89%8D%E5%88%BA%E6%BF%80-%E6%9D%8E%E5%8B%9B%E7%94%A8-82%E9%85%8D%E7%BD%AE-%E5%85%BC%E9%A1%A7%E7%A9%A9%E5%81%A5%E8%88%87%E6%93%8D%E4%BD%9C-230900649.html
- 事件4：老化加速2》大坪數住宅流動凍結 陷入4重困境
  - 來源：Yahoo 台股；發布時間：2026-09-27T23:05:00Z；台北時間：2026-09-28 07:05
  - 摘要：10年來全國人口總數減少約24.07萬人，但64歲以下的人口數卻流失高達180.77萬人，反觀65歲以上人口數則增加約156.7萬人，顯示頭重腳輕的人口金字塔型態已相當明顯。隨著台灣加速老化，未來大坪數住宅流動性凍結，受衝擊最大的，像是郊區
  - 原文連結：https://tw.stock.yahoo.com/news/%E8%80%81%E5%8C%96%E5%8A%A0%E9%80%9F2-%E5%A4%A7%E5%9D%AA%E6%95%B8%E4%BD%8F%E5%AE%85%E6%B5%81%E5%8B%95%E5%87%8D%E7%B5%90-%E9%99%B7%E5%85%A54%E9%87%8D%E5%9B%B0%E5%A2%83-230500260.html
- 事件5：老化加速1》家有一老超過家有一小  逾1/3家戶至少一老
  - 來源：Yahoo 台股；發布時間：2026-09-27T23:00:00Z；台北時間：2026-09-28 07:00
  - 摘要：家中至少有一老比家中有子女還要普遍。根據內政部不動產資訊平台最新發布，今年第一季全國戶籍總數近989.21萬戶，其中家中至少有一老的數量近350.1萬戶，占比約35.39%，平均每2.82戶就有1戶家中至少有一老。高力國際不動產業主代表服務
  - 原文連結：https://tw.stock.yahoo.com/news/%E8%80%81%E5%8C%96%E5%8A%A0%E9%80%9F1-%E5%AE%B6%E6%9C%89-%E8%80%81%E8%B6%85%E9%81%8E%E5%AE%B6%E6%9C%89-%E5%B0%8F-%E9%80%BE1-230000038.html
- 事件6：星展CIO：國際油價區間震盪　提3分析情境
  - 來源：Yahoo 台股；發布時間：2026-09-27T23:00:00Z；台北時間：2026-09-28 07:00
  - 摘要：【記者羅元駿／台北報導】國際油價近期漲跌詭譎，星展集團指出，沙烏地阿拉伯東西向油管部分重啟以及對美伊會談的樂觀情緒，讓布蘭特原油價格從近期高點回落，另外，實體油價持續保持顯著溢價，整體能源產業展現出結構性的供應緊縮。
  - 原文連結：https://tw.stock.yahoo.com/news/%E6%98%9F%E5%B1%95cio-%E5%9C%8B%E9%9A%9B%E6%B2%B9%E5%83%B9%E5%8D%80%E9%96%93%E9%9C%87%E7%9B%AA-%E6%8F%903%E5%88%86%E6%9E%90%E6%83%85%E5%A2%83-230000592.html
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
- 事件11：Debt-hungry AI companies face increased risk as bond yields spike
  - 來源：CNBC；發布時間：Sun, 27 Sep 2026 15:35:34 GMT；台北時間：2026-09-27 23:35
  - 摘要：The AI infrastructure buildout shows no sign of slowing, but the surge in Treasury yields means it's at least going to cost more.
  - 原文連結：https://www.cnbc.com/2026/09/27/debt-hungry-data-center-companies-increased-risk-bond-yields-spike.html
- 事件12：Audemars Piguet says its Royal Pop collaboration with Swatch is breaking sales records, despite luxury watch slump and tariffs
  - 來源：CNBC；發布時間：Sat, 26 Sep 2026 10:00:01 GMT；台北時間：2026-09-26 18:00
  - 摘要：Swiss luxury watchmaker Audemars Piguet says its sales and engagement are breaking records after its risky, eye-catching Royal Pop collaboration with 
  - 原文連結：https://www.cnbc.com/2026/09/26/audemars-piguet-and-royal-pop-defy-luxury-watch-slump-and-tariffs.html


## 三、期貨

**資料來源：**
1. Cloudflare Workers：TAIFEX Proxy — https://taifex.grichtoyang.workers.dev/
2. TAIFEX Open API — https://openapi.taifex.com.tw/

近月契約月份：202610 (日盤成交量最大者)；交易日期：2026-09-24

### 1．台指期近月日盤行情

| 項目 | 數值 | 資料來源 |
|---|---|---|
| 開盤價 | 47,850 | TAIFEX Proxy |
| 最高價 | 48,275 | TAIFEX Proxy |
| 最低價 | 47,797 | TAIFEX Proxy |
| 收盤價 | 48,123 | TAIFEX Proxy |
| 漲跌點數 | -189 | TAIFEX Proxy |
| 漲跌幅 | -0.39 | TAIFEX Proxy |
| 成交量 | 66,143 | TAIFEX Proxy |
| 日盤高點及低點 | 48,275 / 47,797 | TAIFEX Proxy |

### 2．台指期近月夜盤行情

| 項目 | 數值 | 資料來源 |
|---|---|---|
| 開盤價 | 48,400 | TAIFEX Proxy |
| 最高價 | 48,404 | TAIFEX Proxy |
| 最低價 | 47,783 | TAIFEX Proxy |
| 收盤價 | 47,909 | TAIFEX Proxy |
| 漲跌點數 | -403 | TAIFEX Proxy |
| 漲跌幅 | -0.83 | TAIFEX Proxy |
| 成交量 | 28,947 | TAIFEX Proxy |
| 夜盤高點及低點 | 48,404 / 47,783 | TAIFEX Proxy |
| 結算價 | 48,125 | TAIFEX Proxy |
| 未平倉量 | 101,311 | TAIFEX Proxy |

### 3．法人台指期多空未平倉部位

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 外資多方 OI | 9,675 | TAIFEX Proxy |
| 外資空方 OI | 86,706 | TAIFEX Proxy |
| 外資多空淨 OI | -77,031 | TAIFEX Proxy |
| 投信多方 OI | 75,780 | TAIFEX Proxy |
| 投信空方 OI | 2,916 | TAIFEX Proxy |
| 投信多空淨 OI | +72,864 | TAIFEX Proxy |
| 自營商多方 OI | 3,312 | TAIFEX Proxy |
| 自營商空方 OI | 4,832 | TAIFEX Proxy |
| 自營商多空淨 OI | -1,520 | TAIFEX Proxy |
| 三大法人合計多方 OI | 88,767 | TAIFEX Proxy |
| 三大法人合計空方 OI | 94,454 | TAIFEX Proxy |
| 三大法人合計多空淨 OI | -5,687 | TAIFEX Proxy |
| 外資多空淨 OI 變化 | -947 | TAIFEX Proxy |
| 投信多空淨 OI 變化 | -695 | TAIFEX Proxy |
| 自營商多空淨 OI 變化 | +1,536 | TAIFEX Proxy |

### 4．前十大交易人多空未平倉部位

**資料來源：** `TAIFEX OpenAPI OpenInterestOfLargeTradersFutures` (官方資料落後約一日，標示實際日期)

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 前十大交易人多方 OI | 78,199 | TAIFEX Proxy |
| 前十大交易人空方 OI | 70,805 | TAIFEX Proxy |
| 前十大交易人多空淨 OI | +7,394 | TAIFEX Proxy |
| 多空淨 OI 變化 (2026-09-22→2026-09-24) | -2,489 | TAIFEX Proxy snapshots (2026-09-23) |
- 資料日期：2026-09-24 (TypeOfTraders=0 全部交易人；契約月份 202610)

### 5．日盤、夜盤法人交易資料

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 外資日盤多單交易量 | 36,223 | TAIFEX Proxy |
| 外資日盤空單交易量 | 37,132 | TAIFEX Proxy |
| 外資日盤多空淨交易量 | -909 | TAIFEX Proxy |
| 外資夜盤多單交易量 | 16,603 | TAIFEX Proxy |
| 外資夜盤空單交易量 | 16,638 | TAIFEX Proxy |
| 外資夜盤多空淨交易量 | -35 | TAIFEX Proxy |
| 外資日盤／夜盤交易量變化 | -874 | TAIFEX Proxy |
| 投信日盤多空淨交易量 | -695 | TAIFEX Proxy |
| 投信夜盤多空淨交易量 | +0 | TAIFEX Proxy |
| 投信日盤／夜盤交易量變化 | -695 | TAIFEX Proxy |
| 自營商日盤多空淨交易量 | +1,450 | TAIFEX Proxy |
| 自營商夜盤多空淨交易量 | +389 | TAIFEX Proxy |
| 自營商日盤／夜盤交易量變化 | +1,061 | TAIFEX Proxy |
| 三大法人日盤多空淨交易量 | -154 | TAIFEX Proxy |
| 三大法人夜盤多空淨交易量 | +354 | TAIFEX Proxy |
| 法人日盤交易金額淨額 (億元) | -14.8 | TAIFEX Proxy |
| 法人夜盤交易金額淨額 (億元) | +34.0 | TAIFEX Proxy |

### 6．期貨與現貨關係

| 項目 | 數值 | 資料來源 |
|---|---|---|
| 台指期近月價格 | 48,123 | TAIFEX Proxy |
| 加權指數價格 | 48,024.60 | twse-proxy |
| 台指期與加權指數價差 | +98.40 | TAIFEX Proxy+twse-proxy |
| 價差百分比 | +0.20 | TAIFEX Proxy+twse-proxy |
| 日盤基差 | +98.40 | TAIFEX Proxy+twse-proxy |
| 夜盤價格相對日盤收盤的變化 | -214 | TAIFEX Proxy |

### 7．日盤、夜盤與籌碼變化對照

#### 7.1 日夜盤價格與成交量對照 (變化 = 日盤 - 夜盤)

| 項目 | 日盤 | 夜盤 | 變化 (日-夜) | 資料來源 |
|---|---|---|---|---|
| 收盤價 | 48,123 | 47,909 | +214 | TAIFEX Proxy |
| 成交量 | 37,196 | 28,947 | +8,249 | TAIFEX Proxy |
- 台指期總 OI 前日變化：-106（來源：TAIFEX Proxy）


#### 7.2 法人籌碼日夜盤對照 (淨變化 = 日盤淨 - 夜盤淨；OI 為日盤收盤後總量，前日變化另列)

| 法人 | 交易量 |  |  |  |  |  |  | 未平倉量 |  |  |  | 資料來源 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|  | **日盤多單** | **日盤空單** | **日盤淨** | **夜盤多單** | **夜盤空單** | **夜盤淨** | **淨變化 (日-夜)** | **OI多方** | **OI空方** | **OI淨** | **OI前日變化** |  |
| 外資 | 36,223 | 37,132 | -909 | 16,603 | 16,638 | -35 | -874 | 9,675 | 86,706 | -77,031 | -947 | TAIFEX Proxy |
| 投信 | 125 | 820 | -695 | 0 | 0 | +0 | -695 | 75,780 | 2,916 | +72,864 | -695 | TAIFEX Proxy |
| 自營商 | 4,020 | 2,570 | +1,450 | 872 | 483 | +389 | +1,061 | 3,312 | 4,832 | -1,520 | +1,536 | TAIFEX Proxy |
| 三大法人合計 | 40,368 | 40,522 | -154 | 17,475 | 17,121 | +354 | -508 | 88,767 | 94,454 | -5,687 | -106 | TAIFEX Proxy |

#### 7.3 前十大交易人日夜盤對照 (OI 無日夜拆分，列收盤後總量)

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 前十大交易人多方 OI | 78,199 | TAIFEX Proxy |
| 前十大交易人空方 OI | 70,805 | TAIFEX Proxy |
| 前十大交易人多空淨 OI | +7,394 | TAIFEX Proxy |
| 前十大交易人多空淨 OI 變化 (2026-09-22→2026-09-24) | -2,489 | TAIFEX Proxy snapshots (2026-09-23) |

#### 7.4 夜盤劇本分類 (規則對應：夜盤漲跌 × 外資夜盤偏多空)

| 項目 | 數值 | 資料來源 |
|---|---|---|
| 夜盤成交量占比 (夜盤量／(夜盤量＋日盤量)) | 43.76% | TAIFEX Proxy |
| 夜盤漲跌點數 | -403 | TAIFEX Proxy |
| 外資夜盤多空淨交易量 | -35 | TAIFEX Proxy |
| 劇本分類 | 劇本三 | 規則對應 |
| 劇本條件 | 夜盤下跌＋外資偏空 | 規則對應 |
| 劇本特徵 | 開低、續跌機率高 | 規則對應 |

## 四、選擇權

**資料來源：** 主要 TAIFEX 經 Cloudflare Worker Proxy；時區 `Asia/Taipei`

### 1．選擇權交易日期、到期日與資料時間

| 項目 | 數值 | 資料來源 |
|---|---|---|
| 交易日期 | 2026-09-24 | TAIFEX Proxy |
| 到期月份／到期日 | 202609F4 | TAIFEX Proxy |
| 資料更新時間 | 2026-09-28 08:09:09 | 本機 |
| 日盤／夜盤標記 | 日盤收盤後資料 | TAIFEX Proxy |

### 2．Call 總成交量、OI、OI 增減

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Call 總成交量 | 90,216 | TAIFEX Proxy |
| Call 總未平倉量 OI | 31,654 | TAIFEX Proxy |
| Call OI 增減 | +25,482 | TAIFEX Proxy snapshots (2026-09-22) |

### 3．Put 總成交量、OI、OI 增減

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Put 總成交量 | 113,949 | TAIFEX Proxy |
| Put 總未平倉量 OI | 25,184 | TAIFEX Proxy |
| Put OI 增減 | +20,202 | TAIFEX Proxy snapshots (2026-09-22) |

### 4．Call／Put 比例與變化

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Call／Put 成交量比例 | 0.79 | TAIFEX Proxy |
| Call／Put 未平倉量比例 | 1.26 | TAIFEX Proxy |
| Put／Call Ratio | 0.80 | TAIFEX Proxy |
| Call／Put 比例變化 (量比 2026-09-23→2026-09-24) | 25.27 | TAIFEX Proxy |
| 與前一交易日比較 (OI 比 2026-09-23→2026-09-24) | 5.50 | TAIFEX Proxy |
**資料來源：** 比例 `TAIFEX Proxy chain`；變化 `TAIFEX Proxy PutCallRatio`

### 5．外資 Call／Put 部位

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 外資 Call日買 | 29,907 | TAIFEX Proxy |
| 外資 Call日賣 | 29,903 | TAIFEX Proxy |
| 外資 Call日淨 | +4 | TAIFEX Proxy |
| 外資 Put日買 | 47,563 | TAIFEX Proxy |
| 外資 Put日賣 | 46,827 | TAIFEX Proxy |
| 外資 Put日淨 | +736 | TAIFEX Proxy |
| 外資 Call夜買 | 18,103 | TAIFEX Proxy |
| 外資 Call夜賣 | 18,219 | TAIFEX Proxy |
| 外資 Call夜淨 | -116 | TAIFEX Proxy |
| 外資 Put夜買 | 20,577 | TAIFEX Proxy |
| 外資 Put夜賣 | 20,634 | TAIFEX Proxy |
| 外資 Put夜淨 | -57 | TAIFEX Proxy |
| 外資 日盤淨總量 | -732 | TAIFEX Proxy |
| 外資 Call日夜淨增減 (日－夜) | +120 | TAIFEX Proxy |
| 外資 Put日夜淨增減 (日－夜) | +793 | TAIFEX Proxy |

### 6．自營商 Call／Put 部位

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 自營商 Call日買 | 26,239 | TAIFEX Proxy |
| 自營商 Call日賣 | 26,536 | TAIFEX Proxy |
| 自營商 Call日淨 | -297 | TAIFEX Proxy |
| 自營商 Put日買 | 38,901 | TAIFEX Proxy |
| 自營商 Put日賣 | 38,840 | TAIFEX Proxy |
| 自營商 Put日淨 | +61 | TAIFEX Proxy |
| 自營商 Call夜買 | 10,032 | TAIFEX Proxy |
| 自營商 Call夜賣 | 12,257 | TAIFEX Proxy |
| 自營商 Call夜淨 | -2,225 | TAIFEX Proxy |
| 自營商 Put夜買 | 12,328 | TAIFEX Proxy |
| 自營商 Put夜賣 | 12,245 | TAIFEX Proxy |
| 自營商 Put夜淨 | +83 | TAIFEX Proxy |
| 自營商 日盤淨總量 | -358 | TAIFEX Proxy |
| 自營商 Call日夜淨增減 (日－夜) | +1,928 | TAIFEX Proxy |
| 自營商 Put日夜淨增減 (日－夜) | -22 | TAIFEX Proxy |

### 7．主要 Call OI 集中區

| 項目 | 履約價 | OI | 資料來源 |
|---|---|---|---|
| Call OI 第1大履約價 | 51,900 | 2,455 | TAIFEX Proxy |
| Call OI 第2大履約價 | 50,500 | 2,149 | TAIFEX Proxy |
| Call OI 第3大履約價 | 51,000 | 1,774 | TAIFEX Proxy |
| Call OI 最大履約價 | 51,900 | 2,455 | TAIFEX Proxy |

#### Call OI 分布明細 Top10 (機器可讀，到期月份 202609F4)

| # | 履約價 | OI | 佔比 | 資料來源 |
|---|---|---|---|---|
| C1 | 51,900 | 2,455 | 7.76% | TAIFEX Proxy |
| C2 | 50,500 | 2,149 | 6.79% | TAIFEX Proxy |
| C3 | 51,000 | 1,774 | 5.6% | TAIFEX Proxy |
| C4 | 49,000 | 1,351 | 4.27% | TAIFEX Proxy |
| C5 | 50,000 | 1,146 | 3.62% | TAIFEX Proxy |
| C6 | 51,500 | 1,110 | 3.51% | TAIFEX Proxy |
| C7 | 49,500 | 995 | 3.14% | TAIFEX Proxy |
| C8 | 50,300 | 909 | 2.87% | TAIFEX Proxy |
| C9 | 49,400 | 891 | 2.81% | TAIFEX Proxy |
| C10 | 48,500 | 842 | 2.66% | TAIFEX Proxy |


### 8．主要 Put OI 集中區

| 項目 | 履約價 | OI | 資料來源 |
|---|---|---|---|
| Put OI 第1大履約價 | 47,800 | 1,832 | TAIFEX Proxy |
| Put OI 第2大履約價 | 43,000 | 1,552 | TAIFEX Proxy |
| Put OI 第3大履約價 | 47,700 | 1,333 | TAIFEX Proxy |
| Put OI 最大履約價 | 47,800 | 1,832 | TAIFEX Proxy |

#### Put OI 分布明細 Top10 (機器可讀，到期月份 202609F4)

| # | 履約價 | OI | 佔比 | 資料來源 |
|---|---|---|---|---|
| P1 | 47,800 | 1,832 | 7.27% | TAIFEX Proxy |
| P2 | 43,000 | 1,552 | 6.16% | TAIFEX Proxy |
| P3 | 47,700 | 1,333 | 5.29% | TAIFEX Proxy |
| P4 | 47,000 | 1,061 | 4.21% | TAIFEX Proxy |
| P5 | 46,000 | 1,042 | 4.14% | TAIFEX Proxy |
| P6 | 41,500 | 982 | 3.9% | TAIFEX Proxy |
| P7 | 46,500 | 822 | 3.26% | TAIFEX Proxy |
| P8 | 44,800 | 677 | 2.69% | TAIFEX Proxy |
| P9 | 46,900 | 663 | 2.63% | TAIFEX Proxy |
| P10 | 47,500 | 660 | 2.62% | TAIFEX Proxy |


### 9．Call OI 增減集中區

| 項目 | 履約價 (增減口數) | 資料來源 |
|---|---|---|
| Call OI 增加最多的履約價 | 50,500 (+2,132) | TAIFEX Proxy snapshots (2026-09-22) |
| Call OI 減少最多的履約價 | 47,450 (-2) | TAIFEX Proxy snapshots (2026-09-22) |

### 10．Put OI 增減集中區

| 項目 | 履約價 (增減口數) | 資料來源 |
|---|---|---|
| Put OI 增加最多的履約價 | 47,800 (+1,802) | TAIFEX Proxy snapshots (2026-09-22) |
| Put OI 減少最多的履約價 | 40,900 (-95) | TAIFEX Proxy snapshots (2026-09-22) |

### 11．Call Wall

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Call Wall 價位 | 51,900 | TAIFEX Proxy |
| 對應到期月份 | 202609F4 | TAIFEX Proxy |
| 與前一交易日的變化 | unavailable | 端點未提供 |

### 12．Put Wall

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Put Wall 價位 | 47,800 | TAIFEX Proxy |
| 對應到期月份 | 202609F4 | TAIFEX Proxy |
| 與前一交易日的變化 | unavailable | 端點未提供 |

### 13．Gamma Wall

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Gamma Wall 價位 | 47,800.00 | TAIFEX Proxy (options-market-structure-compact (proxy)) |
| 對應到期月份 | 202609F4 | TAIFEX Proxy |
| 資料日期 | 2026-09-24 | TAIFEX Proxy (options-market-structure-compact (proxy)) |

### 14．Gamma Flip

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Gamma Flip 價位 | 47,843.68 | TAIFEX Proxy (options-market-structure-compact (proxy)) |
| 對應到期月份 | 202609F4 | TAIFEX Proxy |
| 資料日期 | 2026-09-24 | TAIFEX Proxy (options-market-structure-compact (proxy)) |

### 15．Max Pain

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Max Pain 價位 | 47,700 | TAIFEX Proxy |
| 對應到期月份 | 202609F4 | TAIFEX Proxy |
| 與前一交易日的變化 | unavailable | 端點未提供 |

### 17．選擇權法人日盤、夜盤交易

| 法人 | 日盤多單 | 日盤空單 | 日盤淨 | 夜盤多單 | 夜盤空單 | 夜盤淨 | 淨變化 (日-夜) | 資料來源 |
|---|---|---|---|---|---|---|---|---|
| 外資 | 76,734 | 77,466 | -732 | 38,737 | 38,796 | -59 | -673 | TAIFEX Proxy |
| 投信 | 0 | 650 | -650 | 0 | 0 | +0 | -650 | TAIFEX Proxy |
| 自營商 | 65,079 | 65,437 | -358 | 22,277 | 24,585 | -2,308 | +1,950 | TAIFEX Proxy |
| 三大法人合計 | 141,813 | 143,553 | -1,740 | 61,014 | 63,381 | -2,367 | +627 | TAIFEX Proxy |
- 方法論：多方＝買Call＋賣Put（看多），空方＝賣Call＋買Put（看空），淨額＝看多－看空（已用 Call／Put 拆分頁交叉驗算一致）
- 公式：多方(買)－空方(賣)＝（買call＋賣put）－（賣call＋買put）＝看多－看空
- 速記：多＝BC＋SP、空＝SC＋BP

#### 法人多空力道表（金額・億元；上游千元／1e5）

| 法人 | 日多方力道 | 日空方力道 | 日淨多空力道 | 夜多方力道 | 夜空方力道 | 夜淨多空力道 | 日淨－夜淨 | 資料來源 |
|---|---|---|---|---|---|---|---|---|
| 外資 | 7.69 | 7.67 | +0.02 | 3.68 | 3.73 | -0.05 | +0.07 | TAIFEX Proxy |
| 投信 | 0.00 | 0.44 | -0.44 | 0.00 | 0.00 | +0 | -0.44 | TAIFEX Proxy |
| 自營商 | 5.86 | 6.13 | -0.28 | 1.82 | 2.33 | -0.52 | +0.24 | TAIFEX Proxy |
| 三大法人合計 | 13.55 | 14.24 | -0.70 | 5.50 | 6.06 | -0.57 | -0.13 | TAIFEX Proxy |

### 18．選擇權前十大

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 買權多方 OI | 12,023 | TAIFEX Proxy |
| 買權空方 OI | 10,907 | TAIFEX Proxy |
| 買權多空淨 OI | +1,116 | TAIFEX Proxy |
| 買權多空淨 OI 變化 (2026-09-22→2026-09-24) | -290 | TAIFEX Proxy snapshots (2026-09-23) |

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 賣權多方 OI | 7,486 | TAIFEX Proxy |
| 賣權空方 OI | 8,368 | TAIFEX Proxy |
| 賣權多空淨 OI | -882 | TAIFEX Proxy |
| 賣權多空淨 OI 變化 (2026-09-22→2026-09-24) | +91 | TAIFEX Proxy snapshots (2026-09-23) |
- 資料日期：買權 2026-09-24／賣權 2026-09-24 (TypeOfTraders=0 全部交易人；契約月份 202610)

#### 大戶流向（全日；前十大無日夜拆分）

| 項目 | 淨變化 | 區間 | 資料來源 |
|---|---|---|---|
| 期貨前十大 | -2,489 | 2026-09-22→2026-09-24 | TAIFEX Proxy snapshots (2026-09-23) |
| 買權前十大 | -290 | 2026-09-22→2026-09-24 | TAIFEX Proxy snapshots (2026-09-23) |
| 賣權前十大 | +91 | 2026-09-22→2026-09-24 | TAIFEX Proxy snapshots (2026-09-23) |

### 16．資料來源、時間、時區與狀態

- 資料來源：TAIFEX 經 Cloudflare Worker Proxy
- 資料日期：2026-09-24；資料時間：2026-09-28 08:09:09；時區：`Asia/Taipei`
- 日盤／夜盤標記：日盤收盤後 + 夜盤盤後
- 註記：同 T0 保護：8 格沿用前版有值（本次抓取缺失不覆寫）
- 未取得欄位 (1)：options.chain_oi_change
- 註記：無日期端點為最新盤勢快照 (判定資料日期 2026-09-25，非 T0 2026-09-24)，適用：日盤價／法人交易／夜盤／選擇權法人；T0 相符時不另標註
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
- margin_ratio：`前值遞補 (DATA 2026-09-21；當日三源皆失敗；民間估算；官方無每日序列)`
- sbl：`TWSE TWT93U + TPEX margin_sbl`
- 期貨選擇權：`TAIFEX Proxy`
- 新聞：台股 Yahoo／國際 Fed＋CNBC＋MarketWatch；台股 Yahoo / 國際 Fed 公告＋CNBC＋MarketWatch RSS；Fed 無摘要；investing 港股為主已退役；cnyes CSR、wantgoo JS 算繪、中央社/央行路徑待查，未採用
- 美股/亞股/期貨/匯率/ADR/商品：`Yahoo Finance Chart API`；美債：`Yahoo Finance (備援)`
- 註記：融資維持率未取得 (三源皆失敗；官方無每日序列)
- 註記：融資維持率採前值遞補 (DATA 2026-09-21)，非 T0 2026-09-24
- 註記：上市 MI_MARGN / TWT96U 無日期欄，採用最新可得
- 註記：借券賣出增減僅上櫃值 (TWSE TWT93U 未取得)
- 本報告僅整理資料，不提供交易判斷。

## 六、期現選方向對照

**規則：** 趨勢偏多／空＝現貨、期貨OI、選擇權日淨三者同向；避險／對沖＝現貨與期選反向；日內反轉＝日淨與夜淨反向；缺值標示，不推估。選擇權多空為看多看空口徑。

| 法人 | 現貨買賣超(億) | 期貨OI淨(口) | 期貨日淨 | 期貨夜淨 | 選擇權日淨 | 選擇權夜淨 | 判定 | 期選組合 | 資料來源 |
|---|---|---|---|---|---|---|---|---|---|
| 外資 | -329.6 | -77,031 | -909 | -35 | -732 | -59 | 趨勢偏空 | 對沖避險 | twse-proxy／TAIFEX Proxy |
| 投信 | -128.2 | +72,864 | -695 | +0 | -650 | +0 | 避險／對沖 | 分歧 | twse-proxy／TAIFEX Proxy |
| 自營商 | +13.4 | -1,520 | +1,450 | +389 | -358 | -2,308 | 避險／對沖 | 強避險 | twse-proxy／TAIFEX Proxy |
