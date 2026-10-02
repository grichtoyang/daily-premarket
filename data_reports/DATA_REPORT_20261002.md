# DATA_REPORT_20261002

- 報告日期：`2026-10-02`
- T0 交易日期：`2026-10-02`
- 資料產出時間：`2026-10-02 19:15:14`
- 時區：`Asia/Taipei`

---

## 一、現貨

### 1. 台股大盤行情

**資料來源：** `Cloudflare Worker：twse-proxy` (備援 `TWSE OpenAPI MI_INDEX`)

| 項目 | 數值 | 單位 | 資料來源 |
|---|---|---|---|
| 加權指數 | 48,475.74 | 點 | twse-proxy |
| 開盤 | 48,390.65 | 點 | FinMind TaiwanStockPrice TAIEX |
| 最高 | 48,491.62 | 點 | FinMind TaiwanStockPrice TAIEX |
| 最低 | 48,205.81 | 點 | FinMind TaiwanStockPrice TAIEX |
| 收盤 | 48,475.74 | 點 | twse-proxy |
| 漲跌點數 | 122.25 | 點 | twse-proxy |
| 漲跌幅 | +0.25 | % | twse-proxy |
| 成交金額 | 9,382.2 | 億元 | twse-proxy market_statistics |

### 2. 市場漲跌家數

#### 2.1 上市公司

**資料來源：** `Cloudflare Worker：twse-proxy` (備援 `TWSE OpenAPI twtazu_od`)

| 項目 | 家數 | 資料來源 |
|---|---|---|
| 上漲家數 | 483 | twse-proxy |
| 下跌家數 | 506 | twse-proxy |
| 平盤家數 | 91 | twse-proxy |
| 漲停家數 | 24 | twse-proxy |
| 跌停家數 | 1 | twse-proxy |

#### 2.2 上櫃公司

**資料來源：** `TPEX OpenAPI tpex_mainborad_highlight`

| 項目 | 家數 | 資料來源 |
|---|---|---|
| 上漲家數 | 452 | TPEX OpenAPI tpex_mainborad_highlight |
| 下跌家數 | 331 | TPEX OpenAPI tpex_mainborad_highlight |
| 平盤家數 | 85 | TPEX OpenAPI tpex_mainborad_highlight |
| 漲停家數 | 31 | TPEX OpenAPI tpex_mainborad_highlight |
| 跌停家數 | 4 | TPEX OpenAPI tpex_mainborad_highlight |

### 3. 三大法人現貨買賣超

**資料來源：** `TWSE RWD BFI82U`

| 法人別 | 買賣超金額 | 單位 | 資料來源 |
|---|---|---|---|
| 外資 | +26.2 | 億元 | twse-proxy /institutional |
| 投信 | +49.1 | 億元 | twse-proxy /institutional |
| 自營商 | +20.3 | 億元 | twse-proxy /institutional |
| 三大法人合計 | +95.6 | 億元 | twse-proxy /institutional |

### 4. 融資融券

**資料來源：** 上市+上櫃 `HiStock` (金額口徑)；維持率 `istock.tw`；備援官方逐股加總

| 項目 | 數值 | 單位 | 資料來源 |
|---|---|---|---|
| 融資餘額 | unavailable | 億元 | HiStock |
| 融資增減 | unavailable | 億元 | HiStock |
| 融券餘額 | 233,322 | 張 | HiStock |
| 融券增減 | -1,492 | 張 | HiStock |
| 融資維持率 | 195.13 | % | 前值遞補 (DATA 2026-10-01；當日三源皆失敗；民間估算；官方無每日序列) |

### 5. 借券資料

**資料來源：** 上市 `TWSE OpenAPI TWT96U` (可借餘額)、上櫃 `TPEX OpenAPI tpex_margin_sbl`

| 項目 | 數值 | 單位 | 資料來源 |
|---|---|---|---|
| 借券餘額 | 2,391,138 | 張 | TWSE TWT93U + TPEX margin_sbl |
| 借券賣出餘額 | unavailable | 張 | TWSE TWT93U + TPEX margin_sbl |
| 借券賣出增減 | unavailable | 張 | TWSE TWT93U + TPEX margin_sbl |

### 6. 市場成交結構

**資料來源：** 上市 `twse-proxy market_statistics`、上櫃 `TPEX OpenAPI tpex_mainborad_highlight`

| 項目 | 成交金額 | 單位 | 資料來源 |
|---|---|---|---|
| 上市成交金額 | 9,382.2 | 億元 | twse-proxy market_statistics |
| 上櫃成交金額 | 2,731.9 | 億元 | TPEX OpenAPI tpex_mainborad_highlight |
| 上市櫃成交金額合計 | 12,114.1 | 億元 | twse-proxy market_statistics+TPEX OpenAPI tpex_mainborad_highlight |

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
| VIX | ^VIX | 15.95 | -0.44 | -2.68 | Yahoo Finance Chart API |

