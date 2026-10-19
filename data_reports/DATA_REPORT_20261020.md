# DATA_REPORT_20261020

- 報告日期：`2026-10-20`
- T0 交易日期：`2026-10-20`
- 資料產出時間：`2026-10-20 01:28:08`
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
| 加權指數 | 47,111.26 | 點 | TWSE OpenAPI MI_INDEX (備援) |
| 開盤 | unavailable | 點 | FinMind |
| 最高 | unavailable | 點 | FinMind |
| 最低 | unavailable | 點 | FinMind |
| 收盤 | 47,111.26 | 點 | TWSE OpenAPI MI_INDEX (備援) |
| 漲跌點數 | 141.39 | 點 | TWSE OpenAPI MI_INDEX (備援) |
| 漲跌幅 | +0.30 | % | TWSE OpenAPI MI_INDEX (備援) |
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
| 外資 | -767.4 | 億元 | twse-proxy /institutional |
| 投信 | +241.4 | 億元 | twse-proxy /institutional |
| 自營商 | -362.6 | 億元 | twse-proxy /institutional |
| 三大法人合計 | -888.6 | 億元 | twse-proxy /institutional |

### 4. 融資融券

**資料來源：** 上市+上櫃 `HiStock` (金額口徑)；維持率 `istock.tw`；備援官方逐股加總

| 項目 | 數值 | 單位 | 資料來源 |
|---|---|---|---|
| 融資餘額 | unavailable | 億元 | HiStock |
| 融資增減 | unavailable | 億元 | HiStock |
| 融券餘額 | 233,602 | 張 | HiStock |
| 融券增減 | 9,022 | 張 | HiStock |
| 融資維持率 | 183.39 | % | 前值遞補 (DATA 2026-10-16；當日三源皆失敗；民間估算；官方無每日序列) |

### 5. 借券資料

**資料來源：** 上市 `TWSE OpenAPI TWT96U` (可借餘額)、上櫃 `TPEX OpenAPI tpex_margin_sbl`

| 項目 | 數值 | 單位 | 資料來源 |
|---|---|---|---|
| 借券餘額 | 2,423,260 | 張 | TWSE TWT93U + TPEX margin_sbl |
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
| S&P 500 | ^GSPC | 7,702.42 | 42.98 | +0.56 | Yahoo Finance Chart API |
| Nasdaq Composite | ^IXIC | 26,479.60 | 339.57 | +1.30 | Yahoo Finance Chart API |
| Nasdaq 100 | ^NDX | 29,602.73 | 415.18 | +1.42 | Yahoo Finance Chart API |
| Dow Jones | ^DJI | 52,005.20 | 2.79 | +0.01 | Yahoo Finance Chart API |
| 費城半導體 SOX | ^SOX | 11,394.95 | 257.66 | +2.31 | Yahoo Finance Chart API |
| VIX | ^VIX | 18.44 | -1.55 | -7.75 | Yahoo Finance Chart API |

### 2. 亞洲主要指數

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 收盤／最新值 | 漲跌點 | 漲跌幅 | 資料來源 |
|---|---|---|---|---|---|
| 日經225 | ^N225 | 65,324.29 | 898.34 | +1.39 | Yahoo Finance Chart API |
| 韓國KOSPI | ^KS11 | 5,668.05 | 113.83 | +2.05 | Yahoo Finance Chart API |
| 香港恆生 | ^HSI | 24,186.83 | 124.11 | +0.52 | Yahoo Finance Chart API |
| 上海綜合 | 000001.SS | 3,716.28 | 8.81 | +0.24 | Yahoo Finance Chart API |
| 深圳成分 | 399001.SZ | 11,802.46 | -14.33 | -0.12 | Yahoo Finance Chart API |

### 3. 美股指數期貨

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 最新值 | 漲跌點 | 漲跌幅 | 資料來源 |
|---|---|---|---|---|---|
| S&P500期貨 | ES=F | 7,746.00 | 41.75 | +0.54 | Yahoo Finance Chart API |
| Nasdaq100期貨 | NQ=F | 29,806.00 | 414.50 | +1.41 | Yahoo Finance Chart API |
| 道瓊期貨 | YM=F | 52,204.00 | -10.00 | -0.02 | Yahoo Finance Chart API |
| Russell2000期貨 | RTY=F | 2,744.60 | 9.10 | +0.33 | Yahoo Finance Chart API |

### 4. 美國國債殖利率

**資料來源：** `U.S. Treasury Fiscal Data API` (失敗時備援 Treasury yield.xml 與 `Yahoo Finance`)

