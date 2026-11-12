# DATA_REPORT_20261113

- 報告日期：`2026-11-13`
- T0 交易日期：`2026-11-13`
- 資料產出時間：`2026-11-13 02:40:19`
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
| 加權指數 | 44,257.15 | 點 | TWSE OpenAPI MI_INDEX (備援) |
| 開盤 | unavailable | 點 | FinMind |
| 最高 | unavailable | 點 | FinMind |
| 最低 | unavailable | 點 | FinMind |
| 收盤 | 44,257.15 | 點 | TWSE OpenAPI MI_INDEX (備援) |
| 漲跌點數 | 1,545.23 | 點 | TWSE OpenAPI MI_INDEX (備援) |
| 漲跌幅 | +3.62 | % | TWSE OpenAPI MI_INDEX (備援) |
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
| 外資 | -6.8 | 億元 | twse-proxy /institutional |
| 投信 | +125.7 | 億元 | twse-proxy /institutional |
| 自營商 | -65.4 | 億元 | twse-proxy /institutional |
| 三大法人合計 | +53.4 | 億元 | twse-proxy /institutional |

### 4. 融資融券

**資料來源：** 上市+上櫃 `HiStock` (金額口徑)；維持率 `istock.tw`；備援官方逐股加總

| 項目 | 數值 | 單位 | 資料來源 |
|---|---|---|---|
| 融資餘額 | unavailable | 億元 | HiStock |
| 融資增減 | unavailable | 億元 | HiStock |
| 融券餘額 | 209,019 | 張 | HiStock |
| 融券增減 | 8,931 | 張 | HiStock |
| 融資維持率 | 151.90 | % | 前值遞補 (DATA 2026-11-12；當日三源皆失敗；民間估算；官方無每日序列) |

### 5. 借券資料

**資料來源：** 上市 `TWSE OpenAPI TWT96U` (可借餘額)、上櫃 `TPEX OpenAPI tpex_margin_sbl`

| 項目 | 數值 | 單位 | 資料來源 |
|---|---|---|---|
| 借券餘額 | 295,441 | 張 | TWSE TWT93U + TPEX margin_sbl |
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
| S&P 500 | ^GSPC | 7,624.01 | 4.63 | +0.06 | Yahoo Finance Chart API |
| Nasdaq Composite | ^IXIC | 25,467.04 | 0.85 | +0.00 | Yahoo Finance Chart API |
| Nasdaq 100 | ^NDX | 28,389.46 | 15.21 | +0.05 | Yahoo Finance Chart API |
| Dow Jones | ^DJI | 52,562.60 | 76.11 | +0.15 | Yahoo Finance Chart API |
| 費城半導體 SOX | ^SOX | 10,547.06 | -17.05 | -0.16 | Yahoo Finance Chart API |
| VIX | ^VIX | 17.72 | 0.23 | +1.32 | Yahoo Finance Chart API |

### 2. 亞洲主要指數

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 收盤／最新值 | 漲跌點 | 漲跌幅 | 資料來源 |
|---|---|---|---|---|---|
| 日經225 | ^N225 | 61,248.59 | 789.01 | +1.31 | Yahoo Finance Chart API |
| 韓國KOSPI | ^KS11 | 5,375.36 | 136.23 | +2.60 | Yahoo Finance Chart API |
| 香港恆生 | ^HSI | 24,315.92 | -241.12 | -0.98 | Yahoo Finance Chart API |
| 上海綜合 | 000001.SS | 3,680.64 | 16.92 | +0.46 | Yahoo Finance Chart API |
| 深圳成分 | 399001.SZ | 11,389.74 | 148.20 | +1.32 | Yahoo Finance Chart API |

### 3. 美股指數期貨

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 最新值 | 漲跌點 | 漲跌幅 | 資料來源 |
|---|---|---|---|---|---|
| S&P500期貨 | ES=F | 7,648.25 | 7.75 | +0.10 | Yahoo Finance Chart API |
| Nasdaq100期貨 | NQ=F | 28,492.50 | 19.25 | +0.07 | Yahoo Finance Chart API |
| 道瓊期貨 | YM=F | 52,673.00 | 95.00 | +0.18 | Yahoo Finance Chart API |
| Russell2000期貨 | RTY=F | 2,827.60 | -26.10 | -0.91 | Yahoo Finance Chart API |

### 4. 美國國債殖利率

**資料來源：** `U.S. Treasury Fiscal Data API` (失敗時備援 Treasury yield.xml 與 `Yahoo Finance`)

| 項目 | API 資料欄位／識別 | 殖利率 | 日變化 | 資料來源 |
|---|---|---|---|---|
| 美國 2 年期殖利率 | 2 Yr | 4.73 | 0.17 | U.S. Treasury yield.xml (網頁備援) |
| 美國 10 年期殖利率 | 10 Yr | 5.11 | 0.11 | Yahoo Finance (備援) |
| 美國 30 年期殖利率 | 30 Yr | 5.44 | 0.08 | Yahoo Finance (備援) |

