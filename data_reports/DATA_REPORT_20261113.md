# DATA_REPORT_20261113

- 報告日期：`2026-11-14`
- T0 交易日期：`2026-11-13`
- 資料產出時間：`2026-11-14 13:01:49`
- 時區：`Asia/Taipei`
- 產出盤別：`全日`
- 產出者：`actions`
- 排定班別：`weekend`

---

## 一、現貨

### 1. 台股大盤行情

**資料來源：** `Cloudflare Worker：twse-proxy` (備援 `TWSE OpenAPI MI_INDEX`)

| 項目 | 數值 | 單位 | 資料來源 |
|---|---|---|---|
| 加權指數 | 43,675.12 | 點 | twse-proxy |
| 開盤 | 43,719.75 | 點 | FinMind TaiwanStockPrice TAIEX |
| 最高 | 44,489.48 | 點 | FinMind TaiwanStockPrice TAIEX |
| 最低 | 43,534.12 | 點 | FinMind TaiwanStockPrice TAIEX |
| 收盤 | 43,675.12 | 點 | twse-proxy |
| 漲跌點數 | 583.25 | 點 | twse-proxy |
| 漲跌幅 | +1.35 | % | twse-proxy |
| 成交金額 | 9,515.8 | 億元 | twse-proxy market_statistics |

### 2. 市場漲跌家數

#### 2.1 上市公司

**資料來源：** `Cloudflare Worker：twse-proxy` (備援 `TWSE OpenAPI twtazu_od`)

| 項目 | 家數 | 資料來源 |
|---|---|---|
| 上漲家數 | 811 | twse-proxy |
| 下跌家數 | 199 | twse-proxy |
| 平盤家數 | 74 | twse-proxy |
| 漲停家數 | 28 | twse-proxy |
| 跌停家數 | 3 | twse-proxy |

#### 2.2 上櫃公司

**資料來源：** `TPEX OpenAPI tpex_mainborad_highlight`

| 項目 | 家數 | 資料來源 |
|---|---|---|
| 上漲家數 | 584 | TPEX OpenAPI tpex_mainborad_highlight |
| 下跌家數 | 230 | TPEX OpenAPI tpex_mainborad_highlight |
| 平盤家數 | 62 | TPEX OpenAPI tpex_mainborad_highlight |
| 漲停家數 | 41 | TPEX OpenAPI tpex_mainborad_highlight |
| 跌停家數 | 1 | TPEX OpenAPI tpex_mainborad_highlight |

### 3. 三大法人現貨買賣超

**資料來源：** `TWSE RWD BFI82U`

| 法人別 | 買賣超金額 | 單位 | 資料來源 |
|---|---|---|---|
| 外資 | +288.4 | 億元 | twse-proxy /institutional |
| 投信 | +95.4 | 億元 | twse-proxy /institutional |
| 自營商 | +68.9 | 億元 | twse-proxy /institutional |
| 三大法人合計 | +452.7 | 億元 | twse-proxy /institutional |

### 4. 融資融券

**資料來源：** 上市+上櫃 `HiStock` (金額口徑)；維持率 `istock.tw`；備援官方逐股加總

| 項目 | 數值 | 單位 | 資料來源 |
|---|---|---|---|
| 融資餘額 | 7,086.2 | 億元 | HiStock 上市+上櫃融資融券 (金額口徑) |
| 融資增減 | +50.5 | 億元 | HiStock 上市+上櫃融資融券 (金額口徑) |
| 融券餘額 | 245,881 | 張 | HiStock 上市+上櫃融資融券 (金額口徑) |
| 融券增減 | -589 | 張 | HiStock 上市+上櫃融資融券 (金額口徑) |
| 融資維持率 | 170.70 | % | stockintelli 大盤融資維持率 (民間估算；官方無每日序列) |

### 5. 借券資料

**資料來源：** 上市 `TWSE OpenAPI TWT96U` (可借餘額)、上櫃 `TPEX OpenAPI tpex_margin_sbl`

| 項目 | 數值 | 單位 | 資料來源 |
|---|---|---|---|
| 借券餘額 | 2,494,875 | 張 | TWSE TWT93U + TPEX margin_sbl |
| 借券賣出餘額 | 37,108 | 張 | TWSE TWT93U + TPEX margin_sbl |
| 借券賣出增減 | 1,160 | 張 | TWSE TWT93U + TPEX margin_sbl |

### 6. 市場成交結構

**資料來源：** 上市 `twse-proxy market_statistics`、上櫃 `TPEX OpenAPI tpex_mainborad_highlight`

| 項目 | 成交金額 | 單位 | 資料來源 |
|---|---|---|---|
| 上市成交金額 | 9,515.8 | 億元 | twse-proxy market_statistics |
| 上櫃成交金額 | 2,183.5 | 億元 | TPEX OpenAPI tpex_mainborad_highlight |
| 上市櫃成交金額合計 | 11,699.3 | 億元 | twse-proxy market_statistics+TPEX OpenAPI tpex_mainborad_highlight |

## 二、重要市場

