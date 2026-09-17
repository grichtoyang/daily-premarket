# DATA_REPORT_20260917

- 報告日期：`2026-09-18`
- T0 交易日期：`2026-09-17`
- 資料產出時間：`2026-09-18 01:09:33`
- 時區：`Asia/Taipei`

---

## 一、現貨

### 1. 台股大盤行情

**資料來源：** `Cloudflare Worker：twse-proxy` (備援 `TWSE OpenAPI MI_INDEX`)

| 項目 | 數值 | 單位 | 資料來源 |
|---|---|---|---|
| 加權指數 | 46,288.00 | 點 | twse-proxy |
| 開盤 | 45,936.11 | 點 | FinMind TaiwanStockPrice TAIEX |
| 最高 | 46,874.84 | 點 | FinMind TaiwanStockPrice TAIEX |
| 最低 | 45,936.11 | 點 | FinMind TaiwanStockPrice TAIEX |
| 收盤 | 46,288.00 | 點 | twse-proxy |
| 漲跌點數 | 439.10 | 點 | twse-proxy |
| 漲跌幅 | +0.96 | % | twse-proxy |
| 成交金額 | 8,666.2 | 億元 | twse-proxy market_statistics |

### 2. 市場漲跌家數

#### 2.1 上市公司

**資料來源：** `Cloudflare Worker：twse-proxy` (備援 `TWSE OpenAPI twtazu_od`)

| 項目 | 家數 | 資料來源 |
|---|---|---|
| 上漲家數 | 758 | twse-proxy |
| 下跌家數 | 244 | twse-proxy |
| 平盤家數 | 67 | twse-proxy |
| 漲停家數 | 25 | twse-proxy |
| 跌停家數 | 1 | twse-proxy |

#### 2.2 上櫃公司

**資料來源：** `TPEX OpenAPI tpex_mainborad_highlight`

| 項目 | 家數 | 資料來源 |
|---|---|---|
| 上漲家數 | 477 | TPEX OpenAPI tpex_mainborad_highlight |
| 下跌家數 | 294 | TPEX OpenAPI tpex_mainborad_highlight |
| 平盤家數 | 96 | TPEX OpenAPI tpex_mainborad_highlight |
| 漲停家數 | 16 | TPEX OpenAPI tpex_mainborad_highlight |
| 跌停家數 | 1 | TPEX OpenAPI tpex_mainborad_highlight |

### 3. 三大法人現貨買賣超

**資料來源：** `TWSE RWD BFI82U`

| 法人別 | 買賣超金額 | 單位 | 資料來源 |
|---|---|---|---|
| 外資 | +121.9 | 億元 | twse-proxy /institutional |
| 投信 | +117.0 | 億元 | twse-proxy /institutional |
| 自營商 | +15.8 | 億元 | twse-proxy /institutional |
| 三大法人合計 | +254.7 | 億元 | twse-proxy /institutional |

### 4. 融資融券

**資料來源：** 上市+上櫃 `HiStock` (金額口徑)；維持率 `istock.tw`；備援官方逐股加總

| 項目 | 數值 | 單位 | 資料來源 |
|---|---|---|---|
| 融資餘額 | 7,913.3 | 億元 | HiStock 上市+上櫃融資融券 (金額口徑) |
| 融資增減 | +54.4 | 億元 | HiStock 上市+上櫃融資融券 (金額口徑) |
| 融券餘額 | 253,521 | 張 | HiStock 上市+上櫃融資融券 (金額口徑) |
| 融券增減 | 22,065 | 張 | HiStock 上市+上櫃融資融券 (金額口徑) |
| 融資維持率 | unavailable | % | istock.tw |

### 5. 借券資料

**資料來源：** 上市 `TWSE OpenAPI TWT96U` (可借餘額)、上櫃 `TPEX OpenAPI tpex_margin_sbl`

| 項目 | 數值 | 單位 | 資料來源 |
|---|---|---|---|
| 借券餘額 | 4,489,570 | 張 | TWSE TWT96U + TPEX margin_sbl |
| 借券賣出餘額 | 37,233 | 張 | TWSE TWT96U + TPEX margin_sbl |
| 借券賣出增減 | 3,125 | 張 | TWSE TWT96U + TPEX margin_sbl |

### 6. 市場成交結構

**資料來源：** 上市 `twse-proxy market_statistics`、上櫃 `TPEX OpenAPI tpex_mainborad_highlight`

| 項目 | 成交金額 | 單位 | 資料來源 |
|---|---|---|---|
| 上市成交金額 | 8,666.2 | 億元 | twse-proxy market_statistics |
| 上櫃成交金額 | 2,636.6 | 億元 | TPEX OpenAPI tpex_mainborad_highlight |
| 上市櫃成交金額合計 | 11,302.8 | 億元 | twse-proxy market_statistics+TPEX OpenAPI tpex_mainborad_highlight |

## 二、重要市場

