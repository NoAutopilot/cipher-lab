#!/usr/bin/env python3
"""Build final row/col-ordered token list for a cryptogram image, splitting any
component whose bbox spans two rows (merged by dilation) at a caller-given y cut.
Assigns a coarse shape-signature (aspect-ratio bucket x fill-density bucket) as an
automatic proxy sign code -- see NOTES.md caveat: single pass, coarse proxy for
true homophone identity."""
import sys, json
import numpy as np
from PIL import Image
from scipy import ndimage

def segment(path, dilate=3, min_area=80, thresh=140):
    im = Image.open(path).convert('L')
    arr = np.array(im)
    ink = arr < thresh
    struct = np.ones((dilate, dilate), dtype=bool)
    closed = ndimage.binary_dilation(ink, structure=struct)
    labeled, n = ndimage.label(closed)
    objs = ndimage.find_objects(labeled)
    comps = []
    for i, sl in enumerate(objs, start=1):
        if sl is None: continue
        ys, xs = sl
        mask = labeled[sl] == i
        area = int(mask.sum())
        if area < min_area: continue
        comps.append({'x0':xs.start,'x1':xs.stop,'y0':ys.start,'y1':ys.stop,
                      'w':xs.stop-xs.start,'h':ys.stop-ys.start,'area':area,
                      'mask':mask})
    return comps, arr.shape

def split_tall(comps, split_y, min_h_to_split=60):
    out = []
    for c in comps:
        if c['h'] >= min_h_to_split and c['y0'] < split_y < c['y1']:
            cut = split_y - c['y0']
            top_mask = c['mask'][:cut, :]
            bot_mask = c['mask'][cut:, :]
            if top_mask.sum() >= 15:
                ys_idx = np.where(top_mask.any(axis=1))[0]
                xs_idx = np.where(top_mask.any(axis=0))[0]
                out.append({'x0':c['x0']+xs_idx.min(),'x1':c['x0']+xs_idx.max()+1,
                            'y0':c['y0'],'y1':c['y0']+cut,
                            'w':xs_idx.max()-xs_idx.min()+1,'h':cut,'area':int(top_mask.sum())})
            if bot_mask.sum() >= 15:
                ys_idx = np.where(bot_mask.any(axis=1))[0]
                xs_idx = np.where(bot_mask.any(axis=0))[0]
                out.append({'x0':c['x0']+xs_idx.min(),'x1':c['x0']+xs_idx.max()+1,
                            'y0':c['y0']+cut,'y1':c['y1'],
                            'w':xs_idx.max()-xs_idx.min()+1,'h':c['y1']-c['y0']-cut,'area':int(bot_mask.sum())})
        else:
            cc = dict(c); cc.pop('mask', None); out.append(cc)
    for o in out:
        o.pop('mask', None)
    return out

def assign_rows(comps, row_bounds):
    for c in comps:
        cy = (c['y0']+c['y1'])/2
        for ri,(a,b) in enumerate(row_bounds):
            if a <= cy < b:
                c['row'] = ri
                break
        else:
            c['row'] = len(row_bounds)-1
    return comps

def shape_code(c):
    ar = c['w']/max(c['h'],1)
    density = c['area']/max(c['w']*c['h'],1)
    ar_b = 'W' if ar>1.35 else ('T' if ar<0.75 else 'S')  # wide/tall/square
    d_b = 'F' if density>0.55 else ('M' if density>0.30 else 'L')  # fill/mid/light
    return f"{ar_b}{d_b}"

if __name__ == '__main__':
    path = sys.argv[1]
    row_bounds = json.loads(sys.argv[2])  # list of [a,b]
    split_y = int(sys.argv[3]) if len(sys.argv) > 3 else None
    comps, shape = segment(path)
    if split_y:
        comps = split_tall(comps, split_y)
    comps = assign_rows(comps, row_bounds)
    comps = [c for c in comps if 0 <= c.get('row',-1) < len(row_bounds)]
    comps.sort(key=lambda c: (c['row'], c['x0']))
    print(f"# {path} image_shape={shape} n_tokens={len(comps)}")
    for idx,c in enumerate(comps):
        code = shape_code(c)
        print(f"{idx}\t{c['row']}\t{c['x0']}\t{c['x1']}\t{c['y0']}\t{c['y1']}\t{c['w']}\t{c['h']}\t{c['area']}\t{code}")
