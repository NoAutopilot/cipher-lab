#!/usr/bin/env python3
"""Pixel-level hanging-indent (headword) counter for Vieyra's New Pocket Dictionary page images.

A1B-LIN-PIX, 3 Oct 2026, ciphers/antt-linhares-chave. Second instrument (after the failed hOCR line counter,
hocr_column_count.py) for the two disputed column counts: leaf 95 col 2 rank 19 ("cagar", 283219) and leaf 255
col 3 rank 15 ("justa", 3241315). Pre-registered in NOTES.md, section "Pixel indent counter (A1B-LIN-PIX)".

The unit is the pixel text row, not an OCR line, so OCR line merges cannot hide a headword:
  * columns: x-extent of each column from hocr_column_count.columns()' word-centre borders (hOCR is used only for
    column borders and, in --calibrate/--locate, to find where a known word sits; never for line segmentation);
    hOCR coordinates are scaled to the image (images/book JPEGs are exactly half the 400 dpi hOCR page);
  * the column crop (body only: below the running head, top TOPF of the page) is binarised at Otsu's threshold,
    and in each 120-px vertical window any x inked in over 80% of its rows (a column rule) is blanked;
  * text rows: the crop's row-ink profile, smoothed over 3 px, cut at runs above 4% of the column width; a run
    taller than 1.6x the median run is split at its interior minima into round(h / median) rows;
  * a row's left edge: after skipping up to two leftmost slivers (an ink run <= 3 px wide followed by >= 4 blank
    px: broken, skewed column-rule fragments), the first x where at least 2 ink pixels fall in the row band, in a 2-px window, ignoring
    rows with under MININK ink pixels (specks, rules);
  * a remaining skewed/broken rule at the crop's left (best straight line in its first 20 px, coverage > 35%) is
    blanked +-1 px;
  * margin = a straight line x = a + b*y fitted to the flush cluster (start: 10th percentile; refit 6 times on rows
    within T of the fit), so page skew does not move rows across the threshold; a row is flush-left (a headword)
    iff its left edge <= margin + T (T = 10 px at this scale, half the ~20 px hanging indent measured on the tuning
    leaves 92-94, 96-97, 100-103, which are neither calibration nor target leaves);
  * rank = ordinal of the flush-left row from the top of the column.
Locating a known word (--calibrate / --locate): every hOCR word in that column whose x0 lies within the column's
flush zone (hOCR scale) is scored by SequenceMatcher ratio of its normalised text against the headword; the best
(ratio >= 0.5, unique to within 0.02 of any other row's best) gives a y; the pixel row containing that y gives the
counter's rank. A tie between different rows or ratio < 0.5 is 'unlocated'.
Usage: pixel_indent_count.py HOCR IMGDIR --leaf N --col C [--show]
       pixel_indent_count.py HOCR IMGDIR --calibrate calibration.tsv
       pixel_indent_count.py HOCR IMGDIR --leaf N --col C --locate WORD [WORD ...]
"""
import argparse, glob, os, sys
from difflib import SequenceMatcher
import numpy as np
from PIL import Image
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from hocr_column_count import load_pages, parse, borders, norm

T = 10
TOPF = 0.05
MININK = 12

def otsu(a):
    h = np.bincount(a.ravel(), minlength=256).astype(float)
    p = h / h.sum(); w = np.cumsum(p); mu = np.cumsum(p * np.arange(256)); mt = mu[-1]
    with np.errstate(divide='ignore', invalid='ignore'):
        s = (mt * w - mu) ** 2 / (w * (1 - w))
    return int(np.nanargmax(s))

def col_extents(page, scale):
    W, H, lines = parse(page)
    b = borders(lines, W)
    words = {1: [], 2: [], 3: []}
    for l in lines:
        for w in l:
            c = (w[0] + w[2]) / 2
            words[1 if c < b[0] else 2 if c < b[1] else 3].append(w)
    ext = {}
    for k, ws in words.items():
        ws = [w for w in ws if w[3] > TOPF * H]
        x0s = sorted(w[0] for w in ws); x1s = sorted(w[2] for w in ws)
        lo = x0s[int(0.02 * (len(x0s) - 1))]; hi = x1s[int(0.98 * (len(x1s) - 1))]
        ext[k] = (int(lo * scale) - 8, int(hi * scale) + 2, ws)
    return ext, H

