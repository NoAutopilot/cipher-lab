#!/usr/bin/env python3
"""TXE2-BOXES (P1, 9 Oct 2026): join the s1/s2 segment boxes of each Spinelli line into one left-to-right box list.
Input: a `tools/glyph_atlas.py segment` run (default mode, the no.87 atlas recipe, --median-h 55) whose --page names are
the confirm line crops (benchmark-tx/txeng/confirm/crops/<line>_s1|s2.jpg). A box is kept from s1 when its centre lies
left of the overlap midpoint and from s2 when right of it (overlap from crops/manifest.json), so a sign in the overlap
is counted once. Writes line, k, crop, x, y, w, h (crop pixels) and prints box count vs passZ position count per line.
Value-blind: only the position COUNT of the line read is used.
  python3 benchmark-tx/txeng2/boxes/spin_join.py SEGDIR [--out benchmark-tx/txeng2/boxes/spinelli_lineboxes.tsv]"""
import argparse, csv, json, os
import numpy as np
from PIL import Image
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../..'))
ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
ap.add_argument('segdir'); ap.add_argument('--min-frac', type=float, default=0.45, help='drop a box whose longer side is under this x the median sign height (fragments, specks)'); ap.add_argument('--ghost', type=float, default=0.45, help='drop a box whose darkest 10%% of pixels are lighter than this x the crop median grey (verso bleed-through)'); ap.add_argument('--out', default='benchmark-tx/txeng2/boxes/spinelli_lineboxes.tsv')
a = ap.parse_args()
man = {c['crop'][:-4]: c for c in json.load(open(os.path.join(ROOT, 'benchmark-tx/txeng/confirm/crops/manifest.json')))['iiif_lines']}
signs = list(csv.DictReader(open(os.path.join(a.segdir, 'signs.tsv')), delimiter='\t'))
npos = {}
for r in csv.DictReader(open(os.path.join(ROOT, 'benchmark-tx/outputs/spinelli-c1519-confirm/passZ_pipeline.tsv')), delimiter='\t'):
    npos[r['line']] = npos.get(r['line'], 0) + 1
out = open(os.path.join(ROOT, a.out), 'w'); out.write('line\tk\tcrop\tx\ty\tw\th\tmarks\n')
for ln in sorted(npos):
    s1, s2 = man[ln + '_s1'], man[ln + '_s2']
    mid = (s2['box'][0] + s1['box'][2]) / 2.0
    kept = []
    grey = {}
    for r in signs:
        seg = r['page']
        if not seg.startswith(ln + '_s'): continue
        x, w, y, h = int(r['x']), int(r['w']), int(r['y']), int(r['h'])
        if max(w, h) < a.min_frac * 55: continue
        if seg not in grey: grey[seg] = np.asarray(Image.open(os.path.join(ROOT, 'benchmark-tx/txeng/confirm/crops', seg + '.jpg')).convert('L'), dtype=float)
        G = grey[seg]; patch = G[y:y + h, x:x + w]
        if patch.size == 0 or np.quantile(patch, 0.1) > a.ghost * np.median(G): continue
        gx = man[seg]['box'][0] + x + w / 2.0
        if (seg.endswith('_s1') and gx < mid) or (seg.endswith('_s2') and gx >= mid):
            kept.append((gx, seg, r))
    kept.sort(key=lambda t: t[0])
    for k, (gx, seg, r) in enumerate(kept, 1):
        out.write('\t'.join([ln, str(k), f'benchmark-tx/txeng/confirm/crops/{seg}.jpg', r['x'], r['y'], r['w'], r['h'], r.get('marks', '')]) + '\n')
    print(ln, 'boxes', len(kept), 'positions', npos[ln], 'OK' if len(kept) == npos[ln] else 'DIFF')
