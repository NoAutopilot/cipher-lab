#!/usr/bin/env python3
"""R9-COST (6 Oct 2026): cut the crops (same boxes as N8-COS/N9-COS2 and R8-COST) in which either earlier pass read a `q`,
and list each crop's q count per earlier pass. Run in a folder holding dec/ (R1166 P1, P2, P4 PNGs); writes qcrops/ and qcrops.tsv.
usage: python3 r9cost_qcrops.py <align_dir>"""
import csv, os, sys
from PIL import Image
A = sys.argv[1]
IM = {'1': 'dec/IMG_R1166_I5853_P1.png', '2': 'dec/IMG_R1166_I5854_P2.png', '4': 'dec/IMG_R1166_I5856_P4.png'}
def tsv(p): return list(csv.DictReader(open(os.path.join(A, p)), delimiter='\t'))
def qn(s): return sum(1 for g in (s or '').split() for t in g.split('_') if t == 'q')
boxes = {r['unit']: (r['page'], *map(int, (r['x0'], r['y0'], r['x1'], r['y1']))) for r in tsv('n8cos_boxes.tsv')}
for r in tsv('n9cos2_boxes_fix.tsv'): boxes[r['unit']] = (r['page'], *map(int, (r['x0'], r['y0'], r['x1'], r['y1'])))
for r in tsv('r8cost_boxes.tsv'): boxes[r['crop']] = ('4', *map(int, (r['x0'], r['y0'], r['x1'], r['y1'])))
reads = {}
for tag, f in (('A', 'n9cos2_passA_W.tsv'), ('B', 'n9cos2_passB_W.tsv'), ('A', 'r8cost_reads/passA.tsv'), ('B', 'r8cost_reads/passB.tsv')):
    for r in tsv(f):
        c = r['crop'] if r['crop'].startswith('p') else 'p4_' + r['crop']
        reads.setdefault(c, {})[tag] = qn(r['signs'])
os.makedirs('qcrops', exist_ok=True); cache = {}
out = ['crop\tpage\tqA\tqB']
for c in sorted(reads, key=lambda c: (boxes[c][0], c)):
    qa, qb = reads[c].get('A', 0), reads[c].get('B', 0)
    if not (qa or qb): continue
    pg, x0, y0, x1, y1 = boxes[c]
    im = cache.setdefault(pg, Image.open(IM[pg]).convert('RGB'))
    cr = im.crop((x0, y0, x1, y1)); w, h = cr.size
    cr.resize((w * 2, h * 2)).save(f'qcrops/{c}.png')
    out.append(f'{c}\t{pg}\t{qa}\t{qb}')
open('qcrops.tsv', 'w').write('\n'.join(out) + '\n'); print(len(out) - 1, 'crops')
