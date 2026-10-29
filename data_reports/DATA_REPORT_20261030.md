# DATA_REPORT_20261030

- 報告日期：`2026-10-30`
- T0 交易日期：`2026-10-30`
- 資料產出時間：`2026-10-30 01:17:35`
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
| 加權指數 | 47,035.58 | 點 | TWSE OpenAPI MI_INDEX (備援) |
| 開盤 | unavailable | 點 | FinMind |
| 最高 | unavailable | 點 | FinMind |
| 最低 | unavailable | 點 | FinMind |
| 收盤 | 47,035.58 | 點 | TWSE OpenAPI MI_INDEX (備援) |
| 漲跌點數 | 939.35 | 點 | TWSE OpenAPI MI_INDEX (備援) |
| 漲跌幅 | +2.04 | % | TWSE OpenAPI MI_INDEX (備援) |
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
| 外資 | -688.2 | 億元 | twse-proxy /institutional |
| 投信 | +70.4 | 億元 | twse-proxy /institutional |
| 自營商 | -215.0 | 億元 | twse-proxy /institutional |
| 三大法人合計 | -832.7 | 億元 | twse-proxy /institutional |

### 4. 融資融券

**資料來源：** 上市+上櫃 `HiStock` (金額口徑)；維持率 `istock.tw`；備援官方逐股加總

| 項目 | 數值 | 單位 | 資料來源 |
|---|---|---|---|
| 融資餘額 | unavailable | 億元 | HiStock |
| 融資增減 | unavailable | 億元 | HiStock |
| 融券餘額 | 193,040 | 張 | HiStock |
| 融券增減 | -7,645 | 張 | HiStock |
| 融資維持率 | 183.30 | % | 前值遞補 (DATA 2026-10-28；當日三源皆失敗；民間估算；官方無每日序列) |

### 5. 借券資料

**資料來源：** 上市 `TWSE OpenAPI TWT96U` (可借餘額)、上櫃 `TPEX OpenAPI tpex_margin_sbl`

| 項目 | 數值 | 單位 | 資料來源 |
|---|---|---|---|
| 借券餘額 | 2,477,010 | 張 | TWSE TWT93U + TPEX margin_sbl |
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
| S&P 500 | ^GSPC | 7,708.89 | -35.09 | -0.45 | Yahoo Finance Chart API |
| Nasdaq Composite | ^IXIC | 26,160.79 | -389.05 | -1.47 | Yahoo Finance Chart API |
| Nasdaq 100 | ^NDX | 29,351.40 | -461.76 | -1.55 | Yahoo Finance Chart API |
| Dow Jones | ^DJI | 52,271.69 | -203.41 | -0.39 | Yahoo Finance Chart API |
| 費城半導體 SOX | ^SOX | 11,496.72 | -187.28 | -1.60 | Yahoo Finance Chart API |
| VIX | ^VIX | 16.22 | -0.69 | -4.08 | Yahoo Finance Chart API |

### 2. 亞洲主要指數

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 收盤／最新值 | 漲跌點 | 漲跌幅 | 資料來源 |
|---|---|---|---|---|---|
| 日經225 | ^N225 | 63,954.19 | 685.82 | +1.08 | Yahoo Finance Chart API |
| 韓國KOSPI | ^KS11 | 6,012.44 | 374.10 | +6.63 | Yahoo Finance Chart API |
| 香港恆生 | ^HSI | 23,094.83 | 53.51 | +0.23 | Yahoo Finance Chart API |
| 上海綜合 | 000001.SS | 3,681.47 | 33.17 | +0.91 | Yahoo Finance Chart API |
| 深圳成分 | 399001.SZ | 11,473.18 | 227.45 | +2.02 | Yahoo Finance Chart API |

### 3. 美股指數期貨

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 最新值 | 漲跌點 | 漲跌幅 | 資料來源 |
|---|---|---|---|---|---|
| S&P500期貨 | ES=F | 7,749.25 | -34.00 | -0.44 | Yahoo Finance Chart API |
| Nasdaq100期貨 | NQ=F | 29,546.50 | -433.00 | -1.44 | Yahoo Finance Chart API |
| 道瓊期貨 | YM=F | 52,457.00 | -239.00 | -0.45 | Yahoo Finance Chart API |
| Russell2000期貨 | RTY=F | 2,870.90 | 31.40 | +1.11 | Yahoo Finance Chart API |

### 4. 美國國債殖利率

**資料來源：** `U.S. Treasury Fiscal Data API` (失敗時備援 Treasury yield.xml 與 `Yahoo Finance`)

| 項目 | API 資料欄位／識別 | 殖利率 | 日變化 | 資料來源 |
|---|---|---|---|---|
| 美國 2 年期殖利率 | 2 Yr | 4.67 | -0.03 | U.S. Treasury yield.xml (網頁備援) |
| 美國 10 年期殖利率 | 10 Yr | 5.00 | -0.05 | Yahoo Finance (備援) |
| 美國 30 年期殖利率 | 30 Yr | 5.34 | -0.02 | Yahoo Finance (備援) |

