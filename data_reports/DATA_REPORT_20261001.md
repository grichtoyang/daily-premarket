# DATA_REPORT_20261001

- 報告日期：`2026-10-01`
- T0 交易日期：`2026-10-01`
- 資料產出時間：`2026-10-01 19:15:47`
- 時區：`Asia/Taipei`

---

## 一、現貨

### 1. 台股大盤行情

**資料來源：** `Cloudflare Worker：twse-proxy` (備援 `TWSE OpenAPI MI_INDEX`)

| 項目 | 數值 | 單位 | 資料來源 |
|---|---|---|---|
| 加權指數 | 48,353.49 | 點 | twse-proxy |
| 開盤 | 47,961.98 | 點 | FinMind TaiwanStockPrice TAIEX |
| 最高 | 48,353.49 | 點 | FinMind TaiwanStockPrice TAIEX |
| 最低 | 47,893.42 | 點 | FinMind TaiwanStockPrice TAIEX |
| 收盤 | 48,353.49 | 點 | twse-proxy |
| 漲跌點數 | 413.36 | 點 | twse-proxy |
| 漲跌幅 | +0.86 | % | twse-proxy |
| 成交金額 | 8,740.5 | 億元 | twse-proxy market_statistics |

### 2. 市場漲跌家數

#### 2.1 上市公司

**資料來源：** `Cloudflare Worker：twse-proxy` (備援 `TWSE OpenAPI twtazu_od`)

| 項目 | 家數 | 資料來源 |
|---|---|---|
| 上漲家數 | 422 | twse-proxy |
| 下跌家數 | 551 | twse-proxy |
| 平盤家數 | 107 | twse-proxy |
| 漲停家數 | 23 | twse-proxy |
| 跌停家數 | 2 | twse-proxy |

#### 2.2 上櫃公司

**資料來源：** `TPEX OpenAPI tpex_mainborad_highlight`

| 項目 | 家數 | 資料來源 |
|---|---|---|
| 上漲家數 | 333 | TPEX OpenAPI tpex_mainborad_highlight |
| 下跌家數 | 417 | TPEX OpenAPI tpex_mainborad_highlight |
| 平盤家數 | 114 | TPEX OpenAPI tpex_mainborad_highlight |
| 漲停家數 | 27 | TPEX OpenAPI tpex_mainborad_highlight |
| 跌停家數 | 2 | TPEX OpenAPI tpex_mainborad_highlight |

### 3. 三大法人現貨買賣超

**資料來源：** `TWSE RWD BFI82U`

| 法人別 | 買賣超金額 | 單位 | 資料來源 |
|---|---|---|---|
| 外資 | +219.4 | 億元 | twse-proxy /institutional |
| 投信 | +56.6 | 億元 | twse-proxy /institutional |
| 自營商 | +16.6 | 億元 | twse-proxy /institutional |
| 三大法人合計 | +292.5 | 億元 | twse-proxy /institutional |

### 4. 融資融券

**資料來源：** 上市+上櫃 `HiStock` (金額口徑)；維持率 `istock.tw`；備援官方逐股加總

| 項目 | 數值 | 單位 | 資料來源 |
|---|---|---|---|
| 融資餘額 | unavailable | 億元 | HiStock |
| 融資增減 | unavailable | 億元 | HiStock |
| 融券餘額 | 235,296 | 張 | HiStock |
| 融券增減 | 18,158 | 張 | HiStock |
| 融資維持率 | 193.66 | % | 前值遞補 (DATA 2026-09-30；當日三源皆失敗；民間估算；官方無每日序列) |

### 5. 借券資料

**資料來源：** 上市 `TWSE OpenAPI TWT96U` (可借餘額)、上櫃 `TPEX OpenAPI tpex_margin_sbl`

| 項目 | 數值 | 單位 | 資料來源 |
|---|---|---|---|
| 借券餘額 | 2,410,056 | 張 | TWSE TWT93U + TPEX margin_sbl |
| 借券賣出餘額 | unavailable | 張 | TWSE TWT93U + TPEX margin_sbl |
| 借券賣出增減 | unavailable | 張 | TWSE TWT93U + TPEX margin_sbl |

### 6. 市場成交結構

**資料來源：** 上市 `twse-proxy market_statistics`、上櫃 `TPEX OpenAPI tpex_mainborad_highlight`

| 項目 | 成交金額 | 單位 | 資料來源 |
|---|---|---|---|
| 上市成交金額 | 8,740.5 | 億元 | twse-proxy market_statistics |
| 上櫃成交金額 | 2,558.5 | 億元 | TPEX OpenAPI tpex_mainborad_highlight |
| 上市櫃成交金額合計 | 11,299.0 | 億元 | twse-proxy market_statistics+TPEX OpenAPI tpex_mainborad_highlight |

## 二、重要市場

### 1. 美股指數

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 收盤／最新值 | 漲跌點 | 漲跌幅 | 資料來源 |
|---|---|---|---|---|---|
| S&P 500 | ^GSPC | 7,651.54 | -19.30 | -0.25 | Yahoo Finance Chart API |
| Nasdaq Composite | ^IXIC | 26,861.06 | 63.52 | +0.24 | Yahoo Finance Chart API |
| Nasdaq 100 | ^NDX | 30,408.50 | 69.17 | +0.23 | Yahoo Finance Chart API |
| Dow Jones | ^DJI | 50,906.05 | -443.87 | -0.86 | Yahoo Finance Chart API |
| 費城半導體 SOX | ^SOX | 12,628.62 | -0.54 | -0.00 | Yahoo Finance Chart API |
| VIX | ^VIX | 16.26 | -0.08 | -0.49 | Yahoo Finance Chart API |

