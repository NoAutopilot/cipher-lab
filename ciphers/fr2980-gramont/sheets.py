#!/usr/bin/env python3
"""Pass sheets: three manuscript lines per sheet, each line as two non-overlapping rows (a = left part, b = right
part), split at an ink-free column near the middle. Reads the full-resolution regions and crops/crops.json.
Usage: sheets.py SRC_DIR OUT_DIR"""
import sys, json, numpy as np
from PIL import Image, ImageDraw
SRC, OUT = sys.argv[1], sys.argv[2]
C = json.load(open('crops/crops.json'))
FILES = {'f29r': 'f29r_full.jpg', 'f30r': 'f30r_full.jpg', 'f30v': 'f30v_full.jpg'}
arr = {k: np.array(Image.open(f'{SRC}/{v}').convert('L')) for k, v in FILES.items()}
rows, splits = [], {}
for lid, r in C.items():
    a = arr[lid[:4]]; (l, ta, _, ba), (_, tb, rr, bb) = r['a'], r['b']
    mid = (r['a'][2] + r['b'][0]) // 2
    band = a[(ta + ba) // 2 - 30:(tb + bb) // 2 + 30, mid - 200:mid + 200] < 120
    col = np.convolve(band.sum(0), np.ones(9) / 9, 'same'); cut = mid - 200 + int(np.argmin(col[20:-20])) + 20
    splits[lid] = cut
    rows.append((lid + 'a', Image.fromarray(a[ta:ba, l:cut + 8])))
    rows.append((lid + 'b', Image.fromarray(a[tb:bb, cut - 8:rr])))
json.dump(splits, open('crops/splits.json', 'w'))
per = 6; n = 0
for i in range(0, len(rows), per):
    grp = rows[i:i + per]; W = max(im.width for _, im in grp) + 260
    sh = Image.new('L', (W, sum(im.height + 16 for _, im in grp)), 255); d = ImageDraw.Draw(sh); y = 0
    for lab, im in grp:
        d.rectangle([0, y, 250, y + im.height], fill=0); d.text((12, y + im.height // 2 - 20), lab, fill=255, font_size=44)
        sh.paste(im, (260, y)); y += im.height + 16
    n += 1; sh.save(f'{OUT}/sheet{n:02d}.jpg', quality=85)
print(n, 'sheets')
