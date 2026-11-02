# V9 Pro Dashboard 42 區塊單位對照表

版本：1.1（2026-11-02；以最新 Builder 輸出 JSON、DATA_REPORT 與 React Template 複核）  
依使用者指定計數：KPI 整組計 1 區塊；六頁共 42 區塊。

## 總覽（7 區塊）

| # | 區塊 | 欄位／資料 | 單位與規則 |
|---:|---|---|---|
| 1 | KPI 指標群（整組計 1） | 加權收盤、外資現貨、台指日／夜盤、外資期貨、PCR、Call Wall、Bias | 點、億元、點、口、倍、點、分；各 KPI 必須各自標示 |
| 2 | 加權 5 日走勢與關鍵水位 | 指數價格、日漲跌、漲跌幅 | 點、點、% |
| 3 | 三大法人快照 | 外資／投信／自營／合計現貨買賣超 | 億元 |
| 4 | 期選結構快照 | 期貨 OI、選擇權 PCR、GEX | 口、倍；GEX 為 NT$／標的價格變動 1%，屬模型估值 |
| 5 | 美股連動 | 指數漲跌幅、SOX 等指數價格 | %；價格依指數點數 |
| 6 | 重大新聞 | 新聞標題、摘要、時間 | 時間須含來源時區；非數值單位 |
| 7 | Bias／因子狀態摘要 | Bias、有效因子數、權重 | 分、項、相對權重點數／正規化權重%（依欄位定義） |

## 現貨（6 區塊）

| # | 區塊 | 欄位／資料 | 單位與規則 |
|---:|---|---|---|
| 8 | 大盤行情 | 加權 OHLC、漲跌點數、漲跌幅、成交金額 | 點、點、%、億元 |
| 9 | 漲跌家數 | 上市／上櫃上漲、下跌、平盤、漲跌停 | 家 |
| 10 | 三大法人現貨 | 外資、投信、自營、合計 | 億元 |
| 11 | 融資融券 | 融資餘額／增減、融券餘額、維持率 | 億元、張、% |
| 12 | 借券／券 | 借券餘額、借券賣出、賣出增減、融券 | 張；圖表縮放須標明萬張／千張 |
| 13 | 成交結構 | 上市、上櫃、合計成交金額 | 億元 |

## 重要市場（8 區塊）

| # | 區塊 | 欄位／資料 | 單位與規則 |
|---:|---|---|---|
| 14 | 美股指數 | 指數收盤、漲跌幅 | 指數點、% |
| 15 | 亞洲指數 | 指數收盤、漲跌幅 | 指數點、% |
| 16 | 美股期貨 | 合約報價、漲跌幅 | 合約點數、% |
| 17 | 美國公債殖利率 | 殖利率水準、日變化 | %、百分點（pp） |
| 18 | 主要匯率 | 貨幣對報價、漲跌幅 | 明確貨幣對報價單位、% |
| 19 | 台灣 ADR | ADR 報價、漲跌幅 | USD/股、% |
| 20 | 原油／黃金／Bitcoin | 商品／加密資產價格、漲跌幅 | 依來源合約定義；BTC 為 USD/BTC；漲跌幅 % |
| 21 | 重大新聞 | 標題、摘要、時間 | 時間須保留來源時區 |

## 期貨（6 區塊）

| # | 區塊 | 欄位／資料 | 單位與規則 |
|---:|---|---|---|
| 22 | 台指期日盤 | OHLC、漲跌、漲跌幅、成交量、基差 | 點、點、%、口、點 |
| 23 | 台指期夜盤 | OHLC、漲跌、漲跌幅、成交量、夜盤變化 | 點、點、%、口、點 |
| 24 | 期現貨價差 | 基差、正逆價差比例、夜盤變化 | 點、%、點；圖表縮放必須標示除數與還原方式 |
| 25 | 法人 OI | 外資、投信、自營、三大合計、前十大 | 口 |
| 26 | 日夜法人交易 | 外資日／夜淨交易及法人 OI | 口；OI 與交易流量分開說明 |
| 27 | 夜盤劇本 | 日夜收盤、成交量、量能占比、外資夜盤淨交易 | 點、口、%、口 |