### 1. 美股指數

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 收盤／最新值 | 漲跌點 | 漲跌幅 | 資料來源 |
|---|---|---|---|---|---|
| S&P 500 | ^GSPC | 7,635.86 | 84.05 | +1.11 | Yahoo Finance Chart API |
| Nasdaq Composite | ^IXIC | 26,405.49 | 427.06 | +1.64 | Yahoo Finance Chart API |
| Nasdaq 100 | ^NDX | 29,443.99 | 498.93 | +1.72 | Yahoo Finance Chart API |
| Dow Jones | ^DJI | 51,810.58 | 348.68 | +0.68 | Yahoo Finance Chart API |
| 費城半導體 SOX | ^SOX | 11,607.61 | 361.50 | +3.21 | Yahoo Finance Chart API |
| VIX | ^VIX | 15.55 | -2.16 | -12.20 | Yahoo Finance Chart API |

### 2. 亞洲主要指數

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 收盤／最新值 | 漲跌點 | 漲跌幅 | 資料來源 |
|---|---|---|---|---|---|
| 日經225 | ^N225 | 63,923.00 | 438.90 | +0.69 | Yahoo Finance Chart API |
| 韓國KOSPI | ^KS11 | 6,717.97 | 90.71 | +1.37 | Yahoo Finance Chart API |
| 香港恆生 | ^HSI | 24,713.78 | 46.54 | +0.19 | Yahoo Finance Chart API |
| 上海綜合 | 000001.SS | 3,891.60 | 27.32 | +0.71 | Yahoo Finance Chart API |
| 深圳成分 | 399001.SZ | 13,454.74 | 166.77 | +1.26 | Yahoo Finance Chart API |

### 3. 美股指數期貨

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 最新值 | 漲跌點 | 漲跌幅 | 資料來源 |
|---|---|---|---|---|---|
| S&P500期貨 | ES=F | 7,705.50 | 149.00 | +1.97 | Yahoo Finance Chart API |
| Nasdaq100期貨 | NQ=F | 29,741.50 | 778.00 | +2.69 | Yahoo Finance Chart API |
| 道瓊期貨 | YM=F | 52,242.00 | 735.00 | +1.43 | Yahoo Finance Chart API |
| Russell2000期貨 | RTY=F | 2,911.30 | 49.60 | +1.73 | Yahoo Finance Chart API |

### 4. 美國國債殖利率

**資料來源：** `U.S. Treasury Fiscal Data API` (失敗時備援 Treasury yield.xml 與 `Yahoo Finance`)

| 項目 | API 資料欄位／識別 | 殖利率 | 日變化 | 資料來源 |
|---|---|---|---|---|
| 美國 2 年期殖利率 | 2 Yr | 4.74 | 0.07 | U.S. Treasury yield.xml (網頁備援) |
| 美國 10 年期殖利率 | 10 Yr | 4.95 | -0.06 | Yahoo Finance (備援) |
| 美國 30 年期殖利率 | 30 Yr | 5.30 | -0.05 | Yahoo Finance (備援) |

### 5. 主要匯率

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 最新值 | 漲跌點 | 漲跌幅 | 資料來源 |
|---|---|---|---|---|---|
| USD/TWD | TWD=X | 31.86 | 0.09 | +0.29 | Yahoo Finance Chart API |
| DXY美元指數 | DX-Y.NYB | 100.25 | -0.06 | -0.06 | Yahoo Finance Chart API |
| USD/JPY | JPY=X | 156.04 | 0.77 | +0.50 | Yahoo Finance Chart API |
| USD/KRW | KRW=X | 1,380.91 | 17.34 | +1.27 | Yahoo Finance Chart API |

### 6. 台灣相關ADR

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 收盤／最新值 | 漲跌點 | 漲跌幅 | 資料來源 |
|---|---|---|---|---|---|
| 台積電ADR | TSM | 428.05 | 10.33 | +2.47 | Yahoo Finance Chart API |
| 聯電ADR | UMC | 24.49 | 1.96 | +8.70 | Yahoo Finance Chart API |
| 日月光ADR | ASX | 40.10 | 2.15 | +5.67 | Yahoo Finance Chart API |

### 7. 原油黃金Bitcoin

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 收盤／最新值 | 漲跌點 | 漲跌幅 | 資料來源 |
|---|---|---|---|---|---|
| WTI原油期貨 | CL=F | 102.07 | -0.36 | -0.35 | Yahoo Finance Chart API |
| 黃金期貨 | GC=F | 4,401.80 | 14.30 | +0.33 | Yahoo Finance Chart API |
| Bitcoin | BTC-USD | 76,780.75 | 630.43 | +0.83 | Yahoo Finance Chart API |

### 8. 重大經濟數據、央行事件與重大市場新聞

**資料來源：** 台股 `tw.stock.yahoo.com` (含內文摘要)；國際 `Fed 公告 RSS`＋`CNBC`＋`MarketWatch` (標題、來源、時間與連結)

