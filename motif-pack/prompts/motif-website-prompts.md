# Motif — AI Website Prompts

64 original, copy-paste prompts for Lovable, Bolt, v0, Cursor and Claude. Each prompt is written like a design brief: direction, layout, motion, copy and accessibility — so the output looks designed, not generated.

**How to use:** copy the whole block inside the code fence → paste into your builder → swap the `[BRACKETS]` for your content. For Cursor/Claude Code, add "Use React + Tailwind" (or your stack) at the top.

| # | Name | Type | Tier |
|---|------|------|------|
| 01 | Aurora — AI SaaS Hero | Hero | **Free** |
| 02 | Ledger — Dark Analytics Dashboard | App | Pro |
| 03 | Hairline — Dev Tool Landing | Landing | Pro |
| 04 | Folio — Editorial UX Portfolio | Portfolio | **Free** |
| 05 | Tiers — Pricing Section with Toggle | Section | **Free** |
| 06 | Bento — Feature Grid | Section | Pro |
| 07 | Waitlist — Launch Countdown Page | Landing | **Free** |
| 08 | Vault — Fintech App Landing | Landing | Pro |
| 09 | Studio — Agency Site with Kinetic Type | Landing | Pro |
| 10 | Drop — Single-Product Store | E-commerce | Pro |
| 11 | Summit — Conference / Event Page | Landing | Pro |
| 12 | Horizon — Cinematic Footer + CTA | Section | Pro |
| 13 | Pinboard — Scrapbook Résumé Site | Portfolio | **Free** |
| 14 | Spread — Scattered-Card Magazine | Landing | Pro |
| 15 | Gate — Login & Sign-up Screens | App | **Free** |
| 16 | Console — Settings & Account Page | App | Pro |
| 17 | Parley — AI Chat Interface | App | Pro |
| 18 | Manual — Docs Site | Landing | Pro |
| 19 | Lost & Found — 404 + Empty States | Sections | Pro |
| 20 | Pocket — Mobile App Onboarding | App | Pro |
| 21 | Halo — Wearable / AR Hardware Launch | Landing | Pro |
| 22 | Maison — Luxury Fashion Store | E-commerce | Pro |
| 23 | Ember & Oak — Restaurant Site | Landing | **Free** |
| 24 | Stride — Fitness & Wellness App | Landing | Pro |
| 25 | Wander — Travel Booking | Landing | Pro |
| 26 | Stage — Musician / Artist Site | Portfolio | Pro |
| 27 | Care — Clinic & Healthcare | Landing | Pro |
| 28 | Haven — Real Estate Listings | Landing | Pro |
| 29 | Learn — Online Course / Cohort | Landing | Pro |
| 30 | Kindred — Nonprofit & Donations | Landing | Pro |
| 31 | Shipped — Changelog & Roadmap | Sections | Pro |
| 32 | Dispatch — Creator Newsletter | Landing | **Free** |
| 33 | Blockhaus — Neo-Brutalist SaaS | Landing | Pro |
| 34 | Tiles — Bento Personal Site | Portfolio | **Free** |
| 35 | Configure — 3D Product Configurator | E-commerce | Pro |
| 36 | Daybreak — Light AI Agent Startup | Landing | Pro |
| 37 | Form & Void — Architecture Studio | Portfolio | Pro |
| 38 | Roast — DTC Coffee Brand | E-commerce | Pro |
| 39 | Encore — Event Ticketing | App | Pro |
| 40 | Counsel — Law & Professional Services | Landing | Pro |
| 41 | Tides — Boutique Hotel & Resort | Landing | Pro |
| 42 | On Air — Podcast Site | Landing | Pro |
| 43 | Nest — Interior Design Studio | Portfolio | Pro |
| 44 | Signal — Live Analytics Hero | Hero | Pro |
| 45 | Ronin Dawn — Game Launch Landing | Landing | Pro |
| 46 | Nova — Coral AI Assistant Landing | Landing | Pro |
| 47 | Tidewater — Outdoor Build & Design Services | Landing | Pro |
| 48 | Meridian — City Residences (Ink Sketch) | Landing | Pro |
| 49 | Jade Pavilion — Wuxia Game Launch | Landing | Pro |
| 50 | Aero — Smart Glasses Launch (Sky) | Landing | Pro |
| 51 | Lumen Fold — Minimal Product Keynote | Landing | Pro |
| 52 | Ember One — Coral Smartphone Launch | Landing | Pro |
| 53 | Lumora — 3D Orb Motion Hero (Video) | Hero | Pro |
| 54 | Softwork — Eye-Tracking Mascot Studio | Landing | Pro |
| 55 | Concord — Human + Robot Motion Hero (Video) | Hero | Pro |
| 56 | Northbound — Polar Expedition Travel | Landing | Pro |
| 57 | Prism Bench — Optics Lab Instrument Maker | Landing | Pro |
| 58 | Wobble Co. — Squishy Toy & Slime Shop | E-commerce | Pro |
| 59 | Duotone Press — Riso Print Studio | Portfolio | **Free** |
| 60 | Fall Line — Downhill Ski Race Event | Landing | Pro |
| 61 | Static FM — Independent Internet Radio | Landing | **Free** |
| 62 | Halden — Quiet Fashion Store | E-commerce | Pro |
| 63 | Facet — Fine Jewelry Configurator | E-commerce | Pro |
| 64 | Lattice — Particle Sphere Intelligence Hero (Video + Canvas) | Hero | Pro |

---

## 01 · Aurora — AI SaaS Hero  `FREE`

```
Build a full-viewport hero section and sticky nav for an AI product called [PRODUCT], which [ONE-LINE VALUE PROP].

DIRECTION: "Cinematic dark". Background #07070B. One animated aurora made of 3 large blurred radial gradients (violet #8B5CF6, cyan #22D3EE, pink #F472B6) drifting slowly on a <canvas> (12s+ loops, low opacity ~0.15, blend mode "lighter"). Add a subtle SVG noise/grain overlay at 5% opacity.

NAV: 64px, sticky, glassmorphism (backdrop-blur 14px, rgba(7,7,11,.6)), 1px bottom border rgba(255,255,255,.08). Logo left, 4 links center (muted #9A9AAB, hover white), "Sign in" ghost pill + "Get started" solid white pill on the right.

HERO CONTENT (centered, max-width 980px):
1. Announcement pill: pulsing green dot + "[NEW FEATURE] is live →", 1px border, 13px text.
2. H1, 96px desktop / 44px mobile, weight 700, letter-spacing -0.045em, line-height 1: "Your [NOUN] on" + one rotating word that cycles every 2.4s through ["autopilot.", "overdrive.", "your terms."]. The rotating word uses a violet→cyan→pink gradient text fill and slides up with a blur transition; the container width animates to fit the word.
3. Subheadline 19px, muted, max 25 words.
4. Two CTAs: solid white pill "Start free" (on hover lifts 2px with violet glow shadow) and ghost pill "Watch demo ▶".
5. Below: an infinite logo marquee "Trusted by teams at" with 8 placeholder wordmarks, edges faded with a mask-image gradient.

MOTION: stagger entrance pill → H1 → sub → CTAs → marquee, 80ms apart, each fading from opacity 0, translateY 24px, blur 6px over 800ms with cubic-bezier(.2,.8,.2,1). A soft 520px radial violet glow follows the cursor.

ACCESSIBILITY: headline contrast ≥ 4.5:1 over the aurora; visible focus rings; wrap all ambient animation in @media (prefers-reduced-motion: reduce) to disable it.
Responsive at 375 / 768 / 1440px. Use real, benefit-led copy — no lorem ipsum.
```

---

## 02 · Ledger — Dark Analytics Dashboard  `PRO`

```
Build a responsive analytics dashboard web app for [COMPANY], a [TYPE OF BUSINESS]. The user is a [ROLE] who checks it daily to answer: (1) Are we on track this month? (2) What changed since yesterday? (3) What needs my attention?

DIRECTION: "Precision". Dark theme (#0A0A0B background, #111114 cards, 1px borders rgba(255,255,255,.07)), one accent color (#7C5CFF) used only for the primary data series and active states. Font: Inter or Geist for UI, tabular numbers everywhere.

LAYOUT:
- Left sidebar 240px (collapsible to 64px icon rail): logo, nav items Overview / Revenue / Customers / Campaigns / Reports / Settings with 1.5px-stroke icons, active item has accent left bar and subtle bg. Workspace switcher at bottom with avatar.
- Top bar: page title "Overview", date-range picker (Today, 7D, 30D, QTD, Custom), segment filter, search (⌘K hint), notifications bell with badge.
- Row 1: 4 KPI tiles — Revenue, Active customers, Conversion rate, Churn. Each: label, big value (32px), delta chip (▲ 12.4% green / ▼ 2.1% red — always with sign), tiny sparkline, "vs last period".
- Row 2: Revenue line chart spanning 8/12 columns (this period vs previous dashed grey, hover crosshair tooltip), plus a sorted horizontal bar chart "Revenue by channel" in 4/12.
- Row 3: "Needs attention" table: account, owner avatar, status badge (At risk / Overdue / Healthy), MRR, last activity, row action menu. Sticky header, sortable columns, search.

STATES: skeleton loaders that match the final layout, an empty state for the table ("No accounts need attention 🎉" is NOT allowed — write: "All accounts are healthy. We'll flag anything at risk here."), and a per-widget error with Retry. Each widget shows "Updated 4 min ago".

DATA: realistic mock data with weekly seasonality and a visible dip + recovery; values in $ with k/M abbreviations.

RESPONSIVE: KPI tiles 2×2 on tablet, horizontal-scroll on mobile; table becomes stacked cards under 640px; sidebar becomes a bottom sheet menu.
Include a light-mode toggle using CSS variables. Charts: Recharts. Keyboard accessible filters; charts have aria-label summaries.
```

---

## 03 · Hairline — Dev Tool Landing  `PRO`

```
Create a landing page for [TOOL], a developer tool that [WHAT IT DOES]. Audience: senior engineers who hate marketing fluff.

DIRECTION: "Precision". Near-black background, a faint 24px hairline grid (rgba(255,255,255,.04)) that slowly drifts, and a radial spotlight that follows the cursor revealing the grid more strongly. Mono font (JetBrains Mono / Geist Mono) for labels, eyebrows and code; clean sans for headings. Accent: electric lime #C6FF3D used sparingly.

SECTIONS:
1. Hero: left-aligned (not centered). Eyebrow "v2.0 — [CHANGELOG ITEM]". H1 64–80px, max 7 words. Sub 1 sentence. CTAs: "npm i [tool]" copy-to-clipboard code pill with a check animation + "Read the docs →". Right side: a terminal window mock that types out a 5-line session with realistic output, then loops.
2. Logos: "Used in production at" — monochrome wordmarks at 50% opacity.
3. "How it works": 3 numbered steps in mono (01 / 02 / 03) with a connecting line that draws itself on scroll.
4. Code comparison: tabs "Before" / "With [TOOL]" showing two code snippets with syntax highlighting; the line count difference is highlighted.
5. Performance: 3 big stat numbers that count up on scroll (e.g., "4.2× faster builds") with footnote-style sources.
6. Testimonials: 3 tweet-style cards with handle, avatar, and date.
7. Final CTA with the install command again, and a minimal footer with GitHub stars badge.

RULES: no stock illustrations, no emoji, no gradient blobs. Copy is terse and specific. Every code block has a Copy button. Motion is subtle (≤ 400ms UI, 700ms reveals), respects prefers-reduced-motion. WCAG AA contrast.
```

---

## 04 · Folio — Editorial UX Portfolio  `FREE`

```
Design a personal portfolio site for [NAME], a [ROLE, e.g., Senior UX Designer] focused on [SPECIALTY]. Goal: get hired or booked — recruiters should understand who I am and see my best 3 case studies within 30 seconds.

DIRECTION: "Editorial". Warm off-white background #F6F3EE, ink text #141414, one accent (#E4572E). Display font: a high-contrast serif (e.g., Instrument Serif, Fraunces) at very large sizes; body in a clean sans. Generous whitespace, asymmetric 12-col layout.

PAGES/SECTIONS:
1. Hero: oversized serif statement across 2–3 lines: "I design [OUTCOME] for [AUDIENCE]." with one word in italic accent color. Below: availability badge ("● Available from [MONTH]"), location/time zone, and links (LinkedIn, Email, Resume PDF).
2. Selected work: 3 case study cards in a staggered (not uniform) layout — alternating large/small. Each shows cover image, project name, company, role, and one result metric ("+32% activation"). On hover the image scales 1.03 and a "View case study →" label slides in; cursor becomes a custom circle with "View".
3. Case study template page: hero with title + metadata row (Role / Timeline / Team / Tools), "The problem", "My process" (numbered steps with artifacts), "Key decisions" (before/after image slider), "Results" (big metrics), "What I'd do next".
4. About: portrait, 3-sentence bio, a "How I work" list, and a small logo row of past companies.
5. Contact: large serif "Let's work together." + email with copy button.

MOTION: headings reveal line by line (clip-path mask up), images fade/scale in on scroll, smooth page transitions. prefers-reduced-motion respected.
Responsive, accessible (alt text, focus states, 4.5:1 contrast). Placeholder images with consistent aspect ratios (4:3 for cards).
```

---

## 05 · Tiers — Pricing Section with Toggle  `FREE`

