# -*- coding: utf-8 -*-
"""C1/C2 單元測試（稽核驗收用）：同 T0 盤別合併＋跨換月檢查。

用法（repo 根目錄）：python scripts/test_same_t0.py
結束碼 0 全過；印出每個案例 PASS/FAIL。
"""
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from src.fetch_data import _norm_t0_arg
from src.fetch_data import merge_same_t0
from src.sources.taifex import _chain_rollover
from src.t0 import slot_params

fails: list = []


def check(name: str, cond: bool) -> None:
    print(("PASS " if cond else "FAIL ") + name)
    if not cond:
        fails.append(name)


HDR = ("# DATA_REPORT_20261014\n\n- 報告日期：`2026-10-15`\n"
       "- T0 交易日期：`2026-10-14`\n")


def doc(session: str, night_open: str, night_close: str, vol: str) -> str:
    ses = f"- 產出盤別：`{session}`\n" if session else ""
    return (HDR + ses + "\n## 三、期貨\n\n### 2．台指期近月夜盤行情\n\n"
            "| 項目 | 數值 | 資料來源 |\n|---|---|---|\n"
            f"| 開盤價 | {night_open} | TAIFEX Proxy |\n"
            f"| 收盤價 | {night_close} | TAIFEX Proxy |\n"
            f"| 成交量 | {vol} | TAIFEX Proxy |\n")


# T1 正插：舊=日盤（48,433/48,755）、新=全日（48,801/47,945＋一格缺失）→ 取新＋補舊
old = doc("日盤", "48,433", "48,755", "21,801")
new = doc("全日", "48,801", "47,945", "unavailable")
m, f = merge_same_t0(old, new, "全日")
check("T1 正插取新夜盤", "| 收盤價 | 47,945 |" in m and "48,801" in m)
check("T1 缺格由舊填補", "| 成交量 | 21,801 |" in m and f >= 1)
check("T1 舊夜盤不殘留", "48,755" not in m)

# T2 反插：舊=全日、新=日盤（延遲倒插）→ 原樣保留舊檔
old2 = doc("全日", "48,801", "47,945", "38,271")
new2 = doc("日盤", "48,433", "48,755", "21,801")
m2, _ = merge_same_t0(old2, new2, "日盤")
check("T2 反插留舊", m2 == old2)

# T3 同盤別 → 維持穩定優先（沿用舊值）
old3 = doc("全日", "48,433", "48,755", "21,801")
new3 = doc("全日", "48,801", "47,945", "38,271")
m3, _ = merge_same_t0(old3, new3, "全日")
check("T3 同盤別沿用舊值", "| 收盤價 | 48,755 |" in m3)

# T4 舊檔無盤別行 → 視為未知，維持舊行為
old4 = doc("", "48,433", "48,755", "21,801")
m4, _ = merge_same_t0(old4, new3, "全日")
check("T4 未知盤別沿用舊值", "| 收盤價 | 48,755 |" in m4)

# T5 C2：快照主力 W2 vs 當前 F3 → 觸發；相同 → 不觸發；未知 → 不觸發
rows_w2 = [{"contract_month": "202610W2", "type": "call", "open_interest": 70030},
           {"contract_month": "202610F3", "type": "call", "open_interest": 17867}]
ok, old_p = _chain_rollover(rows_w2, "202610W2", "202610F3")
check("T5 換月觸發", ok is True and old_p == "202610W2")
ok2, _ = _chain_rollover(rows_w2, "202610F3", "202610F3")
check("T5 同月不觸發", ok2 is False)
ok3, old3p = _chain_rollover(rows_w2, None, "202610F3")
check("T5 無標籤走 OI 後備觸發", ok3 is True and old3p == "202610W2")
ok4, _ = _chain_rollover([], None, "202610F3")
check("T5 空快照不觸發", ok4 is False)
ok5, _ = _chain_rollover(rows_w2, "202610W2", None)
check("T5 當前未知不觸發", ok5 is False)

# T6 班別→參數（純函式，只吃排定日期；closed=set() 不碰網路；週末=週六）
# 平日早班→前一交易日／全日；19:00 班即使半夜跑→當日／日盤；週末→週五／全日
r = slot_params("morning", "2026-10-16", set())
check("T6 平日早班", r["t0"] == "2026-10-15" and r["session"] == "全日")
r = slot_params("morning", "2026-10-19", set())
check("T6 週一早班往前跨週末", r["t0"] == "2026-10-16" and r["session"] == "全日")
r = slot_params("evening", "2026-10-15", set())
check("T6 平日晚班", r["t0"] == "2026-10-15" and r["session"] == "日盤")
r = slot_params("evening", "2026-10-16", set())
check("T6 19點班半夜補跑仍判當日日盤", r["t0"] == "2026-10-16" and r["session"] == "日盤")
r = slot_params("evening", "2026-10-11", set())
check("T6 假日晚班退為前日全日", r["t0"] == "2026-10-09" and r["session"] == "全日")
r = slot_params("weekend", "2026-10-17", set())
check("T6 週六班", r["t0"] == "2026-10-16" and r["session"] == "全日")
try:
    slot_params("midnight", "2026-10-16", set())
    check("T6 非法班別拋錯", False)
