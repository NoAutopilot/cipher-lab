#!/usr/bin/env python3
"""TXE4-2 step 2a (read-free): keep only each f.130 crop's MIDDLE row (the line, f130/pass_instructions.md) and dedupe the
s1/s2 overlap at its midpoint (TXE3-6 / OL1-BOXES rule), writing tiles/line_signs.tsv for box_token_align (page f130, line nn,
s2 x offset +1600). Middle row = the smoothed row-ink profile's peak nearest the crop's vertical centre; a box is kept when its
vertical centre lies within 0.9 x the pooled median sign height (31 px) of that peak (PREREG-txeng4-2 "Fixed inputs").
    python3 middle_row.py [TILE_DIR]"""
import csv, os, sys, numpy as np, cv2
from scipy.ndimage import uniform_filter1d
from scipy.signal import find_peaks
HERE = os.path.dirname(os.path.abspath(__file__))
TD = os.path.join(HERE, sys.argv[1] if len(sys.argv) > 1 else 'tiles')   # optional tile dir (tiles_x/ for the exploration)
A = os.path.join(TD, 'atlas')
MH, BAND, OVER, OFF = 31.0, 0.9, 80, 1600
rows = list(csv.DictReader(open(os.path.join(A, 'signs.tsv')), delimiter='\t'))
out, log = [], []
for page in sorted({r['page'] for r in rows}):
    g = cv2.imread(os.path.join(A, 'crops', page + '.png'), cv2.IMREAD_GRAYSCALE)
    ink = (g < 0.78 * cv2.GaussianBlur(cv2.morphologyEx(g, cv2.MORPH_CLOSE, np.ones((15, 15), np.uint8)), (0, 0), 5)).astype(float)
    prof = uniform_filter1d(ink.sum(axis=1), 15)
    peaks, _ = find_peaks(prof, distance=20, prominence=prof.max() * 0.08)
    if not len(peaks):
        log.append(f'{page}: no peak'); continue
    mid = int(peaks[np.argmin(np.abs(peaks - g.shape[0] / 2))])
    seg = page[-2:]; ln = int(page[6:8])
    kept = dropped_band = dropped_over = 0
    for r in rows:
        if r['page'] != page:
            continue
        yc = int(r['y']) + int(r['h']) / 2; xc = int(r['x']) + int(r['w']) / 2
        if abs(yc - mid) > BAND * MH:
            dropped_band += 1; continue
        if (seg == 's1' and xc > g.shape[1] - OVER) or (seg == 's2' and xc < OVER):
            dropped_over += 1; continue
        x = int(r['x']) + (OFF if seg == 's2' else 0)
        out.append(dict(sid=r['sid'], page='f130', line=ln, pos=0, x=x, y=r['y'], w=r['w'], h=r['h'], rh=r['rh'], rw=r['rw'],
                        dy=r['dy'], marks=r['marks'], src_page=page))
        kept += 1
    log.append(f'{page}: rows at {list(map(int, peaks))}, middle {mid} (crop h {g.shape[0]}): kept {kept}, other rows {dropped_band}, overlap {dropped_over}')
out.sort(key=lambda r: (r['line'], r['x']))
n = {}
for r in out:
    n[r['line']] = n.get(r['line'], 0) + 1; r['pos'] = n[r['line']]
cols = ['sid', 'page', 'line', 'pos', 'x', 'y', 'w', 'h', 'rh', 'rw', 'dy', 'marks', 'src_page']
with open(os.path.join(TD, 'line_signs.tsv'), 'w') as f:
    f.write('\t'.join(cols) + '\n')
    for r in out:
        f.write('\t'.join(str(r[c]) for c in cols) + '\n')
print('\n'.join(log)); print('line_signs.tsv:', len(out), 'boxes;', {l: c for l, c in sorted(n.items())})
