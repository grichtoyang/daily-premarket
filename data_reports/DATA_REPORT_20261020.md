# DATA_REPORT_20261020

- 報告日期：`2026-10-21`
- T0 交易日期：`2026-10-20`
- 資料產出時間：`2026-10-21 10:28:45`
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
| 加權指數 | 46,292.93 | 點 | twse-proxy |
| 開盤 | 46,712.57 | 點 | FinMind TaiwanStockPrice TAIEX |
| 最高 | 46,967.91 | 點 | FinMind TaiwanStockPrice TAIEX |
| 最低 | 46,163.03 | 點 | FinMind TaiwanStockPrice TAIEX |
| 收盤 | 46,292.93 | 點 | twse-proxy |
| 漲跌點數 | -529.15 | 點 | twse-proxy |
| 漲跌幅 | -1.13 | % | twse-proxy |
| 成交金額 | 8,029.5 | 億元 | twse-proxy market_statistics |

### 2. 市場漲跌家數

#### 2.1 上市公司

**資料來源：** `Cloudflare Worker：twse-proxy` (備援 `TWSE OpenAPI twtazu_od`)

| 項目 | 家數 | 資料來源 |
|---|---|---|
| 上漲家數 | 269 | twse-proxy |
| 下跌家數 | 701 | twse-proxy |
| 平盤家數 | 104 | twse-proxy |
| 漲停家數 | 8 | twse-proxy |
| 跌停家數 | 0 | twse-proxy |

#### 2.2 上櫃公司

**資料來源：** `TPEX OpenAPI tpex_mainborad_highlight`

| 項目 | 家數 | 資料來源 |
|---|---|---|
| 上漲家數 | 316 | TPEX OpenAPI tpex_mainborad_highlight |
| 下跌家數 | 451 | TPEX OpenAPI tpex_mainborad_highlight |
| 平盤家數 | 102 | TPEX OpenAPI tpex_mainborad_highlight |
| 漲停家數 | 24 | TPEX OpenAPI tpex_mainborad_highlight |
| 跌停家數 | 0 | TPEX OpenAPI tpex_mainborad_highlight |

### 3. 三大法人現貨買賣超

**資料來源：** `TWSE RWD BFI82U`

| 法人別 | 買賣超金額 | 單位 | 資料來源 |
|---|---|---|---|
| 外資 | -795.4 | 億元 | twse-proxy /institutional |
| 投信 | +187.6 | 億元 | twse-proxy /institutional |
| 自營商 | -355.8 | 億元 | twse-proxy /institutional |
| 三大法人合計 | -963.6 | 億元 | twse-proxy /institutional |

### 4. 融資融券

**資料來源：** 上市+上櫃 `HiStock` (金額口徑)；維持率 `istock.tw`；備援官方逐股加總

| 項目 | 數值 | 單位 | 資料來源 |
|---|---|---|---|
| 融資餘額 | 8,531.1 | 億元 | HiStock 上市+上櫃融資融券 (金額口徑) |
| 融資增減 | -27.3 | 億元 | HiStock 上市+上櫃融資融券 (金額口徑) |
| 融券餘額 | 254,996 | 張 | HiStock 上市+上櫃融資融券 (金額口徑) |
| 融券增減 | 16,098 | 張 | HiStock 上市+上櫃融資融券 (金額口徑) |
| 融資維持率 | 178.93 | % | wantgoo 大盤融資維持率 (資料日期 2026-10-20；民間估算；官方無每日序列；gapfill 自動補登) |

### 5. 借券資料

**資料來源：** 上市 `TWSE OpenAPI TWT96U` (可借餘額)、上櫃 `TPEX OpenAPI tpex_margin_sbl`

| 項目 | 數值 | 單位 | 資料來源 |
|---|---|---|---|
| 借券餘額 | 4,593,735 | 張 | TWSE TWT93U + TPEX margin_sbl |
| 借券賣出餘額 | 39,084 | 張 | TWSE TWT93U + TPEX margin_sbl |
| 借券賣出增減 | 2,097 | 張 | TWSE TWT93U + TPEX margin_sbl |

### 6. 市場成交結構

**資料來源：** 上市 `twse-proxy market_statistics`、上櫃 `TPEX OpenAPI tpex_mainborad_highlight`

| 項目 | 成交金額 | 單位 | 資料來源 |
|---|---|---|---|
| 上市成交金額 | 8,029.5 | 億元 | twse-proxy market_statistics |
| 上櫃成交金額 | 2,067.5 | 億元 | TPEX OpenAPI tpex_mainborad_highlight |
| 上市櫃成交金額合計 | 10,096.9 | 億元 | twse-proxy market_statistics+TPEX OpenAPI tpex_mainborad_highlight |

## 二、重要市場

### 1. 美股指數

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 收盤／最新值 | 漲跌點 | 漲跌幅 | 資料來源 |
|---|---|---|---|---|---|
| S&P 500 | ^GSPC | 7,712.57 | 21.84 | +0.28 | Yahoo Finance Chart API |
| Nasdaq Composite | ^IXIC | 26,424.82 | -6.07 | -0.02 | Yahoo Finance Chart API |
| Nasdaq 100 | ^NDX | 29,490.28 | -39.07 | -0.13 | Yahoo Finance Chart API |
| Dow Jones | ^DJI | 52,495.88 | 529.85 | +1.02 | Yahoo Finance Chart API |
| 費城半導體 SOX | ^SOX | 11,283.81 | -32.53 | -0.29 | Yahoo Finance Chart API |
| VIX | ^VIX | 17.31 | -1.13 | -6.13 | Yahoo Finance Chart API |