### 1. 美股指數

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 收盤／最新值 | 漲跌點 | 漲跌幅 | 資料來源 |
|---|---|---|---|---|---|
| S&P 500 | ^GSPC | 7,561.67 | -30.73 | -0.40 | Yahoo Finance Chart API |
| Nasdaq Composite | ^IXIC | 25,136.27 | -229.82 | -0.91 | Yahoo Finance Chart API |
| Nasdaq 100 | ^NDX | 27,943.74 | -345.45 | -1.22 | Yahoo Finance Chart API |
| Dow Jones | ^DJI | 52,347.55 | 50.46 | +0.10 | Yahoo Finance Chart API |
| 費城半導體 SOX | ^SOX | 10,146.32 | -360.35 | -3.43 | Yahoo Finance Chart API |
| VIX | ^VIX | 19.30 | 0.60 | +3.21 | Yahoo Finance Chart API |

### 2. 亞洲主要指數

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 收盤／最新值 | 漲跌點 | 漲跌幅 | 資料來源 |
|---|---|---|---|---|---|
| 日經225 | ^N225 | 61,142.35 | 322.99 | +0.53 | Yahoo Finance Chart API |
| 韓國KOSPI | ^KS11 | 5,290.53 | -52.20 | -0.98 | Yahoo Finance Chart API |
| 香港恆生 | ^HSI | 23,637.60 | -370.95 | -1.55 | Yahoo Finance Chart API |
| 上海綜合 | 000001.SS | 3,634.35 | -21.48 | -0.59 | Yahoo Finance Chart API |
| 深圳成分 | 399001.SZ | 10,968.79 | -229.19 | -2.05 | Yahoo Finance Chart API |

### 3. 美股指數期貨

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 最新值 | 漲跌點 | 漲跌幅 | 資料來源 |
|---|---|---|---|---|---|
| S&P500期貨 | ES=F | 7,583.00 | -32.25 | -0.42 | Yahoo Finance Chart API |
| Nasdaq100期貨 | NQ=F | 28,034.75 | -349.75 | -1.23 | Yahoo Finance Chart API |
| 道瓊期貨 | YM=F | 52,418.00 | 28.00 | +0.05 | Yahoo Finance Chart API |
| Russell2000期貨 | RTY=F | 2,797.50 | -9.80 | -0.35 | Yahoo Finance Chart API |

### 4. 美國國債殖利率

**資料來源：** `U.S. Treasury Fiscal Data API` (失敗時備援 Treasury yield.xml 與 `Yahoo Finance`)

| 項目 | API 資料欄位／識別 | 殖利率 | 日變化 | 資料來源 |
|---|---|---|---|---|
| 美國 2 年期殖利率 | 2 Yr | 4.88 | 0.02 | U.S. Treasury yield.xml (網頁備援) |
| 美國 10 年期殖利率 | 10 Yr | 5.15 | 0.05 | Yahoo Finance (備援) |
| 美國 30 年期殖利率 | 30 Yr | 5.48 | 0.05 | Yahoo Finance (備援) |

### 5. 主要匯率

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 最新值 | 漲跌點 | 漲跌幅 | 資料來源 |
|---|---|---|---|---|---|
| USD/TWD | TWD=X | 32.94 | 0.08 | +0.23 | Yahoo Finance Chart API |
| DXY美元指數 | DX-Y.NYB | 103.41 | 0.24 | +0.23 | Yahoo Finance Chart API |
| USD/JPY | JPY=X | 159.88 | 0.14 | +0.09 | Yahoo Finance Chart API |
| USD/KRW | KRW=X | 1,336.20 | 2.42 | +0.18 | Yahoo Finance Chart API |

### 6. 台灣相關ADR

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 收盤／最新值 | 漲跌點 | 漲跌幅 | 資料來源 |
|---|---|---|---|---|---|
| 台積電ADR | TSM | 398.73 | -6.76 | -1.67 | Yahoo Finance Chart API |
| 聯電ADR | UMC | 15.40 | -0.36 | -2.28 | Yahoo Finance Chart API |
| 日月光ADR | ASX | 35.55 | -0.74 | -2.04 | Yahoo Finance Chart API |

### 7. 原油黃金Bitcoin

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 收盤／最新值 | 漲跌點 | 漲跌幅 | 資料來源 |
|---|---|---|---|---|---|
| WTI原油期貨 | CL=F | 88.56 | -0.18 | -0.20 | Yahoo Finance Chart API |
| 黃金期貨 | GC=F | 3,886.30 | 1.00 | +0.03 | Yahoo Finance Chart API |
| Bitcoin | BTC-USD | 66,890.70 | -4,452.27 | -6.24 | Yahoo Finance Chart API |

### 8. 重大經濟數據、央行事件與重大市場新聞

**資料來源：** 台股 `tw.stock.yahoo.com` (含內文摘要)；國際 `Fed 公告 RSS`＋`CNBC`＋`MarketWatch` (標題、來源、時間與連結)

- 事件1：股災後想搭反彈列車？蔡明翰提醒1操作禁忌：槓桿別再疊槓桿
  - 來源：Yahoo 台股；發布時間：2026-11-14T00:30:00Z；台北時間：2026-11-14 08:30
  - 摘要：[FTNN新聞網]記者陳宣穎／綜合報導台股11月上旬走勢震盪，相關ETF也隨行情劇烈起伏，隨著市場逐步回穩，元大台灣50（0050）13日來到102.5元，較6日低點92.5元...
  - 原文連結：https://tw.stock.yahoo.com/news/%E8%82%A1%E7%81%BD%E5%BE%8C%E6%83%B3%E6%90%AD%E5%8F%8D%E5%BD%88%E5%88%97%E8%BB%8A-%E8%94%A1%E6%98%8E%E7%BF%B0%E6%8F%90%E9%86%921%E6%93%8D%E4%BD%9C%E7%A6%81%E5%BF%8C-%E6%A7%93%E6%A1%BF%E5%88%A5%E5%86%8D%E7%96%8A%E6%A7%93%E6%A1%BF-003000751.html