### 5. 主要匯率

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 最新值 | 漲跌點 | 漲跌幅 | 資料來源 |
|---|---|---|---|---|---|
| USD/TWD | TWD=X | 32.54 | 0.12 | +0.37 | Yahoo Finance Chart API |
| DXY美元指數 | DX-Y.NYB | 101.98 | -0.21 | -0.20 | Yahoo Finance Chart API |
| USD/JPY | JPY=X | 157.89 | -0.10 | -0.06 | Yahoo Finance Chart API |
| USD/KRW | KRW=X | 1,338.84 | 12.03 | +0.91 | Yahoo Finance Chart API |

### 6. 台灣相關ADR

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 收盤／最新值 | 漲跌點 | 漲跌幅 | 資料來源 |
|---|---|---|---|---|---|
| 台積電ADR | TSM | 431.48 | -8.03 | -1.83 | Yahoo Finance Chart API |
| 聯電ADR | UMC | 17.98 | -0.84 | -4.46 | Yahoo Finance Chart API |
| 日月光ADR | ASX | 43.74 | -0.18 | -0.41 | Yahoo Finance Chart API |

### 7. 原油黃金Bitcoin

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 收盤／最新值 | 漲跌點 | 漲跌幅 | 資料來源 |
|---|---|---|---|---|---|
| WTI原油期貨 | CL=F | 101.74 | -1.04 | -1.01 | Yahoo Finance Chart API |
| 黃金期貨 | GC=F | 4,033.50 | -18.10 | -0.45 | Yahoo Finance Chart API |
| Bitcoin | BTC-USD | 80,939.94 | -327.65 | -0.40 | Yahoo Finance Chart API |

### 8. 重大經濟數據、央行事件與重大市場新聞

**資料來源：** 台股 `tw.stock.yahoo.com` (含內文摘要)；國際 `Fed 公告 RSS`＋`CNBC`＋`MarketWatch` (標題、來源、時間與連結)

- 事件1：台股季線失守成交榜綠油油 智原穩懋逆勢飛
  - 來源：Yahoo 台股；發布時間：2026-10-29T09:05:39Z；台北時間：2026-10-29 17:05
  - 摘要：AI疑慮再起、電子股倒一片，台股下挫667點再失季線！今(29)日加權指數終場下跌667.25點、跌幅1.42%，收46,368.33點，成交金額7,904.13億元。Google母公司Alphabet盤後財報表現不如預期，再度引發市場對A
  - 原文連結：https://tw.stock.yahoo.com/news/google%E8%B2%A1%E5%A0%B1%E5%88%A9%E7%A9%BA%E8%A1%9D%E6%93%8A%E5%8F%B0%E8%82%A1%E9%87%8D%E6%8C%AB667%E9%BB%9E%E5%86%8D%E5%A4%B1%E5%AD%A3%E7%B7%9A%EF%BC%81%E8%81%AF%E9%9B%BB%E6%B3%95%E8%AA%AA%E6%9C%83%E8%AE%8A%E6%B3%95%E6%9C%83-%E6%99%BA%E5%8E%9F%E7%A9%A9%E6%87%8B%E9%80%A3%E5%85%A9%E6%A0%B9%E6%BC%B2%E5%81%9C%E9%80%86%E5%8B%A2%E9%AB%98%E9%A3%9B%EF%BD%9Cyahoo%E8%B2%A1%E7%B6%93%E6%8E%83%E6%8F%8F-090539133.html
- 事件2：友達本業未回春AI事業待驗證 分析師看短線承壓
  - 來源：Yahoo 台股；發布時間：2026-10-29T09:57:30Z；台北時間：2026-10-29 17:57
  - 摘要：面板大廠友達（2409）今（29）日舉行法說會，第三季虧損25億元，第四季面板營收預估持續下滑，不過，同日也宣布以388億元出售廠房給台積電（2330），加上積極布局AI眼鏡、先進封裝等新事業，利多與利空消息交雜。明（30）日股價表現如何？
  - 原文連結：https://tw.stock.yahoo.com/news/%E5%8F%8B%E9%81%94%E6%B3%95%E8%AA%AA%E8%AB%87ai%E8%BD%89%E5%9E%8B-%E7%B6%B2%E5%96%8A%E3%80%8C%E9%82%84%E6%98%AF%E8%A6%81%E7%9B%B8%E4%BF%A1%E8%80%81%E5%AF%A6%E6%A8%B9%E3%80%8D%E5%88%86%E6%9E%90%E5%B8%AB%E7%9C%8B%E6%98%8E%E6%97%A5%E8%82%A1%E5%83%B9%E6%81%90%E6%89%BF%E5%A3%93-103457573.html
