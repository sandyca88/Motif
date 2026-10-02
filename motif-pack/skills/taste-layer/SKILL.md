---
name: taste-layer
description: Make any frontend the agent builds look intentionally designed instead of AI-generated. Applies a professional design system (type scale, spacing rhythm, color, layout, motion, detail rules) to landing pages, web apps, dashboards and components in HTML, React, Vue, Svelte or Tailwind. Use whenever the user asks to build, style, redesign, "make it look better/premium/modern", or when generating any UI from scratch.
license: Commercial — see LICENSE.txt
---

# Taste Layer

Generic AI UIs share the same tells: purple-to-blue gradient everywhere, centered everything, same-size cards in a 3-column grid, emoji icons, `rounded-xl shadow-lg` on every box, lorem-flavored copy. This skill replaces defaults with deliberate decisions.

## Step 0 — Pick a direction before writing code

Choose ONE aesthetic direction and state it in one line at the top of your response. If the user gave none, pick what fits the product:

| Direction | Use for | Signature |
|-----------|---------|-----------|
| **Precision** | dev tools, SaaS, B2B | near-black bg, 1px borders, mono accents, tight tracking, subtle grid |
| **Editorial** | content, portfolios, agencies | serif display + sans body, big type, asymmetric layout, generous whitespace |
| **Soft product** | consumer apps, wellness, fintech for everyone | warm off-white, large radius, pastel accents, friendly rounded sans |
| **Bold brutal** | creative, events, fashion | oversized type, hard edges, one loud color, visible structure |
| **Cinematic dark** | AI, launches, premium hardware | deep black, one glow color, video/3D hero, slow motion |

Commit to it. Every choice below must serve that direction.

## Step 1 — Tokens first

Use the libraries in `references/palettes.md` (24 AA-checked palettes by direction) and `references/font-pairings.md` (20 pairings) instead of inventing values from scratch.

Define CSS variables (or Tailwind theme) before any component:

- **Type scale**: ratio 1.25 (UI) or 1.333–1.5 (marketing). Display headings get negative tracking (−0.02 to −0.045em) and line-height 0.95–1.1. Body 16–18px, line-height 1.5–1.65, max 68ch.
- **Font pairing**: max 2 families. Never default to Inter-only for marketing pages — pair it with a display or serif face, or use a characterful sans.
- **Spacing**: 4px base; sections use 96–160px vertical padding on desktop. Spacing *inside* a group is always smaller than spacing *between* groups.
- **Color**: 1 neutral ramp (9 steps) + 1 accent + semantic (success/warn/danger). Accent covers ≤ 10% of any screen. Avoid pure #000 on #fff — use #0a0a0b / #fafafa.
- **Radius**: one value for controls, one for containers. Nested radius = outer − padding.
- **Elevation**: prefer borders (1px, 6–10% alpha) over drop shadows on dark UIs; use layered soft shadows on light UIs.

## Step 2 — Layout rules

- Break the grid at least once per page: an off-center hero, a bento grid with mixed spans, a full-bleed image, or a sticky side column.
- Vary section rhythm: don't stack five identical "heading + 3 cards" sections.
- Align to a 12-column grid with a max content width (1120–1280px). Text blocks narrower than media.
- Hero: headline ≤ 8 words, sub ≤ 25 words, 1 primary CTA + 1 secondary, visual proof (product shot, demo, video) in the first viewport.

## Step 3 — Detail pass (this is where taste shows)

- Real copy, never lorem. Write benefit-led headlines and specific numbers.
- Icons: one set, one stroke weight (1.5px), sized to cap height of adjacent text. No emoji as icons.
- Images: consistent treatment (same aspect ratios, same grading or duotone).
- Buttons: height 40/44/48, horizontal padding ≈ 1.5× vertical, label weight 500–600.
- Borders on dark UI: `rgba(255,255,255,.08)`; hover raises to `.16`.
- Add one "signature" detail: a grain overlay, a hairline grid, a highlighted word in the display serif, a custom cursor, animated gradient border — but only one or two.
- Numbers in tables/stats use `font-variant-numeric: tabular-nums`.

## Step 4 — Motion

- Durations: 150–250ms for UI feedback, 400–900ms for reveals. Ease: `cubic-bezier(.2,.8,.2,1)`.
- Reveal on scroll with opacity + 16–28px translate + optional blur; stagger siblings 40–80ms.
- Animate only `transform`, `opacity`, `filter`.
- Always include `@media (prefers-reduced-motion: reduce)` that disables non-essential motion.

## Step 5 — Self-check before delivering

Run this checklist and fix anything that fails:

- [ ] Could someone guess the direction from a screenshot?
- [ ] Is there exactly one focal point per viewport?
- [ ] Body text contrast ≥ 4.5:1, focus rings visible?
- [ ] No more than 2 font families, 1 accent color?
- [ ] At least one layout moment that breaks the default grid?
- [ ] All interactive states (hover/focus/active/disabled) styled?
- [ ] Looks right at 375px, 768px and 1440px?

End your response with one sentence naming the direction and the signature detail you used, so the user can ask for alternatives.