### 2. 亞洲主要指數

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 收盤／最新值 | 漲跌點 | 漲跌幅 | 資料來源 |
|---|---|---|---|---|---|
| 日經225 | ^N225 | 68,309.46 | -647.26 | -0.94 | Yahoo Finance Chart API |
| 韓國KOSPI | ^KS11 | 7,003.74 | 32.39 | +0.46 | Yahoo Finance Chart API |
| 香港恆生 | ^HSI | 23,972.29 | -640.98 | -2.60 | Yahoo Finance Chart API |
| 上海綜合 | 000001.SS | 3,842.20 | 11.74 | +0.31 | Yahoo Finance Chart API |
| 深圳成分 | 399001.SZ | 12,887.62 | -14.33 | -0.11 | Yahoo Finance Chart API |

### 3. 美股指數期貨

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 最新值 | 漲跌點 | 漲跌幅 | 資料來源 |
|---|---|---|---|---|---|
| S&P500期貨 | ES=F | 7,763.25 | 39.25 | +0.51 | Yahoo Finance Chart API |
| Nasdaq100期貨 | NQ=F | 30,988.50 | 228.00 | +0.74 | Yahoo Finance Chart API |
| 道瓊期貨 | YM=F | 51,547.00 | 306.00 | +0.60 | Yahoo Finance Chart API |
| Russell2000期貨 | RTY=F | 2,845.30 | 18.40 | +0.65 | Yahoo Finance Chart API |

### 4. 美國國債殖利率

**資料來源：** `U.S. Treasury Fiscal Data API` (失敗時備援 Treasury yield.xml 與 `Yahoo Finance`)

| 項目 | API 資料欄位／識別 | 殖利率 | 日變化 | 資料來源 |
|---|---|---|---|---|
| 美國 2 年期殖利率 | 2 Yr | 4.78 | 0.00 | U.S. Treasury yield.xml (網頁備援) |
| 美國 10 年期殖利率 | 10 Yr | 5.24 | -0.06 | Yahoo Finance (備援) |
| 美國 30 年期殖利率 | 30 Yr | 5.60 | -0.03 | Yahoo Finance (備援) |

### 5. 主要匯率

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 最新值 | 漲跌點 | 漲跌幅 | 資料來源 |
|---|---|---|---|---|---|
| USD/TWD | TWD=X | 31.87 | 0.01 | +0.02 | Yahoo Finance Chart API |
| DXY美元指數 | DX-Y.NYB | 102.08 | -0.02 | -0.02 | Yahoo Finance Chart API |
| USD/JPY | JPY=X | 157.73 | 0.17 | +0.11 | Yahoo Finance Chart API |
| USD/KRW | KRW=X | 1,348.25 | -8.59 | -0.63 | Yahoo Finance Chart API |

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
| WTI原油期貨 | CL=F | 89.25 | -3.62 | -3.90 | Yahoo Finance Chart API |
| 黃金期貨 | GC=F | 4,214.80 | 12.50 | +0.30 | Yahoo Finance Chart API |
| Bitcoin | BTC-USD | 86,462.77 | 1,609.67 | +1.90 | Yahoo Finance Chart API |

### 8. 重大經濟數據、央行事件與重大市場新聞

**資料來源：** 台股 `tw.stock.yahoo.com` (含內文摘要)；國際 `Fed 公告 RSS`＋`CNBC`＋`MarketWatch` (標題、來源、時間與連結)

- 事件1：台積休兵誰扛新高？臻鼎亮燈 ABF揪矽晶圓開派對
  - 來源：Yahoo 台股；發布時間：2026-10-02T08:59:45Z；台北時間：2026-10-02 16:59
  - 摘要：中小型股接棒點火，台股漲122點再創收盤新高！今(2)日加權指數終場上漲122.25點或0.25%，收48,475.74點，本周累計上漲451.14點，周線連三紅，成交金額8,997.10億元。櫃買指數大漲1.94%，電子指數上漲0.22%
  - 原文連結：https://tw.stock.yahoo.com/news/%E6%AC%8A%E5%80%BC%E7%86%84%E7%81%AB%E5%8F%B0%E8%82%A1%E7%BA%8C%E5%89%B5%E9%AB%98%E9%9D%A0%E8%AA%B0%E6%89%9B%EF%BC%9F%E8%87%BB%E9%BC%8E-ky%E6%BC%B2%E5%81%9C%E3%80%81abf%E6%8F%AA%E7%9F%BD%E6%99%B6%E5%9C%93%E6%9A%B4%E8%B5%B0%E7%8B%82%E6%AD%A1%EF%BD%9Cyahoo%E8%B2%A1%E7%B6%93%E6%8E%83%E6%8F%8F-085945117.html
- 事件2：8月獲利暴增665%！「ABF載板股」單月賺進Q2近一半　投信也同步掃貨逾3千張
  - 來源：Yahoo 台股；發布時間：2026-10-02T11:00:00Z；台北時間：2026-10-02 19:00
  - 摘要：[FTNN新聞網]記者黃詩雯／綜合報導台股今（2）日終場上漲122.25點，漲幅0.25%，收在48475.74點，據證交所籌碼動向，投信買超49.09億元，觀察買超個股方面，AB...
  - 原文連結：https://tw.stock.yahoo.com/news/8%E6%9C%88%E7%8D%B2%E5%88%A9%E6%9A%B4%E5%A2%9E665-abf%E8%BC%89%E6%9D%BF%E8%82%A1-%E5%96%AE%E6%9C%88%E8%B3%BA%E9%80%B2q2%E8%BF%91-%E5%8D%8A-%E6%8A%95%E4%BF%A1%E4%B9%9F%E5%90%8C%E6%AD%A5%E6%8E%83%E8%B2%A8%E9%80%BE3%E5%8D%83%E5%BC%B5-110000115.html