### 2. 亞洲主要指數

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 收盤／最新值 | 漲跌點 | 漲跌幅 | 資料來源 |
|---|---|---|---|---|---|
| 日經225 | ^N225 | 68,956.72 | 2,203.00 | +3.30 | Yahoo Finance Chart API |
| 韓國KOSPI | ^KS11 | 6,971.35 | 133.31 | +1.95 | Yahoo Finance Chart API |
| 香港恆生 | ^HSI | 24,613.27 | 89.70 | +0.37 | Yahoo Finance Chart API |
| 上海綜合 | 000001.SS | 3,842.20 | 11.74 | +0.31 | Yahoo Finance Chart API |
| 深圳成分 | 399001.SZ | 12,887.62 | -14.33 | -0.11 | Yahoo Finance Chart API |

### 3. 美股指數期貨

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 最新值 | 漲跌點 | 漲跌幅 | 資料來源 |
|---|---|---|---|---|---|
| S&P500期貨 | ES=F | 7,740.50 | 25.00 | +0.32 | Yahoo Finance Chart API |
| Nasdaq100期貨 | NQ=F | 30,897.75 | 199.00 | +0.65 | Yahoo Finance Chart API |
| 道瓊期貨 | YM=F | 51,316.00 | 38.00 | +0.07 | Yahoo Finance Chart API |
| Russell2000期貨 | RTY=F | 2,820.90 | 3.40 | +0.12 | Yahoo Finance Chart API |

### 4. 美國國債殖利率

**資料來源：** `U.S. Treasury Fiscal Data API` (失敗時備援 Treasury yield.xml 與 `Yahoo Finance`)

| 項目 | API 資料欄位／識別 | 殖利率 | 日變化 | 資料來源 |
|---|---|---|---|---|
| 美國 2 年期殖利率 | 2 Yr | 4.88 | -0.01 | U.S. Treasury yield.xml (網頁備援) |
| 美國 10 年期殖利率 | 10 Yr | 5.29 | 0.04 | Yahoo Finance (備援) |
| 美國 30 年期殖利率 | 30 Yr | 5.64 | 0.04 | Yahoo Finance (備援) |

### 5. 主要匯率

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 最新值 | 漲跌點 | 漲跌幅 | 資料來源 |
|---|---|---|---|---|---|
| USD/TWD | TWD=X | 31.94 | 0.09 | +0.28 | Yahoo Finance Chart API |
| DXY美元指數 | DX-Y.NYB | 101.78 | 0.33 | +0.33 | Yahoo Finance Chart API |
| USD/JPY | JPY=X | 158.16 | 0.76 | +0.48 | Yahoo Finance Chart API |
| USD/KRW | KRW=X | 1,363.14 | 12.64 | +0.94 | Yahoo Finance Chart API |

### 6. 台灣相關ADR

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 收盤／最新值 | 漲跌點 | 漲跌幅 | 資料來源 |
|---|---|---|---|---|---|
| 台積電ADR | TSM | 456.19 | -0.75 | -0.16 | Yahoo Finance Chart API |
| 聯電ADR | UMC | 24.49 | -0.23 | -0.93 | Yahoo Finance Chart API |
| 日月光ADR | ASX | 44.46 | -0.85 | -1.88 | Yahoo Finance Chart API |

### 7. 原油黃金Bitcoin

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 收盤／最新值 | 漲跌點 | 漲跌幅 | 資料來源 |
|---|---|---|---|---|---|
| WTI原油期貨 | CL=F | 91.74 | 1.32 | +1.46 | Yahoo Finance Chart API |
| 黃金期貨 | GC=F | 4,202.10 | 15.40 | +0.37 | Yahoo Finance Chart API |
| Bitcoin | BTC-USD | 83,808.73 | 254.88 | +0.31 | Yahoo Finance Chart API |

### 8. 重大經濟數據、央行事件與重大市場新聞

**資料來源：** 台股 `tw.stock.yahoo.com` (含內文摘要)；國際 `Fed 公告 RSS`＋`CNBC`＋`MarketWatch` (標題、來源、時間與連結)

- 事件1：台股站回4萬8創新高 國巨亮燈、景碩衝進千金圈
  - 來源：Yahoo 台股；發布時間：2026-10-01T09:12:07Z；台北時間：2026-10-01 17:12
  - 摘要：台積電與被動元件雙雙點火，台股大漲413點、改寫收盤新高！今(1)日加權指數盤中一度翻黑，隨後買盤回流，終場上漲413.36點或0.86%，收48,353.49點，成交金額8,388.73億元。櫃買指數上漲0.42%，電子指數上漲1.24%
  - 原文連結：https://tw.stock.yahoo.com/news/%E5%8F%B0%E8%82%A1%E7%AB%99%E5%9B%9E4%E8%90%AC8%E5%86%8D%E5%89%B5%E6%94%B6%E7%9B%A4%E6%96%B0%E9%AB%98%EF%BC%81%E5%9C%8B%E5%B7%A8%E5%B8%B6%E9%9A%8A%E4%BA%AE%E7%87%88%E3%80%81%E6%99%AF%E7%A2%A9%E6%99%89%E5%8D%87%E5%8D%83%E9%87%91%E8%88%87%E8%BC%89%E6%9D%BF%E9%9B%99%E9%9B%84%E6%8A%B1%E5%9C%98%E8%A1%9D%EF%BD%9Cyahoo%E8%B2%A1%E7%B6%93%E6%8E%83%E6%8F%8F-091207408.html