### 5. 主要匯率

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 最新值 | 漲跌點 | 漲跌幅 | 資料來源 |
|---|---|---|---|---|---|
| USD/TWD | TWD=X | 33.00 | 0.04 | +0.13 | Yahoo Finance Chart API |
| DXY美元指數 | DX-Y.NYB | 103.19 | 0.28 | +0.27 | Yahoo Finance Chart API |
| USD/JPY | JPY=X | 159.78 | 1.08 | +0.68 | Yahoo Finance Chart API |
| USD/KRW | KRW=X | unavailable | unavailable | unavailable | Yahoo Finance Chart API |

### 6. 台灣相關ADR

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 收盤／最新值 | 漲跌點 | 漲跌幅 | 資料來源 |
|---|---|---|---|---|---|
| 台積電ADR | TSM | 407.78 | -5.57 | -1.35 | Yahoo Finance Chart API |
| 聯電ADR | UMC | 15.81 | -0.27 | -1.68 | Yahoo Finance Chart API |
| 日月光ADR | ASX | 36.48 | -1.34 | -3.54 | Yahoo Finance Chart API |

### 7. 原油黃金Bitcoin

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 收盤／最新值 | 漲跌點 | 漲跌幅 | 資料來源 |
|---|---|---|---|---|---|
| WTI原油期貨 | CL=F | 88.27 | 1.74 | +2.01 | Yahoo Finance Chart API |
| 黃金期貨 | GC=F | 3,883.70 | -116.80 | -2.92 | Yahoo Finance Chart API |
| Bitcoin | BTC-USD | 71,866.74 | -2,097.73 | -2.84 | Yahoo Finance Chart API |

### 8. 重大經濟數據、央行事件與重大市場新聞

**資料來源：** 台股 `tw.stock.yahoo.com` (含內文摘要)；國際 `Fed 公告 RSS`＋`CNBC`＋`MarketWatch` (標題、來源、時間與連結)

- 事件1：黃仁勳辭輝達執行長 財務長克瑞斯任臨時CEO
  - 來源：Yahoo 台股；發布時間：2026-11-12T14:04:09Z；台北時間：2026-11-12 22:04
  - 摘要：AI晶片巨擘輝達執行長黃仁勳繼日前坦言與中國女商人黃樂過從甚密後，再傳出與公司下屬有染，黃仁勳今天辭執行長，輝達財務長克瑞斯（Colette Kress）已獲任命為臨時執行長。
  - 原文連結：https://tw.stock.yahoo.com/news/%E9%BB%83%E4%BB%81%E5%8B%B3%E8%BE%AD%E8%BC%9D%E9%81%94%E5%9F%B7%E8%A1%8C%E9%95%B7-%E8%B2%A1%E5%8B%99%E9%95%B7%E5%85%8B%E7%91%9E%E6%96%AF%E4%BB%BB%E8%87%A8%E6%99%82ceo-140339917.html
- 事件2：陳立武、木頭姐同場開講 Yahoo財經高峰會今晚9點直播
  - 來源：Yahoo 台股；發布時間：2026-11-12T07:43:22Z；台北時間：2026-11-12 15:43
  - 摘要：2026「Yahoo財經高峰會」(Yahoo Finance Invest) 將於 11 月 12 日盛大登場！本次高峰會以「投資無界，創新無限（ Investing and Innovating Without Limits ）」為主軸，
  - 原文連結：https://tw.stock.yahoo.com/news/2026%E3%80%8Cyahoo%E8%B2%A1%E7%B6%93%E9%AB%98%E5%B3%B0%E6%9C%83%E3%80%8D11%E6%9C%8812%E6%97%A5%E5%85%A8%E7%90%83%E7%9B%B4%E6%92%AD%E7%99%BB%E5%A0%B4%EF%BC%81%E9%87%8D%E9%87%8F%E7%B4%9A%E9%A0%98%E8%A2%96%E6%8F%AD%E6%9B%89%EF%BC%81%E5%89%8D%E7%9E%BB-ai%E3%80%81%E5%88%A9%E7%8E%87%E3%80%81%E5%A4%AA%E7%A9%BA%E7%B6%93%E6%BF%9F%E8%88%87%E9%9B%BB%E5%8B%95%E8%BB%8A%E6%96%B0%E8%B6%A8%E5%8B%A2%E8%88%87%E6%8A%95%E8%B3%87%E9%A2%A8%E9%9A%AA-012336051.html