- 事件3：新台幣再陷32元保衛戰！尾盤「V型反轉」連3紅　周線翻黑
  - 來源：Yahoo 台股；發布時間：2026-10-02T10:47:04Z；台北時間：2026-10-02 18:47
  - 摘要：儘管美債殖利率回落，但避險需求持續流向美元資產，加上美國經濟表現韌性，通膨低於預期等，國際美元居高不下，儘管台股今（10/2）日持續收紅，但熱錢自行調節，並未完全匯入，新台幣匯率依舊開低走低，早盤再度摜破31.9字頭，午後出口商賣壓出籠，尾
  - 原文連結：https://tw.stock.yahoo.com/news/%E6%96%B0%E5%8F%B0%E5%B9%A3%E5%86%8D%E9%99%B732%E5%85%83%E4%BF%9D%E8%A1%9B%E6%88%B0-%E5%B0%BE%E7%9B%A4-v%E5%9E%8B%E5%8F%8D%E8%BD%89-%E9%80%A33%E7%B4%85-%E5%91%A8%E7%B7%9A%E7%BF%BB%E9%BB%91-104704308.html
- 事件4：豪砸28億元攻AI光通訊！「砷化鎵大廠」2027年迎新動能　PA營收占比拚降至6成以下
  - 來源：Yahoo 台股；發布時間：2026-10-02T10:45:00Z；台北時間：2026-10-02 18:45
  - 摘要：[FTNN新聞網]記者黃詩雯／綜合報導砷化鎵晶圓代工廠宏捷科（8086）今年營運維持成長，9月營收4.22億元，月增0.05%、年增8.4%；第三季營收12.66億元，雖季減2....
  - 原文連結：https://tw.stock.yahoo.com/news/%E8%B1%AA%E7%A0%B828%E5%84%84%E5%85%83%E6%94%BBai%E5%85%89%E9%80%9A%E8%A8%8A-%E7%A0%B7%E5%8C%96%E9%8E%B5%E5%A4%A7%E5%BB%A0-2027%E5%B9%B4%E8%BF%8E%E6%96%B0%E5%8B%95%E8%83%BD-pa%E7%87%9F%E6%94%B6%E5%8D%A0%E6%AF%94%E6%8B%9A%E9%99%8D%E8%87%B36%E6%88%90%E4%BB%A5%E4%B8%8B-104500861.html
- 事件5：9月後職缺易踩雷？ 網傳「放棄年終也要走」 內行曝真相
  - 來源：Yahoo 台股；發布時間：2026-10-02T10:35:00Z；台北時間：2026-10-02 18:35
  - 摘要：費時費心找工作，最怕誤入「雷缺」，之前有人認為，9月後到年末這段時期，若公司釋出職缺，可能是員工寧放棄年終獎金也要離職的「雷缺」，最好不要應徵，引發眾人討論。
  - 原文連結：https://tw.stock.yahoo.com/news/9%E6%9C%88%E5%BE%8C%E8%81%B7%E7%BC%BA%E6%98%93%E8%B8%A9%E9%9B%B7-%E7%B6%B2%E5%82%B3-%E6%94%BE%E6%A3%84%E5%B9%B4%E7%B5%82%E4%B9%9F%E8%A6%81%E8%B5%B0-%E5%85%A7%E8%A1%8C%E6%9B%9D%E7%9C%9F%E7%9B%B8-103500222.html
- 事件6：12萬股東快看！00923小換血3進3出「記憶體指標」、景碩、友達強勢入列　「這封測廠」卻遭踢下車
  - 來源：Yahoo 台股；發布時間：2026-10-02T10:30:00Z；台北時間：2026-10-02 18:30
  - 摘要：[FTNN新聞網]記者王凱暄／綜合報導受益人數約12.2萬人、資金規模約398.93億元的市值型ETF群益台ESG低碳50（00923），今（2）日公布成分股定期審核結果，本次...
  - 原文連結：https://tw.stock.yahoo.com/news/12%E8%90%AC%E8%82%A1%E6%9D%B1%E5%BF%AB%E7%9C%8B-00923%E5%B0%8F%E6%8F%9B%E8%A1%803%E9%80%B23%E5%87%BA-%E8%A8%98%E6%86%B6%E9%AB%94%E6%8C%87%E6%A8%99-%E6%99%AF%E7%A2%A9-%E5%8F%8B%E9%81%94%E5%BC%B7%E5%8B%A2%E5%85%A5%E5%88%97-103000252.html
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
- 事件10：Eurozone inflation hits its highest level in three years at 3.8% as energy costs soar
  - 來源：CNBC；發布時間：Fri, 02 Oct 2026 09:39:51 GMT；台北時間：2026-10-02 17:39
  - 摘要：Annual euro zone inflation hit 3.8% last month, its highest level since September 2023.
  - 原文連結：https://www.cnbc.com/2026/10/02/eurozone-inflation-ecb.html
