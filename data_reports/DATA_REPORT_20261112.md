# DATA_REPORT_20261112

- 報告日期：`2026-11-12`
- T0 交易日期：`2026-11-12`
- 資料產出時間：`2026-11-12 02:18:58`
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
| 加權指數 | 42,711.92 | 點 | TWSE OpenAPI MI_INDEX (備援) |
| 開盤 | unavailable | 點 | FinMind |
| 最高 | unavailable | 點 | FinMind |
| 最低 | unavailable | 點 | FinMind |
| 收盤 | 42,711.92 | 點 | TWSE OpenAPI MI_INDEX (備援) |
| 漲跌點數 | 1,050.22 | 點 | TWSE OpenAPI MI_INDEX (備援) |
| 漲跌幅 | +2.52 | % | TWSE OpenAPI MI_INDEX (備援) |
| 成交金額 | unavailable | 億元 | twse-proxy |

### 2. 市場漲跌家數

#### 2.1 上市公司

**資料來源：** `Cloudflare Worker：twse-proxy` (備援 `TWSE OpenAPI twtazu_od`)

| 項目 | 家數 | 資料來源 |
|---|---|---|
| 上漲家數 | unavailable | twse-proxy |
| 下跌家數 | unavailable | twse-proxy |
| 平盤家數 | unavailable | twse-proxy |
| 漲停家數 | unavailable | twse-proxy |
| 跌停家數 | unavailable | twse-proxy |

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
| 外資 | -7.7 | 億元 | twse-proxy /institutional |
| 投信 | +185.9 | 億元 | twse-proxy /institutional |
| 自營商 | +62.6 | 億元 | twse-proxy /institutional |
| 三大法人合計 | +240.8 | 億元 | twse-proxy /institutional |

### 4. 融資融券

**資料來源：** 上市+上櫃 `HiStock` (金額口徑)；維持率 `istock.tw`；備援官方逐股加總

| 項目 | 數值 | 單位 | 資料來源 |
|---|---|---|---|
| 融資餘額 | unavailable | 億元 | HiStock |
| 融資增減 | unavailable | 億元 | HiStock |
| 融券餘額 | 211,131 | 張 | HiStock |
| 融券增減 | 9,835 | 張 | HiStock |
| 融資維持率 | 151.90 | % | 前值遞補 (DATA 2026-11-11；當日三源皆失敗；民間估算；官方無每日序列) |

### 5. 借券資料

**資料來源：** 上市 `TWSE OpenAPI TWT96U` (可借餘額)、上櫃 `TPEX OpenAPI tpex_margin_sbl`

| 項目 | 數值 | 單位 | 資料來源 |
|---|---|---|---|
| 借券餘額 | 287,507 | 張 | TWSE TWT93U + TPEX margin_sbl |
| 借券賣出餘額 | unavailable | 張 | TWSE TWT93U + TPEX margin_sbl |
| 借券賣出增減 | unavailable | 張 | TWSE TWT93U + TPEX margin_sbl |

### 6. 市場成交結構

**資料來源：** 上市 `twse-proxy market_statistics`、上櫃 `TPEX OpenAPI tpex_mainborad_highlight`

| 項目 | 成交金額 | 單位 | 資料來源 |
|---|---|---|---|
| 上市成交金額 | unavailable | 億元 | twse-proxy |
| 上櫃成交金額 | unavailable | 億元 | TPEX |
| 上市櫃成交金額合計 | unavailable | 億元 | twse-proxy+TPEX |

## 二、重要市場

### 1. 美股指數

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 收盤／最新值 | 漲跌點 | 漲跌幅 | 資料來源 |
|---|---|---|---|---|---|
| S&P 500 | ^GSPC | 7,637.95 | 117.02 | +1.56 | Yahoo Finance Chart API |
| Nasdaq Composite | ^IXIC | 25,612.09 | 546.22 | +2.18 | Yahoo Finance Chart API |
| Nasdaq 100 | ^NDX | 28,545.75 | 804.96 | +2.90 | Yahoo Finance Chart API |
| Dow Jones | ^DJI | 52,438.78 | 206.89 | +0.40 | Yahoo Finance Chart API |
| 費城半導體 SOX | ^SOX | 10,737.37 | 739.04 | +7.39 | Yahoo Finance Chart API |
| VIX | ^VIX | 17.56 | -1.90 | -9.76 | Yahoo Finance Chart API |

### 2. 亞洲主要指數

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 收盤／最新值 | 漲跌點 | 漲跌幅 | 資料來源 |
|---|---|---|---|---|---|
| 日經225 | ^N225 | 60,459.58 | 1,684.08 | +2.87 | Yahoo Finance Chart API |
| 韓國KOSPI | ^KS11 | 5,239.13 | 220.28 | +4.39 | Yahoo Finance Chart API |
| 香港恆生 | ^HSI | 24,557.04 | 108.09 | +0.44 | Yahoo Finance Chart API |
| 上海綜合 | 000001.SS | 3,663.72 | 2.93 | +0.08 | Yahoo Finance Chart API |
| 深圳成分 | 399001.SZ | 11,241.54 | 96.05 | +0.86 | Yahoo Finance Chart API |

