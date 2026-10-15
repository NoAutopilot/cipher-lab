#!/usr/bin/env python3
"""BNF-GIEVRE-SORT (15 Oct 2026): sign tiles for fr3985-gievre-1593 f.89 (BnF fr.3985 pencil f.89, canvas 179), cipher lines L01-L03.
Source: the committed line crops images/f89/f89_L0N_s1/s2.jpg (BNF-Q2-TX; native pixels, s1 = x 900-3300, s2 = x 2100-4500 of
images/f179_native.jpg). Each line is stitched at native x=2700 (the crops overlap 2100-3300), stacked into region.jpg, tiled by ink
groups (tools/sorter_recut.py). No reader columns, no key: every starting pile is a shape-cluster pile (value-blind). Focus = tiles
whose x lies within a window of a position where pass A and pass B (passA.tsv, passB.tsv) disagree -- positions only, never the
readings. No network.
  python3 ciphers/fr3985-gievre-1593/sorter/cut.py
"""
import sys, csv
from pathlib import Path
import numpy as np
from PIL import Image
S = Path(__file__).resolve().parent; T = S.parent
sys.path.insert(0, str(T.parents[1] / 'tools'))
import sorter_recut as sr
NAMES = ['L01', 'L02', 'L03']
BAND = 170; X0 = 900; SPLIT = 2700; W = 3600
CFG = sr.Cfg(pitch=85, half=85, xmin=5, xmax=3480, rel=0.80, own=0.8, core=0.3, nclu=8, per_clu=1, nfocus=0, minpix=40, dot=0.10, split=1.6, skip=45, clear=30)

def stitch(n):
    a = np.array(Image.open(T / 'images/f89' / f'f89_{n}_s1.jpg').convert('L')); b = np.array(Image.open(T / 'images/f89' / f'f89_{n}_s2.jpg').convert('L'))
    h = a.shape[0]; line = np.full((h, W), 255, np.uint8)
    line[:, :SPLIT - X0] = a[:, :SPLIT - X0]; line[:, SPLIT - X0:] = b[:, SPLIT - 2100:SPLIT - 2100 + (W - (SPLIT - X0))]
    band = np.full((BAND, W), 255, np.uint8); y0 = (BAND - h) // 2; band[y0:y0 + h] = line
    return band

def main():
    grey = np.vstack([stitch(n) for n in NAMES]); Image.fromarray(grey).save(S / 'region.jpg', quality=88)
    traces = [np.full(W, i * BAND + BAND / 2) for i in range(len(NAMES))]
    tiles, _ = sr.run(grey, traces, NAMES, [[] for _ in NAMES], [[] for _ in NAMES], S, S / 'pages', CFG,
                      fallback=['unsorted'] * len(NAMES), debug=str(S / 'debug'), region_image=str((S / 'region.jpg').relative_to(T.parents[1])))
    # post-cut (by eye on debug/, display px x1.8 = strip px): keep only the cipher spans; the clear-text words between them are not tiled.
    # Spans (strip x): L01 335-645 and 1040-1900 disp; L02 100-350 and 600-1900; L03 120-1680 (display px, x1.8 below).
    KEEP = {'L01': [(335, 645), (1040, 1900)], 'L02': [(100, 350), (600, 1900)], 'L03': [(120, 1680)]}
    tiles = [t for t in tiles if any(a * 1.8 <= t['x'] + t['w'] / 2 <= b * 1.8 for a, b in KEEP[t['page']]) and t['w'] * t['h'] >= 300]
    # Focus: windows around the columns where pass A and pass B (passA.tsv, passB.tsv) disagree, by position only, no reading.
    FOC = {'L01': [(335, 645), (1700, 1900)], 'L02': [(100, 350), (600, 1000), (1230, 1310), (1690, 1760)],
           'L03': [(700, 740), (830, 890), (1240, 1310), (1480, 1680)]}
    foc = [t for t in tiles if any(a * 1.8 <= t['x'] + t['w'] / 2 <= b * 1.8 for a, b in FOC[t['page']])]
    for t in tiles: t['sign'] = 'unsorted' if t['cluster'] == 99 else 'shape-%02d' % t['cluster']; t['family'] = t['sign']
    def w(name, keys):
        with open(S / name, 'w') as o:
            o.write('\t'.join(keys) + '\n'); o.writelines('\t'.join(str(t[k]) for k in keys) + '\n' for t in tiles)
    w('signs.tsv', ['sid', 'page', 'x', 'y', 'w', 'h']); w('labels.tsv', ['sid', 'sign', 'family'])
    with open(S / 'focus.tsv', 'w') as o:
        for t in foc:
            o.write(f"{t['sid']}\tcut from line {t['page']} of the cipher paragraph: which sign is this? Pile it with the same sign elsewhere, make a new pile, or mark a bad cut.\n")
    print(len(foc), 'focus tiles')
    return tiles

if __name__ == '__main__':
    tl = main(); print(len(tl), 'tiles'); 
    from collections import Counter; print(Counter(t['page'] for t in tl))
