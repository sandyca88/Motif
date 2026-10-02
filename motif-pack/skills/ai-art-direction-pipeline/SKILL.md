---
name: ai-art-direction-pipeline
description: Produce premium hero art for websites with AI image and video generators (Gemini / Imagen / Veo, ChatGPT, Midjourney, Runway, Kling, Sora) and turn it into production assets — art-directed prompts, style analysis of a reference, original (non-infringing) variations, eye-tracking character pages, looping video backgrounds, UI overlays for animated thumbnails, cropping, compression and web-ready posters. Use when the user wants AI-generated hero images, product shots, mascots, background videos, animated thumbnails, "make it look like this reference", eye-follow effects, or asks how to generate art for a website or template.
license: Commercial — see LICENSE.txt
---

# AI Art Direction Pipeline

The exact workflow behind Motif's Gemini-made templates (Meridian, Jade Pavilion, Aero, Ember One, Lumora, Softwork, Concord). Five stages: **Analyze → Direct → Generate → Engineer → Ship.**

## 1. Analyze the reference (never copy it)

When the user shares a reference site or image, write a short **style analysis** before any prompt:

| Layer | Questions |
|-------|-----------|
| Color | One saturated field or a gradient? How many accents? |
| Type | Weight, tracking, line breaks, contrast pairs ("Less noise. More you.") |
| Hero object | What is it, what material, how is it lit, what does it sit on? |
| Props | Chips, spheres, particles, stickers — how many, what depth? |
| Frame | Nav style, corner micro-labels, bottom scroll bar, dividers |
| Motion | What moves, how fast, what reacts to the user? |

Then **change the subject, name, copy and composition** while keeping the qualities. Rules:
- No real brands, logos, product names, UI or characters (e.g. use "an original foldable phone", never a named product).
- No reusing another creator's prompt text, video, illustration or logo — even if you can see it.
- Real people: never generate a likeness of a real person.

## 2. Direct — the prompt formulas

**Website-screenshot prompt (thumbnail / marketing image)**
```
Generate an image, wide 16:10 landscape. A [style] website [section type] shown as a flat front-on desktop
screenshot, no browser frame. [Background]. [Nav: logo 'NAME' left, links, CTA right]. [Headline 'TEXT' —
font feel, color]. [Subline]. [Buttons]. [Hero object: material, angle, lighting, what it rests on].
[Props]. [Bottom bar]. Premium Awwwards quality, crisp readable text, no real brand logos, no watermark.
```

**Clean hero-art prompt (for the live site — no UI baked in)**
```
[Subject, material, pose] + [setting] + [lighting] + [camera/lens] + [palette] + "lots of empty space
[where the headline goes]" + "no text, no logos, no watermark".
```

**Loop video prompt**
```
Create a video, 16:9, 8 seconds, seamless loop, no text: [one subject] [one slow action] [environment],
[particles/atmosphere], very slow cinematic [push-in/drift] camera, [lighting], smooth calm motion,
no logos, no watermark.
```
Keep one action per clip. Ask for "seamless loop" and "slow" — fast motion compresses badly and distracts from copy.

**Eye-tracking character prompt** — the key trick is to request eyes WITHOUT pupils:
```
... two large perfectly round plain white eyes WITHOUT any pupils or irises (completely blank solid white
circles, clearly separated, same size, facing the camera) ...
```

## 3. Generate (Gemini in the browser)

1. Use the user's **personal** account — never a work/company account's credits for personal projects.
2. Paste the prompt; for video, wait 1–3 minutes ("Your video is ready").
3. Pick the best of 1–3 attempts; regenerate rather than accepting garbled text or extra fingers.
4. Download full size (images ≈ 2752×1536 JPEG, videos 1280×720 MP4 with audio).

## 4. Engineer

Scripts are in `scripts/` (Python 3 + Pillow + ffmpeg).

- **`prepare_image.py in.jpg out.webp [--ratio 16:10] [--width 1600]`** — center-crop to the card ratio, resize, WebP q82 (typically 40–250 KB).
- **`find_eyes.py bunny.jpg`** — detects the blank white eye discs (bright, low-saturation connected regions) and prints centers and radii in source pixels. Always verify with the printed crop preview; adjust by hand if shading splits a disc.
- **`overlay_ui.py`** — renders a transparent PNG with nav, kicker, headline, buttons and a bottom bar using a JSON spec, so an AI video becomes an animated *website* thumbnail.
- **`make_loop_thumb.sh video.mp4 overlay.png out.mp4`** — crops 16:9 → 16:10, composites the overlay, strips audio, scales to 960×600, H.264 CRF 27, `+faststart` (≈ 300–450 KB for 10 s).
- **`eyes_frames.py`** — renders an orbiting-pupils + blink loop from a still (for an animated thumbnail of an eye-tracking page).

**Eye-tracking implementation** (see `examples/eye-follow.html`):
- Store eye centers/radii in source-image pixels; compute `object-fit: cover` scale `s = max(W/srcW, H/srcH)` and offsets to map them to the screen on every resize.
- Pupil = dark radial-gradient circle (≈ 46% of eye width) with a white highlight; travel ≤ 42% of the eye radius, eased (lerp 0.18 per frame), scaled down when the cursor is close.
- Idle wander after 4 s without input; touch support; blink every 2.6–5.8 s with a fur-colored lid ellipse; `prefers-reduced-motion` disables easing and blinking.

**Video hero implementation:** `<video autoplay muted loop playsinline preload="metadata" poster>` + `object-fit: cover`, pause off-screen (IntersectionObserver) and on `document.hidden`, visible pause button, gradient scrim for AA contrast, LCP = headline text.

## 5. Ship

- Thumbnails: `name.webp` (poster) + optional `name.mp4` (animated) — the storefront picks them up automatically.
- Put the **art prompt inside the template** (`HERO IMAGE PROMPT` / `VIDEO PROMPT` sections) so buyers can regenerate or restyle the art.
- Offer the raw loop video as a bonus asset; never ship another creator's assets.
- Final checks: no garbled text in the visible area, no brand marks, contrast AA on overlaid text, file sizes in budget.