### 3. 美股指數期貨

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 最新值 | 漲跌點 | 漲跌幅 | 資料來源 |
|---|---|---|---|---|---|
| S&P500期貨 | ES=F | 7,656.00 | 111.75 | +1.48 | Yahoo Finance Chart API |
| Nasdaq100期貨 | NQ=F | 28,618.75 | 783.50 | +2.81 | Yahoo Finance Chart API |
| 道瓊期貨 | YM=F | 52,501.00 | 186.00 | +0.36 | Yahoo Finance Chart API |
| Russell2000期貨 | RTY=F | 2,856.40 | 27.50 | +0.97 | Yahoo Finance Chart API |

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
| USD/TWD | TWD=X | 32.87 | 0.08 | +0.25 | Yahoo Finance Chart API |
| DXY美元指數 | DX-Y.NYB | 102.90 | 0.67 | +0.66 | Yahoo Finance Chart API |
| USD/JPY | JPY=X | 159.81 | 1.83 | +1.16 | Yahoo Finance Chart API |
| USD/KRW | KRW=X | 1,336.26 | -7.58 | -0.56 | Yahoo Finance Chart API |

### 6. 台灣相關ADR

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 收盤／最新值 | 漲跌點 | 漲跌幅 | 資料來源 |
|---|---|---|---|---|---|
| 台積電ADR | TSM | 415.99 | 19.51 | +4.92 | Yahoo Finance Chart API |
| 聯電ADR | UMC | 16.10 | 1.06 | +7.08 | Yahoo Finance Chart API |
| 日月光ADR | ASX | 38.06 | 2.58 | +7.27 | Yahoo Finance Chart API |

### 7. 原油黃金Bitcoin

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 收盤／最新值 | 漲跌點 | 漲跌幅 | 資料來源 |
|---|---|---|---|---|---|
| WTI原油期貨 | CL=F | 87.30 | 1.26 | +1.46 | Yahoo Finance Chart API |
| 黃金期貨 | GC=F | 3,999.10 | -31.10 | -0.77 | Yahoo Finance Chart API |
| Bitcoin | BTC-USD | 74,445.14 | 725.02 | +0.98 | Yahoo Finance Chart API |

### 8. 重大經濟數據、央行事件與重大市場新聞

**資料來源：** 台股 `tw.stock.yahoo.com` (含內文摘要)；國際 `Fed 公告 RSS`＋`CNBC`＋`MarketWatch` (標題、來源、時間與連結)

- 事件1：台股重返4萬4誰最吸睛？神山拉尾盤台玻連三燈
  - 來源：Yahoo 台股；發布時間：2026-11-11T08:51:47Z；台北時間：2026-11-11 16:51
  - 摘要：台股連三天強彈，飆漲1545點收最高重回4萬4！今(11)日加權指數早盤震盪後再度走高，終場上漲1545.23點、漲幅3.62%，收在全日最高44257.15點，創史上第六大收盤漲點，上市成交金額8505.72億元。電子類股上漲3.96%，
  - 原文連結：https://tw.stock.yahoo.com/news/%E5%8F%B0%E7%A9%8D%E9%9B%BB%E5%B0%BE%E7%9B%A4%E7%A5%9E%E5%8A%A9%E6%94%BB%EF%BC%81%E5%8F%B0%E8%82%A1%E7%8B%82%E9%A3%861545%E9%BB%9E%E9%87%8D%E8%BF%944%E8%90%AC4-%E5%8F%B0%E7%8E%BB%E6%BC%B2%E5%81%9C%E4%B8%89%E9%80%A3%E7%99%BC%E6%8F%AA%E7%8E%BB%E7%BA%96%E5%B8%83%E9%96%8B%E4%BA%AE%E7%87%88%E5%90%8C%E6%A8%82%E6%9C%83%EF%BD%9Cyahoo%E8%B2%A1%E7%B6%93%E6%8E%83%E6%8F%8F-085147527.html
- 事件2：台股狂飆新台幣卻沒跟上 小升半分收32.86元
  - 來源：Yahoo 台股；發布時間：2026-11-11T10:11:42Z；台北時間：2026-11-11 18:11
  - 摘要：（中央社記者潘姿羽台北11日電）台股展開強勢反彈，連續3個交易日上漲，指數重返4萬4000點大關，不過新台幣匯率持續偏弱震盪，央行尾盤進場調節之下，終場收在32.86元，微升0.5分。由於市場氛圍轉趨觀望，台北及元太外匯市場總成交金額收斂至
  - 原文連結：https://tw.stock.yahoo.com/news/%E5%8F%B0%E8%82%A1%E9%80%A33%E6%BC%B2%E6%94%B6%E5%BE%A944000%E9%BB%9E-%E6%96%B0%E5%8F%B0%E5%B9%A3%E5%8D%87%E5%8B%A2%E4%B9%8F%E5%8A%9B%E6%94%B632-86%E5%85%83-101142283.html
