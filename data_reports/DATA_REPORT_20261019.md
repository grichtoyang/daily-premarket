# DATA_REPORT_20261019

- 報告日期：`2026-10-20`
- T0 交易日期：`2026-10-19`
- 資料產出時間：`2026-10-20 10:34:21`
- 時區：`Asia/Taipei`
- 產出盤別：`全日`
- 產出者：`actions`
- 排定班別：`morning`

---

## 一、現貨

### 1. 台股大盤行情

**資料來源：** `Cloudflare Worker：twse-proxy` (備援 `TWSE OpenAPI MI_INDEX`)

| 項目 | 數值 | 單位 | 資料來源 |
|---|---|---|---|
| 加權指數 | 46,822.08 | 點 | twse-proxy |
| 開盤 | 46,844.64 | 點 | FinMind TaiwanStockPrice TAIEX |
| 最高 | 46,844.64 | 點 | FinMind TaiwanStockPrice TAIEX |
| 最低 | 46,170.00 | 點 | FinMind TaiwanStockPrice TAIEX |
| 收盤 | 46,822.08 | 點 | twse-proxy |
| 漲跌點數 | -289.18 | 點 | twse-proxy |
| 漲跌幅 | -0.61 | % | twse-proxy |
| 成交金額 | 8,667.1 | 億元 | twse-proxy market_statistics |

### 2. 市場漲跌家數

#### 2.1 上市公司

**資料來源：** `Cloudflare Worker：twse-proxy` (備援 `TWSE OpenAPI twtazu_od`)

| 項目 | 家數 | 資料來源 |
|---|---|---|
| 上漲家數 | 163 | twse-proxy |
| 下跌家數 | 849 | twse-proxy |
| 平盤家數 | 61 | twse-proxy |
| 漲停家數 | 7 | twse-proxy |
| 跌停家數 | 2 | twse-proxy |

#### 2.2 上櫃公司

**資料來源：** `TPEX OpenAPI tpex_mainborad_highlight`

| 項目 | 家數 | 資料來源 |
|---|---|---|
| 上漲家數 | 161 | TPEX OpenAPI tpex_mainborad_highlight |
| 下跌家數 | 647 | TPEX OpenAPI tpex_mainborad_highlight |
| 平盤家數 | 62 | TPEX OpenAPI tpex_mainborad_highlight |
| 漲停家數 | 13 | TPEX OpenAPI tpex_mainborad_highlight |
| 跌停家數 | 5 | TPEX OpenAPI tpex_mainborad_highlight |

### 3. 三大法人現貨買賣超

**資料來源：** `TWSE RWD BFI82U`

| 法人別 | 買賣超金額 | 單位 | 資料來源 |
|---|---|---|---|
| 外資 | -767.4 | 億元 | twse-proxy /institutional |
| 投信 | +241.4 | 億元 | twse-proxy /institutional |
| 自營商 | -362.6 | 億元 | twse-proxy /institutional |
| 三大法人合計 | -888.6 | 億元 | twse-proxy /institutional |

### 4. 融資融券

**資料來源：** 上市+上櫃 `HiStock` (金額口徑)；維持率 `istock.tw`；備援官方逐股加總

| 項目 | 數值 | 單位 | 資料來源 |
|---|---|---|---|
| 融資餘額 | 8,558.4 | 億元 | HiStock 上市+上櫃融資融券 (金額口徑) |
| 融資增減 | -80.1 | 億元 | HiStock 上市+上櫃融資融券 (金額口徑) |
| 融券餘額 | 238,903 | 張 | HiStock 上市+上櫃融資融券 (金額口徑) |
| 融券增減 | -32,945 | 張 | HiStock 上市+上櫃融資融券 (金額口徑) |
| 融資維持率 | 183.39 | % | 前值遞補 (DATA 2026-10-16；當日三源皆失敗；民間估算；官方無每日序列) |

### 5. 借券資料

**資料來源：** 上市 `TWSE OpenAPI TWT96U` (可借餘額)、上櫃 `TPEX OpenAPI tpex_margin_sbl`

| 項目 | 數值 | 單位 | 資料來源 |
|---|---|---|---|
| 借券餘額 | 4,573,227 | 張 | TWSE TWT93U + TPEX margin_sbl |
| 借券賣出餘額 | 36,987 | 張 | TWSE TWT93U + TPEX margin_sbl |
| 借券賣出增減 | -1,259 | 張 | TWSE TWT93U + TPEX margin_sbl |

### 6. 市場成交結構

**資料來源：** 上市 `twse-proxy market_statistics`、上櫃 `TPEX OpenAPI tpex_mainborad_highlight`

| 項目 | 成交金額 | 單位 | 資料來源 |
|---|---|---|---|
| 上市成交金額 | 8,667.1 | 億元 | twse-proxy market_statistics |
| 上櫃成交金額 | 2,123.5 | 億元 | TPEX OpenAPI tpex_mainborad_highlight |
| 上市櫃成交金額合計 | 10,790.6 | 億元 | twse-proxy market_statistics+TPEX OpenAPI tpex_mainborad_highlight |

## 二、重要市場

