#!/usr/bin/env python3
"""Connected-component sign segmentation for a Scorpion cryptogram scan.
Usage: python3 segment.py IMAGE.jpg [--dilate N] [--min-area N]
Thresholds to binary ink, does a morphological closing to merge multi-stroke
glyphs (dilate N), labels connected components, drops specks under --min-area,
clusters components into text rows by y-centroid, sorts each row left to right,
and prints one row per cryptogram line with component bounding boxes.
"""
import sys, numpy as np
from PIL import Image
from scipy import ndimage

def main():
    path = sys.argv[1]
    dilate = 3
    min_area = 15
    if '--dilate' in sys.argv:
        dilate = int(sys.argv[sys.argv.index('--dilate')+1])
    if '--min-area' in sys.argv:
        min_area = int(sys.argv[sys.argv.index('--min-area')+1])

    im = Image.open(path).convert('L')
    arr = np.array(im)
    # ink = dark pixels
    thresh = 140
    ink = arr < thresh

    struct = np.ones((dilate, dilate), dtype=bool)
    closed = ndimage.binary_dilation(ink, structure=struct)

    labeled, n = ndimage.label(closed)
    objs = ndimage.find_objects(labeled)
    comps = []
    for i, sl in enumerate(objs, start=1):
        if sl is None:
            continue
        ys, xs = sl
        area = (labeled[sl] == i).sum()
        if area < min_area:
            continue
        cy = (ys.start + ys.stop) / 2
        cx = (xs.start + xs.stop) / 2
        comps.append({
            'id': i, 'y0': ys.start, 'y1': ys.stop, 'x0': xs.start, 'x1': xs.stop,
            'cy': cy, 'cx': cx, 'area': int(area), 'h': ys.stop-ys.start, 'w': xs.stop-xs.start
        })

    comps.sort(key=lambda c: c['cy'])
    # cluster rows by cy gap
    rows = []
    cur = []
    last_cy = None
    row_gap = None
    heights = [c['h'] for c in comps]
    med_h = sorted(heights)[len(heights)//2] if heights else 20
    for c in comps:
        if last_cy is None or (c['cy'] - last_cy) < med_h * 0.8:
            cur.append(c)
        else:
            rows.append(cur)
            cur = [c]
        last_cy = c['cy']
    if cur:
        rows.append(cur)

    print(f"image={path} size={im.size} n_components={len(comps)} n_rows={len(rows)} median_h={med_h}")
    total = 0
    for ri, row in enumerate(rows, start=1):
        row.sort(key=lambda c: c['cx'])
        total += len(row)
        print(f"-- row {ri}: {len(row)} signs --")
        for c in row:
            print(f"  id={c['id']:4d} x=[{c['x0']:4d},{c['x1']:4d}) y=[{c['y0']:4d},{c['y1']:4d}) w={c['w']:3d} h={c['h']:3d} area={c['area']:4d}")
    print(f"TOTAL signs = {total}")

if __name__ == '__main__':
    main()
