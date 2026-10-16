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
