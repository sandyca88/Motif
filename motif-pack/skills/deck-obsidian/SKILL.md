---
name: deck-obsidian
description: Create premium dark keynote-style slide decks: deep black canvas, one luminous gradient accent, oversized statement typography, glass cards, glowing data and cinematic pacing. Use for investor pitches, product launches, strategy presentations, all-hands, conference talks, or when the user asks for a professional, premium, sleek, dark, modern, Apple-keynote-like (but original) or impressive deck.
license: Commercial. See LICENSE.txt
---

# Obsidian Deck

Build a complete, presentable slide deck in the **Obsidian** visual style: storyline first, then design. The result should look like a designer made it, not a template.
## Style: Obsidian

**Mood**: a flagship keynote. Confident, calm, expensive-looking. Every slide gets one idea and plenty of dark space.

| Token | Value |
|-------|-------|
| Canvas | `#050507` with a very subtle radial lift at the top (`radial-gradient(1200px 600px at 50% -10%, rgba(124,92,255,.18), transparent)`) |
| Surface (glass) | `rgba(255,255,255,.04)`, 1px border `rgba(255,255,255,.08)`, radius 28px, `backdrop-filter: blur(20px)` |
| Ink | `#F5F5F7`; muted `#8E8E96`; hairlines `rgba(255,255,255,.08)` |
| Accent gradient | `linear-gradient(90deg,#7C5CFF,#22D3EE)`: only for key numbers, one word per title, and chart highlights |
| Glow | accent at 35–45% opacity, blurred 80–120px, placed behind the focal element only |
| Fonts | display: "Inter Tight" / "SF Pro Display" 600–700 at −0.045em tracking; body 400 at 28–32px; mono labels ("JetBrains Mono") 18px uppercase, +0.12em tracking |

**Motifs**: kicker labels in mono ("02 — MARKET"); one gradient word per title; oversized numerals (240–360px) with gradient fill; glass cards for groups of 3; thin hairline dividers; a subtle glow behind the hero element; slide counter + deck name in the footer at 16px muted.

**Archetypes**
- *Title*: kicker, 2-line title (≤ 8 words) with one gradient word, presenter/date line, glow behind the title.
- *Statement*: one sentence at 88–104px across ~70% width, left aligned.
- *Big number*: gradient numeral + one-line meaning + source footnote.
- *Three pillars*: three glass cards, each with an icon (1.5px stroke), 3-word title, one sentence.
- *Chart*: single chart, grey series with one gradient-highlighted series/bar, direct labels, takeaway on the right.
- *Product*: device frame (CSS/SVG) with screenshot placeholder, 2–3 floating callout chips.
- *Roadmap*: horizontal track with 3–4 milestones, current one glowing.
- *Comparison*: us vs. alternatives table; our column tinted with the accent at 8%.
- *Quote*: large quote, attribution with small avatar circle.
- *The ask*: what you want (amount / decision / next step), 3 uses of funds or actions, contact line.

**Motion**: slide content fades up 24px with 60ms stagger; numbers count up; glow breathes slowly (6s). Reduced-motion: static.

**Avoid**: more than one accent gradient per slide, pure white backgrounds, stock photos with text over them, drop shadows on dark, more than 3 cards per row.

**Sample**: see `examples/sample-deck.html` for a complete 10-slide deck built in this style. Reuse its structure and CSS, and replace the content.

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