### 2. 亞洲主要指數

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 收盤／最新值 | 漲跌點 | 漲跌幅 | 資料來源 |
|---|---|---|---|---|---|
| 日經225 | ^N225 | 64,874.90 | 799.48 | +1.25 | Yahoo Finance Chart API |
| 韓國KOSPI | ^KS11 | 5,786.89 | 234.15 | +4.22 | Yahoo Finance Chart API |
| 香港恆生 | ^HSI | 23,935.14 | 67.40 | +0.28 | Yahoo Finance Chart API |
| 上海綜合 | 000001.SS | 3,736.18 | 0.81 | +0.02 | Yahoo Finance Chart API |
| 深圳成分 | 399001.SZ | 11,850.22 | 48.93 | +0.41 | Yahoo Finance Chart API |

### 3. 美股指數期貨

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 最新值 | 漲跌點 | 漲跌幅 | 資料來源 |
|---|---|---|---|---|---|
| S&P500期貨 | ES=F | 7,779.00 | 23.75 | +0.31 | Yahoo Finance Chart API |
| Nasdaq100期貨 | NQ=F | 29,967.75 | 292.50 | +0.99 | Yahoo Finance Chart API |
| 道瓊期貨 | YM=F | 52,684.00 | -35.00 | -0.07 | Yahoo Finance Chart API |
| Russell2000期貨 | RTY=F | 2,786.30 | -0.60 | -0.02 | Yahoo Finance Chart API |

### 4. 美國國債殖利率

**資料來源：** `U.S. Treasury Fiscal Data API` (失敗時備援 Treasury yield.xml 與 `Yahoo Finance`)

| 項目 | API 資料欄位／識別 | 殖利率 | 日變化 | 資料來源 |
|---|---|---|---|---|
| 美國 2 年期殖利率 | 2 Yr | 4.79 | 0.02 | U.S. Treasury yield.xml (網頁備援) |
| 美國 10 年期殖利率 | 10 Yr | 5.12 | -0.02 | Yahoo Finance (備援) |
| 美國 30 年期殖利率 | 30 Yr | 5.43 | -0.05 | Yahoo Finance (備援) |

### 5. 主要匯率

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 最新值 | 漲跌點 | 漲跌幅 | 資料來源 |
|---|---|---|---|---|---|
| USD/TWD | TWD=X | 32.56 | 0.08 | +0.24 | Yahoo Finance Chart API |
| DXY美元指數 | DX-Y.NYB | 101.78 | 0.05 | +0.05 | Yahoo Finance Chart API |
| USD/JPY | JPY=X | 158.23 | -0.29 | -0.18 | Yahoo Finance Chart API |
| USD/KRW | KRW=X | 1,327.08 | -2.92 | -0.22 | Yahoo Finance Chart API |

### 6. 台灣相關ADR

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 收盤／最新值 | 漲跌點 | 漲跌幅 | 資料來源 |
|---|---|---|---|---|---|
| 台積電ADR | TSM | 425.08 | 4.86 | +1.16 | Yahoo Finance Chart API |
| 聯電ADR | UMC | 19.67 | -0.41 | -2.04 | Yahoo Finance Chart API |
| 日月光ADR | ASX | 40.77 | -0.03 | -0.07 | Yahoo Finance Chart API |

### 7. 原油黃金Bitcoin

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 收盤／最新值 | 漲跌點 | 漲跌幅 | 資料來源 |
|---|---|---|---|---|---|
| WTI原油期貨 | CL=F | 99.18 | -2.61 | -2.56 | Yahoo Finance Chart API |
| 黃金期貨 | GC=F | 4,136.20 | -6.40 | -0.15 | Yahoo Finance Chart API |
| Bitcoin | BTC-USD | 82,665.83 | 812.29 | +0.99 | Yahoo Finance Chart API |

### 8. 重大經濟數據、央行事件與重大市場新聞

**資料來源：** 台股 `tw.stock.yahoo.com` (含內文摘要)；國際 `Fed 公告 RSS`＋`CNBC`＋`MarketWatch` (標題、來源、時間與連結)

- 事件1：台積電法說後首開紅！分析師：本益比17倍真的不貴
  - 來源：Yahoo 台股；發布時間：2026-10-21T01:30:05Z；台北時間：2026-10-21 09:30
  - 摘要：魏哲家主持台積電（2330）15日法說會至今，股價已連跌四天，今首開紅盤，外資法說會前喊目標價4410元，今又傳出高盛最新報告竟看壞台灣半導體，建議「對沖」或「做空」，所設護國神山終於隨在美ADR上漲1.16%，台北現股一早就以上漲20元開
  - 原文連結：https://tw.stock.yahoo.com/news/%E5%8F%B0%E7%A9%8D%E9%9B%BB%E6%B3%95%E8%AA%AA%E6%9C%83%E5%BE%8C%E9%A6%96%E9%96%8B%E7%B4%85%E7%9B%A4-%E6%9C%80%E9%AB%98%E6%BC%B225%E5%85%83%E8%BF%BD%E9%BD%8Aadr%E6%BC%B2%E5%B9%85-%E5%88%86%E6%9E%90%E5%B8%AB%EF%BC%9A%E6%9C%AC%E7%9B%8A%E6%AF%9417%E5%80%8D%E7%9C%9F%E4%B8%8D%E8%B2%B4-013005608.html
