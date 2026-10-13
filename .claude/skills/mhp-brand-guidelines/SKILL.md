---
name: mhp-brand-guidelines
description: Apply the MHP (A Porsche Company) brand design system to anything visual or written for internal use — dashboards, HR/helpline tools, internal web pages, HTML/React/CSS components, slides, Word reports, infographics, charts, social-style graphics, and copy. Provides color tokens, Segoe UI type scale, spacing/radius/stroke/shadow tokens, pills, the official logo and Slash SVGs, the 920-icon approved icon library, document rules, and English/German language rules. Use this skill whenever the user mentions MHP, MHP branding, "on-brand", the Slash, Vital Trust, Kinetic Kiwi, Darkest Blue, Zircon, Sprout Mint, MHP icons, or asks for a UI, page, deck, report, chart, or asset that should look like MHP — even if they don't say "brand guidelines".
---

# MHP Brand Design System

Generates on-brand output for MHP (A Porsche Company). The brand is strict: the rules exist so that every internal artifact looks unmistakably MHP, and several are hard blocks. Read the relevant references before generating — don't work from memory of how "a blue corporate brand" usually looks.

**Scope: internal tools only** (employee-facing dashboards, HR/helpline utilities, internal reference pages, internal documents). Typeface is **Segoe UI**, with **Noto Sans** as the main fallback and **Arial** as the second fallback when Segoe UI isn't available (CSS stack in `typography.md`). Never use Frutiger (external/agency only) or Orbitron (Digital Product names only). If the user is clearly asking for external/public/agency material, say these guidelines don't cover it and ask how to proceed.

## Workflow

1. **Classify the task**, then load only the references it needs (table below). Tasks usually touch several — e.g. a dashboard card needs colors + typography + spacing + stroke-radius + components.
2. **Build using tokens, not eyeballed values.** Use exact hexes, the type scale, spacing and radius tokens from the references.
3. **Use official assets, never redraw them**: logo → `assets/mhp-logo-*.svg`; Slash → `assets/mhp-slash-*.svg`; icons → `scripts/icons.py` (below).
4. **Verify before delivering**: run `scripts/lint_brand.py` on any HTML/CSS/SVG/JSX you produced, and `scripts/contrast.py` for any text/background pair you're unsure of. Fix every COLOR/FONT/GRADIENT/TYPE hit; `[CHECK]` items are reminders — confirm the condition is met (e.g. the Kiwi element really has its Almost Black stroke) and move on. Then walk the checklist at the bottom.
5. **When a rule is silent or conflicting, pick the most conservative on-brand option and tell the user about the gap** instead of guessing silently.

## Which reference to load

| Task involves… | Read |
|---|---|
| Any color, background, text/background pairing, alerts, gradients | `references/colors.md` |
| Any text-bearing layout: headings, body, type sizes | `references/typography.md` |
| Layout grid, margins, padding | `references/spacing-layout.md` |
| Borders, corner radius (incl. nested containers), shadows, blur | `references/stroke-radius-effects.md` |
| Logo, pills/buttons/tags, icon rules | `references/components.md` |
| Slash — hero visuals, slides, social, publications, web banners, images | `references/slash-system.md` |
| Word docs, reports, infographics, charts | `references/document-guidelines.md` (narrower palette than the full set — it wins for those formats) |
| Copywriting, titles, German text, localization | `references/language-localization.md` |

## Hard blocks (memorize these; the references have the detail)

**Color**
- **MHP Blue #000099 is logo-only** (polychrome logo). For any other deep blue use **Vital Trust #1612FF** or **Darkest Blue #00055B**.
- **Kinetic Kiwi** and **Sprout Mint**: never a full-screen/full-section background, never in a gradient. Kiwi is for contained elements (cards, badges, tags), text on it is Almost Black, and on light backgrounds Kiwi elements need an Almost Black stroke. Mint is only for green/sustainability/positive-outcome themes.
- **Gradients**: exactly 45° diagonal, linear, Vital Trust #1612FF ↔ Darkest Blue #00055B only.
- **Text/background pairs must come from the Approved Accessibility Pairings** in `colors.md`. Anything else needs a contrast check (`scripts/contrast.py`) and, for brand text, shouldn't be used.
- Alert colors (green/red/orange) are functional status feedback only — never decorative, never mixed with brand colors. Color is never the only carrier of meaning; add an icon or label.

