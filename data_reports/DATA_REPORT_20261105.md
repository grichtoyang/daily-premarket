# DATA_REPORT_20261105

- 報告日期：`2026-11-05`
- T0 交易日期：`2026-11-05`
- 資料產出時間：`2026-11-05 02:24:12`
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
| 加權指數 | 43,307.54 | 點 | TWSE OpenAPI MI_INDEX (備援) |
| 開盤 | unavailable | 點 | FinMind |
| 最高 | unavailable | 點 | FinMind |
| 最低 | unavailable | 點 | FinMind |
| 收盤 | 43,307.54 | 點 | TWSE OpenAPI MI_INDEX (備援) |
| 漲跌點數 | -1,612.60 | 點 | TWSE OpenAPI MI_INDEX (備援) |
| 漲跌幅 | -3.59 | % | TWSE OpenAPI MI_INDEX (備援) |
| 成交金額 | unavailable | 億元 | twse-proxy market_statistics |

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
| 外資 | -1,499.0 | 億元 | twse-proxy /institutional |
| 投信 | +272.6 | 億元 | twse-proxy /institutional |
| 自營商 | -375.2 | 億元 | twse-proxy /institutional |
| 三大法人合計 | -1,601.6 | 億元 | twse-proxy /institutional |

### 4. 融資融券

**資料來源：** 上市+上櫃 `HiStock` (金額口徑)；維持率 `istock.tw`；備援官方逐股加總

| 項目 | 數值 | 單位 | 資料來源 |
|---|---|---|---|
| 融資餘額 | unavailable | 億元 | HiStock |
| 融資增減 | unavailable | 億元 | HiStock |
| 融券餘額 | 257,961 | 張 | HiStock |
| 融券增減 | 71,711 | 張 | HiStock |
| 融資維持率 | 171.80 | % | 前值遞補 (DATA 2026-11-04；當日三源皆失敗；民間估算；官方無每日序列) |

### 5. 借券資料

**資料來源：** 上市 `TWSE OpenAPI TWT96U` (可借餘額)、上櫃 `TPEX OpenAPI tpex_margin_sbl`

| 項目 | 數值 | 單位 | 資料來源 |
|---|---|---|---|
| 借券餘額 | 2,602,612 | 張 | TWSE TWT93U + TPEX margin_sbl |
| 借券賣出餘額 | unavailable | 張 | TWSE TWT93U + TPEX margin_sbl |
| 借券賣出增減 | unavailable | 張 | TWSE TWT93U + TPEX margin_sbl |

### 6. 市場成交結構

**資料來源：** 上市 `twse-proxy market_statistics`、上櫃 `TPEX OpenAPI tpex_mainborad_highlight`

| 項目 | 成交金額 | 單位 | 資料來源 |
|---|---|---|---|
| 上市成交金額 | unavailable | 億元 | twse-proxy market_statistics |
| 上櫃成交金額 | unavailable | 億元 | TPEX |
| 上市櫃成交金額合計 | unavailable | 億元 | twse-proxy market_statistics+TPEX |

## 二、重要市場

### 1. 美股指數

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 收盤／最新值 | 漲跌點 | 漲跌幅 | 資料來源 |
|---|---|---|---|---|---|
| S&P 500 | ^GSPC | 7,704.19 | 135.27 | +1.79 | Yahoo Finance Chart API |
| Nasdaq Composite | ^IXIC | 25,881.03 | 509.02 | +2.01 | Yahoo Finance Chart API |
| Nasdaq 100 | ^NDX | 28,567.76 | 387.50 | +1.38 | Yahoo Finance Chart API |
| Dow Jones | ^DJI | 53,254.09 | 1,467.37 | +2.83 | Yahoo Finance Chart API |
| 費城半導體 SOX | ^SOX | 10,277.37 | -323.03 | -3.05 | Yahoo Finance Chart API |
| VIX | ^VIX | 16.73 | -4.10 | -19.68 | Yahoo Finance Chart API |

### 2. 亞洲主要指數

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 收盤／最新值 | 漲跌點 | 漲跌幅 | 資料來源 |
|---|---|---|---|---|---|
| 日經225 | ^N225 | 63,081.86 | -208.25 | -0.33 | Yahoo Finance Chart API |
| 韓國KOSPI | ^KS11 | 5,648.79 | -210.29 | -3.59 | Yahoo Finance Chart API |
| 香港恆生 | ^HSI | 23,525.97 | 132.65 | +0.57 | Yahoo Finance Chart API |
| 上海綜合 | 000001.SS | 3,608.10 | -29.93 | -0.82 | Yahoo Finance Chart API |
| 深圳成分 | 399001.SZ | 10,876.99 | -133.69 | -1.21 | Yahoo Finance Chart API |

