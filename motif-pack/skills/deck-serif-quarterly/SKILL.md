---
name: deck-serif-quarterly
description: Create editorial magazine-style slide decks with elegant serif typography, warm ochre and cream tones, pull quotes, drop caps, photo-led layouts and generous whitespace. Use for brand stories, keynotes, culture decks, creative pitches, annual reviews, portfolio presentations, or when the user asks for an editorial, magazine, elegant, luxury or storytelling deck.
license: Commercial. See LICENSE.txt
---

# Serif Quarterly Deck

Build a complete, presentable slide deck in the **Serif Quarterly** visual style: storyline first, then design. The result should look like a designer made it, not a template.
## Style: Serif Quarterly

**Mood**: a beautifully printed magazine. Calm, considered and premium.

| Token | Value |
|-------|-------|
| Paper | `#F5EFE4` |
| Ink | `#1C1A17` |
| Ochre | `#C8872B` (accent), deep olive `#4B4A2E` (secondary) |
| Fonts | high-contrast display serif ("Playfair Display", "Instrument Serif", "Fraunces") with *italic* for emphasis; body serif ("Source Serif", Georgia) 28px; small caps sans for kickers |

**Motifs**: kicker labels in spaced small caps ("THE BRIEF · ISSUE 04"), drop caps on narrative slides, thin double rules, pull quotes with oversized quotation marks in ochre, photo frames with generous white borders and captions in italic, page folios ("— 07 —").

**Archetypes**
- *Cover*: masthead-style title, issue line, full-bleed image placeholder with title overlaid in the lower third.
- *Feature opener*: huge serif headline with one italic word, standfirst paragraph.
- *Narrative*: two-column text with drop cap (only use for ≤ 60 words).
- *Pull quote*: 1 quote at 72–96px with attribution.
- *Photo essay*: one large + two small image frames with captions.
- *By the numbers*: 3 stats in serif numerals with italic labels.
- *Contents*: numbered list like a magazine table of contents.
- *Closing*: sign-off letter style with signature line and next step.

**Motion**: slow fades (900ms), images reveal with a subtle scale 1.04 → 1. Reduced-motion: fades only.

**Avoid**: bold sans headlines, bright saturated colors, bullet lists (write in sentences), cramming.

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
