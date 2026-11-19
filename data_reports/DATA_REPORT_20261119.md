# DATA_REPORT_20261119

- 報告日期：`2026-11-19`
- T0 交易日期：`2026-11-19`
- 首次資料產出時間：`2026-11-19 13:51:44`
- 本次更新開始時間：`2026-11-19 13:51:44`
- 時區：`Asia/Taipei`
- 產出盤別：`日盤`
- 產出者：`actions`
- 排定班別：`manual`

---

## 一、現貨

### 1. 台股大盤行情

**資料來源：** `Cloudflare Worker：twse-proxy` (備援 `TWSE OpenAPI MI_INDEX`)

| 項目 | 數值 | 單位 | 資料來源 |
|---|---|---|---|
| 加權指數 | 38,426.89 | 點 | twse-proxy |
| 開盤 | unavailable | 點 | unavailable |
| 最高 | unavailable | 點 | unavailable |
| 最低 | unavailable | 點 | unavailable |
| 收盤 | 38,426.89 | 點 | twse-proxy |
| 漲跌點數 | -1,768.02 | 點 | twse-proxy |
| 漲跌幅 | -4.40 | % | twse-proxy |
| 成交金額 | 8,952.8 | 億元 | twse-proxy market_statistics |

### 2. 市場漲跌家數

#### 2.1 上市公司

**資料來源：** `Cloudflare Worker：twse-proxy` (備援 `TWSE OpenAPI twtazu_od`)

| 項目 | 家數 | 資料來源 |
|---|---|---|
| 上漲家數 | 67 | twse-proxy |
| 下跌家數 | 993 | twse-proxy |
| 平盤家數 | 25 | twse-proxy |
| 漲停家數 | 1 | twse-proxy |
| 跌停家數 | 128 | twse-proxy |

#### 2.2 上櫃公司

**資料來源：** `TPEX OpenAPI tpex_mainborad_highlight`

| 項目 | 家數 | 資料來源 |
|---|---|---|
| 上漲家數 | unavailable | unavailable |
| 下跌家數 | unavailable | unavailable |
| 平盤家數 | unavailable | unavailable |
| 漲停家數 | unavailable | unavailable |
| 跌停家數 | unavailable | unavailable |

### 3. 三大法人現貨買賣超

**資料來源：** `unavailable`

| 法人別 | 買賣超金額 | 單位 | 資料來源 |
|---|---|---|---|
| 外資 | unavailable | 億元 | unavailable |
| 投信 | unavailable | 億元 | unavailable |
| 自營商 | unavailable | 億元 | unavailable |
| 三大法人合計 | unavailable | 億元 | unavailable |

### 4. 融資融券

**資料來源：** 上市+上櫃 `unavailable` (金額口徑)；維持率 `unavailable`；官方無每日維持率序列

| 項目 | 數值 | 單位 | 資料來源 |
|---|---|---|---|
| 融資餘額 | unavailable | 億元 | unavailable |
| 融資增減 | unavailable | 億元 | unavailable |
| 融券餘額 | unavailable | 張 | unavailable |
| 融券增減 | unavailable | 張 | unavailable |
| 融資維持率 | unavailable | % | unavailable |

### 5. 借券資料

**資料來源：** 各欄位依實際取得市場分別標示；借券賣出餘額／增減使用上市 TWT93U 與上櫃 tpex_margin_sbl，缺值市場不納入加總。

| 項目 | 數值 | 單位 | 資料來源 |
|---|---|---|---|
| 整體市場借券餘額 | unavailable | 張 | unavailable |

| 項目 | 上市 | 上櫃 | 兩者合計 | 單位 |
|---|---|---|---|---|
| 借券賣出餘額 | unavailable | unavailable | unavailable | 張 |
| 借券賣出增減 | unavailable | unavailable | unavailable | 張 |

- 上市來源：unavailable；增減來源：unavailable
- 上櫃來源：unavailable；增減來源：unavailable
- 借券賣出餘額完整性：`unavailable`
- 借券賣出增減完整性：`unavailable`
- TWSE TWT93U（上市）：資料日期：`20261119`；最後預定更新：`23:30`；來源回報產製時間：`unavailable`；本次查詢時間：`2026-11-19T13:52:02+08:00`；狀態：`pending`
- TPEx S47（上櫃）：資料日期：`20261119`；最後預定更新：`22:30`；來源回報產製時間：`unavailable`；本次查詢時間：`2026-11-19T13:52:03+08:00`；狀態：`pending`

### 6. 市場成交結構

**資料來源：** 上市 `twse-proxy market_statistics`、上櫃 `unavailable`

| 項目 | 成交金額 | 單位 | 資料來源 |
|---|---|---|---|
| 上市成交金額 | 8,952.8 | 億元 | twse-proxy market_statistics |
| 上櫃成交金額 | unavailable | 億元 | unavailable |
| 上市櫃成交金額合計 | unavailable | 億元 | unavailable |

## 二、重要市場

### 1. 美股指數

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 收盤／最新值 | 漲跌值 | 漲跌幅 | 資料日期（交易所時區） | 擷取時間（UTC） | 交易所時區 | 資料來源 |
|---|---|---|---|---|---|---|---|---|
| S&P 500 | ^GSPC | 7,323.63 | -16.90 | -0.23 | 2026-11-18 | 2026-11-19T05:52:05+00:00 | America/New_York | Yahoo Finance Chart API |
| Nasdaq Composite | ^IXIC | 24,429.88 | 101.50 | +0.42 | 2026-11-18 | 2026-11-19T05:52:05+00:00 | America/New_York | Yahoo Finance Chart API |
| Nasdaq 100 | ^NDX | 27,116.26 | 114.48 | +0.42 | 2026-11-18 | 2026-11-19T05:52:05+00:00 | America/New_York | Yahoo Finance Chart API |
| Dow Jones | ^DJI | 50,198.17 | -561.25 | -1.11 | 2026-11-18 | 2026-11-19T05:52:05+00:00 | America/New_York | Yahoo Finance Chart API |
| 費城半導體 SOX | ^SOX | 9,652.80 | 9.92 | +0.10 | 2026-11-18 | 2026-11-19T05:52:05+00:00 | America/New_York | Yahoo Finance Chart API |
| VIX | ^VIX | 24.56 | -0.90 | -3.53 | 2026-11-18 | 2026-11-19T05:52:05+00:00 | America/Chicago | Yahoo Finance Chart API |

### 2. 亞洲主要指數

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 收盤／最新值 | 漲跌值 | 漲跌幅 | 資料日期（交易所時區） | 擷取時間（UTC） | 交易所時區 | 資料來源 |
|---|---|---|---|---|---|---|---|---|
| 日經225 | ^N225 | 59,283.48 | 259.20 | +0.44 | 2026-11-19 | 2026-11-19T05:52:05+00:00 | Asia/Tokyo | Yahoo Finance Chart API |
| 韓國KOSPI | ^KS11 | 5,066.06 | -1.38 | -0.03 | 2026-11-19 | 2026-11-19T05:52:05+00:00 | Asia/Seoul | Yahoo Finance Chart API |
| 香港恆生 | ^HSI | 22,840.89 | -453.86 | -1.95 | 2026-11-19 | 2026-11-19T05:52:05+00:00 | Asia/Hong_Kong | Yahoo Finance Chart API |
| 上海綜合 | 000001.SS | 3,574.34 | -13.49 | -0.38 | 2026-11-19 | 2026-11-19T05:52:05+00:00 | Asia/Shanghai | Yahoo Finance Chart API |
| 深圳成分 | 399001.SZ | 10,622.01 | -37.40 | -0.35 | 2026-11-19 | 2026-11-19T05:52:05+00:00 | Asia/Shanghai | Yahoo Finance Chart API |

