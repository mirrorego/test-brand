#!/usr/bin/env python3
"""MHP icon helper — find, size, and (palette-restricted) recolor icons from the
approved library in assets/icons/.  Never draw or modify icon geometry by hand.

  icons.py categories
  icons.py list [category]                  # names, optionally for one category
  icons.py get NAME [--size 60] [--color "#1612FF"] [--out file.svg]
  icons.py stroke SIZE                      # print the brand stroke weight for a size

Icons have no semantic names (e.g. stroke_ico_AI_2) — pick them by LOOKING at the
contact sheets in assets/icon-sheets/<category>-<n>.png, then fetch with `get`.

Stroke weight follows MHP-Stroke-Radius-Effects.md:  60px→2, 120px→3, 160px→3.5,
linearly interpolated between points (extrapolated outside, never below 1).
Rule: every icon of the same rendered size in one composition gets the same weight.
Note: the brand file says "pt"; Figma-style units treat these as px, so we do too.
"""
import argparse, pathlib, re, sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
ICONS = ROOT / "assets" / "icons"

# Brand colors an icon may legitimately take (default is Almost Black).
ALLOWED = {
    "#262626": "Almost Black (default)", "#FFFFFF": "White (on dark/Vital Trust/Darkest Blue)",
    "#1612FF": "Vital Trust", "#00055B": "Darkest Blue", "#595959": "Brand Grey",
    "#DDEF03": "Kinetic Kiwi (needs Almost Black stroke on light bg — use sparingly)",
    "#00CC67": "Sprout Mint (green/sustainability/positive only)",
}
PTS = [(60, 2.0), (120, 3.0), (160, 3.5)]

def stroke_for(size: float) -> float:
    if size <= PTS[0][0]:
        (x0, y0), (x1, y1) = PTS[0], PTS[1]
    elif size >= PTS[-1][0]:
        (x0, y0), (x1, y1) = PTS[-2], PTS[-1]
    else:
        for (x0, y0), (x1, y1) in zip(PTS, PTS[1:]):
            if x0 <= size <= x1:
                break
    return max(1.0, y0 + (y1 - y0) * (size - x0) / (x1 - x0))

def find(name: str) -> pathlib.Path:
    hits = list(ICONS.rglob(f"{name}.svg"))
    if not hits:
        hits = [p for p in ICONS.rglob("*.svg") if name.lower() in p.stem.lower()]
    if len(hits) != 1:
        sys.exit(f"Icon '{name}' not found uniquely: {[h.stem for h in hits][:10]}")
    return hits[0]

def render(path: pathlib.Path, size: float, color: str) -> str:
    svg = path.read_text()
    vb = [float(v) for v in re.search(r'viewBox="([^"]+)"', svg).group(1).split()]
    scale = size / max(vb[2], vb[3])
    w, h = round(vb[2] * scale, 2), round(vb[3] * scale, 2)
    sw = round(stroke_for(size) / scale, 4)            # stroke in viewBox units
    svg = re.sub(r'width="[\d.]+" height="[\d.]+"', f'width="{w:g}" height="{h:g}"', svg, count=1)
    svg = re.sub(r'\sstroke-width="[^"]*"', "", svg)    # drop per-path overrides
    svg = re.sub(r'stroke="#262626"', f'stroke="{color}" stroke-width="{sw:g}"', svg)
    svg = re.sub(r'fill="#262626"', f'fill="{color}"', svg)
    return svg

def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    sub.add_parser("categories")
    l = sub.add_parser("list"); l.add_argument("category", nargs="?")
    g = sub.add_parser("get"); g.add_argument("name")
    g.add_argument("--size", type=float, default=64); g.add_argument("--color", default="#262626")
    g.add_argument("--out")
    s = sub.add_parser("stroke"); s.add_argument("size", type=float)
    a = ap.parse_args()

    if a.cmd == "categories":
        for d in sorted(p for p in ICONS.iterdir() if p.is_dir()):
            print(f"{d.name}\t{len(list(d.glob('*.svg')))} icons")
    elif a.cmd == "list":
        base = ICONS / a.category if a.category else ICONS
        for p in sorted(base.rglob("*.svg")):
            print(p.stem)
    elif a.cmd == "stroke":
        print(f"{stroke_for(a.size):g}")
    else:
        col = a.color.upper()
        if col not in ALLOWED:
            sys.exit(f"{col} is not an approved icon color. Allowed: " + ", ".join(f"{k} ({v})" for k, v in ALLOWED.items()))
        if a.size < 60 or a.size > 160:
            print(f"note: {a.size:g}px is outside the brand's defined 60–160px stroke range; weight extrapolated.", file=sys.stderr)
        out = render(find(a.name), a.size, col)
        if a.out: pathlib.Path(a.out).write_text(out); print(f"wrote {a.out}")
        else: print(out)

if __name__ == "__main__":
    main()
