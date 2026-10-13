#!/usr/bin/env python3
"""WCAG 2.x contrast check + MHP approved-pairing lookup.
  contrast.py FG BG          e.g.  contrast.py "#FFFFFF" "#1612FF"
Reports the ratio, whether the pair is on MHP's Approved Accessibility Pairings
list (the only text/background combos the brand allows), and WCAG AA verdicts.
"""
import sys

APPROVED = {  # (text/element, background)
    ("#FFFFFF", "#1612FF"), ("#FFFFFF", "#00055B"),
    ("#F0F3FF", "#1612FF"), ("#F0F3FF", "#00055B"),
    ("#262626", "#CDD6FF"), ("#262626", "#E4E9FF"), ("#262626", "#F0F3FF"),
    ("#262626", "#00CC67"), ("#262626", "#DDEF03"),
    ("#1612FF", "#F0F3FF"),
}
def lum(h):
    h = h.lstrip("#"); r, g, b = (int(h[i:i+2], 16) / 255 for i in (0, 2, 4))
    f = lambda c: c / 12.92 if c <= 0.03928 else ((c + 0.055) / 1.055) ** 2.4
    return 0.2126 * f(r) + 0.7152 * f(g) + 0.0722 * f(b)
def ratio(a, b):
    la, lb = sorted((lum(a), lum(b)), reverse=True)
    return (la + 0.05) / (lb + 0.05)

if __name__ == "__main__":
    if len(sys.argv) != 3: sys.exit(__doc__)
    fg, bg = (c.upper() if c.startswith("#") else "#" + c.upper() for c in sys.argv[1:])
    r = ratio(fg, bg)
    print(f"{fg} on {bg}: {r:.2f}:1")
    print("MHP approved pairing:", "YES" if (fg, bg) in APPROVED else "NO — not on the approved list; do not use for text")
    print(f"WCAG AA normal text (4.5): {'pass' if r >= 4.5 else 'FAIL'} | large text/icons/UI borders (3.0): {'pass' if r >= 3 else 'FAIL'}")
