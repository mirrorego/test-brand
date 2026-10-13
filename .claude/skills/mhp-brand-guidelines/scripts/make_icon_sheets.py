#!/usr/bin/env python3
"""Build-time script: render visual contact sheets (PNG) of the icon library,
one or more per category, so icons can be picked by *looking* at them
(icon file names are only category + number, not semantic).
Usage: make_icon_sheets.py <icons_dir> <out_dir>
"""
import sys, pathlib, re
from playwright.sync_api import sync_playwright

icons_dir, out_dir = pathlib.Path(sys.argv[1]), pathlib.Path(sys.argv[2])
out_dir.mkdir(parents=True, exist_ok=True)
PER_SHEET, COLS = 60, 10

def natural(p):
    return [int(t) if t.isdigit() else t for t in re.split(r"(\d+)", p.stem)]

def cell(svg_path):
    svg = svg_path.read_text()
    svg = re.sub(r'width="\d+" height="\d+"', 'width="72" height="72"', svg, count=1)
    label = svg_path.stem.replace("stroke_stroke_ico_", "").replace("stroke_ico_", "")
    return f'<div class="c">{svg}<span>{label}</span></div>'

with sync_playwright() as p:
    b = p.chromium.launch()
    page = b.new_page(viewport={"width": 1100, "height": 100})
    for cat in sorted(d for d in icons_dir.iterdir() if d.is_dir()):
        files = sorted(cat.glob("*.svg"), key=natural)
        for i in range(0, len(files), PER_SHEET):
            chunk = files[i:i + PER_SHEET]
            html = f"""<html><body style="margin:0;padding:16px;background:#fff;font-family:Segoe UI,Arial,sans-serif">
<style>.g{{display:grid;grid-template-columns:repeat({COLS},1fr);gap:8px}}
.c{{display:flex;flex-direction:column;align-items:center;padding:8px 2px;border:1px solid #E7E7E7;border-radius:8px}}
.c span{{font-size:10px;color:#575757;margin-top:6px;text-align:center;word-break:break-all}}</style>
<div style="font-size:14px;font-weight:700;margin-bottom:8px">{cat.name} — icons {i+1}–{i+len(chunk)} of {len(files)}</div>
<div class="g">{''.join(cell(f) for f in chunk)}</div></body></html>"""
            page.set_content(html)
            sheet = i // PER_SHEET + 1
            page.screenshot(path=str(out_dir / f"{cat.name}-{sheet}.png"), full_page=True)
    b.close()
print("done")
