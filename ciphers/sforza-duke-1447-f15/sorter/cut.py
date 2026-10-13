#!/usr/bin/env python3
"""SFZ-SORT (13 Oct 2026): blind sign-sorter inputs for the Duke's two glossed 1447 slips, BnF italien 1584 f.5 and f.8
(../sforza-italien1584-1447/duke/), the alphabet-settling step SFZ-DUKE (8 Oct) named after the second machine reader was retired.

Source: the two native Gallica regions already on disk (no network; the manifest ../sforza-italien1584-1447/duke/images/
manifest.json names their URLs): f.5 = canvas 9 region 4000,2280,3420,1300; f.8 = canvas 11 region 4000,860,3120,1450.
The two regions are stacked into one composite (f.5 above f.8, f.8 padded white to the same width), written to
sorter/region.jpg (untracked; this script regenerates it).
Lines: the row-ink peaks of three 700 px windows (left, middle, right) per slip give each line's centre at three x positions;
a quadratic through them is the trace (the slips slope). f.5's left window also picks up the modern dateline note above
line 1 ("1447 10 janvier"), so its first left peak is dropped: 15 cipher lines on f.5, 16 on f.8.
Tiles: tools/sorter_recut.py (deskewed strips, one tile per ink group). No reader columns are passed: the starting piles are the
shape clusters only (k-means on the tile bitmaps), named shape-NN -- value-blind, no reader label, no key, no decode.
Focus: sorter_recut's own pick (frequent shapes first, at most two tiles per cluster). The check after the sort is the
dateline run (f.8 L15-16, f.5 L14-15), read twice identically by SFZ-DUKE; it is not marked on the page.
  python3 ciphers/sforza-duke-1447-f15/sorter/cut.py      (repo root; writes sorter/signs.tsv, labels.tsv, clusters.tsv,
                                                           focus.tsv, fit_recut.tsv, region.json, cipher_lines.tsv; pages/,
                                                           debug/ and region.jpg are untracked)
"""
import sys
from pathlib import Path
import numpy as np
from PIL import Image
from scipy import ndimage as ndi
from scipy.signal import find_peaks
S = Path(__file__).resolve().parent; R = S.parents[2]
sys.path.insert(0, str(R / 'tools'))
import sorter_recut as sr
D = R / 'ciphers' / 'sforza-italien1584-1447' / 'duke' / 'images'
SRC = [('f5', 'src_ark_12148_btv1b100373864_f9_4000_2280_3420_1300.jpg', 1),     # drop the first left peak (dateline note)
       ('f8', 'src_ark_12148_btv1b100373864_f11_4000_860_3120_1450.jpg', 0)]
PAD = 2
CFG = sr.Cfg(pitch=75, half=62, xmin=60, rel=0.72, own=0.5, core=0.3, nclu=40, per_clu=2, nfocus=40, minpix=25, recentre=25,
             split=1.25, jpeg=80)


def peaks(ink, x0, x1):
    pr = np.convolve(ink[:, x0:x1].sum(1), np.ones(25) / 25, 'same')
    return find_peaks(pr, distance=50, prominence=pr.max() * 0.15)[0]


def main():
    greys = [np.array(Image.open(D / f).convert('L')) for _, f, _ in SRC]
    W = max(g.shape[1] for g in greys)
    parts, traces, names, y0 = [], [], [], 0
    for (slip, _, drop), g in zip(SRC, greys):
        h, w = g.shape
        ink = g < 0.72 * (ndi.grey_closing(g.astype(float), size=(31, 31)) + 1)
        xs = [600, w // 2, w - 600]
        ps = [peaks(ink, x - 350, x + 350) for x in xs]
        ps[0] = ps[0][drop:]
        n = min(len(p) for p in ps); assert all(len(p) == n for p in ps), [len(p) for p in ps]
        for i in range(n):
            c = np.polyfit(xs, [p[i] for p in ps], 2)
            tr = np.polyval(c, np.arange(W)) + y0
            traces.append(tr); names.append(f'{slip}_L{i + 1:02d}')
        pad = np.full((h, W), 255, np.uint8); pad[:, :w] = g; parts.append(pad); y0 += h
    grey = np.vstack(parts); Image.fromarray(grey).save(S / 'region.jpg', quality=85)
    tiles, _ = sr.run(grey, traces, names, [[] for _ in names], [[] for _ in names], S, S / 'pages', CFG,
                      fallback=['unsorted'] * len(names), debug=str(S / 'debug'),
                      region_image=str((S / 'region.jpg').relative_to(R)))
    # rename the starting piles to value-blind shape names (sorter_recut leaves every unaligned tile in the fallback pile)
    import csv
    # a 2 px margin round every box: a tight box on a dot or a bar is nearly all ink (preflight's 3-60% ink check; 191 -> 7 tiles)
    rows = list(csv.DictReader(open(S / 'signs.tsv'), delimiter='\t'))
    with open(S / 'signs.tsv', 'w') as o:
        o.write('sid\tpage\tx\ty\tw\th\n')
        for r in rows:
            x, y, w, h = (int(r[k]) for k in 'xywh'); x0, y0 = max(0, x - PAD), max(0, y - PAD)
            x1, y1 = min(W, x + w + PAD), min(2 * CFG.half + 1, y + h + PAD)
            o.write(f"{r['sid']}\t{r['page']}\t{x0}\t{y0}\t{x1 - x0}\t{y1 - y0}\n")
    cl ={r['sid']: int(r['cluster']) for r in csv.DictReader(open(S / 'clusters.tsv'), delimiter='\t')}
    with open(S / 'labels.tsv', 'w') as o:
        o.write('sid\tsign\tfamily\n')
        for sid in cl:
            o.write(f'{sid}\tshape-{cl[sid]:02d}\tshape-{cl[sid]:02d}\n')
    fo = [l.split('\t', 1)[0] for l in open(S / 'focus.tsv') if l.strip()]
    with open(S / 'focus.tsv', 'w') as o:
        for sid in fo:
            o.write(f"{sid}\tf.{sid.split('_')[0][1:]} line {int(sid.split('_')[1][1:])}: started in shape-{cl[sid]:02d} by shape alone. "
                    f"Right pile, another sign, or a bad cut?\n")
    with open(S / 'cipher_lines.tsv', 'w') as o:
        o.writelines(f'{p}\n' for p in names)
    print(len(cl), 'tiles,', len(names), 'lines,', len(fo), 'focus')


if __name__ == '__main__':
    main()