- 事件1：外資帶百億銀彈拉台股 台積電攜塑化股奪回月線
  - 來源：Yahoo 台股；發布時間：2026-09-17T09:06:49Z；台北時間：2026-09-17 17:06
  - 摘要：439.10點、上漲0.96%，收在46,288點，成交金額回升至8,207.65億元。電子指數上漲0.85%、金融指數走揚0.44%，但櫃買指數反跌0.26%，資金明顯集中大型權值股，中小型股表現相對疲弱。

權王台積電(2330)上漲4
  - 原文連結：https://tw.stock.yahoo.com/news/%E8%81%AF%E6%BA%96%E6%9C%83%E5%8D%87%E6%81%AF%E8%90%BD%E5%9C%B0%E5%A4%96%E8%B3%87%E5%B8%B6%E7%99%BE%E5%84%84%E9%8A%80%E5%BD%88%E5%9B%9E%E9%A0%AD%EF%BC%81%E5%8F%B0%E7%A9%8D%E3%80%81%E5%A1%91%E5%8C%96%E9%9B%99%E5%BC%95%E6%93%8E%E6%8B%89%E5%8F%B0%E8%82%A1%E5%A5%AA%E5%9B%9E%E6%9C%88%E7%B7%9A%EF%BD%9Cyahoo%E8%B2%A1%E7%B6%93%E6%8E%83%E6%8F%8F-090649363.html
- 事件2：利率連10凍藏選舉盤算？學者點破央行低估體感通膨
  - 來源：Yahoo 台股；發布時間：2026-09-17T10:05:02Z；台北時間：2026-09-17 18:05
  - 摘要：美國聯準會（Fed）睽違3年首度升息1碼，中央銀行今（17）日召開理監事會議，仍決議維持政策利率不變，連續10季按兵不動，僅小幅鬆綁第二戶房貸管制。國立中山大學政治經濟學系特聘教授、前立委張其祿接受《Yahoo股市》採訪時直言，央行以明年通
  - 原文連結：https://tw.stock.yahoo.com/news/%E5%A4%AE%E8%A1%8C%E3%80%8C%E4%B8%8D%E8%AE%8A%E6%87%89%E8%90%AC%E8%AE%8A%E3%80%8D%E9%81%B8%E8%88%89%E8%80%83%E9%87%8F%EF%BC%9F%E5%AD%B8%E8%80%85%E5%96%8A%E4%BD%8E%E4%BC%B0%E6%B0%91%E7%9C%BE%E9%AB%94%E6%84%9F%E9%80%9A%E8%86%A8%E3%80%8C%E7%99%BE%E5%85%83%E4%BE%BF%E7%95%B6%E5%BF%AB%E5%90%83%E4%B8%8D%E5%88%B0%E3%80%8D-094840079.html
- 事件3：大立光今年第7度獵地擴產 豪擲11.72億台中掃貨
  - 來源：Yahoo 台股；發布時間：2026-09-17T10:24:05Z；台北時間：2026-09-17 18:24
  - 摘要：（中央社記者趙敏雅台北17日電）光學鏡頭廠大立光今天公告，斥資新台幣約11.72億元購入台中市南屯區約2259.25坪土地，以及約3695.25坪建物，供未來擴充產能使用，這是大立光今年第7度購買不動產，合計金額超過80億元。
  - 原文連結：https://tw.stock.yahoo.com/news/%E5%A4%A7%E7%AB%8B%E5%85%89%E4%BB%8A%E5%B9%B4%E7%AC%AC7%E5%BA%A6%E7%8D%B5%E5%9C%B0%E6%8B%9A%E6%93%B4%E7%94%A2-%E6%96%A5%E8%B3%8711-72%E5%84%84%E8%B2%B7%E5%8F%B0%E4%B8%AD%E5%9C%9F%E5%9C%B0%E5%BB%BA%E7%89%A9-102405800.html
- 事件4：存股別只看配息率 金融股高股息與金融ETF各有優勢
  - 來源：Yahoo 台股；發布時間：2026-09-17T07:43:37Z；台北時間：2026-09-17 15:43
  - 摘要：近期有網友在論壇發文：「以前一直以為想領比較有感的配息，就只能在高股息ETF裡面挑，最近才看到某金融ETF這種全球金融ETF，年化大概9.5%左右，突然有點改觀，原來不走傳統高股息選股，也可以有配息現金流？」

在許多投資人印象中，「打造被
  - 原文連結：https://tw.stock.yahoo.com/news/%E9%A0%9895%E9%85%8D%E6%81%AF%E4%B8%8D%E9%9D%A0%E9%AB%98%E8%82%A1%E6%81%AF%EF%BC%9F%E9%87%91%E8%9E%8D%E8%82%A1%E3%80%81%E9%AB%98%E8%82%A1%E6%81%AF%E8%88%87%E9%87%91%E8%9E%8Detf%E6%80%8E%E9%BA%BC%E6%8C%91%EF%BC%9F%E5%AF%A6%E5%8B%99%E9%85%8D%E7%BD%AE%E5%85%A8%E6%94%BB%E7%95%A5%EF%BC%81%EF%BD%9C%E6%8A%95%E8%B3%87%E8%A8%BA%E8%81%8A%E5%AE%A4-074337006.html