### 3. 美股指數期貨

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 最新值 | 漲跌點 | 漲跌幅 | 資料來源 |
|---|---|---|---|---|---|
| S&P500期貨 | ES=F | 7,741.25 | 144.50 | +1.90 | Yahoo Finance Chart API |
| Nasdaq100期貨 | NQ=F | 28,728.75 | 423.00 | +1.49 | Yahoo Finance Chart API |
| 道瓊期貨 | YM=F | 53,430.00 | 1,535.00 | +2.96 | Yahoo Finance Chart API |
| Russell2000期貨 | RTY=F | 2,867.80 | 42.80 | +1.52 | Yahoo Finance Chart API |

### 4. 美國國債殖利率

**資料來源：** `U.S. Treasury Fiscal Data API` (失敗時備援 Treasury yield.xml 與 `Yahoo Finance`)

| 項目 | API 資料欄位／識別 | 殖利率 | 日變化 | 資料來源 |
|---|---|---|---|---|
| 美國 2 年期殖利率 | 2 Yr | 4.61 | 0.02 | U.S. Treasury yield.xml (網頁備援) |
| 美國 10 年期殖利率 | 10 Yr | 4.90 | -0.05 | Yahoo Finance (備援) |
| 美國 30 年期殖利率 | 30 Yr | 5.30 | -0.02 | Yahoo Finance (備援) |

### 5. 主要匯率

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 最新值 | 漲跌點 | 漲跌幅 | 資料來源 |
|---|---|---|---|---|---|
| USD/TWD | TWD=X | 32.83 | 0.25 | +0.76 | Yahoo Finance Chart API |
| DXY美元指數 | DX-Y.NYB | 101.46 | -0.41 | -0.41 | Yahoo Finance Chart API |
| USD/JPY | JPY=X | 158.36 | 0.44 | +0.28 | Yahoo Finance Chart API |
| USD/KRW | KRW=X | 1,340.36 | -4.45 | -0.33 | Yahoo Finance Chart API |

### 6. 台灣相關ADR

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 收盤／最新值 | 漲跌點 | 漲跌幅 | 資料來源 |
|---|---|---|---|---|---|
| 台積電ADR | TSM | 396.93 | -7.86 | -1.94 | Yahoo Finance Chart API |
| 聯電ADR | UMC | 16.07 | -0.33 | -2.04 | Yahoo Finance Chart API |
| 日月光ADR | ASX | 37.14 | -1.91 | -4.89 | Yahoo Finance Chart API |

### 7. 原油黃金Bitcoin

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 收盤／最新值 | 漲跌點 | 漲跌幅 | 資料來源 |
|---|---|---|---|---|---|
| WTI原油期貨 | CL=F | 88.83 | -7.26 | -7.56 | Yahoo Finance Chart API |
| 黃金期貨 | GC=F | 4,078.70 | 138.30 | +3.51 | Yahoo Finance Chart API |
| Bitcoin | BTC-USD | 80,542.44 | 3,197.39 | +4.13 | Yahoo Finance Chart API |

### 8. 重大經濟數據、央行事件與重大市場新聞

**資料來源：** 台股 `tw.stock.yahoo.com` (含內文摘要)；國際 `Fed 公告 RSS`＋`CNBC`＋`MarketWatch` (標題、來源、時間與連結)

- 事件1：｜配息基金推薦｜
  - 來源：Yahoo 台股；發布時間：2026-11-03T03:03:12Z；台北時間：2026-11-03 11:03
  - 摘要：對於習慣領月薪的上班族來說，「每月配息」的基金特別有吸引力。不過，許多人在找「月配息基金推薦」或「2026 配息基金推薦名單」時，往往只注意配息率高低、以及能否每月穩定領息。
  - 原文連結：https://tw.stock.yahoo.com/news/%E6%9C%88%E9%85%8D%E6%81%AF%E5%9F%BA%E9%87%91%E6%98%AF%E4%BB%80%E9%BA%BC%EF%BC%9F%E9%85%8D%E6%81%AF%E5%9F%BA%E9%87%91%E6%8E%A8%E8%96%A6%E6%80%8E%E9%BA%BC%E6%8C%91%EF%BC%9F4%E5%A4%A7%E6%8C%91%E9%81%B8%E9%87%8D%E9%BB%9E%E4%B8%80%E6%AC%A1%E7%9C%8B-030312577.html