- 事件2：記憶體三雄強勢表態全面走揚 領概念族群絕地反攻
  - 來源：Yahoo 台股；發布時間：2026-10-21T01:43:00Z；台北時間：2026-10-21 09:43
  - 摘要：台股今（21）日開盤大漲超過790點，記憶體族群成為盤面焦點全面走揚。其中南亞科、華邦電與旺宏同步強勢表態，華邦電與南亞科漲幅皆超過3%，晶豪科、力成及群聯也表現亮眼，帶動整體記憶體概念股紅通通一片，展現強勁抗跌與上攻動能，引領台股重返強勢
  - 原文連結：https://tw.stock.yahoo.com/news/%E9%87%8D%E5%9B%9E%E6%88%B0%E5%A0%B4-%E8%A8%98%E6%86%B6%E9%AB%94%E4%B8%89%E9%9B%84%E5%85%A8%E9%9D%A2%E7%99%BC%E7%87%99-%E9%A0%98%E8%BB%8D%E6%97%8F%E7%BE%A4%E7%B5%95%E5%9C%B0%E5%8F%8D%E6%94%BB-014300989.html
- 事件3：「11檔秒亮燈」台股開盤飆逾700點火速收復47K
  - 來源：Yahoo 台股；發布時間：2026-10-21T01:18:00Z；台北時間：2026-10-21 09:18
  - 摘要：[FTNN新聞網]記者吳峻光／綜合報導台股今（21）日開盤大漲逾700點，火速收復47K關卡，加權指數最高衝至47088.43點，台積電（2330）一度上漲25元，漲幅達1.04...
  - 原文連結：https://tw.stock.yahoo.com/news/%E5%8F%B0%E8%82%A1%E9%96%8B%E7%9B%A4%E9%A3%86700%E9%BB%9E%E7%81%AB%E9%80%9F%E6%94%B6%E5%BE%A947k-%E5%8F%B0%E7%A9%8D%E9%9B%BB%E4%B8%8A%E6%BC%B225%E5%85%83-11%E6%AA%94%E7%A7%92%E4%BA%AE%E7%87%88-%E8%81%AF%E8%8C%82-%E7%8E%89%E6%99%B6%E5%85%89-011800446.html
- 事件4：台積電高雄楠梓廠工安意外 第4人送醫後傷重不治
  - 來源：Yahoo 台股；發布時間：2026-10-21T01:06:00Z；台北時間：2026-10-21 09:06
  - 摘要：高雄楠梓科技園區台積電F22廠區20日發生重大工安意外，吊車執行鋼構吊掛作業時疑因螺栓斷裂，導致4名焊接外包工人隨鋼梁自高處墜落，經送醫搶救全數宣告不治。南科管理局已勒令現場吊裝作業全面停工並封鎖採證，後續將依職業安全衛生法規究責開罰，詳細
  - 原文連結：https://tw.stock.yahoo.com/news/%E5%BF%AB%E8%A8%8A-%E8%9E%BA%E6%A0%93%E6%96%B7%E8%A3%82%E9%8B%BC%E6%A2%81%E5%A2%9C%E8%90%BD-%E9%AB%98%E9%9B%84%E5%8F%B0%E7%A9%8D%E9%9B%BBf22%E5%BB%A0%E5%B7%A5%E5%AE%89%E6%84%8F%E5%A4%96-%E7%AC%AC4%E4%BA%BA%E5%82%B7%E9%87%8D%E4%B8%8D%E6%B2%BB-010600282.html
- 事件5：00888繳出亮眼成績 今年已漲87%配息率衝17%
  - 來源：Yahoo 台股；發布時間：2026-10-21T00:30:48Z；台北時間：2026-10-21 08:30
  - 摘要：近期全球股市受到美國通膨升溫及AI概念股漲多修正影響，市場短線震盪加劇，不過從企業獲利表現來看，AI產業成長趨勢並未改變。隨著美國科技巨頭持續大手筆投入AI基礎建設，從資料中心、AI伺服器到高效能運算需求全面升溫，市場普遍認為，這波回檔更像
  - 原文連結：https://tw.stock.yahoo.com/news/ai%E8%A1%8C%E6%83%85%E5%85%A8%E9%9D%A2%E5%BC%95%E7%88%86-00888%E4%BB%8A%E5%B9%B4%E5%A4%A7%E6%BC%B287-68-%E9%85%8D%E6%81%AF%E7%8E%87%E8%A1%9D17-003048292.html
- 事件6：外資賣超5檔主動式 00406A受重傷、ETF新兵被砍到破發
  - 來源：Yahoo 台股；發布時間：2026-10-20T23:00:00Z；台北時間：2026-10-21 07:00
  - 摘要：[FTNN新聞網]記者薛明峻／台北報導台股昨（20）日開低走低，終場收在46292.93點，下跌529.15點，跌幅1.13%，成交金額7600.3億元。根據證交所公布籌碼動向，外...
  - 原文連結：https://tw.stock.yahoo.com/news/%E6%8E%9B%E7%89%8C%E9%A6%96%E6%97%A5%E7%A0%B4%E7%99%BC-00415a%E8%88%87-%E9%80%994%E6%AA%94%E4%B8%BB%E5%8B%95%E5%BC%8F-%E9%81%AD%E5%A4%96%E8%B3%87%E7%98%8B%E7%A0%8D19%E8%90%AC%E5%BC%B5-0056%E5%B9%B4%E5%8C%96%E9%85%8D%E6%81%AF%E7%8E%87%E8%A1%9D12-230000137.html
- 事件7：Federal Reserve Board announces termination of enforcement actions with Gardner Bancshares, Inc. and Small Business Bank
  - 來源：Federal Reserve；發布時間：Fri, 16 Oct 2026 15:00:00 GMT；台北時間：2026-10-16 23:00
  - 摘要：Federal Reserve Board announces termination of enforcement actions with Gardner Bancshares, Inc. and Small Business Bank
  - 原文連結：https://www.federalreserve.gov/newsevents/pressreleases/enforcement20261016a.htm
