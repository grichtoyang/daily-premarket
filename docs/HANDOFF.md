# HANDOFF — 每日盤前分析（2026-09-23）

交接日期：2026-09-23 深夜｜當前 session 模型：muse-spark（新對話，已完整掌握專案）

## 一句話現況
0923 日盤報告已 gate PASS 並 push（`5328ccc`）；深夜檢討抓出附錄 Put 分布抄錯已修（`bd2721d`）＋閘門補 oidist 核數規則（`4ca66d1`）；Phase 2 待動工。

## 系統與憑證
- Repo：`https://github.com/grichtoyang/daily-premarket`（Public）；本地 `D:\Opencode\Proj\每日盤前分析`
- Dashboard：`https://daily-premarket.streamlit.app/`
- TAIFEX Proxy：`https://taifex.grichtoyang.workers.dev/`（V1.4，已部署：夜盤 queryDate 修正、snapshot chain 重試、`/options-day-call-put`）
- TWSE Proxy：`https://twse-proxy.grichtoyang.workers.dev/`（V1.1）
- Workflow：08:00 全日班、19:00 日盤班（`Asia/Taipei` 週一～五＋週六 08:00）；晚上重跑只定版一次

## T0 與夜盤規則（已驗證）
- T0：日盤 08:45~13:45；夜盤 T0 15:00 → T+1 05:00，歸屬**開盤日**
- 夜盤查詢：一律查**今天**（今晨收盤那一節；舊規則全日→T0+1 在平日等於今天，假日後分歧而取到回退舊值，2026-10-08 教訓）；proxy 用 `queryDate=YYYY/MM/DD&marketCode=1&MarketCode=1`（`date=`／`Session=F` 無效）
- 假日前一晚可能無夜盤（如 2026-09-24 晚因中秋無交易）：proxy 查無資料會回退最新可得（`requested_date≠date` 可驗），程式無誤；報告須標註節次歸屬，不可逕寫「完整一節」
- 結算價≠收盤價：夜漲跌＝夜收−前結算（如 48497−48225＝+272）

## 選擇權方法論（定版）
- 多方＝BC+SP（看多），空方＝SC+BP（看空），淨＝多−空
- 力道表用**金額**（億元）；口數與金額背離時以金額為準
- 六、期現選方向矩陣＋「期選組合判讀」欄在 DATA/report §7.3
- §17 總表（口數版）保留；§6.9 前十大、§6.8 力道/大戶流向已上線

## 已完成（近期 commit）
- `6a582e5` 夜盤 proxy 修正；`ffa1576` §5/6 完整版+力道表+大戶流向+六組合欄
- `d618912` `/options-day-call-put`；`da28767` 維持率前值遞補+P/C proxy 重試
- `710ba69` 0922 全日報告；`5328ccc` **0923 日盤報告**＋DATA0922速記＋`docs/PHASE2.md`
- `bd2721d` 修 0923 日盤：附錄 oidist Put 10 筆抄錯月份→對齊 DATA＋§7.3 補期選組合欄＋§6.8 外資背離註記＋47800 Gamma 誤植
- `4ca66d1` 閘門補強：`check_report.py` 新增 oidist 履約價+OI 逐筆核對 DATA（舊版重跑會 FAIL 並點名 10 筆）
- 教訓：閘門舊規則只計 oidist 筆數不核數，手寫抄錯攔不住；已用機器交叉驗算確認 MATCH

## 待辦
1. **Phase 2**（見 `docs/PHASE2.md`，待用戶批准）：遠月 OI 掃描陽春版；台股 VIX 找機讀源（目前判定無源不做）
2. 明早驗證 chain OI 增減、前十大上游穩定
3. Muse session（`ses_f556...`）上游 `invalid_request_error` 無法回應——開**新對話**用 `/models` 換 Muse，勿 resume 舊對話
4. 未追蹤檔 `test_form.py`、`test_yahoo.py` 不動
5. 選擇權呈現四分類已定版實作（綜合判斷／市場結構／市場風向／市場情緒＋備查；模板 §6＋dashboard；T字吸附上色；台股 VIX 改連結呈現）

## 發布閘門（必跑，2026-09-23 深夜已加 oidist 核數）
```
python src/check_report.py --data data_reports/DATA_REPORT_YYYYMMDD.md --report reports/Daily_REPORT_YYYYMMDD_日盤.md
```
PASS → 更新 `reports/latest.json` → commit push（新 fix 走新 commit，不 amend 已發布紀錄）
慣例：寫報告時 DATA 有 unavailable 即做最後救援（驗源站→補登 DATA→重跑閘門），報告數字恆⊆DATA（見 docs/SOP.md 3.5）

