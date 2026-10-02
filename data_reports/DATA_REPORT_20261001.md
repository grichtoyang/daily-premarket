# DATA_REPORT_20261001

- 報告日期：`2026-10-02`
- T0 交易日期：`2026-10-01`
- 資料產出時間：`2026-10-02 07:55:07`
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
| 投信 | +58.7 | 億元 | twse-proxy /institutional |
| 自營商 | +16.6 | 億元 | twse-proxy /institutional |
| 三大法人合計 | +294.6 | 億元 | twse-proxy /institutional |

### 4. 融資融券

**資料來源：** 上市+上櫃 `HiStock` (金額口徑)；維持率 `istock.tw`；備援官方逐股加總

| 項目 | 數值 | 單位 | 資料來源 |
|---|---|---|---|
| 融資餘額 | 8,487.4 | 億元 | HiStock 上市+上櫃融資融券 (金額口徑) |
| 融資增減 | +106.1 | 億元 | HiStock 上市+上櫃融資融券 (金額口徑) |
| 融券餘額 | 269,784 | 張 | HiStock 上市+上櫃融資融券 (金額口徑) |
| 融券增減 | -9,456 | 張 | HiStock 上市+上櫃融資融券 (金額口徑) |
| 融資維持率 | 195.13 | % | wantgoo＋istock 大盤融資維持率 (資料日期 2026-10-01；T0當日；補登；民間估算；官方無每日序列) |

### 5. 借券資料

**資料來源：** 上市 `TWSE OpenAPI TWT96U` (可借餘額)、上櫃 `TPEX OpenAPI tpex_margin_sbl`

| 項目 | 數值 | 單位 | 資料來源 |
|---|---|---|---|
| 借券餘額 | 4,474,807 | 張 | TWSE TWT93U + TPEX margin_sbl |
| 借券賣出餘額 | 36,462 | 張 | TWSE TWT93U + TPEX margin_sbl |
| 借券賣出增減 | -7,484 | 張 | TWSE TWT93U + TPEX margin_sbl |

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
| S&P 500 | ^GSPC | 7,666.45 | 14.91 | +0.19 | Yahoo Finance Chart API |
| Nasdaq Composite | ^IXIC | 26,871.60 | 10.54 | +0.04 | Yahoo Finance Chart API |
| Nasdaq 100 | ^NDX | 30,501.56 | 93.06 | +0.31 | Yahoo Finance Chart API |
| Dow Jones | ^DJI | 50,926.56 | 20.51 | +0.04 | Yahoo Finance Chart API |
| 費城半導體 SOX | ^SOX | 12,829.00 | 200.38 | +1.59 | Yahoo Finance Chart API |
| VIX | ^VIX | 16.39 | 0.05 | +0.31 | Yahoo Finance Chart API |

### 2. 亞洲主要指數

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 收盤／最新值 | 漲跌點 | 漲跌幅 | 資料來源 |
|---|---|---|---|---|---|
| 日經225 | ^N225 | 66,753.72 | 1,272.45 | +1.94 | Yahoo Finance Chart API |
| 韓國KOSPI | ^KS11 | 6,838.04 | -32.77 | -0.48 | Yahoo Finance Chart API |
| 香港恆生 | ^HSI | 24,613.27 | 89.70 | +0.37 | Yahoo Finance Chart API |
| 上海綜合 | 000001.SS | 3,842.20 | 11.74 | +0.31 | Yahoo Finance Chart API |
| 深圳成分 | 399001.SZ | 12,887.62 | -14.33 | -0.11 | Yahoo Finance Chart API |

### 3. 美股指數期貨

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 最新值 | 漲跌點 | 漲跌幅 | 資料來源 |
|---|---|---|---|---|---|
| S&P500期貨 | ES=F | 7,728.75 | 13.25 | +0.17 | Yahoo Finance Chart API |
| Nasdaq100期貨 | NQ=F | 30,811.75 | 113.00 | +0.37 | Yahoo Finance Chart API |
| 道瓊期貨 | YM=F | 51,257.00 | -21.00 | -0.04 | Yahoo Finance Chart API |
| Russell2000期貨 | RTY=F | 2,830.40 | 12.90 | +0.46 | Yahoo Finance Chart API |

### 4. 美國國債殖利率