**Typography**
- Segoe UI, falling back to Noto Sans, then Arial. Minimum 9pt anywhere. ~3 font sizes max per document. No justified text in multi-column layouts. No double spaces. Arrows typeset as "→", never "->". One language per document.

**Logo**
- Placement top-right or center-top only. Never bottom-anything. Clear space ≥ 100% of the figurative mark's height on all sides. Never flip, rotate, recolor outside the three variants, stretch, drop the "A Porsche Company" descriptor, or use it inside a sentence. Variants: Vital Trust (light/Zircon/White bg), White (dark/colored bg), Almost Black (special).

**Slash**
- One Slash per composition, exactly 10°, sharp corners, never rotated/cropped/cut/deformed, never at the format edge, never with numbers, never combined with arrows or arrow-like graphics, never on abstract brand imagery. Its color depends on the background (table in `slash-system.md`) — it's not a flat default. It must be the focal point; pills may coexist but must not compete.

**Pills / buttons**
- Always fully rounded ends. One Main Pill (Kiwi, Almost Black text) per surface — **on light surfaces it also needs an Almost Black stroke** (e.g. `border: 2px solid #262626`), as does any Kiwi card/badge/tag on a light background. Secondary/Tertiary flip treatment on dark vs. light surfaces. Functional only — never decorative.

**Icons**
- Only icons from the library. No custom, third-party, or self-drawn icons. If a container is needed, use a circle. Stroke weight scales with size (see tool below).

## Using the logo and Slash

Copy straight from `assets/` into the output (inline the SVG, or reference the file). The Slash is a tall shape (497×900): size it by **height** to fit the layout (Hero ≈ card/headline block height or more, Accent/Micro smaller per `slash-system.md`) and keep it fully inside the frame with the protective clear space — never bleeding off an edge. Available: `mhp-logo-{vital-trust,white,almost-black}.svg`, `mhp-slash-{vital-trust,darkest-blue,white}.svg`. Pick the logo variant by background; pick the Slash color from the background table in `references/slash-system.md`. Scale proportionally only.

## Using icons

The library has 920 icons in 18 categories under `assets/icons/<category>/`. File names are only category + number (e.g. `stroke_ico_safety_medical_8`), so **you can't pick by name — pick by looking**:

1. Run `python scripts/icons.py categories` to see categories, then **view the relevant contact sheet(s)** in `assets/icon-sheets/` (e.g. `safety-medical-1.png`, `general-1.png` … `general-3.png`). Each tile is labeled with the icon's name. Check more than one category when the concept could live in several (a "document" icon might be in `general`, `business`, or `workplace`).
2. Fetch the chosen icon sized and colored for the composition:
   ```
   python scripts/icons.py get stroke_ico_safety_medical_8 --size 120 --color "#1612FF" --out heart.svg
   ```
   The tool sets the brand stroke weight for that size (60px→2, 120px→3, 160px→3.5, interpolated), strips per-path stroke overrides, and refuses colors outside the brand palette. Default color is Almost Black #262626; use White on dark/Vital Trust surfaces.
3. Keep every icon of the same rendered size at the same weight within a composition. Icons smaller than 60px are outside the brand's defined range — the tool extrapolates (never below 1) and says so; mention this to the user if it matters.

If nothing in the library fits, say so and point to brand@mhp.com rather than improvising an icon.

## Quick token reference