- 事件5：聯準會暌違3年再升息 房貸信用卡恐同步拉警報
  - 來源：Yahoo 台股；發布時間：2026-09-17T10:10:00Z；台北時間：2026-09-17 18:10
  - 摘要：[FTNN新聞網]記者林欣愉／綜合報導美國聯準會（Fed）16日宣布升息1碼，將聯邦基金利率目標區間調高至3.75%至4%，為2023年7月以來首次升息。這次升息不只牽動...
  - 原文連結：https://tw.stock.yahoo.com/news/fed%E7%9D%BD%E9%81%953%E5%B9%B4%E9%A6%96%E5%BA%A6%E5%8D%87%E6%81%AF-%E7%BE%8E%E5%9C%8B%E4%BF%A1%E7%94%A8%E5%8D%A1%E5%88%A9%E6%81%AF%E6%81%90%E5%A4%9A%E4%BB%98600%E5%84%84-%E6%88%BF%E8%B2%B8-%E5%AD%98%E6%AC%BE%E5%BD%B1%E9%9F%BF-%E6%AC%A1%E7%9C%8B-101000286.html
- 事件6：聯準會升息1碼　瀚亞投信：台股震盪向上格局　重回基本面
  - 來源：Yahoo 台股；發布時間：2026-09-17T16:28:37Z；台北時間：2026-09-18 00:28
  - 摘要：聯準會9月升息1碼，並暗示年底前再續升1碼。瀚亞投信國內投資部主管姚宗宏表示，9月升息1碼符合市場預期，雖聯準會主席華許談話論調偏鷹，但正面訊號在於聯準會也調高了今年的美國經濟成長率，顯示美國經濟仍有足夠韌性，足以承擔較高利率環境帶來的影響
  - 原文連結：https://tw.stock.yahoo.com/news/%E8%81%AF%E6%BA%96%E6%9C%83%E5%8D%87%E6%81%AF1%E7%A2%BC-%E7%80%9A%E4%BA%9E%E6%8A%95%E4%BF%A1-%E5%8F%B0%E8%82%A1%E9%9C%87%E7%9B%AA%E5%90%91%E4%B8%8A%E6%A0%BC%E5%B1%80-%E9%87%8D%E5%9B%9E%E5%9F%BA%E6%9C%AC%E9%9D%A2-162837885.html
- 事件7：Federal Reserve issues FOMC statement
  - 來源：Federal Reserve；發布時間：Wed, 16 Sep 2026 18:00:00 GMT；台北時間：2026-09-17 02:00
  - 摘要：Federal Reserve issues FOMC statement
  - 原文連結：https://www.federalreserve.gov/newsevents/pressreleases/monetary20260916a.htm
- 事件8：Federal Reserve Board and Federal Open Market Committee release economic projections from the September 15-16 FOMC meeting
  - 來源：Federal Reserve；發布時間：Wed, 16 Sep 2026 18:00:00 GMT；台北時間：2026-09-17 02:00
  - 摘要：Federal Reserve Board and Federal Open Market Committee release economic projections from the September 15-16 FOMC meeting
  - 原文連結：https://www.federalreserve.gov/newsevents/pressreleases/monetary20260916b.htm
- 事件9：Here are five key takeaways from Wednesday's Fed rate hike
  - 來源：CNBC；發布時間：Wed, 16 Sep 2026 21:23:51 GMT；台北時間：2026-09-17 05:23
  - 摘要：The Fed on Wednesday delivered a much-expected interest rate hike.
  - 原文連結：https://www.cnbc.com/2026/09/16/here-are-five-key-takeaways-from-wednesdays-fed-rate-hike.html
- 事件10：'Hostile act': Trump threatens EU with tariffs over Canada associate membership proposal
  - 來源：CNBC；發布時間：Thu, 17 Sep 2026 14:28:39 GMT；台北時間：2026-09-17 22:28
  - 摘要：European Commission President Ursula von der Leyen said EU is opening the door for Canada to become the first associate member of the 27-member bloc.
  - 原文連結：https://www.cnbc.com/2026/09/17/trump-canada-european-union-tariffs-associate-member-ukraine-.html
- 事件11：Trump gains a tariff weapon against China and India. Will he use it?
  - 來源：CNBC；發布時間：Thu, 17 Sep 2026 08:46:04 GMT；台北時間：2026-09-17 16:46
  - 摘要：U.S. House has paved the way for a legislation that will allow Trump to impose up to 100% tariffs on countries buying Russian oil, giving him leverage
  - 原文連結：https://www.cnbc.com/2026/09/17/trump-russia-sanctions-india-china-oil-tariffs.html
