"""Generates the 8 deck-style skills. Each is self-contained: shared deck engine + a distinct style spec."""
import os
ROOT = os.path.dirname(os.path.dirname(__file__))

ENGINE = """
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
"""

STYLES = [

 dict(name="deck-clearview", title="Clearview", tier="Free",
  desc="Create clean, minimalist product-keynote slide decks: bright white canvas, near-black ink, one crisp blue accent, huge centered headlines, product hero visuals floating in whitespace, soft shadows and precise system typography. Use for product launches, feature announcements, company updates, design reviews, or when the user asks for a clean, minimal, elegant, white, premium tech-keynote or 'simple but beautiful' deck.",
  style="""## Style: Clearview

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

**Sample**: see `examples/sample-deck.html` (8 slides) for a complete deck in this style."""),

 dict(name="deck-toybox-bots", title="Toybox Bots", tier="Pro",
  desc="Create playful, colorful slide decks starring a cast of original chunky 3D-style robot mascots built from CSS/SVG shapes, with candy colors, soft clay shading, rounded bold type and sticker-like UI. Use for product onboarding, kids/education, community and developer relations talks, fun internal all-hands, AI assistant explainers, or when the user asks for a cute, playful, mascot, character, 3D, toy-like or fun deck.",
  style="""## Style: Toybox Bots

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

**Avoid**: realistic robots, weapons, scary faces, more than 3 bots on a content slide, any resemblance to known franchises or mascots."""),

 dict(name="deck-chroma-launch", title="Chroma Launch", tier="Pro",
  desc="Create bold, high-energy launch decks with saturated gradient-mesh backgrounds, huge tight display type, glossy product reveals, animated number counters and punchy one-line slides. Use for product launches, app announcements, marketing kickoffs, creator or brand pitches, sales kickoffs, or when the user asks for a vibrant, colorful, gradient, hype or modern launch deck.",
  style="""## Style: Chroma Launch

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

**Avoid**: more than 4 colors per slide, small text, paragraphs, stock photos."""),

 dict(name="deck-obsidian", title="Obsidian", tier="Free",
  desc="Create premium dark keynote-style slide decks: deep black canvas, one luminous gradient accent, oversized statement typography, glass cards, glowing data and cinematic pacing. Use for investor pitches, product launches, strategy presentations, all-hands, conference talks, or when the user asks for a professional, premium, sleek, dark, modern, Apple-keynote-like (but original) or impressive deck.",
  style="""## Style: Obsidian

**Mood**: a flagship keynote. Confident, calm, expensive-looking. Every slide gets one idea and plenty of dark space.

| Token | Value |
|-------|-------|
| Canvas | `#050507` with a very subtle radial lift at the top (`radial-gradient(1200px 600px at 50% -10%, rgba(124,92,255,.18), transparent)`) |
| Surface (glass) | `rgba(255,255,255,.04)`, 1px border `rgba(255,255,255,.08)`, radius 28px, `backdrop-filter: blur(20px)` |
| Ink | `#F5F5F7`; muted `#8E8E96`; hairlines `rgba(255,255,255,.08)` |
| Accent gradient | `linear-gradient(90deg,#7C5CFF,#22D3EE)`: only for key numbers, one word per title, and chart highlights |
| Glow | accent at 35–45% opacity, blurred 80–120px, placed behind the focal element only |
| Fonts | display: "Inter Tight" / "SF Pro Display" 600–700 at −0.045em tracking; body 400 at 28–32px; mono labels ("JetBrains Mono") 18px uppercase, +0.12em tracking |

**Motifs**: kicker labels in mono ("02 — MARKET"); one gradient word per title; oversized numerals (240–360px) with gradient fill; glass cards for groups of 3; thin hairline dividers; a subtle glow behind the hero element; slide counter + deck name in the footer at 16px muted.

**Archetypes**
- *Title*: kicker, 2-line title (≤ 8 words) with one gradient word, presenter/date line, glow behind the title.
- *Statement*: one sentence at 88–104px across ~70% width, left aligned.
- *Big number*: gradient numeral + one-line meaning + source footnote.
- *Three pillars*: three glass cards, each with an icon (1.5px stroke), 3-word title, one sentence.
- *Chart*: single chart, grey series with one gradient-highlighted series/bar, direct labels, takeaway on the right.
- *Product*: device frame (CSS/SVG) with screenshot placeholder, 2–3 floating callout chips.
- *Roadmap*: horizontal track with 3–4 milestones, current one glowing.
- *Comparison*: us vs. alternatives table; our column tinted with the accent at 8%.
- *Quote*: large quote, attribution with small avatar circle.
- *The ask*: what you want (amount / decision / next step), 3 uses of funds or actions, contact line.

**Motion**: slide content fades up 24px with 60ms stagger; numbers count up; glow breathes slowly (6s). Reduced-motion: static.

**Avoid**: more than one accent gradient per slide, pure white backgrounds, stock photos with text over them, drop shadows on dark, more than 3 cards per row.

**Sample**: see `examples/sample-deck.html` for a complete 10-slide deck built in this style. Reuse its structure and CSS, and replace the content."""),
 dict(name="deck-marker-margin", title="Marker Margin", tier="Free",
  desc="Create hand-drawn sketchnote-style slide decks: marker headlines, highlighter swipes, doodled arrows, boxes and icons on warm paper. Use for workshops, explainers, teaching, retros, onboarding talks, or when the user asks for a sketchnote, doodle, whiteboard, hand-drawn or friendly visual-notes presentation.",
  style="""## Style: Marker Margin

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

**Avoid**: perfect geometry, drop shadows, gradients, stock icons."""),

 dict(name="deck-kraft-journal", title="Kraft Journal", tier="Free",
  desc="Create field-journal style slide decks that look like a researcher's notebook: kraft and grid paper, taped photos, stamped labels, typewriter captions and margin notes. Use for research readouts, user interview findings, travel/field reports, case studies, design research shares, or when the user asks for a notebook, journal, field notes or scrapbook-style deck.",
  style="""## Style: Kraft Journal

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

**Avoid**: glossy gradients, perfect alignment everywhere (1–3° rotation on cards is the charm), more than 4 items per slide."""),

 dict(name="deck-paper-collage", title="Paper Collage", tier="Pro",
  desc="Create cut-paper collage slide decks with layered construction-paper shapes, torn edges, soft paper shadows and friendly inclusive illustrations built from simple shapes. Use for community, education, nonprofit, DEI, culture, event or storytelling presentations, or when the user asks for a cut-paper, collage, papercraft or handmade-feel deck.",
  style="""## Style: Paper Collage

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

**Avoid**: stereotyped depictions, photo-realism, thin line icons (everything should feel cut from paper)."""),

 dict(name="deck-grid-signal", title="Grid Signal", tier="Pro",
  desc="Create Swiss/International-style system slide decks: strict 12-column grid, bold sans typography, one signal color, big numbers, visible structure and data-forward layouts. Use for product strategy, design systems, engineering reviews, quarterly business reviews, investor updates, or when the user asks for a clean, modernist, Swiss, systematic or bold minimal deck.",
  style="""## Style: Grid Signal

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

**Avoid**: rounded corners > 4px, shadows, gradients, center alignment (use left alignment), more than 2 font weights."""),

 dict(name="deck-serif-quarterly", title="Serif Quarterly", tier="Pro",
  desc="Create editorial magazine-style slide decks with elegant serif typography, warm ochre and cream tones, pull quotes, drop caps, photo-led layouts and generous whitespace. Use for brand stories, keynotes, culture decks, creative pitches, annual reviews, portfolio presentations, or when the user asks for an editorial, magazine, elegant, luxury or storytelling deck.",
  style="""## Style: Serif Quarterly

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

**Avoid**: bold sans headlines, bright saturated colors, bullet lists (write in sentences), cramming."""),

 dict(name="deck-frost", title="Frost", tier="Pro",
  desc="Create soft glassmorphism slide decks: frosted translucent panels over drifting pastel sky gradients, soft glow, rounded cards and airy typography. Use for AI/product launches, app showcases, tech keynotes, wellness or future-facing vision decks, or when the user asks for a glass, frosted, dreamy, soft gradient or modern Apple-like-but-original deck.",
  style="""## Style: Frost

**Mood**: light, optimistic, futuristic.

| Token | Value |
|-------|-------|
| Sky background | layered radial gradients: `#BFD9FF`, `#E6D5FF`, `#FFE2F0`, `#D6F5FF` on `#F4F7FF` |
| Glass | `rgba(255,255,255,.45)`, `backdrop-filter: blur(24px) saturate(160%)`, 1px border `rgba(255,255,255,.7)`, inner highlight |
| Ink | `#16213A`; muted `#5B6785` |
| Accent | `#5B6CFF` → `#A17BFF` gradient for key numbers only |
| Fonts | airy geometric sans ("Plus Jakarta Sans", "SF Pro Display") 600 for titles, 400 body 28–32px |

**Motifs**: floating glass cards with 32px radius, soft orbs behind glass (blurred circles), subtle light streaks, device frame placeholders (phone/laptop) rendered as glass outlines.

**Archetypes**
- *Title*: centered title on one large glass panel, orbs drifting behind.
- *Feature trio*: three glass cards floating at different depths (slight y offsets).
- *Product shot*: glass device frame with screenshot placeholder + 2 callout chips.
- *Key stat*: gradient number inside a glowing glass circle.
- *Roadmap*: horizontal glass track with milestone pills.
- *Comparison*: two glass columns, recommended one brighter with glow.
- *Closing*: title + CTA pill on glass, orbs converge.

**Motion**: orbs drift slowly (20s), cards float in with blur → sharp. Reduced-motion: static.

**Contrast rule**: always test text on glass over the brightest gradient area; add a stronger white overlay if contrast < 4.5:1.

**Avoid**: dark backgrounds, heavy borders, more than 3 glass layers stacked."""),

 dict(name="deck-pop-riso", title="Pop Riso", tier="Pro",
  desc="Create risograph-print style slide decks: two or three spot colors with overprint blending, halftone textures, misregistration offsets, bold stacked type and confetti-like shapes. Use for creative events, community gatherings, launches, marketing kickoffs, zine-style talks, or when the user asks for a riso, print, zine, poster, energetic, party or bold colorful deck.",
  style="""## Style: Pop Riso

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

**Avoid**: more than 3 spot colors, gradients, thin fonts, small text (min 28px)."""),

 dict(name="deck-boardroom-storyline", title="Boardroom Storyline", tier="Pro",
  desc="Create consulting-style storyline decks for executives: action titles, pyramid-principle structure, executive summary, clean charts with callouts, recommendation and next-steps slides. Use for strategy recommendations, business cases, board or leadership updates, proposals, market analyses, or when the user asks for a consulting, McKinsey-style, executive, business or professional deck.",
  style="""## Style: Boardroom Storyline

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

**Motion**: none or minimal (builds only when presenting live). **Avoid**: decorative imagery, more than one message per slide, 3D charts."""),
]

for s in STYLES:
    d = os.path.join(ROOT, "skills", s["name"]); os.makedirs(d, exist_ok=True)
    body = f"""---
name: {s['name']}
description: {s['desc']}
license: Commercial. See LICENSE.txt
---

# {s['title']} Deck

Build a complete, presentable slide deck in the **{s['title']}** visual style: storyline first, then design. The result should look like a designer made it, not a template.
{s['style']}
{ENGINE}"""
    open(os.path.join(d, "SKILL.md"), "w").write(body)
print("wrote", len(STYLES))
