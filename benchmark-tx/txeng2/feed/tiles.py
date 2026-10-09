#!/usr/bin/env python3
"""TXE2-FEED sorter inputs: one row per focus tile -> <unit>_tiles.tsv (tile, page, x, y, w, h, crops). eval_heldout tiles
are atlas boxes (ciphers/nevers-birago-fr3251-1572/atlas/signs.tsv, the box the sign sorter cuts); f152r and spinelli have
no per-sign box mapped to their line read, so the row names the line's segment crops (every segment: the sorter build
must cut the sign from them -- a segmentation step, not done here). Read-free: no truth, no value."""
import csv, glob, os
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
OUT = os.path.join(ROOT, 'benchmark-tx/txeng2/feed')
rd = lambda p: list(csv.DictReader(open(p), delimiter='\t'))
boxes = {r['sid']: r for r in rd(os.path.join(ROOT, 'ciphers/nevers-birago-fr3251-1572/atlas/signs.tsv'))}
CROPS = {'f152r': 'benchmark-tx/txeng2/f152r/crops/{short}_s*.jpg', 'spinelli': 'benchmark-tx/txeng/confirm/crops/{line}_s*.jpg'}
for unit in ('eval_heldout', 'f152r', 'spinelli'):
    feed = {r['tile']: r for r in csv.DictReader((l for l in open(os.path.join(OUT, unit + '_feed.tsv'))
                                                  if not l.startswith('#')), delimiter='\t')}
    with open(os.path.join(OUT, unit + '_tiles.tsv'), 'w') as f:
        f.write('tile\tline\tpos\tpage\tx\ty\tw\th\tcrops\n')
        for t, _q in (l.rstrip('\n').split('\t') for l in open(os.path.join(OUT, unit + '_focus.tsv'))):
            r = feed[t]; b = boxes.get(t)
            if b:
                f.write('\t'.join([t, r['line'], r['pos'], b['page'], b['x'], b['y'], b['w'], b['h'], '']) + '\n')
            else:
                pat = CROPS[unit].format(line=r['line'], short=r['line'])
                cs = sorted(os.path.relpath(p, ROOT) for p in glob.glob(os.path.join(ROOT, pat)))
                f.write('\t'.join([t, r['line'], r['pos'], '', '', '', '', '', '|'.join(cs)]) + '\n')
    print(unit, sum(1 for _ in open(os.path.join(OUT, unit + '_tiles.tsv'))) - 1, 'tiles')