- 事件3：近7成國人薪水輸給平均 主計總處揭背後三大因素
  - 來源：Yahoo 台股；發布時間：2026-11-11T09:06:15Z；台北時間：2026-11-11 17:06
  - 摘要：主計總處今（11）日公布9月工業及服務業薪資統計，今年前9月全體受僱員工每人每月經常性薪資平均為4萬9,152元，年增2.93%，創近26年來同期次高，但多數國人實際領到的薪水仍低於平均水準。根據統計，前9月約69.97%的受僱員工經常性薪
  - 原文連結：https://tw.stock.yahoo.com/news/%E4%BD%A0%E6%9C%89%E5%97%8E%EF%BC%9F%E5%89%8D9%E6%9C%88%E7%B6%93%E5%B8%B8%E6%80%A7%E8%96%AA%E8%B3%87%E5%B9%B3%E5%9D%874%E8%90%AC9152%E5%85%83-%E8%BF%917%E6%88%90%E5%9C%8B%E4%BA%BA%E9%A0%98%E4%B8%8D%E5%88%B0-090829767.html
- 事件4：前3季每股大賺10元 八方雲集端冬季新品搶市
  - 來源：Yahoo 台股；發布時間：2026-11-11T10:34:51Z；台北時間：2026-11-11 18:34
  - 摘要：連鎖餐飲集團八方雲集（2753）董事會今（11）日通過2026年第三季財報，受惠台灣雙品牌持續展店及規模經濟效益擴大，前三季合併營收達70.04億元，歸屬母公司淨利6.99億元，年增逾一成，每股稅後盈餘（EPS）10元，相當於賺了一個股本，
  - 原文連結：https://tw.stock.yahoo.com/news/%E7%85%8E%E9%A4%83%E8%AE%8A%E8%BA%AB%E9%87%91%E5%85%83%E5%AF%B6%EF%BC%81%E5%85%AB%E6%96%B9%E9%9B%B2%E9%9B%86%E5%89%8D%E4%B8%89%E5%AD%A3%E5%A4%A7%E8%B3%BA1%E5%80%8B%E8%82%A1%E6%9C%AC-%E5%89%B5%E5%90%8C%E6%9C%9F%E6%96%B0%E9%AB%98-103438325.html
- 事件5：會員教練課雙引擎發威 世界健身前3季賺逾半個股本
  - 來源：Yahoo 台股；發布時間：2026-11-11T10:01:25Z；台北時間：2026-11-11 18:01
  - 摘要：國人多愛上健身房？台灣第一大健身連鎖品牌世界健身-KY（2762）今（11）日公布2026年第三季財報，受惠會員及教練課程收入雙雙成長，累計前三季大賺6.15億元，年增1.54倍，每股盈餘（EPS）為5.63元，相當於賺破半個股本。
  - 原文連結：https://tw.stock.yahoo.com/news/%E5%9C%8B%E4%BA%BA%E5%A4%9A%E6%84%9B%E4%B8%8A%E5%81%A5%E8%BA%AB%E6%88%BF%EF%BC%9F-%E4%B8%96%E7%95%8C%E5%81%A5%E8%BA%AB-ky%E5%89%8D%E4%B8%89%E5%AD%A3%E7%8D%B2%E5%88%A9%E7%BF%BB%E5%80%8D-%E5%A4%A7%E8%B3%BA%E5%8D%8A%E5%80%8B%E8%82%A1%E6%9C%AC-095953579.html
- 事件6：PCB繼續漲！三大法人進貨「這2檔」3.1萬張　連4天進場台玻挹注88.02億元
  - 來源：Yahoo 台股；發布時間：2026-11-11T13:00:00Z；台北時間：2026-11-11 21:00
  - 摘要：[FTNN新聞網]記者陳献朋／綜合報導台股加權指數今（11）日收在44257.15點，上漲1545.23點，漲幅3.62%，成交量達8505億元。根據證交所資料，三大法人買超202.5...
  - 原文連結：https://tw.stock.yahoo.com/news/pcb%E7%B9%BC%E7%BA%8C%E6%BC%B2-%E4%B8%89%E5%A4%A7%E6%B3%95%E4%BA%BA%E9%80%B2%E8%B2%A8-%E9%80%992%E6%AA%94-3-1%E8%90%AC%E5%BC%B5-130000093.html
- 事件7：Federal Reserve Board announces approval of two applications by Mutual Federal Bancorp, MHC, and MFB Bancorp, Inc.
  - 來源：Federal Reserve；發布時間：Mon, 9 Nov 2026 21:00:00 GMT；台北時間：2026-11-10 05:00
  - 摘要：Federal Reserve Board announces approval of two applications by Mutual Federal Bancorp, MHC, and MFB Bancorp, Inc.
  - 原文連結：https://www.federalreserve.gov/newsevents/pressreleases/orders20261109a.htm