- 事件2：台股千點回馬槍仍收黑 聯發科、日月光翻紅衝鋒
  - 來源：Yahoo 台股；發布時間：2026-11-04T09:08:11Z；台北時間：2026-11-04 17:08
  - 摘要：台股急殺逾千點後急拉，收跌358點、4萬3仍失守！今(4)日加權指數開高走低，盤中一度下挫1451.72點、跌破4萬2，隨美國期中選舉結果逐步明朗、美股期指與韓股回升，台股自低點回升逾千點，終場下跌358.63點、跌幅0.83%，收42,9
  - 原文連結：https://tw.stock.yahoo.com/news/%E5%A4%96%E8%B3%87%E7%A0%8D1498%E5%84%84%E5%8F%B2%E4%B8%8A%E7%AC%AC5%E5%A4%A7%EF%BC%81%E5%8F%B0%E8%82%A1%E8%B7%8C%E7%A0%B44%E8%90%AC2%E4%B8%8A%E6%BC%94%E5%8D%83%E9%BB%9E%E5%9B%9E%E9%A6%AC%E6%A7%8D%E4%BB%8D%E6%94%B6%E9%BB%91-%E8%81%AF%E7%99%BC%E7%A7%91%E3%80%81%E6%97%A5%E6%9C%88%E5%85%89%E7%BF%BB%E7%B4%85%E7%AA%81%E5%9C%8D%EF%BD%9Cyahoo%E8%B2%A1%E7%B6%93%E6%8E%83%E6%8F%8F-090811547.html
- 事件3：AI下一棒誰接？投信點名封裝、光通訊、電源三路接棒
  - 來源：Yahoo 台股；發布時間：2026-11-04T09:51:53Z；台北時間：2026-11-04 17:51
  - 摘要：[Newtalk新聞] AI 投資熱潮持續延燒，從高頻寬記憶體（HBM）、先進製程到 AI 代理（AI Agent）與實體 AI（Physical AI），相關商機正從晶片擴散至整體供應鏈。國泰投信今（4）日攜手大和國泰證券舉辦「從矽谷到矽
  - 原文連結：https://tw.stock.yahoo.com/news/ai%E4%B8%8B-%E6%A3%92%E8%AA%B0%E6%8E%A5-%E6%8A%95%E4%BF%A1%E6%8F%AD3%E5%A4%A7%E4%BE%9B%E6%87%89%E9%8F%88%E5%95%86%E6%A9%9F-%E8%A8%98%E6%86%B6%E9%AB%94%E9%9C%80%E6%B1%82%E7%9C%8B%E5%88%B02029%E5%B9%B4-095153970.html
- 事件4：永豐銀盜轉手法曝光 銀行已通報並提醒金融同業
  - 來源：Yahoo 台股；發布時間：2026-11-04T09:45:00Z；台北時間：2026-11-04 17:45
  - 摘要：【記者羅元駿／台北報導】針對昨（3）日客戶異常轉帳事件，永豐銀今天說明，內部經查為外部駭客利用新網銀交易系統的供應商安全設定，造成客戶帳戶款項遭不明轉出。另外也指出，依據事證顯示並無個資外洩軌跡，永豐銀也已啓動資安及個資盤點，確保資料不外洩
  - 原文連結：https://tw.stock.yahoo.com/news/%E6%B0%B8%E8%B1%90%E9%8A%80%E8%A1%8C%E5%B8%B3%E6%88%B6%E7%9B%9C%E8%BD%89%E6%A1%88-%E5%85%AC%E5%8F%B8%E8%AD%89%E5%AF%A6%E5%A4%96%E9%83%A8%E9%A7%AD%E5%AE%A2%E5%B0%8E%E8%87%B4-%E7%84%A1%E5%AE%A2%E6%88%B6%E5%80%8B%E8%B3%87%E5%A4%96%E6%B4%A9-094500772.html
- 事件5：美選後誰漲得多？野村用近30年數據找線索
  - 來源：Yahoo 台股；發布時間：2026-11-04T08:39:51Z；台北時間：2026-11-04 16:39
  - 摘要：美國期中選舉於當地時間11月3日舉行，隨選舉不確定性逐步消退，市場焦點重回企業獲利與產業成長動能。根據統計，1998年至2022年近7次美國期中選舉後，美股與台股加權指數雙雙7次全漲，平均報酬分別為9.22%及9.61%，顯示選後股市上漲並
  - 原文連結：https://tw.stock.yahoo.com/news/%E8%B7%8C%E7%A0%B44%E8%90%AC3%E5%85%8D%E9%A9%9A%EF%BC%9F%E9%87%8E%E6%9D%91%E6%9B%AC%E8%BF%9130%E5%B9%B4%E6%9C%9F%E4%B8%AD%E9%81%B8%E8%88%89%E5%BE%8C%E6%95%B8%E6%93%9A%EF%BC%9A%E7%BE%8E%E8%82%A1%E5%8F%B0%E8%82%A1%E3%80%8C7%E6%88%B07%E5%8B%9D%E3%80%8D-085726314.html