- 事件3：黃仁勳下台衝擊台股？台指期夜盤驚濤駭浪！
  - 來源：Yahoo 台股；發布時間：2026-11-12T15:01:49Z；台北時間：2026-11-12 23:01
  - 摘要：輝達（NVIDIA）執行長黃仁勳因外遇風波連環爆，於台灣時間今（12）晚宣布辭去執行長及董事職務，震撼彈波及台指期夜盤一度湧現恐慌賣壓。指數盤中跌破4萬3,000點整數關卡，最低跌超過700點。不過，逢低買盤大舉進場，指數隨即展開深V強彈，
  - 原文連結：https://tw.stock.yahoo.com/news/%E9%BB%83%E4%BB%81%E5%8B%B3%E4%B8%8B%E5%8F%B0%E8%A1%9D%E6%93%8A%E6%98%8E%E5%A4%A9%E5%8F%B0%E8%82%A1%EF%BC%9F%E5%8F%B0%E6%8C%87%E6%9C%9F%E5%A4%9C%E7%9B%A4%E5%9A%87%E8%B7%8C%E9%80%BE700%E9%BB%9E%E5%BE%8C-%E9%A9%9A%E9%9A%AA%E7%BF%BB%E7%B4%85%E7%8B%82%E6%8B%89%E8%BF%91%E5%8D%83%E9%BB%9E-150149695.html
- 事件4：台股昨天噴今天丟4萬4 台玻揪紡織股逆勢開趴
  - 來源：Yahoo 台股；發布時間：2026-11-12T09:18:52Z；台北時間：2026-11-12 17:18
  - 摘要：台股連彈踩煞車，重挫1165點失守4萬4！今(12)日加權指數早盤一度翻紅，隨後賣壓擴大，終場下跌1165.28點、跌幅2.63%，收43091.87點，上市成交金額10151.11億元，盤中高低震盪1581.74點。電子類股下挫3.07%
  - 原文連結：https://tw.stock.yahoo.com/news/%E5%8F%B0%E8%82%A1%E5%8F%8D%E5%BD%88%E5%88%97%E8%BB%8A%E6%80%A5%E7%85%9E%EF%BC%81%E9%87%8D%E6%91%941165%E9%BB%9E%E4%B8%9F4%E8%90%AC4-%E9%9B%BB%E5%AD%90%E6%AC%8A%E5%80%BC%E4%B8%80%E8%B5%B7%E8%85%BF%E8%BB%9F-%E5%8F%B0%E7%8E%BB%E6%8F%AA%E7%B4%A1%E7%B9%94%E6%97%8F%E7%BE%A4%E7%B4%85%E7%9B%A4%E7%95%B6%E8%87%AA%E5%BC%B7%EF%BD%9Cyahoo%E8%B2%A1%E7%B6%93%E6%8E%83%E6%8F%8F-091852246.html
- 事件5：空軍出手縮了限空令何時撤 金管會揭退場關鍵
  - 來源：Yahoo 台股；發布時間：2026-11-12T08:58:56Z；台北時間：2026-11-12 16:58
  - 摘要：金管會限空令9日正式上路，實施包括調整每日盤中借券賣出委託數量，及融券保證金成數等五大救市措施，今（12）被問到成效如何？證期局主祕王秀玲表示，借券賣出（俗稱放空）金額從392億元降到最低163億元，少了230億元，且四天台股漲了8.54%
  - 原文連結：https://tw.stock.yahoo.com/news/%E9%99%90%E7%A9%BA%E4%BB%A4%E6%88%90%E6%95%88%E5%A6%82%E4%BD%95%EF%BC%9F%E4%BD%95%E6%99%82%E6%9C%83%E9%80%80%E5%A0%B4%EF%BC%9F%E9%87%91%E7%AE%A1%E6%9C%83%E4%B8%80%E4%BD%B5%E5%9B%9E%E6%87%89%E4%BA%86-085856827.html
- 事件6：永豐銀遭駭418人被盜轉 金管會緊盯供應商管理恐開罰
  - 來源：Yahoo 台股；發布時間：2026-11-12T09:28:08Z；台北時間：2026-11-12 17:28
  - 摘要：永豐金（2890）旗下永豐銀11月3日異常轉帳4,176萬元，影響418人，董總於記者會上鞠躬道歉，並表示是外部駭客利用新網銀交易系統的供應商安全設定所致。金管會副主委陳彥良11日也證實，此次問題發生在「中台」漏洞。銀行局副局長張嘉魁今（1
  - 原文連結：https://tw.stock.yahoo.com/news/%E6%B0%B8%E8%B1%90%E9%8A%80%E9%81%AD%E9%A7%AD418%E4%BA%BA%E8%A2%AB%E7%9B%9C%E8%BD%894%E5%8D%83%E8%90%AC-%E9%87%91%E7%AE%A1%E6%9C%83%E7%9B%AF%E4%B8%8A%E9%80%99%E7%BC%BA%E5%A4%B1%E6%81%90%E8%A2%AB%E9%96%8B%E7%BD%B0-092808064.html
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
- 事件11：In a policy switch, the Fed says its October 2027 meeting will not see a vote on interest rates
  - 來源：CNBC；發布時間：Thu, 12 Nov 2026 18:26:52 GMT；台北時間：2026-11-13 02:26
  - 摘要：There will be seven voting meetings next year, with the October session set up as extra time for policy deliberation without a formal vote or post-mee
  - 原文連結：https://www.cnbc.com/2026/11/12/in-policy-switch-fed-says-its-october-2027-meeting-will-not-see-a-vote-on-interest-rates.html
