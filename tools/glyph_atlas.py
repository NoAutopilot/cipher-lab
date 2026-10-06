#!/usr/bin/env python3
"""Segment the signs of invented-alphabet cipher pages, cluster them by shape, and publish one atlas.

  python3 tools/glyph_atlas.py segment --page NAME=IMAGE[@x0,y0,x1,y1] [--page ...] --out DIR [--debug]
  python3 tools/glyph_atlas.py cluster --out DIR [--k 60] [--k-marks 16]
  python3 tools/glyph_atlas.py atlas --out DIR --labels labels.json [--per 10] [--prefer PAGE]
  python3 tools/glyph_atlas.py atlas --out DIR --from-truth TOKENS.tsv --per 6 --spread --exclude-leaf PAGE [--canonical SHEET.png]
  python3 tools/glyph_atlas.py classify --out DIR --labels labels.json --page PAGE --tsv boxes.tsv [--exclude-page] [--strips DIR2]
  python3 tools/glyph_atlas.py crop --image PAGE.jpg --box x0,y0,x1,y1[:label] [--box ...] --dest DIR [--scale 4]
  python3 tools/glyph_atlas.py crop --out DIR --sid ID [--sid ...] --dest DIR2 [--scale 4]

Generalises ciphers/dupuy452-carpi-1520/glyphs/ (segment.py, cluster.py, montage.py: page-specific there) for any
page set, and adds what a mixed page needs (fr.2933 Salviati 1525): small marks written ABOVE a sign (tilde, #,
ring, dots, cross, small superscript numbers) are kept as an attribute of the sign below, not as signs of their own.

segment  Per page: background-normalised binarisation (grey closing divides out the paper), 8-connected components,
         line centres from the row ink profile (pitch by autocorrelation), and per line:
         - components whose x-ranges overlap by more than half of the narrower one are merged (a sign in two strokes);
         - a component whose height is under --mark-h x the page's median sign height and whose bottom sits above
           the line centre is a MARK, attached to the base sign below it with the most x-overlap (nearest centre if none).
         Scale-free: every threshold is in units of the page's median component height, so native crops and 1600 px
         reference copies can share one atlas. Writes DIR/signs.tsv, DIR/marks.tsv, DIR/bitmaps.npz (48x48, aspect
         kept), DIR/crops/<page>.png (the grey page, for exemplars) and with --debug DIR/debug_<page>.jpg.
         --cursive (RUN1-SEG, 4 Oct 2026, rah-juan-manuel-1521 DECODE hand): for a joined 16th-c. cursive hand with
         verso bleed-through, where the default mode returns stroke fragments (R9528 f.194: 3,240 "signs" of median
         height 4 px). Each --page is ONE line strip (a tools/iiif_lines.py crop); a page taller than --strip-max x its
         own x-height is first cut into bands at line_centres and each band treated as a strip. Per strip:
         1. ghost floor: binarise at --rel, then keep a component only if its darkest pixels (the --dark-q quantile of
            its background-normalised grey) are under --ghost; bleed-through from the verso is ink seen through paper,
            lighter than any written stroke, so it fails this test even when the binarisation keeps it;
            pixels of a kept component lighter than --ghost-px are dropped too (ghost ink that touches a real stroke);
         2. x-height xh = the height of the core band, the contiguous rows round the row-profile peak (ghost-filtered
            ink, 3-row smoothing; the peak is sought in the middle half of the strip, where a line crop centres its
            own line) carrying at least --core x the peak; every threshold below is in units of xh;
         3. ink outside the core band +- --band x xh is cleared (neighbour lines' tails clipped into the strip), and
            components whose longer side is under --min-side x xh are dropped;
         4. sign candidates are runs of columns carrying ink inside the core band, runs closer than --gap x xh joined
            (flourishes above and below the x-height zone do not bridge words); a box is the run's columns over the
            rows that carry kept ink;
         5. a group wider than --split-w x xh (two joined code words) is split into round(width / (--piece x xh))
            pieces at the column-ink minima nearest the equal-width cut points (+-0.35 piece).
         Output columns are the default mode's; rh/rw/dy are in units of xh, line is the band (1 for a strip), and
         pages.json records median_h = xh. Marks are not separated (cursive superscripts stay with their group).
         Offline test: tools/tests/test_glyph_atlas.py (synthetic joined line with a faint mirrored ghost).
         --median-h PX|pool (R10-FLOR2, 6 Oct 2026; default mode only): every page uses one shared median sign height
         instead of its own, so a line crop whose components are mostly specks (own median 4 px against ~50 on the
         leaf) is cut at the leaf's scale; "pool" takes the median of the pages' own medians. pages.json then records
         the shared value. Catches: a speck-dominated crop of a leaf whose other crops share one scale. Must NOT change:
         a page whose own median already equals the shared value (identical boxes). Offline test: test_glyph_atlas.py.
cluster  HOG (9 orientations, 8x8 cells, 2x2 blocks) of the bitmaps plus log relative height and width, PCA(40),
         k-means with a deliberate over-split (fixed seed), as carpi cluster.py; marks clustered separately.
         --split s52:3 re-splits a mixed cluster (labels 52.0 52.1 52.2). Writes DIR/clusters.tsv and DIR/sheet_signs_NN.png / sheet_marks.png contact sheets (row label "k:count").
atlas    --from-truth TOKENS.tsv [--per 6 --spread --exclude-leaf PAGE ... --codes @FILE --canonical SHEET.png --grid 110x110x9]
         (TX-SHEET, 4 Oct 2026; research/TRANSCRIPTION-PRACTICE-2026-10-04.md #4, the palaeographer's alphabet): a per-hand
         exemplar sheet for line-read passes. TOKENS.tsv names securely read boxes (sid, code, optional grade; --grades
         filters). Per code, --per tiles from those boxes, never from an --exclude-leaf page (the eval item): with --spread
         the medoid then farthest-point picks over the classify features (allographs, cramped and wide forms), else the
         nearest the mean; --trim (0.2) first drops the farthest share of each code's tiles (mis-reads, mis-alignments). Each row: the code, the canonical print shape (--canonical, if given), then the hand's tiles;
         a code with fewer than --min-secure secure tiles keeps the print shape only. --rows-per-sheet codes per image
         (one subagent call each): DIR/<prefix>_NN.png plus <prefix>.tsv (code, n_secure, shown, exemplar sids).
         Page images come from crops/ or, when that gitignored copy is gone, from pages.json.
atlas    labels.json {"signs": {"<cluster>": "CODE"|"_"}, "marks": {"<cluster>": "MARK"|"_"},
                      "desc": {"CODE": "short description"}}; "_" = not a cipher sign (plain letters, noise).
         Writes DIR/atlas.tsv (code, desc, count, pages, exemplar sign ids, attribute marks seen) and DIR/atlas.png:
         one row per code, the code and its count, then --per exemplars cut from the grey page with context margin.

crop     Cut one or more individual glyph crops for an atlas or a by-eye dispute (no clustering pipeline needed).
         --image mode: pixel boxes straight out of any plain image on disk (a full DigitArq/Gallica page,
         no `segment` run required first). --out/--sid mode: reuses a prior `segment` run's own signs.tsv/
         marks.tsv box positions instead of hand-picked pixel coordinates. Either way, each crop gets a fixed
         context margin, is upscaled (--scale, default 4x cubic) for a small secretary-hand glyph, and is
         written as one PNG per box under --dest (named by the box's label/sid, or IMAGE_x0-y0-x1-y1.png).
classify Every box of one page against the labelled boxes of ALL pages (the atlas, labels.json incl. "override"):
         same features as cluster, k nearest labelled boxes (--knn 5, the box itself excluded), distance-weighted vote.
         '_' (plain script, noise) is a class like any code. Writes one row per box in reading order: line, box id, bbox,
         script code, d1 (nearest distance), vote share, the cluster's own code, marks above (their codes, '?' for an
         unlabelled mark, joined by '|'). --strips DIR2 renders one image per line (cut in parts under --max-w px) with
         each box outlined and its position number printed under it, for passes that confirm or correct each box.
         A script-counted box list removes the "one pass has a sign the other lacks" disagreements (fr.2933, 24 Sept).
         --exclude-page: a NEW, unlabelled page must not vote with its own boxes (they are each other's nearest
         neighbours and all vote '_'); with the flag only other pages' boxes are candidates (debosnys c4, 25 Sept 2026).
         --topk 3 (TRANSCRIPTION.md step 5, TX-ATLAS-B72 3 Oct 2026) adds k1 d1 s1 .. k3 d3 s3: the three best codes, each
         with the distance to its nearest labelled box and its vote share among the --knn voters; codes outside the
         voters are ranked after them by nearest distance in a wider pool (--pool 40), share 0. This is the lattice a
         key-constrained decode reads. --holdout PREFIX (repeatable): boxes whose id starts with PREFIX never vote and
         their cluster code is not used for them (a held-out known-answer line scored against an atlas named without it).
         --page all classifies every page into one TSV (a 'page' column is added).
Test: python3 tools/tests/test_glyph_atlas.py (offline: a synthetic page with two sign shapes, one carrying a mark).
"""
import argparse, collections, csv, json, os, sys

