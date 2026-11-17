# DATA_REPORT_20261118

- 報告日期：`2026-11-18`
- T0 交易日期：`2026-11-18`
- 資料產出時間：`2026-11-18 03:31:39`
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
| 加權指數 | 41,040.08 | 點 | TWSE OpenAPI MI_INDEX (備援) |
| 開盤 | unavailable | 點 | FinMind |
| 最高 | unavailable | 點 | FinMind |
| 最低 | unavailable | 點 | FinMind |
| 收盤 | 41,040.08 | 點 | TWSE OpenAPI MI_INDEX (備援) |
| 漲跌點數 | -2,635.04 | 點 | TWSE OpenAPI MI_INDEX (備援) |
| 漲跌幅 | -6.03 | % | TWSE OpenAPI MI_INDEX (備援) |
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
| 外資 | -380.9 | 億元 | twse-proxy /institutional |
| 投信 | -38.2 | 億元 | twse-proxy /institutional |
| 自營商 | -157.0 | 億元 | twse-proxy /institutional |
| 三大法人合計 | -576.1 | 億元 | twse-proxy /institutional |

### 4. 融資融券

**資料來源：** 上市+上櫃 `HiStock` (金額口徑)；維持率 `istock.tw`；備援官方逐股加總

| 項目 | 數值 | 單位 | 資料來源 |
|---|---|---|---|
| 融資餘額 | unavailable | 億元 | HiStock |
| 融資增減 | unavailable | 億元 | HiStock |
| 融券餘額 | 217,384 | 張 | HiStock |
| 融券增減 | 9,249 | 張 | HiStock |
| 融資維持率 | 170.70 | % | 前值遞補 (DATA 2026-11-17；當日三源皆失敗；民間估算；官方無每日序列) |

### 5. 借券資料

**資料來源：** 上市 `TWSE OpenAPI TWT96U` (可借餘額)、上櫃 `TPEX OpenAPI tpex_margin_sbl`

| 項目 | 數值 | 單位 | 資料來源 |
|---|---|---|---|
| 借券餘額 | 313,871 | 張 | TWSE TWT93U + TPEX margin_sbl |
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
| S&P 500 | ^GSPC | 7,326.02 | -90.57 | -1.22 | Yahoo Finance Chart API |
| Nasdaq Composite | ^IXIC | 24,235.93 | -273.83 | -1.12 | Yahoo Finance Chart API |
| Nasdaq 100 | ^NDX | 26,876.12 | -321.03 | -1.18 | Yahoo Finance Chart API |
| Dow Jones | ^DJI | 50,766.75 | -841.42 | -1.63 | Yahoo Finance Chart API |
| 費城半導體 SOX | ^SOX | 9,507.96 | -102.70 | -1.07 | Yahoo Finance Chart API |
| VIX | ^VIX | 25.61 | 2.70 | +11.79 | Yahoo Finance Chart API |

### 2. 亞洲主要指數

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 收盤／最新值 | 漲跌點 | 漲跌幅 | 資料來源 |
|---|---|---|---|---|---|
| 日經225 | ^N225 | 59,662.02 | -1,480.33 | -2.42 | Yahoo Finance Chart API |
| 韓國KOSPI | ^KS11 | 5,100.50 | -190.03 | -3.59 | Yahoo Finance Chart API |
| 香港恆生 | ^HSI | 23,753.84 | 116.24 | +0.49 | Yahoo Finance Chart API |
| 上海綜合 | 000001.SS | 3,602.57 | -31.78 | -0.87 | Yahoo Finance Chart API |
| 深圳成分 | 399001.SZ | 10,690.78 | -278.01 | -2.53 | Yahoo Finance Chart API |

### 3. 美股指數期貨

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 最新值 | 漲跌點 | 漲跌幅 | 資料來源 |
|---|---|---|---|---|---|
| S&P500期貨 | ES=F | 7,358.50 | -80.50 | -1.08 | Yahoo Finance Chart API |
| Nasdaq100期貨 | NQ=F | 27,021.00 | -263.25 | -0.96 | Yahoo Finance Chart API |
| 道瓊期貨 | YM=F | 50,899.00 | -771.00 | -1.49 | Yahoo Finance Chart API |
| Russell2000期貨 | RTY=F | 2,718.80 | -32.60 | -1.18 | Yahoo Finance Chart API |

### 4. 美國國債殖利率

**資料來源：** `U.S. Treasury Fiscal Data API` (失敗時備援 Treasury yield.xml 與 `Yahoo Finance`)

| 項目 | API 資料欄位／識別 | 殖利率 | 日變化 | 資料來源 |
|---|---|---|---|---|
| 美國 2 年期殖利率 | 2 Yr | 4.83 | -0.05 | U.S. Treasury yield.xml (網頁備援) |
| 美國 10 年期殖利率 | 10 Yr | 5.11 | -0.02 | Yahoo Finance (備援) |
| 美國 30 年期殖利率 | 30 Yr | 5.46 | -0.01 | Yahoo Finance (備援) |

