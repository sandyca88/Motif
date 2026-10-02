# Thumbnail image prompts (53 website prompts)

Use these with your own image tool (ChatGPT image, Midjourney, Ideogram, Recraft…). Then:

1. Generate at **16:10** (e.g. 1600×1000). Pick the most realistic, clean result.
2. Save as `motif-pack/build/thumb-images/<key>.webp` (or .jpg/.png), using the key shown below.
3. Run `python3 build.py`: the gallery uses your image instead of the live preview automatically.

**Base prompt (prefix every one):**

> Ultra-clean website design screenshot, 16:10, flat front-on view of a desktop browser viewport (no browser chrome, no device, no people's faces in focus), professional UI/UX, crisp typography rendered as clean readable text, realistic product/lifestyle photography where relevant, soft natural lighting, high detail, Dribbble/Awwwards quality, no watermark, no logos of real brands.

Tip: image tools often garble small text. Keep the headline short and include the exact words in quotes, or add the headline later in Figma.

- **`aurora`**: dark SaaS hero, drifting violet/cyan/pink aurora glow, huge white headline with one gradient word, pill buttons, faint logo row.
- **`ledger`**: dark analytics dashboard, left sidebar, four KPI tiles with green/red delta chips, purple area line chart, horizontal bar chart, table.
- **`hairline`**: developer-tool landing on near-black with faint hairline grid, lime accent, left-aligned bold headline, terminal window with colored log lines.
- **`folio`**: warm off-white editorial portfolio, oversized serif headline with an orange italic word, staggered case-study cards with soft photography.
- **`tiers`**: dark pricing section, three plan cards, middle card raised with violet-cyan gradient border and 'Most popular' ribbon, monthly/yearly toggle.
- **`bento`**: dark bento feature grid, mixed-size rounded tiles with mini UI, orbiting integration icons, glowing bar chart, big '38ms' stat.
- **`waitlist`**: pre-launch page, deep navy with soft blue-pink gradient mesh, big headline, pill email field with white button, glass countdown tiles.
- **`vault`**: light fintech landing, emerald accent, phone mockup with balance card and donut chart, floating white chips 'Bill paid ✓'.
- **`studio`**: bold agency homepage, near-black, gigantic grotesk wordmark split white/orange, uppercase meta row, project list with hover image.
- **`drop`**: single-product store, lavender tint, violet over-ear headphones floating with soft shadow, color swatches, black 'Add to bag' pill.
- **`summit`**: conference site, hot pink to violet gradient, condensed uppercase 'DESIGN SUMMIT 27', thin orbit rings, circular speaker portraits.
- **`horizon`**: cinematic footer, black space with glowing indigo horizon arc and stars, centered headline, footer columns, giant faint wordmark.
- **`pinboard`**: scrapbook résumé, linen board, pinned index cards with tape, polaroids, sticker skill chips, yellow sticky-note testimonial.
- **`spread`**: editorial magazine homepage, off-white paper, Didone masthead, scattered overlapping story cards with duotone photos.
- **`gate`**: sign-up screen split layout, left deep indigo gradient panel with testimonial, right clean white form with SSO buttons and strength meter.
- **`console`**: light SaaS settings page, left section nav, notification toggle matrix, red danger-zone card, black unsaved-changes bar.
- **`parley`**: dark AI chat app, history sidebar, streaming answer with tool-step checklist, citation chips, code block, rounded composer.
- **`manual`**: documentation site, white three-column layout, left nav tree, blue callout, dark code block with language tabs, right table of contents.
- **`lost`**: friendly 404 page, warm cream, huge coral '404', dotted path on an illustrated map with a question-mark pin, search field.
- **`pocket`**: three phone screens of a meal-planning app onboarding: orange welcome, preference chips, first plan with coach mark.
- **`halo`**: dark studio product launch, sleek AR glasses with cyan lens reflections floating over a reflective floor, minimal specs row.
- **`maison`**: quiet-luxury fashion store, beige, Didone wordmark header, large campaign photo of linen clothing, editorial product rail.
- **`ember`**: restaurant homepage, deep roast brown, warm ember lighting, top-down wood-fired dish on a plate, serif headline, orange 'Book a table'.
- **`stride`**: fitness app landing, near-black with electric lime accent, two phone mockups showing activity rings and workout player.
- **`wander`**: travel booking homepage, sunset coastal photo hero with rounded corners, white floating search bar, destination cards row.
- **`stage`**: musician release site, dark with magenta/violet album art square, giant condensed title, waveform preview player, tour dates.
- **`care`**: calm clinic website, soft teal, friendly headline, booking card with date chips and time slots, trust stats row.
- **`haven`**: real-estate site, modern house photo hero with Buy/Rent/Sold search, three listing cards with prices and status tags.
- **`learn`**: online course sales page, cream, serif headline with yellow highlighter, seats-left progress bar, curriculum card.
- **`kindred`**: nonprofit donation page, warm cream and coral, impact headline, goal progress bar, donation card with amount chips.
- **`shipped`**: dark changelog page, filter chips, timeline entries with version badges, colored tags, screenshot placeholders.
- **`dispatch`**: newsletter landing, warm paper, big serif title, single email field with orange button, list of recent issues.
- **`blockhaus`**: neo-brutalist SaaS, off-white, thick black borders, hard offset shadows, pink highlight word, tilted colorful UI cards.
- **`tiles`**: dark bento personal site, rounded tiles: intro with avatar, socials, map with glowing pin, music equalizer, featured project.
- **`configure`**: sneaker configurator, light studio stage with a coral sneaker, right options panel with swatches, materials, price and CTA.
- **`daybreak`**: bright AI startup hero, sunrise peach-to-lilac gradient, headline with orange serif italic, agent task card ticking off items.
- **`formvoid`**: monochrome architecture studio, thin column grid lines, full-width concrete building photo, project index list.
- **`roast`**: coffee brand store, cream background, tilted tomato-red coffee bag with mustard sticker, chunky serif headline, quiz button.
- **`encore`**: event ticketing, dark, pink-violet concert poster card with date badge, seat map with selected seats, hold timer.
- **`counsel`**: law firm homepage, ivory left with serif headline and trust stats, navy right panel listing practice areas with brass accents.
- **`tides`**: boutique seaside hotel, sunset over sea hero, elegant serif hotel name, white booking bar with dates.
- **`onair`**: podcast site, dark studio, cover art with amber 'on air' light, chaptered audio player, episode list.
- **`nest`**: interior design studio, warm neutrals, arch-shaped room photo, serif headline with olive italic, material swatches.
- **`signal`**: real-time analytics hero, deep navy, glowing violet-to-cyan streaming line chart, lime counter, floating event chips.
- **`ronin`**: cinematic game landing, original lone warrior in flowing robes with a long blade on mossy temple steps, giant red sun disc, falling pink petals, massive ivory brush-stroke title "RONIN DAWN" behind the character, red 'Wishlist now' button.
- **`nova`**: full-bleed coral landing, white headline "Fewer tabs. More focus.", glossy original white-and-teal rounded 3D device floating over an orange base, small white UI chips, minimal nav.
- **`tidewater`**: paper-white site with a detailed ink/pencil crosshatched sketch of a backyard pool with pergola, trees and loungers, navy 'Request a quote' pill, headline "Your backyard, reimagined."
- **`meridian`** (generated ✓): hand-drawn ink/pencil sketch of NYC skyscrapers looking up an avenue, MERIDIAN nav, navy 'Book a viewing', headline "Live above the city."
- **`jade`** (generated ✓): wuxia game landing, heroine in ivory/jade/crimson hanfu with a jian on temple stairs, misty peaks, plum blossoms, ivory brush title "JADE PAVILION", red 'Wishlist now'.
- **`aero`** (generated ✓): sky-blue tech launch, original slim matte-black smart glasses floating, headline "See it. Say it. Share it.", 'from $299', glass chips.
- **`lumenfold`** (generated ✓): minimal light-grey keynote hero, 'Lumen Fold / Open up.', blue pill buttons, original foldable phone held in two hands.
- **`ember1`** (generated ✓): coral full-bleed, 'Less noise. More you.', glossy pearl phone with teal camera on a pedestal, chips, gold sphere, cubes.
- **`lumora`** (Gemini video ✓, 8–10s loop): glossy iridescent pearl orb slowly rotating above pastel clouds at golden hour, particles, slow push-in. Save as `lumora.mp4` (plus a `lumora.webp` poster); the site plays it as an animated thumbnail.
