---
name: deck-boardroom-storyline
description: Create consulting-style storyline decks for executives: action titles, pyramid-principle structure, executive summary, clean charts with callouts, recommendation and next-steps slides. Use for strategy recommendations, business cases, board or leadership updates, proposals, market analyses, or when the user asks for a consulting, McKinsey-style, executive, business or professional deck.
license: Commercial. See LICENSE.txt
---

# Boardroom Storyline Deck

Build a complete, presentable slide deck in the **Boardroom Storyline** visual style: storyline first, then design. The result should look like a designer made it, not a template.
## Style: Boardroom Storyline

**Mood**: crisp, credible, decision-ready.

| Token | Value |
|-------|-------|
| Background | `#FFFFFF` |
| Ink | `#0E1A2B`; muted `#5E6B7D`; rules `#D9DEE5` |
| Primary | deep navy `#0B2A5B`; highlight teal `#0FA3A3` used only to mark "the answer" |
| Fonts | "Inter" / "Source Sans" : action titles 40–44px semibold, body 24–28px; footnotes 14px |

**Storyline method (required)**
1. Write the governing thought (the recommendation) in one sentence.
2. Support it with 3 key arguments (MECE). Each argument gets 1–3 evidence slides.
3. Every slide title is an *action title*: a full sentence ≤ 2 lines stating the takeaway.
4. The deck must read as a coherent story from titles alone. Include a "title-only" read-through in your response.

**Archetypes**
- *Executive summary*: situation → complication → resolution in 3 short blocks + the ask.
- *Key argument*: action title, chart on the left 60%, 3 callout bullets on the right 40%.
- *Waterfall / bridge*: explaining change between two numbers.
- *2×2 matrix*: options plotted, recommended quadrant highlighted in teal.
- *Options comparison*: table with criteria rows, Harvey balls, recommended column highlighted.
- *Roadmap*: 3 phases with milestones, owners and dates.
- *Risks & mitigations*: two-column table.
- *Next steps / decision required*: numbered actions with owner + date, and the explicit decision needed.

**Details**: source line bottom-left on every data slide ("Source: …"), tracker in top-right showing the section, page numbers, footnote markers.

**Motion**: none or minimal (builds only when presenting live). **Avoid**: decorative imagery, more than one message per slide, 3D charts.

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