## 環境注意
- PowerShell：用 `curl.exe`；無 `grep`/`head`；CJK 用 `$env:PYTHONIOENCODING='utf-8'`
- git `.git/objects` 偶發 Permission denied → 分開重試 add/commit
- 21:30 後 Yahoo 浮動，勿反覆重跑
- 維持率 runner 端間歇被擋（wantgoo 前有 Cloudflare，同 T0 多次 run 結果不一，本機全通）：`_prev_data_ratio` 已改往前找最近有數值；失敗日誌含 HTTP code；仍缺時手動補登（2026-09-25 補 0924 值 193.87 前例）
- 本機排程為主力（2026-10-01 建 DailyPremarket0800，每日 07:55 跑 scripts/daily_fetch.py＋推送，住宅 IP；Actions 08:00 為備援；筆電已開 WakeToRun＋StartWhenAvailable＋電池可跑，電源選項喚醒計時器用戶自查；首跑 10/2）
- worker 快照 chain 連空（09-23 起）：cron 14:30 撞日報未發布（walls 同死）；2026-09-30 用戶已改 Cron Trigger 為 `30 7 * * 1-5`（台北 15:30）；10/2 驗收快照 chain；勿碰 write-now（會拿現在 chain 蓋舊日期污染標籤）
- 新聞增財訊快報備援（TodayNews Big5＋articleNo 日期＋內文；Yahoo 不足時補位；已單測）
- 報告起草機 src/draft_blocks.py（數字全自動＋解讀全人工；附錄B＋§6草稿；三份 DATA 實測＋閘門格式驗證；下次開工即用）

## 2026-10-07 追加（T0=2026-10-06 全日，已發布 `ea82d25`）
- 報告 `reports/Daily_REPORT_20261006_全日.md` gate RC=0 PASS＋push；`latest.json` 指到 20261006；Dashboard 約 1~2 分鐘更新。
- 關鍵數：加權 49,822.55（+110.51）距 5 萬 31 點；前十大淨多縮水至 +6,112（+2,335，10-02→10-06）；維持率補登 200.72（wantgoo 10-05）；美期漲跌互見（NQ +0.59%）、日經 +1.04%；夜盤 -31 劇本三。
- DATA §18 真值：選擇權前十大＝買權 13,465/11,904/+1,561/+764、賣權 8,331/9,219/-888/+228，資料日期皆 2026-10-05（月選落後一日）；流向 期貨 +2,335（→10-06）／買賣權 +764/+228（→10-05）。報告初版誤植舊鏈值（12,483/9,443/±1,295/483、±498/633、6676、NQ+0.55/日經+2.40/31.76/PE203）已全修。
- DATA OI 增減有重複列（fetch 寫 52,500/+2,875 與 49,000/+1,913；手補 Wall 列 50,000/+1,453、49,000/+1,401），報告用 Wall 列（模板口徑），DATA 未動。
- 工具教訓：bash workdir 遇 CJK 會間歇性路徑亂碼→改用 `workdir=D:\Opencode\Proj`＋python 內 `os.chdir`；powershell `>` 寫 UTF-16→改用 python 內寫檔；git add 用 python glob 避 CJK 字面。
- 2026-10-07 防重演三件套：`src/draft_blocks.py` 加吐 §5.5 前十大／§6.4 比較表／§6.2 流向草稿（含區間＋資料日期，照貼不手改）；新增 `scripts/numcheck.py`（token 稽核＋3 結構檢查＋DATA sha，驗收：今日成品 RC=0、故意改錯 2 處 RC=1 全抓到）；starter prompt 加開工鐵律（凍結 sha→起草機貼數→單輪稽核→gate）。
- 2026-10-08 首跑新流程（T0=2026-10-07 全日，`dbbbc99`）：自查抓 §6.4 P9/P10 錯位 1 處，numcheck 單輪抓 2 處（30Y 誤植 5.64→5.66、收盤距 5 萬改算式）→零 ERROR→gate RC=0，全程約 10 分鐘。維持率三源失敗走前值遞補 200.72；借券增減僅上櫃值；P/C 0.87；夜盤 -375 劇本三。
- 同日 08:35 本機排程晚跑改寫 DATA（Yahoo 刷新＋維持率真值 199.17），pull 被未提交報告擋下而 abort（見 logs/fetch.log）；報告只跟維持率 6 行（`ratio-refresh` commit），Yahoo 浮動不追；近三天本機皆晚跑（08:28～08:40，疑筆電睡過 07:55 醒來補跑），與晨間寫作撞車為常態風險。
- 起草機再補 §6.4 Top10 全表整張貼：驗收時順手抓到已發布報告 §6.4 第 6~8 列 Call 錯位 3 處（token 都在 DATA 裡，numcheck/gate 攔不住，正是手排的代價），已按 draft 值修回。
- 2026-10-09（T0=2026-10-08 全日，盤前適用 10-12）：大跌 -493 失守 5 日線、外資現貨暴增 -758.5、夜盤無新節次（10-07 晚一節，劇本四打折）、F2 換約、借券 SOP 3.5 補登上櫃 40,407/-3；教訓：初版 §4 混入昨日新聞（美光/旺宏/SK/馬斯克無源，numcheck 抓 2 數字＋sweep 抓無數字殘留），起草機補 §4 事件清單（只寫清單內）根治。
- 2026-10-12 早（T0=2026-10-08，報告已存在→只做週一刷新）：週末三次 fetch 改寫 DATA（Yahoo＋新聞輪替＋借券回全口徑），報告 Yahoo/新聞段整批跟新（美股周五反彈、美期全紅、台幣轉升、陸股恢復、主動式ETF、Fed人事雜音）；numcheck 首輪 101→修後 0（另抓 §7.1 殖利率舊行＋附錄A ADR）；gate RC=0；fetch 晨間 08:13/08:23 兩跑，sha 凍結 53e3e7a78aad 後無再改寫。
- 同日續修夜盤（用户指數據錯誤，直查 proxy 證實：查 T0+1 回 DATE=2026-10-08 舊值）：報告夜盤段整段改無夜盤（§5.1/§5.4/§5.6/§6.2/§6.3/§7.3/kpi/levels/verdict/§1/§9/§10/§11，49,593 僅留前一節參考保 gate 錨點）；根因修 `src/sources/taifex.py`（回退比對改查 T0+1 而非 T0，已 live 驗證 NOTE_FIRES=True）。
- 同日再爆：期交所已有週日夜盤新節次（proxy 查 10-12 回 DATE=2026-10-12，收 48,705 -644，與官方 10-08 止一致指向連假後首節）：DATA 夜盤段手動更新＋報告改回真值（levels/scenarios/§9/附錄A/kpi/verdict/§11 全換錨 48,705）；dashboard 半成品還原（DATA 修好即不需要）；fetch 回退註記修保留防再發。

