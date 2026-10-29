---
name: daily-premarket-analysis-v8
description: Produce structured 台股 V8 Pro (templates/v8-pro-golden-master.html) 台股 daily pre-market analysis with 15-Factor + VIX Dynamic + 90% AI + Builder全扛髒數據. Use when user asks for 盤前分析, 每日盤前, 台指盤前, pre-market report, dashboard.
---

# 台股每日盤前分析 Skill V8 Pro - 15因子 + VIX動態 + Builder全扛髒數據 (2026-10-28 最終修復版)

## V8 Pro 最終修復 (2026-10-28 Actions實測OK)

### 核心坑位已根治 (Builder全扛，不靠上游fetch洗數據)

#### 1. 金版重複 canvasId 白屏 (手機)
- 舊：`fut-tx-day:2 / fut-depth:2 / opt-wall:2` + `大盤全景:2` → `35 total 32 unique` → 手機 `querySelectorAll` 拿到重複ID當掉
- 新：`templates/v8-pro-golden-master.html` 207,442 bytes `32 unique 32` `q=2 spot-pcr=0` 無重複
  - 刪除：`台指期 日夜 · Night Path` / `期貨籌碼 · 深度圖 中軸` / `選擇權牆 · Call藍 Put黃` (重複舊卡)
  - 清掉舊觸發：`45,676 -741 / 47164/47337 / 46,041 / 49K2444 / 46,942`

#### 2. 新聞真換行白屏 (1028專屬)
- 舊：`news:[{d:"[FTNN新聞網]\n - 來源"}]` 真換行在雙引號字串內 → JS語法錯誤白屏
- 舊 Builder：`replace('"','\"')` 只防 `"`
- 新 Builder：`json.dumps` 全跳脫，Builder全扛：
```python
import json as _json
def esc(s):
  j = _json.dumps(s, ensure_ascii=False)  # 處理 " \n \r \t \uXXXX
  inner = j[1:-1]
  return inner.replace('</','<\/').replace('<!--','<\!--')
```
- 現在：`newsLines 1` 單行，`braces diff 0`

#### 3. KPI 8宮格舊數據殘留
- 舊：`old_kpi_grid_pattern` 寫死 `46,041 / -846 -1.81% / 46,942 / 46,272 -741`，金版變 `46,096` 就對不上 → `KPI grid rebuilt: 0`
- 新：寬鬆正則，Builder全扛：
```python
old_kpi_grid_pattern = r'{l:"加權收盤",v:"[^"]*",d:"[^"]*",c:"[^"]*"},...8個'  # [^"]* 允許空值
```
- 現在：`KPI grid rebuilt: 1` → 1027 `46,096點` / 1028 `47,035點` 正確

#### 4. Footer 舊數據殘留
- 舊：`re.sub(r'數據來源 · 2026-10-24 盤前機構版[^"]*', ...)` 只替換特定日期
- 新：`re.sub(r'數據來源 · [^"]*', ...)` + `re.sub(r'加權46,096\.43[^"]*', ...)` 不管哪天舊footer都蓋掉

### Builder 特性 (120,710 bytes, 全扛髒數據版)
- 路徑：`scripts/v8_pro_builder.py`
- 執行：`python scripts/v8_pro_builder.py --date YYYYMMDD --golden templates/v8-pro-golden-master.html --data_report DATA_REPORT_YYYYMMDD.md`
- 產出：`dashboards/taifex-YYYYMMDD.html` 208,043~208,231 bytes `q=2 f=0 spot=0 dups {} braces 0`
- 特性：
  - **新聞**：`json.dumps` + `</` → `<\/` 防 `</script>` 跳脫，髒數據Builder全扛
  - **KPI**：寬鬆正則 `[^"]*` 允許空值，舊數據不管是 `46,041` 還是 `46,096` 都蓋掉
  - **Footer**：`數據來源 · [^"]*` 全替換
  - **Canvas**：`q=2` 安全版 `document.querySelectorAll("canvas[id]").forEach((f)=>{...})` + `try/catch`
  - **15-Factor + VIX動態 + 90% AI**：Bias 0-100 + 恐慌加成 + 語意潤飾
  - **NO-FALLBACK**：核心欄位缺失直接報錯，不偷用舊數據

### Golden Master (207,442 bytes, 最終凍結版)
- 路徑：`templates/v8-pro-golden-master.html`
- `32 unique 32` canvasId，無重複，無 `spot-pcr`
- `q=2` 安全版：`document.querySelectorAll("canvas[id]").forEach((f)=>{let d=f.id,m=P[d];if(m)try{m(f)}catch{}})`
- 版型鎖死，數據只改 `he` 物件 + 41張 `analysis`

### 每日流程 (Actions 08:27/37/47 三重備援)
1. 抓 `DATA_REPORT_YYYYMMDD.md` (可能含 `"` `\n` `</script>` 髒字元)
2. Builder 解析：`spot / inst / tx / futures / options / usPct / news` (json.dumps跳脫)
3. 17→15因子算Bias + VIX動態 + RSI/MACD (3層備援，失敗權重0%)
4. 41張全動態注入 + KPI 8宮格 + Footer 全重建 (Builder全扛)
5. 產出 `dashboards/taifex-YYYYMMDD.html` + 驗收 `q=2 dups {} braces 0 newsLines 1 CHECK PASS`
6. GitHub Actions 額外4道保險 (建議加在 yml)：
```bash
grep -o 'canvasId:"[^"]*"' file | sort | uniq -d → 必須0
grep -Pzo 'news:\[.*\n.*\]' file → 必須無真換行
[ $(grep -o "{" file | wc -l) == $(grep -o "}" file | wc -l) ] → 大括號平衡
grep -q 'querySelectorAll("canvas\[id\]")' file → 安全版
```

### 驗收紀錄 (2026-10-28 Actions實測OK)
- `taifex-20261027.html` 208,231 `close 46,096.23` `q=2 dups {} braces 0 newsLines 1`
- `taifex-20261028.html` 208,043 `close 47,035.58` `q=2 dups {} braces 0 newsLines 1` `KPI 47,035點 +939 +2.04%`

### Output Path Rule
- 產出統一 `dashboards/` 唯一
- Golden: `templates/v8-pro-golden-master.html` 207,442
- Builder: `scripts/v8_pro_builder.py` 120,710
- 禁止 `dashboard/` 或 `dashboard_v8/`

### Data Source
- DATA_REPORT: `data_reports/DATA_REPORT_*.md` 或 `DATA_REPORT_*.md`
- 可能含髒數據：`"` `\n` `</script>` `<!--` → Builder已用 `json.dumps` 全扛，不需改fetch
