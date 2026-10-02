---
name: deck-frost
description: Create soft glassmorphism slide decks: frosted translucent panels over drifting pastel sky gradients, soft glow, rounded cards and airy typography. Use for AI/product launches, app showcases, tech keynotes, wellness or future-facing vision decks, or when the user asks for a glass, frosted, dreamy, soft gradient or modern Apple-like-but-original deck.
license: Commercial. See LICENSE.txt
---

# Frost Deck

Build a complete, presentable slide deck in the **Frost** visual style: storyline first, then design. The result should look like a designer made it, not a template.
## Style: Frost

**Mood**: light, optimistic, futuristic.

| Token | Value |
|-------|-------|
| Sky background | layered radial gradients: `#BFD9FF`, `#E6D5FF`, `#FFE2F0`, `#D6F5FF` on `#F4F7FF` |
| Glass | `rgba(255,255,255,.45)`, `backdrop-filter: blur(24px) saturate(160%)`, 1px border `rgba(255,255,255,.7)`, inner highlight |
| Ink | `#16213A`; muted `#5B6785` |
| Accent | `#5B6CFF` → `#A17BFF` gradient for key numbers only |
| Fonts | airy geometric sans ("Plus Jakarta Sans", "SF Pro Display") 600 for titles, 400 body 28–32px |

**Motifs**: floating glass cards with 32px radius, soft orbs behind glass (blurred circles), subtle light streaks, device frame placeholders (phone/laptop) rendered as glass outlines.

**Archetypes**
- *Title*: centered title on one large glass panel, orbs drifting behind.
- *Feature trio*: three glass cards floating at different depths (slight y offsets).
- *Product shot*: glass device frame with screenshot placeholder + 2 callout chips.
- *Key stat*: gradient number inside a glowing glass circle.
- *Roadmap*: horizontal glass track with milestone pills.
- *Comparison*: two glass columns, recommended one brighter with glow.
- *Closing*: title + CTA pill on glass, orbs converge.

**Motion**: orbs drift slowly (20s), cards float in with blur → sharp. Reduced-motion: static.

**Contrast rule**: always test text on glass over the brightest gradient area; add a stronger white overlay if contrast < 4.5:1.

**Avoid**: dark backgrounds, heavy borders, more than 3 glass layers stacked.

## Workflow

1. **Brief**: confirm topic, audience, goal (inform / persuade / teach), slide count (default 10–12) and whether they need PPTX or PDF as well as HTML. Ask at most one question; otherwise assume and state it.
2. **Storyline first**: write a one-line "so what" for the whole deck, then a numbered outline where every slide title is a full sentence stating that slide's point. Show the outline before building if the deck is > 15 slides.
3. **Pick archetypes**: map each outline line to a slide archetype from the style section below. Never use the same archetype more than twice in a row.
4. **Build**: produce ONE self-contained `deck.html`:
   - 16:9 slides (1920×1080 design size, scaled to fit the window), one `<section>` per slide.
   - Arrow keys / space / click to navigate, `F` for fullscreen, slide counter, `#3` deep links.
   - `@media print` puts one slide per page so "Print → Save as PDF" gives a clean PDF.
   - Speaker notes in `<aside class="notes">`, shown with `N`.
   - All art is inline SVG/CSS: no external images unless the user supplies them. Put image placeholders in labelled frames.
5. **Optional PPTX**: if asked, also generate the deck with python-pptx using the same palette and fonts, with real text boxes (editable, not screenshots).
6. **Self-check** (fix before delivering): one idea per slide; ≤ 30 words of body text per slide (except appendix); text contrast ≥ 4.5:1; title sizes consistent; nothing touching the safe margin (80px); style motifs used on ≤ 50% of slides so they stay special.

## Universal rules

- Titles are statements ("Churn fell 18% after onboarding changes"), not labels ("Churn").
- Numbers get big: a key stat slide shows the number at 200–320px.
- Charts: simplify to the one comparison that matters and label it directly; no legends if avoidable.
- End with a clear ask or next step, never "Thank you / Questions?" on its own.