except ValueError:
    check("T6 非法班別拋錯", True)

# T7 新標頭行不影響合併（產出者/排定班別僅供稽核）
tagged = old.replace("- T0 交易日期：`2026-10-14`",
                     "- T0 交易日期：`2026-10-14`\n- 產出者：`local`\n- 排定班別：`morning`")
m7, _ = merge_same_t0(tagged, new, "全日")
check("T7 標頭行不影響取新", "| 收盤價 | 47,945 |" in m7)

# T8 鏈級：--t0 格式收斂＋open 組參 ISO（OPEN-3）
check("T8 compact轉ISO", _norm_t0_arg("20261012") == "2026-10-12")
check("T8 ISO不變", _norm_t0_arg("2026-10-12") == "2026-10-12")
check("T8 空字串", _norm_t0_arg("") == "")
check("T8 亂字串原樣", _norm_t0_arg("abc") == "abc")
try:
    import scripts.open as _op
    _fc = _op._fetch_cmd("evening", "2026-10-15", "20261015")
    _fs = " ".join(_fc)
    check("T8b open組參--t0為ISO", "--t0" in _fc and "2026-10-15" in _fc
          and "20261015" not in _fs)
    check("T8b open組參帶slot", "--slot" in _fc and "evening" in _fc
          and "2026-10-15" in _fc)
except Exception as e:  # noqa: BLE001
    check(f"T8b open import失敗: {e}", False)

# T9 B1：該 T0 尚無報告（protect=False）→ 新舊皆有值且不同取「新」值，並加覆蓋註記
# （fixture 補 `- 未取得欄位 (` 行，讓註記插入點存在，模擬真實 DATA 結構）
old9 = doc("全日", "48,433", "48,755", "21,801") + "\n- 未取得欄位 (0)：無\n"
new9 = doc("全日", "48,801", "47,945", "38,271") + "\n- 未取得欄位 (0)：無\n"
m9, f9 = merge_same_t0(old9, new9, "全日", protect=False)
check("T9 覆蓋模式取新值", "| 收盤價 | 47,945 |" in m9 and "| 開盤價 | 48,801 |" in m9
      and "| 成交量 | 38,271 |" in m9)
check("T9 覆蓋註記含計數", "同 T0 覆蓋：3 格以本次新抓取覆蓋" in m9 and "無凍結對象" in m9)
check("T9 舊值不殘留", "48,755" not in m9 and "21,801" not in m9)
check("T9 無填補", f9 == 0)

# T10 同情境但 protect=True（預設）→ 仍取「舊」值，確保預設行為不變
m10, _f10 = merge_same_t0(old9, new9, "全日", protect=True)
check("T10 保護模式沿用舊值", "| 收盤價 | 48,755 |" in m10 and "| 開盤價 | 48,433 |" in m10
      and "| 成交量 | 21,801 |" in m10)
check("T10 穩定註記且無覆蓋註記", "同 T0 穩定" in m10 and "同 T0 覆蓋" not in m10)

# T11 F11：protect 模式（該 T0 已有已發布報告）重跑時，表格以外的三塊不得被破壞
# fixture 依真實 DATA 結構：標頭四行 → 維持率表格列 → 新聞區塊 → 第五章來源/註記
MR_OLD_SRC = "wantgoo 大盤融資維持率 (民間估算；官方無每日序列)"
MR_NEW_SRC = "前值遞補 (DATA 2026-10-15；當日三源皆失敗；民間估算；官方無每日序列)"
MR_NOTES = ("- 註記：融資維持率未取得 (三源皆失敗；官方無每日序列)\n"
            "- 註記：融資維持率採前值遞補 (DATA 2026-10-15)，非 T0 2026-10-16\n")


