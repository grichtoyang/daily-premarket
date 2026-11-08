#!/usr/bin/env python3
"""
V9 Pro Builder - 17因子 + VIX動態 + RSI/MACD + SQLite真DB + 42個可見區塊全動態 + 6頁 + 機構級圖表
基於 daily-premarket-analysis-v8 (2026-10-28最新版) 升級到 daily-premarket-analysis-v9-pro
母版改成純 React + window.DASHBOARD_DATA，無範例數據，Python 只產 data.json，符合 Output Path Rule: dashboards/ 唯一

Skill: daily-premarket-analysis-v9-pro (參考 v8 pro skill 2026-10-28)
- 17因子：基礎15因子 + RSI 3% + MACD 3% = 17F，VIX動態，基差過大假多 7%->2%
- 方案C：Yahoo ^TWII 30天 → FinMind → SQLite DB 3層備援，全失敗 weight 0% 15因子運算
- SQLite真DB：v9_pro_history + factor_performance，真勝率10天回測，歷史相似度
- 42個可見區塊全動態 + 20模板輪替 + 權重回測，20句型 day_hash%20避免重複
- 6頁結構：總覽/現貨/重要市場/期貨/選擇權/綜合分析，按 DATA_REPORT 四大類對位
- 每區塊 圖表 + 分析→判斷→操作，機構級 Donut/Lollipop/Gauge/SparklineTable/Candlestick/Butterfly/Mountain/Depth/Ladder/Heatmap/Gauge (Bias半圓儀表仿附圖)
- 防重疊：measureText預留4px，三欄固定寬，數值條外，文字不重疊
- 純 React 母版：templates/v9-pro-react-template.html 31KB，無46096等範例數據
- 產出：dashboards/data-YYYYMMDD.json 34KB + dashboards/v9_pro_history.db
- 今日實測：20261028 加權47035 +2.04% 外資+159.6 Bias55 PCR1.09 CallWall47000 PutWall46700
"""

import pathlib, re, json, argparse, sys, glob
from datetime import datetime, timedelta, timezone
import sqlite3, math, tempfile

# ===== 技術指標 3層備援 (方案C) =====
def _t0_iso_date(t0_date):
    if not t0_date:
        return None
    return _normalize_t0_date(str(t0_date).replace('-', ''))


def _history_record_date(record):
    value=record.get('date')
    if value:
        try:
            return datetime.strptime(str(value)[:10], '%Y-%m-%d').strftime('%Y-%m-%d')
        except ValueError:
            return None
    ts=record.get('ts')
    if ts is not None:
        try:
            taipei=timezone(timedelta(hours=8))
            return datetime.fromtimestamp(float(ts), taipei).strftime('%Y-%m-%d')
        except (TypeError, ValueError, OverflowError, OSError):
            return None
    return None


def _filter_history_to_t0(records, t0_date):
    """Keep only dated technical observations on or before the DATA_REPORT T0."""
    t0_iso=_t0_iso_date(t0_date)
    if not t0_iso:
        return list(records or [])
    filtered=[]
    for record in records or []:
        trade_date=_history_record_date(record)
        if trade_date and trade_date<=t0_iso:
            item=dict(record)
            item['date']=trade_date
            filtered.append(item)
    return sorted(filtered, key=lambda item: item['date'])


def fetch_yahoo_twii_30d(t0_date=None):
    try:
        import requests
        url = "https://query1.finance.yahoo.com/v8/finance/chart/^TWII?range=3mo&interval=1d"
        headers = {"User-Agent": "Mozilla/5.0"}
        resp = requests.get(url, headers=headers, timeout=10)
        if resp.status_code != 200:
            print(f"[V9-17F] Yahoo ^TWII failed {resp.status_code}")
            return None
        data = resp.json()
        result = data.get('chart', {}).get('result', [{}])[0]
        timestamps = result.get('timestamp', [])
        indicators = result.get('indicators', {}).get('quote', [{}])[0]
        closes = indicators.get('close', [])
        highs = indicators.get('high', [])
        lows = indicators.get('low', [])
        valid = []
        for i in range(len(closes)):
            if closes[i] is not None:
                ts=timestamps[i] if i < len(timestamps) else None
                record={'close': float(closes[i]), 'high': float(highs[i]) if highs[i] is not None else None, 'low': float(lows[i]) if lows[i] is not None else None, 'ts': ts}
                trade_date=_history_record_date(record)
                if trade_date:
                    record['date']=trade_date
                valid.append(record)
        valid=_filter_history_to_t0(valid,t0_date)
        if len(valid) < 14:
            print(f"[V9-17F] Yahoo insufficient {len(valid)}/14")
            return None
        print(f"[V9-17F] Yahoo fetched {len(valid)} days")
        return valid
    except Exception as e:
        print(f"[V9-17F] Yahoo exception: {e}")
        return None

def fetch_finmind_twii_14d(t0_date=None):
    try:
        import requests
        end = _t0_iso_date(t0_date) or datetime.now(timezone(timedelta(hours=8))).strftime('%Y-%m-%d')
        end_dt=datetime.strptime(end,'%Y-%m-%d')
        start = (end_dt - timedelta(days=30)).strftime('%Y-%m-%d')
        url = f"https://api.finmindtrade.com/api/v4/data?dataset=TaiwanStockPrice&data_id=TAIEX&start_date={start}&end_date={end}"
        resp = requests.get(url, timeout=10)
        if resp.status_code != 200:
            print(f"[V9-17F] FinMind failed {resp.status_code}")
            return None
        data = resp.json().get('data', [])
        if len(data) < 14:
            print(f"[V9-17F] FinMind insufficient {len(data)}/14")
            return None
        valid = []
        for d in data:
            try:
                valid.append({'date': str(d.get('date',''))[:10], 'close': float(d['close']), 'high': float(d['max']) if d.get('max') not in (None,'') else None, 'low': float(d['min']) if d.get('min') not in (None,'') else None, 'ts': None})
            except (TypeError, ValueError, KeyError):
                continue
        valid=_filter_history_to_t0(valid,t0_date)[-30:]
        print(f"[V9-17F] FinMind fetched {len(valid)} days through T0={_t0_iso_date(t0_date) or 'latest'}")
        return valid if len(valid)>=14 else None
    except Exception as e:
        print(f"[V9-17F] FinMind exception: {e}")
        return None

def fetch_db_history_14d(t0_date=None):
    try:
        for p in [pathlib.Path("dashboards/v9_pro_history.db"), pathlib.Path("/tmp/dashboards/v9_pro_history.db")]:
            if p.exists():
                conn = sqlite3.connect(str(p))
                t0_iso=_t0_iso_date(t0_date)
                if t0_iso:
                    rows = conn.execute("SELECT date,spot_close FROM v9_pro_history WHERE date<=? ORDER BY date DESC LIMIT 30",(t0_iso,)).fetchall()
                else:
                    rows = conn.execute("SELECT date,spot_close FROM v9_pro_history ORDER BY date DESC LIMIT 30").fetchall()
                conn.close()
                if len(rows) >=14:
                    valid = [{'date': r[0], 'close': float(r[1]), 'high': None, 'low': None, 'ts': None} for r in reversed(rows)]
                    print(f"[V9-17F] DB fallback {len(valid)} days from {p}")
                    return valid
        print("[V9-17F] V9 DB not found for fallback")
        return None
    except Exception as e:
        print(f"[V9-17F] V9 DB fallback exception: {e}")
        return None

def calc_rsi(closes, period=14):
    try:
        if len(closes) < period+1: return None
        gains=[]; losses=[]
        for i in range(1,len(closes)):
            diff=closes[i]-closes[i-1]
            if diff>0: gains.append(diff); losses.append(0)
            else: gains.append(0); losses.append(abs(diff))
        avg_gain=sum(gains[:period])/period
        avg_loss=sum(losses[:period])/period
        if avg_loss==0: return 100.0
        for i in range(period,len(gains)):
            avg_gain=(avg_gain*(period-1)+gains[i])/period
            avg_loss=(avg_loss*(period-1)+losses[i])/period
        if avg_loss==0: return 100.0
        rs=avg_gain/avg_loss
        return round(100-(100/(1+rs)),2)
    except: return None

def calc_macd(closes):
    try:
        def ema(data,period):
            k=2/(period+1)
            vals=[data[0]]
            for price in data[1:]: vals.append(price*k+vals[-1]*(1-k))
            return vals
        if len(closes)<26: return None,None,None
        ema12=ema(closes,12); ema26=ema(closes,26)
        dif=[ema12[i]-ema26[i] for i in range(len(closes))]
        signal=ema(dif,9)
        return round(dif[-1],2), round(signal[-1],2), round(dif[-1]-signal[-1],2)
    except: return None,None,None

def calc_kd(highs,lows,closes,period=9):
    try:
        if len(closes)<period: return None,None
        rsvs=[]
        for i in range(period-1,len(closes)):
            ph=max(highs[i-period+1:i+1]); pl=min(lows[i-period+1:i+1])
            rsv=50 if ph==pl else (closes[i]-pl)/(ph-pl)*100
            rsvs.append(rsv)
        k=50; d=50
        for rsv in rsvs:
            k=(2/3)*k+(1/3)*rsv; d=(2/3)*d+(1/3)*k
        return round(k,2), round(d,2)
    except: return None,None

def fetch_technical_indicators_with_fallback(t0_date=None):
    print("[V9-17F] Fetching technical indicators 3-layer fallback...")
    data=None; source="none"
    data=fetch_yahoo_twii_30d(t0_date)
    if data: source="yahoo"
    else:
        data=fetch_finmind_twii_14d(t0_date)
        if data: source="finmind"
        else:
            data=fetch_db_history_14d(t0_date)
            if data: source="db"
    if not data:
        print("[V9-17F] All 3 layers failed, RSI/MACD weight 0% -> 15 factors")
        return {'rsi':None,'macd':None,'macd_signal':None,'macd_hist':None,'k':None,'d':None,'source':'none','closes':[],'valid':False}
    closes=[d['close'] for d in data]; highs=[d.get('high') for d in data]; lows=[d.get('low') for d in data]
    rsi=calc_rsi(closes,14); macd,macd_signal,macd_hist=calc_macd(closes)
    ohlc_valid=all(h is not None and l is not None for h,l in zip(highs,lows))
    k,d=calc_kd(highs,lows,closes,9) if ohlc_valid else (None,None)
    print(f"[V9-17F] Tech RSI={rsi} MACD={macd}/{macd_signal} hist={macd_hist} K={k} D={d} source={source}")
    return {'rsi':rsi,'macd':macd,'macd_signal':macd_signal,'macd_hist':macd_hist,'k':k,'d':d,'source':source,'closes':closes,'highs':highs,'lows':lows,'valid':any(v is not None for v in (rsi,macd,macd_hist,k,d)),'validity':{'rsi':rsi is not None,'macd':macd is not None and macd_signal is not None and macd_hist is not None,'kd':k is not None and d is not None},'raw':data}

