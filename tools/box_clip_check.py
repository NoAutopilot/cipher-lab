#!/usr/bin/env python3
"""Clipped-box check for sign-sorter tiles (BOXCLIP, account 3, 12 Oct 2026). Script only: no model, no network.

Question it answers: does a machine box hold only PART of a sign (a g's tail, a t's top) while ink connected to the sign
runs on outside the box? The owner repairs such boxes by hand with the sorter's "Fix the cut". This tool flags the boxes
whose own ink, read straight off the page image, continues past the edge, and proposes the grown box. It never reads a
label, an owner box or a key; its only inputs are the page image(s) and the machine boxes.

Method, frozen in benchmark-tx/boxclip/PREREG-BOXCLIP.md before it was scored:

  1. Box in image pixels: x0 = floor(x*S), y0 = floor(y*S), x1 = ceil((x+w)*S), y1 = ceil((y+h)*S), clipped to the image
     (S = --scale, image pixels per box unit; 1.0 for a page cut at native size, 0.5 for a half-size copy).
  2. Crop = the box plus a margin of 1.5 x its own width left and right and 1.5 x its own height above and below
     (ceil, clipped to the image).
  3. Ink = pixels darker than the Otsu threshold of the crop after a Gaussian blur of sigma 1.0 px. A crop whose
     1st-99th percentile grey range is under 20 levels has no ink (the threshold would only split noise).
  4. Components = 8-connected ink components of the crop. A component TOUCHES the box when at least one of its pixels
     lies inside it. Components under max(3 px, 2% of the box's pixel area) are ignored (speckle).
  5. Neighbours = the other machine boxes on the same page whose vertical extent overlaps this box's by at least half of
     the shorter of the two heights (the same line, whatever the page's slope). A touching component is IGNORED
     (a neighbour's ink, not this sign's) when it has more pixels inside one single neighbour box than inside this box.
  6. For the kept touching components: total = all their ink in the crop; outside = their ink outside this box and
     outside every neighbour box. The box is FLAGGED CLIPPED when outside >= 25% of total. (A touching component's
     outside ink is by construction joined to its ink inside the box, so the "connected to ink inside" condition is met
     by every touching component.)
  7. GROWN box = the bounding box of the pixels of the kept touching components that have ink outside the box, with the
     pixels that lie in a neighbour box removed first. An unflagged box's grown box is the machine box.

Known limitation (stated, not corrected): a page whose boxes cover only some of its signs (the Modena g/q page boxes
only the descender signs) cannot tell an unboxed neighbouring letter's ink from the sign's own, so rule 5 is blind there.

Usage:
  python3 tools/box_clip_check.py --boxes signs.tsv --pages-dir DIR [--scale 1.0] [--out flags.tsv] [--summary]
  python3 tools/box_clip_check.py --boxes signs.tsv --image PAGE=FILE [--image PAGE=FILE ...] [--scale-page PAGE=0.5]
  --boxes   TSV with sid, page, x, y, w, h (the sorter's signs.tsv)
  --pages-dir  folder with <page>.jpg|.jpeg|.png for every page named in --boxes
  --image / --scale-page  one page image and its own scale, overriding --pages-dir / --scale
  --thr, --margin, --sigma  the registered values are 0.25, 1.5, 1.0; change them only for a sensitivity table
  --out     flags TSV: sid, page, x, y, w, h, flagged, outside_frac, n_comp, gx, gy, gw, gh (grown box, box units)
Offline test: tools/tests/test_box_clip_check.py (synthetic page with known answers).
"""
import argparse
import csv
import math
import os
import sys

import numpy as np
from PIL import Image
from scipy import ndimage as ndi
from skimage.filters import threshold_otsu

PARAMS = dict(margin=1.5, sigma=1.0, thr=0.25, min_pix_abs=3, min_pix_rel=0.02, contrast_floor=20.0, same_line=0.5)
EIGHT = np.ones((3, 3), dtype=int)


