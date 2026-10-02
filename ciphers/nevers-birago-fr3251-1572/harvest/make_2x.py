#!/usr/bin/env python3
"""2x reader crops of the f.178v cipher lines (LIKELY-3, 2 Oct 2026): tools/iiif_lines.py cut the native region
harvest/f178v/src_*.jpg into 23 bands x 3 segments (1250 px, 50 px overlap); 1x crops were too small for readers on the
sibling folder (ceppo-nevers HARVEST-D), so this upscales each segment 2x (LANCZOS) into harvest/f178v/lines2x/, which
is regenerable and gitignored.  python3 make_2x.py [--lines 1-10]"""
import argparse, glob, os, re
from PIL import Image
HERE = os.path.dirname(os.path.abspath(__file__))
ap = argparse.ArgumentParser(); ap.add_argument('--lines', default='1-23'); a = ap.parse_args()
lo, hi = map(int, a.lines.split('-'))
out = os.path.join(HERE, 'f178v', 'lines2x'); os.makedirs(out, exist_ok=True)
n = 0
for f in sorted(glob.glob(os.path.join(HERE, 'f178v', 'f178v_L*_s*.jpg'))):
    ln = int(re.search(r'_L(\d+)_', f).group(1))
    if lo <= ln <= hi:
        im = Image.open(f); im = im.resize((im.width * 2, im.height * 2), Image.LANCZOS)
        im.save(os.path.join(out, os.path.basename(f).replace('.jpg', '_2x.png'))); n += 1
print(f'{n} crops -> {out}')
