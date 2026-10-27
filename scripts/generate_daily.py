#!/usr/bin/env python3
"""
V7 Pro - 最保險版：只複製金版，絕不解析 he
- 不做任何 regex 解析 he，避免把檔案弄壞
- 只替換 date:"xxxx-xx-xx" 第一處
- 無任何 /mnt/data 硬編碼
"""
import pathlib, re, hashlib
from datetime import datetime
import argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--date', nargs='?', default=None)
    parser.add_argument('--golden', default='templates/v7-pro-golden-master.html')
    args = parser.parse_args()
    
    date_str = args.date if args.date else datetime.now().strftime('%Y%m%d')
    if len(date_str) != 8 or not date_str.isdigit():
        date_str = datetime.now().strftime('%Y%m%d')
    date_dash = f"{date_str[:4]}-{date_str[4:6]}-{date_str[6:]}"
    
    gm_path = pathlib.Path(args.golden)
    if not gm_path.exists():
        gm_path = pathlib.Path("templates/v7-pro-golden-master.html")
    if not gm_path.exists():
        print(f"ERROR: golden not found {args.golden}")
        return 1
    
    content = gm_path.read_text(encoding='utf-8', errors='ignore')
    print(f"Golden size {len(content)} hash {hashlib.sha256(content.encode()).hexdigest()[:12]}")
    
    if 'he=' not in content:
        print("ERROR: golden has no he= , file is broken! Aborting, not overwriting")
        return 1
    
    # 只換第一個 date:"...."
    if 'date:"' in content:
        content_new = re.sub(r'date:"[^"]+"', f'date:"{date_dash}"', content, count=1)
        print(f"Replaced date -> {date_dash}")
    else:
        content_new = content
        print("No date: found, keeping original")
    
    # 輸出到兩個目錄
    for out_dir in ["dashboard", "dashboards"]:
        out_path = pathlib.Path(f"{out_dir}/taifex-{date_str}.html")
        out_path.parent.mkdir(parents=True, exist_ok=True)
        out_path.write_text(content_new, encoding='utf-8')
        print(f"Wrote {out_path} size {len(content_new)}")
    
    # 檢查輸出是否還包含 he
    if 'he=' in content_new and 'bias-gauge' in content_new:
        print("CHECK OK: output still has he and canvas")
    else:
        print("CHECK FAIL: output lost he!")
        return 1
    
    return 0

if __name__ == "__main__":
    exit(main())
