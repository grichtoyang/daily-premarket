# DATA_REPORT_20261012

- 報告日期：`2026-10-13`
- T0 交易日期：`2026-10-12`
- 資料產出時間：`2026-10-13 12:50:55`
- 時區：`Asia/Taipei`

---

## 一、現貨

### 1. 台股大盤行情

**資料來源：** `Cloudflare Worker：twse-proxy` (備援 `TWSE OpenAPI MI_INDEX`)

| 項目 | 數值 | 單位 | 資料來源 |
|---|---|---|---|
| 加權指數 | 49,301.96 | 點 | twse-proxy |
| 開盤 | 49,272.08 | 點 | FinMind TaiwanStockPrice TAIEX |
| 最高 | 49,412.90 | 點 | FinMind TaiwanStockPrice TAIEX |
| 最低 | 48,768.82 | 點 | FinMind TaiwanStockPrice TAIEX |
| 收盤 | 49,301.96 | 點 | twse-proxy |
| 漲跌點數 | -11.48 | 點 | twse-proxy |
| 漲跌幅 | -0.02 | % | twse-proxy |
| 成交金額 | 8,945.2 | 億元 | twse-proxy market_statistics |

### 2. 市場漲跌家數

#### 2.1 上市公司

**資料來源：** `Cloudflare Worker：twse-proxy` (備援 `TWSE OpenAPI twtazu_od`)

| 項目 | 家數 | 資料來源 |
|---|---|---|
| 上漲家數 | 538 | twse-proxy |
| 下跌家數 | 451 | twse-proxy |
| 平盤家數 | 86 | twse-proxy |
| 漲停家數 | 25 | twse-proxy |
| 跌停家數 | 2 | twse-proxy |

#### 2.2 上櫃公司

**資料來源：** `TPEX OpenAPI tpex_mainborad_highlight`

| 項目 | 家數 | 資料來源 |
|---|---|---|
| 上漲家數 | 330 | TPEX OpenAPI tpex_mainborad_highlight |
| 下跌家數 | 467 | TPEX OpenAPI tpex_mainborad_highlight |
| 平盤家數 | 71 | TPEX OpenAPI tpex_mainborad_highlight |
| 漲停家數 | 28 | TPEX OpenAPI tpex_mainborad_highlight |
| 跌停家數 | 10 | TPEX OpenAPI tpex_mainborad_highlight |

### 3. 三大法人現貨買賣超

**資料來源：** `TWSE RWD BFI82U`

| 法人別 | 買賣超金額 | 單位 | 資料來源 |
|---|---|---|---|
| 外資 | -522.0 | 億元 | twse-proxy /institutional |
| 投信 | +71.4 | 億元 | twse-proxy /institutional |
| 自營商 | -142.9 | 億元 | twse-proxy /institutional |
| 三大法人合計 | -593.5 | 億元 | twse-proxy /institutional |

### 4. 融資融券

**資料來源：** 上市+上櫃 `HiStock` (金額口徑)；維持率 `istock.tw`；備援官方逐股加總

| 項目 | 數值 | 單位 | 資料來源 |
|---|---|---|---|
| 融資餘額 | 8,816.8 | 億元 | HiStock 上市+上櫃融資融券 (金額口徑) |
| 融資增減 | +73.9 | 億元 | HiStock 上市+上櫃融資融券 (金額口徑) |
| 融券餘額 | 253,795 | 張 | HiStock 上市+上櫃融資融券 (金額口徑) |
| 融券增減 | 1,442 | 張 | HiStock 上市+上櫃融資融券 (金額口徑) |
| 融資維持率 | 196.16 | % | wantgoo 大盤融資維持率 (資料日期 2026-10-12；民間估算；官方無每日序列；gapfill 自動補登) |

### 5. 借券資料

**資料來源：** 上市 `TWSE OpenAPI TWT96U` (可借餘額)、上櫃 `TPEX OpenAPI tpex_margin_sbl`

| 項目 | 數值 | 單位 | 資料來源 |
|---|---|---|---|
| 借券餘額 | 4,518,681 | 張 | TWSE TWT93U + TPEX margin_sbl |
| 借券賣出餘額 | 37,606 | 張 | TWSE TWT93U + TPEX margin_sbl |
| 借券賣出增減 | -2,801 | 張 | TWSE TWT93U + TPEX margin_sbl |

### 6. 市場成交結構

**資料來源：** 上市 `twse-proxy market_statistics`、上櫃 `TPEX OpenAPI tpex_mainborad_highlight`

| 項目 | 成交金額 | 單位 | 資料來源 |
|---|---|---|---|
| 上市成交金額 | 8,945.2 | 億元 | twse-proxy market_statistics |
| 上櫃成交金額 | 2,201.8 | 億元 | TPEX OpenAPI tpex_mainborad_highlight |
| 上市櫃成交金額合計 | 11,147.0 | 億元 | twse-proxy market_statistics+TPEX OpenAPI tpex_mainborad_highlight |

## 二、重要市場

### 1. 美股指數

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 收盤／最新值 | 漲跌點 | 漲跌幅 | 資料來源 |
|---|---|---|---|---|---|
| S&P 500 | ^GSPC | 7,807.24 | -4.30 | -0.06 | Yahoo Finance Chart API |
| Nasdaq Composite | ^IXIC | 27,245.90 | -120.27 | -0.44 | Yahoo Finance Chart API |
| Nasdaq 100 | ^NDX | 30,664.70 | -218.45 | -0.71 | Yahoo Finance Chart API |
| Dow Jones | ^DJI | 51,850.55 | 195.60 | +0.38 | Yahoo Finance Chart API |
| 費城半導體 SOX | ^SOX | 12,236.79 | -335.63 | -2.67 | Yahoo Finance Chart API |
| VIX | ^VIX | 15.21 | 0.37 | +2.49 | Yahoo Finance Chart API |

