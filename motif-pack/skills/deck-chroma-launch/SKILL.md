---
name: deck-chroma-launch
description: Create bold, high-energy launch decks with saturated gradient-mesh backgrounds, huge tight display type, glossy product reveals, animated number counters and punchy one-line slides. Use for product launches, app announcements, marketing kickoffs, creator or brand pitches, sales kickoffs, or when the user asks for a vibrant, colorful, gradient, hype or modern launch deck.
license: Commercial. See LICENSE.txt
---

# Chroma Launch Deck

Build a complete, presentable slide deck in the **Chroma Launch** visual style: storyline first, then design. The result should look like a designer made it, not a template.
## Style: Chroma Launch

**Mood**: launch day. Loud color, tight type, and fast pacing, while staying disciplined with one idea per slide.

| Token | Value |
|-------|-------|
| Mesh backgrounds | 3–4 blurred radial blobs per slide from a set: electric violet `#6C2BFF`, hot coral `#FF4F5E`, tangerine `#FF9F1C`, aqua `#00D1C1`, deep ink `#0B0620` |
| Ink | white `#FFFFFF` on mesh; `#0B0620` on light slides |
| Fonts | tight grotesk display ("Inter Tight" 800 / "Clash Display" alt) at −0.055em, 140–220px; body 500 at 30px |
| Glass chips | `rgba(255,255,255,.14)`, blur 16px, 1px `rgba(255,255,255,.3)` border |

**Motifs**: one-line slides with a single huge word; product on a glossy pedestal (radial highlight + reflection); number counters; marquee strips of benefits; stickers ("NEW", "v2.0"); a grain overlay at 6% so gradients don't band.

**Archetypes**
- *Countdown opener*: "3 · 2 · 1" or date, mesh pulsing.
- *Hero reveal*: product on pedestal, name in 200px type.
- *One-word slides*: "Faster." / "Smarter." / "Yours." in sequence.
- *Feature chips*: 4–6 glass chips floating around the product.
- *Big stat*: counter with gradient glow.
- *Pricing / availability*: price in huge type, date, CTA chip.
- *Finale*: brand wordmark + URL + QR placeholder.

**Motion**: mesh blobs drift (10s), words slam in (scale 1.15 → 1, 350ms), counters count up. Reduced-motion: static mesh, fades.

**Contrast rule**: check white text over the lightest blob. Add a 20–30% dark overlay behind text when needed.

**Avoid**: more than 4 colors per slide, small text, paragraphs, stock photos.

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