```
Build a pricing section for [PRODUCT] with 3 plans: [Starter], [Pro], [Team].

LAYOUT: Section heading "Pricing that scales with you" (serif italic on "scales"), short sub. A monthly/yearly segmented toggle with a sliding pill indicator and a "Save 20%" badge next to Yearly. Prices animate (count/roll) when toggled.

CARDS (3 columns desktop, stacked mobile):
- Each card: plan name, one-line "who it's for", price (48px, tabular nums) + "/mo", billed note, primary button, feature list with check icons (5–7 items), and a "Everything in [previous], plus:" line on higher tiers.
- Middle plan is "Most popular": raised 8px, gradient border (violet→cyan) using the padding-box/border-box technique, a small ribbon label, and a solid button (others are outline).
- Below cards: a compact "Compare all features" expandable table (sticky header, grouped rows, ✓ / — / text values).
- Trust row: "Cancel anytime · 14-day free trial · SOC 2" with icons.
- FAQ: 5 accordion questions about billing.

STYLE: works in both light and dark (CSS variables). 1px borders, 20px radius, hover lifts card 4px with soft shadow. Buttons 44px tall.
ACCESSIBILITY: the toggle is a real radio group with keyboard support and aria-live on price changes. Check icons have text equivalents for screen readers.
```

---

## 06 · Bento — Feature Grid  `PRO`

```
Create a "Features" section for [PRODUCT] as a bento grid — 6 tiles of mixed sizes on a 4-column grid (desktop): one 2×2 hero tile, two 2×1 wide tiles, three 1×1 tiles. On tablet: 2 columns; on mobile: single column.

Each tile has: eyebrow label, short title (≤ 6 words), 1-line description, and a LIVE mini visual built in HTML/CSS (no static images):
1. (2×2) Animated product UI mock: a sidebar + list whose items shimmer, then one item expands.
2. (2×1) Integration orbit: product logo in the center, 6 small integration icons orbiting on two rings.
3. (2×1) Chart: bars that grow in on scroll and gently oscillate.
4. (1×1) Security: a lock icon with a pulsing ring.
5. (1×1) Speed: a big number "38ms" that counts up, with a tiny latency sparkline.
6. (1×1) Collaboration: 3 overlapping avatars with animated cursors moving between them.

STYLE: dark cards #0E0E14, 1px border rgba(255,255,255,.08), 24px radius. On hover: a radial spotlight follows the cursor inside the tile (CSS variable --x/--y), border brightens, tile tilts max 6° with perspective.
Section heading above the grid: "Everything you need. Nothing you don't." with the second sentence in muted grey.
Reveal tiles on scroll with a 60ms stagger. Respect prefers-reduced-motion (visuals static).
```

---

## 07 · Waitlist — Launch Countdown Page  `FREE`

```
Build a single-page pre-launch waitlist site for [PRODUCT], launching [DATE].

DIRECTION: minimal and confident. Deep navy-black background with a slow, looping gradient mesh (2 colors: [COLOR A], [COLOR B]) and a subtle grain. Center-aligned, everything fits in one viewport on desktop.

CONTENT:
1. Logo + small "Launching [DATE]" pill.
2. H1 (72px desktop): "[BOLD PROMISE IN ≤ 7 WORDS]".
3. Sub: one sentence on who it's for.
4. Email capture: single input + "Join the waitlist" button inside one rounded container. Inline validation (message below input, not an alert). On success: the form morphs into a success state — "You're #[N] on the list" with a "Share to move up" row (copy link, X, LinkedIn).
5. Countdown: Days / Hours / Minutes / Seconds in tabular numbers with a flip or slide animation on change.
6. Social proof: stacked avatars + "Join 2,400+ designers already waiting".
7. 3 small feature teasers in a row with icons.
8. Footer: © and a privacy note under the form: "No spam. Unsubscribe anytime."

Use proper input type="email", autocomplete="email", label (visually hidden OK), focus ring, and aria-live for form messages. prefers-reduced-motion stops the mesh animation.
```

---

## 08 · Vault — Fintech App Landing  `PRO`

```
Design a landing page for [APP], a mobile-first [BANKING / SAVINGS / INVESTING] app for [AUDIENCE].

DIRECTION: "Soft product" meets premium. Light theme: background #F7F7F4, ink #0F1115, accent deep emerald #0F7B5F with a soft mint #D9F2E6. Large radius (28px), soft layered shadows, rounded geometric sans (e.g., Manrope / General Sans).

SECTIONS:
1. Hero: split layout. Left: H1 "Money that [BENEFIT]." sub, App Store + Google Play badges, rating "4.9 ★ from 12k reviews". Right: a phone mockup (CSS-built frame) showing the app home screen: balance card, spending ring chart, recent transactions. The phone floats gently; a few UI chips ("+$240 saved this month", "Bill paid ✓") pop out around it with staggered delays.
2. Trust bar: "Protected by [REGULATOR/INSURANCE]", bank-grade encryption, logos of press.
3. Feature trio: alternating left/right rows, each with a phone screen visual and a short benefit block: Save automatically / See where money goes / Invest spare change.
4. Interactive calculator: slider "If you save $[X] a month" → animated result "you'll have $[Y] in 5 years" with a small growth chart.
5. Testimonials carousel with real-feeling names, photos, and specific outcomes.
6. Security section with a dark card contrast break.
7. FAQ + final CTA with QR code to download.

Numbers use tabular figures. All claims have footnote markers. Fully responsive; on mobile the phone mockup sits below the headline. AA contrast, reduced-motion support.
```

---

## 09 · Studio — Agency Site with Kinetic Type  `PRO`

```
Create a homepage for [AGENCY NAME], a [DISCIPLINE] studio in [CITY].

DIRECTION: "Bold brutal". Background off-black #0D0D0D, text #F2F2F2, one loud accent [e.g., #FF4D00]. Oversized grotesk display font (e.g., Neue Montreal / Space Grotesk) at 12–16vw. Visible structure: thin 1px dividers, section numbers, grid labels.

SECTIONS:
1. Hero: the agency name fills the viewport width; letters stagger in from below on load (split text, 40ms per letter). Under it, a row: "[DISCIPLINE] — [CITY] — Est. [YEAR]" and a live local time clock.
2. Showreel: a full-bleed muted looping video (poster image fallback) that scales from 80% to 100% width as you scroll into it; custom cursor shows "Play reel".
3. Selected work: a list layout (not cards) — each row: index number, project name in huge type, client, year. On hover, a preview image follows the cursor and the row text shifts to the accent color.
4. Services: 4 columns with numbered headings and short lists.
5. Marquee: an infinite horizontal band "Let's make something loud —" repeating, reversing direction on scroll.
6. Contact: giant email address as a link with an underline that draws on hover; footer with socials.

MOTION: smooth scroll feel, reveal lines with clip-path masks, magnetic buttons (max 8px). Everything disabled/simplified under prefers-reduced-motion. Keyboard focus visible on all links.
```

---

## 10 · Drop — Single-Product Store  `PRO`

```
Build a single-product e-commerce landing page for [PRODUCT NAME], a [PRODUCT TYPE] priced at $[PRICE].

DIRECTION: clean, product-as-hero. Background tinted to the product color ([HEX] at 6%), neutral ink text, one CTA color.

SECTIONS:
1. Hero: large product image centered with a soft shadow ellipse; it rotates slightly on cursor move (max 6°). Left: product name, 1-line promise, rating, price. Right: color swatches (clicking a swatch cross-fades the product image and tints the page background), size selector, "Add to bag" button with a satisfying micro-animation (icon flies to bag counter in nav).
2. Sticky buy bar: appears after scrolling past the hero — thumbnail, name, price, "Add to bag".
3. Feature callouts: product image with 4 hotspot dots; hovering/tapping a dot shows a callout card.
4. Specs: two-column table with icons; materials, dimensions, care.
5. Reviews: average score with star distribution bars, 3 reviews with photos, "Verified buyer" badges.
6. Shipping & returns strip: Free shipping · 30-day returns · 2-year warranty.
7. FAQ and footer.

Include a slide-in cart drawer with quantity steppers, subtotal, and checkout button. Mobile: image gallery becomes a swipeable carousel with dots. AA contrast; swatches have text labels for screen readers.
```

---

## 11 · Summit — Conference / Event Page  `PRO`

```
Create an event website for [EVENT NAME], a [TOPIC] conference on [DATES] in [CITY] (and online).

DIRECTION: energetic but organized. Dark background with a bold 2-color gradient ([COLOR A] → [COLOR B]) used for the hero and ticket section only. Display font condensed and uppercase for headlines; readable sans for body.

SECTIONS:
1. Hero: huge event name, dates + location with calendar icon, countdown, CTA "Get tickets" + "Add to calendar" (.ics download). Background: slowly rotating concentric rings / orbit graphic.
2. Stats row: "40+ speakers · 2 days · 1,200 attendees" counting up.
3. Speakers grid: photo cards (duotone treatment, color on hover), name, role, company; clicking opens a modal with bio and talk title.
4. Schedule: Day 1 / Day 2 tabs; timeline list with time, talk, speaker avatar, track tag (color-coded, with text label), "Add to my agenda" star toggle.
5. Venue: map placeholder, address, travel tips.
6. Tickets: 3 ticket tiers with remaining-quantity bars ("32 left") and early-bird strike-through prices.
7. Sponsors: tiered logo wall (Platinum larger than Gold).
8. FAQ + newsletter signup + footer.

Schedule must be keyboard navigable; tabs use proper ARIA roles. Times shown with time zone. Responsive; schedule collapses to accordion on mobile.
```

---

## 12 · Horizon — Cinematic Footer + CTA  `PRO`

```
Build a final CTA + footer section for [BRAND] that makes the end of the page feel like a finale.

CTA BLOCK: full-width, 80vh tall, with a horizon effect: a large glowing arc (radial gradient ellipse, [ACCENT COLOR]) rising from the bottom edge as the user scrolls into view (scroll-linked: translateY and opacity). Headline 80px centered: "Ready when you are." + sub + 2 CTAs. Subtle particles/stars twinkling above the horizon (CSS or small canvas, ≤ 60 particles).

FOOTER (below the arc, dark):
- Top row: logo + one-line mission, and a newsletter input with inline success state.
- Link columns: Product, Company, Resources, Legal (4–6 links each), muted with hover underline animation.
- Bottom row: © year, status indicator ("● All systems normal"), social icons, language selector.
- A giant, clipped brand wordmark at the very bottom (20vw, 6% opacity, cut off by the viewport edge) as a signature detail.

Everything responsive (columns → accordion under 640px), focus-visible styles, and prefers-reduced-motion disables the particles and scroll-linked effect.
```

---

## 13 · Pinboard — Scrapbook Résumé Site  `FREE`

```
Build a one-page résumé site for [NAME], a [ROLE], designed like a tidy scrapbook pinboard, so it's memorable to recruiters but still scannable in 20 seconds.

DIRECTION: warm cork/linen background (#EFE6D8 with subtle noise), ink #1D1B18, accents: tomato #E4572E, sky #6CA6E0, sun #F4C542. Fonts: a bold grotesk for the name, a typewriter mono for labels, a clean sans for body.

LAYOUT (desktop: loose 12-col grid with pinned items at ±2° rotation; mobile: straight single column, no rotation):
1. Header card (pinned with a pushpin SVG): name at 72px, role, location, "Available from [MONTH]" stamp, buttons: Email, LinkedIn, Download PDF.
2. "Experience" as index cards: company, role, dates in mono, 2 bullet achievements with numbers. Each card has tape corners.
3. "Selected work" as polaroids: image placeholder, project name in handwriting font, 1-line result. Click opens a lightbox with 3 bullets and a link.
4. "Skills" as sticker chips in 3 groups (Research, Design, Tools).
5. "Education & certifications" as a ticket-stub card.
6. "Kind words" as 2 sticky notes with quotes from colleagues.
7. Footer: a torn-paper edge and a contact line.

MOTION: cards drop and settle on load (staggered 60ms, small rotate), polaroids lift on hover with a stronger shadow. prefers-reduced-motion removes rotation and motion.

MUST: all real text is HTML (not images) for ATS/SEO; a print stylesheet that outputs a clean 1-page A4/Letter résumé without decoration; WCAG AA contrast; semantic headings.
```

---

## 14 · Spread — Scattered-Card Magazine  `PRO`

```
Create an editorial magazine homepage for [PUBLICATION NAME], a publication about [TOPIC], where stories are laid out as a scattered collage of cards instead of a rigid grid.

DIRECTION: off-white paper #F6F4EF, ink #151515, one accent [#2B50FF]. Fonts: a condensed display serif for headlines, a text serif for decks, small-caps sans for kickers.

SECTIONS:
1. Masthead: publication name very large across the top, issue number + date + "Subscribe" link, a thin double rule.
2. Scattered feature field (desktop): 7–9 story cards of different sizes placed on a freeform canvas with slight overlaps and ±3° rotations; the lead story is largest. Each card: image placeholder with consistent duotone treatment, kicker, headline, 1-line deck, author. Hovering a card brings it to the front, straightens it, and dims the others slightly.
3. "In focus" band: one full-width story with a big pull quote.
4. Topics row: filter chips (Places, People, Objects, Ideas); selecting one re-arranges the card field with a smooth FLIP animation.
5. Newsletter block styled like a subscription insert card.
6. Footer with issue archive links.

RESPONSIVE: below 900px, the scattered field becomes a clean single-column list (no overlap) in the same order; keep keyboard focus order logical (reading order = DOM order regardless of visual placement).
ACCESSIBILITY: every card is a single link with a visible focus ring; rotations are disabled under prefers-reduced-motion.
```

---

## 15 · Gate — Login & Sign-up Screens  `FREE`

```
Design and build the authentication screens for [PRODUCT]: Sign in, Sign up, Forgot password, Check your email, and Two-factor code.

LAYOUT: split screen on desktop: left 45% is a brand panel ([BRAND COLOR] gradient mesh with a short testimonial and logo), right is the form column (max-width 400px, vertically centered). Mobile: brand panel collapses to a small header.

FORM UX RULES:
- SSO buttons first (Google, Microsoft, GitHub), then "or continue with email" divider.
- Labels always visible (no placeholder-only labels); correct type and autocomplete attributes (email, current-password, new-password, one-time-code).
- Password field with show/hide toggle and a live strength meter + requirement checklist on sign-up.
- Inline validation on blur, not on every keystroke; errors say how to fix ("Use at least 8 characters").
- Primary button shows a loading spinner and disables while submitting; prevent double submit.
- 2FA: 6 separate digit inputs that auto-advance, support paste of the full code, and "Resend code in 0:30" countdown.
- "Check your email" screen shows the address used, a button to open Gmail/Outlook, and "Wrong email? Change it".
- Error states: wrong password (generic message for security), account locked, network error with retry.

STYLE: clean, calm, trustworthy. 44px inputs, 12px radius, clear focus rings in brand color, dark mode support.
Provide all 5 screens with routing between them and realistic copy. WCAG AA; screen-reader announcements for errors (aria-live).
```

