#!/usr/bin/env python3
"""One-off build script: split MHP_Icon_Library.md into per-icon SVG files.
Usage: extract_icons.py <MHP_Icon_Library.md> <out_dir>
"""
import re, sys, pathlib

src, out = pathlib.Path(sys.argv[1]), pathlib.Path(sys.argv[2])
text = src.read_text(encoding="utf-8")
cat_re = re.compile(r"^## \d+\. (.+)$", re.M)
icon_re = re.compile(r"^### (\S+)\s*\n+```svg\n(.*?)\n```", re.M | re.S)

def slug(s):
    return re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-")

cats = [(m.start(), m.group(1).strip()) for m in cat_re.finditer(text)]
n = 0
for m in icon_re.finditer(text):
    cat = [c for pos, c in cats if pos < m.start()][-1]
    d = out / slug(cat)
    d.mkdir(parents=True, exist_ok=True)
    (d / f"{m.group(1)}.svg").write_text(m.group(2).strip() + "\n", encoding="utf-8")
    n += 1
print(f"wrote {n} icons")