### 3. 美股指數期貨

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 最新值 | 漲跌值 | 漲跌幅 | 資料日期（交易所時區） | 擷取時間（UTC） | 交易所時區 | 資料來源 |
|---|---|---|---|---|---|---|---|---|
| S&P500期貨 | ES=F | 7,387.75 | 47.25 | +0.64 | 2026-11-19 | 2026-11-19T05:52:05+00:00 | America/New_York | Yahoo Finance Chart API |
| Nasdaq100期貨 | NQ=F | 27,486.25 | 299.50 | +1.10 | 2026-11-19 | 2026-11-19T05:52:05+00:00 | America/New_York | Yahoo Finance Chart API |
| 道瓊期貨 | YM=F | 50,485.00 | 212.00 | +0.42 | 2026-11-19 | 2026-11-19T05:52:05+00:00 | America/New_York | Yahoo Finance Chart API |
| Russell2000期貨 | RTY=F | 2,729.80 | 7.80 | +0.29 | 2026-11-19 | 2026-11-19T05:52:05+00:00 | America/New_York | Yahoo Finance Chart API |

### 4. 美國國債殖利率

**資料來源：** `U.S. Treasury Fiscal Data API` (失敗時備援 Treasury yield.xml 與 `Yahoo Finance`)

| 項目 | API 資料欄位／識別 | 殖利率（%） | 日變化（百分點） | 資料日期 | 擷取時間（UTC） | 資料來源 |
|---|---|---|---|---|---|---|
| 美國 2 年期殖利率 | 2 Yr | 4.80 | 0.00 | 18-NOV-26 | 2026-11-19T05:52:24+00:00 | U.S. Treasury yield.xml（BC_2YEAR 備援） |
| 美國 10 年期殖利率 | 10 Yr | 5.07 | -0.04 | 2026-11-18 | 2026-11-19T05:52:24+00:00 | Yahoo Finance (備援) |
| 美國 20 年期殖利率 | 20 Yr | 5.44 | -0.06 | 18-NOV-26 | 2026-11-19T05:52:41+00:00 | U.S. Treasury yield.xml（BC_20YEAR 備援） |
| 美國 30 年期殖利率 | 30 Yr | 5.41 | -0.05 | 2026-11-18 | 2026-11-19T05:52:41+00:00 | Yahoo Finance (備援) |

### 5. 主要匯率

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 最新值 | 漲跌值 | 漲跌幅 | 資料日期（交易所時區） | 擷取時間（UTC） | 交易所時區 | 資料來源 |
|---|---|---|---|---|---|---|---|---|
| USD/TWD | TWD=X | 32.95 | 0.04 | +0.11 | 2026-11-19 | 2026-11-19T05:52:05+00:00 | Europe/London | Yahoo Finance Chart API |
| DXY美元指數 | DX-Y.NYB | 103.90 | 0.04 | +0.04 | 2026-11-19 | 2026-11-19T05:52:05+00:00 | America/New_York | Yahoo Finance Chart API |
| USD/JPY | JPY=X | 159.51 | 0.00 | +0.00 | 2026-11-19 | 2026-11-19T05:52:05+00:00 | Europe/London | Yahoo Finance Chart API |
| USD/KRW | KRW=X | 1,330.32 | -2.69 | -0.20 | 2026-11-19 | 2026-11-19T05:52:05+00:00 | Europe/London | Yahoo Finance Chart API |

### 6. 台灣相關ADR

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 收盤／最新值 | 漲跌值 | 漲跌幅 | 資料日期（交易所時區） | 擷取時間（UTC） | 交易所時區 | 資料來源 |
|---|---|---|---|---|---|---|---|---|
| 台積電ADR | TSM | 362.62 | 2.93 | +0.81 | 2026-11-18 | 2026-11-19T05:52:05+00:00 | America/New_York | Yahoo Finance Chart API |
| 聯電ADR | UMC | 13.96 | -0.18 | -1.27 | 2026-11-18 | 2026-11-19T05:52:05+00:00 | America/New_York | Yahoo Finance Chart API |
| 日月光ADR | ASX | 32.52 | 0.69 | +2.17 | 2026-11-18 | 2026-11-19T05:52:05+00:00 | America/New_York | Yahoo Finance Chart API |

### 7. 原油黃金Bitcoin

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 收盤／最新值 | 漲跌值 | 漲跌幅 | 資料日期（交易所時區） | 擷取時間（UTC） | 交易所時區 | 資料來源 |
|---|---|---|---|---|---|---|---|---|
| WTI原油期貨 | CL=F | 82.47 | -0.79 | -0.95 | 2026-11-19 | 2026-11-19T05:52:05+00:00 | America/New_York | Yahoo Finance Chart API |
| 黃金期貨 | GC=F | 3,735.40 | -6.50 | -0.17 | 2026-11-19 | 2026-11-19T05:52:05+00:00 | America/New_York | Yahoo Finance Chart API |
| Bitcoin | BTC-USD | 63,245.63 | -1,648.32 | -2.54 | 2026-11-19 | 2026-11-19T05:52:05+00:00 | UTC | Yahoo Finance Chart API |

### 8. 重大經濟數據、央行事件與重大市場新聞

**資料來源：** 台股 `tw.stock.yahoo.com` (含內文摘要)；國際 `Fed 公告 RSS`＋`CNBC`＋`MarketWatch` (標題、來源、時間與連結)

- 事件1：0050零股大爆量 分析師勸別急接刀
  - 來源：Yahoo 台股；發布時間：2026-11-19T05:49:13Z；台北時間：2026-11-19 13:49
  - 摘要：小資族勇敢抄底！元大台灣50（0050）盤中最低跌至89.8元，創逾一周新低，收盤以90.2元作收，下跌4.14％，但零股成交量一天爆3775萬股。分析師表示，近期投資人不必恐慌殺低，但空手者也別急著「接刀」，靜待量縮止跌、站穩支撐後再分批
  - 原文連結：https://tw.stock.yahoo.com/news/%E5%8F%B0%E8%82%A1%E6%91%94%E7%A0%B43%E8%90%AC9%EF%BC%81%E5%B0%8F%E8%B3%87%E6%97%8F%E6%90%B6%E8%B2%B70050-%E9%9B%B6%E8%82%A1%E4%B8%80%E5%A4%A9%E7%88%863775%E8%90%AC%E8%82%A1-054913626.html
- 事件2：大單利多不敵賣壓 日月光漲一天又重挫
  - 來源：Yahoo 台股；發布時間：2026-11-19T04:40:00Z；台北時間：2026-11-19 12:40
  - 摘要：[FTNN新聞網]記者陳雅婷／綜合報導台股今（19）日賣壓再度擴大，早盤開高後一路走低，盤中最高來到40,315.53點，隨後下探38,259.70點，截至中午12時10分報39,...
  - 原文連結：https://tw.stock.yahoo.com/news/%E8%BC%9D%E9%81%94%E6%95%B8%E5%8D%81%E5%84%84%E7%BE%8E%E5%85%83%E5%A4%A7%E5%96%AE%E8%90%BD%E8%A2%8B-%E6%97%A5%E6%9C%88%E5%85%89%E6%8B%BF%E4%B8%8Bai%E5%B0%81%E8%A3%9D%E5%A4%A7%E6%A9%9F%E6%9C%83-%E8%82%A1%E5%83%B9%E4%BB%8A%E5%8D%BB%E9%87%8D%E6%8C%AB%E9%80%BE5-044000904.html
- 事件3：輝達回不去了？外媒預測黃仁勳籌資另開戰場
  - 來源：Yahoo 台股；發布時間：2026-11-19T04:40:00Z；台北時間：2026-11-19 12:40
  - 摘要：財經中心／李明融報導輝達（NVIDIA）前執行長黃仁勳因風波離任後，外界高度關注他是否還有機會重掌兵符。對此，美媒Semafor商業記者戈斯瓦米分析，董事會當初是經過數小時討論才讓黃仁勳在「自行辭職或遭解雇」間二選一，加上輝達身為上市公司，
  - 原文連結：https://tw.stock.yahoo.com/news/%E9%BB%83%E4%BB%81%E5%8B%B3-%E5%9B%9E%E9%8D%8B%E8%BC%9D%E9%81%94-%E6%A9%9F%E7%8E%87%E6%9B%9D-%E5%A4%96%E5%AA%92%E6%8F%AD-%E8%80%81%E9%BB%83%E5%BE%A9%E4%BB%87%E5%8A%87%E6%9C%AC-044000049.html