### 2. 亞洲主要指數

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 收盤／最新值 | 漲跌點 | 漲跌幅 | 資料來源 |
|---|---|---|---|---|---|
| 日經225 | ^N225 | 67,559.54 | -1,471.38 | -2.13 | Yahoo Finance Chart API |
| 韓國KOSPI | ^KS11 | 5,958.31 | -425.93 | -6.67 | Yahoo Finance Chart API |
| 香港恆生 | ^HSI | 24,176.05 | -95.15 | -0.39 | Yahoo Finance Chart API |
| 上海綜合 | 000001.SS | 3,787.16 | -10.08 | -0.27 | Yahoo Finance Chart API |
| 深圳成分 | 399001.SZ | 12,288.40 | -96.47 | -0.78 | Yahoo Finance Chart API |

### 3. 美股指數期貨

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 最新值 | 漲跌點 | 漲跌幅 | 資料來源 |
|---|---|---|---|---|---|
| S&P500期貨 | ES=F | 7,842.25 | -15.75 | -0.20 | Yahoo Finance Chart API |
| Nasdaq100期貨 | NQ=F | 30,656.25 | -242.00 | -0.78 | Yahoo Finance Chart API |
| 道瓊期貨 | YM=F | 52,241.00 | 131.00 | +0.25 | Yahoo Finance Chart API |
| Russell2000期貨 | RTY=F | 2,816.20 | 4.00 | +0.14 | Yahoo Finance Chart API |

### 4. 美國國債殖利率

**資料來源：** `U.S. Treasury Fiscal Data API` (失敗時備援 Treasury yield.xml 與 `Yahoo Finance`)

| 項目 | API 資料欄位／識別 | 殖利率 | 日變化 | 資料來源 |
|---|---|---|---|---|
| 美國 2 年期殖利率 | 2 Yr | 4.80 | 0.05 | U.S. Treasury yield.xml (網頁備援) |
| 美國 10 年期殖利率 | 10 Yr | 5.24 | -0.00 | Yahoo Finance (備援) |
| 美國 30 年期殖利率 | 30 Yr | 5.60 | -0.00 | Yahoo Finance (備援) |

### 5. 主要匯率

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 最新值 | 漲跌點 | 漲跌幅 | 資料來源 |
|---|---|---|---|---|---|
| USD/TWD | TWD=X | 32.08 | 0.15 | +0.48 | Yahoo Finance Chart API |
| DXY美元指數 | DX-Y.NYB | 102.43 | -0.15 | -0.14 | Yahoo Finance Chart API |
| USD/JPY | JPY=X | 158.26 | 0.20 | +0.13 | Yahoo Finance Chart API |
| USD/KRW | KRW=X | 1,342.38 | -0.61 | -0.05 | Yahoo Finance Chart API |

### 6. 台灣相關ADR

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 收盤／最新值 | 漲跌點 | 漲跌幅 | 資料來源 |
|---|---|---|---|---|---|
| 台積電ADR | TSM | 444.35 | -8.96 | -1.98 | Yahoo Finance Chart API |
| 聯電ADR | UMC | 22.55 | -0.41 | -1.79 | Yahoo Finance Chart API |
| 日月光ADR | ASX | 47.53 | 1.10 | +2.37 | Yahoo Finance Chart API |

### 7. 原油黃金Bitcoin

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 收盤／最新值 | 漲跌點 | 漲跌幅 | 資料來源 |
|---|---|---|---|---|---|
| WTI原油期貨 | CL=F | 92.55 | -1.19 | -1.27 | Yahoo Finance Chart API |
| 黃金期貨 | GC=F | 4,217.50 | 26.90 | +0.64 | Yahoo Finance Chart API |
| Bitcoin | BTC-USD | 83,340.13 | -339.34 | -0.41 | Yahoo Finance Chart API |

### 8. 重大經濟數據、央行事件與重大市場新聞

**資料來源：** 台股 `tw.stock.yahoo.com` (含內文摘要)；國際 `Fed 公告 RSS`＋`CNBC`＋`MarketWatch` (標題、來源、時間與連結)

- 事件1：記憶體風暴拖累「韓版0050」跌破發行價摔近7%
  - 來源：Yahoo 台股；發布時間：2026-10-13T04:46:38Z；台北時間：2026-10-13 12:46
  - 摘要：被稱為韓版0050的大華韓國KOSPI50(009829)今日盤中遭逢重挫，股價跌破10元發行價面額，最低跌至9.56元，跌幅高達6.91%，引發市場關注。主因受美股美光與閃迪暴跌拖累，全球半導體與記憶體板塊慘遭重擊，連動三星與SK海力士等
  - 原文連結：https://tw.stock.yahoo.com/news/%E9%9F%93%E7%89%880050%E4%BB%8A%E6%85%98%E8%B7%8C%E7%A0%B4%E7%99%BC-%E9%87%8D%E6%8C%AB6-91-%E5%8E%9F%E5%9B%A0%E6%9B%9D%E5%85%89-042600003.html