- 事件2：本周爆款短影音｜「溫暖牽手」石舫亘代蔣萬安掃街催票／男師輕生！家屬淚訴遭學生羞辱
  - 來源：Yahoo 台股；發布時間：2026-11-13T23:30:00Z；台北時間：2026-11-14 07:30
  - 摘要：【知新聞編輯部／台北報導】因為生活節奏太過匆忙，常感到與新聞時事脫節？《知新聞》體貼您的忙碌，特別推出「本周爆款短影音」精選推薦！我們將這個禮拜最重要的政經社會要事、最有趣的生活趣聞，以及最震撼的國際焦點，濃縮成數則高效率的短影音。讓您無需
  - 原文連結：https://tw.stock.yahoo.com/news/%E6%9C%AC%E5%91%A8%E7%88%86%E6%AC%BE%E7%9F%AD%E5%BD%B1%E9%9F%B3-%E6%BA%AB%E6%9A%96%E7%89%BD%E6%89%8B-%E7%9F%B3%E8%88%AB%E4%BA%98%E4%BB%A3%E8%94%A3%E8%90%AC%E5%AE%89%E6%8E%83%E8%A1%97%E5%82%AC%E7%A5%A8-%E7%94%B7%E5%B8%AB%E8%BC%95%E7%94%9F-%E5%AE%B6%E5%B1%AC%E6%B7%9A%E8%A8%B4%E9%81%AD%E5%AD%B8%E7%94%9F%E7%BE%9E%E8%BE%B1-233000351.html
- 事件3：輝達邁入後黃仁勳時代　專家指繼任者將面臨兩大挑戰
  - 來源：Yahoo 台股；發布時間：2026-11-13T23:00:00Z；台北時間：2026-11-14 07:00
  - 摘要：【財經中心／台北報導】輝達創辦人黃仁勳因為婚外情事件請辭執行長職務，由財務長克雷斯暫時代理CEO，董事會正在尋找正式繼任者。多位分析人士認為，黃仁勳的離職有特殊性，在AI產業蓬勃發展、輝達處於產業核心地位之際，黃仁勳突然辭去CEO職務，其繼
  - 原文連結：https://tw.stock.yahoo.com/news/%E8%BC%9D%E9%81%94%E9%82%81%E5%85%A5%E5%BE%8C%E9%BB%83%E4%BB%81%E5%8B%B3%E6%99%82%E4%BB%A3-%E5%B0%88%E5%AE%B6%E6%8C%87%E7%B9%BC%E4%BB%BB%E8%80%85%E5%B0%87%E9%9D%A2%E8%87%A8%E5%85%A9%E5%A4%A7%E6%8C%91%E6%88%B0-230000345.html
- 事件4：李濠仲專欄：黃仁勳犯了和員工談戀愛大忌
  - 來源：Yahoo 台股；發布時間：2026-11-13T22:02:00Z；台北時間：2026-11-14 06:02
  - 摘要：起初，黃仁勳被揭露和中國籍商場女子黃樂有婚外情，儘管輿論沸沸揚揚，甚至懷疑黃樂是帶有特殊任務的間諜，但當時輝達內部，多數仍支持黃仁勳繼續帶領公司，新聞延燒的同一時間，
  - 原文連結：https://tw.stock.yahoo.com/news/%E6%9D%8E%E6%BF%A0%E4%BB%B2%E5%B0%88%E6%AC%84-%E9%BB%83%E4%BB%81%E5%8B%B3%E7%8A%AF%E4%BA%86%E5%92%8C%E5%93%A1%E5%B7%A5%E8%AB%87%E6%88%80%E6%84%9B%E5%A4%A7%E5%BF%8C-220200061.html
- 事件5：台股受黃仁勳事件干擾、一周內仍急拉3973點　外資連續11周買超這幾檔股票
  - 來源：Yahoo 台股；發布時間：2026-11-13T19:40:00Z；台北時間：2026-11-14 03:40
  - 摘要：台股本周一在國安基金宣示進場之下，一周內大漲3973點，收在43675.12點...
  - 原文連結：https://tw.stock.yahoo.com/news/%E5%8F%B0%E8%82%A1%E5%8F%97%E9%BB%83%E4%BB%81%E5%8B%B3%E4%BA%8B%E4%BB%B6%E5%B9%B2%E6%93%BE-%E5%91%A8%E5%85%A7%E4%BB%8D%E6%80%A5%E6%8B%893973%E9%BB%9E-%E5%A4%96%E8%B3%87%E9%80%A3%E7%BA%8C11%E5%91%A8%E8%B2%B7%E8%B6%85%E9%80%99%E5%B9%BE%E6%AA%94%E8%82%A1%E7%A5%A8-194000943.html
- 事件6：想抱股10年！「0050 vs. 0052」怎選 網推這檔：永遠火車頭
  - 來源：Yahoo 台股；發布時間：2026-11-13T11:15:00Z；台北時間：2026-11-13 19:15
  - 摘要：元大台灣50（0050）與富邦科技（0052）都是投資新手青睞的熱門標的。一名剛開證券戶的網友表示，打算定期定額長期投資10年，不知二者該如何選擇，引發討論。
  - 原文連結：https://tw.stock.yahoo.com/news/%E6%83%B3%E6%8A%B1%E8%82%A110%E5%B9%B4-0050-vs-0052-%E6%80%8E%E9%81%B8-111500414.html