| 項目 | API 資料欄位／識別 | 殖利率 | 日變化 | 資料來源 |
|---|---|---|---|---|
| 美國 2 年期殖利率 | 2 Yr | 4.74 | -0.03 | U.S. Treasury yield.xml (網頁備援) |
| 美國 10 年期殖利率 | 10 Yr | 5.15 | 0.05 | Yahoo Finance (備援) |
| 美國 30 年期殖利率 | 30 Yr | 5.48 | 0.05 | Yahoo Finance (備援) |

### 5. 主要匯率

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 最新值 | 漲跌點 | 漲跌幅 | 資料來源 |
|---|---|---|---|---|---|
| USD/TWD | TWD=X | 32.47 | 0.15 | +0.45 | Yahoo Finance Chart API |
| DXY美元指數 | DX-Y.NYB | 101.99 | 0.15 | +0.14 | Yahoo Finance Chart API |
| USD/JPY | JPY=X | 158.49 | 0.35 | +0.22 | Yahoo Finance Chart API |
| USD/KRW | KRW=X | 1,332.13 | -8.82 | -0.66 | Yahoo Finance Chart API |

### 6. 台灣相關ADR

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 收盤／最新值 | 漲跌點 | 漲跌幅 | 資料來源 |
|---|---|---|---|---|---|
| 台積電ADR | TSM | 422.00 | 9.39 | +2.28 | Yahoo Finance Chart API |
| 聯電ADR | UMC | 20.19 | 0.37 | +1.87 | Yahoo Finance Chart API |
| 日月光ADR | ASX | 40.72 | 1.19 | +3.00 | Yahoo Finance Chart API |

### 7. 原油黃金Bitcoin

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 收盤／最新值 | 漲跌點 | 漲跌幅 | 資料來源 |
|---|---|---|---|---|---|
| WTI原油期貨 | CL=F | 99.12 | -2.29 | -2.26 | Yahoo Finance Chart API |
| 黃金期貨 | GC=F | 4,157.50 | -23.60 | -0.56 | Yahoo Finance Chart API |
| Bitcoin | BTC-USD | 81,956.04 | -61.56 | -0.08 | Yahoo Finance Chart API |

### 8. 重大經濟數據、央行事件與重大市場新聞

**資料來源：** 台股 `tw.stock.yahoo.com` (含內文摘要)；國際 `Fed 公告 RSS`＋`CNBC`＋`MarketWatch` (標題、來源、時間與連結)

- 事件1：外資連九賣台股收黑 富喬漲停領玻纖布抗空襲
  - 來源：Yahoo 台股；發布時間：2026-10-19T09:34:20Z；台北時間：2026-10-19 17:34
  - 摘要：台積電尾盤撐場，台股跌勢收斂、守住季線！今(19)日加權指數終場下跌289.18點、跌幅0.61%，收46,822.08點，失守4萬7關卡，成交金額8,262.64億元。大盤盤中一度重挫941點、下探46,170點，隨低接買盤進場，逐步收復
  - 原文連結：https://tw.stock.yahoo.com/news/%E5%A4%96%E8%B3%87%E9%80%A3%E4%B9%9D%E8%B3%A3%E7%BA%8C%E7%A0%8D767%E5%84%84%E5%8F%B0%E8%82%A1%E5%B0%BE%E7%9B%A4%E6%8B%89%E5%9B%9E%E4%BB%8D%E5%A4%B147k%EF%BC%81%E5%AF%8C%E5%96%AC%E6%BC%B2%E5%81%9C%E8%A1%9D%E5%A4%A9%E5%83%B9%E9%A0%98%E7%8E%BB%E7%BA%96%E5%B8%83%E6%92%90%E8%B5%B7%E3%80%8C%E6%8A%97%E8%B7%8C%E7%B6%B2%E3%80%8D%EF%BD%9Cyahoo%E8%B2%A1%E7%B6%93%E6%8E%83%E6%8F%8F-093420852.html