- 事件2：台股跳水成交榜綠油油 友達跌逾4% 00406A也承壓
  - 來源：Yahoo 台股；發布時間：2026-10-13T04:27:00Z；台北時間：2026-10-13 12:27
  - 摘要：台股今（13）日盤中加權指數一度重挫逾1200點，隨後跌幅稍微收斂。盤中成交量前五大個股包含友達、國喬、力積電、台塑與聯電，其中友達遭外資大舉砍倉後成交量衝破29萬張，股價下跌超過4%。此外，證交所也公布外資昨日賣超前10大個股名單，台塑、
  - 原文連結：https://tw.stock.yahoo.com/news/%E5%A4%9A%E9%BA%BC%E7%97%9B%E7%9A%84%E9%A0%98%E6%82%9F-%E5%A4%96%E8%B3%87%E5%86%8D%E5%BA%A6%E5%B1%A0%E6%AE%BA-%E9%80%99%E6%AA%94-%E6%88%90%E4%BA%A4%E9%87%8F%E7%88%8629%E8%90%AC%E5%BC%B5%E5%8D%BB%E8%B7%8C%E9%80%BE4-042700721.html
- 事件3：電子股腿軟「金金」發光 分析師曝「631」持股配置
  - 來源：Yahoo 台股；發布時間：2026-10-13T04:06:21Z；台北時間：2026-10-13 12:06
  - 摘要：「金融又變資金避風港了」「金融最後一棒」「老蘇：會說你看吧 漲金融航運就是空頭的開始」「拉金融是要他們出來收傘嗎？選完就知道了」「金融可能會被債券影響喔」「一堆俗辣喊超大聲，還不是躲金融！」「金融：別怕 我在」「感謝高點全換到金融股的自己 
  - 原文連結：https://tw.stock.yahoo.com/news/%E3%80%90hot%E5%8F%B0%E8%82%A1%E3%80%91%E9%87%91%E8%9E%8D%E8%82%A1%E5%8F%88%E6%9C%80%E5%BE%8C%E4%B8%80%E6%A3%92%EF%BC%9F%E7%B6%B2%E5%96%8A%E3%80%8C%E9%82%84%E5%A5%BD%E6%89%8B%E4%B8%8A%E6%9C%89%E8%88%B9%E7%A5%A8%E8%B7%9F%E9%87%91%E9%87%91%E3%80%8D%E5%88%86%E6%9E%90%E5%B8%AB%E6%9B%9D%E6%8C%81%E8%82%A1%E9%85%8D%E7%BD%AE-040621346.html
- 事件4：大盤跌千點 台股成交量榜有9檔是ETF、00406A人氣爆棚
  - 來源：Yahoo 台股；發布時間：2026-10-13T03:30:33Z；台北時間：2026-10-13 11:30
  - 摘要：台股加權指數今（13）一度大跌千點失守4萬9，此時買股不如ETF（指數型基金）？成交量前十大中ETF就占了9檔之多，主動中信台灣收益（00406A）爆近百萬張巨量排名第一，其他像是00685L、00403A、00981A、0050等明星級主
  - 原文連結：https://tw.stock.yahoo.com/news/%E8%B7%8C%E5%8D%83%E9%BB%9E%E8%B2%B7%E8%82%A1%E4%B8%8D%E5%A6%82etf%EF%BC%9F%E5%89%8D%E5%8D%81%E5%A4%A7%E4%BA%BA%E6%B0%A3%E9%9C%B8%E6%A6%9C%E4%B9%9D%E5%B8%AD-%E5%AE%83%E7%88%86%E8%BF%91%E7%99%BE%E8%90%AC%E5%BC%B5%E6%8E%92%E7%AC%AC%E4%B8%80-%E6%8A%95%E9%A1%A7%E8%91%A3%E5%BA%A7%E8%AE%9A%EF%BC%9A%E8%81%B0%E6%98%8E%E6%87%B6%E4%BA%BA%E6%8A%95%E8%B3%87%E6%B3%95-033353120.html
- 事件5：台光電跌停類股低迷 分析師看銅箔基板「基本面不擔心」
  - 來源：Yahoo 台股；發布時間：2026-10-13T03:14:25Z；台北時間：2026-10-13 11:14
  - 摘要：銅箔基板龍頭台光電（2383）今日股價一度重挫至9%，摔破5600元大關，其餘概念股如聯茂（6213）一度閃出綠燈，台燿（6274）也跌逾半根以上，整體表現疲弱。資深分析師謝明哲認為，產業本身並沒有出現問題，反倒是盤面的氣氛導致大漲個股的重
  - 原文連結：https://tw.stock.yahoo.com/news/%E9%8A%85%E7%AE%94%E5%9F%BA%E6%9D%BF%E4%B9%9F%E6%92%90%E4%B8%8D%E4%BD%8F%E8%81%AF%E8%8C%82%E3%80%81%E5%8F%B0%E5%85%89%E9%9B%BB%E6%85%98%E5%90%9E%E8%B7%8C%E5%81%9C-%E5%88%86%E6%9E%90%E5%B8%AB%E7%9C%8B%E6%B3%95%E6%9B%9D-031542064.html
- 事件6：被動元件臉綠、國巨跌逾7% 天二營收續強唯一鎖漲停
  - 來源：Yahoo 台股；發布時間：2026-10-13T02:48:00Z；台北時間：2026-10-13 10:48
  - 摘要：[FTNN新聞網]記者陳思穎／綜合報導台股今（13）日走勢持續低迷，開盤下跌175.69點至49126.27點，盤中最低下探48401.13點，截至上午10點30分，暫報48254.56點...
  - 原文連結：https://tw.stock.yahoo.com/news/%E8%A2%AB%E5%8B%95%E5%85%83%E4%BB%B6%E6%BC%B2%E5%8B%A2%E5%AF%A5%E5%AF%A5-%E9%80%99%E6%AA%94-9%E6%9C%88%E7%87%9F%E6%94%B6%E5%A4%A7%E6%BC%B2132-%E7%9B%A4%E4%B8%AD%E9%A3%86%E6%BC%B2%E5%81%9C-%E8%8F%AF%E6%96%B0%E7%A7%91-024800618.html
