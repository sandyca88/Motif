---
name: deck-paper-collage
description: Create cut-paper collage slide decks with layered construction-paper shapes, torn edges, soft paper shadows and friendly inclusive illustrations built from simple shapes. Use for community, education, nonprofit, DEI, culture, event or storytelling presentations, or when the user asks for a cut-paper, collage, papercraft or handmade-feel deck.
license: Commercial. See LICENSE.txt
---

# Paper Collage Deck

Build a complete, presentable slide deck in the **Paper Collage** visual style: storyline first, then design. The result should look like a designer made it, not a template.
## Style: Paper Collage

**Mood**: handmade, warm, welcoming and human.

| Token | Value |
|-------|-------|
| Background | `#FFF8EF` |
| Paper palette | tomato `#F2613F`, marigold `#F7B32B`, teal `#1F8A8A`, lilac `#B8A1E3`, leaf `#5DAA68`, ink `#222` |
| Skin-tone set (for figures) | `#F4D2B5`, `#E0AC7E`, `#B97A4F`, `#8A5530`, `#5A3825` (use a diverse mix) |
| Fonts | chunky friendly display ("Fraunces" 900 soft, or "Recoleta"); body "DM Sans" 28–32px |

**Motifs**: shapes with a subtle paper grain (SVG `feTurbulence` at low opacity) and a soft offset shadow (`drop-shadow(4px 6px 0 rgba(0,0,0,.12))`); torn-edge dividers (jagged SVG paths); abstract people made of circles + rounded rectangles (no facial detail needed) in diverse tones; confetti of paper dots and squiggles; layered hills/suns/leaves as backgrounds.

**Archetypes**
- *Title*: big collage scene (sun, hills, 3–5 paper figures) with title on a torn paper banner.
- *Story beat*: left half collage illustration, right half one sentence.
- *Three pillars*: three paper cards in different colors, each with a simple cut-paper icon.
- *Big number*: number cut from paper (thick display, layered shadow) + caption.
- *People*: row of paper figures with names/roles on paper tags.
- *Timeline*: torn-paper ribbon with milestones as paper circles.
- *Call to action*: hand-shaped / heart / door collage + a clear ask.

**Motion**: layers slide in with parallax offsets (back layer first), gentle 2° wobble on hover. Reduced-motion: none.

**Avoid**: stereotyped depictions, photo-realism, thin line icons (everything should feel cut from paper).

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
