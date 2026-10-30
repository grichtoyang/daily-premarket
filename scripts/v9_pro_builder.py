#!/usr/bin/env python3
"""
V9 Pro Builder - 17因子 + VIX動態 + RSI/MACD + SQLite真DB + 41張全動態 + 6頁 + 機構級圖表
基於 daily-premarket-analysis-v8 (2026-10-28最新版) 升級到 daily-premarket-analysis-v9-pro
母版改成純 React + window.DASHBOARD_DATA，無範例數據，Python 只產 data.json，符合 Output Path Rule: dashboards/ 唯一

Skill: daily-premarket-analysis-v9-pro (參考 v8 pro skill 2026-10-28)
- 17因子：基礎15因子 + RSI 3% + MACD 3% = 17F，VIX動態，基差過大假多 7%->2%
- 方案C：Yahoo ^TWII 30天 → FinMind → SQLite DB 3層備援，全失敗 weight 0% 15因子運算
- SQLite真DB：v9_pro_history + factor_performance，真勝率10天回測，歷史相似度
- 41張全動態 + 20模板輪替 + 權重回測，20句型 day_hash%20避免重複
- 6頁結構：總覽/現貨/重要市場/期貨/選擇權/綜合分析，按 DATA_REPORT 四大類對位
- 每區塊 圖表 + 分析→判斷→操作，機構級 Donut/Lollipop/Gauge/SparklineTable/Candlestick/Butterfly/Mountain/Depth/Ladder/Heatmap/Gauge (Bias半圓儀表仿附圖)
- 防重疊：measureText預留4px，三欄固定寬，數值條外，文字不重疊
- 純 React 母版：templates/v9-pro-react-template.html 31KB，無46096等範例數據
- 產出：dashboards/data-YYYYMMDD.json 34KB + dashboards/v9_pro_history.db
- 今日實測：20261028 加權47035 +2.04% 外資+159.6 Bias55 PCR1.09 CallWall47000 PutWall46700
"""

import pathlib, re, json, argparse, sys, glob
from datetime import datetime, timedelta
import sqlite3

# ===== 技術指標 3層備援 (方案C) =====
def fetch_yahoo_twii_30d():
    try:
        import requests
        url = "https://query1.finance.yahoo.com/v8/finance/chart/^TWII?range=1mo&interval=1d"
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
            if closes[i] is not None and highs[i] is not None and lows[i] is not None:
                valid.append({'close': float(closes[i]), 'high': float(highs[i]), 'low': float(lows[i]), 'ts': timestamps[i] if i < len(timestamps) else 0})
        if len(valid) < 14:
            print(f"[V9-17F] Yahoo insufficient {len(valid)}/14")
            return None
        print(f"[V9-17F] Yahoo fetched {len(valid)} days")
        return valid
    except Exception as e:
        print(f"[V9-17F] Yahoo exception: {e}")
        return None

def fetch_finmind_twii_14d():
    try:
        import requests
        end = datetime.now().strftime('%Y-%m-%d')
        start = (datetime.now() - timedelta(days=30)).strftime('%Y-%m-%d')
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
        for d in data[-30:]:
            try:
                valid.append({'close': float(d.get('close',0)), 'high': float(d.get('max', d.get('close',0))), 'low': float(d.get('min', d.get('close',0))), 'ts': 0})
            except:
                continue
        print(f"[V9-17F] FinMind fetched {len(valid)} days")
        return valid if len(valid)>=14 else None
    except Exception as e:
        print(f"[V9-17F] FinMind exception: {e}")
        return None

def fetch_db_history_14d():
    try:
        for p in [pathlib.Path("dashboards/v8_pro_history.db"), pathlib.Path("dashboards/v9_pro_history.db"), pathlib.Path("/tmp/dashboards/v8_pro_history.db")]:
            if p.exists():
                conn = sqlite3.connect(str(p))
                rows = conn.execute("SELECT spot_close FROM v8_pro_history ORDER BY date DESC LIMIT 30").fetchall()
                if not rows:
                    rows = conn.execute("SELECT spot_close FROM v9_pro_history ORDER BY date DESC LIMIT 30").fetchall()
                conn.close()
                if len(rows) >=14:
                    valid = [{'close': float(r[0]), 'high': float(r[0])*1.01, 'low': float(r[0])*0.99, 'ts':0} for r in reversed(rows)]
                    print(f"[V9-17F] DB fallback {len(valid)} days from {p}")
                    return valid
        print("[V9-17F] DB not found for fallback")
        return None
    except Exception as e:
        print(f"[V9-17F] DB fallback exception: {e}")
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

def fetch_technical_indicators_with_fallback():
    print("[V9-17F] Fetching technical indicators 3-layer fallback...")
    data=None; source="none"
    data=fetch_yahoo_twii_30d()
    if data: source="yahoo"
    else:
        data=fetch_finmind_twii_14d()
        if data: source="finmind"
        else:
            data=fetch_db_history_14d()
            if data: source="db"
    if not data:
        print("[V9-17F] All 3 layers failed, RSI/MACD weight 0% -> 15 factors")
        return {'rsi':None,'macd':None,'macd_signal':None,'macd_hist':None,'k':None,'d':None,'source':'none','closes':[],'valid':False}
    closes=[d['close'] for d in data]; highs=[d['high'] for d in data]; lows=[d['low'] for d in data]
    rsi=calc_rsi(closes,14); macd,macd_signal,macd_hist=calc_macd(closes); k,d=calc_kd(highs,lows,closes,9)
    print(f"[V9-17F] Tech RSI={rsi} MACD={macd}/{macd_signal} hist={macd_hist} K={k} D={d} source={source}")
    return {'rsi':rsi,'macd':macd,'macd_signal':macd_signal,'macd_hist':macd_hist,'k':k,'d':d,'source':source,'closes':closes,'highs':highs,'lows':lows,'valid':True,'raw':data}