- 事件12：SEC clears path for tokenized stocks, bringing the market closer to 24/7 trading
  - 來源：CNBC；發布時間：Thu, 17 Sep 2026 13:00:28 GMT；台北時間：2026-09-17 21:00
  - 摘要：The long awaited Innovation Exemption comes two days after the Senate voted to block the Clarity Act crypto market structure bill from advancing.
  - 原文連結：https://www.cnbc.com/2026/09/17/sec-clears-path-for-tokenized-stocks-bringing-24/7-trading-closer.html

## 三、期貨

**資料來源：**
1. Cloudflare Workers：TAIFEX Proxy — https://taifex.grichtoyang.workers.dev/
2. TAIFEX Open API — https://openapi.taifex.com.tw/

近月契約月份：202610 (日盤成交量最大者)；交易日期：2026-09-17

### 1．台指期近月日盤行情

| 項目 | 數值 | 資料來源 |
|---|---|---|
| 開盤價 | 46,495 | TAIFEX Proxy |
| 最高價 | 47,037 | TAIFEX Proxy |
| 最低價 | 46,376 | TAIFEX Proxy |
| 收盤價 | 46,445 | TAIFEX Proxy |
| 漲跌點數 | +385 | TAIFEX Proxy |
| 漲跌幅 | +0.84 | TAIFEX Proxy |
| 成交量 | 82,385 | TAIFEX Proxy |
| 日盤高點及低點 | 47,037 / 46,376 | TAIFEX Proxy |

### 2．台指期近月夜盤行情

| 項目 | 數值 | 資料來源 |
|---|---|---|
| 開盤價 | 45,684 | proxy |
| 最高價 | 45,856 | proxy |
| 最低價 | 45,475 | proxy |
| 收盤價 | 45,640 | proxy |
| 漲跌點數 | -87 | proxy |
| 漲跌幅 | -0.19 | proxy |
| 成交量 | 32,283 | TAIFEX Proxy |
| 夜盤高點及低點 | 45,856 / 45,475 | proxy |
| 結算價 | 46,459 | TAIFEX Proxy |
| 未平倉量 | 99,476 | TAIFEX Proxy |

### 3．法人台指期多空未平倉部位

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 外資多方 OI | 8,161 | TAIFEX Proxy |
| 外資空方 OI | 86,835 | TAIFEX Proxy |
| 外資多空淨 OI | -78,674 | TAIFEX Proxy |
| 投信多方 OI | 77,058 | TAIFEX Proxy |
| 投信空方 OI | 3,032 | TAIFEX Proxy |
| 投信多空淨 OI | +74,026 | TAIFEX Proxy |
| 自營商多方 OI | 3,092 | TAIFEX Proxy |
| 自營商空方 OI | 3,779 | TAIFEX Proxy |
| 自營商多空淨 OI | -687 | TAIFEX Proxy |
| 三大法人合計多方 OI | 88,311 | TAIFEX Proxy |
| 三大法人合計空方 OI | 93,646 | TAIFEX Proxy |
| 三大法人合計多空淨 OI | -5,335 | TAIFEX Proxy |
| 外資多空淨 OI 變化 | -2,323 | TAIFEX Proxy |
| 投信多空淨 OI 變化 | +980 | TAIFEX Proxy |
| 自營商多空淨 OI 變化 | -512 | TAIFEX Proxy |

### 4．前十大交易人多空未平倉部位

**資料來源：** `TAIFEX OpenAPI OpenInterestOfLargeTradersFutures` (官方資料落後約一日，標示實際日期)

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 前十大交易人多方 OI | 77,597 | TAIFEX Proxy |
| 前十大交易人空方 OI | 70,668 | TAIFEX Proxy |
| 前十大交易人多空淨 OI | +6,929 | TAIFEX Proxy |
| 多空淨 OI 變化 | unavailable | 端點未提供 |
- 資料日期：2026-09-16 (TypeOfTraders=0 全部交易人；契約月份 202610)

### 5．日盤、夜盤法人交易資料

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 外資日盤多單交易量 | 46,240 | TAIFEX Proxy |
| 外資日盤空單交易量 | 48,514 | TAIFEX Proxy |
| 外資日盤多空淨交易量 | -2,274 | TAIFEX Proxy |
| 外資夜盤多單交易量 | 16,881 | TAIFEX Proxy |
| 外資夜盤空單交易量 | 18,102 | TAIFEX Proxy |
| 外資夜盤多空淨交易量 | -1,221 | TAIFEX Proxy |
| 外資日盤／夜盤交易量變化 | -1,053 | TAIFEX Proxy |
| 投信日盤多空淨交易量 | +980 | TAIFEX Proxy |
| 投信夜盤多空淨交易量 | +0 | TAIFEX Proxy |
| 投信日盤／夜盤交易量變化 | +980 | TAIFEX Proxy |
| 自營商日盤多空淨交易量 | -444 | TAIFEX Proxy |
| 自營商夜盤多空淨交易量 | -35 | TAIFEX Proxy |
| 自營商日盤／夜盤交易量變化 | -409 | TAIFEX Proxy |
| 三大法人日盤多空淨交易量 | -1,738 | TAIFEX Proxy |
| 三大法人夜盤多空淨交易量 | -1,256 | TAIFEX Proxy |
| 法人日盤交易金額淨額 (億元) | -161.0 | TAIFEX Proxy |
| 法人夜盤交易金額淨額 (億元) | -116.1 | TAIFEX Proxy |