- 事件7：Federal Reserve Board announces pricing, effective January 1, 2027, for payment services the Federal Reserve Banks provide to banks and credit unions, and changes to streamline and adjust their check services
  - 來源：Federal Reserve；發布時間：Thu, 12 Nov 2026 18:30:00 GMT；台北時間：2026-11-13 02:30
  - 摘要：Federal Reserve Board announces pricing, effective January 1, 2027, for payment services the Federal Reserve Banks provide to banks and credit unions,
  - 原文連結：https://www.federalreserve.gov/newsevents/pressreleases/other20261112a.htm
- 事件8：Federal Reserve announces revised tentative schedule of Federal Open Market Committee meetings in 2027
  - 來源：Federal Reserve；發布時間：Thu, 12 Nov 2026 17:45:00 GMT；台北時間：2026-11-13 01:45
  - 摘要：Federal Reserve announces revised tentative schedule of Federal Open Market Committee meetings in 2027
  - 原文連結：https://www.federalreserve.gov/newsevents/pressreleases/monetary20261112a.htm
- 事件9：Federal Reserve Board issues enforcement action with former employee of United Community Bank
  - 來源：Federal Reserve；發布時間：Thu, 12 Nov 2026 16:00:00 GMT；台北時間：2026-11-13 00:00
  - 摘要：Federal Reserve Board issues enforcement action with former employee of United Community Bank
  - 原文連結：https://www.federalreserve.gov/newsevents/pressreleases/enforcement20261112a.htm
- 事件10：Federal Reserve Board announces approval of two applications by Mutual Federal Bancorp, MHC, and MFB Bancorp, Inc.
  - 來源：Federal Reserve；發布時間：Mon, 9 Nov 2026 21:00:00 GMT；台北時間：2026-11-10 05:00
  - 摘要：Federal Reserve Board announces approval of two applications by Mutual Federal Bancorp, MHC, and MFB Bancorp, Inc.
  - 原文連結：https://www.federalreserve.gov/newsevents/pressreleases/orders20261109a.htm
- 事件11：AI risks are the biggest threat to the financial system, Fed survey finds
  - 來源：CNBC；發布時間：Fri, 13 Nov 2026 21:18:30 GMT；台北時間：2026-11-14 05:18
  - 摘要：The report comes with Wall Street on edge over high-flying AI hyperscalers, while communities are on alert for the rapid spread of data centers.
  - 原文連結：https://www.cnbc.com/2026/11/13/ai-risks-financial-system-federal-reserve.html
- 事件12：Chicago Fed's Goolsbee says central bank 'has definitely got work to do' on inflation
  - 來源：CNBC；發布時間：Fri, 13 Nov 2026 14:22:07 GMT；台北時間：2026-11-13 22:22
  - 摘要：The policymaker expressed concern about the latest inflation data, telling CNBC that the central bank likely will need to take action.
  - 原文連結：https://www.cnbc.com/2026/11/13/chicago-feds-goolsbee-says-central-bank-has-definitely-got-work-to-do-on-inflation.html


## 三、期貨

**資料來源：**
1. Cloudflare Workers：TAIFEX Proxy — https://taifex.grichtoyang.workers.dev/
2. TAIFEX Open API — https://openapi.taifex.com.tw/

近月契約月份：202611 (日盤成交量最大者)；交易日期：2026-11-13

### 1．台指期近月日盤行情

| 項目 | 數值 | 資料來源 |
|---|---|---|
| 開盤價 | 43,925 | TAIFEX Proxy |
| 最高價 | 44,824 | TAIFEX Proxy |
| 最低價 | 43,692 | TAIFEX Proxy |
| 收盤價 | 43,834 | TAIFEX Proxy |
| 漲跌點數 | +706 | TAIFEX Proxy |
| 漲跌幅 | +1.64 | TAIFEX Proxy |
| 成交量 | 94,919 | TAIFEX Proxy |
| 日盤高點及低點 | 44,824 / 43,692 | TAIFEX Proxy |

### 2．台指期近月夜盤行情

| 項目 | 數值 | 資料來源 |
|---|---|---|
| 開盤價 | 43,921 | TAIFEX Proxy |
| 最高價 | 44,423 | TAIFEX Proxy |
| 最低價 | 42,956 | TAIFEX Proxy |
| 收盤價 | 43,706 | TAIFEX Proxy |
| 漲跌點數 | -133 | TAIFEX Proxy |
| 漲跌幅 | -0.30 | TAIFEX Proxy |
| 成交量 | 56,132 | TAIFEX Proxy |
| 夜盤高點及低點 | 44,423 / 42,956 | TAIFEX Proxy |
| 結算價 | unavailable | TAIFEX Proxy |
| 未平倉量 | unavailable | TAIFEX Proxy |

