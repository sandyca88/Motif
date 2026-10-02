---
name: mascot-avatar-set
description: Design a consistent set of original character avatars or mascots as clean, scalable SVGs: one shared construction system (head shape, eyes, hair, color tokens) producing 8–24 unique variations, plus a grid sheet, individual files and usage guidance. Use when the user asks for avatars, profile pictures, a mascot family, default user avatars, team characters, community stickers, emoji-like characters, or a character set for a product or brand.
license: Commercial. See LICENSE.txt
---

# Mascot Avatar Set

Produce a *family* of characters that look like they came from one designer: same construction rules, varied personalities.

## 1. Brief

Confirm or infer: brand/product, personality (friendly / playful / techy / calm), count (default 12), background use (light, dark or both), and where it will be used (profile pictures, empty states, stickers). **Only design original characters.** If the user names an existing character, mascot or brand figure, explain that you'll make an original one inspired by the *mood* instead.

## 2. Construction system (define before drawing)

Write this spec block first, then follow it for every avatar:

| Part | Rule |
|------|------|
| Canvas | 256×256 viewBox, character centered, 16px safe padding; works when cropped to a circle |
| Head base | pick ONE family shape: blob, rounded square, circle or bean. Vary only proportions (±10%) |
| Eyes | 3–4 eye styles max (dots, ovals, happy arcs, glasses). Same stroke weight everywhere |
| Mouth | 3–4 styles (smile arc, open "o", grin, flat) |
| Hair / top | 6–8 styles built from simple shapes (curls from circles, spikes from triangles, bun, cap, leaf, antenna) |
| Color tokens | 6–8 body colors + 1 ink color + 1 highlight; every avatar uses exactly 1 body + 1 accent |
| Stroke | either all outlined (3–4px ink stroke, round caps) or all flat. Never mixed |
| Shading | one flat highlight shape at 25% white, top-left. No gradients unless the whole set has them |
| Skin tones (humanlike sets) | include a diverse range, evenly distributed across the set |

## 3. Generate variations

- Build each avatar by combining parts deterministically (e.g. avatar *i* uses hair `i % 8`, eyes `(i*3) % 4`, color `(i*5) % 8`) so the set is balanced and no two are identical.
- Check the set as a grid: no two neighbors share the same body color; each part style appears roughly equally often.
- Give each character a short name and a one-word personality tag.

## 4. Output

1. `avatars/avatar-01.svg` … `avatar-NN.svg`: clean SVG (no embedded rasters, ids prefixed to avoid collisions, `role="img"` + `<title>`).
2. `avatar-sheet.html`: a presentation grid showing every avatar on its colored tile with name and number, plus light and dark background rows and a circle-crop preview row.
3. `avatars.json`: `[{id, name, tag, colors, parts}]` for use in apps.
4. If asked, a React component `<Avatar seed="user@email.com" />` that hashes a string to pick parts, so every user gets a stable avatar.
5. Usage notes: minimum size (32px), clear-space, do/don't (no stretching, no recoloring outside tokens).

## Quality bar

- Readable at 32px: test by rendering a 32px row in the sheet.
- Consistent optical size: heads fill ~70% of the canvas height.
- Expressions are friendly and inclusive; avoid caricatured features or stereotypes.
- Files are small: target < 3KB per SVG.