def doc11(ratio, ratio_src, mr_src, notes, nw, rd, tm, who, slot, session="全日"):
    ts = ("2026-10-16T10:00:00Z；台北時間：2026-10-16 18:00" if nw == "舊"
          else "2026-10-19T01:00:00Z；台北時間：2026-10-19 09:00")
    news = "".join(
        f"- 事件{i}：{nw}新聞{i}\n"
        f"  - 來源：Yahoo 台股；發布時間：{ts}\n"
        f"  - 摘要：{nw}摘要{i}\n  - 原文連結：https://ex/{nw}/{i}\n" for i in (1, 2))
    return (f"# DATA_REPORT_20261016\n\n"
            f"- 報告日期：`{rd}`\n- T0 交易日期：`2026-10-16`\n"
            f"- 資料產出時間：`{tm}`\n- 時區：`Asia/Taipei`\n"
            f"- 產出盤別：`{session}`\n- 產出者：`{who}`\n- 排定班別：`{slot}`\n"
            f"\n---\n\n## 一、現貨\n\n### 4. 融資融券\n\n"
            f"| 項目 | 數值 | 單位 | 資料來源 |\n|---|---|---|---|\n"
            f"| 融資維持率 | {ratio} | % | {ratio_src} |\n"
            f"\n## 二、重要市場\n\n"
            f"### 8. 重大經濟數據、央行事件與重大市場新聞\n\n"
            f"**資料來源：** 台股 `tw.stock.yahoo.com`\n\n{news}\n"
            f"## 三、期貨\n\n### 1．台指期近月日盤行情\n\n"
            f"| 項目 | 數值 | 資料來源 |\n|---|---|---|\n"
            f"| 收盤價 | 47,269 | TAIFEX Proxy |\n"
            f"\n## 五、資料來源、時間與完整性\n\n"
            f"- margin：`HiStock 上市+上櫃融資融券 (金額口徑)`\n"
            f"- margin_ratio：`{mr_src}`\n{notes}"
            f"- 未取得欄位 (0)：無\n")


o11 = doc11("183.39", MR_OLD_SRC, MR_OLD_SRC, "", "舊",
            "2026-10-17", "2026-10-17 13:01:48", "local", "weekend")
n11 = doc11("191.61", MR_NEW_SRC, MR_NEW_SRC, MR_NOTES, "新",
            "2026-10-19", "2026-10-19 10:20:59", "actions", "morning")
m11, f11 = merge_same_t0(o11, n11, "全日", protect=True)
check("T11 新聞區塊不刷新", "- 事件1：舊新聞1" in m11 and "- 事件2：舊新聞2" in m11
      and "新新聞" not in m11 and "2026-10-19 09:00" not in m11)
check("T11 標頭四行沿用前版",
      "- 報告日期：`2026-10-17`" in m11 and "- 資料產出時間：`2026-10-17 13:01:48`" in m11
      and "- 產出者：`local`" in m11 and "- 排定班別：`weekend`" in m11
      and "2026-10-19 10:20:59" not in m11 and "產出者：`actions`" not in m11)
check("T11 維持率不降級", "| 融資維持率 | 183.39 | % | " + MR_OLD_SRC + " |" in m11
      and "191.61" not in m11 and "- margin_ratio：`" + MR_OLD_SRC + "`" in m11
      and "前值遞補" not in m11 and "融資維持率採前值遞補" not in m11
      and "融資維持率未取得" not in m11)
check("T11 表格列遞補取舊有計數", f11 >= 2)
check("T11 期貨等其餘內容不受凍結影響", "| 收盤價 | 47,269 | TAIFEX Proxy |" in m11
      and "## 五、資料來源、時間與完整性" in m11)

# T12 protect=False（該 T0 尚無報告）→ 三塊皆不凍結，行為與原版一致
# （表格列取舊值是既有 _fb 規則，protect=False 也照舊，本次未更動）
m12, _ = merge_same_t0(o11, n11, "全日", protect=False)
check("T12 非 protect 新聞照刷", "- 事件1：新新聞1" in m12 and "舊新聞1" not in m12)
check("T12 非 protect 標頭照寫", "- 產出者：`actions`" in m12
      and "- 排定班別：`morning`" in m12
      and "- 報告日期：`2026-10-19`" in m12)
check("T12 非 protect 維持率來源照新抓", "- margin_ratio：`" + MR_NEW_SRC + "`" in m12
      and "融資維持率採前值遞補" in m12
      and "| 融資維持率 | 183.39 | % | " + MR_OLD_SRC + " |" in m12)

# T13 protect 模式重跑且本次無任何新值 → 合併結果與前版逐字相同（main() 據此不寫檔）
m13, f13 = merge_same_t0(o11, o11, "全日", protect=True)
check("T13 合併結果與前版相同", m13 == o11 and f13 == 0)