### 1. 美股指數

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 收盤／最新值 | 漲跌點 | 漲跌幅 | 資料來源 |
|---|---|---|---|---|---|
| S&P 500 | ^GSPC | 7,690.73 | 31.29 | +0.41 | Yahoo Finance Chart API |
| Nasdaq Composite | ^IXIC | 26,430.89 | 290.86 | +1.11 | Yahoo Finance Chart API |
| Nasdaq 100 | ^NDX | 29,529.34 | 341.79 | +1.17 | Yahoo Finance Chart API |
| Dow Jones | ^DJI | 51,966.03 | -36.38 | -0.07 | Yahoo Finance Chart API |
| 費城半導體 SOX | ^SOX | 11,316.34 | 179.05 | +1.61 | Yahoo Finance Chart API |
| VIX | ^VIX | 18.44 | -1.55 | -7.75 | Yahoo Finance Chart API |

### 2. 亞洲主要指數

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 收盤／最新值 | 漲跌點 | 漲跌幅 | 資料來源 |
|---|---|---|---|---|---|
| 日經225 | ^N225 | 64,532.26 | -384.44 | -0.59 | Yahoo Finance Chart API |
| 韓國KOSPI | ^KS11 | 5,595.18 | -172.83 | -3.00 | Yahoo Finance Chart API |
| 香港恆生 | ^HSI | 23,957.33 | -229.50 | -0.95 | Yahoo Finance Chart API |
| 上海綜合 | 000001.SS | 3,728.70 | -2.22 | -0.06 | Yahoo Finance Chart API |
| 深圳成分 | 399001.SZ | 11,824.42 | 7.00 | +0.06 | Yahoo Finance Chart API |

### 3. 美股指數期貨

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 最新值 | 漲跌點 | 漲跌幅 | 資料來源 |
|---|---|---|---|---|---|
| S&P500期貨 | ES=F | 7,749.00 | 14.50 | +0.19 | Yahoo Finance Chart API |
| Nasdaq100期貨 | NQ=F | 29,744.50 | 22.00 | +0.07 | Yahoo Finance Chart API |
| 道瓊期貨 | YM=F | 52,333.00 | 151.00 | +0.29 | Yahoo Finance Chart API |
| Russell2000期貨 | RTY=F | 2,746.80 | 4.50 | +0.16 | Yahoo Finance Chart API |

### 4. 美國國債殖利率

**資料來源：** `U.S. Treasury Fiscal Data API` (失敗時備援 Treasury yield.xml 與 `Yahoo Finance`)

| 項目 | API 資料欄位／識別 | 殖利率 | 日變化 | 資料來源 |
|---|---|---|---|---|
| 美國 2 年期殖利率 | 2 Yr | 4.77 | 0.03 | U.S. Treasury yield.xml (網頁備援) |
| 美國 10 年期殖利率 | 10 Yr | 5.14 | 0.04 | Yahoo Finance (備援) |
| 美國 30 年期殖利率 | 30 Yr | 5.47 | 0.04 | Yahoo Finance (備援) |

### 5. 主要匯率

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 最新值 | 漲跌點 | 漲跌幅 | 資料來源 |
|---|---|---|---|---|---|
| USD/TWD | TWD=X | 32.56 | 0.17 | +0.52 | Yahoo Finance Chart API |
| DXY美元指數 | DX-Y.NYB | 101.90 | -0.08 | -0.08 | Yahoo Finance Chart API |
| USD/JPY | JPY=X | 158.46 | 0.66 | +0.42 | Yahoo Finance Chart API |
| USD/KRW | KRW=X | 1,328.48 | -4.95 | -0.37 | Yahoo Finance Chart API |

### 6. 台灣相關ADR

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 收盤／最新值 | 漲跌點 | 漲跌幅 | 資料來源 |
|---|---|---|---|---|---|
| 台積電ADR | TSM | 420.22 | 7.61 | +1.84 | Yahoo Finance Chart API |
| 聯電ADR | UMC | 20.08 | 0.26 | +1.31 | Yahoo Finance Chart API |
| 日月光ADR | ASX | 40.80 | 1.27 | +3.21 | Yahoo Finance Chart API |

### 7. 原油黃金Bitcoin

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 收盤／最新值 | 漲跌點 | 漲跌幅 | 資料來源 |
|---|---|---|---|---|---|
| WTI原油期貨 | CL=F | 98.42 | -5.24 | -5.05 | Yahoo Finance Chart API |
| 黃金期貨 | GC=F | 4,157.50 | -2.60 | -0.06 | Yahoo Finance Chart API |
| Bitcoin | BTC-USD | 81,608.56 | -409.04 | -0.50 | Yahoo Finance Chart API |

### 8. 重大經濟數據、央行事件與重大市場新聞

**資料來源：** 台股 `tw.stock.yahoo.com` (含內文摘要)；國際 `Fed 公告 RSS`＋`CNBC`＋`MarketWatch` (標題、來源、時間與連結)

- 事件1：台積電走跌拖累大盤逾百點 分析師喊季線下是買點
  - 來源：Yahoo 台股；發布時間：2026-10-20T01:21:50Z；台北時間：2026-10-20 09:21
  - 摘要：投資人再度押寶AI帶動企業獲利，逢低買盤挹注美股晶片股反彈，英特爾、超微與輝達聯袂收高，台積電 ADR 也強彈1.84%，但美股漲勢未能激勵台積電台北現股，今（20）日盤中一度挫20元至2,400元，光是台積電一檔就拖累大盤約160點。倫元
  - 原文連結：https://tw.stock.yahoo.com/news/%E5%8F%B0%E7%A9%8D%E9%9B%BB%E6%91%9420%E5%85%83%EF%BC%81%E5%85%89%E4%B8%80%E6%AA%94%E5%B0%B1%E6%8B%96%E7%B4%AF%E5%A4%A7%E7%9B%A4160%E9%BB%9E-%E5%88%86%E6%9E%90%E5%B8%AB%EF%BC%9A%E5%AD%A3%E7%B7%9A%E4%B8%8B%E6%98%AF%E8%B2%B7%E9%BB%9E-012150993.html