- 事件7：Federal Reserve Board releases results of the 2025 Survey of Consumer Finances, which provides the public and policymakers with detailed insights into the economic condition of American families
  - 來源：Federal Reserve；發布時間：Fri, 9 Oct 2026 14:00:00 GMT；台北時間：2026-10-09 22:00
  - 摘要：Federal Reserve Board releases results of the 2025 Survey of Consumer Finances, which provides the public and policymakers with detailed insights into
  - 原文連結：https://www.federalreserve.gov/newsevents/pressreleases/other20261009a.htm
- 事件8：Federal Reserve Board announces enforcement action against American Express Company to address, among other things, the firmâs failure to sufficiently detect and report certain suspicious activity related to money laundering
  - 來源：Federal Reserve；發布時間：Thu, 8 Oct 2026 20:30:00 GMT；台北時間：2026-10-09 04:30
  - 摘要：Federal Reserve Board announces enforcement action against American Express Company to address, among other things, the firmâs failure to sufficient
  - 原文連結：https://www.federalreserve.gov/newsevents/pressreleases/enforcement20261008a.htm
- 事件9：Minutes of the Federal Open Market Committee, September 15-16, 2026
  - 來源：Federal Reserve；發布時間：Wed, 7 Oct 2026 18:00:00 GMT；台北時間：2026-10-08 02:00
  - 摘要：Minutes of the Federal Open Market Committee, September 15-16, 2026
  - 原文連結：https://www.federalreserve.gov/newsevents/pressreleases/monetary20261007a.htm
- 事件10：IMF warns bond yields could see a 'disorderly' spike as debt, inflation risks worsen
  - 來源：CNBC；發布時間：Tue, 13 Oct 2026 03:19:43 GMT；台北時間：2026-10-13 11:19
  - 摘要：The IMF says risks in the government bond market have worsened and that yields could jump sharply and disorderly.
  - 原文連結：https://www.cnbc.com/2026/10/13/treasury-yields-imf-debt-inflation-.html
- 事件11：Rep. Ilhan Omar blasts federal criminal raid on home: 'I will not be silenced'
  - 來源：CNBC；發布時間：Mon, 12 Oct 2026 18:29:28 GMT；台北時間：2026-10-13 02:29
  - 摘要：The Minnesota Democrat, a Muslim who was born in Somalia, has been targeted for criticism in the past by President Donald Trump.
  - 原文連結：https://www.cnbc.com/2026/10/12/ilhan-omar-home-raided-dhs-immigration-investigation.html
- 事件12：Oil prices fall as traders assess Russian diesel supply prospects and Saudi-Houthi conflict
  - 來源：CNBC；發布時間：Tue, 13 Oct 2026 03:49:23 GMT；台北時間：2026-10-13 11:49
  - 摘要：Oil prices fell as investors assess potential supply disruptions against prospects of more Russian diesel entering global markets.
  - 原文連結：https://www.cnbc.com/2026/10/13/oil-prices-today-brent-wti-hormuz.html


## 三、期貨

**資料來源：**
1. Cloudflare Workers：TAIFEX Proxy — https://taifex.grichtoyang.workers.dev/
2. TAIFEX Open API — https://openapi.taifex.com.tw/

近月契約月份：202610 (日盤成交量最大者)；交易日期：2026-10-12

### 1．台指期近月日盤行情

| 項目 | 數值 | 資料來源 |
|---|---|---|
| 開盤價 | 48,975 | TAIFEX Proxy |
| 最高價 | 49,594 | TAIFEX Proxy |
| 最低價 | 48,910 | TAIFEX Proxy |
| 收盤價 | 49,309 | TAIFEX Proxy |
| 漲跌點數 | -48 | TAIFEX Proxy |
| 漲跌幅 | -0.10 | TAIFEX Proxy |
| 成交量 | 83,737 | TAIFEX Proxy |
| 日盤高點及低點 | 49,594 / 48,910 | TAIFEX Proxy |

### 2．台指期近月夜盤行情

| 項目 | 數值 | 資料來源 |
|---|---|---|
| 開盤價 | 49,275 | TAIFEX Proxy |
| 最高價 | 49,422 | TAIFEX Proxy |
| 最低價 | 48,881 | TAIFEX Proxy |
| 收盤價 | 48,946 | TAIFEX Proxy |
| 漲跌點數 | -399 | TAIFEX Proxy |
| 漲跌幅 | -0.81 | TAIFEX Proxy |
| 成交量 | 19,781 | TAIFEX Proxy |
| 夜盤高點及低點 | 49,422 / 48,881 | TAIFEX Proxy |
| 結算價 | 49,345 | TAIFEX Proxy |
| 未平倉量 | 106,900 | TAIFEX Proxy |

### 3．法人台指期多空未平倉部位

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 外資多方 OI | 11,899 | TAIFEX Proxy |
| 外資空方 OI | 94,705 | TAIFEX Proxy |
| 外資多空淨 OI | -82,806 | TAIFEX Proxy |
| 投信多方 OI | 79,560 | TAIFEX Proxy |
| 投信空方 OI | 2,712 | TAIFEX Proxy |
| 投信多空淨 OI | +76,848 | TAIFEX Proxy |
| 自營商多方 OI | 4,783 | TAIFEX Proxy |
| 自營商空方 OI | 4,636 | TAIFEX Proxy |
| 自營商多空淨 OI | +147 | TAIFEX Proxy |
| 三大法人合計多方 OI | 96,242 | TAIFEX Proxy |
| 三大法人合計空方 OI | 102,053 | TAIFEX Proxy |
| 三大法人合計多空淨 OI | -5,811 | TAIFEX Proxy |
| 外資多空淨 OI 變化 | +388 | TAIFEX Proxy |
| 投信多空淨 OI 變化 | +509 | TAIFEX Proxy |
| 自營商多空淨 OI 變化 | +681 | TAIFEX Proxy |

