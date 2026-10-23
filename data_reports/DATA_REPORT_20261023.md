# DATA_REPORT_20261023

- 報告日期：`2026-10-23`
- T0 交易日期：`2026-10-23`
- 資料產出時間：`2026-10-23 23:37:00`
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
| 加權指數 | 46,041.43 | 點 | TWSE OpenAPI MI_INDEX (備援) |
| 開盤 | unavailable | 點 | FinMind |
| 最高 | unavailable | 點 | FinMind |
| 最低 | unavailable | 點 | FinMind |
| 收盤 | 46,041.43 | 點 | TWSE OpenAPI MI_INDEX (備援) |
| 漲跌點數 | -846.34 | 點 | TWSE OpenAPI MI_INDEX (備援) |
| 漲跌幅 | -1.81 | % | TWSE OpenAPI MI_INDEX (備援) |
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
| 外資 | -815.8 | 億元 | twse-proxy /institutional |
| 投信 | +94.9 | 億元 | twse-proxy /institutional |
| 自營商 | -273.8 | 億元 | twse-proxy /institutional |
| 三大法人合計 | -994.7 | 億元 | twse-proxy /institutional |

### 4. 融資融券

**資料來源：** 上市+上櫃 `HiStock` (金額口徑)；維持率 `istock.tw`；備援官方逐股加總

| 項目 | 數值 | 單位 | 資料來源 |
|---|---|---|---|
| 融資餘額 | unavailable | 億元 | HiStock |
| 融資增減 | unavailable | 億元 | HiStock |
| 融券餘額 | 216,539 | 張 | HiStock |
| 融券增減 | 24,702 | 張 | HiStock |
| 融資維持率 | 182.90 | % | 前值遞補 (DATA 2026-10-22；當日三源皆失敗；民間估算；官方無每日序列) |

### 5. 借券資料

**資料來源：** 上市 `TWSE OpenAPI TWT96U` (可借餘額)、上櫃 `TPEX OpenAPI tpex_margin_sbl`

| 項目 | 數值 | 單位 | 資料來源 |
|---|---|---|---|
| 借券餘額 | 2,465,395 | 張 | TWSE TWT93U + TPEX margin_sbl |
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
| S&P 500 | ^GSPC | 7,649.09 | -14.34 | -0.19 | Yahoo Finance Chart API |
| Nasdaq Composite | ^IXIC | 26,051.95 | 43.09 | +0.17 | Yahoo Finance Chart API |
| Nasdaq 100 | ^NDX | 29,075.47 | 116.78 | +0.40 | Yahoo Finance Chart API |
| Dow Jones | ^DJI | 52,332.93 | -535.05 | -1.01 | Yahoo Finance Chart API |
| 費城半導體 SOX | ^SOX | 10,836.43 | 104.45 | +0.97 | Yahoo Finance Chart API |
| VIX | ^VIX | 19.14 | 0.11 | +0.58 | Yahoo Finance Chart API |

### 2. 亞洲主要指數

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 收盤／最新值 | 漲跌點 | 漲跌幅 | 資料來源 |
|---|---|---|---|---|---|
| 日經225 | ^N225 | 62,907.84 | -1,713.40 | -2.65 | Yahoo Finance Chart API |
| 韓國KOSPI | ^KS11 | 5,533.77 | -201.89 | -3.52 | Yahoo Finance Chart API |
| 香港恆生 | ^HSI | 23,093.37 | 158.69 | +0.69 | Yahoo Finance Chart API |
| 上海綜合 | 000001.SS | 3,690.48 | 32.45 | +0.89 | Yahoo Finance Chart API |
| 深圳成分 | 399001.SZ | 11,673.83 | 316.51 | +2.79 | Yahoo Finance Chart API |

### 3. 美股指數期貨

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 最新值 | 漲跌點 | 漲跌幅 | 資料來源 |
|---|---|---|---|---|---|
| S&P500期貨 | ES=F | 7,694.75 | -9.75 | -0.13 | Yahoo Finance Chart API |
| Nasdaq100期貨 | NQ=F | 29,273.25 | 131.25 | +0.45 | Yahoo Finance Chart API |
| 道瓊期貨 | YM=F | 52,610.00 | -458.00 | -0.86 | Yahoo Finance Chart API |
| Russell2000期貨 | RTY=F | 2,787.80 | -8.30 | -0.30 | Yahoo Finance Chart API |

### 4. 美國國債殖利率

**資料來源：** `U.S. Treasury Fiscal Data API` (失敗時備援 Treasury yield.xml 與 `Yahoo Finance`)

| 項目 | API 資料欄位／識別 | 殖利率 | 日變化 | 資料來源 |
|---|---|---|---|---|
| 美國 2 年期殖利率 | 2 Yr | 4.65 | -0.16 | U.S. Treasury yield.xml (網頁備援) |
| 美國 10 年期殖利率 | 10 Yr | 4.99 | 0.04 | Yahoo Finance (備援) |
| 美國 30 年期殖利率 | 30 Yr | 5.32 | 0.03 | Yahoo Finance (備援) |