### 5. 主要匯率

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 最新值 | 漲跌點 | 漲跌幅 | 資料來源 |
|---|---|---|---|---|---|
| USD/TWD | TWD=X | 32.91 | 0.04 | +0.11 | Yahoo Finance Chart API |
| DXY美元指數 | DX-Y.NYB | 103.46 | -0.09 | -0.09 | Yahoo Finance Chart API |
| USD/JPY | JPY=X | 159.35 | -0.43 | -0.27 | Yahoo Finance Chart API |
| USD/KRW | KRW=X | 1,335.18 | 1.93 | +0.14 | Yahoo Finance Chart API |

### 6. 台灣相關ADR

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 收盤／最新值 | 漲跌點 | 漲跌幅 | 資料來源 |
|---|---|---|---|---|---|
| 台積電ADR | TSM | 359.75 | -13.70 | -3.67 | Yahoo Finance Chart API |
| 聯電ADR | UMC | 14.06 | -0.28 | -1.99 | Yahoo Finance Chart API |
| 日月光ADR | ASX | 31.69 | -1.10 | -3.37 | Yahoo Finance Chart API |

### 7. 原油黃金Bitcoin

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 收盤／最新值 | 漲跌點 | 漲跌幅 | 資料來源 |
|---|---|---|---|---|---|
| WTI原油期貨 | CL=F | 86.05 | 0.33 | +0.38 | Yahoo Finance Chart API |
| 黃金期貨 | GC=F | 3,860.00 | 7.00 | +0.18 | Yahoo Finance Chart API |
| Bitcoin | BTC-USD | 63,603.51 | -1,252.33 | -1.93 | Yahoo Finance Chart API |

### 8. 重大經濟數據、央行事件與重大市場新聞

**資料來源：** 台股 `tw.stock.yahoo.com` (含內文摘要)；國際 `Fed 公告 RSS`＋`CNBC`＋`MarketWatch` (標題、來源、時間與連結)

- 事件1：股王摔下萬元 聯發科鴻海收紅撐住4萬關
  - 來源：Yahoo 台股；發布時間：2026-11-17T09:08:36Z；台北時間：2026-11-17 17:08
  - 摘要：台股急拉後再下殺，重挫947點險守4萬關卡！今(17)日加權指數終場下跌947.97點、跌幅2.31%，收40092.11點，上市成交金額9631.10億元。早盤一度重挫1253.63點，隨後買盤拉抬、急拉1747.39點翻紅，但反攻未能延
  - 原文連結：https://tw.stock.yahoo.com/news/%E5%8F%B0%E8%82%A1%E8%B7%8C%E8%BF%91%E5%8D%83%E9%BB%9E%E8%90%AC%E9%87%91%E8%82%A1%E6%B2%92%E4%BA%86%E3%80%814%E8%90%AC%E9%97%9C%E9%82%84%E5%9C%A8%EF%BC%81%E9%AB%98%E5%83%B9%E8%82%A1%E6%B7%AA%E9%87%8D%E7%81%BD%E5%8D%80-%E8%81%AF%E7%99%BC%E7%A7%91%E9%B4%BB%E6%B5%B7%E7%B6%A0%E5%9C%B0%E4%B8%AD%E9%96%8B%E7%B4%85%E8%8A%B1%EF%BD%9Cyahoo%E8%B2%A1%E7%B6%93%E6%8E%83%E6%8F%8F-090836112.html
- 事件2：韭菜翻車 旺矽、倉和爆違約交割波及6券商
  - 來源：Yahoo 台股；發布時間：2026-11-17T10:29:22Z；台北時間：2026-11-17 18:29
  - 摘要：台股近期震盪劇烈，又有上櫃個股爆出違約交割！櫃買中心今（17）日公告，半導體測試設備廠旺矽（6223）遭通報違約交割，金額高達5,406萬元；另一檔倉和（6538）也遭通報1,096.1萬元，兩檔合計達6,502.1萬元。值得注意的是，旺矽
  - 原文連結：https://tw.stock.yahoo.com/news/%E5%8F%88%E6%9C%89%E9%9F%AD%E8%8F%9C%E7%BF%BB%E8%BB%8A%EF%BC%81%E6%97%BA%E7%9F%BD%E4%BB%8A%E5%B9%B4%E5%86%8D%E7%88%865406%E8%90%AC%E5%85%83%E9%81%95%E7%B4%84%E4%BA%A4%E5%89%B2-%E5%80%89%E5%92%8C%E4%B9%9F%E9%81%AD%E9%80%9A%E5%A0%B1-102922897.html