import numpy as np

try:
    import cv2
    from skimage.feature import hog
    from sklearn.cluster import KMeans
    from sklearn.decomposition import PCA
    from sklearn.preprocessing import StandardScaler
    from PIL import Image
except ImportError as e:  # pragma: no cover
    sys.exit(f'needs opencv-python-headless scikit-image scikit-learn pillow ({e})')

Image.MAX_IMAGE_PIXELS = None
SEED = 20260924
BM = 48


def binarise(grey, rel=0.78):
    k = max(15, int(min(grey.shape) / 40) | 1)
    bg = cv2.morphologyEx(grey, cv2.MORPH_CLOSE, np.ones((k, k), np.uint8))
    bg = cv2.GaussianBlur(bg, (0, 0), k / 3)
    norm = grey.astype(float) / np.maximum(bg.astype(float), 1)
    return (norm < rel).astype(np.uint8)


def line_centres(ink, mh):
    from scipy.ndimage import uniform_filter1d
    from scipy.signal import find_peaks
    prof = uniform_filter1d(ink.sum(axis=1).astype(float), max(3, int(mh / 2)))
    p = prof - prof.mean()
    ac = np.correlate(p, p, 'full')[len(p) - 1:]
    lo = int(2 * mh)
    pitch = lo + int(np.argmax(ac[lo:int(8 * mh)])) if len(ac) > 8 * mh else int(4 * mh)
    peaks, _ = find_peaks(prof, distance=max(3, int(0.7 * pitch)), prominence=prof.max() * 0.08)
    return peaks, pitch