- 同日徹底修夜盤查詢（用户要求上班日早上必須有最新夜盤）：根因是規則全日→T0+1（平日等於今天所以沒爆過，假日後分歧取回退舊值）＋回退靜默採用。改法：夜盤一律查今天、回傳日期不符一律視為無新節次（附屬量/結算/法人夜同口徑；options-after-hours 日盤拆分不動）；量取 OHLC 端點；夜漲跌正值 -652（48,705－前結算 49,357，上游自洽，已同步）；平日行為與舊規則等價。live 驗證通過＋read-only build() 全跑通。
- 2026-10-13（T0=2026-10-12 全日）：小跌 -11 廣度翻多＋投信翻多＋自營翻多，外資大賣 -522 期貨大空，夜盤 -399 劇本三；修正案驗收成功（新規則首跑直接取到週一夜盤，無回退）；開工鐵律追加 prior-audit（比較級數字逐一對前後 DATA，抓 4 處：維持率舊值/Put集中舊區間/夜振幅算式標記/大戶流向舊值）；借券/融資 SOP 3.5 救援值與 fetch 獨立重跑完全一致。
- 同日斷根工程（回應「改善加了不少但問題一直冒出來」）：起草機預填 verdict/levels/scenarios＋關鍵數字速查（剩下全部手填數字消滅；驗收抓到殖利率取錯欄即修）；prior-audit 併入 numcheck（--prev）；新增 scripts/open.py＋verify.py 固定指令，臨時腳本退役；下次開工起只走兩條指令。
- 2026-10-14 早 Actions 02:03＋本機 08:27 雙跑撞車（pull 被未追蹤同名檔擋下）： blend 兩版（T10/comps/期貨流向取 origin 版 10-12 basis，官方 API 本機被擋；其餘取 local 版 08:27 新值；夜盤結算/未平倉雙方皆缺；Gamma 取 local 新值）；另發現本機排程停用未生效（今晨仍跑，待查工作排程器）。
- 同日：前日 DATA_1012 被盤中重寫（05b91fc 12:54 commit；numcheck 實證 121 處不符，已發布報告全部命中舊值）。根治：fetch merge_same_t0 改只填補缺（新舊皆有值沿用舊版；單元測試 6 斷言全過）；DATA_1012 還原發布版（sha 一致）；以後真改進走 gapfill/SOP 明示＋報告重驗，不再靜默覆寫。
- 2026-10-14 早 Actions 08:00 未產出（git log 無今日 chore）：修 `.github/workflows/daily_data.yml`——timeout 20→45 分（重試本來跑不完）、T0FILE 改只認本輪新檔（舊寫法 fetch 全滅時誤拿昨日檔靜默跳過）、無新檔直接 exit 1（不再假裝成功）。
- 排程改制收尾：DailyPremarket0800 已停用（用户動手，隨時可開回）；開工改 on-demand（`open.py --fetch` 先抓取再凍結，20 分鐘超時／失敗自動退回已 pull DATA；Actions 照跑不斷炊）。今日總驗收一次通過，無殘留。
- gapfill 上線（用户定案 Actions 主抓＋本機只補洞）：`scripts/gapfill.py` 只補 unavailable／前值遞補格（融資融券 HiStock／維持率三源 T0 重試＋遞補更新／借券賣出／Yahoo 代號列），不碰正常值（浮動凍結）；今日實測補上維持率真值 196.16（wantgoo 10-12），另抓到日期格式 bug 即修；`open.py --fetch` 改走 gapfill（DATA 缺失才全量）。
- 排程改制（用户決定）：本機 DailyPremarket0800 取消，開工改 on-demand（`open.py --fetch` 先抓取再凍結；失敗退回已 pull DATA；Actions 08:00/19:00 照跑不斷炊）。撞車類問題不再有第二個寫手。
- worker 部署已驗證生效（三截圖）：price 端誠實標 10-08 舊值、institutional 端 10-12 新值（+204/+677 確認為週日夜盤真值，已恢復進報告§5.4/§5.6劇本四/§7.3/kpi）、night-ohlc 新節次與手動值一字不差；選擇權夜/結算維持缺失（源頭不明，不硬填）。
- 同日修 worker 貼標（舊值貼新標籤根因）：`workers/taifex-proxy_V1.4.js` 5 處 `date: today()`（institutional 共用＋price 日/夜＋options 日/夜）改為頁面實際日期（queryDate input／紅字日期段，ROC 轉 ISO；抓不到標 fetch-day）＋台北曆日；已用真實頁面 HTML 驗 extractor（ISO/紅字/ROC/無日期四態全對）。待用户按 DEPLOY.md 整檔貼上部署；部署後驗：after-hours 端點 `date` 應等於頁面日期、`date_source` 為 page。
- 2026-10-14 早 02:03 bot 跑過一次（author 陈晓彤 dates 證實；時間對不上 08:00/19:00/週六任何一班，應為週二 19:00 遲到 7 小時或手動觸發，repo 內無法區分；確定不是 08:00 那班也不是筆電）。
- 定案（用户貼 Actions 截圖：#44 Scheduled, Today at 2:03 AM）：就是週二 19:00 那班遲到 7 小時；前一天 #43（週二 12:50）則是 08:00 那班遲到 5 小時。GitHub 排程連兩天大延遲，與手動觸發無關。結論：排程時間已不可靠，fill-only merge＋fail-loud 使任何時間落地的 run 都無害；開工 on-demand 不再依賴排程準時。另：筆電排程停用未生效（今晨 08:26 照跑＋仍排著明早 07:55，已請用户再檢查工作排程器）。
- 2026-10-14 中午全流程實測驗收（T0=2026-10-13 全日）：open.py --fetch 首跑抓到真 bug（gapfill subprocess 回傳 stdout=None，tail 相加 TypeError 崩潰，DATA 已寫入但凍結中斷；原因未明，疑 Windows pipe 瞬斷，已加 None-safe 守衛，第二跑全程 RC=0）；gapfill 首功（wantgoo 出 T0 真值，維持率 196.16→189.94，-6.22 大跌日去槓桿實錘）；新起草 9 表實戰（verify 首輪只抓 1 處：舊新聞光通訊 3,000 元殘留，修後 RC=0＋GATE_PASS）；bot 10:58 改寫 DATA（數值凍結有效、新聞輪替、sha 換 b01f70560bc0，報告以新凍結為準）。本機排程已由用户刪除（非停用），雙寫手根除。