- 事件4：昨天亮眼今天變臉 5檔輝達概念股躺跌停
  - 來源：Yahoo 台股；發布時間：2026-11-19T04:23:37Z；台北時間：2026-11-19 12:23
  - 摘要：輝達財報雖亮眼並點名台積電、鴻海等6家台廠，但受創辦人風波及股價連黑影響，台股今（19）日無量大跌逾1400點，摜破40K與39K關卡，創意、景碩等概念股苦吞跌停。市場正聚焦Anthropic美股IPO能否拯救AI投資信心。
  - 原文連結：https://tw.stock.yahoo.com/news/%E8%BC%9D%E9%81%94%E6%A6%82%E5%BF%B5%E8%82%A1%E8%B1%AC%E7%BE%8A%E8%AE%8A%E8%89%B2-%E8%82%A1%E5%90%8E%E5%89%B5%E6%84%8F-%E4%BA%AC%E5%85%83%E9%9B%BB%E5%85%A8%E8%B7%8C%E5%81%9C-041700554.html
- 事件5：12月恐升不只1碼 聯準會放鷹點名AI風險
  - 來源：Yahoo 台股；發布時間：2026-11-19T04:39:00Z；台北時間：2026-11-19 12:39
  - 摘要：聯準會公布10月會議記錄顯示，幾乎全數官員支持持續升息以對抗通膨，部分官員更主張若通膨數據不佳，12月可能需升息超過1碼。受此鷹派立場與通膨升溫影響，美元指數創下近19個月新高，黃金與比特幣等資產全面承壓。此外，報告也點出AI基建熱潮與複雜
  - 原文連結：https://tw.stock.yahoo.com/news/%E8%81%AF%E6%BA%96%E6%9C%83%E6%9C%83%E8%AD%B0%E8%A8%98%E9%8C%84%E6%94%BE%E9%B7%B9-%E5%B9%BE%E4%B9%8E%E6%89%80%E6%9C%89%E4%BA%BA-%E5%96%8A%E5%86%8D%E5%8D%87%E6%81%AF-%E8%AD%A6%E5%91%8Aai%E7%86%B1%E6%BD%AE%E6%88%90%E9%A2%A8%E9%9A%AA-043900198.html
- 事件6：兆豐金衝天價後收斂 官股金控齊撐盤
  - 來源：Yahoo 台股；發布時間：2026-11-19T04:26:20Z；台北時間：2026-11-19 12:26
  - 摘要：台股今（19）日盤中重挫1,935.21點，加權指數最低探至38,259.7點，跌破年線、陷3萬8千點保衛戰。金融股多數走低，惟公股龍頭兆豐金（2886）逆勢大漲逾7%，最高攻上56.5元，寫下歷史新天價。華南金（2880）、合庫金（588
  - 原文連結：https://tw.stock.yahoo.com/news/%E9%87%91%E8%9E%8D%E8%82%A1%E6%9C%80%E9%A3%86%EF%BC%81%E5%85%86%E8%B1%90%E9%87%91%E4%B8%80%E5%BA%A6%E9%80%86%E5%8B%A2%E5%A4%A7%E6%BC%B2%E9%80%BE7-%E6%94%B9%E5%AF%AB%E6%AD%B7%E5%8F%B2%E6%96%B0%E5%A4%A9%E5%83%B9-042501962.html
- 事件7：Minutes of the Federal Open Market Committee, October 27-28, 2026
  - 來源：Federal Reserve；發布時間：Wed, 18 Nov 2026 19:00:00 GMT；台北時間：2026-11-19 03:00
  - 摘要：Minutes of the Federal Open Market Committee, October 27-28, 2026
  - 原文連結：https://www.federalreserve.gov/newsevents/pressreleases/monetary20261118a.htm
- 事件8：Federal Reserve Board announces pricing, effective January 1, 2027, for payment services the Federal Reserve Banks provide to banks and credit unions, and changes to streamline and adjust their check services
  - 來源：Federal Reserve；發布時間：Thu, 12 Nov 2026 18:30:00 GMT；台北時間：2026-11-13 02:30
  - 摘要：Federal Reserve Board announces pricing, effective January 1, 2027, for payment services the Federal Reserve Banks provide to banks and credit unions,
  - 原文連結：https://www.federalreserve.gov/newsevents/pressreleases/other20261112a.htm
- 事件9：Federal Reserve announces revised tentative schedule of Federal Open Market Committee meetings in 2027
  - 來源：Federal Reserve；發布時間：Thu, 12 Nov 2026 17:45:00 GMT；台北時間：2026-11-13 01:45
  - 摘要：Federal Reserve announces revised tentative schedule of Federal Open Market Committee meetings in 2027
  - 原文連結：https://www.federalreserve.gov/newsevents/pressreleases/monetary20261112a.htm
- 事件10：Federal Reserve Board issues enforcement action with former employee of United Community Bank
  - 來源：Federal Reserve；發布時間：Thu, 12 Nov 2026 16:00:00 GMT；台北時間：2026-11-13 00:00
  - 摘要：Federal Reserve Board issues enforcement action with former employee of United Community Bank
  - 原文連結：https://www.federalreserve.gov/newsevents/pressreleases/enforcement20261112a.htm
- 事件11：Fed officials expect more rate hikes, worry about AI impact on inflation, minutes show
  - 來源：CNBC；發布時間：Wed, 18 Nov 2026 19:41:59 GMT；台北時間：2026-11-19 03:41
  - 摘要：The Federal Reserve on Wednesday released minutes from its October policy meeting at which it voted to hold its benchmark interest rate in a range bet
  - 原文連結：https://www.cnbc.com/2026/11/18/fed-minutes-october-2026.html
- 事件12：Inside India newsletter: Foreign flows helped the market recover. Now it faces the inflation test
  - 來源：CNBC；發布時間：Thu, 19 Nov 2026 00:01:23 GMT；台北時間：2026-11-19 08:01
  - 摘要：India’s inflation, which has been on the rise for 12 straight months, is becoming a risk to growth and to the reversal of foreign inflows.
  - 原文連結：https://www.cnbc.com/2026/11/19/india-inflation-foreign-investor-nifty50.html


## 三、期貨

**資料來源：**
1. Cloudflare Workers：TAIFEX Proxy — https://taifex.grichtoyang.workers.dev/
2. TAIFEX Open API — https://openapi.taifex.com.tw/

近月契約月份：202612 (日盤成交量最大者)；交易日期：2026-11-19

### 1．台指期近月日盤行情

| 項目 | 數值 | 單位 | 資料來源 |
|---|---|---|---|
| 開盤價 | 41,073 | 點 | TAIFEX Proxy |
| 最高價 | 41,205 | 點 | TAIFEX Proxy |
| 最低價 | 39,523 | 點 | TAIFEX Proxy |
| 收盤價 | 40,312 | 點 | TAIFEX Proxy |
| 漲跌點數 | +205 | 點 | TAIFEX Proxy |
| 漲跌幅 | +0.51 | % | TAIFEX Proxy |
| 成交量 | 74,871 | 口 | TAIFEX Proxy |
| 日盤高點及低點 | 41,205 / 39,523 | 點 | TAIFEX Proxy |

### 2．台指期近月夜盤行情

| 項目 | 數值 | 單位 | 資料來源 |
|---|---|---|---|
| 開盤價 | 40,330 | 點 | TAIFEX Proxy |
| 最高價 | 40,689 | 點 | TAIFEX Proxy |
| 最低價 | 39,411 | 點 | TAIFEX Proxy |
| 收盤價 | 39,987 | 點 | TAIFEX Proxy |
| 漲跌點數 | -345 | 點 | TAIFEX Proxy |
| 漲跌幅 | -0.86 | % | TAIFEX Proxy |
| 成交量 | 56,051 | 口 | TAIFEX Proxy |
| 夜盤高點及低點 | 40,689 / 39,411 | 點 | TAIFEX Proxy |

### 3．法人台指期多空未平倉部位

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 外資多方 OI | unavailable | unavailable |
| 外資空方 OI | unavailable | unavailable |
| 外資多空淨 OI | unavailable | unavailable |
| 投信多方 OI | unavailable | unavailable |
| 投信空方 OI | unavailable | unavailable |
| 投信多空淨 OI | unavailable | unavailable |
| 自營商多方 OI | unavailable | unavailable |
| 自營商空方 OI | unavailable | unavailable |
| 自營商多空淨 OI | unavailable | unavailable |
| 三大法人合計多方 OI | unavailable | unavailable |
| 三大法人合計空方 OI | unavailable | unavailable |
| 三大法人合計多空淨 OI | unavailable | unavailable |
| 外資多空淨 OI 變化 | unavailable | unavailable |
| 投信多空淨 OI 變化 | unavailable | unavailable |
| 自營商多空淨 OI 變化 | unavailable | unavailable |