- 事件12：Analysis: Nvidia’s leadership crisis tests the chipmaker’s role as the ‘central bank of AI’
  - 來源：CNBC；發布時間：Thu, 12 Nov 2026 17:39:54 GMT；台北時間：2026-11-13 01:39
  - 摘要：The tech giant's web of ties to other companies is raising the possibility that it could do far-reaching economic and financial damage.
  - 原文連結：https://www.cnbc.com/2026/11/11/nvidia-jensen-huang-ai-financial-system-risk.html


## 三、期貨

**資料來源：**
1. Cloudflare Workers：TAIFEX Proxy — https://taifex.grichtoyang.workers.dev/
2. TAIFEX Open API — https://openapi.taifex.com.tw/

近月契約月份：202611 (日盤成交量最大者)；交易日期：2026-11-13

### 1．台指期近月日盤行情

| 項目 | 數值 | 資料來源 |
|---|---|---|
| 開盤價 | 44,166 | TAIFEX Proxy |
| 最高價 | 44,555 | TAIFEX Proxy |
| 最低價 | 43,057 | TAIFEX Proxy |
| 收盤價 | 43,178 | TAIFEX Proxy |
| 漲跌點數 | -958 | TAIFEX Proxy |
| 漲跌幅 | -2.17 | TAIFEX Proxy |
| 成交量 | 87,240 | TAIFEX Proxy |
| 日盤高點及低點 | 44,555 / 43,057 | TAIFEX Proxy |

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
| 前十大交易人多方 OI | 105,198 | TAIFEX Proxy |
| 前十大交易人空方 OI | 85,450 | TAIFEX Proxy |
| 前十大交易人多空淨 OI | +19,748 | TAIFEX Proxy |
| 多空淨 OI 變化 (2026-11-11→2026-11-11) | +0 | TAIFEX Proxy snapshots (2026-11-12) |
- 資料日期：2026-11-11 (TypeOfTraders=0 全部交易人；契約月份 202611)

### 5．日盤、夜盤法人交易資料

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 外資日盤多單交易量 | 84,418 | TAIFEX Proxy |
| 外資日盤空單交易量 | 79,685 | TAIFEX Proxy |
| 外資日盤多空淨交易量 | +4,733 | TAIFEX Proxy |
| 外資夜盤多單交易量 | unavailable | TAIFEX Proxy |
| 外資夜盤空單交易量 | unavailable | TAIFEX Proxy |
| 外資夜盤多空淨交易量 | unavailable | TAIFEX Proxy |
| 外資日盤／夜盤交易量變化 | unavailable | TAIFEX Proxy |
| 投信日盤多空淨交易量 | -2,969 | TAIFEX Proxy |
| 投信夜盤多空淨交易量 | unavailable | TAIFEX Proxy |
| 投信日盤／夜盤交易量變化 | unavailable | TAIFEX Proxy |
| 自營商日盤多空淨交易量 | -214 | TAIFEX Proxy |
| 自營商夜盤多空淨交易量 | unavailable | TAIFEX Proxy |
| 自營商日盤／夜盤交易量變化 | unavailable | TAIFEX Proxy |
| 三大法人日盤多空淨交易量 | +1,550 | TAIFEX Proxy |
| 三大法人夜盤多空淨交易量 | unavailable | TAIFEX Proxy |
| 法人日盤交易金額淨額 (億元) | +136.3 | TAIFEX Proxy |
| 法人夜盤交易金額淨額 (億元) | unavailable | TAIFEX Proxy |

### 6．期貨與現貨關係

| 項目 | 數值 | 資料來源 |
|---|---|---|
| 台指期近月價格 | 43,178 | TAIFEX Proxy |
| 加權指數價格 | 44,257.15 | TWSE OpenAPI MI_INDEX (備援) |
| 台指期與加權指數價差 | -1,079.15 | TAIFEX Proxy+TWSE OpenAPI MI_INDEX (備援) |
| 價差百分比 | -2.44 | TAIFEX Proxy+TWSE OpenAPI MI_INDEX (備援) |
| 日盤基差 | -1,079.15 | TAIFEX Proxy+TWSE OpenAPI MI_INDEX (備援) |
| 夜盤價格相對日盤收盤的變化 | unavailable | 端點未提供 |

### 7．日盤、夜盤與籌碼變化對照

#### 7.1 日夜盤價格與成交量對照 (變化 = 日盤 - 夜盤)