### 5. 主要匯率

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 最新值 | 漲跌點 | 漲跌幅 | 資料來源 |
|---|---|---|---|---|---|
| USD/TWD | TWD=X | 32.56 | 0.19 | +0.58 | Yahoo Finance Chart API |
| DXY美元指數 | DX-Y.NYB | 101.75 | 0.14 | +0.14 | Yahoo Finance Chart API |
| USD/JPY | JPY=X | 156.89 | -1.25 | -0.79 | Yahoo Finance Chart API |
| USD/KRW | KRW=X | 1,325.06 | -0.53 | -0.04 | Yahoo Finance Chart API |

### 6. 台灣相關ADR

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 收盤／最新值 | 漲跌點 | 漲跌幅 | 資料來源 |
|---|---|---|---|---|---|
| 台積電ADR | TSM | 418.52 | 6.17 | +1.50 | Yahoo Finance Chart API |
| 聯電ADR | UMC | 18.88 | 0.35 | +1.89 | Yahoo Finance Chart API |
| 日月光ADR | ASX | 38.71 | 0.97 | +2.56 | Yahoo Finance Chart API |

### 7. 原油黃金Bitcoin

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 收盤／最新值 | 漲跌點 | 漲跌幅 | 資料來源 |
|---|---|---|---|---|---|
| WTI原油期貨 | CL=F | 101.96 | 2.49 | +2.50 | Yahoo Finance Chart API |
| 黃金期貨 | GC=F | 4,013.30 | -47.10 | -1.16 | Yahoo Finance Chart API |
| Bitcoin | BTC-USD | 81,390.28 | 78.39 | +0.10 | Yahoo Finance Chart API |

### 8. 重大經濟數據、央行事件與重大市場新聞

**資料來源：** 台股 `tw.stock.yahoo.com` (含內文摘要)；國際 `Fed 公告 RSS`＋`CNBC`＋`MarketWatch` (標題、來源、時間與連結)

- 事件1：獲得四檔ETF青睞 欣興一年漲幅狂飆582%
  - 來源：Yahoo 台股；發布時間：2026-10-23T07:37:25Z；台北時間：2026-10-23 15:37
  - 摘要：主動式ETF成分股誰最會漲？《Yahoo股市》交叉比對規模前五大國內股票型主動式ETF的前十大持股，發現除了台積電（2330）、聯發科（2454）等大型權值股外，台光電（2383）、欣興（3037）及奇鋐（3017）也同時獲得四檔ETF青睞
  - 原文連結：https://tw.stock.yahoo.com/news/%E3%80%90%E8%B7%9F%E8%91%97%E4%B8%BB%E5%8B%95%E5%BC%8Fetf%E8%B2%B71%E3%80%91%E4%B8%8D%E6%98%AF%E5%8F%B0%E7%A9%8D%E9%9B%BB%EF%BC%8100981a%E3%80%8100403a%E6%90%B6%E8%B2%B7%E6%AC%A3%E8%88%88-%E4%B8%80%E5%B9%B4%E5%A4%A7%E6%BC%B2582-073725113.html
- 事件2：房價飆破7字頭 三重建案強勁拉升變有錢人聚集地？
  - 來源：Yahoo 台股；發布時間：2026-10-23T08:06:00Z；台北時間：2026-10-23 16:06
  - 摘要：台北市的高房價將大批購屋族往外推擠，但當傳統被視為衛星市鎮的區域也紛紛站上令人咋舌的價格高點時，受薪階級的成家門檻究竟被推高到何種地步？這項關於蛋白區翻轉與薪資承受力的焦慮，隨著民眾看房實況再度掀起論戰。
  - 原文連結：https://tw.stock.yahoo.com/news/%E4%B8%89%E9%87%8D%E6%88%BF%E5%83%B9%E9%A3%86%E7%A0%B47%E5%AD%97%E9%A0%AD-%E8%AE%8A%E6%9C%89%E9%8C%A2%E4%BA%BA%E8%81%9A%E9%9B%86%E5%9C%B0-%E4%BB%96%E9%A9%9A%E5%91%86-%E5%88%B0%E5%BA%95%E9%83%BD%E5%81%9A%E4%BB%80%E9%BA%BC%E5%B7%A5%E4%BD%9C-080600449.html
