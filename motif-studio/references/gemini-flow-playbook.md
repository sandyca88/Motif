# Gemini & Google Flow playbook (Claude in Chrome)

Use Sandy's **personal** Google account only. Confirm it before generating:
`[...document.querySelectorAll('[aria-label*="@"]')].map(e=>e.getAttribute('aria-label'))` → must show `tosandy@gmail.com`.

## Gemini (gemini.google.com/app)

**Insert a prompt** (typing is unreliable):
```js
const ed=document.querySelector('rich-textarea .ql-editor');ed.focus();
document.execCommand('insertText',false,"<prompt>");
```
**Send:** `find "Send message button"` → click the ref. If nothing happens, click the round arrow by coordinates (bottom-right of the input). Return/Enter often does nothing.

**Upload an image** (for image-to-video or edits). Clicking "Upload files" opens a native picker you can't control, so intercept it:
```js
const oc=HTMLInputElement.prototype.click;
HTMLInputElement.prototype.click=function(){if(this.type==='file'){window.__fi=this;if(!this.isConnected){this.style.display='none';document.body.appendChild(this)}return}return oc.call(this)};
```
Then open **Upload & tools → Upload files**, `find "file input"` (pick the one where `e===window.__fi`, accept="" or image), and `file_upload` with the path. The file limit for the upload tool is **10 MB**.

**Video:** "I'm generating your video…" takes 1–3 min; then "Your video is ready!". Background tabs show black thumbnails (normal). Hover the video → `find "Download video button"` → click. The file lands in `~/Downloads` as `gemini_generated_video_<id>.mp4` (1280×720, 8–10 s, with audio).
**Daily limit:** the page title changes to "Video Generation Limit Reached". Switch to Flow.

**Image:** "Download full size image" → `Gemini_Generated_Image_<id>.jpeg` (≈2752×1536 or 2624×1632). If the first click fails, hover the image and retry.

## Google Flow (labs.google/fx/tools/flow → flow.google.com)

1. Home → **New project**.
2. Install the same file-input hook, click the **+** in the chat panel → **Upload media** → `file_upload` to the new input. Upload all stills you need (they appear in the asset picker).
3. Select an asset → **Add to prompt**, click the chat box (bottom right), type the prompt, click the **→** arrow (Return doesn't send).
4. Flow asks *"kick off this video generation, costing 10 credits?"* → click **Approve** (once per video; never "Always approve" unless Sandy says so). Sandy has authorised using her Flow plan for Motif.
5. When the tile shows a play icon: right-click it → **Download → 720p Original size** (270p = GIF, 1080p = upscale). Files are named after the prompt, e.g. `Animate_image_into_video_<timestamp>.mp4`. The grid reflows as new tiles appear, so take a fresh screenshot before right-clicking.

## Image-to-video tips (worked for Jade Pavilion & Meridian)

- Say what must stay still: *"keep the exact composition and framing, and keep the title lettering, menu and buttons completely still"*.
- Animate only natural things: hair, silk, petals, mist, light; for sketches: drifting sketched clouds, birds, swaying trees, pencil-hatching shimmer.
- Results that accumulate (petals piling up, clouds appearing) need a crossfade loop. Pick a stable window (e.g. 2–8 s) for `loop_thumb.sh`.

## After download → thumbnail

```bash
# poster / still thumbnail (16:10 WebP)
python3 motif-pack/skills/ai-art-direction-pipeline/scripts/prepare_image.py in.jpeg build/thumb-images/<key>.webp --ratio 16:10 --width 1600
# animated thumbnail (seamless loop, 960×600, ~0.6–1.4 MB)
bash scripts/loop_thumb.sh in.mp4 build/thumb-images/<key>.mp4 2 8 1.5
# text-free AI video + website UI on top
python3 scripts/ui_overlay.py spec.json /tmp/ov.png
bash motif-pack/skills/ai-art-direction-pipeline/scripts/make_loop_thumb.sh in.mp4 /tmp/ov.png /tmp/<key>
```
Keep the raw loop as a Pro bonus: `motif-pack/assets/<key>/<key>-…-1280x720.mp4` (re-encode `-an -crf 22`).
The storefront picks up `<key>.webp` / `<key>.mp4` automatically (`.mp4` plays on hover/visible, `.webp` is the poster).
