# DATA_REPORT_20261113

- 報告日期：`2026-11-17`
- T0 交易日期：`2026-11-13`
- 首次資料產出時間：`2026-11-17 16:35:37`
- 本次更新開始時間：`2026-11-17 16:35:37`
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
| 加權指數 | 43,675.12 | 點 | twse-proxy |
| 開盤 | 43,719.75 | 點 | FinMind TaiwanStockPrice TAIEX |
| 最高 | 44,489.48 | 點 | FinMind TaiwanStockPrice TAIEX |
| 最低 | 43,534.12 | 點 | FinMind TaiwanStockPrice TAIEX |
| 收盤 | 43,675.12 | 點 | twse-proxy |
| 漲跌點數 | 583.25 | 點 | twse-proxy |
| 漲跌幅 | +1.35 | % | twse-proxy |
| 成交金額 | 9,515.8 | 億元 | twse-proxy market_statistics |

### 2. 市場漲跌家數

#### 2.1 上市公司

**資料來源：** `Cloudflare Worker：twse-proxy` (備援 `TWSE OpenAPI twtazu_od`)

| 項目 | 家數 | 資料來源 |
|---|---|---|
| 上漲家數 | 811 | twse-proxy |
| 下跌家數 | 199 | twse-proxy |
| 平盤家數 | 74 | twse-proxy |
| 漲停家數 | 28 | twse-proxy |
| 跌停家數 | 3 | twse-proxy |

#### 2.2 上櫃公司

**資料來源：** `TPEX OpenAPI tpex_mainborad_highlight`

| 項目 | 家數 | 資料來源 |
|---|---|---|
| 上漲家數 | 584 | 沿用前版（原來源：TPEX OpenAPI tpex_mainborad_highlight） |
| 下跌家數 | 230 | 沿用前版（原來源：TPEX OpenAPI tpex_mainborad_highlight） |
| 平盤家數 | 62 | 沿用前版（原來源：TPEX OpenAPI tpex_mainborad_highlight） |
| 漲停家數 | 41 | 沿用前版（原來源：TPEX OpenAPI tpex_mainborad_highlight） |
| 跌停家數 | 1 | 沿用前版（原來源：TPEX OpenAPI tpex_mainborad_highlight） |

### 3. 三大法人現貨買賣超

**資料來源：** `unavailable`

| 法人別 | 買賣超金額 | 單位 | 資料來源 |
|---|---|---|---|
| 外資 | +288.4 | 億元 | 沿用前版（原來源：twse-proxy /institutional） |
| 投信 | +95.4 | 億元 | 沿用前版（原來源：twse-proxy /institutional） |
| 自營商 | +68.9 | 億元 | 沿用前版（原來源：twse-proxy /institutional） |
| 三大法人合計 | +452.7 | 億元 | 沿用前版（原來源：twse-proxy /institutional） |

### 4. 融資融券

**資料來源：** 上市+上櫃 `HiStock 上市+上櫃融資融券 (金額口徑；合計需雙市場欄位完整)` (金額口徑)；維持率 `TWSE 上市自建估算（當日暫估；資料日期：2026-11-13；估值 1240 檔；4 檔採最近有效收盤價（價格日期 20260402 至 20261113）；Blave 同 T0 交叉驗證 170.6740%；差異 0.281 個百分點；門檻 <1.00 個百分點；PASS）`；官方無每日維持率序列

| 項目 | 數值 | 單位 | 資料來源 |
|---|---|---|---|
| 融資餘額 | 7,086.2 | 億元 | HiStock 上市+上櫃融資融券 (金額口徑；合計需雙市場欄位完整) |
| 融資增減 | +50.5 | 億元 | HiStock 上市+上櫃融資融券 (金額口徑；合計需雙市場欄位完整) |
| 融券餘額 | 245,881 | 張 | HiStock 上市+上櫃融資融券 (金額口徑；合計需雙市場欄位完整) |
| 融券增減 | -589 | 張 | HiStock 上市+上櫃融資融券 (金額口徑；合計需雙市場欄位完整) |
| 融資維持率 | 170.95 | % | TWSE 上市自建估算（當日暫估；資料日期：2026-11-13；估值 1240 檔；4 檔採最近有效收盤價（價格日期 20260402 至 20261113）；Blave 同 T0 交叉驗證 170.6740%；差異 0.281 個百分點；門檻 <1.00 個百分點；PASS） |

### 5. 借券資料

**資料來源：** 各欄位依實際取得市場分別標示；借券賣出餘額／增減使用上市 TWT93U 與上櫃 tpex_margin_sbl，缺值市場不納入加總。

| 項目 | 數值 | 單位 | 資料來源 |
|---|---|---|---|
| 整體市場借券餘額 | 33,444,253 | 張 | TWSE TWT72U（SLBNLB；上市+上櫃） |

| 項目 | 上市 | 上櫃 | 兩者合計 | 單位 |
|---|---|---|---|---|
| 借券賣出餘額 | 18,406,286.185 | 2,194,511.001 | 20,600,797.186 | 張 |
| 借券賣出增減 | -27,354.195 | +2,645.279 | -24,708.916 | 張 |

- 上市來源：TWSE TWT93U（上市）；增減來源：TWSE TWT93U（上市）
- 上櫃來源：TPEx S47（上櫃）；增減來源：TPEx S47（上櫃）
- 借券賣出餘額完整性：`complete`
- 借券賣出增減完整性：`complete`
- TWSE TWT93U（上市）：資料日期：`20261113`；最後預定更新：`23:30`；來源回報產製時間：`unavailable`；本次查詢時間：`2026-11-17T16:36:01+08:00`；狀態：`available_after_schedule`
- TPEx S47（上櫃）：資料日期：`20261113`；最後預定更新：`22:30`；來源回報產製時間：`unavailable`；本次查詢時間：`2026-11-17T16:36:07+08:00`；狀態：`available_after_schedule`

### 6. 市場成交結構

**資料來源：** 上市 `twse-proxy market_statistics`、上櫃 `unavailable`

| 項目 | 成交金額 | 單位 | 資料來源 |
|---|---|---|---|
| 上市成交金額 | 9,515.8 | 億元 | twse-proxy market_statistics |
| 上櫃成交金額 | 2,183.5 | 億元 | 沿用前版（原來源：TPEX OpenAPI tpex_mainborad_highlight） |
| 上市櫃成交金額合計 | 11,699.3 | 億元 | 沿用前版（原來源：twse-proxy market_statistics／TPEX OpenAPI tpex_mainborad_highlight） |

## 二、重要市場

### 1. 美股指數

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 收盤／最新值 | 漲跌值 | 漲跌幅 | 資料日期（交易所時區） | 擷取時間（UTC） | 交易所時區 | 資料來源 |
|---|---|---|---|---|---|---|---|---|
| S&P 500 | ^GSPC | 7,416.59 | -145.08 | -1.92 | 2026-11-16 | 2026-11-17T08:36:07+00:00 | America/New_York | Yahoo Finance Chart API |
| Nasdaq Composite | ^IXIC | 24,509.76 | -626.51 | -2.49 | 2026-11-16 | 2026-11-17T08:36:07+00:00 | America/New_York | Yahoo Finance Chart API |
| Nasdaq 100 | ^NDX | 27,197.15 | -746.59 | -2.67 | 2026-11-16 | 2026-11-17T08:36:07+00:00 | America/New_York | Yahoo Finance Chart API |
| Dow Jones | ^DJI | 51,608.17 | -739.38 | -1.41 | 2026-11-16 | 2026-11-17T08:36:07+00:00 | America/New_York | Yahoo Finance Chart API |
| 費城半導體 SOX | ^SOX | 9,610.65 | -535.67 | -5.28 | 2026-11-16 | 2026-11-17T08:36:07+00:00 | America/New_York | Yahoo Finance Chart API |
| VIX | ^VIX | 23.15 | 0.24 | +1.05 | 2026-11-17 | 2026-11-17T08:36:07+00:00 | America/Chicago | Yahoo Finance Chart API |

### 2. 亞洲主要指數

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 收盤／最新值 | 漲跌值 | 漲跌幅 | 資料日期（交易所時區） | 擷取時間（UTC） | 交易所時區 | 資料來源 |
|---|---|---|---|---|---|---|---|---|
| 日經225 | ^N225 | 58,860.43 | -801.59 | -1.34 | 2026-11-17 | 2026-11-17T08:36:07+00:00 | Asia/Tokyo | Yahoo Finance Chart API |
| 韓國KOSPI | ^KS11 | 4,968.48 | -132.02 | -2.59 | 2026-11-17 | 2026-11-17T08:36:07+00:00 | Asia/Seoul | Yahoo Finance Chart API |
| 香港恆生 | ^HSI | 23,508.17 | -245.67 | -1.03 | 2026-11-17 | 2026-11-17T08:36:07+00:00 | Asia/Hong_Kong | Yahoo Finance Chart API |
| 上海綜合 | 000001.SS | 3,584.58 | -17.99 | -0.50 | 2026-11-17 | 2026-11-17T08:36:07+00:00 | Asia/Shanghai | Yahoo Finance Chart API |
| 深圳成分 | 399001.SZ | 10,638.52 | -52.26 | -0.49 | 2026-11-17 | 2026-11-17T08:36:07+00:00 | Asia/Shanghai | Yahoo Finance Chart API |

### 3. 美股指數期貨

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 最新值 | 漲跌值 | 漲跌幅 | 資料日期（交易所時區） | 擷取時間（UTC） | 交易所時區 | 資料來源 |
|---|---|---|---|---|---|---|---|---|
| S&P500期貨 | ES=F | 7,427.50 | -11.50 | -0.15 | 2026-11-17 | 2026-11-17T08:36:08+00:00 | America/New_York | Yahoo Finance Chart API |
| Nasdaq100期貨 | NQ=F | 27,313.25 | 29.00 | +0.11 | 2026-11-17 | 2026-11-17T08:36:08+00:00 | America/New_York | Yahoo Finance Chart API |
| 道瓊期貨 | YM=F | 51,491.00 | -179.00 | -0.35 | 2026-11-17 | 2026-11-17T08:36:08+00:00 | America/New_York | Yahoo Finance Chart API |
| Russell2000期貨 | RTY=F | 2,741.90 | -9.50 | -0.35 | 2026-11-17 | 2026-11-17T08:36:08+00:00 | America/New_York | Yahoo Finance Chart API |

### 4. 美國國債殖利率

**資料來源：** `U.S. Treasury Fiscal Data API` (失敗時備援 Treasury yield.xml 與 `Yahoo Finance`)

| 項目 | API 資料欄位／識別 | 殖利率（%） | 日變化（百分點） | 資料日期 | 擷取時間（UTC） | 資料來源 |
|---|---|---|---|---|---|---|
| 美國 2 年期殖利率 | 2 Yr | 4.83 | -0.05 | 16-NOV-26 | 2026-11-17T08:36:29+00:00 | U.S. Treasury yield.xml（BC_2YEAR 備援） |
| 美國 10 年期殖利率 | 10 Yr | 5.12 | -0.03 | 2026-11-16 | 2026-11-17T08:36:29+00:00 | Yahoo Finance (備援) |
| 美國 20 年期殖利率 | 20 Yr | 5.51 | -0.01 | 16-NOV-26 | 2026-11-17T08:36:45+00:00 | U.S. Treasury yield.xml（BC_20YEAR 備援） |
| 美國 30 年期殖利率 | 30 Yr | 5.47 | -0.01 | 2026-11-16 | 2026-11-17T08:36:45+00:00 | Yahoo Finance (備援) |

### 5. 主要匯率

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 最新值 | 漲跌值 | 漲跌幅 | 資料日期（交易所時區） | 擷取時間（UTC） | 交易所時區 | 資料來源 |
|---|---|---|---|---|---|---|---|---|
| USD/TWD | TWD=X | 32.91 | 0.03 | +0.11 | 2026-11-17 | 2026-11-17T08:36:08+00:00 | Europe/London | Yahoo Finance Chart API |
| DXY美元指數 | DX-Y.NYB | 103.54 | -0.01 | -0.01 | 2026-11-17 | 2026-11-17T08:36:08+00:00 | America/New_York | Yahoo Finance Chart API |
| USD/JPY | JPY=X | 159.20 | -0.58 | -0.36 | 2026-11-17 | 2026-11-17T08:36:08+00:00 | Europe/London | Yahoo Finance Chart API |
| USD/KRW | KRW=X | 1,335.98 | 2.73 | +0.20 | 2026-11-17 | 2026-11-17T08:36:08+00:00 | Europe/London | Yahoo Finance Chart API |

### 6. 台灣相關ADR

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 收盤／最新值 | 漲跌值 | 漲跌幅 | 資料日期（交易所時區） | 擷取時間（UTC） | 交易所時區 | 資料來源 |
|---|---|---|---|---|---|---|---|---|
| 台積電ADR | TSM | 373.45 | -25.28 | -6.34 | 2026-11-16 | 2026-11-17T08:36:08+00:00 | America/New_York | Yahoo Finance Chart API |
| 聯電ADR | UMC | 14.34 | -1.06 | -6.88 | 2026-11-16 | 2026-11-17T08:36:08+00:00 | America/New_York | Yahoo Finance Chart API |
| 日月光ADR | ASX | 32.80 | -2.75 | -7.74 | 2026-11-16 | 2026-11-17T08:36:08+00:00 | America/New_York | Yahoo Finance Chart API |

### 7. 原油黃金Bitcoin

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 收盤／最新值 | 漲跌值 | 漲跌幅 | 資料日期（交易所時區） | 擷取時間（UTC） | 交易所時區 | 資料來源 |
|---|---|---|---|---|---|---|---|---|
| WTI原油期貨 | CL=F | 85.43 | -0.29 | -0.34 | 2026-11-17 | 2026-11-17T08:36:08+00:00 | America/New_York | Yahoo Finance Chart API |
| 黃金期貨 | GC=F | 3,869.90 | 16.90 | +0.44 | 2026-11-17 | 2026-11-17T08:36:08+00:00 | America/New_York | Yahoo Finance Chart API |
| Bitcoin | BTC-USD | 64,310.96 | -544.88 | -0.84 | 2026-11-17 | 2026-11-17T08:36:08+00:00 | UTC | Yahoo Finance Chart API |

### 8. 重大經濟數據、央行事件與重大市場新聞

**資料來源：** 台股 `tw.stock.yahoo.com` (含內文摘要)；國際 `Fed 公告 RSS`＋`CNBC`＋`MarketWatch` (標題、來源、時間與連結)

- 事件1：外資何時轉買？分析師點名看月底MSCI調整
  - 來源：Yahoo 台股；發布時間：2026-11-17T07:08:32Z；台北時間：2026-11-17 15:08
  - 摘要：台股今（17）日終場重挫947點，險守4萬點大關，三大法人今日合計賣超547.25億元，其中外資再砍380.93億元，連續2日提款逾千億元。資深台股分析師呂漢威表示，外資賣超金額雖然縮小，但期貨空單卻增加，可能將部分現貨賣壓轉向期貨避險，並
  - 原文連結：https://tw.stock.yahoo.com/news/%E3%80%90follow%E6%B3%95%E4%BA%BA%E3%80%91%E5%A4%96%E8%B3%87%E5%86%8D%E7%A0%8D381%E5%84%84%E5%85%83%EF%BC%81%E9%80%A32%E6%97%A5%E6%8F%90%E6%AC%BE%E9%80%BE%E5%8D%83%E5%84%84%E5%85%83-%E5%88%86%E6%9E%90%E5%B8%AB%EF%BC%9A%E8%B3%A3%E5%A3%93%E8%BD%89%E5%90%91%E6%9C%9F%E8%B2%A8%E9%81%BF%E9%9A%AA-072725252.html
- 事件2：台股跌過頭 投顧董座揭13倍本益比訊號
  - 來源：Yahoo 台股；發布時間：2026-11-17T07:36:57Z；台北時間：2026-11-17 15:36
  - 摘要：台股近期震盪劇烈，明年還有機會再創高嗎？凱基投顧今（17）日發布2027年投資展望，若以明年企業預估獲利的18倍計算，台股有機會上看5萬5千點。凱基投顧董事長朱晏民對台股後市仍持正面看法，認為企業明年獲利有望繼續增加，並看好晶圓代工、散熱、
  - 原文連結：https://tw.stock.yahoo.com/news/%E5%8F%B0%E8%82%A1%E6%98%8E%E5%B9%B4%E4%B8%8A%E7%9C%8B5%E8%90%AC5%E5%8D%83%E9%BB%9E%EF%BC%9F%E5%87%B1%E5%9F%BA%E6%8A%95%E9%A1%A7%E8%91%A3%E5%BA%A7%E7%9C%8B%E5%A5%BD%E5%BE%8C%E5%B8%82-4%E5%A4%A7%E6%97%8F%E7%BE%A4%E5%8F%97%E6%83%A0-082220400.html
- 事件3：吃瓦城要多掏錢了 5品牌11/24起調漲
  - 來源：Yahoo 台股；發布時間：2026-11-17T08:19:24Z；台北時間：2026-11-17 16:19
  - 摘要：瓦城要漲價了！瓦城集團今（17）日宣布，因應食材原物料價格波動、基本工資調升及營運成本增加，將自11月24日起，調整旗下「瓦城」、「非常泰」、「1010湘」、「時時香」及「大心」五品牌部分品項價格，整體平均調幅約3.6%。其中，大心兩年以來
  - 原文連結：https://tw.stock.yahoo.com/news/%E7%93%A6%E5%9F%8E%E8%A6%81%E6%BC%B2%E5%83%B9%E4%BA%86%EF%BC%81%E6%97%97%E4%B8%8B%E4%BA%94%E5%93%81%E7%89%8C1124%E8%B5%B7%E8%AA%BF%E6%BC%B2-%E5%A4%A7%E5%BF%83%E3%80%8C%E9%85%B8%E8%BE%A3%E6%B5%B7%E9%99%B8%E9%BA%B5%E3%80%8D%E4%B8%80%E7%A2%97%E8%B2%B418%E5%85%83-081924031.html
