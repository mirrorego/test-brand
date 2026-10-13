# MHP Brand Design System — Colors

Reference file for generating on-brand code, layouts, and assets. Rules below are constraints, not suggestions (unless specified as flexible) — treat "Forbidden" as hard blocks in generated output.

---

## Color Tokens

| Group | Token | Hex |
|---|---|---|
| Brand | MHP Blue | #000099 |
| Brand | Grey | #595959 |
| Kinetic Kiwi | 50 | #F9FEE8 |
| Kinetic Kiwi | 100 | #F0FFC2 |
| Kinetic Kiwi | 200 | #E6FF88 |
| Kinetic Kiwi | 300 | #DEFF43 |
| Kinetic Kiwi | 400 | #E2FF10 |
| Kinetic Kiwi | Highlight | #DDEF03 |
| Kinetic Kiwi | 600 | #CCCC00 |
| Kinetic Kiwi | 700 | #B3B300 |
| Kinetic Kiwi | 800 | #949400 |
| Kinetic Kiwi | 900 | #6B6B00 |
| Kinetic Kiwi | 950 | #4D4D00 |
| Sprout Mint | 50 | #EEFFF5 |
| Sprout Mint | 100 | #D7FFEA |
| Sprout Mint | 200 | #B2FFD7 |
| Sprout Mint | 300 | #76FFBA |
| Sprout Mint | 400 | #33F594 |
| Sprout Mint | 500 | #09DE74 |
| Sprout Mint | Secondary | #00CC67 |
| Sprout Mint | 700 | #04914C |
| Sprout Mint | 800 | #0A713F |
| Sprout Mint | 900 | #0A5D36 |
| Sprout Mint | 950 | #00341C |
| Vital Trust | Zircon Lightest 50 | #F0F3FF |
| Vital Trust | Zircon Light 100 | #E4E9FF |
| Vital Trust | Zircon 200 | #CDD6FF |
| Vital Trust | 300 | #A5B2FF |
| Vital Trust | 400 | #7280FF |
| Vital Trust | 500 | #3A43FF |
| Vital Trust | Primary | #1612FF |
| Vital Trust | 700 | #0101FF |
| Vital Trust | 800 | #0000CC |
| Vital Trust | 900 | #0202B0 |
| Vital Trust | 950 | #000778 |
| Vital Trust | Darkest Blue | #00055B |
| Neutral | White | #FFFFFF |
| Neutral | 50 / Almost White | #F6F6F6 |
| Neutral | 100 | #E7E7E7 |
| Neutral | 200 | #D1D1D1 |
| Neutral | 300 | #B0B0B0 |
| Neutral | 400 | #888888 |
| Neutral | 500 | #6D6D6D |
| Neutral | 600 / Balanced Neutral | #575757 |
| Neutral | 700 | #4F4F4F |
| Neutral | 800 | #454545 |
| Neutral | 900 | #3D3D3D |
| Neutral | 950 / Almost Black | #262626 |
| Neutral | Black | #000000 |

---

## Color Proportions

Flexible guideline, not a fixed rule — vary from light/content-focused to full-color layouts.

| Color | Hex | Proportion |
|---|---|---|
| Darkest Blue | #00055B | 25% |
| Vital Trust | #1612FF | 25% |
| Zircon Lightest | #F0F3FF | 37% |
| Kinetic Kiwi | #DDEF03 | 5% |
| White | #FFFFFF | 4% |
| Almost Black | #262626 | 4% |

- Darkest Blue + Vital Trust + Zircon Lightest together ≈ 87% of layout color usage.
- **Light visual:** dominant fill = Zircon Lightest.
- **Full-color visual:** dominant fill = Vital Trust + Vital Trust.

---

## Color Usage Rules

### MHP Blue
- **Allowed:** only within the polychrome (full-color) version of the MHP logo.
- **Forbidden:** general UI, layout, text, background, or accent use anywhere else. For any deep-blue need outside the polychrome logo — accents, backgrounds, buttons, headings — use **Vital Trust #1612FF** or **Darkest Blue #00055B** instead.
- This token remains in the Color Tokens table above for reference (logo fidelity), but should not be reached for as a general brand color.

### Sprout Mint
- **Allowed:** Only used for green/sustainability themes or positive outcome as pill, button or text. Used in the same proportions as Kinetic Kiwi.
- **Forbidden:** as a full-screen/full-section background

### Kinetic Kiwi
- **Forbidden:** as a full-screen/full-section background
- **Allowed:** as a fill color for contained elements (cards, badges, tags, etc.)
- Text on top of a Kinetic Kiwi fill must be Almost Black
- **On light backgrounds:** Kinetic Kiwi elements must always have an Almost Black stroke

