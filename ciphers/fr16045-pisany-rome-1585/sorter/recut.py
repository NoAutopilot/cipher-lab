#!/usr/bin/env python3
"""PIS-RECUT (4 Oct 2026): re-cut the f.75r sorter so that ONE TILE = ONE SIGN, on straight (deskewed) line strips.

Owner, on the v2 page: many tiles straddled two signs or cut one in half (f75_L08_02 = looped l + the b beside it), because
build_inputs.py fitted ink-profile blobs to the readers' column COUNT; and the lines slope ~160 px across the region, so the
context strip showed the line above. tighten_tiles.py trimmed only vertically. This script replaces both for the page.

  python3 ciphers/fr16045-pisany-rome-1585/sorter/recut.py [--debug DIR]
  writes sorter/pages/f75_L<nn>.jpg (deskewed), signs.tsv, labels.tsv, focus.tsv, fit_recut.tsv, clusters.tsv, region.json
  (the v2 cut is kept for the record as signs_v2.tsv / signs_tight_v2.tsv / labels_v2.tsv / focus_v2.tsv)

1. Deskew. Per line, build_inputs.traces() gives the line centre y(x) on the Gallica region already on disk. Each column x
   of the region is shifted so that y(x) lands on the strip's middle row (a shear; the slope is ~3 degrees, so a shear is
   indistinguishable from a rotation at this size). Every strip is the full region width and HALF px either side of the
   centre, so the sorter's context view (lines above and below at the same x window) shows straight, neighbouring lines.
2. Segment by the sign's own ink: background-normalised binarisation (pixel < REL x grey closing), 8-connected components
   on the strip +- one pitch. A component belongs to this line if its median row is within OWN x pitch of the centre and it
   has ink within CORE x pitch of it (crosses and descenders of the lines above/below fail one test or the other).
   Components whose x-ranges overlap by more than half of the narrower are one sign (two strokes, dots above). Small
   marks (longer side < DOT x pitch) with no overlap stay their own tile (the owner merges fast; a dot sign is possible).
   A group wider than SPLIT x the line's median sign width is cut into round(width / median) pieces at the column-ink
   minima nearest the equal-width cut points (touching signs: q q, b e x).
3. Starting piles, value-blind. Columns of tx/ciphertext_draft.tsv (pass A vs pass B) carry the v2 tile's x centre as a
   position estimate; tiles and columns are aligned in x order by dynamic programming (cost |dx|, skip cost SKIP px).
   A tile matched within CLEAR px takes that column's pile (same naming as build_inputs.py: S15, S10/S41, S21+1r,
   split-rare, one-reader, NOCELL). Every other tile goes to the pile its shape cluster (k-means on 32x32 bitmaps + aspect,
   NCLU clusters over the page) mostly holds among the clear tiles, and is a focus candidate. Focus (<= 40): unclear
   tiles ranked by their cluster's size (frequent shapes first), at most PER_CLU per cluster.
"""
import argparse, csv, shutil, sys
from collections import Counter, defaultdict
from pathlib import Path
import numpy as np

S = Path(__file__).resolve().parent; T = S.parent; P = S / 'pages'
sys.path.insert(0, str(S))
import build_inputs as bi  # noqa: E402  (traces(), norm(), PITCH, the region image)

sys.path.insert(0, str(S.parents[2] / 'tools'))
import sorter_recut as sr  # noqa: E402  (shared since LL-RECUT, 4 Oct 2026: deskew, recentre, segment, align, run)

MINPAIR = 4
CFG = sr.Cfg(pitch=bi.PITCH, half=120, xmin=15, xmax=2870)   # the scan's dark right edge starts at x ~2880 (build_inputs.blobs)


def main():
    ap = argparse.ArgumentParser(); ap.add_argument('--debug'); a = ap.parse_args()
    for f in ('signs', 'signs_tight', 'labels', 'focus'):          # the v2 cut, kept for the record (once)
        src, dst = S / f'{f}.tsv', S / f'{f}_v2.tsv'
        if src.exists() and not dst.exists(): shutil.copy(src, dst)
    v2 = defaultdict(list)
    for r in csv.DictReader(open(S / 'signs_v2.tsv'), delimiter='\t'):
        v2[r['page']].append(int(r['x']) + int(r['w']) / 2)
    draft = defaultdict(list)
    for r in csv.DictReader(open(T / 'tx' / 'ciphertext_draft.tsv'), delimiter='\t'):
        A = bi.norm(r['sign']) or 'UNREAD'
        if r['why'] == 'agree': draft[r['line']].append(('agree', A, A)); continue
        who, other = r['alt'].split(':', 1); other = bi.norm(other) or 'UNREAD'
        x, y = (A, other) if who == 'B' else (other, A)
        draft[r['line']].append(('gap' if r['why'] == 'gap' else 'differ', x, y))
    pairs = Counter((A, B) for v in draft.values() for k, A, B in v if k == 'differ')
    ones = Counter((A if A != '-' else B) for v in draft.values() for k, A, B in v if k == 'gap')

    def pile(kind, A, B):
        if kind == 'agree': return A, A
        if kind == 'differ': return (f'{A}/{B}' if pairs[(A, B)] >= MINPAIR else 'split-rare'), A
        one = A if A != '-' else B
        return (f'{one}+1r' if ones[one] >= MINPAIR else 'one-reader'), one

    grey = np.array(bi.src); TR = bi.traces(); pages = [f'f75_L{n:02d}' for n in range(1, len(TR) + 1)]
    cols = [[pile(*c) for c in draft[f'L{n:02d}']] for n in range(1, len(TR) + 1)]
    sr.run(grey, TR, pages, cols, [v2[p] for p in pages], S, P, CFG, debug=a.debug,
           region_image=str((T / 'images' / bi.SRC).relative_to(S.parents[2])))   # region.json (SORTER-PAGEVIEW)


if __name__ == '__main__':
    main()
