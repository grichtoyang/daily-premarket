# DATA_REPORT_20261028

- 報告日期：`2026-10-29`
- T0 交易日期：`2026-10-28`
- 資料產出時間：`2026-10-29 09:30:00`
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
| 加權指數 | 47,035.58 | 點 | twse-proxy |
| 開盤 | 46,402.79 | 點 | FinMind TaiwanStockPrice TAIEX |
| 最高 | 47,060.46 | 點 | FinMind TaiwanStockPrice TAIEX |
| 最低 | 46,402.79 | 點 | FinMind TaiwanStockPrice TAIEX |
| 收盤 | 47,035.58 | 點 | twse-proxy |
| 漲跌點數 | 939.35 | 點 | twse-proxy |
| 漲跌幅 | +2.04 | % | twse-proxy |
| 成交金額 | 7,503.4 | 億元 | twse-proxy market_statistics |

### 2. 市場漲跌家數

#### 2.1 上市公司

**資料來源：** `Cloudflare Worker：twse-proxy` (備援 `TWSE OpenAPI twtazu_od`)

| 項目 | 家數 | 資料來源 |
|---|---|---|
| 上漲家數 | 714 | twse-proxy |
| 下跌家數 | 280 | twse-proxy |
| 平盤家數 | 87 | twse-proxy |
| 漲停家數 | 32 | twse-proxy |
| 跌停家數 | 2 | twse-proxy |

#### 2.2 上櫃公司

**資料來源：** `TPEX OpenAPI tpex_mainborad_highlight`

| 項目 | 家數 | 資料來源 |
|---|---|---|
| 上漲家數 | 590 | TPEX OpenAPI tpex_mainborad_highlight |
| 下跌家數 | 202 | TPEX OpenAPI tpex_mainborad_highlight |
| 平盤家數 | 80 | TPEX OpenAPI tpex_mainborad_highlight |
| 漲停家數 | 31 | TPEX OpenAPI tpex_mainborad_highlight |
| 跌停家數 | 0 | TPEX OpenAPI tpex_mainborad_highlight |

### 3. 三大法人現貨買賣超

**資料來源：** `TWSE RWD BFI82U`

| 法人別 | 買賣超金額 | 單位 | 資料來源 |
|---|---|---|---|
| 外資 | +159.6 | 億元 | twse-proxy /institutional |
| 投信 | +143.2 | 億元 | twse-proxy /institutional |
| 自營商 | +21.7 | 億元 | twse-proxy /institutional |
| 三大法人合計 | +324.4 | 億元 | twse-proxy /institutional |

### 4. 融資融券

**資料來源：** 上市+上櫃 `HiStock` (金額口徑)；維持率 `istock.tw`；備援官方逐股加總

| 項目 | 數值 | 單位 | 資料來源 |
|---|---|---|---|
| 融資餘額 | 8,435.4 | 億元 | HiStock 上市+上櫃融資融券 (金額口徑) |
| 融資增減 | +108.9 | 億元 | HiStock 上市+上櫃融資融券 (金額口徑) |
| 融券餘額 | 232,966 | 張 | HiStock 上市+上櫃融資融券 (金額口徑) |
| 融券增減 | -22,109 | 張 | HiStock 上市+上櫃融資融券 (金額口徑) |
| 融資維持率 | 183.30 | % | stockintelli 大盤融資維持率 (民間估算；官方無每日序列) |

### 5. 借券資料

**資料來源：** 上市 `TWSE OpenAPI TWT96U` (可借餘額)、上櫃 `TPEX OpenAPI tpex_margin_sbl`

| 項目 | 數值 | 單位 | 資料來源 |
|---|---|---|---|
| 借券餘額 | 4,590,969 | 張 | TWSE TWT93U + TPEX margin_sbl |
| 借券賣出餘額 | 39,926 | 張 | TWSE TWT93U + TPEX margin_sbl |
| 借券賣出增減 | 2,559 | 張 | TWSE TWT93U + TPEX margin_sbl |

### 6. 市場成交結構

**資料來源：** 上市 `twse-proxy market_statistics`、上櫃 `TPEX OpenAPI tpex_mainborad_highlight`

| 項目 | 成交金額 | 單位 | 資料來源 |
|---|---|---|---|
| 上市成交金額 | 7,503.4 | 億元 | twse-proxy market_statistics |
| 上櫃成交金額 | 1,633.5 | 億元 | TPEX OpenAPI tpex_mainborad_highlight |
| 上市櫃成交金額合計 | 9,136.9 | 億元 | twse-proxy market_statistics+TPEX OpenAPI tpex_mainborad_highlight |

## 二、重要市場

### 1. 美股指數

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 收盤／最新值 | 漲跌點 | 漲跌幅 | 資料來源 |
|---|---|---|---|---|---|
| S&P 500 | ^GSPC | 7,743.98 | 21.38 | +0.28 | Yahoo Finance Chart API |
| Nasdaq Composite | ^IXIC | 26,549.85 | 72.04 | +0.27 | Yahoo Finance Chart API |
| Nasdaq 100 | ^NDX | 29,813.16 | 161.72 | +0.55 | Yahoo Finance Chart API |
| Dow Jones | ^DJI | 52,475.10 | 97.53 | +0.19 | Yahoo Finance Chart API |
| 費城半導體 SOX | ^SOX | 11,684.00 | 201.50 | +1.75 | Yahoo Finance Chart API |
| VIX | ^VIX | 16.91 | -0.61 | -3.48 | Yahoo Finance Chart API |

