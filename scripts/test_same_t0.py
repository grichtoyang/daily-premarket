# -*- coding: utf-8 -*-
"""C1/C2 單元測試（稽核驗收用）：同 T0 盤別合併＋跨換月檢查。

用法（repo 根目錄）：python scripts/test_same_t0.py
結束碼 0 全過；印出每個案例 PASS/FAIL。
"""
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

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

print(f"FAILURES={len(fails)}")
raise SystemExit(1 if fails else 0)
