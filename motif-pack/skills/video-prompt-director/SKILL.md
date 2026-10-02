---
name: video-prompt-director
description: Write cinematic, model-ready prompts for AI video generators (Veo, Sora, Kling, Runway, Pika, Luma, Seedance, Wan, Hailuo and similar): subject, action, camera move, lens, lighting, style, pacing, audio and negative cues, with shot lists and per-model variants. Use when the user wants to generate an AI video clip, B-roll, product shot, ad, music-video moment, social reel, or asks how to prompt a text-to-video or image-to-video model.
license: Commercial. See LICENSE.txt
---

# Video Prompt Director

Treat every prompt like a one-shot film brief. Video models reward **concrete, visual, time-ordered** language. They struggle with abstract adjectives, too many subjects and multiple actions at once.

## 1. Brief (infer or ask once)

Goal and platform (ad, reel 9:16, YouTube 16:9, website hero loop), duration (4–10s per shot is the sweet spot), model if known, whether there's a reference image (image-to-video), and whether audio is needed (for models that generate sound).

## 2. The 8-part shot formula

Write each shot in this order, one sentence or phrase per part:

1. **Shot type & framing**: extreme wide, wide, medium, close-up, macro, overhead, POV.
2. **Subject**: who or what, with 2–3 specific visual details (materials, colors, clothing, age range). Original characters only.
3. **Action**: ONE clear action with a verb and a direction ("pours coffee slowly into a glass cup, steam rising").
4. **Setting**: place, time of day, weather, background elements.
5. **Camera movement**: static / slow push-in / dolly left / orbit 90° / crane up / handheld follow / rack focus. Add speed.
6. **Lens & look**: focal length (24mm wide, 50mm natural, 85mm portrait, 100mm macro), depth of field, film stock or grade ("soft pastel grade", "high-contrast noir", "Kodak-like warm film").
7. **Lighting & mood**: key light direction and quality ("golden-hour backlight, rim light on hair"), atmosphere (haze, dust motes).
8. **Audio** (when supported): ambient sound, SFX, music mood; dialogue in quotes with the speaker named. Otherwise omit.

End with **constraints**: aspect ratio, duration, "no text on screen", "no logos", "consistent character".

**Example (product B-roll, 16:9, 6s):**
> Macro close-up of a matte-black ceramic mug on a walnut table, morning light. Hot coffee is poured in from above, a thin stream forming a swirl as crema rises. Slow push-in, 100mm macro, shallow depth of field, creamy bokeh. Warm golden side light from a window at left, faint steam drifting upward. Soft café ambience and the gentle sound of pouring. 16:9, 6 seconds, no text, no logos.

## 3. Multi-shot sequences

For anything longer than one clip, produce a **shot list** table:

| # | Duration | Shot | Prompt | Transition | Continuity notes |
|---|----------|------|--------|------------|------------------|

Continuity rules: repeat the exact subject description in every shot (copy-paste the "character sheet" line), keep lighting and time of day consistent, alternate shot sizes (wide → medium → close) to cut smoothly, and use match cuts on motion.

## 4. Image-to-video

When a reference image is provided: don't re-describe what's already in the image. Describe **only the motion, camera and change over time** ("the model turns her head toward camera and smiles; slow push-in; hair moves in a light breeze"). Keep motion modest to avoid warping.

## 5. Per-model adaptation

- **Long natural-language models** (e.g. Veo, Sora): full sentences, cinematic vocabulary, audio lines supported by some.
- **Keyword-leaning models** (some Kling/Pika/Wan modes): tighter comma-separated phrases, key terms first, plus a short negative prompt.
- **Runway/Luma-style camera controls**: move camera instructions into the tool's camera settings when available, and keep the text prompt about subject and look.
Always tell the user which parameters to set outside the prompt (duration, aspect ratio, seed, motion strength). Model features change often, so recommend checking the model's current prompt guide.

**Negative cues** (where supported): blurry, warped hands, extra limbs, flicker, text artifacts, watermark, low resolution.

## 6. Output

1. A one-line **creative direction** (mood + look).
2. The **prompt(s)**, each in its own code block, ready to paste.
3. For sequences, the **shot list table** and a **character/style sheet** line to reuse.
4. **Settings** to use (aspect, duration, motion strength, seed tips) and 2 variations (e.g. different camera move or lighting) for A/B testing.

## Rules

- No real people's likeness, celebrities, trademarked characters or brand logos unless the user owns the rights.
- One action per shot; split complex actions into multiple shots.
- Prefer showing over telling: "rain streaks on the window, neon reflections" beats "moody".
