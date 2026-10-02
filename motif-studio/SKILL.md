---
name: motif-studio
description: Sandy's end-to-end playbook for running Motif, her storefront of AI website prompts, Agent Skills and deck styles. Use whenever the user mentions Motif or wants to study a reference site (Aura, MotionSites, Skillry, Fluxa…) and make an original template, write a new website prompt, generate hero images or videos with Gemini or Google Flow, make animated thumbnails, add items or free picks to the storefront, change the site design or theme, rebuild the Pro/Free bundles, update the Drive delivery file, handle PayPal sales and buyer emails, or prepare a release for Netlify.
---

# Motif Studio

Motif is Sandy's shop of **copy-paste website prompts, Agent Skills and deck styles** ("made by a UX designer").
Live site: https://sunny-crumble-7de34c.netlify.app (Netlify project `sunny-crumble-7de34c`).
Project folder: **`~/Downloads/Motif/`** (in the sandbox: `/sessions/<id>/mnt/Downloads/Motif/`). If the folder isn't connected, ask the user to select it before doing anything.

## Where the files are

The full playbook lives next to the project in **`~/Downloads/Motif/motif-studio/`**: `references/*.md` (read the one a step needs) and `scripts/` (run from `~/Downloads/Motif`). Paths below are relative to `~/Downloads/Motif/`. If that folder is missing, ask Sandy to connect her Downloads folder.

## Ground rules (always)

1. **Never push to Netlify unless Sandy says so in this conversation.** Build and preview locally, show screenshots, wait for "push to Netlify".
2. **Originals only.** Study references for *qualities* (palette, type, layout, motion), never copy their prompts, code, images, videos, names, copy or logos. No real brands, products, trademarks or real people's likeness. Third-party free skills are only listed as **credited link-outs** after checking their license. See `motif-studio/references/reference-to-original.md`.
3. **Personal accounts only** for Gemini / Google Flow (tosandy@gmail.com). Never use Equinix/work tools or credits (e.g. Figma Weave) for Motif.
4. **No Pro leaks.** Pro prompt text stays truncated on the site (420 chars); full prompts, Pro skills and assets only ship in the Pro zip delivered by Drive link. Never put the Drive link on the website.
5. **Honest claims.** Prompts are design briefs, not finished code; don't say "tested in X" unless it was tested. Count Motif-made items separately from free community picks.
6. **Ask before big visual or pricing changes;** make concept files (a separate preview HTML) instead of changing the real template when Sandy says "show me a concept".
7. Follow the org rule: only Equinix Nexus registries if any package install is ever needed; prefer the preinstalled Python, Pillow and ffmpeg.

## The workflow

| Step | What to do | Details |
|---|---|---|
| 1. Reference → idea | Open the reference (built-in browser renders JS pages; Chrome tabs render blank in the background). Write a short style analysis, then change subject, name, copy and composition. | `motif-studio/references/reference-to-original.md` |
| 2. Write the prompt | Use the house format (STYLE ANALYSIS → SECTIONS → MOTION → RULES → HERO IMAGE PROMPT / VIDEO PROMPT). Add it to `prompts/motif-website-prompts.md` and the index table. Mark `FREE` or `PRO`. | `motif-studio/references/prompt-format.md` |
| 3. Make the art | Image: Gemini. Video: Gemini (daily limit) or Google Flow (10 credits/video, approve each). Image-to-video for existing stills. Then crop/loop/overlay into a thumbnail. | `motif-studio/references/gemini-flow-playbook.md`, `motif-studio/scripts/` |
| 4. Add to the store | Add the item tuple, thumbnail, optional demo, featured/picks order. Rebuild and verify. | `motif-studio/references/storefront-guide.md` |
| 5. Check | `python3 motif-studio/scripts/check_site.py .` → rebuild, JS syntax, Pro-leak check, counts, banned phrases. Screenshot key pages in **both** themes before reporting. | `motif-studio/scripts/check_site.py` |
| 6. Ship files | `python3 motif-pack/build/bundle.py` rebuilds the Pro/Free zips. Copy the Pro zip to Downloads; Sandy uploads it as a **new version** of the same Drive file (link stays the same). | `motif-studio/references/sales-ops.md` |
| 7. Release | Only when asked: upload `motif-site.zip` on Netlify → Deploys (drag and drop). Verify live. | `motif-studio/references/sales-ops.md` |
| 8. Sales | PayPal one-time payments → tracker row → welcome email with Drive link. | `motif-studio/references/sales-ops.md` |

## Look & feel

Dark theme is the default; light mode is white + cobalt blue, Inter-style sans, no purple gradients. Logo = gradient squircle with eyes (keep). Details and tokens: `motif-studio/references/brand.md`.

## Scripts

- `motif-studio/scripts/check_site.py <project>`: rebuild + all checks; prints a short report.
- `motif-studio/scripts/loop_thumb.sh in.mp4 out.mp4 [start end fade]`: crop 16:9→16:10, 960×600, seamless crossfade loop, no audio.
- `motif-studio/scripts/ui_overlay.py spec.json out.png`: draws website UI (nav, kicker, headline, body, buttons) on a transparent 1152×720 PNG to composite over an AI video; then use the Pro skill's `make_loop_thumb.sh` or ffmpeg overlay.
- The sellable Pro skill `motif-pack/skills/ai-art-direction-pipeline/` has more art tools (prepare_image, find_eyes, eyes_frames, make_loop_thumb). Reuse them; don't duplicate.

## Reporting back

Lead with what changed and what Sandy needs to do (e.g. upload a new Drive version, approve credits, say "push to Netlify"). Mention anything unverified. Keep it short.