- 事件3：台灣IC設計變差？陳冠州揭聯發科比5年前強太多
  - 來源：Yahoo 台股；發布時間：2026-10-29T10:01:17Z；台北時間：2026-10-29 18:01
  - 摘要：台灣半導體產業協會（TSIA）今（29）日舉辦30周年年會論壇，台積電、聯發科、日月光與鈺創等業界巨頭齊聚，針對台灣半導體前景展開深度對談。鈺創董事長盧超群坦言憂心台灣 IC 設計與微系統能力逐漸退步，無法掌握 AI 資料中心關鍵趨勢，聯發
  - 原文連結：https://tw.stock.yahoo.com/news/%E5%8F%B0%E7%81%A3ic%E8%A8%AD%E8%A8%88%E8%AE%8A%E5%B7%AE%EF%BC%9F%E8%81%AF%E7%99%BC%E7%A7%91%E9%99%B3%E5%86%A0%E5%B7%9E%E9%A7%81%E6%96%A5%EF%BC%9A%E6%88%91%E5%80%91%E6%AF%945%E5%B9%B4%E5%89%8D%E5%BC%B7%E5%A4%AA%E5%A4%9A-100117616.html
- 事件4：銀行券商跨查信用將上路 金管會強調客戶不同意不能查
  - 來源：Yahoo 台股；發布時間：2026-10-29T09:53:09Z；台北時間：2026-10-29 17:53
  - 摘要：四貸同堂金管會出手！券商借錢大戶金額破3億元或占券商淨值1%以上，10月底可跨業查詢其銀行聯徵信用！金管會今（29）日證實新制31日正式上路，證期局副局長黃厚銘說，灰名單需經券商客戶同意才能提供，不能強制需合宜，但若客戶不同意，券商基於風險
  - 原文連結：https://tw.stock.yahoo.com/news/%E5%9B%9B%E8%B2%B8%E5%90%8C%E5%A0%82%E9%87%91%E7%AE%A1%E6%9C%83%E5%87%BA%E6%89%8B%EF%BC%81%E5%88%B8%E5%95%86%E5%80%9F%E9%8C%A2%E5%A4%A7%E6%88%B6%E7%A0%B43%E5%84%84%E5%85%83-10%E6%9C%88%E5%BA%95%E5%8F%AF%E8%B7%A8%E6%A5%AD%E6%9F%A5%E9%8A%80%E8%A1%8C%E8%81%AF%E5%BE%B5%E4%BF%A1%E7%94%A8-095309952.html
- 事件5：龔明鑫變飆股老師是假的 經濟部示警遭冒名已報案
  - 來源：Yahoo 台股；發布時間：2026-10-29T09:45:44Z；台北時間：2026-10-29 17:45
  - 摘要：[NOWNEWS今日新聞]經濟部長龔明鑫教你投資、買飆股？繼央行總裁楊金龍上週被冒名開設Threads帳號，經濟部今（29）日表示，近期網路出現冒用新聞媒體及經濟部長名義的假訊息，利用AI技術製作部長...
  - 原文連結：https://tw.stock.yahoo.com/news/%E9%BE%94%E6%98%8E%E9%91%AB%E6%95%99%E4%BD%A0%E8%B2%B7%E9%A3%86%E8%82%A1-%E7%B6%93%E6%BF%9F%E9%83%A8-%E9%81%AD%E5%86%92%E5%90%8D%E5%B7%B2%E5%A0%B1%E6%A1%88-094544709.html
- 事件6：台灣首檔美國金礦ETF登場！009832掛牌首日逆勢上漲　成交突破2萬張
  - 來源：Yahoo 台股；發布時間：2026-10-29T13:45:00Z；台北時間：2026-10-29 21:45
  - 摘要：[FTNN新聞網]實習記者藍彥欣／台北報導金價屢創新高，投資黃金除了買現貨或黃金ETF再添全新選擇。台灣首檔聚焦美國黃金礦業的ETF，兆豐美國黃金礦業（009832...
  - 原文連結：https://tw.stock.yahoo.com/news/%E5%8F%B0%E7%81%A3%E9%A6%96%E6%AA%94%E7%BE%8E%E5%9C%8B%E9%87%91%E7%A4%A6etf%E7%99%BB%E5%A0%B4-009832%E6%8E%9B%E7%89%8C%E9%A6%96%E6%97%A5%E9%80%86%E5%8B%A2%E4%B8%8A%E6%BC%B2-%E6%88%90%E4%BA%A4%E7%AA%81%E7%A0%B42%E8%90%AC%E5%BC%B5-134500249.html
- 事件7：Federal Reserve issues FOMC statement
  - 來源：Federal Reserve；發布時間：Wed, 28 Oct 2026 18:00:00 GMT；台北時間：2026-10-29 02:00
  - 摘要：Federal Reserve issues FOMC statement
  - 原文連結：https://www.federalreserve.gov/newsevents/pressreleases/monetary20261028a.htm
- 事件8：Third-quarter U.S. GDP increases a better-than-expected 3.4% as September inflation accelerates
  - 來源：CNBC；發布時間：Thu, 29 Oct 2026 14:11:31 GMT；台北時間：2026-10-29 22:11
  - 摘要：The personal consumption expenditures price index was projected to increase 0.5% in September for an annual rate of 3.7%, according to the Dow Jones c
  - 原文連結：https://www.cnbc.com/2026/10/29/pce-inflation-report-september-2026-.html
- 事件9：Cramer sees opportunity amid tech turmoil and predicts a holiday win for FedEx
  - 來源：CNBC；發布時間：Thu, 29 Oct 2026 16:01:51 GMT；台北時間：2026-10-30 00:01
  - 摘要：The Investing Club holds its "Morning Meeting" every weekday at 10:20 a.m. ET.
  - 原文連結：https://www.cnbc.com/investingclub/2026/10/29/cramer-sees-opportunity-amid-tech-turmoil-and-predicts-a-holiday-win-for-fedex.html