**資料來源：** `U.S. Treasury Fiscal Data API` (失敗時備援 Treasury yield.xml 與 `Yahoo Finance`)

| 項目 | API 資料欄位／識別 | 殖利率 | 日變化 | 資料來源 |
|---|---|---|---|---|
| 美國 2 年期殖利率 | 2 Yr | 4.78 | 0.00 | U.S. Treasury yield.xml (網頁備援) |
| 美國 10 年期殖利率 | 10 Yr | 5.24 | -0.06 | Yahoo Finance (備援) |
| 美國 30 年期殖利率 | 30 Yr | 5.60 | -0.04 | Yahoo Finance (備援) |

### 5. 主要匯率

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 最新值 | 漲跌點 | 漲跌幅 | 資料來源 |
|---|---|---|---|---|---|
| USD/TWD | TWD=X | 31.89 | 0.02 | +0.07 | Yahoo Finance Chart API |
| DXY美元指數 | DX-Y.NYB | 102.00 | 0.55 | +0.54 | Yahoo Finance Chart API |
| USD/JPY | JPY=X | 157.91 | 0.35 | +0.22 | Yahoo Finance Chart API |
| USD/KRW | KRW=X | 1,360.52 | 3.68 | +0.27 | Yahoo Finance Chart API |

### 6. 台灣相關ADR

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 收盤／最新值 | 漲跌點 | 漲跌幅 | 資料來源 |
|---|---|---|---|---|---|
| 台積電ADR | TSM | 459.20 | 3.01 | +0.66 | Yahoo Finance Chart API |
| 聯電ADR | UMC | 25.21 | 0.72 | +2.94 | Yahoo Finance Chart API |
| 日月光ADR | ASX | 44.73 | 0.27 | +0.61 | Yahoo Finance Chart API |

### 7. 原油黃金Bitcoin

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 收盤／最新值 | 漲跌點 | 漲跌幅 | 資料來源 |
|---|---|---|---|---|---|
| WTI原油期貨 | CL=F | 92.98 | 2.56 | +2.83 | Yahoo Finance Chart API |
| 黃金期貨 | GC=F | 4,208.60 | 21.90 | +0.52 | Yahoo Finance Chart API |
| Bitcoin | BTC-USD | 84,821.28 | 1,267.43 | +1.52 | Yahoo Finance Chart API |

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
- 事件6：AI光通訊大單來了！「連接器廠」1.6T產品2027年出貨美系雙客戶　網通營收拚增逾5成
  - 來源：Yahoo 台股；發布時間：2026-10-01T23:45:00Z；台北時間：2026-10-02 07:45
  - 摘要：[FTNN新聞網]記者黃詩雯／綜合報導連接器廠詮欣（6205）加速拓展AI光通訊市場，1.6T連接器與散熱產品預計2027年出貨兩家美系客戶，加上車用鏡頭、天線新案陸...
  - 原文連結：https://tw.stock.yahoo.com/news/ai%E5%85%89%E9%80%9A%E8%A8%8A%E5%A4%A7%E5%96%AE%E4%BE%86%E4%BA%86-%E9%80%A3%E6%8E%A5%E5%99%A8%E5%BB%A0-1-6t%E7%94%A2%E5%93%812027%E5%B9%B4%E5%87%BA%E8%B2%A8%E7%BE%8E%E7%B3%BB%E9%9B%99%E5%AE%A2%E6%88%B6-%E7%B6%B2%E9%80%9A%E7%87%9F%E6%94%B6%E6%8B%9A%E5%A2%9E%E9%80%BE5%E6%88%90-234500034.html
- 事件7：Federal Reserve Board finalizes changes to enhance the transparency and public accountability of its stress test and reduce volatility in its stress test-related capital requirements
  - 來源：Federal Reserve；發布時間：Wed, 30 Sep 2026 13:00:00 GMT；台北時間：2026-09-30 21:00
  - 摘要：Federal Reserve Board finalizes changes to enhance the transparency and public accountability of its stress test and reduce volatility in its stress t
  - 原文連結：https://www.federalreserve.gov/newsevents/pressreleases/bcreg20260930a.htm
- 事件8：Federal Reserve Board announces approval of application by Peoples Bancorp Inc.
  - 來源：Federal Reserve；發布時間：Fri, 25 Sep 2026 20:30:00 GMT；台北時間：2026-09-26 04:30
  - 摘要：Federal Reserve Board announces approval of application by Peoples Bancorp Inc.
  - 原文連結：https://www.federalreserve.gov/newsevents/pressreleases/orders20260925a.htm