- 事件2：杜金龍自曝在2390元買進台積 揭台股止跌3關鍵
  - 來源：Yahoo 台股；發布時間：2026-10-19T20:05:00Z；台北時間：2026-10-20 04:05
  - 摘要：台股19日盤中重挫941點！股市老先覺杜金龍剖析台股止跌三大訊號，揭密外資上看台積電5000元天價，並點名CCL與ABF載板概念股逢低布局策略。(記者唐家興)
  - 原文連結：https://tw.stock.yahoo.com/news/%E5%8F%B0%E8%82%A1%E6%9A%B4%E8%B7%8C%E8%BF%914000%E9%BB%9E-%E6%9D%9C%E9%87%91%E9%BE%8D%E6%9B%9D%E6%AD%A2%E8%B7%8C%E4%B8%89%E8%A8%8A%E8%99%9F-%E9%BB%9E%E5%90%8D-%E9%80%99%E6%AA%94-%E8%B6%8A%E8%B7%8C%E8%B6%8A%E8%B2%B7-200500901.html
- 事件3：晶心科現增破600名額最後倒數 抽中一張估賺10萬
  - 來源：Yahoo 台股；發布時間：2026-10-20T00:25:00Z；台北時間：2026-10-20 08:25
  - 摘要：[FTNN新聞網]記者張書翰／綜合報導CPU矽智財暨嵌入式處理器大廠晶心科（6533）為因應長期發展高階技術之研發支出資金需求，並充實營運資金，近期辦理現金增資...
  - 原文連結：https://tw.stock.yahoo.com/news/%E6%8A%BD%E4%B8%AD%E7%8B%82%E5%82%B310%E8%90%AC%E5%85%83-%E5%B5%8C%E5%85%A5%E5%BC%8F%E7%B3%BB%E7%B5%B1%E5%A4%A7%E5%BB%A0-%E5%A2%9E%E8%B3%87%E4%BB%8A%E6%88%AA%E6%AD%A2-%E7%A0%B4600%E5%90%8D%E9%A1%8D%E6%9C%80%E5%BE%8C%E5%80%92%E6%95%B8-002500577.html
- 事件4：輝達助撐腰 台郡再鎖漲停5天狂衝42%台虹也亮燈
  - 來源：Yahoo 台股；發布時間：2026-10-20T01:40:45Z；台北時間：2026-10-20 09:40
  - 摘要：輝達題材續燒！受惠交換器題材「入列名單」，台灣軟板大廠台郡（6269） 與上游材料廠台虹（8039）近日連連飆漲，昨日雖然出現賣壓，不過今日早盤台郡迅速鎖上漲停，狂吸3萬張以上買單排隊，台虹也大漲一度閃燈。其中，台郡短短五天內就噴漲42.8
  - 原文連結：https://tw.stock.yahoo.com/news/%E8%BC%9D%E9%81%94%E9%A1%8C%E6%9D%90%E6%92%90%E8%85%B0%EF%BC%81%E5%8F%B0%E9%83%A1%E5%86%8D%E9%8E%96%E6%BC%B2%E5%81%9C5%E5%A4%A9%E7%8B%82%E8%A1%9D42-%E5%8F%B0%E8%99%B9%E7%B4%85%E7%87%88%E8%B7%9F%E8%91%97%E9%96%83-014045829.html
- 事件5：大立光6天跌千點、尖點本益比104倍 全列注意股
  - 來源：Yahoo 台股；發布時間：2026-10-19T23:46:00Z；台北時間：2026-10-20 07:46
  - 摘要：[FTNN新聞網]記者張書翰／綜合報導台股加權指數昨（19）日股價一度重挫逾900點，不過後續逐步回穩，最終以46822.08點作收，下跌289.18點、跌幅0.61，成交金額...
  - 原文連結：https://tw.stock.yahoo.com/news/%E8%BF%91%E6%9C%9F%E8%82%A1%E5%83%B9%E8%B7%8C%E8%B7%8C%E4%B8%8D%E4%BC%91-%E5%A4%A7%E7%AB%8B%E5%85%89%E8%88%87%E9%80%99-%E5%85%89%E5%AD%B8%E9%8F%A1%E9%A0%AD%E5%B7%A8%E6%93%98-%E9%81%AD%E5%88%97%E6%B3%A8%E6%84%8F%E8%82%A1-%E5%B0%96%E9%BB%9E%E8%88%87-234600886.html
- 事件6：馬斯克點名太陽能擴張潛力 元晶、聯合再生等台廠卡位
  - 來源：Yahoo 台股；發布時間：2026-10-19T22:39:57Z；台北時間：2026-10-20 06:39
  - 摘要：特斯拉執行長馬斯克勾勒公司未來發展鎖定AI、機器人之際，也點名太陽能與大規模太空運輸具備極高經濟擴張潛力。
  - 原文連結：https://tw.stock.yahoo.com/news/%E9%A6%AC%E6%96%AF%E5%85%8B%E7%99%BC%E6%96%87%E6%8C%BA%E5%A4%AA%E9%99%BD%E8%83%BD-%E5%85%83%E6%99%B6-%E8%81%AF%E5%90%88%E5%86%8D%E7%94%9F%E6%A8%82-223957918.html
