---
name: deck-toybox-bots
description: Create playful, colorful slide decks starring a cast of original chunky 3D-style robot mascots built from CSS/SVG shapes, with candy colors, soft clay shading, rounded bold type and sticker-like UI. Use for product onboarding, kids/education, community and developer relations talks, fun internal all-hands, AI assistant explainers, or when the user asks for a cute, playful, mascot, character, 3D, toy-like or fun deck.
license: Commercial. See LICENSE.txt
---

# Toybox Bots Deck

Build a complete, presentable slide deck in the **Toybox Bots** visual style: storyline first, then design. The result should look like a designer made it, not a template.
## Style: Toybox Bots

**Mood**: friendly, curious, a little mischievous. Complex ideas explained by a cast of little robots.

| Token | Value |
|-------|-------|
| Canvas | midnight `#12162B` with a faint 64px tile grid, or cream `#FFF7EC` for light decks |
| Candy palette | berry `#FF4D8D`, grape `#8B5CF6`, mint `#2ED3A0`, sky `#3BA7FF`, sun `#FFC53D`, tangerine `#FF7A2F` |
| Clay shading | each shape: base color + `inset -10px -14px 24px rgba(0,0,0,.22)` + `inset 8px 10px 18px rgba(255,255,255,.35)` for a soft 3D look |
| Fonts | rounded heavy display ("Nunito" 900 / "Baloo 2" 800) at −0.02em; body "Nunito" 600 28–32px |

**Cast (define once, reuse everywhere)**: 4–6 ORIGINAL bots, each with a name, one color, one head shape (capsule, cube, dome, gumdrop), one eye style (visor, two dots, single lens) and one prop (antenna, propeller, headphones, leaf). Build them as reusable SVG/CSS components with poses: *wave*, *point*, *think*, *celebrate*, *carry box*. Never draw existing characters, mascots or brand robots.

**Motifs**: bots peeking from slide edges; speech bubbles; sticker badges (white 6px outline, slight rotation); rounded tiles like toy blocks; confetti dots; progress shown as a bot climbing steps.

**Archetypes**
- *Title*: cast lineup on colored tiles (grid of 4–8), big rounded title.
- *Meet the problem*: one bot looking confused next to a tangled line.
- *How it works*: 3 steps, each "performed" by a different bot with a pose.
- *Big number*: number on a giant toy block, bot celebrating.
- *Feature trio*: three sticker cards, each with a bot icon.
- *Roadmap*: bot climbing a staircase of milestones.
- *Q&A / end*: all bots waving + clear next step.

**Motion**: bots bounce in with overshoot (`cubic-bezier(.34,1.56,.64,1)`), idle bob 3s, blink every 4s. Reduced-motion: static poses.

**Avoid**: realistic robots, weapons, scary faces, more than 3 bots on a content slide, any resemblance to known franchises or mascots.

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
