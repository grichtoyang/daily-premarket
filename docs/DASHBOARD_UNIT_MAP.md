# V9 Pro Dashboard 42 區塊單位對照表

版本：1.2（2026-11-02；增加逐欄位語義稽核、T0 時間邊界與方向定義）  
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

## 2026-11-02 完整欄位語義稽核

### 稽核規則
- **來源欄位**：確認 DATA_REPORT／API 的欄位意義、日期、口徑與原始單位。
- **Builder**：確認解析欄位、公式、正負號、單位換算、缺值及時間邊界。
- **JSON／Dashboard**：確認欄位名稱、資料型別、顯示單位與卡片敘述不改變原意。
- PASS 代表程式契約與樣本資料可對應；不代表上游供應商所有原始資料均已獨立稽核。
- NOT TESTED 代表需外部來源／多日樣本才能完成的統計或供應商層驗證；不可將其視為 PASS。

### 42 區塊逐項稽核矩陣

| # | 欄位語義核對重點 | 結果 | 稽核結論 |
|---:|---|---|---|
| 1 | KPI 收盤、外資、期貨、PCR、Wall、Bias 的各自單位 | PASS | 價格點、金額億元、口數、PCR 倍、Bias 分分開標示；缺值不以 0 代替 |
| 2 | 五日價格序列與 T0 日期 | PASS | Yahoo／FinMind／SQLite 技術序列統一依 Asia/Taipei 日期截斷至 DATA_REPORT T0；未來日期不進 RSI／MACD／KD／MA 或 spot5 |
| 3 | 三大法人現貨買賣超 | PASS | 正值買超、負值賣超；單位億元；合計與三法人分項執行容差交叉檢查 |
| 4 | 期貨 OI、PCR、GEX | PASS | OI 是部位存量；PCR 固定 Put OI ÷ Call OI；GEX 是模型估值且不作方向性 Bias 因子 |
| 5 | 美股連動 | PASS | SOX 缺值顯示 unavailable；VIX 波動率不納入股票指數廣度；DXY 分開呈現 |
| 6 | 重大新聞 | PASS | 修正第一則事件被跳過；保留 12 則樣本、發布時間及原文連結欄位 |
| 7 | Bias／因子摘要 | PASS | 有效因子數、方向數與正規化權重依實際 active factors；GEX 有值仍因非方向指標而不納入 Bias；factor_quality.disabled_factors 與 missing_factors 分開 |
| 8 | 加權 OHLC、漲跌與成交金額 | PASS | OHLC 價格與漲跌點數分離；close 由 twse-proxy、O/H/L 由 FinMind，皆依 T0；來源分別保留 |
| 9 | 上市／上櫃漲跌家數 | PASS | 上市與上櫃欄位路徑分開；上漲、下跌、平盤、漲跌停單位均為家 |
| 10 | 三大法人現貨 | PASS | 外資、投信、自營商及合計均以億元顯示；不把不同市場口數混入 |
| 11 | 融資融券與維持率 | PASS | 融資金額億元、融券張、維持率%；維持率保留來源、日期、上市估算範圍與 T0 狀態 |
| 12 | 借券／借券賣出 | PASS | 餘額與增減以張呈現；上櫃借券賣出增減範圍明確註記，未取得的上市 TWT93U 不冒充全市場 |
| 13 | 上市／上櫃成交結構 | PASS | 上市、上櫃、合計均為億元；合計與分項執行交叉檢查 |
| 14 | 美股指數 | PASS | 收盤點數與漲跌幅分開；VIX 不當作股票指數 |
| 15 | 亞洲指數 | PASS | 報價點數與漲跌幅分開；不以單日同步漲跌聲稱相關性 |
| 16 | 美股期貨 | PASS | 合約報價與漲跌幅分開；缺值不補零 |
| 17 | 美國公債殖利率 | PASS | 殖利率水準為 %；日變化為百分點 pp，不加錯百分號 |
| 18 | 主要匯率 | PASS | USD/TWD、USD/JPY、USD/KRW 明確標示每美元兌本幣；DXY 為指數點／漲跌幅 |
| 19 | 台灣 ADR | PASS | 報價 USD／股、漲跌幅%；ADR 漲跌幅代理不宣稱為 ADR 溢價 |
| 20 | 原油／黃金／Bitcoin | PASS | WTI USD／桶、黃金 USD／金衡盎司、BTC USD／BTC；不混用現貨與期貨合約名稱 |
| 21 | 重大新聞 | PASS | 與總覽新聞使用同一解析契約；時間與來源連結保留 |
| 22 | 台指期日盤 | PASS | OHLC／基差／漲跌點數為點；成交量及 OI 為口；漲跌幅為 % |
| 23 | 台指期夜盤 | PASS | 夜盤 OHLC、漲跌點數、成交量、相對日盤變化分欄；缺值不補 0 |
| 24 | 期現貨價差 | PASS | 基差點與基差比例%分開；比例缺值維持 null |
| 25 | 法人 OI | PASS | 外資、投信、自營與前十大淨 OI 均為口；屬存量，不與日淨交易直接相減 |
| 26 | 日夜法人交易 | PASS | 日盤／夜盤淨交易為流量口數；與 OI 存量分開命名及顯示 |
| 27 | 夜盤劇本 | PASS | 收盤／高低／變化為點，成交量與法人淨交易為口；價位稱觀察價，不保證支撐 |
| 28 | Call／Put 成交量、OI、PCR | PASS | 成交量與 OI 都是口；PCR 僅為 Put OI／Call OI；成交量占比另為 % |
| 29 | 主要 OI 集中 | PASS | 履約價及現價為點、OI 為口；最大 OI 不自動等同 Wall |
| 30 | Call OI Top10 | PASS | 履約價、OI、占比分別為點、口、%；表頭列不當成資料列 |
| 31 | Put OI Top10 | PASS | 履約價、OI、占比分別為點、口、%；表頭列不當成資料列 |
| 32 | Call／Put／Gamma／Flip／Max Pain | PASS | 各價位均為點；缺值不補硬編碼價位 |
| 33 | 選擇權法人交易與力道 | PASS | options.instOpt 是日夜淨交易口數；options.instOptForce 是多空力道金額億元，兩者不可混用 |
| 34 | 選擇權前十大 | PASS | Call／Put OI 與快照變化均為口；存量與變化欄分開 |
| 35 | 履約價 GEX | PASS | Net／Gross 與逐履約價加總核對；單位 NT$／標的價格變動 1%；模型曝險估值，不是 TAIFEX 官方 GEX，也不是已知造市商真實持倉 |
| 36 | 三市場法人結構 | PASS | 現貨金額億元、期貨／選擇權交易口數分開；一致性只比較方向，不比較不同量綱絕對值 |
| 37 | 多空買賣力道 | PASS | 金額欄億元、交易口數欄口；不將力道金額誤當交易口數 |
| 38 | 日夜盤劇本 | PASS | 價格點、成交量口、占比%及 OI 口分開；存量／流量分開 |
| 39 | 三劇本路徑 | PASS | 價格路徑以點表示；只做條件推演，不虛構機率或勝率 |
| 40 | 多空條件檢查表 | PASS | 因子分數為分、數量為項、權重為%；GEX 不因有數值而自動成為方向因子 |
| 41 | 相關性熱圖 | PASS | Pearson 係數無量綱、範圍 -1 至 +1；完整有效樣本未達 5 筆不產生假矩陣；查詢依 T0 截斷 |
| 42 | 交易計畫 | PASS | Bias 分、價位點；歷史相似樣本只報隔日平均變動與上／下跌比例，不再把下跌比例誤稱為勝率 |

