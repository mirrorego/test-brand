# MHP Brand Design System — The Slash

Reference file for generating on-brand code, layouts, and assets. Rules below are constraints, not suggestions — treat "Forbidden" as hard blocks in generated output.

The Slash is MHP's primary and defining visual identity element — the central brand signature across all applications. Within the visual hierarchy, the Slash always takes highest priority: the primary source of visual emphasis, direction, and structural rhythm.

---

## Design Principles

The Slash serves a dual role:
- **Decorative:** introduces rhythm, tension, and dynamic energy into compositions.
- **Functional:** acts as a structural/directional device — guides visual flow, frames content, reinforces hierarchy.

Five core principles: precision in geometry and execution, dynamic expression through motion and scale, technical clarity across all implementations, strong and consistent brand recognition, scalable application across all contexts.

### Core Rules
- **Rule 01:** Apply with intention and restraint — structural and brand-defining, not purely decorative.
- **Rule 02 — Forbidden:** The Slash must never compete with additional symbolic graphic elements. Combinations with arrow or arrow-like directional graphics are not permitted.
- **Rule 03:** Pills may coexist within their standard application framework, provided they don't visually compete with the Slash. Pills remain exclusively functional and non-decorative. The Slash must always remain the central focal point.

---

## Geometric Foundation

- **Angle:** exactly 10°, fixed and non-negotiable across all applications.
- **Forbidden:** rounded corners. The Slash is strictly non-rounded, sharp, linear geometry.
- This is the same shape defined in `components.md` (official SVG source of truth — do not redraw).

---

## Color System

Color usage follows a systematic logic across backgrounds. The Slash must be perceivable against its background, and any text on top of it must remain accessible.

| Mode | Background | Slash Color |
|---|---|---|
| Light | Zircon Light | Vital Trust |
| Light | Zircon Lightest | Darkest Blue |
| Light | Zircon | White |
| Dark | Vital Trust | Darkest Blue |
| Dark | Darkest Blue | Vital Trust |
| On Imagery | Light images | Darkest Blue |
| On Imagery | Dark images | White |
| On Imagery | Neutral images | Vital Trust |

> **Updated per brand rule (MHP Blue restricted to polychrome logo only):** this table originally came from the source PDFs with MHP Blue used as both a Slash color and a background option in several rows. Since MHP Blue is now restricted to the polychrome logo only (see `colors.md` → Color Usage Rules), those rows have been replaced with Darkest Blue as the nearest equivalent deep-blue tone, and the "Dark mode: MHP Blue background" row has been removed entirely (MHP Blue can no longer be used as a background surface). **This is an override of the literal PDF source — confirm with the design system owner that Darkest Blue is the correct substitute before treating this table as final,** since the original documents specified exact values without anticipating this restriction.

> **Conflict with `components.md`:** the Components file currently states a simpler rule ("Default fill: Vital Trust; recolor only to MHP Blue or White on dark backgrounds"). This table supersedes that — color is determined by the specific background tone, not a flat default. Update `components.md` to reference this table rather than its own simplified version.

---

## Dos and Don'ts — Forbidden

- Do not use the Slash in any color other than defined in the Color System table above.
- Do not use more than one Slash element in a single composition.
- Do not crop or deform the Slash.
- Do not use the Slash at any angle other than 10°.
- Do not use the Slash on abstract brand imagery.
- Do not rotate the Slash.
- Do not cut the Slash.
- Do not place the Slash at the edge of the format (see Protective Clear Space below).
- Do not combine the Slash with other brand elements (arrows, etc. — see Rule 02).
- Do not use the Slash in combination with any kind of numbers (e.g. "30%" overlays).

---

## Sizing Framework

### Slash Types & Use Cases

| Type | Role | Use Cases |
|---|---|---|
| Hero / Macro (XL) | Strongest visual anchor | Cover slides, campaign openers, header images, hero visuals, announcements |
| Accent (L/M) | Supporting visual accent within sections/cards | Content slides, headline emphasis, section dividers |
| Micro (S/XS) | Micro-interactions, interface details, system indicators | Quote slides, navigation, status representation, microtypography |

- **Forbidden:** scaling the Slash smaller or larger than the sizes defined for its respective application.

### The Slash-Based Grid System