### 6．期貨與現貨關係

| 項目 | 數值 | 資料來源 |
|---|---|---|
| 台指期近月價格 | 46,445 | TAIFEX Proxy |
| 加權指數價格 | 46,288.00 | twse-proxy |
| 台指期與加權指數價差 | +157 | TAIFEX Proxy+twse-proxy |
| 價差百分比 | +0.34 | TAIFEX Proxy+twse-proxy |
| 日盤基差 | +157 | TAIFEX Proxy+twse-proxy |
| 夜盤價格相對日盤收盤的變化 | -805 | proxy |

### 7．日盤、夜盤與籌碼變化對照

#### 7.1 日夜盤價格與成交量對照 (變化 = 日盤 - 夜盤)

| 項目 | 日盤 | 夜盤 | 變化 (日-夜) | 資料來源 |
|---|---|---|---|---|
| 收盤價 | 46,445 | 45,640 | +805 | TAIFEX Proxy |
| 成交量 | 50,102 | 32,283 | +17,819 | TAIFEX Proxy |
- 台指期總 OI 前日變化：-1,855（來源：TAIFEX Proxy）


#### 7.2 法人籌碼日夜盤對照 (淨變化 = 日盤淨 - 夜盤淨；OI 為日盤收盤後總量，前日變化另列)

| 法人 | 交易量 |  |  |  |  |  |  | 未平倉量 |  |  |  | 資料來源 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|  | **日盤多單** | **日盤空單** | **日盤淨** | **夜盤多單** | **夜盤空單** | **夜盤淨** | **淨變化 (日-夜)** | **OI多方** | **OI空方** | **OI淨** | **OI前日變化** |  |
| 外資 | 46,240 | 48,514 | -2,274 | 16,881 | 18,102 | -1,221 | -1,053 | 8,161 | 86,835 | -78,674 | -2,323 | TAIFEX Proxy |
| 投信 | 1,030 | 50 | +980 | 0 | 0 | +0 | +980 | 77,058 | 3,032 | +74,026 | +980 | TAIFEX Proxy |
| 自營商 | 3,695 | 4,139 | -444 | 740 | 775 | -35 | -409 | 3,092 | 3,779 | -687 | -512 | TAIFEX Proxy |
| 三大法人合計 | 50,965 | 52,703 | -1,738 | 17,621 | 18,877 | -1,256 | -482 | 88,311 | 93,646 | -5,335 | -1,855 | TAIFEX Proxy |

#### 7.3 前十大交易人日夜盤對照 (OI 無日夜拆分，列收盤後總量)

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 前十大交易人多方 OI | 77,597 | TAIFEX Proxy |
| 前十大交易人空方 OI | 70,668 | TAIFEX Proxy |
| 前十大交易人多空淨 OI | +6,929 | TAIFEX Proxy |
| 前十大交易人多空淨 OI 變化 | unavailable | 端點未提供 |

#### 7.4 夜盤劇本分類 (規則對應：夜盤漲跌 × 外資夜盤偏多空)

| 項目 | 數值 | 資料來源 |
|---|---|---|
| 夜盤成交量占比 (夜盤量／(夜盤量＋日盤量)) | 39.19% | TAIFEX Proxy |
| 夜盤漲跌點數 | -87 | TAIFEX Proxy |
| 外資夜盤多空淨交易量 | -1,221 | TAIFEX Proxy |
| 劇本分類 | 劇本三 | 規則對應 |
| 劇本條件 | 夜盤下跌＋外資偏空 | 規則對應 |
| 劇本特徵 | 開低、續跌機率高 | 規則對應 |

## 四、選擇權

**資料來源：** 主要 TAIFEX 經 Cloudflare Worker Proxy；時區 `Asia/Taipei`

### 1．選擇權交易日期、到期日與資料時間

| 項目 | 數值 | 資料來源 |
|---|---|---|
| 交易日期 | 2026-09-17 | TAIFEX Proxy |
| 到期月份／到期日 | 202609F3 | TAIFEX Proxy |
| 資料更新時間 | 2026-09-18 01:09:33 | 本機 |
| 日盤／夜盤標記 | 日盤收盤後資料 | TAIFEX Proxy |

### 2．Call 總成交量、OI、OI 增減

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Call 總成交量 | 169,196 | TAIFEX Proxy |
| Call 總未平倉量 OI | 44,075 | TAIFEX Proxy |
| Call OI 增減 (2026-09-16→2026-09-17) | +27,058 | TAIFEX Proxy snapshots (2026-09-16) |