- 事件8：Housing is flashing warning signs just as the Fed weighs more interest rate hikes
  - 來源：CNBC；發布時間：Tue, 20 Oct 2026 19:28:43 GMT；台北時間：2026-10-21 03:28
  - 摘要：Housing data deteriorated further in September, according to separate reports Tuesday.
  - 原文連結：https://www.cnbc.com/2026/10/20/housing-mortgage-rates-real-estate-federal-reserve.html
- 事件9：Trump sued over 50% tariffs on Canada in latest trade challenge
  - 來源：CNBC；發布時間：Tue, 20 Oct 2026 18:06:13 GMT；台北時間：2026-10-21 02:06
  - 摘要：A new lawsuit challenges President Donald Trump's tariffs on a range of Canadian goods using Section 338 of the Tariff Act of 1930.
  - 原文連結：https://www.cnbc.com/2026/10/20/trump-tariffs-canada-section-338-lawsuit.html
- 事件10：Capital One's strong quarter and progressing Discover integration are rewarded on Wall Street
  - 來源：CNBC；發布時間：Tue, 20 Oct 2026 23:34:14 GMT；台北時間：2026-10-21 07:34
  - 摘要：Stronger net interest income and credit performance were the stars of the bank's earnings.
  - 原文連結：https://www.cnbc.com/investingclub/2026/10/20/capital-one-strong-quarter-and-progressing-discover-integration-are-rewarded.html
- 事件11：Investors look to earnings to reset the bull market. The key level to watch on the S&P 500
  - 來源：CNBC；發布時間：Tue, 20 Oct 2026 12:52:29 GMT；台北時間：2026-10-20 20:52
  - 摘要：The key level traders are watching on the S&P 500 that could mean an even bigger decline is ahead.
  - 原文連結：https://www.cnbc.com/2026/10/20/santoli-key-sp-500-level-to-watch.html
- 事件12：Obsessed with CoreWeave and the AI trade? You're missing out on some great stocks
  - 來源：CNBC；發布時間：Tue, 20 Oct 2026 21:17:47 GMT；台北時間：2026-10-21 05:17
  - 摘要：Today's earnings show there's a cohort of the market that can thrive outside of the data center buildout.
  - 原文連結：https://www.cnbc.com/investingclub/2026/10/20/obsessed-with-the-ai-trade-youre-missing-out-on-some-great-stocks.html


## 三、期貨

**資料來源：**
1. Cloudflare Workers：TAIFEX Proxy — https://taifex.grichtoyang.workers.dev/
2. TAIFEX Open API — https://openapi.taifex.com.tw/

近月契約月份：202610 (日盤成交量最大者)；交易日期：2026-10-20

### 1．台指期近月日盤行情

| 項目 | 數值 | 資料來源 |
|---|---|---|
| 開盤價 | 46,434 | TAIFEX Proxy |
| 最高價 | 46,920 | TAIFEX Proxy |
| 最低價 | 46,162 | TAIFEX Proxy |
| 收盤價 | 46,384 | TAIFEX Proxy |
| 漲跌點數 | -385 | TAIFEX Proxy |
| 漲跌幅 | -0.82 | TAIFEX Proxy |
| 成交量 | 122,189 | TAIFEX Proxy |
| 日盤高點及低點 | 46,920 / 46,162 | TAIFEX Proxy |

### 2．台指期近月夜盤行情

| 項目 | 數值 | 資料來源 |
|---|---|---|
| 開盤價 | 46,490 | TAIFEX Proxy |
| 最高價 | 47,098 | TAIFEX Proxy |
| 最低價 | 46,136 | TAIFEX Proxy |
| 收盤價 | 46,975 | TAIFEX Proxy |
| 漲跌點數 | +634 | TAIFEX Proxy |
| 漲跌幅 | +1.37 | TAIFEX Proxy |
| 成交量 | 30,400 | TAIFEX Proxy |
| 夜盤高點及低點 | 47,098 / 46,136 | TAIFEX Proxy |
| 結算價 | 46,341 | TAIFEX Proxy |
| 未平倉量 | 16,625 | TAIFEX Proxy |

### 3．法人台指期多空未平倉部位

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 外資多方 OI | 11,524 | TAIFEX Proxy |
| 外資空方 OI | 101,272 | TAIFEX Proxy |
| 外資多空淨 OI | -89,748 | TAIFEX Proxy |
| 投信多方 OI | 87,171 | TAIFEX Proxy |
| 投信空方 OI | 2,782 | TAIFEX Proxy |
| 投信多空淨 OI | +84,389 | TAIFEX Proxy |
| 自營商多方 OI | 7,105 | TAIFEX Proxy |
| 自營商空方 OI | 4,405 | TAIFEX Proxy |
| 自營商多空淨 OI | +2,700 | TAIFEX Proxy |
| 三大法人合計多方 OI | 105,800 | TAIFEX Proxy |
| 三大法人合計空方 OI | 108,459 | TAIFEX Proxy |
| 三大法人合計多空淨 OI | -2,659 | TAIFEX Proxy |
| 外資多空淨 OI 變化 | +1,397 | TAIFEX Proxy |
| 投信多空淨 OI 變化 | +289 | TAIFEX Proxy |
| 自營商多空淨 OI 變化 | -129 | TAIFEX Proxy |

### 4．前十大交易人多空未平倉部位