| Role | Token | Hex |
|---|---|---|
| Primary | Vital Trust | #1612FF |
| Deep | Darkest Blue | #00055B |
| Light surface | Zircon Lightest / Light / Zircon | #F0F3FF / #E4E9FF / #CDD6FF |
| Accent (contained only) | Kinetic Kiwi Highlight | #DDEF03 |
| Green themes only | Sprout Mint Secondary | #00CC67 |
| Text | Almost Black | #262626 |
| Secondary text/graphics | Brand Grey | #595959 |
| Backgrounds | White / Almost White | #FFFFFF / #F6F6F6 |

Proportions (flexible guideline): Darkest Blue 25%, Vital Trust 25%, Zircon Lightest 37%, Kiwi 5%, White 4%, Almost Black 4%. Light visuals are dominated by Zircon Lightest; full-color visuals by Vital Trust. Full 50–950 scales are in `colors.md`.

Type (Segoe UI → Noto Sans → Arial): Headline 1–4 Bold 92/80/60/48px; Subline 1–2 Bold 36/28px; Body Large/Medium/Small Regular 24/18/16px; Caption 12px; line heights in `typography.md`.

Radius tokens 16/24/32px (nested containers derive from the parent — formulas in `stroke-radius-effects.md`; when a pill is present use 0.5 × pill height). Spacing tokens and the 12-/6-column grid (24px gutter) are in `spacing-layout.md`.

## Known gaps and conflicts in the source guidelines

Surface these to the user when a task depends on them; don't resolve them silently.

1. **Sprout Mint pills:** Mint is forbidden on pills/CTAs generally, yet an "Alternative Pill" in Mint exists for sustainability/positive-outcome contexts. Treat Mint pills as sustainability-context-only.
2. **Slash colors with MHP Blue removed:** the Slash color table substitutes Darkest Blue where the original PDFs used MHP Blue. That is an inference, not a confirmed value — flag if a task depends on those rows.
3. **Icon stroke:** `components.md` says ~3% of icon width (1/32); `stroke-radius-effects.md` gives a size table (60→2, 120→3, 160→3.5 with interpolation). They disagree (e.g. at 160px: 5 vs 3.5). The brand index points to the size table, so `icons.py` follows it.
4. **Arrows:** `document-guidelines.md` allows slashes, arrows, and pills in infographics, but the Slash rules forbid combining the Slash with arrows. Don't put a Slash and arrows in the same infographic.
5. **Full-color proportion typo:** `colors.md` says full-color dominant fill = "Vital Trust + Vital Trust" — almost certainly Vital Trust + Darkest Blue. Use that reading, and mention it if it matters.
6. **Noto Sans web delivery is undefined:** the Adobe Fonts kit only serves Segoe UI, and no loading method for Noto Sans is specified. On the web it only renders if installed on the viewer's device; otherwise the stack falls through to Arial. Don't add a Google Fonts or self-hosted Noto Sans link without confirmation.
7. **Motion principles** are undefined ("TBD") — keep animation minimal and don't invent a brand motion language.
8. **Presentations:** a PowerPoint master template hasn't been built yet; follow the 16:9 Slash layouts in `slash-system.md` and say it's an interpretation.

## Pre-delivery checklist

- Only token colors; MHP Blue only inside the logo; no Kiwi/Mint backgrounds or gradients
- Every text/background pair is on the approved list (or checked and flagged)
- Segoe UI everywhere (fallback stack `segoe-ui, "Segoe UI", "Noto Sans", Arial, sans-serif`); sizes from the scale; nothing under 9pt; "→" not "->"
- Logo placement/clear space/variant correct; at most one Slash, correct color for the background, not at an edge
- Icons come from the library at the right stroke weight; same size → same weight
- Pills: one Main per surface, correct light/dark variants, fully rounded
- Radii from tokens or derived formulas; one structural stroke width per asset
- Shadow row matches the *surface* (white / light / dark), not the element
- Copy: American English/Chicago, Title Case headings; German per Duden with colon inclusivity (Mitarbeiter:innen)
- `lint_brand.py` clean