- 事件10：The politics of President Lagarde's European Central Bank early exit  — and who could replace her
  - 來源：CNBC；發布時間：Thu, 29 Oct 2026 14:53:06 GMT；台北時間：2026-10-29 22:53
  - 摘要：European Central Bank President Christine Lagarde will step down on Feb. 7 next year, she announced Thursday.
  - 原文連結：https://www.cnbc.com/2026/10/29/lagarde-ecb-stand-down.html
- 事件11：European Central Bank keeps key interest rate on hold at 2.5%
  - 來源：CNBC；發布時間：Thu, 29 Oct 2026 14:48:01 GMT；台北時間：2026-10-29 22:48
  - 摘要：Markets saw the decision as a hawkish pause and were last pricing in a 67% chance of a December rate hike.
  - 原文連結：https://www.cnbc.com/2026/10/29/european-central-bank-interest-rates.html
- 事件12：Our church has a $1.5 million bequest earning 3.75% in a bank account. Is inflation eroding it?
  - 來源：MarketWatch；發布時間：Thu, 29 Oct 2026 16:00:00 GMT；台北時間：2026-10-30 00:00
  - 摘要：&#x201c;Given the size and long-term nature of this gift, we want to make sure the funds are managed prudently.&#x201d;
  - 原文連結：https://www.marketwatch.com/story/there-may-be-better-investment-options-my-church-received-1-5-million-from-a-parishioner-is-3-75-interest-enough-5164d790?mod=mw_rss_topstories


## 三、期貨

**資料來源：**
1. Cloudflare Workers：TAIFEX Proxy — https://taifex.grichtoyang.workers.dev/
2. TAIFEX Open API — https://openapi.taifex.com.tw/

近月契約月份：202611 (日盤成交量最大者)；交易日期：2026-10-30

### 1．台指期近月日盤行情

| 項目 | 數值 | 資料來源 |
|---|---|---|
| 開盤價 | 47,187 | TAIFEX Proxy |
| 最高價 | 47,218 | TAIFEX Proxy |
| 最低價 | 46,310 | TAIFEX Proxy |
| 收盤價 | 46,577 | TAIFEX Proxy |
| 漲跌點數 | -672 | TAIFEX Proxy |
| 漲跌幅 | -1.42 | TAIFEX Proxy |
| 成交量 | 56,666 | TAIFEX Proxy |
| 日盤高點及低點 | 47,218 / 46,310 | TAIFEX Proxy |

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
| 前十大交易人多方 OI | 94,315 | TAIFEX Proxy |
| 前十大交易人空方 OI | 79,412 | TAIFEX Proxy |
| 前十大交易人多空淨 OI | +14,903 | TAIFEX Proxy |
| 多空淨 OI 變化 (2026-10-28→2026-10-28) | +0 | TAIFEX Proxy snapshots (2026-10-29) |
- 資料日期：2026-10-28 (TypeOfTraders=0 全部交易人；契約月份 202611)

### 5．日盤、夜盤法人交易資料

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 外資日盤多單交易量 | 48,741 | TAIFEX Proxy |
| 外資日盤空單交易量 | 53,346 | TAIFEX Proxy |
| 外資日盤多空淨交易量 | -4,605 | TAIFEX Proxy |
| 外資夜盤多單交易量 | unavailable | TAIFEX Proxy |
| 外資夜盤空單交易量 | unavailable | TAIFEX Proxy |
| 外資夜盤多空淨交易量 | unavailable | TAIFEX Proxy |
| 外資日盤／夜盤交易量變化 | unavailable | TAIFEX Proxy |
| 投信日盤多空淨交易量 | +39 | TAIFEX Proxy |
| 投信夜盤多空淨交易量 | unavailable | TAIFEX Proxy |
| 投信日盤／夜盤交易量變化 | unavailable | TAIFEX Proxy |
| 自營商日盤多空淨交易量 | +992 | TAIFEX Proxy |
| 自營商夜盤多空淨交易量 | unavailable | TAIFEX Proxy |
| 自營商日盤／夜盤交易量變化 | unavailable | TAIFEX Proxy |
| 三大法人日盤多空淨交易量 | -3,574 | TAIFEX Proxy |
| 三大法人夜盤多空淨交易量 | unavailable | TAIFEX Proxy |
| 法人日盤交易金額淨額 (億元) | -335.0 | TAIFEX Proxy |
| 法人夜盤交易金額淨額 (億元) | unavailable | TAIFEX Proxy |

### 6．期貨與現貨關係

| 項目 | 數值 | 資料來源 |
|---|---|---|
| 台指期近月價格 | 46,577 | TAIFEX Proxy |
| 加權指數價格 | 47,035.58 | TWSE OpenAPI MI_INDEX (備援) |
| 台指期與加權指數價差 | -458.58 | TAIFEX Proxy+TWSE OpenAPI MI_INDEX (備援) |
| 價差百分比 | -0.97 | TAIFEX Proxy+TWSE OpenAPI MI_INDEX (備援) |
| 日盤基差 | -458.58 | TAIFEX Proxy+TWSE OpenAPI MI_INDEX (備援) |
| 夜盤價格相對日盤收盤的變化 | unavailable | 端點未提供 |