- 事件2：5檔ETF換股大風吹 國巨富邦金國泰金被請下車
  - 來源：Yahoo 台股；發布時間：2026-10-19T10:04:21Z；台北時間：2026-10-19 18:04
  - 摘要：台灣指數公司今（19）日公布最新指數定期審核結果，共有 00905、00881、00935、00701 及 00733 等 5 檔熱門台股 ETF 進行成分股調整，最高一次替換超過40檔。其中00701將富邦金、國泰金等大型金控全數剔除，0
  - 原文連結：https://tw.stock.yahoo.com/news/64%E8%90%AC%E5%A4%9A%E4%BA%BA%E6%B3%A8%E6%84%8F%EF%BC%815%E6%AA%94%E5%8F%B0%E8%82%A1etf%E6%8F%9B%E8%82%A1-%E5%9C%8B%E5%B7%A8%E3%80%81%E5%AF%8C%E9%82%A6%E9%87%91%E3%80%81%E5%9C%8B%E6%B3%B0%E9%87%91%E7%AD%89%E8%A2%AB%E8%B8%A2-100421858.html
- 事件3：璞玉指數擴編至394檔 重電四雄報到統一亞泥出局
  - 來源：Yahoo 台股；發布時間：2026-10-19T10:56:18Z；台北時間：2026-10-19 18:56
  - 摘要：台灣指數公司今（19）日公布最新「臺灣璞玉指數」定期審核結果，調整自本日收盤後正式生效。本次成分股調整呈現「大換血」態勢，計納入東元等129 檔、刪除統一、亞泥、遠東新等66 檔成分股。
  - 原文連結：https://tw.stock.yahoo.com/news/%E7%92%9E%E7%8E%89%E6%8C%87%E6%95%B8%E5%A4%A7%E6%8F%9B%E8%A1%80%EF%BC%81%E3%80%8C129%E9%80%B266%E5%87%BA%E3%80%8D-%E4%BA%9E%E6%B3%A5%E3%80%81%E9%81%A0%E6%9D%B1%E6%96%B0%E3%80%81%E7%B5%B1%E4%B8%80%E9%81%AD%E8%B8%A2-105618843.html
- 事件4：台股回測季線郭哲榮仍看多 喊年底五萬點發祭品文
  - 來源：Yahoo 台股；發布時間：2026-10-19T10:27:00Z；台北時間：2026-10-19 18:27
  - 摘要：美股受通膨與AI疑慮拖累，台股近日回測季線，摩爾投顧投資長郭哲榮發下豪語，若年底台股未攻上5萬點將發放5千份雞排。面對台股重挫，郭哲榮認為第四季最佳買點就在本週，預期美伊衝突有望緩解，看好精材、環球晶、中美晶及微星等個股表現，並重申三年內台
  - 原文連結：https://tw.stock.yahoo.com/news/%E9%A0%90%E8%A8%80%E5%8F%B0%E8%82%A1%E5%B9%B4%E5%BA%955%E8%90%AC%E9%BB%9E-%E9%83%AD%E5%93%B2%E6%A6%AE%E7%99%BC%E7%A5%AD%E5%93%81%E6%96%87-%E6%B2%92%E7%A0%B4%E7%99%BC%E9%9B%9E%E6%8E%925%E5%8D%83%E4%BB%BD-102700709.html
- 事件5：鴻海砸236億入股三菱電機 布局電動車拚IPO
  - 來源：Yahoo 台股；發布時間：2026-10-19T09:28:11Z；台北時間：2026-10-19 17:28
  - 摘要：[非凡新聞]記者許佑娟,攝影陳昱志鴻海搶攻電動車市場，再有新動作，宣布斥資1150億日圓，折合台幣約236億元，取得三菱電機50%股權，今（19）日在雙方在東京舉行記者會，透露未來若營運達到預期目標，也將考慮推動IPO...
  - 原文連結：https://tw.stock.yahoo.com/news/%E9%B4%BB%E6%B5%B71150%E5%84%84%E6%97%A5%E5%9C%93%E5%85%A5%E8%82%A1%E4%B8%89%E8%8F%B1-%E5%B8%83%E5%B1%80%E9%9B%BB%E5%8B%95%E8%BB%8A%E6%8B%9Aipo-092811016.html