### 4．前十大交易人多空未平倉部位

**資料來源：** `TAIFEX OpenAPI OpenInterestOfLargeTradersFutures`（備援 TAIFEX Proxy；欄位依實際取得來源標示）

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 前十大交易人多方 OI | 100,057 | TAIFEX Proxy |
| 前十大交易人空方 OI | 93,315 | TAIFEX Proxy |
| 前十大交易人多空淨 OI | +6,742 | TAIFEX Proxy |
| 多空淨 OI 變化 | unavailable | 換月基準重建 |
- 資料日期：2026-11-18 (TypeOfTraders=0 全部交易人；契約月份 202612)

### 5．日盤、夜盤法人交易資料

| 項目 | 數值 | 單位 | 資料來源 |
|---|---|---|---|
| 外資日盤多單交易量 | 93,106 | 口 | TAIFEX Proxy |
| 外資日盤空單交易量 | 95,726 | 口 | TAIFEX Proxy |
| 外資日盤多空淨交易量 | -2,620 | 口 | TAIFEX Proxy |
| 外資夜盤多單交易量 | 33,877 | 口 | TAIFEX Proxy |
| 外資夜盤空單交易量 | 33,985 | 口 | TAIFEX Proxy |
| 外資夜盤多空淨交易量 | -108 | 口 | TAIFEX Proxy |
| 外資日盤／夜盤交易量變化 | -2,512 | 口 | TAIFEX Proxy |
| 投信日盤多空淨交易量 | +2,347 | 口 | TAIFEX Proxy |
| 投信夜盤多空淨交易量 | +0 | 口 | TAIFEX Proxy |
| 投信日盤／夜盤交易量變化 | +2,347 | 口 | TAIFEX Proxy |
| 自營商日盤多空淨交易量 | -2,486 | 口 | TAIFEX Proxy |
| 自營商夜盤多空淨交易量 | +262 | 口 | TAIFEX Proxy |
| 自營商日盤／夜盤交易量變化 | -2,748 | 口 | TAIFEX Proxy |
| 三大法人日盤多空淨交易量 | -2,759 | 口 | TAIFEX Proxy |
| 三大法人夜盤多空淨交易量 | +154 | 口 | TAIFEX Proxy |
| 法人日盤交易金額淨額 | -221.7 | 億元 | TAIFEX Proxy |
| 法人夜盤交易金額淨額 | +12.2 | 億元 | TAIFEX Proxy |

### 6．期貨與現貨關係

| 項目 | 數值 | 資料來源 |
|---|---|---|
| 台指期近月價格 | 40,312 | TAIFEX Proxy |
| 加權指數價格 | 38,426.89 | twse-proxy |
| 台指期與加權指數價差 | +1,885.11 | TAIFEX Proxy／twse-proxy |
| 價差百分比 | +4.91 | TAIFEX Proxy／twse-proxy |
| 日盤基差 | +1,885.11 | TAIFEX Proxy／twse-proxy |
| 夜盤價格相對日盤收盤的變化 | -325 | TAIFEX Proxy |

### 7．日盤、夜盤與籌碼變化對照

#### 7.1 日夜盤價格與成交量對照 (變化 = 日盤 - 夜盤)

| 項目 | 日盤 | 夜盤 | 變化 (日-夜) | 資料來源 |
|---|---|---|---|---|
| 收盤價 | 40,312 | 39,987 | +325 | TAIFEX Proxy |
| 成交量 | 74,871 | 56,051 | +18,820 | TAIFEX Proxy |
- 台指期總 OI 前日變化：unavailable（來源：unavailable）


#### 7.2 法人籌碼日夜盤對照 (淨變化 = 日盤淨 - 夜盤淨；OI 為日盤收盤後總量，前日變化另列)

| 法人 | 交易量 |  |  |  |  |  |  | 未平倉量 |  |  |  | 資料來源 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|  | **日盤多單** | **日盤空單** | **日盤淨** | **夜盤多單** | **夜盤空單** | **夜盤淨** | **淨變化 (日-夜)** | **OI多方** | **OI空方** | **OI淨** | **OI前日變化** |  |
| 外資 | 93,106 | 95,726 | -2,620 | 33,877 | 33,985 | -108 | -2,512 | unavailable | unavailable | unavailable | unavailable | unavailable |
| 投信 | 2,599 | 252 | +2,347 | 0 | 0 | +0 | +2,347 | unavailable | unavailable | unavailable | unavailable | unavailable |
| 自營商 | 12,215 | 14,701 | -2,486 | 1,121 | 859 | +262 | -2,748 | unavailable | unavailable | unavailable | unavailable | unavailable |
| 三大法人合計 | 107,920 | 110,679 | -2,759 | 34,998 | 34,844 | +154 | -2,913 | unavailable | unavailable | unavailable | unavailable | unavailable |

#### 7.3 前十大交易人日夜盤對照 (OI 無日夜拆分，列收盤後總量)

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 前十大交易人多方 OI | 100,057 | TAIFEX Proxy |
| 前十大交易人空方 OI | 93,315 | TAIFEX Proxy |
| 前十大交易人多空淨 OI | +6,742 | TAIFEX Proxy |
| 前十大交易人多空淨 OI 變化 | unavailable | 換月基準重建 |

#### 7.4 夜盤劇本分類 (規則對應：夜盤漲跌 × 外資夜盤偏多空)

| 項目 | 數值 | 資料來源 |
|---|---|---|
| 夜盤成交量占比 (夜盤量／(夜盤量＋日盤量)) | 42.81% | TAIFEX Proxy |
| 夜盤漲跌點數 | -345 | TAIFEX Proxy |
| 外資夜盤多空淨交易量 | -108 | TAIFEX Proxy |
| 劇本分類 | 劇本三 | 規則對應 |
| 劇本條件 | 夜盤下跌＋外資偏空 | 規則對應 |
| 劇本特徵 | 開低、續跌機率高 | 規則對應 |

## 四、選擇權

**資料來源：** 主要 TAIFEX 經 Cloudflare Worker Proxy；時區 `Asia/Taipei`

### 1．選擇權交易日期、到期日與報告產製時間

| 項目 | 數值 | 資料來源 |
|---|---|---|
| 交易日期 | 2026-11-19 | TAIFEX Proxy |
| 到期月份／到期日 | 202611 | TAIFEX Proxy |
| 本次報告產製時間 | 2026-11-19 13:51:44 | 本機 |
| 日盤／夜盤標記 | 日盤收盤後資料 | TAIFEX Proxy |

### 2．Call 總成交量、OI、OI 增減

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Call 總成交量 | 409,461 | TAIFEX Proxy |
| Call 總未平倉量 OI | 167,265 | TAIFEX Proxy |
| Call OI 增減（共同合約） | unavailable | unavailable |

### 3．Put 總成交量、OI、OI 增減

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Put 總成交量 | 402,395 | TAIFEX Proxy |
| Put 總未平倉量 OI | 113,894 | TAIFEX Proxy |
| Put OI 增減（共同合約） | unavailable | unavailable |

### 4．Call／Put 比例與變化

| 項目 | 數值 | 單位 | 資料來源 |
|---|---|---|---|
| Call／Put 成交量比例 | 1.02 | 倍 | TAIFEX Proxy |
| Call／Put 未平倉量比例 | 1.47 | 倍 | TAIFEX Proxy |
| Put／Call Ratio | 0.68 | 倍 | TAIFEX Proxy |
| Call／Put 成交量比例變化 (2026-11-17→2026-11-18) | 13.02 | 百分點（pp） | TAIFEX Proxy |
| Call／Put OI 比例變化 (2026-11-17→2026-11-18) | -14.28 | 百分點（pp） | TAIFEX Proxy |
**資料來源：** 比例 `TAIFEX Proxy chain`；變化 `TAIFEX Proxy PutCallRatio`