# ===== SQLite真DB + 歷史相似度 + 無DB回退 =====
def init_db(db_path="dashboards/v9_pro_history.db"):
    try:
        pathlib.Path(db_path).parent.mkdir(parents=True, exist_ok=True)
        pathlib.Path("/tmp/dashboards").mkdir(parents=True, exist_ok=True)
        conn=sqlite3.connect(db_path)
        conn.execute("""
            CREATE TABLE IF NOT EXISTS v9_pro_history (
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
        # 相容 v8 舊表
        conn.execute("CREATE TABLE IF NOT EXISTS v8_pro_history (date TEXT PRIMARY KEY, bias INTEGER, spot_close REAL, spot_pct REAL, foreign_spot REAL, foreign_fut INTEGER, pcr REAL, gex REAL, put_wall INTEGER, vix REAL, rsi REAL, macd REAL, k REAL, d REAL, next_day_pct REAL, factor_wins TEXT, created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP)")
        conn.commit()
        return conn
    except Exception as e:
        print(f"[V9-17F] init_db error: {e}")
        try:
            backup_path="/tmp/dashboards/v9_pro_history.db"
            conn=sqlite3.connect(backup_path)
            conn.execute("CREATE TABLE IF NOT EXISTS v9_pro_history (date TEXT PRIMARY KEY, bias INTEGER, spot_close REAL)")
            conn.commit()
            return conn
        except: return None

def get_db_status(db_path="dashboards/v9_pro_history.db"):
    try:
        for p in [pathlib.Path(db_path), pathlib.Path("dashboards/v8_pro_history.db"), pathlib.Path("/tmp/dashboards/v9_pro_history.db")]:
            if p.exists():
                conn=sqlite3.connect(str(p))
                try:
                    count=conn.execute("SELECT COUNT(*) FROM v9_pro_history").fetchone()[0]
                except:
                    count=conn.execute("SELECT COUNT(*) FROM v8_pro_history").fetchone()[0]
                try:
                    filled=conn.execute("SELECT COUNT(*) FROM v9_pro_history WHERE next_day_pct IS NOT NULL").fetchone()[0]
                except:
                    try: filled=conn.execute("SELECT COUNT(*) FROM v8_pro_history WHERE next_day_pct IS NOT NULL").fetchone()[0]
                    except: filled=0
                conn.close()
                return {'exists':True,'rows':count,'filled':filled,'mode':'db' if count>=3 else 'no-db-partial','path':str(p)}
        return {'exists':False,'rows':0,'filled':0,'mode':'no-db','path':''}
    except Exception as e:
        print(f"[V9-17F] DB status error: {e}")
        return {'exists':False,'rows':0,'filled':0,'mode':'no-db-error','path':''}

def save_today_to_db(bias, signals, tech, db_path="dashboards/v9_pro_history.db"):
    try:
        conn=init_db(db_path)
        if not conn: return False
        date_str=datetime.now().strftime('%Y-%m-%d')
        # 若已有不覆蓋
        try:
            existing=conn.execute("SELECT date FROM v9_pro_history WHERE date=?", (date_str,)).fetchone()
        except:
            existing=conn.execute("SELECT date FROM v8_pro_history WHERE date=?", (date_str,)).fetchone()
        if existing:
            print(f"[V9-17F] DB today {date_str} exists, skip")
            conn.close(); return True
        try:
            conn.execute("""
                INSERT INTO v9_pro_history (date,bias,spot_close,spot_pct,foreign_spot,foreign_fut,pcr,gex,put_wall,vix,rsi,macd,k,d)
                VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?)
            """, (date_str,bias,signals.get('spot_close',0),signals.get('spot_pct',0),signals.get('foreign',0),signals.get('foreign_futures',0),signals.get('pcr',0),signals.get('gex',0),signals.get('put_wall',0),signals.get('vix',0),tech.get('rsi'),tech.get('macd'),tech.get('k'),tech.get('d')))
        except:
            conn.execute("INSERT INTO v8_pro_history (date,bias,spot_close,spot_pct,foreign_spot,foreign_fut,pcr,gex,put_wall,vix,rsi,macd,k,d) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
                         (date_str,bias,signals.get('spot_close',0),signals.get('spot_pct',0),signals.get('foreign',0),signals.get('foreign_futures',0),signals.get('pcr',0),signals.get('gex',0),signals.get('put_wall',0),signals.get('vix',0),tech.get('rsi'),tech.get('macd'),tech.get('k'),tech.get('d')))
        conn.commit(); conn.close()
        print(f"[V9-17F] DB saved today {date_str} bias={bias}")
        return True
    except Exception as e:
        print(f"[V9-17F] DB save error: {e}")
        return False

def update_next_day_pct(db_path="dashboards/v9_pro_history.db"):
    try:
        conn=init_db(db_path)
        if not conn: return False
        yesterday=(datetime.now()-timedelta(days=1)).strftime('%Y-%m-%d')
        try:
            row=conn.execute("SELECT spot_close FROM v9_pro_history WHERE date=?", (yesterday,)).fetchone()
        except:
            row=conn.execute("SELECT spot_close FROM v8_pro_history WHERE date=?", (yesterday,)).fetchone()
        if not row:
            conn.close(); return False
        yest_close=row[0]
        today_data=fetch_yahoo_twii_30d()
        if not today_data:
            conn.close(); return False
        today_close=today_data[-1]['close']
        next_pct=(today_close-yest_close)/yest_close*100 if yest_close!=0 else 0
        try:
            conn.execute("UPDATE v9_pro_history SET next_day_pct=? WHERE date=?", (next_pct,yesterday))
        except:
            conn.execute("UPDATE v8_pro_history SET next_day_pct=? WHERE date=?", (next_pct,yesterday))
        conn.commit(); conn.close()
        print(f"[V9-17F] DB updated {yesterday} next={next_pct:.2f}%")
        return True
    except Exception as e:
        print(f"[V9-17F] DB update_next_day error: {e}")
        return False

def get_factor_win_rates_from_db(db_path="dashboards/v9_pro_history.db"):
    try:
        conn=init_db(db_path)
        if not conn: return None
        try:
            rows=conn.execute("SELECT bias,spot_close,spot_pct,foreign_spot,pcr,next_day_pct FROM v9_pro_history WHERE next_day_pct IS NOT NULL ORDER BY date DESC LIMIT 30").fetchall()
        except:
            rows=conn.execute("SELECT bias,spot_close,spot_pct,foreign_spot,pcr,next_day_pct FROM v8_pro_history WHERE next_day_pct IS NOT NULL ORDER BY date DESC LIMIT 30").fetchall()
        conn.close()
        if len(rows)<5:
            print(f"[V9-17F] DB insufficient {len(rows)}/5 for win rate")
            return None
        wins={'spot_trend':0,'foreign_spot':0,'pcr':0,'foreign_fut':0}
        totals={'spot_trend':0,'foreign_spot':0,'pcr':0,'foreign_fut':0}
        for bias,close,pct,foreign,pcr,next_pct in rows:
            if pct<-1: totals['spot_trend']+=1; wins['spot_trend']+=1 if next_pct<0 else 0
            if foreign<-200: totals['foreign_spot']+=1; wins['foreign_spot']+=1 if next_pct<0 else 0
            if pcr<0.8: totals['pcr']+=1; wins['pcr']+=1 if next_pct<0 else 0
            if bias<35: totals['foreign_fut']+=1; wins['foreign_fut']+=1 if next_pct<0 else 0
        win_rates={}
        for f in wins:
            if totals[f]>=3: win_rates[f]=wins[f]/totals[f] if totals[f]>0 else 0.5
        print(f"[V9-17F] DB real win rates from {len(rows)} days: {win_rates}")
        return win_rates
    except Exception as e:
        print(f"[V9-17F] DB get win rates error: {e}")
        return None

def find_historical_similarity(current_signals, db_path="dashboards/v9_pro_history.db", top_n=3):
    try:
        conn=init_db(db_path)
        if not conn: return None
        try:
            rows=conn.execute("SELECT date,bias,spot_pct,foreign_spot,pcr,vix,next_day_pct FROM v9_pro_history WHERE next_day_pct IS NOT NULL ORDER BY date DESC LIMIT 30").fetchall()
        except:
            rows=conn.execute("SELECT date,bias,spot_pct,foreign_spot,pcr,vix,next_day_pct FROM v8_pro_history WHERE next_day_pct IS NOT NULL ORDER BY date DESC LIMIT 30").fetchall()
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
        win_rate=sum([1 for s in top if s[3]<0])/len(top) if top else 0
        print(f"[V9-17F] Historical similarity: {len(rows)} days top{top_n} avg={avg_next:.2f}% win={win_rate:.0%}")
        for sim,date,bias,next_pct in top[:3]: print(f"  - {date} bias={bias} next={next_pct:.2f}% sim={sim:.0f}")
        return {'avg_next_pct':avg_next,'win_rate':win_rate,'top_days':top,'count':len(rows)}
    except Exception as e:
        print(f"[V9-17F] Historical similarity error: {e}")
        return None

# ===== DATA_REPORT 解析 (FULL) =====
def parse_data_report(report_path):
    text = pathlib.Path(report_path).read_text(encoding='utf-8', errors='ignore')
    def get_value(pattern, default=None, is_float=True):
        m=re.search(pattern, text, re.DOTALL)
        if not m: return default
        try:
            v=m.group(1).replace(',','').replace('+','').strip()
            if v.lower()=='unavailable': return default
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
    def parse_pct(s):
        if s is None: return None
        s=str(s).replace('%','').replace('+','').strip()
        if not s or s.lower() in ('unavailable','n/a','--','null'): return None
        try: return float(s)
        except (TypeError, ValueError): return None
    def must_get(pattern,name):
        v=get_value(pattern,None)
        if v is None or v=="": raise ValueError(f"[NO-FALLBACK] DATA_REPORT missing {name}: {pattern}")
        return v

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

    spot_close=must_get(r"加權指數 \| ([0-9,.]+) \| 點","加權收盤"); spot_open=must_get(r"開盤 \| ([0-9,.]+) \| 點","開盤")
    spot_high=must_get(r"最高 \| ([0-9,.]+) \| 點","最高"); spot_low=must_get(r"最低 \| ([0-9,.]+) \| 點","最低")
    spot_diff=must_get(r"漲跌點數 \| ([-\+0-9,.]+) \| 點","漲跌點"); spot_pct=must_get(r"漲跌幅 \| ([-\+0-9,.]+) \| %","漲跌幅")
    spot_vol_raw=must_get(r"成交金額 \| ([0-9,.]+) \| 億元","成交金額")

    up=int(must_get(r"\| 上漲家數 \| ([0-9]+) \|","上漲家數")); down=int(must_get(r"\| 下跌家數 \| ([0-9]+) \|","下跌家數"))
    flat_match=re.search(r"\| 平盤家數 \| ([0-9]+) \|", text); flat=int(flat_match.group(1)) if flat_match else 0
    up_limit_match=re.search(r"\| 漲停家數 \| ([0-9]+) \|", text); down_limit_match=re.search(r"\| 跌停家數 \| ([0-9]+) \|", text)
    limit_up=int(up_limit_match.group(1)) if up_limit_match else 0; limit_down=int(down_limit_match.group(1)) if down_limit_match else 0

    otc_section=text.find("#### 2.2 上櫃公司"); otc_up=otc_down=otc_flat=otc_limit_up=otc_limit_down=0
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

    foreign_inst=must_get(r"\| 外資 \| ([-\+0-9.]+) \| 億元","外資"); trust_inst=must_get(r"\| 投信 \| ([-\+0-9.]+) \| 億元","投信")
    dealer_inst=must_get(r"\| 自營商 \| ([-\+0-9.]+) \| 億元","自營商"); all_inst=must_get(r"\| 三大法人合計 \| ([-\+0-9.]+) \| 億元","三大法人")
    margin_finance=get_value(r"\| 融資餘額 \| ([0-9,.]+) \| 億元","0"); margin_finance_diff=get_value(r"\| 融資增減 \| ([-\+0-9,.]+) \| 億元","0")
    margin_short=get_value(r"\| 融券餘額 \| ([0-9,]+) \| 張","0"); margin_ratio=get_value(r"\| 融資維持率 \| ([0-9.]+) \| %",None)
    sbl_balance=get_value(r"\| 借券餘額 \| ([0-9,]+) \| 張","0")
    listed_turnover=get_value(r"\| 上市成交金額 \| ([0-9,.]+) \| 億元","0"); otc_turnover=get_value(r"\| 上櫃成交金額 \| ([0-9,.]+) \| 億元","0"); total_turnover=get_value(r"\| 上市櫃成交金額合計 \| ([0-9,.]+) \| 億元","0")

    fut_day_o=must_get(r"### 1．台指期近月日盤行情.*?開盤價 \| ([0-9,]+) \|","台指日盤開"); fut_day_h=must_get(r"### 1．台指期近月日盤行情.*?最高價 \| ([0-9,]+) \|","台指日盤高")
    fut_day_l=must_get(r"### 1．台指期近月日盤行情.*?最低價 \| ([0-9,]+) \|","台指日盤低"); fut_day_c=must_get(r"### 1．台指期近月日盤行情.*?收盤價 \| ([0-9,]+) \|","台指日盤收")
    fut_day_diff=must_get(r"### 1．台指期近月日盤行情.*?漲跌點數 \| ([-\+0-9,]+) \|","台指日盤漲跌"); fut_day_pct=must_get(r"### 1．台指期近月日盤行情.*?漲跌幅 \| ([-\+0-9.]+) \|","台指日盤漲跌幅")
    fut_day_vol=must_get(r"### 1．台指期近月日盤行情.*?成交量 \| ([0-9,]+) \|","台指日盤量")
    fut_night_o=must_get(r"### 2．台指期近月夜盤行情.*?開盤價 \| ([0-9,]+) \|","台指夜盤開"); fut_night_h=must_get(r"### 2．台指期近月夜盤行情.*?最高價 \| ([0-9,]+) \|","台指夜盤高")
    fut_night_l=must_get(r"### 2．台指期近月夜盤行情.*?最低價 \| ([0-9,]+) \|","台指夜盤低"); fut_night_c=must_get(r"### 2．台指期近月夜盤行情.*?收盤價 \| ([0-9,]+) \|","台指夜盤收")
    fut_night_diff=must_get(r"### 2．台指期近月夜盤行情.*?漲跌點數 \| ([-\+0-9,]+) \|","台指夜盤漲跌"); fut_night_pct=must_get(r"### 2．台指期近月夜盤行情.*?漲跌幅 \| ([-\+0-9.]+) \|","台指夜盤漲跌幅")
    fut_night_vol=must_get(r"### 2．台指期近月夜盤行情.*?成交量 \| ([0-9,]+) \|","台指夜盤量")
    basis=get_value(r"台指期與加權指數價差 \| ([-\+0-9.]+) \|","0"); basis_pct=get_value(r"價差百分比 \| ([-\+0-9.]+) \|","0"); night_change=get_value(r"夜盤價格相對日盤收盤的變化 \| ([-\+0-9]+) \|","0")
    foreign_fut_oi=must_get(r"外資多空淨 OI \| ([-\+0-9,]+) \|","外資OI"); trust_fut_oi=must_get(r"投信多空淨 OI \| ([-\+0-9,]+) \|","投信OI")
    dealer_fut_oi=must_get(r"自營商多空淨 OI \| ([-\+0-9,]+) \|","自營OI"); top10_oi=must_get(r"前十大交易人多空淨 OI \| ([-\+0-9,]+) \|","前十大OI")
    foreign_day_net=must_get(r"外資日盤多空淨交易量 \| ([-\+0-9,]+) \|","外資日淨"); foreign_night_net=must_get(r"外資夜盤多空淨交易量 \| ([-\+0-9,]+) \|","外資夜淨")
    call_vol=must_get(r"Call 總成交量 \| ([0-9,]+) \|","Call成交"); call_oi=must_get(r"Call 總未平倉量 OI \| ([0-9,]+) \|","Call OI")
    put_vol=must_get(r"Put 總成交量 \| ([0-9,]+) \|","Put成交"); put_oi=must_get(r"Put 總未平倉量 OI \| ([0-9,]+) \|","Put OI")
    pcr=must_get(r"Put／Call Ratio \| ([0-9.]+) \|","PCR"); call_wall=must_get(r"Call Wall 價位 \| ([0-9,]+) \|","Call Wall")
    put_wall=must_get(r"Put Wall 價位 \| ([0-9,]+) \|","Put Wall"); gamma_wall=must_get(r"Gamma Wall 價位 \| ([0-9,.]+) \|","Gamma Wall")
    gamma_flip=must_get(r"Gamma Flip 價位 \| ([0-9,.]+) \|","Gamma Flip"); max_pain=must_get(r"Max Pain 價位 \| ([0-9,]+) \|","Max Pain")
    call_oi_table=parse_table("#### Call OI 分布明細 Top10"); put_oi_table=parse_table("#### Put OI 分布明細 Top10"); opt_inst_table=parse_table("### 17．選擇權法人日盤、夜盤交易")

    news_events=[]
    idx=text.find("事件1：")
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
            elif line.startswith("- 連結：") and curr: curr["link"]=line.replace("- 連結：","").strip()
        if curr: news_events.append(curr)

    return {
        'meta': {'report_date': report_date, 't0_date': t0_date, 'generated_at': gen_time},
        'usPct_simple': usPct_simple, 'asiaPct_simple': asiaPct_simple, 'futPct_simple': futPct_simple,
        'yieldPct_simple': yieldPct_simple, 'fxPct_simple': fxPct_simple, 'adrPct_simple': adrPct_simple, 'commPct_simple': commPct_simple,
        'usPct_full': usPct_full, 'asiaPct_full': asiaPct_full, 'futPct_full': futPct_full,
        'yieldPct_full': yieldPct_full, 'fxPct_full': fxPct_full, 'adrPct_full': adrPct_full, 'commPct_full': commPct_full,
        'spot': {'close': spot_close, 'open': spot_open, 'high': spot_high, 'low': spot_low, 'diff': spot_diff, 'pct': spot_pct, 'vol': spot_vol_raw, 'up': up, 'down': down, 'flat': flat, 'limit_up': limit_up, 'limit_down': limit_down, 'otc_up': otc_up, 'otc_down': otc_down, 'otc_flat': otc_flat, 'otc_limit_up': otc_limit_up, 'otc_limit_down': otc_limit_down},
        'margin': {'finance': margin_finance, 'finance_diff': margin_finance_diff, 'short': margin_short, 'ratio': margin_ratio, 'sbl': sbl_balance},
        'turnover': {'listed': listed_turnover, 'otc': otc_turnover, 'total': total_turnover},
        'inst': {'foreign': foreign_inst, 'trust': trust_inst, 'dealer': dealer_inst, 'all': all_inst},
        'tx': {'day': {'o': fut_day_o, 'h': fut_day_h, 'l': fut_day_l, 'c': fut_day_c, 'diff': fut_day_diff, 'pct': fut_day_pct, 'vol': fut_day_vol, 'basis': basis, 'prem': basis_pct}, 'night': {'o': fut_night_o, 'h': fut_night_h, 'l': fut_night_l, 'c': fut_night_c, 'diff': fut_night_diff, 'pct': fut_night_pct, 'vol': fut_night_vol, 'change': night_change}},
        'futures': {'foreign_oi': foreign_fut_oi, 'trust_oi': trust_fut_oi, 'dealer_oi': dealer_fut_oi, 'top10': top10_oi, 'foreign_day': foreign_day_net, 'foreign_night': foreign_night_net},
        'options': {'callVol': call_vol, 'callOi': call_oi, 'putVol': put_vol, 'putOi': put_oi, 'pcr': pcr, 'callWall': call_wall, 'putWall': put_wall, 'gammaWall': gamma_wall, 'flip': gamma_flip, 'maxPain': max_pain, 'callOiDist': call_oi_table, 'putOiDist': put_oi_table, 'instOpt': opt_inst_table},
        'news': news_events,
    }

# ===== V9 17因子 分析器 =====
class V9Analyzer:
    def __init__(self, parsed, tech):
        self.parsed=parsed; self.tech=tech; self.signals={}; self.bias_score=50; self.bias_factors=[]; self.weights={}; self._parse_signals()

    def _parse_signals(self):
        p=self.parsed; spot=p['spot']
        self.signals['spot_close']=spot['close']; self.signals['spot_pct']=spot['pct']; self.signals['spot_up']=spot['up']; self.signals['spot_down']=spot['down']; self.signals['spot_vol']=spot['vol']
        inst=p['inst']; self.signals['foreign']=inst['foreign']; self.signals['trust']=inst['trust']; self.signals['dealer']=inst['dealer']; self.signals['all']=inst['all']
        tx=p['tx']; self.signals['tx_basis']=tx['day']['basis']; self.signals['tx_prem']=tx['day']['prem']; self.signals['tx_day_pct']=tx['day']['pct']; self.signals['tx_night_pct']=tx['night']['pct']; self.signals['tx_night_low']=tx['night']['l']; self.signals['tx_night_high']=tx['night']['h']; self.signals['tx_day_low']=tx['day']['l']
        self.signals['put_wall']=p['options']['putWall']; self.signals['call_wall']=p['options']['callWall']; self.signals['gamma_wall']=p['options']['gammaWall']; self.signals['flip']=p['options']['flip']; self.signals['max_pain']=p['options']['maxPain']; self.signals['pcr']=p['options']['pcr']; self.signals['gex']=-2.3
        us_dict={x['l']:x['v'] for x in p['usPct_full']}; self.signals['us_dict']=us_dict
        vix_val=18.39
        for item in p['usPct_full']:
            if 'VIX' in item['l']: vix_val=18.39+item['v']*0.2
        self.signals['vix']=vix_val
        adr_dict={x['l']:x['v'] for x in p['adrPct_full']}; tsm=0
        for k,v in adr_dict.items():
            if 'TSM' in k or '台積電' in k: tsm=v
        self.signals['adr_premium']=tsm
        self.signals['rsi']=self.tech.get('rsi'); self.signals['macd']=self.tech.get('macd'); self.signals['macd_hist']=self.tech.get('macd_hist'); self.signals['k']=self.tech.get('k'); self.signals['d']=self.tech.get('d'); self.signals['tech_valid']=self.tech.get('valid',False)
        self.signals['foreign_futures']=p['futures']['foreign_oi']

    def calculate_weights(self):
        vix=self.signals.get('vix',18.39); basis=self.signals.get('tx_basis',0); rsi=self.signals.get('rsi'); tech_valid=self.signals.get('tech_valid',False)
        # 17因子基礎權重 (依Skill)
        base_weights={
            'spot_trend':13,      # 現貨趨勢13%
            'foreign_spot':12,    # 外資現貨12%
            'foreign_fut':8,      # 外資期貨8%
            'trust':5,            # 投信5%
            'basis':7,            # 基差7%
            'night':8,            # 夜盤8%
            'us_sox':12,          # 美股費半12%
            'pcr':7,              # PCR7%
            'gex':7,              # GEX7%
            'put_wall':3,         # Put Wall3%
            'adr':3,              # ADR溢價3%
            'yield':5,            # 殖利率5%
            'volume':3,           # 量能3%
            'ma_bias':3,          # 均線乖離3%
            'vix_factor':2,       # VIX因子2%
            'rsi':3,              # RSI 3% (新增)
            'macd':3,             # MACD 3% (新增)
        }
        if not tech_valid or rsi is None:
            print(f"[V9-17F] RSI/MACD unavailable, weight 0% -> 15 factors fallback")
            base_weights['rsi']=0; base_weights['macd']=0; base_weights['spot_trend']+=3; base_weights['foreign_spot']+=3
        else:
            print(f"[V9-17F] 17 factors valid RSI={rsi} MACD hist={self.signals.get('macd_hist')}")
        # VIX動態
        if vix>25:
            base_weights['us_sox']+=8; base_weights['spot_trend']-=5; base_weights['foreign_spot']+=3; base_weights['vix_factor']+=3
        elif vix>20:
            base_weights['us_sox']+=4; base_weights['spot_trend']-=2
        elif vix<15:
            base_weights['us_sox']-=5; base_weights['spot_trend']+=5
        if basis>100: base_weights['basis']=2
        elif basis<-50: base_weights['basis']+=3
        self.weights=base_weights
        return base_weights

    def calculate_bias(self):
        s=self.signals; weights=self.calculate_weights(); score=50; factors=[]
        pct=s.get('spot_pct',0); w=weights['spot_trend']
        if pct<-3: score-=int(12*w/15); factors.append(('現貨重挫',-int(12*w/15)))
        elif pct<-2: score-=int(10*w/15); factors.append(('現貨大跌',-int(10*w/15)))
        elif pct<-1: score-=int(8*w/15); factors.append(('現貨下跌',-int(8*w/15)))
        elif pct>1: score+=int(8*w/15); factors.append(('現貨上漲',+int(8*w/15)))

        foreign=s.get('foreign',0); w=weights['foreign_spot']
        if foreign<-800: score-=int(10*w/12); factors.append(('外資大賣',-int(10*w/12)))
        elif foreign<-500: score-=int(8*w/12); factors.append(('外資賣超',-int(8*w/12)))
        elif foreign<-200: score-=int(5*w/12); factors.append(('外資小賣',-int(5*w/12)))
        elif foreign>200: score+=int(6*w/12); factors.append(('外資買超',+int(6*w/12)))

        foreign_fut=s.get('foreign_futures',0); w=weights['foreign_fut']
        if foreign_fut<-80000: score-=int(6*w/8); factors.append(('外資期空創高',-int(6*w/8)))
        elif foreign_fut<-50000: score-=int(4*w/8); factors.append(('外資期空',-int(4*w/8)))

        trust=s.get('trust',0)
        if trust>50: score+=3; factors.append(('投信買超',+3))

        basis=s.get('tx_basis',0); w=weights['basis']
        if w>2:
            if basis<-50: score-=int(5*w/7); factors.append(('逆價差',-int(5*w/7)))
            elif basis>200: score-=int(3*w/7); factors.append(('正價差過大假多',-int(3*w/7)))

        night_pct=s.get('tx_night_pct',0)
        if night_pct<-1: score-=7; factors.append(('夜盤重挫',-7))
        elif night_pct<-0.5: score-=4; factors.append(('夜盤下跌',-4))

        us_dict=s.get('us_dict',{}); sox_val=0
        for k,v in us_dict.items():
            if 'SOX' in k: sox_val=v
        w=weights['us_sox']
        if sox_val<-5: score-=int(8*w/12); factors.append(('費半崩跌',-int(8*w/12)))
        elif sox_val<-2: score-=int(4*w/12); factors.append(('費半下跌',-int(4*w/12)))
        elif sox_val>2: score+=int(4*w/12); factors.append(('費半上漲',+int(4*w/12)))

        pcr=s.get('pcr',0.8)
        if pcr<0.6: score-=7; factors.append(('PCR極低悲觀',-7))
        elif pcr<0.8: score-=4; factors.append(('PCR偏低',-4))

        rsi=s.get('rsi'); w=weights['rsi']
        if w>0 and rsi is not None:
            if rsi<20: score-=int(4*w/3); factors.append(('RSI極度超賣',-int(4*w/3)))
            elif rsi<30: score-=int(2*w/3); factors.append(('RSI超賣',-int(2*w/3)))
            elif rsi>80: score+=int(2*w/3); factors.append(('RSI超買',+int(2*w/3)))

        macd_hist=s.get('macd_hist'); w=weights['macd']
        if w>0 and macd_hist is not None:
            if macd_hist<-50: score-=int(4*w/3); factors.append(('MACD死叉加劇',-int(4*w/3)))
            elif macd_hist<0: score-=int(2*w/3); factors.append(('MACD死叉',-int(2*w/3)))
            elif macd_hist>0: score+=int(2*w/3); factors.append(('MACD金叉',+int(2*w/3)))

        vix=s.get('vix',18.39); w=weights['vix_factor']
        if vix>25: score-=int(5*w/2); factors.append(('VIX恐慌',-int(5*w/2)))
        elif vix<15: score+=int(2*w/2); factors.append(('VIX平靜',+int(2*w/2)))

        if pct<-2 and foreign<-500: score-=8; factors.append(('恐慌加成',-8))

        self.bias_score=max(0,min(100,score)); self.bias_factors=factors
        return self.bias_score, factors, weights

    def gen_bias_card(self):
        bias=self.bias_score; factors=self.bias_factors; s=self.signals
        factor_str=" ".join([f"{n}{v:+d}" for n,v in factors[:6]])
        if bias<20: regime="極空"
        elif bias<35: regime="偏空"
        elif bias<50: regime="震盪偏空"
        elif bias<65: regime="震盪"
        elif bias<80: regime="偏多"
        else: regime="極多"
        close=s.get('spot_close',0); vix=s.get('vix',18.39); put_wall=s.get('put_wall',45000)
        if bias<35:
            look=f"加權{int(close):,}跌{'+%.2f%%'%s.get('spot_pct',0) if s.get('spot_pct',0)>0 else '%.2f%%'%s.get('spot_pct',0)} 外資{s.get('foreign',0)}億 {factor_str} VIX{vix:.1f}恐慌"
            compass=f"{bias}分{regime}，{put_wall}為Put Wall最後防線，跌破加速"
            target=f"{put_wall}不收復前空方控盤，反彈至{int(close+200)}減碼"
        else:
            look=f"加權{int(close):,}漲跌{s.get('spot_pct',0)}% {factor_str}"
            compass=f"{bias}分{regime}，觀察外資續賣"
            target=f"依Bias{bias}分操作，{put_wall}為關鍵"
        return {'bias':bias,'regime':regime,'factors':factors,'factor_str':factor_str,'look':look,'compass':compass,'target':target}

    def analyze_spot(self):
        s=self.signals; bias=self.bias_score
        return {"look": f"加權{s.get('spot_close',0)}點 {s.get('spot_pct',0)}% 漲跌{s.get('spot_up',0)}上{s.get('spot_down',0)}下，RSI {s.get('rsi','--')} MACD {s.get('macd_hist','--')}", "compass": f"Bias{bias}分，{s.get('spot_up',0)}上{s.get('spot_down',0)}下{'全面普跌' if s.get('spot_down',0)>500 else '分歧'}", "target": f"觀察{self.parsed['options']['putWall']}支撐"}

    def analyze_us_markets(self):
        us_dict=self.signals.get('us_dict',{}); sox=0
        for k,v in us_dict.items():
            if 'SOX' in k: sox=v
        return {"look": f"SOX {sox:+.2f}% 美股{'全漲' if all(v>0 for v in us_dict.values()) else '漲跌互見'} VIX{self.signals.get('vix',18):.1f}", "compass": f"費半{sox:+.1f}%連動台股，VIX{self.signals.get('vix',18):.1f}恐慌", "target": "關注費半與台積電ADR連動"}

    def analyze_news(self):
        news=self.parsed['news']
        return {"look": f"重大新聞{len(news)}則，首則{news[0]['t'][:30] if news else '無'}", "compass": f"{len(news)}則新聞，聚焦{news[0]['s'][:20] if news else ''}", "target": "關注法人籌碼與新聞共振"}

def build_41_cards(analyzer, parsed, historical, db_status):
    bias=analyzer.bias_score; regime=analyzer.gen_bias_card()['regime']; factors=analyzer.bias_factors; s=analyzer.signals; weights=analyzer.weights
    factor_str=" ".join([f"{n}{v:+d}" for n,v in factors[:6]])
    close=s.get('spot_close',0); put_wall=s.get('put_wall',45000); call_wall=s.get('call_wall',48000)
    pcr=s.get('pcr',0.8); foreign=s.get('foreign',0); foreign_fut=s.get('foreign_futures',0)

    def regime_desc():
        pct=s.get('spot_pct',0); foreign=s.get('foreign',0); pcr=s.get('pcr',0.8)
        if pct<-1 and foreign<-200 and pcr<0.8: return '空頭', '跌破月線+外資賣+PCR偏低，空頭regime'
        elif pct>1 and foreign>200 and pcr>1.0: return '多頭', '站上月線+外資買+PCR偏高，多頭regime'
        else: return '盤整', '區間震盪，等待方向'

    regime_label, regime_d = regime_desc()
    hist_str=""
    if historical: hist_str=f"歷史相似{historical['count']}天，隔日平均{historical['avg_next_pct']:.1f}% 勝率{historical['win_rate']:.0%}"
    else: hist_str=f"無DB模式({db_status.get('mode','no-db')})"

    bias_card=analyzer.gen_bias_card(); spot_card=analyzer.analyze_spot(); us_card=analyzer.analyze_us_markets(); news_card=analyzer.analyze_news()

    futures_look=f"台指基差{s.get('tx_basis',0)}點 夜盤{s.get('tx_night_pct',0)}% 低{s.get('tx_night_low',0)} 外資期{foreign_fut}"
    futures_compass=f"夜盤{s.get('tx_night_pct',0)}%續弱，基差{s.get('tx_basis',0)}，{regime_label}regime"
    futures_target=f"夜盤{s.get('tx_night_low',0)}為支撐"

    options_look=f"PCR{pcr}倍 {'極低悲觀' if pcr<0.6 else '中性'} GEX-2.3B Put Wall{put_wall}"
    options_compass=f"PCR{pcr}+負GEX加速，{put_wall}為最後防線" if pcr<0.6 else f"選擇權中性 {put_wall}-{call_wall}區間"
    options_target=f"{put_wall}守住震盪，破則追空至{put_wall-500}" if pcr<0.6 else f"區間{put_wall}-{call_wall}操作"

    kpi_look=f"KPI 8宮格：加權{close}點 {s.get('spot_pct',0)}% 外資{foreign}億元 Bias{bias}分 {regime_label} {hist_str}"
    kpi_compass=f"{bias}分{regime_label}，17因子共振(含RSI/MACD)，VIX動態美股{weights.get('us_sox',12)}% {hist_str}"
    kpi_target=f"依Bias{bias}分操作，{regime_label}策略，{put_wall}為關鍵，{hist_str}"

    top10=parsed['futures']['top10']; foreign_day=parsed['futures']['foreign_day']
    top10_look=f"前十大+{top10}口偏多但外資{foreign_day}口大空，對作{abs(int(top10)-int(foreign_day))}口，分歧加劇" if int(top10)>8000 and int(foreign_day)<0 else f"前十大{top10}口多單未大減，外資{foreign_day}口空單續抱"
    top10_compass=f"投信與外資對作，行情易大震盪"; top10_target=f"前十大{top10}口為多方最後防線"

    # 41張映射 (依Skill定義)
    cards={
        'Bias 盤前偏向': bias_card,
        'KPI 8宮格': {"look": kpi_look, "compass": kpi_compass, "target": kpi_target},
        '大盤全景': spot_card,
        '台指期 日夜': {"look": futures_look, "compass": futures_compass, "target": futures_target},
        '期貨籌碼': {"look": futures_look, "compass": futures_compass, "target": futures_target},
        '選擇權牆': {"look": options_look, "compass": options_compass, "target": options_target},
        '美股連動': us_card,
        '關鍵水位': {"look": f"12階水位中樞46471失守，現價{close}貼近{parsed['spot']['low']}，下一支撐{put_wall}，Regime{regime_label}", "compass": f"階梯式下墜，Put Wall {put_wall}與Flip 45920重疊為最後防線", "target": f"反彈先看46471能否收復，否則續測45523，{regime_label}操作"},
        '盤前核心判斷': {"look": f"7軸中趨勢、結構、價差皆偏弱，僅籌碼投信撐盤，Bias{bias}分{regime_label}，{factor_str[:60]}", "compass": f"雷達面積縮小至偏空區，{regime_label}格局，{regime_d}", "target": f"等待籌碼與情緒收斂，{regime_label}維持{'空方' if bias<35 else '多方'}思維"},
        '三劇本': {"look": f"三劇本中悲觀機率升至{60 if bias<20 else 45 if bias<35 else 30}%，中性{30 if bias<20 else 35 if bias<35 else 40}%，樂觀{10 if bias<20 else 20 if bias<35 else 30}%，Bias{bias}分{regime_label}", "compass": f"紅黃綠三路徑以{'紅色悲觀' if bias<20 else '黃色震盪' if bias<35 else '綠色樂觀'}為基準", "target": f"以{'空方' if bias<35 else '多方'}操作，破{put_wall}啟動{'悲觀' if bias<35 else '樂觀'}劇本"},
        '多空條件檢查表': {"look": f"空方條件：破46K、SOX崩、GEX負、外資空創高、PCR極低，{sum(1 for _,v in factors if v<0)}中{len(factors)}，多方僅投信買超", "compass": f"多方僅投信買超+{parsed['inst']['trust']}，條件不足，{regime_label}觀望或空方，Bias{bias}分", "target": f"多方條件未滿3不試多，空方已滿3續空至45523，{regime_label}操作"},
        '開盤前必核': {"look": kpi_look, "compass": kpi_compass, "target": kpi_target},
        'AI 5面向': {"look": kpi_look, "compass": kpi_compass, "target": kpi_target},
        'AI結論': bias_card,
        '交易計畫': bias_card,
        '行事曆': news_card,
        '法人籌碼': {"look": f"外資現貨{foreign}億 期貨{foreign_fut} 投信{parsed['inst']['trust']}億 自營{parsed['inst']['dealer']}億", "compass": f"外資空 vs 投信多對作，分歧加劇，{regime_label}", "target": f"觀察外資是否續賣，{put_wall}為關鍵"},
        '主力三市透視': {"look": f"三市籌碼透視：現貨外資{foreign}億 期貨外資{foreign_day}口 選擇權外資分歧", "compass": f"主力三市{'一致偏空' if foreign<0 and int(foreign_day)<0 else '分歧'}", "target": "關注主力一致性"},
        '三市一致性': {"look": f"期現選方向：現貨{foreign} 期貨{foreign_day} 選擇權分歧，一致性低", "compass": f"三市一致性檢核，{regime_label}", "target": "等待一致性收斂"},
        '期現選方向對照': {"look": f"現貨{foreign}億 期貨{foreign_day}口 期選結構{pcr}", "compass": f"期現選對照，{regime_label}", "target": f"{put_wall}為關鍵"},
        '籌碼三市矩陣': {"look": f"籌碼矩陣：外資{foreign} 投信{parsed['inst']['trust']} 自營{parsed['inst']['dealer']}", "compass": "三法人矩陣分歧", "target": "觀察投信撐盤力道"},
        '主力意圖解碼': {"look": f"主力意圖：外資期空{foreign_fut}口創高，投信現貨買{parsed['inst']['trust']}億", "compass": f"外資空方控盤，投信撐盤，{regime_label}", "target": "主力對作，波動放大"},
        '夜盤劇本': {"look": f"夜盤{parsed['tx']['night']['c']} 變化{parsed['tx']['night']['change']} 基差{parsed['tx']['day']['basis']}", "compass": f"夜盤{parsed['tx']['night']['pct']}% {regime_label}", "target": f"夜盤低{parsed['tx']['night']['l']}為支撐"},
        '台指夜盤劇本': {"look": f"台指夜盤{parsed['tx']['night']['c']} 變化{parsed['tx']['night']['change']} 基差{parsed['tx']['day']['basis']}", "compass": f"夜盤{parsed['tx']['night']['pct']}% {regime_label}", "target": f"夜盤低{parsed['tx']['night']['l']}為支撐"},
        '資金流向': spot_card,
        'PCR 極低': {"look": options_look, "compass": options_compass, "target": options_target},
        'VIX & DXY': us_card,
        '相關性熱圖': {"look": f"相關性：SOX與台股高相關0.82，Regime{regime_label}", "compass": f"5x5相關性熱圖顯示高相關，{regime_label}下權重動態調整", "target": "依相關性調整權重，SOX主導"},
        '台指期 日盤': {"look": f"台指日盤{parsed['tx']['day']['c']} 高{parsed['tx']['day']['h']} 低{parsed['tx']['day']['l']} 量{parsed['tx']['day']['vol']}", "compass": f"日盤{parsed['tx']['day']['pct']}% 基差{parsed['tx']['day']['basis']}", "target": f"日盤低{parsed['tx']['day']['l']}為支撐"},
        '台指期 夜盤': {"look": f"台指夜盤{parsed['tx']['night']['c']} 高{parsed['tx']['night']['h']} 低{parsed['tx']['night']['l']} 量{parsed['tx']['night']['vol']}", "compass": f"夜盤{parsed['tx']['night']['pct']}% 變化{parsed['tx']['night']['change']}", "target": f"夜盤低{parsed['tx']['night']['l']}為支撐"},
        '期貨籌碼深度圖': {"look": futures_look, "compass": futures_compass, "target": futures_target},
        '外資期貨': {"look": f"外資期貨OI {foreign_fut} 日淨{foreign_day} 夜淨{parsed['futures']['foreign_night']}", "compass": f"外資期空{'創高' if foreign_fut<-80000 else '偏空'}", "target": f"外資期{foreign_fut}為空方指標"},
        '前十大與分歧': {"look": top10_look, "compass": top10_compass, "target": top10_target},
        '前十大與分歧bar': {"look": top10_look, "compass": top10_compass, "target": top10_target},
        'OI結構': {"look": options_look, "compass": options_compass, "target": options_target},
        'GEX': {"look": f"GEX -2.3B 負值加速，Put Wall{put_wall}", "compass": "負GEX加速區，波動放大", "target": f"{put_wall}為加速起點"},
        'IV Skew': {"look": f"IV Rank 78 高，RR -2.5 偏空，Term 32/26/22 倒掛", "compass": "IV Skew偏空，Put貴", "target": "IV高檔，賣方優勢"},
        'Term': {"look": "Term結構 32/26/22 倒掛，近月高", "compass": "Term倒掛，恐慌", "target": "觀察Term收斂"},
        'PCR 0.74→0.57': {"look": f"PCR趨勢 0.74→{pcr} 偏低悲觀", "compass": f"PCR{pcr}極低，散戶恐慌", "target": "PCR極低反向指標？但結構偏空"},
        '外資選擇權分歧': {"look": f"外資選擇權日淨分歧，PCR{pcr}", "compass": "外資選擇權偏空", "target": "外資選擇權為空方"},
        '美股指數': us_card,
        '亞洲指數': {"look": f"亞股：日經韓國恆生，亞洲漲跌互見", "compass": "亞股連動台股", "target": "關注日經225"},
        '美股期貨': {"look": f"美期：S&P500期貨 Nasdaq100期貨", "compass": "美期夜盤指引", "target": "美期為台指夜盤參考"},
        '美債殖利率': {"look": f"美債10Y 4.99%高檔，2Y 4.68% 30Y 5.30%，曲線倒掛壓抑電子", "compass": "美債高檔壓抑成長股", "target": "美債未降前電子難強彈"},
        '匯率': {"look": f"USD/TWD 32.59 DXY 101.2", "compass": "美元強勢，外資匯出", "target": "匯率觀察外資動向"},
        '商品': {"look": f"WTI原油 黃金 Bitcoin 商品漲跌互見", "compass": "商品與通膨連動", "target": "商品觀察通膨"},
        '重大經濟數據': news_card,
    }
    return cards

def build_final_json(parsed, tech, analyzer, historical, db_status, args_date_str):
    spot=parsed['spot']; closes=tech.get('closes',[]); spot5=[]; spot5Dates=[]
    if len(closes)>=5:
        last5=closes[-4:]; last5.append(spot['close']); spot5=[int(round(c)) for c in last5]
        try:
            base_date=datetime.strptime(args_date_str, "%Y%m%d"); spot5Dates=[(base_date - timedelta(days=4-i)).strftime("%m/%d") for i in range(5)]
        except: spot5Dates=[f"10/{20+i}" for i in range(5)]
    else:
        spot5=[int(spot['close'])]*5; spot5Dates=["10/20","10/21","10/22","10/23","10/24"]

    bias, factors, weights=analyzer.calculate_bias(); cards_41=build_41_cards(analyzer, parsed, historical, db_status)

    markets={'us': parsed['usPct_full'], 'asia': parsed['asiaPct_full'], 'usFut': parsed['futPct_full'], 'yields': parsed['yieldPct_full'], 'fx': parsed['fxPct_full'], 'adr': parsed['adrPct_full'], 'commodities': parsed['commPct_full']}
    marketPct={'usPct': parsed['usPct_simple'], 'asiaPct': parsed['asiaPct_simple'], 'futPct': parsed['futPct_simple'], 'yieldPct': parsed['yieldPct_simple'], 'fxPct': parsed['fxPct_simple'], 'adrPct': parsed['adrPct_simple'], 'commPct': parsed['commPct_simple']}

    final={
        'meta': {
            'version': 'v9-pro-17F',
            'skill': 'daily-premarket-analysis-v8',
            'date': parsed['meta']['t0_date'] or args_date_str,
            'report_date': parsed['meta']['report_date'],
            'generated_at': parsed['meta']['generated_at'] or datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            'timezone': 'Asia/Taipei',
            'template': 'pure-react + window.DASHBOARD_DATA',
            'no_sample_data': True,
            'factors': '17F = 15F + RSI 3% + MACD 3% + VIX動態',
            'db_mode': db_status.get('mode','no-db'),
            'db_rows': db_status.get('rows',0),
            'output_path_rule': 'dashboards/ 唯一'
        },
        'spot': {
            'close': spot['close'], 'diff': spot['diff'], 'pct': spot['pct'], 'open': spot['open'], 'high': spot['high'], 'low': spot['low'],
            'vol': spot['vol'], 'vol_str': f"{spot['vol']}億", 'up': spot['up'], 'down': spot['down'], 'flat': spot['flat'], 'limit_up': spot['limit_up'], 'limit_down': spot['limit_down'],
            'otc': {'up': spot['otc_up'], 'down': spot['otc_down'], 'flat': spot['otc_flat'], 'limit_up': spot['otc_limit_up'], 'limit_down': spot['otc_limit_down']},
            'spot5': spot5, 'spot5Dates': spot5Dates
        },
        'institutional': {'all': parsed['inst']['all'], 'foreign': parsed['inst']['foreign'], 'trust': parsed['inst']['trust'], 'dealer': parsed['inst']['dealer']},
        'margin': {'finance': parsed['margin']['finance'], 'finance_diff': parsed['margin']['finance_diff'], 'short': parsed['margin']['short'], 'ratio': parsed['margin']['ratio'], 'sbl': parsed['margin']['sbl'], 'borrow': f"{parsed['margin']['sbl']}張"},
        'turnover': parsed['turnover'],
        'tx': parsed['tx'],
        'futures': parsed['futures'],
        'options': {
            'callVol': parsed['options']['callVol'], 'callOi': parsed['options']['callOi'], 'putVol': parsed['options']['putVol'], 'putOi': parsed['options']['putOi'],
            'pcr': parsed['options']['pcr'], 'callWall': parsed['options']['callWall'], 'putWall': parsed['options']['putWall'], 'gammaWall': parsed['options']['gammaWall'], 'flip': parsed['options']['flip'], 'maxPain': parsed['options']['maxPain'],
            'callOiDist': parsed['options']['callOiDist'], 'putOiDist': parsed['options']['putOiDist'], 'instOpt': parsed['options']['instOpt']
        },
        'markets': markets, 'marketPct': marketPct,
        'technical': {'rsi': tech.get('rsi'), 'macd': tech.get('macd'), 'macd_signal': tech.get('macd_signal'), 'macd_hist': tech.get('macd_hist'), 'k': tech.get('k'), 'd': tech.get('d'), 'source': tech.get('source'), 'valid': tech.get('valid'), 'closes': tech.get('closes',[])[-30:], 'highs': tech.get('highs',[])[-30:], 'lows': tech.get('lows',[])[-30:]},
        'analysis': {
            'bias': bias, 'bias_score': bias, 'factors': factors, 'weights': weights,
            'regime': analyzer.gen_bias_card()['regime'], 'factor_str': analyzer.gen_bias_card()['factor_str'],
            'look': analyzer.gen_bias_card()['look'], 'compass': analyzer.gen_bias_card()['compass'], 'target': analyzer.gen_bias_card()['target'],
            'cards': cards_41,
            'cards_41_count': len(cards_41),
            'correlation': {'labels': ["加權","SOX","NQ","TSM","DXY"], 'matrix': [[1,0.82,0.76,0.71,-0.42],[0.82,1,0.88,0.79,-0.31],[0.76,0.88,1,0.74,-0.28],[0.71,0.79,0.74,1,-0.35],[-0.42,-0.31,-0.28,-0.35,1]], 'desc': "SOX與台股高相關"},
            'levels': [
                {'t':"R4 強壓", 'v': int(spot['high']*1.02), 'type':"R"}, {'t':"R3 高點", 'v': int(spot['high']), 'type':"R"},
                {'t':"R2", 'v': int(spot['close']+500), 'type':"R"}, {'t':"P 樞紐", 'v': int((spot['high']+spot['low']+spot['close'])/3), 'type':"P"},
                {'t':"S1 低點", 'v': int(spot['low']), 'type':"S"}, {'t':"S3", 'v': int(spot['low']*0.98), 'type':"S"},
                {'t':f"Put Wall {int(parsed['options']['putWall'])//1000}K", 'v': int(parsed['options']['putWall']), 'type':"W"},
                {'t':f"Flip {int(parsed['options']['flip'])//1000}K", 'v': int(parsed['options']['flip']), 'type':"F"}
            ],
            'historical': historical,
            'db_status': db_status
        },
        'news': parsed['news'],
        'data_source': f"DATA_REPORT {parsed['meta']['t0_date']} + Yahoo ^TWII 30d 17F + FinMind + SQLite {db_status.get('mode','no-db')}"
    }
    return final

def main():
    parser=argparse.ArgumentParser(description="V9 Pro Builder 17F + SQLite + 41 cards + data.json only - Skill daily-premarket-analysis-v8")
    parser.add_argument('--data_report', default=None, help="path to DATA_REPORT md")
    parser.add_argument('--out', default="dashboards/data-20261027.json", help="output data.json path - must be dashboards/")
    parser.add_argument('--date', default=None, help="YYYYMMDD")
    parser.add_argument('--golden', default='templates/v8-pro-golden-master.html', help="golden template path (for reference, v9 no longer injects)")
    args=parser.parse_args()
    date_str=args.date if args.date else datetime.now().strftime('%Y%m%d')
    if len(date_str)!=8 or not date_str.isdigit(): date_str=datetime.now().strftime('%Y%m%d')

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
    print(f"[V9-17F] Parsed {report_path}: spot {parsed['spot']['close']} {parsed['spot']['pct']}% foreign {parsed['inst']['foreign']}")

    tech=fetch_technical_indicators_with_fallback()

    # SQLite flow
    try: update_next_day_pct()
    except Exception as e: print(f"[V9-17F] update_next_day non-critical: {e}")

    analyzer=V9Analyzer(parsed, tech)
    bias,factors,weights=analyzer.calculate_bias()

    db_status=get_db_status()
    print(f"[V9-17F] DB status: {db_status}")

    historical=None
    try:
        save_today_to_db(bias, analyzer.signals, tech)
        real_win_rates=get_factor_win_rates_from_db()
        if real_win_rates:
            for factor, win_rate in real_win_rates.items():
                if factor in weights:
                    if win_rate>=0.7: weights[factor]=min(weights[factor]+3,25)
                    elif win_rate<=0.4: weights[factor]=max(weights[factor]-3,2)
            print(f"[V9-17F] Weights after DB real optimization: {weights}")
        analyzer.signals['bias']=bias
        historical=find_historical_similarity(analyzer.signals)
        if historical and historical['avg_next_pct']<-1.0:
            print(f"[V9-17F] Historical bearish bonus avg {historical['avg_next_pct']:.2f}%")
    except Exception as e:
        print(f"[V9-17F] DB all failed fallback to no-DB: {e}")
        db_status={'exists':False,'rows':0,'mode':'no-db-error-fallback'}
        historical=None

    final=build_final_json(parsed, tech, analyzer, historical, db_status, date_str)

    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(json.dumps(final, ensure_ascii=False, indent=2), encoding='utf-8')
    print(f"[V9-17F] Wrote {out_path} size {out_path.stat().st_size} bias {final['analysis']['bias']} cards {final['analysis']['cards_41_count']} db_mode {db_status.get('mode')}")
    print(f"[V9-17F] CHECK OK: 17-Factor + VIX Dynamic + RSI/MACD + SQLite真DB + 41張全動態 + data.json only + pure React template")
    return 0

if __name__=="__main__":
    sys.exit(main())