- 事件6：瑤池金母挑戰者來了？這檔新主動式ETF將掛牌　專家曝操盤者是「九倍女股神」：績效曾贏陳釧瑤
  - 來源：Yahoo 台股；發布時間：2026-10-19T15:07:46Z；台北時間：2026-10-19 23:07
  - 摘要：ETF是不少台股投資人的偏好，其中除了追蹤指數的被動式ETF，主動式ETF也備受關注，而主打「零配息」的復華台灣新星主動式ETF（00418A）即將掛牌，也引起市場注意。對此，本名許凱廸的財經作家阿格力直言，00418A的經理人在媒體上被號
  - 原文連結：https://tw.stock.yahoo.com/news/%E7%91%A4%E6%B1%A0%E9%87%91%E6%AF%8D%E6%8C%91%E6%88%B0%E8%80%85%E4%BE%86%E4%BA%86-%E9%80%99%E6%AA%94%E6%96%B0%E4%B8%BB%E5%8B%95%E5%BC%8Fetf%E5%B0%87%E6%8E%9B%E7%89%8C-%E5%B0%88%E5%AE%B6%E6%9B%9D%E6%93%8D%E7%9B%A4%E8%80%85%E6%98%AF-%E4%B9%9D%E5%80%8D%E5%A5%B3%E8%82%A1%E7%A5%9E-%E7%B8%BE%E6%95%88%E6%9B%BE%E8%B4%8F%E9%99%B3%E9%87%A7%E7%91%A4-150746066.html
- 事件7：Federal Reserve Board announces termination of enforcement actions with Gardner Bancshares, Inc. and Small Business Bank
  - 來源：Federal Reserve；發布時間：Fri, 16 Oct 2026 15:00:00 GMT；台北時間：2026-10-16 23:00
  - 摘要：Federal Reserve Board announces termination of enforcement actions with Gardner Bancshares, Inc. and Small Business Bank
  - 原文連結：https://www.federalreserve.gov/newsevents/pressreleases/enforcement20261016a.htm
- 事件8：OpenAI bugging suspect's conduct could pose danger to U.S. national security, feds warn
  - 來源：CNBC；發布時間：Mon, 19 Oct 2026 15:10:54 GMT；台北時間：2026-10-19 23:10
  - 摘要：Saudi national Abdulrahman Alfozan is accused of planting a recording device in an executive conference room at OpenAI headquarters in San Francisco.
  - 原文連結：https://www.cnbc.com/2026/10/19/openai-bugging-suspect-alfozan-saudi-royal-family.html
- 事件9：French unrest compounds debt crisis fears. Paris-listed stocks, bonds and the euro fall
  - 來源：CNBC；發布時間：Mon, 19 Oct 2026 12:59:13 GMT；台北時間：2026-10-19 20:59
  - 摘要："It looks like either the bond markets riot, or the people riot, or both," one analyst told CNBC.
  - 原文連結：https://www.cnbc.com/2026/10/19/france-protests-bond-yields-markets.html
- 事件10：Indonesian stocks plunge to six-year low as MSCI downgrade fears mount
  - 來源：CNBC；發布時間：Mon, 19 Oct 2026 03:00:33 GMT；台北時間：2026-10-19 11:00
  - 摘要：Indonesia's benchmark stock index plunged to its lowest level in six years.
  - 原文連結：https://www.cnbc.com/2026/10/19/indonesian-stocks-msci-downgrade-fears-mount.html
- 事件11：Micron and other chip stocks spring back to life after bruising selloff
  - 來源：MarketWatch；發布時間：Mon, 19 Oct 2026 16:59:00 GMT；台北時間：2026-10-20 00:59
  - 摘要：It&#x2019;s a key week for tech stocks as Nvidia gears up for a European conference and Meta prepares to report earnings.
  - 原文連結：https://www.marketwatch.com/story/micron-and-other-chip-stocks-spring-back-to-life-after-bruising-selloff-16486541?mod=mw_rss_topstories


## 三、期貨

**資料來源：**
1. Cloudflare Workers：TAIFEX Proxy — https://taifex.grichtoyang.workers.dev/
2. TAIFEX Open API — https://openapi.taifex.com.tw/

近月契約月份：202610 (日盤成交量最大者)；交易日期：2026-10-20

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
| 前十大交易人多方 OI | 75,382 | TAIFEX Proxy |
| 前十大交易人空方 OI | 72,888 | TAIFEX Proxy |
| 前十大交易人多空淨 OI | +2,494 | TAIFEX Proxy |
| 多空淨 OI 變化 (2026-10-16→2026-10-16) | +0 | TAIFEX Proxy snapshots (2026-10-19) |
- 資料日期：2026-10-16 (TypeOfTraders=0 全部交易人；契約月份 202610)

