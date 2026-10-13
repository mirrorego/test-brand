#!/usr/bin/env python3
"""Quick MHP brand lint for HTML / CSS / SVG / JSX / TSX / MD output.
  lint_brand.py FILE [FILE...]
Flags hard-block violations (off-palette colors, MHP Blue outside the logo, wrong
fonts, non-45deg or Kiwi/Mint gradients, tiny text, '->' arrows). It is a safety net,
not a substitute for reading the rules — warnings need human judgment.
"""
import re, sys, pathlib

TOKENS = {h.upper() for h in """
000099 595959 F9FEE8 F0FFC2 E6FF88 DEFF43 E2FF10 DDEF03 CCCC00 B3B300 949400 6B6B00 4D4D00
EEFFF5 D7FFEA B2FFD7 76FFBA 33F594 09DE74 00CC67 04914C 0A713F 0A5D36 00341C
F0F3FF E4E9FF CDD6FF A5B2FF 7280FF 3A43FF 1612FF 0101FF 0000CC 0202B0 000778 00055B
FFFFFF F6F6F6 E7E7E7 D1D1D1 B0B0B0 888888 6D6D6D 575757 4F4F4F 454545 3D3D3D 262626 000000
FCE8E8 E32626 710F0F FFF1DB FFA10A 7A4B00""".split()}
BAD_FONTS = ["frutiger", "orbitron", "arial", "helvetica", "inter", "roboto", "times", "georgia",
             "open sans", "calibri", "system-ui", "-apple-system", "comic"]

def short(h):  # expand #abc -> AABBCC ; drop alpha from 8-digit
    h = h.lstrip("#").upper()
    if len(h) in (3, 4): h = "".join(c * 2 for c in h)
    return h[:6]

def lint(path):
    t = pathlib.Path(path).read_text(errors="ignore"); out = []
    ln = lambda m: t.count("\n", 0, m.start()) + 1
    for m in re.finditer(r"#[0-9A-Fa-f]{8}\b|#[0-9A-Fa-f]{6}\b|#[0-9A-Fa-f]{3,4}\b", t):
        h = short(m.group())
        if h not in TOKENS:
            out.append((ln(m), "COLOR", f"{m.group()} is not an MHP token"))
        elif h == "000099":
            out.append((ln(m), "COLOR", "MHP Blue #000099 is polychrome-logo-only — use #1612FF or #00055B"))
    for m in re.finditer(r"font-family\s*:\s*([^;}\n]+)", t, re.I):
        fam = m.group(1).lower()
        if "segoe ui" not in fam:
            out.append((ln(m), "FONT", f"font-family lacks Segoe UI: {m.group(1).strip()}"))
        elif any(b in fam.split("segoe ui")[0] for b in BAD_FONTS):
            out.append((ln(m), "FONT", f"off-brand font listed before Segoe UI: {m.group(1).strip()}"))
        if any(b in fam for b in ("frutiger", "orbitron")):
            out.append((ln(m), "FONT", "Frutiger/Orbitron are not allowed in internal tools"))
    for m in re.finditer(r"(linear|radial|conic)-gradient\(([^;]*)", t, re.I):
        body = m.group(0)
        if m.group(1).lower() != "linear":
            out.append((ln(m), "GRADIENT", "only 45° linear gradients are allowed"))
        elif not re.search(r"\b45deg\b|\b225deg\b", body):
            out.append((ln(m), "GRADIENT", "gradient angle must be exactly 45° (or reverse, 225°)"))
        if re.search(r"DDEF03|00CC67|E2FF10|09DE74", body, re.I):
            out.append((ln(m), "GRADIENT", "Kinetic Kiwi / Sprout Mint may never appear in a gradient"))
    for m in re.finditer(r"font-size\s*:\s*(\d+(?:\.\d+)?)(px|pt)", t, re.I):
        v, u = float(m.group(1)), m.group(2).lower()
        if (u == "pt" and v < 9) or (u == "px" and v < 12):
            out.append((ln(m), "TYPE", f"font-size {v:g}{u} is below the 9pt floor (12px Caption is the smallest scale step)"))
    for m in re.finditer(r"(?<![\w-])->(?![\w-])", t):
        out.append((ln(m), "TYPE", 'use "→", never "->" (ignore if inside code)'))
    for m in re.finditer(r"background(?:-color)?\s*:\s*#DDEF03", t, re.I):
        out.append((ln(m), "CHECK", "Kinetic Kiwi fill on a light surface needs an Almost Black (#262626) stroke; text on it must be #262626; never a full-section background"))
    for m in re.finditer(r"rotate\([^)]*\)", t):
        out.append((ln(m), "CHECK", "rotation found — logo/Slash/icons must never be rotated"))
    return sorted(out)

if __name__ == "__main__":
    if len(sys.argv) < 2: sys.exit(__doc__)
    bad = 0
    for f in sys.argv[1:]:
        for line, kind, msg in lint(f):
            print(f"{f}:{line}: [{kind}] {msg}"); bad += 1
    print(f"{bad} issue(s)" if bad else "clean — no lint issues found")
    sys.exit(1 if bad else 0)