- 事件3：美麗新影城退出淡海提告宏泰敗訴 爆還欠債上億元
  - 來源：Yahoo 台股；發布時間：2026-10-23T08:09:10Z；台北時間：2026-10-23 16:09
  - 摘要：台北地院依據租賃契約書認定，宏泰人壽裝修影城花費1億5000萬元，如果美麗新租用未滿15年，須照剩餘年數比例補償工程款；影城只開6年就不再營業，換算下來，「房客」還欠「房東」1.36億元，所以宏泰扣留設備有理，判決美麗新敗訴。美麗新淡海影城
  - 原文連結：https://tw.stock.yahoo.com/news/%E7%8D%A8-%E5%BD%B1%E5%9F%8E%E6%AF%80%E6%96%BC%E9%A2%B1%E9%A2%A8-%E7%BE%8E%E9%BA%97%E6%96%B0%E9%80%80%E5%87%BA%E6%B7%A1%E6%B5%B7%E5%91%8A%E5%AE%8F%E6%B3%B0%E5%90%9E%E6%95%97-%E9%82%84%E7%88%86%E6%AC%A0%E5%82%B5%E4%B8%8A%E5%84%84-080910000.html
- 事件4：颱風來襲航班大規模取消 旅行社逾百團行程受影響
  - 來源：Yahoo 台股；發布時間：2026-10-23T06:56:54Z；台北時間：2026-10-23 14:56
  - 摘要：薔琵颱風來襲，今（23）日全台航班大規模取消，打亂民眾出國及返台計畫。《Yahoo股市》統計，鳳凰旅遊（5706）確認取消7團、延後出發5團，旅天下（6961）則有約17團取消或延後，兩家合計約29團受衝擊；可樂旅遊另預估近百團行程受到影響
  - 原文連結：https://tw.stock.yahoo.com/news/%E9%80%A3%E5%81%87%E6%B3%A1%E6%B9%AF%E4%BA%86%EF%BC%81%E9%B3%B3%E5%87%B0%E3%80%81%E6%97%85%E5%A4%A9%E4%B8%8B29%E5%9C%98%E5%8F%96%E6%B6%88%E6%88%96%E5%BB%B6%E5%BE%8C-%E5%8F%AF%E6%A8%82%E6%97%85%E9%81%8A%E8%BF%91%E7%99%BE%E5%9C%98%E8%A1%8C%E7%A8%8B%E5%8F%97%E5%BD%B1%E9%9F%BF-065654363.html
- 事件5：多檔科技ETF今年漲翻倍 基金教授獻策避重複押寶
  - 來源：Yahoo 台股；發布時間：2026-10-22T22:29:00Z；台北時間：2026-10-23 06:29
  - 摘要：今年科技ETF績效亮眼，多檔報酬翻倍，讓不少投資人既怕追高，又怕錯過行情。但ETF名稱不同，買進的股票可能高度重疊。基金教授朱岳中提醒，挑ETF不能只看排行榜，應拆開持股、辨認產業布局，再決定如何搭配，避免看似分散，實際仍重押同一波AI行情
  - 原文連結：https://tw.stock.yahoo.com/news/%E9%8C%A2%E9%8F%A1%E4%BD%A0%E5%AE%B61-%E7%A7%91%E6%8A%80etf%E4%BB%8A%E5%B9%B4%E6%BC%B2%E7%BF%BB%E5%80%8D-%E5%9F%BA%E9%87%91%E6%95%99%E6%8E%88%E9%BB%9E%E5%90%8D3%E6%AA%94-%E6%95%99%E4%BD%A0%E9%81%BF%E9%96%8B%E9%87%8D%E8%A4%87%E6%8A%BC%E5%AF%B6-222900806.html
- 事件6：前三季本業虧損但整體淨利1234萬 揚明光Q4出貨估下滑
  - 來源：Yahoo 台股；發布時間：2026-10-23T06:46:13Z；台北時間：2026-10-23 14:46
  - 摘要：光學廠揚明光（3504）今（23）日公告董事會通過今年前三季合併財報，累計營收21.7億元，歸屬母公司業主淨利1,234萬元，每股盈餘（EPS）0.11元。揚明光表示，第三季受惠客戶AR眼鏡進入量產、車用LiDAR鏡頭新機種出貨增加，營收較
  - 原文連結：https://tw.stock.yahoo.com/news/%E6%8F%9A%E6%98%8E%E5%85%89%E5%89%8D%E4%B8%89%E5%AD%A3%E8%B3%BA1234%E8%90%AC%E5%85%83-%E7%AC%AC%E5%9B%9B%E5%AD%A3%E5%87%BA%E8%B2%A8%E4%BC%B0%E4%B8%8B%E6%BB%91-064613824.html
- 事件7：10-year Treasury yield drops back to 5% this week as investors seek cover from AI worries
  - 來源：CNBC；發布時間：Fri, 23 Oct 2026 15:27:33 GMT；台北時間：2026-10-23 23:27
  - 摘要：The 10-year Treasury yield stayed below 5% Friday after AI-driven tech selling sent investors into government bonds.
  - 原文連結：https://www.cnbc.com/2026/10/23/bonds-yields-us-treasurys.html
