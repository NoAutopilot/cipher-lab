#!/usr/bin/env python3
"""R10-FLOR2 (6 Oct 2026): sign-sorter inputs for c.127 cipher lines L02-L18 (images/c127b2/ crops, GAPS106), cut by
tools/glyph_atlas.py segment with the R9-FLOR thresholds plus a shared scale (--mark-h 0.7 --min-area 0.25
--median-h pool; pool = 48.5 px, the median of these 33 crops' own medians, range 4-72). No machine pass has read these lines, so the starting piles
are provisional SHAPE CLUSTERS (glyph_atlas cluster, k-means, fixed seed), named k01..kNN, not sign names or values.

Kept: every box on L02_s1..L18_s1 and L02_s2..L17_s2, except
  - clear text (eye-checked on the crops, R10-FLOR2): L02_s1 x < 420 ("ghalio"), L18_s1 x >= 1045 (from the "/" on,
    "...medite delcquan..."), all of L18_s2 (clear);
  - the s1/s2 overlap (100 px, manifest boxes 150-2130 / 2030-4010): a box belongs to s1 if its centre is under s1 x
    1930, to s2 if its centre is at or past s2 x 50, so a boundary sign is a tile once.
Boxes touching the crop's top or bottom edge are trimmed to the run of ink rows holding the line centre (trim()).
Lines L03-L17 were not eye-checked for clear words beyond GAPS106's note (only L02 and L18 named as mixed).
Focus box: the widest boxes (rw >= 1.9 x the shared median, likeliest two signs in one box, e.g. L08_s1) and the
boxes with the tallest marks attached; questions are free prose answered by Fix the cut / BAD-CUT / a pile.

  python3 sorter/c127b2/build_inputs.py [SCRATCH]   (from ciphers/florence-dieci-responsive; writes sorter/c127b2/
        signs.tsv, labels.tsv, marks.tsv, clusters.tsv, focus.tsv, cipher_lines.tsv; segment output goes to SCRATCH)
"""
import csv, os, subprocess, sys
import numpy as np
from PIL import Image
from pathlib import Path
T = Path(__file__).resolve().parents[2]; S = T / 'sorter' / 'c127b2'; TOOL = T.parents[1] / 'tools' / 'glyph_atlas.py'
OUT = Path(sys.argv[1] if len(sys.argv) > 1 else '/tmp/r10flor2')
K = 30                      # over-split on purpose: the pilot sorter had 27 piles for 120 tiles
X_RANGE = {'c127b2_L02_s1': (420, 1980), 'c127b2_L18_s1': (0, 1045)}
LINES = [f'c127b2_L{n:02d}_s{s}' for n in range(2, 19) for s in (1, 2) if (n, s) != (18, 2)]


def tsv(p):
    return list(csv.DictReader(open(p), delimiter='\t'))


def keep(r):
    c = int(r['x']) + int(r['w']) / 2
    lo, hi = X_RANGE.get(r['page'], (0, 1980))
    if r['page'].endswith('_s1'):
        hi = min(hi, 1930)
    else:
        lo = max(lo, 50)
    return lo <= c < hi


pages = [a for p in LINES for a in ('--page', f'{p}={T}/images/c127b2/{p}.jpg')]
run = lambda *a: subprocess.run([sys.executable, str(TOOL), *a], check=True, capture_output=True, text=True).stdout
print(run('segment', '--out', str(OUT), '--mark-h', '0.7', '--min-area', '0.25', '--median-h', 'pool', *pages)
      .splitlines()[0])
signs = [r for r in tsv(OUT / 'signs.tsv') if keep(r)]