- 事件3：5檔ETF換股 南亞科一口氣獲3檔納入
  - 來源：Yahoo 台股；發布時間：2026-11-17T09:25:11Z；台北時間：2026-11-17 17:25
  - 摘要：台灣指數公司今（17）日公布，不配息的0050之稱的凱基台灣TOP50 （009816）、中信小資高價30（00894）、中信綠能及電動車（00896）、兆豐台灣晶圓製造（00913）、元大台灣價值高息（00940）5檔案ETF換股，其中，
  - 原文連結：https://tw.stock.yahoo.com/news/5%E6%AA%94etf%E6%8F%9B%E8%82%A1%EF%BC%8100940%E3%80%8C10%E9%80%B210%E5%87%BA%E3%80%8D-%E5%88%AA%E8%8B%B1%E6%A5%AD%E9%81%94%E3%80%81%E8%81%AF%E7%99%BC%E7%A7%91%E5%A2%9E%E5%8D%97%E4%BA%9E%E7%A7%91-092511942.html
- 事件4：美選後藍色浪潮誰沾光？四大產業台鏈出列
  - 來源：Yahoo 台股；發布時間：2026-11-17T10:00:00Z；台北時間：2026-11-17 18:00
  - 摘要：美國期中選舉結果尚未開票完畢，但民主黨已確定拿下參眾兩院多數，並從共和黨手中奪下德州等6州的州長席位。這場選舉並不只是影響美國本土的政治版圖，同時也可能牽動美國能源投資、資料中心建置及台廠接單。美國期中選舉選什麼？川普的施政將受到哪些牽制？
  - 原文連結：https://tw.stock.yahoo.com/news/%E3%80%8C%E8%97%8D%E8%89%B2%E6%B5%AA%E6%BD%AE%E3%80%8D%E4%BE%86%E8%A5%B2%EF%BC%81%E7%BE%8E%E5%9C%8B%E6%9C%9F%E4%B8%AD%E9%81%B8%E8%88%89%E5%BE%8C%E5%93%AA%E4%BA%9B%E7%94%A2%E6%A5%AD%E6%9C%89%E6%9C%9B%E6%88%90%E8%B4%8F%E5%AE%B6%EF%BC%9F%E5%9B%9B%E5%A4%A7%E7%94%A2%E6%A5%AD%E5%8F%97%E6%83%A0%E5%8F%B0%E9%8F%88%E5%87%BA%E5%88%97%EF%BC%81%EF%BD%9C%E7%9B%A4%E9%BB%9E%E6%A6%82%E5%BF%B5%E8%82%A1-100000395.html
- 事件5：大到不能倒銀行揭榜 6家名單連3年不變
  - 來源：Yahoo 台股；發布時間：2026-11-17T08:23:26Z；台北時間：2026-11-17 16:23
  - 摘要：金管會今（17）日公布今年度系統性重要銀行（D-SIBs，俗稱大到不能倒銀行）名單，維持中信銀行、台北富邦銀行、國泰世華銀行、合庫銀行、兆豐銀行與第一銀行等6家銀行，名單跟2025年及2024年相同。D-SIBs是在金融市場是具有領導性地位
  - 原文連結：https://tw.stock.yahoo.com/news/%E5%A4%A7%E5%88%B0%E4%B8%8D%E8%83%BD%E5%80%92%EF%BC%81%E9%87%91%E7%AE%A1%E6%9C%83%E4%BB%8A%E5%85%AC%E5%B8%836%E5%AE%B6%E7%B3%BB%E7%B5%B1%E6%80%A7%E9%8A%80%E8%A1%8C%E5%90%8D%E5%96%AE-082326041.html
- 事件6：黃仁勳回鍋戰》親曝願重返輝達CEO　認錯喊話：這是我畢生心血
  - 來源：Yahoo 台股；發布時間：2026-11-17T17:11:10Z；台北時間：2026-11-18 01:11
  - 摘要：黃仁勳離開親手創辦輝達（NVIDIA）的第5天，美國時間17日終於親自表態願意重返執行長職務。他再次坦承個人生活犯下嚴重錯誤，願意承擔全部責任，面對各界要求他重新掌舵的呼聲，黃仁勳明確表示，只要董事會認為符合股東、員工、公司及美國的利益，他
  - 原文連結：https://tw.stock.yahoo.com/news/%E9%BB%83%E4%BB%81%E5%8B%B3%E5%9B%9E%E9%8D%8B%E6%88%B0-%E8%A6%AA%E6%9B%9D%E9%A1%98%E9%87%8D%E8%BF%94%E8%BC%9D%E9%81%94ceo-%E8%AA%8D%E9%8C%AF%E5%96%8A%E8%A9%B1-%E9%80%99%E6%98%AF%E6%88%91%E7%95%A2%E7%94%9F%E5%BF%83%E8%A1%80-171110305.html
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
- 事件10：Lisa Cook lawyer signals Fed governor won't attend Trump committee's hearing
  - 來源：CNBC；發布時間：Tue, 17 Nov 2026 16:03:38 GMT；台北時間：2026-11-18 00:03
  - 摘要：Cook's attorney sounded more hostile than ever in his first known letter to be sent in the matter since the GOP's drubbing in the Nov. 3 midterm elect
  - 原文連結：https://www.cnbc.com/2026/11/17/lisa-cook-trump-fed-committee-hearing.html