# ── T11 追加（F11 修正，2026-10-19）────────────────────────────────────────────
# `四.資料來源` 區的 `- 資料日期：…；資料時間：<本次抓取時間>` 性質同標頭的
# 「資料產出時間」。Case A 不凍結的話，同盤別重跑必然逐字不同 → 一定寫檔
# （sha 漂移＋無意義 commit），main() 的「不寫檔」那條等於白做。
_DT_LINE = "\n- 資料日期：2026-10-16；資料時間：{t}；時區：`Asia/Taipei`\n"
_DT_MARK = "\n## 五、資料來源、時間與完整性"
o11t = o11.replace(_DT_MARK, _DT_LINE.format(t="2026-10-17 13:01:48") + _DT_MARK)
n11t = n11.replace(_DT_MARK, _DT_LINE.format(t="2026-10-19 10:20:59") + _DT_MARK)
m11t, _f11t = merge_same_t0(o11t, n11t, "全日", protect=True)
check("T11 追加：資料時間行凍結",
      "- 資料日期：2026-10-16；資料時間：2026-10-17 13:01:48；時區" in m11t
      and "2026-10-19 10:20:59；時區" not in m11t)
# Case B 對照：盤別升級時資料時間必須跟著更新（否則 sha 會停在舊產出時間）
o14t = doc11("183.39", MR_OLD_SRC, MR_OLD_SRC, "", "舊", "2026-10-17",
             "2026-10-17 13:01:48", "local", "evening", session="日盤")
n14t = doc11("191.61", MR_NEW_SRC, MR_NEW_SRC, MR_NOTES, "新", "2026-10-19",
             "2026-10-19 10:20:59", "actions", "morning", session="全日")

# ── T14（F11 修正，2026-10-19）────────────────────────────────────────────────
# Case B 盤別升級：同一 T0 先跑日盤發布、隔天早上再跑全日——這是每日盤前報告的
# 正規路徑（週二早上的報告＝週一全日＋週二盤前新聞）。新聞若仍凍結，每天早上的
# 報告永遠只拿到前一晚的新聞 → 產品品質倒退。維持率是 T0 的數值不是事件流，
# 兩種情境都不得降級成前值遞補。
m14, _f14 = merge_same_t0(o14t, n14t, "全日", protect=True)
check("T14 Case B（盤別升級）新聞照刷",
      "- 事件1：新新聞1" in m14 and "- 事件2：新新聞2" in m14
      and "舊新聞" not in m14 and "2026-10-19 09:00" in m14)
check("T14 盤別升級標頭照更新",
      "- 產出者：`actions`" in m14 and "- 排定班別：`morning`" in m14
      and "- 報告日期：`2026-10-19`" in m14
      and "- 資料產出時間：`2026-10-19 10:20:59`" in m14
      and "- 產出者：`local`" not in m14 and "- 排定班別：`evening`" not in m14)
check("T14 盤別升級維持率仍不降級",
      "| 融資維持率 | 183.39 | % | " + MR_OLD_SRC + " |" in m14
      and "191.61" not in m14 and "- margin_ratio：`" + MR_OLD_SRC + "`" in m14
      and "前值遞補" not in m14 and "融資維持率採前值遞補" not in m14
      and "融資維持率未取得" not in m14)

# Case B 的 `四.資料來源` 資料時間同樣照更新
o14ts = o14t.replace(_DT_MARK, _DT_LINE.format(t="2026-10-17 13:01:48") + _DT_MARK)
n14ts = n14t.replace(_DT_MARK, _DT_LINE.format(t="2026-10-19 10:20:59") + _DT_MARK)
m14ts, _ = merge_same_t0(o14ts, n14ts, "全日", protect=True)
check("T14 盤別升級資料時間照更新",
      "- 資料日期：2026-10-16；資料時間：2026-10-19 10:20:59；時區" in m14ts
      and "2026-10-17 13:01:48；時區" not in m14ts)

# 保守失敗：前版完全沒有盤別標記（`- 產出盤別：`/`- 日盤／夜盤標記：`都缺）
# → 判斷不出升級，一律走 Case A 凍結（安全失敗）
o14u = "\n".join(ln for ln in o11.split("\n") if not ln.startswith("- 產出盤別："))
n14u = "\n".join(ln for ln in n11.split("\n") if not ln.startswith("- 產出盤別："))
m14u, _ = merge_same_t0(o14u, n14u, "全日", protect=True)
check("T14 判不出前版盤別保守凍結（新聞沿用前版）",
      "- 事件1：舊新聞1" in m14u and "新新聞" not in m14u)
check("T14 判不出前版盤別保守凍結（標頭沿用前版）",
      "- 產出者：`local`" in m14u and "- 產出者：`actions`" not in m14u)

print(f"FAILURES={len(fails)}")
raise SystemExit(1 if fails else 0)