- 事件8：Brent crude oil tops $116, a six-month high, as tensions swell in the Middle East
  - 來源：CNBC；發布時間：Fri, 23 Oct 2026 13:50:46 GMT；台北時間：2026-10-23 21:50
  - 摘要：U.S. President Donald Trump accused Iran on Thursday of trying to manipulate the oil market.
  - 原文連結：https://www.cnbc.com/2026/10/23/oil-price-brent-wti-iran-war-saudi-arabia.html
- 事件9：AI agents could disrupt bank deposits. Why Wall Street may be overreacting
  - 來源：CNBC；發布時間：Fri, 23 Oct 2026 15:00:49 GMT；台北時間：2026-10-23 23:00
  - 摘要：Analysts say the fears that AI agents could disrupt the banking industry are overblown, for now.
  - 原文連結：https://www.cnbc.com/investingclub/2026/10/23/ai-agents-could-disrupt-bank-deposits-why-wall-street-may-be-overreacting.html


## 三、期貨

**資料來源：**
1. Cloudflare Workers：TAIFEX Proxy — https://taifex.grichtoyang.workers.dev/
2. TAIFEX Open API — https://openapi.taifex.com.tw/

近月契約月份：202611 (日盤成交量最大者)；交易日期：2026-10-23

### 1．台指期近月日盤行情

| 項目 | 數值 | 資料來源 |
|---|---|---|
| 開盤價 | 47,164 | TAIFEX Proxy |
| 最高價 | 47,337 | TAIFEX Proxy |
| 最低價 | 46,217 | TAIFEX Proxy |
| 收盤價 | 46,272 | TAIFEX Proxy |
| 漲跌點數 | -741 | TAIFEX Proxy |
| 漲跌幅 | -1.58 | TAIFEX Proxy |
| 成交量 | 55,226 | TAIFEX Proxy |
| 日盤高點及低點 | 47,337 / 46,217 | TAIFEX Proxy |

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
| 前十大交易人多方 OI | 89,928 | TAIFEX Proxy |
| 前十大交易人空方 OI | 80,904 | TAIFEX Proxy |
| 前十大交易人多空淨 OI | +9,024 | TAIFEX Proxy |
| 多空淨 OI 變化 (2026-10-21→2026-10-22) | +1,334 | TAIFEX Proxy snapshots (2026-10-22) |
- 資料日期：2026-10-22 (TypeOfTraders=0 全部交易人；契約月份 202611)

### 5．日盤、夜盤法人交易資料

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 外資日盤多單交易量 | 50,162 | TAIFEX Proxy |
| 外資日盤空單交易量 | 51,383 | TAIFEX Proxy |
| 外資日盤多空淨交易量 | -1,221 | TAIFEX Proxy |
| 外資夜盤多單交易量 | unavailable | TAIFEX Proxy |
| 外資夜盤空單交易量 | unavailable | TAIFEX Proxy |
| 外資夜盤多空淨交易量 | unavailable | TAIFEX Proxy |
| 外資日盤／夜盤交易量變化 | unavailable | TAIFEX Proxy |
| 投信日盤多空淨交易量 | -177 | TAIFEX Proxy |
| 投信夜盤多空淨交易量 | unavailable | TAIFEX Proxy |
| 投信日盤／夜盤交易量變化 | unavailable | TAIFEX Proxy |
| 自營商日盤多空淨交易量 | +1,565 | TAIFEX Proxy |
| 自營商夜盤多空淨交易量 | unavailable | TAIFEX Proxy |
| 自營商日盤／夜盤交易量變化 | unavailable | TAIFEX Proxy |
| 三大法人日盤多空淨交易量 | +167 | TAIFEX Proxy |
| 三大法人夜盤多空淨交易量 | unavailable | TAIFEX Proxy |
| 法人日盤交易金額淨額 (億元) | +14.1 | TAIFEX Proxy |
| 法人夜盤交易金額淨額 (億元) | unavailable | TAIFEX Proxy |

### 6．期貨與現貨關係

| 項目 | 數值 | 資料來源 |
|---|---|---|
| 台指期近月價格 | 46,272 | TAIFEX Proxy |
| 加權指數價格 | 46,041.43 | TWSE OpenAPI MI_INDEX (備援) |
| 台指期與加權指數價差 | +230.57 | TAIFEX Proxy+TWSE OpenAPI MI_INDEX (備援) |
| 價差百分比 | +0.50 | TAIFEX Proxy+TWSE OpenAPI MI_INDEX (備援) |
| 日盤基差 | +230.57 | TAIFEX Proxy+TWSE OpenAPI MI_INDEX (備援) |
| 夜盤價格相對日盤收盤的變化 | unavailable | 端點未提供 |

### 7．日盤、夜盤與籌碼變化對照

#### 7.1 日夜盤價格與成交量對照 (變化 = 日盤 - 夜盤)

| 項目 | 日盤 | 夜盤 | 變化 (日-夜) | 資料來源 |
|---|---|---|---|---|
| 收盤價 | 46,272 | unavailable | unavailable | TAIFEX Proxy |
| 成交量 | 55,226 | unavailable | unavailable | TAIFEX Proxy |
- 台指期總 OI 前日變化：+0（來源：TAIFEX Proxy）


