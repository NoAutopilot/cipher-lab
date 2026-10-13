#!/usr/bin/env python3
"""VIV-WALK contact sheets from images/walk/*.jpg (untracked), canvas id burned in; sheets go to images/walk/sheets/ (untracked).
  python3 walk/sheets.py VOL FROM TO [--per 20] [--cols 4] [--tile 390] [--top FRAC]   (--top: only the top FRAC of each opening, enlarged)"""
import sys, os, glob, argparse
from PIL import Image, ImageDraw, ImageFont
ap = argparse.ArgumentParser(); ap.add_argument('vol'); ap.add_argument('a', type=int); ap.add_argument('b', type=int)
ap.add_argument('--per', type=int, default=20); ap.add_argument('--cols', type=int, default=4); ap.add_argument('--tile', type=int, default=390)
ap.add_argument('--top', type=float, default=0); ap.add_argument('--list'); a = ap.parse_args()
here = os.path.dirname(os.path.abspath(__file__)); src = os.path.join(os.path.dirname(here), 'images', 'walk'); od = os.path.join(src, 'sheets'); os.makedirs(od, exist_ok=True)
fs = sorted(glob.glob(f'{src}/fr{a.vol}_c*.jpg'))
fs = [f for f in fs if a.a <= int(f[-7:-4]) <= a.b]
if a.list: keep = {int(x) for x in a.list.split(',')}; fs = [f for f in fs if int(f[-7:-4]) in keep]
font = ImageFont.load_default(size=22) if hasattr(ImageFont, 'load_default') else None
for k in range(0, len(fs), a.per):
    grp = fs[k:k + a.per]; ims = []
    for f in grp:
        im = Image.open(f).convert('L')
        if a.top: im = im.crop((0, 0, im.width, int(im.height * a.top)))
        im = im.resize((a.tile, int(im.height * a.tile / im.width))); ims.append((int(f[-7:-4]), im))
    th = max(i.height for _, i in ims); rows = (len(ims) + a.cols - 1) // a.cols
    sh = Image.new('L', (a.cols * (a.tile + 6), rows * (th + 6)), 255); d = ImageDraw.Draw(sh)
    for j, (c, im) in enumerate(ims):
        x, y = (j % a.cols) * (a.tile + 6), (j // a.cols) * (th + 6); sh.paste(im, (x, y))
        d.rectangle((x, y, x + 70, y + 26), fill=0); d.text((x + 4, y + 1), f'c{c}', fill=255, font=font)
    name = f'{od}/fr{a.vol}_{ims[0][0]:03d}-{ims[-1][0]:03d}{"_top" if a.top else ""}.jpg'; sh.save(name, quality=85); print(name, sh.size)
