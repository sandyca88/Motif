---
name: motion-hero-builder
description: Build cinematic, animated hero sections and landing-page openers — animated gradients, aurora/orb backgrounds, rotating headline words, scroll-driven reveals, video or 3D-style backdrops, magnetic buttons — that stay fast and accessible. Use when the user asks for an animated hero, "motion site", "make the landing page feel alive", a launch page, or a hero with video/gradient/3D background, in HTML, React, Next.js or Tailwind.
license: Commercial — see LICENSE.txt
---

# Motion Hero Builder

The goal: a first viewport that feels premium in the first 2 seconds, loads fast, and never blocks reading.

## 1. Brief

Confirm or infer: product, one-line value prop, primary CTA, mood (calm / energetic / technical / luxurious), and stack. Pick ONE motion concept from the menu below and name it.

## 2. Motion concept menu

| Concept | Technique | Best for |
|---------|-----------|----------|
| **Aurora** | 2–3 blurred radial gradients drifting on `<canvas>` or CSS `@keyframes`, `mix-blend-mode: screen` | AI, SaaS |
| **Hairline grid** | CSS background grid slowly translating + radial spotlight following cursor | dev tools |
| **Word rotator** | Headline with one swapping word, vertical slide + blur, width animates to fit | any |
| **Video backdrop** | Muted, looping, `playsinline`, ≤ 3MB webm/mp4 with poster image and dark overlay | brands, hardware |
| **Orbit / rings** | Concentric rings or orbiting dots in SVG around the product mark | platforms, integrations |
| **Stacked reveal** | Product screenshot rises from below with perspective tilt that flattens on scroll | product launches |
| **Kinetic type** | Letters stagger in (split text), oversized display type | agencies, events |

Combine at most 2 (e.g., Aurora + Word rotator).

## 3. Structure (always)

```
[announcement pill]      → small, links to news/offer
[H1 ≤ 8 words]           → one emphasized word (serif italic or gradient)
[sub ≤ 25 words]
[primary CTA][secondary] → primary solid, secondary ghost
[proof]                  → logos marquee, rating, or product visual
```

## 4. Motion rules

- Entrance: stagger pill → H1 → sub → CTAs → visual, 80ms apart, 600–900ms each, ease `cubic-bezier(.2,.8,.2,1)`, from `opacity:0; translateY(24px); filter: blur(6px)`.
- Ambient motion is slow (≥ 6s loops) and low contrast so text stays readable (headline contrast ≥ 4.5:1 over the busiest frame).
- Interactive: magnetic primary button (max 8px pull), cursor spotlight, card tilt ≤ 8°.
- Animate only `transform`, `opacity`, `filter`; use `will-change` sparingly; pause canvas/video when off-screen (IntersectionObserver) and when `document.hidden`.
- `prefers-reduced-motion: reduce` → no ambient loops, entrances become simple fades, video shows poster.

## 5. Performance budget

- No animation library required; use CSS + ~60 lines of vanilla JS. If the project already uses GSAP or Framer Motion, use it.
- LCP element is the H1 text, not a background.
- Hero JS < 10KB, video lazy-loaded after first paint, fonts `font-display: swap`.

## 6. Deliver

1. One-line concept statement ("Aurora + Word rotator, calm technical mood").
2. Complete, self-contained code for the hero (and nav) in the user's stack.
3. A "Tuning knobs" list: the 4–6 CSS variables they can change (colors, speed, blur, intensity).
4. Offer 2 alternative concepts from the menu in one line each.