- 事件2：信用互查惹暴跌疑慮 金管會澄清新制「不是四貸管制」
  - 來源：Yahoo 台股；發布時間：2026-10-01T09:02:17Z；台北時間：2026-10-01 17:02
  - 摘要：金管會10月底將上路銀行與券商跨業信用查詢機制，被視為終於出手管制了！房產趨勢專家李同榮針對這項政策，用八個字形容：「遲來警覺，為時不晚」。但也有財經網紅憂金管會管制「台股恐暴跌？」銀行局副局長王允中今（1）日鄭重澄清「從來沒有四貸管制措施
  - 原文連結：https://tw.stock.yahoo.com/news/%E6%96%B0%E5%88%B6%E4%B8%8A%E8%B7%AF%E8%82%A1%E5%B8%82%E6%9C%83%E6%9A%B4%E8%B7%8C%EF%BC%9F%E9%87%91%E7%AE%A1%E6%9C%83%E6%BE%84%E6%B8%85%EF%BC%9A%E5%BE%9E%E4%BE%86%E6%B2%92%E6%9C%89%E5%9B%9B%E8%B2%B8%E5%90%8C%E5%A0%82%E7%AE%A1%E5%88%B6%E6%8E%AA%E6%96%BD-090217437.html
- 事件3：台股熱不熱、槓桿高不高？儀表板四大門道一次看懂
  - 來源：Yahoo 台股；發布時間：2026-09-29T10:00:00Z；台北時間：2026-09-29 18:00
  - 摘要：證交所與櫃買中心推出的「臺股儀表板」已於9月23日正式上線，首波整合三大面向數據，讓投資人掌握證券商授信業務、投資人違約概況及上市櫃公司營收。臺股儀表板究竟是股市照妖鏡，還是投資警報器？本文除了帶你了解臺股儀表板揭露了哪些重要資訊，還要教你
  - 原文連結：https://tw.stock.yahoo.com/news/%E8%87%BA%E8%82%A1%E5%84%80%E8%A1%A8%E6%9D%BF%E6%8F%AD%E9%9C%B2%E4%B8%89%E5%A4%A7%E9%9D%A2%E5%90%91%E6%95%B8%E6%93%9A-%E6%98%AF%E8%82%A1%E5%B8%82%E7%85%A7%E5%A6%96%E9%8F%A1%E9%82%84%E6%98%AF%E6%8A%95%E8%B3%87%E8%AD%A6%E5%A0%B1%E5%99%A8%EF%BC%9F%E7%9C%8B%E6%87%82%E5%9B%9B%E5%A4%A7%E9%96%80%E9%81%93%E4%B8%8D%E5%8F%AA%E6%B9%8A%E7%86%B1%E9%AC%A7%EF%BC%81%EF%BD%9C%E7%9C%8B%E5%9C%96%E8%AA%AA%E8%82%A1%E5%B8%82-100000687.html
- 事件4：外資回頭緯創重返200元有戲？分析師點出開盤關鍵
  - 來源：Yahoo 台股；發布時間：2026-10-01T09:44:28Z；台北時間：2026-10-01 17:44
  - 摘要：外資今（1）日大舉掃貨緯創（3231）29,330張，居個股買超之冠，明日股價能否延續漲勢成為市場焦點。分析師認為，人工智慧新創Anthropic與馬斯克旗下SpaceX算力合作題材搭配法人買盤肯定，讓緯創短線走勢偏多，195.5元是明日觀
  - 原文連結：https://tw.stock.yahoo.com/news/%E7%B7%AF%E5%89%B5%E9%87%8D%E7%8D%B2%E5%A4%96%E8%B3%87%E9%9D%92%E7%9D%9E-%E6%98%8E%E5%A4%A9%E9%87%8D%E8%BF%94200%E5%85%83%EF%BC%9F%E5%88%86%E6%9E%90%E5%B8%AB%EF%BC%9A%E5%85%88%E7%9C%8B%E9%96%8B%E7%9B%A4%E9%80%99%E9%97%9C-094428265.html
- 事件5：「金九銀十」發威 鋼廠齊漲盤價最高加千元
  - 來源：Yahoo 台股；發布時間：2026-10-01T10:08:31Z；台北時間：2026-10-01 18:08
  - 摘要：[非凡新聞]記者陳明萱,攝影吳國豪「金九銀十」效應持續加溫，迎來Q4旺季，多家主力鋼廠同步調漲10月份盤價，像是鍍面大廠燁輝，10月鍍鋅烤漆鋼捲每噸漲1000元，創5個月來最大漲幅。在原料成本有撐、需求動能回升下，...
  - 原文連結：https://tw.stock.yahoo.com/news/%E9%8B%BC%E5%B8%82%E6%97%BA%E5%AD%A3%E5%A0%B1%E5%88%B0-%E9%8B%BC%E5%BB%A0%E9%BD%8A%E6%BC%B210%E6%9C%88%E7%9B%A4%E5%83%B9-%E6%9C%80%E9%AB%98%E9%81%94%E5%8D%83%E5%85%83-100831359.html
- 事件6：SAP 與哈佛商業評論攜手公佈第六屆數位轉型《鼎革獎》台灣企業數位轉型進入自主營運新階段
  - 來源：Yahoo 台股；發布時間：2026-10-01T11:06:30Z；台北時間：2026-10-01 19:06
  - 摘要：【互傳媒／ 記者 陳家珍／台北報導】 SAP 台灣（思愛普軟體系統股份有限公司）與哈佛商業評論全球繁體中文版攜
  - 原文連結：https://tw.stock.yahoo.com/news/sap-%E8%88%87%E5%93%88%E4%BD%9B%E5%95%86%E6%A5%AD%E8%A9%95%E8%AB%96%E6%94%9C%E6%89%8B%E5%85%AC%E4%BD%88%E7%AC%AC%E5%85%AD%E5%B1%86%E6%95%B8%E4%BD%8D%E8%BD%89%E5%9E%8B-%E9%BC%8E%E9%9D%A9%E7%8D%8E-%E5%8F%B0%E7%81%A3%E4%BC%81%E6%A5%AD%E6%95%B8%E4%BD%8D%E8%BD%89%E5%9E%8B%E9%80%B2%E5%85%A5%E8%87%AA%E4%B8%BB%E7%87%9F%E9%81%8B%E6%96%B0%E9%9A%8E%E6%AE%B5-110630211.html