| 項目 | 日盤 | 夜盤 | 變化 (日-夜) | 資料來源 |
|---|---|---|---|---|
| 收盤價 | 43,178 | unavailable | unavailable | TAIFEX Proxy |
| 成交量 | 87,240 | unavailable | unavailable | TAIFEX Proxy |
- 台指期總 OI 前日變化：+0（來源：TAIFEX Proxy）


#### 7.2 法人籌碼日夜盤對照 (淨變化 = 日盤淨 - 夜盤淨；OI 為日盤收盤後總量，前日變化另列)

| 法人 | 交易量 |  |  |  |  |  |  | 未平倉量 |  |  |  | 資料來源 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|  | **日盤多單** | **日盤空單** | **日盤淨** | **夜盤多單** | **夜盤空單** | **夜盤淨** | **淨變化 (日-夜)** | **OI多方** | **OI空方** | **OI淨** | **OI前日變化** |  |
| 外資 | 84,418 | 79,685 | +4,733 | unavailable | unavailable | unavailable | unavailable | unavailable | unavailable | unavailable | unavailable | TAIFEX Proxy |
| 投信 | 2,499 | 5,468 | -2,969 | unavailable | unavailable | unavailable | unavailable | unavailable | unavailable | unavailable | unavailable | TAIFEX Proxy |
| 自營商 | 5,159 | 5,373 | -214 | unavailable | unavailable | unavailable | unavailable | unavailable | unavailable | unavailable | unavailable | TAIFEX Proxy |
| 三大法人合計 | 92,076 | 90,526 | +1,550 | unavailable | unavailable | unavailable | unavailable | 0 | 0 | +0 | +0 | TAIFEX Proxy |

#### 7.3 前十大交易人日夜盤對照 (OI 無日夜拆分，列收盤後總量)

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 前十大交易人多方 OI | 105,198 | TAIFEX Proxy |
| 前十大交易人空方 OI | 85,450 | TAIFEX Proxy |
| 前十大交易人多空淨 OI | +19,748 | TAIFEX Proxy |
| 前十大交易人多空淨 OI 變化 (2026-11-11→2026-11-11) | +0 | TAIFEX Proxy snapshots (2026-11-12) |

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
| 交易日期 | 2026-11-13 | TAIFEX Proxy |
| 到期月份／到期日 | 202611F2 | TAIFEX Proxy |
| 資料更新時間 | 2026-11-13 02:40:19 | 本機 |
| 日盤／夜盤標記 | 日盤收盤後資料 | TAIFEX Proxy |

### 2．Call 總成交量、OI、OI 增減

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Call 總成交量 | 193,627 | TAIFEX Proxy |
| Call 總未平倉量 OI | 53,656 | TAIFEX Proxy |
| Call OI 增減 (2026-11-12→2026-11-13) | +0 | TAIFEX Proxy snapshots (2026-11-12) |

### 3．Put 總成交量、OI、OI 增減

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Put 總成交量 | 189,184 | TAIFEX Proxy |
| Put 總未平倉量 OI | 36,473 | TAIFEX Proxy |
| Put OI 增減 (2026-11-12→2026-11-13) | +0 | TAIFEX Proxy snapshots (2026-11-12) |

### 4．Call／Put 比例與變化

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Call／Put 成交量比例 | 1.02 | TAIFEX Proxy |
| Call／Put 未平倉量比例 | 1.47 | TAIFEX Proxy |
| Put／Call Ratio | 0.68 | TAIFEX Proxy |
| Call／Put 比例變化 (量比 2026-11-10→2026-11-11) | -11.28 | TAIFEX Proxy |
| 與前一交易日比較 (OI 比 2026-11-10→2026-11-11) | -1.37 | TAIFEX Proxy |
**資料來源：** 比例 `TAIFEX Proxy chain`；變化 `TAIFEX Proxy PutCallRatio`

### 5．外資 Call／Put 部位

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 外資 Call日買 | 58,933 | TAIFEX Proxy |
| 外資 Call日賣 | 57,152 | TAIFEX Proxy |
| 外資 Call日淨 | +1,781 | TAIFEX Proxy |
| 外資 Put日買 | 66,840 | TAIFEX Proxy |
| 外資 Put日賣 | 67,404 | TAIFEX Proxy |
| 外資 Put日淨 | -564 | TAIFEX Proxy |
| 外資 Call夜買 | 22,289 | TAIFEX Proxy |
| 外資 Call夜賣 | 22,047 | TAIFEX Proxy |
| 外資 Call夜淨 | +242 | TAIFEX Proxy |
| 外資 Put夜買 | 24,796 | TAIFEX Proxy |
| 外資 Put夜賣 | 24,617 | TAIFEX Proxy |
| 外資 Put夜淨 | +179 | TAIFEX Proxy |
| 外資 日盤淨總量 | +2,345 | TAIFEX Proxy |
| 外資 Call日夜淨增減 (日－夜) | +1,539 | TAIFEX Proxy |
| 外資 Put日夜淨增減 (日－夜) | -743 | TAIFEX Proxy |