### 2. 亞洲主要指數

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 收盤／最新值 | 漲跌點 | 漲跌幅 | 資料來源 |
|---|---|---|---|---|---|
| 日經225 | ^N225 | 64,644.02 | 1,375.65 | +2.17 | Yahoo Finance Chart API |
| 韓國KOSPI | ^KS11 | 5,953.74 | 315.40 | +5.59 | Yahoo Finance Chart API |
| 香港恆生 | ^HSI | 23,041.32 | -170.49 | -0.73 | Yahoo Finance Chart API |
| 上海綜合 | 000001.SS | 3,648.30 | -49.22 | -1.33 | Yahoo Finance Chart API |
| 深圳成分 | 399001.SZ | 11,245.73 | -288.65 | -2.50 | Yahoo Finance Chart API |

### 3. 美股指數期貨

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 最新值 | 漲跌點 | 漲跌幅 | 資料來源 |
|---|---|---|---|---|---|
| S&P500期貨 | ES=F | 7,764.00 | 5.75 | +0.07 | Yahoo Finance Chart API |
| Nasdaq100期貨 | NQ=F | 29,691.00 | -121.00 | -0.41 | Yahoo Finance Chart API |
| 道瓊期貨 | YM=F | 52,831.00 | 252.00 | +0.48 | Yahoo Finance Chart API |
| Russell2000期貨 | RTY=F | 2,858.80 | 30.30 | +1.07 | Yahoo Finance Chart API |

### 4. 美國國債殖利率

**資料來源：** `U.S. Treasury Fiscal Data API` (失敗時備援 Treasury yield.xml 與 `Yahoo Finance`)

| 項目 | API 資料欄位／識別 | 殖利率 | 日變化 | 資料來源 |
|---|---|---|---|---|
| 美國 2 年期殖利率 | 2 Yr | 4.67 | -0.03 | U.S. Treasury yield.xml (網頁備援) |
| 美國 10 年期殖利率 | 10 Yr | 5.05 | 0.05 | Yahoo Finance (備援) |
| 美國 30 年期殖利率 | 30 Yr | 5.36 | 0.06 | Yahoo Finance (備援) |

### 5. 主要匯率

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 最新值 | 漲跌點 | 漲跌幅 | 資料來源 |
|---|---|---|---|---|---|
| USD/TWD | TWD=X | 32.40 | -0.03 | -0.09 | Yahoo Finance Chart API |
| DXY美元指數 | DX-Y.NYB | 102.16 | -0.16 | -0.16 | Yahoo Finance Chart API |
| USD/JPY | JPY=X | 157.80 | -0.19 | -0.12 | Yahoo Finance Chart API |
| USD/KRW | KRW=X | 1,332.18 | 5.37 | +0.40 | Yahoo Finance Chart API |

### 6. 台灣相關ADR

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 收盤／最新值 | 漲跌點 | 漲跌幅 | 資料來源 |
|---|---|---|---|---|---|
| 台積電ADR | TSM | 436.87 | 12.50 | +2.95 | Yahoo Finance Chart API |
| 聯電ADR | UMC | 19.45 | 0.27 | +1.41 | Yahoo Finance Chart API |
| 日月光ADR | ASX | 42.06 | 2.15 | +5.39 | Yahoo Finance Chart API |

### 7. 原油黃金Bitcoin

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 收盤／最新值 | 漲跌點 | 漲跌幅 | 資料來源 |
|---|---|---|---|---|---|
| WTI原油期貨 | CL=F | 101.92 | 2.02 | +2.02 | Yahoo Finance Chart API |
| 黃金期貨 | GC=F | 4,071.80 | -2.80 | -0.07 | Yahoo Finance Chart API |
| Bitcoin | BTC-USD | 80,783.24 | -21.84 | -0.03 | Yahoo Finance Chart API |

### 8. 重大經濟數據、央行事件與重大市場新聞

**資料來源：** 台股 `tw.stock.yahoo.com` (含內文摘要)；國際 `Fed 公告 RSS`＋`CNBC`＋`MarketWatch` (標題、來源、時間與連結)

- 事件1：台光電、台燿上季賺出新高 聯亞盈餘暴漲528%
  - 來源：Yahoo 台股；發布時間：2026-10-28T21:30:00Z；台北時間：2026-10-29 05:30
  - 摘要：年增率2倍起跳多家重量級電子廠昨同步公告第3季財報，包括全球銅箔基板（CCL）龍頭台光電（2383）、銅箔基板二哥台燿（6274）及光通訊股王聯亞（3081）財報皆傳出佳音，同步創下單季新高。台光電第3季毛利率37.7%，季增3.8個百分點
  - 原文連結：https://tw.stock.yahoo.com/news/%E5%8F%B0%E5%85%89%E9%9B%BB-%E5%8F%B0%E7%87%BF-%E8%81%AF%E4%BA%9E%E5%A0%B1%E5%96%9C-q3%E8%B2%A1%E5%A0%B1%E5%90%8C%E5%89%B5%E5%96%AE%E5%AD%A3%E6%96%B0%E9%AB%98-213000047.html