- 事件11：St. Louis Fed's Musalem says four more rate hikes may be needed in coming months
  - 來源：CNBC；發布時間：Tue, 17 Nov 2026 13:40:54 GMT；台北時間：2026-11-17 21:40
  - 摘要：The forecast represents one of the most hawkish views among policymakers.
  - 原文連結：https://www.cnbc.com/2026/11/17/alberto-musalem-fed-interest-rates.html
- 事件12：Demis Hassabis’ AI company raises $5 billion, months after he left as Google DeepMind CEO
  - 來源：CNBC；發布時間：Tue, 17 Nov 2026 13:58:07 GMT；台北時間：2026-11-17 21:58
  - 摘要：Isomorphic Labs is looking to develop new medicines using AI.
  - 原文連結：https://www.cnbc.com/2026/11/17/isomorphic-labs-series-c-ai-drug-discovery-.html


## 三、期貨

**資料來源：**
1. Cloudflare Workers：TAIFEX Proxy — https://taifex.grichtoyang.workers.dev/
2. TAIFEX Open API — https://openapi.taifex.com.tw/

近月契約月份：202611 (日盤成交量最大者)；交易日期：2026-11-18

### 1．台指期近月日盤行情

| 項目 | 數值 | 資料來源 |
|---|---|---|
| 開盤價 | 40,590 | TAIFEX Proxy |
| 最高價 | 41,828 | TAIFEX Proxy |
| 最低價 | 39,761 | TAIFEX Proxy |
| 收盤價 | 40,073 | TAIFEX Proxy |
| 漲跌點數 | -708 | TAIFEX Proxy |
| 漲跌幅 | -1.74 | TAIFEX Proxy |
| 成交量 | 138,833 | TAIFEX Proxy |
| 日盤高點及低點 | 41,828 / 39,761 | TAIFEX Proxy |

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
| 前十大交易人多方 OI | 39,917 | TAIFEX Proxy |
| 前十大交易人空方 OI | 35,820 | TAIFEX Proxy |
| 前十大交易人多空淨 OI | +4,097 | TAIFEX Proxy |
| 多空淨 OI 變化 (2026-11-16→2026-11-16) | +0 | TAIFEX Proxy snapshots (2026-11-17) |
- 資料日期：2026-11-16 (TypeOfTraders=0 全部交易人；契約月份 202611)

### 5．日盤、夜盤法人交易資料

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 外資日盤多單交易量 | 153,931 | TAIFEX Proxy |
| 外資日盤空單交易量 | 155,075 | TAIFEX Proxy |
| 外資日盤多空淨交易量 | -1,144 | TAIFEX Proxy |
| 外資夜盤多單交易量 | unavailable | TAIFEX Proxy |
| 外資夜盤空單交易量 | unavailable | TAIFEX Proxy |
| 外資夜盤多空淨交易量 | unavailable | TAIFEX Proxy |
| 外資日盤／夜盤交易量變化 | unavailable | TAIFEX Proxy |
| 投信日盤多空淨交易量 | -1,180 | TAIFEX Proxy |
| 投信夜盤多空淨交易量 | unavailable | TAIFEX Proxy |
| 投信日盤／夜盤交易量變化 | unavailable | TAIFEX Proxy |
| 自營商日盤多空淨交易量 | -1,820 | TAIFEX Proxy |
| 自營商夜盤多空淨交易量 | unavailable | TAIFEX Proxy |
| 自營商日盤／夜盤交易量變化 | unavailable | TAIFEX Proxy |
| 三大法人日盤多空淨交易量 | -4,144 | TAIFEX Proxy |
| 三大法人夜盤多空淨交易量 | unavailable | TAIFEX Proxy |
| 法人日盤交易金額淨額 (億元) | -341.2 | TAIFEX Proxy |
| 法人夜盤交易金額淨額 (億元) | unavailable | TAIFEX Proxy |

### 6．期貨與現貨關係

| 項目 | 數值 | 資料來源 |
|---|---|---|
| 台指期近月價格 | 40,073 | TAIFEX Proxy |
| 加權指數價格 | 41,040.08 | TWSE OpenAPI MI_INDEX (備援) |
| 台指期與加權指數價差 | -967.08 | TAIFEX Proxy+TWSE OpenAPI MI_INDEX (備援) |
| 價差百分比 | -2.36 | TAIFEX Proxy+TWSE OpenAPI MI_INDEX (備援) |
| 日盤基差 | -967.08 | TAIFEX Proxy+TWSE OpenAPI MI_INDEX (備援) |
| 夜盤價格相對日盤收盤的變化 | unavailable | 端點未提供 |

### 7．日盤、夜盤與籌碼變化對照