- 事件7：Federal Reserve Board announces termination of enforcement actions with Gardner Bancshares, Inc. and Small Business Bank
  - 來源：Federal Reserve；發布時間：Fri, 16 Oct 2026 15:00:00 GMT；台北時間：2026-10-16 23:00
  - 摘要：Federal Reserve Board announces termination of enforcement actions with Gardner Bancshares, Inc. and Small Business Bank
  - 原文連結：https://www.federalreserve.gov/newsevents/pressreleases/enforcement20261016a.htm
- 事件8：Crushed tech stocks bounce — plus, new doctor survey keeps us positive on Lilly
  - 來源：CNBC；發布時間：Mon, 19 Oct 2026 19:13:00 GMT；台北時間：2026-10-20 03:13
  - 摘要：Every weekday, the Investing Club releases the Homestretch; an actionable afternoon update just in time for the last hour of trading.
  - 原文連結：https://www.cnbc.com/investingclub/2026/10/19/crushed-tech-stocks-bounce-new-doctor-survey-keeps-us-positive-on-lilly.html
- 事件9：Indonesian stocks plunge to six-year low as MSCI downgrade fears mount
  - 來源：CNBC；發布時間：Mon, 19 Oct 2026 03:00:33 GMT；台北時間：2026-10-19 11:00
  - 摘要：Indonesia's benchmark stock index plunged to its lowest level in six years.
  - 原文連結：https://www.cnbc.com/2026/10/19/indonesian-stocks-msci-downgrade-fears-mount.html
- 事件10：Micron and other chip stocks spring back to life after bruising selloff
  - 來源：MarketWatch；發布時間：Mon, 19 Oct 2026 21:06:00 GMT；台北時間：2026-10-20 05:06
  - 摘要：It&#x2019;s a key week for tech stocks as Nvidia gears up for a European conference and Meta prepares to report earnings.
  - 原文連結：https://www.marketwatch.com/story/micron-and-other-chip-stocks-spring-back-to-life-after-bruising-selloff-16486541?mod=mw_rss_topstories


## 三、期貨

**資料來源：**
1. Cloudflare Workers：TAIFEX Proxy — https://taifex.grichtoyang.workers.dev/
2. TAIFEX Open API — https://openapi.taifex.com.tw/

近月契約月份：202610 (日盤成交量最大者)；交易日期：2026-10-19

### 1．台指期近月日盤行情

| 項目 | 數值 | 資料來源 |
|---|---|---|
| 開盤價 | 46,627 | TAIFEX Proxy |
| 最高價 | 46,902 | TAIFEX Proxy |
| 最低價 | 46,390 | TAIFEX Proxy |
| 收盤價 | 46,779 | TAIFEX Proxy |
| 漲跌點數 | -505 | TAIFEX Proxy |
| 漲跌幅 | -1.07 | TAIFEX Proxy |
| 成交量 | 142,874 | TAIFEX Proxy |
| 日盤高點及低點 | 46,902 / 46,390 | TAIFEX Proxy |

### 2．台指期近月夜盤行情

| 項目 | 數值 | 資料來源 |
|---|---|---|
| 開盤價 | 46,842 | TAIFEX Proxy |
| 最高價 | 47,033 | TAIFEX Proxy |
| 最低價 | 46,497 | TAIFEX Proxy |
| 收盤價 | 46,691 | TAIFEX Proxy |
| 漲跌點數 | -78 | TAIFEX Proxy |
| 漲跌幅 | -0.17 | TAIFEX Proxy |
| 成交量 | 26,868 | TAIFEX Proxy |
| 夜盤高點及低點 | 47,033 / 46,497 | TAIFEX Proxy |
| 結算價 | unavailable | TAIFEX Proxy |
| 未平倉量 | unavailable | TAIFEX Proxy |

### 3．法人台指期多空未平倉部位

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 外資多方 OI | 11,962 | TAIFEX Proxy |
| 外資空方 OI | 103,107 | TAIFEX Proxy |
| 外資多空淨 OI | -91,145 | TAIFEX Proxy |
| 投信多方 OI | 86,878 | TAIFEX Proxy |
| 投信空方 OI | 2,778 | TAIFEX Proxy |
| 投信多空淨 OI | +84,100 | TAIFEX Proxy |
| 自營商多方 OI | 7,200 | TAIFEX Proxy |
| 自營商空方 OI | 4,371 | TAIFEX Proxy |
| 自營商多空淨 OI | +2,829 | TAIFEX Proxy |
| 三大法人合計多方 OI | 106,040 | TAIFEX Proxy |
| 三大法人合計空方 OI | 110,256 | TAIFEX Proxy |
| 三大法人合計多空淨 OI | -4,216 | TAIFEX Proxy |
| 外資多空淨 OI 變化 | +2,530 | TAIFEX Proxy |
| 投信多空淨 OI 變化 | +1,636 | TAIFEX Proxy |
| 自營商多空淨 OI 變化 | -368 | TAIFEX Proxy |

### 4．前十大交易人多空未平倉部位

