---
name: deck-grid-signal
description: Create Swiss/International-style system slide decks: strict 12-column grid, bold sans typography, one signal color, big numbers, visible structure and data-forward layouts. Use for product strategy, design systems, engineering reviews, quarterly business reviews, investor updates, or when the user asks for a clean, modernist, Swiss, systematic or bold minimal deck.
license: Commercial. See LICENSE.txt
---

# Grid Signal Deck

Build a complete, presentable slide deck in the **Grid Signal** visual style: storyline first, then design. The result should look like a designer made it, not a template.
## Style: Grid Signal

**Mood**: precise, confident, architectural.

| Token | Value |
|-------|-------|
| Background | `#F4F4F0` (light) or `#0C0C0E` (dark variant) |
| Ink | `#111` / `#F4F4F0` |
| Signal | cobalt `#1F3FFF` (only one accent; ≤ 15% of any slide) |
| Grid | 12 columns, 80px margins, 24px gutters; optional visible hairlines `rgba(0,0,0,.08)` |
| Fonts | neo-grotesk ("Inter Tight", "Helvetica Neue", "Neue Haas") 700 for headings at −0.04em tracking; mono for labels |

**Motifs**: section numbers in the top-left corner ("02 / Strategy"), thin rules separating zones, oversized numerals, solid signal-color blocks occupying exact grid columns, small mono metadata row at the bottom (date · deck name · page).

**Archetypes**
- *Title*: headline set left across 8 columns, huge; signal block 4 columns right; metadata row.
- *Section divider*: giant section numeral (400px) + section name.
- *Statement*: one sentence at 88–110px across 10 columns.
- *Key metrics*: 3–4 columns each with big number, label, delta.
- *Chart*: single simplified chart occupying 8 columns + 4-column takeaway.
- *Comparison table*: strict grid table, signal color highlights the recommended option.
- *System diagram*: boxes aligned to the grid, arrows orthogonal only.
- *Decision / ask*: left: the decision needed; right: options with a recommended one in signal color.

**Motion**: blocks wipe in along grid lines (clip-path), numbers count up. Reduced-motion: none.

**Avoid**: rounded corners > 4px, shadows, gradients, center alignment (use left alignment), more than 2 font weights.

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