### 6．自營商 Call／Put 部位

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 自營商 Call日買 | 55,099 | TAIFEX Proxy |
| 自營商 Call日賣 | 53,952 | TAIFEX Proxy |
| 自營商 Call日淨 | +1,147 | TAIFEX Proxy |
| 自營商 Put日買 | 47,742 | TAIFEX Proxy |
| 自營商 Put日賣 | 50,455 | TAIFEX Proxy |
| 自營商 Put日淨 | -2,713 | TAIFEX Proxy |
| 自營商 Call夜買 | 17,288 | TAIFEX Proxy |
| 自營商 Call夜賣 | 16,821 | TAIFEX Proxy |
| 自營商 Call夜淨 | +467 | TAIFEX Proxy |
| 自營商 Put夜買 | 17,043 | TAIFEX Proxy |
| 自營商 Put夜賣 | 19,073 | TAIFEX Proxy |
| 自營商 Put夜淨 | -2,030 | TAIFEX Proxy |
| 自營商 日盤淨總量 | +3,860 | TAIFEX Proxy |
| 自營商 Call日夜淨增減 (日－夜) | +680 | TAIFEX Proxy |
| 自營商 Put日夜淨增減 (日－夜) | -683 | TAIFEX Proxy |

### 7．主要 Call OI 集中區

| 項目 | 履約價 | OI | 資料來源 |
|---|---|---|---|
| Call OI 第1大履約價 | 46,000 | 4,909 | TAIFEX Proxy |
| Call OI 第2大履約價 | 47,000 | 3,136 | TAIFEX Proxy |
| Call OI 第3大履約價 | 45,000 | 2,567 | TAIFEX Proxy |
| Call OI 最大履約價 | 46,000 | 4,909 | TAIFEX Proxy |

#### Call OI 分布明細 Top10 (機器可讀，到期月份 202611F2)

| # | 履約價 | OI | 佔比 | 資料來源 |
|---|---|---|---|---|
| C1 | 46,000 | 4,909 | 9.15% | TAIFEX Proxy |
| C2 | 47,000 | 3,136 | 5.84% | TAIFEX Proxy |
| C3 | 45,000 | 2,567 | 4.78% | TAIFEX Proxy |
| C4 | 44,000 | 2,028 | 3.78% | TAIFEX Proxy |
| C5 | 44,500 | 1,462 | 2.72% | TAIFEX Proxy |
| C6 | 46,500 | 1,403 | 2.61% | TAIFEX Proxy |
| C7 | 45,700 | 1,288 | 2.4% | TAIFEX Proxy |
| C8 | 48,000 | 1,098 | 2.05% | TAIFEX Proxy |
| C9 | 45,500 | 1,096 | 2.04% | TAIFEX Proxy |
| C10 | 44,600 | 1,031 | 1.92% | TAIFEX Proxy |


### 8．主要 Put OI 集中區

| 項目 | 履約價 | OI | 資料來源 |
|---|---|---|---|
| Put OI 第1大履約價 | 43,000 | 1,804 | TAIFEX Proxy |
| Put OI 第2大履約價 | 42,000 | 1,646 | TAIFEX Proxy |
| Put OI 第3大履約價 | 40,000 | 1,635 | TAIFEX Proxy |
| Put OI 最大履約價 | 43,000 | 1,804 | TAIFEX Proxy |

#### Put OI 分布明細 Top10 (機器可讀，到期月份 202611F2)

| # | 履約價 | OI | 佔比 | 資料來源 |
|---|---|---|---|---|
| P1 | 43,000 | 1,804 | 4.95% | TAIFEX Proxy |
| P2 | 42,000 | 1,646 | 4.51% | TAIFEX Proxy |
| P3 | 40,000 | 1,635 | 4.48% | TAIFEX Proxy |
| P4 | 39,000 | 1,434 | 3.93% | TAIFEX Proxy |
| P5 | 41,000 | 1,390 | 3.81% | TAIFEX Proxy |
| P6 | 42,500 | 1,300 | 3.56% | TAIFEX Proxy |
| P7 | 35,700 | 1,218 | 3.34% | TAIFEX Proxy |
| P8 | 42,400 | 944 | 2.59% | TAIFEX Proxy |
| P9 | 42,800 | 853 | 2.34% | TAIFEX Proxy |
| P10 | 41,500 | 839 | 2.3% | TAIFEX Proxy |


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
| 對應到期月份 | 202611F2 | TAIFEX Proxy |
| 與前一交易日的變化 (2026-11-12→2026-11-13) | +0 | TAIFEX Proxy snapshots (2026-11-12) |

### 12．Put Wall

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Put Wall 價位 | 43,000 | TAIFEX Proxy |
| 對應到期月份 | 202611F2 | TAIFEX Proxy |
| 與前一交易日的變化 (2026-11-12→2026-11-13) | +0 | TAIFEX Proxy snapshots (2026-11-12) |