### 7．日盤、夜盤與籌碼變化對照

#### 7.1 日夜盤價格與成交量對照 (變化 = 日盤 - 夜盤)

| 項目 | 日盤 | 夜盤 | 變化 (日-夜) | 資料來源 |
|---|---|---|---|---|
| 收盤價 | 46,577 | unavailable | unavailable | TAIFEX Proxy |
| 成交量 | 56,666 | unavailable | unavailable | TAIFEX Proxy |
- 台指期總 OI 前日變化：+0（來源：TAIFEX Proxy）


#### 7.2 法人籌碼日夜盤對照 (淨變化 = 日盤淨 - 夜盤淨；OI 為日盤收盤後總量，前日變化另列)

| 法人 | 交易量 |  |  |  |  |  |  | 未平倉量 |  |  |  | 資料來源 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|  | **日盤多單** | **日盤空單** | **日盤淨** | **夜盤多單** | **夜盤空單** | **夜盤淨** | **淨變化 (日-夜)** | **OI多方** | **OI空方** | **OI淨** | **OI前日變化** |  |
| 外資 | 48,741 | 53,346 | -4,605 | unavailable | unavailable | unavailable | unavailable | unavailable | unavailable | unavailable | unavailable | TAIFEX Proxy |
| 投信 | 578 | 539 | +39 | unavailable | unavailable | unavailable | unavailable | unavailable | unavailable | unavailable | unavailable | TAIFEX Proxy |
| 自營商 | 5,353 | 4,361 | +992 | unavailable | unavailable | unavailable | unavailable | unavailable | unavailable | unavailable | unavailable | TAIFEX Proxy |
| 三大法人合計 | 54,672 | 58,246 | -3,574 | unavailable | unavailable | unavailable | unavailable | 0 | 0 | +0 | +0 | TAIFEX Proxy |

#### 7.3 前十大交易人日夜盤對照 (OI 無日夜拆分，列收盤後總量)

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 前十大交易人多方 OI | 94,315 | TAIFEX Proxy |
| 前十大交易人空方 OI | 79,412 | TAIFEX Proxy |
| 前十大交易人多空淨 OI | +14,903 | TAIFEX Proxy |
| 前十大交易人多空淨 OI 變化 (2026-10-28→2026-10-28) | +0 | TAIFEX Proxy snapshots (2026-10-29) |

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
| 交易日期 | 2026-10-30 | TAIFEX Proxy |
| 到期月份／到期日 | 202610F5 | TAIFEX Proxy |
| 資料更新時間 | 2026-10-30 01:17:35 | 本機 |
| 日盤／夜盤標記 | 日盤收盤後資料 | TAIFEX Proxy |

### 2．Call 總成交量、OI、OI 增減

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Call 總成交量 | 197,738 | TAIFEX Proxy |
| Call 總未平倉量 OI | 62,516 | TAIFEX Proxy |
| Call OI 增減 (2026-10-29→2026-10-30) | +0 | TAIFEX Proxy snapshots (2026-10-29) |

### 3．Put 總成交量、OI、OI 增減

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Put 總成交量 | 159,516 | TAIFEX Proxy |
| Put 總未平倉量 OI | 35,052 | TAIFEX Proxy |
| Put OI 增減 (2026-10-29→2026-10-30) | +0 | TAIFEX Proxy snapshots (2026-10-29) |

### 4．Call／Put 比例與變化

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Call／Put 成交量比例 | 1.24 | TAIFEX Proxy |
| Call／Put 未平倉量比例 | 1.78 | TAIFEX Proxy |
| Put／Call Ratio | 0.56 | TAIFEX Proxy |
| Call／Put 比例變化 (量比 2026-10-27→2026-10-28) | 2.40 | TAIFEX Proxy |
| 與前一交易日比較 (OI 比 2026-10-27→2026-10-28) | 7.42 | TAIFEX Proxy |
**資料來源：** 比例 `TAIFEX Proxy chain`；變化 `TAIFEX Proxy PutCallRatio`

### 5．外資 Call／Put 部位

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 外資 Call日買 | 48,121 | TAIFEX Proxy |
| 外資 Call日賣 | 48,611 | TAIFEX Proxy |
| 外資 Call日淨 | -490 | TAIFEX Proxy |
| 外資 Put日買 | 54,731 | TAIFEX Proxy |
| 外資 Put日賣 | 54,418 | TAIFEX Proxy |
| 外資 Put日淨 | +313 | TAIFEX Proxy |
| 外資 Call夜買 | 17,080 | TAIFEX Proxy |
| 外資 Call夜賣 | 17,883 | TAIFEX Proxy |
| 外資 Call夜淨 | -803 | TAIFEX Proxy |
| 外資 Put夜買 | 20,800 | TAIFEX Proxy |
| 外資 Put夜賣 | 20,402 | TAIFEX Proxy |
| 外資 Put夜淨 | +398 | TAIFEX Proxy |
| 外資 日盤淨總量 | -803 | TAIFEX Proxy |
| 外資 Call日夜淨增減 (日－夜) | +313 | TAIFEX Proxy |
| 外資 Put日夜淨增減 (日－夜) | -85 | TAIFEX Proxy |