---

## 16 · Console — Settings & Account Page  `PRO`

```
Build a settings area for [SAAS PRODUCT] with left-rail navigation and these sections: Profile, Account & security, Notifications, Team members, Billing, API keys, Danger zone.

LAYOUT: 240px sticky section nav (with icons and the active section highlighted as you scroll), content column max 720px. Each section is a card with a title, a one-line description and grouped fields.

PATTERNS:
- Profile: avatar upload with crop preview, name, username with availability check, bio with character counter.
- Security: change password, 2FA toggle with setup modal (QR placeholder + backup codes download), active sessions list with "Sign out" per device.
- Notifications: a matrix table (rows = events, columns = Email / Push / In-app) using toggles, with "Mute all for 1 hour" option.
- Team: members table with role dropdown (Owner/Admin/Member/Viewer), pending invites with resend/revoke, "Invite" modal accepting multiple emails as chips.
- Billing: current plan card with usage bars (seats, storage), payment method, invoices table with download links.
- API keys: list with masked keys, copy button, created/last-used dates, "Create key" modal that shows the key once with a warning.
- Danger zone: red-bordered card; destructive actions require typing the workspace name to confirm.

SAVE BEHAVIOR: sticky bottom bar appears only when there are unsaved changes ("You have unsaved changes · Discard · Save"), plus a toast on save with Undo where possible.
Include skeleton loading and empty states (no API keys yet, no invites). Keyboard accessible; toggles are real switches with labels.
```

---

## 17 · Parley — AI Chat Interface  `PRO`

```
Build a production-quality AI assistant chat interface for [PRODUCT], called [ASSISTANT NAME].

LAYOUT: left sidebar (260px, collapsible) with "New chat", search, and conversation history grouped by Today / Previous 7 days / Older (rename, pin and delete on hover). Main area: conversation with max-width 760px centered, and a composer docked at the bottom.

EMPTY STATE: greeting with the assistant's name, 4 suggestion cards (icon + short prompt) relevant to [USE CASE], and a note on what the assistant can and can't do.

MESSAGES:
- User messages right-aligned in a subtle bubble; assistant messages full-width without a bubble, with avatar.
- Streaming response with a smooth token-by-token reveal and a "Stop generating" button.
- Rich markdown: headings, lists, tables, code blocks with language label + copy button + syntax highlighting.
- A collapsible "Thinking / Used 3 tools" step list showing tool calls with status icons (running, done, failed).
- Citations as numbered chips that open a source preview popover.
- Per-message actions on hover: copy, regenerate, thumbs up/down (down opens a short feedback form), edit (for user messages).

COMPOSER: auto-growing textarea (max 8 lines), attach button with file chips (name, size, remove), model/mode selector, voice button, Enter to send / Shift+Enter for newline, disabled send when empty, character hint when near the limit.

STATES: network error inline with retry, rate-limit message with countdown, long-response "Continue" button.
Dark and light themes, smooth scroll-to-bottom button when scrolled up, full keyboard support, aria-live for new messages.
```

---

## 18 · Manual — Docs Site  `PRO`

```
Create a documentation site for [PRODUCT / API].

LAYOUT (3 columns on desktop): left nav tree (collapsible groups, current page highlighted, version switcher at top), center content (max 72ch), right "On this page" table of contents with scroll-spy. Top bar: logo, search (⌘K), Guides / API reference / Changelog tabs, GitHub link, theme toggle.

CONTENT COMPONENTS (build all):
- Callouts: Note, Tip, Warning, Danger (icon + tinted border).
- Code blocks with tabs for languages (cURL, JavaScript, Python), copy button, line highlighting, filename header.
- Steps component (numbered, vertical line).
- API endpoint block: method badge (GET/POST colors), path, parameters table (name, type, required, description), example request/response tabs.
- Cards grid for "Next steps".
- Previous / Next page navigation and "Was this page helpful?" with Yes/No.
- "Edit this page" and "Last updated" footer.

SEARCH: ⌘K command palette with fuzzy results grouped by section, keyboard navigation, recent searches.
Sample content: a "Quickstart" page that gets a developer to a first successful API call in 5 steps.
Mobile: nav becomes a slide-over drawer, TOC becomes a dropdown at the top. Accessible headings with anchor links.
```

---

## 19 · Lost & Found — 404 + Empty States  `PRO`

```
Design a set of delightful but useful error and empty states for [PRODUCT]: 404 page, 500 page, offline, no search results, empty inbox/list, no permissions, and first-run "nothing here yet".

Each state has: a small original illustration built from simple SVG shapes in the brand palette ([COLORS]) with one subtle looping animation (≤ 4s, gentle), a clear headline, one sentence explaining what happened and why, one primary action and one secondary action.

SPECIFICS:
- 404: search box + links to the 4 most popular pages; illustration of a map with a dotted path ending in a question mark.
- 500: "We're on it" + status page link + retry; show an error reference ID the user can copy for support.
- Offline: detects navigator.onLine, auto-retries when back online, with a toast "You're back online".
- No search results: shows the query, suggests spelling fixes, "Clear filters" if filters are active, and popular searches.
- Empty list: explains the value of the object ("Projects keep your files and team in one place"), primary "Create project", secondary "Import".
- No permission: who to ask (show the workspace owner's name/avatar) + "Request access" button with a sent state.

Present all states on one showcase page with tabs, plus each as a reusable component. Copy is warm, specific and never blames the user. prefers-reduced-motion stops the loops. WCAG AA contrast.
```

---

## 20 · Pocket — Mobile App Onboarding  `PRO`

```
Build a mobile app onboarding flow (render in a 390×844 phone frame, React or HTML) for [APP], a [CATEGORY] app. Goal: get the user to [AHA MOMENT] in under 60 seconds.

SCREENS:
1. Welcome: full-bleed brand illustration (SVG shapes), app name, one-line promise, "Get started" + "I already have an account".
2. Value carousel: 3 swipeable cards (swipe + dots + skip), each with a mini animated UI illustration of a key benefit. Skippable at any time.
3. Personalization: "What brings you here?" multi-select chips (6 options), "Continue" enabled after 1 selection.
4. Permission priming: explain WHY before the system prompt ("Get a reminder when your plan is ready"), with "Allow notifications" and "Not now". Never ask for more than one permission here.
5. Account: Sign in with Apple / Google, or email (deferred password: magic link).
6. First success: a pre-filled starter [ITEM] based on their choices, with a coach mark pointing at the one thing to tap, and a small celebration when done.
7. Home with a dismissible 3-step "Get set up" checklist.

MOTION: native-feeling transitions (shared-element slide between screens, 300ms spring), haptic-style button press scale (0.97).
UX RULES: thumb-zone primary buttons (bottom, 56px tall), safe-area padding, progress indicator on steps 3–5, back navigation on every screen, all copy specific to [APP]. Support dark mode and dynamic type (text scales to 130% without breaking layout).
```

---

## 21 · Halo — Wearable / AR Hardware Launch  `PRO`

```
Build a cinematic launch page for [PRODUCT], a [wearable / AR glasses / smart device] by [BRAND], that makes a physical product feel premium and desirable.

DIRECTION: dark studio. Background #050608, product lit like a hero object with a soft top light and floor reflection. One cool accent ([#7DD3FC]) for UI details. Display font: wide geometric sans at 96–160px, tight tracking. Body: clean sans 18px.

SECTIONS:
1. Hero: the product (CSS/SVG render or image placeholder) centered on a reflective floor, slowly rotating ±8° with the cursor. Headline ≤ 5 words above it; "Pre-order $[PRICE]" + "Watch the film" below. Subtle light sweep across the product every 6s.
2. Scroll-driven exploded view: as the user scrolls, the product separates into 3–4 labeled layers (lens, chip, battery, frame) with thin leader lines and specs.
3. "Day with [PRODUCT]": horizontal scroll of 4 moments (morning, commute, work, night) with a UI overlay mock showing what the wearer sees.
4. Specs grid: 6 tiles with big numbers (weight, battery, field of view, etc.), tabular numerals, hairline borders.
5. Colors/finishes: swatches that re-tint the hero product.
6. Compare models: 2–3 columns with the recommended one highlighted.
7. Pre-order band: price, ship date, trade-in note, and a sticky "Pre-order" bar after the hero.
8. FAQ + footer with support links.

MOTION: scroll-linked transforms only (transform/opacity), 60fps; reduced-motion shows the exploded view as a static labeled diagram.
A11y: every visual has a text equivalent; contrast AA; keyboard-reachable swatches.
```

---

## 22 · Maison — Luxury Fashion Store  `PRO`

```
Create a luxury fashion e-commerce homepage and product page for [BRAND], a [womenswear / menswear / accessories] label.

DIRECTION: quiet luxury. Background #F4F1EC, ink #111, accent none (use black/white contrast), high-contrast serif for the logo and headlines (e.g. Didone style), small spaced uppercase sans for navigation. Generous whitespace, editorial photography placeholders at consistent 4:5 ratio.

HOMEPAGE:
1. Minimal header: centered wordmark, left "Menu", right "Search · Account · Bag (0)".
2. Full-bleed campaign hero (video or image placeholder) with a single line: "[COLLECTION NAME]" and "Discover" link.
3. Asymmetric editorial grid: 1 large + 2 small images with captions.
4. "New arrivals" horizontal product rail: image swaps to a second angle on hover, name, price.
5. Brand story block: serif pull quote + short paragraph.
6. Newsletter with 10% offer, then a restrained footer.

PRODUCT PAGE: sticky left gallery (vertical thumbnails, zoom on click), right column with name, price, color swatches, size selector with "Size guide" drawer, "Add to bag" (full-width black), delivery & returns accordion, materials & care, "Complete the look" rail.

CART: slide-in drawer with line items, quantity, subtotal, free-shipping progress bar.
RULES: no discount-store patterns (no countdown timers, no flashing badges). Motion is slow fades (600–900ms). AA contrast, visible focus states, alt text on all products.
```

---

## 23 · Ember & Oak — Restaurant Site  `FREE`

```
Build a website for [RESTAURANT NAME], a [cuisine] restaurant in [CITY], that makes people hungry and gets them to book a table in two taps.

DIRECTION: warm and appetizing. Background #1A1410 (deep roast) with cream text #F3E9DC, accent ember orange [#E0703A]. Display: characterful serif; body: humanist sans. Food photography placeholders with warm grading.

SECTIONS:
1. Hero: full-bleed food image/video placeholder with a dark gradient, restaurant name, one-line promise ("Wood-fired, local, late"), buttons "Book a table" and "View menu". Opening hours pill ("Open today 5–11pm", with open/closed state computed from the current time).
2. Menu: tabs (Starters, Mains, Desserts, Drinks); each dish shows name, one-line description, price aligned right with dotted leaders, dietary tags (V, VG, GF) with a legend.
3. Story: chef portrait placeholder + 3 short sentences.
4. Gallery: masonry of 6 images with lightbox.
5. Reservations: date, time and party-size pickers + name/phone/email, with inline validation and a confirmation state (or a placeholder link to [booking provider]).
6. Location: address, map placeholder, parking/transit notes, hours table.
7. Footer: phone (tap-to-call), Instagram link, private events inquiry.

MOBILE FIRST: a sticky bottom bar with "Call" and "Book". Menu prices readable at 16px. Contrast AA on the dark theme; reduced motion respected.
```

---

## 24 · Stride — Fitness & Wellness App  `PRO`

```
Design a landing page for [APP NAME], a fitness and wellness app that offers [workouts / running plans / yoga / habit coaching].

DIRECTION: energetic but clean. Background #0C0F0A, accent electric lime [#C7F53B] with a secondary soft coral; rounded bold sans for headlines; phone mockups as the main visual.

SECTIONS:
1. Hero: two overlapping phone mockups (workout player + progress rings), headline ≤ 6 words, App Store / Google Play badges, rating line.
2. Animated progress rings that fill on scroll (move, sleep, mindful minutes) with labels.
3. "Plans for every body": filter chips (Beginner, 20 min, No equipment, Low impact) that reorder a grid of plan cards (duration, intensity dots, coach avatar).
4. Coach section: 3 coach cards with specialty and a short quote.
5. Results: before/after style stat cards (not body photos): "Ran first 5K in 8 weeks", "+42% weekly active minutes", with small print on methodology.
6. Pricing: monthly/yearly toggle, free-trial callout.
7. FAQ (cancellation, devices, health disclaimers) and footer.

RULES: inclusive imagery and language (no body shaming, diverse bodies and ages in placeholders); a clear medical disclaimer; reduced-motion stops ring and counter animations; AA contrast.
```

---

## 25 · Wander — Travel Booking  `PRO`

```
Create a travel booking homepage for [BRAND], which sells [boutique stays / guided trips / experiences] in [REGIONS].

DIRECTION: airy and aspirational. Background #FBFAF7, ink #1D2320, accent deep teal [#0F766E], sand secondary. Rounded 20px cards, large photography placeholders.

SECTIONS:
1. Hero: full-bleed destination image with a floating search bar (Where · Dates · Guests · Search). Where = autocomplete with recent searches; Dates = a two-month range calendar with nightly price hints; Guests = stepper (adults, children, pets).
2. "Trending now": horizontal carousel of destination cards (image, name, "from $[X]/night", rating) with arrow buttons and scroll-snap.
3. Categories row with icons (Beach, Cabins, City, Design stays, Pet friendly) that filter the listing grid below.
4. Listing grid: card with image carousel dots, save (heart) toggle, title, dates, price per night + total, rating and review count, "Superhost"-style badge renamed for [BRAND].
5. Map toggle: split view with the list left and a map placeholder with price pins right.
6. Trust section: free cancellation policy, 24/7 support, verified reviews.
7. Newsletter + footer.

UX: search works with keyboard only; the date picker is accessible (ARIA grid); prices always show the total including fees; loading skeletons for listings.
```

