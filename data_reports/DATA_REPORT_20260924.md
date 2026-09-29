# DATA_REPORT_20260924

- 報告日期：`2026-09-29`
- T0 交易日期：`2026-09-24`
- 資料產出時間：`2026-09-29 08:08:43`
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
| 借券餘額 | 2,441,375 | 張 | TWSE TWT93U + TPEX margin_sbl |
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
| S&P 500 | ^GSPC | 7,683.69 | -59.72 | -0.77 | Yahoo Finance Chart API |
| Nasdaq Composite | ^IXIC | 26,820.38 | -248.34 | -0.92 | Yahoo Finance Chart API |
| Nasdaq 100 | ^NDX | 30,276.81 | -331.32 | -1.08 | Yahoo Finance Chart API |
| Dow Jones | ^DJI | 51,481.51 | -347.11 | -0.67 | Yahoo Finance Chart API |
| 費城半導體 SOX | ^SOX | 12,465.24 | -203.69 | -1.61 | Yahoo Finance Chart API |
| VIX | ^VIX | 16.07 | 1.20 | +8.07 | Yahoo Finance Chart API |

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
| S&P500期貨 | ES=F | 7,750.00 | -53.75 | -0.69 | Yahoo Finance Chart API |
| Nasdaq100期貨 | NQ=F | 30,598.00 | -291.25 | -0.94 | Yahoo Finance Chart API |
| 道瓊期貨 | YM=F | 51,848.00 | -315.00 | -0.60 | Yahoo Finance Chart API |
| Russell2000期貨 | RTY=F | 2,840.60 | -18.70 | -0.65 | Yahoo Finance Chart API |

### 4. 美國國債殖利率

**資料來源：** `U.S. Treasury Fiscal Data API` (失敗時備援 Treasury yield.xml 與 `Yahoo Finance`)

| 項目 | API 資料欄位／識別 | 殖利率 | 日變化 | 資料來源 |
|---|---|---|---|---|
| 美國 2 年期殖利率 | 2 Yr | 4.92 | 0.11 | U.S. Treasury yield.xml (網頁備援) |
| 美國 10 年期殖利率 | 10 Yr | 5.24 | 0.06 | Yahoo Finance (備援) |
| 美國 30 年期殖利率 | 30 Yr | 5.56 | 0.06 | Yahoo Finance (備援) |

### 5. 主要匯率

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 最新值 | 漲跌點 | 漲跌幅 | 資料來源 |
|---|---|---|---|---|---|
| USD/TWD | TWD=X | 31.78 | 0.00 | +0.01 | Yahoo Finance Chart API |
| DXY美元指數 | DX-Y.NYB | 101.19 | 0.22 | +0.22 | Yahoo Finance Chart API |
| USD/JPY | JPY=X | 157.45 | -0.01 | -0.01 | Yahoo Finance Chart API |
| USD/KRW | KRW=X | 1,359.28 | 4.77 | +0.35 | Yahoo Finance Chart API |

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
| WTI原油期貨 | CL=F | 93.18 | 0.77 | +0.83 | Yahoo Finance Chart API |
| 黃金期貨 | GC=F | 4,158.90 | -162.30 | -3.76 | Yahoo Finance Chart API |
| Bitcoin | BTC-USD | 83,478.63 | -979.45 | -1.16 | Yahoo Finance Chart API |

### 8. 重大經濟數據、央行事件與重大市場新聞

**資料來源：** 台股 `tw.stock.yahoo.com` (含內文摘要)；國際 `Fed 公告 RSS`＋`CNBC`＋`MarketWatch` (標題、來源、時間與連結)

