# MHP Brand Design System — Typography

Reference file for generating on-brand code, layouts, and assets. Rules below are constraints, not suggestions — treat "Forbidden" as hard blocks in generated output.

---

## Typeface Selection
- **All materials:** Segoe UI (Light, Regular, Italic, Bold, Black)
- **Fallback order** (when Segoe UI is not available):
  1. **Noto Sans** — main fallback
  2. **Arial** — second fallback
- Fallbacks follow the same Type Scale and weights as Segoe UI (Regular → Regular, Bold → Bold, etc.)
- **Orbitron:** strictly prohibited for body/standard text — official Digital Product naming only

---

## Web Delivery — Segoe UI
Segoe UI is licensed for web use via Adobe Fonts (Typekit), not self-hosted. Do not extract or embed the raw font file (e.g. base64 `@font-face`) — the license only covers serving through Adobe's kit link.

- **Rule:** every generated HTML file must include the kit `<link>` in `<head>`, placed before the `<style>` block (or before any other stylesheet `<link>`, e.g. `styles.css` in `index.html`):
  ```html
  <link rel="stylesheet" href="https://use.typekit.net/brx4bpj.css">
  ```
- **CSS:** `font-family: segoe-ui, "Segoe UI", "Noto Sans", Arial, sans-serif;`
- **Domains:** Adobe Fonts web projects are not domain-restricted — the kit link works on any site, any hosting, or an HTML email with no per-domain approval needed.
- **Weights:** confirm the kit includes the weight(s) needed (e.g. Bold/700 for Link Dark) before relying on it — Adobe's default embed snippet only guarantees Regular/400 unless additional weights are added to the kit.

---

## Type Scale

**Segoe**
| Style | Spec | Size / Line height | Tracking |
|---|---|---|---|
| Headline 1 | Bold | 92px / 90px | 0 |
| Headline 2 | Bold | 80px / 90px | 0 |
| Headline 3 | Bold | 60px / 60px | 0 |
| Headline 4 | Bold | 48px / 48px | 0 |
| Subline 1 | Bold | 36px / 36px | 0 |
| Subline 2 | Bold | 28px / 28px | 0 |
| Body Large | Regular | 24px / 32px | 0 |
| Body Medium | Regular | 18px / 24px | 0 |
| Body Small | Regular | 16px / 20px | 0 |
| Link Dark | Bold | 16px / 18px | 0 |
| Caption | Regular | 12px / 18px | 0 |

---

## Formatting Rules
- Minimum font size: 9pt anywhere (accessibility floor — never go below)
- Max ~3 font sizes per document
- No justified text (Blocksatz) in multi-column layouts
- No double spaces
- Arrows typeset as "→", never "->"
- One consistent language per document — no language-mixing

---

**Contact:** Brand questions: brand@mhp.com