**資料來源：** `TAIFEX OpenAPI OpenInterestOfLargeTradersFutures` (官方資料落後約一日，標示實際日期)

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 前十大交易人多方 OI | 7,685 | TAIFEX Proxy |
| 前十大交易人空方 OI | 11,817 | TAIFEX Proxy |
| 前十大交易人多空淨 OI | -4,132 | TAIFEX Proxy |
| 多空淨 OI 變化 (2026-10-16→2026-10-20) | -6,626 | TAIFEX Proxy snapshots (2026-10-19) |
- 資料日期：2026-10-20 (TypeOfTraders=0 全部交易人；契約月份 202610)

### 5．日盤、夜盤法人交易資料

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 外資日盤多單交易量 | 95,138 | TAIFEX Proxy |
| 外資日盤空單交易量 | 93,688 | TAIFEX Proxy |
| 外資日盤多空淨交易量 | +1,450 | TAIFEX Proxy |
| 外資夜盤多單交易量 | 19,927 | TAIFEX Proxy |
| 外資夜盤空單交易量 | 19,207 | TAIFEX Proxy |
| 外資夜盤多空淨交易量 | +720 | TAIFEX Proxy |
| 外資日盤／夜盤交易量變化 | +730 | TAIFEX Proxy |
| 投信日盤多空淨交易量 | +289 | TAIFEX Proxy |
| 投信夜盤多空淨交易量 | +0 | TAIFEX Proxy |
| 投信日盤／夜盤交易量變化 | +289 | TAIFEX Proxy |
| 自營商日盤多空淨交易量 | +1,521 | TAIFEX Proxy |
| 自營商夜盤多空淨交易量 | +141 | TAIFEX Proxy |
| 自營商日盤／夜盤交易量變化 | +1,380 | TAIFEX Proxy |
| 三大法人日盤多空淨交易量 | +3,260 | TAIFEX Proxy |
| 三大法人夜盤多空淨交易量 | +861 | TAIFEX Proxy |
| 法人日盤交易金額淨額 (億元) | +304.1 | TAIFEX Proxy |
| 法人夜盤交易金額淨額 (億元) | +80.4 | TAIFEX Proxy |

### 6．期貨與現貨關係

| 項目 | 數值 | 資料來源 |
|---|---|---|
| 台指期近月價格 | 46,384 | TAIFEX Proxy |
| 加權指數價格 | 46,292.93 | twse-proxy |
| 台指期與加權指數價差 | +91.07 | TAIFEX Proxy+twse-proxy |
| 價差百分比 | +0.20 | TAIFEX Proxy+twse-proxy |
| 日盤基差 | +91.07 | TAIFEX Proxy+twse-proxy |
| 夜盤價格相對日盤收盤的變化 | +591 | TAIFEX Proxy |

### 7．日盤、夜盤與籌碼變化對照

#### 7.1 日夜盤價格與成交量對照 (變化 = 日盤 - 夜盤)

| 項目 | 日盤 | 夜盤 | 變化 (日-夜) | 資料來源 |
|---|---|---|---|---|
| 收盤價 | 46,384 | 46,975 | -591 | TAIFEX Proxy |
| 成交量 | 95,321 | 30,400 | +64,921 | TAIFEX Proxy |
- 台指期總 OI 前日變化：+1,557（來源：TAIFEX Proxy）


#### 7.2 法人籌碼日夜盤對照 (淨變化 = 日盤淨 - 夜盤淨；OI 為日盤收盤後總量，前日變化另列)

| 法人 | 交易量 |  |  |  |  |  |  | 未平倉量 |  |  |  | 資料來源 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|  | **日盤多單** | **日盤空單** | **日盤淨** | **夜盤多單** | **夜盤空單** | **夜盤淨** | **淨變化 (日-夜)** | **OI多方** | **OI空方** | **OI淨** | **OI前日變化** |  |
| 外資 | 95,138 | 93,688 | +1,450 | 19,927 | 19,207 | +720 | +730 | 11,524 | 101,272 | -89,748 | +1,397 | TAIFEX Proxy |
| 投信 | 35,516 | 35,227 | +289 | 0 | 0 | +0 | +289 | 87,171 | 2,782 | +84,389 | +289 | TAIFEX Proxy |
| 自營商 | 10,196 | 8,675 | +1,521 | 2,546 | 2,405 | +141 | +1,380 | 7,105 | 4,405 | +2,700 | -129 | TAIFEX Proxy |
| 三大法人合計 | 140,850 | 137,590 | +3,260 | 22,473 | 21,612 | +861 | +2,399 | 105,800 | 108,459 | -2,659 | +1,557 | TAIFEX Proxy |

#### 7.3 前十大交易人日夜盤對照 (OI 無日夜拆分，列收盤後總量)

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 前十大交易人多方 OI | 7,685 | TAIFEX Proxy |
| 前十大交易人空方 OI | 11,817 | TAIFEX Proxy |
| 前十大交易人多空淨 OI | -4,132 | TAIFEX Proxy |
| 前十大交易人多空淨 OI 變化 (2026-10-16→2026-10-20) | -6,626 | TAIFEX Proxy snapshots (2026-10-19) |

#### 7.4 夜盤劇本分類 (規則對應：夜盤漲跌 × 外資夜盤偏多空)

| 項目 | 數值 | 資料來源 |
|---|---|---|
| 夜盤成交量占比 (夜盤量／(夜盤量＋日盤量)) | 24.18% | TAIFEX Proxy |
| 夜盤漲跌點數 | +634 | TAIFEX Proxy |
| 外資夜盤多空淨交易量 | +720 | TAIFEX Proxy |
| 劇本分類 | 劇本一 | 規則對應 |
| 劇本條件 | 夜盤上漲＋外資偏多 | 規則對應 |
| 劇本特徵 | 開高、續漲機率高 | 規則對應 |