- 事件4：投顧看明年台股最悲觀恐探32K 揭最大黑天鵝
  - 來源：Yahoo 台股；發布時間：2026-11-17T06:23:57Z；台北時間：2026-11-17 14:23
  - 摘要：全球AI晶片霸主輝達（NVIDIA）前執行長黃仁勳日前閃電辭職，引發全球震撼。群益金融集團今（17）日舉辦「2027年投資展望說明會」，預估明年台股指數主要區間落在35,000至50,000點，樂觀情境下有機會挑戰53,000點，悲觀情境則
  - 原文連結：https://tw.stock.yahoo.com/news/%E3%80%8C%E6%9C%80%E5%A4%A7%E9%BB%91%E5%A4%A9%E9%B5%9D%E3%80%8D%E6%9B%9D%E5%85%89%EF%BC%81%E7%BE%A4%E7%9B%8A%E6%8A%95%E9%A1%A7%E7%9C%8B%E6%98%8E%E5%B9%B4%E5%8F%B0%E8%82%A1%E6%9C%80%E6%85%98%E6%81%90%E4%B8%8B%E6%8E%A232000%E9%BB%9E-13%E6%AA%94%E3%80%8C%E6%98%8E%E7%89%8C%E3%80%8D%E4%B8%80%E6%AC%A1%E7%9C%8B-062357141.html
- 事件5：今年EPS會更高！玉山金董座：會適度提高股利
  - 來源：Yahoo 台股；發布時間：2026-11-17T06:37:12Z；台北時間：2026-11-17 14:37
  - 摘要：擁61萬股東的玉山金控（2884）今（17）日召開第三季法人說明會，由董事長黃男州親自主持。今年前10月每股獲利2.14元，被問到明年的股利看法？黃 男州承諾說「今年EPS會更高，也會適度提高股利，給長期支持玉山金的股東。」未來都會以現金股
  - 原文連結：https://tw.stock.yahoo.com/news/%E7%8E%89%E5%B1%B1%E9%87%91%E6%B3%95%E8%AA%AA1%E3%80%8B%E8%AB%87%E6%98%8E%E5%B9%B4%E8%82%A1%E5%88%A9-%E9%BB%83%E7%94%B7%E5%B7%9E%E6%89%BF%E8%AB%BE%E3%80%8C%E6%9C%83%E8%B6%85%E9%81%8E%E4%BB%8A%E5%B9%B4%E3%80%8D-%E4%B8%89%E5%95%86%E5%A3%BD%E8%B3%BA%E9%8C%A2%E5%85%88%E7%95%99%E5%B8%B3%E4%B8%8A-063712284.html
- 事件6：ASIC三雄有機會篡位 法人點名爆發力最強股獲利拚增三倍
  - 來源：Yahoo 台股；發布時間：2026-11-16T22:00:30Z；台北時間：2026-11-17 06:00
  - 摘要：輝達失去黃仁勳，是否會影響客戶訂單外流對手？法人認為，目前已經確定VERA RUBIN從2026年起出貨，以及下世代FEYNMAN預定2028年問世，短期不會出現轉單，但會加速CSP研發自研晶片，未來ASIC有望篡位，首推創意、世芯、聯發科
  - 原文連結：https://tw.stock.yahoo.com/news/%E8%BC%9D%E9%81%94%E6%B2%92%E4%BA%86%E9%BB%83%E4%BB%81%E5%8B%B3-asic%E4%B8%89%E9%9B%84%E7%AF%A1%E4%BD%8D-%E8%80%81%E7%89%8C%E6%8A%95%E9%A1%A7%E9%A6%96%E6%8E%A8%E5%89%B5%E6%84%8F-%E4%B8%96%E8%8A%AF-%E8%81%AF%E7%99%BC%E7%A7%91-220030159.html
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
- 事件10：Analysis: The Fed's chairman sees an AI revolution coming. Now he has to figure out what it means
  - 來源：CNBC；發布時間：Tue, 17 Nov 2026 00:42:33 GMT；台北時間：2026-11-17 08:42
  - 摘要：Kevin Warsh sees AI at a turning point. He faces tough questions on jobs and interest rates.
  - 原文連結：https://www.cnbc.com/2026/11/16/kevin-warsh-fed-ai-jobs-productivity-interest-rateshtml.html
- 事件11：Treasury yields are broadly flat as investors await retail sales data
  - 來源：CNBC；發布時間：Tue, 17 Nov 2026 08:23:51 GMT；台北時間：2026-11-17 16:23
  - 摘要：U.S. Treasury yields were little changed on Tuesday morning as investors awaited economic data and comments from Federal Reserve officials later in th
  - 原文連結：https://www.cnbc.com/2026/11/17/treasury-yields-bonds-inflation.html
- 事件12：Fed Chairman Kevin Warsh stresses importance of AI to economy, but says it could ‘disappoint’
  - 來源：CNBC；發布時間：Mon, 16 Nov 2026 18:46:07 GMT；台北時間：2026-11-17 02:46
  - 摘要：unavailable
  - 原文連結：https://www.cnbc.com/2026/11/16/fed-ai-task-force-kevin-warsh.html


## 三、期貨

**資料來源：**
1. Cloudflare Workers：TAIFEX Proxy — https://taifex.grichtoyang.workers.dev/
2. TAIFEX Open API — https://openapi.taifex.com.tw/

近月契約月份：202611 (日盤成交量最大者)；交易日期：2026-11-13

### 1．台指期近月日盤行情

| 項目 | 數值 | 單位 | 資料來源 |
|---|---|---|---|
| 開盤價 | 40,590 | 點 | TAIFEX Proxy |
| 最高價 | 41,828 | 點 | TAIFEX Proxy |
| 最低價 | 39,761 | 點 | TAIFEX Proxy |
| 收盤價 | 40,073 | 點 | TAIFEX Proxy |
| 漲跌點數 | -708 | 點 | TAIFEX Proxy |
| 漲跌幅 | -1.74 | % | TAIFEX Proxy |
| 成交量 | 138,833 | 口 | TAIFEX Proxy |
| 日盤高點及低點 | 41,828 / 39,761 | 點 | TAIFEX Proxy |

### 2．台指期近月夜盤行情

| 項目 | 數值 | 單位 | 資料來源 |
|---|---|---|---|
| 開盤價 | 43,921 | 點 | TAIFEX Proxy |
| 最高價 | 44,423 | 點 | TAIFEX Proxy |
| 最低價 | 42,956 | 點 | TAIFEX Proxy |
| 收盤價 | 43,706 | 點 | TAIFEX Proxy |
| 漲跌點數 | -133 | 點 | TAIFEX Proxy |
| 漲跌幅 | -0.30 | % | TAIFEX Proxy |
| 成交量 | 56,132 | 口 | TAIFEX Proxy |
| 夜盤高點及低點 | 44,423 / 42,956 | 點 | TAIFEX Proxy |

### 3．法人台指期多空未平倉部位

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 外資多方 OI | 6,186 | TAIFEX Proxy |
| 外資空方 OI | 107,056 | TAIFEX Proxy |
| 外資多空淨 OI | -100,870 | TAIFEX Proxy |
| 投信多方 OI | 103,019 | TAIFEX Proxy |
| 投信空方 OI | 3,096 | TAIFEX Proxy |
| 投信多空淨 OI | +99,923 | TAIFEX Proxy |
| 自營商多方 OI | 3,733 | TAIFEX Proxy |
| 自營商空方 OI | 6,504 | TAIFEX Proxy |
| 自營商多空淨 OI | -2,771 | TAIFEX Proxy |
| 三大法人合計多方 OI | 112,938 | TAIFEX Proxy |
| 三大法人合計空方 OI | 116,656 | TAIFEX Proxy |
| 三大法人合計多空淨 OI | -3,718 | TAIFEX Proxy |
| 外資多空淨 OI 變化 | -1,297 | TAIFEX Proxy |
| 投信多空淨 OI 變化 | +1,022 | TAIFEX Proxy |
| 自營商多空淨 OI 變化 | -2,584 | TAIFEX Proxy |

### 4．前十大交易人多空未平倉部位

**資料來源：** `TAIFEX OpenAPI OpenInterestOfLargeTradersFutures`（備援 TAIFEX Proxy；欄位依實際取得來源標示）

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 前十大交易人多方 OI | 39,917 | TAIFEX Proxy |
| 前十大交易人空方 OI | 35,820 | TAIFEX Proxy |
| 前十大交易人多空淨 OI | +4,097 | TAIFEX Proxy |
| 多空淨 OI 變化 (2026-11-11→2026-11-16) | -15,651 | TAIFEX Proxy snapshots (2026-11-12) |
- 資料日期：2026-11-16 (TypeOfTraders=0 全部交易人；契約月份 202611)

### 5．日盤、夜盤法人交易資料

| 項目 | 數值 | 單位 | 資料來源 |
|---|---|---|---|
| 外資日盤多單交易量 | 153,931 | 口 | TAIFEX Proxy |
| 外資日盤空單交易量 | 155,075 | 口 | TAIFEX Proxy |
| 外資日盤多空淨交易量 | -1,144 | 口 | TAIFEX Proxy |
| 外資夜盤多單交易量 | 30,221 | 口 | 沿用前版（原來源：TAIFEX Proxy） |
| 外資夜盤空單交易量 | 31,852 | 口 | 沿用前版（原來源：TAIFEX Proxy） |
| 外資夜盤多空淨交易量 | -1,631 | 口 | 沿用前版（原來源：TAIFEX Proxy） |
| 外資日盤／夜盤交易量變化 | +334 | 口 | 沿用前版（原來源：TAIFEX Proxy） |
| 投信日盤多空淨交易量 | -1,180 | 口 | TAIFEX Proxy |
| 投信夜盤多空淨交易量 | +0 | 口 | 沿用前版（原來源：TAIFEX Proxy） |
| 投信日盤／夜盤交易量變化 | +1,022 | 口 | 沿用前版（原來源：TAIFEX Proxy） |
| 自營商日盤多空淨交易量 | -1,820 | 口 | TAIFEX Proxy |
| 自營商夜盤多空淨交易量 | +741 | 口 | 沿用前版（原來源：TAIFEX Proxy） |
| 自營商日盤／夜盤交易量變化 | -3,264 | 口 | 沿用前版（原來源：TAIFEX Proxy） |
| 三大法人日盤多空淨交易量 | -4,144 | 口 | TAIFEX Proxy |
| 三大法人夜盤多空淨交易量 | -890 | 口 | 沿用前版（原來源：TAIFEX Proxy） |
| 法人日盤交易金額淨額 | -341.2 | 億元 | TAIFEX Proxy |
| 法人夜盤交易金額淨額 | -79.5 | 億元 | 沿用前版（原來源：TAIFEX Proxy） |

### 6．期貨與現貨關係

| 項目 | 數值 | 資料來源 |
|---|---|---|
| 台指期近月價格 | 40,073 | TAIFEX Proxy |
| 加權指數價格 | 43,675.12 | twse-proxy |
| 台指期與加權指數價差 | -3,602.12 | TAIFEX Proxy／twse-proxy |
| 價差百分比 | -8.25 | TAIFEX Proxy／twse-proxy |
| 日盤基差 | -3,602.12 | TAIFEX Proxy／twse-proxy |
| 夜盤價格相對日盤收盤的變化 | +3,633 | TAIFEX Proxy |

### 7．日盤、夜盤與籌碼變化對照

#### 7.1 日夜盤價格與成交量對照 (變化 = 日盤 - 夜盤)

| 項目 | 日盤 | 夜盤 | 變化 (日-夜) | 資料來源 |
|---|---|---|---|---|
| 收盤價 | 40,073 | 43,706 | -3,633 | TAIFEX Proxy |
| 成交量 | 138,833 | 56,132 | +82,701 | TAIFEX Proxy |
- 台指期總 OI 前日變化：-2,859（來源：TAIFEX Proxy）


#### 7.2 法人籌碼日夜盤對照 (淨變化 = 日盤淨 - 夜盤淨；OI 為日盤收盤後總量，前日變化另列)

| 法人 | 交易量 |  |  |  |  |  |  | 未平倉量 |  |  |  | 資料來源 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|  | **日盤多單** | **日盤空單** | **日盤淨** | **夜盤多單** | **夜盤空單** | **夜盤淨** | **淨變化 (日-夜)** | **OI多方** | **OI空方** | **OI淨** | **OI前日變化** |  |
| 外資 | 153,931 | 155,075 | -1,144 | 30,221 | 31,852 | -1,631 | +334 | 6,186 | 107,056 | -100,870 | -1,297 | 沿用前版（原來源：TAIFEX Proxy） |
| 投信 | 33,611 | 34,791 | -1,180 | 0 | 0 | +0 | +1,022 | 103,019 | 3,096 | +99,923 | +1,022 | 沿用前版（原來源：TAIFEX Proxy） |
| 自營商 | 15,358 | 17,178 | -1,820 | 1,679 | 938 | +741 | -3,264 | 3,733 | 6,504 | -2,771 | -2,584 | 沿用前版（原來源：TAIFEX Proxy） |
| 三大法人合計 | 202,900 | 207,044 | -4,144 | 31,900 | 32,790 | -890 | -1,908 | 112,938 | 116,656 | -3,718 | -2,859 | 沿用前版（原來源：TAIFEX Proxy） |

#### 7.3 前十大交易人日夜盤對照 (OI 無日夜拆分，列收盤後總量)

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 前十大交易人多方 OI | 39,917 | TAIFEX Proxy |
| 前十大交易人空方 OI | 35,820 | TAIFEX Proxy |
| 前十大交易人多空淨 OI | +4,097 | TAIFEX Proxy |
| 前十大交易人多空淨 OI 變化 (2026-11-11→2026-11-16) | -15,651 | TAIFEX Proxy snapshots (2026-11-12) |

#### 7.4 夜盤劇本分類 (規則對應：夜盤漲跌 × 外資夜盤偏多空)

| 項目 | 數值 | 資料來源 |
|---|---|---|
| 夜盤成交量占比 (夜盤量／(夜盤量＋日盤量)) | 28.79% | TAIFEX Proxy |
| 夜盤漲跌點數 | -133 | TAIFEX Proxy |
| 外資夜盤多空淨交易量 | -1,631 | 沿用前版（原來源：TAIFEX Proxy） |
| 劇本分類 | 劇本三 | 沿用前版（原來源：規則對應） |
| 劇本條件 | 夜盤下跌＋外資偏空 | 沿用前版（原來源：規則對應） |
| 劇本特徵 | 開低、續跌機率高 | 沿用前版（原來源：規則對應） |

## 四、選擇權

**資料來源：** 主要 TAIFEX 經 Cloudflare Worker Proxy；時區 `Asia/Taipei`

### 1．選擇權交易日期、到期日與報告產製時間

| 項目 | 數值 | 資料來源 |
|---|---|---|
| 交易日期 | 2026-11-13 | TAIFEX Proxy |
| 到期月份／到期日 | 202611F2 | TAIFEX Proxy |
| 本次報告產製時間 | 2026-11-17 16:35:37 | 本機 |
| 日盤／夜盤標記 | 日盤收盤後資料 | TAIFEX Proxy |

### 2．Call 總成交量、OI、OI 增減

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Call 總成交量 | 419,770 | TAIFEX Proxy |
| Call 總未平倉量 OI | 83,365 | TAIFEX Proxy |
| Call OI 增減（共同合約） (2026-11-12→2026-11-13) | +29,709 | TAIFEX Proxy snapshot bundle (2026-11-12→2026-11-13) |

### 3．Put 總成交量、OI、OI 增減

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Put 總成交量 | 430,162 | TAIFEX Proxy |
| Put 總未平倉量 OI | 74,992 | TAIFEX Proxy |
| Put OI 增減（共同合約） (2026-11-12→2026-11-13) | +38,519 | TAIFEX Proxy snapshot bundle (2026-11-12→2026-11-13) |

### 4．Call／Put 比例與變化

| 項目 | 數值 | 單位 | 資料來源 |
|---|---|---|---|
| Call／Put 成交量比例 | 0.98 | 倍 | TAIFEX Proxy |
| Call／Put 未平倉量比例 | 1.11 | 倍 | TAIFEX Proxy |
| Put／Call Ratio | 0.90 | 倍 | TAIFEX Proxy |
| Call／Put 成交量比例變化 (2026-11-13→2026-11-16) | -17.65 | 百分點（pp） | TAIFEX Proxy |
| Call／Put OI 比例變化 (2026-11-13→2026-11-16) | -3.96 | 百分點（pp） | TAIFEX Proxy |
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
| Call OI 第1大履約價 | 44,000 | 4,861 | TAIFEX Proxy |
| Call OI 第2大履約價 | 46,000 | 4,603 | TAIFEX Proxy |
| Call OI 第3大履約價 | 45,000 | 4,321 | TAIFEX Proxy |
| Call OI 最大履約價 | 44,000 | 4,861 | TAIFEX Proxy |

#### Call OI 分布明細 Top10 (機器可讀，到期月份 202611F2)