- 事件8：Federal Reserve Board announces termination of enforcement action with Allegiant United Holdings, LLC, Nano Financial Holdings, Inc., and Nano Banc
  - 來源：Federal Reserve；發布時間：Thu, 5 Nov 2026 16:00:00 GMT；台北時間：2026-11-06 00:00
  - 摘要：Federal Reserve Board announces termination of enforcement action with Allegiant United Holdings, LLC, Nano Financial Holdings, Inc., and Nano Banc
  - 原文連結：https://www.federalreserve.gov/newsevents/pressreleases/enforcement20261105a.htm
- 事件9：Fed's Goolsbee calls inflation report 'borderline disturbing' as central bank weighs more hikes
  - 來源：CNBC；發布時間：Wed, 11 Nov 2026 16:49:02 GMT；台北時間：2026-11-12 00:49
  - 摘要：The consumer price index rose more than expected in October, raising alarm among Federal Reserve officials.
  - 原文連結：https://www.cnbc.com/2026/11/11/goolsbee-october-inflation-fed-rates-disturbing-distressing.html
- 事件10：White House vows to press ahead with tariffs despite midterm backlash over rising prices
  - 來源：CNBC；發布時間：Tue, 10 Nov 2026 21:45:46 GMT；台北時間：2026-11-11 05:45
  - 摘要：Business executives warned at a Washington summit of rising costs and shifting supply chains as polls showed growing opposition to Trump's tariffs.
  - 原文連結：https://www.cnbc.com/2026/11/10/trump-tariffs-midterms-gary-cohn-inflation.html
- 事件11：Credit card debt climbs to a record $1.29 trillion, New York Fed research finds
  - 來源：CNBC；發布時間：Tue, 10 Nov 2026 18:08:40 GMT；台北時間：2026-11-11 02:08
  - 摘要：As high prices continue to strain household budgets, many consumers have turned to credit cards to help make ends meet.
  - 原文連結：https://www.cnbc.com/2026/11/10/credit-card-debt-record.html
- 事件12：Homeowners tap equity as HELOC balances post biggest jump since 2005: New York Fed report
  - 來源：CNBC；發布時間：Tue, 10 Nov 2026 21:37:43 GMT；台北時間：2026-11-11 05:37
  - 摘要：The rise in balances on HELOCs marks the 18th consecutive quarterly increase, according to a new report from the Federal Reserve Bank of New York.
  - 原文連結：https://www.cnbc.com/2026/11/10/heloc-balances-new-york-fed.html


## 三、期貨

**資料來源：**
1. Cloudflare Workers：TAIFEX Proxy — https://taifex.grichtoyang.workers.dev/
2. TAIFEX Open API — https://openapi.taifex.com.tw/

近月契約月份：202611 (日盤成交量最大者)；交易日期：2026-11-12

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
| 開盤價 | unavailable | 端點未提供 |
| 最高價 | unavailable | 端點未提供 |
| 最低價 | unavailable | 端點未提供 |
| 收盤價 | unavailable | 端點未提供 |
| 漲跌點數 | unavailable | 端點未提供 |
| 漲跌幅 | unavailable | 端點未提供 |
| 成交量 | unavailable | TAIFEX Proxy |
| 夜盤高點及低點 | unavailable / unavailable | 端點未提供 |
| 結算價 | unavailable | TAIFEX Proxy |
| 未平倉量 | unavailable | TAIFEX Proxy |

### 3．法人台指期多空未平倉部位

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 外資多方 OI | unavailable | TAIFEX Proxy |
| 外資空方 OI | unavailable | TAIFEX Proxy |
| 外資多空淨 OI | unavailable | TAIFEX Proxy |
| 投信多方 OI | unavailable | TAIFEX Proxy |
| 投信空方 OI | unavailable | TAIFEX Proxy |
| 投信多空淨 OI | unavailable | TAIFEX Proxy |
| 自營商多方 OI | unavailable | TAIFEX Proxy |
| 自營商空方 OI | unavailable | TAIFEX Proxy |
| 自營商多空淨 OI | unavailable | TAIFEX Proxy |
| 三大法人合計多方 OI | 0 | TAIFEX Proxy |
| 三大法人合計空方 OI | 0 | TAIFEX Proxy |
| 三大法人合計多空淨 OI | +0 | TAIFEX Proxy |
| 外資多空淨 OI 變化 | unavailable | TAIFEX Proxy |
| 投信多空淨 OI 變化 | unavailable | TAIFEX Proxy |
| 自營商多空淨 OI 變化 | unavailable | TAIFEX Proxy |

### 4．前十大交易人多空未平倉部位