- 事件7：Federal Reserve Board finalizes changes to enhance the transparency and public accountability of its stress test and reduce volatility in its stress test-related capital requirements
  - 來源：Federal Reserve；發布時間：Wed, 30 Sep 2026 13:00:00 GMT；台北時間：2026-09-30 21:00
  - 摘要：Federal Reserve Board finalizes changes to enhance the transparency and public accountability of its stress test and reduce volatility in its stress t
  - 原文連結：https://www.federalreserve.gov/newsevents/pressreleases/bcreg20260930a.htm
- 事件8：Federal Reserve Board announces approval of application by Peoples Bancorp Inc.
  - 來源：Federal Reserve；發布時間：Fri, 25 Sep 2026 20:30:00 GMT；台北時間：2026-09-26 04:30
  - 摘要：Federal Reserve Board announces approval of application by Peoples Bancorp Inc.
  - 原文連結：https://www.federalreserve.gov/newsevents/pressreleases/orders20260925a.htm
- 事件9：Federal Reserve Board requests public comment on two proposals related to establishing a regulatory framework for Board-supervised payment stablecoin issuers under the GENIUS Act
  - 來源：Federal Reserve；發布時間：Thu, 24 Sep 2026 18:30:00 GMT；台北時間：2026-09-25 02:30
  - 摘要：Federal Reserve Board requests public comment on two proposals related to establishing a regulatory framework for Board-supervised payment stablecoin 
  - 原文連結：https://www.federalreserve.gov/newsevents/pressreleases/bcreg20260924a.htm
- 事件10：Federal Reserve Board issues enforcement action with former employee of Sandy Spring Bank
  - 來源：Federal Reserve；發布時間：Thu, 24 Sep 2026 15:00:00 GMT；台北時間：2026-09-24 23:00
  - 摘要：Federal Reserve Board issues enforcement action with former employee of Sandy Spring Bank
  - 原文連結：https://www.federalreserve.gov/newsevents/pressreleases/enforcement20260924a.htm
- 事件11：10-year Treasury yield hits highest level since 2002 as global bond rout gathers pace
  - 來源：CNBC；發布時間：Thu, 01 Oct 2026 10:22:44 GMT；台北時間：2026-10-01 18:22
  - 摘要：Treasury yields were higher on Thursday amid a global sell-off in government debt.
  - 原文連結：https://www.cnbc.com/2026/10/01/us-treasury-bond-yield.html
- 事件12：Fed's Kashkari says inflation is 'still too high' even after softer-than-expected PCE data, labor market is 'pretty good'
  - 來源：CNBC；發布時間：Wed, 30 Sep 2026 23:44:28 GMT；台北時間：2026-10-01 07:44
  - 摘要：Kashkari sat down with CNBC's Steve Liesman for an exclusive conversation Wednesday night.
  - 原文連結：https://www.cnbc.com/2026/09/30/watch-minneapolis-fed-president-neel-kashkari.html


## 三、期貨

**資料來源：**
1. Cloudflare Workers：TAIFEX Proxy — https://taifex.grichtoyang.workers.dev/
2. TAIFEX Open API — https://openapi.taifex.com.tw/

近月契約月份：202610 (日盤成交量最大者)；交易日期：2026-10-01

### 1．台指期近月日盤行情

| 項目 | 數值 | 資料來源 |
|---|---|---|
| 開盤價 | 48,398 | TAIFEX Proxy |
| 最高價 | 48,719 | TAIFEX Proxy |
| 最低價 | 48,168 | TAIFEX Proxy |
| 收盤價 | 48,685 | TAIFEX Proxy |
| 漲跌點數 | +355 | TAIFEX Proxy |
| 漲跌幅 | +0.73 | TAIFEX Proxy |
| 成交量 | 63,175 | TAIFEX Proxy |
| 日盤高點及低點 | 48,719 / 48,168 | TAIFEX Proxy |

### 2．台指期近月夜盤行情

| 項目 | 數值 | 資料來源 |
|---|---|---|
| 開盤價 | 48,320 | TAIFEX Proxy |
| 最高價 | 48,592 | TAIFEX Proxy |
| 最低價 | 48,158 | TAIFEX Proxy |
| 收盤價 | 48,298 | TAIFEX Proxy |
| 漲跌點數 | -32 | TAIFEX Proxy |
| 漲跌幅 | -0.07 | TAIFEX Proxy |
| 成交量 | 28,717 | TAIFEX Proxy |
| 夜盤高點及低點 | 48,592 / 48,158 | TAIFEX Proxy |
| 結算價 | 48,698 | TAIFEX Proxy |
| 未平倉量 | 107,607 | TAIFEX Proxy |

### 3．法人台指期多空未平倉部位

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 外資多方 OI | 12,373 | TAIFEX Proxy |
| 外資空方 OI | 91,927 | TAIFEX Proxy |
| 外資多空淨 OI | -79,554 | TAIFEX Proxy |
| 投信多方 OI | 77,476 | TAIFEX Proxy |
| 投信空方 OI | 2,861 | TAIFEX Proxy |
| 投信多空淨 OI | +74,615 | TAIFEX Proxy |
| 自營商多方 OI | 3,251 | TAIFEX Proxy |
| 自營商空方 OI | 4,691 | TAIFEX Proxy |
| 自營商多空淨 OI | -1,440 | TAIFEX Proxy |
| 三大法人合計多方 OI | 93,100 | TAIFEX Proxy |
| 三大法人合計空方 OI | 99,479 | TAIFEX Proxy |
| 三大法人合計多空淨 OI | -6,379 | TAIFEX Proxy |
| 外資多空淨 OI 變化 | -1,403 | TAIFEX Proxy |
| 投信多空淨 OI 變化 | +776 | TAIFEX Proxy |
| 自營商多空淨 OI 變化 | -370 | TAIFEX Proxy |