## 四、選擇權

**資料來源：** 主要 TAIFEX 經 Cloudflare Worker Proxy；時區 `Asia/Taipei`

### 1．選擇權交易日期、到期日與資料時間

| 項目 | 數值 | 資料來源 |
|---|---|---|
| 交易日期 | 2026-10-20 | TAIFEX Proxy |
| 到期月份／到期日 | 202610 | TAIFEX Proxy |
| 資料更新時間 | 2026-10-21 10:28:45 | 本機 |
| 日盤／夜盤標記 | 日盤收盤後資料 | TAIFEX Proxy |

### 2．Call 總成交量、OI、OI 增減

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Call 總成交量 | 213,460 | TAIFEX Proxy |
| Call 總未平倉量 OI | 106,703 | TAIFEX Proxy |
| Call OI 增減 (2026-10-19→2026-10-20) | +12,811 | TAIFEX Proxy snapshots (2026-10-19) |

### 3．Put 總成交量、OI、OI 增減

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Put 總成交量 | 279,705 | TAIFEX Proxy |
| Put 總未平倉量 OI | 68,220 | TAIFEX Proxy |
| Put OI 增減 (2026-10-19→2026-10-20) | +12,972 | TAIFEX Proxy snapshots (2026-10-19) |

### 4．Call／Put 比例與變化

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Call／Put 成交量比例 | 0.76 | TAIFEX Proxy |
| Call／Put 未平倉量比例 | 1.56 | TAIFEX Proxy |
| Put／Call Ratio | 0.64 | TAIFEX Proxy |
| Call／Put 比例變化 (量比 2026-10-19→2026-10-20) | 34.52 | TAIFEX Proxy |
| 與前一交易日比較 (OI 比 2026-10-19→2026-10-20) | 4.57 | TAIFEX Proxy |
**資料來源：** 比例 `TAIFEX Proxy chain`；變化 `TAIFEX Proxy PutCallRatio`

### 5．外資 Call／Put 部位

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 外資 Call日買 | 59,878 | TAIFEX Proxy |
| 外資 Call日賣 | 60,428 | TAIFEX Proxy |
| 外資 Call日淨 | -550 | TAIFEX Proxy |
| 外資 Put日買 | 119,704 | TAIFEX Proxy |
| 外資 Put日賣 | 118,554 | TAIFEX Proxy |
| 外資 Put日淨 | +1,150 | TAIFEX Proxy |
| 外資 Call夜買 | 47,285 | TAIFEX Proxy |
| 外資 Call夜賣 | 47,033 | TAIFEX Proxy |
| 外資 Call夜淨 | +252 | TAIFEX Proxy |
| 外資 Put夜買 | 78,388 | TAIFEX Proxy |
| 外資 Put夜賣 | 77,847 | TAIFEX Proxy |
| 外資 Put夜淨 | +541 | TAIFEX Proxy |
| 外資 日盤淨總量 | -1,700 | TAIFEX Proxy |
| 外資 Call日夜淨增減 (日－夜) | -802 | TAIFEX Proxy |
| 外資 Put日夜淨增減 (日－夜) | +609 | TAIFEX Proxy |

### 6．自營商 Call／Put 部位

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 自營商 Call日買 | 61,142 | TAIFEX Proxy |
| 自營商 Call日賣 | 60,075 | TAIFEX Proxy |
| 自營商 Call日淨 | +1,067 | TAIFEX Proxy |
| 自營商 Put日買 | 74,895 | TAIFEX Proxy |
| 自營商 Put日賣 | 80,857 | TAIFEX Proxy |
| 自營商 Put日淨 | -5,962 | TAIFEX Proxy |
| 自營商 Call夜買 | 26,221 | TAIFEX Proxy |
| 自營商 Call夜賣 | 27,893 | TAIFEX Proxy |
| 自營商 Call夜淨 | -1,672 | TAIFEX Proxy |
| 自營商 Put夜買 | 40,344 | TAIFEX Proxy |
| 自營商 Put夜賣 | 40,407 | TAIFEX Proxy |
| 自營商 Put夜淨 | -63 | TAIFEX Proxy |
| 自營商 日盤淨總量 | +7,029 | TAIFEX Proxy |
| 自營商 Call日夜淨增減 (日－夜) | +2,739 | TAIFEX Proxy |
| 自營商 Put日夜淨增減 (日－夜) | -5,899 | TAIFEX Proxy |

### 7．主要 Call OI 集中區

| 項目 | 履約價 | OI | 資料來源 |
|---|---|---|---|
| Call OI 第1大履約價 | 49,500 | 6,380 | TAIFEX Proxy |
| Call OI 第2大履約價 | 54,000 | 5,734 | TAIFEX Proxy |
| Call OI 第3大履約價 | 52,000 | 5,159 | TAIFEX Proxy |
| Call OI 最大履約價 | 49,500 | 6,380 | TAIFEX Proxy |

#### Call OI 分布明細 Top10 (機器可讀，到期月份 202610)

