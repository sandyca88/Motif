---
name: deck-clearview
description: Create clean, minimalist product-keynote slide decks: bright white canvas, near-black ink, one crisp blue accent, huge centered headlines, product hero visuals floating in whitespace, soft shadows and precise system typography. Use for product launches, feature announcements, company updates, design reviews, or when the user asks for a clean, minimal, elegant, white, premium tech-keynote or 'simple but beautiful' deck.
license: Commercial. See LICENSE.txt
---

# Clearview Deck

Build a complete, presentable slide deck in the **Clearview** visual style: storyline first, then design. The result should look like a designer made it, not a template.
## Style: Clearview

**Mood**: a calm, confident product keynote. Almost nothing on screen, and everything on screen matters.

| Token | Value |
|-------|-------|
| Canvas | `#FBFBFD` (main), `#F2F2F5` for alternating "tile" slides, `#0B0B0C` for one dramatic reveal slide |
| Ink | `#1D1D1F`; secondary `#6E6E73`; hairline `#E3E3E8` |
| Accent | crisp blue `#0A66FF`, only for links, one keyword or one data highlight per slide |
| Gradient (reveal slides only) | `linear-gradient(90deg,#0A66FF,#8B5CF6,#EC4899)` on one headline word |
| Fonts | system UI stack (`-apple-system, "SF Pro Display", "Inter", "Segoe UI", sans-serif`); display 600 at −0.04em; body 400 at 30–34px, secondary color |
| Shadow | product visuals only: `0 40px 80px -20px rgba(0,0,0,.18)` |

**Motifs**: centered headline + short subline; one product hero (device frame, card or object) floating with a soft shadow; "tile" slides with 2–4 rounded panels (28px radius) on `#F2F2F5`; small eyebrow in accent color above headlines; big numbers in near-black with a small secondary caption; lots of whitespace (content ≤ 60% of slide area).

**Archetypes**
- *Title*: centered eyebrow, 2-line headline, subline, product hero below.
- *Reveal*: black slide, gradient-word headline, product glowing softly.
- *Feature tile grid*: 2×2 rounded tiles, each with an icon, 3-word title and one line.
- *Big number*: centered 280px number, caption below.
- *Product detail*: product left, 3 labelled callouts with thin leader lines right.
- *Comparison*: before/after two tiles.
- *Availability*: "Available [date]" + price + one CTA line.

**Motion**: gentle fade + 16px rise, 700ms; product scales from 0.96. Reduced-motion: fade only.

**Avoid**: dark text-heavy slides, more than one accent, bullet lists longer than 3, busy backgrounds, borrowed brand names or logos. This is an original style, not a copy of any company's keynote.

**Sample**: see `examples/sample-deck.html` (8 slides) for a complete deck in this style.

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