- 事件6：股票漲了權證卻跌？拆解認購權證價格5大變數
  - 來源：Yahoo 台股；發布時間：2026-11-03T08:23:18Z；台北時間：2026-11-03 16:23
  - 摘要：「明明看對方向，標的股票也漲了，為什麼買進的認購權證價格反而下跌？」這是許多權證新手在實際交易中最常遇到的疑惑，甚至常誤以為是發行券商在背後動手腳。

事實上，權證屬於衍生性金融商品，它的定價並非與股價「一對一綁定」，而是由標的股價、剩餘天
  - 原文連結：https://tw.stock.yahoo.com/news/%E6%A8%99%E7%9A%84%E8%82%A1%E7%A5%A8%E4%B8%8A%E6%BC%B2%EF%BC%8C%E8%AA%8D%E8%B3%BC%E6%AC%8A%E8%AD%89%E7%82%BA%E4%BD%95%E5%8F%8D%E8%80%8C%E4%B8%8B%E8%B7%8C%EF%BC%9F%E4%B8%80%E6%96%87%E7%9C%8B%E6%87%82%E5%BD%B1%E9%9F%BF%E6%AC%8A%E8%AD%89%E5%83%B9%E6%A0%BC%E7%9A%84-5-%E5%A4%A7%E8%AE%8A%E5%8B%95%E5%9B%A0%E7%B4%A0-082318070.html
- 事件7：Federal Reserve Board announces approval of application by The Bank of Nova Scotia
  - 來源：Federal Reserve；發布時間：Thu, 29 Oct 2026 20:30:00 GMT；台北時間：2026-10-30 04:30
  - 摘要：Federal Reserve Board announces approval of application by The Bank of Nova Scotia
  - 原文連結：https://www.federalreserve.gov/newsevents/pressreleases/orders20261029a.htm
- 事件8：10-year Treasury yield slides as traders mull over Democrats' midterm victories, oil prices drop
  - 來源：CNBC；發布時間：Wed, 04 Nov 2026 17:11:00 GMT；台北時間：2026-11-05 01:11
  - 摘要：Treasury yields were last little changed Wednesday as investors weighed big wins from Democrats in the U.S. midterm elections.
  - 原文連結：https://www.cnbc.com/2026/11/03/treasury-yields-fall-as-democrats-win-big-in-us-midterm-elections.html
- 事件9：These 12 stocks are good bets to beat the 10-year Treasury over the next decade
  - 來源：MarketWatch；發布時間：Wed, 04 Nov 2026 18:03:00 GMT；台北時間：2026-11-05 02:03
  - 摘要：Investment newsletters&#x2019; favorite Dividend Aristocrat stocks
  - 原文連結：https://www.marketwatch.com/story/these-12-stocks-are-good-bets-to-beat-the-10-year-treasury-over-the-next-decade-cc4f308b?mod=mw_rss_topstories
- 事件10：AI data center stocks and Musk's SpaceX decline as Texas governor result raises risks of a slowdown
  - 來源：CNBC；發布時間：Wed, 04 Nov 2026 14:43:57 GMT；台北時間：2026-11-04 22:43
  - 摘要：AI fortunes were mixed as premarket trading opened on Wednesday.
  - 原文連結：https://www.cnbc.com/2026/11/04/ai-stocks-texas-governor-data-centers.html
- 事件11：Hospital stocks rally while drugmakers brace for scrutiny. Here's what the Democratic wave means for healthcare.
  - 來源：MarketWatch；發布時間：Wed, 04 Nov 2026 17:19:00 GMT；台北時間：2026-11-05 01:19
  - 摘要：The Democratic victory in the midterm elections could be a huge boon to the nation&#x2019;s largest hospitals.
  - 原文連結：https://www.marketwatch.com/story/hospital-stocks-rally-while-drugmakers-brace-for-scrutiny-heres-what-the-democratic-wave-means-for-healthcare-625b79f3?mod=mw_rss_topstories
- 事件12：Micron and other chip stocks slip as election results strike at the core of data-center optimism
  - 來源：MarketWatch；發布時間：Wed, 04 Nov 2026 15:17:00 GMT；台北時間：2026-11-04 23:17
  - 摘要：Democratic victories in Texas and other states raise long-term questions about the AI buildout, though they do not &#x201c;unwind projects already fun
  - 原文連結：https://www.marketwatch.com/story/micron-and-other-chip-stocks-slip-as-election-results-strike-at-the-core-of-data-center-optimism-b55d19b3?mod=mw_rss_topstories


## 三、期貨

**資料來源：**
1. Cloudflare Workers：TAIFEX Proxy — https://taifex.grichtoyang.workers.dev/
2. TAIFEX Open API — https://openapi.taifex.com.tw/

