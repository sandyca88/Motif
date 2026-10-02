# Motif website-prompt format

File: `motif-pack/prompts/motif-website-prompts.md`. Each prompt is a heading + fenced block, then `---`. Insert new prompts **before** the final `*© Motif…*` line, and add a row to the index table at the top (keep the "NN original" count in the intro sentence current).

```
## NN · Name — Short Descriptor  `PRO`        ← or `FREE`; exactly two spaces before the backticks

(fenced block containing the prompt)

---
```

The build reads prompts with the regex `## (\d\d) · (.+?)  \`(FREE|PRO)\`\n\n\`\`\`\n(.*?)\`\`\``. Anything after `HERO IMAGE PROMPT` / `VIDEO PROMPT` is shown free on the site as "copy the image prompt".

## Structure inside the block

1. **Opening line:** `Create a [type] site for "[BRAND]", a [what it is]. [Mood in one sentence].`
2. **STYLE (or STYLE ANALYSIS):** palette with hex values and one named accent, type (sizes, weights, tracking), frame details, signature graphic idea.
3. **SECTIONS:** numbered, hero first; each with concrete components, copy placeholders in `[BRACKETS]` and one interaction.
4. **MOTION:** what animates, durations, performance (pause off-screen), `prefers-reduced-motion` fallback.
5. **RULES:** original brand/product, no real logos or people, AA contrast notes, accessibility (keyboard, labels), honest data ("sample" labels).
6. **HERO IMAGE PROMPT (16:10):** subject, material, lighting, camera, palette, *"lots of empty space on the [left] for a headline"*, *"no text, no logos, no watermark"*.
7. **VIDEO PROMPT (16:9, 8 s)** when the template is motion-first: one subject, one slow action, *"seamless loop"*, *"very slow cinematic camera drift"*, no text/logos. For image-to-video add *"Keep the exact composition and keep all text, menu and buttons completely still. Animate only …"*.

Free prompts: complete and generous (they sell Pro). Pro prompts: richer sections, configurators, motion specs, video prompt.

## Example (trimmed)

```
Create a bold launch page for "[PHONE NAME]", an original smartphone by [BRAND], using a single-color "toy-like premium" style …

STYLE ANALYSIS (what makes this look work — keep all of it):
- One full-bleed warm color [coral #E36A4C] everywhere in the hero …
- White typography only: tiny spaced uppercase kicker (11px, +0.2em), huge two-line headline (96–120px, −0.05em) …

SECTIONS:
1. Hero as above. The phone bobs slowly (6s) and tilts toward the cursor (max 6°) …
2. Camera: dark section, giant lens close-up, 3 stats with counters …

RULES: original phone design, name and logo — no real brand's product, logo or UI; check contrast …

HERO IMAGE PROMPT (16:10):
"Glossy 3D product render of an original sleek smartphone in pearl white …, full-bleed warm coral orange background, soft studio lighting, premium, no logos, no text, no watermark."
```

## Naming

Short, ownable, not a real company (check the existing list for clashes). Pattern used: evocative noun + descriptor ("Fall Line — Downhill Ski Race Event", "Lattice — Particle Sphere Intelligence Hero (Video + Canvas)").