#### 7.2 法人籌碼日夜盤對照 (淨變化 = 日盤淨 - 夜盤淨；OI 為日盤收盤後總量，前日變化另列)

| 法人 | 交易量 |  |  |  |  |  |  | 未平倉量 |  |  |  | 資料來源 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|  | **日盤多單** | **日盤空單** | **日盤淨** | **夜盤多單** | **夜盤空單** | **夜盤淨** | **淨變化 (日-夜)** | **OI多方** | **OI空方** | **OI淨** | **OI前日變化** |  |
| 外資 | 50,162 | 51,383 | -1,221 | unavailable | unavailable | unavailable | unavailable | unavailable | unavailable | unavailable | unavailable | TAIFEX Proxy |
| 投信 | 568 | 745 | -177 | unavailable | unavailable | unavailable | unavailable | unavailable | unavailable | unavailable | unavailable | TAIFEX Proxy |
| 自營商 | 5,489 | 3,924 | +1,565 | unavailable | unavailable | unavailable | unavailable | unavailable | unavailable | unavailable | unavailable | TAIFEX Proxy |
| 三大法人合計 | 56,219 | 56,052 | +167 | unavailable | unavailable | unavailable | unavailable | 0 | 0 | +0 | +0 | TAIFEX Proxy |

#### 7.3 前十大交易人日夜盤對照 (OI 無日夜拆分，列收盤後總量)

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 前十大交易人多方 OI | 89,928 | TAIFEX Proxy |
| 前十大交易人空方 OI | 80,904 | TAIFEX Proxy |
| 前十大交易人多空淨 OI | +9,024 | TAIFEX Proxy |
| 前十大交易人多空淨 OI 變化 (2026-10-21→2026-10-22) | +1,334 | TAIFEX Proxy snapshots (2026-10-22) |

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
| 交易日期 | 2026-10-23 | TAIFEX Proxy |
| 到期月份／到期日 | 202610F4 | TAIFEX Proxy |
| 資料更新時間 | 2026-10-23 23:37:00 | 本機 |
| 日盤／夜盤標記 | 日盤收盤後資料 | TAIFEX Proxy |

### 2．Call 總成交量、OI、OI 增減

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Call 總成交量 | 178,535 | TAIFEX Proxy |
| Call 總未平倉量 OI | 55,024 | TAIFEX Proxy |
| Call OI 增減 (2026-10-22→2026-10-23) | +0 | TAIFEX Proxy snapshots (2026-10-22) |

### 3．Put 總成交量、OI、OI 增減

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Put 總成交量 | 155,316 | TAIFEX Proxy |
| Put 總未平倉量 OI | 31,411 | TAIFEX Proxy |
| Put OI 增減 (2026-10-22→2026-10-23) | +0 | TAIFEX Proxy snapshots (2026-10-22) |

### 4．Call／Put 比例與變化

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Call／Put 成交量比例 | 1.15 | TAIFEX Proxy |
| Call／Put 未平倉量比例 | 1.75 | TAIFEX Proxy |
| Put／Call Ratio | 0.57 | TAIFEX Proxy |
| Call／Put 比例變化 (量比 2026-10-21→2026-10-22) | -25.67 | TAIFEX Proxy |
| 與前一交易日比較 (OI 比 2026-10-21→2026-10-22) | 3.32 | TAIFEX Proxy |
**資料來源：** 比例 `TAIFEX Proxy chain`；變化 `TAIFEX Proxy PutCallRatio`

### 5．外資 Call／Put 部位

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 外資 Call日買 | 45,172 | TAIFEX Proxy |
| 外資 Call日賣 | 45,054 | TAIFEX Proxy |
| 外資 Call日淨 | +118 | TAIFEX Proxy |
| 外資 Put日買 | 52,064 | TAIFEX Proxy |
| 外資 Put日賣 | 52,245 | TAIFEX Proxy |
| 外資 Put日淨 | -181 | TAIFEX Proxy |
| 外資 Call夜買 | 31,148 | TAIFEX Proxy |
| 外資 Call夜賣 | 31,095 | TAIFEX Proxy |
| 外資 Call夜淨 | +53 | TAIFEX Proxy |
| 外資 Put夜買 | 45,050 | TAIFEX Proxy |
| 外資 Put夜賣 | 44,680 | TAIFEX Proxy |
| 外資 Put夜淨 | +370 | TAIFEX Proxy |
| 外資 日盤淨總量 | +299 | TAIFEX Proxy |
| 外資 Call日夜淨增減 (日－夜) | +65 | TAIFEX Proxy |
| 外資 Put日夜淨增減 (日－夜) | -551 | TAIFEX Proxy |