### 4．前十大交易人多空未平倉部位

**資料來源：** `TAIFEX OpenAPI OpenInterestOfLargeTradersFutures` (官方資料落後約一日，標示實際日期)

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 前十大交易人多方 OI | 82,061 | TAIFEX Proxy |
| 前十大交易人空方 OI | 76,208 | TAIFEX Proxy |
| 前十大交易人多空淨 OI | +5,853 | TAIFEX Proxy |
| 多空淨 OI 變化 (2026-10-07→2026-10-12) | -1,689 | TAIFEX Proxy snapshots (2026-10-08) |
- 資料日期：2026-10-12 (TypeOfTraders=0 全部交易人；契約月份 202610)

### 5．日盤、夜盤法人交易資料

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 外資日盤多單交易量 | 47,775 | TAIFEX Proxy |
| 外資日盤空單交易量 | 47,132 | TAIFEX Proxy |
| 外資日盤多空淨交易量 | +643 | TAIFEX Proxy |
| 外資夜盤多單交易量 | 10,314 | TAIFEX Proxy |
| 外資夜盤空單交易量 | 11,428 | TAIFEX Proxy |
| 外資夜盤多空淨交易量 | -1,114 | TAIFEX Proxy |
| 外資日盤／夜盤交易量變化 | +1,757 | TAIFEX Proxy |
| 投信日盤多空淨交易量 | +509 | TAIFEX Proxy |
| 投信夜盤多空淨交易量 | +0 | TAIFEX Proxy |
| 投信日盤／夜盤交易量變化 | +509 | TAIFEX Proxy |
| 自營商日盤多空淨交易量 | +667 | TAIFEX Proxy |
| 自營商夜盤多空淨交易量 | +221 | TAIFEX Proxy |
| 自營商日盤／夜盤交易量變化 | +446 | TAIFEX Proxy |
| 三大法人日盤多空淨交易量 | +1,819 | TAIFEX Proxy |
| 三大法人夜盤多空淨交易量 | -893 | TAIFEX Proxy |
| 法人日盤交易金額淨額 (億元) | +177.6 | TAIFEX Proxy |
| 法人夜盤交易金額淨額 (億元) | -87.8 | TAIFEX Proxy |

### 6．期貨與現貨關係

| 項目 | 數值 | 資料來源 |
|---|---|---|
| 台指期近月價格 | 49,309 | TAIFEX Proxy |
| 加權指數價格 | 49,301.96 | twse-proxy |
| 台指期與加權指數價差 | +7.04 | TAIFEX Proxy+twse-proxy |
| 價差百分比 | +0.01 | TAIFEX Proxy+twse-proxy |
| 日盤基差 | +7.04 | TAIFEX Proxy+twse-proxy |
| 夜盤價格相對日盤收盤的變化 | -363 | TAIFEX Proxy |

### 7．日盤、夜盤與籌碼變化對照

#### 7.1 日夜盤價格與成交量對照 (變化 = 日盤 - 夜盤)

| 項目 | 日盤 | 夜盤 | 變化 (日-夜) | 資料來源 |
|---|---|---|---|---|
| 收盤價 | 49,309 | 48,946 | +363 | TAIFEX Proxy |
| 成交量 | 44,296 | 19,781 | +24,515 | TAIFEX Proxy |
- 台指期總 OI 前日變化：+1,578（來源：TAIFEX Proxy）


#### 7.2 法人籌碼日夜盤對照 (淨變化 = 日盤淨 - 夜盤淨；OI 為日盤收盤後總量，前日變化另列)

| 法人 | 交易量 |  |  |  |  |  |  | 未平倉量 |  |  |  | 資料來源 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|  | **日盤多單** | **日盤空單** | **日盤淨** | **夜盤多單** | **夜盤空單** | **夜盤淨** | **淨變化 (日-夜)** | **OI多方** | **OI空方** | **OI淨** | **OI前日變化** |  |
| 外資 | 47,775 | 47,132 | +643 | 10,314 | 11,428 | -1,114 | +1,757 | 11,899 | 94,705 | -82,806 | +388 | TAIFEX Proxy |
| 投信 | 2,063 | 1,554 | +509 | 0 | 0 | +0 | +509 | 79,560 | 2,712 | +76,848 | +509 | TAIFEX Proxy |
| 自營商 | 5,473 | 4,806 | +667 | 776 | 555 | +221 | +446 | 4,783 | 4,636 | +147 | +681 | TAIFEX Proxy |
| 三大法人合計 | 55,311 | 53,492 | +1,819 | 11,090 | 11,983 | -893 | +2,712 | 96,242 | 102,053 | -5,811 | +1,578 | TAIFEX Proxy |

#### 7.3 前十大交易人日夜盤對照 (OI 無日夜拆分，列收盤後總量)

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 前十大交易人多方 OI | 82,061 | TAIFEX Proxy |
| 前十大交易人空方 OI | 76,208 | TAIFEX Proxy |
| 前十大交易人多空淨 OI | +5,853 | TAIFEX Proxy |
| 前十大交易人多空淨 OI 變化 (2026-10-07→2026-10-12) | -1,689 | TAIFEX Proxy snapshots (2026-10-08) |

#### 7.4 夜盤劇本分類 (規則對應：夜盤漲跌 × 外資夜盤偏多空)

