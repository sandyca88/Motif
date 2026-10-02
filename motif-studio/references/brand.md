# Motif brand & UI

**Voice:** "made by a UX designer". Calm, confident, plain English. Honest about what's included. No hype words, no fake urgency or fake counts.

**Logo:** gradient squircle (conic violet → cyan → pink) with two white eyes that follow the cursor and blink (`.mk`). Keep it in both themes. Concepts B (morph) and C (family) are sold in the Animated Mascot Logo Kit, not used on the site.

## Dark theme (default)

| Token | Value |
|---|---|
| `--bg` / `--card` / `--surf` | #0b0b0c / #141416 / #101012 |
| `--tx` / `--tx2` / `--mut` | #f5f5f7 / #cfcfd6 / #8e8e96 |
| Accents | violet #8b5cf6, cyan #22d3ee, pink #f472b6 (gradient word in headline, kickers in cyan) |
| Buttons | white pill (`.btn.w`), outline pill (`.btn.g`) |

## Light theme (white + cobalt, inspired by clean fintech sites)

| Token | Value |
|---|---|
| `--bg` / `--card` | #ffffff / #ffffff, hairline borders #e8eaee |
| `--tx` / `--tx2` / `--mut` | #0a0a0a / #334155 / #64748b |
| Accent `--blue` | #2848e0 (text, kickers, highlighted word), button gradient #3d5cff → #2848e0 with soft blue glow |
| Type | Inter-style sans, headings −0.045em, highlighted word in solid blue (no serif italic, no gradients) |

Sandy tried a violet light mode and chose to **keep blue**.

## Layout decisions (home)

Badge → big headline "Give your AI agent *real* [rotating word]" → subline → one-line chat finder pill (All/Website/Skill/Deck) → Browse prompts / Start free → **Cinematic templates** (Jade Pavilion, Meridian, Concord) above the fold → category cards → Editor's picks → New this month (Motif items only) → community picks → Pro teaser. No stats row (it duplicated the category counts).

## Thumbnails

16:10 cards. Prefer real Gemini/Flow art or video for flagship items; coded HTML previews (1280×800, `BASE` from thumbs_a.py) for the rest. Free-pick cards: dark gradient card with FREE + license chips, title, chips, "by <author> · via GitHub", small abstract art.