- 事件2：新台幣急貶 美元高利定存提前解約潮「棄息賺匯差」
  - 來源：Yahoo 台股；發布時間：2026-10-28T22:40:18Z；台北時間：2026-10-29 06:40
  - 摘要：新台幣急貶，意外出現美元高利定存戶提前解約的現象。銀行業者表示，近期部分美元存戶不再等待定存到期，而是選擇提前解約，將美元換回新台幣，先行實現匯差收益。尤其近期台股回檔，部分投資人考慮將資金轉進股市，形成「棄息賺匯差、換匯低接股票」。
  - 原文連結：https://tw.stock.yahoo.com/news/%E7%BE%8E%E5%85%83%E9%AB%98%E5%88%A9%E5%AE%9A%E5%AD%98-%E5%87%BA%E7%8F%BE%E6%8F%90%E5%89%8D%E8%A7%A3%E7%B4%84%E6%BD%AE-224018134.html
- 事件3：00878本季配息尚未揭曉 股民熱議：挑戰1.2元
  - 來源：Yahoo 台股；發布時間：2026-10-28T14:15:00Z；台北時間：2026-10-28 22:15
  - 摘要：[FTNN新聞網]實習記者陳又綺／綜合報導國泰永續高股息（00878）即將迎來2026年最後一次配息，市場關注第4季配息金額是否有望延續上季水準，甚至進一步調高。...
  - 原文連結：https://tw.stock.yahoo.com/news/00878%E5%B9%B4%E7%AC%AC4%E5%AD%A3%E9%85%8D%E6%81%AF%E5%80%92%E6%95%B8-11-17%E9%99%A4%E6%81%AF-12-11%E9%A0%98%E9%8C%A2-141500898.html
- 事件4：產能近滿載 聯電明年晶圓估漲價一成
  - 來源：Yahoo 台股；發布時間：2026-10-28T23:01:00Z；台北時間：2026-10-29 07:01
  - 摘要：晶圓代工大廠聯電產能逼近滿載，明年準備靠漲價拚成長！聯電執行長王石透露，隨著部分製程供不應求，2027年整體晶圓平均售價（ASP）預估年增約10%。過去靠增加出貨量衝營收的策略，將轉向提高每片晶圓的價值。 聯電這次敢喊漲，關鍵在部分製程產能
  - 原文連結：https://tw.stock.yahoo.com/news/%E8%81%AF%E9%9B%BB%E5%8D%83%E5%84%84%E7%9B%A4%E7%AE%971-%E7%94%A2%E8%83%BD%E5%90%83%E7%B7%8A%E6%94%B9%E6%89%93%E5%83%B9%E6%A0%BC%E7%89%8C-%E6%98%8E%E5%B9%B4%E6%99%B6%E5%9C%93%E5%9D%87%E5%83%B9%E5%96%8A%E6%BC%B21%E6%88%90-230100252.html
- 事件5：冠西電90天暴漲559%、東台成交量增13倍 全列注意股
  - 來源：Yahoo 台股；發布時間：2026-10-29T00:20:00Z；台北時間：2026-10-29 08:20
  - 摘要：[FTNN新聞網]記者莊蕙如／綜合報導證交所公布10月28日共20檔注意股，南亞（1303）、玉晶光（3406）、大量（3167）、聯茂（6213）等熱門股全數入列。其中冠西...
  - 原文連結：https://tw.stock.yahoo.com/news/%E6%9C%80%E7%8B%82%E4%B8%8D%E6%98%AF%E5%8D%97%E4%BA%9E-%E9%80%99%E6%AA%94-90%E5%A4%A9%E6%9A%B4%E6%BC%B2559-%E7%8E%89%E6%99%B6%E5%85%8960%E5%A4%A9%E9%A3%86197-20%E6%AA%94%E6%B3%A8%E6%84%8F%E8%82%A1-002000880.html
- 事件6：美四大指數全收漲 甲骨文飆逾10%
  - 來源：Yahoo 台股；發布時間：2026-10-28T21:14:39Z；台北時間：2026-10-29 05:14
  - 摘要：美股三大指數連三日收高，Fed按兵不動、利率維持3.75%至4%，未明示12月是否再升息。 甲骨文飆10.73%，上修2030營收至2250億美元；SK海力士強勁展望，記憶體族群走揚。 微軟盤後靠雲端銷售上揚、Alphabet走低；市場聚焦
  - 原文連結：https://tw.stock.yahoo.com/news/%E7%BE%8E%E8%82%A1%E7%9B%A4%E5%BE%8C-fed%E6%8C%89%E5%85%B5%E4%B8%8D%E5%8B%95-%E4%B8%89%E5%A4%A7%E6%8C%87%E6%95%B8%E9%80%A3%E4%B8%89%E7%B4%85-sk%E6%B5%B7%E5%8A%9B%E5%A3%ABadr-%E7%94%B2%E9%AA%A8%E6%96%87%E7%8B%82%E9%A3%86%E8%B6%8510-211439991.html
