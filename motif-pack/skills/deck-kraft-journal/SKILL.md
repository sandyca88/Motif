---
name: deck-kraft-journal
description: Create field-journal style slide decks that look like a researcher's notebook: kraft and grid paper, taped photos, stamped labels, typewriter captions and margin notes. Use for research readouts, user interview findings, travel/field reports, case studies, design research shares, or when the user asks for a notebook, journal, field notes or scrapbook-style deck.
license: Commercial. See LICENSE.txt
---

# Kraft Journal Deck

Build a complete, presentable slide deck in the **Kraft Journal** visual style: storyline first, then design. The result should look like a designer made it, not a template.
## Style: Kraft Journal

**Mood**: evidence from the field. Tactile, honest, observational.

| Token | Value |
|-------|-------|
| Page | `#F3EEE3` with 32px pale-blue grid lines (`#DCE4EC`) |
| Kraft | `#C9A77C` card stock for tabs and labels |
| Ink | `#23201C`; margin notes in `#B4412E` |
| Tape | semi-transparent `rgba(255,236,170,.75)` strips, rotated ±4° |
| Fonts | typewriter mono for labels ("Courier Prime", "IBM Plex Mono"); serif body ("Source Serif", Georgia) 28–32px; handwritten margin notes ("Caveat") |

**Motifs**: photo frames as white polaroid cards with tape corners; rubber-stamp labels (outlined uppercase mono, rotated −3°, slightly faded); index tabs on the page edge showing section; paper clips (SVG); red handwritten margin arrows pointing at insights; "Fig. 3" style captions.

**Archetypes**
- *Title*: journal cover: kraft background, stamped title label, "Vol. / Date / Location" typewriter line.
- *Observation*: taped photo placeholder left, typewriter observation right, red margin note with the insight.
- *Quote wall*: 3–4 index cards with participant quotes, pinned at slight angles, participant IDs stamped.
- *Pattern*: grid-paper tally or affinity cluster (sticky notes grouped with hand circles).
- *Key finding*: stamped "FINDING 02" + one serif sentence + evidence count ("7 of 9 participants").
- *Map / journey*: dotted route on grid paper with numbered pins.
- *Recommendation*: checklist on lined paper with priority stamps (NOW / NEXT / LATER).

**Motion**: cards drop in with a small rotate + settle (spring-like ease), stamps "thunk" (scale 1.2 → 1). Reduced-motion: simple fades.

**Avoid**: glossy gradients, perfect alignment everywhere (1–3° rotation on cards is the charm), more than 4 items per slide.

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