| 項目 | 數值 | 資料來源 |
|---|---|---|
| 夜盤成交量占比 (夜盤量／(夜盤量＋日盤量)) | 30.87% | TAIFEX Proxy |
| 夜盤漲跌點數 | -399 | TAIFEX Proxy |
| 外資夜盤多空淨交易量 | -1,114 | TAIFEX Proxy |
| 劇本分類 | 劇本三 | 規則對應 |
| 劇本條件 | 夜盤下跌＋外資偏空 | 規則對應 |
| 劇本特徵 | 開低、續跌機率高 | 規則對應 |

## 四、選擇權

**資料來源：** 主要 TAIFEX 經 Cloudflare Worker Proxy；時區 `Asia/Taipei`

### 1．選擇權交易日期、到期日與資料時間

| 項目 | 數值 | 資料來源 |
|---|---|---|
| 交易日期 | 2026-10-12 | TAIFEX Proxy |
| 到期月份／到期日 | 202610F2 | TAIFEX Proxy |
| 資料更新時間 | 2026-10-13 12:50:55 | 本機 |
| 日盤／夜盤標記 | 日盤收盤後資料 | TAIFEX Proxy |

### 2．Call 總成交量、OI、OI 增減

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Call 總成交量 | 280,654 | TAIFEX Proxy |
| Call 總未平倉量 OI | 54,429 | TAIFEX Proxy |
| Call OI 增減 (2026-10-08→2026-10-12) | +12,161 | TAIFEX Proxy snapshots (2026-10-08) |

### 3．Put 總成交量、OI、OI 增減

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Put 總成交量 | 295,175 | TAIFEX Proxy |
| Put 總未平倉量 OI | 54,199 | TAIFEX Proxy |
| Put OI 增減 (2026-10-08→2026-10-12) | +27,438 | TAIFEX Proxy snapshots (2026-10-08) |

### 4．Call／Put 比例與變化

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Call／Put 成交量比例 | 0.95 | TAIFEX Proxy |
| Call／Put 未平倉量比例 | 1.00 | TAIFEX Proxy |
| Put／Call Ratio | 1.00 | TAIFEX Proxy |
| Call／Put 比例變化 (量比 2026-10-08→2026-10-12) | 15.21 | TAIFEX Proxy |
| 與前一交易日比較 (OI 比 2026-10-08→2026-10-12) | 4.60 | TAIFEX Proxy |
**資料來源：** 比例 `TAIFEX Proxy chain`；變化 `TAIFEX Proxy PutCallRatio`

### 5．外資 Call／Put 部位

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 外資 Call日買 | 95,635 | TAIFEX Proxy |
| 外資 Call日賣 | 95,307 | TAIFEX Proxy |
| 外資 Call日淨 | +328 | TAIFEX Proxy |
| 外資 Put日買 | 105,662 | TAIFEX Proxy |
| 外資 Put日賣 | 111,299 | TAIFEX Proxy |
| 外資 Put日淨 | -5,637 | TAIFEX Proxy |
| 外資 Call夜買 | 22,051 | TAIFEX Proxy |
| 外資 Call夜賣 | 22,463 | TAIFEX Proxy |
| 外資 Call夜淨 | -412 | TAIFEX Proxy |
| 外資 Put夜買 | 18,504 | TAIFEX Proxy |
| 外資 Put夜賣 | 18,397 | TAIFEX Proxy |
| 外資 Put夜淨 | +107 | TAIFEX Proxy |
| 外資 日盤淨總量 | +5,965 | TAIFEX Proxy |
| 外資 Call日夜淨增減 (日－夜) | +740 | TAIFEX Proxy |
| 外資 Put日夜淨增減 (日－夜) | -5,744 | TAIFEX Proxy |

### 6．自營商 Call／Put 部位

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 自營商 Call日買 | 90,212 | TAIFEX Proxy |
| 自營商 Call日賣 | 92,681 | TAIFEX Proxy |
| 自營商 Call日淨 | -2,469 | TAIFEX Proxy |
| 自營商 Put日買 | 96,811 | TAIFEX Proxy |
| 自營商 Put日賣 | 95,561 | TAIFEX Proxy |
| 自營商 Put日淨 | +1,250 | TAIFEX Proxy |
| 自營商 Call夜買 | 16,037 | TAIFEX Proxy |
| 自營商 Call夜賣 | 17,065 | TAIFEX Proxy |
| 自營商 Call夜淨 | -1,028 | TAIFEX Proxy |
| 自營商 Put夜買 | 14,153 | TAIFEX Proxy |
| 自營商 Put夜賣 | 12,847 | TAIFEX Proxy |
| 自營商 Put夜淨 | +1,306 | TAIFEX Proxy |
| 自營商 日盤淨總量 | -3,719 | TAIFEX Proxy |
| 自營商 Call日夜淨增減 (日－夜) | -1,441 | TAIFEX Proxy |
| 自營商 Put日夜淨增減 (日－夜) | -56 | TAIFEX Proxy |

### 7．主要 Call OI 集中區

| 項目 | 履約價 | OI | 資料來源 |
|---|---|---|---|
| Call OI 第1大履約價 | 53,400 | 3,632 | TAIFEX Proxy |
| Call OI 第2大履約價 | 49,400 | 3,228 | TAIFEX Proxy |
| Call OI 第3大履約價 | 50,000 | 2,417 | TAIFEX Proxy |
| Call OI 最大履約價 | 53,400 | 3,632 | TAIFEX Proxy |

#### Call OI 分布明細 Top10 (機器可讀，到期月份 202610F2)