**資料來源：** `TAIFEX OpenAPI OpenInterestOfLargeTradersFutures` (官方資料落後約一日，標示實際日期)

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 前十大交易人多方 OI | 104,067 | TAIFEX Proxy |
| 前十大交易人空方 OI | 88,625 | TAIFEX Proxy |
| 前十大交易人多空淨 OI | +15,442 | TAIFEX Proxy |
| 多空淨 OI 變化 (2026-11-10→2026-11-10) | +0 | TAIFEX Proxy snapshots (2026-11-11) |
- 資料日期：2026-11-10 (TypeOfTraders=0 全部交易人；契約月份 202611)

### 5．日盤、夜盤法人交易資料

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 外資日盤多單交易量 | 80,899 | TAIFEX Proxy |
| 外資日盤空單交易量 | 81,678 | TAIFEX Proxy |
| 外資日盤多空淨交易量 | -779 | TAIFEX Proxy |
| 外資夜盤多單交易量 | unavailable | TAIFEX Proxy |
| 外資夜盤空單交易量 | unavailable | TAIFEX Proxy |
| 外資夜盤多空淨交易量 | unavailable | TAIFEX Proxy |
| 外資日盤／夜盤交易量變化 | unavailable | TAIFEX Proxy |
| 投信日盤多空淨交易量 | +3,351 | TAIFEX Proxy |
| 投信夜盤多空淨交易量 | unavailable | TAIFEX Proxy |
| 投信日盤／夜盤交易量變化 | unavailable | TAIFEX Proxy |
| 自營商日盤多空淨交易量 | -92 | TAIFEX Proxy |
| 自營商夜盤多空淨交易量 | unavailable | TAIFEX Proxy |
| 自營商日盤／夜盤交易量變化 | unavailable | TAIFEX Proxy |
| 三大法人日盤多空淨交易量 | +2,480 | TAIFEX Proxy |
| 三大法人夜盤多空淨交易量 | unavailable | TAIFEX Proxy |
| 法人日盤交易金額淨額 (億元) | +216.1 | TAIFEX Proxy |
| 法人夜盤交易金額淨額 (億元) | unavailable | TAIFEX Proxy |

### 6．期貨與現貨關係

| 項目 | 數值 | 資料來源 |
|---|---|---|
| 台指期近月價格 | 44,091 | TAIFEX Proxy |
| 加權指數價格 | 42,711.92 | TWSE OpenAPI MI_INDEX (備援) |
| 台指期與加權指數價差 | +1,379.08 | TAIFEX Proxy+TWSE OpenAPI MI_INDEX (備援) |
| 價差百分比 | +3.23 | TAIFEX Proxy+TWSE OpenAPI MI_INDEX (備援) |
| 日盤基差 | +1,379.08 | TAIFEX Proxy+TWSE OpenAPI MI_INDEX (備援) |
| 夜盤價格相對日盤收盤的變化 | unavailable | 端點未提供 |

### 7．日盤、夜盤與籌碼變化對照

#### 7.1 日夜盤價格與成交量對照 (變化 = 日盤 - 夜盤)

| 項目 | 日盤 | 夜盤 | 變化 (日-夜) | 資料來源 |
|---|---|---|---|---|
| 收盤價 | 44,091 | unavailable | unavailable | TAIFEX Proxy |
| 成交量 | 81,696 | unavailable | unavailable | TAIFEX Proxy |
- 台指期總 OI 前日變化：+0（來源：TAIFEX Proxy）


#### 7.2 法人籌碼日夜盤對照 (淨變化 = 日盤淨 - 夜盤淨；OI 為日盤收盤後總量，前日變化另列)

| 法人 | 交易量 |  |  |  |  |  |  | 未平倉量 |  |  |  | 資料來源 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|  | **日盤多單** | **日盤空單** | **日盤淨** | **夜盤多單** | **夜盤空單** | **夜盤淨** | **淨變化 (日-夜)** | **OI多方** | **OI空方** | **OI淨** | **OI前日變化** |  |
| 外資 | 80,899 | 81,678 | -779 | unavailable | unavailable | unavailable | unavailable | unavailable | unavailable | unavailable | unavailable | TAIFEX Proxy |
| 投信 | 4,978 | 1,627 | +3,351 | unavailable | unavailable | unavailable | unavailable | unavailable | unavailable | unavailable | unavailable | TAIFEX Proxy |
| 自營商 | 6,716 | 6,808 | -92 | unavailable | unavailable | unavailable | unavailable | unavailable | unavailable | unavailable | unavailable | TAIFEX Proxy |
| 三大法人合計 | 92,593 | 90,113 | +2,480 | unavailable | unavailable | unavailable | unavailable | 0 | 0 | +0 | +0 | TAIFEX Proxy |

#### 7.3 前十大交易人日夜盤對照 (OI 無日夜拆分，列收盤後總量)

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 前十大交易人多方 OI | 104,067 | TAIFEX Proxy |
| 前十大交易人空方 OI | 88,625 | TAIFEX Proxy |
| 前十大交易人多空淨 OI | +15,442 | TAIFEX Proxy |
| 前十大交易人多空淨 OI 變化 (2026-11-10→2026-11-10) | +0 | TAIFEX Proxy snapshots (2026-11-11) |