#### 7.1 日夜盤價格與成交量對照 (變化 = 日盤 - 夜盤)

| 項目 | 日盤 | 夜盤 | 變化 (日-夜) | 資料來源 |
|---|---|---|---|---|
| 收盤價 | 40,073 | unavailable | unavailable | TAIFEX Proxy |
| 成交量 | 138,833 | unavailable | unavailable | TAIFEX Proxy |
- 台指期總 OI 前日變化：+0（來源：TAIFEX Proxy）


#### 7.2 法人籌碼日夜盤對照 (淨變化 = 日盤淨 - 夜盤淨；OI 為日盤收盤後總量，前日變化另列)

| 法人 | 交易量 |  |  |  |  |  |  | 未平倉量 |  |  |  | 資料來源 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|  | **日盤多單** | **日盤空單** | **日盤淨** | **夜盤多單** | **夜盤空單** | **夜盤淨** | **淨變化 (日-夜)** | **OI多方** | **OI空方** | **OI淨** | **OI前日變化** |  |
| 外資 | 153,931 | 155,075 | -1,144 | unavailable | unavailable | unavailable | unavailable | unavailable | unavailable | unavailable | unavailable | TAIFEX Proxy |
| 投信 | 33,611 | 34,791 | -1,180 | unavailable | unavailable | unavailable | unavailable | unavailable | unavailable | unavailable | unavailable | TAIFEX Proxy |
| 自營商 | 15,358 | 17,178 | -1,820 | unavailable | unavailable | unavailable | unavailable | unavailable | unavailable | unavailable | unavailable | TAIFEX Proxy |
| 三大法人合計 | 202,900 | 207,044 | -4,144 | unavailable | unavailable | unavailable | unavailable | 0 | 0 | +0 | +0 | TAIFEX Proxy |

#### 7.3 前十大交易人日夜盤對照 (OI 無日夜拆分，列收盤後總量)

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 前十大交易人多方 OI | 39,917 | TAIFEX Proxy |
| 前十大交易人空方 OI | 35,820 | TAIFEX Proxy |
| 前十大交易人多空淨 OI | +4,097 | TAIFEX Proxy |
| 前十大交易人多空淨 OI 變化 (2026-11-16→2026-11-16) | +0 | TAIFEX Proxy snapshots (2026-11-17) |

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
| 交易日期 | 2026-11-18 | TAIFEX Proxy |
| 到期月份／到期日 | 202611 | TAIFEX Proxy |
| 資料更新時間 | 2026-11-18 03:31:39 | 本機 |
| 日盤／夜盤標記 | 日盤收盤後資料 | TAIFEX Proxy |

### 2．Call 總成交量、OI、OI 增減

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Call 總成交量 | 258,518 | TAIFEX Proxy |
| Call 總未平倉量 OI | 142,228 | TAIFEX Proxy |
| Call OI 增減 (2026-11-17→2026-11-18) | +0 | TAIFEX Proxy snapshots (2026-11-17) |

### 3．Put 總成交量、OI、OI 增減

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Put 總成交量 | 206,995 | TAIFEX Proxy |
| Put 總未平倉量 OI | 78,316 | TAIFEX Proxy |
| Put OI 增減 (2026-11-17→2026-11-18) | +0 | TAIFEX Proxy snapshots (2026-11-17) |

### 4．Call／Put 比例與變化

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Call／Put 成交量比例 | 1.25 | TAIFEX Proxy |
| Call／Put 未平倉量比例 | 1.82 | TAIFEX Proxy |
| Put／Call Ratio | 0.55 | TAIFEX Proxy |
| Call／Put 比例變化 (量比 2026-11-13→2026-11-16) | -17.65 | TAIFEX Proxy |
| 與前一交易日比較 (OI 比 2026-11-13→2026-11-16) | -3.96 | TAIFEX Proxy |
**資料來源：** 比例 `TAIFEX Proxy chain`；變化 `TAIFEX Proxy PutCallRatio`

### 5．外資 Call／Put 部位

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 外資 Call日買 | 66,734 | TAIFEX Proxy |
| 外資 Call日賣 | 64,552 | TAIFEX Proxy |
| 外資 Call日淨 | +2,182 | TAIFEX Proxy |
| 外資 Put日買 | 68,854 | TAIFEX Proxy |
| 外資 Put日賣 | 68,672 | TAIFEX Proxy |
| 外資 Put日淨 | +182 | TAIFEX Proxy |
| 外資 Call夜買 | 28,132 | TAIFEX Proxy |
| 外資 Call夜賣 | 27,501 | TAIFEX Proxy |
| 外資 Call夜淨 | +631 | TAIFEX Proxy |
| 外資 Put夜買 | 15,841 | TAIFEX Proxy |
| 外資 Put夜賣 | 16,953 | TAIFEX Proxy |
| 外資 Put夜淨 | -1,112 | TAIFEX Proxy |
| 外資 日盤淨總量 | +2,000 | TAIFEX Proxy |
| 外資 Call日夜淨增減 (日－夜) | +1,551 | TAIFEX Proxy |
| 外資 Put日夜淨增減 (日－夜) | +1,294 | TAIFEX Proxy |