### 6．自營商 Call／Put 部位

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 自營商 Call日買 | 65,292 | TAIFEX Proxy |
| 自營商 Call日賣 | 64,470 | TAIFEX Proxy |
| 自營商 Call日淨 | +822 | TAIFEX Proxy |
| 自營商 Put日買 | 52,508 | TAIFEX Proxy |
| 自營商 Put日賣 | 54,441 | TAIFEX Proxy |
| 自營商 Put日淨 | -1,933 | TAIFEX Proxy |
| 自營商 Call夜買 | 25,115 | TAIFEX Proxy |
| 自營商 Call夜賣 | 25,696 | TAIFEX Proxy |
| 自營商 Call夜淨 | -581 | TAIFEX Proxy |
| 自營商 Put夜買 | 36,173 | TAIFEX Proxy |
| 自營商 Put夜賣 | 36,732 | TAIFEX Proxy |
| 自營商 Put夜淨 | -559 | TAIFEX Proxy |
| 自營商 日盤淨總量 | +2,755 | TAIFEX Proxy |
| 自營商 Call日夜淨增減 (日－夜) | +1,403 | TAIFEX Proxy |
| 自營商 Put日夜淨增減 (日－夜) | -1,374 | TAIFEX Proxy |

### 7．主要 Call OI 集中區

| 項目 | 履約價 | OI | 資料來源 |
|---|---|---|---|
| Call OI 第1大履約價 | 49,000 | 2,444 | TAIFEX Proxy |
| Call OI 第2大履約價 | 47,000 | 2,275 | TAIFEX Proxy |
| Call OI 第3大履約價 | 51,000 | 1,993 | TAIFEX Proxy |
| Call OI 最大履約價 | 49,000 | 2,444 | TAIFEX Proxy |

#### Call OI 分布明細 Top10 (機器可讀，到期月份 202610F4)

| # | 履約價 | OI | 佔比 | 資料來源 |
|---|---|---|---|---|
| C1 | 49,000 | 2,444 | 4.44% | TAIFEX Proxy |
| C2 | 47,000 | 2,275 | 4.13% | TAIFEX Proxy |
| C3 | 51,000 | 1,993 | 3.62% | TAIFEX Proxy |
| C4 | 48,000 | 1,851 | 3.36% | TAIFEX Proxy |
| C5 | 47,500 | 1,600 | 2.91% | TAIFEX Proxy |
| C6 | 48,350 | 1,591 | 2.89% | TAIFEX Proxy |
| C7 | 47,600 | 1,555 | 2.83% | TAIFEX Proxy |
| C8 | 48,500 | 1,424 | 2.59% | TAIFEX Proxy |
| C9 | 45,100 | 1,401 | 2.55% | TAIFEX Proxy |
| C10 | 47,200 | 1,139 | 2.07% | TAIFEX Proxy |


### 8．主要 Put OI 集中區

| 項目 | 履約價 | OI | 資料來源 |
|---|---|---|---|
| Put OI 第1大履約價 | 46,000 | 1,829 | TAIFEX Proxy |
| Put OI 第2大履約價 | 46,500 | 1,537 | TAIFEX Proxy |
| Put OI 第3大履約價 | 45,500 | 1,531 | TAIFEX Proxy |
| Put OI 最大履約價 | 46,000 | 1,829 | TAIFEX Proxy |

#### Put OI 分布明細 Top10 (機器可讀，到期月份 202610F4)

| # | 履約價 | OI | 佔比 | 資料來源 |
|---|---|---|---|---|
| P1 | 46,000 | 1,829 | 5.82% | TAIFEX Proxy |
| P2 | 46,500 | 1,537 | 4.89% | TAIFEX Proxy |
| P3 | 45,500 | 1,531 | 4.87% | TAIFEX Proxy |
| P4 | 45,000 | 1,478 | 4.71% | TAIFEX Proxy |
| P5 | 44,000 | 1,106 | 3.52% | TAIFEX Proxy |
| P6 | 45,800 | 956 | 3.04% | TAIFEX Proxy |
| P7 | 45,900 | 854 | 2.72% | TAIFEX Proxy |
| P8 | 46,450 | 819 | 2.61% | TAIFEX Proxy |
| P9 | 45,400 | 768 | 2.45% | TAIFEX Proxy |
| P10 | 47,000 | 756 | 2.41% | TAIFEX Proxy |


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
| Call Wall 價位 | 49,000 | TAIFEX Proxy |
| 對應到期月份 | 202610F4 | TAIFEX Proxy |
| 與前一交易日的變化 (2026-10-22→2026-10-23) | +0 | TAIFEX Proxy snapshots (2026-10-22) |

### 12．Put Wall

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Put Wall 價位 | 46,000 | TAIFEX Proxy |
| 對應到期月份 | 202610F4 | TAIFEX Proxy |
| 與前一交易日的變化 (2026-10-22→2026-10-23) | +0 | TAIFEX Proxy snapshots (2026-10-22) |