### 4．前十大交易人多空未平倉部位

**資料來源：** `TAIFEX OpenAPI OpenInterestOfLargeTradersFutures` (官方資料落後約一日，標示實際日期)

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 前十大交易人多方 OI | 80,962 | TAIFEX Proxy |
| 前十大交易人空方 OI | 74,433 | TAIFEX Proxy |
| 前十大交易人多空淨 OI | +6,529 | TAIFEX Proxy |
| 多空淨 OI 變化 (2026-09-29→2026-09-30) | +1,787 | TAIFEX Proxy snapshots (2026-09-30) |
- 資料日期：2026-09-30 (TypeOfTraders=0 全部交易人；契約月份 202610)

### 5．日盤、夜盤法人交易資料

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 外資日盤多單交易量 | 35,309 | TAIFEX Proxy |
| 外資日盤空單交易量 | 36,698 | TAIFEX Proxy |
| 外資日盤多空淨交易量 | -1,389 | TAIFEX Proxy |
| 外資夜盤多單交易量 | 16,127 | TAIFEX Proxy |
| 外資夜盤空單交易量 | 16,915 | TAIFEX Proxy |
| 外資夜盤多空淨交易量 | -788 | TAIFEX Proxy |
| 外資日盤／夜盤交易量變化 | -601 | TAIFEX Proxy |
| 投信日盤多空淨交易量 | +776 | TAIFEX Proxy |
| 投信夜盤多空淨交易量 | +0 | TAIFEX Proxy |
| 投信日盤／夜盤交易量變化 | +776 | TAIFEX Proxy |
| 自營商日盤多空淨交易量 | -355 | TAIFEX Proxy |
| 自營商夜盤多空淨交易量 | +463 | TAIFEX Proxy |
| 自營商日盤／夜盤交易量變化 | -818 | TAIFEX Proxy |
| 三大法人日盤多空淨交易量 | -968 | TAIFEX Proxy |
| 三大法人夜盤多空淨交易量 | -325 | TAIFEX Proxy |
| 法人日盤交易金額淨額 (億元) | -93.3 | TAIFEX Proxy |
| 法人夜盤交易金額淨額 (億元) | -31.5 | TAIFEX Proxy |

### 6．期貨與現貨關係

| 項目 | 數值 | 資料來源 |
|---|---|---|
| 台指期近月價格 | 48,685 | TAIFEX Proxy |
| 加權指數價格 | 48,353.49 | twse-proxy |
| 台指期與加權指數價差 | +331.51 | TAIFEX Proxy+twse-proxy |
| 價差百分比 | +0.69 | TAIFEX Proxy+twse-proxy |
| 日盤基差 | +331.51 | TAIFEX Proxy+twse-proxy |
| 夜盤價格相對日盤收盤的變化 | -387 | TAIFEX Proxy |

### 7．日盤、夜盤與籌碼變化對照

#### 7.1 日夜盤價格與成交量對照 (變化 = 日盤 - 夜盤)

| 項目 | 日盤 | 夜盤 | 變化 (日-夜) | 資料來源 |
|---|---|---|---|---|
| 收盤價 | 48,685 | 48,298 | +387 | TAIFEX Proxy |
| 成交量 | 34,458 | 28,717 | +5,741 | TAIFEX Proxy |
- 台指期總 OI 前日變化：-997（來源：TAIFEX Proxy）


#### 7.2 法人籌碼日夜盤對照 (淨變化 = 日盤淨 - 夜盤淨；OI 為日盤收盤後總量，前日變化另列)

| 法人 | 交易量 |  |  |  |  |  |  | 未平倉量 |  |  |  | 資料來源 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|  | **日盤多單** | **日盤空單** | **日盤淨** | **夜盤多單** | **夜盤空單** | **夜盤淨** | **淨變化 (日-夜)** | **OI多方** | **OI空方** | **OI淨** | **OI前日變化** |  |
| 外資 | 35,309 | 36,698 | -1,389 | 16,127 | 16,915 | -788 | -601 | 12,373 | 91,927 | -79,554 | -1,403 | TAIFEX Proxy |
| 投信 | 798 | 22 | +776 | 0 | 0 | +0 | +776 | 77,476 | 2,861 | +74,615 | +776 | TAIFEX Proxy |
| 自營商 | 3,020 | 3,375 | -355 | 944 | 481 | +463 | -818 | 3,251 | 4,691 | -1,440 | -370 | TAIFEX Proxy |
| 三大法人合計 | 39,127 | 40,095 | -968 | 17,071 | 17,396 | -325 | -643 | 93,100 | 99,479 | -6,379 | -997 | TAIFEX Proxy |

#### 7.3 前十大交易人日夜盤對照 (OI 無日夜拆分，列收盤後總量)

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 前十大交易人多方 OI | 80,962 | TAIFEX Proxy |
| 前十大交易人空方 OI | 74,433 | TAIFEX Proxy |
| 前十大交易人多空淨 OI | +6,529 | TAIFEX Proxy |
| 前十大交易人多空淨 OI 變化 (2026-09-29→2026-09-30) | +1,787 | TAIFEX Proxy snapshots (2026-09-30) |

#### 7.4 夜盤劇本分類 (規則對應：夜盤漲跌 × 外資夜盤偏多空)

| 項目 | 數值 | 資料來源 |
|---|---|---|
| 夜盤成交量占比 (夜盤量／(夜盤量＋日盤量)) | 45.46% | TAIFEX Proxy |
| 夜盤漲跌點數 | -32 | TAIFEX Proxy |
| 外資夜盤多空淨交易量 | -788 | TAIFEX Proxy |
| 劇本分類 | 劇本三 | 規則對應 |
| 劇本條件 | 夜盤下跌＋外資偏空 | 規則對應 |
| 劇本特徵 | 開低、續跌機率高 | 規則對應 |