### 13．Gamma Wall

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Gamma Wall 價位 | 43,000.00 | TAIFEX Proxy (options-gamma-levels) |
| 對應到期月份 | 202611F2 | TAIFEX Proxy |
| 資料日期 | 2026-11-13 | TAIFEX Proxy (options-gamma-levels) |

### 14．Gamma Flip

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Gamma Flip 價位 | 43,236.34 | TAIFEX Proxy (options-gamma-levels) |
| 對應到期月份 | 202611F2 | TAIFEX Proxy |
| 資料日期 | 2026-11-13 | TAIFEX Proxy (options-gamma-levels) |

### 15．Max Pain

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Max Pain 價位 | 42,950 | TAIFEX Proxy |
| 對應到期月份 | 202611F2 | TAIFEX Proxy |
| 與前一交易日的變化 (2026-11-12→2026-11-13) | +0 | TAIFEX Proxy snapshots (2026-11-12) |

### 17．選擇權法人日盤、夜盤交易

| 法人 | 日盤多單 | 日盤空單 | 日盤淨 | 夜盤多單 | 夜盤空單 | 夜盤淨 | 淨變化 (日-夜) | 資料來源 |
|---|---|---|---|---|---|---|---|---|
| 外資 | 126,337 | 123,992 | +2,345 | unavailable | unavailable | unavailable | unavailable | TAIFEX Proxy |
| 投信 | 595 | 668 | -73 | unavailable | unavailable | unavailable | unavailable | TAIFEX Proxy |
| 自營商 | 105,554 | 101,694 | +3,860 | unavailable | unavailable | unavailable | unavailable | TAIFEX Proxy |
| 三大法人合計 | 232,486 | 226,354 | +6,132 | unavailable | unavailable | unavailable | unavailable | TAIFEX Proxy |
- 方法論：多方＝買Call＋賣Put（看多），空方＝賣Call＋買Put（看空），淨額＝看多－看空（已用 Call／Put 拆分頁交叉驗算一致）
- 公式：多方(買)－空方(賣)＝（買call＋賣put）－（賣call＋買put）＝看多－看空
- 速記：多＝BC＋SP、空＝SC＋BP

#### 法人多空力道表（金額・億元；上游千元／1e5）

| 法人 | 日多方力道 | 日空方力道 | 日淨多空力道 | 夜多方力道 | 夜空方力道 | 夜淨多空力道 | 日淨－夜淨 | 資料來源 |
|---|---|---|---|---|---|---|---|---|
| 外資 | 15.56 | 15.16 | +0.40 | 5.76 | 5.95 | -0.19 | +0.58 | TAIFEX Proxy |
| 投信 | 0.03 | 0.27 | -0.24 | 0.00 | 0.00 | +0 | -0.24 | TAIFEX Proxy |
| 自營商 | 11.95 | 12.58 | -0.64 | 4.48 | 4.05 | +0.43 | -1.07 | TAIFEX Proxy |
| 三大法人合計 | 27.53 | 28.01 | -0.48 | 10.25 | 10.00 | +0.25 | -0.73 | TAIFEX Proxy |

### 18．選擇權前十大

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 買權多方 OI | 23,549 | TAIFEX Proxy |
| 買權空方 OI | 28,526 | TAIFEX Proxy |
| 買權多空淨 OI | -4,977 | TAIFEX Proxy |
| 買權多空淨 OI 變化 (2026-11-11→2026-11-11) | +0 | TAIFEX Proxy snapshots (2026-11-12) |

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 賣權多方 OI | 14,352 | TAIFEX Proxy |
| 賣權空方 OI | 16,859 | TAIFEX Proxy |
| 賣權多空淨 OI | -2,507 | TAIFEX Proxy |
| 賣權多空淨 OI 變化 (2026-11-11→2026-11-11) | +0 | TAIFEX Proxy snapshots (2026-11-12) |
- 資料日期：買權 2026-11-11／賣權 2026-11-11 (TypeOfTraders=0 全部交易人；契約月份 202611)

#### 大戶流向（全日；前十大無日夜拆分）

| 項目 | 淨變化 | 區間 | 資料來源 |
|---|---|---|---|
| 期貨前十大 | +0 | 2026-11-11→2026-11-11 | TAIFEX Proxy snapshots (2026-11-12) |
| 買權前十大 | +0 | 2026-11-11→2026-11-11 | TAIFEX Proxy snapshots (2026-11-12) |
| 賣權前十大 | +0 | 2026-11-11→2026-11-11 | TAIFEX Proxy snapshots (2026-11-12) |

### 16．資料來源、時間、時區與狀態