**資料來源：** `TAIFEX OpenAPI OpenInterestOfLargeTradersFutures` (官方資料落後約一日，標示實際日期)

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 前十大交易人多方 OI | 40,132 | TAIFEX Proxy |
| 前十大交易人空方 OI | 41,382 | TAIFEX Proxy |
| 前十大交易人多空淨 OI | -1,250 | TAIFEX Proxy |
| 多空淨 OI 變化 (2026-10-14→2026-10-19) | -5,321 | TAIFEX Proxy snapshots (2026-10-15) |
- 資料日期：2026-10-19 (TypeOfTraders=0 全部交易人；契約月份 202610)

### 5．日盤、夜盤法人交易資料

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 外資日盤多單交易量 | 101,671 | TAIFEX Proxy |
| 外資日盤空單交易量 | 99,130 | TAIFEX Proxy |
| 外資日盤多空淨交易量 | +2,541 | TAIFEX Proxy |
| 外資夜盤多單交易量 | 15,798 | TAIFEX Proxy |
| 外資夜盤空單交易量 | 15,848 | TAIFEX Proxy |
| 外資夜盤多空淨交易量 | -50 | TAIFEX Proxy |
| 外資日盤／夜盤交易量變化 | +2,591 | TAIFEX Proxy |
| 投信日盤多空淨交易量 | +1,576 | TAIFEX Proxy |
| 投信夜盤多空淨交易量 | +0 | TAIFEX Proxy |
| 投信日盤／夜盤交易量變化 | +1,576 | TAIFEX Proxy |
| 自營商日盤多空淨交易量 | -197 | TAIFEX Proxy |
| 自營商夜盤多空淨交易量 | +210 | TAIFEX Proxy |
| 自營商日盤／夜盤交易量變化 | -407 | TAIFEX Proxy |
| 三大法人日盤多空淨交易量 | +3,920 | TAIFEX Proxy |
| 三大法人夜盤多空淨交易量 | +160 | TAIFEX Proxy |
| 法人日盤交易金額淨額 (億元) | +367.1 | TAIFEX Proxy |
| 法人夜盤交易金額淨額 (億元) | +14.7 | TAIFEX Proxy |

### 6．期貨與現貨關係

| 項目 | 數值 | 資料來源 |
|---|---|---|
| 台指期近月價格 | 46,779 | TAIFEX Proxy |
| 加權指數價格 | 46,822.08 | twse-proxy |
| 台指期與加權指數價差 | -43.08 | TAIFEX Proxy+twse-proxy |
| 價差百分比 | -0.09 | TAIFEX Proxy+twse-proxy |
| 日盤基差 | -43.08 | TAIFEX Proxy+twse-proxy |
| 夜盤價格相對日盤收盤的變化 | -88 | TAIFEX Proxy |

### 7．日盤、夜盤與籌碼變化對照

#### 7.1 日夜盤價格與成交量對照 (變化 = 日盤 - 夜盤)

| 項目 | 日盤 | 夜盤 | 變化 (日-夜) | 資料來源 |
|---|---|---|---|---|
| 收盤價 | 46,779 | 46,691 | +88 | TAIFEX Proxy |
| 成交量 | 101,828 | 26,868 | +74,960 | TAIFEX Proxy |
- 台指期總 OI 前日變化：+3,798（來源：TAIFEX Proxy）


#### 7.2 法人籌碼日夜盤對照 (淨變化 = 日盤淨 - 夜盤淨；OI 為日盤收盤後總量，前日變化另列)

| 法人 | 交易量 |  |  |  |  |  |  | 未平倉量 |  |  |  | 資料來源 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|  | **日盤多單** | **日盤空單** | **日盤淨** | **夜盤多單** | **夜盤空單** | **夜盤淨** | **淨變化 (日-夜)** | **OI多方** | **OI空方** | **OI淨** | **OI前日變化** |  |
| 外資 | 101,671 | 99,130 | +2,541 | 15,798 | 15,848 | -50 | +2,591 | 11,962 | 103,107 | -91,145 | +2,530 | TAIFEX Proxy |
| 投信 | 42,112 | 40,536 | +1,576 | 0 | 0 | +0 | +1,576 | 86,878 | 2,778 | +84,100 | +1,636 | TAIFEX Proxy |
| 自營商 | 12,961 | 13,158 | -197 | 1,474 | 1,264 | +210 | -407 | 7,200 | 4,371 | +2,829 | -368 | TAIFEX Proxy |
| 三大法人合計 | 156,744 | 152,824 | +3,920 | 17,272 | 17,112 | +160 | +3,760 | 106,040 | 110,256 | -4,216 | +3,798 | TAIFEX Proxy |

#### 7.3 前十大交易人日夜盤對照 (OI 無日夜拆分，列收盤後總量)

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 前十大交易人多方 OI | 40,132 | TAIFEX Proxy |
| 前十大交易人空方 OI | 41,382 | TAIFEX Proxy |
| 前十大交易人多空淨 OI | -1,250 | TAIFEX Proxy |
| 前十大交易人多空淨 OI 變化 (2026-10-14→2026-10-19) | -5,321 | TAIFEX Proxy snapshots (2026-10-15) |

#### 7.4 夜盤劇本分類 (規則對應：夜盤漲跌 × 外資夜盤偏多空)

