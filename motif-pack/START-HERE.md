# Start here: Motif

Thanks for supporting Motif! This folder holds everything in your plan.

## What's inside

| Folder / file | What it is |
|---|---|
| `skills/` | Agent Skills and deck styles. Each folder has a `SKILL.md`. |
| `claude-app-zips/` | The same skills, zipped one by one for the Claude app. |
| `motif-website-prompts.md` (free download: `motif-free-prompts.md`) | Website prompts (design briefs for AI site builders). |
| `assets/` | Hero video loops for the cinematic templates (Pro only). |
| `examples/` | Working demo pages you can open in a browser (Pro only). |
| `THUMBNAIL-IMAGE-PROMPTS.md` | Image prompts for recreating the hero art (Pro only). |
| `LICENSE.txt` | What you can and can't do with these files. |

## Use a skill

- **Claude app (claude.ai / desktop):** Customize → Skills → **+** → Create skill → **Upload a skill**, then pick a zip from `claude-app-zips/`. Switch it on, then ask Claude to use it.
- **Claude Code:** copy a folder from `skills/` into `~/.claude/skills/` (all projects) or `.claude/skills/` (one project).
- **Cursor:** copy a folder into `~/.cursor/skills/` or your project's `.cursor/skills/`. Type `/` in Agent chat to pick it.
- **Codex:** copy a folder into `~/.codex/skills/` and restart Codex.

Example: `cp -R skills/ux-heuristic-audit ~/.claude/skills/`

## Use a website prompt

1. Open `motif-website-prompts.md` and pick a prompt.
2. Replace every **[BRACKET]** with your own name, copy and details.
3. Paste it into **Lovable, v0, Bolt, Cursor or Claude** and let it build, then iterate ("make the hero calmer", "add pricing").
4. For templates with art, use the **HERO IMAGE PROMPT** / **VIDEO PROMPT** at the end of the prompt in Gemini or another image/video tool. Ready-made loops are in `assets/`.

A prompt is a detailed design brief, not finished code. Your AI tool builds the site, so results vary by tool and model.

## Use a deck style

Install a `deck-…` skill, then ask: *"Make a 10-slide investor deck about [topic] using the Obsidian deck style."* You get an HTML deck you can present or print to PDF.

## Help

Full guide with screenshots-free steps: https://sunny-crumble-7de34c.netlify.app/#/guide
Stuck or lost your link? https://sunny-crumble-7de34c.netlify.app/#/contact/order

Please don't share or re-upload these files. Your license covers your own and your clients' projects.
