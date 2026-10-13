# MHP Brand Design System — Stroke, Radius & Effects

Reference file for generating on-brand code, layouts, and assets. Rules below are constraints, not suggestions — treat "Forbidden" as hard blocks in generated output.

---

## Stroke Rules

Two separate stroke rules apply, depending on what's being drawn. Don't conflate them.

### 1. Icon stroke width (size-dependent)

Icon line weight scales with icon size — larger icons get proportionally heavier strokes. Use the defined points below; for icon sizes falling between them, interpolate linearly rather than rounding to the nearest defined value.

| Icon size | Line weight |
|---|---|
| 60px | 2pt |
| 120px | 3pt |
| 160px | 3.5pt |

**Within a single composition:** every icon at the same size must use the same line weight. If a composition mixes icon sizes (e.g. a large hero icon next to smaller inline ones), each size follows its own value from the table above — this is expected and not a violation of consistency, since the rule is "consistent per size," not "one flat width regardless of size."

### 2. Structural stroke width (asset-level)

Separators, button/pill outlines, and container borders should use one consistent stroke width across a single asset or deliverable (e.g. one PDF, one slide deck, one web page) — pick a weight appropriate to the asset's overall scale and apply it uniformly, rather than varying border weights arbitrarily between similar elements. This is independent of the icon-scaling rule above; icons follow their own size-based formula even within an asset that otherwise uses a single structural stroke weight.

---

## Radius Tokens

| Token | Value (px) |
|---|---|
| Small | 16 |
| Medium | 24 |
| Large | 32 |

Use these three values directly for standalone elements (cards, buttons, images) — pick the token closest to the element's intended visual weight.

### Nested Container Radius Rules

When a container sits inside another rounded container, its corner radius is *derived* from the parent rather than picked independently, so the nesting reads as visually consistent. Two formulas apply depending on whether a pill is present in the visual:

- **Standard formula** (no pill present): `nested radius = parent (inner) container radius + padding between the two containers`
  - Example: a Medium (24px) parent container with 12px of internal padding around a nested card → nested card radius = 24 + 12 = 36px.
- **Pill-relative formula** (a pill is present anywhere in the visual): `nested radius = 0.5 × pill height`, overriding the standard formula for that nested container.
  - Example: a 40px-tall pill in the composition → any nested container radius in that same visual = 20px, regardless of what the standard formula would otherwise produce.

If a visual has no nesting at all (a single flat container), use a Radius Token directly instead of either formula.

---

## Effect Styles

| Effect | Blur | Offset (x/y) | Color |
|---|---|---|---|
| Drop shadow — on white background | 32px | 5 / 7 | #A5B2FF4F |
| Drop shadow — on light background | 30px | 5 / 7 | #6D6D6D26 |
| Drop shadow — on dark background | 32px | 0 / 5 | #26262633 |
| Background blur | 26px | — | — |

Choose the drop shadow row that matches the surface the element sits on — white, light-neutral, or dark — not the color of the element itself. Background blur is applied to the backdrop behind a surface (e.g. a translucent card), not to the element's own edges.

---

**Contact:** Brand questions: brand@mhp.com