### 5．外資 Call／Put 部位

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 外資 Call日買 | 143,558 | TAIFEX Proxy |
| 外資 Call日賣 | 139,131 | TAIFEX Proxy |
| 外資 Call日淨 | +4,427 | TAIFEX Proxy |
| 外資 Put日買 | 148,683 | TAIFEX Proxy |
| 外資 Put日賣 | 150,740 | TAIFEX Proxy |
| 外資 Put日淨 | -2,057 | TAIFEX Proxy |
| 外資 Call夜買 | 20,465 | TAIFEX Proxy |
| 外資 Call夜賣 | 21,034 | TAIFEX Proxy |
| 外資 Call夜淨 | -569 | TAIFEX Proxy |
| 外資 Put夜買 | 20,222 | TAIFEX Proxy |
| 外資 Put夜賣 | 21,075 | TAIFEX Proxy |
| 外資 Put夜淨 | -853 | TAIFEX Proxy |
| 外資 日盤淨總量 | +6,484 | TAIFEX Proxy |
| 外資 Call日夜淨增減 (日－夜) | +4,996 | TAIFEX Proxy |
| 外資 Put日夜淨增減 (日－夜) | -1,204 | TAIFEX Proxy |

### 6．自營商 Call／Put 部位

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 自營商 Call日買 | 103,086 | TAIFEX Proxy |
| 自營商 Call日賣 | 114,939 | TAIFEX Proxy |
| 自營商 Call日淨 | -11,853 | TAIFEX Proxy |
| 自營商 Put日買 | 94,078 | TAIFEX Proxy |
| 自營商 Put日賣 | 111,089 | TAIFEX Proxy |
| 自營商 Put日淨 | -17,011 | TAIFEX Proxy |
| 自營商 Call夜買 | 15,065 | TAIFEX Proxy |
| 自營商 Call夜賣 | 16,102 | TAIFEX Proxy |
| 自營商 Call夜淨 | -1,037 | TAIFEX Proxy |
| 自營商 Put夜買 | 12,324 | TAIFEX Proxy |
| 自營商 Put夜賣 | 12,906 | TAIFEX Proxy |
| 自營商 Put夜淨 | -582 | TAIFEX Proxy |
| 自營商 日盤淨總量 | +5,158 | TAIFEX Proxy |
| 自營商 Call日夜淨增減 (日－夜) | -10,816 | TAIFEX Proxy |
| 自營商 Put日夜淨增減 (日－夜) | -16,429 | TAIFEX Proxy |

### 7．主要 Call OI 集中區

| 項目 | 履約價 | OI | 資料來源 |
|---|---|---|---|
| Call OI 第1大履約價 | 46,000 | 7,825 | TAIFEX Proxy |
| Call OI 第2大履約價 | 43,500 | 7,630 | TAIFEX Proxy |
| Call OI 第3大履約價 | 44,000 | 6,064 | TAIFEX Proxy |
| Call OI 最大履約價 | 46,000 | 7,825 | TAIFEX Proxy |

#### Call OI 分布明細 Top10 (機器可讀，到期月份 202611)

| # | 履約價 | OI | 佔比 | 資料來源 |
|---|---|---|---|---|
| C1 | 46,000 | 7,825 | 4.68% | TAIFEX Proxy |
| C2 | 43,500 | 7,630 | 4.56% | TAIFEX Proxy |
| C3 | 44,000 | 6,064 | 3.63% | TAIFEX Proxy |
| C4 | 41,000 | 4,767 | 2.85% | TAIFEX Proxy |
| C5 | 45,000 | 3,808 | 2.28% | TAIFEX Proxy |
| C6 | 43,000 | 3,709 | 2.22% | TAIFEX Proxy |
| C7 | 42,000 | 3,502 | 2.09% | TAIFEX Proxy |
| C8 | 48,000 | 3,396 | 2.03% | TAIFEX Proxy |
| C9 | 46,500 | 3,343 | 2.0% | TAIFEX Proxy |
| C10 | 47,000 | 3,093 | 1.85% | TAIFEX Proxy |


### 8．主要 Put OI 集中區

| 項目 | 履約價 | OI | 資料來源 |
|---|---|---|---|
| Put OI 第1大履約價 | 33,700 | 11,549 | TAIFEX Proxy |
| Put OI 第2大履約價 | 40,000 | 4,691 | TAIFEX Proxy |
| Put OI 第3大履約價 | 36,000 | 4,490 | TAIFEX Proxy |
| Put OI 最大履約價 | 33,700 | 11,549 | TAIFEX Proxy |

#### Put OI 分布明細 Top10 (機器可讀，到期月份 202611)

| # | 履約價 | OI | 佔比 | 資料來源 |
|---|---|---|---|---|
| P1 | 33,700 | 11,549 | 10.14% | TAIFEX Proxy |
| P2 | 40,000 | 4,691 | 4.12% | TAIFEX Proxy |
| P3 | 36,000 | 4,490 | 3.94% | TAIFEX Proxy |
| P4 | 38,000 | 4,109 | 3.61% | TAIFEX Proxy |
| P5 | 37,000 | 4,094 | 3.59% | TAIFEX Proxy |
| P6 | 39,000 | 4,030 | 3.54% | TAIFEX Proxy |
| P7 | 36,200 | 3,830 | 3.36% | TAIFEX Proxy |
| P8 | 39,500 | 3,525 | 3.09% | TAIFEX Proxy |
| P9 | 38,500 | 2,697 | 2.37% | TAIFEX Proxy |
| P10 | 36,500 | 2,604 | 2.29% | TAIFEX Proxy |


### 9．Call OI 增減集中區

| 項目 | 履約價 (增減口數) | 資料來源 |
|---|---|---|
| Call OI 增加最多的履約價（共同合約） | unavailable | unavailable |
| Call OI 減少最多的履約價（共同合約） | unavailable | unavailable |

### 10．Put OI 增減集中區

| 項目 | 履約價 (增減口數) | 資料來源 |
|---|---|---|
| Put OI 增加最多的履約價（共同合約） | unavailable | unavailable |
| Put OI 減少最多的履約價（共同合約） | unavailable | unavailable |

### 11．Call Wall

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Call Wall 價位 | 46,000 | TAIFEX Proxy |
| 對應到期月份 | 202611 | TAIFEX Proxy |
| 與前一交易日的變化 | unavailable | 本日 Chain 日期不符（實際 2026-11-18／應為 2026-11-19） |

### 12．Put Wall

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Put Wall 價位 | 33,700 | TAIFEX Proxy |
| 對應到期月份 | 202611 | TAIFEX Proxy |
| 與前一交易日的變化 | unavailable | 本日 Chain 日期不符（實際 2026-11-18／應為 2026-11-19） |

### 13．Gamma Wall

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Gamma Wall 價位 | 39,500.00 | options-market-structure-compact (proxy) |
| GEX 實際使用到期月份 | 202611F3 | options-gamma-levels（GEX 實際使用） |
| GEX 實際到期日 | 2026-11-20 | options-gamma-levels（GEX 實際使用） |
| Options Key Levels 主到期月份 | 202611 | TAIFEX Proxy |
| 資料日期 | 2026-11-18 | TAIFEX Proxy (options-market-structure-compact (proxy)) |

### 14．Gamma Flip

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Gamma Flip 價位 | 36,223.97 | options-market-structure-compact (proxy) |
| GEX 實際使用到期月份 | 202611F3 | options-gamma-levels（GEX 實際使用） |
| GEX 實際到期日 | 2026-11-20 | options-gamma-levels（GEX 實際使用） |
| 主到期月份（Key Levels） | 202611 | TAIFEX Proxy |
| 原始 Call OI（選定到期日全部有效 Chain 合約） | 45,066 | options-gamma-levels（GEX 到期日） |
| 模型納入 Call OI（通過 GEX 計算條件） | 0 | TAIFEX Gamma model（逐履約價） |
| 原始 Put OI（選定到期日全部有效 Chain 合約） | 13,105 | options-gamma-levels（GEX 到期日） |
| 模型納入 Put OI（通過 GEX 計算條件） | 0 | TAIFEX Gamma model（逐履約價） |
| GEX 資料日期 | 2026-11-18 | TAIFEX Proxy (options-market-structure-compact (proxy)) |
- OI 對帳口徑：原始 OI 統計選定到期日全部有效 Chain 合約；模型納入 OI 僅統計通過結算價、IV 與 Gamma 計算條件並納入逐履約價 GEX 的合約。兩者差額不等於 Chain 缺漏。