### 3．法人台指期多空未平倉部位

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 外資多方 OI | 6,186 | TAIFEX Proxy |
| 外資空方 OI | 107,056 | TAIFEX Proxy |
| 外資多空淨 OI | -100,870 | TAIFEX Proxy |
| 投信多方 OI | 103,019 | TAIFEX Proxy |
| 投信空方 OI | 3,096 | TAIFEX Proxy |
| 投信多空淨 OI | +99,923 | TAIFEX Proxy |
| 自營商多方 OI | 3,733 | TAIFEX Proxy |
| 自營商空方 OI | 6,504 | TAIFEX Proxy |
| 自營商多空淨 OI | -2,771 | TAIFEX Proxy |
| 三大法人合計多方 OI | 112,938 | TAIFEX Proxy |
| 三大法人合計空方 OI | 116,656 | TAIFEX Proxy |
| 三大法人合計多空淨 OI | -3,718 | TAIFEX Proxy |
| 外資多空淨 OI 變化 | -1,297 | TAIFEX Proxy |
| 投信多空淨 OI 變化 | +1,022 | TAIFEX Proxy |
| 自營商多空淨 OI 變化 | -2,584 | TAIFEX Proxy |

### 4．前十大交易人多空未平倉部位

**資料來源：** `TAIFEX OpenAPI OpenInterestOfLargeTradersFutures` (官方資料落後約一日，標示實際日期)

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 前十大交易人多方 OI | 91,547 | TAIFEX Proxy |
| 前十大交易人空方 OI | 71,991 | TAIFEX Proxy |
| 前十大交易人多空淨 OI | +19,556 | TAIFEX Proxy |
| 多空淨 OI 變化 (2026-11-11→2026-11-13) | -192 | TAIFEX Proxy snapshots (2026-11-12) |
- 資料日期：2026-11-13 (TypeOfTraders=0 全部交易人；契約月份 202611)

### 5．日盤、夜盤法人交易資料

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 外資日盤多單交易量 | 104,183 | TAIFEX Proxy |
| 外資日盤空單交易量 | 105,480 | TAIFEX Proxy |
| 外資日盤多空淨交易量 | -1,297 | TAIFEX Proxy |
| 外資夜盤多單交易量 | 30,221 | TAIFEX Proxy |
| 外資夜盤空單交易量 | 31,852 | TAIFEX Proxy |
| 外資夜盤多空淨交易量 | -1,631 | TAIFEX Proxy |
| 外資日盤／夜盤交易量變化 | +334 | TAIFEX Proxy |
| 投信日盤多空淨交易量 | +1,022 | TAIFEX Proxy |
| 投信夜盤多空淨交易量 | +0 | TAIFEX Proxy |
| 投信日盤／夜盤交易量變化 | +1,022 | TAIFEX Proxy |
| 自營商日盤多空淨交易量 | -2,523 | TAIFEX Proxy |
| 自營商夜盤多空淨交易量 | +741 | TAIFEX Proxy |
| 自營商日盤／夜盤交易量變化 | -3,264 | TAIFEX Proxy |
| 三大法人日盤多空淨交易量 | -2,798 | TAIFEX Proxy |
| 三大法人夜盤多空淨交易量 | -890 | TAIFEX Proxy |
| 法人日盤交易金額淨額 (億元) | -248.6 | TAIFEX Proxy |
| 法人夜盤交易金額淨額 (億元) | -79.5 | TAIFEX Proxy |

### 6．期貨與現貨關係

| 項目 | 數值 | 資料來源 |
|---|---|---|
| 台指期近月價格 | 43,834 | TAIFEX Proxy |
| 加權指數價格 | 43,675.12 | twse-proxy |
| 台指期與加權指數價差 | +158.88 | TAIFEX Proxy+twse-proxy |
| 價差百分比 | +0.36 | TAIFEX Proxy+twse-proxy |
| 日盤基差 | +158.88 | TAIFEX Proxy+twse-proxy |
| 夜盤價格相對日盤收盤的變化 | -128 | TAIFEX Proxy |

### 7．日盤、夜盤與籌碼變化對照

#### 7.1 日夜盤價格與成交量對照 (變化 = 日盤 - 夜盤)

| 項目 | 日盤 | 夜盤 | 變化 (日-夜) | 資料來源 |
|---|---|---|---|---|
| 收盤價 | 43,834 | 43,706 | +128 | TAIFEX Proxy |
| 成交量 | 94,919 | 56,132 | +38,787 | TAIFEX Proxy |
- 台指期總 OI 前日變化：-2,859（來源：TAIFEX Proxy）


#### 7.2 法人籌碼日夜盤對照 (淨變化 = 日盤淨 - 夜盤淨；OI 為日盤收盤後總量，前日變化另列)

| 法人 | 交易量 |  |  |  |  |  |  | 未平倉量 |  |  |  | 資料來源 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|  | **日盤多單** | **日盤空單** | **日盤淨** | **夜盤多單** | **夜盤空單** | **夜盤淨** | **淨變化 (日-夜)** | **OI多方** | **OI空方** | **OI淨** | **OI前日變化** |  |
| 外資 | 104,183 | 105,480 | -1,297 | 30,221 | 31,852 | -1,631 | +334 | 6,186 | 107,056 | -100,870 | -1,297 | TAIFEX Proxy |
| 投信 | 9,181 | 8,159 | +1,022 | 0 | 0 | +0 | +1,022 | 103,019 | 3,096 | +99,923 | +1,022 | TAIFEX Proxy |
| 自營商 | 8,904 | 11,427 | -2,523 | 1,679 | 938 | +741 | -3,264 | 3,733 | 6,504 | -2,771 | -2,584 | TAIFEX Proxy |
| 三大法人合計 | 122,268 | 125,066 | -2,798 | 31,900 | 32,790 | -890 | -1,908 | 112,938 | 116,656 | -3,718 | -2,859 | TAIFEX Proxy |

