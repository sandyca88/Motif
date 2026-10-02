---
name: deck-pop-riso
description: Create risograph-print style slide decks: two or three spot colors with overprint blending, halftone textures, misregistration offsets, bold stacked type and confetti-like shapes. Use for creative events, community gatherings, launches, marketing kickoffs, zine-style talks, or when the user asks for a riso, print, zine, poster, energetic, party or bold colorful deck.
license: Commercial. See LICENSE.txt
---

# Pop Riso Deck

Build a complete, presentable slide deck in the **Pop Riso** visual style: storyline first, then design. The result should look like a designer made it, not a template.
## Style: Pop Riso

**Mood**: loud, joyful, printed-poster energy.

| Token | Value |
|-------|-------|
| Paper | `#FFF6E8` |
| Spot colors (pick 2–3) | fluorescent pink `#FF48B0`, blue `#0078BF`, yellow `#FFE800`, green `#00A95C` |
| Blend | shapes use `mix-blend-mode: multiply` so overlaps create new colors like real overprint |
| Fonts | ultra-bold condensed display ("Anton", "Bebas Neue", "Archivo Black") UPPERCASE; body "Space Grotesk" 28px |

**Motifs**: halftone dot fill (SVG pattern of circles); misregistration: duplicate the headline in a second spot color offset 4–6px behind; grain overlay; stars, bursts, squiggles and half-circles as confetti; stacked headlines that fill the slide width.

**Archetypes**
- *Poster title*: stacked 3-line headline filling width, overprinted shapes, date/venue in a sticker circle.
- *Agenda*: numbered bold rows with a color bar behind each.
- *Big word*: one word, full-bleed, misregistered.
- *Stat burst*: number inside a starburst shape with halftone shadow.
- *People / speakers*: portrait frames as halftone duotone circles.
- *Three things*: three colored blocks overprinting each other with labels.
- *Finale*: giant CTA, confetti shapes everywhere.

**Motion**: shapes pop in with overshoot (`cubic-bezier(.34,1.56,.64,1)`), headline layers slide into registration. Reduced-motion: none.

**Avoid**: more than 3 spot colors, gradients, thin fonts, small text (min 28px).

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