### 6．自營商 Call／Put 部位

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 自營商 Call日買 | 69,887 | TAIFEX Proxy |
| 自營商 Call日賣 | 73,892 | TAIFEX Proxy |
| 自營商 Call日淨 | -4,005 | TAIFEX Proxy |
| 自營商 Put日買 | 64,742 | TAIFEX Proxy |
| 自營商 Put日賣 | 64,997 | TAIFEX Proxy |
| 自營商 Put日淨 | -255 | TAIFEX Proxy |
| 自營商 Call夜買 | 17,481 | TAIFEX Proxy |
| 自營商 Call夜賣 | 20,567 | TAIFEX Proxy |
| 自營商 Call夜淨 | -3,086 | TAIFEX Proxy |
| 自營商 Put夜買 | 19,141 | TAIFEX Proxy |
| 自營商 Put夜賣 | 18,195 | TAIFEX Proxy |
| 自營商 Put夜淨 | +946 | TAIFEX Proxy |
| 自營商 日盤淨總量 | -3,750 | TAIFEX Proxy |
| 自營商 Call日夜淨增減 (日－夜) | -919 | TAIFEX Proxy |
| 自營商 Put日夜淨增減 (日－夜) | -1,201 | TAIFEX Proxy |

### 7．主要 Call OI 集中區

| 項目 | 履約價 | OI | 資料來源 |
|---|---|---|---|
| Call OI 第1大履約價 | 46,000 | 8,984 | TAIFEX Proxy |
| Call OI 第2大履約價 | 43,500 | 6,804 | TAIFEX Proxy |
| Call OI 第3大履約價 | 44,000 | 6,330 | TAIFEX Proxy |
| Call OI 最大履約價 | 46,000 | 8,984 | TAIFEX Proxy |

#### Call OI 分布明細 Top10 (機器可讀，到期月份 202611)

| # | 履約價 | OI | 佔比 | 資料來源 |
|---|---|---|---|---|
| C1 | 46,000 | 8,984 | 6.32% | TAIFEX Proxy |
| C2 | 43,500 | 6,804 | 4.78% | TAIFEX Proxy |
| C3 | 44,000 | 6,330 | 4.45% | TAIFEX Proxy |
| C4 | 45,000 | 4,173 | 2.93% | TAIFEX Proxy |
| C5 | 48,000 | 3,871 | 2.72% | TAIFEX Proxy |
| C6 | 43,000 | 3,538 | 2.49% | TAIFEX Proxy |
| C7 | 47,500 | 3,524 | 2.48% | TAIFEX Proxy |
| C8 | 46,500 | 3,464 | 2.44% | TAIFEX Proxy |
| C9 | 47,000 | 3,313 | 2.33% | TAIFEX Proxy |
| C10 | 44,500 | 2,816 | 1.98% | TAIFEX Proxy |


### 8．主要 Put OI 集中區

| 項目 | 履約價 | OI | 資料來源 |
|---|---|---|---|
| Put OI 第1大履約價 | 33,700 | 11,788 | TAIFEX Proxy |
| Put OI 第2大履約價 | 38,000 | 2,997 | TAIFEX Proxy |
| Put OI 第3大履約價 | 40,000 | 2,889 | TAIFEX Proxy |
| Put OI 最大履約價 | 33,700 | 11,788 | TAIFEX Proxy |

#### Put OI 分布明細 Top10 (機器可讀，到期月份 202611)

| # | 履約價 | OI | 佔比 | 資料來源 |
|---|---|---|---|---|
| P1 | 33,700 | 11,788 | 15.05% | TAIFEX Proxy |
| P2 | 38,000 | 2,997 | 3.83% | TAIFEX Proxy |
| P3 | 40,000 | 2,889 | 3.69% | TAIFEX Proxy |
| P4 | 36,000 | 2,750 | 3.51% | TAIFEX Proxy |
| P5 | 37,000 | 2,241 | 2.86% | TAIFEX Proxy |
| P6 | 39,000 | 2,213 | 2.83% | TAIFEX Proxy |
| P7 | 42,000 | 1,959 | 2.5% | TAIFEX Proxy |
| P8 | 36,500 | 1,789 | 2.28% | TAIFEX Proxy |
| P9 | 35,000 | 1,568 | 2.0% | TAIFEX Proxy |
| P10 | 44,000 | 1,536 | 1.96% | TAIFEX Proxy |


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
| 對應到期月份 | 202611 | TAIFEX Proxy |
| 與前一交易日的變化 (2026-11-17→2026-11-18) | +0 | TAIFEX Proxy snapshots (2026-11-17) |