近月契約月份：202611 (日盤成交量最大者)；交易日期：2026-11-05

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
| 前十大交易人多方 OI | 94,444 | TAIFEX Proxy |
| 前十大交易人空方 OI | 82,876 | TAIFEX Proxy |
| 前十大交易人多空淨 OI | +11,568 | TAIFEX Proxy |
| 多空淨 OI 變化 (2026-11-03→2026-11-03) | +0 | TAIFEX Proxy snapshots (2026-11-04) |
- 資料日期：2026-11-03 (TypeOfTraders=0 全部交易人；契約月份 202611)

### 5．日盤、夜盤法人交易資料

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 外資日盤多單交易量 | 93,663 | TAIFEX Proxy |
| 外資日盤空單交易量 | 95,523 | TAIFEX Proxy |
| 外資日盤多空淨交易量 | -1,860 | TAIFEX Proxy |
| 外資夜盤多單交易量 | unavailable | TAIFEX Proxy |
| 外資夜盤空單交易量 | unavailable | TAIFEX Proxy |
| 外資夜盤多空淨交易量 | unavailable | TAIFEX Proxy |
| 外資日盤／夜盤交易量變化 | unavailable | TAIFEX Proxy |
| 投信日盤多空淨交易量 | +2,502 | TAIFEX Proxy |
| 投信夜盤多空淨交易量 | unavailable | TAIFEX Proxy |
| 投信日盤／夜盤交易量變化 | unavailable | TAIFEX Proxy |
| 自營商日盤多空淨交易量 | -991 | TAIFEX Proxy |
| 自營商夜盤多空淨交易量 | unavailable | TAIFEX Proxy |
| 自營商日盤／夜盤交易量變化 | unavailable | TAIFEX Proxy |
| 三大法人日盤多空淨交易量 | -349 | TAIFEX Proxy |
| 三大法人夜盤多空淨交易量 | unavailable | TAIFEX Proxy |
| 法人日盤交易金額淨額 (億元) | -26.1 | TAIFEX Proxy |
| 法人夜盤交易金額淨額 (億元) | unavailable | TAIFEX Proxy |

### 6．期貨與現貨關係

| 項目 | 數值 | 資料來源 |
|---|---|---|
| 台指期近月價格 | 43,204 | TAIFEX Proxy |
| 加權指數價格 | 43,307.54 | TWSE OpenAPI MI_INDEX (備援) |
| 台指期與加權指數價差 | -103.54 | TAIFEX Proxy+TWSE OpenAPI MI_INDEX (備援) |
| 價差百分比 | -0.24 | TAIFEX Proxy+TWSE OpenAPI MI_INDEX (備援) |
| 日盤基差 | -103.54 | TAIFEX Proxy+TWSE OpenAPI MI_INDEX (備援) |
| 夜盤價格相對日盤收盤的變化 | unavailable | 端點未提供 |

### 7．日盤、夜盤與籌碼變化對照

#### 7.1 日夜盤價格與成交量對照 (變化 = 日盤 - 夜盤)

| 項目 | 日盤 | 夜盤 | 變化 (日-夜) | 資料來源 |
|---|---|---|---|---|
| 收盤價 | 43,204 | unavailable | unavailable | TAIFEX Proxy |
| 成交量 | 113,674 | unavailable | unavailable | TAIFEX Proxy |
- 台指期總 OI 前日變化：+0（來源：TAIFEX Proxy）


#### 7.2 法人籌碼日夜盤對照 (淨變化 = 日盤淨 - 夜盤淨；OI 為日盤收盤後總量，前日變化另列)

| 法人 | 交易量 |  |  |  |  |  |  | 未平倉量 |  |  |  | 資料來源 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|  | **日盤多單** | **日盤空單** | **日盤淨** | **夜盤多單** | **夜盤空單** | **夜盤淨** | **淨變化 (日-夜)** | **OI多方** | **OI空方** | **OI淨** | **OI前日變化** |  |
| 外資 | 93,663 | 95,523 | -1,860 | unavailable | unavailable | unavailable | unavailable | unavailable | unavailable | unavailable | unavailable | TAIFEX Proxy |
| 投信 | 2,514 | 12 | +2,502 | unavailable | unavailable | unavailable | unavailable | unavailable | unavailable | unavailable | unavailable | TAIFEX Proxy |
| 自營商 | 12,388 | 13,379 | -991 | unavailable | unavailable | unavailable | unavailable | unavailable | unavailable | unavailable | unavailable | TAIFEX Proxy |
| 三大法人合計 | 108,565 | 108,914 | -349 | unavailable | unavailable | unavailable | unavailable | 0 | 0 | +0 | +0 | TAIFEX Proxy |