---

## 26 · Stage — Musician / Artist Site  `PRO`

```
Build a website for [ARTIST NAME], a [genre] artist, to promote their new release "[RELEASE]" and sell tickets and merch.

DIRECTION: bold, moody and tied to the album art. Palette pulled from the cover: [PRIMARY], [SECONDARY], near-black. Display font: expressive grotesk or condensed; allow one oversized word to bleed off the edge.

SECTIONS:
1. Hero: album artwork placeholder large on the left, release title huge on the right, "Listen now" button opening a popover with links (Spotify, Apple Music, YouTube, Bandcamp placeholders), and a small audio preview player (play/pause, 30s waveform scrubber).
2. Tour dates: list rows (date, city, venue, "Tickets" button / "Sold out" state / "Notify me"), with a "Near me" sort placeholder.
3. Video: featured music-video embed placeholder with a custom poster and play button.
4. Merch: 4 product cards with hover second image, price, "Add to cart".
5. About: short bio, press photo, "Download press kit" link.
6. Mailing list: "Get tour presales first" with email + country select.
7. Footer: social icons and booking/management contacts.

MOTION: a subtle grain overlay, a slow gradient shift from the album colors, and text that reveals line by line. Reduced-motion friendly; audio never autoplays; all controls are keyboard-accessible with labels.
```

---

## 27 · Care — Clinic & Healthcare  `PRO`

```
Design a website for [CLINIC NAME], a [dental / family medicine / physiotherapy / dermatology] clinic in [CITY], focused on trust and easy booking.

DIRECTION: calm and reassuring. Background #F7FAFA, ink #13232B, accent [#1C7C8C] teal with a soft mint. Rounded sans, generous line-height (1.6), large tap targets (≥ 48px).

SECTIONS:
1. Hero: friendly headline ("Care that fits your schedule"), subline, "Book an appointment" primary + "Call us" secondary, trust row (years open, rating, "Accepting new patients" badge, insurance accepted).
2. Services grid: 6–8 cards with simple line icons, one sentence each, "Learn more".
3. How booking works: 3 steps (choose service → pick time → confirm), with estimated wait time.
4. Online booking widget: service select, clinician select (with "Any available"), calendar with available slots, patient details form, confirmation screen with add-to-calendar.
5. Team: clinician cards with photo placeholder, credentials, languages spoken.
6. Patient info: what to bring, insurance and payment, accessibility of the building, FAQ.
7. Location & hours, emergency notice ("If this is an emergency, call [NUMBER]"), footer.

RULES: plain language (reading age ~12); WCAG 2.2 AA strictly (this audience includes older and low-vision users); support 200% zoom; no autoplay; privacy note near forms.
```

---

## 28 · Haven — Real Estate Listings  `PRO`

```
Create a real-estate website for [AGENCY], with a search-first homepage and a property detail page.

DIRECTION: modern and trustworthy. Background #FFFFFF, ink #111827, accent [#B45309] warm bronze, neutral stone surfaces. Photography-led cards with 3:2 images.

HOMEPAGE:
1. Hero with a large property image and a segmented search (Buy / Rent / Sold) + location autocomplete + price range + beds filter.
2. Featured listings grid: image carousel, price, address, beds/baths/sqft icons, status badge (New, Open house, Under offer), save toggle.
3. "Explore neighborhoods": image tiles with median price and short vibe description.
4. Valuation CTA: "What's your home worth?" with an address field leading to a lead form.
5. Agent spotlight + testimonials, then footer.

PROPERTY PAGE: photo mosaic (1 large + 4 small, "View all 32 photos" lightbox), sticky summary card (price, key facts, "Book a viewing" with date/time slots, agent contact), description, features checklist, floor plan placeholder, map & nearby (schools, transit, parks) tabs, mortgage calculator (price, deposit slider, rate, term → monthly payment), similar homes rail.

UX: filters persist in the URL; results count updates live; empty state for no matches with "widen your search" suggestions; all numbers use tabular figures.
```

---

## 29 · Learn — Online Course / Cohort  `PRO`

```
Build a sales page for "[COURSE NAME]", an online [self-paced course / live cohort] by [INSTRUCTOR] that teaches [OUTCOME] to [AUDIENCE].

DIRECTION: credible and motivating. Background #FFFDF8, ink #1B1B1F, accent [#4F46E5], highlighter yellow for emphasis. Friendly serif headlines + clean sans body.

SECTIONS:
1. Hero: outcome-driven headline ("Ship your first [X] in 6 weeks"), subline, next cohort start date + seats left bar, "Enroll" and "Watch free lesson" buttons, instructor mini-bio with avatar.
2. "Is this for you?": two columns — "Perfect if you…" / "Not for you if…".
3. Curriculum: accordion of modules with lesson counts, durations and a preview badge on free lessons.
4. What you'll build: 3 project cards with outcome screenshots placeholders.
5. Instructor: photo, credentials, why they teach this.
6. Student outcomes: testimonial cards with role and specific result; a short results stat row.
7. Pricing: 2–3 tiers (Self-paced, Cohort, Team) with a comparison, payment plan note, refund guarantee badge.
8. FAQ and a final CTA with the cohort date countdown.

RULES: honest urgency only (real dates/seats); captions/transcripts noted for video; accessible accordions; mobile sticky "Enroll" bar.
```

---

## 30 · Kindred — Nonprofit & Donations  `PRO`

```
Design a website for [ORGANIZATION], a nonprofit that [MISSION], optimized for donations and volunteer sign-ups.

DIRECTION: hopeful and human. Background #FFFBF5, ink #1F2A2E, accent [#E4572E] warm coral with a leaf green secondary. Rounded friendly type; documentary-style photography placeholders (people with dignity, not pity).

SECTIONS:
1. Hero: impact headline ("Clean water for 40,000 people this year"), short subline, "Donate" primary + "Volunteer" secondary, progress bar toward the annual goal.
2. Impact numbers that count up on scroll (people helped, projects, % of funds to programs).
3. Stories: 3 story cards with a photo, quote and "Read story".
4. How your gift helps: donation amount chips ($25 / $50 / $100 / Other) each mapped to a concrete outcome ("$50 = school supplies for 5 kids"), one-time / monthly toggle with monthly pre-selected, and a clear "Donate $50 monthly" button.
5. Transparency: where money goes (simple bar chart), annual report download, charity registration number.
6. Volunteer & events: upcoming events list with sign-up.
7. Partners logo row, newsletter, footer with contact and privacy.

RULES: donation form is short (amount → details → payment), shows fees coverage option, works with keyboard, AA contrast, and never uses guilt-driven copy.
```

---

## 31 · Shipped — Changelog & Roadmap  `PRO`

```
Build a public changelog and roadmap page for [PRODUCT] that turns product updates into marketing.

DIRECTION: product-native. Match [PRODUCT]'s brand: default is a clean dark theme (#0B0B0E, ink #EDEDF0, accent [#7C5CFF]), mono labels for versions and dates.

CHANGELOG:
- Left sticky rail: filter chips (New, Improved, Fixed, API) and a month index.
- Timeline entries: date + version badge, title, 1–2 sentence summary, optional screenshot/video placeholder, "What's new" bullet list, tags, and a permalink copy button.
- "Subscribe to updates" (email + RSS link) at the top.

ROADMAP:
- Three columns: Planned · In progress · Shipped (Kanban-like cards), each card with title, short description, category tag, and upvote button with count (optimistic update).
- "Suggest a feature" modal with title, description and category.

DETAILS: entries are rendered from a JSON array so non-developers can add updates; deep links scroll to and highlight an entry; empty state for filters with no results; keyboard navigation between entries (J/K); reduced motion respected; AA contrast.
```

---

## 32 · Dispatch — Creator Newsletter  `FREE`

```
Create a landing page for "[NEWSLETTER NAME]", a [weekly / monthly] newsletter by [CREATOR] about [TOPIC], designed to convert visitors into subscribers.

DIRECTION: editorial and personal. Background #FAF7F2, ink #171717, accent [#D9480F]. Serif for headlines and issue titles, clean sans for UI. Feels like a well-designed magazine page, not a SaaS site.

SECTIONS:
1. Hero: creator avatar, newsletter name, a one-sentence promise ("One idea a week to design better products"), email input + "Subscribe" in one field group, social proof ("Join 12,400 designers"), and "Read a sample issue" link.
2. What you get: 3 short points with small hand-drawn-style icons (SVG).
3. Recent issues: list of 5 issue cards (number, date, title, 1-line teaser, reading time) linking to an archive page.
4. Reader quotes: 3 short testimonials with names and roles.
5. About the author: portrait placeholder, 3-sentence bio, links.
6. Final subscribe block repeating the promise + "No spam. Unsubscribe in one click."

UX: the form validates email inline, shows a success state with a "check your inbox" note and what to expect next; input has a label and autocomplete="email". Loads fast (no heavy animation), AA contrast, looks great on mobile.
```

---

## 33 · Blockhaus — Neo-Brutalist SaaS  `PRO`

```
Create a landing page for [PRODUCT], a [project management / invoicing / scheduling] SaaS, in a confident neo-brutalist style.

DIRECTION: off-white #F5F1E8 background, pure black 3px borders, hard offset shadows (6px 6px 0 #000), flat bright fills: lemon #FFE14D, pink #FF7AB6, cobalt #3A5BFF, mint #7CE0B5. Chunky grotesk display (e.g. Archivo Black) + mono for labels. No gradients, no blur.

SECTIONS:
1. Nav as a bordered bar with square buttons; primary CTA has a hard shadow that "presses" (translate 3px, shadow shrinks) on click.
2. Hero: left-aligned huge headline with one word on a colored highlight block, subline, two buttons, and a right-side stacked "UI card" collage (task card, invoice card, chat bubble) each rotated slightly with borders and shadows.
3. Logo strip in bordered boxes.
4. Features: 6 bordered cards in a grid with a colored header strip each, icon, title, 1 sentence.
5. Interactive demo block: tabs (Board / List / Calendar) switching a mini UI mock.
6. Pricing: 3 bordered cards, recommended one with a sticker ("MOST LOVED") rotated -6°.
7. FAQ as bordered accordion, footer with a giant wordmark.

RULES: brutalist ≠ hard to use: AA contrast, visible focus (4px outline), 44px targets; hover states wiggle max 2°; reduced motion disables wiggle.
```

---

## 34 · Tiles — Bento Personal Site  `FREE`

```
Build a one-page personal site for [NAME], a [ROLE], as a bento grid of tiles that each show one thing about them.

DIRECTION: [light: #F4F4F5 bg, white tiles] or [dark: #0B0B0C bg, #151517 tiles], 24px radius, 12px gaps, one accent [#6366F1]. Clean sans (Inter / Geist).

GRID (desktop 4 columns, tablet 2, mobile 1; tiles have mixed spans):
- Intro tile (2×2): avatar, name, one-line bio, location + local time, "Available for work" status dot.
- Social tiles (1×1 each): GitHub / LinkedIn / X / Dribbble with icon, handle and follower count placeholder; entire tile is the link.
- Now tile: "Currently building…" with a small project image.
- Map tile: stylized map placeholder with a pin on [CITY].
- Music tile: "On repeat" album art + track name + animated equalizer bars.
- Featured project tiles (2×1): screenshot, name, one-line result.
- Writing tile: 3 latest post titles with dates.
- Contact tile: email with copy-to-clipboard and a toast.

DETAILS: tiles lift and slightly brighten on hover; entrance stagger 40ms; everything is a real link or button with focus rings; reduced motion respected; loads fast.
```

---

## 35 · Configure — 3D Product Configurator  `PRO`

```
Create a product configurator page for [PRODUCT] (e.g. a sneaker, chair, bike, or headphones) where customers customize and buy.

LAYOUT: left 60% is the product stage (use a CSS/SVG layered illustration with swappable parts, or a <model-viewer>/Three.js placeholder if the project uses 3D), right 40% is the options panel with a sticky price summary.

STAGE: neutral studio gradient background, soft floor shadow, drag to rotate (or arrows for 4 preset angles), zoom button, "View in your space" placeholder button, and hotspot dots that explain features.

OPTIONS PANEL (stepper: 1 Color · 2 Material · 3 Details · 4 Size):
- Color swatches with names and "Popular" tag; selecting one recolors the matching part with a 300ms transition.
- Material cards (Leather / Knit / Recycled) with price deltas (+$20).
- Details: toggles for extras (monogram text input with live preview on the product, reflective laces, etc.).
- Size selector with a size guide drawer.
- Summary: itemized price, delivery estimate, "Add to bag", "Save design" (shareable URL encoding the options), and "Reset".

UX: every option change updates price and preview instantly; the chosen configuration persists in the URL; disabled combinations explain why ("Monogram not available on Knit"); keyboard support for all swatches (radio groups); AA contrast.
```

---

## 36 · Daybreak — Light AI Agent Startup  `PRO`