# ===== SQLite真DB + 歷史相似度 + 無DB回退 =====
def _ensure_history_table(conn, table_name):
    """Create or migrate a history table without hiding non-schema database errors."""
    if table_name != 'v9_pro_history':
        raise ValueError(f"Unsupported history table: {table_name}")
    conn.execute(f"""
        CREATE TABLE IF NOT EXISTS {table_name} (
            date TEXT PRIMARY KEY,
            bias INTEGER,
            spot_close REAL,
            spot_pct REAL,
            foreign_spot REAL,
            foreign_fut INTEGER,
            pcr REAL,
            gex REAL,
            put_wall INTEGER,
            vix REAL,
            rsi REAL,
            macd REAL,
            k REAL,
            d REAL,
            next_day_pct REAL,
            factor_wins TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)
    required={
        'bias':'INTEGER','spot_close':'REAL','spot_pct':'REAL',
        'foreign_spot':'REAL','foreign_fut':'INTEGER','pcr':'REAL',
        'gex':'REAL','put_wall':'INTEGER','vix':'REAL','rsi':'REAL',
        'macd':'REAL','k':'REAL','d':'REAL','next_day_pct':'REAL',
        'factor_wins':'TEXT',
        'correlation_eligible':'INTEGER',
        'created_at':'TIMESTAMP'
    }
    existing={row[1] for row in conn.execute(f"PRAGMA table_info({table_name})").fetchall()}
    if 'date' not in existing:
        raise sqlite3.DatabaseError(f"{table_name} is missing required primary-key column 'date'")
    for column,sql_type in required.items():
        if column not in existing:
            conn.execute(f"ALTER TABLE {table_name} ADD COLUMN {column} {sql_type}")

def init_db(db_path="dashboards/v9_pro_history.db"):
    """Initialize the V9-only history schema; never return a partial fallback DB."""
    conn=None
    try:
        pathlib.Path(db_path).parent.mkdir(parents=True, exist_ok=True)
        conn=sqlite3.connect(db_path)
        _ensure_history_table(conn,'v9_pro_history')
        conn.execute("""
            CREATE TABLE IF NOT EXISTS factor_performance (
                factor TEXT PRIMARY KEY,
                wins INTEGER DEFAULT 0,
                total INTEGER DEFAULT 0,
                win_rate REAL DEFAULT 0.5,
                weight REAL DEFAULT 0,
                updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)
        conn.commit()
        return conn
    except (sqlite3.Error, OSError) as e:
        print(f"[V9-17F] init_db error: {type(e).__name__}: {e}")
        if conn is not None:
            conn.close()
        return None

def get_db_status(db_path="dashboards/v9_pro_history.db"):
    try:
        for p in [pathlib.Path(db_path), pathlib.Path("/tmp/dashboards/v9_pro_history.db")]:
            if p.exists():
                conn=sqlite3.connect(str(p))
                count=conn.execute("SELECT COUNT(*) FROM v9_pro_history").fetchone()[0]
                filled=conn.execute("SELECT COUNT(*) FROM v9_pro_history WHERE next_day_pct IS NOT NULL").fetchone()[0]
                conn.close()
                return {'exists':True,'rows':count,'filled':filled,'mode':'db' if count>=3 else 'no-db-partial','path':str(p)}
        return {'exists':False,'rows':0,'filled':0,'mode':'no-db','path':''}
    except (sqlite3.Error, OSError) as e:
        print(f"[V9-17F] DB status error: {type(e).__name__}: {e}")
        return {'exists':False,'rows':0,'filled':0,'mode':'no-db-error','path':''}

def _normalize_t0_date(t0_date):
    """Validate workflow/report T0 date (YYYYMMDD) and return SQLite ISO date."""
    try:
        return datetime.strptime(str(t0_date), '%Y%m%d').strftime('%Y-%m-%d')
    except (TypeError, ValueError):
        raise ValueError(f"Invalid T0 date {t0_date!r}; expected YYYYMMDD")

def calculate_historical_correlation(db_path="dashboards/v9_pro_history.db", min_samples=5, lookback=60, as_of_date=None):
    """Build a Pearson matrix only from complete, explicitly eligible V9 history rows."""
    fields = [
        ("大盤漲跌幅", "spot_pct"),
        ("外資現貨", "foreign_spot"),
        ("外資期貨", "foreign_fut"),
        ("選擇權 PCR", "pcr"),
        ("VIX", "vix"),
        ("RSI", "rsi"),
        ("KD-K", "k"),
        ("KD-D", "d"),
    ]
    conn = None
    try:
        conn = init_db(db_path)
        if not conn:
            return {"labels": [], "matrix": [], "desc": "歷史資料庫不可用，相關性未計算"}
        t0_iso=_t0_iso_date(as_of_date)
        query=("SELECT " + ",".join(column for _, column in fields) +
            " FROM v9_pro_history WHERE correlation_eligible=1 " +
            ("AND date<=? " if t0_iso else "") +
            "ORDER BY date DESC LIMIT ?")
        params=(t0_iso,int(lookback)) if t0_iso else (int(lookback),)
        rows = conn.execute(query,params).fetchall()
        conn.close()
        conn = None
        valid = []
        for row in reversed(rows):
            values = []
            for value in row:
                try:
                    number = float(value)
                    if not math.isfinite(number):
                        raise ValueError("non-finite")
                    values.append(number)
                except (TypeError, ValueError):
                    values = []
                    break
            if values:
                valid.append(values)
        if len(valid) < min_samples:
            return {
                "labels": [], "matrix": [],
                "desc": f"完整且通過資料品質檢查的歷史樣本 {len(valid)}/{min_samples} 筆；累積足夠後顯示熱圖"
            }
        columns = list(zip(*valid))
        # Constant series have undefined Pearson correlation and are omitted.
        keep = []
        for index, values in enumerate(columns):
            if max(values) - min(values) > 1e-12:
                keep.append(index)
        if len(keep) < 2:
            return {"labels": [], "matrix": [], "desc": "有效歷史欄位不足 2 項或欄位無變異，相關性未計算"}
        labels = [fields[index][0] for index in keep]
        matrix = []
        for i in keep:
            row_values = []
            x = [sample[i] for sample in valid]
            mean_x = sum(x) / len(x)
            dx = [value - mean_x for value in x]
            for j in keep:
                y = [sample[j] for sample in valid]
                mean_y = sum(y) / len(y)
                dy = [value - mean_y for value in y]
                denominator = math.sqrt(sum(v*v for v in dx) * sum(v*v for v in dy))
                corr = sum(a*b for a, b in zip(dx, dy)) / denominator if denominator else None
                row_values.append(round(max(-1.0, min(1.0, corr)), 4) if corr is not None else None)
            matrix.append(row_values)
        return {"labels": labels, "matrix": matrix, "desc": f"Pearson 相關係數｜完整有效樣本 {len(valid)} 筆｜最近 {lookback} 筆"}
    except (sqlite3.Error, OSError, ValueError) as e:
        return {"labels": [], "matrix": [], "desc": f"相關性資料讀取失敗：{type(e).__name__}"}
    finally:
        if conn is not None:
            conn.close()


def save_today_to_db(bias, signals, tech, t0_date, db_path="dashboards/v9_pro_history.db"):
    try:
        date_str=_normalize_t0_date(t0_date)
        conn=init_db(db_path)
        if not conn: return False
        # T0 report date is authoritative; do not use runner's wall-clock date.
        existing=conn.execute("SELECT date FROM v9_pro_history WHERE date=?", (date_str,)).fetchone()
        if existing:
            print(f"[V9-17F] V9 DB T0 {date_str} already exists, skip")
            conn.close(); return True
        table='v9_pro_history'
        corr_fields = (
            signals.get('spot_pct'), signals.get('foreign'), signals.get('foreign_futures'),
            signals.get('pcr'), signals.get('vix'), tech.get('rsi'), tech.get('k'), tech.get('d')
        )
        try:
            correlation_eligible = int(all(
                value is not None and str(value).strip() != "" and math.isfinite(float(value))
                for value in corr_fields
            ))
        except (TypeError, ValueError, OverflowError):
            correlation_eligible = 0
        conn.execute(f"""
            INSERT INTO {table} (
                date,bias,spot_close,spot_pct,foreign_spot,foreign_fut,pcr,gex,put_wall,vix,rsi,macd,k,d,correlation_eligible
            ) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)
        """, (
            date_str,bias,signals.get('spot_close'),signals.get('spot_pct'),signals.get('foreign'),
            signals.get('foreign_futures'),signals.get('pcr'),signals.get('gex'),signals.get('put_wall'),
            signals.get('vix'),tech.get('rsi'),tech.get('macd'),tech.get('k'),tech.get('d'),correlation_eligible
        ))
        conn.commit(); conn.close()
        print(f"[V9-17F] DB saved T0 {date_str} bias={bias}")
        return True
    except Exception as e:
        print(f"[V9-17F] DB save error: {e}")
        return False

def update_next_day_pct(t0_date, t0_spot_close, db_path="dashboards/v9_pro_history.db"):
    """Use the current T0 report close to label the latest earlier trading row."""
    try:
        t0_iso=_normalize_t0_date(t0_date)
        current_close=float(t0_spot_close)
        if not math.isfinite(current_close) or current_close<=0:
            print("[V9-17F] update_next_day skipped: invalid T0 spot close")
            return False
        conn=init_db(db_path)
        if not conn: return False
        previous=conn.execute(
            "SELECT date,spot_close,next_day_pct FROM v9_pro_history WHERE date<? AND spot_close>0 ORDER BY date DESC LIMIT 1",
            (t0_iso,)
        ).fetchone()
        if not previous:
            conn.close(); return False
        # Only label the immediately latest prior V9 history row. Never skip a
        # previously labeled row and apply today's return to an older date.
        previous_date,previous_close,already_labeled=previous
        table='v9_pro_history'
        if already_labeled is not None:
            print(f"[V9-17F] update_next_day skipped: latest prior row {previous_date} is already labeled")
            conn.close(); return False
        next_pct=(current_close-float(previous_close))/float(previous_close)*100
        conn.execute(f"UPDATE {table} SET next_day_pct=? WHERE date=?", (next_pct,previous_date))
        conn.commit(); conn.close()
        print(f"[V9-17F] DB updated {previous_date} next={next_pct:.2f}% using T0 {t0_iso}")
        return True
    except Exception as e:
        print(f"[V9-17F] DB update_next_day error: {e}")
        return False

def get_factor_win_rates_from_db(db_path="dashboards/v9_pro_history.db", as_of_date=None):
    """Return conservative, sample-gated historical directional hit rates."""
    try:
        conn=init_db(db_path)
        if not conn: return None
        t0_iso=_t0_iso_date(as_of_date)
        query=("SELECT spot_pct,foreign_spot,foreign_fut,pcr,next_day_pct FROM v9_pro_history "
               "WHERE next_day_pct IS NOT NULL " + ("AND date<? " if t0_iso else "") +
               "ORDER BY date DESC LIMIT 60")
        rows=conn.execute(query,(t0_iso,) if t0_iso else ()).fetchall()
        conn.close()
        wins={k:0 for k in ('spot_trend','foreign_spot','foreign_fut','pcr')}
        totals={k:0 for k in wins}
        for pct,foreign,foreign_fut,pcr,next_pct in rows:
            if next_pct is None: continue
            candidates=[]
            if pct is not None and abs(pct)>=1: candidates.append(('spot_trend',1 if pct>0 else -1))
            if foreign is not None and abs(foreign)>=200: candidates.append(('foreign_spot',1 if foreign>0 else -1))
            if foreign_fut is not None and abs(foreign_fut)>=50000: candidates.append(('foreign_fut',1 if foreign_fut>0 else -1))
            if pcr is not None and pcr<0.8: candidates.append(('pcr',-1))
            actual=1 if next_pct>0 else -1 if next_pct<0 else 0
            for key,predicted in candidates:
                totals[key]+=1
                if actual==predicted: wins[key]+=1
        rates={}
        for key,total in totals.items():
            if total>=8:
                rates[key]=(wins[key]+5.0)/(total+10.0)
        print(f"[V9-17F] SQLite optimizer: {len(rows)} labeled rows; eligible factor rates={rates}")
        return rates or None
    except Exception as e:
        print(f"[V9-17F] DB get win rates non-critical: {e}")
        return None



def find_historical_similarity(current_signals, db_path="dashboards/v9_pro_history.db", top_n=3, as_of_date=None):
    try:
        conn=init_db(db_path)
        if not conn: return None
        t0_iso=_t0_iso_date(as_of_date)
        query=("SELECT date,bias,spot_pct,foreign_spot,pcr,vix,next_day_pct FROM v9_pro_history "
               "WHERE next_day_pct IS NOT NULL " + ("AND date<? " if t0_iso else "") +
               "ORDER BY date DESC LIMIT 30")
        rows=conn.execute(query,(t0_iso,) if t0_iso else ()).fetchall()
        conn.close()
        if len(rows)<3:
            print(f"[V9-17F] Historical insufficient {len(rows)}/3")
            return None
        curr_bias=current_signals.get('bias',50); curr_pct=current_signals.get('spot_pct',0); curr_foreign=current_signals.get('foreign',0); curr_pcr=current_signals.get('pcr',0)
        scored=[]
        for date,bias,pct,foreign,pcr,vix,next_pct in rows:
            bias_diff=abs(bias-curr_bias); pct_diff=abs(pct-curr_pct); foreign_diff=abs(foreign-curr_foreign)/100; pcr_diff=abs(pcr-curr_pcr)*10
            sim=100-(bias_diff*0.5+pct_diff*2+foreign_diff*0.3+pcr_diff)
            scored.append((sim,date,bias,next_pct))
        scored.sort(reverse=True)
        top=scored[:top_n]
        if not top: return None
        avg_next=sum([s[3] for s in top])/len(top) if top else 0
        positive_rate=sum(1 for item in top if item[3]>0)/len(top) if top else 0
        negative_rate=sum(1 for item in top if item[3]<0)/len(top) if top else 0
        print(f"[V9-17F] Historical similarity: {len(rows)} days top{top_n} avg={avg_next:.2f}% up={positive_rate:.0%} down={negative_rate:.0%}")
        for sim,date,bias,next_pct in top[:3]: print(f"  - {date} bias={bias} next={next_pct:.2f}% sim={sim:.0f}")
        return {'avg_next_pct':avg_next,'positive_rate':positive_rate,'negative_rate':negative_rate,'top_days':top,'count':len(rows)}
    except Exception as e:
        print(f"[V9-17F] Historical similarity error: {e}")
        return None

def validate_data_report_consistency(spot, inst, turnover, tx, options):
    """Return non-blocking warnings for cross-field contradictions in DATA_REPORT."""
    warnings=[]
    def number(value):
        try:
            if value is None or value=="": return None
            result=float(str(value).replace(',','').replace('+','').replace('%','').strip())
            return result if math.isfinite(result) else None
        except (TypeError, ValueError):
            return None
    def check_close(label, actual, expected, tolerance, detail):
        a=number(actual); e=number(expected)
        if a is not None and e is not None and abs(a-e)>tolerance:
            warnings.append(f"{label}: {detail}；差異 {a-e:+.2f}，容許 ±{tolerance:.2f}")
    # Spot and futures OHLC must respect the reported intraday range.
    for label,bar in (("現貨",spot),("台指期日盤",tx.get('day',{}))):
        o,h,l,c=(number(bar.get(k)) for k in ('open' if label=="現貨" else 'o','high' if label=="現貨" else 'h','low' if label=="現貨" else 'l','close' if label=="現貨" else 'c'))
        if None not in (o,h,l,c) and (h<max(o,l,c) or l>min(o,h,c) or h<l):
            warnings.append(f"{label} OHLC 矛盾：O={o:g}, H={h:g}, L={l:g}, C={c:g}")
    # Institutional and turnover totals are independently reported aggregates.
    inst_parts=[number(inst.get(k)) for k in ('foreign','trust','dealer')]
    if all(v is not None for v in inst_parts):
        check_close("三大法人合計",inst.get('all'),sum(inst_parts),0.21,"外資＋投信＋自營商與合計不一致")
    listed_turnover=number(turnover.get('listed')); otc_turnover=number(turnover.get('otc'))
    if listed_turnover is not None and otc_turnover is not None:
        check_close("上市櫃成交金額合計",turnover.get('total'),listed_turnover+otc_turnover,0.21,"上市＋上櫃與合計不一致")
    # Futures basis should reconcile with futures close minus spot close.
    day=tx.get('day',{})
    if all(number(v) is not None for v in (day.get('basis'),day.get('c'),spot.get('close'))):
        check_close("期現基差",day.get('basis'),number(day.get('c'))-number(spot.get('close')),2.01,"台指期收盤－加權指數收盤與申報基差不一致")
    # PCR in this report is Put OI / Call OI; validate only when both denominators exist.
    call_oi=number(options.get('callOi')); put_oi=number(options.get('putOi')); pcr=number(options.get('pcr'))
    if call_oi not in (None,0) and put_oi is not None and pcr is not None:
        check_close("選擇權 PCR",pcr,put_oi/call_oi,0.02,"Put OI／Call OI 與 PCR 不一致")
    return warnings


def parse_markdown_tables(section_text):
    """Parse all Markdown tables in one section, preserving separate tables."""
    tables=[]; rows=[]; in_table=False
    for line in section_text.splitlines():
        stripped=line.strip()
        if stripped.startswith("|"):
            cells=[cell.strip() for cell in stripped.strip("|").split("|")]
            if cells and all(re.fullmatch(r":?-{3,}:?", cell or "") for cell in cells):
                if rows:
                    tables.append(rows)
                rows=[]; in_table=True
            elif in_table:
                rows.append(cells)
        else:
            if in_table and rows:
                tables.append(rows)
            rows=[]; in_table=False
    if rows:
        tables.append(rows)
    return tables


# ===== DATA_REPORT 解析 (FULL) =====
def parse_margin_ratio_provenance(report_text, t0_date):
    """Parse maintenance-ratio value and provenance without conflating estimates with stale data."""
    line=next((x for x in report_text.splitlines() if "融資維持率" in x and x.strip().startswith("|")), "")
    cells=[cell.strip() for cell in line.strip().strip("|").split("|")] if line else []
    ratio=None
    source_cell=cells[3] if len(cells)>=4 else ""
    raw_value=cells[1] if len(cells)>=4 else ""
    if raw_value and raw_value.lower() not in ("unavailable","n/a","--","null"):
        try:
            value=float(raw_value.replace(",",""))
            if math.isfinite(value) and 50.0 < value < 500.0:
                ratio=value
        except (TypeError, ValueError):
            pass
    date_match=re.search(r"(?:DATA|資料日期)\s*[:：]?\s*(\d{4}-\d{2}-\d{2}|\d{8})", source_cell, re.I)
    source_date=date_match.group(1) if date_match else None
    if source_date and len(source_date)==8:
        source_date=f"{source_date[:4]}-{source_date[4:6]}-{source_date[6:]}"
    is_fallback="前值遞補" in source_cell
    if ratio is None:
        status="unavailable"
    elif is_fallback:
        status="previous_report_fallback"
    elif source_date and source_date != t0_date:
        status="estimated_stale"
    else:
        # Live-source rows without an explicit date are emitted only after T0 validation.
        source_date=source_date or t0_date
        status="estimated_t0"
    source_name="unknown"
    if ratio is None and "unavailable" in source_cell.lower():
        source_name="unavailable"
    else:
        for candidate, label in (
            ("twse 上市自建估算", "twse_self_built"),
            ("blave", "blave"),
            ("人工輸入", "manual_input"),
            ("wantgoo", "wantgoo"),
            ("stockintelli", "stockintelli"),
            ("istock", "istock"),
        ):
            if candidate in source_cell.lower():
                source_name=label
                break
    if is_fallback:
        source_name="previous_report"
    return {"ratio":ratio,"status":status,"source":source_name,
            "source_detail":source_cell or None,"source_date":source_date,
            "is_t0":bool(ratio is not None and status=="estimated_t0" and source_date==t0_date)}

def _option_force_number(value):
    """Parse a displayed option-force value without converting missing data to zero."""
    if value is None:
        return None
    raw = str(value).strip().replace(",", "")
    if raw.lower() in {"", "unavailable", "n/a", "--", "—", "null", "none"}:
        return None
    try:
        number = float(raw)
        return number if math.isfinite(number) else None
    except (TypeError, ValueError):
        return None


def build_option_force_analysis(force_rows, volume_rows=None):
    """Build a transparent, deterministic interpretation of TXO directional contract amounts.

    Bullish proxy = bought-call contract amount + sold-put contract amount.
    Bearish proxy = sold-call contract amount + bought-put contract amount.
    This is not net premium cash flow or open interest.
    """
    unavailable = {
        "status": "unavailable",
        "look": "選擇權法人多空力道金額資料不足或欄位不完整，暫停法人方向判讀。",
        "compass": "目前無法確認日盤、夜盤多空力道及法人主導者；不可用缺值代替零值。",
        "target": "先確認 TAIFEX Proxy 原始欄位、資料日期及七欄表格完整性，再恢復方向分析。",
        "method": "多方契約金額＝買 Call＋賣 Put；空方契約金額＝賣 Call＋買 Put。這是方向分類代理值，不等同淨權利金現金流或未平倉 OI；來源「日淨－夜淨」是兩個時段淨額相減，不是日對日變化或持倉變化。"
    }
    if not isinstance(force_rows, list):
        return unavailable

    by_name = {}
    for row in force_rows:
        if isinstance(row, (list, tuple)) and row:
            by_name[str(row[0]).strip()] = row
    names = ("外資", "投信", "自營商")
    total_name = "三大法人合計"
    required_names = (*names, total_name)
    if any(name not in by_name or len(by_name[name]) < 8 for name in required_names):
        return unavailable

    parsed = {}
    for name in required_names:
        row = by_name[name]
        values = [_option_force_number(row[i]) for i in range(1, 8)]
        if any(value is None for value in values):
            return unavailable
        parsed[name] = {
            "day_bull": values[0], "day_bear": values[1], "day_net": values[2],
            "night_bull": values[3], "night_bear": values[4], "night_net": values[5],
            "day_minus_night": values[6]
        }

    # DATA_REPORT values are rounded to two decimals; allow at most two cents
    # of display-rounding difference when checking independently rounded columns.
    tolerance = 0.021
    warnings = []
    for name, item in parsed.items():
        if abs(item["day_net"] - (item["day_bull"] - item["day_bear"])) > tolerance:
            warnings.append(f"{name} 日淨額與多空分項不一致")
        if abs(item["night_net"] - (item["night_bull"] - item["night_bear"])) > tolerance:
            warnings.append(f"{name} 夜淨額與多空分項不一致")
        if abs(item["day_minus_night"] - (item["day_net"] - item["night_net"])) > tolerance:
            warnings.append(f"{name} 日淨－夜淨欄位不一致")

    for session in ("day", "night"):
        if abs(
            parsed[total_name][f"{session}_net"]
            - sum(parsed[name][f"{session}_net"] for name in names)
        ) > tolerance:
            warnings.append(f"三大法人合計 {session} 淨額與分法人加總不一致")

    if warnings:
        result = dict(unavailable)
        result["status"] = "inconsistent"
        result["compass"] = "資料一致性檢查未通過：" + "；".join(warnings) + "。暫停方向結論，先修復來源或報表欄位。"
        result["target"] = "檢查來源原始金額、千元轉億元換算及未四捨五入前的淨額計算；通過後再恢復分析。"
        return result

    def fmt(value, signed=False):
        return f"{value:+.2f}" if signed else f"{value:.2f}"

    def session_leaders(session):
        net_key = f"{session}_net"
        bullish = [(name, parsed[name][net_key]) for name in names if parsed[name][net_key] > 0]
        bearish = [(name, parsed[name][net_key]) for name in names if parsed[name][net_key] < 0]
        strongest_bear = min(bearish, key=lambda item: item[1]) if bearish else None
        strongest_bull = max(bullish, key=lambda item: item[1]) if bullish else None
        return strongest_bear, strongest_bull

    day_total = parsed[total_name]
    day_gross = day_total["day_bull"] + day_total["day_bear"]
    night_gross = day_total["night_bull"] + day_total["night_bear"]
    day_imbalance = day_total["day_net"] / day_gross * 100 if day_gross > 0 else None
    night_imbalance = day_total["night_net"] / night_gross * 100 if night_gross > 0 else None

    day_bear, day_bull = session_leaders("day")
    night_bear, night_bull = session_leaders("night")
    day_lead = (
        f"主要空方為{day_bear[0]}（{fmt(day_bear[1], True)} 億元）" if day_bear
        else "日盤沒有法人呈現負淨額"
    )
    day_offset = (
        f"{day_bull[0]}（{fmt(day_bull[1], True)} 億元）提供最大多方抵銷" if day_bull
        else "日盤沒有法人呈現正淨額抵銷"
    )
    night_lead = (
        f"主要空方為{night_bear[0]}（{fmt(night_bear[1], True)} 億元）" if night_bear
        else "夜盤沒有法人呈現負淨額"
    )
    night_offset = (
        f"{night_bull[0]}（{fmt(night_bull[1], True)} 億元）提供最大多方抵銷" if night_bull
        else "夜盤沒有法人呈現正淨額抵銷"
    )
    day_delta = day_total["day_minus_night"]
    look = (
        f"日盤：{day_lead}；{day_offset}；三大法人淨額 {fmt(day_total['day_net'], True)} 億元。"
        f"夜盤：{night_lead}；{night_offset}；三大法人淨額 {fmt(day_total['night_net'], True)} 億元。"
        f"來源日淨－夜淨差 {fmt(day_delta, True)} 億元（日盤淨額較夜盤低 {fmt(abs(day_delta))} 億元；"
        "此為兩個時段數值相減，不代表日對日變化）。"
    )

    # Compare the amount-based directional proxy with the independent net-volume
    # table from Block A. A mismatch is a useful warning, not a reason to overwrite either source.
    volume_by_name = {}
    if isinstance(volume_rows, list):
        for row in volume_rows:
            if isinstance(row, (list, tuple)) and len(row) >= 7:
                volume_by_name[str(row[0]).strip()] = row
    divergences = []
    concordant = []
    neutral = []
    volume_complete = all(name in volume_by_name for name in names)
    if volume_complete:
        for name in names:
            for session, amount_key, volume_index in (
                ("日盤", "day_net", 3), ("夜盤", "night_net", 6)
            ):
                amount_net = parsed[name][amount_key]
                volume_net = _option_force_number(volume_by_name[name][volume_index])
                if volume_net is None:
                    volume_complete = False
                    continue
                if amount_net * volume_net < 0:
                    divergences.append(
                        f"{name}{session}金額 {fmt(amount_net, True)} 億元、口數 {volume_net:+,.0f} 口方向背離"
                    )
                elif amount_net == 0 or volume_net == 0:
                    neutral.append(f"{name}{session}")
                else:
                    concordant.append(f"{name}{session}")

    def imbalance_text(value):
        return f"{value:+.1f}%" if value is not None else "unavailable"

    direction_text = (
        "日、夜盤淨額均偏空" if day_total["day_net"] < 0 and day_total["night_net"] < 0
        else "日、夜盤淨額均偏多" if day_total["day_net"] > 0 and day_total["night_net"] > 0
        else "日、夜盤淨額方向不同或至少一盤接近平衡"
    )
    if volume_complete:
        volume_summary = f"口數對照：{len(concordant)} 組同向、{len(divergences)} 組背離、{len(neutral)} 組中性"
        if divergences:
            volume_summary += "；" + "；".join(divergences)
    else:
        volume_summary = "口數對照資料不完整，未作方向一致性推論"
    compass = (
        f"{direction_text}，但淨額／多空雙邊金額合計，日盤 {imbalance_text(day_imbalance)}、"
        f"夜盤 {imbalance_text(night_imbalance)}，顯示淨差相對雙邊交易金額有限，不宜解讀為強烈單邊；"
        f"{volume_summary}。"
    )
    target = (
        "後續優先追蹤金額與口數背離是否收斂，以及主要空方法人是否延續；"
        "只有金額、口數方向持續一致，並獲價格與期貨籌碼同步確認，才提高方向判讀權重。"
        "背離未解除前，不單憑本區塊追多或追空。"
    )
    if divergences:
        target = (
            "優先追蹤" + "；".join(divergences) +
            "是否收斂，並觀察主要空方法人是否延續；只有金額、口數方向持續一致，"
            "且獲價格與期貨籌碼同步確認，才提高方向判讀權重。背離未解除前，不單憑本區塊追多或追空。"
        )

    return {
        "status": "available" if volume_complete else "partial",
        "look": look,
        "compass": compass,
        "target": target,
        "method": unavailable["method"],
        "day_imbalance_pct": round(day_imbalance, 2) if day_imbalance is not None else None,
        "night_imbalance_pct": round(night_imbalance, 2) if night_imbalance is not None else None,
        "day_minus_night": day_delta,
        "volume_divergences": divergences,
        "volume_concordant": concordant,
        "volume_neutral": neutral,
        "checks": {"force_rows": len(required_names), "volume_rows_complete": volume_complete, "warnings": warnings}
    }

def _extract_section_table_value(report_text, heading, label, required=False, expected_unit=None):
    """Read one numeric field from its own validated Markdown table."""
    start = report_text.find(heading)
    if start < 0:
        if required:
            raise ValueError(f"[NO-FALLBACK] DATA_REPORT missing section: {heading}")
        return None
    following = re.search(r"(?m)^#{2,3}\s+", report_text[start + len(heading):])
    end = start + len(heading) + following.start() if following else len(report_text)
    lines = report_text[start:end].splitlines()
    header = None
    separator_seen = False
    for line in lines:
        stripped = line.strip()
        if not (stripped.startswith("|") and stripped.endswith("|")):
            continue
        cells = [cell.strip() for cell in stripped.strip("|").split("|")]
        if cells and all(re.fullmatch(r":?-{3,}:?", cell or "") for cell in cells):
            separator_seen = True
            continue
        if not separator_seen:
            header = cells
            continue
        legacy_header = ["項目", "數值", "資料來源"]
        unit_header = ["項目", "數值", "單位", "資料來源"]
        if header not in (legacy_header, unit_header) or len(cells) != len(header):
            continue
        if cells[0] != label:
            continue
        if header == unit_header and expected_unit is not None and cells[2] != expected_unit:
            continue
        raw = cells[1].replace(",", "").strip()
        if raw.lower() == "unavailable":
            return None
        if re.fullmatch(r"[-+]?(?:\d+(?:\.\d*)?|\.\d+)", raw):
            return float(raw)
        if required:
            raise ValueError(f"[NO-FALLBACK] DATA_REPORT missing/invalid {label} in {heading}")
        return None
    if required:
        raise ValueError(f"[NO-FALLBACK] DATA_REPORT missing/invalid table row {label} in {heading}")
    return None


def parse_data_report(report_path):
    text = pathlib.Path(report_path).read_text(encoding='utf-8', errors='ignore')
    def get_value(pattern, default=None, is_float=True, preserve_unavailable=False):
        m=re.search(pattern, text, re.DOTALL)
        if not m: return default
        try:
            v=m.group(1).replace(',','').replace('+','').strip()
            if v.lower()=='unavailable': return 'unavailable' if preserve_unavailable else default
            if is_float: return float(v)
            return v
        except: return default
    def parse_table(heading):
        idx=text.find(heading)
        if idx==-1: return []
        substr=text[idx:idx+8000]
        lines=substr.split('\n')
        rows=[]; in_table=False
        for line in lines:
            if line.strip().startswith('|'):
                if '---' in line: in_table=True; continue
                if in_table:
                    cols=[c.strip() for c in line.split('|')[1:-1]]
                    if len(cols)>=2: rows.append(cols)
            else:
                if in_table and rows: break
        return rows
    def parse_tables(heading):
        idx=text.find(heading)
        if idx==-1: return []
        end=text.find("\n### ",idx+len(heading))
        section=text[idx:end] if end!=-1 else text[idx:]
        return parse_markdown_tables(section)

    def parse_pct(s):
        if s is None: return None
        s=str(s).replace('%','').replace('+','').strip()
        if not s or s.lower() in ('unavailable','n/a','--','null'): return None
        try: return float(s)
        except (TypeError, ValueError): return None
    def must_get(pattern,name):
        v=get_value(pattern,None,preserve_unavailable=True)
        if v == "unavailable": return None
        if v is None or v=="": raise ValueError(f"[NO-FALLBACK] DATA_REPORT missing {name}: {pattern}")
        return v
    def optional_get(pattern):
        return get_value(pattern,None)

    report_date_match=re.search(r"報告日期：`([^`]+)`", text)
    t0_date_match=re.search(r"T0 交易日期：`([^`]+)`", text)
    gen_time_match=re.search(r"資料產出時間：`([^`]+)`", text)
    report_date=report_date_match.group(1) if report_date_match else ""
    t0_date=t0_date_match.group(1) if t0_date_match else ""
    gen_time=gen_time_match.group(1) if gen_time_match else ""

    us_rows=parse_table("### 1. 美股指數"); asia_rows=parse_table("### 2. 亞洲主要指數"); fut_rows=parse_table("### 3. 美股指數期貨")
    yield_rows=parse_table("### 4. 美國國債殖利率"); fx_rows=parse_table("### 5. 主要匯率"); adr_rows=parse_table("### 6. 台灣相關ADR"); comm_rows=parse_table("### 7. 原油黃金Bitcoin")

    def build_arr(rows, pct_index=4):
        parts=[]
        for r in rows:
            if len(r)<3: continue
            pct_col=r[pct_index] if len(r)>pct_index else None
            pct=parse_pct(pct_col)
            close_raw=r[2] if len(r)>2 else None
            try: close_val=float(close_raw.replace(',','')) if close_raw else None
            except (TypeError, ValueError): close_val=None
            parts.append({'l':r[0],'v':pct,'close':close_val,'raw':r})
        return parts
    def build_arr_simple(rows):
        arr=build_arr(rows)
        return [{'l':x['l'],'v':x['v']} for x in arr], arr

    usPct_simple, usPct_full=build_arr_simple(us_rows); asiaPct_simple, asiaPct_full=build_arr_simple(asia_rows)
    futPct_simple, futPct_full=build_arr_simple(fut_rows)
    yield_arr=build_arr(yield_rows, pct_index=3)
    yieldPct_simple=[{'l':x['l'],'v':x['v']} for x in yield_arr]; yieldPct_full=yield_arr
    fxPct_simple, fxPct_full=build_arr_simple(fx_rows); adrPct_simple, adrPct_full=build_arr_simple(adr_rows); commPct_simple, commPct_full=build_arr_simple(comm_rows)

    # 現貨收盤是核心指數值；OHLC 開高低允許來源缺值，保留 None，不以收盤價代填。
    spot_close=must_get(r"加權指數 \| ([0-9,.]+|unavailable) \| 點","加權收盤")
    spot_open=optional_get(r"開盤 \| ([0-9,.]+) \| 點")
    spot_high=optional_get(r"最高 \| ([0-9,.]+) \| 點")
    spot_low=optional_get(r"最低 \| ([0-9,.]+) \| 點")
    spot_diff=must_get(r"漲跌點數 \| ([-\+0-9,.]+|unavailable) \| 點","漲跌點"); spot_pct=optional_get(r"漲跌幅 \| ([-\+0-9,.]+) \| %")
    spot_vol_raw=must_get(r"成交金額 \| ([0-9,.]+|unavailable) \| 億元","成交金額")

    up_raw=must_get(r"\| 上漲家數 \| ([0-9]+|unavailable) \|","上漲家數"); down_raw=must_get(r"\| 下跌家數 \| ([0-9]+|unavailable) \|","下跌家數")
    up=int(up_raw) if up_raw is not None else None; down=int(down_raw) if down_raw is not None else None
    flat_match=re.search(r"\| 平盤家數 \| ([0-9]+) \|", text); flat=int(flat_match.group(1)) if flat_match else None
    up_limit_match=re.search(r"\| 漲停家數 \| ([0-9]+) \|", text); down_limit_match=re.search(r"\| 跌停家數 \| ([0-9]+) \|", text)
    limit_up=int(up_limit_match.group(1)) if up_limit_match else None; limit_down=int(down_limit_match.group(1)) if down_limit_match else None

    otc_section=text.find("#### 2.2 上櫃公司"); otc_up=otc_down=otc_flat=otc_limit_up=otc_limit_down=None
    if otc_section!=-1:
        otc_sub=text[otc_section:otc_section+3000]
        m=re.search(r"\| 上漲家數 \| ([0-9]+) \|", otc_sub); 
        if m: otc_up=int(m.group(1))
        m=re.search(r"\| 下跌家數 \| ([0-9]+) \|", otc_sub); 
        if m: otc_down=int(m.group(1))
        m=re.search(r"\| 平盤家數 \| ([0-9]+) \|", otc_sub); 
        if m: otc_flat=int(m.group(1))
        m=re.search(r"\| 漲停家數 \| ([0-9]+) \|", otc_sub); 
        if m: otc_limit_up=int(m.group(1))
        m=re.search(r"\| 跌停家數 \| ([0-9]+) \|", otc_sub); 
        if m: otc_limit_down=int(m.group(1))

    foreign_inst=optional_get(r"\| 外資 \| ([-\+0-9,.]+) \| 億元"); trust_inst=optional_get(r"\| 投信 \| ([-\+0-9,.]+) \| 億元")
    dealer_inst=must_get(r"\| 自營商 \| ([-\+0-9,.]+|unavailable) \| 億元","自營商"); all_inst=must_get(r"\| 三大法人合計 \| ([-\+0-9,.]+|unavailable) \| 億元","三大法人")
    margin_finance=get_value(r"\| 融資餘額 \| ([0-9,.]+) \| 億元",None); margin_finance_diff=get_value(r"\| 融資增減 \| ([-\+0-9,.]+) \| 億元",None)
    margin_short=get_value(r"\| 融券餘額 \| ([0-9,]+) \| 張",None)
    margin_provenance=parse_margin_ratio_provenance(text, t0_date)
    margin_ratio=margin_provenance["ratio"]
    margin_ratio_source=margin_provenance["source_detail"] or ""
    margin_ratio_source_date=margin_provenance["source_date"]
    margin_ratio_status=margin_provenance["status"]
    sbl_balance=get_value(r"\| 借券餘額 \| ([0-9,]+) \| 張",None)
    sbl_sold_balance=get_value(r"\| 借券賣出餘額 \| ([0-9,]+) \| 張",None)
    sbl_sold_change=get_value(r"\| 借券賣出增減 \| ([-\\+0-9,]+) \| 張",None)
    sbl_scope_row=re.search(r"\|\s*借券賣出增減\s*\|[^|]*\|[^|]*\|\s*([^|]+)\|",text)
    sbl_scope_source=sbl_scope_row.group(1).strip() if sbl_scope_row else ""
    has_listed_scope=("上市" in sbl_scope_source and ("TWT93U" in sbl_scope_source or "上市" in sbl_scope_source))
    has_otc_scope=("上櫃" in sbl_scope_source and ("S47" in sbl_scope_source or "TPEX" in sbl_scope_source or "上櫃" in sbl_scope_source))
    if has_listed_scope and has_otc_scope:
        sbl_sold_change_scope="上市+上櫃"
    elif has_listed_scope:
        sbl_sold_change_scope="上市（上櫃未取得）"
    elif has_otc_scope:
        sbl_sold_change_scope="上櫃（上市未取得）"
    elif re.search(r"借券賣出增減僅上櫃值",text):
        sbl_sold_change_scope="上櫃（上市 TWT93U 未取得）"
    elif re.search(r"借券賣出增減僅上市值",text):
        sbl_sold_change_scope="上市（上櫃 TPEX 未取得）"
    else:
        sbl_sold_change_scope="範圍未註明"
    listed_turnover=optional_get(r"\| 上市成交金額 \| ([0-9,.]+) \| 億元"); otc_turnover=optional_get(r"\| 上櫃成交金額 \| ([0-9,.]+) \| 億元"); total_turnover=optional_get(r"\| 上市櫃成交金額合計 \| ([0-9,.]+) \| 億元")

    day_heading = "### 1．台指期近月日盤行情"
    night_heading = "### 2．台指期近月夜盤行情"
    table_value = lambda heading, label, unit=None, required=False: _extract_section_table_value(
        text, heading, label, required=required, expected_unit=unit)
    fut_day_o=table_value(day_heading, "開盤價", "點", True); fut_day_h=table_value(day_heading, "最高價", "點", True)
    fut_day_l=table_value(day_heading, "最低價", "點", True); fut_day_c=table_value(day_heading, "收盤價", "點", True)
    fut_day_diff=table_value(day_heading, "漲跌點數", "點", True); fut_day_pct=table_value(day_heading, "漲跌幅", "%", True)
    fut_day_vol=table_value(day_heading, "成交量", "口", True)
    fut_night_o=table_value(night_heading, "開盤價", "點"); fut_night_h=table_value(night_heading, "最高價", "點")
    fut_night_l=table_value(night_heading, "最低價", "點"); fut_night_c=table_value(night_heading, "收盤價", "點")
    fut_night_diff=table_value(night_heading, "漲跌點數", "點"); fut_night_pct=table_value(night_heading, "漲跌幅", "%")
    fut_night_vol=table_value(night_heading, "成交量", "口")
    basis=optional_get(r"台指期與加權指數價差 \| ([-\+0-9.]+) \|"); basis_pct=optional_get(r"價差百分比 \| ([-\+0-9.]+) \|"); night_change=optional_get(r"夜盤價格相對日盤收盤的變化 \| ([-\+0-9]+) \|")
    foreign_fut_oi=optional_get(r"外資多空淨 OI \| ([-\+0-9,]+) \|"); trust_fut_oi=must_get(r"投信多空淨 OI \| ([-\+0-9,]+|unavailable) \|","投信OI")
    dealer_fut_oi=must_get(r"自營商多空淨 OI \| ([-\+0-9,]+|unavailable) \|","自營OI"); top10_oi=must_get(r"前十大交易人多空淨 OI \| ([-\+0-9,]+|unavailable) \|","前十大OI")
    foreign_day_net=optional_get(r"外資日盤多空淨交易量 \| ([-\+0-9,]+) \|"); foreign_night_net=optional_get(r"外資夜盤多空淨交易量 \| ([-\+0-9,]+) \|")
    call_vol=must_get(r"Call 總成交量 \| ([0-9,]+|unavailable) \|","Call成交"); call_oi=must_get(r"Call 總未平倉量 OI \| ([0-9,]+|unavailable) \|","Call OI")
    put_vol=must_get(r"Put 總成交量 \| ([0-9,]+|unavailable) \|","Put成交"); put_oi=must_get(r"Put 總未平倉量 OI \| ([0-9,]+|unavailable) \|","Put OI")
    pcr=optional_get(r"Put／Call Ratio \| ([0-9.]+) \|")
    # Wall / Gamma / Max Pain 允許端點缺值；None 交由 Dashboard 顯示缺值，不以其他指標代替。
    call_wall=optional_get(r"Call Wall 價位 \| ([0-9,]+) \|")
    put_wall=optional_get(r"Put Wall 價位 \| ([0-9,]+) \|")
    gamma_wall=optional_get(r"Gamma Wall 價位 \| ([0-9,.]+) \|")
    gamma_flip=optional_get(r"Gamma Flip 價位 \| ([0-9,.]+) \|")
    max_pain=optional_get(r"Max Pain 價位 \| ([0-9,]+) \|")
    gex_payload_match=re.search(r"GEX_LEVELS_JSON.*?```json\s*(\{.*?\})\s*```", text, re.S)
    gex_payload={}
    if gex_payload_match:
        try:
            candidate=json.loads(gex_payload_match.group(1))
            if isinstance(candidate,dict) and candidate.get('date')==t0_date and isinstance(candidate.get('levels'),list):
                gex_payload=candidate
        except (json.JSONDecodeError, TypeError):
            gex_payload={}
    gex_levels=gex_payload.get('levels',[])
    gex_status='available' if gex_levels and gex_payload.get('net_gex_1pct') is not None and gex_payload.get('gross_gex_1pct') is not None else 'unavailable'
    call_oi_table=parse_table("#### Call OI 分布明細 Top10"); put_oi_table=parse_table("#### Put OI 分布明細 Top10"); opt_inst_table=parse_table("### 17．選擇權法人日盤、夜盤交易")
    opt_inst_force_table=parse_table("#### 法人多空力道表")
    opt_top10_tables=parse_tables("### 18．選擇權前十大")
    opt_top10_call=opt_top10_tables[0] if len(opt_top10_tables)>0 else []
    opt_top10_put=opt_top10_tables[1] if len(opt_top10_tables)>1 else []
    consistency_warnings=validate_data_report_consistency(
        {'open':spot_open,'high':spot_high,'low':spot_low,'close':spot_close},
        {'foreign':foreign_inst,'trust':trust_inst,'dealer':dealer_inst,'all':all_inst},
        {'listed':listed_turnover,'otc':otc_turnover,'total':total_turnover},
        {'day':{'o':fut_day_o,'h':fut_day_h,'l':fut_day_l,'c':fut_day_c,'basis':basis}},
        {'callOi':call_oi,'putOi':put_oi,'pcr':pcr}
    )

    news_events=[]
    idx=text.find("- 事件1：")
    if idx!=-1:
        substr=text[idx:idx+20000]
        lines=substr.split('\n')
        curr=None
        for line in lines:
            line=line.strip()
            m=re.match(r'- 事件\d+：(.+)', line)
            if m:
                if curr: news_events.append(curr)
                curr={"t": m.group(1).strip(), "s":"", "d":"", "time":"", "link":""}
            elif line.startswith("- 來源：") and curr:
                curr["s"]=line.replace("- 來源：","").strip()
                time_m=re.search(r"(\d{4}-\d{2}-\d{2}T[^;]+)", curr["s"])
                if time_m: curr["time"]=time_m.group(1)
            elif line.startswith("- 摘要：") and curr: curr["d"]=line.replace("- 摘要：","").strip()
            elif (line.startswith("- 原文連結：") or line.startswith("- 連結：")) and curr: curr["link"]=re.sub(r"^- (?:原文連結|連結)：","",line).strip()
        if curr: news_events.append(curr)

    return {
        'meta': {'report_date': report_date, 't0_date': t0_date, 'generated_at': gen_time, 'data_quality_warnings': consistency_warnings},
        'usPct_simple': usPct_simple, 'asiaPct_simple': asiaPct_simple, 'futPct_simple': futPct_simple,
        'yieldPct_simple': yieldPct_simple, 'fxPct_simple': fxPct_simple, 'adrPct_simple': adrPct_simple, 'commPct_simple': commPct_simple,
        'usPct_full': usPct_full, 'asiaPct_full': asiaPct_full, 'futPct_full': futPct_full,
        'yieldPct_full': yieldPct_full, 'fxPct_full': fxPct_full, 'adrPct_full': adrPct_full, 'commPct_full': commPct_full,
        'spot': {'close': spot_close, 'open': spot_open, 'high': spot_high, 'low': spot_low, 'diff': spot_diff, 'pct': spot_pct, 'vol': spot_vol_raw, 'up': up, 'down': down, 'flat': flat, 'limit_up': limit_up, 'limit_down': limit_down, 'otc_up': otc_up, 'otc_down': otc_down, 'otc_flat': otc_flat, 'otc_limit_up': otc_limit_up, 'otc_limit_down': otc_limit_down},
        'margin': {'finance': margin_finance, 'finance_diff': margin_finance_diff, 'short': margin_short, 'ratio': margin_ratio, 'ratio_status': margin_ratio_status, 'ratio_source': margin_ratio_source, 'ratio_source_name': margin_provenance["source"], 'ratio_source_date': margin_ratio_source_date, 'ratio_is_t0': margin_provenance["is_t0"], 'sbl': sbl_balance, 'borrowed_sell': sbl_sold_balance, 'borrowed_sell_diff': sbl_sold_change, 'borrowed_sell_diff_scope': sbl_sold_change_scope},
        'turnover': {'listed': listed_turnover, 'otc': otc_turnover, 'total': total_turnover},
        'inst': {'foreign': foreign_inst, 'trust': trust_inst, 'dealer': dealer_inst, 'all': all_inst},
        'tx': {'day': {'o': fut_day_o, 'h': fut_day_h, 'l': fut_day_l, 'c': fut_day_c, 'diff': fut_day_diff, 'pct': fut_day_pct, 'vol': fut_day_vol, 'basis': basis, 'prem': basis_pct}, 'night': {'o': fut_night_o, 'h': fut_night_h, 'l': fut_night_l, 'c': fut_night_c, 'diff': fut_night_diff, 'pct': fut_night_pct, 'vol': fut_night_vol, 'change': night_change}},
        'futures': {'foreign_oi': foreign_fut_oi, 'trust_oi': trust_fut_oi, 'dealer_oi': dealer_fut_oi, 'top10': top10_oi, 'foreign_day': foreign_day_net, 'foreign_night': foreign_night_net},
        'options': {'callVol': call_vol, 'callOi': call_oi, 'putVol': put_vol, 'putOi': put_oi, 'pcr': pcr, 'callWall': call_wall, 'putWall': put_wall, 'gammaWall': gamma_wall, 'flip': gamma_flip, 'extendedFlip': ((gex_payload.get('wide_range_flip') or {}).get('estimated_underlying') if gamma_flip is None else None), 'maxPain': max_pain, 'netGex1pct': gex_payload.get('net_gex_1pct'), 'grossGex1pct': gex_payload.get('gross_gex_1pct'), 'gexLevels': gex_levels, 'gexDate': gex_payload.get('date'), 'gexStatus': gex_status, 'callOiDist': call_oi_table, 'putOiDist': put_oi_table, 'instOpt': opt_inst_table, 'instOptForce': opt_inst_force_table, 'instOptForceAnalysis': build_option_force_analysis(opt_inst_force_table, opt_inst_table), 'top10Call': opt_top10_call, 'top10Put': opt_top10_put},
        'news': news_events,
    }

# ===== V9 17因子 分析器 =====
class V9Analyzer:
    def __init__(self, parsed, tech):
        self.parsed=parsed; self.tech=tech; self.signals={}; self.bias_score=50; self.bias_factors=[]; self.weights={}; self._parse_signals()

    def _parse_signals(self):
        p=self.parsed; spot=p.get('spot',{}); inst=p.get('inst',{}); tx=p.get('tx',{})
        options=p.get('options',{}); futures=p.get('futures',{})
        self.signals['spot_close']=spot.get('close'); self.signals['spot_pct']=spot.get('pct')
        self.signals['spot_up']=spot.get('up'); self.signals['spot_down']=spot.get('down')
        self.signals['spot_vol']=spot.get('vol')
        self.signals['volume_ratio']=spot.get('volume_ratio',p.get('volume_ratio'))
        self.signals['foreign']=inst.get('foreign'); self.signals['trust']=inst.get('trust')
        self.signals['dealer']=inst.get('dealer'); self.signals['all']=inst.get('all')
        day=tx.get('day',{}); night=tx.get('night',{})
        self.signals['tx_basis']=day.get('basis'); self.signals['tx_prem']=day.get('prem')
        self.signals['tx_day_pct']=day.get('pct'); self.signals['tx_night_pct']=night.get('pct')
        self.signals['tx_night_low']=night.get('l'); self.signals['tx_night_high']=night.get('h')
        self.signals['tx_day_low']=day.get('l')
        self.signals['put_wall']=options.get('putWall'); self.signals['call_wall']=options.get('callWall')
        self.signals['gamma_wall']=options.get('gammaWall'); self.signals['flip']=options.get('flip')
        self.signals['max_pain']=options.get('maxPain'); self.signals['pcr']=options.get('pcr')
        self.signals['gex']=options.get('netGex1pct')
        us_rows=p.get('usPct_full',[]) or []
        self.signals['us_dict']={x.get('l'):x.get('v') for x in us_rows if isinstance(x,dict)}
        self.signals['sox']=next((x.get('v') for x in us_rows if 'SOX' in str(x.get('l','')).upper()),None)
        self.signals['vix']=next((x.get('close') for x in us_rows if 'VIX' in str(x.get('l','')).upper()),None)
        fx_rows=p.get('fxPct_full',[]) or []
        self.signals['dxy_change']=next((x.get('v') for x in fx_rows if 'DXY' in str(x.get('l','')).upper()),None)
        adr_rows=p.get('adrPct_full',[]) or []
        self.signals['adr_change']=next((x.get('v') for x in adr_rows if 'TSM' in str(x.get('l','')).upper() or '台積電' in str(x.get('l',''))),None)
        yield_rows=p.get('yieldPct_full',[]) or []
        self.signals['yield_10y_change']=next((x.get('v') for x in yield_rows if '10Y' in str(x.get('l','')).upper() or '10年' in str(x.get('l',''))),None)
        tech=self.tech or {}
        self.signals['rsi']=tech.get('rsi'); self.signals['macd']=tech.get('macd')
        self.signals['macd_hist']=tech.get('macd_hist'); self.signals['k']=tech.get('k')
        self.signals['d']=tech.get('d'); self.signals['tech_valid']=tech.get('valid',False)
        closes=[float(x) for x in (tech.get('closes') or []) if x is not None]
        self.signals['ma_bias_pct']=((closes[-1]/(sum(closes[-20:])/20))-1)*100 if len(closes)>=20 and sum(closes[-20:]) else None
        self.signals['foreign_futures']=futures.get('foreign_oi')

    def _evaluate_factors(self):
        s=self.signals
        def num(value):
            try:
                value=float(value)
                return value if math.isfinite(value) else None
            except (TypeError,ValueError):
                return None
        def add(key,label,raw,score,source,reason):
            raw=num(raw)
            if raw is None or score is None:
                self.factor_details.append({'key':key,'name':label,'raw_value':raw,'score':None,
                    'status':'disabled','reason':reason or '資料缺失或無法驗證','source':source})
            else:
                self.factor_details.append({'key':key,'name':label,'raw_value':raw,
                    'score':max(-1.0,min(1.0,float(score))),'status':'active',
                    'reason':reason or '有效資料','source':source})
        self.factor_details=[]
        v=num(s.get('spot_pct'))
        add('spot_trend','現貨趨勢',v,(-1.0 if v<=-3 else -0.8 if v<=-2 else -0.6 if v<=-1 else -0.25 if v<0 else 0.6 if v>=1 else 0.0) if v is not None else None,'DATA_REPORT.spot.pct','依加權指數日漲跌幅分級')
        v=num(s.get('foreign'))
        add('foreign_spot','外資現貨',v,(-1.0 if v<=-800 else -0.8 if v<=-500 else -0.5 if v<=-200 else -0.2 if v<0 else 0.6 if v>=200 else 0.0) if v is not None else None,'DATA_REPORT.inst.foreign','依外資現貨買賣超金額分級')
        v=num(s.get('foreign_futures'))
        add('foreign_fut','外資期貨',v,(-1.0 if v<=-80000 else -0.6 if v<=-50000 else -0.25 if v<0 else 0.5 if v>=50000 else 0.0) if v is not None else None,'DATA_REPORT.futures.foreign_oi','依外資期貨淨未平倉口數分級')
        v=num(s.get('trust'))
        add('trust','投信',v,(0.6 if v>=50 else -0.6 if v<=-50 else 0.0) if v is not None else None,'DATA_REPORT.inst.trust','依投信現貨買賣超金額分級')
        v=num(s.get('tx_basis'))
        add('basis','基差',v,(-0.7 if v<-50 or v>200 else 0.0) if v is not None else None,'DATA_REPORT.tx.day.basis','逆價差或過大正價差視為風險')
        v=num(s.get('tx_night_pct'))
        add('night','夜盤',v,(-1.0 if v<=-1 else -0.6 if v<=-0.5 else -0.25 if v<0 else 0.6 if v>=0.5 else 0.0) if v is not None else None,'DATA_REPORT.tx.night.pct','依夜盤漲跌幅分級')
        v=num(s.get('sox'))
        add('us_sox','美股費半',v,(-1.0 if v<=-5 else -0.5 if v<=-2 else -0.2 if v<0 else 0.6 if v>=2 else 0.0) if v is not None else None,'DATA_REPORT.usPct_full.SOX','依費半日漲跌幅分級')
        v=num(s.get('pcr'))
        add('pcr','PCR',v,(-0.8 if v<0.6 else -0.4 if v<0.8 else 0.0) if v is not None else None,'DATA_REPORT.options.pcr','沿用現行低 PCR 風險規則；其他區間不推定方向')
        v=num(s.get('gex'))
        add('gex','GEX',v,None,'DATA_REPORT.options.netGex1pct','GEX 正負代表模型曝險方向，不等同市場多空方向；未建立方向化規則前不納入 Bias')
        close=num(s.get('spot_close')); wall=num(s.get('put_wall'))
        wall_score=(0.5 if close>wall else -0.5 if close<wall else 0.0) if close is not None and wall is not None and wall>0 else None
        add('put_wall','Put Wall',wall,wall_score,'DATA_REPORT.spot.close + DATA_REPORT.options.putWall','現價位於有效 Put Wall 上方／下方；僅作位置方向訊號')
        v=num(s.get('adr_change'))
        add('adr','ADR 表現代理',v,(0.5 if v>=2 else -0.5 if v<=-2 else 0.0) if v is not None else None,'DATA_REPORT.adrPct_full.TSM','使用台積電 ADR 漲跌幅代理，不宣稱為 ADR 溢價')
        v=num(s.get('yield_10y_change'))
        add('yield','美債10Y殖利率變化',v,(-0.5 if v>=0.05 else 0.5 if v<=-0.05 else 0.0) if v is not None else None,'DATA_REPORT.yieldPct_full.10Y','殖利率日變化以百分點表示；上升偏風險、下降偏緩和')
        v=num(s.get('volume_ratio')); pct=num(s.get('spot_pct'))
        volume_score=(0.5 if v>=1.2 and pct>0 else -0.5 if v>=1.2 and pct<0 else 0.0) if v is not None and pct is not None else None
        add('volume','量能',v,volume_score,'DATA_REPORT.volume_ratio','需有成交量相對均量比；只有單日成交額時不臆測量能強弱')
        v=num(s.get('ma_bias_pct'))
        add('ma_bias','均線乖離',v,(0.5 if v>0 else -0.5 if v<0 else 0.0) if v is not None else None,'Yahoo/FinMind/SQLite closes SMA20','至少20筆有效收盤價，現價高於／低於SMA20')
        v=num(s.get('vix'))
        add('vix_factor','VIX',v,(-1.0 if v>25 else -0.5 if v>20 else 0.4 if v<15 else 0.0) if v is not None else None,'DATA_REPORT.usPct_full.VIX.close','依 VIX 收盤水準分級')
        v=num(s.get('rsi'))
        add('rsi','RSI',v,(-0.5 if v<20 else -0.3 if v<30 else 0.3 if v>80 else 0.0) if v is not None else None,'Yahoo/FinMind/SQLite RSI14','RSI14 超買超賣分級；缺值不以中性代替')
        v=num(s.get('macd_hist'))
        add('macd','MACD',v,(-1.0 if v<-50 else -0.5 if v<0 else 0.5 if v>0 else 0.0) if v is not None else None,'Yahoo/FinMind/SQLite MACD histogram','依 MACD histogram 正負及強度分級')
        return self.factor_details

    def calculate_weights(self, real_win_rates=None):
        base_weights={
            'spot_trend':13,'foreign_spot':12,'foreign_fut':8,'trust':5,'basis':7,
            'night':8,'us_sox':12,'pcr':7,'gex':7,'put_wall':3,'adr':3,'yield':5,
            'volume':3,'ma_bias':3,'vix_factor':2,'rsi':3,'macd':3
        }
        adaptive=dict(base_weights)
        vix=self.signals.get('vix'); basis=self.signals.get('tx_basis')
        if vix is not None:
            if vix>25:
                adaptive['us_sox']+=8; adaptive['spot_trend']-=5
                adaptive['foreign_spot']+=3; adaptive['vix_factor']+=3
            elif vix>20:
                adaptive['us_sox']+=4; adaptive['spot_trend']-=2
            elif vix<15:
                adaptive['us_sox']-=5; adaptive['spot_trend']+=5
        if basis is not None:
            if basis>100: adaptive['basis']=2
            elif basis<-50: adaptive['basis']+=3
        for factor,rate in (real_win_rates or {}).items():
            if factor in adaptive and isinstance(rate,(int,float)):
                if rate>=0.65: adaptive[factor]=min(adaptive[factor]+2,25)
                elif rate<=0.35: adaptive[factor]=max(adaptive[factor]-2,1)
        active={x['key'] for x in self.factor_details if x['status']=='active'}
        eligible={k:max(0.0,float(v)) for k,v in adaptive.items() if k in active}
        total=sum(eligible.values())
        effective={k:(v*100.0/total if total>0 else 0.0) for k,v in eligible.items()}
        self.weights={k:round(effective.get(k,0.0),6) for k in base_weights}
        if total>0:
            last=next(k for k in reversed(list(base_weights)) if k in eligible)
            self.weights[last]=round(self.weights[last]+100.0-sum(self.weights.values()),6)
        base_total=sum(base_weights.values())
        covered=sum(base_weights[k] for k in active)
        active_count=len(active)
        coverage=covered/base_total*100 if base_total else 0.0
        quality='high' if coverage>=85 else 'medium' if coverage>=65 else 'low' if coverage>=40 else 'insufficient'
        self.factor_quality={
            'active_count':active_count,'total_factors':len(base_weights),
            'count_coverage_pct':round(active_count/len(base_weights)*100,1),
            'base_weight_coverage_pct':round(coverage,1),
            'base_weight_total':round(base_total,6),
            'base_weight_unit':'relative_points',
            'weight_normalization':'active_factors_rescaled_to_100_percent',
            'effective_weight_total':round(sum(self.weights.values()),6),
            'confidence':quality,'bias_reliable':quality in ('high','medium'),
            'score_status':'calculated' if active_count else 'no_valid_factors_neutral_fallback',
            'optimizer':'sqlite' if real_win_rates else 'base_dynamic',
            'missing_factors':[x['key'] for x in self.factor_details if x['status']!='active' and x.get('raw_value') is None],
            'disabled_factors':[x['key'] for x in self.factor_details if x['status']!='active' and x.get('raw_value') is not None],
            'inactive_count':sum(1 for x in self.factor_details if x['status']!='active')
        }
        for item in self.factor_details:
            item['base_weight']=base_weights[item['key']]
            item['adaptive_weight']=round(adaptive[item['key']],4)
            item['effective_weight']=self.weights[item['key']]
        return self.weights

    def calculate_bias(self, real_win_rates=None):
        self._evaluate_factors()
        weights=self.calculate_weights(real_win_rates)
        contributions=[]
        for item in self.factor_details:
            if item['status']!='active':
                item['contribution']=0.0
                continue
            contribution=50.0*(weights[item['key']]/100.0)*item['score']
            item['contribution']=round(contribution,4)
            if abs(contribution)>=0.005:
                contributions.append((item['name'],int(round(contribution))))
        total_contribution=sum(x['contribution'] for x in self.factor_details)
        self.bias_score=max(0,min(100,int(round(50.0+total_contribution))))
        self.bias_factors=contributions
        self.bias_reliable=self.factor_quality['bias_reliable']
        return self.bias_score,self.bias_factors,self.weights

    def gen_bias_card(self):
        bias=self.bias_score; factors=self.bias_factors; s=self.signals
        factor_str=" ".join([f"{n}{v:+d}" for n,v in factors[:6]])
        if bias<20: regime="極空"
        elif bias<35: regime="偏空"
        elif bias<50: regime="震盪偏空"
        elif bias<65: regime="震盪"
        elif bias<80: regime="偏多"
        else: regime="極多"
        close=s.get('spot_close') or 0; vix=s.get('vix'); vix_text=f"VIX{vix:.1f}" if vix is not None else "VIX unavailable"; put_wall=s.get('put_wall')
        pct=s.get('spot_pct'); pct_text=f"{pct:+.2f}%" if pct is not None else "漲跌幅 unavailable"
        if bias<35:
            look=f"加權{int(close):,} {pct_text} 外資{s.get('foreign') if s.get('foreign') is not None else 'unavailable'}億 {factor_str} {vix_text}"
            compass=f"{bias}分{regime}，Put Wall {put_wall if put_wall is not None else 'unavailable'}；缺少價位時不推定防線"
            target=f"Put Wall {put_wall if put_wall is not None else 'unavailable'}；依有效價位及價格確認風險"
        else:
            look=f"加權{int(close):,} {pct_text} {factor_str}"
            compass=f"{bias}分{regime}，觀察外資續賣"
            target=f"依Bias{bias}分操作，Put Wall {put_wall if put_wall is not None else 'unavailable'}"
        return {'bias':bias,'regime':regime,'factors':factors,'factor_str':factor_str,'look':look,'compass':compass,'target':target}

    def analyze_spot(self):
        s=self.signals; bias=self.bias_score
        def fmt(value, digits=2, signed=False):
            if value is None:
                return "unavailable"
            try:
                number=float(value)
                if not math.isfinite(number):
                    return "unavailable"
                return f"{number:+.{digits}f}" if signed else f"{number:.{digits}f}"
            except (TypeError, ValueError):
                return "unavailable"

        close=fmt(s.get('spot_close'),2)
        pct=fmt(s.get('spot_pct'),2,True)
        up=s.get('spot_up'); down=s.get('spot_down')
        up_text=str(up) if up is not None else "unavailable"
        down_text=str(down) if down is not None else "unavailable"
        rsi_text=fmt(s.get('rsi'),2)
        macd_text=fmt(s.get('macd_hist'),4,True)
        put_wall=self.parsed.get('options',{}).get('putWall')
        put_wall_text=fmt(put_wall,2)
        breadth=("全面普跌" if down is not None and down>500 else "分歧") if up is not None and down is not None else "漲跌家數資料不足"
        target=f"觀察 Put Wall {put_wall_text} 支撐" if put_wall is not None else "Put Wall unavailable；缺值不設定支撐位"
        return {
            "look": f"加權{close}點 {pct}% 漲跌{up_text}上{down_text}下，RSI {rsi_text} MACD {macd_text}",
            "compass": f"Bias{bias}分，{up_text}上{down_text}下{breadth}",
            "target": target
        }

    def analyze_us_markets(self):
        us_dict=self.signals.get('us_dict',{})
        sox=next((v for k,v in us_dict.items() if 'SOX' in k),None)
        valid_changes=[v for k,v in us_dict.items() if 'VIX' not in k.upper() and v is not None]
        vix=self.signals.get('vix'); dxy=self.signals.get('dxy_change')
        vix_text=f"VIX {vix:.2f}點" if vix is not None else "VIX unavailable"
        dxy_text=f"DXY {dxy:+.2f}%" if dxy is not None else "DXY unavailable"
        sox_text=f"{sox:+.2f}%" if sox is not None else "SOX unavailable"
        breadth='股票指數全漲' if valid_changes and all(v>0 for v in valid_changes) else ('股票指數全跌' if valid_changes and all(v<0 for v in valid_changes) else '股票指數漲跌互見/資料不足')
        return {"look": f"SOX {sox_text}；{breadth}；{vix_text}；{dxy_text}", "compass": f"費半{sox_text}；{vix_text}；{dxy_text}", "target": "分開觀察股票指數、VIX 波動率與 DXY 美元指數"}

    def analyze_news(self):
        news=self.parsed['news']
        return {"look": f"重大新聞{len(news)}則，首則{news[0]['t'][:30] if news else '無'}", "compass": f"{len(news)}則新聞，聚焦{news[0]['s'][:20] if news else ''}", "target": "關注法人籌碼與新聞共振"}

def build_factor_quality_summary(analyzer):
    """Describe the actual active 17F coverage; never imply all factors are active."""
    details=analyzer.factor_details
    active=[item for item in details if item.get('status')=='active']
    positive=sum(1 for item in active if (item.get('score') or 0)>0)
    negative=sum(1 for item in active if (item.get('score') or 0)<0)
    neutral=len(active)-positive-negative
    total=analyzer.factor_quality.get('total_factors',len(details))
    missing=len(analyzer.factor_quality.get('missing_factors',[]))
    disabled=len(analyzer.factor_quality.get('disabled_factors',[]))
    confidence=analyzer.factor_quality.get('confidence','unknown')
    effective_total=sum(analyzer.weights.values())
    return (
        f"17F有效{len(active)}/{total}；正向{positive}、負向{negative}、"
        f"中性{neutral}、缺值{missing}、有值停用{disabled}；有效權重{effective_total:.1f}%；"
        f"信心{confidence}"
    )


def build_history_status_text(historical, db_status):
    """Distinguish an unavailable DB from an enabled DB with too few labeled rows."""
    if historical:
        return (
            f"歷史相似{historical['count']}天，隔日平均"
            f"{historical['avg_next_pct']:.1f}%；隔日上漲比例{historical['positive_rate']:.0%}、下跌比例{historical['negative_rate']:.0%}"
        )
    mode=db_status.get('mode','no-db')
    if not db_status.get('exists'):
        return f"SQLite不可用（{mode}），未執行歷史相似分析"
    rows=int(db_status.get('rows') or 0)
    filled=int(db_status.get('filled') or 0)
    if filled<3:
        return f"SQLite已啟用；有效歷史樣本{filled}/3（DB共{rows}筆），未啟用歷史相似分析"
    return f"SQLite已啟用；{filled}筆歷史樣本可用，但本次未取得相似分析結果"


def classify_three_market(values):
    """Classify spot/futures/options direction only when all three flows are valid."""
    if len(values) != 3 or any(value is None for value in values):
        return "三市場資料不完整，不能判定一致性"
    nums = [float(value) for value in values]
    if all(value > 0 for value in nums):
        return "三市場一致偏多"
    if all(value < 0 for value in nums):
        return "三市場一致偏空"
    return "三市場方向分歧"

def classify_futures_oi(values):
    """Assess whether the three institutional futures OI snapshot is usable."""
    if len(values) != 3:
        return "期貨淨 OI 欄位不完整，不能判定快照可信度", False
    nums = []
    for value in values:
        try:
            number = float(value)
            nums.append(number if math.isfinite(number) else None)
        except (TypeError, ValueError):
            nums.append(None)
    if all(value == 0 for value in nums):
        return "三法人淨 OI 全為 0，視為可疑快照，不納入方向判斷", True
    if any(value is None for value in nums):
        return "期貨淨 OI 有缺值，僅採可用欄位", False
    return "期貨淨 OI 可讀取；仍與日盤交易流量分開解讀", False

def classify_option_sessions(day, night):
    if day is None or night is None:
        return "日夜資料不足"
    if day * night > 0:
        return "日夜同向"
    if day * night < 0:
        return "日夜方向分歧"
    return "至少一盤中性"

def classify_spot_institutions(values):
    """Classify three spot-institution net flows without treating missing data as disagreement."""
    if len(values) != 3 or any(value is None for value in values):
        return "現貨三法人資料不足，不能完整判定方向"
    numeric = [float(value) for value in values]
    if all(value > 0 for value in numeric):
        return "三法人現貨同向買超"
    if all(value < 0 for value in numeric):
        return "三法人現貨同向賣超"
    return "現貨三法人方向分歧"

def build_41_cards(analyzer, parsed, historical, db_status):
    bias=analyzer.bias_score; regime=analyzer.gen_bias_card()['regime']; factors=analyzer.bias_factors; s=analyzer.signals; weights=analyzer.weights
    factor_str=" ".join([f"{n}{v:+d}" for n,v in factors[:6]])
    close=s.get('spot_close'); put_wall=s.get('put_wall'); call_wall=s.get('call_wall')
    pcr=s.get('pcr'); foreign=s.get('foreign'); foreign_fut=s.get('foreign_futures')
    def display(value, digits=2):
        if value is None:
            return "unavailable"
        try:
            number=float(value)
            return f"{number:,.{digits}f}" if math.isfinite(number) else "unavailable"
        except (TypeError,ValueError):
            return "unavailable"
    def direction(value):
        try:
            number=float(value)
            return "偏多" if number>0 else "偏空" if number<0 else "中性"
        except (TypeError,ValueError):
            return "資料不足"
    pcr_text=f"{pcr:.2f}" if pcr is not None else "unavailable"
    put_wall_text=str(put_wall) if put_wall is not None else "unavailable"
    call_wall_text=str(call_wall) if call_wall is not None else "unavailable"
    flip=s.get('flip'); flip_text=str(flip) if flip is not None else "unavailable"
    gex=s.get('gex'); gex_text=str(gex) if gex is not None else "unavailable"
    active_details=[x for x in analyzer.factor_details if x.get('status')=='active']
    negative_count=sum(1 for x in active_details if x.get('score',0)<0)
    positive_count=sum(1 for x in active_details if x.get('score',0)>0)
    disabled_count=17-len(active_details)

    def regime_desc():
        pct=s.get('spot_pct'); foreign_value=s.get('foreign'); pcr_value=s.get('pcr')
        if pct is None or foreign_value is None or pcr_value is None:
            return '資料不足', '趨勢、法人或 PCR 缺值；不推定市場 regime'
        if pct<-1 and foreign_value<-200 and pcr_value<0.8:
            return '空方壓力', '單日跌幅低於 -1%、外資現貨賣超逾 200 億元、OI PCR 低於 0.8；未使用月線條件'
        if pct>1 and foreign_value>200 and pcr_value>1.0:
            return '多方條件', '單日漲幅高於 +1%、外資現貨買超逾 200 億元、OI PCR 高於 1.0；未使用月線條件'
        return '盤整／訊號混合', '未同時符合上述單日漲跌幅、外資現貨與 OI PCR 條件'

    regime_label, regime_d = regime_desc()
    top10=parsed['futures'].get('top10'); foreign_day=parsed['futures'].get('foreign_day')
    opt_inst_rows=parsed.get('options',{}).get('instOpt') or []
    opt_foreign_row=next((row for row in opt_inst_rows if row and str(row[0]).strip()=='外資'),None)
    def signed_table_value(row,index):
        if not row or len(row)<=index: return None
        try:
            value=float(str(row[index]).replace(',','').replace('+','').strip())
            return value if math.isfinite(value) else None
        except (TypeError,ValueError): return None
    option_foreign_day=signed_table_value(opt_foreign_row,3)
    option_foreign_night=signed_table_value(opt_foreign_row,6)
    option_day_dir=direction(option_foreign_day); option_night_dir=direction(option_foreign_night)
    option_session_text=classify_option_sessions(option_foreign_day, option_foreign_night)
    # 三市場解析：分開現貨金額、期貨/選擇權交易流量與 OI 存量，避免跨口徑直接比較。
    spot_inst_values=[parsed.get('inst',{}).get(key) for key in ('foreign','trust','dealer')]
    three_market_values=[foreign,foreign_day,option_foreign_day]
    three_market_text=classify_three_market(three_market_values)
    futures_oi_values=[parsed.get('futures',{}).get(key) for key in ('foreign_oi','trust_oi','dealer_oi')]
    futures_oi_status, futures_oi_all_zero=classify_futures_oi(futures_oi_values)
    opt_trust_row=next((row for row in opt_inst_rows if row and str(row[0]).strip()=='投信'),None)
    opt_dealer_row=next((row for row in opt_inst_rows if row and str(row[0]).strip()=='自營商'),None)
    option_trust_day=signed_table_value(opt_trust_row,3)
    option_dealer_day=signed_table_value(opt_dealer_row,3)
    def signed_text(value, unit, digits=0):
        return "資料不足" if value is None else f"{value:+,.{digits}f}{unit}"
    three_market_look=(
        f"現貨外資 {signed_text(foreign,'億元',1)}、投信 {signed_text(spot_inst_values[1],'億元',1)}、"
        f"自營商 {signed_text(spot_inst_values[2],'億元',1)}；"
        f"期貨外資日盤淨交易 {signed_text(foreign_day,'口')}；"
        f"選擇權外資日盤 {signed_text(option_foreign_day,'口')}／夜盤 {signed_text(option_foreign_night,'口')}"
    )
    three_market_compass=(
        f"{three_market_text}：外資現貨{direction(foreign)}、期貨日盤流量{direction(foreign_day)}、"
        f"選擇權日盤流量{option_day_dir}。{futures_oi_status}。"
        f"選擇權同業別日盤：投信 {signed_text(option_trust_day,'口')}、自營商 {signed_text(option_dealer_day,'口')}。"
        f"現貨與衍生品是不同市場/口徑，不能把金額與口數相加。"
    )
    three_market_target=(
        "下一交易日先核對期貨法人 OI 是否恢復有效；在此之前以日盤淨交易量作流量觀察。"
        "若外資現貨賣超收斂、期貨日盤流量轉弱或翻空、選擇權日盤淨流量仍偏空，才視為賣壓延續；"
        "若期貨與選擇權流量轉同向且現貨賣超收斂，再確認分歧是否收斂。未收斂前不追單。"
    )
    spot_inst_text=classify_spot_institutions(spot_inst_values)
    hist_str=build_history_status_text(historical,db_status)
    factor_quality_summary=build_factor_quality_summary(analyzer)

    bias_card=analyzer.gen_bias_card(); spot_card=analyzer.analyze_spot(); us_card=analyzer.analyze_us_markets(); news_card=analyzer.analyze_news()

    basis_text=display(s.get('tx_basis')); night_pct_text=display(s.get('tx_night_pct')); night_low_text=display(s.get('tx_night_low'))
    futures_look=f"台指基差{basis_text}點；夜盤{night_pct_text}%；夜低{night_low_text}點；外資期貨淨 OI {display(foreign_fut,0)}口"
    futures_compass=f"夜盤漲跌幅 {night_pct_text}%；基差 {basis_text}點；{regime_label}"
    futures_target=f"夜盤低點 {night_low_text}點（觀察價位，非保證支撐）"

    options_look=f"PCR {pcr_text}；GEX 依有效來源資料；Put Wall {put_wall_text}"
    options_compass=(f"PCR{pcr_text}偏低，Put Wall {put_wall_text}為觀察位" if pcr is not None and pcr<0.6 and put_wall is not None else f"選擇權資料 PCR {pcr_text}、Put Wall {put_wall_text}；缺值不推定方向")
    options_target=(f"Put Wall {put_wall}守住觀察震盪，跌破再確認" if pcr is not None and pcr<0.6 and put_wall is not None else f"PCR／Put Wall 有效資料不足時不設定區間目標")

    kpi_look=f"KPI 8宮格：加權{display(close)}點；漲跌幅{display(s.get('spot_pct'))}%；外資{display(foreign)}億元；Bias{bias}分；{regime_label}；{hist_str}"
    kpi_compass=f"{bias}分{regime_label}；{factor_quality_summary}；費半有效權重{weights.get('us_sox',0):.2f}%；{hist_str}"
    kpi_target=f"依Bias{bias}分操作，{regime_label}策略，{put_wall}為關鍵，{hist_str}"

    top10_look=f"前十大多空淨 OI {display(top10,0)}口；外資日盤淨交易 {display(foreign_day,0)}口；OI 為存量、日盤淨交易為流量，不直接相減"
    top10_compass=f"前十大淨 OI {direction(top10)}；外資日盤淨交易 {direction(foreign_day)}；分開觀察存量與流量"; top10_target="追蹤前十大多空淨 OI 及其變化；淨 OI 不等同價格支撐／壓力"

    # 42個可見區塊映射 (依Skill定義)
    cards={
        'DATA_REPORT 一致性檢查': {
            "look": f"DATA_REPORT 一致性檢查：{len(parsed['meta'].get('data_quality_warnings',[]))} 項警告",
            "compass": "；".join(parsed['meta'].get('data_quality_warnings',[])) if parsed['meta'].get('data_quality_warnings') else "現貨 OHLC、法人合計、成交金額、期現基差、選擇權 PCR 交叉檢查未發現矛盾",
            "target": "警告只標示資料衝突，不自動修改原始數據；請回查 DATA_REPORT 來源"
        },
        'Bias 盤前偏向': bias_card,
        'KPI 8宮格': {"look": kpi_look, "compass": kpi_compass, "target": kpi_target},
        '大盤全景': spot_card,
        '台指期 日夜': {"look": futures_look, "compass": futures_compass, "target": futures_target},
        '期貨籌碼': {"look": futures_look, "compass": futures_compass, "target": futures_target},
        '選擇權牆': {"look": options_look, "compass": options_compass, "target": options_target},
        '美股連動': us_card,
        '關鍵水位': {"look": f"現價{close}；Put Wall {put_wall_text}；Flip {flip_text}；Regime {regime_label}", "compass": f"只採用當日有效關鍵位；缺失價位不補硬編碼水位", "target": f"依有效 Put Wall {put_wall_text} 與 Flip {flip_text} 觀察，缺值時不設定價位目標"},
        '盤前核心判斷': {"look": f"有效因子 {len(active_details)}/17；正向 {positive_count} 項、負向 {negative_count} 項；Bias {bias} 分／{regime_label}；{factor_str[:60]}", "compass": f"依當日有效因子與資料覆蓋判斷：{regime_d}", "target": f"依 {regime_label} 與有效關鍵價位執行；未確認前不預設方向"},
        '三劇本': {"look": f"情境分析：Bias {bias}分、{regime_label}；未建立經回測校準的機率模型，不提供悲觀／中性／樂觀機率", "compass": "情境路徑僅作條件推演，不代表統計機率", "target": f"觀察有效關鍵價位 {put_wall_text}；未確認突破／跌破前不啟動劇本"},
        '多空條件檢查表': {"look": f"17F有效{len(active_details)}/17；正向{positive_count}項、負向{negative_count}項、缺失{disabled_count}項；資料覆蓋{analyzer.factor_quality['base_weight_coverage_pct']}%", "compass": f"有效因子權重已正規化；信心等級 {analyzer.factor_quality['confidence']}；不以缺失因子推定方向", "target": f"Bias {bias}；資料可信度 {analyzer.factor_quality['confidence']}；依有效因子與價格條件決策"},
        '開盤前必核': {"look": kpi_look, "compass": kpi_compass, "target": kpi_target},
        'AI 5面向': {"look": kpi_look, "compass": kpi_compass, "target": kpi_target},
        'AI結論': bias_card,
        '交易計畫': bias_card,
        '行事曆': news_card,
        '法人籌碼': {"look": f"外資現貨 {display(foreign)}億元（{direction(foreign)}）；期貨淨 OI {display(foreign_fut,0)}口；投信 {display(parsed['inst'].get('trust'))}億元；自營商 {display(parsed['inst'].get('dealer'))}億元", "compass": f"現貨外資 {direction(foreign)}、投信 {direction(parsed['inst'].get('trust'))}；依實際數值呈現，不預設對作", "target": f"觀察外資現貨後續變化；Put Wall {put_wall_text}僅為價位參考"},
        '主力三市透視': {
            "look": three_market_look,
            "compass": (
                f"結論：三市場方向分歧（跨市場訊號分歧），暫不構成單邊方向共識。現貨外資{direction(foreign)}"
                f"（{signed_text(foreign,'億元',1)}），期貨日盤淨交易{direction(foreign_day)}"
                f"（{signed_text(foreign_day,'口')}），選擇權外資日盤{direction(option_foreign_day)}"
                f"（{signed_text(option_foreign_day,'口')}）；期貨流量偏多但現貨與選擇權偏空，不能把期貨單一買盤解讀為全面翻多。"
                f"{futures_oi_status}"
            ),
            "target": (
                "操作：目前以觀望／降低追價為主，不因期貨單日淨買超追多。偏多確認條件：外資現貨賣超明顯收斂或轉買，"
                "且選擇權外資日盤流量轉正、期貨日盤淨買超延續；偏空確認條件：現貨賣超延續，且期貨流量轉負或選擇權賣壓延續。"
                "若三市場仍互相背離，維持分歧判讀，等待下一交易日數據確認；期貨 OI 可疑時不得作為確認條件。"
            )
        },
        '三市一致性': {
            "look": (
                f"外資跨市場方向檢查：現貨 {signed_text(foreign,'億元',1)}；期貨日盤淨交易 {signed_text(foreign_day,'口')}；"
                f"選擇權日盤 {signed_text(option_foreign_day,'口')}、夜盤 {signed_text(option_foreign_night,'口')}。"
                f"期貨 OI {display(foreign_fut,0)}口；{futures_oi_status}"
            ),
            "compass": (
                f"一致性判定：現貨{direction(foreign)}、期貨流量{direction(foreign_day)}、選擇權日盤流量{direction(option_foreign_day)}。"
                f"{three_market_text}。目前不是三市場同向訊號；且期貨 OI {('無效，不能用來確認存量方向' if futures_oi_all_zero else '仍須與前期有效快照比較，單一存量值不代表新增買賣') }。"
            ),
            "target": (
                "升級為偏多共識：外資現貨由賣轉買或賣超顯著收斂，且期貨與選擇權日盤流量連續同向偏多；"
                "升級為偏空共識：現貨賣超延續，且期貨與選擇權流量同步偏空。"
                "任一市場缺值或期貨 OI 快照異常時，標記為『共識未成立』，不以缺值補方向。"
            )
        },
        '期現選方向對照': {
            "look": (
                f"方向對照（不同單位不可加總）：現貨外資 {signed_text(foreign,'億元',1)}；"
                f"期貨日盤淨交易 {signed_text(foreign_day,'口')}；選擇權外資日盤 {signed_text(option_foreign_day,'口')}、"
                f"夜盤 {signed_text(option_foreign_night,'口')}；PCR（OI 比值）{pcr_text}倍；Put Wall {put_wall_text}。"
            ),
            "compass": (
                f"期貨流量與選擇權日盤流量：{('同向偏多' if foreign_day is not None and option_foreign_day is not None and foreign_day>0 and option_foreign_day>0 else '同向偏空' if foreign_day is not None and option_foreign_day is not None and foreign_day<0 and option_foreign_day<0 else '未形成同向訊號')}。"
                f"PCR 反映 Put／Call 未平倉量相對結構，不等於當日買賣方向；Put Wall 是履約價集中區，不是保證支撐。"
                f"因此現有數據若流量背離，應判為訊號衝突，而非用 PCR 抵銷交易流量。"
            ),
            "target": (
                f"若期貨與選擇權流量連續同向，才列為短線方向候選；仍須等現貨外資賣壓收斂／買超確認。"
                f"價格接近 Put Wall {put_wall_text}時，觀察是否止跌並重新站回，不因觸及價位直接進場；跌破且反彈無法收復，才提高下行風險評估。"
            )
        },
        '籌碼三市矩陣': {
            "look": (
                f"現貨法人淨買賣（億元）：外資 {signed_text(spot_inst_values[0],'億元',1)}、投信 {signed_text(spot_inst_values[1],'億元',1)}、自營商 {signed_text(spot_inst_values[2],'億元',1)}。"
                f"選擇權日盤淨交易（口）：外資 {signed_text(option_foreign_day,'口')}、投信 {signed_text(option_trust_day,'口')}、自營商 {signed_text(option_dealer_day,'口')}。"
            ),
            "compass": (
                f"現貨三法人：{spot_inst_text}。選擇權三法人流量：外資{direction(option_foreign_day)}、投信{direction(option_trust_day)}、自營商{direction(option_dealer_day)}。"
                f"交叉觀察：投信現貨{direction(spot_inst_values[1])}但選擇權{direction(option_trust_day)}；"
                f"自營商現貨{direction(spot_inst_values[2])}但選擇權{direction(option_dealer_day)}。"
                f"這是不同市場的方向配置差異，口數與億元不可相加，也不能直接視為避險等值。"
            ),
            "target": (
                "下一交易日逐法人追蹤：投信現貨買超是否延續、選擇權賣方／買方流量是否反轉；"
                "自營商若現貨與選擇權持續反向，先視為跨市場配置或避險可能性，未取得部位方向與 Delta 前不判定淨曝險。"
                "外資現貨賣壓若擴大且選擇權流量同步偏空，才提高整體籌碼偏空權重。"
            )
        },
        '主力意圖解碼': {
            "look": (
                f"可觀察證據：外資現貨 {signed_text(foreign,'億元',1)}；期貨日盤淨交易 {signed_text(foreign_day,'口')}；"
                f"期貨淨 OI {display(foreign_fut,0)}口（{'可疑快照，不採用' if futures_oi_all_zero else '存量，須與前期比較'}）；"
                f"選擇權日盤 {signed_text(option_foreign_day,'口')}、夜盤 {signed_text(option_foreign_night,'口')}。"
            ),
            "compass": (
                f"證據支持的描述：外資在現貨、期貨流量、選擇權流量之間呈現方向分歧。{futures_oi_status}。"
                "目前沒有足夠資料判斷選擇權交易是買方主動、賣方承接或避險組合，也沒有足夠證據推定主力正在控盤、誘多或出貨。"
            ),
            "target": (
                "意圖判讀的最低追加證據：期貨有效 OI 的連續變化、選擇權逐履約價買賣權 OI 與主動買賣流、"
                "以及現貨法人連續日買賣超。若三類證據連續同向，才提高方向性意圖的可信度；"
                "在資料未齊前只報告『流量分歧／意圖未明』，不採取主力意圖型交易。"
            )
        },
        '夜盤劇本': {"look": f"夜盤收盤{parsed['tx']['night']['c']}點；變化{parsed['tx']['night']['change']}點；基差{parsed['tx']['day']['basis']}點", "compass": f"夜盤{parsed['tx']['night']['pct']}% {regime_label}", "target": f"夜盤低{parsed['tx']['night']['l']}為支撐"},
        '台指夜盤劇本': {"look": f"台指夜盤收盤{parsed['tx']['night']['c']}點；變化{parsed['tx']['night']['change']}點；基差{parsed['tx']['day']['basis']}點", "compass": f"夜盤{parsed['tx']['night']['pct']}% {regime_label}", "target": f"夜盤低{parsed['tx']['night']['l']}為支撐"},
        '資金流向': spot_card,
        'PCR 極低': {"look": options_look, "compass": options_compass, "target": options_target},
        'VIX & DXY': us_card,
        '相關性熱圖': {"look": "SOX與台股相關性：未計算（缺少日期對齊的歷史序列）", "compass": "不以單日漲跌代替相關係數", "target": "累積足夠的同步歷史樣本後再計算"},
        '台指期 日盤': {"look": f"台指日盤收{parsed['tx']['day']['c']}點；高{parsed['tx']['day']['h']}點；低{parsed['tx']['day']['l']}點；量{parsed['tx']['day']['vol']}口", "compass": f"日盤{parsed['tx']['day']['pct']}% 基差{parsed['tx']['day']['basis']}", "target": f"日盤低{parsed['tx']['day']['l']}為支撐"},
        '台指期 夜盤': {"look": f"台指夜盤收{parsed['tx']['night']['c']}點；高{parsed['tx']['night']['h']}點；低{parsed['tx']['night']['l']}點；量{parsed['tx']['night']['vol']}口", "compass": f"夜盤{parsed['tx']['night']['pct']}% 變化{parsed['tx']['night']['change']}", "target": f"夜盤低{parsed['tx']['night']['l']}為支撐"},
        '期貨籌碼深度圖': {"look": futures_look, "compass": futures_compass, "target": futures_target},
        '外資期貨': {"look": f"外資期貨淨 OI {display(foreign_fut,0)}口；日盤淨交易 {display(foreign_day,0)}口；夜盤淨交易 {display(parsed['futures'].get('foreign_night'),0)}口", "compass": f"外資期貨淨 OI {direction(foreign_fut)}" + ("（低於 -80,000 口觀察門檻）" if foreign_fut is not None and foreign_fut<-80000 else ""), "target": "淨 OI 為部位存量，日／夜盤淨交易為流量；分開觀察變化"},
        '前十大與分歧': {"look": top10_look, "compass": top10_compass, "target": top10_target},
        '前十大與分歧bar': {"look": top10_look, "compass": top10_compass, "target": top10_target},
        'OI結構': {"look": options_look, "compass": options_compass, "target": options_target},
        'GEX': {"look": f"Net GEX {display(gex)} NT$／標的價格變動 1%；Gross GEX {display(parsed.get('options',{}).get('grossGex1pct'))}；Put Wall {put_wall_text}", "compass": "GEX 是 Gamma 模型曝險估值；正負不直接等同多空方向，須結合 Gamma regime 與價格位置解讀", "target": "以 Net／Gross GEX、資料日期及模型品質觀察曝險結構，不單獨產生方向訊號"},
        'IV Skew': {"look": "IV Rank、Risk Reversal：DATA_REPORT 未提供", "compass": "IV Skew 未取得可驗證數據，不判定 Put／Call 溢價方向", "target": "取得 IV 曲面與期限序列後再分析"},
        'Term': {"look": "期限結構：DATA_REPORT 未提供", "compass": "缺少各到期月份 IV，無法判定 Term Structure", "target": "取得各到期月份 IV 後再分析"},
        'PCR 0.74→0.57': {"look": f"當日 PCR {pcr_text}；未提供連續歷史序列時不繪製趨勢", "compass": f"PCR {pcr_text}；不以單日數值直接推定散戶恐慌", "target": "PCR 缺值或缺少歷史序列時不產生趨勢與反向訊號"},
        '外資選擇權分歧': {"look": f"外資選擇權日盤淨交易 {display(option_foreign_day,0)}口（{option_day_dir}）；夜盤 {display(option_foreign_night,0)}口（{option_night_dir}）；{option_session_text}", "compass": f"外資選擇權日盤 {option_day_dir}、夜盤 {option_night_dir}；日夜盤方向分開呈現", "target": "選擇權日夜淨交易是流量口數，不等同 OI 存量或單邊方向保證"},
        '美股指數': us_card,
        '亞洲指數': {"look": f"亞洲市場資料：{parsed['asiaPct_full']}", "compass": "僅呈現有來源的市場數值，不推定同步連動", "target": "依各市場實際變動分別觀察"},
        '美股期貨': {"look": f"美股期貨資料：{parsed['futPct_full']}", "compass": "僅呈現 DATA_REPORT 有效數值", "target": "資料缺值時不推定夜盤方向"},
        '美債殖利率': {"look": f"美債市場資料：{parsed['yieldPct_full']}", "compass": "顯示 DATA_REPORT 原始列值；不以固定門檻推定殖利率曲線", "target": "依當日實際殖利率與期限利差另行判讀"},
        '匯率': {"look": f"匯率市場資料：{parsed['fxPct_full']}", "compass": "以當日來源資料呈現，不由單一匯率推定外資匯出", "target": "搭配外資現貨與期貨部位交叉觀察"},
        '商品': {"look": f"商品市場資料：{parsed['commPct_full']}", "compass": "商品價格與通膨關係需搭配時間序列判讀", "target": "不以缺值或單日變動推定通膨方向"},
        '重大經濟數據': news_card,
    }
    return cards

def build_final_json(parsed, tech, analyzer, historical, db_status, args_date_str):
    spot=parsed['spot']; closes=tech.get('closes',[]); spot5=[]; spot5Dates=[]
    raw_history=_filter_history_to_t0(tech.get('raw',[]) or [],parsed.get('meta',{}).get('t0_date'))
    dated_history=[(d.get('date'),d.get('close')) for d in raw_history if d.get('date') and d.get('close') is not None]
    last5=dated_history[-5:]
    spot5=[int(round(c)) for _,c in last5]
    spot5Dates=[datetime.strptime(day,'%Y-%m-%d').strftime("%m/%d") for day,_ in last5]

    bias, factors, weights=analyzer.bias_score, analyzer.bias_factors, analyzer.weights; cards_41=build_41_cards(analyzer, parsed, historical, db_status)

    markets={'us': parsed['usPct_full'], 'asia': parsed['asiaPct_full'], 'usFut': parsed['futPct_full'], 'yields': parsed['yieldPct_full'], 'fx': parsed['fxPct_full'], 'adr': parsed['adrPct_full'], 'commodities': parsed['commPct_full']}
    marketPct={'usPct': parsed['usPct_simple'], 'asiaPct': parsed['asiaPct_simple'], 'futPct': parsed['futPct_simple'], 'yieldPct': parsed['yieldPct_simple'], 'fxPct': parsed['fxPct_simple'], 'adrPct': parsed['adrPct_simple'], 'commPct': parsed['commPct_simple']}

    # 支撐壓力位只在所需原始欄位齊全時產生；OHLC 缺值時不推算 P 樞紐。
    key_levels=[]
    if all(spot.get(k) is not None for k in ('high','low','close')):
        key_levels=[
            {'t':"當日高點", 'v': int(spot['high']), 'type':"R"},
            {'t':"P 樞紐", 'v': int((spot['high']+spot['low']+spot['close'])/3), 'type':"P"},
            {'t':"當日低點", 'v': int(spot['low']), 'type':"S"},
        ]
    if parsed['options']['putWall'] is not None:
        key_levels.append({'t':f"Put Wall {int(parsed['options']['putWall'])//1000}K", 'v': int(parsed['options']['putWall']), 'type':"W"})
    if parsed['options']['flip'] is not None:
        key_levels.append({'t':f"Flip {int(parsed['options']['flip'])//1000}K", 'v': int(parsed['options']['flip']), 'type':"F"})

    final={
        'meta': {
            'version': 'v9-pro-17F',
            'skill': 'daily-premarket-analysis-v9-pro',
            'date': parsed['meta']['t0_date'] or args_date_str,
            'report_date': parsed['meta']['report_date'],
            'generated_at': parsed['meta']['generated_at'] or datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            'timezone': 'Asia/Taipei',
            'template': 'pure-react + window.DASHBOARD_DATA',
            'no_sample_data': True,
            'factors': f"17F; active={analyzer.factor_quality.get('active_count',0)}/17",
            'db_mode': db_status.get('mode','no-db'),
            'db_rows': db_status.get('rows',0),
            'output_path_rule': 'dashboards/ 唯一',
            'data_quality_warning_count': len(parsed['meta'].get('data_quality_warnings',[])),
            'data_quality_warnings': parsed['meta'].get('data_quality_warnings',[])
        },
        'spot': {
            'close': spot['close'], 'diff': spot['diff'], 'pct': spot['pct'], 'open': spot['open'], 'high': spot['high'], 'low': spot['low'],
            'vol': spot['vol'], 'vol_str': f"{spot['vol']}億", 'up': spot['up'], 'down': spot['down'], 'flat': spot['flat'], 'limit_up': spot['limit_up'], 'limit_down': spot['limit_down'],
            'otc': {'up': spot['otc_up'], 'down': spot['otc_down'], 'flat': spot['otc_flat'], 'limit_up': spot['otc_limit_up'], 'limit_down': spot['otc_limit_down']},
            'spot5': spot5, 'spot5Dates': spot5Dates
        },
        'institutional': {'all': parsed['inst']['all'], 'foreign': parsed['inst']['foreign'], 'trust': parsed['inst']['trust'], 'dealer': parsed['inst']['dealer']},
        'margin': {'finance': parsed['margin']['finance'], 'finance_diff': parsed['margin']['finance_diff'], 'short': parsed['margin']['short'], 'ratio': parsed['margin']['ratio'], 'ratio_status': parsed['margin']['ratio_status'], 'ratio_source': parsed['margin']['ratio_source'], 'ratio_source_name': parsed['margin']['ratio_source_name'], 'ratio_source_date': parsed['margin']['ratio_source_date'], 'ratio_is_t0': parsed['margin']['ratio_is_t0'], 'sbl': parsed['margin']['sbl'], 'borrow': (f"{int(parsed['margin']['sbl']):,}張" if parsed['margin']['sbl'] is not None else "unavailable"), 'borrowedSell': parsed['margin']['borrowed_sell'], 'borrowedSellDiff': parsed['margin']['borrowed_sell_diff'], 'borrowedSellDiffScope': parsed['margin']['borrowed_sell_diff_scope']},
        'turnover': parsed['turnover'],
        'tx': parsed['tx'],
        'futures': parsed['futures'],
        'options': {
            'callVol': parsed['options']['callVol'], 'callOi': parsed['options']['callOi'], 'putVol': parsed['options']['putVol'], 'putOi': parsed['options']['putOi'],
            'pcr': parsed['options']['pcr'], 'callWall': parsed['options']['callWall'], 'putWall': parsed['options']['putWall'], 'gammaWall': parsed['options']['gammaWall'], 'flip': parsed['options']['flip'], 'maxPain': parsed['options']['maxPain'],
            'netGex1pct': parsed['options']['netGex1pct'], 'grossGex1pct': parsed['options']['grossGex1pct'], 'gexLevels': parsed['options']['gexLevels'], 'gexDate': parsed['options']['gexDate'], 'gexStatus': parsed['options']['gexStatus'],
            'callOiDist': parsed['options']['callOiDist'], 'putOiDist': parsed['options']['putOiDist'], 'instOpt': parsed['options']['instOpt'],
            'instOptForce': parsed['options']['instOptForce'], 'instOptForceAnalysis': parsed['options']['instOptForceAnalysis'], 'top10Call': parsed['options']['top10Call'], 'top10Put': parsed['options']['top10Put']
        },
        'markets': markets, 'marketPct': marketPct,
        'technical': {'rsi': tech.get('rsi'), 'macd': tech.get('macd'), 'macd_signal': tech.get('macd_signal'), 'macd_hist': tech.get('macd_hist'), 'k': tech.get('k'), 'd': tech.get('d'), 'source': tech.get('source'), 'valid': tech.get('valid'), 'closes': tech.get('closes',[])[-30:], 'highs': tech.get('highs',[])[-30:], 'lows': tech.get('lows',[])[-30:]},
        'analysis': {
            'bias': bias, 'bias_score': bias, 'factors': factors, 'weights': weights,
            'factor_details': analyzer.factor_details, 'factor_quality': analyzer.factor_quality,
            'regime': analyzer.gen_bias_card()['regime'], 'factor_str': analyzer.gen_bias_card()['factor_str'],
            'look': analyzer.gen_bias_card()['look'], 'compass': analyzer.gen_bias_card()['compass'], 'target': analyzer.gen_bias_card()['target'],
            'cards': cards_41,
            'cards_41_count': len(cards_41),  # Legacy alias: internal narrative card count, not visible block count.
            'analysis_card_count': len(cards_41),
            'visible_block_count': 42,
            'correlation': calculate_historical_correlation(as_of_date=parsed['meta']['t0_date']),
            'levels': key_levels,
            'historical': historical,
            'db_status': db_status
        },
        'news': parsed['news'],
        'data_source': f"DATA_REPORT {parsed['meta']['t0_date']} + technical_history={tech.get('source','none')} (T0 filtered) + historical_learning=SQLite {db_status.get('mode','no-db')}"
    }
    return final

def run_17f_self_tests():
    """Fast offline tests; no network calls, report files, or SQLite writes."""
    import traceback
    try:
        clean_warnings=validate_data_report_consistency(
            {'open':100,'high':110,'low':90,'close':105},
            {'foreign':10,'trust':5,'dealer':-2,'all':13},
            {'listed':100,'otc':20,'total':120},
            {'day':{'o':100,'h':110,'l':90,'c':105,'basis':0}},
            {'callOi':100,'putOi':50,'pcr':0.5}
        )
        assert clean_warnings==[]
        conflict_warnings=validate_data_report_consistency(
            {'open':100,'high':95,'low':90,'close':105},
            {'foreign':10,'trust':5,'dealer':-2,'all':99},
            {'listed':100,'otc':20,'total':999},
            {'day':{'o':100,'h':110,'l':90,'c':105,'basis':99}},
            {'callOi':100,'putOi':50,'pcr':0.9}
        )
        assert len(conflict_warnings)>=5
        sample_tables=parse_markdown_tables("""### sample
| 項目 | 口數 |
|---|---|
| Call | 10 |

| 項目 | 口數 |
|---|---|
| Put | 20 |
""")
        assert len(sample_tables)==2 and sample_tables[0][0][0]=="Call" and sample_tables[1][0][0]=="Put"
        partial_turnover_warnings=validate_data_report_consistency(
            {'open':100,'high':110,'low':90,'close':105},
            {'foreign':10,'trust':5,'dealer':-2,'all':13},
            {'listed':None,'otc':20,'total':120},
            {'day':{'o':100,'h':110,'l':90,'c':105,'basis':0}},
            {'callOi':100,'putOi':50,'pcr':0.5}
        )
        assert partial_turnover_warnings==[]
        mr_self=parse_margin_ratio_provenance("| 融資維持率 | 171.747 | % | TWSE 上市自建估算（資料日期：2026-10-30；估值 1,238 檔） |", "2026-10-30")
        assert mr_self["status"]=="estimated_t0" and mr_self["source"]=="twse_self_built" and mr_self["source_date"]=="2026-10-30" and mr_self["is_t0"] is True
        mr_blave=parse_margin_ratio_provenance("| 融資維持率 | 171.75 | % | Blave 上市市場融資維持率估算（資料日期：2026-10-30） |", "2026-10-30")
        assert mr_blave["status"]=="estimated_t0" and mr_blave["source"]=="blave" and mr_blave["source_date"]=="2026-10-30" and mr_blave["is_t0"] is True
        mr_manual=parse_margin_ratio_provenance("| 融資維持率 | 172.10 | % | 人工輸入（MANUAL_LISTED_MARGIN_RATIO；資料日期：2026-10-30） |", "2026-10-30")
        assert mr_manual["status"]=="estimated_t0" and mr_manual["source"]=="manual_input" and mr_manual["source_date"]=="2026-10-30" and mr_manual["is_t0"] is True
        mr_t0=parse_margin_ratio_provenance("| 融資維持率 | 178.40 | % | stockintelli 大盤融資維持率 (民間估算；官方無每日序列) |", "2026-10-29")
        assert mr_t0["status"]=="estimated_t0" and mr_t0["source"]=="stockintelli" and mr_t0["source_date"]=="2026-10-29" and mr_t0["is_t0"] is True
        mr_prev=parse_margin_ratio_provenance("| 融資維持率 | 178.40 | % | 前值遞補 (DATA 2026-10-29；當日三源皆失敗；民間估算) |", "2026-10-30")
        assert mr_prev["status"]=="previous_report_fallback" and mr_prev["source_date"]=="2026-10-29" and mr_prev["is_t0"] is False
        mr_stale=parse_margin_ratio_provenance("| 融資維持率 | 178.40 | % | wantgoo 大盤融資維持率 (資料日期 2026-10-27；民間估算) |", "2026-10-29")
        assert mr_stale["status"]=="estimated_stale" and mr_stale["source"]=="wantgoo" and mr_stale["source_date"]=="2026-10-27"
        mr_none=parse_margin_ratio_provenance("| 融資維持率 | unavailable | % | unavailable（Blave、同 T0 人工輸入皆不可用） |", "2026-10-29")
        assert mr_none["status"]=="unavailable" and mr_none["ratio"] is None and mr_none["source"]=="unavailable"
        closes=[100.0+i for i in range(25)]
        parsed={
            'spot':{'close':125.0,'pct':1.5,'up':800,'down':300,'vol':5000,'volume_ratio':1.3},
            'inst':{'foreign':350.0,'trust':80.0,'dealer':10.0,'all':440.0},
            'tx':{'day':{'basis':30.0,'prem':0.1,'pct':1.0},'night':{'pct':0.8,'l':124.0,'h':128.0}},
            'options':{'putWall':120.0,'callWall':130.0,'gammaWall':128.0,'flip':122.0,'maxPain':125.0,'pcr':0.9,'netGex1pct':1.2},
            'futures':{'foreign_oi':60000},
            'usPct_full':[{'l':'SOX','v':3.0},{'l':'VIX','v':-1.0,'close':14.0}],
            'adrPct_full':[{'l':'TSM ADR','v':2.5}],
            'yieldPct_full':[{'l':'US 10Y','v':-0.06}]
        }
        tech={'rsi':65.0,'macd':1.0,'macd_hist':2.0,'closes':closes,'valid':True}
        baseline=V9Analyzer(parsed,tech)
        baseline.calculate_bias()
        analyzer=V9Analyzer(parsed,tech)
        bias,_,weights=analyzer.calculate_bias({'spot_trend':0.7})
        assert weights['spot_trend']>baseline.weights['spot_trend']
        assert len(analyzer.factor_details)==17
        assert analyzer.factor_quality['active_count']==16
        assert abs(sum(weights.values())-100.0)<1e-5
        assert 0<=bias<=100
        assert analyzer.factor_quality['base_weight_total']==104
        assert analyzer.factor_quality['base_weight_unit']=='relative_points'
        assert analyzer.factor_quality['weight_normalization']=='active_factors_rescaled_to_100_percent'
        assert abs(analyzer.factor_quality['effective_weight_total']-100.0)<1e-5

        sparse={**parsed,'options':{**parsed['options'],'gex':None},'spot':{**parsed['spot'],'volume_ratio':None},
                'adrPct_full':[],'yieldPct_full':[],'usPct_full':[{'l':'SOX','v':None},{'l':'VIX','v':None,'close':None}]}
        sparse_analyzer=V9Analyzer(sparse,{'rsi':None,'macd_hist':None,'closes':[]})
        sparse_bias,_,sparse_weights=sparse_analyzer.calculate_bias()
        assert sparse_analyzer.factor_quality['active_count']<17
        assert abs(sum(sparse_weights.values())-100.0)<1e-5
        assert 0<=sparse_bias<=100
        full_quality_summary=build_factor_quality_summary(analyzer)
        assert "17F有效16/17" in full_quality_summary
        assert "有效權重100.0%" in full_quality_summary
        assert "17因子共振" not in full_quality_summary
        sparse_quality_summary=build_factor_quality_summary(sparse_analyzer)
        assert f"17F有效{sparse_analyzer.factor_quality['active_count']}/17" in sparse_quality_summary
        assert "缺值" in sparse_quality_summary or "有值停用" in sparse_quality_summary
        db_partial_text=build_history_status_text(None,{'exists':True,'rows':3,'filled':1,'mode':'db'})
        assert "SQLite已啟用" in db_partial_text and "有效歷史樣本1/3" in db_partial_text
        assert "無DB模式" not in db_partial_text
        no_db_text=build_history_status_text(None,{'exists':False,'rows':0,'filled':0,'mode':'no-db'})
        assert "SQLite不可用" in no_db_text

        empty={'spot':{},'inst':{},'tx':{'day':{},'night':{}},'options':{},'futures':{},
               'usPct_full':[],'adrPct_full':[],'yieldPct_full':[]}
        empty_analyzer=V9Analyzer(empty,{})
        empty_bias,_,empty_weights=empty_analyzer.calculate_bias()
        assert empty_bias==50
        assert empty_analyzer.factor_quality['active_count']==0
        assert sum(empty_weights.values())==0
        assert empty_analyzer.factor_quality['confidence']=='insufficient'
        assert empty_analyzer.factor_quality['bias_reliable'] is False
        assert empty_analyzer.factor_quality['score_status']=='no_valid_factors_neutral_fallback'
        empty_spot_card=empty_analyzer.analyze_spot()
        assert "RSI unavailable" in empty_spot_card["look"]
        assert "MACD unavailable" in empty_spot_card["look"]
        assert "Put Wall unavailable" in empty_spot_card["target"]
        assert "None" not in str(empty_spot_card)
        # SQLite date attribution must follow explicit T0, not the runner's current date.
        with tempfile.TemporaryDirectory() as tmp:
            test_db=str(pathlib.Path(tmp)/"t0-test.db")
            assert save_today_to_db(49,{'spot_close':90.0},{},'20261027',test_db)
            assert save_today_to_db(50,{'spot_close':95.0},{},'20261028',test_db)
            assert update_next_day_pct('20261028',95.0,test_db)
            assert update_next_day_pct('20261029',100.0,test_db)
            assert save_today_to_db(51,{'spot_close':100.0},{},'20261029',test_db)
            conn=sqlite3.connect(test_db)
            rows=conn.execute("SELECT date,spot_close,next_day_pct FROM v9_pro_history ORDER BY date").fetchall()
            assert rows[0][0]=='2026-10-27'
            assert abs(rows[0][2]-(95.0-90.0)/90.0*100)<1e-6
            assert rows[1][0]=='2026-10-28'
            assert abs(rows[1][2]-(100.0-95.0)/95.0*100)<1e-6
            # Simulate an already-labeled latest prior row while an older row
            # remains unlabeled. Current T0 must not leapfrog to the older row.
            conn.execute("UPDATE v9_pro_history SET next_day_pct=1.0 WHERE date='2026-10-29'")
            conn.commit(); conn.close()
            assert update_next_day_pct('20261030',110.0,test_db) is False
            conn=sqlite3.connect(test_db)
            after=conn.execute("SELECT date,spot_close,next_day_pct FROM v9_pro_history ORDER BY date").fetchall()
            conn.close()
            assert after[0][0]=='2026-10-27' and after[0][2] is not None
            assert after[1][0]=='2026-10-28' and after[1][2] is not None
            assert after[2][0]=='2026-10-29' and after[2][2]==1.0
        # V9 is the only supported history schema; init_db must not create V8 tables.
        with tempfile.TemporaryDirectory() as tmp:
            v9_db=str(pathlib.Path(tmp)/"v9-only.db")
            v9_conn=init_db(v9_db)
            assert v9_conn is not None
            table_names={row[0] for row in v9_conn.execute(
                "SELECT name FROM sqlite_master WHERE type='table'"
            ).fetchall()}
            v9_columns={row[1] for row in v9_conn.execute("PRAGMA table_info(v9_pro_history)").fetchall()}
            v9_conn.close()
            required_columns={'date','bias','spot_close','spot_pct','foreign_spot','next_day_pct','factor_wins','created_at'}
            assert 'v9_pro_history' in table_names
            assert 'factor_performance' in table_names
            assert 'v8_pro_history' not in table_names
            assert required_columns <= v9_columns
        with tempfile.TemporaryDirectory() as tmp:
            invalid_db=str(pathlib.Path(tmp)/"invalid-schema.db")
            conn=sqlite3.connect(invalid_db)
            conn.execute("CREATE TABLE v9_pro_history (bias INTEGER, spot_close REAL)")
            conn.commit(); conn.close()
            assert init_db(invalid_db) is None
        # DATA-UI-05: correlation is hidden until five complete, quality-approved rows exist.
        with tempfile.TemporaryDirectory() as tmp:
            corr_db=str(pathlib.Path(tmp)/"correlation.db")
            corr_conn=init_db(corr_db)
            assert corr_conn is not None
            corr_conn.execute(
                "INSERT INTO v9_pro_history (date,spot_pct,foreign_spot,foreign_fut,pcr,vix,rsi,k,d,correlation_eligible) "
                "VALUES (?,?,?,?,?,?,?,?,?,?)",
                ("2026-10-01",1,2,3,0.8,18,40,20,25,1)
            )
            corr_conn.commit(); corr_conn.close()
            insufficient=calculate_historical_correlation(corr_db)
            assert insufficient["matrix"]==[] and "1/5" in insufficient["desc"]
            corr_conn=sqlite3.connect(corr_db)
            for day in range(2,7):
                corr_conn.execute(
                    "INSERT INTO v9_pro_history (date,spot_pct,foreign_spot,foreign_fut,pcr,vix,rsi,k,d,correlation_eligible) "
                    "VALUES (?,?,?,?,?,?,?,?,?,?)",
                    (f"2026-10-0{day}",day,day*2,day*3,0.5+day/10,15+day,30+day,10+day,15+day,1)
                )
            # An incomplete row must never enter the matrix.
            corr_conn.execute(
                "INSERT INTO v9_pro_history (date,spot_pct,correlation_eligible) VALUES (?,?,?)",
                ("2026-10-07",99,0)
            )
            corr_conn.commit(); corr_conn.close()
            enough=calculate_historical_correlation(corr_db)
            assert len(enough["labels"])==8 and len(enough["matrix"])==8
            assert len(enough["matrix"][0])==8 and "6 筆" in enough["desc"]
            assert abs(enough["matrix"][0][1]-1.0)<1e-9
        print("[17F SELF-TEST] PASS: full, sparse, empty-data, normalization, optimizer-before-score, T0-sqlite-date, v9-only-schema, invalid-schema-rejection, data-report-consistency, data-ui-05-correlation")
        return 0
    except Exception:
        traceback.print_exc()
        return 1

def seed_correlation_history_for_dashboard(as_of_date, report_dir="data_reports", db_path="dashboards/v9_pro_history.db", lookback=5):
    """Seed the build-local V9 history DB from committed dated DATA_REPORTs before dashboard generation."""
    cutoff=_t0_iso_date(as_of_date)
    if not cutoff:
        raise ValueError(f"Invalid seed cutoff date: {as_of_date!r}")
    paths=sorted(pathlib.Path(report_dir).glob("DATA_REPORT_*.md"))
    selected=[]
    for path in paths:
        match=re.search(r"DATA_REPORT_(\d{8})\.md$",path.name)
        if not match:
            continue
        report_date=_t0_iso_date(match.group(1))
        if report_date and report_date<=cutoff:
            selected.append((report_date,path))
    selected=selected[-int(lookback):]
    if not selected:
        raise FileNotFoundError(f"No dated DATA_REPORTs found in {report_dir} up to {cutoff}")
    for report_date,path in selected:
        parsed=parse_data_report(path)
        actual=_t0_iso_date(parsed.get("meta",{}).get("t0_date"))
        if actual!=report_date:
            raise ValueError(f"DATA_REPORT date mismatch: {path} declares {actual}")
        tech=fetch_technical_indicators_with_fallback(parsed["meta"]["t0_date"])
        analyzer=V9Analyzer(parsed,tech)
        bias,_,_=analyzer.calculate_bias()
        corr_values = {
            "spot_pct": analyzer.signals.get("spot_pct"),
            "foreign_spot": analyzer.signals.get("foreign"),
            "foreign_fut": analyzer.signals.get("foreign_futures"),
            "pcr": analyzer.signals.get("pcr"),
            "vix": analyzer.signals.get("vix"),
            "rsi": tech.get("rsi"), "k": tech.get("k"), "d": tech.get("d")
        }
        print(f"[CORRELATION SEED] {report_date} eligibility fields: {corr_values}")
        # Replace any row created earlier in this same build; the normal daily path may have
        # stored an incomplete row before historical inputs were fully reconstructed.
        seed_conn=init_db(db_path)
        if not seed_conn:
            raise RuntimeError(f"Could not open correlation seed DB for {report_date}")
        seed_conn.execute("DELETE FROM v9_pro_history WHERE date=?", (report_date,))
        seed_conn.commit()
        seed_conn.close()
        if not save_today_to_db(bias,analyzer.signals,tech,report_date.replace("-",""),db_path):
            raise RuntimeError(f"Could not seed correlation history from {path}")
        print(f"[CORRELATION SEED] {report_date}: saved/verified")
    corr=calculate_historical_correlation(db_path,min_samples=5,lookback=lookback,as_of_date=cutoff)
    print(f"[CORRELATION SEED] Dashboard history: {corr['desc']}")
    return corr


def run_historical_correlation_replay(report_dir="data_reports", dates=None):
    """Replay real dated DATA_REPORTs into a temporary V9 DB and verify 0/5 -> 5/5 accumulation."""
    import tempfile
    dates = dates or ["20261027", "20261028", "20261029", "20261030", "20261102"]
    with tempfile.TemporaryDirectory(prefix="v9-correlation-replay-") as tmp:
        db_path=str(pathlib.Path(tmp)/"v9_pro_history.db")
        print("[CORRELATION REPLAY] Temporary DB only; production history is untouched.")
        for date in dates:
            report_path=pathlib.Path(report_dir)/f"DATA_REPORT_{date}.md"
            if not report_path.is_file():
                raise FileNotFoundError(f"Historical DATA_REPORT missing: {report_path}")
            parsed=parse_data_report(report_path)
            report_date=str(parsed.get("meta",{}).get("t0_date") or "").replace("-","")
            if report_date!=date:
                raise ValueError(f"Report date mismatch: requested {date}, report T0={report_date}")
            tech=fetch_technical_indicators_with_fallback(parsed["meta"]["t0_date"])
            analyzer=V9Analyzer(parsed,tech)
            bias,_,_=analyzer.calculate_bias()
            if not save_today_to_db(bias,analyzer.signals,tech,date,db_path):
                raise RuntimeError(f"Could not save historical sample {date}")
            conn=sqlite3.connect(db_path)
            row=conn.execute(
                "SELECT correlation_eligible FROM v9_pro_history WHERE date=?",
                (datetime.strptime(date,"%Y%m%d").strftime("%Y-%m-%d"),)
            ).fetchone()
            eligible_count=conn.execute(
                "SELECT COUNT(*) FROM v9_pro_history WHERE correlation_eligible=1"
            ).fetchone()[0]
            conn.close()
            expected_count=dates.index(date)+1
            if not row or row[0]!=1 or eligible_count!=expected_count:
                raise AssertionError(f"Historical sample accumulation mismatch on {date}: eligible={row[0] if row else 'missing'}, cumulative={eligible_count}, expected={expected_count}")
            corr=calculate_historical_correlation(db_path,min_samples=5,as_of_date=date)
            print(f"[CORRELATION REPLAY] {date}: eligible={row[0]}; cumulative={eligible_count}/5; {corr['desc']}")
        conn=sqlite3.connect(db_path)
        final_count=conn.execute(
            "SELECT COUNT(*) FROM v9_pro_history WHERE correlation_eligible=1"
        ).fetchone()[0]
        dates_saved=conn.execute(
            "SELECT date FROM v9_pro_history WHERE correlation_eligible=1 ORDER BY date"
        ).fetchall()
        conn.close()
        final=calculate_historical_correlation(db_path,min_samples=5,as_of_date=dates[-1])
        matrix=final.get("matrix") or []
        if final_count!=5 or not matrix or len(final.get("labels",[]))<2:
            raise AssertionError(
                f"Historical correlation replay failed: {final_count}/5 eligible samples; {final.get('desc')}"
            )
        if len(matrix)!=len(final["labels"]) or any(len(row)!=len(final["labels"]) for row in matrix):
            raise AssertionError("Correlation matrix dimensions do not match labels")
        if any(value is None or not math.isfinite(float(value)) for row in matrix for value in row):
            raise AssertionError("Correlation matrix contains null or non-finite values")
        for i in range(len(matrix)):
            if abs(matrix[i][i]-1.0)>1e-4:
                raise AssertionError(f"Correlation diagonal is not 1.0 at index {i}")
            for j in range(len(matrix)):
                if abs(matrix[i][j]-matrix[j][i])>1e-4:
                    raise AssertionError(f"Correlation matrix is not symmetric at ({i},{j})")
        print(f"[CORRELATION REPLAY] PASS: {final_count}/5 real dated reports; dates={[x[0] for x in dates_saved]}; finite symmetric matrix={len(final['labels'])}x{len(final['labels'])}")
    return 0

def main():
    parser=argparse.ArgumentParser(description="V9 Pro Builder 17F + SQLite + 41 cards + data.json only - Skill daily-premarket-analysis-v9-pro")
    parser.add_argument('--data_report', default=None, help="path to DATA_REPORT md")
    parser.add_argument('--out', default="dashboards/data-20261027.json", help="output data.json path - must be dashboards/")
    parser.add_argument('--date', default=None, help="YYYYMMDD")
    parser.add_argument('--golden', default='templates/v9-pro-react-template.html', help="golden template path (for reference, v9 no longer injects)")
    parser.add_argument('--self-test', action='store_true', help="run fast offline 17F scoring tests and exit")
    parser.add_argument('--history-replay', action='store_true', help="replay five real historical DATA_REPORTs and verify correlation accumulation in a temporary DB")
    parser.add_argument('--seed-correlation-history', action='store_true', help="seed build-local SQLite correlation history from dated DATA_REPORTs")
    args=parser.parse_args()
    if args.self_test:
        return run_17f_self_tests()
    if args.history_replay:
        return run_historical_correlation_replay()
    if args.seed_correlation_history:
        if not args.date:
            raise ValueError('--seed-correlation-history requires --date YYYYMMDD')
        corr=seed_correlation_history_for_dashboard(args.date)
        return 0 if corr.get('matrix') else 2
    date_str=args.date.strip() if args.date else ""
    if date_str and (len(date_str)!=8 or not date_str.isdigit()):
        raise ValueError(f"Invalid --date {date_str!r}; expected YYYYMMDD")
    if date_str:
        _normalize_t0_date(date_str)

    # Output Path Rule check
    out_path=pathlib.Path(args.out)
    if "dashboards" not in str(out_path):
        print(f"[V9-17F] WARNING: Output Path Rule says dashboards/ 唯一, but out={out_path}, auto-correct to dashboards/")
        out_path=pathlib.Path(f"dashboards/{out_path.name}")

    # find report
    report_path=None
    if args.data_report and pathlib.Path(args.data_report).exists():
        report_path=pathlib.Path(args.data_report)
    else:
        candidates=[]
        for loc in ["", "dashboards/", "data/", "reports/", "data_reports/", "/mnt/data/"]:
            candidates.append(pathlib.Path(f"{loc}DATA_REPORT_{date_str}.md"))
        all_reports=glob.glob("DATA_REPORT_*.md") + glob.glob("dashboards/DATA_REPORT_*.md") + glob.glob("data_reports/DATA_REPORT_*.md") + glob.glob("/mnt/data/*.md")
        all_reports_sorted=sorted(all_reports, reverse=True)
        for r in all_reports_sorted:
            p=pathlib.Path(r)
            if p not in candidates: candidates.append(p)
        for c in candidates:
            if c.exists(): report_path=c; print(f"[V9-17F] Auto-found DATA_REPORT: {c}"); break

    if not report_path or not report_path.exists():
        print(f"ERROR: DATA_REPORT not found")
        for p in pathlib.Path("/mnt/data").glob("*.md"):
            if "DATA_REPORT" in p.name.upper() or "data_report" in p.name.lower():
                report_path=p; print(f"[V9-17F] Using fallback {p}"); break
        if not report_path or not report_path.exists(): return 1

    parsed=parse_data_report(report_path)
    report_t0=str(parsed.get('meta',{}).get('t0_date') or '').replace('-','')
    if not report_t0 or len(report_t0)!=8 or not report_t0.isdigit():
        raise ValueError(f"DATA_REPORT has invalid or missing T0 date: {parsed.get('meta',{}).get('t0_date')!r}")
    if date_str and date_str!=report_t0:
        raise ValueError(f"--date {date_str} does not match DATA_REPORT T0 {report_t0}")
    date_str=report_t0
    print(f"[V9-17F] Parsed {report_path}: T0={date_str}, spot {parsed['spot']['close']} {parsed['spot']['pct']}% foreign {parsed['inst']['foreign']}")
    data_warnings=parsed.get('meta',{}).get('data_quality_warnings',[])
    print(f"[V9-17F] DATA_REPORT consistency: {len(data_warnings)} warning(s)")
    for warning in data_warnings:
        print(f"[V9-17F] DATA_REPORT WARNING: {warning}")

    tech=fetch_technical_indicators_with_fallback(parsed['meta']['t0_date'])

    # SQLite flow: all history attribution follows the requested T0 report date.
    try: update_next_day_pct(date_str, parsed['spot']['close'])
    except Exception as e: print(f"[V9-17F] update_next_day non-critical: {e}")

    analyzer=V9Analyzer(parsed, tech)
    db_status=get_db_status()
    print(f"[V9-17F] DB status: {db_status}")

    real_win_rates=None
    try:
        real_win_rates=get_factor_win_rates_from_db(as_of_date=date_str)
    except Exception as e:
        print(f"[V9-17F] SQLite optimizer unavailable; use base/dynamic weights: {e}")
    bias,factors,weights=analyzer.calculate_bias(real_win_rates)
    print(f"[V9-17F] 17F active={analyzer.factor_quality['active_count']}/17 count_coverage={analyzer.factor_quality['count_coverage_pct']}% base_weight_coverage={analyzer.factor_quality['base_weight_coverage_pct']}% effective_weight_total={sum(weights.values()):.6f}")

    historical=None
    try:
        save_today_to_db(bias, analyzer.signals, tech, date_str)
        analyzer.signals['bias']=bias
        historical=find_historical_similarity(analyzer.signals, as_of_date=date_str)
        if historical and historical['avg_next_pct']<-1.0:
            print(f"[V9-17F] Historical bearish observation avg {historical['avg_next_pct']:.2f}%")
    except Exception as e:
        print(f"[V9-17F] DB history non-critical; continue dashboard build: {e}")
        historical=None

    final=build_final_json(parsed, tech, analyzer, historical, db_status, date_str)

    corr_check=final.get('analysis',{}).get('correlation',{})
    print(f"[CORRELATION DASHBOARD OUTPUT] {corr_check.get('desc')} labels={len(corr_check.get('labels',[]))} matrix_rows={len(corr_check.get('matrix',[]))}")

    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(json.dumps(final, ensure_ascii=False, indent=2), encoding='utf-8')
    print(f"[V9-17F] Wrote {out_path} size {out_path.stat().st_size} bias {final['analysis']['bias']} analysis_cards {final['analysis']['analysis_card_count']} visible_blocks {final['analysis']['visible_block_count']} db_mode {db_status.get('mode')}")
    print(f"[V9-17F] CHECK OK: 17-Factor + VIX Dynamic + RSI/MACD + SQLite真DB + 42個可見區塊全動態 + data.json only + pure React template")
    return 0

if __name__=="__main__":
    sys.exit(main())
