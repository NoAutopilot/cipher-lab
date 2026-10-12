#!/usr/bin/env python3
"""BOXCLIP diagnostics, run AFTER the test was scored (benchmark-tx/boxclip/RESULTS.md, commit 3cf5ee86e). Script only.
Reads scores.tsv and the two signs.tsv files; computes nothing that feeds back into the method or the gate. It appends a
"Diagnostics (not the test)" section to RESULTS.md (replacing an earlier copy of that section).

Registered in PREREG-BOXCLIP.md (limitation iv): how many positives have an owner box that leaves the page image.
Post-hoc, to explain the FAIL and not to rescue it (no threshold is proposed from any of this):
  - how much of the owner's growth (owner box minus machine box) lies inside the page's OTHER machine boxes, the one place the
    registered grown box is forbidden to go (rule 7);
  - the continuous statistic's separation of positives from negatives per sorter (rank AUC of outside_frac; 0.5 = none);
  - how large the grown boxes are against the machine boxes they replace.
"""
import csv
import os
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
SORT = {'modena': (os.path.join(ROOT, 'ciphers/decode-1162-modena-ambung-1492/sorter/signs.tsv'), 2592, 3888),
        'matignon': (os.path.join(ROOT, 'ciphers/matignon-mayenne-1586/sorter/signs.tsv'), 3330, 93)}


def rd(p):
    return list(csv.DictReader(open(p, newline=''), delimiter='\t'))


def auc(pos, neg):
    """rank AUC: P(pos > neg) + 0.5 P(tie)"""
    if not pos or not neg:
        return float('nan')
    s = 0.0
    for a in pos:
        for b in neg:
            s += 1.0 if a > b else 0.5 if a == b else 0.0
    return s / (len(pos) * len(neg))


def main():
    sc = rd(os.path.join(HERE, 'scores.tsv'))
    L = ['', '## Diagnostics (not the test)', '',
         'Written after the verdict above was committed (`diagnostics.py`). It explains the FAIL; it changes no threshold and proposes none.', '']
    # 1. owner boxes leaving the image (registered), 2. owner growth inside other machine boxes (post-hoc)
    L += ['| sorter | positives | owner box leaves the page image (registered diagnostic) | owner growth that lies inside another machine box: median share of (owner box minus machine box) | positives whose growth is more than half inside other machine boxes |',
          '|---|---|---|---|---|']
    for name, (sp, W, H) in SORT.items():
        allb = rd(sp)
        pos = [r for r in sc if r['sorter'] == name and r['label'] == '1']
        out = 0; shares = []
        for r in pos:
            ox, oy, ow, oh = (int(r[k]) for k in ('ox', 'oy', 'ow', 'oh'))
            mx, my, mw, mh = (int(r[k]) for k in ('mx', 'my', 'mw', 'mh'))
            if ox < 0 or oy < 0 or ox + ow > W or oy + oh > H:
                out += 1
            # raster over the owner box
            g = np.zeros((oh, ow), bool)                      # growth = owner minus machine
            g[:, :] = True
            x0, y0, x1, y1 = max(mx, ox), max(my, oy), min(mx + mw, ox + ow), min(my + mh, oy + oh)
            if x1 > x0 and y1 > y0:
                g[y0 - oy:y1 - oy, x0 - ox:x1 - ox] = False
            if not g.any():
                continue
            nb = np.zeros_like(g)
            for b in allb:
                if b['sid'] == r['sid'] or b['page'] != r['page']:
                    continue
                bx, by, bw, bh = (int(float(b[k])) for k in 'xywh')
                a0, b0, a1, b1 = max(bx, ox), max(by, oy), min(bx + bw, ox + ow), min(by + bh, oy + oh)
                if a1 > a0 and b1 > b0:
                    nb[b0 - oy:b1 - oy, a0 - ox:a1 - ox] = True
            shares.append(float((g & nb).sum() / g.sum()))
        L.append('| %s | %d | %d | %.2f (n=%d with growth) | %d |' % (name, len(pos), out, float(np.median(shares)) if shares else float('nan'),
                                                                    len(shares), sum(s > .5 for s in shares)))
    L += ['']
    # 3. AUC of outside_frac
    L += ['| sorter | positives: median outside_frac | negatives: median outside_frac | rank AUC (0.5 = no separation) | boxes with outside_frac > 0 |', '|---|---|---|---|---|']
    for name in list(SORT) + ['pooled']:
        rr = [r for r in sc if name == 'pooled' or r['sorter'] == name]
        p = [float(r['outside_frac']) for r in rr if r['label'] == '1']; n = [float(r['outside_frac']) for r in rr if r['label'] == '0']
        L.append('| %s | %.3f | %.3f | %.3f | %d of %d |' % (name, np.median(p), np.median(n), auc(p, n), sum(float(r['outside_frac']) > 0 for r in rr), len(rr)))
    L += ['']
    # 4. size of grown boxes
    L += ['| sorter | flagged boxes | median grown area / machine area | median grown width / machine width | median grown height / machine height |', '|---|---|---|---|---|']
    for name in SORT:
        fl = [r for r in sc if r['sorter'] == name and r['flagged'] == '1']
        if not fl:
            L.append('| %s | 0 | - | - | - |' % name); continue
        a = [int(r['gw']) * int(r['gh']) / (int(r['mw']) * int(r['mh'])) for r in fl]
        w = [int(r['gw']) / int(r['mw']) for r in fl]; h = [int(r['gh']) / int(r['mh']) for r in fl]
        L.append('| %s | %d | %.2f | %.2f | %.2f |' % (name, len(fl), np.median(a), np.median(w), np.median(h)))
    # 5. exploratory: the same check with every box alone on its page (neighbour rule off), to see where the signal is lost
    sys.path.insert(0, HERE)
    import run_boxclip as R
    sys.path.insert(0, os.path.join(ROOT, 'tools'))
    import box_clip_check as BC
    S = R.load()
    L += ['', 'Exploratory, not registered: the same frozen check with each labelled box alone on its page (the neighbour rule off, so a neighbour\'s joined ink counts as outside).', '',
          '| sorter | flagged positives | flagged negatives | recall | false-alarm | balanced acc | rank AUC of outside_frac | median outside_frac, positives / negatives |', '|---|---|---|---|---|---|---|---|']
    for name, T in S.items():
        by = {r['sid']: r for r in T['rows']}; rows = []
        for l in T['labels']:
            r = by[l['sid']]
            g = BC.check_boxes(T['images'][r['page']], [(r['sid'], *[float(r[c]) for c in 'xywh'])], T['scale'])[0]
            rows.append((l['label'], g['flagged'], g['outside_frac']))
        P = [x for x in rows if x[0]]; N = [x for x in rows if not x[0]]
        tp = sum(x[1] for x in P); fp = sum(x[1] for x in N)
        rec, fa = tp / len(P), fp / len(N)
        L.append('| %s | %d of %d | %d of %d | %.3f | %.3f | %.3f | %.3f | %.3f / %.3f |' % (
            name, tp, len(P), fp, len(N), rec, fa, (rec + 1 - fa) / 2, auc([x[2] for x in P], [x[2] for x in N]),
            np.median([x[2] for x in P]), np.median([x[2] for x in N])))
    p = os.path.join(HERE, 'RESULTS.md')
    cur = open(p).read().split('\n## Diagnostics (not the test)')[0].rstrip('\n') + '\n'
    open(p, 'w').write(cur + '\n'.join(L) + '\n')
    print('\n'.join(L))
    return 0


if __name__ == '__main__':
    sys.exit(main())