```
Design a landing page for [STARTUP], an AI agent that [DOES A JOB, e.g. "handles customer support inboxes"], using a bright, optimistic light theme (not another dark AI site).

DIRECTION: background #FFFCF7 with a soft sunrise gradient at the top (peach #FFD9C2 → lilac #E6DDFF), ink #16151A, accent [#FF6B3D]. Rounded sans display at 80–96px with one word in an italic serif. Soft 1px borders and gentle shadows.

SECTIONS:
1. Hero: headline, subline, email field + "Get early access", and a live-looking "agent at work" card: a task list where items tick off one by one (Read 24 emails → Drafted 18 replies → Escalated 2 to you), with timestamps.
2. "How it works": 3 steps connected by a dotted path: Connect tools → Set rules → Approve or auto-send.
3. Integrations cloud: app-icon placeholders orbiting slowly around the product logo.
4. Human-in-the-loop section: an approval card mock with a diff (before/after reply) and "Approve / Edit / Reject".
5. Metrics: 3 stats with sources (time saved, response time, CSAT).
6. Security & privacy: SOC 2, data retention controls, "your data isn't used to train models" statement placeholder.
7. Pricing (usage-based slider that shows estimated monthly cost), FAQ, footer.

RULES: honest AI copy (no "it thinks like a human"); show what the agent can't do; reduced motion stops the ticking and orbit; AA contrast.
```

---

## 37 · Form & Void — Architecture Studio  `PRO`

```
Build a portfolio website for [STUDIO], an architecture and spatial design practice in [CITY].

DIRECTION: monochrome and architectural. Background #EDEDEA, ink #0E0E0E, zero accent color; photography does the talking. A precise grotesk at light and medium weights; small caps labels; strict 12-column grid with visible thin column lines in the hero only.

SECTIONS:
1. Hero: full-screen image slideshow placeholder (crossfade every 6s, with project name + location + year bottom-left and a progress line).
2. Selected projects index: a text list (number, project, typology, location, year); hovering a row reveals a floating image preview following the cursor; filter by typology (Residential, Cultural, Workplace, Interiors).
3. Project page template: title block, facts table (client, area m², status, team), large images alternating full-bleed and 2-up, drawings (plan/section placeholders on white), and a short text column (max 60ch).
4. Studio: philosophy in 2–3 sentences at large size, team grid (black-and-white portraits), awards list.
5. Contact: address, email, map placeholder, careers link.

MOTION: slow and weighty (800ms+ ease-in-out), image reveals with clip-path wipes; reduced motion = instant.
A11y: alt text that describes the space; keyboard-navigable slideshow with pause; AA contrast.
```

---

## 38 · Roast — DTC Coffee Brand  `PRO`

```
Create a direct-to-consumer e-commerce homepage and subscription flow for [BRAND], a specialty coffee roaster.

DIRECTION: playful craft. Background #F6EFE6, ink #2B1B12, accents from the packaging: [tomato #E2533A], [mustard #E6B422], [sage #8FA98B]. Chunky rounded serif headlines, hand-drawn SVG doodles (beans, steam, stars) as accents.

SECTIONS:
1. Hero: large bag packshot placeholder with a tilted sticker ("Roasted Monday, at your door Wednesday"), headline, "Shop coffee" + "Take the quiz".
2. Taste quiz: 3 questions (how you brew, what flavors you like, milk or black) with illustrated option cards → result card recommending a coffee with a match percentage.
3. Shop grid: bag cards with origin, roast level scale (5 dots), tasting notes chips, price, "Add"; filters by roast and brew method.
4. Subscription builder: choose coffee (or "Roaster's choice"), grind (whole bean / espresso / filter / French press), size, frequency (1/2/4 weeks), with a live price and "save 15%" badge; editable anytime note.
5. Story & sourcing: map placeholder with farm pins and farmer quotes.
6. Reviews + UGC gallery, footer.

UX: cart drawer with subscription vs one-time clearly labeled, free-shipping progress bar, accessible quiz (radio groups), reduced motion for the doodle animations.
```

---

## 39 · Encore — Event Ticketing  `PRO`

```
Design an event ticketing experience for [PLATFORM]: an events discovery page, an event detail page and a seat/ticket selection flow.

DIRECTION: nightlife energy with clarity. Background #0D0B14, ink #F5F3FF, accent [#FF3D7F] with a secondary [#7C5CFF]; event imagery is the color. Condensed display type for event names.

DISCOVERY: city selector, date chips (Tonight, This weekend, Pick dates), category chips (Concerts, Comedy, Sports, Theatre), event cards (image, date badge, title, venue, "from $[X]", "Selling fast" tag when true).

EVENT PAGE: hero image with title, date/time, venue (map link), lineup, "Get tickets" sticky button, set times, venue info (age limit, accessibility, bag policy), refund policy, similar events.

CHECKOUT FLOW:
1. Ticket types (GA, VIP, Accessible) with quantity steppers and remaining counts, or a seat map (SVG sections → zoom into rows; seats as buttons with states: available, selected, unavailable, accessible).
2. A 10:00 hold timer with a clear warning at 2:00.
3. Order summary with all fees shown before payment (no surprise fees), promo code field.
4. Confirmation with QR ticket, add to Apple/Google Wallet placeholders, and "Add to calendar".

A11y: the seat map has a list-view alternative; timers announce via aria-live; AA contrast on dark.
```

---

## 40 · Counsel — Law & Professional Services  `PRO`

```
Build a website for [FIRM NAME], a [law / accounting / consulting] firm serving [AUDIENCE], that feels established, modern and approachable.

DIRECTION: navy #0F1E33 and ivory #F8F5EF, accent muted brass [#B08D57]; classic serif headlines + clean sans body; plenty of whitespace; subtle hairline dividers. No gavel/scales clichés.

SECTIONS:
1. Hero: plain-spoken headline ("Clear advice for growing businesses"), subline, "Book a consultation" + "Our services", and a trust row (years, clients served, ratings, memberships).
2. Practice areas: 6 cards with a short "We help when…" line each, linking to detail pages.
3. Practice page template: who it's for, common situations, how we work (steps), fees approach (fixed-fee packages table), FAQs, related insights.
4. People: filterable team grid (practice, location) with bios, credentials, languages, and a vCard download.
5. Insights: article cards with category, read time, author.
6. Consultation form: topic select, short description, preferred contact method and time; clear note on confidentiality and response time.
7. Offices with maps, regulatory disclaimers in the footer.

RULES: readable legal copy (short sentences), WCAG AA, no stock handshake imagery (use abstract textures or real-office placeholders).
```

---

## 41 · Tides — Boutique Hotel & Resort  `PRO`

```
Create a website for [HOTEL NAME], a boutique [coastal / mountain / city] hotel, that sells the feeling and drives direct bookings.

DIRECTION: slow luxury. Palette drawn from the place: [sand #EDE3D1], [sea #2F5D62], [sunset #D98A5B], ink #1D1B18. Elegant serif display, light sans body; wide margins; imagery at 3:2 and 4:5.

SECTIONS:
1. Hero: full-bleed video/image placeholder with a slow Ken Burns zoom, hotel name, one-line sense of place, and a booking bar (check-in, check-out, guests, "Check availability") that sticks to the top after scrolling.
2. Welcome: short poetic paragraph + 2 offset images.
3. Rooms & suites: cards with image carousel, size, bed type, view, "from $[X]/night", "Explore" → room detail with amenities icons and floor plan.
4. Experiences: horizontal scroller (spa, dining, excursions) with duration and price.
5. Dining: restaurant block with menu link and reservation.
6. Offers: 3 package cards (Stay 3 pay 2, Honeymoon, Early bird) with terms link.
7. Location & getting here, reviews, newsletter, footer with sustainability commitments.

UX: best-rate guarantee message near the booking bar; accessible date picker; reduced motion disables Ken Burns; AA contrast on overlaid text.
```

---

## 42 · On Air — Podcast Site  `PRO`

```
Design a website for "[PODCAST NAME]", a [weekly] podcast about [TOPIC] hosted by [HOST(S)].

DIRECTION: warm studio vibe. Background #121015, ink #F6F1EA, accent [#F59E0B] amber "on air" light; bold rounded display type; cover art is the hero color source.

SECTIONS:
1. Hero: cover art placeholder, show name, one-line promise, "Listen on" buttons (Apple Podcasts, Spotify, YouTube, RSS placeholders), and a latest-episode player: play/pause, ±15s skip, speed (1×, 1.5×, 2×), progress scrubber with chapter markers, and time remaining.
2. Episode list: cards with episode number, title, guest avatar, date, duration, short summary, "Play" (loads into a persistent mini player docked at the bottom that survives navigation), and "Show notes".
3. Episode page: player, chapters (clickable timestamps), guest bio, links mentioned, full transcript with search and "copy link at timestamp".
4. Hosts: photos and short bios.
5. Subscribe/newsletter block and a "Be a guest" / sponsorship inquiry form.
6. Footer with social links.

A11y: transcripts for every episode, labelled player controls, keyboard shortcuts (space, ←/→), AA contrast.
```

---

## 43 · Nest — Interior Design Studio  `PRO`

```
Build a portfolio and inquiry site for [STUDIO], an interior design studio known for [STYLE, e.g. warm minimalism].

DIRECTION: soft and tactile. Background #F3EEE7, ink #2A2522, accents clay [#B7775A] and olive [#6E7250]; fabric/paper texture overlay at 4%; elegant serif headlines + light sans body; rounded-arch image masks as a signature shape.

SECTIONS:
1. Hero: large arch-masked image, headline ("Homes that feel like you"), short subline, "Start a project" CTA.
2. Services: Full-service design, E-design, Styling, each with what's included and starting price.
3. Projects: masonry grid with room-type filters (Living, Kitchen, Bedroom, Commercial); project page with before/after slider, mood board (swatches of materials with names), and a shoppable "Get the look" list.
4. Process: 5 steps timeline (Discovery → Concept → Design → Sourcing → Install) with durations.
5. Testimonials with client home photos.
6. Inquiry form (multi-step): project type, rooms, budget range chips, timeline, inspiration link/upload, contact details; progress indicator and a friendly confirmation.

UX: gentle fade/scale reveals, arch masks animate subtly on hover; accessible before/after slider (range input); AA contrast on light neutrals.
```

---

## 44 · Signal — Live Analytics Hero  `PRO`

```
Create a striking hero + 3 sections for [PRODUCT], a real-time analytics product, built around a live data visualization instead of a static screenshot.

DIRECTION: deep navy #070B17, ink #E6ECFF, data colors cyan [#22D3EE], violet [#8B5CF6], lime [#A3E635]. Tight grotesk display 88–112px; mono for numbers.

HERO: headline ("See every signal as it happens"), subline, CTAs, and behind/next to it a live canvas visualization: a flowing line chart that streams new points every 500ms with a glowing leading dot, a counter ticking "events/sec", and small floating event chips ("signup · Berlin · 2s ago") that fade in and out. Pause when off-screen or tab hidden.

SECTION 2 — Live KPIs: 4 tiles with sparklines and deltas that update every few seconds (use mock data generators with realistic noise).
SECTION 3 — Funnel: an animated funnel with step conversion % and drop-off labels; hover shows counts.
SECTION 4 — Integrations & CTA: SDK install snippet with tabs (JS, Python, Go), copy button, and a final CTA.

PERFORMANCE: single <canvas>, requestAnimationFrame, devicePixelRatio-aware, < 15KB JS for the viz. A11y: the viz has a text summary that updates politely (aria-live="polite", throttled), reduced motion shows a static chart, AA contrast.
```

---

## 45 · Ronin Dawn — Game Launch Landing  `PRO`

```
Build a cinematic launch landing page for "[GAME TITLE]", a [genre, e.g. action RPG] set in [WORLD, e.g. a mythic mountain empire].

DIRECTION: epic key-art first. Full-bleed hero artwork placeholder (a lone original hero character mid-pose in a dramatic environment: falling petals, mist, a huge low sun or moon disc behind them), color grade [deep crimson + ink black + warm ivory]. Title as a massive distressed brush/stencil wordmark overlapping the character (character partly in front of the letters via a layered cut-out: background → title → character → foreground particles). Body type: clean condensed sans; UI in ivory on black.

SECTIONS:
1. Hero: layered parallax (3–4 layers move at different speeds on mouse/scroll), animated drifting particles (petals/embers) on canvas, platform badges (PC / console placeholders), "Wishlist now" primary + "Watch trailer" secondary with a play icon, release date.
2. Trailer: full-width video embed placeholder with a custom poster and a letterboxed frame.
3. World & story: 3 panels with lore art placeholders and short evocative copy.
4. Characters: horizontal selector of 4 original heroes; selecting one swaps a large portrait, name, class, and 3 ability icons with descriptions.
5. Gameplay features: 4 cards with looping GIF/video placeholders (combat, exploration, crafting, co-op).
6. Editions: Standard / Deluxe / Collector's comparison with included items.
7. Newsletter/Discord CTA, age rating, legal footer.

MOTION: dramatic but controlled (600–1000ms), parallax via transform only, particles pause off-screen; prefers-reduced-motion removes parallax and particles.
RULES: all characters and names must be original; no real game IP. AA contrast on text over art (use gradient scrims).
```

---

## 46 · Nova — Coral AI Assistant Landing  `PRO`

```
Create a landing page for "[PRODUCT]", a friendly AI assistant that [turns scattered tasks into a calm daily plan], with a bold single-color hero and a glossy 3D-style product object.

DIRECTION: full-bleed warm coral background [#F2735A] with white typography; one secondary accent [deep teal #0F5E5A] used inside the 3D object; tight modern grotesk display at 88–110px, two short lines. Small spaced uppercase kicker above the headline. Everything else is minimal white UI chrome.

SECTIONS:
1. Nav: logo left, 3 links center, outlined white "Try [PRODUCT]" button right.
2. Hero: left column with kicker, two-line headline (≤ 6 words, a playful contrast like "[Fewer tabs.] [More focus.]"), 2-line subline, a white rectangular CTA with an arrow icon and a round "See it in action" play button. Right column: an original glossy 3D-style device/object (build with layered CSS gradients or a transparent render placeholder) floating above a soft reflection, orbited by 2–3 small white UI chips ("Inbox sorted", "3 tasks planned") and a couple of floating glossy spheres/cubes.
3. Scroll hint row at the bottom: "01 / Meet [PRODUCT]" left, "Scroll to explore" right, thin divider.
4. How it works: 3 steps on white with coral numerals.
5. Use cases: 4 cards (Inbox, Calendar, Notes, Tasks) each with a mini UI mock.
6. Testimonials, pricing (2 plans), FAQ, footer.

MOTION: the object bobs slowly (6s), chips drift in with stagger, the object tilts slightly toward the cursor (max 6°). Reduced motion: static.
RULES: original product shape and name; AA contrast (white on coral must be ≥ 3:1 for large text, use darker coral if needed for small text).
```