- 資料來源：TAIFEX 經 Cloudflare Worker Proxy
- 資料日期：2026-11-13；資料時間：2026-11-13 02:40:19；時區：`Asia/Taipei`
- 日盤／夜盤標記：日盤收盤後 + 夜盤盤後
- 未取得欄位 (20)：taiex.open, taiex.high, taiex.low, listed_breadth.up, listed_breadth.down, listed_breadth.flat, listed_breadth.limit_up, listed_breadth.limit_down, otc_breadth.up, otc_breadth.down, otc_breadth.flat, otc_breadth.limit_up, otc_breadth.limit_down, margin.fin_yi, margin.fin_chg_yi, sbl.sale_bal, sbl.sale_chg, turnover.listed, turnover.otc, turnover.total
- 註記：無日期端點為最新盤勢快照 (判定資料日期 2026-11-12，非 T0 2026-11-13)，適用：日盤價／法人交易／夜盤／選擇權法人；T0 相符時不另標註
- 註記：futures-price-after-hours 日期 2026-11-12 非今日 2026-11-13，視為無新節次，不採用
- 註記：futures-institutional-after-hours 日期 2026-11-12 非今日 2026-11-13，視為無新節次，不採用
- 註記：options-institutional-after-hours 日期 2026-11-12 非今日 2026-11-13，視為無新節次，不採用
- 註記：Call/Put Wall 與 Max Pain 資料日期 2026-11-12 (T0 2026-11-13 端點不穩，採最新可得)
- 註記：夜盤開高低收未取得 (proxy 與官方皆無)，僅成交量/OI/結算價
- 註記：法人 OI 未取得
- 註記：法人交易量變化無昨日交易端點，標 unavailable
- 註記：選擇權 chain 資料日期 2026-11-12 (T0 2026-11-13 端點不穩，採最新可得)

## 五、資料來源、時間與完整性

- 期貨/匯率為最新報價，其餘為 T0 收盤資料；時間皆為 `Asia/Taipei`。
- taiex：`TWSE OpenAPI MI_INDEX (備援)`
- institutional：`twse-proxy /institutional`
- margin_short：`TWSE MI_MARGN + TPEX margin_balance (張)`
- margin_ratio：`前值遞補 (DATA 2026-11-12；當日三源皆失敗；民間估算；官方無每日序列)`
- sbl：`TWSE TWT93U + TPEX margin_sbl`
- 期貨選擇權：`TAIFEX Proxy`
- 新聞：台股 Yahoo／國際 Fed＋CNBC＋MarketWatch；台股 Yahoo（不足時財訊快報備援）/ 國際 Fed 公告＋CNBC＋MarketWatch RSS；Fed 無摘要；investing 港股為主已退役；cnyes CSR、wantgoo JS 算繪、中央社/台灣央行路徑待查，未採用
- 美股/亞股/期貨/匯率/ADR/商品：`Yahoo Finance Chart API`；美債：`Yahoo Finance (備援)`
- 註記：twse-proxy 連線失敗，TAIEX 改用 MI_INDEX 備援
- 註記：大盤開高低未取得 (FinMind 失敗；MI_INDEX 無此欄)
- 註記：twtazu_od 備援日期不符 (回傳舊資料)，上市漲跌標 unavailable
- 註記：上櫃 highlight 日期不符或缺值 (回傳 1151112, T0=1151113)
- 註記：三大法人回傳日期 20261112 (T0 20261113)，採用最新可得
- 註記：HiStock 未取得，融資餘額/增減標 unavailable (官方逐股加總僅有張數)
- 註記：融券沿用官方逐股加總 (張)
- 註記：融資維持率未取得 (三源皆失敗；官方無每日序列)
- 註記：融資維持率採前值遞補 (DATA 2026-11-12)，非 T0 2026-11-13
- 註記：上市 MI_MARGN / TWT96U 無日期欄，採用最新可得
- 本報告僅整理資料，不提供交易判斷。

## 六、期現選方向對照

**規則：** 趨勢偏多／空＝現貨、期貨OI、選擇權日淨三者同向；避險／對沖＝現貨與期選反向；日內反轉＝日淨與夜淨反向；缺值標示，不推估。選擇權多空為看多看空口徑。

| 法人 | 現貨買賣超(億) | 期貨OI淨(口) | 期貨日淨 | 期貨夜淨 | 選擇權日淨 | 選擇權夜淨 | 判定 | 期選組合 | 資料來源 |
|---|---|---|---|---|---|---|---|---|---|
| 外資 | -6.8 | unavailable | +4,733 | unavailable | +2,345 | unavailable | 資料不足 | 資料不足 | twse-proxy／TAIFEX Proxy |
| 投信 | +125.7 | unavailable | -2,969 | unavailable | -73 | unavailable | 資料不足 | 資料不足 | twse-proxy／TAIFEX Proxy |
| 自營商 | -65.4 | unavailable | -214 | unavailable | +3,860 | unavailable | 資料不足 | 資料不足 | twse-proxy／TAIFEX Proxy |