| # | 履約價 | OI | 佔比 | 資料來源 |
|---|---|---|---|---|
| C1 | 53,400 | 3,632 | 6.67% | TAIFEX Proxy |
| C2 | 49,400 | 3,228 | 5.93% | TAIFEX Proxy |
| C3 | 50,000 | 2,417 | 4.44% | TAIFEX Proxy |
| C4 | 49,500 | 2,143 | 3.94% | TAIFEX Proxy |
| C5 | 53,000 | 1,757 | 3.23% | TAIFEX Proxy |
| C6 | 49,200 | 1,690 | 3.1% | TAIFEX Proxy |
| C7 | 51,200 | 1,652 | 3.04% | TAIFEX Proxy |
| C8 | 49,300 | 1,609 | 2.96% | TAIFEX Proxy |
| C9 | 49,350 | 1,553 | 2.85% | TAIFEX Proxy |
| C10 | 49,900 | 1,507 | 2.77% | TAIFEX Proxy |


### 8．主要 Put OI 集中區

| 項目 | 履約價 | OI | 資料來源 |
|---|---|---|---|
| Put OI 第1大履約價 | 49,350 | 3,520 | TAIFEX Proxy |
| Put OI 第2大履約價 | 49,200 | 3,425 | TAIFEX Proxy |
| Put OI 第3大履約價 | 49,000 | 3,299 | TAIFEX Proxy |
| Put OI 最大履約價 | 49,350 | 3,520 | TAIFEX Proxy |

#### Put OI 分布明細 Top10 (機器可讀，到期月份 202610F2)

| # | 履約價 | OI | 佔比 | 資料來源 |
|---|---|---|---|---|
| P1 | 49,350 | 3,520 | 6.49% | TAIFEX Proxy |
| P2 | 49,200 | 3,425 | 6.32% | TAIFEX Proxy |
| P3 | 49,000 | 3,299 | 6.09% | TAIFEX Proxy |
| P4 | 49,300 | 3,247 | 5.99% | TAIFEX Proxy |
| P5 | 49,100 | 2,832 | 5.23% | TAIFEX Proxy |
| P6 | 48,900 | 2,228 | 4.11% | TAIFEX Proxy |
| P7 | 49,150 | 2,189 | 4.04% | TAIFEX Proxy |
| P8 | 49,250 | 2,035 | 3.75% | TAIFEX Proxy |
| P9 | 48,700 | 1,983 | 3.66% | TAIFEX Proxy |
| P10 | 48,800 | 1,968 | 3.63% | TAIFEX Proxy |


### 9．Call OI 增減集中區

| 項目 | 履約價 (增減口數) | 資料來源 |
|---|---|---|
| Call OI 增加最多的履約價 | 49,400 (+2,612) | TAIFEX Proxy snapshots (2026-10-08) |
| Call OI 減少最多的履約價 | 50,400 (-869) | TAIFEX Proxy snapshots (2026-10-08) |

### 10．Put OI 增減集中區

| 項目 | 履約價 (增減口數) | 資料來源 |
|---|---|---|
| Put OI 增加最多的履約價 | 49,350 (+3,282) | TAIFEX Proxy snapshots (2026-10-08) |
| Put OI 減少最多的履約價 | 46,800 (-393) | TAIFEX Proxy snapshots (2026-10-08) |

### 11．Call Wall

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Call Wall 價位 | 53,400 | TAIFEX Proxy |
| 對應到期月份 | 202610F2 | TAIFEX Proxy |
| 與前一交易日的變化 (2026-10-08→2026-10-12) | +0 | TAIFEX Proxy snapshots (2026-10-08) |

### 12．Put Wall

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Put Wall 價位 | 49,350 | TAIFEX Proxy |
| 對應到期月份 | 202610F2 | TAIFEX Proxy |
| 與前一交易日的變化 (2026-10-08→2026-10-12) | +350 | TAIFEX Proxy snapshots (2026-10-08) |

### 13．Gamma Wall

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Gamma Wall 價位 | 49,500.00 | TAIFEX Proxy (options-market-structure-compact (proxy)) |
| 對應到期月份 | 202610F2 | TAIFEX Proxy |
| 資料日期 | 2026-10-12 | TAIFEX Proxy (options-market-structure-compact (proxy)) |

### 14．Gamma Flip

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Gamma Flip 價位 | 48,946.81 | TAIFEX Proxy (options-market-structure-compact (proxy)) |
| 對應到期月份 | 202610F2 | TAIFEX Proxy |
| 資料日期 | 2026-10-12 | TAIFEX Proxy (options-market-structure-compact (proxy)) |

### 15．Max Pain

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Max Pain 價位 | 49,250 | TAIFEX Proxy |
| 對應到期月份 | 202610F2 | TAIFEX Proxy |
| 與前一交易日的變化 (2026-10-08→2026-10-12) | +50 | TAIFEX Proxy snapshots (2026-10-08) |

### 17．選擇權法人日盤、夜盤交易

| 法人 | 日盤多單 | 日盤空單 | 日盤淨 | 夜盤多單 | 夜盤空單 | 夜盤淨 | 淨變化 (日-夜) | 資料來源 |
|---|---|---|---|---|---|---|---|---|
| 外資 | 206,934 | 200,969 | +5,965 | 40,448 | 40,967 | -519 | +6,484 | TAIFEX Proxy |
| 投信 | 0 | 5,030 | -5,030 | 0 | 0 | +0 | -5,030 | TAIFEX Proxy |
| 自營商 | 185,773 | 189,492 | -3,719 | 28,884 | 31,218 | -2,334 | -1,385 | TAIFEX Proxy |
| 三大法人合計 | 392,707 | 395,491 | -2,784 | 69,332 | 72,185 | -2,853 | +69 | TAIFEX Proxy |
- 方法論：多方＝買Call＋賣Put（看多），空方＝賣Call＋買Put（看空），淨額＝看多－看空（已用 Call／Put 拆分頁交叉驗算一致）
- 公式：多方(買)－空方(賣)＝（買call＋賣put）－（賣call＋買put）＝看多－看空
- 速記：多＝BC＋SP、空＝SC＋BP