def rows_of(crop):
    th = otsu(crop)
    ink = crop < th
    # vertical column rules (skewed, broken): in each 120-px vertical window, x with ink in > 80% of its rows is blanked
    raw = ink.copy()
    for y in range(0, ink.shape[0], 40):
        w = raw[max(0, y - 40):y + 80]
        ink[y:y + 40, w.mean(0) > 0.8] = False
    # a skewed, broken rule at the column's left: best straight line x = x0 + k*y in the first 20 px; blank +-1 px
    Hc = ink.shape[0]; ys = np.arange(Hc); best = (0, None)
    for k in np.arange(-0.02, 0.0201, 0.002):
        for x0 in range(0, 20):
            xs = np.round(x0 + k * ys).astype(int)
            ok = (xs >= 0) & (xs < ink.shape[1])
            cov = raw[ys[ok], xs[ok]].mean() if ok.any() else 0
            if cov > best[0]:
                best = (cov, xs)
    if best[0] > 0.35:
        for dx in (-1, 0, 1):
            xs = np.clip(best[1] + dx, 0, ink.shape[1] - 1)
            ink[ys, xs] = False
    prof = np.convolve(ink.sum(1), np.ones(3) / 3, 'same')
    on = prof > 0.04 * ink.shape[1]
    runs, y = [], 0
    while y < len(on):
        if on[y]:
            s = y
            while y < len(on) and on[y]:
                y += 1
            if y - s >= 3:
                runs.append((s, y))
        y += 1
    if not runs:
        return [], ink
    med = float(np.median([e - s for s, e in runs]))
    out = []
    for s, e in runs:
        h = e - s
        n = int(round(h / med)) if h > 1.6 * med else 1
        if n <= 1:
            out.append((s, e)); continue
        cuts = [s]
        for i in range(1, n):
            g = s + int(i * h / n); lo, hi = max(s + 2, g - int(med / 2)), min(e - 2, g + int(med / 2))
            cuts.append(lo + int(np.argmin(prof[lo:hi])) if hi > lo else g)
        cuts.append(e)
        out += [(cuts[i], cuts[i + 1]) for i in range(n)]
    return out, ink

def left_edge(ink, s, e):
    band = ink[s:e]
    if band.sum() < MININK:
        return None
    cs = band.sum(0)
    on = cs > 0
    x = 0
    for _ in range(2):  # skip a leftmost sliver (rule fragment): <= 3 px wide, then >= 4 blank px
        xs = np.nonzero(on[x:])[0]
        if not len(xs):
            return None
        a = x + int(xs[0]); b = a
        while b < len(on) and on[b]:
            b += 1
        if b - a <= 3 and not on[b:b + 4].any() and on[b + 4:].any():
            x = b
        else:
            break
    win = np.convolve(cs[x:], np.ones(2), 'valid')
    xs = np.nonzero(win >= 2)[0]
    return x + int(xs[0]) if len(xs) else None

def count(page, img, col):
    a = np.array(Image.open(img).convert('L'))
    W, H, _ = parse(page)
    scale = a.shape[1] / W
    ext, _ = col_extents(page, scale)
    x0, x1, ws = ext[col]
    top = int(TOPF * a.shape[0])
    crop = a[top:, max(0, x0):x1]
    rows, ink = rows_of(crop)
    rs = []
    for s, e in rows:
        le = left_edge(ink, s, e)
        if le is not None:
            rs.append([s + top, e + top, le])
    if not rs:
        return [], scale, ws, x0
    # skew-tolerant margin: a line x = a + b*y fitted to the flush cluster, refitted 6 times
    Y = np.array([(r[0] + r[1]) / 2 for r in rs]); E = np.array([r[2] for r in rs], float)
    fit = np.full(len(rs), np.percentile(E, 10))
    for _ in range(6):
        m = E <= fit + T
        if m.sum() < 3:
            break
        b, a0 = np.polyfit(Y[m], E[m], 1)
        fit = a0 + b * Y
    margin = int(round(fit[0]))
    rank = 0
    for i, r in enumerate(rs):
        r[2] = r[2] - fit[i] + margin  # report edges relative to the fitted margin
        flush = r[2] <= margin + T
        if flush:
            rank += 1
        r += [flush, rank if flush else None, r[2] - margin]
    return rs, scale, ws, x0 + margin