### 6．自營商 Call／Put 部位

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 自營商 Call日買 | 61,592 | TAIFEX Proxy |
| 自營商 Call日賣 | 67,754 | TAIFEX Proxy |
| 自營商 Call日淨 | -6,162 | TAIFEX Proxy |
| 自營商 Put日買 | 45,946 | TAIFEX Proxy |
| 自營商 Put日賣 | 45,783 | TAIFEX Proxy |
| 自營商 Put日淨 | +163 | TAIFEX Proxy |
| 自營商 Call夜買 | 11,907 | TAIFEX Proxy |
| 自營商 Call夜賣 | 12,895 | TAIFEX Proxy |
| 自營商 Call夜淨 | -988 | TAIFEX Proxy |
| 自營商 Put夜買 | 14,174 | TAIFEX Proxy |
| 自營商 Put夜賣 | 13,910 | TAIFEX Proxy |
| 自營商 Put夜淨 | +264 | TAIFEX Proxy |
| 自營商 日盤淨總量 | -6,325 | TAIFEX Proxy |
| 自營商 Call日夜淨增減 (日－夜) | -5,174 | TAIFEX Proxy |
| 自營商 Put日夜淨增減 (日－夜) | -101 | TAIFEX Proxy |

### 7．主要 Call OI 集中區

| 項目 | 履約價 | OI | 資料來源 |
|---|---|---|---|
| Call OI 第1大履約價 | 48,500 | 4,246 | TAIFEX Proxy |
| Call OI 第2大履約價 | 49,200 | 3,912 | TAIFEX Proxy |
| Call OI 第3大履約價 | 47,000 | 2,685 | TAIFEX Proxy |
| Call OI 最大履約價 | 48,500 | 4,246 | TAIFEX Proxy |

#### Call OI 分布明細 Top10 (機器可讀，到期月份 202610F5)

| # | 履約價 | OI | 佔比 | 資料來源 |
|---|---|---|---|---|
| C1 | 48,500 | 4,246 | 6.79% | TAIFEX Proxy |
| C2 | 49,200 | 3,912 | 6.26% | TAIFEX Proxy |
| C3 | 47,000 | 2,685 | 4.29% | TAIFEX Proxy |
| C4 | 46,300 | 1,948 | 3.12% | TAIFEX Proxy |
| C5 | 46,600 | 1,876 | 3.0% | TAIFEX Proxy |
| C6 | 47,500 | 1,799 | 2.88% | TAIFEX Proxy |
| C7 | 48,000 | 1,643 | 2.63% | TAIFEX Proxy |
| C8 | 46,800 | 1,604 | 2.57% | TAIFEX Proxy |
| C9 | 48,200 | 1,555 | 2.49% | TAIFEX Proxy |
| C10 | 47,300 | 1,533 | 2.45% | TAIFEX Proxy |


### 8．主要 Put OI 集中區

| 項目 | 履約價 | OI | 資料來源 |
|---|---|---|---|
| Put OI 第1大履約價 | 46,000 | 2,822 | TAIFEX Proxy |
| Put OI 第2大履約價 | 45,000 | 2,366 | TAIFEX Proxy |
| Put OI 第3大履約價 | 45,500 | 1,826 | TAIFEX Proxy |
| Put OI 最大履約價 | 46,000 | 2,822 | TAIFEX Proxy |

#### Put OI 分布明細 Top10 (機器可讀，到期月份 202610F5)

| # | 履約價 | OI | 佔比 | 資料來源 |
|---|---|---|---|---|
| P1 | 46,000 | 2,822 | 8.05% | TAIFEX Proxy |
| P2 | 45,000 | 2,366 | 6.75% | TAIFEX Proxy |
| P3 | 45,500 | 1,826 | 5.21% | TAIFEX Proxy |
| P4 | 45,600 | 1,446 | 4.13% | TAIFEX Proxy |
| P5 | 45,700 | 1,360 | 3.88% | TAIFEX Proxy |
| P6 | 45,800 | 1,308 | 3.73% | TAIFEX Proxy |
| P7 | 45,900 | 1,304 | 3.72% | TAIFEX Proxy |
| P8 | 46,500 | 1,160 | 3.31% | TAIFEX Proxy |
| P9 | 46,200 | 1,118 | 3.19% | TAIFEX Proxy |
| P10 | 45,400 | 1,048 | 2.99% | TAIFEX Proxy |


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
| Call Wall 價位 | 48,500 | TAIFEX Proxy |
| 對應到期月份 | 202610F5 | TAIFEX Proxy |
| 與前一交易日的變化 (2026-10-29→2026-10-30) | +0 | TAIFEX Proxy snapshots (2026-10-29) |

### 12．Put Wall

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Put Wall 價位 | 46,000 | TAIFEX Proxy |
| 對應到期月份 | 202610F5 | TAIFEX Proxy |
| 與前一交易日的變化 (2026-10-29→2026-10-30) | +0 | TAIFEX Proxy snapshots (2026-10-29) |