def ink_mask(crop, sigma=PARAMS['sigma'], contrast_floor=PARAMS['contrast_floor']):
    """Otsu ink mask of a grey crop after a light Gaussian blur; all False when the crop has no contrast."""
    g = ndi.gaussian_filter(np.asarray(crop, dtype=float), sigma)
    if g.size == 0:
        return np.zeros(g.shape, bool)
    lo, hi = np.percentile(g, 1), np.percentile(g, 99)
    if hi - lo < contrast_floor:
        return np.zeros(g.shape, bool)
    return g < threshold_otsu(g)


def box_px(b, scale, W, H):
    x, y, w, h = b
    x0 = max(0, int(math.floor(x * scale))); y0 = max(0, int(math.floor(y * scale)))
    x1 = min(W, int(math.ceil((x + w) * scale))); y1 = min(H, int(math.ceil((y + h) * scale)))
    return x0, y0, x1, y1


def check_boxes(img, boxes, scale=1.0, **kw):
    """img: 2-D grey array of one page. boxes: list of (sid, x, y, w, h) -- ALL machine boxes of that page (the neighbour
    rule needs them). Returns one dict per box, in order: sid, flagged, outside_frac, n_comp, grown (x, y, w, h in box
    units, the box itself when unflagged)."""
    P = dict(PARAMS); P.update(kw)
    H, W = img.shape
    rects = [box_px(b[1:], scale, W, H) for b in boxes]
    out = []
    for i, (sid, x, y, w, h) in enumerate(boxes):
        x0, y0, x1, y1 = rects[i]
        res = dict(sid=sid, flagged=False, outside_frac=0.0, n_comp=0, grown=(x, y, w, h))
        if x1 <= x0 or y1 <= y0:
            out.append(res); continue
        mx = int(math.ceil(P['margin'] * (x1 - x0))); my = int(math.ceil(P['margin'] * (y1 - y0)))
        cx0, cy0 = max(0, x0 - mx), max(0, y0 - my)
        cx1, cy1 = min(W, x1 + mx), min(H, y1 + my)
        mask = ink_mask(img[cy0:cy1, cx0:cx1], P['sigma'], P['contrast_floor'])
        if not mask.any():
            out.append(res); continue
        lab, n = ndi.label(mask, structure=EIGHT)
        area = np.bincount(lab[mask], minlength=n + 1)
        inb = np.zeros(mask.shape, bool); inb[y0 - cy0:y1 - cy0, x0 - cx0:x1 - cx0] = True
        in_c = np.bincount(lab[inb & mask], minlength=n + 1)
        nbu = np.zeros(mask.shape, bool)
        other = np.zeros(n + 1, dtype=int)
        for j, (ax0, ay0, ax1, ay1) in enumerate(rects):
            if j == i or ax1 <= ax0 or ay1 <= ay0:
                continue
            ov = min(y1, ay1) - max(y0, ay0)
            if ov < P['same_line'] * min(y1 - y0, ay1 - ay0):
                continue
            sx0, sy0 = max(ax0, cx0) - cx0, max(ay0, cy0) - cy0
            sx1, sy1 = min(ax1, cx1) - cx0, min(ay1, cy1) - cy0
            if sx1 <= sx0 or sy1 <= sy0:
                continue
            m = np.zeros(mask.shape, bool); m[sy0:sy1, sx0:sx1] = True
            other = np.maximum(other, np.bincount(lab[m & mask], minlength=n + 1))
            nbu |= m
        nbu &= ~inb
        nb_c = np.bincount(lab[nbu & mask], minlength=n + 1)
        min_pix = max(P['min_pix_abs'], int(round(P['min_pix_rel'] * (x1 - x0) * (y1 - y0))))
        keep = (in_c > 0) & (area >= min_pix) & ~(other > in_c)
        keep[0] = False
        res['n_comp'] = int(keep.sum())
        tot = int(area[keep].sum())
        if tot == 0:
            out.append(res); continue
        far_c = area - in_c - nb_c
        far = int(far_c[keep].sum())
        res['outside_frac'] = far / tot
        if res['outside_frac'] >= P['thr'] and far > 0:
            cross = keep & (far_c > 0)
            sel = cross[lab] & mask & ~nbu
            ys, xs = np.nonzero(sel)
            gx0, gx1 = cx0 + xs.min(), cx0 + xs.max() + 1
            gy0, gy1 = cy0 + ys.min(), cy0 + ys.max() + 1
            res['flagged'] = True
            res['grown'] = (int(round(gx0 / scale)), int(round(gy0 / scale)),
                            int(round((gx1 - gx0) / scale)), int(round((gy1 - gy0) / scale)))
        out.append(res)
    return out