def trim(r):
    """A box touching the crop's top or bottom edge usually carries a neighbour line's descender or ascender (the
    sorter_preflight strip-height shape). Keep only the run of ink rows, inside the box's columns, that holds the
    line centre (the crop's middle row); a near-blank row (under 2 px or 4% of the width darker than 0.7 x the crop median) separates the
    neighbour stroke."""
    im = IMG.setdefault(r['page'], np.array(Image.open(T / 'images' / 'c127b2' / f'{r["page"]}.jpg').convert('L')))
    H = im.shape[0]
    x, y, w, h = (int(r[k]) for k in ('x', 'y', 'w', 'h'))
    if y > 2 and y + h < H - 2:
        return 0
    ink = (im[:, x:x + w] < 0.7 * np.median(im)).sum(1) >= max(2, 0.04 * w)   # a row of real stroke, not a speck
    c = min(max(H // 2, y), y + h - 1)
    if not ink[c]:
        near = [i for i in range(y, y + h) if ink[i]]
        if not near:
            return 0
        c = min(near, key=lambda i: abs(i - H // 2))
    a, b = c, c
    while a > y and ink[a - 1]:
        a -= 1
    while b < y + h - 1 and ink[b + 1]:
        b += 1
    if (a, b + 1) == (y, y + h):
        return 0
    r['y'], r['h'] = str(a), str(b + 1 - a)
    return 1


IMG = {}
print(f'trimmed {sum(trim(r) for r in signs)} edge-touching boxes to the line-centre ink run')
ids = {r['sid'] for r in signs}
marks = [m for m in tsv(OUT / 'marks.tsv') if m['sid'] in ids]
run('cluster', '--out', str(OUT), '--k', str(K), '--k-marks', '4', '--pca-scale', 'shared')
cl = {r['id']: int(r['cluster']) for r in tsv(OUT / 'clusters.tsv') if r['kind'] == 'sign'}
name = lambda r: f'k{cl[r["sid"]] + 1:02d}'
with open(S / 'signs.tsv', 'w') as f:
    f.write('sid\tpage\tx\ty\tw\th\n')
    for r in signs:
        f.write('\t'.join(r[k] for k in ('sid', 'page', 'x', 'y', 'w', 'h')) + '\n')
with open(S / 'labels.tsv', 'w') as f:
    f.write('sid\tsign\tfamily\tcluster\n')
    for r in signs:
        f.write(f'{r["sid"]}\t{name(r)}\t{name(r)}\t{name(r)}\n')
with open(S / 'marks.tsv', 'w') as f:
    f.write('x\ty\tw\th\tsid\n')
    for m in marks:
        f.write('\t'.join(m[k] for k in ('x', 'y', 'w', 'h', 'sid')) + '\n')
with open(S / 'cipher_lines.tsv', 'w') as f:
    f.write('line\tx0\tx1\n')
    for p in LINES:
        lo, hi = X_RANGE.get(p, (0, 1980))
        f.write(f'{p}\t{lo}\t{hi}\n')
EXTRA = ('c127b2_L08_s1_01_002', 'c127b2_L08_s1_01_003')
wide = sorted(signs, key=lambda r: -float(r['rw']))
focus = [r for r in wide if float(r['rw']) >= 1.9 and r['sid'] not in EXTRA][:16]
nm = {}
for m in marks:
    nm[m['sid']] = max(nm.get(m['sid'], 0), float(m['rh']))
tallmk = [s for s in sorted(nm, key=lambda s: -nm[s]) if s not in {r['sid'] for r in focus}][:4]
EXTRA = {sid: 'Letter-like forms ("a b a b") between cipher signs on L08: a clear word written in the line (BAD-CUT / '
               'Not a letter) or cipher signs? If cipher, Fix the cut into single signs.'
         for sid in ('c127b2_L08_s1_01_002', 'c127b2_L08_s1_01_003')}
with open(S / 'focus.tsv', 'w') as f:
    for sid, q in EXTRA.items():
        if sid in ids:
            f.write(f'{sid}\t{q}\n')
    for r in focus:
        f.write(f'{r["sid"]}\tA wide box ({float(r["rw"]):.1f} x the median sign height): one sign, or two written '
                f'together? Fix the cut if two; otherwise put it in its pile.\n')
    for s in tallmk:
        f.write(f'{s}\tA large mark is attached above this sign: is it part of the sign (a different sign), a '
                f'separate sign, or a stray stroke?\n')
print(f'{len(signs)} tiles on {len(LINES)} crops, {len(set(map(name, signs)))} provisional piles, {len(marks)} marks, '
      f'{len(focus) + len(tallmk) + 2} focus tiles')