- 事件1：歌禮宣佈同類首創和同類最佳的口服小分子IL-17A抑制劑ASC50治療斑塊狀銀屑病在美國的28天概念驗證臨床研究取得積極結果
  - 來源：Yahoo 台股；發布時間：2026-09-29T00:00:00Z；台北時間：2026-09-29 08:00
  - 摘要：歌禮製藥有限公司（香港聯交所代碼：1672，簡稱「歌禮」）宣佈，ASC50在美國輕度至中度斑塊狀銀屑病患者中開展的一項隨機、雙盲、安慰劑對照的28天概念驗證臨床試驗取得積極結果。該I期研究旨在評估每日一次200毫克ASC50在輕度至中度斑塊
  - 原文連結：https://tw.stock.yahoo.com/news/%E6%AD%8C%E7%A6%AE%E5%AE%A3%E4%BD%88%E5%90%8C%E9%A1%9E%E9%A6%96%E5%89%B5%E5%92%8C%E5%90%8C%E9%A1%9E%E6%9C%80%E4%BD%B3%E7%9A%84%E5%8F%A3%E6%9C%8D%E5%B0%8F%E5%88%86%E5%AD%90il-17a%E6%8A%91%E5%88%B6%E5%8A%91asc50%E6%B2%BB%E7%99%82%E6%96%91%E5%A1%8A%E7%8B%80%E9%8A%80%E5%B1%91%E7%97%85%E5%9C%A8%E7%BE%8E%E5%9C%8B%E7%9A%8428%E5%A4%A9%E6%A6%82%E5%BF%B5%E9%A9%97%E8%AD%89%E8%87%A8%E5%BA%8A%E7%A0%94%E7%A9%B6%E5%8F%96%E5%BE%97%E7%A9%8D%E6%A5%B5%E7%B5%90%E6%9E%9C-000000435.html
- 事件2：美的將在Data Center World Asia 2026發佈行業首創電力-製冷超融合架構
  - 來源：Yahoo 台股；發布時間：2026-09-28T23:58:00Z；台北時間：2026-09-29 07:58
  - 摘要：美的樓宇科技（Midea Building Technologies，簡稱「MBT」）將於9月29日至30日在新加坡濱海灣金沙參加Data Centre World Asia 2026（2026新加坡亞洲數據中心展）。MBT將在T10展位展
  - 原文連結：https://tw.stock.yahoo.com/news/%E7%BE%8E%E7%9A%84%E5%B0%87%E5%9C%A8data-center-world-asia-2026%E7%99%BC%E4%BD%88%E8%A1%8C%E6%A5%AD%E9%A6%96%E5%89%B5%E9%9B%BB%E5%8A%9B-235800061.html
- 事件3：AI代理人危險嗎？黃仁勳：並不反對政府監管
  - 來源：Yahoo 台股；發布時間：2026-09-28T23:50:00Z；台北時間：2026-09-29 07:50
  - 摘要：黃仁勳強調，自己絕非反對政府監管，但解決當前威脅的核心關鍵，在於「加速研發安全...
  - 原文連結：https://tw.stock.yahoo.com/news/ai%E4%BB%A3%E7%90%86%E4%BA%BA%E5%8D%B1%E9%9A%AA%E5%97%8E-%E9%BB%83%E4%BB%81%E5%8B%B3-%E4%B8%A6%E4%B8%8D%E5%8F%8D%E5%B0%8D%E6%94%BF%E5%BA%9C%E7%9B%A3%E7%AE%A1-235000316.html
- 事件4：破9千元申購最後衝刺！這「航太重鎮」增資倒數　破400機會趕緊抽
  - 來源：Yahoo 台股；發布時間：2026-09-28T23:50:00Z；台北時間：2026-09-29 07:50
  - 摘要：[FTNN新聞網]記者張書翰／綜合報導航太與精密機械大廠晟田（4541）為充實營運資金、興建廠房、並購置機器設備，近期辦理現金增資發行新股，預計將增資5000萬...
  - 原文連結：https://tw.stock.yahoo.com/news/%E7%A0%B49%E5%8D%83%E5%85%83%E7%94%B3%E8%B3%BC%E6%9C%80%E5%BE%8C%E8%A1%9D%E5%88%BA-%E9%80%99-%E8%88%AA%E5%A4%AA%E9%87%8D%E9%8E%AE-%E5%A2%9E%E8%B3%87%E5%80%92%E6%95%B8-%E7%A0%B4400%E6%A9%9F%E6%9C%83%E8%B6%95%E7%B7%8A%E6%8A%BD-235000751.html
- 事件5：非農業用地仍作農用 這樣做少繳遺產稅560萬
  - 來源：Yahoo 台股；發布時間：2026-09-28T23:30:00Z；台北時間：2026-09-29 07:30
  - 摘要：財政部北區國稅局表示，被繼承人原來所有的「農業用地」，於死亡前經政府依法變更為「非農業用地」，但受限於土地所在地的都市計畫細部計畫尚未完成，或尚未實施市地重劃、區段徵收，導致於被繼承人死亡時仍無法按變更後的用途使用，只要現況仍維持農業使用，
  - 原文連結：https://tw.stock.yahoo.com/news/%E9%9D%9E%E8%BE%B2%E6%A5%AD%E7%94%A8%E5%9C%B0%E4%BB%8D%E4%BD%9C%E8%BE%B2%E7%94%A8-%E9%80%99%E6%A8%A3%E5%81%9A%E5%B0%91%E7%B9%B3%E9%81%BA%E7%94%A2%E7%A8%85560%E8%90%AC-233000657.html
