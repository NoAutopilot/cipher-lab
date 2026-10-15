#!/usr/bin/env python3
"""MANT-YSHAPE (15 Oct 2026) step 1, outcome-blind: locate the 4|9 digit glyph of every y49/known.tsv slot inside its
committed strip with tools/glyph_atlas.py's own segmenter. Signs are cut by segment_page, those shorter than half the
strip's median sign height are dropped as separator dots, and the rest are sorted by x; a slot is located only when the
count equals the digits of the strip's settled tokens (then the slot is the sign at its digit index), else 'unlocated'.
No 4/9 score is computed here. Writes yshape/located.tsv. --check: exit 1 if stale."""
import argparse, io, os, sys
import numpy as np
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.dirname(HERE)
sys.path.insert(0, os.path.join(ROOT, 'y49')); sys.path.insert(0, os.path.join(ROOT, '..', '..', 'tools'))
import census49 as C
import glyph_atlas as G
SEG = argparse.Namespace(rel=0.78, mark_h=0.55, mark_above=0.3, min_area=0.12, merge_vgap=0.6, debug=False,
                         shared_mh=None, out=None)
DIRS = {'0494': 'f0494_08', '0474': 'f0474_08', '0089': 'f0089_08', '0136': 'f0136_08', '0309': 'f0309_08',
        '0312': 'f0312_08', '0314': 'f0314_08', '0317': 'f0317_08', '0490': 'f0490_08', '0490L': 'f0490_08'}
def crop_path(leaf, crop):
    return os.path.join(ROOT, DIRS[leaf], 'crops', crop + '.jpg')
def main():
    toks = {lf: t for lf, _, _, t in C.LEAVES}
    known = C.rows('y49/known.tsv')
    cache, rows, bms = {}, [], []
    for k in known:
        lf, tid, crop = k['leaf'], k['tokid'], k['crop']
        seq = [t for t in toks[lf] if t['crop'] == crop]
        idx = next(i for i, t in enumerate(seq) if t['tokid'] == tid)
        digits = ''.join(t['settled'] for t in seq)
        before = sum(len(t['settled']) for t in seq[:idx])
        tok = seq[idx]['settled']
        di = before + next(i for i, c in enumerate(tok) if c in '49')
        p = crop_path(lf, crop)
        if p not in cache:
            S, _, _, mh = G.segment_page(crop, p, None, SEG)
            S = sorted([s for s in S if s['h'] >= 0.5 * mh], key=lambda s: s['x'])
            cache[p] = S
        S = cache[p]
        ok = len(S) == len(digits) and digits.isdigit()
        kind = 'conflict' if (k['known'] == '9' and '4' in tok) else ('clean' if k['known'] in tok else 'other')
        rows.append([lf, tid, crop, tok, k['known'], kind, len(digits), len(S), 'located' if ok else 'unlocated',
                     *( [S[di]['x'], S[di]['y'], S[di]['w'], S[di]['h'], '%.3f' % S[di]['rh'], '%.3f' % S[di]['rw']]
                        if ok else ['', '', '', '', '', ''])])
        bms.append(S[di]['bm'] if ok else np.zeros((G.BM, G.BM), np.uint8))
    H = ['leaf', 'tokid', 'crop', 'settled', 'known', 'kind', 'n_digits', 'n_signs', 'status', 'x', 'y', 'w', 'h', 'rh', 'rw']
    txt = '\t'.join(H) + '\n' + ''.join('\t'.join(map(str, r)) + '\n' for r in rows)
    p = os.path.join(HERE, 'located.tsv')
    if '--check' in sys.argv:
        stale = not os.path.exists(p) or open(p).read() != txt
        print('STALE located.tsv' if stale else 'up to date'); sys.exit(1 if stale else 0)
    open(p, 'w').write(txt)
    from collections import Counter
    print(Counter((r[5], r[8]) for r in rows))
if __name__ == '__main__':
    main()