| # | 履約價 | OI | 佔比 | 資料來源 |
|---|---|---|---|---|
| C1 | 44,000 | 4,861 | 5.83% | TAIFEX Proxy |
| C2 | 46,000 | 4,603 | 5.52% | TAIFEX Proxy |
| C3 | 45,000 | 4,321 | 5.18% | TAIFEX Proxy |
| C4 | 43,800 | 3,483 | 4.18% | TAIFEX Proxy |
| C5 | 47,000 | 3,084 | 3.7% | TAIFEX Proxy |
| C6 | 44,500 | 2,626 | 3.15% | TAIFEX Proxy |
| C7 | 44,600 | 2,551 | 3.06% | TAIFEX Proxy |
| C8 | 43,850 | 2,455 | 2.94% | TAIFEX Proxy |
| C9 | 43,900 | 2,434 | 2.92% | TAIFEX Proxy |
| C10 | 44,200 | 2,025 | 2.43% | TAIFEX Proxy |


### 8．主要 Put OI 集中區

| 項目 | 履約價 | OI | 資料來源 |
|---|---|---|---|
| Put OI 第1大履約價 | 43,000 | 3,916 | TAIFEX Proxy |
| Put OI 第2大履約價 | 39,000 | 3,474 | TAIFEX Proxy |
| Put OI 第3大履約價 | 43,500 | 3,020 | TAIFEX Proxy |
| Put OI 最大履約價 | 43,000 | 3,916 | TAIFEX Proxy |

#### Put OI 分布明細 Top10 (機器可讀，到期月份 202611F2)

| # | 履約價 | OI | 佔比 | 資料來源 |
|---|---|---|---|---|
| P1 | 43,000 | 3,916 | 5.22% | TAIFEX Proxy |
| P2 | 39,000 | 3,474 | 4.63% | TAIFEX Proxy |
| P3 | 43,500 | 3,020 | 4.03% | TAIFEX Proxy |
| P4 | 42,000 | 2,975 | 3.97% | TAIFEX Proxy |
| P5 | 43,700 | 2,709 | 3.61% | TAIFEX Proxy |
| P6 | 43,750 | 2,690 | 3.59% | TAIFEX Proxy |
| P7 | 43,600 | 2,500 | 3.33% | TAIFEX Proxy |
| P8 | 43,800 | 2,395 | 3.19% | TAIFEX Proxy |
| P9 | 40,000 | 2,303 | 3.07% | TAIFEX Proxy |
| P10 | 41,000 | 1,795 | 2.39% | TAIFEX Proxy |


### 9．Call OI 增減集中區

| 項目 | 履約價 (增減口數) | 資料來源 |
|---|---|---|
| Call OI 增加最多的履約價（共同合約） | 43,800 (+3,043) | TAIFEX Proxy snapshot bundle (2026-11-12→2026-11-13) |
| Call OI 減少最多的履約價（共同合約） | 49,500 (-400) | TAIFEX Proxy snapshot bundle (2026-11-12→2026-11-13) |

### 10．Put OI 增減集中區

| 項目 | 履約價 (增減口數) | 資料來源 |
|---|---|---|
| Put OI 增加最多的履約價（共同合約） | 43,750 (+2,607) | TAIFEX Proxy snapshot bundle (2026-11-12→2026-11-13) |
| Put OI 減少最多的履約價（共同合約） | 42,800 (-89) | TAIFEX Proxy snapshot bundle (2026-11-12→2026-11-13) |

### 11．Call Wall

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Call Wall 價位 | 44,000 | TAIFEX Proxy |
| 對應到期月份 | 202611F2 | TAIFEX Proxy |
| 與前一交易日的變化 (2026-11-12→2026-11-13) | -2,000 | TAIFEX Proxy snapshots (2026-11-12) |

### 12．Put Wall

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Put Wall 價位 | 43,000 | TAIFEX Proxy |
| 對應到期月份 | 202611F2 | TAIFEX Proxy |
| 與前一交易日的變化 (2026-11-12→2026-11-13) | +0 | TAIFEX Proxy snapshots (2026-11-12) |

### 13．Gamma Wall

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Gamma Wall 價位 | 43,600.00 | options-gamma-levels |
| GEX 實際使用到期月份 | 202611 | options-gamma-levels（GEX 實際使用） |
| GEX 實際到期日 | 2026-11-18 | options-gamma-levels（GEX 實際使用） |
| Options Key Levels 主到期月份 | 202611F2 | TAIFEX Proxy |
| 資料日期 | 2026-11-13 | TAIFEX Proxy (options-gamma-levels) |

### 14．Gamma Flip

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Gamma Flip 價位 | 42,826.92 | options-gamma-levels |
| GEX 實際使用到期月份 | 202611 | options-gamma-levels（GEX 實際使用） |
| GEX 實際到期日 | 2026-11-18 | options-gamma-levels（GEX 實際使用） |
| 主到期月份（Key Levels） | 202611F2 | TAIFEX Proxy |
| 原始 Call OI（選定到期日全部有效 Chain 合約） | 69,907 | options-gamma-levels（GEX 到期日） |
| 模型納入 Call OI（通過 GEX 計算條件） | 69,907 | TAIFEX Gamma model（逐履約價） |
| 原始 Put OI（選定到期日全部有效 Chain 合約） | 40,635 | options-gamma-levels（GEX 到期日） |
| 模型納入 Put OI（通過 GEX 計算條件） | 37,142 | TAIFEX Gamma model（逐履約價） |
| GEX 資料日期 | 2026-11-13 | TAIFEX Proxy (options-gamma-levels) |
- OI 對帳口徑：原始 OI 統計選定到期日全部有效 Chain 合約；模型納入 OI 僅統計通過結算價、IV 與 Gamma 計算條件並納入逐履約價 GEX 的合約。兩者差額不等於 Chain 缺漏。

**Gamma Flip 零交叉搜尋診斷**
- 搜尋標的區間：39,307.61～48,042.63
- 搜尋步長／計算次數：11.00／321
- 起點／終點 Net GEX：-1,930,241,705.68／995,777.66
- 搜尋區間最低／最高 Net GEX：-2,004,789,128.44／995,777.66
- 正負號交叉次數：1
- 解讀限制：此 Flip 僅代表目前 Call 正／Put 負假設下的模型零交叉；Aggregate OI 無法識別 Dealer 實際淨部位，不等同市場實際 Dealer Gamma Flip。

**GEX 到期日配對診斷（原始候選清單）**
```json
{"requested_date":"2026-11-13","chain_expiries":[{"contract_month":"202611F2","expiry":"2026-11-13"},{"contract_month":"202611","expiry":"2026-11-18"},{"contract_month":"202611F3","expiry":"2026-11-20"},{"contract_month":"202611W4","expiry":"2026-11-25"},{"contract_month":"202611F4","expiry":"2026-11-27"},{"contract_month":"202612","expiry":"2026-12-16"},{"contract_month":"202701","expiry":"2027-01-20"},{"contract_month":"202703","expiry":"2027-03-17"},{"contract_month":"202706","expiry":"2027-06-16"}],"delta_expiries":[{"contract_month":"202611","expiry":"2026-11-18"},{"contract_month":"202611F3","expiry":"2026-11-20"},{"contract_month":"202611W4","expiry":"2026-11-25"},{"contract_month":"202611F4","expiry":"2026-11-27"},{"contract_month":"202612","expiry":"2026-12-16"},{"contract_month":"202701","expiry":"2027-01-20"},{"contract_month":"202703","expiry":"2027-03-17"},{"contract_month":"202706","expiry":"2027-06-16"}],"common_expiries":[{"contract_month":"202611","expiry":"2026-11-18","delta_contract_month":"202611","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202611F3","expiry":"2026-11-20","delta_contract_month":"202611F3","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202611W4","expiry":"2026-11-25","delta_contract_month":"202611W4","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202611F4","expiry":"2026-11-27","delta_contract_month":"202611F4","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202612","expiry":"2026-12-16","delta_contract_month":"202612","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202701","expiry":"2027-01-20","delta_contract_month":"202701","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202703","expiry":"2027-03-17","delta_contract_month":"202703","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202706","expiry":"2027-06-16","delta_contract_month":"202706","match_type":"exact_contract_month_and_expiry"}],"same_day_common_expiries":[],"future_common_expiries":[{"contract_month":"202611","expiry":"2026-11-18","delta_contract_month":"202611","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202611F3","expiry":"2026-11-20","delta_contract_month":"202611F3","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202611W4","expiry":"2026-11-25","delta_contract_month":"202611W4","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202611F4","expiry":"2026-11-27","delta_contract_month":"202611F4","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202612","expiry":"2026-12-16","delta_contract_month":"202612","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202701","expiry":"2027-01-20","delta_contract_month":"202701","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202703","expiry":"2027-03-17","delta_contract_month":"202703","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202706","expiry":"2027-06-16","delta_contract_month":"202706","match_type":"exact_contract_month_and_expiry"}],"future_exact_common_expiries":[{"contract_month":"202611","expiry":"2026-11-18","delta_contract_month":"202611","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202611F3","expiry":"2026-11-20","delta_contract_month":"202611F3","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202611W4","expiry":"2026-11-25","delta_contract_month":"202611W4","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202611F4","expiry":"2026-11-27","delta_contract_month":"202611F4","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202612","expiry":"2026-12-16","delta_contract_month":"202612","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202701","expiry":"2027-01-20","delta_contract_month":"202701","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202703","expiry":"2027-03-17","delta_contract_month":"202703","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202706","expiry":"2027-06-16","delta_contract_month":"202706","match_type":"exact_contract_month_and_expiry"}],"future_date_fallback_common_expiries":[],"per_expiry_row_counts":[{"contract_month":"202611F2","expiry":"2026-11-13","chain_rows":496,"delta_rows":0},{"contract_month":"202611","expiry":"2026-11-18","chain_rows":616,"delta_rows":616},{"contract_month":"202611F3","expiry":"2026-11-20","chain_rows":404,"delta_rows":404},{"contract_month":"202611W4","expiry":"2026-11-25","chain_rows":292,"delta_rows":354},{"contract_month":"202611F4","expiry":"2026-11-27","chain_rows":230,"delta_rows":330},{"contract_month":"202612","expiry":"2026-12-16","chain_rows":562,"delta_rows":562},{"contract_month":"202701","expiry":"2027-01-20","chain_rows":410,"delta_rows":410},{"contract_month":"202703","expiry":"2027-03-17","chain_rows":284,"delta_rows":284},{"contract_month":"202706","expiry":"2027-06-16","chain_rows":284,"delta_rows":284}],"selected":{"contract_month":"202611","expiry":"2026-11-18","delta_contract_month":"202611","match_type":"exact_contract_month_and_expiry"},"selection_reason":"earliest_future_exact_common_expiry"}
```

**TAIFEX Delta 原始資料與 Parser 階段診斷**
```json
{"requested_date":"2026-11-13","source":"taifex_web","fallback_used":false,"attempts":[{"attempt":1,"source":"taifex_web","fallback":false,"http_status":200,"raw_rows":3249,"primary_error":null,"parser":{"input_rows":3249,"array_rows":3249,"object_rows":0,"short_rows":4,"non_txo_rows":1,"txo_rows":3244,"invalid_contract_month":0,"invalid_expiry":0,"unknown_option_type_rows":0,"invalid_strike_rows":0,"invalid_delta_rows":0,"parsed_rows":3244,"per_expiry":[{"contract_month":"202611","expiry":"2026-11-18","raw_txo_rows":616,"recognized_type_rows":616,"valid_strike_rows":616,"valid_delta_rows":616,"parsed_rows":616},{"contract_month":"202611F3","expiry":"2026-11-20","raw_txo_rows":404,"recognized_type_rows":404,"valid_strike_rows":404,"valid_delta_rows":404,"parsed_rows":404},{"contract_month":"202611W4","expiry":"2026-11-25","raw_txo_rows":354,"recognized_type_rows":354,"valid_strike_rows":354,"valid_delta_rows":354,"parsed_rows":354},{"contract_month":"202611F4","expiry":"2026-11-27","raw_txo_rows":330,"recognized_type_rows":330,"valid_strike_rows":330,"valid_delta_rows":330,"parsed_rows":330},{"contract_month":"202612","expiry":"2026-12-16","raw_txo_rows":562,"recognized_type_rows":562,"valid_strike_rows":562,"valid_delta_rows":562,"parsed_rows":562},{"contract_month":"202701","expiry":"2027-01-20","raw_txo_rows":410,"recognized_type_rows":410,"valid_strike_rows":410,"valid_delta_rows":410,"parsed_rows":410},{"contract_month":"202703","expiry":"2027-03-17","raw_txo_rows":284,"recognized_type_rows":284,"valid_strike_rows":284,"valid_delta_rows":284,"parsed_rows":284},{"contract_month":"202706","expiry":"2027-06-16","raw_txo_rows":284,"recognized_type_rows":284,"valid_strike_rows":284,"valid_delta_rows":284,"parsed_rows":284}]},"accepted_txo_rows":3244}],"parser":{"input_rows":3249,"array_rows":3249,"object_rows":0,"short_rows":4,"non_txo_rows":1,"txo_rows":3244,"invalid_contract_month":0,"invalid_expiry":0,"unknown_option_type_rows":0,"invalid_strike_rows":0,"invalid_delta_rows":0,"parsed_rows":3244,"per_expiry":[{"contract_month":"202611","expiry":"2026-11-18","raw_txo_rows":616,"recognized_type_rows":616,"valid_strike_rows":616,"valid_delta_rows":616,"parsed_rows":616},{"contract_month":"202611F3","expiry":"2026-11-20","raw_txo_rows":404,"recognized_type_rows":404,"valid_strike_rows":404,"valid_delta_rows":404,"parsed_rows":404},{"contract_month":"202611W4","expiry":"2026-11-25","raw_txo_rows":354,"recognized_type_rows":354,"valid_strike_rows":354,"valid_delta_rows":354,"parsed_rows":354},{"contract_month":"202611F4","expiry":"2026-11-27","raw_txo_rows":330,"recognized_type_rows":330,"valid_strike_rows":330,"valid_delta_rows":330,"parsed_rows":330},{"contract_month":"202612","expiry":"2026-12-16","raw_txo_rows":562,"recognized_type_rows":562,"valid_strike_rows":562,"valid_delta_rows":562,"parsed_rows":562},{"contract_month":"202701","expiry":"2027-01-20","raw_txo_rows":410,"recognized_type_rows":410,"valid_strike_rows":410,"valid_delta_rows":410,"parsed_rows":410},{"contract_month":"202703","expiry":"2027-03-17","raw_txo_rows":284,"recognized_type_rows":284,"valid_strike_rows":284,"valid_delta_rows":284,"parsed_rows":284},{"contract_month":"202706","expiry":"2027-06-16","raw_txo_rows":284,"recognized_type_rows":284,"valid_strike_rows":284,"valid_delta_rows":284,"parsed_rows":284}]},"final_rows":3244,"per_expiry_rows":[{"contract_month":"202611","expiry":"2026-11-18","raw_txo_rows":616,"recognized_type_rows":616,"valid_strike_rows":616,"valid_delta_rows":616,"parsed_rows":616},{"contract_month":"202611F3","expiry":"2026-11-20","raw_txo_rows":404,"recognized_type_rows":404,"valid_strike_rows":404,"valid_delta_rows":404,"parsed_rows":404},{"contract_month":"202611W4","expiry":"2026-11-25","raw_txo_rows":354,"recognized_type_rows":354,"valid_strike_rows":354,"valid_delta_rows":354,"parsed_rows":354},{"contract_month":"202611F4","expiry":"2026-11-27","raw_txo_rows":330,"recognized_type_rows":330,"valid_strike_rows":330,"valid_delta_rows":330,"parsed_rows":330},{"contract_month":"202612","expiry":"2026-12-16","raw_txo_rows":562,"recognized_type_rows":562,"valid_strike_rows":562,"valid_delta_rows":562,"parsed_rows":562},{"contract_month":"202701","expiry":"2027-01-20","raw_txo_rows":410,"recognized_type_rows":410,"valid_strike_rows":410,"valid_delta_rows":410,"parsed_rows":410},{"contract_month":"202703","expiry":"2027-03-17","raw_txo_rows":284,"recognized_type_rows":284,"valid_strike_rows":284,"valid_delta_rows":284,"parsed_rows":284},{"contract_month":"202706","expiry":"2027-06-16","raw_txo_rows":284,"recognized_type_rows":284,"valid_strike_rows":284,"valid_delta_rows":284,"parsed_rows":284}]}
```

**擴大區間 Gamma Flip 診斷（±15%；不覆蓋正式 ±10% 結果）**
- 搜尋標的區間：37,123.85～50,226.39
- 搜尋步長／計算次數：11.00／1192
- 起點／終點 Net GEX：-1,245,952,286.65／5,114,533,597.55
- 搜尋區間最低／最高 Net GEX：-2,004,789,588.95／8,593,046,533.08
- 正負號交叉次數：1
- 擴大區間診斷 Flip：42,826.92

### 14A．GEX 整體曝險與履約價分布

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Net GEX（標的變動 1%） | 1,412,258,607.07 NT$ | TAIFEX Gamma model；NT$／標的變動 1% |
| Gross GEX（標的變動 1%） | 8,942,949,081.36 NT$ | TAIFEX Gamma model；NT$／標的變動 1% |
| 模型品質 | usable | Black-Scholes Gamma using TAIFEX settlement-implied volatility |
| 部位正負號假設 | Call 正／Put 負為模型假設；Aggregate OI 不揭露 Dealer 實際淨部位，此值不可視為實際 Dealer GEX | 模型限制；非 TAIFEX 公布的 Dealer 部位 |
| 履約價資料筆數 | 306 | 資料日期：2026-11-13 |
| 正 Net GEX 最大履約價 | 43,600 | 依 Net GEX 排序 |
| 負 Net GEX 最低履約價 | 42,000 | 依 Net GEX 排序 |
- 正 Net GEX Top 5：43,600（354,740,569.28 NT$）、43,400（338,245,330.48 NT$）、43,200（315,930,327.56 NT$）、45,000（244,879,077.75 NT$）、43,800（229,859,477.17 NT$）
- 負 Net GEX Top 5：42,000（-246,319,452.05 NT$）、42,500（-179,133,274.21 NT$）、42,300（-118,924,227.34 NT$）、40,000（-100,670,098.50 NT$）、41,500（-95,181,757.34 NT$）