- 12 horizontal columns aligned along the fixed 10° Slash angle.
- Grid proportions derive directly from the Slash: the foundational structure spans 8 rows in height; column spacing = half the height of one row.
- This is a directional grid, not a conventional orthogonal one — it introduces movement and structural tension into layout architecture.

### Adaptive Format System (Stencils)

Predefined, pre-built grid templates per format — do not modify the underlying grid structure or proportions:

| Format | Use |
|---|---|
| Widescreen 16:9 | Presentations, websites, widescreen digital |
| Web Banner | Website stages |
| DIN A4 | Whitepapers, reports, editorial documentation |
| Single Post 4:5 | Social media (max feed reach, Instagram/LinkedIn) |
| Square 1:1 | Social media, cross-platform branding |
| Portrait 3:4 | Social media (Instagram, Facebook, LinkedIn, Pinterest) |
| Portrait 2:3 | Social media, same usage as 3:4 |

### Spatial Relationships & Composition Rules

- **Protective Clear Space:** the Slash requires defined clear space to the outer edges of its format — never edge-to-edge, never bleeding off the format. Clear space is derived automatically from the grid system's outer margin.
- **Forbidden:** letting the Slash visually collide with body copy, interactive components, or other graphic/decorative elements. The Slash must always appear intentional, isolated, and structurally integrated.

### Relationship to Typography

- **Large (Macro) Slash:** may combine with headlines, subheadlines, and image elements — dominant compositional anchor in hero/campaign layouts.
- **Medium (Accent) Slash:** may combine with headlines and sectional typography to support hierarchy without overpowering the layout.
- **Small/Micro Slash — Forbidden:** must not directly interact with typographic elements; reserved for subtle structural/interface use, maintaining minimum clear space.

**Headline positioning (Hero Slash) — three anchor options:**

| Option | Anchor Point | Notes |
|---|---|---|
| A — Offset Left | Half a Slash width to the left of the Slash | Most separation between text and Slash; reads as two distinct visual blocks |
| B — Edge Aligned | Left-bottom edge of the Slash | Text baseline ties directly to the Slash's left edge; tighter visual connection |
| C — Center Aligned | Center line of the Slash's bottom edge | Text centers on the Slash's midpoint; most integrated, statement-style composition |

- Pick **one** anchor option per composition — don't mix multiple anchor logics on the same page.
- **Default alignment is left.** Options A, B, and C above are all left-aligned variants and should be the default choice for any composition. Right-aligned text (below) is the exception, used only when the layout specifically calls for it — don't reach for right-alignment as a stylistic default.
- The chosen anchor applies consistently regardless of which background/color combination is used (Vital Trust, Darkest Blue, or White Slash per the Color System table) — anchor logic and color logic are independent decisions.
- **Line count:** both headlines (shorter, ~3 lines) and longer statements/quotes (~4 lines) are supported within the same anchor system — the text area scales with content length but must stay within the 12-column grid and the 1/8-height clear space top and bottom. Don't let a 4-line statement compress the clear space margins to fit.

**Right-aligned text:** only one anchor permitted — the right-bottom edge of the Slash. Headlines in right-aligned compositions are always uppercase (e.g. "THIS MUST BE A HEADLINE IN CAPITALS") regardless of background/color combination chosen. Sublines may use standard capitalization, minimum 12pt.

**Micro Slash + text:** spacing between Slash and text is fixed at 2× the Slash's width, regardless of format. The baseline of the first text line must align with the Slash's bottom edge; cap height of the first line must never extend above the Slash's top edge. When text is long enough to wrap across multiple lines, the container (not the Slash) governs wrapping/truncation — the Slash's position relative to the first line stays fixed even if later lines get clipped by the layout's width constraint.

**Exceptions (mainly social media):** the Slash may act as an independent, expressive background element rather than being directly tied to the headline — but text must still sit comfortably within the Slash's visual boundaries with at least half a row of space from its edges, and text must never be aligned directly with the Slash's top or bottom edge.

### Relationship to Images

- Keep at least three corners of the Slash visible at all times.
- Image's color palette must provide sufficient contrast for the Slash to stand out in its specified brand color.
- **Forbidden:** placing the Slash over complex/busy image areas that reduce readability; using images where the Slash doesn't achieve enough contrast; cropping the main subject too tightly to leave no clear space.
- Choose images with a clear, isolatable focal point and a clean, calm background.