**Gamma Flip 零交叉搜尋診斷**
- 搜尋標的區間：36,175.42～44,214.40
- 搜尋步長／計算次數：10.00／6
- 起點／終點 Net GEX：-32,021,696.29／976,268.34
- 搜尋區間最低／最高 Net GEX：-32,021,696.29／976,268.34
- 正負號交叉次數：1
- 解讀限制：此 Flip 僅代表目前 Call 正／Put 負假設下的模型零交叉；Aggregate OI 無法識別 Dealer 實際淨部位，不等同市場實際 Dealer Gamma Flip。

**GEX 到期日配對診斷（原始候選清單）**
```json
{"requested_date":"2026-11-18","chain_expiries":[{"contract_month":"202611","expiry":"2026-11-18"},{"contract_month":"202611F3","expiry":"2026-11-20"},{"contract_month":"202611W4","expiry":"2026-11-25"},{"contract_month":"202611F4","expiry":"2026-11-27"},{"contract_month":"202612W1","expiry":"2026-12-02"},{"contract_month":"202612","expiry":"2026-12-16"},{"contract_month":"202701","expiry":"2027-01-20"},{"contract_month":"202703","expiry":"2027-03-17"},{"contract_month":"202706","expiry":"2027-06-16"}],"delta_expiries":[{"contract_month":"202611F3","expiry":"2026-11-20"},{"contract_month":"202611W4","expiry":"2026-11-25"},{"contract_month":"202611F4","expiry":"2026-11-27"},{"contract_month":"202612W1","expiry":"2026-12-02"},{"contract_month":"202612","expiry":"2026-12-16"},{"contract_month":"202701","expiry":"2027-01-20"},{"contract_month":"202702","expiry":"2027-02-17"},{"contract_month":"202703","expiry":"2027-03-17"},{"contract_month":"202706","expiry":"2027-06-16"}],"common_expiries":[{"contract_month":"202611F3","expiry":"2026-11-20","delta_contract_month":"202611F3","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202611W4","expiry":"2026-11-25","delta_contract_month":"202611W4","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202611F4","expiry":"2026-11-27","delta_contract_month":"202611F4","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202612W1","expiry":"2026-12-02","delta_contract_month":"202612W1","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202612","expiry":"2026-12-16","delta_contract_month":"202612","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202701","expiry":"2027-01-20","delta_contract_month":"202701","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202703","expiry":"2027-03-17","delta_contract_month":"202703","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202706","expiry":"2027-06-16","delta_contract_month":"202706","match_type":"exact_contract_month_and_expiry"}],"same_day_common_expiries":[],"future_common_expiries":[{"contract_month":"202611F3","expiry":"2026-11-20","delta_contract_month":"202611F3","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202611W4","expiry":"2026-11-25","delta_contract_month":"202611W4","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202611F4","expiry":"2026-11-27","delta_contract_month":"202611F4","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202612W1","expiry":"2026-12-02","delta_contract_month":"202612W1","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202612","expiry":"2026-12-16","delta_contract_month":"202612","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202701","expiry":"2027-01-20","delta_contract_month":"202701","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202703","expiry":"2027-03-17","delta_contract_month":"202703","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202706","expiry":"2027-06-16","delta_contract_month":"202706","match_type":"exact_contract_month_and_expiry"}],"future_exact_common_expiries":[{"contract_month":"202611F3","expiry":"2026-11-20","delta_contract_month":"202611F3","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202611W4","expiry":"2026-11-25","delta_contract_month":"202611W4","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202611F4","expiry":"2026-11-27","delta_contract_month":"202611F4","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202612W1","expiry":"2026-12-02","delta_contract_month":"202612W1","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202612","expiry":"2026-12-16","delta_contract_month":"202612","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202701","expiry":"2027-01-20","delta_contract_month":"202701","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202703","expiry":"2027-03-17","delta_contract_month":"202703","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202706","expiry":"2027-06-16","delta_contract_month":"202706","match_type":"exact_contract_month_and_expiry"}],"future_date_fallback_common_expiries":[],"per_expiry_row_counts":[{"contract_month":"202611","expiry":"2026-11-18","chain_rows":616,"delta_rows":0},{"contract_month":"202611F3","expiry":"2026-11-20","chain_rows":404,"delta_rows":404},{"contract_month":"202611W4","expiry":"2026-11-25","chain_rows":390,"delta_rows":390},{"contract_month":"202611F4","expiry":"2026-11-27","chain_rows":366,"delta_rows":366},{"contract_month":"202612W1","expiry":"2026-12-02","chain_rows":214,"delta_rows":218},{"contract_month":"202612","expiry":"2026-12-16","chain_rows":562,"delta_rows":562},{"contract_month":"202701","expiry":"2027-01-20","chain_rows":410,"delta_rows":410},{"contract_month":"202702","expiry":"2027-02-17","chain_rows":0,"delta_rows":246},{"contract_month":"202703","expiry":"2027-03-17","chain_rows":284,"delta_rows":284},{"contract_month":"202706","expiry":"2027-06-16","chain_rows":284,"delta_rows":284}],"selected":{"contract_month":"202611F3","expiry":"2026-11-20","delta_contract_month":"202611F3","match_type":"exact_contract_month_and_expiry"},"selection_reason":"earliest_future_exact_common_expiry"}
```