---

## Approved Accessibility Pairings

Only combinations below are approved — do not mix outside this table. Ratios are calculated per the WCAG 2.x contrast formula (relative luminance of each color, `(L_lighter + 0.05) / (L_darker + 0.05)`), matching the method in [The A11Y Project's checklist](https://www.a11yproject.com/checklist/#color-contrast). Every pairing here clears the strictest threshold (normal text, 4.5:1) with margin.

> Note: only the main Vital Trust ↔ Darkest Blue gradient is listed here for text pairing — both ends are dark enough for reliable White-text contrast. MHP Blue is excluded from this table — see Color Usage Rules above (logo-only, not for general accessibility pairings).

| Text / Element | Background | Contrast Ratio |
|---|---|---|
| White #FFFFFF | Vital Trust #1612FF | 8.19:1 |
| White #FFFFFF | Darkest Blue #00055B | 17.91:1 |
| White #FFFFFF | Gradient: Vital Trust → Darkest Blue (main) | 8.19:1 – 17.91:1 across the gradient |
| Zircon Lightest #F0F3FF | Vital Trust #1612FF | 7.40:1 |
| Zircon Lightest #F0F3FF | Darkest Blue #00055B | 16.17:1 |
| Almost Black #262626 | Zircon #CDD6FF | 10.56:1 |
| Almost Black #262626 | Zircon Light #E4E9FF | 12.54:1 |
| Almost Black #262626 | Zircon Lightest #F0F3FF | 13.67:1 |
| Almost Black #262626 | Sprout Mint #00CC67 | 7.09:1 |
| Almost Black #262626 | Kinetic Kiwi #DDEF03 | 11.83:1 |
| Vital Trust #1612FF | Zircon Lightest #F0F3FF | 7.40:1 |

### WCAG Contrast Thresholds (reference)

Source: [The A11Y Project Checklist — Color Contrast](https://www.a11yproject.com/checklist/#color-contrast), based on [WCAG 2.x Success Criterion 1.4.3 and 1.4.11](https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html).

| Content type | Minimum ratio (AA) |
|---|---|
| Normal-sized text | 4.5:1 |
| Large text (≥18pt, or ≥14pt bold) | 3:1 |
| Icons and meaningful graphics | 3:1 |
| UI component borders (inputs, toggles, etc.) | 3:1 |

**Rules:**
- Any text/background combination not in the Approved Pairings table above must be checked against these ratios before use — don't assume a brand-adjacent color is safe.
- Color is never the sole way to convey information (status, errors, links) — pair with an icon, label, or pattern. This applies to alert colors in particular (see Alerts section below).
- Placing text over photography or the abstract/imagery backgrounds in `slash-system.md` requires an extra contrast check on a case-by-case basis — busy or midtone images can drop effective contrast below these thresholds even when the nominal text color would pass against a flat background.

---

## Alerts (Semantic Colors)

Alert colors signal system feedback: green = success, red = error, orange = warning. Use consistently; keep contrast high, especially for error/warning text.

- **Forbidden:** mixing alert colors with brand colors. These are functional, not decorative — don't reach for them outside actual status feedback (form validation, toasts, banners, status badges).

| Status | Light Tint | Base | Dark Tint |
|---|---|---|---|
| Success | #EEFFF5 (SLT) | #00CC67 (SL) | #0A5D36 (SDT) |
| Error | #FCE8E8 (ELT) | #E32626 (EL) | #710F0F (EDT) |
| Warning | #FFF1DB (WLT) | #FFA10A (WL) | #7A4B00 (WDT) |

> Note: Success base (#00CC67) is the same hex as Sprout Mint/Secondary. When used as a **status color**, it follows the Alerts rules (fine on buttons/badges for success states). When used as a **brand color**, it follows the Sprout Mint rules above (forbidden on buttons/pills/CTAs). Context determines which rule applies — a green "Saved successfully" toast is Alerts; a green CTA button is brand, and forbidden.

---

## Gradients

- **Angle:** exactly 45°, diagonal, bottom-left → top-right (or reverse). No 0°/90°/180°, no radial, angular, or multi-color/highlight gradients.
- **Forbidden:** Sprout Mint and Kinetic Kiwi may never appear in a gradient.

| Gradient | From | To |
|---|---|---|
| Recommended 1 (main) | Vital Trust #1612FF | Darkest Blue #00055B |

---

**Note:** There is an unresolved conflict in the source document — the Sprout Mint rule forbids its use on pills/CTAs, but the Pills component table (not part of this color extract) lists an "Alternative Pill" in Sprout Mint for sustainability contexts. This needs to be resolved before shipping.

---

**Contact:** Brand questions: brand@mhp.com