### 3．Put 總成交量、OI、OI 增減

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Put 總成交量 | 187,349 | TAIFEX Proxy |
| Put 總未平倉量 OI | 33,953 | TAIFEX Proxy |
| Put OI 增減 (2026-09-16→2026-09-17) | +21,289 | TAIFEX Proxy snapshots (2026-09-16) |

### 4．Call／Put 比例與變化

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Call／Put 成交量比例 | 0.90 | TAIFEX Proxy |
| Call／Put 未平倉量比例 | 1.30 | TAIFEX Proxy |
| Put／Call Ratio | 0.77 | TAIFEX Proxy |
| Call／Put 比例變化 (量比 2026-09-15→2026-09-16) | -0.08 | TAIFEX OpenAPI |
| 與前一交易日比較 (OI 比 2026-09-15→2026-09-16) | -2.33 | TAIFEX OpenAPI |
**資料來源：** 比例 `TAIFEX Proxy chain`；變化 `TAIFEX OpenAPI PutCallRatio`

### 5．外資 Call／Put 部位

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 外資 Call 部位 (夜盤淨口數) | -119 | TAIFEX Proxy |
| 外資 Put 部位 (夜盤淨口數) | -364 | TAIFEX Proxy |
| 外資 Call／Put 淨部位 (日盤淨口數) | -1,277 | TAIFEX Proxy |
| 外資部位增減 | unavailable | 端點未提供 |

### 6．自營商 Call／Put 部位

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 自營商 Call 部位 (夜盤淨口數) | -139 | TAIFEX Proxy |
| 自營商 Put 部位 (夜盤淨口數) | -778 | TAIFEX Proxy |
| 自營商 Call／Put 淨部位 (日盤淨口數) | +1,039 | TAIFEX Proxy |
| 自營商部位增減 | unavailable | 端點未提供 |

### 7．主要 Call OI 集中區

| 項目 | 履約價 | OI | 資料來源 |
|---|---|---|---|
| Call OI 第1大履約價 | 48,200 | 3,709 | TAIFEX Proxy |
| Call OI 第2大履約價 | 47,000 | 2,824 | TAIFEX Proxy |
| Call OI 第3大履約價 | 48,500 | 2,381 | TAIFEX Proxy |
| Call OI 最大履約價 | 48,200 | 3,709 | TAIFEX Proxy |

#### Call OI 分布明細 Top10 (機器可讀，到期月份 202609F3)

| # | 履約價 | OI | 佔比 | 資料來源 |
|---|---|---|---|---|
| C1 | 48,200 | 3,709 | 8.42% | TAIFEX Proxy |
| C2 | 47,000 | 2,824 | 6.41% | TAIFEX Proxy |
| C3 | 48,500 | 2,381 | 5.4% | TAIFEX Proxy |
| C4 | 48,000 | 2,245 | 5.09% | TAIFEX Proxy |
| C5 | 47,200 | 1,909 | 4.33% | TAIFEX Proxy |
| C6 | 47,500 | 1,760 | 3.99% | TAIFEX Proxy |
| C7 | 47,100 | 1,435 | 3.26% | TAIFEX Proxy |
| C8 | 46,500 | 1,388 | 3.15% | TAIFEX Proxy |
| C9 | 47,300 | 1,195 | 2.71% | TAIFEX Proxy |
| C10 | 46,800 | 1,133 | 2.57% | TAIFEX Proxy |


### 8．主要 Put OI 集中區

| 項目 | 履約價 | OI | 資料來源 |
|---|---|---|---|
| Put OI 第1大履約價 | 46,000 | 2,273 | TAIFEX Proxy |
| Put OI 第2大履約價 | 45,500 | 1,915 | TAIFEX Proxy |
| Put OI 第3大履約價 | 45,000 | 1,701 | TAIFEX Proxy |
| Put OI 最大履約價 | 46,000 | 2,273 | TAIFEX Proxy |

#### Put OI 分布明細 Top10 (機器可讀，到期月份 202609F3)

| # | 履約價 | OI | 佔比 | 資料來源 |
|---|---|---|---|---|
| P1 | 46,000 | 2,273 | 6.69% | TAIFEX Proxy |
| P2 | 45,500 | 1,915 | 5.64% | TAIFEX Proxy |
| P3 | 45,000 | 1,701 | 5.01% | TAIFEX Proxy |
| P4 | 44,000 | 1,429 | 4.21% | TAIFEX Proxy |
| P5 | 42,500 | 1,369 | 4.03% | TAIFEX Proxy |
| P6 | 44,500 | 1,357 | 4.0% | TAIFEX Proxy |
| P7 | 45,700 | 1,127 | 3.32% | TAIFEX Proxy |
| P8 | 45,600 | 965 | 2.84% | TAIFEX Proxy |
| P9 | 45,300 | 892 | 2.63% | TAIFEX Proxy |
| P10 | 45,400 | 873 | 2.57% | TAIFEX Proxy |