- 事件7：Federal Reserve issues FOMC statement
  - 來源：Federal Reserve；發布時間：Wed, 28 Oct 2026 18:00:00 GMT；台北時間：2026-10-29 02:00
  - 摘要：Federal Reserve issues FOMC statement
  - 原文連結：https://www.federalreserve.gov/newsevents/pressreleases/monetary20261028a.htm
- 事件8：Here are five key takeaways from the Fed rate decision and Warsh news conference
  - 來源：CNBC；發布時間：Wed, 28 Oct 2026 21:31:46 GMT；台北時間：2026-10-29 05:31
  - 摘要：Even though the interest-rate vote went as expected, there were a few surprises out of this week's Federal Open Market Committee meeting.
  - 原文連結：https://www.cnbc.com/2026/10/28/fed-rate-decision-warsh-takeaways.html
- 事件9：Bond investor Jeff Gundlach on Fed's rate pause: 'What are you waiting for?'
  - 來源：CNBC；發布時間：Wed, 28 Oct 2026 19:53:50 GMT；台北時間：2026-10-29 03:53
  - 摘要：The DoubleLine founder spoke with CNBC's "Closing Bell" on Wednesday after the Fed held interest rates steady.
  - 原文連結：https://www.cnbc.com/2026/10/28/bond-investor-jeff-gundlach-talks-feds-rate-pause-with-cnbc.html
- 事件10：10-year Treasury yield creeps higher even as Fed keeps rates the same
  - 來源：CNBC；發布時間：Wed, 28 Oct 2026 20:17:19 GMT；台北時間：2026-10-29 04:17
  - 摘要：Treasury yields edged higher as traders await the Federal Reserve's latest monetary policy decision.
  - 原文連結：https://www.cnbc.com/2026/10/28/us-treasurys-bonds-yields-federal-reserve.html
- 事件11：Bessent says 'not necessarily' a mistake if the Fed hikes again
  - 來源：CNBC；發布時間：Wed, 28 Oct 2026 21:06:37 GMT；台北時間：2026-10-29 05:06
  - 摘要：Treasury Secretary Scott Bessent joined CNBC for an interview on Oct. 28, 2026.
  - 原文連結：https://www.cnbc.com/2026/10/28/scott-bessent-interview.html
- 事件12：Samsung Electronics third-quarter profit in line with estimates amid rising demand for AI memory chips
  - 來源：CNBC；發布時間：Thu, 29 Oct 2026 01:13:47 GMT；台北時間：2026-10-29 09:13
  - 摘要：Samsung Electronics reported third-quarter earnings on Thursday.
  - 原文連結：https://www.cnbc.com/2026/10/29/samsung-electronics-third-quarter-earnings.html


## 三、期貨

**資料來源：**
1. Cloudflare Workers：TAIFEX Proxy — https://taifex.grichtoyang.workers.dev/
2. TAIFEX Open API — https://openapi.taifex.com.tw/

近月契約月份：202611 (日盤成交量最大者)；交易日期：2026-10-28

### 1．台指期近月日盤行情

| 項目 | 數值 | 資料來源 |
|---|---|---|
| 開盤價 | 46,971 | TAIFEX Proxy |
| 最高價 | 47,272 | TAIFEX Proxy |
| 最低價 | 46,892 | TAIFEX Proxy |
| 收盤價 | 47,244 | TAIFEX Proxy |
| 漲跌點數 | +1,138 | TAIFEX Proxy |
| 漲跌幅 | +2.47 | TAIFEX Proxy |
| 成交量 | 43,867 | TAIFEX Proxy |
| 日盤高點及低點 | 47,272 / 46,892 | TAIFEX Proxy |

### 2．台指期近月夜盤行情

| 項目 | 數值 | 資料來源 |
|---|---|---|
| 開盤價 | 47,280 | TAIFEX Proxy |
| 最高價 | 47,607 | TAIFEX Proxy |
| 最低價 | 46,968 | TAIFEX Proxy |
| 收盤價 | 47,121 | TAIFEX Proxy |
| 漲跌點數 | -128 | TAIFEX Proxy |
| 漲跌幅 | -0.27 | TAIFEX Proxy |
| 成交量 | 31,298 | TAIFEX Proxy |
| 夜盤高點及低點 | 47,607 / 46,968 | TAIFEX Proxy |
| 結算價 | unavailable | TAIFEX Proxy |
| 未平倉量 | unavailable | TAIFEX Proxy |

### 3．法人台指期多空未平倉部位

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 外資多方 OI | 10,510 | TAIFEX Proxy |
| 外資空方 OI | 95,427 | TAIFEX Proxy |
| 外資多空淨 OI | -84,917 | TAIFEX Proxy |
| 投信多方 OI | 89,821 | TAIFEX Proxy |
| 投信空方 OI | 2,642 | TAIFEX Proxy |
| 投信多空淨 OI | +87,179 | TAIFEX Proxy |
| 自營商多方 OI | 4,719 | TAIFEX Proxy |
| 自營商空方 OI | 4,236 | TAIFEX Proxy |
| 自營商多空淨 OI | +483 | TAIFEX Proxy |
| 三大法人合計多方 OI | 105,050 | TAIFEX Proxy |
| 三大法人合計空方 OI | 102,305 | TAIFEX Proxy |
| 三大法人合計多空淨 OI | +2,745 | TAIFEX Proxy |
| 外資多空淨 OI 變化 | +1,126 | TAIFEX Proxy |
| 投信多空淨 OI 變化 | +2,127 | TAIFEX Proxy |
| 自營商多空淨 OI 變化 | -971 | TAIFEX Proxy |