### 13．Gamma Wall

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Gamma Wall 價位 | 47,000.00 | TAIFEX Proxy (options-market-structure-compact (proxy)) |
| 對應到期月份 | 202610F4 | TAIFEX Proxy |
| 資料日期 | 2026-10-21 | TAIFEX Proxy (options-market-structure-compact (proxy)) |

### 14．Gamma Flip

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Gamma Flip 價位 | 46,174.50 | TAIFEX Proxy (options-market-structure-compact (proxy)) |
| 對應到期月份 | 202610F4 | TAIFEX Proxy |
| 資料日期 | 2026-10-21 | TAIFEX Proxy (options-market-structure-compact (proxy)) |

### 15．Max Pain

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Max Pain 價位 | 46,000 | TAIFEX Proxy |
| 對應到期月份 | 202610F4 | TAIFEX Proxy |
| 與前一交易日的變化 (2026-10-22→2026-10-23) | +0 | TAIFEX Proxy snapshots (2026-10-22) |

### 17．選擇權法人日盤、夜盤交易

| 法人 | 日盤多單 | 日盤空單 | 日盤淨 | 夜盤多單 | 夜盤空單 | 夜盤淨 | 淨變化 (日-夜) | 資料來源 |
|---|---|---|---|---|---|---|---|---|
| 外資 | 97,417 | 97,118 | +299 | unavailable | unavailable | unavailable | unavailable | TAIFEX Proxy |
| 投信 | 0 | 2,000 | -2,000 | unavailable | unavailable | unavailable | unavailable | TAIFEX Proxy |
| 自營商 | 119,733 | 116,978 | +2,755 | unavailable | unavailable | unavailable | unavailable | TAIFEX Proxy |
| 三大法人合計 | 217,150 | 216,096 | +1,054 | unavailable | unavailable | unavailable | unavailable | TAIFEX Proxy |
- 方法論：多方＝買Call＋賣Put（看多），空方＝賣Call＋買Put（看空），淨額＝看多－看空（已用 Call／Put 拆分頁交叉驗算一致）
- 公式：多方(買)－空方(賣)＝（買call＋賣put）－（賣call＋買put）＝看多－看空
- 速記：多＝BC＋SP、空＝SC＋BP

#### 法人多空力道表（金額・億元；上游千元／1e5）

| 法人 | 日多方力道 | 日空方力道 | 日淨多空力道 | 夜多方力道 | 夜空方力道 | 夜淨多空力道 | 日淨－夜淨 | 資料來源 |
|---|---|---|---|---|---|---|---|---|
| 外資 | 11.44 | 11.58 | -0.14 | 8.57 | 8.75 | -0.18 | +0.04 | TAIFEX Proxy |
| 投信 | 0.00 | 1.10 | -1.10 | 0.00 | 0.00 | +0 | -1.10 | TAIFEX Proxy |
| 自營商 | 12.75 | 14.01 | -1.26 | 7.08 | 7.52 | -0.44 | -0.82 | TAIFEX Proxy |
| 三大法人合計 | 24.18 | 26.69 | -2.51 | 15.64 | 16.26 | -0.62 | -1.89 | TAIFEX Proxy |

### 18．選擇權前十大

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 買權多方 OI | 7,058 | TAIFEX Proxy |
| 買權空方 OI | 8,732 | TAIFEX Proxy |
| 買權多空淨 OI | -1,674 | TAIFEX Proxy |
| 買權多空淨 OI 變化 (2026-10-21→2026-10-22) | -215 | TAIFEX Proxy snapshots (2026-10-22) |

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 賣權多方 OI | 7,763 | TAIFEX Proxy |
| 賣權空方 OI | 9,398 | TAIFEX Proxy |
| 賣權多空淨 OI | -1,635 | TAIFEX Proxy |
| 賣權多空淨 OI 變化 (2026-10-21→2026-10-22) | -350 | TAIFEX Proxy snapshots (2026-10-22) |
- 資料日期：買權 2026-10-22／賣權 2026-10-22 (TypeOfTraders=0 全部交易人；契約月份 202611)

#### 大戶流向（全日；前十大無日夜拆分）

| 項目 | 淨變化 | 區間 | 資料來源 |
|---|---|---|---|
| 期貨前十大 | +1,334 | 2026-10-21→2026-10-22 | TAIFEX Proxy snapshots (2026-10-22) |
| 買權前十大 | -215 | 2026-10-21→2026-10-22 | TAIFEX Proxy snapshots (2026-10-22) |
| 賣權前十大 | -350 | 2026-10-21→2026-10-22 | TAIFEX Proxy snapshots (2026-10-22) |

### 16．資料來源、時間、時區與狀態