#### 7.3 前十大交易人日夜盤對照 (OI 無日夜拆分，列收盤後總量)

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 前十大交易人多方 OI | 91,547 | TAIFEX Proxy |
| 前十大交易人空方 OI | 71,991 | TAIFEX Proxy |
| 前十大交易人多空淨 OI | +19,556 | TAIFEX Proxy |
| 前十大交易人多空淨 OI 變化 (2026-11-11→2026-11-13) | -192 | TAIFEX Proxy snapshots (2026-11-12) |

#### 7.4 夜盤劇本分類 (規則對應：夜盤漲跌 × 外資夜盤偏多空)

| 項目 | 數值 | 資料來源 |
|---|---|---|
| 夜盤成交量占比 (夜盤量／(夜盤量＋日盤量)) | 37.16% | TAIFEX Proxy |
| 夜盤漲跌點數 | -133 | TAIFEX Proxy |
| 外資夜盤多空淨交易量 | -1,631 | TAIFEX Proxy |
| 劇本分類 | 劇本三 | 規則對應 |
| 劇本條件 | 夜盤下跌＋外資偏空 | 規則對應 |
| 劇本特徵 | 開低、續跌機率高 | 規則對應 |

## 四、選擇權

**資料來源：** 主要 TAIFEX 經 Cloudflare Worker Proxy；時區 `Asia/Taipei`

### 1．選擇權交易日期、到期日與資料時間

| 項目 | 數值 | 資料來源 |
|---|---|---|
| 交易日期 | 2026-11-13 | TAIFEX Proxy |
| 到期月份／到期日 | 202611F2 | TAIFEX Proxy |
| 資料更新時間 | 2026-11-14 13:01:49 | 本機 |
| 日盤／夜盤標記 | 日盤收盤後資料 | TAIFEX Proxy |

### 2．Call 總成交量、OI、OI 增減

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Call 總成交量 | 419,770 | TAIFEX Proxy |
| Call 總未平倉量 OI | 83,365 | TAIFEX Proxy |
| Call OI 增減 (2026-11-12→2026-11-13) | +29,709 | TAIFEX Proxy snapshots (2026-11-12) |

### 3．Put 總成交量、OI、OI 增減

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Put 總成交量 | 430,162 | TAIFEX Proxy |
| Put 總未平倉量 OI | 74,992 | TAIFEX Proxy |
| Put OI 增減 (2026-11-12→2026-11-13) | +38,519 | TAIFEX Proxy snapshots (2026-11-12) |

### 4．Call／Put 比例與變化

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Call／Put 成交量比例 | 0.98 | TAIFEX Proxy |
| Call／Put 未平倉量比例 | 1.11 | TAIFEX Proxy |
| Put／Call Ratio | 0.90 | TAIFEX Proxy |
| Call／Put 比例變化 (量比 2026-11-12→2026-11-13) | 0.49 | TAIFEX Proxy |
| 與前一交易日比較 (OI 比 2026-11-12→2026-11-13) | -8.94 | TAIFEX Proxy |
**資料來源：** 比例 `TAIFEX Proxy chain`；變化 `TAIFEX Proxy PutCallRatio`

### 5．外資 Call／Put 部位

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 外資 Call日買 | 140,200 | TAIFEX Proxy |
| 外資 Call日賣 | 140,699 | TAIFEX Proxy |
| 外資 Call日淨 | -499 | TAIFEX Proxy |
| 外資 Put日買 | 151,226 | TAIFEX Proxy |
| 外資 Put日賣 | 150,457 | TAIFEX Proxy |
| 外資 Put日淨 | +769 | TAIFEX Proxy |
| 外資 Call夜買 | 21,531 | TAIFEX Proxy |
| 外資 Call夜賣 | 21,045 | TAIFEX Proxy |
| 外資 Call夜淨 | +486 | TAIFEX Proxy |
| 外資 Put夜買 | 18,972 | TAIFEX Proxy |
| 外資 Put夜賣 | 19,140 | TAIFEX Proxy |
| 外資 Put夜淨 | -168 | TAIFEX Proxy |
| 外資 日盤淨總量 | -1,268 | TAIFEX Proxy |
| 外資 Call日夜淨增減 (日－夜) | -985 | TAIFEX Proxy |
| 外資 Put日夜淨增減 (日－夜) | +937 | TAIFEX Proxy |

### 6．自營商 Call／Put 部位

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 自營商 Call日買 | 122,287 | TAIFEX Proxy |
| 自營商 Call日賣 | 118,011 | TAIFEX Proxy |
| 自營商 Call日淨 | +4,276 | TAIFEX Proxy |
| 自營商 Put日買 | 103,902 | TAIFEX Proxy |
| 自營商 Put日賣 | 120,492 | TAIFEX Proxy |
| 自營商 Put日淨 | -16,590 | TAIFEX Proxy |
| 自營商 Call夜買 | 11,595 | TAIFEX Proxy |
| 自營商 Call夜賣 | 14,562 | TAIFEX Proxy |
| 自營商 Call夜淨 | -2,967 | TAIFEX Proxy |
| 自營商 Put夜買 | 14,823 | TAIFEX Proxy |
| 自營商 Put夜賣 | 13,424 | TAIFEX Proxy |
| 自營商 Put夜淨 | +1,399 | TAIFEX Proxy |
| 自營商 日盤淨總量 | +20,866 | TAIFEX Proxy |
| 自營商 Call日夜淨增減 (日－夜) | +7,243 | TAIFEX Proxy |
| 自營商 Put日夜淨增減 (日－夜) | -17,989 | TAIFEX Proxy |

