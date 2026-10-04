#!/usr/bin/env python3
"""ARM-SORTER (4 Oct 2026): cut the shorthand marks of Armstrong to Madison, 20 Feb 1808, into tiles for the sign sorter.

  python3 ciphers/armstrong-madison-1808/sorter/segment_marks.py [--debug DIR]

Reads runs.tsv (one row per mark run: frame and a box in that frame's native pixels, located by eye on ruler overviews
of the ARM-TR line bands) and exclude.tsv (tiles inside a run box that are numerals or a neighbour line's ink, removed by
eye from the debug overlays), and writes signs.tsv (sid, page, x, y, w, h in the frame image's pixels) and labels.tsv
(sid, sign, family: every tile starts in pile "unsorted" before clustering). Disk only.

Why not tools/glyph_atlas.py segment: tried first. --cursive needs an x-height band, and these marks are isolated
strokes of very different heights (its xh estimates ran 10-76 px over the 37 runs, dropping or merging whole marks);
the default mode thresholds by each strip's median component height, which on a strip of a few marks is a dust speck
(median 5 px on p3-L12a), so it cut 640 pieces. Here every threshold is absolute: the frames share one scale (about
60-70 px digit height on 0030, 0031 and 0033).
Steps per run box: background-normalised grey (divide by a 41 px grey closing); ink < 0.62 x background; 8-connected
components; keep a component only if its darkest 10% is under 0.45 x background (bleed-through and ghost ink are
lighter) and its longer side >= 9 px; drop components whose vertical centre is more than 60 px from the run's ink centre line (area-weighted
median of component centres: a neighbour line's descender or ascender); a small component (longer side < 18 px:
a dot, a short tick) joins the nearest kept component whose box lies within 22 px, or stays a tile of its own; two
components whose x-ranges overlap by more than 60% of the narrower are one tile (a mark in two strokes). Over-splits
rather than merges: the owner merges in the sorter.
"""
import argparse, csv
from pathlib import Path
import numpy as np, cv2
HERE = Path(__file__).resolve().parent; T = HERE.parent

def boxes_for(g):
    bg = cv2.morphologyEx(g, cv2.MORPH_CLOSE, cv2.getStructuringElement(cv2.MORPH_RECT, (41, 41)))
    norm = g.astype(float) / np.maximum(bg.astype(float), 1)
    ink = (norm < 0.62).astype(np.uint8)
    n, lab, st, _ = cv2.connectedComponentsWithStats(ink, connectivity=8)
    H, W = g.shape; comps = []
    for i in range(1, n):
        x, y, w, h, a = st[i]
        if max(w, h) < 9 or a < 25: continue
        vals = norm[lab == i]
        if np.quantile(vals, 0.1) > 0.45: continue
        comps.append([x, y, x + w, y + h])
    # neighbour lines: keep components whose vertical centre lies within 60 px of the run's ink centre line (area-
    # weighted median of component centres; line pitch is 120-150 px on these frames)
    if comps:
        cy = np.array([(c[1]+c[3])/2 for c in comps]); wt = np.array([(c[2]-c[0])*(c[3]-c[1]) for c in comps], float)
        o = np.argsort(cy); cum = np.cumsum(wt[o]); mid = cy[o][np.searchsorted(cum, cum[-1]/2)]
        comps = [c for c in comps if abs((c[1]+c[3])/2 - mid) <= 60]
    big = [c for c in comps if max(c[2]-c[0], c[3]-c[1]) >= 18]
    small = [c for c in comps if max(c[2]-c[0], c[3]-c[1]) < 18]
    def gap(a, b):
        dx = max(0, max(a[0], b[0]) - min(a[2], b[2])); dy = max(0, max(a[1], b[1]) - min(a[3], b[3]))
        return max(dx, dy)
    for s in small:
        if big:
            j = min(range(len(big)), key=lambda k: gap(s, big[k]))
            if gap(s, big[j]) <= 22:
                b = big[j]; big[j] = [min(b[0], s[0]), min(b[1], s[1]), max(b[2], s[2]), max(b[3], s[3])]; continue
        big.append(s)
    changed = True
    while changed:
        changed = False; big.sort()
        for i in range(len(big) - 1):
            a, b = big[i], big[i+1]
            ov = min(a[2], b[2]) - max(a[0], b[0]); nar = min(a[2]-a[0], b[2]-b[0])
            if ov > 0.6 * nar:
                big[i] = [min(a[0], b[0]), min(a[1], b[1]), max(a[2], b[2]), max(a[3], b[3])]; del big[i+1]; changed = True; break
    return sorted(big)

def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('--debug', help='write one overlay per run here, tile numbers drawn')
    a = ap.parse_args()
    excl = set()
    if (HERE/'exclude.tsv').exists():
        for r in csv.DictReader(open(HERE/'exclude.tsv'), delimiter='\t'): excl.add(r['sid'])
    imgs = {}; signs = []; dbg = Path(a.debug) if a.debug else None
    if dbg: dbg.mkdir(parents=True, exist_ok=True)
    for r in csv.DictReader(open(HERE/'runs.tsv'), delimiter='\t'):
        page = f"M34-014-{r['frame']}"
        if page not in imgs: imgs[page] = cv2.imread(str(T/'images'/f'{page}.jpg'), cv2.IMREAD_GRAYSCALE)
        x0, y0, x1, y1 = (int(r[k]) for k in ('x0', 'y0', 'x1', 'y1'))
        g = imgs[page][y0:y1, x0:x1]; bx = boxes_for(g)
        vis = cv2.cvtColor(g, cv2.COLOR_GRAY2BGR) if dbg else None
        for i, (a0, b0, a1, b1) in enumerate(bx, 1):
            sid = f"{r['run']}_{i:02d}"; keep = sid not in excl
            if keep: signs.append((sid, page, x0 + a0, y0 + b0, a1 - a0, b1 - b0, r['run']))
            if dbg:
                cv2.rectangle(vis, (a0, b0), (a1, b1), (0, 0, 255) if keep else (200, 200, 200), 1)
                cv2.putText(vis, str(i), (a0, max(10, b0 - 2)), cv2.FONT_HERSHEY_SIMPLEX, 0.45, (255, 0, 0), 1)
        if dbg: cv2.imwrite(str(dbg/f"{r['run']}.jpg"), vis)
    with open(HERE/'signs.tsv', 'w') as f:
        f.write('sid\tpage\tx\ty\tw\th\trun\n')
        for s in signs: f.write('\t'.join(map(str, s)) + '\n')
    with open(HERE/'labels.tsv', 'w') as f:
        f.write('sid\tsign\tfamily\n')
        for s in signs: f.write(f'{s[0]}\tunsorted\tmarks\n')
    print(len(signs), 'tiles,', len(excl), 'excluded by eye')

if __name__ == '__main__': main()
