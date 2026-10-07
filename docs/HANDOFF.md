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
- 夜盤查詢：全日版查 **T0+1**，日盤版查 **T0**；proxy 用 `queryDate=YYYY/MM/DD&marketCode=1&MarketCode=1`（`date=`／`Session=F` 無效）
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