- 事件9：Trump could target three Fed governors. Removing them may be harder than it looks
  - 來源：CNBC；發布時間：Thu, 01 Oct 2026 21:14:49 GMT；台北時間：2026-10-02 05:14
  - 摘要：Trump could seek to remove Jerome Powell, Lisa Cook and Michael Barr from the Federal Reserve, but court rulings and lengthy litigation could limit hi
  - 原文連結：https://www.cnbc.com/2026/10/01/trump-fed-powell-lisa-cook-michael-barr-removal.html
- 事件10：Trump Accounts have auto-enrolled more than 60 million children, Treasury says
  - 來源：CNBC；發布時間：Thu, 01 Oct 2026 16:52:22 GMT；台北時間：2026-10-02 00:52
  - 摘要：More than 60 million children have been automatically enrolled in Trump Accounts, according to a Treasury Department announcement exclusively provided
  - 原文連結：https://www.cnbc.com/2026/10/01/treasury-trump-accounts-auto-enroll-more-than-60-million-children.html
- 事件11：Treasury yields fall from multiyear highs
  - 來源：CNBC；發布時間：Thu, 01 Oct 2026 21:17:31 GMT；台北時間：2026-10-02 05:17
  - 摘要：Treasury yields were higher on Thursday as investors kept selling government debt.
  - 原文連結：https://www.cnbc.com/2026/10/01/us-treasury-bond-yield.html
- 事件12：Treasury sanctions operation targets Iran's auto, rail industries in latest economic attack
  - 來源：CNBC；發布時間：Thu, 01 Oct 2026 18:37:16 GMT；台北時間：2026-10-02 02:37
  - 摘要："Operation Economic Outcast" was touted by President Donald Trump as Iran's "economic D-Day" when Treasury Secretary Scott Bessent unveiled it in Augu
  - 原文連結：https://www.cnbc.com/2026/10/01/treasury-sanctions-iran-auto-rail.html


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
| 開盤價 | 48,622 | TAIFEX Proxy |
| 最高價 | 48,661 | TAIFEX Proxy |
| 最低價 | 48,210 | TAIFEX Proxy |
| 收盤價 | 48,475 | TAIFEX Proxy |
| 漲跌點數 | -223 | TAIFEX Proxy |
| 漲跌幅 | -0.46 | TAIFEX Proxy |
| 成交量 | 28,717 | TAIFEX Proxy |
| 夜盤高點及低點 | 48,661 / 48,210 | TAIFEX Proxy |
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
| 多空淨 OI 變化 | +1,787 | TAIFEX Proxy snapshots (2026-09-30) |
- 資料日期：unavailable (TypeOfTraders=0 全部交易人；契約月份 unavailable)

### 5．日盤、夜盤法人交易資料

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 外資日盤多單交易量 | 35,309 | TAIFEX Proxy |
| 外資日盤空單交易量 | 36,698 | TAIFEX Proxy |
| 外資日盤多空淨交易量 | -1,389 | TAIFEX Proxy |
| 外資夜盤多單交易量 | 20,282 | TAIFEX Proxy |
| 外資夜盤空單交易量 | 21,659 | TAIFEX Proxy |
| 外資夜盤多空淨交易量 | -1,377 | TAIFEX Proxy |
| 外資日盤／夜盤交易量變化 | -12 | TAIFEX Proxy |
| 投信日盤多空淨交易量 | +776 | TAIFEX Proxy |
| 投信夜盤多空淨交易量 | +0 | TAIFEX Proxy |
| 投信日盤／夜盤交易量變化 | +776 | TAIFEX Proxy |
| 自營商日盤多空淨交易量 | -355 | TAIFEX Proxy |
| 自營商夜盤多空淨交易量 | +654 | TAIFEX Proxy |
| 自營商日盤／夜盤交易量變化 | -1,009 | TAIFEX Proxy |
| 三大法人日盤多空淨交易量 | -968 | TAIFEX Proxy |
| 三大法人夜盤多空淨交易量 | -723 | TAIFEX Proxy |
| 法人日盤交易金額淨額 (億元) | -93.3 | TAIFEX Proxy |
| 法人夜盤交易金額淨額 (億元) | -69.8 | TAIFEX Proxy |