### 12．Put Wall

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Put Wall 價位 | 33,700 | TAIFEX Proxy |
| 對應到期月份 | 202611 | TAIFEX Proxy |
| 與前一交易日的變化 (2026-11-17→2026-11-18) | +0 | TAIFEX Proxy snapshots (2026-11-17) |

### 13．Gamma Wall

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Gamma Wall 價位 | 40,000.00 | TAIFEX Proxy (options-gamma-levels) |
| 對應到期月份 | 202611 | TAIFEX Proxy |
| 資料日期 | 2026-11-18 | TAIFEX Proxy (options-gamma-levels) |

### 14．Gamma Flip

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Gamma Flip 價位 | 40,423.40 | TAIFEX Proxy (options-gamma-levels) |
| 對應到期月份 | 202611 | TAIFEX Proxy |
| 資料日期 | 2026-11-18 | TAIFEX Proxy (options-gamma-levels) |

### 15．Max Pain

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Max Pain 價位 | 41,600 | TAIFEX Proxy |
| 對應到期月份 | 202611 | TAIFEX Proxy |
| 與前一交易日的變化 (2026-11-17→2026-11-18) | +0 | TAIFEX Proxy snapshots (2026-11-17) |

### 17．選擇權法人日盤、夜盤交易

| 法人 | 日盤多單 | 日盤空單 | 日盤淨 | 夜盤多單 | 夜盤空單 | 夜盤淨 | 淨變化 (日-夜) | 資料來源 |
|---|---|---|---|---|---|---|---|---|
| 外資 | 135,406 | 133,406 | +2,000 | unavailable | unavailable | unavailable | unavailable | TAIFEX Proxy |
| 投信 | 8,005 | 18,220 | -10,215 | unavailable | unavailable | unavailable | unavailable | TAIFEX Proxy |
| 自營商 | 134,884 | 138,634 | -3,750 | unavailable | unavailable | unavailable | unavailable | TAIFEX Proxy |
| 三大法人合計 | 278,295 | 290,260 | -11,965 | unavailable | unavailable | unavailable | unavailable | TAIFEX Proxy |
- 方法論：多方＝買Call＋賣Put（看多），空方＝賣Call＋買Put（看空），淨額＝看多－看空（已用 Call／Put 拆分頁交叉驗算一致）
- 公式：多方(買)－空方(賣)＝（買call＋賣put）－（賣call＋買put）＝看多－看空
- 速記：多＝BC＋SP、空＝SC＋BP

#### 法人多空力道表（金額・億元；上游千元／1e5）

| 法人 | 日多方力道 | 日空方力道 | 日淨多空力道 | 夜多方力道 | 夜空方力道 | 夜淨多空力道 | 日淨－夜淨 | 資料來源 |
|---|---|---|---|---|---|---|---|---|
| 外資 | 24.03 | 21.58 | +2.45 | 5.96 | 5.34 | +0.62 | +1.83 | TAIFEX Proxy |
| 投信 | 0.17 | 11.21 | -11.04 | 0.00 | 0.00 | +0.00 | -11.04 | TAIFEX Proxy |
| 自營商 | 29.03 | 21.62 | +7.41 | 5.68 | 6.23 | -0.55 | +7.96 | TAIFEX Proxy |
| 三大法人合計 | 53.23 | 54.40 | -1.18 | 11.64 | 11.57 | +0.07 | -1.25 | TAIFEX Proxy |

### 18．選擇權前十大

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 買權多方 OI | 46,765 | TAIFEX Proxy |
| 買權空方 OI | 70,976 | TAIFEX Proxy |
| 買權多空淨 OI | -24,211 | TAIFEX Proxy |
| 買權多空淨 OI 變化 (2026-11-16→2026-11-16) | +0 | TAIFEX Proxy snapshots (2026-11-17) |

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 賣權多方 OI | 30,112 | TAIFEX Proxy |
| 賣權空方 OI | 28,929 | TAIFEX Proxy |
| 賣權多空淨 OI | +1,183 | TAIFEX Proxy |
| 賣權多空淨 OI 變化 (2026-11-16→2026-11-16) | +0 | TAIFEX Proxy snapshots (2026-11-17) |
- 資料日期：買權 2026-11-16／賣權 2026-11-16 (TypeOfTraders=0 全部交易人；契約月份 202611)

#### 大戶流向（全日；前十大無日夜拆分）

| 項目 | 淨變化 | 區間 | 資料來源 |
|---|---|---|---|
| 期貨前十大 | +0 | 2026-11-16→2026-11-16 | TAIFEX Proxy snapshots (2026-11-17) |
| 買權前十大 | +0 | 2026-11-16→2026-11-16 | TAIFEX Proxy snapshots (2026-11-17) |
| 賣權前十大 | +0 | 2026-11-16→2026-11-16 | TAIFEX Proxy snapshots (2026-11-17) |

### 16．資料來源、時間、時區與狀態