---

## 47 · Tidewater — Outdoor Build & Design Services  `PRO`

```
Design a website for [COMPANY], a [pool / landscaping / deck & patio] design-and-build company in [REGION], using a hand-drawn architectural illustration style to feel premium and calm.

DIRECTION: paper-white background, ink-black line illustration hero (a detailed pencil/ink sketch of the finished outdoor space — e.g. a pool with a pergola, loungers, trees and a stone deck — drawn in fine crosshatching, placeholder image), deep navy accent [#0E2A47] for buttons, tiny monospace uppercase labels in the corners, large elegant sans headline with tight tracking.

SECTIONS:
1. Nav: logo left, 5 small uppercase links, navy "Request a quote →" pill right.
2. Hero: corner micro-labels ("DESIGNED · BUILT · WARRANTED" style), the sketch illustration spanning the width, then below it a split row: big headline left ("[Your backyard,] [reimagined.]"), a short paragraph + "Explore our work →" link center, and a round play button "Watch the process" right. A "01 / 04" slide counter with a progress line.
3. Services: 4 columns with small line icons (Design, Build, Landscaping, Maintenance).
4. Projects: before/after slider (sketch → photo placeholder), then a gallery grid with location and year.
5. Process: 5 steps with durations; "Most projects finish in [8–12] weeks".
6. Quote request: multi-step form (project type, size, budget range chips, timeline, address, contact), with a confirmation screen.
7. Reviews, service area map, warranty badges, footer.

MOTION: the sketch "draws in" on load (stroke reveal or mask wipe, 1.2s), subtle parallax on scroll; reduced motion shows it instantly.
RULES: original illustration and company name; AA contrast; form works with keyboard and has clear errors.
```

---

## 48 · Meridian — City Residences (Ink Sketch)  `PRO`

```
Design a luxury residential tower website for "[BUILDING NAME]" in [CITY, e.g. Manhattan], using a hand-drawn ink-sketch hero to feel architectural, timeless and calm.

DIRECTION: paper-white #FBFBF8 background, black ink illustration (placeholder image: a detailed pen-and-pencil sketch of tall skyscrapers seen from street level up an avenue, fine crosshatching, trees and street lamps in the foreground), deep navy accent [#13254A], elegant high-contrast serif headline, small uppercase sans navigation, tiny monospace corner labels.

SECTIONS:
1. Nav: wordmark left, 5 small uppercase links (Residences, Amenities, Neighborhood, Availability, Contact), navy pill "Book a viewing" right.
2. Hero: the sketch spans the full width in a softly bordered frame; below it a split row — headline left ("Live above the city."), a 2-line paragraph center, a round navy play button "Watch the film" right. On load the sketch fades up from 0 with a subtle ink-reveal mask.
3. Residences: tabs (1 bed · 2 bed · 3 bed · Penthouse) with a floor plan placeholder, sqft, views, starting price and "Download floor plan".
4. Amenities: 6 tiles with sketch-style icons (rooftop, spa, library, concierge, gym, residents' lounge).
5. Neighborhood: a hand-drawn map placeholder with numbered pins and a list of nearby places with walking times.
6. Availability table: unit, floor, beds, sqft, price, status (Available / Reserved / Sold) with filters.
7. Viewing request form: name, email, phone, preferred date/time, residence type; confirmation state.
8. Footer: sales gallery address, legal disclaimers, equal-housing line.

RULES: original building name and artwork; AA contrast; tabular numerals in the availability table; reduced motion shows the sketch instantly.
HERO IMAGE PROMPT (paste into Gemini / ChatGPT / Midjourney, 16:10):
"A detailed hand-drawn black ink and pencil architectural sketch of tall New York City skyscrapers seen from street level looking up an avenue, fine crosshatching and linework, trees and street lamps in the foreground, paper-white background, ink only, no text, no watermark."

VIDEO PROMPT (image-to-video, 8 s — upload your hero image to Gemini / Veo or Google Flow):
"Animate this image into an 8-second 16:9 video. Keep the exact composition and framing, and keep the logo, menu, headline, body text and buttons completely still. Animate only the ink sketch of the city street: soft sketched clouds drift slowly behind the skyscrapers, street trees sway gently, a few tiny sketched pedestrians and cars move along the avenue, birds glide between the towers, and the pencil hatching subtly shimmers as if being drawn. Black-and-white hand-drawn ink style, no camera movement, calm and elegant, no color, no new objects."
Tip: generate the still WITHOUT UI text for production, animate it, then keep the real HTML text on top. Loop it with a 1.5 s crossfade (see the AI Art Direction Pipeline skill).
```

---

## 49 · Jade Pavilion — Wuxia Game Launch  `PRO`

```
Build a cinematic launch landing page for "[GAME TITLE]", a [wuxia action-adventure] game set among ancient Chinese mountain temples.

DIRECTION: painterly key art first. Full-bleed hero image (see IMAGE PROMPT) of an original heroine in elegant silk hanfu on temple stairs, misty peaks, plum blossoms, golden sunrise. Title as a huge ivory brush-calligraphy wordmark layered BETWEEN the background and the heroine (background → title → character → foreground petals). Palette: jade green #2F6B5A, imperial red #B8322A, gold #C9A24B, ivory #F4EBDD on ink black. Display: calligraphic/brush display for the title, elegant serif for headings, clean sans for UI.

SECTIONS:
1. Hero: layered parallax (3–4 cut-out layers, transform-only), drifting petal particles on canvas, release date, platform badges, red "Wishlist now" + ghost "Watch trailer".
2. Trailer in a letterboxed frame with an ornamental gold border.
3. The world: 3 scroll-revealed panels (Temple, Bamboo Forest, Imperial City) with art placeholders and short lyrical copy.
4. Heroes: selector of 4 original characters (portrait, name, school of martial arts, 3 abilities).
5. Features: combat, qinggong traversal, crafting, co-op — cards with looping clip placeholders.
6. Editions comparison, newsletter/Discord CTA, ratings and legal footer.

MOTION: graceful, 600–1000ms, ink-wash transitions between sections (mask wipes). Reduced motion removes parallax and particles.
RULES: original characters, names and art; respectful, authentic cultural detail (no caricature); AA contrast via gradient scrims.

HERO IMAGE PROMPT (16:10):
"Cinematic painterly key art for a wuxia video game: an elegant young Chinese heroine in flowing layered silk hanfu in ivory, jade green and crimson with gold embroidery, holding a slender jian sword, standing on long stone stairs leading up to an ancient Chinese mountain temple with curved tiled roofs and red pillars, misty peaks, pine trees and drifting plum blossom petals, soft golden sunrise light, highly detailed, premium AAA game art, no text, no watermark."

VIDEO PROMPT (image-to-video, 8 s — upload your hero image to Gemini / Veo or Google Flow):
"Animate this image into an 8-second 16:9 video. Keep the exact composition and framing, and keep the title lettering, menu and buttons completely still. Animate gently: the heroine's long hair, silk sleeves and ribbons flow softly in the wind, pink cherry blossom petals drift slowly across the frame, mist rolls slowly over the mountains and temple stairs, warm sunlight flickers subtly. No camera movement, calm cinematic motion, no new objects."
Tip: for the live site, animate a clean version of the art (no title) and set the calligraphy title in HTML so it stays crisp. Loop with a 1.5 s crossfade.
```

---

## 50 · Aero — Smart Glasses Launch (Sky)  `PRO`

```
Create a bright, premium launch page for "[PRODUCT]", a pair of everyday smart glasses by [BRAND] (camera, open-ear audio, AI assistant).

DIRECTION: airy and optimistic. Light sky-blue background (#DCEBFA → #F4F9FF gradient), ink #0E1726, accent [#1F6FEB]. The product (see IMAGE PROMPT) floats in soft studio light with a gentle shadow. Rounded geometric sans, headline 96px+, short lines. Lots of whitespace.

SECTIONS:
1. Nav: logo, 4 links, dark pill "Pre-order".
2. Hero: headline ≤ 5 words (e.g. "[See it. Say it. Share it.]"), subline, price "from $[X]", CTAs; the glasses rotate ±10° with the cursor; 3 floating glass chips ("12MP camera", "Open-ear audio", "Hands-free AI").
3. Feature scroll: as you scroll, the glasses zoom into hotspots (camera, speakers, touch strip, battery) with labels.
4. Styles: frame/lens swatches that recolor the product image (Sky, Graphite, Sand; clear / sun / transition lenses).
5. "A day with [PRODUCT]": horizontal cards (commute, run, travel, dinner) with lifestyle photo placeholders.
6. Specs grid, privacy section (capture LED, controls), compare, FAQ, pre-order band, footer.

MOTION: smooth and light (400–700ms), scroll-linked transforms only; reduced motion shows static labeled hotspots.
RULES: original product design and name — do not use or imitate any real brand's glasses, logo or marketing; AA contrast on the light background.

HERO IMAGE PROMPT (16:10):
"Premium product photography of a pair of original modern smart glasses with a slim matte black frame and subtle tiny camera lens in the corner, floating at a slight three-quarter angle, soft studio lighting, gentle shadow, light sky-blue gradient background, minimal, high-end tech launch aesthetic, ultra sharp, no logos, no text, no watermark."
```

---

## 51 · Lumen Fold — Minimal Product Keynote  `PRO`

```
Create a minimal, premium product launch page for "[PRODUCT]" by [BRAND], a [foldable phone / new device], in a clean consumer-tech keynote style: centered type, generous whitespace, one hero product shot.

DIRECTION: light grey canvas #F5F5F7, ink #1D1D1F, secondary #6E6E73, accent blue [#0A66FF] for links and pill buttons. System-UI sans (SF Pro / Inter) — display 600 at −0.04em, 96–120px. A thin dark global nav bar (#161617, 44px) with 8–10 small category links, search and bag icons, and an ORIGINAL logo mark.

SECTIONS:
1. Hero (centered): product name (huge), one-line tagline ("[Open up.]"), two small grey lines with pre-order/availability dates, two pill buttons (solid blue "Learn more", outlined blue "View pricing"), then the hero photo (see IMAGE PROMPT) bleeding off the bottom edge. Hero image scales from 0.94 → 1 and fades in.
2. Highlights carousel: 5 rounded cards on #fff with big captions ("Unfolds to a [7.6]-inch display", "All-day battery", "Pro camera system"), autoplay with pause control, dot pagination.
3. Design: product turning from closed to open on scroll (sequence of 3–5 frames or a CSS 3D hinge illustration), with one short line per state.
4. Feature tiles: 2×2 bento on #fff (Display, Camera, Chip, Durability) with one stat each in large numerals.
5. Compare: 3 models side by side with color dots, sizes, prices and "Buy" links.
6. Trade-in & financing band, then a dense, small-type footer with link columns and legal text.

MOTION: restrained (fade + 16px rise, 700ms); scroll-linked hinge animation uses transform only; reduced motion shows static frames.
RULES: original product name, logo, UI and app icons — do not use any real company's brand, logo, product names or interface; AA contrast; nav collapses to a hamburger under 834px.

HERO IMAGE PROMPT (16:10):
"Realistic premium product photography of an original foldable smartphone opened wide, held by two hands at the bottom edges, its inner screen showing a colorful original home screen with a photo widget, a weather widget and a grid of original rounded app icons, very light grey studio background, soft even lighting, minimal, ultra sharp, no real brand logos or icons, no text, no watermark."
```

---

## 52 · Ember One — Coral Smartphone Launch  `PRO`

```
Create a bold launch page for "[PHONE NAME]", an original smartphone by [BRAND], using a single-color "toy-like premium" style: one saturated background, huge tight white type, and a glossy 3D product on a pedestal.

STYLE ANALYSIS (what makes this look work — keep all of it):
- One full-bleed warm color [coral #E36A4C] everywhere in the hero; no gradients except soft lighting on the product.
- White typography only: a tiny spaced uppercase kicker (11px, +0.2em), a huge two-line headline (96–120px, −0.05em tracking, line-height 0.95) built as a playful contrast ("[Less noise.] [More you.]"), and a 2-line subline at 16px.
- Rectangular (not pill) white CTA with a small arrow + a round outlined play button with a text label.
- Hero object: glossy pearl-white phone with a large circular camera in deep teal glass, tilted ~20°, resting on a glossy white/orange rounded pedestal; soft contact shadow.
- Ambient props: 2 small white UI chips with tiny icons, 1 glossy gold sphere, 2 little white cubes — floating at different depths.
- Frame details: minimal nav (logo left, 3 links center, white rectangular "Pre-order ↗" right), tiny micro-labels in the top-right corner, and a bottom bar with a thin white divider, "01 / MEET [NAME]" left and "SCROLL TO GO DEEPER ↓" right.

SECTIONS:
1. Hero as above. The phone bobs slowly (6s) and tilts toward the cursor (max 6°); chips drift in with a 120ms stagger.
2. Camera: dark section, giant lens close-up, 3 stats (48MP, 5× zoom, Night mode) with counters.
3. Colors: swatch row (Coral, Pearl, Teal, Graphite) recoloring the phone and the page background together.
4. Features: 4 white cards on coral (Battery, Display, Durability, AI) with one big number each.
5. Compare models, trade-in band, pre-order CTA with price, footer.

RULES: original phone design, name and logo — no real brand's product, logo or UI; check contrast (use #C4513A behind small white text); reduced motion = static hero.

HERO IMAGE PROMPT (16:10):
"Glossy 3D product render of an original sleek smartphone in pearl white with a large circular camera module in deep teal glass, tilted at an angle, resting on a glossy white and orange rounded pedestal, two small floating white UI chips, a small glossy gold sphere and two little white cubes, full-bleed warm coral orange background, soft studio lighting, premium, no logos, no text, no watermark."
```