### 9．Call OI 增減集中區

| 項目 | 履約價 (增減口數) | 資料來源 |
|---|---|---|
| Call OI 增加最多的履約價 | 48,200 (+3,518) | TAIFEX Proxy snapshots (2026-09-16) |
| Call OI 減少最多的履約價 | 45,300 (-166) | TAIFEX Proxy snapshots (2026-09-16) |

### 10．Put OI 增減集中區

| 項目 | 履約價 (增減口數) | 資料來源 |
|---|---|---|
| Put OI 增加最多的履約價 | 46,000 (+2,003) | TAIFEX Proxy snapshots (2026-09-16) |
| Put OI 減少最多的履約價 | 41,200 (-135) | TAIFEX Proxy snapshots (2026-09-16) |

### 11．Call Wall

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Call Wall 價位 | 48,200 | TAIFEX Proxy |
| 對應到期月份 | 202609F3 | TAIFEX Proxy |
| 與前一交易日的變化 (2026-09-16→2026-09-17) | +2,200 | TAIFEX Proxy snapshots (2026-09-16) |

### 12．Put Wall

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Put Wall 價位 | 46,000 | TAIFEX Proxy |
| 對應到期月份 | 202609F3 | TAIFEX Proxy |
| 與前一交易日的變化 (2026-09-16→2026-09-17) | +500 | TAIFEX Proxy snapshots (2026-09-16) |

### 13．Gamma Wall

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Gamma Wall 價位 | 46,500.00 | TAIFEX Proxy (options-market-structure-compact (proxy)) |
| 對應到期月份 | 202609F3 | TAIFEX Proxy |
| 資料日期 | 2026-09-16 | TAIFEX Proxy (options-market-structure-compact (proxy)) |

### 14．Gamma Flip

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Gamma Flip 價位 | 45,426.22 | TAIFEX Proxy (options-market-structure-compact (proxy)) |
| 對應到期月份 | 202609F3 | TAIFEX Proxy |
| 資料日期 | 2026-09-16 | TAIFEX Proxy (options-market-structure-compact (proxy)) |

### 15．Max Pain

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Max Pain 價位 | 46,000 | TAIFEX Proxy |
| 對應到期月份 | 202609F3 | TAIFEX Proxy |
| 與前一交易日的變化 (2026-09-16→2026-09-17) | +250 | TAIFEX Proxy snapshots (2026-09-16) |

### 16．資料來源、時間、時區與狀態

- 資料來源：TAIFEX 經 Cloudflare Worker Proxy
- 資料日期：2026-09-17；資料時間：2026-09-18 01:09:33；時區：`Asia/Taipei`
- 日盤／夜盤標記：日盤收盤後 + 夜盤盤後
- 未取得欄位 (5)：margin.ratio, futures.top10_change, options.chain_oi_change, options.pos_change, options.wall_change
- 註記：Gamma 資料日期 2026-09-16 (T0 2026-09-17 尚無，上游 FMTQIK 落後，採最新可得)
- 註記：夜盤 OHLC 資料日期 2026-09-16 (T0 2026-09-17)，來源 proxy
- 註記：法人交易量變化無昨日交易端點，標 unavailable
- 註記：Gamma Wall/Flip 資料日期 2026-09-16 (來源 options-market-structure-compact (proxy))

## 五、資料來源、時間與完整性

- 期貨/匯率為最新報價，其餘為 T0 收盤資料；時間皆為 `Asia/Taipei`。
- taiex：`twse-proxy`
- taiex_ohlc：`FinMind TaiwanStockPrice TAIEX`
- listed_turnover：`twse-proxy market_statistics`
- listed_breadth：`twse-proxy`
- otc：`TPEX OpenAPI tpex_mainborad_highlight`
- institutional：`twse-proxy /institutional`
- margin：`HiStock 上市+上櫃融資融券 (金額口徑)`
- sbl：`TWSE TWT96U + TPEX margin_sbl`
- 期貨選擇權：`TAIFEX Proxy`
- 新聞：台股 Yahoo／國際 Fed＋CNBC＋MarketWatch；台股 Yahoo / 國際 Fed 公告＋CNBC＋MarketWatch RSS；Fed 無摘要；investing 港股為主已退役；cnyes CSR、wantgoo JS 算繪、中央社/央行路徑待查，未採用
- 美股/亞股/期貨/匯率/ADR/商品：`Yahoo Finance Chart API`；美債：`Yahoo Finance (備援)`
- 註記：融資維持率未取得 (istock 失敗；官方無每日序列)
- 註記：上市 MI_MARGN / TWT96U 無日期欄，採用最新可得
- 註記：借券賣出餘額/增減為上櫃值 (上市 TWT93U 無機器接口)
- 本報告僅整理資料，不提供交易判斷。