#### GEX_LEVELS_JSON（僅衍生後逐履約價 GEX，不含原始報價；GEX 單位 NT$／標的變動 1%）

```json
{"date":"2026-11-13","underlying":43675.12,"unit":"NTD per 1% underlying move","model":"Black-Scholes Gamma using TAIFEX settlement-implied volatility","quality":"usable","net_gex_1pct":1412258607.069811,"gross_gex_1pct":8942949081.363073,"gamma_diagnostics":{"chain_rows":616,"delta_rows":616,"matched_strike_keys":616,"positive_oi_settlement_eligible":490,"invalid_oi":126,"invalid_settlement":0,"below_intrinsic":53,"iv_failed":0,"iv_out_of_range":0,"gamma_failed":0,"modeled_contracts":437},"formal_flip_diagnostics":{"search_lower_underlying":39307.608,"search_upper_underlying":48042.632000000005,"step":11,"evaluations":321,"start_net_gex_1pct":-1930241705.6775908,"end_net_gex_1pct":995777.6619077618,"min_net_gex_1pct":-2004789128.4383447,"max_net_gex_1pct":995777.6619077618,"zero_crossings":1,"found":true},"wide_range_flip":{"lower_underlying":42821.852,"upper_underlying":42832.852,"estimated_underlying":42826.918880216974,"lower_net_gex_1pct":-7376499.212168876,"upper_net_gex_1pct":8637593.850871053},"wide_range_flip_diagnostics":{"search_lower_underlying":37123.852,"search_upper_underlying":50226.388,"reference_underlying":43675.12,"step":11,"evaluations":1192,"start_net_gex_1pct":-1245952286.6480184,"end_net_gex_1pct":5114533597.553315,"min_net_gex_1pct":-2004789588.9507823,"max_net_gex_1pct":8593046533.07948,"zero_crossings":1,"found":true,"selected_crossing_distance":848.2011197830288},"expiry_selection_diagnostics":{"requested_date":"2026-11-13","chain_expiries":[{"contract_month":"202611F2","expiry":"2026-11-13"},{"contract_month":"202611","expiry":"2026-11-18"},{"contract_month":"202611F3","expiry":"2026-11-20"},{"contract_month":"202611W4","expiry":"2026-11-25"},{"contract_month":"202611F4","expiry":"2026-11-27"},{"contract_month":"202612","expiry":"2026-12-16"},{"contract_month":"202701","expiry":"2027-01-20"},{"contract_month":"202703","expiry":"2027-03-17"},{"contract_month":"202706","expiry":"2027-06-16"}],"delta_expiries":[{"contract_month":"202611","expiry":"2026-11-18"},{"contract_month":"202611F3","expiry":"2026-11-20"},{"contract_month":"202611W4","expiry":"2026-11-25"},{"contract_month":"202611F4","expiry":"2026-11-27"},{"contract_month":"202612","expiry":"2026-12-16"},{"contract_month":"202701","expiry":"2027-01-20"},{"contract_month":"202703","expiry":"2027-03-17"},{"contract_month":"202706","expiry":"2027-06-16"}],"common_expiries":[{"contract_month":"202611","expiry":"2026-11-18","delta_contract_month":"202611","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202611F3","expiry":"2026-11-20","delta_contract_month":"202611F3","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202611W4","expiry":"2026-11-25","delta_contract_month":"202611W4","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202611F4","expiry":"2026-11-27","delta_contract_month":"202611F4","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202612","expiry":"2026-12-16","delta_contract_month":"202612","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202701","expiry":"2027-01-20","delta_contract_month":"202701","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202703","expiry":"2027-03-17","delta_contract_month":"202703","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202706","expiry":"2027-06-16","delta_contract_month":"202706","match_type":"exact_contract_month_and_expiry"}],"same_day_common_expiries":[],"future_common_expiries":[{"contract_month":"202611","expiry":"2026-11-18","delta_contract_month":"202611","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202611F3","expiry":"2026-11-20","delta_contract_month":"202611F3","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202611W4","expiry":"2026-11-25","delta_contract_month":"202611W4","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202611F4","expiry":"2026-11-27","delta_contract_month":"202611F4","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202612","expiry":"2026-12-16","delta_contract_month":"202612","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202701","expiry":"2027-01-20","delta_contract_month":"202701","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202703","expiry":"2027-03-17","delta_contract_month":"202703","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202706","expiry":"2027-06-16","delta_contract_month":"202706","match_type":"exact_contract_month_and_expiry"}],"future_exact_common_expiries":[{"contract_month":"202611","expiry":"2026-11-18","delta_contract_month":"202611","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202611F3","expiry":"2026-11-20","delta_contract_month":"202611F3","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202611W4","expiry":"2026-11-25","delta_contract_month":"202611W4","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202611F4","expiry":"2026-11-27","delta_contract_month":"202611F4","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202612","expiry":"2026-12-16","delta_contract_month":"202612","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202701","expiry":"2027-01-20","delta_contract_month":"202701","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202703","expiry":"2027-03-17","delta_contract_month":"202703","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202706","expiry":"2027-06-16","delta_contract_month":"202706","match_type":"exact_contract_month_and_expiry"}],"future_date_fallback_common_expiries":[],"per_expiry_row_counts":[{"contract_month":"202611F2","expiry":"2026-11-13","chain_rows":496,"delta_rows":0},{"contract_month":"202611","expiry":"2026-11-18","chain_rows":616,"delta_rows":616},{"contract_month":"202611F3","expiry":"2026-11-20","chain_rows":404,"delta_rows":404},{"contract_month":"202611W4","expiry":"2026-11-25","chain_rows":292,"delta_rows":354},{"contract_month":"202611F4","expiry":"2026-11-27","chain_rows":230,"delta_rows":330},{"contract_month":"202612","expiry":"2026-12-16","chain_rows":562,"delta_rows":562},{"contract_month":"202701","expiry":"2027-01-20","chain_rows":410,"delta_rows":410},{"contract_month":"202703","expiry":"2027-03-17","chain_rows":284,"delta_rows":284},{"contract_month":"202706","expiry":"2027-06-16","chain_rows":284,"delta_rows":284}],"selected":{"contract_month":"202611","expiry":"2026-11-18","delta_contract_month":"202611","match_type":"exact_contract_month_and_expiry"},"selection_reason":"earliest_future_exact_common_expiry"},"levels":[{"strike":33700.0,"call_gex_1pct":0.0,"put_gex_1pct":-4550756.53476221,"net_gex_1pct":-4550756.53476221,"gross_gex_1pct":4550756.53476221,"call_oi":0,"put_oi":1971},{"strike":33800.0,"call_gex_1pct":0.0,"put_gex_1pct":-101497.64872967722,"net_gex_1pct":-101497.64872967722,"gross_gex_1pct":101497.64872967722,"call_oi":0,"put_oi":39},{"strike":33900.0,"call_gex_1pct":0.0,"put_gex_1pct":-63681.800904603006,"net_gex_1pct":-63681.800904603006,"gross_gex_1pct":63681.800904603006,"call_oi":0,"put_oi":24},{"strike":34000.0,"call_gex_1pct":0.0,"put_gex_1pct":-169675.68511020593,"net_gex_1pct":-169675.68511020593,"gross_gex_1pct":169675.68511020593,"call_oi":0,"put_oi":62},{"strike":34100.0,"call_gex_1pct":0.0,"put_gex_1pct":-78150.4823399347,"net_gex_1pct":-78150.4823399347,"gross_gex_1pct":78150.4823399347,"call_oi":0,"put_oi":28},{"strike":34200.0,"call_gex_1pct":0.0,"put_gex_1pct":-54699.198560125966,"net_gex_1pct":-54699.198560125966,"gross_gex_1pct":54699.198560125966,"call_oi":0,"put_oi":19},{"strike":34300.0,"call_gex_1pct":0.0,"put_gex_1pct":-52094.354992210734,"net_gex_1pct":-52094.354992210734,"gross_gex_1pct":52094.354992210734,"call_oi":0,"put_oi":17},{"strike":34400.0,"call_gex_1pct":0.0,"put_gex_1pct":-121940.19440532174,"net_gex_1pct":-121940.19440532174,"gross_gex_1pct":121940.19440532174,"call_oi":0,"put_oi":39},{"strike":34500.0,"call_gex_1pct":0.0,"put_gex_1pct":-35808.90474147636,"net_gex_1pct":-35808.90474147636,"gross_gex_1pct":35808.90474147636,"call_oi":0,"put_oi":11},{"strike":34600.0,"call_gex_1pct":0.0,"put_gex_1pct":-10065.489538773218,"net_gex_1pct":-10065.489538773218,"gross_gex_1pct":10065.489538773218,"call_oi":0,"put_oi":3},{"strike":34700.0,"call_gex_1pct":0.0,"put_gex_1pct":-48412.096684060954,"net_gex_1pct":-48412.096684060954,"gross_gex_1pct":48412.096684060954,"call_oi":0,"put_oi":14},{"strike":34800.0,"call_gex_1pct":0.0,"put_gex_1pct":-110484.35353796778,"net_gex_1pct":-110484.35353796778,"gross_gex_1pct":110484.35353796778,"call_oi":0,"put_oi":31},{"strike":34900.0,"call_gex_1pct":0.0,"put_gex_1pct":-140857.76572638963,"net_gex_1pct":-140857.76572638963,"gross_gex_1pct":140857.76572638963,"call_oi":0,"put_oi":38},{"strike":35000.0,"call_gex_1pct":0.0,"put_gex_1pct":-859485.5033622704,"net_gex_1pct":-859485.5033622704,"gross_gex_1pct":859485.5033622704,"call_oi":0,"put_oi":225},{"strike":35100.0,"call_gex_1pct":0.0,"put_gex_1pct":-3936.677786685794,"net_gex_1pct":-3936.677786685794,"gross_gex_1pct":3936.677786685794,"call_oi":0,"put_oi":1},{"strike":35200.0,"call_gex_1pct":0.0,"put_gex_1pct":-147301.32158455133,"net_gex_1pct":-147301.32158455133,"gross_gex_1pct":147301.32158455133,"call_oi":0,"put_oi":36},{"strike":35300.0,"call_gex_1pct":0.0,"put_gex_1pct":-1602747.1957063964,"net_gex_1pct":-1602747.1957063964,"gross_gex_1pct":1602747.1957063964,"call_oi":0,"put_oi":377},{"strike":35400.0,"call_gex_1pct":0.0,"put_gex_1pct":-166468.33739471264,"net_gex_1pct":-166468.33739471264,"gross_gex_1pct":166468.33739471264,"call_oi":0,"put_oi":38},{"strike":35500.0,"call_gex_1pct":0.0,"put_gex_1pct":-311793.09606821736,"net_gex_1pct":-311793.09606821736,"gross_gex_1pct":311793.09606821736,"call_oi":0,"put_oi":68},{"strike":35600.0,"call_gex_1pct":0.0,"put_gex_1pct":-28346.396631125248,"net_gex_1pct":-28346.396631125248,"gross_gex_1pct":28346.396631125248,"call_oi":0,"put_oi":6},{"strike":35700.0,"call_gex_1pct":0.0,"put_gex_1pct":-170391.15714078132,"net_gex_1pct":-170391.15714078132,"gross_gex_1pct":170391.15714078132,"call_oi":0,"put_oi":35},{"strike":35800.0,"call_gex_1pct":0.0,"put_gex_1pct":-45810.67360046376,"net_gex_1pct":-45810.67360046376,"gross_gex_1pct":45810.67360046376,"call_oi":0,"put_oi":9},{"strike":35900.0,"call_gex_1pct":0.0,"put_gex_1pct":-137327.74347046707,"net_gex_1pct":-137327.74347046707,"gross_gex_1pct":137327.74347046707,"call_oi":0,"put_oi":26},{"strike":36000.0,"call_gex_1pct":0.0,"put_gex_1pct":-3886260.89847204,"net_gex_1pct":-3886260.89847204,"gross_gex_1pct":3886260.89847204,"call_oi":0,"put_oi":714},{"strike":36100.0,"call_gex_1pct":0.0,"put_gex_1pct":-189446.11486552533,"net_gex_1pct":-189446.11486552533,"gross_gex_1pct":189446.11486552533,"call_oi":0,"put_oi":34},{"strike":36200.0,"call_gex_1pct":0.0,"put_gex_1pct":-308095.40897806943,"net_gex_1pct":-308095.40897806943,"gross_gex_1pct":308095.40897806943,"call_oi":0,"put_oi":54},{"strike":36300.0,"call_gex_1pct":0.0,"put_gex_1pct":-300046.73540885694,"net_gex_1pct":-300046.73540885694,"gross_gex_1pct":300046.73540885694,"call_oi":0,"put_oi":51},{"strike":36400.0,"call_gex_1pct":0.0,"put_gex_1pct":-752881.0318505073,"net_gex_1pct":-752881.0318505073,"gross_gex_1pct":752881.0318505073,"call_oi":0,"put_oi":118},{"strike":36500.0,"call_gex_1pct":0.0,"put_gex_1pct":-5041013.012924542,"net_gex_1pct":-5041013.012924542,"gross_gex_1pct":5041013.012924542,"call_oi":0,"put_oi":749},{"strike":36600.0,"call_gex_1pct":0.0,"put_gex_1pct":-420785.2080313569,"net_gex_1pct":-420785.2080313569,"gross_gex_1pct":420785.2080313569,"call_oi":0,"put_oi":61},{"strike":36700.0,"call_gex_1pct":23835.081882679267,"put_gex_1pct":-388968.70067624684,"net_gex_1pct":-365133.6187935676,"gross_gex_1pct":412803.7825589261,"call_oi":1,"put_oi":55},{"strike":36800.0,"call_gex_1pct":48663.75109746422,"put_gex_1pct":-3564175.406963353,"net_gex_1pct":-3515511.655865889,"gross_gex_1pct":3612839.158060817,"call_oi":2,"put_oi":466},{"strike":36900.0,"call_gex_1pct":24844.486539177175,"put_gex_1pct":-627632.3733683865,"net_gex_1pct":-602787.8868292094,"gross_gex_1pct":652476.8599075637,"call_oi":1,"put_oi":80},{"strike":37000.0,"call_gex_1pct":25373.629843834948,"put_gex_1pct":-3276341.906876627,"net_gex_1pct":-3250968.277032792,"gross_gex_1pct":3301715.5367204617,"call_oi":1,"put_oi":407},{"strike":37100.0,"call_gex_1pct":25920.06294084911,"put_gex_1pct":-431800.7407135167,"net_gex_1pct":-405880.6777726676,"gross_gex_1pct":457720.8036543658,"call_oi":1,"put_oi":51},{"strike":37200.0,"call_gex_1pct":26484.58895296034,"put_gex_1pct":-978622.4349643898,"net_gex_1pct":-952137.8460114294,"gross_gex_1pct":1005107.0239173501,"call_oi":1,"put_oi":110},{"strike":37300.0,"call_gex_1pct":0.0,"put_gex_1pct":-1206059.8319738547,"net_gex_1pct":-1206059.8319738547,"gross_gex_1pct":1206059.8319738547,"call_oi":0,"put_oi":132},{"strike":37400.0,"call_gex_1pct":0.0,"put_gex_1pct":-1633317.1634418997,"net_gex_1pct":-1633317.1634418997,"gross_gex_1pct":1633317.1634418997,"call_oi":0,"put_oi":174},{"strike":37500.0,"call_gex_1pct":28295.514830667737,"put_gex_1pct":-1360875.3846650177,"net_gex_1pct":-1332579.86983435,"gross_gex_1pct":1389170.8994956855,"call_oi":1,"put_oi":138},{"strike":37600.0,"call_gex_1pct":0.0,"put_gex_1pct":-1231959.9759235627,"net_gex_1pct":-1231959.9759235627,"gross_gex_1pct":1231959.9759235627,"call_oi":0,"put_oi":119},{"strike":37700.0,"call_gex_1pct":177662.26849366815,"put_gex_1pct":-1151414.4924708428,"net_gex_1pct":-973752.2239771746,"gross_gex_1pct":1329076.760964511,"call_oi":6,"put_oi":104},{"strike":37800.0,"call_gex_1pct":0.0,"put_gex_1pct":-1480624.5130169014,"net_gex_1pct":-1480624.5130169014,"gross_gex_1pct":1480624.5130169014,"call_oi":0,"put_oi":130},{"strike":37900.0,"call_gex_1pct":0.0,"put_gex_1pct":-461649.3736594886,"net_gex_1pct":-461649.3736594886,"gross_gex_1pct":461649.3736594886,"call_oi":0,"put_oi":38},{"strike":38000.0,"call_gex_1pct":412966.08149877115,"put_gex_1pct":-18627684.404623955,"net_gex_1pct":-18214718.323125184,"gross_gex_1pct":19040650.486122727,"call_oi":13,"put_oi":1441},{"strike":38100.0,"call_gex_1pct":32539.640994148413,"put_gex_1pct":-3261611.937799755,"net_gex_1pct":-3229072.2968056067,"gross_gex_1pct":3294151.5787939033,"call_oi":1,"put_oi":245},{"strike":38200.0,"call_gex_1pct":66684.47520745241,"put_gex_1pct":-1866727.0775709748,"net_gex_1pct":-1800042.6023635224,"gross_gex_1pct":1933411.5527784273,"call_oi":2,"put_oi":134},{"strike":38300.0,"call_gex_1pct":34176.033158757375,"put_gex_1pct":-2332011.102385602,"net_gex_1pct":-2297835.0692268447,"gross_gex_1pct":2366187.135544359,"call_oi":1,"put_oi":160},{"strike":38400.0,"call_gex_1pct":0.0,"put_gex_1pct":-796569.7694152187,"net_gex_1pct":-796569.7694152187,"gross_gex_1pct":796569.7694152187,"call_oi":0,"put_oi":53},{"strike":38500.0,"call_gex_1pct":508394.1935610369,"put_gex_1pct":-5124112.831457787,"net_gex_1pct":-4615718.63789675,"gross_gex_1pct":5632507.025018824,"call_oi":14,"put_oi":317},{"strike":38550.0,"call_gex_1pct":0.0,"put_gex_1pct":-166346.53161378554,"net_gex_1pct":-166346.53161378554,"gross_gex_1pct":166346.53161378554,"call_oi":0,"put_oi":10},{"strike":38600.0,"call_gex_1pct":37254.38136273163,"put_gex_1pct":-2430069.9346799734,"net_gex_1pct":-2392815.553317242,"gross_gex_1pct":2467324.316042705,"call_oi":1,"put_oi":142},{"strike":38650.0,"call_gex_1pct":0.0,"put_gex_1pct":-765078.5232154243,"net_gex_1pct":-765078.5232154243,"gross_gex_1pct":765078.5232154243,"call_oi":0,"put_oi":44},{"strike":38700.0,"call_gex_1pct":305869.36634201655,"put_gex_1pct":-2678267.951362114,"net_gex_1pct":-2372398.5850200974,"gross_gex_1pct":2984137.3177041304,"call_oi":8,"put_oi":148},{"strike":38750.0,"call_gex_1pct":0.0,"put_gex_1pct":-606914.2311690552,"net_gex_1pct":-606914.2311690552,"gross_gex_1pct":606914.2311690552,"call_oi":0,"put_oi":33},{"strike":38800.0,"call_gex_1pct":274778.2946135556,"put_gex_1pct":-6060111.672806504,"net_gex_1pct":-5785333.378192948,"gross_gex_1pct":6334889.96742006,"call_oi":7,"put_oi":317},{"strike":38850.0,"call_gex_1pct":0.0,"put_gex_1pct":-213765.50515965448,"net_gex_1pct":-213765.50515965448,"gross_gex_1pct":213765.50515965448,"call_oi":0,"put_oi":11},{"strike":38900.0,"call_gex_1pct":403179.7960413757,"put_gex_1pct":-1617545.0957021161,"net_gex_1pct":-1214365.2996607404,"gross_gex_1pct":2020724.8917434919,"call_oi":10,"put_oi":81},{"strike":38950.0,"call_gex_1pct":0.0,"put_gex_1pct":-533443.7922007205,"net_gex_1pct":-533443.7922007205,"gross_gex_1pct":533443.7922007205,"call_oi":0,"put_oi":26},{"strike":39000.0,"call_gex_1pct":1988552.0285077803,"put_gex_1pct":-24279318.96525302,"net_gex_1pct":-22290766.93674524,"gross_gex_1pct":26267870.9937608,"call_oi":48,"put_oi":1152},{"strike":39050.0,"call_gex_1pct":0.0,"put_gex_1pct":-633754.0033501082,"net_gex_1pct":-633754.0033501082,"gross_gex_1pct":633754.0033501082,"call_oi":0,"put_oi":29},{"strike":39100.0,"call_gex_1pct":170350.0350039439,"put_gex_1pct":-1978394.6908416322,"net_gex_1pct":-1808044.6558376884,"gross_gex_1pct":2148744.7258455763,"call_oi":4,"put_oi":89},{"strike":39150.0,"call_gex_1pct":0.0,"put_gex_1pct":-184250.9054757242,"net_gex_1pct":-184250.9054757242,"gross_gex_1pct":184250.9054757242,"call_oi":0,"put_oi":8},{"strike":39200.0,"call_gex_1pct":350393.20201496856,"put_gex_1pct":-1323839.7445870799,"net_gex_1pct":-973446.5425721114,"gross_gex_1pct":1674232.9466020484,"call_oi":8,"put_oi":56},{"strike":39250.0,"call_gex_1pct":0.0,"put_gex_1pct":-266887.36069344013,"net_gex_1pct":-266887.36069344013,"gross_gex_1pct":266887.36069344013,"call_oi":0,"put_oi":11},{"strike":39300.0,"call_gex_1pct":45403.478493051436,"put_gex_1pct":-1405728.590450989,"net_gex_1pct":-1360325.1119579377,"gross_gex_1pct":1451132.0689440405,"call_oi":1,"put_oi":56},{"strike":39350.0,"call_gex_1pct":0.0,"put_gex_1pct":-1313459.7480380288,"net_gex_1pct":-1313459.7480380288,"gross_gex_1pct":1313459.7480380288,"call_oi":0,"put_oi":51},{"strike":39400.0,"call_gex_1pct":186915.5625200481,"put_gex_1pct":-2140145.605202769,"net_gex_1pct":-1953230.0426827208,"gross_gex_1pct":2327061.167722817,"call_oi":4,"put_oi":81},{"strike":39450.0,"call_gex_1pct":189659.6996487328,"put_gex_1pct":-354966.2595968323,"net_gex_1pct":-165306.55994809946,"gross_gex_1pct":544625.9592455651,"call_oi":4,"put_oi":13},{"strike":39500.0,"call_gex_1pct":962344.2144020593,"put_gex_1pct":-8799282.168931048,"net_gex_1pct":-7836937.954528989,"gross_gex_1pct":9761626.383333107,"call_oi":20,"put_oi":312},{"strike":39550.0,"call_gex_1pct":0.0,"put_gex_1pct":-1484898.9394413487,"net_gex_1pct":-1484898.9394413487,"gross_gex_1pct":1484898.9394413487,"call_oi":0,"put_oi":51},{"strike":39600.0,"call_gex_1pct":545300.5452516791,"put_gex_1pct":-2193251.72874491,"net_gex_1pct":-1647951.183493231,"gross_gex_1pct":2738552.2739965892,"call_oi":11,"put_oi":73},{"strike":39650.0,"call_gex_1pct":0.0,"put_gex_1pct":-708419.8070010511,"net_gex_1pct":-708419.8070010511,"gross_gex_1pct":708419.8070010511,"call_oi":0,"put_oi":23},{"strike":39700.0,"call_gex_1pct":1175307.5145286703,"put_gex_1pct":-2446054.9418154918,"net_gex_1pct":-1270747.4272868214,"gross_gex_1pct":3621362.456344162,"call_oi":23,"put_oi":77},{"strike":39750.0,"call_gex_1pct":51892.696734486104,"put_gex_1pct":-1074620.880772112,"net_gex_1pct":-1022728.1840376258,"gross_gex_1pct":1126513.577506598,"call_oi":1,"put_oi":33},{"strike":39800.0,"call_gex_1pct":1001395.8433053148,"put_gex_1pct":-16207201.622891894,"net_gex_1pct":-15205805.77958658,"gross_gex_1pct":17208597.466197208,"call_oi":19,"put_oi":475},{"strike":39850.0,"call_gex_1pct":0.0,"put_gex_1pct":-384597.85566772195,"net_gex_1pct":-384597.85566772195,"gross_gex_1pct":384597.85566772195,"call_oi":0,"put_oi":11},{"strike":39900.0,"call_gex_1pct":1312028.5268895014,"put_gex_1pct":-3224703.736107142,"net_gex_1pct":-1912675.2092176408,"gross_gex_1pct":4536732.262996644,"call_oi":24,"put_oi":90},{"strike":39950.0,"call_gex_1pct":0.0,"put_gex_1pct":-1266616.367769517,"net_gex_1pct":-1266616.367769517,"gross_gex_1pct":1266616.367769517,"call_oi":0,"put_oi":34},{"strike":40000.0,"call_gex_1pct":9763698.563613636,"put_gex_1pct":-110433797.05939986,"net_gex_1pct":-100670098.49578622,"gross_gex_1pct":120197495.6230135,"call_oi":173,"put_oi":2880},{"strike":40050.0,"call_gex_1pct":0.0,"put_gex_1pct":-1183869.8262637886,"net_gex_1pct":-1183869.8262637886,"gross_gex_1pct":1183869.8262637886,"call_oi":0,"put_oi":30},{"strike":40100.0,"call_gex_1pct":1107739.5973518146,"put_gex_1pct":-3410941.5134085547,"net_gex_1pct":-2303201.91605674,"gross_gex_1pct":4518681.110760369,"call_oi":19,"put_oi":84},{"strike":40150.0,"call_gex_1pct":59272.19403276028,"put_gex_1pct":-960910.7144281865,"net_gex_1pct":-901638.5203954263,"gross_gex_1pct":1020182.9084609468,"call_oi":1,"put_oi":23},{"strike":40200.0,"call_gex_1pct":1988872.2475487627,"put_gex_1pct":-2492870.6374646085,"net_gex_1pct":-503998.3899158458,"gross_gex_1pct":4481742.885013372,"call_oi":33,"put_oi":58},{"strike":40250.0,"call_gex_1pct":61293.12331280891,"put_gex_1pct":-1024398.5939935606,"net_gex_1pct":-963105.4706807517,"gross_gex_1pct":1085691.7173063694,"call_oi":1,"put_oi":23},{"strike":40300.0,"call_gex_1pct":8505917.767057793,"put_gex_1pct":-5358777.209045682,"net_gex_1pct":3147140.558012111,"gross_gex_1pct":13864694.976103475,"call_oi":136,"put_oi":117},{"strike":40350.0,"call_gex_1pct":1081537.754086188,"put_gex_1pct":-2187993.185231508,"net_gex_1pct":-1106455.4311453202,"gross_gex_1pct":3269530.9393176963,"call_oi":17,"put_oi":46},{"strike":40400.0,"call_gex_1pct":1941806.7513134924,"put_gex_1pct":-2689143.297961383,"net_gex_1pct":-747336.5466478907,"gross_gex_1pct":4630950.049274876,"call_oi":30,"put_oi":55},{"strike":40450.0,"call_gex_1pct":1251451.2458023478,"put_gex_1pct":-1112262.2071562945,"net_gex_1pct":139189.0386460533,"gross_gex_1pct":2363713.4529586425,"call_oi":19,"put_oi":22},{"strike":40500.0,"call_gex_1pct":2748562.039951459,"put_gex_1pct":-29929100.340679955,"net_gex_1pct":-27180538.300728496,"gross_gex_1pct":32677662.380631413,"call_oi":41,"put_oi":576},{"strike":40550.0,"call_gex_1pct":683654.5318868373,"put_gex_1pct":-1174895.4284350956,"net_gex_1pct":-491240.89654825826,"gross_gex_1pct":1858549.960321933,"call_oi":10,"put_oi":22},{"strike":40600.0,"call_gex_1pct":1461582.8599202335,"put_gex_1pct":-5683153.993207313,"net_gex_1pct":-4221571.13328708,"gross_gex_1pct":7144736.853127547,"call_oi":21,"put_oi":103},{"strike":40650.0,"call_gex_1pct":921311.089363361,"put_gex_1pct":-2690904.6571813696,"net_gex_1pct":-1769593.5678180086,"gross_gex_1pct":3612215.746544731,"call_oi":13,"put_oi":47},{"strike":40700.0,"call_gex_1pct":1587955.3301139537,"put_gex_1pct":-6112681.11807922,"net_gex_1pct":-4524725.787965266,"gross_gex_1pct":7700636.448193174,"call_oi":22,"put_oi":103},{"strike":40750.0,"call_gex_1pct":441180.1567838314,"put_gex_1pct":-1659409.323069702,"net_gex_1pct":-1218229.1662858706,"gross_gex_1pct":2100589.479853533,"call_oi":6,"put_oi":27},{"strike":40800.0,"call_gex_1pct":2023725.4844159507,"put_gex_1pct":-19072622.611816622,"net_gex_1pct":-17048897.12740067,"gross_gex_1pct":21096348.096232574,"call_oi":27,"put_oi":301},{"strike":40850.0,"call_gex_1pct":458259.67091650894,"put_gex_1pct":-3579634.336680248,"net_gex_1pct":-3121374.665763739,"gross_gex_1pct":4037894.007596757,"call_oi":6,"put_oi":55},{"strike":40900.0,"call_gex_1pct":1245535.702212306,"put_gex_1pct":-6685714.417049441,"net_gex_1pct":-5440178.714837135,"gross_gex_1pct":7931250.119261746,"call_oi":16,"put_oi":99},{"strike":40950.0,"call_gex_1pct":555541.2853104178,"put_gex_1pct":-2011559.87044803,"net_gex_1pct":-1456018.5851376122,"gross_gex_1pct":2567101.155758448,"call_oi":7,"put_oi":29},{"strike":41000.0,"call_gex_1pct":23209469.940528397,"put_gex_1pct":-101700840.4692406,"net_gex_1pct":-78491370.52871221,"gross_gex_1pct":124910310.409769,"call_oi":287,"put_oi":1423},{"strike":41050.0,"call_gex_1pct":989661.000950421,"put_gex_1pct":-1491752.9929325716,"net_gex_1pct":-502091.9919821506,"gross_gex_1pct":2481413.9938829923,"call_oi":12,"put_oi":20},{"strike":41100.0,"call_gex_1pct":1177794.2288910747,"put_gex_1pct":-28496318.052437536,"net_gex_1pct":-27318523.82354646,"gross_gex_1pct":29674112.28132861,"call_oi":14,"put_oi":372},{"strike":41150.0,"call_gex_1pct":514179.84901709395,"put_gex_1pct":-2292083.355813702,"net_gex_1pct":-1777903.5067966082,"gross_gex_1pct":2806263.204830796,"call_oi":6,"put_oi":29},{"strike":41200.0,"call_gex_1pct":4634783.099915401,"put_gex_1pct":-8004848.936234168,"net_gex_1pct":-3370065.8363187667,"gross_gex_1pct":12639632.036149569,"call_oi":53,"put_oi":98},{"strike":41250.0,"call_gex_1pct":1338930.0610641004,"put_gex_1pct":-3110510.5887066917,"net_gex_1pct":-1771580.5276425914,"gross_gex_1pct":4449440.649770793,"call_oi":15,"put_oi":37},{"strike":41300.0,"call_gex_1pct":1999894.482917118,"put_gex_1pct":-8646540.852406234,"net_gex_1pct":-6646646.369489116,"gross_gex_1pct":10646435.335323352,"call_oi":22,"put_oi":99},{"strike":41350.0,"call_gex_1pct":2042157.8765942568,"put_gex_1pct":-3783354.63267203,"net_gex_1pct":-1741196.7560777732,"gross_gex_1pct":5825512.509266287,"call_oi":22,"put_oi":42},{"strike":41400.0,"call_gex_1pct":1417626.1306670113,"put_gex_1pct":-15085375.609371318,"net_gex_1pct":-13667749.478704307,"gross_gex_1pct":16503001.740038328,"call_oi":15,"put_oi":163},{"strike":41450.0,"call_gex_1pct":1158547.767105825,"put_gex_1pct":-5057673.356121766,"net_gex_1pct":-3899125.589015941,"gross_gex_1pct":6216221.123227592,"call_oi":12,"put_oi":53},{"strike":41500.0,"call_gex_1pct":7202086.238482654,"put_gex_1pct":-102383843.58265853,"net_gex_1pct":-95181757.34417588,"gross_gex_1pct":109585929.82114118,"call_oi":73,"put_oi":1039},{"strike":41550.0,"call_gex_1pct":1707458.4754164952,"put_gex_1pct":-6898473.670025902,"net_gex_1pct":-5191015.194609406,"gross_gex_1pct":8605932.145442396,"call_oi":17,"put_oi":68},{"strike":41600.0,"call_gex_1pct":2772471.1692058956,"put_gex_1pct":-20742150.99359679,"net_gex_1pct":-17969679.824390892,"gross_gex_1pct":23514622.162802685,"call_oi":27,"put_oi":198},{"strike":41650.0,"call_gex_1pct":627132.812167661,"put_gex_1pct":-17904179.041339416,"net_gex_1pct":-17277046.229171757,"gross_gex_1pct":18531311.853507075,"call_oi":6,"put_oi":166},{"strike":41700.0,"call_gex_1pct":2352045.9501460963,"put_gex_1pct":-14226147.979998237,"net_gex_1pct":-11874102.02985214,"gross_gex_1pct":16578193.930144332,"call_oi":22,"put_oi":128},{"strike":41750.0,"call_gex_1pct":1849860.413649754,"put_gex_1pct":-4917302.023575973,"net_gex_1pct":-3067441.609926219,"gross_gex_1pct":6767162.437225726,"call_oi":17,"put_oi":43},{"strike":41800.0,"call_gex_1pct":4008989.927589946,"put_gex_1pct":-23774870.721798588,"net_gex_1pct":-19765880.794208642,"gross_gex_1pct":27783860.649388533,"call_oi":36,"put_oi":202},{"strike":41850.0,"call_gex_1pct":1133400.4558969936,"put_gex_1pct":-4239978.082809405,"net_gex_1pct":-3106577.626912412,"gross_gex_1pct":5373378.5387063995,"call_oi":10,"put_oi":35},{"strike":41900.0,"call_gex_1pct":3460078.4549417295,"put_gex_1pct":-12710519.687255645,"net_gex_1pct":-9250441.232313916,"gross_gex_1pct":16170598.142197374,"call_oi":30,"put_oi":102},{"strike":41950.0,"call_gex_1pct":2244294.9867089004,"put_gex_1pct":-5127161.306693091,"net_gex_1pct":-2882866.3199841906,"gross_gex_1pct":7371456.293401992,"call_oi":19,"put_oi":40},{"strike":42000.0,"call_gex_1pct":43634939.30135419,"put_gex_1pct":-289954391.3552414,"net_gex_1pct":-246319452.05388722,"gross_gex_1pct":333589330.6565956,"call_oi":363,"put_oi":2198},{"strike":42050.0,"call_gex_1pct":1223162.1249903147,"put_gex_1pct":-6635370.656205005,"net_gex_1pct":-5412208.53121469,"gross_gex_1pct":7858532.78119532,"call_oi":10,"put_oi":49},{"strike":42100.0,"call_gex_1pct":1991244.641682117,"put_gex_1pct":-16461582.934839536,"net_gex_1pct":-14470338.29315742,"gross_gex_1pct":18452827.576521654,"call_oi":16,"put_oi":118},{"strike":42150.0,"call_gex_1pct":1658654.4382225852,"put_gex_1pct":-3997343.197860488,"net_gex_1pct":-2338688.759637903,"gross_gex_1pct":5655997.636083074,"call_oi":13,"put_oi":28},{"strike":42200.0,"call_gex_1pct":4414480.594024236,"put_gex_1pct":-14825617.74253356,"net_gex_1pct":-10411137.148509324,"gross_gex_1pct":19240098.336557798,"call_oi":34,"put_oi":101},{"strike":42250.0,"call_gex_1pct":3303044.6141673448,"put_gex_1pct":-7522046.148421014,"net_gex_1pct":-4219001.534253669,"gross_gex_1pct":10825090.76258836,"call_oi":25,"put_oi":50},{"strike":42300.0,"call_gex_1pct":3092214.955996543,"put_gex_1pct":-122016442.291349,"net_gex_1pct":-118924227.33535245,"gross_gex_1pct":125108657.24734554,"call_oi":23,"put_oi":787},{"strike":42350.0,"call_gex_1pct":1793959.7420495334,"put_gex_1pct":-3809365.09540666,"net_gex_1pct":-2015405.3533571265,"gross_gex_1pct":5603324.837456193,"call_oi":13,"put_oi":24},{"strike":42400.0,"call_gex_1pct":7935294.992934665,"put_gex_1pct":-23327131.644657783,"net_gex_1pct":-15391836.651723118,"gross_gex_1pct":31262426.63759245,"call_oi":57,"put_oi":144},{"strike":42450.0,"call_gex_1pct":2125068.9533991297,"put_gex_1pct":-3498633.507763799,"net_gex_1pct":-1373564.5543646691,"gross_gex_1pct":5623702.4611629285,"call_oi":15,"put_oi":21},{"strike":42500.0,"call_gex_1pct":71223808.11556648,"put_gex_1pct":-250357082.3232295,"net_gex_1pct":-179133274.207663,"gross_gex_1pct":321580890.438796,"call_oi":494,"put_oi":1478},{"strike":42550.0,"call_gex_1pct":1760863.5496348173,"put_gex_1pct":-2602592.1754098423,"net_gex_1pct":-841728.625775025,"gross_gex_1pct":4363455.725044659,"call_oi":12,"put_oi":15},{"strike":42600.0,"call_gex_1pct":12695389.933391333,"put_gex_1pct":-25249763.841112573,"net_gex_1pct":-12554373.90772124,"gross_gex_1pct":37945153.7745039,"call_oi":85,"put_oi":141},{"strike":42650.0,"call_gex_1pct":2128535.4690476446,"put_gex_1pct":-4525936.659292324,"net_gex_1pct":-2397401.19024468,"gross_gex_1pct":6654472.128339969,"call_oi":14,"put_oi":25},{"strike":42700.0,"call_gex_1pct":4179189.1343088867,"put_gex_1pct":-24476471.149352543,"net_gex_1pct":-20297282.015043657,"gross_gex_1pct":28655660.28366143,"call_oi":27,"put_oi":132},{"strike":42750.0,"call_gex_1pct":3467229.6673785644,"put_gex_1pct":-5671070.562867044,"net_gex_1pct":-2203840.895488479,"gross_gex_1pct":9138300.230245609,"call_oi":22,"put_oi":30},{"strike":42800.0,"call_gex_1pct":7222158.161129273,"put_gex_1pct":-39941168.275256045,"net_gex_1pct":-32719010.11412677,"gross_gex_1pct":47163326.43638532,"call_oi":45,"put_oi":206},{"strike":42850.0,"call_gex_1pct":2778865.5028768186,"put_gex_1pct":-11125463.454195442,"net_gex_1pct":-8346597.9513186235,"gross_gex_1pct":13904328.95707226,"call_oi":17,"put_oi":56},{"strike":42900.0,"call_gex_1pct":8070002.324429795,"put_gex_1pct":-47113836.948683694,"net_gex_1pct":-39043834.6242539,"gross_gex_1pct":55183839.27311349,"call_oi":49,"put_oi":232},{"strike":42950.0,"call_gex_1pct":1509905.042238842,"put_gex_1pct":-12664685.659571087,"net_gex_1pct":-11154780.617332244,"gross_gex_1pct":14174590.70180993,"call_oi":9,"put_oi":62},{"strike":43000.0,"call_gex_1pct":383793624.849066,"put_gex_1pct":-354145655.7197638,"net_gex_1pct":29647969.129302204,"gross_gex_1pct":737939280.5688298,"call_oi":2322,"put_oi":1708},{"strike":43050.0,"call_gex_1pct":4426375.710227147,"put_gex_1pct":-15448678.077728074,"net_gex_1pct":-11022302.367500927,"gross_gex_1pct":19875053.78795522,"call_oi":26,"put_oi":73},{"strike":43100.0,"call_gex_1pct":6938467.343004158,"put_gex_1pct":-44630027.682629146,"net_gex_1pct":-37691560.339624986,"gross_gex_1pct":51568495.025633305,"call_oi":40,"put_oi":206},{"strike":43150.0,"call_gex_1pct":2504442.4241240015,"put_gex_1pct":-14649625.532813523,"net_gex_1pct":-12145183.10868952,"gross_gex_1pct":17154067.956937525,"call_oi":14,"put_oi":67},{"strike":43200.0,"call_gex_1pct":359724741.5679101,"put_gex_1pct":-43794414.01160288,"net_gex_1pct":315930327.5563072,"gross_gex_1pct":403519155.57951295,"call_oi":2044,"put_oi":195},{"strike":43250.0,"call_gex_1pct":3766920.94049157,"put_gex_1pct":-10670098.58582988,"net_gex_1pct":-6903177.64533831,"gross_gex_1pct":14437019.52632145,"call_oi":21,"put_oi":48},{"strike":43300.0,"call_gex_1pct":74441871.00826977,"put_gex_1pct":-27484215.723818272,"net_gex_1pct":46957655.2844515,"gross_gex_1pct":101926086.73208804,"call_oi":412,"put_oi":122},{"strike":43350.0,"call_gex_1pct":3112820.458921413,"put_gex_1pct":-10305643.218163446,"net_gex_1pct":-7192822.759242033,"gross_gex_1pct":13418463.67708486,"call_oi":17,"put_oi":45},{"strike":43400.0,"call_gex_1pct":374383051.6419458,"put_gex_1pct":-36137721.162614994,"net_gex_1pct":338245330.4793308,"gross_gex_1pct":410520772.8045608,"call_oi":2067,"put_oi":154},{"strike":43450.0,"call_gex_1pct":2043846.7799529792,"put_gex_1pct":-5595245.04595137,"net_gex_1pct":-3551398.265998391,"gross_gex_1pct":7639091.825904349,"call_oi":11,"put_oi":24},{"strike":43500.0,"call_gex_1pct":54700233.292560905,"put_gex_1pct":-123278925.2917315,"net_gex_1pct":-68578691.9991706,"gross_gex_1pct":177979158.5842924,"call_oi":285,"put_oi":520},{"strike":43550.0,"call_gex_1pct":8348623.098703817,"put_gex_1pct":-6459167.032462533,"net_gex_1pct":1889456.0662412848,"gross_gex_1pct":14807790.13116635,"call_oi":44,"put_oi":27},{"strike":43600.0,"call_gex_1pct":390426760.2798086,"put_gex_1pct":-35686190.99594668,"net_gex_1pct":354740569.2838619,"gross_gex_1pct":426112951.2757553,"call_oi":2094,"put_oi":149},{"strike":43650.0,"call_gex_1pct":11191240.875664541,"put_gex_1pct":-11419146.541466255,"net_gex_1pct":-227905.66580171324,"gross_gex_1pct":22610387.417130798,"call_oi":57,"put_oi":48},{"strike":43700.0,"call_gex_1pct":22608599.189999387,"put_gex_1pct":-62947363.64525453,"net_gex_1pct":-40338764.45525514,"gross_gex_1pct":85555962.83525392,"call_oi":118,"put_oi":256},{"strike":43750.0,"call_gex_1pct":12084482.522875026,"put_gex_1pct":-10658754.33041103,"net_gex_1pct":1425728.192463996,"gross_gex_1pct":22743236.853286058,"call_oi":63,"put_oi":44},{"strike":43800.0,"call_gex_1pct":303793991.1894601,"put_gex_1pct":-73934514.02115396,"net_gex_1pct":229859477.16830614,"gross_gex_1pct":377728505.2106141,"call_oi":1552,"put_oi":300},{"strike":43850.0,"call_gex_1pct":34632104.51024019,"put_gex_1pct":-36268564.63595446,"net_gex_1pct":-1636460.1257142723,"gross_gex_1pct":70900669.14619465,"call_oi":179,"put_oi":147},{"strike":43900.0,"call_gex_1pct":38986278.806555755,"put_gex_1pct":-56957369.49756329,"net_gex_1pct":-17971090.691007532,"gross_gex_1pct":95943648.30411905,"call_oi":200,"put_oi":225},{"strike":43950.0,"call_gex_1pct":16002041.738542657,"put_gex_1pct":-23182144.116522275,"net_gex_1pct":-7180102.377979618,"gross_gex_1pct":39184185.85506493,"call_oi":82,"put_oi":93},{"strike":44000.0,"call_gex_1pct":537702431.3322514,"put_gex_1pct":-489788854.76906127,"net_gex_1pct":47913576.56319016,"gross_gex_1pct":1027491286.1013126,"call_oi":2770,"put_oi":1963},{"strike":44050.0,"call_gex_1pct":12906927.734967675,"put_gex_1pct":-14350998.954140475,"net_gex_1pct":-1444071.2191728,"gross_gex_1pct":27257926.68910815,"call_oi":66,"put_oi":57},{"strike":44100.0,"call_gex_1pct":216906818.20622036,"put_gex_1pct":-36933766.66256394,"net_gex_1pct":179973051.5436564,"gross_gex_1pct":253840584.8687843,"call_oi":1101,"put_oi":149},{"strike":44150.0,"call_gex_1pct":15478349.077073924,"put_gex_1pct":-5500138.173740839,"net_gex_1pct":9978210.903333087,"gross_gex_1pct":20978487.250814762,"call_oi":79,"put_oi":22},{"strike":44200.0,"call_gex_1pct":45586291.85501262,"put_gex_1pct":-27284655.364167303,"net_gex_1pct":18301636.490845315,"gross_gex_1pct":72870947.21917993,"call_oi":231,"put_oi":110},{"strike":44250.0,"call_gex_1pct":12835861.215333715,"put_gex_1pct":-10998934.448641643,"net_gex_1pct":1836926.7666920722,"gross_gex_1pct":23834795.663975358,"call_oi":65,"put_oi":44},{"strike":44300.0,"call_gex_1pct":56924633.880226165,"put_gex_1pct":-36879763.838039406,"net_gex_1pct":20044870.04218676,"gross_gex_1pct":93804397.71826556,"call_oi":294,"put_oi":150},{"strike":44350.0,"call_gex_1pct":10034439.685015867,"put_gex_1pct":-4963932.909238185,"net_gex_1pct":5070506.775777682,"gross_gex_1pct":14998372.59425405,"call_oi":52,"put_oi":21},{"strike":44400.0,"call_gex_1pct":30450982.372464284,"put_gex_1pct":-38938256.30519936,"net_gex_1pct":-8487273.932735078,"gross_gex_1pct":69389238.67766365,"call_oi":157,"put_oi":165},{"strike":44450.0,"call_gex_1pct":13600343.95051841,"put_gex_1pct":-4267400.655434829,"net_gex_1pct":9332943.295083582,"gross_gex_1pct":17867744.60595324,"call_oi":71,"put_oi":18},{"strike":44500.0,"call_gex_1pct":99537867.59264429,"put_gex_1pct":-57339709.911244966,"net_gex_1pct":42198157.68139932,"gross_gex_1pct":156877577.50388926,"call_oi":535,"put_oi":248},{"strike":44550.0,"call_gex_1pct":6895670.243189918,"put_gex_1pct":-1157813.9230196695,"net_gex_1pct":5737856.320170248,"gross_gex_1pct":8053484.166209588,"call_oi":37,"put_oi":5},{"strike":44600.0,"call_gex_1pct":25148455.69978376,"put_gex_1pct":-63937087.10022009,"net_gex_1pct":-38788631.40043633,"gross_gex_1pct":89085542.80000386,"call_oi":134,"put_oi":280},{"strike":44650.0,"call_gex_1pct":7118228.917623983,"put_gex_1pct":-1797572.8471080693,"net_gex_1pct":5320656.070515914,"gross_gex_1pct":8915801.764732052,"call_oi":38,"put_oi":8},{"strike":44700.0,"call_gex_1pct":18960563.8148806,"put_gex_1pct":-28711969.812709123,"net_gex_1pct":-9751405.997828525,"gross_gex_1pct":47672533.62758972,"call_oi":104,"put_oi":129},{"strike":44750.0,"call_gex_1pct":5154235.540506699,"put_gex_1pct":-4061216.7890289654,"net_gex_1pct":1093018.7514777337,"gross_gex_1pct":9215452.329535665,"call_oi":29,"put_oi":19},{"strike":44800.0,"call_gex_1pct":26692011.69655794,"put_gex_1pct":-23185972.045510106,"net_gex_1pct":3506039.6510478333,"gross_gex_1pct":49877983.742068045,"call_oi":151,"put_oi":112},{"strike":44850.0,"call_gex_1pct":8930725.490019225,"put_gex_1pct":-201062.97390406133,"net_gex_1pct":8729662.516115163,"gross_gex_1pct":9131788.463923287,"call_oi":51,"put_oi":1},{"strike":44900.0,"call_gex_1pct":22099642.435264394,"put_gex_1pct":-47037873.2715722,"net_gex_1pct":-24938230.83630781,"gross_gex_1pct":69137515.7068366,"call_oi":128,"put_oi":243},{"strike":44950.0,"call_gex_1pct":3732347.250239287,"put_gex_1pct":0.0,"net_gex_1pct":3732347.250239287,"gross_gex_1pct":3732347.250239287,"call_oi":22,"put_oi":0},{"strike":45000.0,"call_gex_1pct":379852097.58738893,"put_gex_1pct":-134973019.83759016,"net_gex_1pct":244879077.74979877,"gross_gex_1pct":514825117.4249791,"call_oi":2276,"put_oi":758},{"strike":45050.0,"call_gex_1pct":10216256.476865567,"put_gex_1pct":0.0,"net_gex_1pct":10216256.476865567,"gross_gex_1pct":10216256.476865567,"call_oi":62,"put_oi":0},{"strike":45100.0,"call_gex_1pct":25787269.822451204,"put_gex_1pct":-31333730.295372464,"net_gex_1pct":-5546460.47292126,"gross_gex_1pct":57121000.11782367,"call_oi":161,"put_oi":200},{"strike":45150.0,"call_gex_1pct":8584958.234750355,"put_gex_1pct":0.0,"net_gex_1pct":8584958.234750355,"gross_gex_1pct":8584958.234750355,"call_oi":55,"put_oi":0},{"strike":45200.0,"call_gex_1pct":41101913.52734595,"put_gex_1pct":-13511031.786043746,"net_gex_1pct":27590881.7413022,"gross_gex_1pct":54612945.313389696,"call_oi":268,"put_oi":113},{"strike":45250.0,"call_gex_1pct":5998632.45073186,"put_gex_1pct":0.0,"net_gex_1pct":5998632.45073186,"gross_gex_1pct":5998632.45073186,"call_oi":40,"put_oi":0},{"strike":45300.0,"call_gex_1pct":26311142.531503655,"put_gex_1pct":-12258090.09794339,"net_gex_1pct":14053052.433560265,"gross_gex_1pct":38569232.62944704,"call_oi":180,"put_oi":133},{"strike":45350.0,"call_gex_1pct":7567862.320141298,"put_gex_1pct":0.0,"net_gex_1pct":7567862.320141298,"gross_gex_1pct":7567862.320141298,"call_oi":53,"put_oi":0},{"strike":45400.0,"call_gex_1pct":13483860.876325577,"put_gex_1pct":0.0,"net_gex_1pct":13483860.876325577,"gross_gex_1pct":13483860.876325577,"call_oi":97,"put_oi":0},{"strike":45450.0,"call_gex_1pct":2570235.4618963287,"put_gex_1pct":0.0,"net_gex_1pct":2570235.4618963287,"gross_gex_1pct":2570235.4618963287,"call_oi":19,"put_oi":0},{"strike":45500.0,"call_gex_1pct":62558264.07652132,"put_gex_1pct":0.0,"net_gex_1pct":62558264.07652132,"gross_gex_1pct":62558264.07652132,"call_oi":476,"put_oi":0},{"strike":45550.0,"call_gex_1pct":2550256.245984607,"put_gex_1pct":0.0,"net_gex_1pct":2550256.245984607,"gross_gex_1pct":2550256.245984607,"call_oi":20,"put_oi":0},{"strike":45600.0,"call_gex_1pct":45662712.34468477,"put_gex_1pct":0.0,"net_gex_1pct":45662712.34468477,"gross_gex_1pct":45662712.34468477,"call_oi":370,"put_oi":0},{"strike":45700.0,"call_gex_1pct":29987923.307763886,"put_gex_1pct":0.0,"net_gex_1pct":29987923.307763886,"gross_gex_1pct":29987923.307763886,"call_oi":258,"put_oi":0},{"strike":45800.0,"call_gex_1pct":34324105.33262933,"put_gex_1pct":0.0,"net_gex_1pct":34324105.33262933,"gross_gex_1pct":34324105.33262933,"call_oi":320,"put_oi":0},{"strike":45900.0,"call_gex_1pct":33755093.42465078,"put_gex_1pct":0.0,"net_gex_1pct":33755093.42465078,"gross_gex_1pct":33755093.42465078,"call_oi":334,"put_oi":0},{"strike":46000.0,"call_gex_1pct":165220004.55359867,"put_gex_1pct":0.0,"net_gex_1pct":165220004.55359867,"gross_gex_1pct":165220004.55359867,"call_oi":1791,"put_oi":0},{"strike":46100.0,"call_gex_1pct":52910648.70857656,"put_gex_1pct":0.0,"net_gex_1pct":52910648.70857656,"gross_gex_1pct":52910648.70857656,"call_oi":630,"put_oi":0},{"strike":46200.0,"call_gex_1pct":22832487.14892742,"put_gex_1pct":0.0,"net_gex_1pct":22832487.14892742,"gross_gex_1pct":22832487.14892742,"call_oi":293,"put_oi":0},{"strike":46300.0,"call_gex_1pct":32626353.928657364,"put_gex_1pct":0.0,"net_gex_1pct":32626353.928657364,"gross_gex_1pct":32626353.928657364,"call_oi":461,"put_oi":0},{"strike":46400.0,"call_gex_1pct":27881668.37587306,"put_gex_1pct":0.0,"net_gex_1pct":27881668.37587306,"gross_gex_1pct":27881668.37587306,"call_oi":434,"put_oi":0},{"strike":46500.0,"call_gex_1pct":54235233.52938141,"put_gex_1pct":0.0,"net_gex_1pct":54235233.52938141,"gross_gex_1pct":54235233.52938141,"call_oi":926,"put_oi":0},{"strike":46600.0,"call_gex_1pct":13135112.584502313,"put_gex_1pct":0.0,"net_gex_1pct":13135112.584502313,"gross_gex_1pct":13135112.584502313,"call_oi":245,"put_oi":0},{"strike":46700.0,"call_gex_1pct":12029409.521611871,"put_gex_1pct":0.0,"net_gex_1pct":12029409.521611871,"gross_gex_1pct":12029409.521611871,"call_oi":251,"put_oi":0},{"strike":46800.0,"call_gex_1pct":16229282.345510595,"put_gex_1pct":0.0,"net_gex_1pct":16229282.345510595,"gross_gex_1pct":16229282.345510595,"call_oi":386,"put_oi":0},{"strike":46900.0,"call_gex_1pct":15934527.64595753,"put_gex_1pct":0.0,"net_gex_1pct":15934527.64595753,"gross_gex_1pct":15934527.64595753,"call_oi":415,"put_oi":0},{"strike":47000.0,"call_gex_1pct":49330380.09541542,"put_gex_1pct":0.0,"net_gex_1pct":49330380.09541542,"gross_gex_1pct":49330380.09541542,"call_oi":1340,"put_oi":0},{"strike":47100.0,"call_gex_1pct":12990901.118870353,"put_gex_1pct":0.0,"net_gex_1pct":12990901.118870353,"gross_gex_1pct":12990901.118870353,"call_oi":383,"put_oi":0},{"strike":47200.0,"call_gex_1pct":9360073.28750203,"put_gex_1pct":0.0,"net_gex_1pct":9360073.28750203,"gross_gex_1pct":9360073.28750203,"call_oi":317,"put_oi":0},{"strike":47300.0,"call_gex_1pct":16400809.58199343,"put_gex_1pct":0.0,"net_gex_1pct":16400809.58199343,"gross_gex_1pct":16400809.58199343,"call_oi":589,"put_oi":0},{"strike":47400.0,"call_gex_1pct":2442475.733359915,"put_gex_1pct":0.0,"net_gex_1pct":2442475.733359915,"gross_gex_1pct":2442475.733359915,"call_oi":102,"put_oi":0},{"strike":47500.0,"call_gex_1pct":169677113.5207593,"put_gex_1pct":0.0,"net_gex_1pct":169677113.5207593,"gross_gex_1pct":169677113.5207593,"call_oi":7867,"put_oi":0},{"strike":47600.0,"call_gex_1pct":2713270.4955561715,"put_gex_1pct":0.0,"net_gex_1pct":2713270.4955561715,"gross_gex_1pct":2713270.4955561715,"call_oi":133,"put_oi":0},{"strike":47700.0,"call_gex_1pct":3512537.525666697,"put_gex_1pct":0.0,"net_gex_1pct":3512537.525666697,"gross_gex_1pct":3512537.525666697,"call_oi":191,"put_oi":0},{"strike":47800.0,"call_gex_1pct":7404765.823736268,"put_gex_1pct":0.0,"net_gex_1pct":7404765.823736268,"gross_gex_1pct":7404765.823736268,"call_oi":430,"put_oi":0},{"strike":47900.0,"call_gex_1pct":6922988.320745271,"put_gex_1pct":0.0,"net_gex_1pct":6922988.320745271,"gross_gex_1pct":6922988.320745271,"call_oi":441,"put_oi":0},{"strike":48000.0,"call_gex_1pct":64493334.789494954,"put_gex_1pct":0.0,"net_gex_1pct":64493334.789494954,"gross_gex_1pct":64493334.789494954,"call_oi":4451,"put_oi":0},{"strike":48100.0,"call_gex_1pct":2567720.5144324717,"put_gex_1pct":0.0,"net_gex_1pct":2567720.5144324717,"gross_gex_1pct":2567720.5144324717,"call_oi":197,"put_oi":0},{"strike":48200.0,"call_gex_1pct":2551583.082118927,"put_gex_1pct":0.0,"net_gex_1pct":2551583.082118927,"gross_gex_1pct":2551583.082118927,"call_oi":207,"put_oi":0},{"strike":48300.0,"call_gex_1pct":2335095.63907412,"put_gex_1pct":0.0,"net_gex_1pct":2335095.63907412,"gross_gex_1pct":2335095.63907412,"call_oi":198,"put_oi":0},{"strike":48400.0,"call_gex_1pct":1695435.9581778685,"put_gex_1pct":0.0,"net_gex_1pct":1695435.9581778685,"gross_gex_1pct":1695435.9581778685,"call_oi":154,"put_oi":0},{"strike":48500.0,"call_gex_1pct":59555587.87831944,"put_gex_1pct":0.0,"net_gex_1pct":59555587.87831944,"gross_gex_1pct":59555587.87831944,"call_oi":5975,"put_oi":0},{"strike":48600.0,"call_gex_1pct":1285805.60509333,"put_gex_1pct":0.0,"net_gex_1pct":1285805.60509333,"gross_gex_1pct":1285805.60509333,"call_oi":135,"put_oi":0},{"strike":48700.0,"call_gex_1pct":858597.5546369726,"put_gex_1pct":0.0,"net_gex_1pct":858597.5546369726,"gross_gex_1pct":858597.5546369726,"call_oi":99,"put_oi":0},{"strike":48800.0,"call_gex_1pct":852489.9312542279,"put_gex_1pct":0.0,"net_gex_1pct":852489.9312542279,"gross_gex_1pct":852489.9312542279,"call_oi":103,"put_oi":0},{"strike":48900.0,"call_gex_1pct":327218.74570788984,"put_gex_1pct":0.0,"net_gex_1pct":327218.74570788984,"gross_gex_1pct":327218.74570788984,"call_oi":43,"put_oi":0},{"strike":49000.0,"call_gex_1pct":8214386.661015249,"put_gex_1pct":0.0,"net_gex_1pct":8214386.661015249,"gross_gex_1pct":8214386.661015249,"call_oi":1156,"put_oi":0},{"strike":49100.0,"call_gex_1pct":278170.68359144876,"put_gex_1pct":0.0,"net_gex_1pct":278170.68359144876,"gross_gex_1pct":278170.68359144876,"call_oi":43,"put_oi":0},{"strike":49200.0,"call_gex_1pct":540747.5699539664,"put_gex_1pct":0.0,"net_gex_1pct":540747.5699539664,"gross_gex_1pct":540747.5699539664,"call_oi":88,"put_oi":0},{"strike":49300.0,"call_gex_1pct":448132.8656430895,"put_gex_1pct":0.0,"net_gex_1pct":448132.8656430895,"gross_gex_1pct":448132.8656430895,"call_oi":81,"put_oi":0},{"strike":49400.0,"call_gex_1pct":388989.3925964039,"put_gex_1pct":0.0,"net_gex_1pct":388989.3925964039,"gross_gex_1pct":388989.3925964039,"call_oi":79,"put_oi":0},{"strike":49500.0,"call_gex_1pct":1607783.5571985203,"put_gex_1pct":0.0,"net_gex_1pct":1607783.5571985203,"gross_gex_1pct":1607783.5571985203,"call_oi":359,"put_oi":0},{"strike":49600.0,"call_gex_1pct":487580.239231599,"put_gex_1pct":0.0,"net_gex_1pct":487580.239231599,"gross_gex_1pct":487580.239231599,"call_oi":116,"put_oi":0},{"strike":49700.0,"call_gex_1pct":287386.638778392,"put_gex_1pct":0.0,"net_gex_1pct":287386.638778392,"gross_gex_1pct":287386.638778392,"call_oi":73,"put_oi":0},{"strike":49800.0,"call_gex_1pct":312658.85626404424,"put_gex_1pct":0.0,"net_gex_1pct":312658.85626404424,"gross_gex_1pct":312658.85626404424,"call_oi":85,"put_oi":0},{"strike":49900.0,"call_gex_1pct":1501097.0578355438,"put_gex_1pct":0.0,"net_gex_1pct":1501097.0578355438,"gross_gex_1pct":1501097.0578355438,"call_oi":438,"put_oi":0},{"strike":50000.0,"call_gex_1pct":9818419.101154033,"put_gex_1pct":0.0,"net_gex_1pct":9818419.101154033,"gross_gex_1pct":9818419.101154033,"call_oi":2936,"put_oi":0},{"strike":50100.0,"call_gex_1pct":431811.65398229344,"put_gex_1pct":0.0,"net_gex_1pct":431811.65398229344,"gross_gex_1pct":431811.65398229344,"call_oi":139,"put_oi":0},{"strike":50200.0,"call_gex_1pct":635259.370039071,"put_gex_1pct":0.0,"net_gex_1pct":635259.370039071,"gross_gex_1pct":635259.370039071,"call_oi":221,"put_oi":0},{"strike":50300.0,"call_gex_1pct":154431.9023888143,"put_gex_1pct":0.0,"net_gex_1pct":154431.9023888143,"gross_gex_1pct":154431.9023888143,"call_oi":55,"put_oi":0},{"strike":50400.0,"call_gex_1pct":186239.3028778045,"put_gex_1pct":0.0,"net_gex_1pct":186239.3028778045,"gross_gex_1pct":186239.3028778045,"call_oi":72,"put_oi":0},{"strike":50500.0,"call_gex_1pct":751056.965663037,"put_gex_1pct":0.0,"net_gex_1pct":751056.965663037,"gross_gex_1pct":751056.965663037,"call_oi":317,"put_oi":0},{"strike":50600.0,"call_gex_1pct":134362.11207596093,"put_gex_1pct":0.0,"net_gex_1pct":134362.11207596093,"gross_gex_1pct":134362.11207596093,"call_oi":58,"put_oi":0},{"strike":50700.0,"call_gex_1pct":29506.21613578788,"put_gex_1pct":0.0,"net_gex_1pct":29506.21613578788,"gross_gex_1pct":29506.21613578788,"call_oi":14,"put_oi":0},{"strike":50800.0,"call_gex_1pct":94851.46839351754,"put_gex_1pct":0.0,"net_gex_1pct":94851.46839351754,"gross_gex_1pct":94851.46839351754,"call_oi":46,"put_oi":0},{"strike":50900.0,"call_gex_1pct":833249.4446916534,"put_gex_1pct":0.0,"net_gex_1pct":833249.4446916534,"gross_gex_1pct":833249.4446916534,"call_oi":448,"put_oi":0},{"strike":51000.0,"call_gex_1pct":1114290.2077638214,"put_gex_1pct":0.0,"net_gex_1pct":1114290.2077638214,"gross_gex_1pct":1114290.2077638214,"call_oi":612,"put_oi":0},{"strike":51100.0,"call_gex_1pct":77960.02926534049,"put_gex_1pct":0.0,"net_gex_1pct":77960.02926534049,"gross_gex_1pct":77960.02926534049,"call_oi":48,"put_oi":0},{"strike":51200.0,"call_gex_1pct":81130.53678376347,"put_gex_1pct":0.0,"net_gex_1pct":81130.53678376347,"gross_gex_1pct":81130.53678376347,"call_oi":51,"put_oi":0},{"strike":51300.0,"call_gex_1pct":34288.34635661003,"put_gex_1pct":0.0,"net_gex_1pct":34288.34635661003,"gross_gex_1pct":34288.34635661003,"call_oi":22,"put_oi":0},{"strike":51400.0,"call_gex_1pct":43844.13699030267,"put_gex_1pct":0.0,"net_gex_1pct":43844.13699030267,"gross_gex_1pct":43844.13699030267,"call_oi":32,"put_oi":0},{"strike":51500.0,"call_gex_1pct":193395.45494540752,"put_gex_1pct":0.0,"net_gex_1pct":193395.45494540752,"gross_gex_1pct":193395.45494540752,"call_oi":144,"put_oi":0},{"strike":51600.0,"call_gex_1pct":132997.85536698106,"put_gex_1pct":0.0,"net_gex_1pct":132997.85536698106,"gross_gex_1pct":132997.85536698106,"call_oi":101,"put_oi":0},{"strike":51700.0,"call_gex_1pct":63515.669196074945,"put_gex_1pct":0.0,"net_gex_1pct":63515.669196074945,"gross_gex_1pct":63515.669196074945,"call_oi":56,"put_oi":0},{"strike":51800.0,"call_gex_1pct":91230.2885817208,"put_gex_1pct":0.0,"net_gex_1pct":91230.2885817208,"gross_gex_1pct":91230.2885817208,"call_oi":82,"put_oi":0},{"strike":51900.0,"call_gex_1pct":45847.5472154524,"put_gex_1pct":0.0,"net_gex_1pct":45847.5472154524,"gross_gex_1pct":45847.5472154524,"call_oi":42,"put_oi":0},{"strike":52000.0,"call_gex_1pct":700636.5988761936,"put_gex_1pct":0.0,"net_gex_1pct":700636.5988761936,"gross_gex_1pct":700636.5988761936,"call_oi":654,"put_oi":0},{"strike":52100.0,"call_gex_1pct":38910.708697161295,"put_gex_1pct":0.0,"net_gex_1pct":38910.708697161295,"gross_gex_1pct":38910.708697161295,"call_oi":37,"put_oi":0},{"strike":52200.0,"call_gex_1pct":50992.09195819606,"put_gex_1pct":0.0,"net_gex_1pct":50992.09195819606,"gross_gex_1pct":50992.09195819606,"call_oi":58,"put_oi":0},{"strike":52300.0,"call_gex_1pct":37124.49689572948,"put_gex_1pct":0.0,"net_gex_1pct":37124.49689572948,"gross_gex_1pct":37124.49689572948,"call_oi":43,"put_oi":0},{"strike":52400.0,"call_gex_1pct":21200.538555932497,"put_gex_1pct":0.0,"net_gex_1pct":21200.538555932497,"gross_gex_1pct":21200.538555932497,"call_oi":25,"put_oi":0},{"strike":52500.0,"call_gex_1pct":93311.44711051688,"put_gex_1pct":0.0,"net_gex_1pct":93311.44711051688,"gross_gex_1pct":93311.44711051688,"call_oi":112,"put_oi":0},{"strike":52600.0,"call_gex_1pct":39297.168685977005,"put_gex_1pct":0.0,"net_gex_1pct":39297.168685977005,"gross_gex_1pct":39297.168685977005,"call_oi":48,"put_oi":0},{"strike":52700.0,"call_gex_1pct":28163.21406890508,"put_gex_1pct":0.0,"net_gex_1pct":28163.21406890508,"gross_gex_1pct":28163.21406890508,"call_oi":35,"put_oi":0},{"strike":52800.0,"call_gex_1pct":14103.395883797826,"put_gex_1pct":0.0,"net_gex_1pct":14103.395883797826,"gross_gex_1pct":14103.395883797826,"call_oi":22,"put_oi":0},{"strike":52900.0,"call_gex_1pct":19538.55427054894,"put_gex_1pct":0.0,"net_gex_1pct":19538.55427054894,"gross_gex_1pct":19538.55427054894,"call_oi":31,"put_oi":0},{"strike":53000.0,"call_gex_1pct":885683.1758768912,"put_gex_1pct":0.0,"net_gex_1pct":885683.1758768912,"gross_gex_1pct":885683.1758768912,"call_oi":1429,"put_oi":0},{"strike":53100.0,"call_gex_1pct":23774.42884177439,"put_gex_1pct":0.0,"net_gex_1pct":23774.42884177439,"gross_gex_1pct":23774.42884177439,"call_oi":39,"put_oi":0},{"strike":53200.0,"call_gex_1pct":14992.253620426036,"put_gex_1pct":0.0,"net_gex_1pct":14992.253620426036,"gross_gex_1pct":14992.253620426036,"call_oi":25,"put_oi":0},{"strike":53300.0,"call_gex_1pct":10030.8479222697,"put_gex_1pct":0.0,"net_gex_1pct":10030.8479222697,"gross_gex_1pct":10030.8479222697,"call_oi":17,"put_oi":0},{"strike":53400.0,"call_gex_1pct":40066.21771218014,"put_gex_1pct":0.0,"net_gex_1pct":40066.21771218014,"gross_gex_1pct":40066.21771218014,"call_oi":69,"put_oi":0},{"strike":53500.0,"call_gex_1pct":75443.3246968144,"put_gex_1pct":0.0,"net_gex_1pct":75443.3246968144,"gross_gex_1pct":75443.3246968144,"call_oi":132,"put_oi":0},{"strike":53600.0,"call_gex_1pct":11815.697040076418,"put_gex_1pct":0.0,"net_gex_1pct":11815.697040076418,"gross_gex_1pct":11815.697040076418,"call_oi":21,"put_oi":0},{"strike":53700.0,"call_gex_1pct":23770.752423386803,"put_gex_1pct":0.0,"net_gex_1pct":23770.752423386803,"gross_gex_1pct":23770.752423386803,"call_oi":58,"put_oi":0},{"strike":53800.0,"call_gex_1pct":11299.652025060122,"put_gex_1pct":0.0,"net_gex_1pct":11299.652025060122,"gross_gex_1pct":11299.652025060122,"call_oi":28,"put_oi":0},{"strike":53900.0,"call_gex_1pct":6359.02874861059,"put_gex_1pct":0.0,"net_gex_1pct":6359.02874861059,"gross_gex_1pct":6359.02874861059,"call_oi":16,"put_oi":0},{"strike":54000.0,"call_gex_1pct":88473.51332223011,"put_gex_1pct":0.0,"net_gex_1pct":88473.51332223011,"gross_gex_1pct":88473.51332223011,"call_oi":226,"put_oi":0},{"strike":54100.0,"call_gex_1pct":3856.6281008252117,"put_gex_1pct":0.0,"net_gex_1pct":3856.6281008252117,"gross_gex_1pct":3856.6281008252117,"call_oi":10,"put_oi":0},{"strike":54200.0,"call_gex_1pct":5699.929987096783,"put_gex_1pct":0.0,"net_gex_1pct":5699.929987096783,"gross_gex_1pct":5699.929987096783,"call_oi":15,"put_oi":0},{"strike":54300.0,"call_gex_1pct":7489.365845636544,"put_gex_1pct":0.0,"net_gex_1pct":7489.365845636544,"gross_gex_1pct":7489.365845636544,"call_oi":20,"put_oi":0},{"strike":54400.0,"call_gex_1pct":7012.461268260292,"put_gex_1pct":0.0,"net_gex_1pct":7012.461268260292,"gross_gex_1pct":7012.461268260292,"call_oi":19,"put_oi":0},{"strike":54500.0,"call_gex_1pct":20737.546608240566,"put_gex_1pct":0.0,"net_gex_1pct":20737.546608240566,"gross_gex_1pct":20737.546608240566,"call_oi":57,"put_oi":0},{"strike":54600.0,"call_gex_1pct":6456.294127931983,"put_gex_1pct":0.0,"net_gex_1pct":6456.294127931983,"gross_gex_1pct":6456.294127931983,"call_oi":18,"put_oi":0},{"strike":54700.0,"call_gex_1pct":8134.454011876268,"put_gex_1pct":0.0,"net_gex_1pct":8134.454011876268,"gross_gex_1pct":8134.454011876268,"call_oi":23,"put_oi":0},{"strike":54800.0,"call_gex_1pct":2790.2344554766973,"put_gex_1pct":0.0,"net_gex_1pct":2790.2344554766973,"gross_gex_1pct":2790.2344554766973,"call_oi":8,"put_oi":0},{"strike":54900.0,"call_gex_1pct":8600.033358781018,"put_gex_1pct":0.0,"net_gex_1pct":8600.033358781018,"gross_gex_1pct":8600.033358781018,"call_oi":25,"put_oi":0},{"strike":55000.0,"call_gex_1pct":173060.49367339295,"put_gex_1pct":0.0,"net_gex_1pct":173060.49367339295,"gross_gex_1pct":173060.49367339295,"call_oi":510,"put_oi":0},{"strike":55100.0,"call_gex_1pct":4686.845294530219,"put_gex_1pct":0.0,"net_gex_1pct":4686.845294530219,"gross_gex_1pct":4686.845294530219,"call_oi":14,"put_oi":0},{"strike":55200.0,"call_gex_1pct":1321.2760850498366,"put_gex_1pct":0.0,"net_gex_1pct":1321.2760850498366,"gross_gex_1pct":1321.2760850498366,"call_oi":4,"put_oi":0},{"strike":55300.0,"call_gex_1pct":3911.569305871572,"put_gex_1pct":0.0,"net_gex_1pct":3911.569305871572,"gross_gex_1pct":3911.569305871572,"call_oi":12,"put_oi":0},{"strike":55400.0,"call_gex_1pct":1708.1194917622008,"put_gex_1pct":0.0,"net_gex_1pct":1708.1194917622008,"gross_gex_1pct":1708.1194917622008,"call_oi":9,"put_oi":0},{"strike":55500.0,"call_gex_1pct":2435.017226367293,"put_gex_1pct":0.0,"net_gex_1pct":2435.017226367293,"gross_gex_1pct":2435.017226367293,"call_oi":13,"put_oi":0},{"strike":55600.0,"call_gex_1pct":3142.994158071551,"put_gex_1pct":0.0,"net_gex_1pct":3142.994158071551,"gross_gex_1pct":3142.994158071551,"call_oi":17,"put_oi":0},{"strike":55700.0,"call_gex_1pct":912.5417606974885,"put_gex_1pct":0.0,"net_gex_1pct":912.5417606974885,"gross_gex_1pct":912.5417606974885,"call_oi":5,"put_oi":0},{"strike":55800.0,"call_gex_1pct":1441.4914599735182,"put_gex_1pct":0.0,"net_gex_1pct":1441.4914599735182,"gross_gex_1pct":1441.4914599735182,"call_oi":8,"put_oi":0},{"strike":55900.0,"call_gex_1pct":11030.7113157312,"put_gex_1pct":0.0,"net_gex_1pct":11030.7113157312,"gross_gex_1pct":11030.7113157312,"call_oi":62,"put_oi":0},{"strike":56000.0,"call_gex_1pct":14758.099244638779,"put_gex_1pct":0.0,"net_gex_1pct":14758.099244638779,"gross_gex_1pct":14758.099244638779,"call_oi":84,"put_oi":0},{"strike":56100.0,"call_gex_1pct":7634.698406849826,"put_gex_1pct":0.0,"net_gex_1pct":7634.698406849826,"gross_gex_1pct":7634.698406849826,"call_oi":44,"put_oi":0},{"strike":56200.0,"call_gex_1pct":342.7719223134217,"put_gex_1pct":0.0,"net_gex_1pct":342.7719223134217,"gross_gex_1pct":342.7719223134217,"call_oi":2,"put_oi":0},{"strike":56400.0,"call_gex_1pct":334.5169565922347,"put_gex_1pct":0.0,"net_gex_1pct":334.5169565922347,"gross_gex_1pct":334.5169565922347,"call_oi":2,"put_oi":0},{"strike":56500.0,"call_gex_1pct":2644.1342077945687,"put_gex_1pct":0.0,"net_gex_1pct":2644.1342077945687,"gross_gex_1pct":2644.1342077945687,"call_oi":16,"put_oi":0},{"strike":56600.0,"call_gex_1pct":163.29912819697876,"put_gex_1pct":0.0,"net_gex_1pct":163.29912819697876,"gross_gex_1pct":163.29912819697876,"call_oi":1,"put_oi":0},{"strike":56700.0,"call_gex_1pct":161.3795501697459,"put_gex_1pct":0.0,"net_gex_1pct":161.3795501697459,"gross_gex_1pct":161.3795501697459,"call_oi":1,"put_oi":0},{"strike":56900.0,"call_gex_1pct":8040.407409905209,"put_gex_1pct":0.0,"net_gex_1pct":8040.407409905209,"gross_gex_1pct":8040.407409905209,"call_oi":51,"put_oi":0},{"strike":57000.0,"call_gex_1pct":61404.120858160284,"put_gex_1pct":0.0,"net_gex_1pct":61404.120858160284,"gross_gex_1pct":61404.120858160284,"call_oi":394,"put_oi":0},{"strike":57100.0,"call_gex_1pct":52077.849043304566,"put_gex_1pct":0.0,"net_gex_1pct":52077.849043304566,"gross_gex_1pct":52077.849043304566,"call_oi":338,"put_oi":0},{"strike":57200.0,"call_gex_1pct":75712.70579746751,"put_gex_1pct":0.0,"net_gex_1pct":75712.70579746751,"gross_gex_1pct":75712.70579746751,"call_oi":497,"put_oi":0},{"strike":57300.0,"call_gex_1pct":249453.2325716669,"put_gex_1pct":0.0,"net_gex_1pct":249453.2325716669,"gross_gex_1pct":249453.2325716669,"call_oi":1656,"put_oi":0}]}
```