- 事件11：Oil prices fall over 3% on report of potential diesel, crude stock release; Brent back below $100
  - 來源：CNBC；發布時間：Fri, 02 Oct 2026 09:34:33 GMT；台北時間：2026-10-02 17:34
  - 摘要：It comes after Reuters reported that EU nations were discussing a proposal to release diesel reserves following pressure from the Trump administration
  - 原文連結：https://www.cnbc.com/2026/10/02/oil-wti-brent-diesel-stock-release-europe.html
- 事件12：How AI is redefining Wall Street jobs — and boosting demand for this new 'hottest skill' by 1,721%
  - 來源：CNBC；發布時間：Fri, 02 Oct 2026 10:00:01 GMT；台北時間：2026-10-02 18:00
  - 摘要：Banks are fueling a hiring surge for AI engineers who are good at "agent orchestration" — the ability to coordinate teams of specialized agents.
  - 原文連結：https://www.cnbc.com/2026/10/02/ai-redefining-wall-street-jobs.html


## 三、期貨

**資料來源：**
1. Cloudflare Workers：TAIFEX Proxy — https://taifex.grichtoyang.workers.dev/
2. TAIFEX Open API — https://openapi.taifex.com.tw/

近月契約月份：202610 (日盤成交量最大者)；交易日期：2026-10-02

### 1．台指期近月日盤行情

| 項目 | 數值 | 資料來源 |
|---|---|---|
| 開盤價 | 48,552 | TAIFEX Proxy |
| 最高價 | 48,802 | TAIFEX Proxy |
| 最低價 | 48,472 | TAIFEX Proxy |
| 收盤價 | 48,671 | TAIFEX Proxy |
| 漲跌點數 | -27 | TAIFEX Proxy |
| 漲跌幅 | -0.06 | TAIFEX Proxy |
| 成交量 | 71,568 | TAIFEX Proxy |
| 日盤高點及低點 | 48,802 / 48,472 | TAIFEX Proxy |

### 2．台指期近月夜盤行情

| 項目 | 數值 | 資料來源 |
|---|---|---|
| 開盤價 | 48,622 | TAIFEX Proxy |
| 最高價 | 48,661 | TAIFEX Proxy |
| 最低價 | 48,210 | TAIFEX Proxy |
| 收盤價 | 48,475 | TAIFEX Proxy |
| 漲跌點數 | -223 | TAIFEX Proxy |
| 漲跌幅 | -0.46 | TAIFEX Proxy |
| 成交量 | 37,554 | TAIFEX Proxy |
| 夜盤高點及低點 | 48,661 / 48,210 | TAIFEX Proxy |
| 結算價 | 48,669 | TAIFEX Proxy |
| 未平倉量 | 106,691 | TAIFEX Proxy |

### 3．法人台指期多空未平倉部位

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 外資多方 OI | 11,893 | TAIFEX Proxy |
| 外資空方 OI | 92,197 | TAIFEX Proxy |
| 外資多空淨 OI | -80,304 | TAIFEX Proxy |
| 投信多方 OI | 77,530 | TAIFEX Proxy |
| 投信空方 OI | 2,861 | TAIFEX Proxy |
| 投信多空淨 OI | +74,669 | TAIFEX Proxy |
| 自營商多方 OI | 3,340 | TAIFEX Proxy |
| 自營商空方 OI | 4,346 | TAIFEX Proxy |
| 自營商多空淨 OI | -1,006 | TAIFEX Proxy |
| 三大法人合計多方 OI | 92,763 | TAIFEX Proxy |
| 三大法人合計空方 OI | 99,404 | TAIFEX Proxy |
| 三大法人合計多空淨 OI | -6,641 | TAIFEX Proxy |
| 外資多空淨 OI 變化 | -750 | TAIFEX Proxy |
| 投信多空淨 OI 變化 | +54 | TAIFEX Proxy |
| 自營商多空淨 OI 變化 | +434 | TAIFEX Proxy |

### 4．前十大交易人多空未平倉部位

**資料來源：** `TAIFEX OpenAPI OpenInterestOfLargeTradersFutures` (官方資料落後約一日，標示實際日期)

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 前十大交易人多方 OI | 80,995 | TAIFEX Proxy |
| 前十大交易人空方 OI | 76,012 | TAIFEX Proxy |
| 前十大交易人多空淨 OI | +4,983 | TAIFEX Proxy |
| 多空淨 OI 變化 (2026-09-30→2026-10-01) | -1,546 | TAIFEX Proxy snapshots (2026-10-01) |
- 資料日期：2026-10-01 (TypeOfTraders=0 全部交易人；契約月份 202610)

