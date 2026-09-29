#!/usr/bin/env python3
"""Group E: per-line pixel boxes (image coordinates) from glyphs/signs.tsv + glyphs/pages.json,
and every pictogram-class box with its image coordinates. Writes line_boxes.tsv, pict_boxes.tsv.
Pictogram class = PICT-* plus SUN, STAR, HEART, RAM (h3_unit_profile.py's shape class, as H31)."""
import csv, json, os, collections
D = os.path.dirname(os.path.abspath(__file__)); T = os.path.join(D, '..', '..')
pages = json.load(open(os.path.join(T, 'glyphs/pages.json')))
lab = {r['sid']: r for r in csv.DictReader(open(os.path.join(T, 'glyphs/box_labels.tsv')), delimiter='\t')}
lines = collections.defaultdict(list)
for r in csv.DictReader(open(os.path.join(T, 'glyphs/signs.tsv')), delimiter='\t'):
    ox, oy = pages[r['page']]['box'][:2]
    x, y, w, h = (int(float(r[k])) for k in 'xywh')
    lines[(r['page'], int(r['line']))].append((int(r['pos']), x+ox, y+oy, w, h, r['sid']))
PICT = lambda s: s.startswith('PICT-') or s in ('SUN', 'STAR', 'HEART', 'RAM')
with open(os.path.join(D, 'line_boxes.tsv'), 'w') as f, open(os.path.join(D, 'pict_boxes.tsv'), 'w') as g:
    f.write('line\timage\tx0\ty0\tx1\ty1\tboxes\n'); g.write('line\tpos\tof\tsign\timage\tx0\ty0\tx1\ty1\n')
    for (p, l), bs in sorted(lines.items()):
        img = os.path.basename(pages[p]['image']); bs.sort()
        x0 = min(b[1] for b in bs); y0 = min(b[2] for b in bs)
        x1 = max(b[1]+b[3] for b in bs); y1 = max(b[2]+b[4] for b in bs)
        f.write(f'{p}_L{l:02d}\t{img}\t{x0}\t{y0}\t{x1}\t{y1}\t{len(bs)}\n')
        for b in bs:
            s = lab.get(b[5], {}).get('sign', '')
            if PICT(s): g.write(f'{p}_L{l:02d}\t{b[0]}\t{len(bs)}\t{s}\t{img}\t{b[1]}\t{b[2]}\t{b[1]+b[3]}\t{b[2]+b[4]}\n')