### 5．日盤、夜盤法人交易資料

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 外資日盤多單交易量 | 101,671 | TAIFEX Proxy |
| 外資日盤空單交易量 | 99,130 | TAIFEX Proxy |
| 外資日盤多空淨交易量 | +2,541 | TAIFEX Proxy |
| 外資夜盤多單交易量 | unavailable | TAIFEX Proxy |
| 外資夜盤空單交易量 | unavailable | TAIFEX Proxy |
| 外資夜盤多空淨交易量 | unavailable | TAIFEX Proxy |
| 外資日盤／夜盤交易量變化 | unavailable | TAIFEX Proxy |
| 投信日盤多空淨交易量 | +1,576 | TAIFEX Proxy |
| 投信夜盤多空淨交易量 | unavailable | TAIFEX Proxy |
| 投信日盤／夜盤交易量變化 | unavailable | TAIFEX Proxy |
| 自營商日盤多空淨交易量 | -197 | TAIFEX Proxy |
| 自營商夜盤多空淨交易量 | unavailable | TAIFEX Proxy |
| 自營商日盤／夜盤交易量變化 | unavailable | TAIFEX Proxy |
| 三大法人日盤多空淨交易量 | +3,920 | TAIFEX Proxy |
| 三大法人夜盤多空淨交易量 | unavailable | TAIFEX Proxy |
| 法人日盤交易金額淨額 (億元) | +367.1 | TAIFEX Proxy |
| 法人夜盤交易金額淨額 (億元) | unavailable | TAIFEX Proxy |

### 6．期貨與現貨關係

| 項目 | 數值 | 資料來源 |
|---|---|---|
| 台指期近月價格 | 46,779 | TAIFEX Proxy |
| 加權指數價格 | 47,111.26 | TWSE OpenAPI MI_INDEX (備援) |
| 台指期與加權指數價差 | -332.26 | TAIFEX Proxy+TWSE OpenAPI MI_INDEX (備援) |
| 價差百分比 | -0.71 | TAIFEX Proxy+TWSE OpenAPI MI_INDEX (備援) |
| 日盤基差 | -332.26 | TAIFEX Proxy+TWSE OpenAPI MI_INDEX (備援) |
| 夜盤價格相對日盤收盤的變化 | unavailable | 端點未提供 |

### 7．日盤、夜盤與籌碼變化對照

#### 7.1 日夜盤價格與成交量對照 (變化 = 日盤 - 夜盤)

| 項目 | 日盤 | 夜盤 | 變化 (日-夜) | 資料來源 |
|---|---|---|---|---|
| 收盤價 | 46,779 | unavailable | unavailable | TAIFEX Proxy |
| 成交量 | 101,828 | unavailable | unavailable | TAIFEX Proxy |
- 台指期總 OI 前日變化：+0（來源：TAIFEX Proxy）


#### 7.2 法人籌碼日夜盤對照 (淨變化 = 日盤淨 - 夜盤淨；OI 為日盤收盤後總量，前日變化另列)

| 法人 | 交易量 |  |  |  |  |  |  | 未平倉量 |  |  |  | 資料來源 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|  | **日盤多單** | **日盤空單** | **日盤淨** | **夜盤多單** | **夜盤空單** | **夜盤淨** | **淨變化 (日-夜)** | **OI多方** | **OI空方** | **OI淨** | **OI前日變化** |  |
| 外資 | 101,671 | 99,130 | +2,541 | unavailable | unavailable | unavailable | unavailable | unavailable | unavailable | unavailable | unavailable | TAIFEX Proxy |
| 投信 | 42,112 | 40,536 | +1,576 | unavailable | unavailable | unavailable | unavailable | unavailable | unavailable | unavailable | unavailable | TAIFEX Proxy |
| 自營商 | 12,961 | 13,158 | -197 | unavailable | unavailable | unavailable | unavailable | unavailable | unavailable | unavailable | unavailable | TAIFEX Proxy |
| 三大法人合計 | 156,744 | 152,824 | +3,920 | unavailable | unavailable | unavailable | unavailable | 0 | 0 | +0 | +0 | TAIFEX Proxy |

#### 7.3 前十大交易人日夜盤對照 (OI 無日夜拆分，列收盤後總量)

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 前十大交易人多方 OI | 75,382 | TAIFEX Proxy |
| 前十大交易人空方 OI | 72,888 | TAIFEX Proxy |
| 前十大交易人多空淨 OI | +2,494 | TAIFEX Proxy |
| 前十大交易人多空淨 OI 變化 (2026-10-16→2026-10-16) | +0 | TAIFEX Proxy snapshots (2026-10-19) |

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
| 交易日期 | 2026-10-20 | TAIFEX Proxy |
| 到期月份／到期日 | 202610 | TAIFEX Proxy |
| 資料更新時間 | 2026-10-20 01:28:08 | 本機 |
| 日盤／夜盤標記 | 日盤收盤後資料 | TAIFEX Proxy |

