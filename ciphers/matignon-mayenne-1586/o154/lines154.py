#!/usr/bin/env python3
"""MAT-154 (15 Oct 2026): f.154r line strips from the scratch native region (regen_o154.sh), deskewed by the common slope the
iiif_lines.py --follow-slope fits agreed on (-0.0163, i.e. lines rise ~58 px over 3579 px), then line centres from the row ink
profile of the levelled region (28 lines expected, Bourdeau f154-1..28). Writes OUT/rot.jpg, OUT/lines/L01.jpg.. and OUT/lines.tsv.
Images go to OUT only (scratchpad; never committed). Usage: python3 lines154.py REGION.jpg OUT
"""
import math, os, sys
import numpy as np
from PIL import Image
src, out = sys.argv[1:3]; os.makedirs(os.path.join(out, 'lines'), exist_ok=True)
im = Image.open(src).convert('L').crop((0, 0, 3579, 3250))
deg = math.degrees(math.atan(0.0163))
rot = im.rotate(-deg, resample=Image.BICUBIC, fillcolor=235)   # PIL rotates counter-clockwise; lines rise to the right
rot.save(os.path.join(out, 'rot.jpg'), quality=90)
g = np.asarray(rot, dtype=float)[:, 300:3400]
prof = (g < 120).sum(1).astype(float)
prof = np.convolve(prof, np.ones(15) / 15, 'same')
pk = []
for y in range(40, len(prof) - 40):
    if prof[y] == prof[y - 40:y + 41].max() and prof[y] > 0.25 * prof.max():
        if not pk or y - pk[-1] > 60: pk.append(y)
print(len(pk), 'centres', pk)
half = 62
with open(os.path.join(out, 'lines.tsv'), 'w') as f:
    f.write('line\tcentre_rot_y\ty0\ty1\n')
    for k, c in enumerate(pk, 1):
        y0, y1 = max(0, c - half), min(rot.height, c + half)
        rot.crop((0, y0, rot.width, y1)).save(os.path.join(out, 'lines', f'L{k:02d}.jpg'), quality=92)
        f.write(f'{k}\t{c}\t{y0}\t{y1}\n')
