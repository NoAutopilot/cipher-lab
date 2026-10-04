#!/usr/bin/env python3
"""LL-RECUT (4 Oct 2026): re-cut the f.101v sorter so that ONE TILE = ONE SIGN, on straight (deskewed) line strips.

Owner, on the v2 page (as on Pisany f.75): many tiles straddled two signs or cut one in half, because build_inputs.py fitted
ink-profile blobs to the readers' column COUNT; and the lines slope up to ~100 px across the region. This script replaces
build_inputs.py in build.sh, with the method of the Pisany re-cut, now shared as tools/sorter_recut.py (docstring there):
deskew along build_inputs.traces() (re-centred per window on the strip's own ink), tiles from each sign's own ink
(connected components owned by the line, x-overlapping strokes joined, wide groups split at ink minima), starting piles
value-blind: tiles aligned in x order to the reader columns of tx/ciphertext_draft.tsv (positioned at the v2 tile centres,
lines 1-29) take that column's pile (same names as v2); every other tile -- and all of lines 30-33, which no reader row
belongs to alone -- starts in the pile its shape cluster mostly holds, and the most frequent of those are the focus box.

  python3 ciphers/fr16106-vivonne-longlee-1579/sorter/recut.py [--debug DIR]
  writes sorter/pages/f101v_L<nn>.jpg (deskewed), signs.tsv, labels.tsv, focus.tsv, fit_recut.tsv, clusters.tsv, region.json
  (the v2 cut is kept for the record as signs_v2.tsv / labels_v2.tsv / focus_v2.tsv; its x/y refer to the v2 sloped pages/)
"""
import argparse, csv, shutil, sys
from collections import Counter, defaultdict
from pathlib import Path
import numpy as np

S = Path(__file__).resolve().parent; T = S.parent; P = S / 'pages'
sys.path.insert(0, str(S)); sys.path.insert(0, str(S.parents[2] / 'tools'))
import build_inputs as bi  # noqa: E402  (traces(), PITCH, the region image; its main() is not run on import)
import sorter_recut as sr  # noqa: E402

MINPAIR = 4; MAPPED = 29          # VIV-T bands 1-29 sit on lines 1-29 (build_inputs.py); 30-33 have no reader row of their own
CFG = sr.Cfg(pitch=bi.PITCH, half=122, xmin=450, xmax=bi.W - 40,      # left margin (cipher starts x ~600); gutter scan edge
             nclu=100, gen_share=0.2, generic=('split-rare', 'one-reader', 'UNREAD', 'foot-unplaced'))   # unaligned tiles prefer a named pile


def main():
    ap = argparse.ArgumentParser(); ap.add_argument('--debug'); a = ap.parse_args()
    for f in ('signs', 'labels', 'focus'):                          # the v2 cut, kept for the record (once)
        src, dst = S / f'{f}.tsv', S / f'{f}_v2.tsv'
        if src.exists() and not dst.exists(): shutil.copy(src, dst)
    v2 = defaultdict(list)
    for r in csv.DictReader(open(S / 'signs_v2.tsv'), delimiter='\t'):
        v2[r['page']].append(int(r['x']) + int(r['w']) / 2)
    draft = defaultdict(list)                                       # as build_inputs.main()
    for r in csv.DictReader(open(T / 'tx' / 'ciphertext_draft.tsv'), delimiter='\t'):
        x, alt = r['sign'] or '?', r['alt'] if r['alt'][-1:] != ':' else r['alt'] + '?'
        if r['why'] == 'agree':
            draft[r['line']].append(('agree', x, x)); continue
        who, other = alt.split(':', 1); other = other or '?'
        A, B = (x, other) if who == 'B' else (other, x)
        draft[r['line']].append(('gap' if r['why'] == 'gap' else 'differ', A, B))
    inl = lambda ln: int(ln[-2:]) <= MAPPED
    pairs = Counter((A, B) for ln, v in draft.items() if inl(ln) for k, A, B in v if k == 'differ')
    ones = Counter((A if A != '-' else B) for ln, v in draft.items() if inl(ln) for k, A, B in v if k == 'gap')

    def pile(kind, A, B):
        if kind == 'agree':
            lab, fam = (A if A not in ('', '?') else 'UNREAD'), A
        elif kind == 'differ':
            lab, fam = (f'{A}/{B}' if pairs[(A, B)] >= MINPAIR else 'split-rare'), A
        else:
            one = A if A != '-' else B; lab, fam = (f'{one}+1r' if ones[one] >= MINPAIR else 'one-reader'), one
        fam = fam if fam not in ('', '?', '-') else 'UNREAD'
        return (lab.replace('?', 'UNREAD') if lab != 'split-rare' else lab), fam

    grey = np.array(bi.src); TR = bi.traces(); n = len(TR)
    pages = [f'f101v_L{k:02d}' for k in range(1, n + 1)]
    cols = [[pile(*c) for c in draft[f'c107_L{k:02d}']] if k <= MAPPED else [] for k in range(1, n + 1)]
    fb = ['one-reader' if k <= MAPPED else 'foot-unplaced' for k in range(1, n + 1)]
    sr.run(grey, TR, pages, cols, [v2[p] for p in pages], S, P, CFG, fallback=fb, debug=a.debug,
           region_image=str((T / 'images' / bi.man[0]['source_file']).relative_to(S.parents[2])))   # region.json (SORTER-PAGEVIEW)


if __name__ == '__main__':
    main()
