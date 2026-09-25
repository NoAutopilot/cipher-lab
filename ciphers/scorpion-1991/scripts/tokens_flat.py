#!/usr/bin/env python3
"""Flat raster-order token list (sort by y then x) with coarse shape-signature code."""
import sys
import numpy as np
from PIL import Image
from scipy import ndimage

path = sys.argv[1]
dilate = int(sys.argv[2]) if len(sys.argv) > 2 else 3
min_area = int(sys.argv[3]) if len(sys.argv) > 3 else 80

im = Image.open(path).convert('L')
arr = np.array(im)
ink = arr < 140
struct = np.ones((dilate, dilate), dtype=bool)
closed = ndimage.binary_dilation(ink, structure=struct)
labeled, n = ndimage.label(closed)
objs = ndimage.find_objects(labeled)
comps = []
for i, sl in enumerate(objs, start=1):
    if sl is None: continue
    ys, xs = sl
    area = int((labeled[sl] == i).sum())
    if area < min_area: continue
    comps.append({'x0':xs.start,'x1':xs.stop,'y0':ys.start,'y1':ys.stop,
                  'cx':(xs.start+xs.stop)/2,'cy':(ys.start+ys.stop)/2,
                  'w':xs.stop-xs.start,'h':ys.stop-ys.start,'area':area})

med_h = sorted(c['h'] for c in comps)[len(comps)//2]
row_h = med_h * 1.15
comps.sort(key=lambda c: (round(c['cy']/row_h), c['cx']))

def shape_code(c):
    ar = c['w']/max(c['h'],1)
    density = c['area']/max(c['w']*c['h'],1)
    ar_b = 'W' if ar>1.35 else ('T' if ar<0.75 else 'S')
    d_b = 'F' if density>0.55 else ('M' if density>0.30 else 'L')
    return f"{ar_b}{d_b}"

print(f"# {path} n={len(comps)} med_h={med_h} row_h={row_h:.1f}")
for idx,c in enumerate(comps):
    print(f"{idx}\t{round(c['cy']/row_h)}\t{c['x0']}\t{c['x1']}\t{c['y0']}\t{c['y1']}\t{c['w']}\t{c['h']}\t{c['area']}\t{shape_code(c)}")