### 7．主要 Call OI 集中區

| 項目 | 履約價 | OI | 資料來源 |
|---|---|---|---|
| Call OI 第1大履約價 | 44,000 | 4,861 | TAIFEX Proxy |
| Call OI 第2大履約價 | 46,000 | 4,603 | TAIFEX Proxy |
| Call OI 第3大履約價 | 45,000 | 4,321 | TAIFEX Proxy |
| Call OI 最大履約價 | 44,000 | 4,861 | TAIFEX Proxy |

#### Call OI 分布明細 Top10 (機器可讀，到期月份 202611F2)

| # | 履約價 | OI | 佔比 | 資料來源 |
|---|---|---|---|---|
| C1 | 44,000 | 4,861 | 5.83% | TAIFEX Proxy |
| C2 | 46,000 | 4,603 | 5.52% | TAIFEX Proxy |
| C3 | 45,000 | 4,321 | 5.18% | TAIFEX Proxy |
| C4 | 43,800 | 3,483 | 4.18% | TAIFEX Proxy |
| C5 | 47,000 | 3,084 | 3.7% | TAIFEX Proxy |
| C6 | 44,500 | 2,626 | 3.15% | TAIFEX Proxy |
| C7 | 44,600 | 2,551 | 3.06% | TAIFEX Proxy |
| C8 | 43,850 | 2,455 | 2.94% | TAIFEX Proxy |
| C9 | 43,900 | 2,434 | 2.92% | TAIFEX Proxy |
| C10 | 44,200 | 2,025 | 2.43% | TAIFEX Proxy |


### 8．主要 Put OI 集中區

| 項目 | 履約價 | OI | 資料來源 |
|---|---|---|---|
| Put OI 第1大履約價 | 43,000 | 3,916 | TAIFEX Proxy |
| Put OI 第2大履約價 | 39,000 | 3,474 | TAIFEX Proxy |
| Put OI 第3大履約價 | 43,500 | 3,020 | TAIFEX Proxy |
| Put OI 最大履約價 | 43,000 | 3,916 | TAIFEX Proxy |

#### Put OI 分布明細 Top10 (機器可讀，到期月份 202611F2)

| # | 履約價 | OI | 佔比 | 資料來源 |
|---|---|---|---|---|
| P1 | 43,000 | 3,916 | 5.22% | TAIFEX Proxy |
| P2 | 39,000 | 3,474 | 4.63% | TAIFEX Proxy |
| P3 | 43,500 | 3,020 | 4.03% | TAIFEX Proxy |
| P4 | 42,000 | 2,975 | 3.97% | TAIFEX Proxy |
| P5 | 43,700 | 2,709 | 3.61% | TAIFEX Proxy |
| P6 | 43,750 | 2,690 | 3.59% | TAIFEX Proxy |
| P7 | 43,600 | 2,500 | 3.33% | TAIFEX Proxy |
| P8 | 43,800 | 2,395 | 3.19% | TAIFEX Proxy |
| P9 | 40,000 | 2,303 | 3.07% | TAIFEX Proxy |
| P10 | 41,000 | 1,795 | 2.39% | TAIFEX Proxy |


### 9．Call OI 增減集中區

| 項目 | 履約價 (增減口數) | 資料來源 |
|---|---|---|
| Call OI 增加最多的履約價 | 43,800 (+3,043) | TAIFEX Proxy snapshots (2026-11-12) |
| Call OI 減少最多的履約價 | 49,500 (-400) | TAIFEX Proxy snapshots (2026-11-12) |

### 10．Put OI 增減集中區

| 項目 | 履約價 (增減口數) | 資料來源 |
|---|---|---|
| Put OI 增加最多的履約價 | 43,750 (+2,607) | TAIFEX Proxy snapshots (2026-11-12) |
| Put OI 減少最多的履約價 | 42,800 (-89) | TAIFEX Proxy snapshots (2026-11-12) |

### 11．Call Wall

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Call Wall 價位 | 44,000 | TAIFEX Proxy |
| 對應到期月份 | 202611F2 | TAIFEX Proxy |
| 與前一交易日的變化 (2026-11-12→2026-11-13) | -2,000 | TAIFEX Proxy snapshots (2026-11-12) |

### 12．Put Wall

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Put Wall 價位 | 43,000 | TAIFEX Proxy |
| 對應到期月份 | 202611F2 | TAIFEX Proxy |
| 與前一交易日的變化 (2026-11-12→2026-11-13) | +0 | TAIFEX Proxy snapshots (2026-11-12) |

### 13．Gamma Wall

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Gamma Wall 價位 | 43,600.00 | TAIFEX Proxy (options-market-structure-compact (proxy)) |
| 對應到期月份 | 202611F2 | TAIFEX Proxy |
| 資料日期 | 2026-11-13 | TAIFEX Proxy (options-market-structure-compact (proxy)) |