### 2．Call 總成交量、OI、OI 增減

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Call 總成交量 | 182,637 | TAIFEX Proxy |
| Call 總未平倉量 OI | 93,892 | TAIFEX Proxy |
| Call OI 增減 (2026-10-19→2026-10-20) | +0 | TAIFEX Proxy snapshots (2026-10-19) |

### 3．Put 總成交量、OI、OI 增減

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Put 總成交量 | 176,987 | TAIFEX Proxy |
| Put 總未平倉量 OI | 55,248 | TAIFEX Proxy |
| Put OI 增減 (2026-10-19→2026-10-20) | +0 | TAIFEX Proxy snapshots (2026-10-19) |

### 4．Call／Put 比例與變化

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Call／Put 成交量比例 | 1.03 | TAIFEX Proxy |
| Call／Put 未平倉量比例 | 1.70 | TAIFEX Proxy |
| Put／Call Ratio | 0.59 | TAIFEX Proxy |
| Call／Put 比例變化 (量比 2026-10-15→2026-10-16) | 13.76 | TAIFEX Proxy |
| 與前一交易日比較 (OI 比 2026-10-15→2026-10-16) | 6.76 | TAIFEX Proxy |
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
| 外資 Call夜買 | 26,248 | TAIFEX Proxy |
| 外資 Call夜賣 | 26,357 | TAIFEX Proxy |
| 外資 Call夜淨 | -109 | TAIFEX Proxy |
| 外資 Put夜買 | 26,085 | TAIFEX Proxy |
| 外資 Put夜賣 | 25,181 | TAIFEX Proxy |
| 外資 Put夜淨 | +904 | TAIFEX Proxy |
| 外資 日盤淨總量 | +616 | TAIFEX Proxy |
| 外資 Call日夜淨增減 (日－夜) | +1,635 | TAIFEX Proxy |
| 外資 Put日夜淨增減 (日－夜) | +6 | TAIFEX Proxy |

### 6．自營商 Call／Put 部位

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 自營商 Call日買 | 56,571 | TAIFEX Proxy |
| 自營商 Call日賣 | 52,550 | TAIFEX Proxy |
| 自營商 Call日淨 | +4,021 | TAIFEX Proxy |
| 自營商 Put日買 | 51,580 | TAIFEX Proxy |
| 自營商 Put日賣 | 51,005 | TAIFEX Proxy |
| 自營商 Put日淨 | +575 | TAIFEX Proxy |
| 自營商 Call夜買 | 23,084 | TAIFEX Proxy |
| 自營商 Call夜賣 | 23,366 | TAIFEX Proxy |
| 自營商 Call夜淨 | -282 | TAIFEX Proxy |
| 自營商 Put夜買 | 18,090 | TAIFEX Proxy |
| 自營商 Put夜賣 | 20,527 | TAIFEX Proxy |
| 自營商 Put夜淨 | -2,437 | TAIFEX Proxy |
| 自營商 日盤淨總量 | +3,446 | TAIFEX Proxy |
| 自營商 Call日夜淨增減 (日－夜) | +4,303 | TAIFEX Proxy |
| 自營商 Put日夜淨增減 (日－夜) | +3,012 | TAIFEX Proxy |

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
| 與前一交易日的變化 (2026-10-19→2026-10-20) | +0 | TAIFEX Proxy snapshots (2026-10-19) |

### 12．Put Wall

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Put Wall 價位 | 45,000 | TAIFEX Proxy |
| 對應到期月份 | 202610 | TAIFEX Proxy |
| 與前一交易日的變化 (2026-10-19→2026-10-20) | +0 | TAIFEX Proxy snapshots (2026-10-19) |

### 13．Gamma Wall

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Gamma Wall 價位 | unavailable | 端點未提供 |
| 對應到期月份 | 202610 | TAIFEX Proxy |
| 資料日期 | unavailable | 端點未提供 |

### 14．Gamma Flip

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Gamma Flip 價位 | unavailable | 端點未提供 |
| 對應到期月份 | 202610 | TAIFEX Proxy |
| 資料日期 | unavailable | 端點未提供 |

### 15．Max Pain

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Max Pain 價位 | 46,500 | TAIFEX Proxy |
| 對應到期月份 | 202610 | TAIFEX Proxy |
| 與前一交易日的變化 (2026-10-19→2026-10-20) | +0 | TAIFEX Proxy snapshots (2026-10-19) |

### 17．選擇權法人日盤、夜盤交易