---

## 53 · Lumora — 3D Orb Motion Hero (Video)  `PRO`

```
Build a dreamy, motion-first hero (+ 3 supporting sections) for "[BRAND]", a [wellness / AI / creative studio] brand, where a looping cinematic video sets the mood.

DIRECTION: soft pastel dreamscape. Background video (see VIDEO PROMPT): a glossy iridescent pearl orb slowly rotating above a sea of pastel clouds at golden hour. Overlay a subtle gradient scrim (top and bottom) for legibility. Type: elegant light sans display (weight 300–400) at 88–120px with one word in an italic serif; ink #1B1530 on light areas or white #FFFFFF over the video; accent lilac [#B9A3FF].

HERO:
- Full-viewport <video autoplay muted loop playsinline poster="[poster.jpg]"> with object-fit: cover. Pause it when off-screen (IntersectionObserver) and when document.hidden; show the poster under prefers-reduced-motion or Save-Data.
- Glassmorphism nav pill (blur 16px, white 12%), logo left, 4 links, "Join the waitlist" button.
- Centered headline that reveals word by word (blur 8px → 0, translateY 20px, 80ms stagger), a one-line subline, and two CTAs (solid white, ghost glass).
- A mouse-reactive parallax layer of tiny glowing particles (canvas, ≤ 80 particles) above the video; the headline tilts ≤ 3° toward the cursor.
- Bottom: "Scroll" indicator with a looping line animation.

SECTIONS:
2. Three glass cards that rise on scroll with staggered spring easing, each with a small looping orb icon.
3. A "story" band where the orb (as an image) scales and moves with scroll position (scroll-linked transform), with three short statements fading in and out.
4. Final CTA over a blurred still frame from the video.

PERFORMANCE: video ≤ 4 MB (H.264 MP4 + WebM), 1080p max, preload="metadata"; LCP is the headline text, not the video.
A11y: a pause/play button for the background video, AA contrast with the scrim, keyboard focus visible.

VIDEO PROMPT (Gemini Veo / Runway / Kling / Sora — 16:9, 8s, seamless loop):
"A single large glossy iridescent pearl orb with soft lilac, peach and aqua reflections floating and slowly rotating in the center above a calm sea of soft pastel clouds at golden hour, gentle drifting mist, tiny glowing particles rising, very slow cinematic push-in camera, dreamy premium 3D render, soft volumetric light, smooth calm motion, no people, no text, no logos, no watermark."

POSTER IMAGE PROMPT (16:10): same scene as a still frame, centered orb, wide negative space above for the headline.
```

---

## 54 · Softwork — Eye-Tracking Mascot Studio  `PRO`

```
Build a playful one-screen studio homepage for "[STUDIO]" where an original fuzzy mascot fills the viewport and its eyes follow the visitor's cursor.

DIRECTION: soft, tactile, friendly. Full-bleed mascot image (see IMAGE PROMPT) with object-fit: cover on a warm pale background [#F5E0CF]; ink [#2A1A14]; accent [#E9785F]. Rounded heavy display font (Nunito 900 / similar) for the wordmark and headline; same family 400 for body.

LAYOUT (desktop): wordmark top-left with a small round accent dot; pill nav top-right (Work, Studio, Lab, dark "Say hi"); bottom-left: chip "[got a soft spot?]", headline "[small ideas,] [big hugs.]", one-line subline; bottom-right: bold two-line line "[let's make something you'll want to hug*]" + tiny footnote; bottom-center micro hint "move your cursor · tap on mobile". Under 1000px the two text blocks sit on soft frosted cards and stack.

EYE TRACKING (the signature):
- The image's eyes are blank white discs. Store their centers and radii in SOURCE pixels, e.g. SRC {w:2752,h:1536}, EYES [{x:1182,y:741,rx:85,ry:92},{x:1568,y:741,rx:85,ry:92}].
- On load and resize, map them to the screen using object-fit: cover math: s = max(W/srcW, H/srcH); ox = (W − srcW·s)/2; oy = (H − srcH·s)/2.
- Draw each pupil as an absolutely positioned div (≈ 46% of eye width): dark radial gradient + small white highlight.
- Each frame: direction = cursor − eye center; offset = direction · min(1, distance/(6·rx)) · 0.42·radius; ease with lerp 0.18.
- No input for 4 s → slow idle wander (Lissajous path). Touch: follow the finger.
- Blink every 2.6–5.8 s: a fur-colored ellipse lid scales from 0 → 1 (90 ms) and back.
- prefers-reduced-motion: no easing, no blinking.

RULES: original character only (no existing mascots); all text is real HTML; AA contrast on the text cards; the mascot image is decorative (aria-hidden).

HERO IMAGE PROMPT (16:9):
"A cute original fluffy baby bunny character made of soft peach felt and knitted wool texture, round chubby body filling the lower two thirds of the frame, centered, hugging a small plush mint-green star with both paws. Big friendly face with two large perfectly round plain white eyes WITHOUT any pupils or irises (completely blank solid white circles, clearly separated, same size, facing the camera), small rosy cheeks, tiny pink nose, two long floppy ears. Very pale warm peach background, soft studio lighting, high-end 3D toy render, lots of empty space above the head, no text, no logos, no watermark."
Tip: run the Motif skill script find_eyes.py on the result to get the eye coordinates automatically.
```

---

## 55 · Concord — Human + Robot Motion Hero (Video)  `PRO`

```
Create a calm, premium hero for "[COMPANY]", a [collaborative robotics / AI] company, built around a looping video of a human hand and a robotic hand holding a glowing sphere together.

DIRECTION: bright off-white studio (#F4F4F4 → #FFFFFF), ink #111216, muted #6B6E76, soft iridescent accent (blue/peach/mint) only from the video's sphere. Light geometric sans display (weight 300–400, 64–96px), centered.

HERO:
- Full-bleed <video autoplay muted loop playsinline poster> (see VIDEO PROMPT), object-fit: cover; soft white gradient scrims at top (for the headline) and bottom (for copy) — no dark overlays.
- Nav: wordmark left, a black pill "＋ Menu" toggle, a light pill with two category links, and a right pill with a dark round icon + "Book a demo".
- Centered headline "[Built together.]" + one-line subline "[Human intuition. Machine precision. One shared intelligence.]"; the headline letters fade/rise in with 30ms stagger.
- Bottom-left: small caps kicker + two-line statement; bottom-right: three outlined pill tags (e.g. Haptics, Co-learning, Safety AI); a thin vertical divider between them.
- Optional: the sphere's glow follows the cursor via a radial-gradient light layer (mix-blend: soft-light) for subtle interactivity.

SECTIONS: 3 capability cards with short looping clips, a "how we work together" 3-step strip, trust (safety certifications), CTA.
PERFORMANCE & A11Y: video ≤ 4 MB, pause off-screen and on tab hidden, pause button, reduced-motion shows the poster, AA contrast via scrims.

VIDEO PROMPT (Gemini Veo / Runway / Kling / Sora — 16:9, 8s, seamless loop):
"On a bright soft off-white studio background, a realistic human hand enters from the left and an elegant white-and-silver robotic hand with visible joints enters from the right; together they gently shape and lift a small glowing translucent sphere of light between them, which pulses softly with iridescent blue, peach and mint light, tiny particles drifting, the hands move slowly and gracefully in sync like collaborators, soft diffused lighting, shallow depth of field, very slow camera drift, minimal premium tech aesthetic, no text, no logos, no watermark."
```

---

## 56 · Northbound — Polar Expedition Travel  `PRO`

```
Create a luxury expedition-travel site for "[COMPANY]", a small-ship operator running [Arctic and Antarctic] voyages. The mood is quiet, cold and expensive: think printed field journal, not cruise brochure.

STYLE:
- Palette: ice white #F4F6F7, glacier blue #A9C6D3, deep fjord #0E2230, one signal accent [expedition orange #E8642C] used only on CTAs and route lines.
- Type: a refined serif for headlines (60–96px, −0.02em), a mono for coordinates and data (12px, +0.12em uppercase), a clean grotesk for body.
- Every section has a small coordinate label in the corner ("78°13′N 15°38′E") and a thin hairline grid, like a nautical chart.

SECTIONS:
1. Hero: full-bleed photo of a small expedition ship among sea ice (see HERO IMAGE PROMPT). Headline "[Go where the map goes quiet.]", a single orange "Plan a voyage" button and a secondary "View 2027 departures". A live-looking strip at the bottom: water temp, daylight hours, next departure countdown.
2. Route explorer: an SVG polar map; hovering a voyage card draws its route as an animated orange dashed line (stroke-dashoffset), with day markers that pop in.
3. Voyages: 3 tall cards (photo, duration, ship, from-price, "only 4 suites left" scarcity chip that is real data, not fake).
4. Life on board: horizontal scroll of journal entries — date, coordinate, a short first-person note and a photo, styled like taped polaroids.
5. Ship & suites: tabbed deck plan with selectable suite types and a price-per-person toggle.
6. Expedition team: naturalists and guides with credentials.
7. Sustainability: 3 honest numbers with sources; footer with a request-a-call form (name, dates, party size, budget band).

MOTION: slow parallax on ice layers, drifting snow particles (canvas, ≤ 60 flakes, paused off-screen), route draw on scroll. prefers-reduced-motion = static map with routes visible.

RULES: original ship and brand; no real operator names; AA contrast on photos (gradient scrim); prices with "from" and currency.

HERO IMAGE PROMPT (16:10):
"Cinematic wide photo of a small modern dark-hulled expedition ship moving slowly through scattered blue sea ice at golden hour in the polar regions, low sun, pale pink and blue sky, mist on the water, distant snowy mountains, calm and luxurious, lots of empty sky on the left for a headline, no text, no logos, no watermark."
```

---

## 57 · Prism Bench — Optics Lab Instrument Maker  `PRO`

```
Create a product site for "[BRAND]", a maker of precision optical benches and lens kits for labs, schools and makers. The page should feel like a beautiful instrument: dark, exact, and alive with light.

STYLE:
- Background near-black #07080A with a faint 8px dot grid; panels in #101217 with 1px #1E222A borders.
- Light is the hero: rainbow dispersion (prism spectrum) and thin laser lines in [cyan #38E1FF], [magenta #FF3DCB] and [amber #FFB020].
- Type: a technical grotesk; big numbers in tabular figures; mono labels like "λ 532 nm · f/2.8 · ±0.01 mm".

SECTIONS:
1. Hero: an interactive canvas ray simulator. A white beam enters from the left, hits a glass prism in the center and splits into a spectrum. The user drags the prism (or moves the cursor) to rotate it, and the refraction angles update live using Snell's law (n≈1.52, use per-color n for dispersion). Headline "[Bend light. Measure everything.]", CTA "Configure a bench".
2. Components: a grid of parts (lenses, mirrors, beam splitters, mounts) as clean 3D-ish cards; hover shows a spec sheet flyout.
3. Configurator: pick rail length, light source and 4 components; a live side-view diagram and the total price update instantly; "Add to quote".
4. Experiments: 6 lesson cards (focal length, interference, polarization …) with difficulty and time.
5. Specs table with tolerances; testimonials from labs; FAQ; footer with distributors.

MOTION: beam rendering at 60fps with additive blending; a subtle caustic shimmer on panels; numbers tick when they enter. Reduced motion = static spectrum render.

RULES: original brand and product shapes; physics should look plausible; keyboard control for the prism (arrow keys rotate); the canvas has a text alternative.

HERO IMAGE PROMPT (16:10, for social/thumbnail):
"Dark minimal studio photo of a precision optical bench on black: a clear glass prism splitting a thin white laser beam into a vivid rainbow spectrum, thin cyan and magenta laser lines, small anodized black lens mounts on a rail, faint dot grid, crisp reflections, lots of dark empty space on the left, no text, no logos, no watermark."
```

---

## 58 · Wobble Co. — Squishy Toy & Slime Shop  `PRO`

```
Create a joyful DTC store for "[BRAND]", which sells handmade slime, putty and squishy toys. It should feel tactile and silly but still be a serious, fast shop.

STYLE:
- Candy palette on cream #FFF7EC: bubblegum #FF7AB6, lime #B8F15A, grape #8C6CFF, sky #6FD3FF; ink #2B1B3A.
- Chunky rounded display type (very heavy, tight, slightly bouncy baseline), thick 3px ink outlines on cards and buttons, hard offset shadows (6px 6px 0 ink).
- Everything is a blob: buttons, badges and image masks use soft organic border-radius shapes.

SECTIONS:
1. Hero: a big glossy slime blob (SVG/CSS metaball or a canvas soft body) that stretches toward the cursor and jiggles on click with a squelch-y spring. Headline "[Squish responsibly.]", CTA "Shop the drop", a sticker "New: Galaxy Goo".
2. Texture picker: tabs for Fluffy, Crunchy, Clear, Butter, Cloud — each changes the hero blob material (gloss, sparkle, matte) and filters products below.
3. Products: cards with a looping 3-second "poke" video or GIF on hover, scent and texture chips, rating, quick-add button with a bounce.
4. Build-a-slime: choose base, color, add-ins and scent; a jar preview fills with the chosen color; shows price and "ships in 2 days".
5. Safety & ingredients (non-toxic, age guidance) — clear and parent-friendly; reviews wall; Instagram-style UGC grid; footer with a newsletter that promises "1 email a week, max".

MOTION: springy everything (overshoot 1.2), stickers that wobble on hover, confetti on add-to-cart (≤ 40 pieces). Reduced motion = no jiggle, simple fades.

RULES: original brand and mascot; honest safety copy; cart works without JS animation; AA contrast on candy colors (use ink text, not white, on lime and sky).

HERO IMAGE PROMPT (16:10):
"Playful glossy 3D render of a big bubblegum pink slime blob being stretched, with lime and grape colored slime swirls and tiny star sparkles mixed in, soft studio lighting, cream background, a few small glossy candy-colored spheres floating, cheerful and tactile, lots of empty space on the left, no text, no logos, no watermark."
```

