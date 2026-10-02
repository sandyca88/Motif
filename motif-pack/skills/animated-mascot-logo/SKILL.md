---
name: animated-mascot-logo
description: Design and build a living, animated mascot logo for a brand or product — a simple shape with eyes that looks at the cursor, blinks, breathes, squishes on hover, morphs between shapes, or appears as a family of character avatars — in pure HTML/CSS/JS (no libraries), plus favicon/app-icon exports and an animated logo video/GIF. Use when the user asks for an animated logo, mascot, brand character, cute logo, logo with eyes, "make the logo feel alive", agent/bot avatars, loading/thinking indicators, or a logo animation for social media.
license: Commercial — see LICENSE.txt
---

# Animated Mascot Logo Kit

Turn a plain logo shape into a character people remember. Three proven concepts (live in `examples/mascot-concepts.html`):

| Concept | What it does | Best for |
|---------|--------------|----------|
| **A · Glance** | One mark; eyes follow the cursor, blink every 3–6 s, gentle breathing, squish on hover | Primary logo, nav, favicon, inline in headlines ("Meet ◉ Brand") |
| **B · Morph** | The mark morphs between shapes (squircle → circle → drop) while the eyes stay | A brand with several products/libraries; hero or loading states |
| **C · Family** | A crew of shapes + colors with the same eyes, hopping in turn, with a typing indicator | Category icons, AI agent/bot avatars, team or feature sections |

## 1. Brief (ask or infer)
Brand name, existing logo shape/colors, personality (curious / calm / playful / precise), where it appears (nav 24–32px, favicon 16px, hero 120px+, avatars 40–64px).

## 2. Design rules
- **Start from the brand's own shape** (rounded square, circle, letterform counter). Never imitate another company's mascot.
- **Eyes carry 90% of the character.** Two white ovals ≈ 18% × 24% of the shape, centered slightly above middle; pupils ≈ 62% × 52% of the eye with a small white highlight. No mouth = calmer, more premium.
- Body: brand gradient (conic or radial) + inner top highlight + soft colored glow below. Keep it readable at 16px: test the favicon early.
- Family members share eyes and proportions; vary only shape and one color each.

## 3. Motion recipes (CSS/JS)
- **Look-at-cursor:** per mark, `dx,dy = pointer − center`; `k = min(1, dist/180)`; pupil `translate(dx/dist·k·28%, dy/dist·k·30%)`. After 3.5 s idle, wander on a slow Lissajous path.
- **Blink:** add `.blink` (eye height → 3%) for 120 ms at random 3–6 s intervals, independently per mark.
- **Breathe:** `scale(1.03) translateY(-2px)` over 4 s, ease-in-out, infinite.
- **Squish on hover:** keyframes `scale(1.12,.88) → (.94,1.06) → 1` over 500 ms with `cubic-bezier(.34,1.56,.64,1)`.
- **Morph:** animate `border-radius` between shape keyframes over 6 s; swap a label in sync.
- **Family hop:** staggered `translateY(-10px) scale(1.04,.96)` with animation-delay per member.
- **Thinking state:** three dots that rise in sequence (1.2 s loop) beside the mark.
- Always: `prefers-reduced-motion: reduce` → no animation; pointer listeners passive; one rAF loop for all marks.

## 4. Exports
- SVG/PNG mark at 1024/512/192/180/32/16 px (favicon + apple-touch-icon + PWA icon), dark-background app icon.
- Animated logo: 3 s loop (look around → blink → squish hop), MP4 (H.264) for social and a ≤ 1 MB GIF for email/README. Render frames from the same geometry (e.g. Pillow) and encode with ffmpeg.
- Optional 3D hero render — prompt: "A premium 3D render of an original cute app-icon mascot: a soft glossy rounded-square jelly character with a smooth gradient from [color A] through [color B] to [color C], subtle glass-like translucency, soft specular highlight, two small friendly white oval eyes with black pupils, no mouth, floating with a soft glow on a [background], minimal, centered, no text, no logos."

## 5. Deliver
1. Concept sheet (A/B/C live) and the chosen mark as a drop-in component (`<span class="mark">` + 30 lines of JS).
2. Inline usage examples: nav logo, headline ("Meet ◉ Brand"), favicon, avatars, thinking indicator.
3. Export pack (PNGs, MP4, GIF) and a short usage guide (min size 16px, clear-space = 25% of mark, don't stretch, don't recolor eyes).