- 事件6：31萬股民注意！00406A、00400A下周除息「這檔年化配息率飆16%」　最後上車日快筆記
  - 來源：Yahoo 台股；發布時間：2026-09-28T23:30:00Z；台北時間：2026-09-29 07:30
  - 摘要：[FTNN新聞網]記者薛明峻／台北報導採月月配的2檔主動式台股ETF主動中信台灣收益（00406A）、主動國泰動能高息（00400A），將於下周先後除息，根據投信日前公...
  - 原文連結：https://tw.stock.yahoo.com/news/31%E8%90%AC%E8%82%A1%E6%B0%91%E6%B3%A8%E6%84%8F-00406a-00400a%E4%B8%8B%E5%91%A8%E9%99%A4%E6%81%AF-%E9%80%99%E6%AA%94%E5%B9%B4%E5%8C%96%E9%85%8D%E6%81%AF%E7%8E%87%E9%A3%8616-%E6%9C%80%E5%BE%8C%E4%B8%8A%E8%BB%8A%E6%97%A5%E5%BF%AB%E7%AD%86%E8%A8%98-233000718.html
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
- 事件11：Feds can't withhold counterterrorism funds from states to force election admin changes, judge rules
  - 來源：CNBC；發布時間：Mon, 28 Sep 2026 21:52:10 GMT；台北時間：2026-09-29 05:52
  - 摘要：The judge said FEMA never explained how the election changes it wanted were "tied to the goal of shoring up vulnerabilities to terrorist attacks."
  - 原文連結：https://www.cnbc.com/2026/09/28/elections-dhs-counterterrorism.html
- 事件12：Treasury Secretary Scott Bessent hires Wall Street economist David Zervos
  - 來源：CNBC；發布時間：Mon, 28 Sep 2026 14:14:45 GMT；台北時間：2026-09-28 22:14
  - 摘要：Zervos is joining the Treasury Department as counselor to Bessent, adding a prominent markets voice to the administration's economic policy team.
  - 原文連結：https://www.cnbc.com/2026/09/28/david-zervos-treasury-department-scott-bessent.html


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
| 資料更新時間 | 2026-09-29 08:08:43 | 本機 |
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
- 資料日期：2026-09-24；資料時間：2026-09-29 08:08:43；時區：`Asia/Taipei`
- 日盤／夜盤標記：日盤收盤後 + 夜盤盤後
- 註記：同 T0 保護：10 格沿用前版有值（本次抓取缺失不覆寫）
- 未取得欄位 (3)：sbl.sale_bal, sbl.sale_chg, options.chain_oi_change
- 註記：無日期端點為最新盤勢快照 (判定資料日期 2026-09-28，非 T0 2026-09-24)，適用：日盤價／法人交易／夜盤／選擇權法人；T0 相符時不另標註
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
- 本報告僅整理資料，不提供交易判斷。

## 六、期現選方向對照

**規則：** 趨勢偏多／空＝現貨、期貨OI、選擇權日淨三者同向；避險／對沖＝現貨與期選反向；日內反轉＝日淨與夜淨反向；缺值標示，不推估。選擇權多空為看多看空口徑。

| 法人 | 現貨買賣超(億) | 期貨OI淨(口) | 期貨日淨 | 期貨夜淨 | 選擇權日淨 | 選擇權夜淨 | 判定 | 期選組合 | 資料來源 |
|---|---|---|---|---|---|---|---|---|---|
| 外資 | -329.6 | -77,031 | -909 | -35 | -732 | -59 | 趨勢偏空 | 對沖避險 | twse-proxy／TAIFEX Proxy |
| 投信 | -128.2 | +72,864 | -695 | +0 | -650 | +0 | 避險／對沖 | 分歧 | twse-proxy／TAIFEX Proxy |
| 自營商 | +13.4 | -1,520 | +1,450 | +389 | -358 | -2,308 | 避險／對沖 | 強避險 | twse-proxy／TAIFEX Proxy |