| # | 履約價 | OI | 佔比 | 資料來源 |
|---|---|---|---|---|
| C1 | 49,500 | 6,380 | 5.98% | TAIFEX Proxy |
| C2 | 54,000 | 5,734 | 5.37% | TAIFEX Proxy |
| C3 | 52,000 | 5,159 | 4.83% | TAIFEX Proxy |
| C4 | 47,000 | 3,789 | 3.55% | TAIFEX Proxy |
| C5 | 49,000 | 3,655 | 3.43% | TAIFEX Proxy |
| C6 | 48,000 | 3,622 | 3.39% | TAIFEX Proxy |
| C7 | 53,000 | 2,501 | 2.34% | TAIFEX Proxy |
| C8 | 47,900 | 2,485 | 2.33% | TAIFEX Proxy |
| C9 | 47,500 | 2,370 | 2.22% | TAIFEX Proxy |
| C10 | 47,200 | 2,265 | 2.12% | TAIFEX Proxy |


### 8．主要 Put OI 集中區

| 項目 | 履約價 | OI | 資料來源 |
|---|---|---|---|
| Put OI 第1大履約價 | 46,000 | 4,486 | TAIFEX Proxy |
| Put OI 第2大履約價 | 45,000 | 4,104 | TAIFEX Proxy |
| Put OI 第3大履約價 | 46,500 | 2,041 | TAIFEX Proxy |
| Put OI 最大履約價 | 46,000 | 4,486 | TAIFEX Proxy |

#### Put OI 分布明細 Top10 (機器可讀，到期月份 202610)

| # | 履約價 | OI | 佔比 | 資料來源 |
|---|---|---|---|---|
| P1 | 46,000 | 4,486 | 6.58% | TAIFEX Proxy |
| P2 | 45,000 | 4,104 | 6.02% | TAIFEX Proxy |
| P3 | 46,500 | 2,041 | 2.99% | TAIFEX Proxy |
| P4 | 45,500 | 1,891 | 2.77% | TAIFEX Proxy |
| P5 | 44,000 | 1,890 | 2.77% | TAIFEX Proxy |
| P6 | 46,200 | 1,853 | 2.72% | TAIFEX Proxy |
| P7 | 47,000 | 1,820 | 2.67% | TAIFEX Proxy |
| P8 | 44,500 | 1,775 | 2.6% | TAIFEX Proxy |
| P9 | 45,800 | 1,614 | 2.37% | TAIFEX Proxy |
| P10 | 45,700 | 1,376 | 2.02% | TAIFEX Proxy |


### 9．Call OI 增減集中區

| 項目 | 履約價 (增減口數) | 資料來源 |
|---|---|---|
| Call OI 增加最多的履約價 | 49,000 (+1,757) | TAIFEX Proxy snapshots (2026-10-19) |
| Call OI 減少最多的履約價 | 48,200 (-698) | TAIFEX Proxy snapshots (2026-10-19) |

### 10．Put OI 增減集中區

| 項目 | 履約價 (增減口數) | 資料來源 |
|---|---|---|
| Put OI 增加最多的履約價 | 45,800 (+961) | TAIFEX Proxy snapshots (2026-10-19) |
| Put OI 減少最多的履約價 | 44,300 (-372) | TAIFEX Proxy snapshots (2026-10-19) |

### 11．Call Wall

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Call Wall 價位 | 49,500 | TAIFEX Proxy |
| 對應到期月份 | 202610 | TAIFEX Proxy |
| 與前一交易日的變化 (2026-10-19→2026-10-20) | +0 | TAIFEX Proxy snapshots (2026-10-19) |

### 12．Put Wall

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Put Wall 價位 | 46,000 | TAIFEX Proxy |
| 對應到期月份 | 202610 | TAIFEX Proxy |
| 與前一交易日的變化 (2026-10-19→2026-10-20) | +1,000 | TAIFEX Proxy snapshots (2026-10-19) |

### 13．Gamma Wall

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Gamma Wall 價位 | 46,000.00 | TAIFEX Proxy (options-market-structure-compact (proxy)) |
| 對應到期月份 | 202610 | TAIFEX Proxy |
| 資料日期 | 2026-10-20 | TAIFEX Proxy (options-market-structure-compact (proxy)) |

### 14．Gamma Flip

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Gamma Flip 價位 | 46,462.76 | TAIFEX Proxy (options-market-structure-compact (proxy)) |
| 對應到期月份 | 202610 | TAIFEX Proxy |
| 資料日期 | 2026-10-20 | TAIFEX Proxy (options-market-structure-compact (proxy)) |

### 15．Max Pain

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Max Pain 價位 | 46,500 | TAIFEX Proxy |
| 對應到期月份 | 202610 | TAIFEX Proxy |
| 與前一交易日的變化 (2026-10-19→2026-10-20) | +0 | TAIFEX Proxy snapshots (2026-10-19) |

### 17．選擇權法人日盤、夜盤交易

| 法人 | 日盤多單 | 日盤空單 | 日盤淨 | 夜盤多單 | 夜盤空單 | 夜盤淨 | 淨變化 (日-夜) | 資料來源 |
|---|---|---|---|---|---|---|---|---|
| 外資 | 178,432 | 180,132 | -1,700 | 125,132 | 125,421 | -289 | -1,411 | TAIFEX Proxy |
| 投信 | 3 | 1,700 | -1,697 | 2 | 0 | +2 | -1,699 | TAIFEX Proxy |
| 自營商 | 141,999 | 134,970 | +7,029 | 66,628 | 68,237 | -1,609 | +8,638 | TAIFEX Proxy |
| 三大法人合計 | 320,434 | 316,802 | +3,632 | 191,762 | 193,658 | -1,896 | +5,528 | TAIFEX Proxy |
- 方法論：多方＝買Call＋賣Put（看多），空方＝賣Call＋買Put（看空），淨額＝看多－看空（已用 Call／Put 拆分頁交叉驗算一致）
- 公式：多方(買)－空方(賣)＝（買call＋賣put）－（賣call＋買put）＝看多－看空
- 速記：多＝BC＋SP、空＝SC＋BP