### 4．前十大交易人多空未平倉部位

**資料來源：** `TAIFEX OpenAPI OpenInterestOfLargeTradersFutures` (官方資料落後約一日，標示實際日期)

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 前十大交易人多方 OI | 94,315 | TAIFEX Proxy |
| 前十大交易人空方 OI | 79,412 | TAIFEX Proxy |
| 前十大交易人多空淨 OI | +14,903 | TAIFEX Proxy |
| 多空淨 OI 變化 (2026-10-22→2026-10-28) | +5,879 | TAIFEX Proxy snapshots (2026-10-27) |
- 資料日期：2026-10-28 (TypeOfTraders=0 全部交易人；契約月份 202611)

### 5．日盤、夜盤法人交易資料

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 外資日盤多單交易量 | 40,386 | TAIFEX Proxy |
| 外資日盤空單交易量 | 39,336 | TAIFEX Proxy |
| 外資日盤多空淨交易量 | +1,050 | TAIFEX Proxy |
| 外資夜盤多單交易量 | 17,164 | TAIFEX Proxy |
| 外資夜盤空單交易量 | 18,253 | TAIFEX Proxy |
| 外資夜盤多空淨交易量 | -1,089 | TAIFEX Proxy |
| 外資日盤／夜盤交易量變化 | +2,139 | TAIFEX Proxy |
| 投信日盤多空淨交易量 | +2,127 | TAIFEX Proxy |
| 投信夜盤多空淨交易量 | +0 | TAIFEX Proxy |
| 投信日盤／夜盤交易量變化 | +2,127 | TAIFEX Proxy |
| 自營商日盤多空淨交易量 | -964 | TAIFEX Proxy |
| 自營商夜盤多空淨交易量 | +68 | TAIFEX Proxy |
| 自營商日盤／夜盤交易量變化 | -1,032 | TAIFEX Proxy |
| 三大法人日盤多空淨交易量 | +2,213 | TAIFEX Proxy |
| 三大法人夜盤多空淨交易量 | -1,021 | TAIFEX Proxy |
| 法人日盤交易金額淨額 (億元) | +207.6 | TAIFEX Proxy |
| 法人夜盤交易金額淨額 (億元) | -96.4 | TAIFEX Proxy |

### 6．期貨與現貨關係

| 項目 | 數值 | 資料來源 |
|---|---|---|
| 台指期近月價格 | 47,244 | TAIFEX Proxy |
| 加權指數價格 | 47,035.58 | twse-proxy |
| 台指期與加權指數價差 | +208.42 | TAIFEX Proxy+twse-proxy |
| 價差百分比 | +0.44 | TAIFEX Proxy+twse-proxy |
| 日盤基差 | +208.42 | TAIFEX Proxy+twse-proxy |
| 夜盤價格相對日盤收盤的變化 | -123 | TAIFEX Proxy |

### 7．日盤、夜盤與籌碼變化對照

#### 7.1 日夜盤價格與成交量對照 (變化 = 日盤 - 夜盤)

| 項目 | 日盤 | 夜盤 | 變化 (日-夜) | 資料來源 |
|---|---|---|---|---|
| 收盤價 | 47,244 | 47,121 | +123 | TAIFEX Proxy |
| 成交量 | 43,867 | 31,298 | +12,569 | TAIFEX Proxy |
- 台指期總 OI 前日變化：+2,282（來源：TAIFEX Proxy）


#### 7.2 法人籌碼日夜盤對照 (淨變化 = 日盤淨 - 夜盤淨；OI 為日盤收盤後總量，前日變化另列)

| 法人 | 交易量 |  |  |  |  |  |  | 未平倉量 |  |  |  | 資料來源 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|  | **日盤多單** | **日盤空單** | **日盤淨** | **夜盤多單** | **夜盤空單** | **夜盤淨** | **淨變化 (日-夜)** | **OI多方** | **OI空方** | **OI淨** | **OI前日變化** |  |
| 外資 | 40,386 | 39,336 | +1,050 | 17,164 | 18,253 | -1,089 | +2,139 | 10,510 | 95,427 | -84,917 | +1,126 | TAIFEX Proxy |
| 投信 | 2,144 | 17 | +2,127 | 0 | 0 | +0 | +2,127 | 89,821 | 2,642 | +87,179 | +2,127 | TAIFEX Proxy |
| 自營商 | 4,002 | 4,966 | -964 | 568 | 500 | +68 | -1,032 | 4,719 | 4,236 | +483 | -971 | TAIFEX Proxy |
| 三大法人合計 | 46,532 | 44,319 | +2,213 | 17,732 | 18,753 | -1,021 | +3,234 | 105,050 | 102,305 | +2,745 | +2,282 | TAIFEX Proxy |

