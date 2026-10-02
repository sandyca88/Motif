# Storefront guide (how the Motif site is built)

Everything lives in `~/Downloads/Motif/`:

```
Motif/
├─ motif-pack/
│  ├─ build/
│  │  ├─ build.py                 item list → motif-storefront.html
│  │  ├─ storefront_template.html  the whole site (CSS + JS, hash router)
│  │  ├─ thumbs_a.py … thumbs_m.py coded HTML thumbnails, T["<key>"] = BASE + "<html>"
│  │  ├─ thumb-images/            <key>.webp / .jpg / .png poster, <key>.mp4 animated
│  │  ├─ package_site.py          build + public motif-site/ folder + motif-site.zip
│  │  └─ bundle.py                per-skill zips + Pro/Free bundles (dist/)
│  ├─ prompts/motif-website-prompts.md   all website prompts
│  ├─ skills/<skill>/SKILL.md     Motif skills & deck styles (Pro unless in FREE list)
│  ├─ assets/<key>/…mp4           bonus video loops (Pro bundle)
│  ├─ examples/<demo>/index.html  live demos (copied to site samples/)
│  ├─ brand/                      logo PNGs, OG image (copied to site)
│  ├─ dist/                       built zips (Pro zip is NEVER published)
│  ├─ START-HERE.md, LICENSE.txt, FREE-PICKS.md, THUMBNAIL-IMAGE-PROMPTS.md, PAYMENTS-SETUP.md
│  └─ ops/ (copy of tracker + email templates)
├─ motif-site/        public site folder (rebuilt; deletions may be blocked, so files are overwritten)
└─ motif-site.zip     what gets uploaded to Netlify
```

## Add an item (build.py `items` list)

Tuple: `(key, title, category, kind, tags, free, prompt#, desc, zip)`
- `kind`: `"prompt"`, `"skill"` or `"deck"`; `prompt#` = two-digit number for prompts, else `None`.
- `zip`: skill folder name for skills/decks (e.g. `'taste-layer'`), else `None`.
- Free skills must also be in `FREE` in `bundle.py`.
- Thumbnail: add `T["<key>"]` in a thumbs file (new file → import it at the top of build.py and merge into `TH`), and/or drop `<key>.webp`/`.mp4` into `thumb-images/`.
- Extras in the loop after the list: `d['sample']` + `d['samplelabel']` for a live demo (also copy the folder in `package_site.py`); `EXT` dict for third-party link-outs (`d['ext']`, `d['lic']`, `d['site']`, tag `open-source`).

## Ordering knobs

| What | Where |
|---|---|
| Home "Cinematic templates" + Prompts "Featured" | `HERO3=[...]` in the template |
| Editor's picks rank | `PO=(...)` in build.py |
| Free page top items | `TOPFREE=[...]` in `fill()` |
| Skills page community row first card | `OSSFIRST=[...]` in `ossStrip()` |
| Prompts gallery default | items with real image/video first, then newest |
| Skills/Free "Newest" | Motif items first, link-outs last |

## Pages (hash routes)

`#/` home (hero, chat finder, featured, categories, picks, new) · `#/prompts` gallery · `#/skills` (community strip on top) · `#/decks` · `#/free` · `#/item/<key>` · `#/pricing` (plans, What you get, FAQ) · `#/guide/<tab>` · `#/thanks/<plan>` · `#/contact[/order]` · `#/legal/<license|refunds|terms|privacy|delivery>`.

## Config constants (template)

`PAYPAL.business` (sandyca88@yahoo.com), `PLANS` (pro $49 one-time 1 year, life $99, tips), `LIVE_SITE`, `CONTACT_TO` (FormSubmit → tosandy.work@gmail.com; must be activated on the live site; Netlify Forms is the suggested upgrade), `LEMON` (empty; Lemon Squeezy links later), `SIGNIN_ENABLED=false`.

## Gotchas learned

- Code that runs on first render (route()) must be defined **before** `function route`, or the page goes blank (TDZ). `node --check` won't catch it, so screenshot the page.
- Light theme uses `html[data-theme=light]` overrides at the end of the CSS; avoid hardcoded dark colors (use `--surf`, `--surf2`, `--tx2`, `--mut`, `--inv`). Check both themes.
- Counts: `own(kind)` = Motif-made only; `count(kind)` includes link-outs. Use `own` for anything describing the Pro download.
- Preview: `present_files` an HTML copy with `<script>location.hash="#/…"</script>` injected after `<head>` to open a specific page; force light mode by replacing the theme init. Name previews `zz-*.html` or `*-preview.html` (excluded from the zip) and clean them up.
- The preview panel can't fetch the web; thumbnails load from the local thumbs/ folder.

## Rebuild & verify

```bash
cd ~/Downloads/Motif
python3 motif-pack/build/package_site.py      # site + motif-site.zip
python3 motif-pack/build/bundle.py            # Pro/Free zips (after skill/prompt/asset changes)
python3 <skill>/scripts/check_site.py .       # all checks
```
