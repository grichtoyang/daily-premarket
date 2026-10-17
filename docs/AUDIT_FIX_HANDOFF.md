# 稽核修正交接（給 Muse；稽核者：OpenCode，2026-10-16）

> 用途：OpenCode 只負責稽核、不改檔。Muse 依本清單修正；改完把 diff／commit 交回，
> OpenCode 照「我的驗收」逐項複核。全程照 SOP「只修不加、功能凍結」。

## 0. 基準與鐵律

- 現況已驗證（稽核當下）：
  `python scripts/verify.py --t0 20261015 --prev 20261013`
  → `DATA_SHA=227210ebb47f`、`NUMCHECK_ERRORS=0`、`GATE_PASS`（RC=0）。
  **任何修改後這個結果不得變差。**
- 鐵律：只修不加、功能凍結；不動歷史報告／歷史 DATA（含 `data_reports/DATA_REPORT_20261014.md` 不重寫）。
- 時間皆 Asia/Taipei。

---

## 1. 必修

### C1（最高）`merge_same_t0` 凍結夜盤，中和 185f378 的 T0+1 修正

- 證據：
  - 以 old=`48,433/48,755/+363`、new=`48,801/47,945/-853` 丟 `src/fetch_data.py::merge_same_t0`
    → `filled=0`，輸出仍是舊值（規則被靜默吃掉）。
  - `data_reports/DATA_REPORT_20261014.md` 夜盤 = `48,433／48,755／+363／21,801`，與
    `…20261013.md` 一字相同；而 proxy `futures-night-ohlc?date=2026/10/14` 真值為
    `48,801／47,945／-853`。→ 1014 夜盤整整偏一節。
- 成因：同一 T0 檔先被 19:00「日盤」寫入（夜盤＝T0-1 節），隔晨「全日」再寫（夜盤＝T0 節），
  但 `src/fetch_data.py:177-181`「新舊皆有值且不同 → 沿用舊值」把後寫的正確夜盤蓋回。
- 建議改法：
  1. `src/fetch_data.py::build()` 標頭新增一行 `- 產出盤別：{session}`（純新增，舊檔無此行視為未知）。
  2. `merge_same_t0(old, new, new_session)` 加前置規則：
     - old=日盤、new=全日 → 以新檔為準（仍可對舊檔做 MISSING 填空）；
     - old=全日、new=日盤（延遲班次倒插）→ 保留舊檔（全日為權威）；
     - 盤別相同或未知 → 維持現行「穩定優先」行為。
  3. `main()` 把 `session` 傳進 merge。
- 我的驗收：
  1. 兩段單元案例（正插：日盤→全日取新；反插：全日→日盤留舊）行為正確；
  2. `compile`／`import` 通過；
  3. `verify.py --t0 20261015 --prev 20261013` 仍 PASS；
  4. 不重寫 `DATA_REPORT_20261014.md`。

### C2（高）跨到期換月產生假的「日對日變化」

- 證據：`DATA_1013/1014` 到期月 = `202610W2`、`DATA_1015` = `202610F3`；
  `src/sources/taifex.py:451` 的 snapshot 對齊鍵含 `contract_expiry_date`，換月後大量 strike 配不到
  → 差額直接等於當前 OI（Call 70,030→69,146 卻報 `+51,279`、Put 65,057→33,377 卻報 `+23,370`、
  Put Wall `-4,300`、Call Wall `+500`、Max Pain `-1,450` 皆失真）。
- 建議改法：`taifex.py` 算 `snapchg` 前比對「快照 chain 到期日集合」vs「當前 chain 到期日集合」，
  若不相交（換月）→ `snapchg["chain"]=None`、`snapchg["walls"]=None`，並加註
  「跨到期換月（舊X→新Y），日對日 OI/Walls 變化不適用」。DATA 因此落 `unavailable`。
- 我的驗收：以 1015 情境（W2→F3）建構測試 → 對應欄位 `unavailable`＋註記；verify 仍 PASS。

---

## 2. 應修（報告／文件，低風險）

- **H1**：`reports/Daily_REPORT_20261015_全日.md:186` 刪除「Fed 9月會議紀要（10/7公布）」該 bullet
  （DATA_1015 §二.8 事件清單無此項）。並在 `prompts/daily_starter_Muse.md` 補寫手鐵律：
  **§4.1/§4.2 每條須對應 DATA 事件，逐條比對起草機 `_news_list` 清單**。
- **H2**：修 `reports/Daily_REPORT_20261015_全日.md` §八——情境A 標題「開高喘息」但觸發條件為
  「開盤低於 47,366」（向下），且情境C 重複同名。須標題與觸發方向一致、四列命名不重複
  （對齊機器區 `:633-638` 的 開高/開平/開低測撐/破支撐走弱）。
- **H3**：`src/draft_blocks.py::_levels_filled` 讓「支撐/支撐二」按接近現價排序
  （或人工對調 44,500／46,456）。
- **M1**：`src/fetch_data.py:8` docstring 與 `:947` argparse help 改為「全日→T0+1、日盤→今天」。
- **M2**：`docs/HANDOFF.md:17/74` 現行段標為已被 `:91` 取代（避免同檔自相矛盾）。
- **M3**：`docs/DEPLOY.md:6/44` 版本字串 V1.3 → V1.4。
- **M4**：`reports/Daily_REPORT_20261015_全日.md` 備查註記「202610F3 為當月月選」→
  「第 3 週序列（週選）」。

---

## 3. 選配（先別動，需再討論）

