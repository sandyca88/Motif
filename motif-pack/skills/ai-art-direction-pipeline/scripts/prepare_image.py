"""Center-crop to a ratio, resize and save as WebP.  usage: prepare_image.py in.jpg out.webp [--ratio 16:10] [--width 1600]"""
import sys, argparse
from PIL import Image
a = argparse.ArgumentParser(); a.add_argument('src'); a.add_argument('dst'); a.add_argument('--ratio', default='16:10'); a.add_argument('--width', type=int, default=1600); a.add_argument('--quality', type=int, default=82)
o = a.parse_args(); rw, rh = map(float, o.ratio.split(':'))
im = Image.open(o.src).convert('RGB'); w, h = im.size; tw, th = w, int(w * rh / rw)
if th > h: th = h; tw = int(h * rw / rh)
l, t = (w - tw) // 2, (h - th) // 2
im.crop((l, t, l + tw, t + th)).resize((o.width, int(o.width * rh / rw)), Image.LANCZOS).save(o.dst, 'WEBP', quality=o.quality, method=6)
print('saved', o.dst)