### 6．期貨與現貨關係

| 項目 | 數值 | 資料來源 |
|---|---|---|
| 台指期近月價格 | 48,685 | TAIFEX Proxy |
| 加權指數價格 | 48,353.49 | twse-proxy |
| 台指期與加權指數價差 | +331.51 | TAIFEX Proxy+twse-proxy |
| 價差百分比 | +0.69 | TAIFEX Proxy+twse-proxy |
| 日盤基差 | +331.51 | TAIFEX Proxy+twse-proxy |
| 夜盤價格相對日盤收盤的變化 | -210 | TAIFEX Proxy |

### 7．日盤、夜盤與籌碼變化對照

#### 7.1 日夜盤價格與成交量對照 (變化 = 日盤 - 夜盤)

| 項目 | 日盤 | 夜盤 | 變化 (日-夜) | 資料來源 |
|---|---|---|---|---|
| 收盤價 | 48,685 | 48,475 | +210 | TAIFEX Proxy |
| 成交量 | 34,458 | 28,717 | +5,741 | TAIFEX Proxy |
- 台指期總 OI 前日變化：-997（來源：TAIFEX Proxy）


#### 7.2 法人籌碼日夜盤對照 (淨變化 = 日盤淨 - 夜盤淨；OI 為日盤收盤後總量，前日變化另列)

| 法人 | 交易量 |  |  |  |  |  |  | 未平倉量 |  |  |  | 資料來源 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|  | **日盤多單** | **日盤空單** | **日盤淨** | **夜盤多單** | **夜盤空單** | **夜盤淨** | **淨變化 (日-夜)** | **OI多方** | **OI空方** | **OI淨** | **OI前日變化** |  |
| 外資 | 35,309 | 36,698 | -1,389 | 20,282 | 21,659 | -1,377 | -12 | 12,373 | 91,927 | -79,554 | -1,403 | TAIFEX Proxy |
| 投信 | 798 | 22 | +776 | 0 | 0 | +0 | +776 | 77,476 | 2,861 | +74,615 | +776 | TAIFEX Proxy |
| 自營商 | 3,020 | 3,375 | -355 | 1,505 | 851 | +654 | -1,009 | 3,251 | 4,691 | -1,440 | -370 | TAIFEX Proxy |
| 三大法人合計 | 39,127 | 40,095 | -968 | 21,787 | 22,510 | -723 | -245 | 93,100 | 99,479 | -6,379 | -997 | TAIFEX Proxy |

#### 7.3 前十大交易人日夜盤對照 (OI 無日夜拆分，列收盤後總量)

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 前十大交易人多方 OI | 80,962 | TAIFEX Proxy |
| 前十大交易人空方 OI | 74,433 | TAIFEX Proxy |
| 前十大交易人多空淨 OI | +6,529 | TAIFEX Proxy |
| 前十大交易人多空淨 OI 變化 | +1,787 | TAIFEX Proxy snapshots (2026-09-30) |

#### 7.4 夜盤劇本分類 (規則對應：夜盤漲跌 × 外資夜盤偏多空)

| 項目 | 數值 | 資料來源 |
|---|---|---|
| 夜盤成交量占比 (夜盤量／(夜盤量＋日盤量)) | 45.46% | TAIFEX Proxy |
| 夜盤漲跌點數 | -223 | TAIFEX Proxy |
| 外資夜盤多空淨交易量 | -1,377 | TAIFEX Proxy |
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
| 資料更新時間 | 2026-10-02 07:55:07 | 本機 |
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
| Call／Put 比例變化 (量比 2026-09-30→2026-10-01) | -8.09 | TAIFEX Proxy |
| 與前一交易日比較 (OI 比 2026-09-30→2026-10-01) | 1.97 | TAIFEX Proxy |
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
| 外資 Call夜買 | 52,503 | TAIFEX Proxy |
| 外資 Call夜賣 | 52,350 | TAIFEX Proxy |
| 外資 Call夜淨 | +153 | TAIFEX Proxy |
| 外資 Put夜買 | 48,191 | TAIFEX Proxy |
| 外資 Put夜賣 | 47,677 | TAIFEX Proxy |
| 外資 Put夜淨 | +514 | TAIFEX Proxy |
| 外資 日盤淨總量 | -103 | TAIFEX Proxy |
| 外資 Call日夜淨增減 (日－夜) | +68 | TAIFEX Proxy |
| 外資 Put日夜淨增減 (日－夜) | -190 | TAIFEX Proxy |