### 5．日盤、夜盤法人交易資料

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 外資日盤多單交易量 | 39,654 | TAIFEX Proxy |
| 外資日盤空單交易量 | 40,456 | TAIFEX Proxy |
| 外資日盤多空淨交易量 | -802 | TAIFEX Proxy |
| 外資夜盤多單交易量 | 20,282 | TAIFEX Proxy |
| 外資夜盤空單交易量 | 21,659 | TAIFEX Proxy |
| 外資夜盤多空淨交易量 | -1,377 | TAIFEX Proxy |
| 外資日盤／夜盤交易量變化 | +575 | TAIFEX Proxy |
| 投信日盤多空淨交易量 | +54 | TAIFEX Proxy |
| 投信夜盤多空淨交易量 | +0 | TAIFEX Proxy |
| 投信日盤／夜盤交易量變化 | +54 | TAIFEX Proxy |
| 自營商日盤多空淨交易量 | +428 | TAIFEX Proxy |
| 自營商夜盤多空淨交易量 | +654 | TAIFEX Proxy |
| 自營商日盤／夜盤交易量變化 | -226 | TAIFEX Proxy |
| 三大法人日盤多空淨交易量 | -320 | TAIFEX Proxy |
| 三大法人夜盤多空淨交易量 | -723 | TAIFEX Proxy |
| 法人日盤交易金額淨額 (億元) | -30.3 | TAIFEX Proxy |
| 法人夜盤交易金額淨額 (億元) | -69.8 | TAIFEX Proxy |

### 6．期貨與現貨關係

| 項目 | 數值 | 資料來源 |
|---|---|---|
| 台指期近月價格 | 48,671 | TAIFEX Proxy |
| 加權指數價格 | 48,475.74 | twse-proxy |
| 台指期與加權指數價差 | +195.26 | TAIFEX Proxy+twse-proxy |
| 價差百分比 | +0.40 | TAIFEX Proxy+twse-proxy |
| 日盤基差 | +195.26 | TAIFEX Proxy+twse-proxy |
| 夜盤價格相對日盤收盤的變化 | -196 | TAIFEX Proxy |

### 7．日盤、夜盤與籌碼變化對照

#### 7.1 日夜盤價格與成交量對照 (變化 = 日盤 - 夜盤)

| 項目 | 日盤 | 夜盤 | 變化 (日-夜) | 資料來源 |
|---|---|---|---|---|
| 收盤價 | 48,671 | 48,475 | +196 | TAIFEX Proxy |
| 成交量 | 34,014 | 37,554 | -3,540 | TAIFEX Proxy |
- 台指期總 OI 前日變化：-262（來源：TAIFEX Proxy）


#### 7.2 法人籌碼日夜盤對照 (淨變化 = 日盤淨 - 夜盤淨；OI 為日盤收盤後總量，前日變化另列)

| 法人 | 交易量 |  |  |  |  |  |  | 未平倉量 |  |  |  | 資料來源 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|  | **日盤多單** | **日盤空單** | **日盤淨** | **夜盤多單** | **夜盤空單** | **夜盤淨** | **淨變化 (日-夜)** | **OI多方** | **OI空方** | **OI淨** | **OI前日變化** |  |
| 外資 | 39,654 | 40,456 | -802 | 20,282 | 21,659 | -1,377 | +575 | 11,893 | 92,197 | -80,304 | -750 | TAIFEX Proxy |
| 投信 | 111 | 57 | +54 | 0 | 0 | +0 | +54 | 77,530 | 2,861 | +74,669 | +54 | TAIFEX Proxy |
| 自營商 | 3,841 | 3,413 | +428 | 1,505 | 851 | +654 | -226 | 3,340 | 4,346 | -1,006 | +434 | TAIFEX Proxy |
| 三大法人合計 | 43,606 | 43,926 | -320 | 21,787 | 22,510 | -723 | +403 | 92,763 | 99,404 | -6,641 | -262 | TAIFEX Proxy |

#### 7.3 前十大交易人日夜盤對照 (OI 無日夜拆分，列收盤後總量)

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 前十大交易人多方 OI | 80,995 | TAIFEX Proxy |
| 前十大交易人空方 OI | 76,012 | TAIFEX Proxy |
| 前十大交易人多空淨 OI | +4,983 | TAIFEX Proxy |
| 前十大交易人多空淨 OI 變化 (2026-09-30→2026-10-01) | -1,546 | TAIFEX Proxy snapshots (2026-10-01) |

#### 7.4 夜盤劇本分類 (規則對應：夜盤漲跌 × 外資夜盤偏多空)

| 項目 | 數值 | 資料來源 |
|---|---|---|
| 夜盤成交量占比 (夜盤量／(夜盤量＋日盤量)) | 52.47% | TAIFEX Proxy |
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
| 交易日期 | 2026-10-02 | TAIFEX Proxy |
| 到期月份／到期日 | 202610F1 | TAIFEX Proxy |
| 資料更新時間 | 2026-10-02 19:15:14 | 本機 |
| 日盤／夜盤標記 | 日盤收盤後資料 | TAIFEX Proxy |

### 2．Call 總成交量、OI、OI 增減

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Call 總成交量 | 309,089 | TAIFEX Proxy |
| Call 總未平倉量 OI | 61,225 | TAIFEX Proxy |
| Call OI 增減 (2026-10-01→2026-10-02) | +21,707 | TAIFEX Proxy snapshots (2026-10-01) |

### 3．Put 總成交量、OI、OI 增減

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Put 總成交量 | 274,213 | TAIFEX Proxy |
| Put 總未平倉量 OI | 54,441 | TAIFEX Proxy |
| Put OI 增減 (2026-10-01→2026-10-02) | +23,623 | TAIFEX Proxy snapshots (2026-10-01) |

