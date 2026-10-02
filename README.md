# Motif

Source for **Motif**, a storefront of copy-paste AI website prompts, Agent Skills and deck styles, made by a UX designer.
Live site: https://sunny-crumble-7de34c.netlify.app

> **Keep this repository private.** It contains the full Pro prompts, Pro skills and bonus video assets that customers pay for.
> All rights reserved. Third-party free picks are only linked, never included.

## What's here

| Path | What it is |
|---|---|
| `motif-pack/skills/` | 29 Motif skills and deck styles (each folder has a `SKILL.md`) |
| `motif-pack/prompts/motif-website-prompts.md` | All 64 website prompts |
| `motif-pack/build/` | Site template, item list, thumbnails, and build scripts |
| `motif-pack/assets/`, `examples/`, `brand/` | Video loops, live demo pages, logo files |
| `motif-studio/` | Sandy's personal Claude skill: the full workflow, references and helper scripts |

## Build

Requires Python 3 with Pillow, plus `zip`, `ffmpeg` and `node` for some scripts.

```bash
python3 motif-pack/build/package_site.py     # builds motif-site/ and motif-site.zip (upload to Netlify)
python3 motif-pack/build/bundle.py           # builds Pro/Free bundles into motif-pack/dist/
python3 motif-studio/scripts/check_site.py . # checks: syntax, Pro-leak, media, counts
```

Build output (`motif-site/`, `dist/`, zips) and private business files (buyer tracker, email templates with the delivery link) are git-ignored on purpose.