def bitmap(mask):
    h, w = mask.shape
    s = max(h, w)
    can = np.zeros((s, s), np.uint8)
    can[(s - h) // 2:(s - h) // 2 + h, (s - w) // 2:(s - w) // 2 + w] = mask * 255
    return cv2.resize(can, (BM, BM), interpolation=cv2.INTER_AREA)


def segment_page(name, path, box, a):
    grey = np.array(Image.open(path).convert('L'))
    if box:
        x0, y0, x1, y1 = box
        grey = grey[y0:y1, x0:x1]
    ink = binarise(grey, a.rel)
    ink = cv2.morphologyEx(ink, cv2.MORPH_OPEN, np.ones((2, 2), np.uint8)) if min(grey.shape) > 2500 else ink
    n, lab, st, cen = cv2.connectedComponentsWithStats(ink, connectivity=8)
    areas = st[1:, 4]
    big = st[1:][areas >= np.percentile(areas, 60)]
    mh = float(np.median(big[:, 3])) if len(big) else 20.0
    if getattr(a, 'shared_mh', None):
        mh = a.shared_mh   # --median-h: one scale for every page (a speck-dominated crop's own median collapses)
    keep = [i for i in range(1, n) if st[i, 4] >= max(4, (a.min_area * mh) ** 2)
            and st[i, 3] <= 3.5 * mh and st[i, 2] <= 5 * mh]
    kept = np.zeros_like(ink)
    for i in keep:
        kept[lab == i] = 1
    peaks, pitch = line_centres(kept, mh)
    if not len(peaks):
        return [], [], grey, mh
    comps = collections.defaultdict(list)
    for i in keep:
        x, y, w, h, ar = st[i]
        li = int(np.argmin(np.abs(peaks - cen[i][1])))
        comps[li].append(dict(x=x, y=y, w=w, h=h, ids=[i]))
    signs, marks = [], []
    for li in sorted(comps):
        lc = peaks[li]
        cs = comps[li]
        is_mark = lambda c: c['h'] < a.mark_h * mh and c['w'] < 1.5 * mh and c['y'] + c['h'] < lc - a.mark_above * mh
        base = sorted([c for c in cs if not is_mark(c)], key=lambda c: c['x'])
        mk = [c for c in cs if is_mark(c)]
        merged = []
        for c in base:
            if merged:
                p = merged[-1]
                ov = min(p['x'] + p['w'], c['x'] + c['w']) - max(p['x'], c['x'])
                vgap = max(0, c['y'] - (p['y'] + p['h']), p['y'] - (c['y'] + c['h']))
                if ov > 0.5 * min(p['w'], c['w']) and vgap <= a.merge_vgap * mh:
                    x0_, y0_ = min(p['x'], c['x']), min(p['y'], c['y'])
                    p.update(x=x0_, y=y0_, w=max(p['x'] + p['w'], c['x'] + c['w']) - x0_,
                             h=max(p['y'] + p['h'], c['y'] + c['h']) - y0_, ids=p['ids'] + c['ids'])
                    continue
            merged.append(dict(c))
        merged = [c for c in merged if c['h'] >= 0.3 * mh or c['w'] >= 0.6 * mh]  # specks, dots of i
        for k, c in enumerate(merged):
            sub = np.isin(lab[c['y']:c['y'] + c['h'], c['x']:c['x'] + c['w']], c['ids']).astype(np.uint8)
            signs.append(dict(sid=f'{name}_{li + 1:02d}_{k + 1:03d}', page=name, line=li + 1, pos=k + 1,
                              x=c['x'], y=c['y'], w=c['w'], h=c['h'], rh=c['h'] / mh, rw=c['w'] / mh,
                              dy=(c['y'] + c['h'] / 2 - lc) / mh, marks='', bm=bitmap(sub)))
        line_signs = signs[len(signs) - len(merged):]
        for m in mk:
            mx = m['x'] + m['w'] / 2
            best, bov = None, 0
            for s in line_signs:
                ov = min(s['x'] + s['w'], m['x'] + m['w']) - max(s['x'], m['x'])
                if ov > bov:
                    best, bov = s, ov
            if best is None and line_signs:
                best = min(line_signs, key=lambda s: abs(s['x'] + s['w'] / 2 - mx))
            sub = np.isin(lab[m['y']:m['y'] + m['h'], m['x']:m['x'] + m['w']], m['ids']).astype(np.uint8)
            mid = f'{name}_{li + 1:02d}_m{len(marks) + 1:04d}'
            marks.append(dict(mid=mid, page=name, line=li + 1, x=m['x'], y=m['y'], w=m['w'], h=m['h'],
                              rh=m['h'] / mh, rw=m['w'] / mh, sid=best['sid'] if best else '', bm=bitmap(sub)))
            if best:
                best['marks'] += ('|' if best['marks'] else '') + mid
    if a.debug:
        d = cv2.cvtColor(grey, cv2.COLOR_GRAY2BGR)
        t = max(1, int(mh / 12))
        for s in signs:
            cv2.rectangle(d, (s['x'], s['y']), (s['x'] + s['w'], s['y'] + s['h']), (0, 0, 255), t)
        for m in marks:
            cv2.rectangle(d, (m['x'], m['y']), (m['x'] + m['w'], m['y'] + m['h']), (255, 0, 0), t)
        for p in peaks:
            cv2.line(d, (0, int(p)), (d.shape[1], int(p)), (0, 160, 0), t)
        sc = 1600 / d.shape[1]
        cv2.imwrite(os.path.join(a.out, f'debug_{name}.jpg'), cv2.resize(d, None, fx=sc, fy=sc))
    return signs, marks, grey, mh


def _cursive_strip(name, grey, norm, ink, li, yoff, a):
    """One line strip of a joined cursive hand -> sign-candidate boxes (see --cursive in the module docstring)."""
    n, lab, st, _ = cv2.connectedComponentsWithStats(ink, connectivity=8)
    keep = []
    for i in range(1, n):
        if st[i, 4] < 4:
            continue
        x, y, w, h, _ = st[i]
        vals = norm[y:y + h, x:x + w][lab[y:y + h, x:x + w] == i]
        if np.quantile(vals, a.dark_q) < a.ghost:
            keep.append(i)
    if not keep:
        return [], 0.0
    kept = np.isin(lab, keep) & (norm < a.ghost_px)
    prof = kept.sum(axis=1).astype(float)
    from scipy.ndimage import uniform_filter1d
    prof = uniform_filter1d(prof, 3)
    q = len(prof) // 4          # the strip's own line is centred in it (iiif_lines); neighbours' edges lie outside
    pk = q + int(np.argmax(prof[q:len(prof) - q])) if len(prof) >= 8 else int(np.argmax(prof))
    lo = hi = pk
    while lo > 0 and prof[lo - 1] >= a.core * prof[pk]:
        lo -= 1
    while hi < len(prof) - 1 and prof[hi + 1] >= a.core * prof[pk]:
        hi += 1
    xh = float(max(3, hi - lo + 1))
    b0, b1 = max(0, int(lo - a.band * xh)), min(len(prof), int(hi + a.band * xh) + 1)
    small = [i for i in keep if max(st[i, 2], st[i, 3]) < a.min_side * xh]
    if small:
        kept[np.isin(lab, small)] = False
    kept[:b0] = False
    kept[b1:] = False
    # sign candidates are runs of columns with ink inside the core band; a gap under --gap x xh does not separate
    col = kept[lo:hi + 1].any(axis=0)
    runs, u = [], None
    for x_ in range(len(col) + 1):
        on = x_ < len(col) and col[x_]
        if on and u is None:
            u = x_
        elif not on and u is not None:
            if runs and u - runs[-1][1] < a.gap * xh:
                runs[-1][1] = x_
            else:
                runs.append([u, x_])
            u = None
    groups = []
    for u, v in runs:
        rows = np.where(kept[:, u:v].any(axis=1))[0]
        groups.append(dict(x=u, y=int(rows[0]), w=v - u, h=int(rows[-1] - rows[0] + 1)))
    med = a.piece * xh
    out = []
    for g in groups:
        sub = kept[g['y']:g['y'] + g['h'], g['x']:g['x'] + g['w']].astype(np.uint8)
        if g['w'] > a.split_w * xh:
            k = max(2, int(round(g['w'] / med)))
            col = sub.sum(axis=0).astype(float)
            cuts, step = [0], g['w'] / k
            for j in range(1, k):
                c0 = int(j * step - 0.35 * step)
                c1 = int(j * step + 0.35 * step)
                c0, c1 = max(cuts[-1] + 1, c0), min(g['w'] - 1, c1)
                if c1 <= c0:
                    continue
                cuts.append(c0 + int(np.argmin(col[c0:c1])))
            cuts.append(g['w'])
            for u, v in zip(cuts, cuts[1:]):
                piece = sub[:, u:v]
                rows = np.where(piece.any(axis=1))[0]
                if not len(rows):
                    continue
                out.append(dict(x=g['x'] + u, y=g['y'] + int(rows[0]), w=v - u, h=int(rows[-1] - rows[0] + 1),
                                bm=piece[rows[0]:rows[-1] + 1]))
        else:
            out.append(dict(x=g['x'], y=g['y'], w=g['w'], h=g['h'], bm=sub))
    lc = (lo + hi) / 2
    signs = []
    for k, c in enumerate(out):
        signs.append(dict(sid=f'{name}_{li + 1:02d}_{k + 1:03d}', page=name, line=li + 1, pos=k + 1,
                          x=c['x'], y=c['y'] + yoff, w=c['w'], h=c['h'], rh=c['h'] / xh, rw=c['w'] / xh,
                          dy=(c['y'] + c['h'] / 2 - lc) / xh, marks='', bm=bitmap(c['bm'])))
    return signs, xh


def segment_cursive(name, path, box, a):
    grey = np.array(Image.open(path).convert('L'))
    if box:
        x0, y0, x1, y1 = box
        grey = grey[y0:y1, x0:x1]
    k = max(15, int(min(grey.shape) / 40) | 1)
    k = min(k, max(15, int(max(grey.shape) / 40) | 1))
    bg = cv2.GaussianBlur(cv2.morphologyEx(grey, cv2.MORPH_CLOSE, np.ones((k, k), np.uint8)), (0, 0), k / 3)
    norm = grey.astype(float) / np.maximum(bg.astype(float), 1)
    ink = (norm < a.rel).astype(np.uint8)
    bands = [(0, grey.shape[0])]
    # a strip is at most --strip-max x-heights tall; estimate xh roughly from the darkest-ink row profile
    dark = (norm < a.ghost).astype(np.uint8)
    prof = dark.sum(axis=1).astype(float)
    if prof.max() > 0:
        n_, _, st_, _ = cv2.connectedComponentsWithStats(dark, connectivity=8)
        hs = st_[1:, 3][st_[1:, 4] >= 4]
        mh = float(np.median(hs[hs >= np.percentile(hs, 60)])) if len(hs) else 20.0
        if grey.shape[0] > a.strip_max * max(mh, 3):
            peaks, pitch = line_centres(dark, mh)
            if len(peaks) > 1:
                mids = [0] + [int((p + q) / 2) for p, q in zip(peaks, peaks[1:])] + [grey.shape[0]]
                bands = list(zip(mids, mids[1:]))
    signs, xhs = [], []
    for li, (y0, y1) in enumerate(bands):
        S, xh = _cursive_strip(name, grey[y0:y1], norm[y0:y1], ink[y0:y1], li, y0, a)
        signs += S
        if xh:
            xhs.append(xh)
    xh = float(np.median(xhs)) if xhs else 0.0
    if a.debug:
        d = cv2.cvtColor(grey, cv2.COLOR_GRAY2BGR)
        for s_ in signs:
            cv2.rectangle(d, (s_['x'], s_['y']), (s_['x'] + s_['w'], s_['y'] + s_['h']), (0, 0, 255), 1)
        cv2.imwrite(os.path.join(a.out, f'debug_{name}.jpg'), d)
    return signs, [], grey, xh


SIGN_COLS = ['sid', 'page', 'line', 'pos', 'x', 'y', 'w', 'h', 'rh', 'rw', 'dy', 'marks']
MARK_COLS = ['mid', 'page', 'line', 'x', 'y', 'w', 'h', 'rh', 'rw', 'sid']


def own_median_h(path, box, a):
    """The page's own median sign height, exactly as segment_page computes it before any --median-h override."""
    grey = np.array(Image.open(path).convert('L'))
    if box:
        x0, y0, x1, y1 = box
        grey = grey[y0:y1, x0:x1]
    ink = binarise(grey, a.rel)
    ink = cv2.morphologyEx(ink, cv2.MORPH_OPEN, np.ones((2, 2), np.uint8)) if min(grey.shape) > 2500 else ink
    n, lab, st, cen = cv2.connectedComponentsWithStats(ink, connectivity=8)
    areas = st[1:, 4]
    big = st[1:][areas >= np.percentile(areas, 60)] if len(areas) else st[1:]
    return float(np.median(big[:, 3])) if len(big) else 20.0


def cmd_segment(a):
    os.makedirs(os.path.join(a.out, 'crops'), exist_ok=True)
    allS, allM, scale = [], [], {}
    a.shared_mh = None
    if a.median_h:
        if a.cursive:
            sys.exit('--median-h applies to the default (non --cursive) mode only')
        if a.median_h == 'pool':
            own = []
            for spec in a.page:
                name, rest = spec.split('=', 1)
                path, box = (rest.split('@') + [None])[:2]
                own.append(own_median_h(path, [int(v) for v in box.split(',')] if box else None, a))
            a.shared_mh = float(np.median(own))
            print(f'--median-h pool: median of {len(own)} pages\' own medians = {a.shared_mh:.1f}px '
                  f'(range {min(own):.0f}-{max(own):.0f})')
        else:
            a.shared_mh = float(a.median_h)
            if a.shared_mh <= 0:
                sys.exit('--median-h must be a positive number of pixels or "pool"')
    for spec in a.page:
        name, rest = spec.split('=', 1)
        path, box = (rest.split('@') + [None])[:2]
        box = [int(v) for v in box.split(',')] if box else None
        S, M, grey, mh = (segment_cursive if a.cursive else segment_page)(name, path, box, a)
        cv2.imwrite(os.path.join(a.out, 'crops', f'{name}.png'), grey)
        scale[name] = dict(image=path, box=box, median_h=mh)
        allS += S
        allM += M
        print(f'{name}: {len(S)} signs, {len(M)} marks, median sign height {mh:.0f}px')
    for fn, rows, cols in (('signs.tsv', allS, SIGN_COLS), ('marks.tsv', allM, MARK_COLS)):
        with open(os.path.join(a.out, fn), 'w') as f:
            f.write('\t'.join(cols) + '\n')
            for r in rows:
                f.write('\t'.join(f'{r[c]:.3f}' if isinstance(r[c], float) else str(r[c]) for c in cols) + '\n')
    np.savez_compressed(os.path.join(a.out, 'bitmaps.npz'),
                        signs=np.array([r['bm'] for r in allS] or np.zeros((0, BM, BM)), np.uint8),
                        marks=np.array([r['bm'] for r in allM] or np.zeros((0, BM, BM)), np.uint8))
    json.dump(scale, open(os.path.join(a.out, 'pages.json'), 'w'), indent=1)


def read(out, fn):
    return list(csv.DictReader(open(os.path.join(out, fn)), delimiter='\t'))


def feats(bm, rows, size_w=3.0, pca_scale='unit'):
    H = np.array([hog(b.astype(float) / 255, orientations=9, pixels_per_cell=(8, 8), cells_per_block=(2, 2))
                  for b in bm])
    ncomp = min(40, len(bm) - 1, H.shape[1])
    Z = PCA(n_components=ncomp, random_state=SEED).fit_transform(StandardScaler().fit_transform(H))
    # 'unit' (carpi cluster.py, and the fr.2933 run): every component to unit variance. 'shared': one scale for all,
    # keeping the variance ratios -- needed for small samples, where 'unit' blows the noise components up.
    Z = StandardScaler().fit_transform(Z) if pca_scale == 'unit' else Z / (Z[:, 0].std() or 1)
    E = np.stack([np.log(np.array([float(r['rh']) for r in rows])),
                  np.log(np.array([float(r['rw']) for r in rows]))], axis=1)
    E = StandardScaler().fit_transform(E) if pca_scale == 'unit' else E   # log ratios are already scale-free
    return np.hstack([Z, E * size_w])


def sheet(bm, lab, dist, path, per=24, cell=56, rows_per=20):
    ks = sorted(set(lab), key=lambda v: [int(x) for x in str(v).split('.')])
    outs = []
    for start in range(0, len(ks), rows_per):
        chunk = ks[start:start + rows_per]
        img = np.full((len(chunk) * cell, (per + 2) * cell), 255, np.uint8)
        for ri, k in enumerate(chunk):
            idx = np.where(lab == k)[0]
            idx = idx[np.argsort(dist[idx])]
            pick = list(idx[:per // 2]) + list(idx[per // 2:][::max(1, (len(idx) - per // 2) // (per // 2) or 1)][:per // 2])
            cv2.putText(img, f'{k}:{len(idx)}', (2, ri * cell + 32), cv2.FONT_HERSHEY_SIMPLEX, 0.5, 0, 1)
            for ci, i in enumerate(pick[:per]):
                b = cv2.resize(255 - bm[i], (cell - 6, cell - 6), interpolation=cv2.INTER_AREA)
                img[ri * cell + 3:ri * cell + cell - 3, (ci + 2) * cell + 3:(ci + 3) * cell - 3] = b
            cv2.line(img, (0, (ri + 1) * cell - 1), (img.shape[1], (ri + 1) * cell - 1), 200, 1)
        p = path.replace('.png', f'_{start // rows_per:02d}.png') if len(ks) > rows_per else path
        cv2.imwrite(p, img)
        outs.append(p)
    return outs


def cmd_cluster(a):
    z = np.load(os.path.join(a.out, 'bitmaps.npz'))
    with open(os.path.join(a.out, 'clusters.tsv'), 'w') as f:
        f.write('id\tkind\tcluster\tdist\n')
        for kind, fn, key, k in (('sign', 'signs.tsv', 'sid', a.k), ('mark', 'marks.tsv', 'mid', a.k_marks)):
            rows, bm = read(a.out, fn), z[kind + 's']
            if len(rows) < 2:
                continue
            X = feats(bm, rows, pca_scale=a.pca_scale)
            km = KMeans(n_clusters=min(k, len(rows)), n_init=10, random_state=SEED).fit(X)
            dist = np.linalg.norm(X - km.cluster_centers_[km.labels_], axis=1)
            lab = np.array([str(l) for l in km.labels_], dtype=object)
            for spec in (a.split or []):
                sk, _, sn = spec.partition(':')
                if not sk.startswith(kind[0]):
                    continue
                idx = np.where(lab == sk[1:])[0]
                if len(idx) > int(sn):
                    sub = KMeans(n_clusters=int(sn), n_init=10, random_state=SEED).fit(X[idx])
                    dist[idx] = np.linalg.norm(X[idx] - sub.cluster_centers_[sub.labels_], axis=1)
                    lab[idx] = [f'{sk[1:]}.{j}' for j in sub.labels_]
            for r, l, d in zip(rows, lab, dist):
                f.write(f'{r[key]}\t{kind}\t{l}\t{d:.3f}\n')
            outs = sheet(bm, lab, dist, os.path.join(a.out, f'sheet_{kind}s.png'))
            print(f'{kind}s: {len(rows)} in {len(set(km.labels_))} clusters -> {", ".join(outs)}')


def cmd_atlas(a):
    if a.from_truth:
        return cmd_atlas_truth(a)
    if not a.labels:
        sys.exit('atlas needs --labels (or --from-truth)')
    L = json.load(open(a.labels))
    signs = {r['sid']: r for r in read(a.out, 'signs.tsv')}
    marks = {r['mid']: r for r in read(a.out, 'marks.tsv')}
    cl = read(a.out, 'clusters.tsv')
    over = L.get('override', {})
    code, mcode, dist = {}, {}, {}
    for r in cl:
        (code if r['kind'] == 'sign' else mcode)[r['id']] = (L['signs'] if r['kind'] == 'sign' else L['marks']).get(r['cluster'], '_')
        dist[r['id']] = float(r['dist'])
    code.update({k: v for k, v in over.items() if k in code})
    mcode.update({k: v for k, v in over.items() if k in mcode})
    by = collections.defaultdict(list)
    for sid, c in code.items():
        if c != '_':
            by[c].append(sid)
    pages = {}
    order = L.get('order') or sorted(by)
    rows_out, strips = [], []
    cell, per = 72, a.per
    for c in order:
        ids = sorted(by.get(c, []), key=lambda s: (signs[s]['page'] not in (a.prefer or []), dist[s]))
        if not ids:
            continue
        seen = collections.Counter(mcode.get(m, '_') for s in ids for m in signs[s]['marks'].split('|') if m)
        seen.pop('_', None)
        pg = sorted({signs[s]['page'] for s in ids})
        ex = ids[:per]
        rows_out.append([c, L.get('desc', {}).get(c, ''), str(len(ids)), ','.join(pg), ','.join(ex),
                         ' '.join(f'{m}:{n}' for m, n in seen.most_common())])
        strip = np.full((cell, (per + 2) * cell), 255, np.uint8)
        cv2.putText(strip, c, (4, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.8, 0, 2)
        cv2.putText(strip, str(len(ids)), (4, 60), cv2.FONT_HERSHEY_SIMPLEX, 0.5, 0, 1)
        for ci, s in enumerate(ex):
            r = signs[s]
            if r['page'] not in pages:
                pages[r['page']] = cv2.imread(os.path.join(a.out, 'crops', r['page'] + '.png'), cv2.IMREAD_GRAYSCALE)
            g = pages[r['page']]
            x, y, w, h = (int(r[k]) for k in 'xywh')
            m = int(0.25 * max(w, h))
            top = int(0.6 * max(w, h))  # keep the marks above
            sub = g[max(0, y - top):y + h + m, max(0, x - m):x + w + m]
            sc = (cell - 4) / max(sub.shape)
            sub = cv2.resize(sub, (max(1, int(sub.shape[1] * sc)), max(1, int(sub.shape[0] * sc))), interpolation=cv2.INTER_AREA)
            y0, x0 = (cell - sub.shape[0]) // 2, (ci + 2) * cell + (cell - sub.shape[1]) // 2
            strip[y0:y0 + sub.shape[0], x0:x0 + sub.shape[1]] = sub
        cv2.line(strip, (0, cell - 1), (strip.shape[1], cell - 1), 190, 1)
        strips.append(strip)
    if strips:
        cv2.imwrite(os.path.join(a.out, 'atlas.png'), np.vstack(strips))
    with open(os.path.join(a.out, 'atlas.tsv'), 'w') as f:
        f.write('code\tdesc\tcount\tpages\texemplars\tmarks_seen\n')
        for r in rows_out:
            f.write('\t'.join(r) + '\n')
    print(f'{len(rows_out)} codes, {sum(int(r[2]) for r in rows_out)} signs labelled')


def _page_grey(out, page, cache):
    """crops/<page>.png from 'segment'; when that gitignored copy is gone, the page image named in pages.json."""
    if page not in cache:
        cp = os.path.join(out, 'crops', page + '.png')
        g = cv2.imread(cp, cv2.IMREAD_GRAYSCALE) if os.path.exists(cp) else None
        if g is None:
            info = json.load(open(os.path.join(out, 'pages.json'))).get(page, {})
            g = cv2.imread(info.get('image', ''), cv2.IMREAD_GRAYSCALE)
            if g is not None and info.get('box'):
                x0, y0, x1, y1 = info['box']
                g = g[y0:y1, x0:x1]
        if g is None:
            sys.exit(f'no image for page {page}: run segment again (crops/) or fix pages.json')
        cache[page] = g
    return cache[page]


def _tile(g, r, cell):
    x, y, w, h = (int(r[k]) for k in 'xywh')
    m = int(0.2 * max(w, h)); top = int(0.6 * max(w, h))      # keep the marks (dots, ticks) above the sign
    sub = g[max(0, y - top):y + h + m, max(0, x - m):x + w + m]
    sc = min((cell - 6) / sub.shape[1], (cell - 6) / sub.shape[0], 3.0)
    sub = cv2.resize(sub, (max(1, int(sub.shape[1] * sc)), max(1, int(sub.shape[0] * sc))), interpolation=cv2.INTER_CUBIC)
    t = np.full((cell, cell), 255, np.uint8)
    y0, x0 = (cell - sub.shape[0]) // 2, (cell - sub.shape[1]) // 2
    t[y0:y0 + sub.shape[0], x0:x0 + sub.shape[1]] = sub
    return t


def pick_spread(X, per, spread, trim=0.0):
    """Indices of `per` rows of X: the medoid first (the row nearest the mean), then with spread each next row is the
    one farthest from all picked so far (farthest-point sampling over HOG + log size: allographs, cramped and wide
    forms), without spread the next-nearest to the mean. trim: with 5+ rows, the farthest `trim` share from the mean
    is dropped first, so the spread does not reach for a mis-read or mis-aligned tile (TX-SHEET: a phi in the T86 row)."""
    if trim and len(X) >= 5:
        keep = np.argsort(np.linalg.norm(X - X.mean(0), axis=1))[:max(per, int(round(len(X) * (1 - trim))))]
        return [int(keep[k]) for k in pick_spread(X[keep], per, spread)]
    if len(X) <= per:
        return list(np.argsort(np.linalg.norm(X - X.mean(0), axis=1)))
    d0 = np.linalg.norm(X - X.mean(0), axis=1)
    if not spread:
        return list(np.argsort(d0)[:per])
    pick = [int(np.argmin(d0))]
    dmin = np.linalg.norm(X - X[pick[0]], axis=1)
    while len(pick) < per:
        j = int(np.argmax(dmin)); pick.append(j)
        dmin = np.minimum(dmin, np.linalg.norm(X - X[j], axis=1))
    return pick


def cmd_atlas_truth(a):
    """atlas --from-truth: the per-hand exemplar sheet (the palaeographer's alphabet, TX-SHEET 4 Oct 2026)."""
    signs = read(a.out, 'signs.tsv')
    idx = {r['sid']: i for i, r in enumerate(signs)}
    excl = set(a.exclude_leaf or [])
    by = collections.defaultdict(list)
    skipped = collections.Counter()
    for r in csv.DictReader(open(a.from_truth), delimiter='\t'):
        sid, c = r['sid'], r['code']
        if sid not in idx:
            skipped['unknown sid'] += 1; continue
        if signs[idx[sid]]['page'] in excl:
            skipped['excluded leaf'] += 1; continue
        if a.grades and r.get('grade', '') not in a.grades:
            skipped['grade'] += 1; continue
        by[c].append(idx[sid])
    if a.codes:
        codes = [x.strip() for x in (open(a.codes[1:]).read().split() if a.codes.startswith('@') else a.codes.split(','))
                 if x.strip()]
    else:
        codes = sorted(by)
    canon = {}
    if a.canonical:
        cw, ch, nc = (int(v) for v in a.grid.lower().split('x'))
        im = cv2.imread(a.canonical, cv2.IMREAD_GRAYSCALE)
        for n, c in enumerate(sorted(codes)):      # the canonical sheet lays its cells out in sorted code order
            gx, gy = (n % nc) * cw, (n // nc) * ch
            canon[c] = im[gy + 24:gy + ch - 2, gx + 2:gx + cw - 2]   # below the cell's printed id
    bm = np.load(os.path.join(a.out, 'bitmaps.npz'))['signs']
    X = feats(bm, signs, pca_scale='shared')
    cell, cache = a.cell, {}
    rows_tsv, strips = [], []
    font = cv2.FONT_HERSHEY_SIMPLEX
    for c in codes:
        ids = by.get(c, [])
        use = len(ids) >= a.min_secure
        pick = [ids[k] for k in pick_spread(X[ids], a.per, a.spread, a.trim)] if use else []
        strip = np.full((cell, (a.per + 2) * cell + 12), 255, np.uint8)
        cv2.putText(strip, c, (4, cell // 2), font, 0.8, 0, 2)
        cv2.putText(strip, 'print' if c in canon else '', (4, cell // 2 + 22), font, 0.4, 90, 1)
        if c in canon:
            cc = canon[c]
            sc = min((cell - 6) / cc.shape[1], (cell - 6) / cc.shape[0])
            cc = cv2.resize(cc, (max(1, int(cc.shape[1] * sc)), max(1, int(cc.shape[0] * sc))), interpolation=cv2.INTER_AREA)
            y0, x0 = (cell - cc.shape[0]) // 2, cell + (cell - cc.shape[1]) // 2
            strip[y0:y0 + cc.shape[0], x0:x0 + cc.shape[1]] = cc
        cv2.line(strip, (2 * cell + 5, 4), (2 * cell + 5, cell - 4), 120, 2)      # print | the hand
        for k, i in enumerate(pick):
            t = _tile(_page_grey(a.out, signs[i]['page'], cache), signs[i], cell)
            x0 = (k + 2) * cell + 12
            strip[:, x0:x0 + cell] = np.minimum(strip[:, x0:x0 + cell], t)
            cv2.rectangle(strip, (x0, 0), (x0 + cell - 1, cell - 1), 200, 1)
        cv2.line(strip, (0, cell - 1), (strip.shape[1], cell - 1), 150, 1)
        strips.append(strip)
        rows_tsv.append([c, str(len(ids)), 'hand' if use else 'print-only', ','.join(signs[i]['sid'] for i in pick)])
    made = []
    for s0 in range(0, len(strips), a.rows_per_sheet):
        p = os.path.join(a.sheet_dir or a.out, f'{a.sheet_prefix}_{s0 // a.rows_per_sheet + 1:02d}.png')
        cv2.imwrite(p, np.vstack(strips[s0:s0 + a.rows_per_sheet]))
        made.append(p)
    with open(os.path.join(a.sheet_dir or a.out, f'{a.sheet_prefix}.tsv'), 'w') as f:
        f.write('code\tn_secure\tshown\texemplars\n')
        for r in rows_tsv:
            f.write('\t'.join(r) + '\n')
    nh = sum(r[2] == 'hand' for r in rows_tsv)
    print(f'{len(codes)} codes: {nh} with {a.per}-tile hand rows (>= {a.min_secure} secure), {len(codes) - nh} print-only; '
          f'skipped {dict(skipped)} -> {", ".join(made)}')


def cmd_crop(a):
    os.makedirs(a.dest, exist_ok=True)
    made = []
    if a.sid:
        if not a.out:
            sys.exit('--sid needs --out (the segment run to read signs.tsv/marks.tsv from)')
        signs = {r['sid']: r for r in read(a.out, 'signs.tsv')}
        marks = {r['mid']: r for r in read(a.out, 'marks.tsv')}
        cache = {}
        for sid in a.sid:
            r = signs.get(sid) or marks.get(sid)
            if r is None:
                print(f'no such id: {sid}', file=sys.stderr)
                continue
            if r['page'] not in cache:
                cache[r['page']] = cv2.imread(os.path.join(a.out, 'crops', r['page'] + '.png'), cv2.IMREAD_GRAYSCALE)
            g = cache[r['page']]
            x, y, w, h = (int(float(r[k])) for k in 'xywh')
            y0, y1 = max(0, y - a.margin), min(g.shape[0], y + h + a.margin)
            x0, x1 = max(0, x - a.margin), min(g.shape[1], x + w + a.margin)
            sub = cv2.resize(g[y0:y1, x0:x1], None, fx=a.scale, fy=a.scale, interpolation=cv2.INTER_CUBIC)
            p = os.path.join(a.dest, f'{sid}.png')
            cv2.imwrite(p, sub)
            made.append(p)
    else:
        if not a.image or not a.box:
            sys.exit('--box mode needs --image and at least one --box x0,y0,x1,y1[:label]')
        img = cv2.imread(a.image, cv2.IMREAD_GRAYSCALE)
        if img is None:
            sys.exit(f'cannot read {a.image}')
        stem = os.path.splitext(os.path.basename(a.image))[0]
        for spec in a.box:
            box, _, label = spec.partition(':')
            x0, y0, x1, y1 = (int(v) for v in box.split(','))
            ym0, ym1 = max(0, y0 - a.margin), min(img.shape[0], y1 + a.margin)
            xm0, xm1 = max(0, x0 - a.margin), min(img.shape[1], x1 + a.margin)
            sub = cv2.resize(img[ym0:ym1, xm0:xm1], None, fx=a.scale, fy=a.scale, interpolation=cv2.INTER_CUBIC)
            name = label or f'{stem}_{x0}-{y0}-{x1}-{y1}'
            p = os.path.join(a.dest, f'{name}.png')
            cv2.imwrite(p, sub)
            made.append(p)
    print(f'{len(made)} crops -> {a.dest}')


def cmd_classify(a):
    from sklearn.neighbors import NearestNeighbors
    L = json.load(open(a.labels))
    over = L.get('override', {})
    rows = read(a.out, 'signs.tsv')
    mrows = {r['mid']: r for r in read(a.out, 'marks.tsv')}
    cl = {(r['kind'], r['id']): r['cluster'] for r in read(a.out, 'clusters.tsv')}
    bm = np.load(os.path.join(a.out, 'bitmaps.npz'))['signs']
    X = feats(bm, rows, pca_scale=a.pca_scale)
    lab = np.array([over.get(r['sid'], L['signs'].get(cl.get(('sign', r['sid'])), '_')) for r in rows], dtype=object)
    mlab = {m: over.get(m, L['marks'].get(cl.get(('mark', m)), '_')) for m in mrows}
    hold = tuple(a.holdout or ())
    held = np.array([bool(hold) and r['sid'].startswith(hold) for r in rows])
    lab[held] = '_held'                     # never a vote, never a cluster code
    allp = a.page == 'all'
    tgt = [i for i, r in enumerate(rows) if allp or r['page'] == a.page]
    if allp and a.exclude_page:
        sys.exit('--exclude-page needs one --page, not all')
    # --exclude-page: the target page's own boxes never vote. Without it, an unlabelled new page's boxes are each
    # other's nearest neighbours and vote '_' for one another (debosnys c4a/c4b, 25 Sept 2026: 33%/45% noise, 6.5%/26%
    # with the page excluded). Only boxes of OTHER pages (the labelled set) remain candidates.
    ok = ~held
    if a.exclude_page:
        ok &= np.array([r['page'] != a.page for r in rows])
        if not ok.any():
            sys.exit('--exclude-page: no boxes of any other page to vote with')
    cand = np.where(ok)[0]
    pool = min(len(cand), max(a.knn + 1, a.pool if a.topk > 1 else 0))
    nn = NearestNeighbors(n_neighbors=pool).fit(X[cand])
    d, ix = nn.kneighbors(X[tgt])
    ix = cand[ix]
    out = []
    for n, i in enumerate(tgt):
        pairs = [(x, j) for x, j in zip(d[n], ix[n]) if j != i]
        dd, ii = zip(*pairs[:a.knn])
        votes = collections.Counter()
        for x, j in zip(dd, ii):
            votes[lab[j]] += 1 / (x + 1e-6)
        best = max(votes, key=votes.get)
        r = rows[i]
        mk = '|'.join(('?' if mlab.get(m, '_') == '_' else mlab[m]) for m in r['marks'].split('|') if m)
        row = dict(page=r['page'], line=int(r['line']), box=r['sid'], pos=int(r['pos']), x=int(r['x']), y=int(r['y']),
                   w=int(r['w']), h=int(r['h']), code=best, dist=f'{dd[0]:.3f}',
                   share=f'{votes[best] / sum(votes.values()):.2f}', cluster_code='_held' if held[i] else lab[i], marks=mk)
        if a.topk > 1:
            near = {}
            for x, j in pairs:
                near.setdefault(lab[j], x)
            tot = sum(votes.values())
            rank = sorted(votes, key=lambda c: -votes[c]) + sorted((c for c in near if c not in votes), key=near.get)
            for k in range(a.topk):
                c = rank[k] if k < len(rank) else ''
                row[f'k{k + 1}'] = c
                row[f'd{k + 1}'] = f'{near[c]:.3f}' if c else ''
                row[f's{k + 1}'] = f'{votes.get(c, 0) / tot:.2f}' if c else ''
        out.append(row)
    out.sort(key=lambda r: (r['page'], r['line'], r['pos']))
    cols = (['page'] if allp else []) + ['line', 'box', 'pos', 'x', 'y', 'w', 'h', 'code', 'dist', 'share',
                                        'cluster_code', 'marks']
    if a.topk > 1:
        cols += [f'{v}{k + 1}' for k in range(a.topk) for v in 'kds']
    with open(a.tsv, 'w') as f:
        f.write('\t'.join(cols) + '\n')
        for r in out:
            f.write('\t'.join(str(r[c]) for c in cols) + '\n')
    agree = sum(r['code'] == r['cluster_code'] for r in out)
    print(f'{a.page}: {len(out)} boxes classified; kNN code = cluster code for {agree}; '
          f'{sum(r["code"] != "_" for r in out)} cipher codes')
    if a.strips and not allp:
        strips(a, out, [m for m in mrows.values() if m['page'] == a.page])


def strips(a, out, marks):
    os.makedirs(a.strips, exist_ok=True)
    g = cv2.imread(os.path.join(a.out, 'crops', a.page + '.png'), cv2.IMREAD_GRAYSCALE)
    by = collections.defaultdict(list)
    for r in out:
        by[r['line']].append(r)
    mby = collections.defaultdict(list)
    for m in marks:
        mby[int(m['line'])].append(m)
    made = []
    for li, bs in sorted(by.items()):
        ys = [b['y'] for b in bs] + [int(m['y']) for m in mby[li]]
        y0 = max(0, min(ys) - 8)
        y1 = min(g.shape[0], max(b['y'] + b['h'] for b in bs) + 8)
        x0 = max(0, min(b['x'] for b in bs) - 10)
        x1 = min(g.shape[1], max(b['x'] + b['w'] for b in bs) + 10)
        nparts = max(1, -(-(x1 - x0) // a.max_w))
        cuts = [x0]
        for k in range(1, nparts):          # cut between boxes near each equal share
            target = x0 + k * (x1 - x0) / nparts
            gap = min(bs, key=lambda b: abs(b['x'] - target))
            cuts.append(gap['x'] - 4)
        cuts.append(x1)
        for k in range(nparts):
            cx0, cx1 = cuts[k], cuts[k + 1]
            band = cv2.cvtColor(g[y0:y1, cx0:cx1], cv2.COLOR_GRAY2BGR)
            lab_h = 44
            img = np.full((band.shape[0] + lab_h, band.shape[1], 3), 255, np.uint8)
            img[:band.shape[0]] = band
            for j, b in enumerate(b for b in bs if cx0 <= b['x'] < cx1):
                col = (0, 0, 220) if b['pos'] % 2 else (200, 90, 0)
                cv2.rectangle(img, (b['x'] - cx0, b['y'] - y0), (b['x'] + b['w'] - cx0, b['y'] + b['h'] - y0), col, 2)
                cv2.putText(img, str(b['pos']), (b['x'] - cx0, band.shape[0] + 16 + 20 * (j % 2)),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.6, col, 2)
            p = os.path.join(a.strips, f'{a.page}_L{li:02d}' + (f'{"abcdefgh"[k]}' if nparts > 1 else '') + '.jpg')
            cv2.imwrite(p, img, [cv2.IMWRITE_JPEG_QUALITY, 85])
            made.append(p)
    print(f'{len(made)} strips -> {a.strips}')


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sp = ap.add_subparsers(dest='cmd', required=True)
    s = sp.add_parser('segment')
    s.add_argument('--page', action='append', required=True)
    s.add_argument('--out', required=True)
    s.add_argument('--rel', type=float, default=0.78, help='ink if pixel < rel x local background (0.78)')
    s.add_argument('--mark-h', type=float, default=0.55, help='mark if height < this x median height (0.55)')
    s.add_argument('--mark-above', type=float, default=0.3, help='mark bottom must sit this x median height above the line centre (0.3)')
    s.add_argument('--min-area', type=float, default=0.12, help='drop a component whose side is under this x median height (0.12); raise on a noisy page')
    s.add_argument('--median-h', help='default mode: use this shared median sign height (px) on every page instead of each '
                   'page\'s own; "pool" = the median of the pages\' own medians. For line crops of one leaf where a '
                   'speck-dominated crop collapses its own median (R9-FLOR, c.127 L08_s1: 4 px against ~50)')
    s.add_argument('--merge-vgap', type=float, default=0.6, help='merge same-line, x-overlapping components only if the vertical gap between them is under this x median height (0.6); stops distant dust specks chaining into one giant box')
    s.add_argument('--cursive', action='store_true',
                   help='joined cursive hand with bleed-through: one line strip per --page, ghost floor, fragments grouped '
                        'by x-height gaps, over-wide groups split at column-ink minima (see the docstring)')
    s.add_argument('--ghost', type=float, default=0.55, help='--cursive: a component is ink only if its --dark-q quantile is under this x local background (0.55)')
    s.add_argument('--dark-q', type=float, default=0.1, help='--cursive: darkness quantile tested against --ghost (0.1)')
    s.add_argument('--core', type=float, default=0.5, help='--cursive: x-height band = the rows round the row-profile peak with ink >= this x the peak (0.5)')
    s.add_argument('--ghost-px', type=float, default=0.75, help='--cursive: a pixel of a kept component counts as ink only under this x background (0.75); clears ghost ink touching real strokes')
    s.add_argument('--band', type=float, default=1.0, help='--cursive: ink is kept only within this x xh above and below the core band (1.0); cuts neighbour lines')
    s.add_argument('--min-side', type=float, default=0.25, help='--cursive: drop a component whose longer side is under this x xh (0.25)')
    s.add_argument('--gap', type=float, default=0.7, help='--cursive: column runs in the core band closer than this x xh are one sign (0.7)')
    s.add_argument('--split-w', type=float, default=4.0, help='--cursive: split a group wider than this x xh (4.0)')
    s.add_argument('--piece', type=float, default=2.8, help='--cursive: an over-wide group is split into round(width / (this x xh)) pieces (2.8)')
    s.add_argument('--strip-max', type=float, default=6.0, help='--cursive: a page taller than this x the median sign height is cut into line bands first (6)')
    s.add_argument('--debug', action='store_true')
    c = sp.add_parser('cluster')
    c.add_argument('--out', required=True)
    c.add_argument('--k', type=int, default=60)
    c.add_argument('--k-marks', type=int, default=16)
    c.add_argument('--pca-scale', choices=['unit', 'shared'], default='unit',
                   help="unit: each PCA component standardised (default, large samples); shared: small samples")
    c.add_argument('--split', action='append', help="re-split one cluster: s52:3 (sign cluster 52 into 3), m10:2")
    t = sp.add_parser('atlas')
    t.add_argument('--out', required=True)
    t.add_argument('--labels', help='labels.json (cluster-named atlas); not needed with --from-truth')
    t.add_argument('--per', type=int, default=10)
    t.add_argument('--from-truth', help='TSV with sid, code [, grade]: securely read boxes; writes the per-hand exemplar '
                                        'sheet instead of the cluster atlas (TX-SHEET, see the docstring)')
    t.add_argument('--spread', action='store_true', help='--from-truth: pick tiles by farthest-point spread, not nearest the mean')
    t.add_argument('--trim', type=float, default=0.2, help='--from-truth: drop this farthest share of a code\'s tiles before picking (0.2)')
    t.add_argument('--exclude-leaf', action='append', help='--from-truth: page never used for exemplars (the eval leaves), repeatable')
    t.add_argument('--grades', help='--from-truth: keep only rows whose grade is in this string (e.g. CHS)')
    t.add_argument('--codes', help='--from-truth: every code to show, comma list or @file (default: the codes in the TSV)')
    t.add_argument('--min-secure', type=int, default=2, help='--from-truth: fewer secure tiles than this -> the print shape only (2)')
    t.add_argument('--canonical', help='--from-truth: the canonical sign sheet PNG (cells in sorted --codes order)')
    t.add_argument('--grid', default='110x110x9', help='--from-truth: canonical cell width x height x columns (110x110x9)')
    t.add_argument('--cell', type=int, default=96, help='--from-truth: tile size in px (96)')
    t.add_argument('--rows-per-sheet', type=int, default=13, help='--from-truth: codes per sheet image, one subagent call (13)')
    t.add_argument('--sheet-dir', help='--from-truth: where the sheets go (default --out)')
    t.add_argument('--sheet-prefix', default='sheet_truth', help='--from-truth: file prefix (sheet_truth)')
    t.add_argument('--prefer', action='append', help='take exemplars from this page first (a native-resolution page)')
    k = sp.add_parser('classify')
    k.add_argument('--out', required=True)
    k.add_argument('--labels', required=True)
    k.add_argument('--page', required=True, help="the page whose boxes are classified, or 'all'")
    k.add_argument('--tsv', required=True, help='output box list')
    k.add_argument('--knn', type=int, default=5)
    k.add_argument('--pca-scale', choices=['unit', 'shared'], default='unit')
    k.add_argument('--exclude-page', action='store_true',
                   help="never let the target page's own boxes vote (kNN over other pages' boxes only); use it when the "
                        "page is new and unlabelled, otherwise its boxes vote '_' for each other (debosnys c4, 25 Sept 2026)")
    k.add_argument('--strips', help='directory for per-line strips with box numbers')
    k.add_argument('--topk', type=int, default=1, help='also write the k best codes with distance and vote share (3)')
    k.add_argument('--pool', type=int, default=40, help='neighbour pool for codes outside the --knn voters (40)')
    k.add_argument('--holdout', action='append', help='box-id prefix that never votes (repeatable)')
    k.add_argument('--max-w', type=int, default=1800, help='cut a line strip into parts under this width (px)')
    r = sp.add_parser('crop')
    r.add_argument('--image', help='a plain image file to cut pixel --box crops from directly')
    r.add_argument('--box', action='append', default=[], help='x0,y0,x1,y1[:label] in --image, repeatable')
    r.add_argument('--out', help="a prior 'segment' run's output dir, for --sid mode")
    r.add_argument('--sid', action='append', default=[], help="a signs.tsv/marks.tsv id from --out, repeatable")
    r.add_argument('--dest', required=True, help='directory to write one PNG per crop into')
    r.add_argument('--margin', type=int, default=6, help='pixels of context kept around each box (default 6)')
    r.add_argument('--scale', type=int, default=4, help='upscale factor, cubic interpolation (default 4)')
    a = ap.parse_args(argv)
    {'segment': cmd_segment, 'cluster': cmd_cluster, 'atlas': cmd_atlas, 'classify': cmd_classify,
     'crop': cmd_crop}[a.cmd](a)


if __name__ == '__main__':
    main()