- 資料來源：TAIFEX 經 Cloudflare Worker Proxy
- 資料日期：2026-10-23；資料時間：2026-10-23 23:37:00；時區：`Asia/Taipei`
- 日盤／夜盤標記：日盤收盤後 + 夜盤盤後
- 未取得欄位 (20)：taiex.open, taiex.high, taiex.low, listed_breadth.up, listed_breadth.down, listed_breadth.flat, listed_breadth.limit_up, listed_breadth.limit_down, otc_breadth.up, otc_breadth.down, otc_breadth.flat, otc_breadth.limit_up, otc_breadth.limit_down, margin.fin_yi, margin.fin_chg_yi, sbl.sale_bal, sbl.sale_chg, turnover.listed, turnover.otc, turnover.total
- 註記：futures-price-after-hours 日期 2026-10-22 非今日 2026-10-23，視為無新節次，不採用
- 註記：futures-institutional-after-hours 日期 2026-10-27 非今日 2026-10-23，視為無新節次，不採用
- 註記：options-institutional-after-hours 日期 2026-10-27 非今日 2026-10-23，視為無新節次，不採用
- 註記：Call/Put Wall 與 Max Pain 資料日期 2026-10-22 (T0 2026-10-23 端點不穩，採最新可得)
- 註記：Gamma 資料日期 2026-10-21 (T0 2026-10-23 尚無，上游 FMTQIK 落後，採最新可得)
- 註記：夜盤開高低收未取得 (proxy 與官方皆無)，僅成交量/OI/結算價
- 註記：法人 OI 未取得
- 註記：法人交易量變化無昨日交易端點，標 unavailable
- 註記：選擇權 chain 資料日期 2026-10-22 (T0 2026-10-23 端點不穩，採最新可得)
- 註記：Gamma Wall/Flip 資料日期 2026-10-21 (來源 options-market-structure-compact (proxy))

## 五、資料來源、時間與完整性

- 期貨/匯率為最新報價，其餘為 T0 收盤資料；時間皆為 `Asia/Taipei`。
- taiex：`TWSE OpenAPI MI_INDEX (備援)`
- listed_breadth：`twse-proxy`
- listed_turnover：`twse-proxy market_statistics`
- institutional：`twse-proxy /institutional`
- margin_short：`TWSE MI_MARGN + TPEX margin_balance (張)`
- margin_ratio：`前值遞補 (DATA 2026-10-22；當日三源皆失敗；民間估算；官方無每日序列)`
- sbl：`TWSE TWT93U + TPEX margin_sbl`
- 期貨選擇權：`TAIFEX Proxy`
- 新聞：台股 Yahoo／國際 Fed＋CNBC＋MarketWatch；台股 Yahoo（不足時財訊快報備援）/ 國際 Fed 公告＋CNBC＋MarketWatch RSS；Fed 無摘要；investing 港股為主已退役；cnyes CSR、wantgoo JS 算繪、中央社/台灣央行路徑待查，未採用
- 美股/亞股/期貨/匯率/ADR/商品：`Yahoo Finance Chart API`；美債：`Yahoo Finance (備援)`
- 註記：twse-proxy taiex 缺值，改用 MI_INDEX 備援
- 註記：大盤開高低未取得 (FinMind 失敗；MI_INDEX 無此欄)
- 註記：twtazu_od 備援日期不符 (回傳舊資料)，上市漲跌標 unavailable
- 註記：上櫃 highlight 日期不符或缺值 (回傳 1151022, T0=1151023)
- 註記：三大法人回傳日期 20261022 (T0 20261023)，採用最新可得
- 註記：HiStock 未取得，融資餘額/增減標 unavailable (官方逐股加總僅有張數)
- 註記：融券沿用官方逐股加總 (張)
- 註記：融資維持率未取得 (三源皆失敗；官方無每日序列)
- 註記：融資維持率採前值遞補 (DATA 2026-10-22)，非 T0 2026-10-23
- 註記：上市 MI_MARGN / TWT96U 無日期欄，採用最新可得
- 本報告僅整理資料，不提供交易判斷。

## 六、期現選方向對照

**規則：** 趨勢偏多／空＝現貨、期貨OI、選擇權日淨三者同向；避險／對沖＝現貨與期選反向；日內反轉＝日淨與夜淨反向；缺值標示，不推估。選擇權多空為看多看空口徑。

| 法人 | 現貨買賣超(億) | 期貨OI淨(口) | 期貨日淨 | 期貨夜淨 | 選擇權日淨 | 選擇權夜淨 | 判定 | 期選組合 | 資料來源 |
|---|---|---|---|---|---|---|---|---|---|
| 外資 | -815.8 | unavailable | -1,221 | unavailable | +299 | unavailable | 資料不足 | 資料不足 | twse-proxy／TAIFEX Proxy |
| 投信 | +94.9 | unavailable | -177 | unavailable | -2,000 | unavailable | 資料不足 | 資料不足 | twse-proxy／TAIFEX Proxy |
| 自營商 | -273.8 | unavailable | +1,565 | unavailable | +2,755 | unavailable | 資料不足 | 資料不足 | twse-proxy／TAIFEX Proxy |