### 15．Max Pain

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Max Pain 價位 | 43,700 | TAIFEX Proxy |
| 對應到期月份 | 202611F2 | TAIFEX Proxy |
| 與前一交易日的變化 (2026-11-12→2026-11-13) | +750 | TAIFEX Proxy snapshots (2026-11-12) |

### 17．選擇權法人日盤、夜盤交易

| 法人 | 日盤多單 | 日盤空單 | 日盤淨 | 夜盤多單 | 夜盤空單 | 夜盤淨 | 淨變化 (日-夜) | 資料來源 |
|---|---|---|---|---|---|---|---|---|
| 外資 | 135,406 | 133,406 | +2,000 | 40,671 | 40,017 | +654 | -1,922 | 沿用前版（原來源：TAIFEX Proxy） |
| 投信 | 8,005 | 18,220 | -10,215 | 0 | 0 | +0 | -18,799 | 沿用前版（原來源：TAIFEX Proxy） |
| 自營商 | 134,884 | 138,634 | -3,750 | 25,019 | 29,385 | -4,366 | +25,232 | 沿用前版（原來源：TAIFEX Proxy） |
| 三大法人合計 | 278,295 | 290,260 | -11,965 | 65,690 | 69,402 | -3,712 | +4,511 | 沿用前版（原來源：TAIFEX Proxy） |
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
| 買權多空淨 OI 變化 (2026-11-11→2026-11-16) | -19,234 | TAIFEX Proxy snapshots (2026-11-12) |

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 賣權多方 OI | 30,112 | TAIFEX Proxy |
| 賣權空方 OI | 28,929 | TAIFEX Proxy |
| 賣權多空淨 OI | +1,183 | TAIFEX Proxy |
| 賣權多空淨 OI 變化 (2026-11-11→2026-11-16) | +3,690 | TAIFEX Proxy snapshots (2026-11-12) |
- 資料日期：買權 2026-11-16／賣權 2026-11-16 (TypeOfTraders=0 全部交易人；契約月份 202611)