#### 7.3 前十大交易人日夜盤對照 (OI 無日夜拆分，列收盤後總量)

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 前十大交易人多方 OI | 94,315 | TAIFEX Proxy |
| 前十大交易人空方 OI | 79,412 | TAIFEX Proxy |
| 前十大交易人多空淨 OI | +14,903 | TAIFEX Proxy |
| 前十大交易人多空淨 OI 變化 (2026-10-22→2026-10-28) | +5,879 | TAIFEX Proxy snapshots (2026-10-27) |

#### 7.4 夜盤劇本分類 (規則對應：夜盤漲跌 × 外資夜盤偏多空)

| 項目 | 數值 | 資料來源 |
|---|---|---|
| 夜盤成交量占比 (夜盤量／(夜盤量＋日盤量)) | 41.64% | TAIFEX Proxy |
| 夜盤漲跌點數 | -128 | TAIFEX Proxy |
| 外資夜盤多空淨交易量 | -1,089 | TAIFEX Proxy |
| 劇本分類 | 劇本三 | 規則對應 |
| 劇本條件 | 夜盤下跌＋外資偏空 | 規則對應 |
| 劇本特徵 | 開低、續跌機率高 | 規則對應 |

## 四、選擇權

**資料來源：** 主要 TAIFEX 經 Cloudflare Worker Proxy；時區 `Asia/Taipei`

### 1．選擇權交易日期、到期日與資料時間

| 項目 | 數值 | 資料來源 |
|---|---|---|
| 交易日期 | 2026-10-28 | TAIFEX Proxy |
| 到期月份／到期日 | 202610W4 | TAIFEX Proxy |
| 資料更新時間 | 2026-10-29 09:30:00 | 本機 |
| 日盤／夜盤標記 | 日盤收盤後資料 | TAIFEX Proxy |

### 2．Call 總成交量、OI、OI 增減

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Call 總成交量 | 324,138 | TAIFEX Proxy |
| Call 總未平倉量 OI | 57,669 | TAIFEX Proxy |
| Call OI 增減 (2026-10-27→2026-10-28) | +23,751 | TAIFEX Proxy snapshots (2026-10-27) |

### 3．Put 總成交量、OI、OI 增減

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Put 總成交量 | 306,077 | TAIFEX Proxy |
| Put 總未平倉量 OI | 63,005 | TAIFEX Proxy |
| Put OI 增減 (2026-10-27→2026-10-28) | +47,367 | TAIFEX Proxy snapshots (2026-10-27) |

### 4．Call／Put 比例與變化

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Call／Put 成交量比例 | 1.06 | TAIFEX Proxy |
| Call／Put 未平倉量比例 | 0.92 | TAIFEX Proxy |
| Put／Call Ratio | 1.09 | TAIFEX Proxy |
| Call／Put 比例變化 (量比 2026-10-27→2026-10-28) | 2.40 | TAIFEX Proxy |
| 與前一交易日比較 (OI 比 2026-10-27→2026-10-28) | 7.42 | TAIFEX Proxy |
**資料來源：** 比例 `TAIFEX Proxy chain`；變化 `TAIFEX Proxy PutCallRatio`

### 5．外資 Call／Put 部位

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 外資 Call日買 | 110,075 | TAIFEX Proxy |
| 外資 Call日賣 | 108,785 | TAIFEX Proxy |
| 外資 Call日淨 | +1,290 | TAIFEX Proxy |
| 外資 Put日買 | 101,138 | TAIFEX Proxy |
| 外資 Put日賣 | 108,064 | TAIFEX Proxy |
| 外資 Put日淨 | -6,926 | TAIFEX Proxy |
| 外資 Call夜買 | 17,080 | TAIFEX Proxy |
| 外資 Call夜賣 | 17,883 | TAIFEX Proxy |
| 外資 Call夜淨 | -803 | TAIFEX Proxy |
| 外資 Put夜買 | 20,800 | TAIFEX Proxy |
| 外資 Put夜賣 | 20,402 | TAIFEX Proxy |
| 外資 Put夜淨 | +398 | TAIFEX Proxy |
| 外資 日盤淨總量 | +8,216 | TAIFEX Proxy |
| 外資 Call日夜淨增減 (日－夜) | +2,093 | TAIFEX Proxy |
| 外資 Put日夜淨增減 (日－夜) | -7,324 | TAIFEX Proxy |

### 6．自營商 Call／Put 部位

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 自營商 Call日買 | 99,143 | TAIFEX Proxy |
| 自營商 Call日賣 | 88,493 | TAIFEX Proxy |
| 自營商 Call日淨 | +10,650 | TAIFEX Proxy |
| 自營商 Put日買 | 86,692 | TAIFEX Proxy |
| 自營商 Put日賣 | 89,683 | TAIFEX Proxy |
| 自營商 Put日淨 | -2,991 | TAIFEX Proxy |
| 自營商 Call夜買 | 11,907 | TAIFEX Proxy |
| 自營商 Call夜賣 | 12,895 | TAIFEX Proxy |
| 自營商 Call夜淨 | -988 | TAIFEX Proxy |
| 自營商 Put夜買 | 14,174 | TAIFEX Proxy |
| 自營商 Put夜賣 | 13,910 | TAIFEX Proxy |
| 自營商 Put夜淨 | +264 | TAIFEX Proxy |
| 自營商 日盤淨總量 | +13,641 | TAIFEX Proxy |
| 自營商 Call日夜淨增減 (日－夜) | +11,638 | TAIFEX Proxy |
| 自營商 Put日夜淨增減 (日－夜) | -3,255 | TAIFEX Proxy |