**TAIFEX Delta 原始資料與 Parser 階段診斷**
```json
{"requested_date":"2026-11-18","source":"taifex_web","fallback_used":false,"index_duration_ms":2257,"index_error":null,"openapi_fetch_duration_ms":209,"attempts":[{"attempt":1,"duration_ms":1129,"source":"taifex_web","fallback":false,"http_status":502,"raw_rows":0,"primary_error":"TAIFEX primary HTTP 200 / rows 0","parser":{"input_rows":0,"array_rows":0,"object_rows":0,"short_rows":0,"non_txo_rows":0,"txo_rows":0,"invalid_contract_month":0,"invalid_expiry":0,"unknown_option_type_rows":0,"invalid_strike_rows":0,"invalid_delta_rows":0,"parsed_rows":0,"per_expiry":[]},"accepted_txo_rows":0},{"attempt":2,"duration_ms":3228,"source":"taifex_web","fallback":false,"http_status":200,"raw_rows":3169,"primary_error":null,"parser":{"input_rows":3169,"array_rows":3169,"object_rows":0,"short_rows":4,"non_txo_rows":1,"txo_rows":3164,"invalid_contract_month":0,"invalid_expiry":0,"unknown_option_type_rows":0,"invalid_strike_rows":0,"invalid_delta_rows":0,"parsed_rows":3164,"per_expiry":[{"contract_month":"202611F3","expiry":"2026-11-20","raw_txo_rows":404,"recognized_type_rows":404,"valid_strike_rows":404,"valid_delta_rows":404,"parsed_rows":404},{"contract_month":"202611W4","expiry":"2026-11-25","raw_txo_rows":390,"recognized_type_rows":390,"valid_strike_rows":390,"valid_delta_rows":390,"parsed_rows":390},{"contract_month":"202611F4","expiry":"2026-11-27","raw_txo_rows":366,"recognized_type_rows":366,"valid_strike_rows":366,"valid_delta_rows":366,"parsed_rows":366},{"contract_month":"202612W1","expiry":"2026-12-02","raw_txo_rows":218,"recognized_type_rows":218,"valid_strike_rows":218,"valid_delta_rows":218,"parsed_rows":218},{"contract_month":"202612","expiry":"2026-12-16","raw_txo_rows":562,"recognized_type_rows":562,"valid_strike_rows":562,"valid_delta_rows":562,"parsed_rows":562},{"contract_month":"202701","expiry":"2027-01-20","raw_txo_rows":410,"recognized_type_rows":410,"valid_strike_rows":410,"valid_delta_rows":410,"parsed_rows":410},{"contract_month":"202702","expiry":"2027-02-17","raw_txo_rows":246,"recognized_type_rows":246,"valid_strike_rows":246,"valid_delta_rows":246,"parsed_rows":246},{"contract_month":"202703","expiry":"2027-03-17","raw_txo_rows":284,"recognized_type_rows":284,"valid_strike_rows":284,"valid_delta_rows":284,"parsed_rows":284},{"contract_month":"202706","expiry":"2027-06-16","raw_txo_rows":284,"recognized_type_rows":284,"valid_strike_rows":284,"valid_delta_rows":284,"parsed_rows":284}]},"accepted_txo_rows":3164}],"parser":{"input_rows":3169,"array_rows":3169,"object_rows":0,"short_rows":4,"non_txo_rows":1,"txo_rows":3164,"invalid_contract_month":0,"invalid_expiry":0,"unknown_option_type_rows":0,"invalid_strike_rows":0,"invalid_delta_rows":0,"parsed_rows":3164,"per_expiry":[{"contract_month":"202611F3","expiry":"2026-11-20","raw_txo_rows":404,"recognized_type_rows":404,"valid_strike_rows":404,"valid_delta_rows":404,"parsed_rows":404},{"contract_month":"202611W4","expiry":"2026-11-25","raw_txo_rows":390,"recognized_type_rows":390,"valid_strike_rows":390,"valid_delta_rows":390,"parsed_rows":390},{"contract_month":"202611F4","expiry":"2026-11-27","raw_txo_rows":366,"recognized_type_rows":366,"valid_strike_rows":366,"valid_delta_rows":366,"parsed_rows":366},{"contract_month":"202612W1","expiry":"2026-12-02","raw_txo_rows":218,"recognized_type_rows":218,"valid_strike_rows":218,"valid_delta_rows":218,"parsed_rows":218},{"contract_month":"202612","expiry":"2026-12-16","raw_txo_rows":562,"recognized_type_rows":562,"valid_strike_rows":562,"valid_delta_rows":562,"parsed_rows":562},{"contract_month":"202701","expiry":"2027-01-20","raw_txo_rows":410,"recognized_type_rows":410,"valid_strike_rows":410,"valid_delta_rows":410,"parsed_rows":410},{"contract_month":"202702","expiry":"2027-02-17","raw_txo_rows":246,"recognized_type_rows":246,"valid_strike_rows":246,"valid_delta_rows":246,"parsed_rows":246},{"contract_month":"202703","expiry":"2027-03-17","raw_txo_rows":284,"recognized_type_rows":284,"valid_strike_rows":284,"valid_delta_rows":284,"parsed_rows":284},{"contract_month":"202706","expiry":"2027-06-16","raw_txo_rows":284,"recognized_type_rows":284,"valid_strike_rows":284,"valid_delta_rows":284,"parsed_rows":284}]},"final_rows":3164,"per_expiry_rows":[{"contract_month":"202611F3","expiry":"2026-11-20","raw_txo_rows":404,"recognized_type_rows":404,"valid_strike_rows":404,"valid_delta_rows":404,"parsed_rows":404},{"contract_month":"202611W4","expiry":"2026-11-25","raw_txo_rows":390,"recognized_type_rows":390,"valid_strike_rows":390,"valid_delta_rows":390,"parsed_rows":390},{"contract_month":"202611F4","expiry":"2026-11-27","raw_txo_rows":366,"recognized_type_rows":366,"valid_strike_rows":366,"valid_delta_rows":366,"parsed_rows":366},{"contract_month":"202612W1","expiry":"2026-12-02","raw_txo_rows":218,"recognized_type_rows":218,"valid_strike_rows":218,"valid_delta_rows":218,"parsed_rows":218},{"contract_month":"202612","expiry":"2026-12-16","raw_txo_rows":562,"recognized_type_rows":562,"valid_strike_rows":562,"valid_delta_rows":562,"parsed_rows":562},{"contract_month":"202701","expiry":"2027-01-20","raw_txo_rows":410,"recognized_type_rows":410,"valid_strike_rows":410,"valid_delta_rows":410,"parsed_rows":410},{"contract_month":"202702","expiry":"2027-02-17","raw_txo_rows":246,"recognized_type_rows":246,"valid_strike_rows":246,"valid_delta_rows":246,"parsed_rows":246},{"contract_month":"202703","expiry":"2027-03-17","raw_txo_rows":284,"recognized_type_rows":284,"valid_strike_rows":284,"valid_delta_rows":284,"parsed_rows":284},{"contract_month":"202706","expiry":"2027-06-16","raw_txo_rows":284,"recognized_type_rows":284,"valid_strike_rows":284,"valid_delta_rows":284,"parsed_rows":284}]}
```

**擴大區間 Gamma Flip 診斷（±15%；不覆蓋正式 ±10% 結果）**
- 搜尋標的區間：34,165.67～46,224.15
- 搜尋步長／計算次數：10.00／1207
- 起點／終點 Net GEX：-288,195,673.28／2,053,614,650.75
- 搜尋區間最低／最高 Net GEX：-359,419,741.27／3,232,351,157.02
- 正負號交叉次數：1
- 擴大區間診斷 Flip：36,223.97

### 14A．GEX 整體曝險與履約價分布

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Net GEX（標的變動 1%） | unavailable | 端點未提供 |
| Gross GEX（標的變動 1%） | unavailable | 端點未提供 |
| 模型品質 | unavailable | unavailable |
| 部位正負號假設 | unavailable | 模型限制；非 TAIFEX 公布的 Dealer 部位 |
| 履約價資料筆數 | unavailable | 資料日期：2026-11-18 |
| 正 Net GEX 最大履約價 | unavailable | 依 Net GEX 排序 |
| 負 Net GEX 最低履約價 | unavailable | 依 Net GEX 排序 |
- GEX 明細 unavailable；不以 Wall／Flip proxy 代替。

### 15．Max Pain

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Max Pain 價位 | 40,500 | TAIFEX Proxy |
| 對應到期月份 | 202611 | TAIFEX Proxy |
| 與前一交易日的變化 | unavailable | 本日 Chain 日期不符（實際 2026-11-18／應為 2026-11-19） |

### 17．選擇權法人日盤、夜盤交易

| 法人 | 日盤多單 | 日盤空單 | 日盤淨 | 夜盤多單 | 夜盤空單 | 夜盤淨 | 淨變化 (日-夜) | 資料來源 |
|---|---|---|---|---|---|---|---|---|
| 外資 | 294,298 | 287,814 | +6,484 | 41,540 | 41,256 | +284 | +6,200 | TAIFEX Proxy |
| 投信 | 374 | 17,556 | -17,182 | 0 | 0 | +0 | -17,182 | TAIFEX Proxy |
| 自營商 | 214,175 | 209,017 | +5,158 | 27,971 | 28,426 | -455 | +5,613 | TAIFEX Proxy |
| 三大法人合計 | 508,847 | 514,387 | -5,540 | 69,511 | 69,682 | -171 | -5,369 | TAIFEX Proxy |
- 方法論：多方＝買Call＋賣Put（看多），空方＝賣Call＋買Put（看空），淨額＝看多－看空（已用 Call／Put 拆分頁交叉驗算一致）
- 公式：多方(買)－空方(賣)＝（買call＋賣put）－（賣call＋買put）＝看多－看空
- 速記：多＝BC＋SP、空＝SC＋BP

#### 法人多空力道表（金額・億元；上游千元／1e5）

| 法人 | 日多方力道 | 日空方力道 | 日淨多空力道 | 夜多方力道 | 夜空方力道 | 夜淨多空力道 | 日淨－夜淨 | 資料來源 |
|---|---|---|---|---|---|---|---|---|
| 外資 | 31.21 | 25.05 | +6.16 | 5.97 | 5.92 | +0.04 | +6.12 | TAIFEX Proxy |
| 投信 | 0.13 | 13.02 | -12.89 | 0.00 | 0.00 | +0 | -12.89 | TAIFEX Proxy |
| 自營商 | 27.68 | 22.09 | +5.59 | 5.07 | 5.03 | +0.05 | +5.54 | TAIFEX Proxy |
| 三大法人合計 | 59.01 | 60.16 | -1.14 | 11.04 | 10.95 | +0.09 | -1.23 | TAIFEX Proxy |