#### 7.3 前十大交易人日夜盤對照 (OI 無日夜拆分，列收盤後總量)

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 前十大交易人多方 OI | 94,444 | TAIFEX Proxy |
| 前十大交易人空方 OI | 82,876 | TAIFEX Proxy |
| 前十大交易人多空淨 OI | +11,568 | TAIFEX Proxy |
| 前十大交易人多空淨 OI 變化 (2026-11-03→2026-11-03) | +0 | TAIFEX Proxy snapshots (2026-11-04) |

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
| 交易日期 | 2026-11-05 | TAIFEX Proxy |
| 到期月份／到期日 | 202611W1 | TAIFEX Proxy |
| 資料更新時間 | 2026-11-05 02:24:12 | 本機 |
| 日盤／夜盤標記 | 日盤收盤後資料 | TAIFEX Proxy |

### 2．Call 總成交量、OI、OI 增減

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Call 總成交量 | 438,164 | TAIFEX Proxy |
| Call 總未平倉量 OI | 123,799 | TAIFEX Proxy |
| Call OI 增減 (2026-11-04→2026-11-05) | +0 | TAIFEX Proxy snapshots (2026-11-04) |

### 3．Put 總成交量、OI、OI 增減

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Put 總成交量 | 387,135 | TAIFEX Proxy |
| Put 總未平倉量 OI | 65,804 | TAIFEX Proxy |
| Put OI 增減 (2026-11-04→2026-11-05) | +0 | TAIFEX Proxy snapshots (2026-11-04) |

### 4．Call／Put 比例與變化

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Call／Put 成交量比例 | 1.13 | TAIFEX Proxy |
| Call／Put 未平倉量比例 | 1.88 | TAIFEX Proxy |
| Put／Call Ratio | 0.53 | TAIFEX Proxy |
| Call／Put 比例變化 (量比 2026-11-02→2026-11-03) | -13.76 | TAIFEX Proxy |
| 與前一交易日比較 (OI 比 2026-11-02→2026-11-03) | -13.81 | TAIFEX Proxy |
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
| 外資 Call夜買 | 41,041 | TAIFEX Proxy |
| 外資 Call夜賣 | 40,726 | TAIFEX Proxy |
| 外資 Call夜淨 | +315 | TAIFEX Proxy |
| 外資 Put夜買 | 39,417 | TAIFEX Proxy |
| 外資 Put夜賣 | 39,990 | TAIFEX Proxy |
| 外資 Put夜淨 | -573 | TAIFEX Proxy |
| 外資 日盤淨總量 | +3,629 | TAIFEX Proxy |
| 外資 Call日夜淨增減 (日－夜) | -1,311 | TAIFEX Proxy |
| 外資 Put日夜淨增減 (日－夜) | -4,052 | TAIFEX Proxy |

### 6．自營商 Call／Put 部位

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 自營商 Call日買 | 113,663 | TAIFEX Proxy |
| 自營商 Call日賣 | 117,752 | TAIFEX Proxy |
| 自營商 Call日淨 | -4,089 | TAIFEX Proxy |
| 自營商 Put日買 | 96,474 | TAIFEX Proxy |
| 自營商 Put日賣 | 101,454 | TAIFEX Proxy |
| 自營商 Put日淨 | -4,980 | TAIFEX Proxy |
| 自營商 Call夜買 | 20,047 | TAIFEX Proxy |
| 自營商 Call夜賣 | 22,430 | TAIFEX Proxy |
| 自營商 Call夜淨 | -2,383 | TAIFEX Proxy |
| 自營商 Put夜買 | 20,192 | TAIFEX Proxy |
| 自營商 Put夜賣 | 20,485 | TAIFEX Proxy |
| 自營商 Put夜淨 | -293 | TAIFEX Proxy |
| 自營商 日盤淨總量 | +891 | TAIFEX Proxy |
| 自營商 Call日夜淨增減 (日－夜) | -1,706 | TAIFEX Proxy |
| 自營商 Put日夜淨增減 (日－夜) | -4,687 | TAIFEX Proxy |

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
| 對應到期月份 | 202611W1 | TAIFEX Proxy |
| 與前一交易日的變化 (2026-11-04→2026-11-05) | +0 | TAIFEX Proxy snapshots (2026-11-04) |

### 12．Put Wall

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Put Wall 價位 | 42,000 | TAIFEX Proxy |
| 對應到期月份 | 202611W1 | TAIFEX Proxy |
| 與前一交易日的變化 (2026-11-04→2026-11-05) | +0 | TAIFEX Proxy snapshots (2026-11-04) |

### 13．Gamma Wall

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Gamma Wall 價位 | 44,000.00 | TAIFEX Proxy (options-gamma-levels) |
| 對應到期月份 | 202611W1 | TAIFEX Proxy |
| 資料日期 | 2026-11-05 | TAIFEX Proxy (options-gamma-levels) |