#### 法人多空力道表（金額・億元；上游千元／1e5）

| 法人 | 日多方力道 | 日空方力道 | 日淨多空力道 | 夜多方力道 | 夜空方力道 | 夜淨多空力道 | 日淨－夜淨 | 資料來源 |
|---|---|---|---|---|---|---|---|---|
| 外資 | 15.89 | 16.21 | -0.32 | 9.15 | 9.22 | -0.06 | -0.25 | TAIFEX Proxy |
| 投信 | 0.00 | 1.25 | -1.25 | 0.00 | 0.00 | +0.00 | -1.25 | TAIFEX Proxy |
| 自營商 | 12.25 | 9.62 | +2.63 | 4.77 | 4.84 | -0.08 | +2.71 | TAIFEX Proxy |
| 三大法人合計 | 28.14 | 27.08 | +1.06 | 13.92 | 14.06 | -0.14 | +1.20 | TAIFEX Proxy |

### 18．選擇權前十大

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 買權多方 OI | 54,137 | TAIFEX Proxy |
| 買權空方 OI | 67,666 | TAIFEX Proxy |
| 買權多空淨 OI | -13,529 | TAIFEX Proxy |
| 買權多空淨 OI 變化 (2026-10-16→2026-10-20) | -8,180 | TAIFEX Proxy snapshots (2026-10-19) |

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 賣權多方 OI | 29,725 | TAIFEX Proxy |
| 賣權空方 OI | 21,734 | TAIFEX Proxy |
| 賣權多空淨 OI | +7,991 | TAIFEX Proxy |
| 賣權多空淨 OI 變化 (2026-10-16→2026-10-20) | +4,712 | TAIFEX Proxy snapshots (2026-10-19) |
- 資料日期：買權 2026-10-20／賣權 2026-10-20 (TypeOfTraders=0 全部交易人；契約月份 202610)

#### 大戶流向（全日；前十大無日夜拆分）

| 項目 | 淨變化 | 區間 | 資料來源 |
|---|---|---|---|
| 期貨前十大 | -6,626 | 2026-10-16→2026-10-20 | TAIFEX Proxy snapshots (2026-10-19) |
| 買權前十大 | -8,180 | 2026-10-16→2026-10-20 | TAIFEX Proxy snapshots (2026-10-19) |
| 賣權前十大 | +4,712 | 2026-10-16→2026-10-20 | TAIFEX Proxy snapshots (2026-10-19) |

### 16．資料來源、時間、時區與狀態

- 資料來源：TAIFEX 經 Cloudflare Worker Proxy
- 資料日期：2026-10-20；資料時間：2026-10-21 10:28:45；時區：`Asia/Taipei`
- 日盤／夜盤標記：日盤收盤後 + 夜盤盤後
- 註記：同 T0 保護：2 格沿用前版有值（本次抓取缺失不覆寫）
- 註記：同 T0 覆蓋：58 格以本次新抓取覆蓋（該 T0 尚無報告，無凍結對象）
- 未取得欄位 (0)：無
- 註記：gapfill 自動補登 L77 維持率＝178.93（wantgoo 2026-10-20）
- 註記：futures-price-after-hours 日期 2026-10-20 非今日 2026-10-21，視為無新節次，不採用
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
- margin_ratio：`前值遞補 (DATA 2026-10-19；當日三源皆失敗；民間估算；官方無每日序列)`
- sbl：`TWSE TWT93U + TPEX margin_sbl`
- 期貨選擇權：`TAIFEX Proxy`
- 新聞：台股 Yahoo／國際 Fed＋CNBC＋MarketWatch；台股 Yahoo（不足時財訊快報備援）/ 國際 Fed 公告＋CNBC＋MarketWatch RSS；Fed 無摘要；investing 港股為主已退役；cnyes CSR、wantgoo JS 算繪、中央社/台灣央行路徑待查，未採用
- 美股/亞股/期貨/匯率/ADR/商品：`Yahoo Finance Chart API`；美債：`Yahoo Finance (備援)`
- 註記：融資維持率未取得 (三源皆失敗；官方無每日序列)
- 註記：融資維持率採前值遞補 (DATA 2026-10-19)，非 T0 2026-10-20
- 註記：上市 MI_MARGN / TWT96U 無日期欄，採用最新可得
- 註記：借券賣出增減僅上櫃值 (TWSE TWT93U 未取得)
- 本報告僅整理資料，不提供交易判斷。

## 六、期現選方向對照

**規則：** 趨勢偏多／空＝現貨、期貨OI、選擇權日淨三者同向；避險／對沖＝現貨與期選反向；日內反轉＝日淨與夜淨反向；缺值標示，不推估。選擇權多空為看多看空口徑。

| 法人 | 現貨買賣超(億) | 期貨OI淨(口) | 期貨日淨 | 期貨夜淨 | 選擇權日淨 | 選擇權夜淨 | 判定 | 期選組合 | 資料來源 |
|---|---|---|---|---|---|---|---|---|---|
| 外資 | -795.4 | -89,748 | +1,450 | +720 | -1,700 | -289 | 趨勢偏空 | 對沖避險 | twse-proxy／TAIFEX Proxy |
| 投信 | +187.6 | +84,389 | +289 | +0 | -1,697 | +2 | 避險／對沖 | 分歧 | twse-proxy／TAIFEX Proxy |
| 自營商 | -355.8 | +2,700 | +1,521 | +141 | +7,029 | -1,609 | 避險／對沖 | 趨勢偏多 | twse-proxy／TAIFEX Proxy |