## 選擇權（8 區塊）

| # | 區塊 | 欄位／資料 | 單位與規則 |
|---:|---|---|---|
| 28 | PCR／成交量結構 | Call／Put 成交量、OI、PCR、成交量占比 | 口、口、倍（Put OI ÷ Call OI）、% |
| 29 | 主要 OI 集中 | 履約價、OI、現價、Call／Put Wall | 點、口、點 |
| 30 | Call OI 分布 Top10 | 履約價、OI、佔比 | 點、口、% |
| 31 | Put OI 分布 Top10 | 履約價、OI、佔比 | 點、口、% |
| 32 | Call Wall／Put Wall／Gamma／Flip／Max Pain | 各關鍵價位 | 點 |
| 33 | 選擇權法人交易 | `options.instOpt` 日／夜盤多空淨交易；`options.instOptForce` 法人多空力道表 | 交易口數：口；力道金額：億元。前者依 DATA_REPORT 第 17 節，後者依「法人多空力道表」；兩組數值不可混用 |
| 34 | 前十大選擇權 | Call／Put OI 與快照變化 | 口 |
| 35 | 履約價 GEX 分布 | Net／Gross GEX、逐履約價曝險 | NT$／標的價格變動 1%；履約價為點。依 Worker 公式量綱推導，非 TAIFEX 官方欄位 |

## 綜合分析（7 區塊）

| # | 區塊 | 欄位／資料 | 單位與規則 |
|---:|---|---|---|
| 36 | 多空籌碼結構－三市場法人 | 現貨法人買賣超、期貨 OI／日夜淨交易、選擇權法人 | 億元、口；選擇權依來源分口數／金額 |
| 37 | 多空買賣力道 | 法人日／夜多空力道 | 來源表若為金額則億元；若為口數則口，圖表逐數列標示 |
| 38 | 日夜盤劇本 | 日夜收盤、變化、成交量、量能占比、外資 OI | 點、點、口、%、口 |
| 39 | 三劇本路徑 | 現價、Gamma Wall、Call Wall、Put Wall、Flip | 點 |
| 40 | 多空條件檢查表 | Bias、因子分數、有效因子數 | 分、分、項 |
| 41 | 相關性熱圖 | 相關係數 | 無量綱，-1 至 +1 |
| 42 | 交易計畫 | Bias、關鍵價位、進出場／風險界線 | 分、點；價格路徑只標示條件，不虛構勝率 |

## 核對範圍、結果與限制