### 6．自營商 Call／Put 部位

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 自營商 Call日買 | 42,089 | TAIFEX Proxy |
| 自營商 Call日賣 | 43,013 | TAIFEX Proxy |
| 自營商 Call日淨 | -924 | TAIFEX Proxy |
| 自營商 Put日買 | 39,052 | TAIFEX Proxy |
| 自營商 Put日賣 | 37,829 | TAIFEX Proxy |
| 自營商 Put日淨 | +1,223 | TAIFEX Proxy |
| 自營商 Call夜買 | 25,486 | TAIFEX Proxy |
| 自營商 Call夜賣 | 29,000 | TAIFEX Proxy |
| 自營商 Call夜淨 | -3,514 | TAIFEX Proxy |
| 自營商 Put夜買 | 24,828 | TAIFEX Proxy |
| 自營商 Put夜賣 | 24,489 | TAIFEX Proxy |
| 自營商 Put夜淨 | +339 | TAIFEX Proxy |
| 自營商 日盤淨總量 | -2,147 | TAIFEX Proxy |
| 自營商 Call日夜淨增減 (日－夜) | +2,590 | TAIFEX Proxy |
| 自營商 Put日夜淨增減 (日－夜) | +884 | TAIFEX Proxy |

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
| Call 最大 OI 履約價增減 (Call Wall 49,000) | 49,000 (+980) | TAIFEX Proxy snapshots (2026-09-30) |

### 10．Put OI 增減集中區

| 項目 | 履約價 (增減口數) | 資料來源 |
|---|---|---|
| Put OI 增加最多的履約價 | 48,000 (+1,929) | TAIFEX Proxy snapshots (2026-09-30) |
| Put OI 減少最多的履約價 | 49,000 (-96) | TAIFEX Proxy snapshots (2026-09-30) |
| Put 最大 OI 履約價增減 (Put Wall 48,000) | 48,000 (+1,929) | TAIFEX Proxy snapshots (2026-09-30) |

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
| Gamma Wall 價位 | 48,500.00 | TAIFEX Proxy (options-gamma-levels) |
| 對應到期月份 | 202610F1 | TAIFEX Proxy |
| 資料日期 | 2026-10-01 | TAIFEX Proxy (options-gamma-levels) |

### 14．Gamma Flip

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Gamma Flip 價位 | 48,161.56 | TAIFEX Proxy (options-gamma-levels) |
| 對應到期月份 | 202610F1 | TAIFEX Proxy |
| 資料日期 | 2026-10-01 | TAIFEX Proxy (options-gamma-levels) |

### 15．Max Pain

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Max Pain 價位 | 47,950 | TAIFEX Proxy |
| 對應到期月份 | 202610F1 | TAIFEX Proxy |
| 與前一交易日的變化 (2026-09-30→2026-10-01) | -200 | TAIFEX Proxy snapshots (2026-09-30) |

### 17．選擇權法人日盤、夜盤交易

| 法人 | 日盤多單 | 日盤空單 | 日盤淨 | 夜盤多單 | 夜盤空單 | 夜盤淨 | 淨變化 (日-夜) | 資料來源 |
|---|---|---|---|---|---|---|---|---|
| 外資 | 101,902 | 102,005 | -103 | 100,180 | 100,541 | -361 | +258 | TAIFEX Proxy |
| 投信 | 0 | 2,439 | -2,439 | 0 | 0 | +0 | -2,439 | TAIFEX Proxy |
| 自營商 | 79,918 | 82,065 | -2,147 | 49,975 | 53,828 | -3,853 | +1,706 | TAIFEX Proxy |
| 三大法人合計 | 181,820 | 186,509 | -4,689 | 150,155 | 154,369 | -4,214 | -475 | TAIFEX Proxy |
- 方法論：多方＝買Call＋賣Put（看多），空方＝賣Call＋買Put（看空），淨額＝看多－看空（已用 Call／Put 拆分頁交叉驗算一致）
- 公式：多方(買)－空方(賣)＝（買call＋賣put）－（賣call＋買put）＝看多－看空
- 速記：多＝BC＋SP、空＝SC＋BP