#### 大戶流向（全日；前十大無日夜拆分）

| 項目 | 淨變化 | 區間 | 資料來源 |
|---|---|---|---|
| 期貨前十大 | -15,651 | 2026-11-11→2026-11-16 | TAIFEX Proxy snapshots (2026-11-12) |
| 買權前十大 | -19,234 | 2026-11-11→2026-11-16 | TAIFEX Proxy snapshots (2026-11-12) |
| 賣權前十大 | +3,690 | 2026-11-11→2026-11-16 | TAIFEX Proxy snapshots (2026-11-12) |

### 16．資料來源、時間、時區與狀態

- 資料來源：TAIFEX 經 Cloudflare Worker Proxy
- 資料日期：2026-11-13；本次報告產製時間：2026-11-17 16:35:37；時區：`Asia/Taipei`
- 日盤／夜盤標記：日盤收盤後 + 夜盤盤後
- 部分取得欄位 (1)：turnover.total
- 註記：--force-rewrite 明示覆蓋（人工指定）
- 註記：同 T0 保護：92 格沿用前版有值（本次抓取缺失不覆寫）
- 註記：同 T0 覆蓋：288 格以本次新抓取覆蓋（該 T0 尚無報告，無凍結對象）
- 未取得欄位 (10)：otc_breadth.up, otc_breadth.down, otc_breadth.flat, otc_breadth.limit_up, otc_breadth.limit_down, institutional.foreign, institutional.trust, institutional.dealer, institutional.total, turnover.otc

