#!/usr/bin/env python3
"""OL1-PAGE, the next rule (PREREG-txeng2-21, TXE2-OL1PAGE, 10 Oct 2026): split the re-cut sorter inputs (recut_ol1_boxes.py's
sorter/{signs,labels,marks,focus}.tsv, pages.json) into one input set per hand, sorter/<short>/, so each page's preflight median is the
hand's own. Nothing is re-cut. On the luzerne inputs only, EVERY box (sign box and mark box alike) is padded uniformly by 4 px a side,
clamped to its crop, before the tile is cut and measured: a declared presentation parameter for an 11-px hand, never a selected subset.
Read-free: boxes and crop sizes only.
  python3 benchmark-tx/txeng2/oracle1/split_per_hand.py"""
import csv, json, os
from PIL import Image
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../..'))
O = os.path.join(ROOT, 'benchmark-tx/txeng2/oracle1'); S = os.path.join(O, 'sorter')
SHORT = {'vivonne1573-f102r': 'vivonne', 'birago1572-no87': 'birago', 'luzerne108a-p1': 'luzerne'}
PAD = {'luzerne': 4}
rd = lambda p: list(csv.DictReader(open(p), delimiter='\t'))
hand = {r['box_id']: SHORT[r['hand']] for r in rd(os.path.join(O, 'boxes/boxes_recut_all.tsv'))}
pages = json.load(open(os.path.join(S, 'pages.json')))
size = {}
def W(p, rows, cols):
    with open(p, 'w') as f:
        f.write('\t'.join(cols) + '\n'); f.writelines('\t'.join(str(r[c]) for c in cols) + '\n' for r in rows)
for h in SHORT.values():
    d = os.path.join(S, h); os.makedirs(d, exist_ok=True)
    signs = [r for r in rd(os.path.join(S, 'signs.tsv')) if hand[r['sid']] == h]
    pad = PAD.get(h, 0)
    for r in signs:
        if pad:
            if r['page'] not in size:
                size[r['page']] = Image.open(os.path.join(ROOT, pages[r['page']]['image'])).size
            iw, ih = size[r['page']]
            x, y, w, hh = (int(r[k]) for k in ('x', 'y', 'w', 'h'))
            x0, y0, x1, y1 = max(0, x - pad), max(0, y - pad), min(iw, x + w + pad), min(ih, y + hh + pad)
            r.update(x=x0, y=y0, w=x1 - x0, h=y1 - y0)
    keep = {r['sid'] for r in signs}
    W(os.path.join(d, 'signs.tsv'), signs, ['sid', 'page', 'x', 'y', 'w', 'h'])
    W(os.path.join(d, 'labels.tsv'), [r for r in rd(os.path.join(S, 'labels.tsv')) if r['sid'] in keep], ['sid', 'sign', 'family'])
    W(os.path.join(d, 'marks.tsv'), [r for r in rd(os.path.join(S, 'marks.tsv')) if r['sid'] in keep], ['x', 'y', 'w', 'h', 'sid', 'kind', 'mark_id'])
    W(os.path.join(d, 'focus.tsv'), [r for r in rd(os.path.join(S, 'focus.tsv')) if r['sid'] in keep], ['sid', 'question'])
    pg = {r['page'] for r in signs}
    json.dump({k: v for k, v in pages.items() if k in pg}, open(os.path.join(d, 'pages.json'), 'w'), indent=1, sort_keys=True)
    with open(os.path.join(d, 'cipher_lines.tsv'), 'w') as f:
        f.write(f'# every crop of the {h} OL1 manifest lines is a cipher line (manifest.tsv); no x-range given\n')
        f.writelines(n + '\n' for n in sorted(pg))
    print(h, len(signs), 'tiles', len(pg), 'crops', 'pad', pad)