### 14．Gamma Flip

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Gamma Flip 價位 | 39,901.34 | TAIFEX Proxy (options-gamma-levels) |
| 對應到期月份 | 202611W1 | TAIFEX Proxy |
| 資料日期 | 2026-11-05 | TAIFEX Proxy (options-gamma-levels) |

### 15．Max Pain

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Max Pain 價位 | 43,100 | TAIFEX Proxy |
| 對應到期月份 | 202611W1 | TAIFEX Proxy |
| 與前一交易日的變化 (2026-11-04→2026-11-05) | +0 | TAIFEX Proxy snapshots (2026-11-04) |

### 17．選擇權法人日盤、夜盤交易

| 法人 | 日盤多單 | 日盤空單 | 日盤淨 | 夜盤多單 | 夜盤空單 | 夜盤淨 | 淨變化 (日-夜) | 資料來源 |
|---|---|---|---|---|---|---|---|---|
| 外資 | 295,701 | 292,072 | +3,629 | unavailable | unavailable | unavailable | unavailable | TAIFEX Proxy |
| 投信 | 202 | 15,585 | -15,383 | unavailable | unavailable | unavailable | unavailable | TAIFEX Proxy |
| 自營商 | 215,117 | 214,226 | +891 | unavailable | unavailable | unavailable | unavailable | TAIFEX Proxy |
| 三大法人合計 | 511,020 | 521,883 | -10,863 | unavailable | unavailable | unavailable | unavailable | TAIFEX Proxy |
- 方法論：多方＝買Call＋賣Put（看多），空方＝賣Call＋買Put（看空），淨額＝看多－看空（已用 Call／Put 拆分頁交叉驗算一致）
- 公式：多方(買)－空方(賣)＝（買call＋賣put）－（賣call＋買put）＝看多－看空
- 速記：多＝BC＋SP、空＝SC＋BP

#### 法人多空力道表（金額・億元；上游千元／1e5）

| 法人 | 日多方力道 | 日空方力道 | 日淨多空力道 | 夜多方力道 | 夜空方力道 | 夜淨多空力道 | 日淨－夜淨 | 資料來源 |
|---|---|---|---|---|---|---|---|---|
| 外資 | 21.05 | 20.57 | +0.47 | 7.00 | 6.93 | +0.07 | +0.41 | TAIFEX Proxy |
| 投信 | 0.05 | 14.56 | -14.51 | 0.00 | 0.00 | +0 | -14.51 | TAIFEX Proxy |
| 自營商 | 33.99 | 21.10 | +12.89 | 5.38 | 4.84 | +0.54 | +12.35 | TAIFEX Proxy |
| 三大法人合計 | 55.09 | 56.23 | -1.14 | 12.38 | 11.77 | +0.61 | -1.75 | TAIFEX Proxy |

### 18．選擇權前十大

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 買權多方 OI | 10,686 | TAIFEX Proxy |
| 買權空方 OI | 13,733 | TAIFEX Proxy |
| 買權多空淨 OI | -3,047 | TAIFEX Proxy |
| 買權多空淨 OI 變化 (2026-11-03→2026-11-03) | +0 | TAIFEX Proxy snapshots (2026-11-04) |

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 賣權多方 OI | 7,889 | TAIFEX Proxy |
| 賣權空方 OI | 10,181 | TAIFEX Proxy |
| 賣權多空淨 OI | -2,292 | TAIFEX Proxy |
| 賣權多空淨 OI 變化 (2026-11-03→2026-11-03) | +0 | TAIFEX Proxy snapshots (2026-11-04) |
- 資料日期：買權 2026-11-03／賣權 2026-11-03 (TypeOfTraders=0 全部交易人；契約月份 202611)

#### 大戶流向（全日；前十大無日夜拆分）

| 項目 | 淨變化 | 區間 | 資料來源 |
|---|---|---|---|
| 期貨前十大 | +0 | 2026-11-03→2026-11-03 | TAIFEX Proxy snapshots (2026-11-04) |
| 買權前十大 | +0 | 2026-11-03→2026-11-03 | TAIFEX Proxy snapshots (2026-11-04) |
| 賣權前十大 | +0 | 2026-11-03→2026-11-03 | TAIFEX Proxy snapshots (2026-11-04) |

### 16．資料來源、時間、時區與狀態