### 13．Gamma Wall

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Gamma Wall 價位 | 47,500.00 | TAIFEX Proxy (options-market-structure-compact (proxy)) |
| 對應到期月份 | 202610F5 | TAIFEX Proxy |
| 資料日期 | 2026-10-28 | TAIFEX Proxy (options-market-structure-compact (proxy)) |

### 14．Gamma Flip

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Gamma Flip 價位 | 46,571.29 | TAIFEX Proxy (options-market-structure-compact (proxy)) |
| 對應到期月份 | 202610F5 | TAIFEX Proxy |
| 資料日期 | 2026-10-28 | TAIFEX Proxy (options-market-structure-compact (proxy)) |

### 15．Max Pain

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Max Pain 價位 | 46,000 | TAIFEX Proxy |
| 對應到期月份 | 202610F5 | TAIFEX Proxy |
| 與前一交易日的變化 (2026-10-29→2026-10-30) | +0 | TAIFEX Proxy snapshots (2026-10-29) |

### 17．選擇權法人日盤、夜盤交易

| 法人 | 日盤多單 | 日盤空單 | 日盤淨 | 夜盤多單 | 夜盤空單 | 夜盤淨 | 淨變化 (日-夜) | 資料來源 |
|---|---|---|---|---|---|---|---|---|
| 外資 | 102,539 | 103,342 | -803 | unavailable | unavailable | unavailable | unavailable | TAIFEX Proxy |
| 投信 | 0 | 2,776 | -2,776 | unavailable | unavailable | unavailable | unavailable | TAIFEX Proxy |
| 自營商 | 107,375 | 113,700 | -6,325 | unavailable | unavailable | unavailable | unavailable | TAIFEX Proxy |
| 三大法人合計 | 209,914 | 219,818 | -9,904 | unavailable | unavailable | unavailable | unavailable | TAIFEX Proxy |
- 方法論：多方＝買Call＋賣Put（看多），空方＝賣Call＋買Put（看空），淨額＝看多－看空（已用 Call／Put 拆分頁交叉驗算一致）
- 公式：多方(買)－空方(賣)＝（買call＋賣put）－（賣call＋買put）＝看多－看空
- 速記：多＝BC＋SP、空＝SC＋BP

#### 法人多空力道表（金額・億元；上游千元／1e5）

| 法人 | 日多方力道 | 日空方力道 | 日淨多空力道 | 夜多方力道 | 夜空方力道 | 夜淨多空力道 | 日淨－夜淨 | 資料來源 |
|---|---|---|---|---|---|---|---|---|
| 外資 | 9.19 | 9.33 | -0.14 | 3.39 | 3.67 | -0.28 | +0.14 | TAIFEX Proxy |
| 投信 | 0.00 | 0.75 | -0.75 | 0.00 | 0.00 | +0 | -0.75 | TAIFEX Proxy |
| 自營商 | 8.11 | 8.38 | -0.27 | 2.22 | 2.33 | -0.11 | -0.16 | TAIFEX Proxy |
| 三大法人合計 | 17.30 | 18.47 | -1.17 | 5.61 | 6.00 | -0.39 | -0.77 | TAIFEX Proxy |

### 18．選擇權前十大

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 買權多方 OI | 8,231 | TAIFEX OpenAPI |
| 買權空方 OI | 9,363 | TAIFEX OpenAPI |
| 買權多空淨 OI | -1,132 | TAIFEX OpenAPI |
| 買權多空淨 OI 變化 (2026-10-28→2026-10-28) | +0 | TAIFEX Proxy snapshots (2026-10-29) |

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 賣權多方 OI | 7,999 | TAIFEX Proxy |
| 賣權空方 OI | 10,051 | TAIFEX Proxy |
| 賣權多空淨 OI | -2,052 | TAIFEX Proxy |
| 賣權多空淨 OI 變化 (2026-10-28→2026-10-28) | +0 | TAIFEX Proxy snapshots (2026-10-29) |
- 資料日期：買權 2026-10-28／賣權 2026-10-28 (TypeOfTraders=0 全部交易人；契約月份 202611)

#### 大戶流向（全日；前十大無日夜拆分）

| 項目 | 淨變化 | 區間 | 資料來源 |
|---|---|---|---|
| 期貨前十大 | +0 | 2026-10-28→2026-10-28 | TAIFEX Proxy snapshots (2026-10-29) |
| 買權前十大 | +0 | 2026-10-28→2026-10-28 | TAIFEX Proxy snapshots (2026-10-29) |
| 賣權前十大 | +0 | 2026-10-28→2026-10-28 | TAIFEX Proxy snapshots (2026-10-29) |

### 16．資料來源、時間、時區與狀態