---

## 59 · Duotone Press — Riso Print Studio  `FREE`

```
Create a site for "[STUDIO]", a small risograph print studio that prints zines, posters and art prints. It should look printed: two inks, misregistration, grain.

STYLE:
- Paper #F3EEE3 background with a subtle grain (SVG feTurbulence noise at 6% opacity).
- Only two "inks" plus paper: [fluorescent pink #FF48B0] and [blue #0078BF]. Where they overlap, use mix-blend-mode: multiply to get the purple overprint.
- Halftone images: run photos through a CSS/SVG halftone (or pre-processed dots) in one ink each.
- Type: a condensed heavy grotesk for headlines, set huge and slightly misregistered — the pink layer offset 3px right/2px down from the blue layer.

SECTIONS:
1. Hero: giant two-layer headline "[Two inks. Infinite trouble.]" where the layers drift slightly apart with the cursor (max 6px) and snap back. A stamped circular badge "Open studio · Thursdays". CTA "Get a quote".
2. Services: zines, posters, art prints, stationery — cards that look like index cards with a hand-drawn underline.
3. Ink library: swatch dots for available inks; clicking two inks re-colors the whole page live (CSS variables) so visitors can preview their combo.
4. Price calculator: paper size, quantity, ink count, paper stock → instant price and turnaround.
5. Shop: prints by local artists with edition numbers ("12/50").
6. Workshop dates, map, footer with an email signup styled as a tear-off coupon.

MOTION: ink layers slide in from slight offsets, a printer "feed" animation on the quote button. Reduced motion = static overprint.

RULES: original studio and artwork; AA contrast (blue ink text on paper passes, pink is for large type and decoration only).
```

---

## 60 · Fall Line — Downhill Ski Race Event  `PRO`

```
Create an event site for "[EVENT]", a weekend downhill ski race and festival in [MOUNTAIN TOWN]. Energy of a race-day poster, information clarity of a timing board.

STYLE:
- Snow white #F7F9FB and deep night #0B1220 sections alternate; race accent [safety red #FF2D2D] and a timing yellow [#FFD400].
- Type: an extended, italic sports display face for headlines (slanted for speed), tabular mono for times ("1:42.38").
- Diagonal layout: section edges cut at the slope angle (clip-path, ~8°).

SECTIONS:
1. Hero: full-bleed action photo (see HERO IMAGE PROMPT). Headline "[The mountain doesn't wait.]" with a live countdown to the start (days/hours/min/sec flip digits). CTAs "Register to race" and "Get spectator pass".
2. Course: an elevation-profile SVG of the run; scroll moves a skier dot down the line while stats update (vertical drop, max gradient, gates, record time).
3. Schedule: a two-day timeline with tabs (Fri/Sat), each slot with time, title and location; "Add to calendar" per slot.
4. Live results board: a dark timing table with bib, name, country flag emoji, split times and gap; new rows slide in; demo data clearly marked "sample".
5. Categories & fees, festival lineup (music, food), travel & lodging partners, FAQ, footer with a sponsor strip (placeholder logos).

MOTION: speed-line streaks on hero scroll, digit flips on the countdown, results rows slide. Reduced motion = static.

RULES: original event and town; no real athlete names; times in tabular numerals; registration form accessible.

HERO IMAGE PROMPT (16:10):
"Dynamic action photo of a ski racer in a red suit carving a hard turn on a steep groomed piste, snow spray exploding in sunlight, blue sky, sharp alpine peaks, shot from low angle with a telephoto lens, motion and speed, lots of empty sky on the right for a headline, no text, no logos, no bib numbers, no watermark."
```

---

## 61 · Static FM — Independent Internet Radio  `FREE`

```
Create a site for "[STATION]", an independent internet radio station with live shows, resident DJs and an archive. Late-night, underground, very playable.

STYLE:
- Black #0A0A0A, off-white #EDEDE6, one acid accent [#C6FF3D]. Occasional scanline overlay (repeating-linear-gradient, 4% opacity).
- Type: a bold grotesk set in all caps for the logo and show names, a mono for times and track IDs.
- Layout like a broadcast schedule: lots of thin rules, time columns, "ON AIR" indicators.

SECTIONS:
1. Hero: a persistent live player — big play/pause, "ON AIR" pill blinking, current show, DJ, and a live waveform/spectrum visualizer (Web Audio AnalyserNode when playing; animated placeholder when paused). Headline "[Tune out. Tune in.]".
2. Schedule: today's grid in the visitor's time zone, the current slot highlighted and a "now" line that moves.
3. Residents: DJ cards with a portrait, genres as chips, next show time.
4. Archive: searchable list of past shows with tag filters; clicking one loads it into the same persistent player (it keeps playing across sections).
5. Support the station: membership tiers, merch, footer with socials and a "submit a mix" form.

MOTION: visualizer bars, marquee of tracklist, hover glitch on show titles (2 frames, subtle). Reduced motion = no glitch, static bars.

RULES: original station name and DJs; the player is keyboard accessible with labels; never autoplay audio.
```

---

## 62 · Halden — Quiet Fashion Store  `PRO`

```
Create an ecommerce site for "[BRAND]", a slow-fashion label making a small seasonal collection. The style is calm, editorial and confident: large photography, a lot of air, tiny type.

STYLE:
- Bone #EFEBE4 background, charcoal #1C1B19 text, one muted accent [olive #6B6A4A].
- Type: a light high-contrast serif for big editorial words (120px+), a small 12–13px grotesk in uppercase with +0.08em tracking for nav, prices and labels.
- Images are the layout: asymmetric 12-column grid where photos span 5/7/4 columns and overlap section edges.

SECTIONS:
1. Hero: one full-height editorial photo (see HERO IMAGE PROMPT) with the season name "[AW27 — The Long Field]" in the giant serif, and "Shop the collection" as a quiet underlined link.
2. Lookbook: a horizontal scroll-snap story of 6 looks; each look shows the pieces worn with "Shop this look" hotspots.
3. Product grid: 2 images per card (swap on hover), name, price, color dots; filter by category, size and color without page reloads.
4. Product page: big gallery, size selector with a fit guide modal, fabric and care, "made in" details, delivery & returns, and complete-the-look suggestions.
5. Atelier story: process photos with short captions; footer with a newsletter and store addresses.

MOTION: slow image reveals (clip-path from bottom, 900ms), cursor-following "View" label over images, smooth cart drawer. Reduced motion = simple fades.

RULES: original brand; real sizing information fields; accessible product options (radio groups); price formatting per currency.

HERO IMAGE PROMPT (16:10):
"Editorial fashion photograph of a model in a relaxed olive wool coat and cream knit walking through a tall golden autumn field at dusk, soft overcast light, muted earthy palette, film grain, calm and minimal, the figure placed on the right third with lots of empty field and sky on the left, no text, no logos, no watermark."
```

---

## 63 · Facet — Fine Jewelry Configurator  `PRO`

```
Create a luxury jewelry site for "[BRAND]" where customers design an engagement ring: pick a stone, a cut, a metal and a band, then see it rendered beautifully.

STYLE:
- Velvet black #0B0A0C with warm highlights, champagne gold [#D8B983], soft white #F7F3EC.
- Type: an elegant didone for headlines with generous letter spacing on small caps; a quiet sans for UI.
- Lighting is the brand: sparkles, soft glints and slow highlights sweeping across text (background-clip text with a moving gradient).

SECTIONS:
1. Hero: a large ring render (see HERO IMAGE PROMPT) that slowly rotates (sprite sequence or a simple three.js model with an environment map). Small glints sparkle at random facets. Headline "[Made to be looked at.]", CTA "Design your ring".
2. Configurator: step tabs (Stone → Cut → Metal → Band → Engraving). Each choice updates the preview and a running price; cut shapes shown as clean line icons; carat slider with a size-on-hand preview.
3. The 4Cs explained in an honest, visual way with a comparison slider.
4. Craft: atelier process timeline; ethical sourcing with certificates.
5. Book an appointment (in store or video), reviews, FAQ (sizing, resizing, warranty), footer.

MOTION: highlight sweeps, sparkle particles (≤ 24, randomized), configurator crossfades at 300ms. Reduced motion = no sparkles.

RULES: original designs and brand; never claim certifications you don't have; price shown "from" until all steps are chosen; accessible step navigation.

HERO IMAGE PROMPT (16:10):
"Luxury macro product photo of an original solitaire engagement ring with a brilliant round diamond on a slim champagne gold band, resting on dark velvet, dramatic soft studio light, tiny bright sparkles and caustic light reflections, shallow depth of field, elegant and minimal, lots of dark empty space on the left, no text, no logos, no watermark."
```

---

## 64 · Lattice — Particle Sphere Intelligence Hero (Video + Canvas)  `PRO`

```
Create a premium dark landing page for "[PRODUCT]", a [data / AI intelligence platform]. The hero is a living particle sphere wrapped in thin orbit rings: calm, precise, a little cosmic.

STYLE ANALYSIS (keep all of it):
- Background near-black #050608 with a very faint film grain (SVG noise, 4%) and a soft teal radial glow behind the sphere (rgba(40,170,210,.25)).
- One accent: electric cyan [#39C6FF] for the kicker dot, particles and active states. Everything else is white-to-grey.
- Type: a geometric sans at weight 500. Kicker 13px uppercase +0.18em in cyan with a 7px dot before it. Headline 84–104px, −0.045em, line-height 1.02, filled with a vertical gradient (#FFFFFF → #9AA1AB) via background-clip:text. Body 19px #8B929C, max 470px wide.
- Nav: small script/italic wordmark left, 4 uppercase links centered (13px, +0.06em, grey), outlined pill "Join the beta" right.
- Buttons: two pills. Primary has a dark-to-teal gradient fill and a 1px teal border with a small glowing "thumb" on its left edge that slides right on hover; secondary is outlined.
- Layout: copy left (40%), sphere right (60%), the sphere's orbit rings extend past the viewport edge on the right and bottom.

HERO HEADLINE (swap freely): kicker "[SIGNAL PLATFORM]", headline "[See the shape / of your data.]", body "[PRODUCT] maps every event, agent and customer into one living graph, so your team can see patterns before they become problems.", buttons "Start exploring" and "Read the docs".

THE SPHERE (build it in canvas, no libraries):
- 1,400 points on a sphere using a Fibonacci lattice (golden angle) for even spacing; radius = 34% of the hero height.
- Rotate slowly around Y (0.06 rad/s) and tilt 18° on X. Project with a simple perspective (fov 600). Size and opacity scale with depth: back points 0.6px at 15% opacity, front points 2.4px at 90%.
- 40 "nodes": every 35th point is drawn larger (4–6px) with a soft glow (shadowBlur 12, cyan) and a subtle pulse.
- 6 "signals": short bright cyan streaks that travel along great-circle arcs between random nodes (ease-in-out over 1.6s, fading tail); spawn a new one every 0.8s.
- 3 orbit rings: thin ellipses (1px, cyan at 18–30% opacity) at different tilts, each slowly precessing; one small bright satellite dot rides the outer ring.
- Interaction: the sphere tilts up to 10° toward the cursor (lerp 0.06); on scroll it drifts right and fades as the next section arrives.
- Performance: devicePixelRatio capped at 2, pause the loop when the hero is off-screen or the tab is hidden, and a static frame for prefers-reduced-motion.
- OPTIONAL VIDEO MODE: instead of canvas, play the looping video from the VIDEO PROMPT below as <video autoplay muted loop playsinline poster>, mix-blend-mode: screen over the black background, and keep the text as live HTML.

SECTIONS:
2. Logo strip (placeholder customer logos, grey, 40% opacity).
3. "How it works": three steps (Connect · Map · Act), each with a small canvas mini-sphere that shows the step (raw dots → connected graph → highlighted path).
4. Feature grid: 6 dark glass cards (1px #1A1E24 border, hover lifts and lights the border cyan) — Live graph, Anomaly alerts, Agent actions, Private by design, API, Audit trail.
5. Big metric band: three counters ("2.4B events / day", "38 ms p95", "99.99% uptime") with tabular numbers.
6. Pricing (3 tiers), FAQ accordion, a final CTA with a smaller sphere, footer.

RULES: original product name, logo and copy; no real company names or logos; AA contrast for body text on black (#8B929C passes at 19px); keyboard focus rings in cyan; the hero works without JavaScript (static gradient + text).

VIDEO PROMPT (16:9, 8 s, for Gemini / Veo):
"Create a video, 16:9, 8 seconds, seamless loop, no text: on a pure black background, a glowing sphere made of thousands of tiny cyan and blue light particles slowly rotates, a few larger glowing nodes pulse softly, thin bright light streaks travel across the sphere's surface like data signals, two or three very thin translucent cyan orbit rings circle around it at different angles with a small bright dot moving along one ring, subtle teal glow in the center, very slow cinematic camera drift, calm, precise, premium technology aesthetic, no logos, no watermark."

HERO IMAGE PROMPT (16:10, poster / thumbnail):
"Wide dark website hero art: on a black background on the right side, a sphere made of thousands of tiny glowing cyan particles with a few larger bright nodes and thin light streaks across it, surrounded by thin translucent cyan orbit rings that extend off the right edge, soft teal glow inside, fine film grain, lots of empty black space on the left for a headline, no text, no logos, no watermark."
```

---

*© Motif. Licensed for use in your own and client projects. Do not resell or redistribute the prompts themselves.*
