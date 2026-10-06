#!/usr/bin/env python3
"""R9-WVOSORT: whiten everything outside each f.23 cipher row's zone before glyph_atlas segments it (seg_in/*.png), so
the clear rows written between the cipher rows do not merge into the cipher signs. The rows slope, so the zone
follows a baseline fitted (least squares) to the bottoms of the unmasked segmentation's boxes (seg_raw/, glyph_atlas
segment --merge-vgap 0.15 on pages/) whose centre lies within -40 .. +60 px of the eye centre (iiif_lines --centres)
and whose height is at least 0.6 x the row median; zone = baseline -95 .. +18 px at every column."""
import csv, numpy as np
from PIL import Image
eye = [170, 315, 470, 645, 810, 1005, 1180, 1365, 1550, 1710]   # region y (iiif_lines --centres); page y = +130
raw = list(csv.DictReader(open('seg_raw/signs.tsv'), delimiter='\t'))
rows = list(csv.DictReader(open('bands.tsv'), delimiter='\t'))
out = []
for r, e in zip(rows, eye):
    a = np.asarray(Image.open(f"pages/{r['page']}.png").convert('L')).astype(float)
    H, W = a.shape
    c0 = 48 + (e + 130 - int(r['band_y0']))
    bx = [s for s in raw if s['page'] == r['page']]
    bx = [(int(s['x']) + int(s['w']) / 2, int(s['y']) + int(s['h']), int(s['h'])) for s in bx
          if c0 - 40 <= int(s['y']) + int(s['h']) / 2 <= c0 + 60]
    mh = np.median([h for _, _, h in bx])
    pts = [(x, y) for x, y, h in bx if h >= 0.6 * mh]
    k, b = np.polyfit([p[0] for p in pts], [p[1] for p in pts], 1)
    m = a.copy()
    for x in range(W):
        bl = k * x + b
        m[:max(0, int(bl - 95)), x] = 255; m[min(H, int(bl + 18)):, x] = 255
    Image.fromarray(m.astype(np.uint8)).save(f"seg_in/{r['page']}.png")
    out.append((r['page'], c0, round(k, 4), round(b, 1)))
open('zones.tsv', 'w').write('page\teye_centre\tslope\tbaseline_at_x0\n' + ''.join('\t'.join(map(str, o)) + '\n' for o in out))
for o in out: print(*o)