- 資料來源：TAIFEX 經 Cloudflare Worker Proxy
- 資料日期：2026-10-30；資料時間：2026-10-30 01:17:35；時區：`Asia/Taipei`
- 日盤／夜盤標記：日盤收盤後 + 夜盤盤後
- 未取得欄位 (22)：taiex.open, taiex.high, taiex.low, listed_breadth.up, listed_breadth.down, listed_breadth.flat, listed_breadth.limit_up, listed_breadth.limit_down, otc_breadth.up, otc_breadth.down, otc_breadth.flat, otc_breadth.limit_up, otc_breadth.limit_down, margin.fin_yi, margin.fin_chg_yi, sbl.sale_bal, sbl.sale_chg, turnover.listed, turnover.otc, turnover.total, futures.gamma_wall, futures.gamma_flip
- 註記：無日期端點為最新盤勢快照 (判定資料日期 2026-10-29，非 T0 2026-10-30)，適用：日盤價／法人交易／夜盤／選擇權法人；T0 相符時不另標註
- 註記：futures-price-after-hours 日期 2026-10-29 非今日 2026-10-30，視為無新節次，不採用
- 註記：futures-institutional-after-hours 日期 2026-10-29 非今日 2026-10-30，視為無新節次，不採用
- 註記：options-institutional-after-hours 日期 2026-10-29 非今日 2026-10-30，視為無新節次，不採用
- 註記：Gamma Wall/Flip 端點不可用（上游 502），標 unavailable
- 註記：Call/Put Wall 與 Max Pain 資料日期 2026-10-29 (T0 2026-10-30 端點不穩，採最新可得)
- 註記：Gamma 資料日期 2026-10-28 (T0 2026-10-30 尚無，上游 FMTQIK 落後，採最新可得)
- 註記：夜盤開高低收未取得 (proxy 與官方皆無)，僅成交量/OI/結算價
- 註記：法人 OI 未取得
- 註記：法人交易量變化無昨日交易端點，標 unavailable
- 註記：選擇權 chain 資料日期 2026-10-29 (T0 2026-10-30 端點不穩，採最新可得)
- 註記：Gamma Wall/Flip 資料日期 2026-10-28 (來源 options-market-structure-compact (proxy))

## 五、資料來源、時間與完整性

- 期貨/匯率為最新報價，其餘為 T0 收盤資料；時間皆為 `Asia/Taipei`。
- taiex：`TWSE OpenAPI MI_INDEX (備援)`
- listed_breadth：`twse-proxy`
- listed_turnover：`twse-proxy market_statistics`
- institutional：`twse-proxy /institutional`
- margin_short：`TWSE MI_MARGN + TPEX margin_balance (張)`
- margin_ratio：`前值遞補 (DATA 2026-10-28；當日三源皆失敗；民間估算；官方無每日序列)`
- sbl：`TWSE TWT93U + TPEX margin_sbl`
- 期貨選擇權：`TAIFEX Proxy`
- 新聞：台股 Yahoo／國際 Fed＋CNBC＋MarketWatch；台股 Yahoo（不足時財訊快報備援）/ 國際 Fed 公告＋CNBC＋MarketWatch RSS；Fed 無摘要；investing 港股為主已退役；cnyes CSR、wantgoo JS 算繪、中央社/台灣央行路徑待查，未採用
- 美股/亞股/期貨/匯率/ADR/商品：`Yahoo Finance Chart API`；美債：`Yahoo Finance (備援)`
- 註記：twse-proxy taiex 缺值，改用 MI_INDEX 備援
- 註記：大盤開高低未取得 (FinMind 失敗；MI_INDEX 無此欄)
- 註記：twtazu_od 備援日期不符 (回傳舊資料)，上市漲跌標 unavailable
- 註記：上櫃 highlight 日期不符或缺值 (回傳 1151029, T0=1151030)
- 註記：三大法人回傳日期 20261029 (T0 20261030)，採用最新可得
- 註記：HiStock 未取得，融資餘額/增減標 unavailable (官方逐股加總僅有張數)
- 註記：融券沿用官方逐股加總 (張)
- 註記：融資維持率未取得 (三源皆失敗；官方無每日序列)
- 註記：融資維持率採前值遞補 (DATA 2026-10-28)，非 T0 2026-10-30
- 註記：上市 MI_MARGN / TWT96U 無日期欄，採用最新可得
- 本報告僅整理資料，不提供交易判斷。

## 六、期現選方向對照

**規則：** 趨勢偏多／空＝現貨、期貨OI、選擇權日淨三者同向；避險／對沖＝現貨與期選反向；日內反轉＝日淨與夜淨反向；缺值標示，不推估。選擇權多空為看多看空口徑。

| 法人 | 現貨買賣超(億) | 期貨OI淨(口) | 期貨日淨 | 期貨夜淨 | 選擇權日淨 | 選擇權夜淨 | 判定 | 期選組合 | 資料來源 |
|---|---|---|---|---|---|---|---|---|---|
| 外資 | -688.2 | unavailable | -4,605 | unavailable | -803 | unavailable | 資料不足 | 資料不足 | twse-proxy／TAIFEX Proxy |
| 投信 | +70.4 | unavailable | +39 | unavailable | -2,776 | unavailable | 資料不足 | 資料不足 | twse-proxy／TAIFEX Proxy |
| 自營商 | -215.0 | unavailable | +992 | unavailable | -6,325 | unavailable | 資料不足 | 資料不足 | twse-proxy／TAIFEX Proxy |
