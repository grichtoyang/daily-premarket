import argparse, re, pathlib, hashlib
from datetime import datetime
import urllib.request
import json

def fetch_text(url):
    print(f"Fetching {url}")
    with urllib.request.urlopen(url) as r:
        return r.read().decode('utf-8', errors='ignore')

def parse_data_report(md_text):
    """解析 DATA_REPORT_*.md，提取關鍵數據"""
    data = {}
    # 簡易正則解析 - 依你的 DATA_REPORT 格式調整
    m = re.search(r'加權\s*([0-9,\.]+)', md_text)
    if m:
        data['close'] = float(m.group(1).replace(',',''))
    m = re.search(r'外資\s*([+-]?[0-9\.]+)億', md_text)
    if m:
        data['foreign'] = float(m.group(1))
    # ... 可擴充
    return data

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--date', default=datetime.now().strftime('%Y%m%d'))
    args = parser.parse_args()
    date_str = args.date
    date_dash = f"{date_str[:4]}-{date_str[4:6]}-{date_str[6:]}"

    gm_path = pathlib.Path("templates/v7-pro-golden-master.html")
    if not gm_path.exists():
        gm_url = "https://raw.githubusercontent.com/grichtoyang/daily-premarket/main/templates/v7-pro-golden-master.html"
        content = fetch_text(gm_url)
        gm_path.parent.mkdir(parents=True, exist_ok=True)
        gm_path.write_text(content, encoding='utf-8')
    else:
        content = gm_path.read_text(encoding='utf-8')

    h = hashlib.sha256(content.encode('utf-8')).hexdigest()[:12]
    print(f"Golden Master hash {h} expected e6cf29a748b0 match {h=='e6cf29a748b0'}")

    report_url = f"https://grichtoyang.github.io/daily-premarket/data_reports/DATA_REPORT_{date_str}.md"
    try:
        report = fetch_text(report_url)
        parsed = parse_data_report(report)
        # 替換 he 物件中的 date 和其他欄位
        content = re.sub(r'date:"2026-10-24"', f'date:"{date_dash}"', content)
        if 'close' in parsed:
            # 替換加權顯示
            content = re.sub(r'加權[0-9,]+', f"加權{parsed['close']:.0f}", content)
    except Exception as e:
        print(f"Report fetch failed {e}, 使用原數據")

    # 確保圖表異常修復存在
    if 'requestAnimationFrame' not in content:
        old = 'function B(e){let n=e.getBoundingClientRect();if(n.width===0||n.height===0)return'
        new = """function B(e){
  let n=e.getBoundingClientRect();
  if(n.width===0||n.height===0){
    requestAnimationFrame(()=>{
      let nn=e.getBoundingClientRect();
      if(nn.width>0 && window.__P && window.__P[e.id]) window.__P[e.id](e);
    });
    return null;
  }"""
        content = content.replace(old, new)

    out_dir = pathlib.Path("dashboard")
    out_dir.mkdir(exist_ok=True)
    # 確保有 .gitkeep
    (out_dir / ".gitkeep").touch(exist_ok=True)
    out_path = out_dir / f"taifex-{date_str}.html"
    out_path.write_text(content, encoding='utf-8')
    print(f"Generated {out_path} size {len(content)}")

if __name__ == "__main__":
    main()