## 四、選擇權

**資料來源：** 主要 TAIFEX 經 Cloudflare Worker Proxy；時區 `Asia/Taipei`

### 1．選擇權交易日期、到期日與資料時間

| 項目 | 數值 | 資料來源 |
|---|---|---|
| 交易日期 | 2026-10-01 | TAIFEX Proxy |
| 到期月份／到期日 | 202610F1 | TAIFEX Proxy |
| 資料更新時間 | 2026-10-01 19:15:47 | 本機 |
| 日盤／夜盤標記 | 日盤收盤後資料 | TAIFEX Proxy |

### 2．Call 總成交量、OI、OI 增減

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Call 總成交量 | 154,734 | TAIFEX Proxy |
| Call 總未平倉量 OI | 39,518 | TAIFEX Proxy |
| Call OI 增減 (2026-09-30→2026-10-01) | +21,390 | TAIFEX Proxy snapshots (2026-09-30) |

### 3．Put 總成交量、OI、OI 增減

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Put 總成交量 | 138,746 | TAIFEX Proxy |
| Put 總未平倉量 OI | 30,818 | TAIFEX Proxy |
| Put OI 增減 (2026-09-30→2026-10-01) | +19,404 | TAIFEX Proxy snapshots (2026-09-30) |

### 4．Call／Put 比例與變化

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Call／Put 成交量比例 | 1.12 | TAIFEX Proxy |
| Call／Put 未平倉量比例 | 1.28 | TAIFEX Proxy |
| Put／Call Ratio | 0.78 | TAIFEX Proxy |
| Call／Put 比例變化 (量比 2026-09-29→2026-09-30) | 8.81 | TAIFEX Proxy |
| 與前一交易日比較 (OI 比 2026-09-29→2026-09-30) | 5.27 | TAIFEX Proxy |
**資料來源：** 比例 `TAIFEX Proxy chain`；變化 `TAIFEX Proxy PutCallRatio`

### 5．外資 Call／Put 部位

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 外資 Call日買 | 49,630 | TAIFEX Proxy |
| 外資 Call日賣 | 49,409 | TAIFEX Proxy |
| 外資 Call日淨 | +221 | TAIFEX Proxy |
| 外資 Put日買 | 52,596 | TAIFEX Proxy |
| 外資 Put日賣 | 52,272 | TAIFEX Proxy |
| 外資 Put日淨 | +324 | TAIFEX Proxy |
| 外資 Call夜買 | 23,209 | TAIFEX Proxy |
| 外資 Call夜賣 | 23,415 | TAIFEX Proxy |
| 外資 Call夜淨 | -206 | TAIFEX Proxy |
| 外資 Put夜買 | 22,029 | TAIFEX Proxy |
| 外資 Put夜賣 | 22,179 | TAIFEX Proxy |
| 外資 Put夜淨 | -150 | TAIFEX Proxy |
| 外資 日盤淨總量 | -103 | TAIFEX Proxy |
| 外資 Call日夜淨增減 (日－夜) | +427 | TAIFEX Proxy |
| 外資 Put日夜淨增減 (日－夜) | +474 | TAIFEX Proxy |

### 6．自營商 Call／Put 部位

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 自營商 Call日買 | 42,089 | TAIFEX Proxy |
| 自營商 Call日賣 | 43,013 | TAIFEX Proxy |
| 自營商 Call日淨 | -924 | TAIFEX Proxy |
| 自營商 Put日買 | 39,052 | TAIFEX Proxy |
| 自營商 Put日賣 | 37,829 | TAIFEX Proxy |
| 自營商 Put日淨 | +1,223 | TAIFEX Proxy |
| 自營商 Call夜買 | 13,073 | TAIFEX Proxy |
| 自營商 Call夜賣 | 15,525 | TAIFEX Proxy |
| 自營商 Call夜淨 | -2,452 | TAIFEX Proxy |
| 自營商 Put夜買 | 15,708 | TAIFEX Proxy |
| 自營商 Put夜賣 | 13,229 | TAIFEX Proxy |
| 自營商 Put夜淨 | +2,479 | TAIFEX Proxy |
| 自營商 日盤淨總量 | -2,147 | TAIFEX Proxy |
| 自營商 Call日夜淨增減 (日－夜) | +1,528 | TAIFEX Proxy |
| 自營商 Put日夜淨增減 (日－夜) | -1,256 | TAIFEX Proxy |

### 7．主要 Call OI 集中區

| 項目 | 履約價 | OI | 資料來源 |
|---|---|---|---|
| Call OI 第1大履約價 | 49,000 | 2,420 | TAIFEX Proxy |
| Call OI 第2大履約價 | 52,000 | 1,695 | TAIFEX Proxy |
| Call OI 第3大履約價 | 48,800 | 1,583 | TAIFEX Proxy |
| Call OI 最大履約價 | 49,000 | 2,420 | TAIFEX Proxy |

#### Call OI 分布明細 Top10 (機器可讀，到期月份 202610F1)

| # | 履約價 | OI | 佔比 | 資料來源 |
|---|---|---|---|---|
| C1 | 49,000 | 2,420 | 6.12% | TAIFEX Proxy |
| C2 | 52,000 | 1,695 | 4.29% | TAIFEX Proxy |
| C3 | 48,800 | 1,583 | 4.01% | TAIFEX Proxy |
| C4 | 48,500 | 1,543 | 3.9% | TAIFEX Proxy |
| C5 | 50,500 | 1,479 | 3.74% | TAIFEX Proxy |
| C6 | 49,500 | 1,462 | 3.7% | TAIFEX Proxy |
| C7 | 48,600 | 1,345 | 3.4% | TAIFEX Proxy |
| C8 | 49,700 | 1,299 | 3.29% | TAIFEX Proxy |
| C9 | 50,000 | 1,278 | 3.23% | TAIFEX Proxy |
| C10 | 48,400 | 1,240 | 3.14% | TAIFEX Proxy |


