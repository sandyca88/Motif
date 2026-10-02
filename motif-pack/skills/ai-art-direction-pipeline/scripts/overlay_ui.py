"""Render a transparent website-UI overlay PNG from a JSON spec, to composite on an AI video/image.
usage: overlay_ui.py spec.json out.png
spec: {"size":[1152,720],"font":"path.ttf","bold":"path-bold.ttf","display":"path-display.otf","ink":"#111216",
       "scrim":{"left":0.38,"top":0,"bottom":0,"color":"#ffffff"},"logo":"brand","nav":["Work","Studio"],"cta":"Get started",
       "kicker":"SMALL CAPS LINE","headline":["Line one","line two"],"headline_pos":[60,260],"headline_size":74,"align":"left",
       "sub":"Subline text","buttons":["Primary","Secondary"],"bottom":["01 / INTRO","SCROLL ↓"]}"""
import json, sys
from PIL import Image, ImageDraw, ImageFont
s = json.load(open(sys.argv[1])); W, H = s.get('size', [1152, 720])
hexc = lambda c, a=255: tuple(int(c.lstrip('#')[i:i+2], 16) for i in (0, 2, 4)) + (a,)
ink = hexc(s.get('ink', '#111216')); F = lambda k, n: ImageFont.truetype(s.get(k) or s['font'], n)
ov = Image.new('RGBA', (W, H), (0, 0, 0, 0)); sc = s.get('scrim', {})
if sc:
    m = Image.new('L', (W, H), 0); md = ImageDraw.Draw(m); col = hexc(sc.get('color', '#ffffff'))
    if sc.get('left'):
        L = int(W * sc['left'])
        for x in range(L): md.line([(x, 0), (x, H)], fill=int(110 * (1 - x / L) ** 1.5))
    if sc.get('top'):
        T = int(H * sc['top'])
        for y in range(T): md.line([(0, y), (W, y)], fill=max(m.getpixel((0, y)), int(120 * (1 - y / T))))
    if sc.get('bottom'):
        B = int(H * sc['bottom'])
        for y in range(H - B, H): md.line([(0, y), (W, y)], fill=int(150 * ((y - (H - B)) / B)))
    ov.paste(col, (0, 0), m)
d = ImageDraw.Draw(ov)
d.text((40, 30), s.get('logo', ''), font=F('bold', 24), fill=ink)
x = W // 2 - 60 * len(s.get('nav', [])) // 2
for t in s.get('nav', []): d.text((x, 34), t, font=F('font', 16), fill=ink[:3] + (200,)); x += 100
if s.get('cta'):
    tw = d.textlength(s['cta'], font=F('bold', 16)) + 36; d.rounded_rectangle([W - 40 - tw, 24, W - 40, 60], radius=18, fill=ink); d.text((W - 40 - tw + 18, 32), s['cta'], font=F('bold', 16), fill=(255, 255, 255, 255))
hx, hy = s.get('headline_pos', [60, 260]); hs = s.get('headline_size', 72); center = s.get('align') == 'center'
if s.get('kicker'): d.text((hx, hy - 26), s['kicker'], font=F('bold', 13), fill=ink[:3] + (190,))
for i, line in enumerate(s.get('headline', [])):
    f = F('display', hs); tx = (W - d.textlength(line, font=f)) / 2 if center else hx; d.text((tx, hy + i * hs * 1.05), line, font=f, fill=ink)
y = hy + len(s.get('headline', [])) * hs * 1.05 + 16
if s.get('sub'):
    f = F('font', 19); tx = (W - d.textlength(s['sub'], font=f)) / 2 if center else hx; d.text((tx, y), s['sub'], font=f, fill=ink[:3] + (215,)); y += 56
bx = hx
for i, b in enumerate(s.get('buttons', [])):
    f = F('bold', 17); tw = d.textlength(b, font=f) + 44
    if i == 0: d.rounded_rectangle([bx, y, bx + tw, y + 44], radius=22, fill=ink); d.text((bx + 22, y + 11), b, font=f, fill=(255, 255, 255, 255))
    else: d.rounded_rectangle([bx, y, bx + tw, y + 44], radius=22, fill=(255, 255, 255, 140), outline=ink[:3] + (80,)); d.text((bx + 22, y + 11), b, font=f, fill=ink)
    bx += tw + 14
if s.get('bottom'):
    d.line([(60, H - 44), (W - 60, H - 44)], fill=(255, 255, 255, 150)); f = F('bold', 12)
    d.text((60, H - 34), s['bottom'][0], font=f, fill=(255, 255, 255, 230)); d.text((W - 60 - d.textlength(s['bottom'][-1], font=f), H - 34), s['bottom'][-1], font=f, fill=(255, 255, 255, 230))
ov.save(sys.argv[2]); print('saved', sys.argv[2])