### 4．Call／Put 比例與變化

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Call／Put 成交量比例 | 1.13 | TAIFEX Proxy |
| Call／Put 未平倉量比例 | 1.12 | TAIFEX Proxy |
| Put／Call Ratio | 0.89 | TAIFEX Proxy |
| Call／Put 比例變化 (量比 2026-09-30→2026-10-01) | -8.09 | TAIFEX Proxy |
| 與前一交易日比較 (OI 比 2026-09-30→2026-10-01) | 1.97 | TAIFEX Proxy |
**資料來源：** 比例 `TAIFEX Proxy chain`；變化 `TAIFEX Proxy PutCallRatio`

### 5．外資 Call／Put 部位

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 外資 Call日買 | 110,844 | TAIFEX Proxy |
| 外資 Call日賣 | 111,325 | TAIFEX Proxy |
| 外資 Call日淨 | -481 | TAIFEX Proxy |
| 外資 Put日買 | 100,159 | TAIFEX Proxy |
| 外資 Put日賣 | 104,402 | TAIFEX Proxy |
| 外資 Put日淨 | -4,243 | TAIFEX Proxy |
| 外資 Call夜買 | 52,503 | TAIFEX Proxy |
| 外資 Call夜賣 | 52,350 | TAIFEX Proxy |
| 外資 Call夜淨 | +153 | TAIFEX Proxy |
| 外資 Put夜買 | 48,191 | TAIFEX Proxy |
| 外資 Put夜賣 | 47,677 | TAIFEX Proxy |
| 外資 Put夜淨 | +514 | TAIFEX Proxy |
| 外資 日盤淨總量 | +3,762 | TAIFEX Proxy |
| 外資 Call日夜淨增減 (日－夜) | -634 | TAIFEX Proxy |
| 外資 Put日夜淨增減 (日－夜) | -4,757 | TAIFEX Proxy |

### 6．自營商 Call／Put 部位

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 自營商 Call日買 | 71,525 | TAIFEX Proxy |
| 自營商 Call日賣 | 77,521 | TAIFEX Proxy |
| 自營商 Call日淨 | -5,996 | TAIFEX Proxy |
| 自營商 Put日買 | 75,505 | TAIFEX Proxy |
| 自營商 Put日賣 | 75,627 | TAIFEX Proxy |
| 自營商 Put日淨 | -122 | TAIFEX Proxy |
| 自營商 Call夜買 | 25,486 | TAIFEX Proxy |
| 自營商 Call夜賣 | 29,000 | TAIFEX Proxy |
| 自營商 Call夜淨 | -3,514 | TAIFEX Proxy |
| 自營商 Put夜買 | 24,828 | TAIFEX Proxy |
| 自營商 Put夜賣 | 24,489 | TAIFEX Proxy |
| 自營商 Put夜淨 | +339 | TAIFEX Proxy |
| 自營商 日盤淨總量 | -5,874 | TAIFEX Proxy |
| 自營商 Call日夜淨增減 (日－夜) | -2,482 | TAIFEX Proxy |
| 自營商 Put日夜淨增減 (日－夜) | -461 | TAIFEX Proxy |

### 7．主要 Call OI 集中區

| 項目 | 履約價 | OI | 資料來源 |
|---|---|---|---|
| Call OI 第1大履約價 | 48,500 | 6,284 | TAIFEX Proxy |
| Call OI 第2大履約價 | 48,450 | 4,895 | TAIFEX Proxy |
| Call OI 第3大履約價 | 48,600 | 3,156 | TAIFEX Proxy |
| Call OI 最大履約價 | 48,500 | 6,284 | TAIFEX Proxy |

#### Call OI 分布明細 Top10 (機器可讀，到期月份 202610F1)

| # | 履約價 | OI | 佔比 | 資料來源 |
|---|---|---|---|---|
| C1 | 48,500 | 6,284 | 10.26% | TAIFEX Proxy |
| C2 | 48,450 | 4,895 | 8.0% | TAIFEX Proxy |
| C3 | 48,600 | 3,156 | 5.15% | TAIFEX Proxy |
| C4 | 49,000 | 3,135 | 5.12% | TAIFEX Proxy |
| C5 | 48,800 | 2,656 | 4.34% | TAIFEX Proxy |
| C6 | 48,550 | 2,627 | 4.29% | TAIFEX Proxy |
| C7 | 48,400 | 2,207 | 3.6% | TAIFEX Proxy |
| C8 | 48,700 | 2,137 | 3.49% | TAIFEX Proxy |
| C9 | 52,000 | 1,690 | 2.76% | TAIFEX Proxy |
| C10 | 50,500 | 1,649 | 2.69% | TAIFEX Proxy |


### 8．主要 Put OI 集中區

| 項目 | 履約價 | OI | 資料來源 |
|---|---|---|---|
| Put OI 第1大履約價 | 48,400 | 4,590 | TAIFEX Proxy |
| Put OI 第2大履約價 | 48,350 | 4,143 | TAIFEX Proxy |
| Put OI 第3大履約價 | 48,300 | 3,838 | TAIFEX Proxy |
| Put OI 最大履約價 | 48,400 | 4,590 | TAIFEX Proxy |

#### Put OI 分布明細 Top10 (機器可讀，到期月份 202610F1)

