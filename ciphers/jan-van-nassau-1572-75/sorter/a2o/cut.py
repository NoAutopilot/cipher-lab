#!/usr/bin/env python3
"""SORT-A2o (10 Oct 2026): sign tiles for the JVN-GLY glyph questions, cut from the committed crops images/jvn_gly/X1-X7.
Each crop is one 'line' of a stacked composite (region.jpg); tiles are ink groups (tools/sorter_recut.py). No reader columns:
every starting pile is the shape-cluster pile (value-blind). Focus = every tile of X3 (the three glyphs in question on 5551
p3 L2) and X7_140 (the digit between 85/29 and 'Perm'), by page name only; no value, key or machine label on the page.
  python3 ciphers/jan-van-nassau-1572-75/sorter/a2o/cut.py
"""
import sys, csv
from pathlib import Path
import numpy as np
from PIL import Image
S = Path(__file__).resolve().parent; T = S.parents[1]
sys.path.insert(0, str(T.parents[1] / 'tools'))
import sorter_recut as sr
NAMES = ['X1', 'X2', 'X3', 'X4', 'X5', 'X6', 'X7_140']
BAND = 170
CFG = sr.Cfg(pitch=85, half=85, xmin=3, rel=0.80, own=0.8, core=0.3, nclu=8, per_clu=1, nfocus=0, minpix=12, dot=0.10, split=1.6, skip=45, clear=30)

def main():
    W = 560; parts = []; traces = []
    for i, n in enumerate(NAMES):
        g = np.array(Image.open(T / 'images' / 'jvn_gly' / f'{n}.jpg').convert('L'))
        band = np.full((BAND, W), 255, np.uint8)
        h, w = g.shape; y0 = (BAND - h) // 2; band[y0:y0 + h, :w] = g; parts.append(band)
        traces.append(np.full(W, i * BAND + BAND / 2))
    grey = np.vstack(parts); Image.fromarray(grey).save(S / 'region.jpg', quality=85)
    tiles, _ = sr.run(grey, traces, NAMES, [[] for _ in NAMES], [[] for _ in NAMES], S, S / 'pages', CFG,
                      fallback=['unsorted'] * len(NAMES), debug=str(S / 'debug'), region_image=str((S / 'region.jpg').relative_to(T.parents[1])))
    # post-cut (by eye on debug/ and a 2x grid): the auto ink groups split or join cursive digits badly on X3 and X7_140, and X5 is one
    # group, so those three crops are tiled by hand (boxes in band px = the page strip px); the other crops keep their ink groups,
    # minus dot-sized specks and word-wide groups.
    MAN = {'X3': [('g1', 8, 46, 60, 82), ('s', 85, 30, 42, 86), ('1a', 126, 50, 14, 48), ('0', 140, 58, 16, 36), ('4', 156, 56, 18, 44),
                  ('ch', 188, 44, 56, 64), ('1b', 250, 48, 14, 46), ('4b', 264, 52, 26, 52), ('6', 292, 52, 30, 46),
                  ('1c', 372, 60, 14, 40), ('2', 388, 62, 26, 40), ('7', 418, 60, 22, 44)],
           'X7_140': [('2a', 8, 80, 24, 44), ('7a', 32, 82, 24, 44), ('8', 90, 78, 34, 42), ('5', 122, 82, 28, 38), ('2b', 178, 82, 28, 38),
                      ('9', 206, 84, 28, 46), ('140', 236, 80, 48, 42), ('1', 238, 84, 12, 34), ('mid', 250, 86, 16, 32), ('0', 264, 86, 20, 32),
                      ('1b', 476, 74, 14, 40), ('3', 492, 70, 28, 48), ('7b', 522, 70, 26, 48)],
           'X5': [('s', 10, 42, 36, 80), ('ic', 46, 42, 40, 80), ('h', 86, 42, 46, 90)]}
    tiles = [t for t in tiles if t['w'] * t['h'] >= 300 and t['page'] not in MAN and t['w'] <= 60]
    for pg, bx in MAN.items():
        for k, (nm, x, y, w, h) in enumerate(bx, 1):
            tiles.append(dict(sid=f'{pg}_{k:02d}', page=pg, x=x, y=y, w=w, h=h, cluster=99))
    tiles.sort(key=lambda t: (NAMES.index(t['page']), t['x']))
    for t in tiles: t['sign'] = 'unsorted' if t['cluster'] == 99 else 'shape-%02d' % t['cluster']; t['family'] = t['sign']
    def w(name, keys):
        with open(S / name, 'w') as o:
            o.write('\t'.join(keys) + '\n'); o.writelines('\t'.join(str(t[k]) for k in keys) + '\n' for t in tiles)
    w('signs.tsv', ['sid', 'page', 'x', 'y', 'w', 'h']); w('labels.tsv', ['sid', 'sign', 'family'])
    with open(S / 'focus.tsv', 'w') as o:
        for t in tiles:
            if t['page'] == 'X3' and t['x'] < 260 or t['page'] == 'X7_140' and 230 <= t['x'] <= 290:
                o.write(f"{t['sid']}\tcut from crop {t['page']} (5551 p3, line 2): which sign is this? Pile it with the crops of known words (X1-X2, X4-X6), or make a new pile, or mark a bad cut.\n")

if __name__ == '__main__': main()
