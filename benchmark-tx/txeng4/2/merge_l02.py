#!/usr/bin/env python3
"""TXE4-2: merge TILE_DIR/atlas_l02 (f130_L02_s1 segmented at its own median) into TILE_DIR/atlas (the pooled run, where that
crop came out empty): signs/marks rows, bitmaps, pages.json, the crop copy.    python3 merge_l02.py TILE_DIR"""
import csv, json, os, shutil, sys, numpy as np
A = os.path.join(sys.argv[1], 'atlas'); B = os.path.join(sys.argv[1], 'atlas_l02')
order = None
for fn in ('signs.tsv', 'marks.tsv'):
    a = open(os.path.join(A, fn)).read().rstrip('\n').split('\n'); b = open(os.path.join(B, fn)).read().rstrip('\n').split('\n')
    assert a[0] == b[0]; rows = a[1:] + b[1:]; rows = [r for r in rows if r]
    hdr = a[0].split('\t')
    if fn == 'signs.tsv':
        key = lambda r: (dict(zip(hdr, r.split('\t')))['page'], int(dict(zip(hdr, r.split('\t')))['line']), int(dict(zip(hdr, r.split('\t')))['pos']))
        rs = sorted(rows, key=key); order = [rows.index(r) for r in rs]
    else:
        rs = rows
    open(os.path.join(A, fn), 'w').write('\n'.join([a[0]] + rs) + '\n')
za = np.load(os.path.join(A, 'bitmaps.npz')); zb = np.load(os.path.join(B, 'bitmaps.npz'))
np.savez_compressed(os.path.join(A, 'bitmaps.npz'), signs=np.concatenate([za['signs'], zb['signs']])[order],
                    marks=np.concatenate([za['marks'], zb['marks']]))
pj = json.load(open(os.path.join(A, 'pages.json'))); pj.update(json.load(open(os.path.join(B, 'pages.json'))))
json.dump(pj, open(os.path.join(A, 'pages.json'), 'w'), indent=1)
shutil.copy(os.path.join(B, 'crops', 'f130_L02_s1.png'), os.path.join(A, 'crops', 'f130_L02_s1.png'))
print('merged L02 s1:', len(order), 'signs')