| 項目 | 數值 | 資料來源 |
|---|---|---|
| 夜盤成交量占比 (夜盤量／(夜盤量＋日盤量)) | 20.88% | TAIFEX Proxy |
| 夜盤漲跌點數 | -78 | TAIFEX Proxy |
| 外資夜盤多空淨交易量 | -50 | TAIFEX Proxy |
| 劇本分類 | 劇本三 | 規則對應 |
| 劇本條件 | 夜盤下跌＋外資偏空 | 規則對應 |
| 劇本特徵 | 開低、續跌機率高 | 規則對應 |

## 四、選擇權

**資料來源：** 主要 TAIFEX 經 Cloudflare Worker Proxy；時區 `Asia/Taipei`

### 1．選擇權交易日期、到期日與資料時間

| 項目 | 數值 | 資料來源 |
|---|---|---|
| 交易日期 | 2026-10-19 | TAIFEX Proxy |
| 到期月份／到期日 | 202610 | TAIFEX Proxy |
| 資料更新時間 | 2026-10-20 10:34:21 | 本機 |
| 日盤／夜盤標記 | 日盤收盤後資料 | TAIFEX Proxy |

### 2．Call 總成交量、OI、OI 增減

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Call 總成交量 | 182,637 | TAIFEX Proxy |
| Call 總未平倉量 OI | 93,892 | TAIFEX Proxy |
| Call OI 增減 | unavailable | 端點未提供 |

### 3．Put 總成交量、OI、OI 增減

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Put 總成交量 | 176,987 | TAIFEX Proxy |
| Put 總未平倉量 OI | 55,248 | TAIFEX Proxy |
| Put OI 增減 | unavailable | 端點未提供 |

### 4．Call／Put 比例與變化

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Call／Put 成交量比例 | 1.03 | TAIFEX Proxy |
| Call／Put 未平倉量比例 | 1.70 | TAIFEX Proxy |
| Put／Call Ratio | 0.59 | TAIFEX Proxy |
| Call／Put 比例變化 (量比 2026-10-16→2026-10-19) | 5.79 | TAIFEX Proxy |
| 與前一交易日比較 (OI 比 2026-10-16→2026-10-19) | -6.00 | TAIFEX Proxy |
**資料來源：** 比例 `TAIFEX Proxy chain`；變化 `TAIFEX Proxy PutCallRatio`

### 5．外資 Call／Put 部位

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 外資 Call日買 | 51,524 | TAIFEX Proxy |
| 外資 Call日賣 | 49,998 | TAIFEX Proxy |
| 外資 Call日淨 | +1,526 | TAIFEX Proxy |
| 外資 Put日買 | 66,117 | TAIFEX Proxy |
| 外資 Put日賣 | 65,207 | TAIFEX Proxy |
| 外資 Put日淨 | +910 | TAIFEX Proxy |
| 外資 Call夜買 | 26,047 | TAIFEX Proxy |
| 外資 Call夜賣 | 25,804 | TAIFEX Proxy |
| 外資 Call夜淨 | +243 | TAIFEX Proxy |
| 外資 Put夜買 | 44,272 | TAIFEX Proxy |
| 外資 Put夜賣 | 44,228 | TAIFEX Proxy |
| 外資 Put夜淨 | +44 | TAIFEX Proxy |
| 外資 日盤淨總量 | +616 | TAIFEX Proxy |
| 外資 Call日夜淨增減 (日－夜) | +1,283 | TAIFEX Proxy |
| 外資 Put日夜淨增減 (日－夜) | +866 | TAIFEX Proxy |

### 6．自營商 Call／Put 部位

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 自營商 Call日買 | 56,571 | TAIFEX Proxy |
| 自營商 Call日賣 | 52,550 | TAIFEX Proxy |
| 自營商 Call日淨 | +4,021 | TAIFEX Proxy |
| 自營商 Put日買 | 51,580 | TAIFEX Proxy |
| 自營商 Put日賣 | 51,005 | TAIFEX Proxy |
| 自營商 Put日淨 | +575 | TAIFEX Proxy |
| 自營商 Call夜買 | 10,608 | TAIFEX Proxy |
| 自營商 Call夜賣 | 12,147 | TAIFEX Proxy |
| 自營商 Call夜淨 | -1,539 | TAIFEX Proxy |
| 自營商 Put夜買 | 22,511 | TAIFEX Proxy |
| 自營商 Put夜賣 | 22,474 | TAIFEX Proxy |
| 自營商 Put夜淨 | +37 | TAIFEX Proxy |
| 自營商 日盤淨總量 | +3,446 | TAIFEX Proxy |
| 自營商 Call日夜淨增減 (日－夜) | +5,560 | TAIFEX Proxy |
| 自營商 Put日夜淨增減 (日－夜) | +538 | TAIFEX Proxy |

### 7．主要 Call OI 集中區

| 項目 | 履約價 | OI | 資料來源 |
|---|---|---|---|
| Call OI 第1大履約價 | 49,500 | 6,136 | TAIFEX Proxy |
| Call OI 第2大履約價 | 54,000 | 5,735 | TAIFEX Proxy |
| Call OI 第3大履約價 | 52,000 | 5,172 | TAIFEX Proxy |
| Call OI 最大履約價 | 49,500 | 6,136 | TAIFEX Proxy |

#### Call OI 分布明細 Top10 (機器可讀，到期月份 202610)