| # | 履約價 | OI | 佔比 | 資料來源 |
|---|---|---|---|---|
| P1 | 48,400 | 4,590 | 8.43% | TAIFEX Proxy |
| P2 | 48,350 | 4,143 | 7.61% | TAIFEX Proxy |
| P3 | 48,300 | 3,838 | 7.05% | TAIFEX Proxy |
| P4 | 48,000 | 3,079 | 5.66% | TAIFEX Proxy |
| P5 | 48,450 | 2,756 | 5.06% | TAIFEX Proxy |
| P6 | 47,900 | 2,537 | 4.66% | TAIFEX Proxy |
| P7 | 48,200 | 2,456 | 4.51% | TAIFEX Proxy |
| P8 | 48,100 | 1,990 | 3.66% | TAIFEX Proxy |
| P9 | 47,500 | 1,918 | 3.52% | TAIFEX Proxy |
| P10 | 47,000 | 1,835 | 3.37% | TAIFEX Proxy |


### 9．Call OI 增減集中區

| 項目 | 履約價 (增減口數) | 資料來源 |
|---|---|---|
| Call OI 增加最多的履約價 | 48,500 (+4,741) | TAIFEX Proxy snapshots (2026-10-01) |
| Call OI 減少最多的履約價 | 49,500 (-230) | TAIFEX Proxy snapshots (2026-10-01) |

### 10．Put OI 增減集中區

| 項目 | 履約價 (增減口數) | 資料來源 |
|---|---|---|
| Put OI 增加最多的履約價 | 48,400 (+4,146) | TAIFEX Proxy snapshots (2026-10-01) |
| Put OI 減少最多的履約價 | 47,600 (-913) | TAIFEX Proxy snapshots (2026-10-01) |

### 11．Call Wall

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Call Wall 價位 | 48,500 | TAIFEX Proxy |
| 對應到期月份 | 202610F1 | TAIFEX Proxy |
| 與前一交易日的變化 (2026-10-01→2026-10-02) | -500 | TAIFEX Proxy snapshots (2026-10-01) |

### 12．Put Wall

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Put Wall 價位 | 48,400 | TAIFEX Proxy |
| 對應到期月份 | 202610F1 | TAIFEX Proxy |
| 與前一交易日的變化 (2026-10-01→2026-10-02) | +400 | TAIFEX Proxy snapshots (2026-10-01) |

### 13．Gamma Wall

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Gamma Wall 價位 | 48,500.00 | TAIFEX Proxy (options-market-structure-compact (proxy)) |
| 對應到期月份 | 202610F1 | TAIFEX Proxy |
| 資料日期 | 2026-10-01 | TAIFEX Proxy (options-market-structure-compact (proxy)) |

### 14．Gamma Flip

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Gamma Flip 價位 | 47,831.68 | TAIFEX Proxy (options-market-structure-compact (proxy)) |
| 對應到期月份 | 202610F1 | TAIFEX Proxy |
| 資料日期 | 2026-10-01 | TAIFEX Proxy (options-market-structure-compact (proxy)) |

### 15．Max Pain

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Max Pain 價位 | 48,350 | TAIFEX Proxy |
| 對應到期月份 | 202610F1 | TAIFEX Proxy |
| 與前一交易日的變化 (2026-10-01→2026-10-02) | +400 | TAIFEX Proxy snapshots (2026-10-01) |

### 17．選擇權法人日盤、夜盤交易

| 法人 | 日盤多單 | 日盤空單 | 日盤淨 | 夜盤多單 | 夜盤空單 | 夜盤淨 | 淨變化 (日-夜) | 資料來源 |
|---|---|---|---|---|---|---|---|---|
| 外資 | 215,246 | 211,484 | +3,762 | 100,180 | 100,541 | -361 | +4,123 | TAIFEX Proxy |
| 投信 | 0 | 3,100 | -3,100 | 0 | 0 | +0 | -3,100 | TAIFEX Proxy |
| 自營商 | 147,152 | 153,026 | -5,874 | 49,975 | 53,828 | -3,853 | -2,021 | TAIFEX Proxy |
| 三大法人合計 | 362,398 | 367,610 | -5,212 | 150,155 | 154,369 | -4,214 | -998 | TAIFEX Proxy |
- 方法論：多方＝買Call＋賣Put（看多），空方＝賣Call＋買Put（看空），淨額＝看多－看空（已用 Call／Put 拆分頁交叉驗算一致）
- 公式：多方(買)－空方(賣)＝（買call＋賣put）－（賣call＋買put）＝看多－看空
- 速記：多＝BC＋SP、空＝SC＋BP

#### 法人多空力道表（金額・億元；上游千元／1e5）

| 法人 | 日多方力道 | 日空方力道 | 日淨多空力道 | 夜多方力道 | 夜空方力道 | 夜淨多空力道 | 日淨－夜淨 | 資料來源 |
|---|---|---|---|---|---|---|---|---|
| 外資 | 10.14 | 9.97 | +0.17 | 6.17 | 6.17 | +0.00 | +0.17 | TAIFEX Proxy |
| 投信 | 0.00 | 2.32 | -2.32 | 0.00 | 0.00 | +0 | -2.32 | TAIFEX Proxy |
| 自營商 | 8.73 | 6.69 | +2.04 | 2.56 | 3.03 | -0.46 | +2.50 | TAIFEX Proxy |
| 三大法人合計 | 18.87 | 18.98 | -0.11 | 8.74 | 9.19 | -0.46 | +0.35 | TAIFEX Proxy |