**Do / Don't reference:**

| ✓ Do | ✗ Don't |
|---|---|
| Choose images with a clear focal point that can be isolated and combined with the Slash | Place the Slash over complex image areas that reduce readability or recognition |
| Ensure enough contrast between image and Slash | Choose images where the Slash doesn't achieve enough contrast or visibility |
| Keep backgrounds clean and visually calm to support the Slash | Use images with busy backgrounds or too many competing visual elements |
| Maintain sufficient space around the main subject to preserve Clear Space | Crop or position the main subject too tightly, leaving no room for the required Clear Space |

**Subject/Slash placement:** the main subject (person, product, focal object) is typically positioned on one side of the frame with the Slash placed on the opposite side, sized/cropped so it doesn't overlap or compete with the subject. Center-line alignment between subject and Slash helps balance the composition without them colliding.

**Best-case technique — Cutout Integration:** rather than keeping the Slash as a flat, separate overlay, the strongest compositions layer an isolated cutout element (subject or object cut from its background) on top of or overlapping the Slash — see "Cutout Integration" under Web Hero / Banner Pattern below for full detail. This applies across formats, not just web.

### Web Hero / Banner Pattern

Applies to `colors.md`-approved image backgrounds used in Web Presence hero sections and banner cards (see Applications → Web Presence).

**Option 1 — Preferred, when a clear-subject image is available:**

This is the default choice whenever the source image has an isolatable subject (a product, device, vehicle, or similar). Structure:

1. Full-bleed image fills the hero container, rounded corners per `stroke-radius-effects.md`.
2. Content card on the left: light/white rounded card, containing a bold headline, a short 1–2 line description, and a single CTA button.
3. The Slash sits on the right side of the image, sized to roughly the height of the card, positioned so it never overlaps the card or its text.
4. **Cutout Integration is applied by default in this option:** the image's main subject is cut out and layered in front of the Slash, partially covering it — see Cutout Integration below. This is what makes this pattern the preferred one, not just a plain image-with-Slash overlay.
5. Slash color follows the On Imagery row for the image's tone (e.g. Vital Trust on a neutral/dark space or tech image).

The CTA button is a **Secondary Pill** (solid Vital Trust fill, white text) — this is correct per the corrected Pills spec in `components.md`.

**Option 2 — Article/Report Header (no card, text directly on image):**

Used for editorial/report page headers (e.g. mhp.com insights and publication pages) rather than promotional banners. Structure, confirmed from live page markup:

1. Full-bleed hero image, edge-to-edge, no rounded card container over the text.
2. A small eyebrow label above the headline (e.g. "Report") — identifies the content type.
3. Large H1 headline set directly on the image.
4. A one-line supporting subheadline below the headline, lighter weight than the H1.
5. A single CTA button below the subheadline (e.g. "Download Report") — text sits in the left portion of the hero, image extends full-width behind it.
6. Text color follows the Approved Accessibility Pairings in `colors.md` for the image's tone (e.g. White text on a dark image).

> **Unverified:** exact colors, the eyebrow label's styling (pill vs. plain label), and whether/how the Slash is integrated into this specific header could not be confirmed — the fetch tool retrieved this page's text/structure but not the rendered hero image itself. Confirm visually before treating the Slash placement or exact color values here as settled; the *layout structure* (eyebrow → H1 → subheadline → single CTA, no card) is confirmed from the page markup.

**Other approved options** (use when no clean subject cutout is available — e.g. abstract or purely atmospheric imagery):

1. Full-bleed image fills the banner/hero container (rounded corners per `stroke-radius-effects.md`).
2. A content card (white or Zircon Lightest background, rounded corners) sits on top of the image, positioned opposite the Slash — typically left-aligned. Card contains: short headline, optional one-line description, and a CTA Pill (Secondary Pill — solid Vital Trust fill on the light card — is common here; see `components.md` → Pills).
3. The Slash sits on the side of the image without the content card (typically right), positioned so it never overlaps the card or its text.
4. Follow the On Imagery Color System row for Slash color based on whether the image reads as light, dark, or neutral.
5. Cutout Integration (below) may still be applied opportunistically if a partial subject is available, even without a fully clean cutout.