- 資料來源：TAIFEX 經 Cloudflare Worker Proxy
- 資料日期：2026-11-18；資料時間：2026-11-18 03:31:39；時區：`Asia/Taipei`
- 日盤／夜盤標記：日盤收盤後 + 夜盤盤後
- 未取得欄位 (20)：taiex.open, taiex.high, taiex.low, listed_breadth.up, listed_breadth.down, listed_breadth.flat, listed_breadth.limit_up, listed_breadth.limit_down, otc_breadth.up, otc_breadth.down, otc_breadth.flat, otc_breadth.limit_up, otc_breadth.limit_down, margin.fin_yi, margin.fin_chg_yi, sbl.sale_bal, sbl.sale_chg, turnover.listed, turnover.otc, turnover.total
- 註記：無日期端點為最新盤勢快照 (判定資料日期 2026-11-17，非 T0 2026-11-18)，適用：日盤價／法人交易／夜盤／選擇權法人；T0 相符時不另標註
- 註記：futures-price-after-hours 日期 2026-11-17 非今日 2026-11-18，視為無新節次，不採用
- 註記：futures-institutional-after-hours 日期 2026-11-17 非今日 2026-11-18，視為無新節次，不採用
- 註記：options-institutional-after-hours 日期 2026-11-17 非今日 2026-11-18，視為無新節次，不採用
- 註記：Call/Put Wall 與 Max Pain 資料日期 2026-11-17 (T0 2026-11-18 端點不穩，採最新可得)
- 註記：夜盤開高低收未取得 (proxy 與官方皆無)，僅成交量/OI/結算價
- 註記：法人 OI 未取得
- 註記：法人交易量變化無昨日交易端點，標 unavailable
- 註記：選擇權 chain 資料日期 2026-11-17 (T0 2026-11-18 端點不穩，採最新可得)

## 五、資料來源、時間與完整性

- 期貨/匯率為最新報價，其餘為 T0 收盤資料；時間皆為 `Asia/Taipei`。
- taiex：`TWSE OpenAPI MI_INDEX (備援)`
- institutional：`twse-proxy /institutional`
- margin_short：`TWSE MI_MARGN + TPEX margin_balance (張)`
- margin_ratio：`前值遞補 (DATA 2026-11-17；當日三源皆失敗；民間估算；官方無每日序列)`
- sbl：`TWSE TWT93U + TPEX margin_sbl`
- 期貨選擇權：`TAIFEX Proxy`
- 新聞：台股 Yahoo／國際 Fed＋CNBC＋MarketWatch；台股 Yahoo（不足時財訊快報備援）/ 國際 Fed 公告＋CNBC＋MarketWatch RSS；Fed 無摘要；investing 港股為主已退役；cnyes CSR、wantgoo JS 算繪、中央社/台灣央行路徑待查，未採用
- 美股/亞股/期貨/匯率/ADR/商品：`Yahoo Finance Chart API`；美債：`Yahoo Finance (備援)`
- 註記：twse-proxy 連線失敗，TAIEX 改用 MI_INDEX 備援
- 註記：大盤開高低未取得 (FinMind 失敗；MI_INDEX 無此欄)
- 註記：twtazu_od 備援日期不符 (回傳舊資料)，上市漲跌標 unavailable
- 註記：上櫃 highlight 日期不符或缺值 (回傳 1151117, T0=1151118)
- 註記：三大法人回傳日期 20261117 (T0 20261118)，採用最新可得
- 註記：HiStock 未取得，融資餘額/增減標 unavailable (官方逐股加總僅有張數)
- 註記：融券沿用官方逐股加總 (張)
- 註記：融資維持率未取得 (三源皆失敗；官方無每日序列)
- 註記：融資維持率採前值遞補 (DATA 2026-11-17)，非 T0 2026-11-18
- 註記：上市 MI_MARGN / TWT96U 無日期欄，採用最新可得
- 本報告僅整理資料，不提供交易判斷。

## 六、期現選方向對照

**規則：** 趨勢偏多／空＝現貨、期貨OI、選擇權日淨三者同向；避險／對沖＝現貨與期選反向；日內反轉＝日淨與夜淨反向；缺值標示，不推估。選擇權多空為看多看空口徑。

| 法人 | 現貨買賣超(億) | 期貨OI淨(口) | 期貨日淨 | 期貨夜淨 | 選擇權日淨 | 選擇權夜淨 | 判定 | 期選組合 | 資料來源 |
|---|---|---|---|---|---|---|---|---|---|
| 外資 | -380.9 | unavailable | -1,144 | unavailable | +2,000 | unavailable | 資料不足 | 資料不足 | twse-proxy／TAIFEX Proxy |
| 投信 | -38.2 | unavailable | -1,180 | unavailable | -10,215 | unavailable | 資料不足 | 資料不足 | twse-proxy／TAIFEX Proxy |
| 自營商 | -157.0 | unavailable | -1,820 | unavailable | -3,750 | unavailable | 資料不足 | 資料不足 | twse-proxy／TAIFEX Proxy |