def load_grey(path):
    return np.asarray(Image.open(path).convert('L'))


def find_page(pages_dir, page):
    for ext in ('.jpg', '.jpeg', '.png', '.JPG', '.PNG'):
        p = os.path.join(pages_dir, page + ext)
        if os.path.exists(p):
            return p
    return None


def run(rows, images, scales, **kw):
    """rows: dicts with sid, page, x, y, w, h (strings or numbers). images: page -> grey array. scales: page -> scale.
    Returns flag rows in input order."""
    by_page = {}
    for k, r in enumerate(rows):
        by_page.setdefault(r['page'], []).append(k)
    res = [None] * len(rows)
    for page, idx in by_page.items():
        boxes = [(rows[k]['sid'], *[float(rows[k][c]) for c in 'xywh']) for k in idx]
        got = check_boxes(images[page], boxes, scales.get(page, 1.0), **kw)
        for k, g in zip(idx, got):
            res[k] = g
    return res


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.split('\n')[0], formatter_class=argparse.RawDescriptionHelpFormatter,
                                 epilog=__doc__)
    ap.add_argument('--boxes', required=True)
    ap.add_argument('--pages-dir')
    ap.add_argument('--image', action='append', default=[], metavar='PAGE=FILE')
    ap.add_argument('--scale', type=float, default=1.0)
    ap.add_argument('--scale-page', action='append', default=[], metavar='PAGE=S')
    ap.add_argument('--thr', type=float, default=PARAMS['thr'])
    ap.add_argument('--margin', type=float, default=PARAMS['margin'])
    ap.add_argument('--sigma', type=float, default=PARAMS['sigma'])
    ap.add_argument('--out')
    ap.add_argument('--summary', action='store_true')
    a = ap.parse_args(argv)
    with open(a.boxes, newline='') as f:
        rows = list(csv.DictReader(f, delimiter='\t'))
    files = dict(s.split('=', 1) for s in a.image)
    scales = {p: a.scale for p in {r['page'] for r in rows}}
    scales.update({k: float(v) for k, v in (s.split('=', 1) for s in a.scale_page)})
    images = {}
    for page in scales:
        path = files.get(page) or (find_page(a.pages_dir, page) if a.pages_dir else None)
        if not path or not os.path.exists(path):
            sys.exit('no image for page %s (give --pages-dir or --image %s=FILE)' % (page, page))
        images[page] = load_grey(path)
    res = run(rows, images, scales, thr=a.thr, margin=a.margin, sigma=a.sigma)
    if a.out:
        with open(a.out, 'w', newline='') as f:
            w = csv.writer(f, delimiter='\t', lineterminator='\n')
            w.writerow(['sid', 'page', 'x', 'y', 'w', 'h', 'flagged', 'outside_frac', 'n_comp', 'gx', 'gy', 'gw', 'gh'])
            for r, g in zip(rows, res):
                w.writerow([r['sid'], r['page'], r['x'], r['y'], r['w'], r['h'], int(g['flagged']),
                            '%.3f' % g['outside_frac'], g['n_comp'], *g['grown']])
    if a.summary or not a.out:
        pages = sorted({r['page'] for r in rows})
        for p in pages:
            gs = [g for r, g in zip(rows, res) if r['page'] == p]
            print('%s: %d of %d boxes flagged clipped' % (p, sum(g['flagged'] for g in gs), len(gs)))
    return 0


if __name__ == '__main__':
    sys.exit(main())
