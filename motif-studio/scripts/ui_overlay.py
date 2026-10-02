"""Draw a website UI layer (transparent PNG) to put over an AI video or image.
usage: python3 ui_overlay.py spec.json out.png
spec keys (all optional except headline):
  size [1152,720] · theme "dark"|"light" · accent "#39c6ff" · scrim_left 0.5 (0 = none)
  logo "Lattice" · nav ["PLATFORM","FEATURES"] · cta "Join the beta"
  kicker "SIGNAL PLATFORM" · headline ["See the shape","of your data."] · headline_size 70
  body ["line 1","line 2"] · buttons ["Start exploring","Read the docs"] · x 56 · y 276
Fonts: Poppins from /usr/share/fonts/truetype/google-fonts if present, else DejaVu.
"""
import json, os, sys
from PIL import Image, ImageDraw, ImageFont
s = json.load(open(sys.argv[1])); W, H = s.get('size', [1152, 720])
G = '/usr/share/fonts/truetype/google-fonts/'
def F(w, n):
    for p in (G + {'r': 'Poppins-Regular.ttf', 'm': 'Poppins-Medium.ttf', 'b': 'Poppins-SemiBold.ttf', 'i': 'Poppins-LightItalic.ttf'}[w],
              '/usr/share/fonts/truetype/dejavu/DejaVuSans' + ('-Bold' if w == 'b' else '') + '.ttf'):
        if os.path.exists(p): return ImageFont.truetype(p, n)
    return ImageFont.load_default()
hexc = lambda c, a=255: tuple(int(c.lstrip('#')[i:i + 2], 16) for i in (0, 2, 4)) + (a,)
dark = s.get('theme', 'dark') == 'dark'
ink, mut, bg = ((242, 244, 247, 255), (139, 146, 156, 255), (5, 6, 8)) if dark else ((10, 10, 10, 255), (100, 116, 139, 255), (255, 255, 255))
acc = hexc(s.get('accent', '#39c6ff' if dark else '#2848e0'))
ov = Image.new('RGBA', (W, H), (0, 0, 0, 0))
sl = s.get('scrim_left', 0.5)
if sl:
    m = Image.new('L', (W, H), 0); md = ImageDraw.Draw(m); L = int(W * sl)
    for x in range(L): md.line([(x, 0), (x, H)], fill=int(235 * (1 - x / L) ** 1.4))
    ov.paste(bg + (255,), (0, 0), m)
d = ImageDraw.Draw(ov); X = s.get('x', 56); Y = s.get('y', 276)
if s.get('logo'): d.text((44, 30), s['logo'], font=F('i', 24), fill=ink)
nx = W // 2 - 140
for t in s.get('nav', []):
    f = F('m', 12); d.text((nx, 38), t, font=f, fill=mut); nx += d.textlength(t, font=f) + 34
if s.get('cta'):
    f = F('m', 14); tw = d.textlength(s['cta'], font=f) + 40
    d.rounded_rectangle([W - 44 - tw, 26, W - 44, 62], radius=18, outline=mut, width=1); d.text((W - 44 - tw + 20, 34), s['cta'], font=f, fill=ink)
if s.get('kicker'):
    d.ellipse([X + 4, Y - 26, X + 11, Y - 19], fill=acc); d.text((X + 22, Y - 32), s['kicker'], font=F('m', 13), fill=acc)
hs = s.get('headline_size', 70); y = Y
for line in s.get('headline', []):
    d.text((X, y), line, font=F('m', hs), fill=ink); y += int(hs * 1.08)
y += 14
for line in s.get('body', []):
    d.text((X + 2, y), line, font=F('r', 17), fill=mut); y += 27
y += 28; bx = X + 2
for i, b in enumerate(s.get('buttons', [])):
    f = F('m', 15); tw = d.textlength(b, font=f) + 48
    if i == 0: d.rounded_rectangle([bx, y, bx + tw, y + 48], radius=24, fill=acc[:3] + (235,)); d.text((bx + 24, y + 12), b, font=f, fill=(255, 255, 255, 255))
    else: d.rounded_rectangle([bx, y, bx + tw, y + 48], radius=24, outline=mut, width=1); d.text((bx + 24, y + 12), b, font=f, fill=ink)
    bx += tw + 14
ov.save(sys.argv[2]); print('saved', sys.argv[2], W, H)