#### 法人多空力道表（金額・億元；上游千元／1e5）

| 法人 | 日多方力道 | 日空方力道 | 日淨多空力道 | 夜多方力道 | 夜空方力道 | 夜淨多空力道 | 日淨－夜淨 | 資料來源 |
|---|---|---|---|---|---|---|---|---|
| 外資 | 9.78 | 9.36 | +0.41 | 3.28 | 3.35 | -0.07 | +0.48 | TAIFEX Proxy |
| 投信 | 0.00 | 3.78 | -3.78 | 0.00 | 0.00 | +0 | -3.78 | TAIFEX Proxy |
| 自營商 | 12.81 | 10.14 | +2.66 | 1.80 | 2.30 | -0.50 | +3.17 | TAIFEX Proxy |
| 三大法人合計 | 22.58 | 23.28 | -0.70 | 5.08 | 5.65 | -0.57 | -0.13 | TAIFEX Proxy |

### 18．選擇權前十大

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 買權多方 OI | 13,946 | TAIFEX Proxy |
| 買權空方 OI | 12,731 | TAIFEX Proxy |
| 買權多空淨 OI | +1,215 | TAIFEX Proxy |
| 買權多空淨 OI 變化 (2026-10-07→2026-10-12) | -492 | TAIFEX Proxy snapshots (2026-10-08) |

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 賣權多方 OI | 10,922 | TAIFEX Proxy |
| 賣權空方 OI | 10,928 | TAIFEX Proxy |
| 賣權多空淨 OI | -6 | TAIFEX Proxy |
| 賣權多空淨 OI 變化 (2026-10-07→2026-10-12) | -53 | TAIFEX Proxy snapshots (2026-10-08) |
- 資料日期：買權 2026-10-12／賣權 2026-10-12 (TypeOfTraders=0 全部交易人；契約月份 202610)

#### 大戶流向（全日；前十大無日夜拆分）

| 項目 | 淨變化 | 區間 | 資料來源 |
|---|---|---|---|
| 期貨前十大 | -1,689 | 2026-10-07→2026-10-12 | TAIFEX Proxy snapshots (2026-10-08) |
| 買權前十大 | -492 | 2026-10-07→2026-10-12 | TAIFEX Proxy snapshots (2026-10-08) |
| 賣權前十大 | -53 | 2026-10-07→2026-10-12 | TAIFEX Proxy snapshots (2026-10-08) |

### 16．資料來源、時間、時區與狀態

- 資料來源：TAIFEX 經 Cloudflare Worker Proxy
- 資料日期：2026-10-12；資料時間：2026-10-13 12:50:55；時區：`Asia/Taipei`
- 日盤／夜盤標記：日盤收盤後 + 夜盤盤後
- 註記：同 T0 保護：4 格沿用前版有值（本次抓取缺失不覆寫）
- 未取得欄位 (0)：無
- 註記：futures-price-after-hours 日期 2026-10-12 非今日 2026-10-13，視為無新節次，不採用
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
- margin_ratio：`前值遞補 (DATA 2026-10-08；當日三源皆失敗；民間估算；官方無每日序列)`
- sbl：`TWSE TWT93U + TPEX margin_sbl`
- 期貨選擇權：`TAIFEX Proxy`
- 新聞：台股 Yahoo／國際 Fed＋CNBC＋MarketWatch；台股 Yahoo（不足時財訊快報備援）/ 國際 Fed 公告＋CNBC＋MarketWatch RSS；Fed 無摘要；investing 港股為主已退役；cnyes CSR、wantgoo JS 算繪、中央社/台灣央行路徑待查，未採用
- 美股/亞股/期貨/匯率/ADR/商品：`Yahoo Finance Chart API`；美債：`Yahoo Finance (備援)`
- 註記：融資維持率未取得 (三源皆失敗；官方無每日序列)
- 註記：融資維持率採前值遞補 (DATA 2026-10-08)，非 T0 2026-10-12
- 註記：上市 MI_MARGN / TWT96U 無日期欄，採用最新可得
- 註記：借券賣出增減僅上櫃值 (TWSE TWT93U 未取得)
- 本報告僅整理資料，不提供交易判斷。

## 六、期現選方向對照

**規則：** 趨勢偏多／空＝現貨、期貨OI、選擇權日淨三者同向；避險／對沖＝現貨與期選反向；日內反轉＝日淨與夜淨反向；缺值標示，不推估。選擇權多空為看多看空口徑。

| 法人 | 現貨買賣超(億) | 期貨OI淨(口) | 期貨日淨 | 期貨夜淨 | 選擇權日淨 | 選擇權夜淨 | 判定 | 期選組合 | 資料來源 |
|---|---|---|---|---|---|---|---|---|---|
| 外資 | -522.0 | -82,806 | +643 | -1,114 | +5,965 | -519 | 避險／對沖 | 分歧 | twse-proxy／TAIFEX Proxy |
| 投信 | +71.4 | +76,848 | +509 | +0 | -5,030 | +0 | 避險／對沖 | 分歧 | twse-proxy／TAIFEX Proxy |
| 自營商 | -142.9 | +147 | +667 | +221 | -3,719 | -2,334 | 避險／對沖 | 分歧 | twse-proxy／TAIFEX Proxy |