### 18．選擇權前十大

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 買權多方 OI | 11,882 | TAIFEX Proxy |
| 買權空方 OI | 14,309 | TAIFEX Proxy |
| 買權多空淨 OI | -2,427 | TAIFEX Proxy |
| 買權多空淨 OI 變化 | unavailable | 換月基準重建 |

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 賣權多方 OI | 10,359 | TAIFEX Proxy |
| 賣權空方 OI | 10,230 | TAIFEX Proxy |
| 賣權多空淨 OI | +129 | TAIFEX Proxy |
| 賣權多空淨 OI 變化 | unavailable | 換月基準重建 |
- 資料日期：買權 2026-11-18／賣權 2026-11-18 (TypeOfTraders=0 全部交易人；契約月份 202612)

#### 大戶流向（全日；前十大無日夜拆分）

| 項目 | 淨變化 | 區間 | 資料來源 |
|---|---|---|---|
| 期貨前十大 | unavailable | — | 換月基準重建 |
| 買權前十大 | unavailable | — | 換月基準重建 |
| 賣權前十大 | unavailable | — | 換月基準重建 |

### 16．資料來源、時間、時區與狀態

- 資料來源：TAIFEX 經 Cloudflare Worker Proxy
- 資料日期：2026-11-19；本次報告產製時間：2026-11-19 13:51:44；時區：`Asia/Taipei`
- 日盤／夜盤標記：日盤收盤後 + 夜盤盤後
- 換月註記：期貨前十大：前一交易日快照只有舊契約月份，無新主力月份可比基準；換月建立新基準，不跨月相減；買權前十大：前一交易日快照只有舊契約月份，無新主力月份可比基準；換月建立新基準，不跨月相減；賣權前十大：前一交易日快照只有舊契約月份，無新主力月份可比基準；換月建立新基準，不跨月相減
- 部分取得欄位 (1)：turnover.total
- 註記：--force-rewrite 明示覆蓋（人工指定）
- 未取得欄位 (25)：taiex.open, taiex.high, taiex.low, otc_breadth.up, otc_breadth.down, otc_breadth.flat, otc_breadth.limit_up, otc_breadth.limit_down, institutional.foreign, institutional.trust, institutional.dealer, institutional.total, margin.fin_yi, margin.fin_chg_yi, margin.s_bal, margin.s_chg, margin.ratio, sbl.bal, sbl.sale_bal, sbl.sale_chg, turnover.otc, options.chain_oi_change, options.wall_change, futures.top10_change, options.top10_change

## 五、資料來源、時間與完整性

- 台股現貨、TAIFEX 期貨／選擇權以 T0 為基準；海外指數、匯率、ADR、原油、黃金與 Bitcoin 採各來源最新可得報價。各表格均列示實際資料日期；時間皆為 `Asia/Taipei`。
- taiex：`twse-proxy`
- listed_breadth：`twse-proxy`
- listed_turnover：`twse-proxy market_statistics`
- margin_ratio：`unavailable（TWSE 自建、Blave、同 T0 人工輸入皆不可用）`
- sbl_bal：`unavailable`
- sbl_sale_bal_listed：`unavailable`
- sbl_sale_bal_otc：`unavailable`
- sbl_sale_chg_listed：`unavailable`
- sbl_sale_chg_otc：`unavailable`
- sbl_sale_bal：`unavailable`
- sbl_sale_chg：`unavailable`
- 期貨選擇權：`TAIFEX Proxy`
- 新聞：台股 Yahoo／國際 Fed＋CNBC＋MarketWatch；台股 Yahoo（不足時財訊快報備援）/ 國際 Fed 公告＋CNBC＋MarketWatch RSS；Fed 無摘要；investing 港股為主已退役；cnyes CSR、wantgoo JS 算繪、中央社/台灣央行路徑待查，未採用
- 美股/亞股/期貨/匯率/ADR/商品：`Yahoo Finance Chart API`；美債：`Yahoo Finance (備援)`
- 註記：大盤開高低部分欄位未取得 (FinMind T0 欄位缺值；MI_INDEX 無此欄)
- 註記：上櫃 highlight 日期不符或缺值 (回傳 None, T0=1151119)
- 註記：上櫃成交金額歷史備援缺值或日期不符 (T0=1151119)
- 註記：三大法人未取得
- 註記：HiStock 未取得，融資餘額/增減標 unavailable (官方逐股加總僅有張數)
- 註記：上市融資維持率 unavailable；自建計算：ValueError: TWSE margin date mismatch: missing != 20261119；Blave：exact T0 2026-11-19 not found。不影響其他融資融券欄位、DATA_REPORT、JSON 與 Dashboard 產出。
- 註記：上市 MI_MARGN 無日期欄，採用最新可得
- 註記：借券餘額未取得：TWSE TWT72U（SLBNLB）資料日期或欄位驗證失敗
- 註記：借券賣出餘額市場覆蓋不完整；來源欄已明確標示實際取得市場
- 註記：借券賣出增減市場覆蓋不完整；來源欄已明確標示實際取得市場
- 註記：[partial] 成交金額合計僅取得單一市場；不提供不完整的合計數值
- TAIFEX 註記：futures-price-after-hours 日期 2026-11-18 非今日 2026-11-19，視為無新節次，不採用
- TAIFEX 註記：GEX Worker 診斷：code=TXO_CHAIN_PARSE_FAILED；stage=chain_parse；HTTP=502；TXO option chain not found；No usable TXO option-chain rows
- TAIFEX 註記：Call/Put Wall 與 Max Pain 資料日期 2026-11-18 (T0 2026-11-19 端點不穩，採最新可得)
- TAIFEX 註記：Gamma 資料日期 2026-11-18 (T0 2026-11-19 尚無，上游 FMTQIK 落後，採最新可得)
- TAIFEX 註記：期貨三大法人 OI 部分欄位缺值；對應合計標 unavailable
- TAIFEX 註記：法人交易量未提供前日變化端點；日盤、夜盤交易量及日夜淨額差仍照常列示
- TAIFEX 註記：選擇權 chain 資料日期 2026-11-18 (T0 2026-11-19 端點不穩，採最新可得)
- TAIFEX 註記：Gamma 原始端點不可用（上游 502）；已由 options-market-structure-compact (proxy) 備援取得（Wall 有值；Flip 有值）
- TAIFEX 註記：Gamma GEX 實際使用到期月份 202611F3（到期日 2026-11-20）與 Options Key Levels 主到期月份 202611 不同；GEX 數值應以實際使用到期月份為準
- TAIFEX 註記：逐履約價 GEX／Net GEX／Gross GEX 未取得或資料不完整，標 unavailable（不以 Wall/Flip proxy 代替）
- TAIFEX 註記：Gamma Wall/Flip 資料日期 2026-11-18 (來源 options-market-structure-compact (proxy))
- TAIFEX 註記：選擇權 OI 前日變化 unavailable：本日 Chain 實際日期 2026-11-18，T0 應為 2026-11-19；不以遞補舊資料冒充當日資料
- TAIFEX 註記：選擇權 Call Wall／Put Wall／Max Pain 前日變化 unavailable：reason=current_chain_date_mismatch; detail=n/a
- 本報告僅整理資料，不提供交易判斷。

## 六、期現選方向對照

**規則：** 趨勢偏多／空＝現貨、期貨OI、選擇權日淨三者同向；避險／對沖＝現貨與期選反向；日內反轉＝日淨與夜淨反向；缺值標示，不推估。選擇權多空為看多看空口徑。

| 法人 | 現貨買賣超(億) | 期貨OI淨(口) | 期貨日淨 | 期貨夜淨 | 選擇權日淨 | 選擇權夜淨 | 判定 | 期選組合 | 資料來源 |
|---|---|---|---|---|---|---|---|---|---|
| 外資 | unavailable | unavailable | -2,620 | -108 | +6,484 | +284 | 資料不足 | 資料不足 | TAIFEX Proxy |
| 投信 | unavailable | unavailable | +2,347 | +0 | -17,182 | +0 | 資料不足 | 資料不足 | TAIFEX Proxy |
| 自營商 | unavailable | unavailable | -2,486 | +262 | +5,158 | -455 | 資料不足 | 資料不足 | TAIFEX Proxy |