## 五、資料來源、時間與完整性

- 台股現貨、TAIFEX 期貨／選擇權以 T0 為基準；海外指數、匯率、ADR、原油、黃金與 Bitcoin 採各來源最新可得報價。各表格均列示實際資料日期；時間皆為 `Asia/Taipei`。
- taiex：`twse-proxy`
- taiex_ohlc：`FinMind TaiwanStockPrice TAIEX`
- listed_breadth：`twse-proxy`
- listed_turnover：`twse-proxy market_statistics`
- margin：`HiStock 上市+上櫃融資融券 (金額口徑；合計需雙市場欄位完整)`
- margin_ratio：`TWSE 上市自建估算（當日暫估；資料日期：2026-11-13；估值 1240 檔；4 檔採最近有效收盤價（價格日期 20260402 至 20261113）；Blave 同 T0 交叉驗證 170.6740%；差異 0.281 個百分點；門檻 <1.00 個百分點；PASS）`
- sbl_bal：`TWSE TWT72U（SLBNLB；上市+上櫃）`
- sbl_sale_bal_listed：`TWSE TWT93U（上市）`
- sbl_sale_bal_otc：`TPEx S47（上櫃）`
- sbl_sale_chg_listed：`TWSE TWT93U（上市）`
- sbl_sale_chg_otc：`TPEx S47（上櫃）`
- sbl_sale_bal：`TWSE TWT93U（上市） + TPEX S47（上櫃）`
- sbl_sale_chg：`TWSE TWT93U（上市） + TPEX S47（上櫃）`
- 期貨選擇權：`TAIFEX Proxy`
- 新聞：台股 Yahoo／國際 Fed＋CNBC＋MarketWatch；台股 Yahoo（不足時財訊快報備援）/ 國際 Fed 公告＋CNBC＋MarketWatch RSS；Fed 無摘要；investing 港股為主已退役；cnyes CSR、wantgoo JS 算繪、中央社/台灣央行路徑待查，未採用
- 美股/亞股/期貨/匯率/ADR/商品：`Yahoo Finance Chart API`；美債：`Yahoo Finance (備援)`
- 註記：上櫃 highlight 日期不符或缺值 (回傳 1151117, T0=1151113)
- 註記：三大法人未取得
- 註記：上市市場維持率為當日暫估，以 TWSE 自建計算為主；4 檔採最近有效收盤價（價格日期 20260402 至 20261113）。Blave 同 T0 交叉驗證 170.6740%；差異 0.281 個百分點；門檻 <1.00 個百分點；PASS。Blave 不可用不影響 DATA_REPORT 產出。
- 註記：上市 MI_MARGN 無日期欄，採用最新可得
- 註記：[partial] 成交金額合計僅取得單一市場；不提供不完整的合計數值
- TAIFEX 註記：無日期端點為最新盤勢快照 (判定資料日期 2026-11-17，非 T0 2026-11-13)，適用：日盤價／法人交易／夜盤／選擇權法人；T0 相符時不另標註
- TAIFEX 註記：futures-price-after-hours 日期 2026-11-17 非今日 2026-11-16，視為無新節次，不採用
- TAIFEX 註記：futures-institutional-after-hours 日期 2026-11-17 非今日 2026-11-16，視為無新節次，不採用
- TAIFEX 註記：options-institutional-after-hours 日期 2026-11-17 非今日 2026-11-16，視為無新節次，不採用
- TAIFEX 註記：法人交易量未提供前日變化端點；日盤、夜盤交易量及日夜淨額差仍照常列示
- TAIFEX 註記：Gamma GEX 實際使用到期月份 202611（到期日 2026-11-18）與 Options Key Levels 主到期月份 202611F2 不同；GEX 數值應以實際使用到期月份為準
- 本報告僅整理資料，不提供交易判斷。

## 六、期現選方向對照

**規則：** 趨勢偏多／空＝現貨、期貨OI、選擇權日淨三者同向；避險／對沖＝現貨與期選反向；日內反轉＝日淨與夜淨反向；缺值標示，不推估。選擇權多空為看多看空口徑。

| 法人 | 現貨買賣超(億) | 期貨OI淨(口) | 期貨日淨 | 期貨夜淨 | 選擇權日淨 | 選擇權夜淨 | 判定 | 期選組合 | 資料來源 |
|---|---|---|---|---|---|---|---|---|---|
| 外資 | +288.4 | -100,870 | -1,144 | -1,631 | +2,000 | +654 | 資料不足 | 資料不足 | 沿用前版（原來源：twse-proxy／TAIFEX Proxy） |
| 投信 | +95.4 | +99,923 | -1,180 | +0 | -10,215 | +0 | 資料不足 | 資料不足 | 沿用前版（原來源：twse-proxy／TAIFEX Proxy） |
| 自營商 | +68.9 | -2,771 | -1,820 | +741 | -3,750 | -4,366 | 資料不足 | 資料不足 | 沿用前版（原來源：twse-proxy／TAIFEX Proxy） |
