"""Render an orbiting-pupils + blink loop from a still with blank eyes (for animated thumbnails).
usage: eyes_frames.py image.webp out.mp4 --eyes "x,y,rx,ry;x,y,rx,ry" [--lid "#F0B99B"] [--frames 96]
Eye values are in the image's own pixel space (run find_eyes.py first and scale if you resized)."""
import argparse, math, os, subprocess, tempfile
from PIL import Image, ImageDraw
a = argparse.ArgumentParser(); a.add_argument('src'); a.add_argument('out'); a.add_argument('--eyes', required=True); a.add_argument('--lid', default='#F0B99B'); a.add_argument('--frames', type=int, default=96)
o = a.parse_args(); base = Image.open(o.src).convert('RGB'); eyes = [tuple(map(float, e.split(','))) for e in o.eyes.split(';')]
lid = tuple(int(o.lid.lstrip('#')[i:i+2], 16) for i in (0, 2, 4)); tmp = tempfile.mkdtemp()
for i in range(o.frames):
    t = i / o.frames * 2 * math.pi; fr = base.copy(); d = ImageDraw.Draw(fr); blink = int(o.frames * .6) <= i <= int(o.frames * .6) + 3
    for (ex, ey, rx, ry) in eyes:
        px, py, r = ex + math.cos(t) * rx * .4, ey + math.sin(t) * ry * .4, rx * .46
        d.ellipse([px - r, py - r, px + r, py + r], fill=(29, 20, 17)); h = r * .3
        d.ellipse([px - r * .45, py - r * .6, px - r * .45 + h, py - r * .6 + h], fill=(255, 255, 255))
        if blink: d.ellipse([ex - rx * 1.04, ey - ry * 1.04, ex + rx * 1.04, ey + ry * 1.04], fill=lid)
    fr.save(f'{tmp}/{i:03d}.png')
subprocess.run(['ffmpeg', '-v', 'error', '-y', '-framerate', '24', '-i', f'{tmp}/%03d.png', '-vf', 'scale=trunc(iw/2)*2:trunc(ih/2)*2', '-c:v', 'libx264', '-crf', '26', '-pix_fmt', 'yuv420p', '-movflags', '+faststart', o.out], check=True)
print('saved', o.out)