def locate(rs, scale, ws, margin_x, hw):
    """counter rank of the flush row holding the best hOCR match for hw: (rank, ratio, word, row_index) or None."""
    best = {}
    for w in ws:
        if w[0] * scale > margin_x + T + 4:
            continue
        cy = (w[1] + w[3]) / 2 * scale
        ri = next((i for i, r in enumerate(rs) if r[0] - 2 <= cy <= r[1] + 2), None)
        if ri is None:
            continue
        t = norm(w[4])
        q = max(SequenceMatcher(None, norm(hw), c).ratio() for c in (t, t.replace('f', 's')))
        if q > best.get(ri, (0,))[0]:
            best[ri] = (q, w[4])
    if not best:
        return None
    order = sorted(best.items(), key=lambda kv: -kv[1][0])
    ri, (q, word) = order[0]
    if q < 0.5 or (len(order) > 1 and order[1][1][0] >= q - 0.02):
        return ('unlocated', q, word, ri)
    return (rs[ri][4], q, word, ri)

def img_for(d, leaf):
    g = glob.glob(os.path.join(d, '*_leaf%04d_*.jpg' % leaf))
    return g[0] if g else None

def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('hocr'); ap.add_argument('imgdir')
    ap.add_argument('--leaf', type=int); ap.add_argument('--col', type=int)
    ap.add_argument('--show', action='store_true'); ap.add_argument('--locate', nargs='*')
    ap.add_argument('--calibrate')
    a = ap.parse_args()
    if a.calibrate:
        rows = [l.rstrip('\n').split('\t') for l in open(a.calibrate)][1:]
        pages = load_pages(a.hocr, {int(r[3]) for r in rows})
        hit = miss = unloc = 0
        print('src\tgroup\tleaf\tcol\trank\theadword\tcounter_rank\tratio\tocr_word\tverdict')
        for src, grp, page, leaf, col, rank, hw in rows:
            rs, sc, ws, mx = count(pages[int(leaf)], img_for(a.imgdir, int(leaf)), int(col))
            L = locate(rs, sc, ws, mx, hw)
            if L is None or L[0] in ('unlocated', None):
                v = 'unlocated'; unloc += 1
            elif L[0] == int(rank):
                v = 'hit'; hit += 1
            else:
                v = 'MISS'; miss += 1
            print('\t'.join(map(str, [src, grp, leaf, col, rank, hw, L[0] if L else '-', '%.2f' % L[1] if L else '-',
                                      L[2] if L else '-', v])))
        ok = miss == 0 and unloc <= 3
        print('# T %d: hit %d, MISS %d, unlocated %d of %d -> %s' % (T, hit, miss, unloc, len(rows), 'PASS' if ok else 'FAIL'))
        sys.exit(0 if ok else 1)
    page = load_pages(a.hocr, {a.leaf})[a.leaf]
    rs, sc, ws, mx = count(page, img_for(a.imgdir, a.leaf), a.col)
    if a.show:
        for r in rs:
            print('%4d-%4d edge%+4d %s' % (r[0], r[1], r[5], ('rank %d' % r[4]) if r[3] else '   indent'))
    print('# leaf %d col %d: %d rows, %d flush-left' % (a.leaf, a.col, len(rs), sum(1 for r in rs if r[3])))
    for w in a.locate or []:
        print('locate %s -> %s' % (w, locate(rs, sc, ws, mx, w)))

if __name__ == '__main__':
    main()