- worker `workers/taifex-proxy_V1.4.js` 主路徑（`:5401-5404`）只回 `requestedDate`、未帶頁面實際日期，
  使 client「回傳日期==查詢日」把關（`src/sources/taifex.py:88/111`）形同自我實現。
  **先做一次「T0+1 為休市日」的唯讀實測**，再決定是否改 worker＋重新部署。

---

## 4. 交回時請附（供 OpenCode 複核）

1. `git diff` 或 commit hash；
2. `python scripts/verify.py --t0 20261015 --prev 20261013` 輸出；
3. C1/C2 的單元測試輸出；
4. OpenCode 複核方式：重跑上述 verify ＋直接呼叫 `merge_same_t0` 正/反案例
   ＋ proxy `?date=2026/10/14`、`?date=2026/10/16` 交叉比對。

---

## 5. 2026-10-17 狀態更新（清帳）

> 逐項標記現況（照實填，不宣稱未完成的事）；證據以檔案行號＋commit 為準。

- **C1**：盤別部分已實作——`src/fetch_data.py:274` 標頭輸出 `- 產出盤別：`、`:82-108` `merge_same_t0` 日盤/全日 優先規則（舊日盤→新全日以新檔為準；舊全日→新日盤保留舊檔；同盤別維持穩定優先）。「新舊皆有值沿用舊值」凍結夜盤的問題在 2026-10-17 另案處理（merge 覆蓋條件：尚無報告時以新抓取為準；夜盤查詢日改查 T0 的次一交易日，commit `f511e8d`）。
- **C2**：2026-10-17 已實作——`src/sources/taifex.py:511-521` 換月檢查（`_chain_rollover` 呼叫在 `:514-517`）＋`:570-587` `_chain_rollover` 純函式。注意：實作採「快照主力 vs 當前主力」比對，較原建議「到期日集合不相交」更嚴（兩邊 chain 常同時含新舊合約，集合比對會漏判，見 `:513` 程式註解）；換月時 `snapchg["chain"]/["walls"]=None` → 變化欄位落 `unavailable`＋註記「跨到期換月…日對日 OI/Walls 變化不適用」。（本檔行號為 2026-10-17 工作區狀態；B3 改動在檔頭，若 `src/sources/taifex.py` 再變動，請以函式名 `_chain_rollover` 為準定位。）
- **H1**：已修（commit `b22bdf7`）——`reports/Daily_REPORT_20261015_全日.md:186` 原「Fed 9月會議紀要（10/7公布）」bullet 已刪（現為「Fed 調查與 PPI」，對應 DATA 事件）；`prompts/daily_starter.md:17`（原 `daily_starter_Muse.md`）已補「§4.1/§4.2每條須對應DATA事件號，逐條比對_news_list」鐵律。
- **H2**：駁回（稽核當下誤判，留歷史不動）——`reports/Daily_REPORT_20261015_全日.md:479-501` §八 四情境標題「開高續攻／開平震盪／開低測撐／破支撐走弱」命名不重複，情境A觸發「開盤高於47,366」、情境C觸發「開盤低於47,366」與標題方向一致（`docs/HANDOFF.md:92` 同此結論）。
- **H3**：報告面已人工修正——`reports/Daily_REPORT_20261016_全日.md:675-677`：支撐＝46,107 夜低、支撐二＝44,500 Put Wall，並補 `白話`。注意：`src/draft_blocks.py:504-512` `_levels_filled` 仍為固定映射（支撐=Put Wall、支撐二=夜低），未改「按接近現價排序」；未來報告仍需人工對調（殘留）。
- **M1**：已修——`src/fetch_data.py:8` docstring「影響夜盤查詢日：全日→T0+1，日盤→今天」；`:975-976` argparse help「全日查 T0+1，日盤查今天」。符合「全日→T0+1、日盤→今天」。
- **M2**：已修——`docs/HANDOFF.md:17` 已標「[以下已取代 2026-10-16，留作歷史]」、`:74` 已標「[規則部分已取代，strict-gate 與附屬同口徑保留有效]」，現行規則在 `:91`，同檔不再自相矛盾。
- **M3**：已修——版本字串已為 V1.4：`workers/DEPLOY.md:4`（`taifex-proxy_V1.4.js`）、`:44`（`version 應為 "V1.4 — V1.3 + daily snapshots (KV) (additive)"`，commit `b22bdf7`）。注意：稽核單原記 `docs/DEPLOY.md:6/44`，實際檔案在 `workers/DEPLOY.md`（`docs/DEPLOY.md` 不存在）。
- **M4**：已修——`reports/Daily_REPORT_20261015_全日.md:443` 現為「到期換約注意202610F3為第3週序列（週選）」（commit `b22bdf7`），非「當月月選」。
- 附註：2026-10-17 另有兩項改動（工作區修改、未 commit）：(a) `.github/workflows/daily_data.yml` 有界失敗——`Fetch daily data` **step 級** `timeout-minutes: 12`＋每次 fetch 嘗試 `timeout 480`＋`PYTHONUNBUFFERED=1`＋sleep 90；(b) `src/sources/taifex.py` 夜盤日曆 fail-loud（`_next_trading_day`／`_night_query_date` 在 `src.t0._LAST_CAL_ERROR` 非空時回 None，夜盤欄落 unavailable＋註記）。另：2026-10-14 commit `6aa493f` 已有 `src/t0.py` 層級的日曆 fail-loud（`_LAST_CAL_ERROR`→`resolve()` `cal_fail`），兩者層級不同。