| 法人 | 日盤多單 | 日盤空單 | 日盤淨 | 夜盤多單 | 夜盤空單 | 夜盤淨 | 淨變化 (日-夜) | 資料來源 |
|---|---|---|---|---|---|---|---|---|
| 外資 | 116,731 | 116,115 | +616 | unavailable | unavailable | unavailable | unavailable | TAIFEX Proxy |
| 投信 | 40 | 3,100 | -3,060 | unavailable | unavailable | unavailable | unavailable | TAIFEX Proxy |
| 自營商 | 107,576 | 104,130 | +3,446 | unavailable | unavailable | unavailable | unavailable | TAIFEX Proxy |
| 三大法人合計 | 224,347 | 223,345 | +1,002 | unavailable | unavailable | unavailable | unavailable | TAIFEX Proxy |
- 方法論：多方＝買Call＋賣Put（看多），空方＝賣Call＋買Put（看空），淨額＝看多－看空（已用 Call／Put 拆分頁交叉驗算一致）
- 公式：多方(買)－空方(賣)＝（買call＋賣put）－（賣call＋買put）＝看多－看空
- 速記：多＝BC＋SP、空＝SC＋BP

#### 法人多空力道表（金額・億元；上游千元／1e5）

| 法人 | 日多方力道 | 日空方力道 | 日淨多空力道 | 夜多方力道 | 夜空方力道 | 夜淨多空力道 | 日淨－夜淨 | 資料來源 |
|---|---|---|---|---|---|---|---|---|
| 外資 | 13.52 | 13.28 | +0.24 | 6.01 | 6.03 | -0.01 | +0.25 | TAIFEX Proxy |
| 投信 | 0.00 | 2.76 | -2.76 | 0.00 | 0.00 | +0 | -2.76 | TAIFEX Proxy |
| 自營商 | 12.10 | 10.51 | +1.59 | 4.75 | 4.32 | +0.43 | +1.16 | TAIFEX Proxy |
| 三大法人合計 | 25.62 | 26.55 | -0.93 | 10.76 | 10.35 | +0.41 | -1.35 | TAIFEX Proxy |

### 18．選擇權前十大

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 買權多方 OI | 35,177 | TAIFEX Proxy |
| 買權空方 OI | 40,526 | TAIFEX Proxy |
| 買權多空淨 OI | -5,349 | TAIFEX Proxy |
| 買權多空淨 OI 變化 (2026-10-16→2026-10-16) | +0 | TAIFEX Proxy snapshots (2026-10-19) |

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 賣權多方 OI | 19,028 | TAIFEX Proxy |
| 賣權空方 OI | 15,749 | TAIFEX Proxy |
| 賣權多空淨 OI | +3,279 | TAIFEX Proxy |
| 賣權多空淨 OI 變化 (2026-10-16→2026-10-16) | +0 | TAIFEX Proxy snapshots (2026-10-19) |
- 資料日期：買權 2026-10-16／賣權 2026-10-16 (TypeOfTraders=0 全部交易人；契約月份 202610)

#### 大戶流向（全日；前十大無日夜拆分）

| 項目 | 淨變化 | 區間 | 資料來源 |
|---|---|---|---|
| 期貨前十大 | +0 | 2026-10-16→2026-10-16 | TAIFEX Proxy snapshots (2026-10-19) |
| 買權前十大 | +0 | 2026-10-16→2026-10-16 | TAIFEX Proxy snapshots (2026-10-19) |
| 賣權前十大 | +0 | 2026-10-16→2026-10-16 | TAIFEX Proxy snapshots (2026-10-19) |

### 16．資料來源、時間、時區與狀態