### 18．選擇權前十大

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 買權多方 OI | 12,568 | TAIFEX Proxy |
| 買權空方 OI | 11,784 | TAIFEX Proxy |
| 買權多空淨 OI | +784 | TAIFEX Proxy |
| 買權多空淨 OI 變化 (2026-09-30→2026-10-01) | -262 | TAIFEX Proxy snapshots (2026-10-01) |

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 賣權多方 OI | 8,187 | TAIFEX Proxy |
| 賣權空方 OI | 9,273 | TAIFEX Proxy |
| 賣權多空淨 OI | -1,086 | TAIFEX Proxy |
| 賣權多空淨 OI 變化 (2026-09-30→2026-10-01) | -462 | TAIFEX Proxy snapshots (2026-10-01) |
- 資料日期：買權 2026-10-01／賣權 2026-10-01 (TypeOfTraders=0 全部交易人；契約月份 202610)

#### 大戶流向（全日；前十大無日夜拆分）

| 項目 | 淨變化 | 區間 | 資料來源 |
|---|---|---|---|
| 期貨前十大 | -1,546 | 2026-09-30→2026-10-01 | TAIFEX Proxy snapshots (2026-10-01) |
| 買權前十大 | -262 | 2026-09-30→2026-10-01 | TAIFEX Proxy snapshots (2026-10-01) |
| 賣權前十大 | -462 | 2026-09-30→2026-10-01 | TAIFEX Proxy snapshots (2026-10-01) |

### 16．資料來源、時間、時區與狀態

- 資料來源：TAIFEX 經 Cloudflare Worker Proxy
- 資料日期：2026-10-02；資料時間：2026-10-02 19:15:14；時區：`Asia/Taipei`
- 日盤／夜盤標記：日盤收盤後 + 夜盤盤後
- 未取得欄位 (4)：margin.fin_yi, margin.fin_chg_yi, sbl.sale_bal, sbl.sale_chg
- 註記：Gamma 資料日期 2026-10-01 (T0 2026-10-02 尚無，上游 FMTQIK 落後，採最新可得)
- 註記：法人交易量變化無昨日交易端點，標 unavailable
- 註記：Gamma Wall/Flip 資料日期 2026-10-01 (來源 options-market-structure-compact (proxy))

## 五、資料來源、時間與完整性

- 期貨/匯率為最新報價，其餘為 T0 收盤資料；時間皆為 `Asia/Taipei`。
- taiex：`twse-proxy`
- taiex_ohlc：`FinMind TaiwanStockPrice TAIEX`
- listed_turnover：`twse-proxy market_statistics`
- listed_breadth：`twse-proxy`
- otc：`TPEX OpenAPI tpex_mainborad_highlight`
- institutional：`twse-proxy /institutional`
- margin_short：`TWSE MI_MARGN + TPEX margin_balance (張)`
- margin_ratio：`前值遞補 (DATA 2026-10-01；當日三源皆失敗；民間估算；官方無每日序列)`
- sbl：`TWSE TWT93U + TPEX margin_sbl`
- 期貨選擇權：`TAIFEX Proxy`
- 新聞：台股 Yahoo／國際 Fed＋CNBC＋MarketWatch；台股 Yahoo（不足時財訊快報備援）/ 國際 Fed 公告＋CNBC＋MarketWatch RSS；Fed 無摘要；investing 港股為主已退役；cnyes CSR、wantgoo JS 算繪、中央社/台灣央行路徑待查，未採用
- 美股/亞股/期貨/匯率/ADR/商品：`Yahoo Finance Chart API`；美債：`Yahoo Finance (備援)`
- 註記：HiStock 未取得，融資餘額/增減標 unavailable (官方逐股加總僅有張數)
- 註記：融券沿用官方逐股加總 (張)
- 註記：融資維持率未取得 (三源皆失敗；官方無每日序列)
- 註記：融資維持率採前值遞補 (DATA 2026-10-01)，非 T0 2026-10-02
- 註記：上市 MI_MARGN / TWT96U 無日期欄，採用最新可得
- 本報告僅整理資料，不提供交易判斷。

## 六、期現選方向對照

**規則：** 趨勢偏多／空＝現貨、期貨OI、選擇權日淨三者同向；避險／對沖＝現貨與期選反向；日內反轉＝日淨與夜淨反向；缺值標示，不推估。選擇權多空為看多看空口徑。

| 法人 | 現貨買賣超(億) | 期貨OI淨(口) | 期貨日淨 | 期貨夜淨 | 選擇權日淨 | 選擇權夜淨 | 判定 | 期選組合 | 資料來源 |
|---|---|---|---|---|---|---|---|---|---|
| 外資 | +26.2 | -80,304 | -802 | -1,377 | +3,762 | -361 | 避險／對沖 | 強避險 | twse-proxy／TAIFEX Proxy |
| 投信 | +49.1 | +74,669 | +54 | +0 | -3,100 | +0 | 避險／對沖 | 分歧 | twse-proxy／TAIFEX Proxy |
| 自營商 | +20.3 | -1,006 | +428 | +654 | -5,874 | -3,853 | 避險／對沖 | 強避險 | twse-proxy／TAIFEX Proxy |