#### 法人多空力道表（金額・億元；上游千元／1e5）

| 法人 | 日多方力道 | 日空方力道 | 日淨多空力道 | 夜多方力道 | 夜空方力道 | 夜淨多空力道 | 日淨－夜淨 | 資料來源 |
|---|---|---|---|---|---|---|---|---|
| 外資 | 8.09 | 7.98 | +0.11 | 6.17 | 6.17 | +0.00 | +0.11 | TAIFEX Proxy |
| 投信 | 0.00 | 1.83 | -1.83 | 0.00 | 0.00 | +0 | -1.83 | TAIFEX Proxy |
| 自營商 | 6.42 | 5.54 | +0.88 | 2.56 | 3.03 | -0.46 | +1.34 | TAIFEX Proxy |
| 三大法人合計 | 14.51 | 15.35 | -0.84 | 8.74 | 9.19 | -0.46 | -0.38 | TAIFEX Proxy |

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
| 期貨前十大 | +1,787 | — | TAIFEX Proxy snapshots (2026-09-30) |
| 買權前十大 | +427 | 2026-09-29→2026-09-30 | TAIFEX Proxy snapshots (2026-09-30) |
| 賣權前十大 | +177 | 2026-09-29→2026-09-30 | TAIFEX Proxy snapshots (2026-09-30) |

### 16．資料來源、時間、時區與狀態

- 資料來源：TAIFEX 經 Cloudflare Worker Proxy
- 資料日期：2026-10-01；資料時間：2026-10-02 07:55:07；時區：`Asia/Taipei`
- 日盤／夜盤標記：日盤收盤後 + 夜盤盤後
- 註記：同 T0 保護：9 格沿用前版有值（本次抓取缺失不覆寫）
- 未取得欄位 (1)：futures.top10_change
- 註記：夜盤 OHLC 資料日期 2026-10-02 (T0 2026-10-01)，來源 proxy
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
- margin_ratio：`wantgoo＋istock 大盤融資維持率 (資料日期 2026-10-01；T0當日；補登；民間估算；官方無每日序列)`
- sbl：`TWSE TWT93U + TPEX margin_sbl`
- 期貨選擇權：`TAIFEX Proxy`
- 新聞：台股 Yahoo／國際 Fed＋CNBC＋MarketWatch；台股 Yahoo（不足時財訊快報備援）/ 國際 Fed 公告＋CNBC＋MarketWatch RSS；Fed 無摘要；investing 港股為主已退役；cnyes CSR、wantgoo JS 算繪、中央社/台灣央行路徑待查，未採用
- 美股/亞股/期貨/匯率/ADR/商品：`Yahoo Finance Chart API`；美債：`Yahoo Finance (備援)`
- 註記：融資維持率 195.13 為補登（T0 當日值；wantgoo 195.13＋istock 195.08 雙源共識；晨跑 runner 端被擋，詳 HANDOFF）
- 註記：上市 MI_MARGN / TWT96U 無日期欄，採用最新可得
- 註記：借券賣出增減僅上櫃值 (TWSE TWT93U 未取得)
- 本報告僅整理資料，不提供交易判斷。

## 六、期現選方向對照

**規則：** 趨勢偏多／空＝現貨、期貨OI、選擇權日淨三者同向；避險／對沖＝現貨與期選反向；日內反轉＝日淨與夜淨反向；缺值標示，不推估。選擇權多空為看多看空口徑。

| 法人 | 現貨買賣超(億) | 期貨OI淨(口) | 期貨日淨 | 期貨夜淨 | 選擇權日淨 | 選擇權夜淨 | 判定 | 期選組合 | 資料來源 |
|---|---|---|---|---|---|---|---|---|---|
| 外資 | +219.4 | -79,554 | -1,389 | -1,377 | -103 | -361 | 避險／對沖 | 強避險 | twse-proxy／TAIFEX Proxy |
| 投信 | +58.7 | +74,615 | +776 | +0 | -2,439 | +0 | 避險／對沖 | 分歧 | twse-proxy／TAIFEX Proxy |
| 自營商 | +16.6 | -1,440 | -355 | +654 | -2,147 | -3,853 | 避險／對沖 | 強避險 | twse-proxy／TAIFEX Proxy |