### 本輪已修正的語義缺陷

1. **T0 look-ahead leakage**：原技術資料抓取以 runner 當下日期為終點，歷史 DATA_REPORT 可能混入 T0 之後的行情；Yahoo、FinMind、SQLite 現均以 T0 截斷，歷史學習與相關性亦加 as-of 日期限制。
2. **GEX 方向性誤讀**：原分析器讀取不存在的 options.gex；改讀 options.netGex1pct 保留原始數值，但因 GEX 正負不等同市場多空方向，暫不納入 Bias。
3. **VIX 混入股票廣度**：股票指數廣度排除 VIX；SOX 缺值不再默認為 0；DXY 獨立呈現。
4. **Regime 敘述錯置**：原規則只看單日漲跌幅、外資現貨及 OI PCR，文字卻宣稱跌破／站上月線；已改為如實列出實際門檻。
5. **存量與流量相減**：前十大淨 OI（存量）與外資日盤淨交易（流量）原先直接相減並稱對作口數；已取消不具統計意義的差額。
6. **固定方向敘述**：外資選擇權、現貨法人、三市場一致性與現貨三法人矩陣改依當日實際正負值生成。
7. **歷史相似「勝率」誤稱**：原值實際計算的是隔日負報酬比例，已改為分別顯示隔日上漲比例與下跌比例，不再稱勝率。
8. **新聞首則遺漏**：修正事件解析起點及「原文連結」標籤解析。
9. **技術水位標籤**：原將當日最高／最低直接標成 R3／S1，已改為「當日高點／當日低點」；P 樞紐點仍依 (H+L+C)/3。
10. **缺值與來源描述**：基差比例、夜盤變化缺值改保留 null；技術資料來源改輸出實際 Yahoo／FinMind／SQLite provider，不再固定寫成全部來源。

### 必須保留的模型限制／未測項

- **方向規則屬啟發式，不是統計定律**：PCR 低值、RSI 區間、外資 OI 等 Bias 分數門檻是目前既定模型規則；本輪核對其欄位、量綱與程式實作，不代表已用獨立樣本證明預測力。
- **GEX 是 OI-based Black-Scholes 模型估值**：其正負號取決於模型的 Call／Put 符號假設；缺少實際交易對手持倉方向時，不可聲稱是造市商實際 Net Gamma。
- **上游供應商資料正確性**：程式可驗證日期、格式、欄位、算術關係與跨欄位一致性；無法僅靠單一 DATA_REPORT 證明上游每一筆原始資料無誤。
- **多日預測效能**：因子分數與歷史相似度的策略有效性仍需累積無前視偏誤的樣本及 walk-forward 回測；本次不把語義 PASS 宣稱為策略績效 PASS。
- **最終使用者視覺驗收**：程式與瀏覽器技術測試通過後，仍保留使用者對 42 區塊內容呈現的最後確認。