### 14．Gamma Flip

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Gamma Flip 價位 | 42,826.92 | TAIFEX Proxy (options-market-structure-compact (proxy)) |
| 對應到期月份 | 202611F2 | TAIFEX Proxy |
| 資料日期 | 2026-11-13 | TAIFEX Proxy (options-market-structure-compact (proxy)) |

### 15．Max Pain

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Max Pain 價位 | 43,700 | TAIFEX Proxy |
| 對應到期月份 | 202611F2 | TAIFEX Proxy |
| 與前一交易日的變化 (2026-11-12→2026-11-13) | +750 | TAIFEX Proxy snapshots (2026-11-12) |

### 17．選擇權法人日盤、夜盤交易

| 法人 | 日盤多單 | 日盤空單 | 日盤淨 | 夜盤多單 | 夜盤空單 | 夜盤淨 | 淨變化 (日-夜) | 資料來源 |
|---|---|---|---|---|---|---|---|---|
| 外資 | 290,657 | 291,925 | -1,268 | 40,671 | 40,017 | +654 | -1,922 | TAIFEX Proxy |
| 投信 | 165 | 18,964 | -18,799 | 0 | 0 | +0 | -18,799 | TAIFEX Proxy |
| 自營商 | 242,779 | 221,913 | +20,866 | 25,019 | 29,385 | -4,366 | +25,232 | TAIFEX Proxy |
| 三大法人合計 | 533,601 | 532,802 | +799 | 65,690 | 69,402 | -3,712 | +4,511 | TAIFEX Proxy |
- 方法論：多方＝買Call＋賣Put（看多），空方＝賣Call＋買Put（看空），淨額＝看多－看空（已用 Call／Put 拆分頁交叉驗算一致）
- 公式：多方(買)－空方(賣)＝（買call＋賣put）－（賣call＋買put）＝看多－看空
- 速記：多＝BC＋SP、空＝SC＋BP

#### 法人多空力道表（金額・億元；上游千元／1e5）

| 法人 | 日多方力道 | 日空方力道 | 日淨多空力道 | 夜多方力道 | 夜空方力道 | 夜淨多空力道 | 日淨－夜淨 | 資料來源 |
|---|---|---|---|---|---|---|---|---|
| 外資 | 22.02 | 21.22 | +0.80 | 6.23 | 5.88 | +0.35 | +0.45 | TAIFEX Proxy |
| 投信 | 0.01 | 10.28 | -10.27 | 0.00 | 0.00 | +0 | -10.27 | TAIFEX Proxy |
| 自營商 | 29.85 | 19.66 | +10.20 | 4.17 | 5.38 | -1.21 | +11.41 | TAIFEX Proxy |
| 三大法人合計 | 51.88 | 51.15 | +0.73 | 10.40 | 11.26 | -0.86 | +1.59 | TAIFEX Proxy |

### 18．選擇權前十大

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 買權多方 OI | 42,709 | TAIFEX Proxy |
| 買權空方 OI | 49,621 | TAIFEX Proxy |
| 買權多空淨 OI | -6,912 | TAIFEX Proxy |
| 買權多空淨 OI 變化 (2026-11-11→2026-11-13) | -1,935 | TAIFEX Proxy snapshots (2026-11-12) |

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 賣權多方 OI | 21,882 | TAIFEX Proxy |
| 賣權空方 OI | 19,471 | TAIFEX Proxy |
| 賣權多空淨 OI | +2,411 | TAIFEX Proxy |
| 賣權多空淨 OI 變化 (2026-11-11→2026-11-13) | +4,918 | TAIFEX Proxy snapshots (2026-11-12) |
- 資料日期：買權 2026-11-13／賣權 2026-11-13 (TypeOfTraders=0 全部交易人；契約月份 202611)

#### 大戶流向（全日；前十大無日夜拆分）

| 項目 | 淨變化 | 區間 | 資料來源 |
|---|---|---|---|
| 期貨前十大 | -192 | 2026-11-11→2026-11-13 | TAIFEX Proxy snapshots (2026-11-12) |
| 買權前十大 | -1,935 | 2026-11-11→2026-11-13 | TAIFEX Proxy snapshots (2026-11-12) |
| 賣權前十大 | +4,918 | 2026-11-11→2026-11-13 | TAIFEX Proxy snapshots (2026-11-12) |

### 16．資料來源、時間、時區與狀態

- 資料來源：TAIFEX 經 Cloudflare Worker Proxy
- 資料日期：2026-11-13；資料時間：2026-11-14 13:01:49；時區：`Asia/Taipei`
- 日盤／夜盤標記：日盤收盤後 + 夜盤盤後
- 註記：同 T0 覆蓋：150 格以本次新抓取覆蓋（該 T0 尚無報告，無凍結對象）
- 未取得欄位 (2)：futures.gamma_wall, futures.gamma_flip
- 註記：futures-price-after-hours 日期 2026-11-13 非今日 2026-11-16，視為無新節次，不採用
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
| 外資 | +288.4 | -100,870 | -1,297 | -1,631 | -1,268 | +654 | 避險／對沖 | 強避險 | twse-proxy／TAIFEX Proxy |
| 投信 | +95.4 | +99,923 | +1,022 | +0 | -18,799 | +0 | 避險／對沖 | 分歧 | twse-proxy／TAIFEX Proxy |
| 自營商 | +68.9 | -2,771 | -2,523 | +741 | +20,866 | -4,366 | 避險／對沖 | 強避險 | twse-proxy／TAIFEX Proxy |