- 本表已逐區塊列出 1–42 的主要 Dashboard JSON path、DATA_REPORT 章節、單位及資料缺失規則；最新 2026-10-30 Builder JSON 的主要頂層路徑與欄位結構已實際比對。
- 原始資料解析集中於 \`parse_data_report()\`；標準化欄位輸出由 \`build_final_json()\` 組裝；分析衍生卡片由 \`build_41_cards()\` 產生。React 六頁元件再將 JSON path 對應到各顯示區塊。這三層不可混稱為同一個 parser。
- 現貨／期貨／選擇權主要欄位及重要市場陣列結構已由最新 JSON 驗證；重要市場的報價單位依 DATA_REPORT 欄位定義及來源報價方向，並非每一原始列均有獨立 unit 欄。
- 匯率方向：USD/TWD、USD/JPY、USD/KRW 均為每 1 USD 兌本幣；DXY 為指數點。WTI 為 USD／桶、黃金為 USD／金衡盎司、Bitcoin 為 USD／BTC。殖利率水準為 %，日變化為百分點（pp）。
- GEX 單位已由 Worker 生產公式與 DATA_REPORT 14A 明列單位確認為 NT$／標的價格變動 1%；屬 Black-Scholes 模型估值，非 TAIFEX 官方欄位。
- 缺值策略需以實際欄位為準：Builder 保留 \`None\`／\`null\` 的欄位，React 依區塊顯示 unavailable；相關性樣本不足時顯示說明文字，不建立假矩陣。
- 42 區塊表格的結構完整性由 \`test_42_block_registry_and_chart_notes_are_complete\` 驗證；欄位級對照仍需以新資料來源或 schema 變更時重新複核。
- Desktop／Mobile 六頁技術渲染已在本次最新完整建置 HTML 檢查：無 JS page error、無水平溢位；版面人工視覺檢查仍以實際頁面截圖為準。

## 42 區塊資料路徑／來源對照（依目前 React Template 與 DATA_REPORT）

> 路徑以 Dashboard JSON 的 camelCase 欄位為準；Builder 內部解析變數可能使用 snake_case，最終由資料組裝層映射。來源章節以 DATA_REPORT 的實際章節為準。缺值一律顯示 unavailable，不得以 0 代替；若目前 Builder 對特定欄位採預設值，該欄位仍列為待修正風險。

| # | Dashboard JSON path（主要欄位） | DATA_REPORT 來源 | 缺值／單位備註 |
|---:|---|---|---|
| 1 | spot.close/diff/pct; institutional.foreign/all; tx.day/night.c/diff/pct; futures.foreign_oi; options.pcr/callWall; analysis.bias | 一.1、一.3、三.1–3、四.4／11、分析層 | KPI 各欄分別標點／億元／口／倍／分 |
| 2 | spot.spot5, spot.spot5Dates, analysis.levels | 一.1；分析層衍生關鍵水位 | 價格點；缺歷史序列時不可補造 |
| 3 | institutional.foreign/trust/dealer/all | 一.3 | 億元；正負代表買賣超方向 |
| 4 | futures.*; options.pcr; options.netGex1pct/grossGex1pct/gexLevels | 三.3–5、四.4、四.14A | OI 口、PCR 倍、GEX NT$／標的變動 1%；模型品質須獨立顯示 |
| 5 | markets.us, marketPct.usPct | 二.1 | 指數點與漲跌幅 % 分開 |
| 6 | news[] | 一.8／二.8（依頁面新聞來源） | 保留來源、時間、時區；無來源時間不得偽造 |
| 7 | analysis.bias/bias_score/factor_details/factor_quality/weights | 分析層計算 | Bias 分、因子數項、權重依模型定義 |
| 8 | spot.open/high/low/close/diff/pct/vol | 一.1 | 點／%／億元；OHLC 缺值顯示 unavailable |
| 9 | spot.up/down/flat/limit_up/limit_down；spot.otc.up/down/flat/limit_up/limit_down | 一.2.1–2.2 | 家；上市與上櫃分開；上櫃欄位巢狀於 spot.otc |
| 10 | institutional.foreign/trust/dealer/all | 一.3 | 億元 |
| 11 | margin.finance/finance_diff/short/ratio/ratio_status/ratio_source/ratio_source_date | 一.4 | 億元／張／%；維持率須帶來源與日期 |
| 12 | margin.sbl/borrowedSell/borrowedSellDiff/borrowedSellDiffScope/short | 一.5、一.4 | 張；圖表縮放為萬張／千張，表格保留原始張數 |
| 13 | turnover.listed/otc/total | 一.6 | 億元；上市＋上櫃與合計交叉檢查 |
| 14 | markets.us, marketPct.usPct | 二.1 | 收盤指數點、漲跌幅 % |
| 15 | markets.asia, marketPct.asiaPct | 二.2 | 收盤指數點、漲跌幅 % |
| 16 | markets.usFut, marketPct.futPct | 二.3 | 期貨合約報價點、漲跌幅 % |
| 17 | markets.yields, marketPct.yieldPct | 二.4 | 殖利率水準 %；日變化 pp |
| 18 | markets.fx, marketPct.fxPct | 二.5 | USD/TWD、USD/JPY、USD/KRW 以每美元兌本幣；DXY 為指數點 |
| 19 | markets.adr, marketPct.adrPct | 二.6 | USD／股、漲跌幅 % |
| 20 | markets.commodities, marketPct.commPct | 二.7 | WTI USD／桶、黃金 USD／金衡盎司、BTC USD／BTC；依來源合約 |
| 21 | news[] | 二.8 | 時間保留來源時區；文字欄無數值單位 |
| 22 | tx.day.o/h/l/c/diff/pct/vol/basis | 三.1、三.6 | 點／%／口；基差點 |
| 23 | tx.night.o/h/l/c/diff/pct/vol/change | 三.2、三.6 | 點／%／口 |
| 24 | tx.day.basis/prem, tx.night.change | 三.6 | 基差點、價差比例 %、夜盤變化點 |
| 25 | futures.foreign_oi/trust_oi/dealer_oi/top10 | 三.3–4 | 口；淨 OI 不等於當日交易流量 |
| 26 | futures.foreign_day/foreign_night 及法人日夜淨交易欄 | 三.5、三.7 | 口；交易流量與 OI 分開 |
| 27 | tx.day.c/vol, tx.night.c/vol/change, futures.foreign_night | 三.1–2、三.5、三.7 | 價格點、量口、占比 %；圖表混合序列逐項標示 |
| 28 | options.callVol/callOi/putVol/putOi/pcr | 四.2–4 | 口／倍；成交量占比 % 不可當 PCR |
| 29 | options.callOiDist/putOiDist, spot.close, options.callWall/putWall | 四.7–8、四.11–12 | 履約價點、OI 口 |
| 30 | options.callOiDist | 四.7 Top10 | 履約價點、OI 口、占比 % |
| 31 | options.putOiDist | 四.8 Top10 | 履約價點、OI 口、占比 % |
| 32 | options.callWall/putWall/gammaWall/flip/maxPain | 四.11–14 | 全部為點 |
| 33 | options.instOpt, options.instOptForce | 四.17、四.18「法人多空力道表」 | instOpt 交易淨口數＝口；instOptForce 金額力道＝億元，兩者分列 |
| 34 | options.top10Call/top10Put | 四.18 選擇權前十大 | OI 口；快照變化亦為口 |
| 35 | options.netGex1pct/grossGex1pct/gexLevels/gexDate/gexStatus | 四.14A GEX_LEVELS_JSON | GEX NT$／標的變動 1%；履約價點；保留模型品質／日期 |
| 36 | institutional.*; futures.*; options.instOpt／instOptForce | 一.3、三.3–5、四.17–18 | 現貨億元；期貨 OI／淨交易與選擇權 instOpt 為口；instOptForce 為億元 |
| 37 | options.instOptForce | 四.18「法人多空力道表」 | 本區塊各法人日／夜多空力道均為億元；不得混入 options.instOpt 交易口數 |
| 38 | tx.day/night.*; futures.foreign_oi/foreign_day/foreign_night | 三.1–5、三.7 | 價格點、量口、占比 % |
| 39 | spot.close; analysis.levels; options.callWall/putWall/gammaWall/flip/maxPain | 一.1、四.11–14、分析層 | 全部價格水位點 |
| 40 | analysis.bias/bias_score/factor_details/factor_quality | 分析層計算 | 分／項；有效因子數不得把缺失因子當 0 分 |
| 41 | analysis.correlation.labels/matrix | 分析層歷史樣本計算 | 無量綱 [-1,+1]；不足樣本時不可假造矩陣 |
| 42 | analysis.cards 交易計畫欄、analysis.bias、analysis.levels、options.*Wall/flip/maxPain | 分析層計算、四.11–14 | Bias 分、價位點；情境為條件路徑，不代表機率 |

### 本次實際核對邊界

- 已以 DATA_REPORT_20261030 與 dashboards/data-20261030.json 核對現貨、重要市場、期貨、選擇權及 GEX 的實際欄位。
- options.instOpt 是日／夜盤交易淨口數（口）；options.instOptForce 是法人多空力道金額（億元），不可共用同一單位。
- 既有已提交的 dashboards/data-20261030.json 舊快照未包含借券賣出欄位；最新 UI Regression 重新執行 Builder 後的非部署預覽 JSON 已包含 borrowedSell=36,178 張、borrowedSellDiff=-1,273 張及 scope=上櫃（上市 TWT93U 未取得），Dashboard 表格會依 scope 顯示。此項資料鏈以最新 Builder 產出驗證 PASS。
- 重要市場原始 DATA_REPORT 的表格欄位未逐列印出「單位」欄；單位依 DATA_REPORT_TEMPLATE 的章節 schema 與 Yahoo／Treasury 報價慣例解讀，不能宣稱每筆原始列都已由 parser 驗證單位後綴。