### 8．主要 Put OI 集中區

| 項目 | 履約價 | OI | 資料來源 |
|---|---|---|---|
| Put OI 第1大履約價 | 48,000 | 2,297 | TAIFEX Proxy |
| Put OI 第2大履約價 | 47,600 | 2,103 | TAIFEX Proxy |
| Put OI 第3大履約價 | 47,500 | 1,805 | TAIFEX Proxy |
| Put OI 最大履約價 | 48,000 | 2,297 | TAIFEX Proxy |

#### Put OI 分布明細 Top10 (機器可讀，到期月份 202610F1)

| # | 履約價 | OI | 佔比 | 資料來源 |
|---|---|---|---|---|
| P1 | 48,000 | 2,297 | 7.45% | TAIFEX Proxy |
| P2 | 47,600 | 2,103 | 6.82% | TAIFEX Proxy |
| P3 | 47,500 | 1,805 | 5.86% | TAIFEX Proxy |
| P4 | 47,000 | 1,713 | 5.56% | TAIFEX Proxy |
| P5 | 47,900 | 1,484 | 4.82% | TAIFEX Proxy |
| P6 | 47,800 | 1,287 | 4.18% | TAIFEX Proxy |
| P7 | 47,400 | 1,036 | 3.36% | TAIFEX Proxy |
| P8 | 47,300 | 897 | 2.91% | TAIFEX Proxy |
| P9 | 47,550 | 780 | 2.53% | TAIFEX Proxy |
| P10 | 46,500 | 752 | 2.44% | TAIFEX Proxy |


### 9．Call OI 增減集中區

| 項目 | 履約價 (增減口數) | 資料來源 |
|---|---|---|
| Call OI 增加最多的履約價 | 50,500 (+1,250) | TAIFEX Proxy snapshots (2026-09-30) |
| Call OI 減少最多的履約價 | 47,150 (-9) | TAIFEX Proxy snapshots (2026-09-30) |

### 10．Put OI 增減集中區

| 項目 | 履約價 (增減口數) | 資料來源 |
|---|---|---|
| Put OI 增加最多的履約價 | 48,000 (+1,929) | TAIFEX Proxy snapshots (2026-09-30) |
| Put OI 減少最多的履約價 | 49,000 (-96) | TAIFEX Proxy snapshots (2026-09-30) |

### 11．Call Wall

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Call Wall 價位 | 49,000 | TAIFEX Proxy |
| 對應到期月份 | 202610F1 | TAIFEX Proxy |
| 與前一交易日的變化 (2026-09-30→2026-10-01) | +800 | TAIFEX Proxy snapshots (2026-09-30) |

### 12．Put Wall

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Put Wall 價位 | 48,000 | TAIFEX Proxy |
| 對應到期月份 | 202610F1 | TAIFEX Proxy |
| 與前一交易日的變化 (2026-09-30→2026-10-01) | +0 | TAIFEX Proxy snapshots (2026-09-30) |

### 13．Gamma Wall

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Gamma Wall 價位 | 47,800.00 | TAIFEX Proxy (options-market-structure-compact (proxy)) |
| 對應到期月份 | 202610F1 | TAIFEX Proxy |
| 資料日期 | 2026-09-30 | TAIFEX Proxy (options-market-structure-compact (proxy)) |

### 14．Gamma Flip

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Gamma Flip 價位 | 47,906.74 | TAIFEX Proxy (options-market-structure-compact (proxy)) |
| 對應到期月份 | 202610F1 | TAIFEX Proxy |
| 資料日期 | 2026-09-30 | TAIFEX Proxy (options-market-structure-compact (proxy)) |

### 15．Max Pain

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Max Pain 價位 | 47,950 | TAIFEX Proxy |
| 對應到期月份 | 202610F1 | TAIFEX Proxy |
| 與前一交易日的變化 (2026-09-30→2026-10-01) | -200 | TAIFEX Proxy snapshots (2026-09-30) |

### 17．選擇權法人日盤、夜盤交易

| 法人 | 日盤多單 | 日盤空單 | 日盤淨 | 夜盤多單 | 夜盤空單 | 夜盤淨 | 淨變化 (日-夜) | 資料來源 |
|---|---|---|---|---|---|---|---|---|
| 外資 | 101,902 | 102,005 | -103 | 45,388 | 45,444 | -56 | -47 | TAIFEX Proxy |
| 投信 | 0 | 2,439 | -2,439 | 0 | 0 | +0 | -2,439 | TAIFEX Proxy |
| 自營商 | 79,918 | 82,065 | -2,147 | 26,302 | 31,233 | -4,931 | +2,784 | TAIFEX Proxy |
| 三大法人合計 | 181,820 | 186,509 | -4,689 | 71,690 | 76,677 | -4,987 | +298 | TAIFEX Proxy |
- 方法論：多方＝買Call＋賣Put（看多），空方＝賣Call＋買Put（看空），淨額＝看多－看空（已用 Call／Put 拆分頁交叉驗算一致）
- 公式：多方(買)－空方(賣)＝（買call＋賣put）－（賣call＋買put）＝看多－看空
- 速記：多＝BC＋SP、空＝SC＋BP

#### 法人多空力道表（金額・億元；上游千元／1e5）

