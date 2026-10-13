#!/usr/bin/env python3
"""BNF-RONDI-SORT (13 Oct 2026): sign tiles for fr.3613 f.62r cipher lines L01-L17, cut from the committed crops images/f62/.
Each line's two overlapping segments (s1, s2) are joined into one band of a stacked region (s2 shifted by the box y offsets in
images/f62/manifest.json), tiles are ink groups (tools/sorter_recut.py), every starting pile is a shape cluster (value-blind).
Focus = tiles that line up (monotone DP over evenly spaced columns) with a column where tx/passA.tsv and tx/passB.tsv split
(tx/disagreements.tsv); the page carries no value, no pass text and no machine label. No network.
  python3 ciphers/fr3613-rondinelli-1590/sorter/cut.py
"""
import sys, csv, json
from pathlib import Path
import numpy as np
from PIL import Image
S = Path(__file__).resolve().parent; T = S.parent; ROOT = T.parents[1]
sys.path.insert(0, str(ROOT / 'tools'))
import sorter_recut as sr
NL, BAND, W = 17, 300, 3500
CEN = 150
CFG = sr.Cfg(pitch=100, half=100, xmin=20, xmax=3360, rel=0.78, own=0.7, core=0.25, nclu=10, per_clu=1, nfocus=0, minpix=25, dot=0.12,
             split=1.5, skip=60, clear=30, recentre=50)

def main():
    man = {e['crop']: e for e in json.load(open(T / 'images/f62/manifest.json'))['iiif_lines']}
    grey = np.full((NL * BAND, W), 255, np.uint8); pages, traces = [], []
    for n in range(1, NL + 1):
        p = f'f62_L{n:02d}'; y0 = (n - 1) * BAND
        b1, b2 = man[p + '_s1.jpg']['box'], man[p + '_s2.jpg']['box']
        a = np.array(Image.open(T / 'images/f62' / (p + '_s1.jpg')).convert('L'))
        b = np.array(Image.open(T / 'images/f62' / (p + '_s2.jpg')).convert('L'))
        dy = b2[1] - b1[1]; dx = b2[0] - b1[0]
        yy = CEN - a.shape[0] // 2
        grey[y0 + yy:y0 + yy + a.shape[0], :a.shape[1]] = a
        seam = dx + (a.shape[1] - dx) // 2
        yb = yy + dy
        h = b.shape[0]; lo, hi = max(0, -yb), min(h, BAND - yb)
        grey[y0 + yb + lo:y0 + yb + hi, seam:dx + b.shape[1]] = b[lo:hi, seam - dx:]
        pages.append(p); traces.append(np.full(W, y0 + CEN, float))
    Image.fromarray(grey).save(S / 'region.jpg', quality=85)
    tiles, _ = sr.run(grey, traces, pages, [[] for _ in pages], [[] for _ in pages], S, S / 'pages', CFG,
                      fallback=['unsorted'] * len(pages), debug=str(S / 'debug'), region_image=str((S / 'region.jpg').relative_to(ROOT)))
    # blind starting piles: shape clusters only
    cl = {r['sid']: r['cluster'] for r in csv.DictReader(open(S / 'clusters.tsv'), delimiter='\t')}
    for t in tiles: t['sign'] = t['family'] = 'shape-%02d' % int(cl[t['sid']])
    with open(S / 'labels.tsv', 'w') as o:
        o.write('sid\tsign\tfamily\n'); o.writelines(f"{t['sid']}\t{t['sign']}\t{t['family']}\n" for t in tiles)
    dis = {}
    for r in csv.DictReader(open(T / 'tx/disagreements.tsv'), delimiter='\t'): dis.setdefault(r['line'], set()).add(int(r['col']))
    ncols = {r['line']: int(r['columns']) for r in csv.DictReader(open(T / 'tx/agreement.tsv'), delimiter='\t')}
    focus = []
    for p in pages:
        ts = [t for t in tiles if t['page'] == p]
        if not ts or p not in dis: continue
        cx_t = [t['x'] + t['w'] / 2 for t in ts]; m = ncols[p]
        cx = list(np.linspace(cx_t[0], cx_t[-1], m)) if m > 1 else cx_t[:1]
        al = sr.align(cx_t, cx, 80)
        for i, j in al.items():
            if (j + 1) in dis[p]: focus.append(ts[i]['sid'])
    with open(S / 'focus.tsv', 'w') as o:
        for s in focus: o.write(f"{s}\tTwo blind readers wrote this place differently. Which sign is it? Pile it with the others like it, start another pile, fix the cut, or send it to BAD-CUT.\n")
    print(len(tiles), 'tiles', len(focus), 'focus', len(set(t['sign'] for t in tiles)), 'piles')

if __name__ == '__main__': main()