| # | 履約價 | OI | 佔比 | 資料來源 |
|---|---|---|---|---|
| C1 | 49,500 | 6,136 | 6.54% | TAIFEX Proxy |
| C2 | 54,000 | 5,735 | 6.11% | TAIFEX Proxy |
| C3 | 52,000 | 5,172 | 5.51% | TAIFEX Proxy |
| C4 | 48,000 | 3,707 | 3.95% | TAIFEX Proxy |
| C5 | 53,000 | 2,511 | 2.67% | TAIFEX Proxy |
| C6 | 50,000 | 2,410 | 2.57% | TAIFEX Proxy |
| C7 | 47,000 | 2,291 | 2.44% | TAIFEX Proxy |
| C8 | 48,500 | 2,132 | 2.27% | TAIFEX Proxy |
| C9 | 49,000 | 1,898 | 2.02% | TAIFEX Proxy |
| C10 | 48,300 | 1,673 | 1.78% | TAIFEX Proxy |


### 8．主要 Put OI 集中區

| 項目 | 履約價 | OI | 資料來源 |
|---|---|---|---|
| Put OI 第1大履約價 | 45,000 | 4,210 | TAIFEX Proxy |
| Put OI 第2大履約價 | 46,000 | 3,606 | TAIFEX Proxy |
| Put OI 第3大履約價 | 44,500 | 1,772 | TAIFEX Proxy |
| Put OI 最大履約價 | 45,000 | 4,210 | TAIFEX Proxy |

#### Put OI 分布明細 Top10 (機器可讀，到期月份 202610)

| # | 履約價 | OI | 佔比 | 資料來源 |
|---|---|---|---|---|
| P1 | 45,000 | 4,210 | 7.62% | TAIFEX Proxy |
| P2 | 46,000 | 3,606 | 6.53% | TAIFEX Proxy |
| P3 | 44,500 | 1,772 | 3.21% | TAIFEX Proxy |
| P4 | 44,000 | 1,749 | 3.17% | TAIFEX Proxy |
| P5 | 46,500 | 1,644 | 2.98% | TAIFEX Proxy |
| P6 | 47,000 | 1,568 | 2.84% | TAIFEX Proxy |
| P7 | 45,500 | 1,274 | 2.31% | TAIFEX Proxy |
| P8 | 40,000 | 1,262 | 2.28% | TAIFEX Proxy |
| P9 | 43,000 | 1,096 | 1.98% | TAIFEX Proxy |
| P10 | 44,200 | 1,055 | 1.91% | TAIFEX Proxy |


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
| Call Wall 價位 | 49,500 | TAIFEX Proxy |
| 對應到期月份 | 202610 | TAIFEX Proxy |
| 與前一交易日的變化 | unavailable | 端點未提供 |

### 12．Put Wall

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Put Wall 價位 | 45,000 | TAIFEX Proxy |
| 對應到期月份 | 202610 | TAIFEX Proxy |
| 與前一交易日的變化 | unavailable | 端點未提供 |

### 13．Gamma Wall

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Gamma Wall 價位 | 48,000.00 | TAIFEX Proxy (options-market-structure-compact (proxy)) |
| 對應到期月份 | 202610 | TAIFEX Proxy |
| 資料日期 | 2026-10-19 | TAIFEX Proxy (options-market-structure-compact (proxy)) |

### 14．Gamma Flip

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Gamma Flip 價位 | 46,487.74 | TAIFEX Proxy (options-market-structure-compact (proxy)) |
| 對應到期月份 | 202610 | TAIFEX Proxy |
| 資料日期 | 2026-10-19 | TAIFEX Proxy (options-market-structure-compact (proxy)) |

### 15．Max Pain

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Max Pain 價位 | 46,500 | TAIFEX Proxy |
| 對應到期月份 | 202610 | TAIFEX Proxy |
| 與前一交易日的變化 | unavailable | 端點未提供 |

### 17．選擇權法人日盤、夜盤交易

| 法人 | 日盤多單 | 日盤空單 | 日盤淨 | 夜盤多單 | 夜盤空單 | 夜盤淨 | 淨變化 (日-夜) | 資料來源 |
|---|---|---|---|---|---|---|---|---|
| 外資 | 116,731 | 116,115 | +616 | 70,275 | 70,076 | +199 | +417 | TAIFEX Proxy |
| 投信 | 40 | 3,100 | -3,060 | 3 | 0 | +3 | -3,063 | TAIFEX Proxy |
| 自營商 | 107,576 | 104,130 | +3,446 | 33,082 | 34,658 | -1,576 | +5,022 | TAIFEX Proxy |
| 三大法人合計 | 224,347 | 223,345 | +1,002 | 103,360 | 104,734 | -1,374 | +2,376 | TAIFEX Proxy |
- 方法論：多方＝買Call＋賣Put（看多），空方＝賣Call＋買Put（看空），淨額＝看多－看空（已用 Call／Put 拆分頁交叉驗算一致）
- 公式：多方(買)－空方(賣)＝（買call＋賣put）－（賣call＋買put）＝看多－看空
- 速記：多＝BC＋SP、空＝SC＋BP

#### 法人多空力道表（金額・億元；上游千元／1e5）

| 法人 | 日多方力道 | 日空方力道 | 日淨多空力道 | 夜多方力道 | 夜空方力道 | 夜淨多空力道 | 日淨－夜淨 | 資料來源 |
|---|---|---|---|---|---|---|---|---|
| 外資 | 13.52 | 13.28 | +0.24 | 6.70 | 6.73 | -0.03 | +0.26 | TAIFEX Proxy |
| 投信 | 0.00 | 2.76 | -2.76 | 0.00 | 0.00 | +0.00 | -2.76 | TAIFEX Proxy |
| 自營商 | 12.10 | 10.51 | +1.59 | 3.15 | 3.13 | +0.02 | +1.57 | TAIFEX Proxy |
| 三大法人合計 | 25.62 | 26.55 | -0.93 | 9.86 | 9.87 | -0.01 | -0.92 | TAIFEX Proxy |