### 7．主要 Call OI 集中區

| 項目 | 履約價 | OI | 資料來源 |
|---|---|---|---|
| Call OI 第1大履約價 | 47,000 | 6,050 | TAIFEX Proxy |
| Call OI 第2大履約價 | 47,200 | 2,608 | TAIFEX Proxy |
| Call OI 第3大履約價 | 46,950 | 2,484 | TAIFEX Proxy |
| Call OI 最大履約價 | 47,000 | 6,050 | TAIFEX Proxy |

#### Call OI 分布明細 Top10 (機器可讀，到期月份 202610W4)

| # | 履約價 | OI | 佔比 | 資料來源 |
|---|---|---|---|---|
| C1 | 47,000 | 6,050 | 10.49% | TAIFEX Proxy |
| C2 | 47,200 | 2,608 | 4.52% | TAIFEX Proxy |
| C3 | 46,950 | 2,484 | 4.31% | TAIFEX Proxy |
| C4 | 47,100 | 2,446 | 4.24% | TAIFEX Proxy |
| C5 | 46,900 | 2,439 | 4.23% | TAIFEX Proxy |
| C6 | 47,050 | 1,992 | 3.45% | TAIFEX Proxy |
| C7 | 48,600 | 1,971 | 3.42% | TAIFEX Proxy |
| C8 | 48,200 | 1,882 | 3.26% | TAIFEX Proxy |
| C9 | 46,800 | 1,854 | 3.21% | TAIFEX Proxy |
| C10 | 48,500 | 1,563 | 2.71% | TAIFEX Proxy |


### 8．主要 Put OI 集中區

| 項目 | 履約價 | OI | 資料來源 |
|---|---|---|---|
| Put OI 第1大履約價 | 46,700 | 4,447 | TAIFEX Proxy |
| Put OI 第2大履約價 | 46,800 | 4,013 | TAIFEX Proxy |
| Put OI 第3大履約價 | 46,500 | 3,351 | TAIFEX Proxy |
| Put OI 最大履約價 | 46,700 | 4,447 | TAIFEX Proxy |

#### Put OI 分布明細 Top10 (機器可讀，到期月份 202610W4)

| # | 履約價 | OI | 佔比 | 資料來源 |
|---|---|---|---|---|
| P1 | 46,700 | 4,447 | 7.06% | TAIFEX Proxy |
| P2 | 46,800 | 4,013 | 6.37% | TAIFEX Proxy |
| P3 | 46,500 | 3,351 | 5.32% | TAIFEX Proxy |
| P4 | 46,850 | 2,634 | 4.18% | TAIFEX Proxy |
| P5 | 45,000 | 2,552 | 4.05% | TAIFEX Proxy |
| P6 | 46,900 | 2,541 | 4.03% | TAIFEX Proxy |
| P7 | 46,000 | 2,328 | 3.69% | TAIFEX Proxy |
| P8 | 46,750 | 2,242 | 3.56% | TAIFEX Proxy |
| P9 | 46,400 | 2,076 | 3.29% | TAIFEX Proxy |
| P10 | 46,950 | 1,991 | 3.16% | TAIFEX Proxy |


### 9．Call OI 增減集中區

| 項目 | 履約價 (增減口數) | 資料來源 |
|---|---|---|
| Call OI 增加最多的履約價 | 47,000 (+4,506) | TAIFEX Proxy snapshots (2026-10-27) |
| Call OI 減少最多的履約價 | 46,000 (-326) | TAIFEX Proxy snapshots (2026-10-27) |

### 10．Put OI 增減集中區

| 項目 | 履約價 (增減口數) | 資料來源 |
|---|---|---|
| Put OI 增加最多的履約價 | 46,700 (+4,416) | TAIFEX Proxy snapshots (2026-10-27) |
| Put OI 減少最多的履約價 | 41,600 (-161) | TAIFEX Proxy snapshots (2026-10-27) |

### 11．Call Wall

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Call Wall 價位 | 47,000 | TAIFEX Proxy |
| 對應到期月份 | 202610W4 | TAIFEX Proxy |
| 與前一交易日的變化 (2026-10-27→2026-10-28) | -1,600 | TAIFEX Proxy snapshots (2026-10-27) |

### 12．Put Wall

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Put Wall 價位 | 46,700 | TAIFEX Proxy |
| 對應到期月份 | 202610W4 | TAIFEX Proxy |
| 與前一交易日的變化 (2026-10-27→2026-10-28) | +1,700 | TAIFEX Proxy snapshots (2026-10-27) |

### 13．Gamma Wall

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Gamma Wall 價位 | 47,500.00 | TAIFEX Proxy (options-market-structure-compact (proxy)) |
| 對應到期月份 | 202610W4 | TAIFEX Proxy |
| 資料日期 | 2026-10-28 | TAIFEX Proxy (options-market-structure-compact (proxy)) |