#### 7.4 夜盤劇本分類 (規則對應：夜盤漲跌 × 外資夜盤偏多空)

| 項目 | 數值 | 資料來源 |
|---|---|---|
| 夜盤成交量占比 (夜盤量／(夜盤量＋日盤量)) | unavailable | TAIFEX Proxy |
| 夜盤漲跌點數 | unavailable | TAIFEX Proxy+TWSE OpenAPI MI_INDEX (備援) |
| 外資夜盤多空淨交易量 | unavailable | TAIFEX Proxy |
| 劇本分類 | unavailable | 規則對應 |
| 劇本條件 | unavailable | 規則對應 |
| 劇本特徵 | unavailable | 規則對應 |

## 四、選擇權

**資料來源：** 主要 TAIFEX 經 Cloudflare Worker Proxy；時區 `Asia/Taipei`

### 1．選擇權交易日期、到期日與資料時間

| 項目 | 數值 | 資料來源 |
|---|---|---|
| 交易日期 | 2026-11-12 | TAIFEX Proxy |
| 到期月份／到期日 | 202611W2 | TAIFEX Proxy |
| 資料更新時間 | 2026-11-12 02:18:58 | 本機 |
| 日盤／夜盤標記 | 日盤收盤後資料 | TAIFEX Proxy |

### 2．Call 總成交量、OI、OI 增減

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Call 總成交量 | 366,892 | TAIFEX Proxy |
| Call 總未平倉量 OI | 85,471 | TAIFEX Proxy |
| Call OI 增減 (2026-11-11→2026-11-12) | +0 | TAIFEX Proxy snapshots (2026-11-11) |

### 3．Put 總成交量、OI、OI 增減

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Put 總成交量 | 394,841 | TAIFEX Proxy |
| Put 總未平倉量 OI | 109,230 | TAIFEX Proxy |
| Put OI 增減 (2026-11-11→2026-11-12) | +0 | TAIFEX Proxy snapshots (2026-11-11) |

### 4．Call／Put 比例與變化

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Call／Put 成交量比例 | 0.93 | TAIFEX Proxy |
| Call／Put 未平倉量比例 | 0.78 | TAIFEX Proxy |
| Put／Call Ratio | 1.28 | TAIFEX Proxy |
| Call／Put 比例變化 (量比 2026-11-09→2026-11-10) | 38.55 | TAIFEX Proxy |
| 與前一交易日比較 (OI 比 2026-11-09→2026-11-10) | 15.35 | TAIFEX Proxy |
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
| 外資 Call夜買 | 45,358 | TAIFEX Proxy |
| 外資 Call夜賣 | 46,232 | TAIFEX Proxy |
| 外資 Call夜淨 | -874 | TAIFEX Proxy |
| 外資 Put夜買 | 60,552 | TAIFEX Proxy |
| 外資 Put夜賣 | 59,808 | TAIFEX Proxy |
| 外資 Put夜淨 | +744 | TAIFEX Proxy |
| 外資 日盤淨總量 | +6,098 | TAIFEX Proxy |
| 外資 Call日夜淨增減 (日－夜) | +3,028 | TAIFEX Proxy |
| 外資 Put日夜淨增減 (日－夜) | -4,688 | TAIFEX Proxy |

### 6．自營商 Call／Put 部位

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 自營商 Call日買 | 85,562 | TAIFEX Proxy |
| 自營商 Call日賣 | 88,582 | TAIFEX Proxy |
| 自營商 Call日淨 | -3,020 | TAIFEX Proxy |
| 自營商 Put日買 | 94,874 | TAIFEX Proxy |
| 自營商 Put日賣 | 112,565 | TAIFEX Proxy |
| 自營商 Put日淨 | -17,691 | TAIFEX Proxy |
| 自營商 Call夜買 | 17,307 | TAIFEX Proxy |
| 自營商 Call夜賣 | 19,920 | TAIFEX Proxy |
| 自營商 Call夜淨 | -2,613 | TAIFEX Proxy |
| 自營商 Put夜買 | 23,322 | TAIFEX Proxy |
| 自營商 Put夜賣 | 28,361 | TAIFEX Proxy |
| 自營商 Put夜淨 | -5,039 | TAIFEX Proxy |
| 自營商 日盤淨總量 | +14,671 | TAIFEX Proxy |
| 自營商 Call日夜淨增減 (日－夜) | -407 | TAIFEX Proxy |
| 自營商 Put日夜淨增減 (日－夜) | -12,652 | TAIFEX Proxy |

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
| Call Wall 價位 | 46,000 | TAIFEX Proxy |
| 對應到期月份 | 202611W2 | TAIFEX Proxy |
| 與前一交易日的變化 (2026-11-11→2026-11-12) | +0 | TAIFEX Proxy snapshots (2026-11-11) |