- 資料來源：TAIFEX 經 Cloudflare Worker Proxy
- 資料日期：2026-11-05；資料時間：2026-11-05 02:24:12；時區：`Asia/Taipei`
- 日盤／夜盤標記：日盤收盤後 + 夜盤盤後
- 未取得欄位 (20)：taiex.open, taiex.high, taiex.low, listed_breadth.up, listed_breadth.down, listed_breadth.flat, listed_breadth.limit_up, listed_breadth.limit_down, otc_breadth.up, otc_breadth.down, otc_breadth.flat, otc_breadth.limit_up, otc_breadth.limit_down, margin.fin_yi, margin.fin_chg_yi, sbl.sale_bal, sbl.sale_chg, turnover.listed, turnover.otc, turnover.total
- 註記：無日期端點為最新盤勢快照 (判定資料日期 2026-11-04，非 T0 2026-11-05)，適用：日盤價／法人交易／夜盤／選擇權法人；T0 相符時不另標註
- 註記：futures-price-after-hours 日期 2026-11-04 非今日 2026-11-05，視為無新節次，不採用
- 註記：futures-institutional-after-hours 日期 2026-11-04 非今日 2026-11-05，視為無新節次，不採用
- 註記：options-institutional-after-hours 日期 2026-11-04 非今日 2026-11-05，視為無新節次，不採用
- 註記：Call/Put Wall 與 Max Pain 資料日期 2026-11-04 (T0 2026-11-05 端點不穩，採最新可得)
- 註記：夜盤開高低收未取得 (proxy 與官方皆無)，僅成交量/OI/結算價
- 註記：法人 OI 未取得
- 註記：法人交易量變化無昨日交易端點，標 unavailable
- 註記：選擇權 chain 資料日期 2026-11-04 (T0 2026-11-05 端點不穩，採最新可得)

## 五、資料來源、時間與完整性

- 期貨/匯率為最新報價，其餘為 T0 收盤資料；時間皆為 `Asia/Taipei`。
- taiex：`TWSE OpenAPI MI_INDEX (備援)`
- listed_breadth：`twse-proxy`
- listed_turnover：`twse-proxy market_statistics`
- institutional：`twse-proxy /institutional`
- margin_short：`TWSE MI_MARGN + TPEX margin_balance (張)`
- margin_ratio：`前值遞補 (DATA 2026-11-04；當日三源皆失敗；民間估算；官方無每日序列)`
- sbl：`TWSE TWT93U + TPEX margin_sbl`
- 期貨選擇權：`TAIFEX Proxy`
- 新聞：台股 Yahoo／國際 Fed＋CNBC＋MarketWatch；台股 Yahoo（不足時財訊快報備援）/ 國際 Fed 公告＋CNBC＋MarketWatch RSS；Fed 無摘要；investing 港股為主已退役；cnyes CSR、wantgoo JS 算繪、中央社/台灣央行路徑待查，未採用
- 美股/亞股/期貨/匯率/ADR/商品：`Yahoo Finance Chart API`；美債：`Yahoo Finance (備援)`
- 註記：twse-proxy taiex 缺值，改用 MI_INDEX 備援
- 註記：大盤開高低未取得 (FinMind 失敗；MI_INDEX 無此欄)
- 註記：twtazu_od 備援日期不符 (回傳舊資料)，上市漲跌標 unavailable
- 註記：上櫃 highlight 日期不符或缺值 (回傳 1151104, T0=1151105)
- 註記：三大法人回傳日期 20261104 (T0 20261105)，採用最新可得
- 註記：HiStock 未取得，融資餘額/增減標 unavailable (官方逐股加總僅有張數)
- 註記：融券沿用官方逐股加總 (張)
- 註記：融資維持率未取得 (三源皆失敗；官方無每日序列)
- 註記：融資維持率採前值遞補 (DATA 2026-11-04)，非 T0 2026-11-05
- 註記：上市 MI_MARGN / TWT96U 無日期欄，採用最新可得
- 本報告僅整理資料，不提供交易判斷。

## 六、期現選方向對照

**規則：** 趨勢偏多／空＝現貨、期貨OI、選擇權日淨三者同向；避險／對沖＝現貨與期選反向；日內反轉＝日淨與夜淨反向；缺值標示，不推估。選擇權多空為看多看空口徑。

| 法人 | 現貨買賣超(億) | 期貨OI淨(口) | 期貨日淨 | 期貨夜淨 | 選擇權日淨 | 選擇權夜淨 | 判定 | 期選組合 | 資料來源 |
|---|---|---|---|---|---|---|---|---|---|
| 外資 | -1,499.0 | unavailable | -1,860 | unavailable | +3,629 | unavailable | 資料不足 | 資料不足 | twse-proxy／TAIFEX Proxy |
| 投信 | +272.6 | unavailable | +2,502 | unavailable | -15,383 | unavailable | 資料不足 | 資料不足 | twse-proxy／TAIFEX Proxy |
| 自營商 | -375.2 | unavailable | -991 | unavailable | +891 | unavailable | 資料不足 | 資料不足 | twse-proxy／TAIFEX Proxy |