### 18．選擇權前十大

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 買權多方 OI | 47,479 | TAIFEX Proxy |
| 買權空方 OI | 58,250 | TAIFEX Proxy |
| 買權多空淨 OI | -10,771 | TAIFEX Proxy |
| 買權多空淨 OI 變化 (2026-10-14→2026-10-19) | -11,768 | TAIFEX Proxy snapshots (2026-10-15) |

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 賣權多方 OI | 22,782 | TAIFEX Proxy |
| 賣權空方 OI | 19,527 | TAIFEX Proxy |
| 賣權多空淨 OI | +3,255 | TAIFEX Proxy |
| 賣權多空淨 OI 變化 (2026-10-14→2026-10-19) | +2,412 | TAIFEX Proxy snapshots (2026-10-15) |
- 資料日期：買權 2026-10-19／賣權 2026-10-19 (TypeOfTraders=0 全部交易人；契約月份 202610)

#### 大戶流向（全日；前十大無日夜拆分）

| 項目 | 淨變化 | 區間 | 資料來源 |
|---|---|---|---|
| 期貨前十大 | -5,321 | 2026-10-14→2026-10-19 | TAIFEX Proxy snapshots (2026-10-15) |
| 買權前十大 | -11,768 | 2026-10-14→2026-10-19 | TAIFEX Proxy snapshots (2026-10-15) |
| 賣權前十大 | +2,412 | 2026-10-14→2026-10-19 | TAIFEX Proxy snapshots (2026-10-15) |

### 16．資料來源、時間、時區與狀態

- 資料來源：TAIFEX 經 Cloudflare Worker Proxy
- 資料日期：2026-10-19；資料時間：2026-10-20 10:34:21；時區：`Asia/Taipei`
- 日盤／夜盤標記：日盤收盤後 + 夜盤盤後
- 未取得欄位 (2)：options.chain_oi_change, options.wall_change
- 註記：futures-price-after-hours 日期 2026-10-19 非今日 2026-10-20，視為無新節次，不採用
- 註記：法人交易量變化無昨日交易端點，標 unavailable
- 註記：跨到期換月（舊202610F3→新202610），日對日 OI/Walls 變化不適用

## 五、資料來源、時間與完整性

- 期貨/匯率為最新報價，其餘為 T0 收盤資料；時間皆為 `Asia/Taipei`。
- taiex：`twse-proxy`
- taiex_ohlc：`FinMind TaiwanStockPrice TAIEX`
- listed_turnover：`twse-proxy market_statistics`
- listed_breadth：`twse-proxy`
- otc：`TPEX OpenAPI tpex_mainborad_highlight`
- institutional：`twse-proxy /institutional`
- margin：`HiStock 上市+上櫃融資融券 (金額口徑)`
- margin_ratio：`前值遞補 (DATA 2026-10-16；當日三源皆失敗；民間估算；官方無每日序列)`
- sbl：`TWSE TWT93U + TPEX margin_sbl`
- 期貨選擇權：`TAIFEX Proxy`
- 新聞：台股 Yahoo／國際 Fed＋CNBC＋MarketWatch；台股 Yahoo（不足時財訊快報備援）/ 國際 Fed 公告＋CNBC＋MarketWatch RSS；Fed 無摘要；investing 港股為主已退役；cnyes CSR、wantgoo JS 算繪、中央社/台灣央行路徑待查，未採用
- 美股/亞股/期貨/匯率/ADR/商品：`Yahoo Finance Chart API`；美債：`Yahoo Finance (備援)`
- 註記：融資維持率未取得 (三源皆失敗；官方無每日序列)
- 註記：融資維持率採前值遞補 (DATA 2026-10-16)，非 T0 2026-10-19
- 註記：上市 MI_MARGN / TWT96U 無日期欄，採用最新可得
- 註記：借券賣出增減僅上櫃值 (TWSE TWT93U 未取得)
- 本報告僅整理資料，不提供交易判斷。

## 六、期現選方向對照

**規則：** 趨勢偏多／空＝現貨、期貨OI、選擇權日淨三者同向；避險／對沖＝現貨與期選反向；日內反轉＝日淨與夜淨反向；缺值標示，不推估。選擇權多空為看多看空口徑。

| 法人 | 現貨買賣超(億) | 期貨OI淨(口) | 期貨日淨 | 期貨夜淨 | 選擇權日淨 | 選擇權夜淨 | 判定 | 期選組合 | 資料來源 |
|---|---|---|---|---|---|---|---|---|---|
| 外資 | -767.4 | -91,145 | +2,541 | -50 | +616 | +199 | 避險／對沖 | 對沖避險 | twse-proxy／TAIFEX Proxy |
| 投信 | +241.4 | +84,100 | +1,576 | +0 | -3,060 | +3 | 避險／對沖 | 分歧 | twse-proxy／TAIFEX Proxy |
| 自營商 | -362.6 | +2,829 | -197 | +210 | +3,446 | -1,576 | 避險／對沖 | 趨勢偏多 | twse-proxy／TAIFEX Proxy |