### 12．Put Wall

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Put Wall 價位 | 35,700 | TAIFEX Proxy |
| 對應到期月份 | 202611W2 | TAIFEX Proxy |
| 與前一交易日的變化 (2026-11-11→2026-11-12) | +0 | TAIFEX Proxy snapshots (2026-11-11) |

### 13．Gamma Wall

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Gamma Wall 價位 | 45,000.00 | TAIFEX Proxy (options-gamma-levels) |
| 對應到期月份 | 202611W2 | TAIFEX Proxy |
| 資料日期 | 2026-11-12 | TAIFEX Proxy (options-gamma-levels) |

### 14．Gamma Flip

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Gamma Flip 價位 | 43,546.87 | TAIFEX Proxy (options-gamma-levels) |
| 對應到期月份 | 202611W2 | TAIFEX Proxy |
| 資料日期 | 2026-11-12 | TAIFEX Proxy (options-gamma-levels) |

### 15．Max Pain

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Max Pain 價位 | 42,950 | TAIFEX Proxy |
| 對應到期月份 | 202611W2 | TAIFEX Proxy |
| 與前一交易日的變化 (2026-11-11→2026-11-12) | +0 | TAIFEX Proxy snapshots (2026-11-11) |

### 17．選擇權法人日盤、夜盤交易

| 法人 | 日盤多單 | 日盤空單 | 日盤淨 | 夜盤多單 | 夜盤空單 | 夜盤淨 | 淨變化 (日-夜) | 資料來源 |
|---|---|---|---|---|---|---|---|---|
| 外資 | 267,484 | 261,386 | +6,098 | unavailable | unavailable | unavailable | unavailable | TAIFEX Proxy |
| 投信 | 240 | 3,147 | -2,907 | unavailable | unavailable | unavailable | unavailable | TAIFEX Proxy |
| 自營商 | 198,127 | 183,456 | +14,671 | unavailable | unavailable | unavailable | unavailable | TAIFEX Proxy |
| 三大法人合計 | 465,851 | 447,989 | +17,862 | unavailable | unavailable | unavailable | unavailable | TAIFEX Proxy |
- 方法論：多方＝買Call＋賣Put（看多），空方＝賣Call＋買Put（看空），淨額＝看多－看空（已用 Call／Put 拆分頁交叉驗算一致）
- 公式：多方(買)－空方(賣)＝（買call＋賣put）－（賣call＋買put）＝看多－看空
- 速記：多＝BC＋SP、空＝SC＋BP

#### 法人多空力道表（金額・億元；上游千元／1e5）

| 法人 | 日多方力道 | 日空方力道 | 日淨多空力道 | 夜多方力道 | 夜空方力道 | 夜淨多空力道 | 日淨－夜淨 | 資料來源 |
|---|---|---|---|---|---|---|---|---|
| 外資 | 19.77 | 19.07 | +0.70 | 9.26 | 9.42 | -0.16 | +0.86 | TAIFEX Proxy |
| 投信 | 0.00 | 2.06 | -2.05 | 0.00 | 0.00 | +0 | -2.05 | TAIFEX Proxy |
| 自營商 | 18.54 | 15.39 | +3.15 | 4.84 | 4.71 | +0.13 | +3.02 | TAIFEX Proxy |
| 三大法人合計 | 38.31 | 36.51 | +1.80 | 14.10 | 14.13 | -0.03 | +1.83 | TAIFEX Proxy |

### 18．選擇權前十大

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 買權多方 OI | 21,840 | TAIFEX Proxy |
| 買權空方 OI | 27,346 | TAIFEX Proxy |
| 買權多空淨 OI | -5,506 | TAIFEX Proxy |
| 買權多空淨 OI 變化 (2026-11-10→2026-11-10) | +0 | TAIFEX Proxy snapshots (2026-11-11) |

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 賣權多方 OI | 13,497 | TAIFEX Proxy |
| 賣權空方 OI | 16,623 | TAIFEX Proxy |
| 賣權多空淨 OI | -3,126 | TAIFEX Proxy |
| 賣權多空淨 OI 變化 (2026-11-10→2026-11-10) | +0 | TAIFEX Proxy snapshots (2026-11-11) |
- 資料日期：買權 2026-11-10／賣權 2026-11-10 (TypeOfTraders=0 全部交易人；契約月份 202611)

#### 大戶流向（全日；前十大無日夜拆分）

| 項目 | 淨變化 | 區間 | 資料來源 |
|---|---|---|---|
| 期貨前十大 | +0 | 2026-11-10→2026-11-10 | TAIFEX Proxy snapshots (2026-11-11) |
| 買權前十大 | +0 | 2026-11-10→2026-11-10 | TAIFEX Proxy snapshots (2026-11-11) |
| 賣權前十大 | +0 | 2026-11-10→2026-11-10 | TAIFEX Proxy snapshots (2026-11-11) |

### 16．資料來源、時間、時區與狀態

