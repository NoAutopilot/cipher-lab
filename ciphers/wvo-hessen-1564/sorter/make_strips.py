#!/usr/bin/env python3
"""R9-WVOSORT: cut the ten f.23 cipher-row strips (pages/f23_C01..C10.png) from images/01109_p3_400full.jpg, full text
width (page x 550..3300), each = the row's band from `tools/iiif_lines.py --centres` (sorter/strips/manifest.json,
even bands) +- PAD px, since the rows slope and the band alone clips the low end of a row."""
import json
from PIL import Image
PAD = 48
PAD_BOT = {}  # all strips use BOT below (owner 6 Oct 2026: descenders cut off at 48 px)
BOT = 130   # bottom pad for every strip (C09's row also slopes about 40 px across the leaf)
m = json.load(open('strips/manifest.json'))['iiif_lines']
im = Image.open('../images/01109_p3_400full.jpg').convert('L')
rows = []
for c in m:
    if c['segment'] != 1 or c['band'] % 2: continue
    y0, y1 = c['box'][1], c['box'][3]; n = 'f23_C%02d' % (c['band'] // 2)
    im.crop((550, y0 - PAD, 3300, y1 + PAD_BOT.get(n, BOT))).save(f'pages/{n}.png'); rows.append((n, y0, y1, PAD_BOT.get(n, BOT)))
open('bands.tsv', 'w').write('page\tband_y0\tband_y1\tstrip_y0\tstrip_y1\tx0\tx1\n' +
                             ''.join(f'{n}\t{a}\t{b}\t{a-PAD}\t{b+pb}\t550\t3300\n' for n, a, b, pb in rows))
print(len(rows), 'strips, pad', PAD)