**Multi-banner stacks** (e.g. a list of feature banners): repeat the same left-card / right-Slash pattern consistently across every banner in the stack — don't alternate sides between banners, so the eye can scan the list predictably.

**Cutout Integration — best-case pattern:** the strongest execution of the Slash on an image background layers a cut-out element from the image (e.g. a product, device, or subject silhouetted out of its background) directly on top of, or overlapping, the Slash. This creates depth and visually fuses the Slash into the image rather than leaving it as a flat overlay — the Slash reads as integrated into the scene, not stamped on top of it. This is the same technique referenced under Applications → Social Media (Layout 1.2 "Image Background") and applies equally well to Web Hero/Banner compositions.
- The cutout may partially cover the Slash — this is intentional layering, not a violation of the "keep at least three corners of the Slash visible" rule, since the Slash itself is uncropped and unaltered; an object is simply placed in front of it.
- The Protective Clear Space rule still applies to the *frame edges* — a cutout covering part of the Slash doesn't exempt the composition from keeping the Slash away from the outer edges of the format.
- Use this technique when the source image has a clear, isolatable object (a product, device, vehicle, person) that can be cleanly cut out — don't force a cutout from a busy or low-contrast image just to use the technique.

---

## Applications

### Web Presence
Grid: Web Banner. Defines the foundation for a cohesive digital brand experience — layouts, interactions, and visual elements follow consistent logic while allowing flexibility across digital journeys.

### Publications
Grid: DIN A4. A consistent title system uses the Micro Slash as a visual guideline for headlines, linking typography to the brand element. The Slash can also serve as a highlight element per the defined application rules.

### Presentations
Grid: Widescreen 16:9. Defined layout set: title slide, two Table of Contents variations, two divider slide variations, and an exemplary content slide. *(Next step: a professional PowerPoint master template needs to be developed from these principles.)*

### Social Media
Three grid systems: **Single Image 4:5** (max reach on Instagram/LinkedIn), **Square 1:1** (cross-platform, product/branding), **Portrait 3:4** / **Portrait 2:3** (engaging vertical space across Instagram, Facebook, LinkedIn, Pinterest). CTA and logo placement follow a consistent grid-based position, with limited exceptions (e.g. certain carousel layouts) that must still follow overall Slash system principles.

**Single Post layouts (4:5 or 1:1):**
| Layout | Description |
|---|---|
| 1.1 Solid Color Background | Macro Slash centered in 12×12 grid with freestanding highlight element (cut-out image above Slash, then headline/subheadline). At 1:1, Slash scales from XL to L. |
| 1.2 Image Background | Macro Slash centered in 12×12 grid (4:5) with an integrated freestanding visual element layered above for depth; headline/subheadline positioned above the composition. |
| 1.3 Micro Slash Supporting Headline | Slash used as a subtle identifier alongside the headline; background can be photographic or solid brand color. |

**Carousels (4:5 only):**
| Layout | Description |
|---|---|
| 2.1 Classic Carousel | Title slide: strong image + Macro Slash, headline above. Content slides: L Slash as anchor + numbering + statement below. MHP Arrows used as navigation, bottom-right corner. |
| 2.2 Dynamic Split Layout | Title slide styled like 1.1. Content slides: horizontally split layout, alternating color/image fields, Micro Slash as supporting element. Final slide: full-color background with CTA/closing statement. MHP Arrows for navigation, bottom-right. |

**Quotation Posts (4:5 or 1:1):**
| Layout | Description |
|---|---|
| 3.1 Bold Macro Slash | Macro Slash dominant in background; headline above establishes hierarchy. |
| 3.2 Standard Micro Slash | Micro Slash as statement opener; headline at top; quotation left-aligned. |
| 3.3 Long Version | Spacious format for longer statements; Macro Slash dominant in back, same approach as 3.1. |

**Social Media Headers:** predefined finished assets per channel — use as provided; don't recompose.

### Events
Applied consistently across trade shows and exhibition stands for a recognizable presence — but individual stand requirements/dimensions must be considered case by case. No single rigid system is defined for all stand formats; the Slash principles serve as a flexible framework that must still maintain core brand rules.

---

## Motion Principles

TBD — not yet defined.

---

**Contact:** Brand questions: brand@mhp.com