- 資料來源：TAIFEX 經 Cloudflare Worker Proxy
- 資料日期：2026-11-12；資料時間：2026-11-12 02:18:58；時區：`Asia/Taipei`
- 日盤／夜盤標記：日盤收盤後 + 夜盤盤後
- 未取得欄位 (20)：taiex.open, taiex.high, taiex.low, listed_breadth.up, listed_breadth.down, listed_breadth.flat, listed_breadth.limit_up, listed_breadth.limit_down, otc_breadth.up, otc_breadth.down, otc_breadth.flat, otc_breadth.limit_up, otc_breadth.limit_down, margin.fin_yi, margin.fin_chg_yi, sbl.sale_bal, sbl.sale_chg, turnover.listed, turnover.otc, turnover.total
- 註記：無日期端點為最新盤勢快照 (判定資料日期 2026-11-11，非 T0 2026-11-12)，適用：日盤價／法人交易／夜盤／選擇權法人；T0 相符時不另標註
- 註記：futures-price-after-hours 日期 2026-11-11 非今日 2026-11-12，視為無新節次，不採用
- 註記：futures-institutional-after-hours 日期 2026-11-11 非今日 2026-11-12，視為無新節次，不採用
- 註記：options-institutional-after-hours 日期 2026-11-11 非今日 2026-11-12，視為無新節次，不採用
- 註記：Call/Put Wall 與 Max Pain 資料日期 2026-11-11 (T0 2026-11-12 端點不穩，採最新可得)
- 註記：夜盤開高低收未取得 (proxy 與官方皆無)，僅成交量/OI/結算價
- 註記：法人 OI 未取得
- 註記：法人交易量變化無昨日交易端點，標 unavailable
- 註記：選擇權 chain 資料日期 2026-11-11 (T0 2026-11-12 端點不穩，採最新可得)

## 五、資料來源、時間與完整性

- 期貨/匯率為最新報價，其餘為 T0 收盤資料；時間皆為 `Asia/Taipei`。
- taiex：`TWSE OpenAPI MI_INDEX (備援)`
- institutional：`twse-proxy /institutional`
- margin_short：`TWSE MI_MARGN + TPEX margin_balance (張)`
- margin_ratio：`前值遞補 (DATA 2026-11-11；當日三源皆失敗；民間估算；官方無每日序列)`
- sbl：`TWSE TWT93U + TPEX margin_sbl`
- 期貨選擇權：`TAIFEX Proxy`
- 新聞：台股 Yahoo／國際 Fed＋CNBC＋MarketWatch；台股 Yahoo（不足時財訊快報備援）/ 國際 Fed 公告＋CNBC＋MarketWatch RSS；Fed 無摘要；investing 港股為主已退役；cnyes CSR、wantgoo JS 算繪、中央社/台灣央行路徑待查，未採用
- 美股/亞股/期貨/匯率/ADR/商品：`Yahoo Finance Chart API`；美債：`Yahoo Finance (備援)`
- 註記：twse-proxy 連線失敗，TAIEX 改用 MI_INDEX 備援
- 註記：大盤開高低未取得 (FinMind 失敗；MI_INDEX 無此欄)
- 註記：twtazu_od 備援日期不符 (回傳舊資料)，上市漲跌標 unavailable
- 註記：上櫃 highlight 日期不符或缺值 (回傳 1151111, T0=1151112)
- 註記：三大法人回傳日期 20261111 (T0 20261112)，採用最新可得
- 註記：HiStock 未取得，融資餘額/增減標 unavailable (官方逐股加總僅有張數)
- 註記：融券沿用官方逐股加總 (張)
- 註記：融資維持率未取得 (三源皆失敗；官方無每日序列)
- 註記：融資維持率採前值遞補 (DATA 2026-11-11)，非 T0 2026-11-12
- 註記：上市 MI_MARGN / TWT96U 無日期欄，採用最新可得
- 本報告僅整理資料，不提供交易判斷。

## 六、期現選方向對照

**規則：** 趨勢偏多／空＝現貨、期貨OI、選擇權日淨三者同向；避險／對沖＝現貨與期選反向；日內反轉＝日淨與夜淨反向；缺值標示，不推估。選擇權多空為看多看空口徑。

| 法人 | 現貨買賣超(億) | 期貨OI淨(口) | 期貨日淨 | 期貨夜淨 | 選擇權日淨 | 選擇權夜淨 | 判定 | 期選組合 | 資料來源 |
|---|---|---|---|---|---|---|---|---|---|
| 外資 | -7.7 | unavailable | -779 | unavailable | +6,098 | unavailable | 資料不足 | 資料不足 | twse-proxy／TAIFEX Proxy |
| 投信 | +185.9 | unavailable | +3,351 | unavailable | -2,907 | unavailable | 資料不足 | 資料不足 | twse-proxy／TAIFEX Proxy |
| 自營商 | +62.6 | unavailable | -92 | unavailable | +14,671 | unavailable | 資料不足 | 資料不足 | twse-proxy／TAIFEX Proxy |