- 資料來源：TAIFEX 經 Cloudflare Worker Proxy
- 資料日期：2026-10-20；資料時間：2026-10-20 01:28:08；時區：`Asia/Taipei`
- 日盤／夜盤標記：日盤收盤後 + 夜盤盤後
- 未取得欄位 (22)：taiex.open, taiex.high, taiex.low, listed_breadth.up, listed_breadth.down, listed_breadth.flat, listed_breadth.limit_up, listed_breadth.limit_down, otc_breadth.up, otc_breadth.down, otc_breadth.flat, otc_breadth.limit_up, otc_breadth.limit_down, margin.fin_yi, margin.fin_chg_yi, sbl.sale_bal, sbl.sale_chg, turnover.listed, turnover.otc, turnover.total, futures.gamma_wall, futures.gamma_flip
- 註記：無日期端點為最新盤勢快照 (判定資料日期 2026-10-19，非 T0 2026-10-20)，適用：日盤價／法人交易／夜盤／選擇權法人；T0 相符時不另標註
- 註記：futures-price-after-hours 日期 2026-10-19 非今日 2026-10-20，視為無新節次，不採用
- 註記：futures-institutional-after-hours 日期 2026-10-19 非今日 2026-10-20，視為無新節次，不採用
- 註記：options-institutional-after-hours 日期 2026-10-19 非今日 2026-10-20，視為無新節次，不採用
- 註記：Call/Put Wall 與 Max Pain 資料日期 2026-10-19 (T0 2026-10-20 端點不穩，採最新可得)
- 註記：夜盤開高低收未取得 (proxy 與官方皆無)，僅成交量/OI/結算價
- 註記：法人 OI 未取得
- 註記：法人交易量變化無昨日交易端點，標 unavailable
- 註記：選擇權 chain 資料日期 2026-10-19 (T0 2026-10-20 端點不穩，採最新可得)
- 註記：Gamma Wall/Flip 無資料 (proxy 端點上游無資料)，標 unavailable

## 五、資料來源、時間與完整性

- 期貨/匯率為最新報價，其餘為 T0 收盤資料；時間皆為 `Asia/Taipei`。
- taiex：`TWSE OpenAPI MI_INDEX (備援)`
- listed_breadth：`twse-proxy`
- listed_turnover：`twse-proxy market_statistics`
- institutional：`twse-proxy /institutional`
- margin_short：`TWSE MI_MARGN + TPEX margin_balance (張)`
- margin_ratio：`前值遞補 (DATA 2026-10-16；當日三源皆失敗；民間估算；官方無每日序列)`
- sbl：`TWSE TWT93U + TPEX margin_sbl`
- 期貨選擇權：`TAIFEX Proxy`
- 新聞：台股 Yahoo／國際 Fed＋CNBC＋MarketWatch；台股 Yahoo（不足時財訊快報備援）/ 國際 Fed 公告＋CNBC＋MarketWatch RSS；Fed 無摘要；investing 港股為主已退役；cnyes CSR、wantgoo JS 算繪、中央社/台灣央行路徑待查，未採用
- 美股/亞股/期貨/匯率/ADR/商品：`Yahoo Finance Chart API`；美債：`Yahoo Finance (備援)`
- 註記：亞洲指數與前份 DATA (DATA_REPORT_20261016.md) 完全相同，疑似 Yahoo 未更新，僅參考不解讀方向
- 註記：twse-proxy taiex 缺值，改用 MI_INDEX 備援
- 註記：大盤開高低未取得 (FinMind 失敗；MI_INDEX 無此欄)
- 註記：twtazu_od 備援日期不符 (回傳舊資料)，上市漲跌標 unavailable
- 註記：上櫃 highlight 日期不符或缺值 (回傳 1151019, T0=1151020)
- 註記：三大法人回傳日期 20261019 (T0 20261020)，採用最新可得
- 註記：HiStock 未取得，融資餘額/增減標 unavailable (官方逐股加總僅有張數)
- 註記：融券沿用官方逐股加總 (張)
- 註記：融資維持率未取得 (三源皆失敗；官方無每日序列)
- 註記：融資維持率採前值遞補 (DATA 2026-10-16)，非 T0 2026-10-20
- 註記：上市 MI_MARGN / TWT96U 無日期欄，採用最新可得
- 本報告僅整理資料，不提供交易判斷。

## 六、期現選方向對照

**規則：** 趨勢偏多／空＝現貨、期貨OI、選擇權日淨三者同向；避險／對沖＝現貨與期選反向；日內反轉＝日淨與夜淨反向；缺值標示，不推估。選擇權多空為看多看空口徑。

| 法人 | 現貨買賣超(億) | 期貨OI淨(口) | 期貨日淨 | 期貨夜淨 | 選擇權日淨 | 選擇權夜淨 | 判定 | 期選組合 | 資料來源 |
|---|---|---|---|---|---|---|---|---|---|
| 外資 | -767.4 | unavailable | +2,541 | unavailable | +616 | unavailable | 資料不足 | 資料不足 | twse-proxy／TAIFEX Proxy |
| 投信 | +241.4 | unavailable | +1,576 | unavailable | -3,060 | unavailable | 資料不足 | 資料不足 | twse-proxy／TAIFEX Proxy |
| 自營商 | -362.6 | unavailable | -197 | unavailable | +3,446 | unavailable | 資料不足 | 資料不足 | twse-proxy／TAIFEX Proxy |
