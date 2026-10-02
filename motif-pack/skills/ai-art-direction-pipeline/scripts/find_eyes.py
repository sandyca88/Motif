"""Find blank white eye discs in a character image.  usage: find_eyes.py image.jpg [--preview crop.jpg]
Prints eye centers/radii in SOURCE pixels. Works best when the eyes were generated without pupils."""
import sys, argparse
from collections import deque
import numpy as np
from PIL import Image, ImageDraw
a = argparse.ArgumentParser(); a.add_argument('src'); a.add_argument('--preview', default='eyes-preview.jpg'); a.add_argument('--min', type=int, default=225); a.add_argument('--sat', type=int, default=16)
o = a.parse_args(); im = Image.open(o.src).convert('RGB'); S = 4
sm = np.asarray(im.resize((im.width // S, im.height // S))).astype(int)
H, W, _ = sm.shape; mask = (sm.min(2) > o.min) & ((sm.max(2) - sm.min(2)) < o.sat); seen = np.zeros_like(mask); comps = []
for y in range(H):
    for x in range(W):
        if mask[y, x] and not seen[y, x]:
            q = deque([(y, x)]); seen[y, x] = 1; pts = []
            while q:
                cy, cx = q.popleft(); pts.append((cy, cx))
                for dy, dx in ((1,0),(-1,0),(0,1),(0,-1)):
                    ny, nx = cy + dy, cx + dx
                    if 0 <= ny < H and 0 <= nx < W and mask[ny, nx] and not seen[ny, nx]: seen[ny, nx] = 1; q.append((ny, nx))
            if len(pts) > 30: comps.append(pts)
comps.sort(key=len, reverse=True); eyes = []
for p in comps[:2]:
    ys = [q[0] for q in p]; xs = [q[1] for q in p]
    eyes.append(dict(x=int((min(xs)+max(xs))/2*S), y=int((min(ys)+max(ys))/2*S), rx=int((max(xs)-min(xs))/2*S), ry=int((max(ys)-min(ys))/2*S)))
eyes.sort(key=lambda e: e['x'])
if len(eyes) == 2:  # symmetric character: shading often shrinks one disc, so use the larger size for both
    rx = max(e['rx'] for e in eyes); ry = max(e['ry'] for e in eyes); y = max(eyes, key=lambda e: e['rx'])['y']
    big = max(eyes, key=lambda e: e['rx']); small = min(eyes, key=lambda e: e['rx'])
    small['x'] = small['x'] + (rx - small['rx']) * (1 if small['x'] > big['x'] else -1)
    for e in eyes: e.update(rx=rx, ry=ry, y=y)
print('source size', im.size); print('EYES =', eyes)
if eyes:
    d = ImageDraw.Draw(im)
    for e in eyes: d.ellipse([e['x']-e['rx'], e['y']-e['ry'], e['x']+e['rx'], e['y']+e['ry']], outline=(255,0,0), width=6)
    pad = 300; xs = [e['x'] for e in eyes]; ys = [e['y'] for e in eyes]
    im.crop((max(0, min(xs)-pad), max(0, min(ys)-pad), min(im.width, max(xs)+pad), min(im.height, max(ys)+pad))).save(o.preview)
    print('check outline accuracy in', o.preview, '(if shading split a disc, widen --sat or edit by hand)')
