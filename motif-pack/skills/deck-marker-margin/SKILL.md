---
name: deck-marker-margin
description: Create hand-drawn sketchnote-style slide decks: marker headlines, highlighter swipes, doodled arrows, boxes and icons on warm paper. Use for workshops, explainers, teaching, retros, onboarding talks, or when the user asks for a sketchnote, doodle, whiteboard, hand-drawn or friendly visual-notes presentation.
license: Commercial. See LICENSE.txt
---

# Marker Margin Deck

Build a complete, presentable slide deck in the **Marker Margin** visual style: storyline first, then design. The result should look like a designer made it, not a template.
## Style: Marker Margin

**Mood**: a smart friend explaining on a whiteboard. Warm, clear, a bit playful.

| Token | Value |
|-------|-------|
| Paper | `#FBF7EE` with a faint dotted grid (`radial-gradient` 1px dots, 28px) |
| Ink | `#1E1B18` |
| Highlighter | `#FFE14D` (primary), `#9BE7C4`, `#FFB4C2` |
| Accent ink | `#2F6BFF` for arrows and callouts |
| Headline font | a marker/handwritten face (e.g. "Permanent Marker", "Caveat Brush"; fallback `"Comic Neue", "Segoe Print", cursive`) |
| Body font | rounded sans ("Nunito", system-ui) 28–34px |

**Motifs (SVG)**: wobbly hand-drawn rectangles (paths with slight jitter, not perfect `rect`s), curved arrows with open arrowheads, underline squiggles, highlighter swipes behind key words (rotated −1°, 60% opacity, rough edges), stick-figure/icon doodles drawn with 3–4px round-cap strokes.

**Archetypes**
- *Title*: huge marker headline, one highlighted word, small doodle top-right, presenter + date bottom-left.
- *Big question*: centered question, arrow curving to a sticky note with the answer teaser.
- *Three ideas*: three sketched boxes connected by arrows, each with a doodle icon + 6-word caption.
- *Before → After*: two panels, left crossed-out scribble, right checkmarked.
- *Key stat*: giant marker number with circle scribble around it + one sentence.
- *Process*: numbered bubbles along a hand-drawn path.
- *Quote*: large quote with a hand-drawn speech bubble.
- *Recap*: checklist with hand-drawn checkboxes being ticked (animate stroke-dashoffset).

**Motion**: strokes draw in (`stroke-dasharray` animation, 600ms), highlighters wipe left→right. Respect `prefers-reduced-motion`.

**Avoid**: perfect geometry, drop shadows, gradients, stock icons.

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