### 14．Gamma Flip

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Gamma Flip 價位 | 46,571.29 | TAIFEX Proxy (options-market-structure-compact (proxy)) |
| 對應到期月份 | 202610W4 | TAIFEX Proxy |
| 資料日期 | 2026-10-28 | TAIFEX Proxy (options-market-structure-compact (proxy)) |

### 15．Max Pain

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Max Pain 價位 | 46,750 | TAIFEX Proxy |
| 對應到期月份 | 202610W4 | TAIFEX Proxy |
| 與前一交易日的變化 (2026-10-27→2026-10-28) | +1,350 | TAIFEX Proxy snapshots (2026-10-27) |

### 17．選擇權法人日盤、夜盤交易

| 法人 | 日盤多單 | 日盤空單 | 日盤淨 | 夜盤多單 | 夜盤空單 | 夜盤淨 | 淨變化 (日-夜) | 資料來源 |
|---|---|---|---|---|---|---|---|---|
| 外資 | 218,139 | 209,923 | +8,216 | 37,482 | 38,683 | -1,201 | +9,417 | TAIFEX Proxy |
| 投信 | 0 | 12,786 | -12,786 | 0 | 0 | +0 | -12,786 | TAIFEX Proxy |
| 自營商 | 188,826 | 175,185 | +13,641 | 25,817 | 27,069 | -1,252 | +14,893 | TAIFEX Proxy |
| 三大法人合計 | 406,965 | 397,894 | +9,071 | 63,299 | 65,752 | -2,453 | +11,524 | TAIFEX Proxy |
- 方法論：多方＝買Call＋賣Put（看多），空方＝賣Call＋買Put（看空），淨額＝看多－看空（已用 Call／Put 拆分頁交叉驗算一致）
- 公式：多方(買)－空方(賣)＝（買call＋賣put）－（賣call＋買put）＝看多－看空
- 速記：多＝BC＋SP、空＝SC＋BP

#### 法人多空力道表（金額・億元；上游千元／1e5）

| 法人 | 日多方力道 | 日空方力道 | 日淨多空力道 | 夜多方力道 | 夜空方力道 | 夜淨多空力道 | 日淨－夜淨 | 資料來源 |
|---|---|---|---|---|---|---|---|---|
| 外資 | 11.44 | 10.31 | +1.13 | 3.39 | 3.67 | -0.28 | +1.41 | TAIFEX Proxy |
| 投信 | 0.00 | 7.69 | -7.69 | 0.00 | 0.00 | +0 | -7.69 | TAIFEX Proxy |
| 自營商 | 17.29 | 10.29 | +7.00 | 2.22 | 2.33 | -0.11 | +7.11 | TAIFEX Proxy |
| 三大法人合計 | 28.73 | 28.29 | +0.44 | 5.61 | 6.00 | -0.39 | +0.83 | TAIFEX Proxy |

### 18．選擇權前十大

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 買權多方 OI | 8,231 | TAIFEX Proxy |
| 買權空方 OI | 9,363 | TAIFEX Proxy |
| 買權多空淨 OI | -1,132 | TAIFEX Proxy |
| 買權多空淨 OI 變化 (2026-10-22→2026-10-28) | +542 | TAIFEX Proxy snapshots (2026-10-27) |

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 賣權多方 OI | 7,999 | TAIFEX Proxy |
| 賣權空方 OI | 10,051 | TAIFEX Proxy |
| 賣權多空淨 OI | -2,052 | TAIFEX Proxy |
| 賣權多空淨 OI 變化 (2026-10-22→2026-10-28) | -417 | TAIFEX Proxy snapshots (2026-10-27) |
- 資料日期：買權 2026-10-28／賣權 2026-10-28 (TypeOfTraders=0 全部交易人；契約月份 202611)

#### 大戶流向（全日；前十大無日夜拆分）

| 項目 | 淨變化 | 區間 | 資料來源 |
|---|---|---|---|
| 期貨前十大 | +5,879 | 2026-10-22→2026-10-28 | TAIFEX Proxy snapshots (2026-10-27) |
| 買權前十大 | +542 | 2026-10-22→2026-10-28 | TAIFEX Proxy snapshots (2026-10-27) |
| 賣權前十大 | -417 | 2026-10-22→2026-10-28 | TAIFEX Proxy snapshots (2026-10-27) |

### 16．資料來源、時間、時區與狀態

- 資料來源：TAIFEX 經 Cloudflare Worker Proxy
- 資料日期：2026-10-28；資料時間：2026-10-29 09:30:00；時區：`Asia/Taipei`
- 日盤／夜盤標記：日盤收盤後 + 夜盤盤後
- 未取得欄位 (0)：無
- 註記：futures-price-after-hours 日期 2026-10-28 非今日 2026-10-29，視為無新節次，不採用
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
| 外資 | +159.6 | -84,917 | +1,050 | -1,089 | +8,216 | -1,201 | 避險／對沖 | 強避險 | twse-proxy／TAIFEX Proxy |
| 投信 | +143.2 | +87,179 | +2,127 | +0 | -12,786 | +0 | 避險／對沖 | 分歧 | twse-proxy／TAIFEX Proxy |
| 自營商 | +21.7 | +483 | -964 | +68 | +13,641 | -1,252 | 趨勢偏多 | 趨勢偏多 | twse-proxy／TAIFEX Proxy |
