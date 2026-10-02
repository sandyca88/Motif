# Reference → original

Sandy often shares a site (Aura templates, MotionSites, Skillry, Fluxa, x.ai, havenorbi…) or a screenshot and says "make one like this". The job is to capture **why it works**, then build something new.

## 1. Look at it properly

- JS-rendered pages (Aura, Netlify/Framer builds) return empty HTML to web_fetch. Open them in the **built-in browser** (`preview_start` → `get_page_text` / screenshot). Request access per site.
- Claude-in-Chrome background tabs often render **blank** screenshots; read the DOM with JS instead, or use the built-in browser.
- Read computed styles for fonts and colors (`getComputedStyle` on h1, p, buttons) rather than guessing.

## 2. Write a style analysis (6 layers)

| Layer | Questions |
|---|---|
| Color | One saturated field or neutral + one accent? Where does the accent appear? |
| Type | Family feel, weight, tracking, line-height, which word is highlighted and how (color vs gradient vs serif italic) |
| Hero object | What is it, material, lighting, angle, what it rests on |
| Props | Chips, spheres, particles, cards: how many, what depth |
| Frame | Nav style, corner micro-labels, scroll hints, bottom bars, dividers, grid lines |
| Motion | What moves, speed, what reacts to the cursor/scroll |

## 3. Change everything identifiable

- New product name, brand name, headline and copy (e.g. reference "Omi · Architect the Invisible" → Motif "Lattice · See the shape of your data").
- New subject and composition (different object, different layout ratio, different sections).
- No real brands/products/logos/UI (say "an original foldable phone", never a named product). No real people's likeness. No named characters.
- Don't reuse anyone's prompt text, video, illustration, logo, mascot or code, even if visible or "free to remix" on their platform.
- Check for **name clashes** with existing Motif items (we had two "Halo"s; #64 became "Lattice").

## 4. What may be listed from others

- Free skills/repos: only as **credited link-out** cards (`ext` + optional `site`), after reading the LICENSE (raw.githubusercontent.com/<owner>/<repo>/main/LICENSE, or README "License" section). Record license in `FREE-PICKS.md`. Never re-host or sell.
- Paid or "remix inside our platform" content (Aura community templates, Skillry, MotionSites): **never copy**. Offer originals in the same genre instead.
- Trademark-y inspirations (Apple, Meta glasses, Grok bot): make the *genre* (minimal keynote, smart glasses, friendly bot mark) with original names and shapes.

## 5. Deliver

Original prompt (see `prompt-format.md`) + art + storefront item. Tell Sandy in one line what was taken as inspiration and what was changed.