| 法人 | 日多方力道 | 日空方力道 | 日淨多空力道 | 夜多方力道 | 夜空方力道 | 夜淨多空力道 | 日淨－夜淨 | 資料來源 |
|---|---|---|---|---|---|---|---|---|
| 外資 | 8.09 | 7.98 | +0.11 | 3.60 | 3.65 | -0.05 | +0.16 | TAIFEX Proxy |
| 投信 | 0.00 | 1.83 | -1.83 | 0.00 | 0.00 | +0 | -1.83 | TAIFEX Proxy |
| 自營商 | 6.42 | 5.54 | +0.88 | 1.81 | 2.42 | -0.61 | +1.49 | TAIFEX Proxy |
| 三大法人合計 | 14.51 | 15.35 | -0.84 | 5.42 | 6.07 | -0.66 | -0.18 | TAIFEX Proxy |

### 18．選擇權前十大

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 買權多方 OI | 12,234 | TAIFEX Proxy |
| 買權空方 OI | 11,188 | TAIFEX Proxy |
| 買權多空淨 OI | +1,046 | TAIFEX Proxy |
| 買權多空淨 OI 變化 (2026-09-29→2026-09-30) | +427 | TAIFEX Proxy snapshots (2026-09-30) |

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 賣權多方 OI | 8,471 | TAIFEX Proxy |
| 賣權空方 OI | 9,095 | TAIFEX Proxy |
| 賣權多空淨 OI | -624 | TAIFEX Proxy |
| 賣權多空淨 OI 變化 (2026-09-29→2026-09-30) | +177 | TAIFEX Proxy snapshots (2026-09-30) |
- 資料日期：買權 2026-09-30／賣權 2026-09-30 (TypeOfTraders=0 全部交易人；契約月份 202610)

#### 大戶流向（全日；前十大無日夜拆分）

| 項目 | 淨變化 | 區間 | 資料來源 |
|---|---|---|---|
| 期貨前十大 | +1,787 | 2026-09-29→2026-09-30 | TAIFEX Proxy snapshots (2026-09-30) |
| 買權前十大 | +427 | 2026-09-29→2026-09-30 | TAIFEX Proxy snapshots (2026-09-30) |
| 賣權前十大 | +177 | 2026-09-29→2026-09-30 | TAIFEX Proxy snapshots (2026-09-30) |

### 16．資料來源、時間、時區與狀態

- 資料來源：TAIFEX 經 Cloudflare Worker Proxy
- 資料日期：2026-10-01；資料時間：2026-10-01 19:15:47；時區：`Asia/Taipei`
- 日盤／夜盤標記：日盤收盤後 + 夜盤盤後
- 未取得欄位 (4)：margin.fin_yi, margin.fin_chg_yi, sbl.sale_bal, sbl.sale_chg
- 註記：Gamma 資料日期 2026-09-30 (T0 2026-10-01 尚無，上游 FMTQIK 落後，採最新可得)
- 註記：法人交易量變化無昨日交易端點，標 unavailable
- 註記：Gamma Wall/Flip 資料日期 2026-09-30 (來源 options-market-structure-compact (proxy))

## 五、資料來源、時間與完整性

- 期貨/匯率為最新報價，其餘為 T0 收盤資料；時間皆為 `Asia/Taipei`。
- taiex：`twse-proxy`
- taiex_ohlc：`FinMind TaiwanStockPrice TAIEX`
- listed_turnover：`twse-proxy market_statistics`
- listed_breadth：`twse-proxy`
- otc：`TPEX OpenAPI tpex_mainborad_highlight`
- institutional：`twse-proxy /institutional`
- margin_short：`TWSE MI_MARGN + TPEX margin_balance (張)`
- margin_ratio：`前值遞補 (DATA 2026-09-30；當日三源皆失敗；民間估算；官方無每日序列)`
- sbl：`TWSE TWT93U + TPEX margin_sbl`
- 期貨選擇權：`TAIFEX Proxy`
- 新聞：台股 Yahoo／國際 Fed＋CNBC＋MarketWatch；台股 Yahoo（不足時財訊快報備援）/ 國際 Fed 公告＋CNBC＋MarketWatch RSS；Fed 無摘要；investing 港股為主已退役；cnyes CSR、wantgoo JS 算繪、中央社/台灣央行路徑待查，未採用
- 美股/亞股/期貨/匯率/ADR/商品：`Yahoo Finance Chart API`；美債：`Yahoo Finance (備援)`
- 註記：HiStock 未取得，融資餘額/增減標 unavailable (官方逐股加總僅有張數)
- 註記：融券沿用官方逐股加總 (張)
- 註記：融資維持率未取得 (三源皆失敗；官方無每日序列)
- 註記：融資維持率採前值遞補 (DATA 2026-09-30)，非 T0 2026-10-01
- 註記：上市 MI_MARGN / TWT96U 無日期欄，採用最新可得
- 本報告僅整理資料，不提供交易判斷。

## 六、期現選方向對照

**規則：** 趨勢偏多／空＝現貨、期貨OI、選擇權日淨三者同向；避險／對沖＝現貨與期選反向；日內反轉＝日淨與夜淨反向；缺值標示，不推估。選擇權多空為看多看空口徑。

| 法人 | 現貨買賣超(億) | 期貨OI淨(口) | 期貨日淨 | 期貨夜淨 | 選擇權日淨 | 選擇權夜淨 | 判定 | 期選組合 | 資料來源 |
|---|---|---|---|---|---|---|---|---|---|
| 外資 | +219.4 | -79,554 | -1,389 | -788 | -103 | -56 | 避險／對沖 | 強避險 | twse-proxy／TAIFEX Proxy |
| 投信 | +56.6 | +74,615 | +776 | +0 | -2,439 | +0 | 避險／對沖 | 分歧 | twse-proxy／TAIFEX Proxy |
| 自營商 | +16.6 | -1,440 | -355 | +463 | -2,147 | -4,931 | 避險／對沖 | 強避險 | twse-proxy／TAIFEX Proxy |
