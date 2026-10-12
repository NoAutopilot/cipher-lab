#!/usr/bin/env python3
"""Segment the signs of invented-alphabet cipher pages, cluster them by shape, and publish one atlas.

  python3 tools/glyph_atlas.py segment --page NAME=IMAGE[@x0,y0,x1,y1] [--page ...] --out DIR [--debug]
  python3 tools/glyph_atlas.py cluster --out DIR [--k 60] [--k-marks 16]
  python3 tools/glyph_atlas.py atlas --out DIR --labels labels.json [--per 10] [--prefer PAGE]
  python3 tools/glyph_atlas.py atlas --out DIR --from-truth TOKENS.tsv --per 6 --spread --exclude-leaf PAGE [--canonical SHEET.png]
  python3 tools/glyph_atlas.py classify --out DIR --labels labels.json --page PAGE --tsv boxes.tsv [--exclude-page] [--strips DIR2]
        [--jitter 5 --jitter-px 2 --jitter-scale 0.05]   (per-box stability under crop perturbation, TXE-J)
  python3 tools/glyph_atlas.py classify --out DIR --labels labels.json --boxes BOXES.tsv --tsv out.tsv [--boxes-median-h PX]
        (TXE3-5 BOXES, 11 Oct 2026: classify boxes that are NOT atlas rows -- a person's corrected cuts, a second
        segmenter's proposals -- re-cut from their own image into the atlas's fitted feature space, kNN over the atlas;
        BOXES.tsv columns box_id, crop|image|page, x, y, w, h [, line, order|pos, kind]; rh/rw use --boxes-median-h,
        default the median h of the file's kind=sign boxes, so two box sets of one hand share one size scale.
        Catches: the same hand's boxes moved or deleted by a person (the only change is the cut). Must NOT change: a
        box list equal to the atlas's own boxes on the same image reproduces the stored top-1 (re-cut fidelity).
        Offline test: tools/tests/test_glyph_atlas.py.)
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
         --split-wide W [--split-piece P] [--split-random SEED] (TXE3-6 UNIT, 11 Oct 2026; default mode only): after the
         x-overlap merge, a sign box wider than W x the page's median sign height is split into max(2, round(w / (P x mh)))
         pieces (P default 1.0) at the column-ink minimum within +-0.35 piece of each equal-width cut -- the --cursive
         step-5 rule made available for a joining hand boxed by connected components (Vivonne 1573: 516 pen-unit boxes
         against 610 signs on 12 lines). --split-random SEED puts the same number of cuts at uniformly random columns
         instead (each at least 0.2 piece from the edges and from each other): the rule-3 control that must score worse
         than the ink-minimum cut if cutting at sign boundaries is what helps. Catches: a joined pair twice the median
         width -> two boxes. Must NOT change: a page with no box wider than W (identical output to the default).
         Offline test: test_glyph_atlas.py.
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
         --train-labels TSV [--round R] (MQS-CLASSIFY-ROUNDS, 9 Oct 2026; Lasry 2026 HistoCrypt, "Location Matters",
         train-correct-retrain): a person's sorted piles (box, code [, round]) override the box labels before the vote;
         --round R keeps rows with round <= R so err_true can be read per round (tx_bench.py). Catches: boxes a person
         labelled now vote with their sorted code, and a later round's correction of a box wins. Must NOT: change
         anything when the file is empty or --round 0 (output identical to no flag), nor accept a box id that is not
         in signs.tsv (exit). Measured on Birago no.87: tools/tests/PREREG-MQS-CLASSIFY-ROUNDS.md, shelf row.
match    --page NAME=IMAGE[@box] ... [--stored PAGE ...] --exclude-page P ... [--k 140] [--shuffle N] [--positive NAME]
         (MQS-GLYPH-MATCH, 9 Oct 2026; research/MARY-STUART-TALK-2026-10-09.tsv M03, the second-wave sweep of a sender's
         and recipient's series for the same glyph set, Lasry, Biermann and Tomokiyo 2023, Cryptologia 47:2, p.108 n.38):
         image-only shape match of candidate leaves against an atlas. Shapes only: labels.json, cluster names and codes
         are never read. The atlas signs minus every --exclude-page are re-featured (classify features; scaler and PCA
         fitted on the atlas only, queries transformed) and re-clustered by k-means (--k, SEED); per cluster a centroid
         and a radius (the --radius-q quantile of member distances). Each --page is segmented fresh (default segment
         parameters, whole image); --stored PAGE uses that atlas page's own rows as the query (it must be excluded).
         IR(leaf) = share of the leaf's signs within the radius of their nearest centroid. --shuffle N re-scores with
         cluster labels permuted across atlas signs (seeds 1..N; centroids and radii recomputed), the null that can
         differ because IR is a function of the labels. --positive NAME prints margin = IR(NAME) - max IR(others) and
         the null margins' p95. Writes --tsv (leaf, n_signs, ir, rank, ir_s1..ir_sN).
         Catches: a held-out leaf of the atlas's own hand scoring above other hands' leaves. Must NOT: let an excluded
         page's signs shape the fit (an excluded page's rows never reach scaler, PCA or k-means), nor accept --stored
         for a page that is still in the atlas (exit). Measured: tools/tests/PREREG-MQS-GLYPH-MATCH.md, shelf row.
Test: python3 tools/tests/test_glyph_atlas.py (offline: a synthetic page with two sign shapes, one carrying a mark).
"""
import argparse, collections, csv, json, os, re, sys

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


# Overlay colours, BGR for cv2: Okabe-Ito blue #0072B2 and the project's dark orange #B35900 (cvd_check.py
# sheets_light), replacing red vs green (MQS-CVD-AUDIT lead, deutan dE 3.7-5.1; MQS-CVD-FIX, 9 Oct 2026).
OVERLAY_BLUE = (178, 114, 0)  # BGR colour; on a line cvd_check.py --audit scans
OVERLAY_ORANGE = (0, 89, 179)  # BGR colour


def _dashed_line(img, x0, y, x1, col, t, dash=None):
    """Horizontal dashed line from x0 to x1 at row y."""
    dash = dash or max(6, 4 * t)
    for x in range(x0, x1, 2 * dash):
        cv2.line(img, (x, y), (min(x + dash, x1), y), col, t)


def _dashed_rect(img, x, y, w, h, col, t, dash=None):
    """Rectangle outline drawn as dashes (the non-colour cue beside a solid one)."""
    dash = dash or max(3, 2 * t)
    for xa in range(x, x + w, 2 * dash):
        xb = min(xa + dash, x + w)
        cv2.line(img, (xa, y), (xb, y), col, t)
        cv2.line(img, (xa, y + h), (xb, y + h), col, t)
    for ya in range(y, y + h, 2 * dash):
        yb = min(ya + dash, y + h)
        cv2.line(img, (x, ya), (x, yb), col, t)
        cv2.line(img, (x + w, ya), (x + w, yb), col, t)


def _wide_cuts(col, w, k, rnd=None, min_gap=0):
    """Column cut points (0 < c < w) dividing a w-wide ink-column profile `col` into k pieces: at the ink minimum within
    +-0.35 piece of each equal-width cut (the --cursive step-5 rule), or with `rnd` at sorted uniform random columns at
    least `min_gap` apart and from the edges (the --split-random control)."""
    step = w / k
    if rnd is not None:
        lo, hi = int(min_gap), int(w - min_gap)
        for _ in range(200):
            cs = sorted(int(v) for v in rnd.uniform(lo, hi, k - 1))
            if hi > lo and all(b - a >= min_gap for a, b in zip([0] + cs, cs + [w])):
                return cs
        return [int(round(j * step)) for j in range(1, k)]     # degenerate box: equal spacing
    cuts = [0]
    for j in range(1, k):
        c0 = int(j * step - 0.35 * step)
        c1 = int(j * step + 0.35 * step)
        c0, c1 = max(cuts[-1] + 1, c0), min(w - 1, c1)
        if c1 <= c0:
            continue
        cuts.append(c0 + int(np.argmin(col[c0:c1])))
    return cuts[1:]


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
        sw = getattr(a, 'split_wide', 0) or 0
        if sw > 0:
            # --split-wide: a box wider than sw x mh is cut into pieces (pen units -> sign units); see the docstring
            piece_px = max(1.0, (getattr(a, 'split_piece', 1.0) or 1.0) * mh)
            rnd = getattr(a, '_split_rng', None)
            split = []
            for c in merged:
                if c['w'] <= sw * mh:
                    split.append(c)
                    continue
                sub = np.isin(lab[c['y']:c['y'] + c['h'], c['x']:c['x'] + c['w']], c['ids']).astype(np.uint8)
                k = max(2, int(round(c['w'] / piece_px)))
                cuts = _wide_cuts(sub.sum(axis=0).astype(float), c['w'], k, rnd, 0.2 * piece_px)
                for u, v in zip([0] + cuts, cuts + [c['w']]):
                    rows = np.where(sub[:, u:v].any(axis=1))[0]
                    if not len(rows):
                        continue
                    split.append(dict(x=c['x'] + u, y=c['y'] + int(rows[0]), w=v - u, h=int(rows[-1] - rows[0] + 1),
                                      ids=c['ids'], split_from=c['x']))
            merged = split
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
        # CVD-safe overlay (MQS-CVD-FIX, 9 Oct 2026; was red/blue/green): signs solid orange boxes, marks dashed
        # blue boxes, line peaks dashed blue full-width lines -- shape and dash carry the kind, not hue alone.
        for s in signs:
            cv2.rectangle(d, (s['x'], s['y']), (s['x'] + s['w'], s['y'] + s['h']), OVERLAY_ORANGE, t)
        for m in marks:
            _dashed_rect(d, m['x'], m['y'], m['w'], m['h'], OVERLAY_BLUE, t)
        for p in peaks:
            _dashed_line(d, 0, int(p), d.shape[1], OVERLAY_BLUE, t)
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
            cv2.rectangle(d, (s_['x'], s_['y']), (s_['x'] + s_['w'], s_['y'] + s_['h']), OVERLAY_ORANGE, 1)
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
    a._split_rng = np.random.default_rng(a.split_random) if getattr(a, 'split_random', None) is not None else None
    if getattr(a, 'split_wide', 0) and a.cursive:
        sys.exit('--split-wide applies to the default (non --cursive) mode only; --cursive has --split-w/--piece')
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


def _hog(bm):
    return np.array([hog(b.astype(float) / 255, orientations=9, pixels_per_cell=(8, 8), cells_per_block=(2, 2))
                     for b in bm])


def feats(bm, rows, size_w=3.0, pca_scale='unit', project=False):
    """Feature matrix of the atlas bitmaps. project=True also returns proj(bitmaps, rh, rw) -> rows in the SAME
    fitted space (scalers and PCA fitted on the atlas only), for query tiles that are not in the atlas (--jitter)."""
    H = _hog(bm)
    ncomp = min(40, len(bm) - 1, H.shape[1])
    s1 = StandardScaler().fit(H)
    pca = PCA(n_components=ncomp, random_state=SEED)
    Z = pca.fit_transform(s1.transform(H))
    # 'unit' (carpi cluster.py, and the fr.2933 run): every component to unit variance. 'shared': one scale for all,
    # keeping the variance ratios -- needed for small samples, where 'unit' blows the noise components up.
    s2 = StandardScaler().fit(Z) if pca_scale == 'unit' else None
    z0 = Z[:, 0].std() or 1
    Z = s2.transform(Z) if s2 else Z / z0
    E = np.stack([np.log(np.array([float(r['rh']) for r in rows])),
                  np.log(np.array([float(r['rw']) for r in rows]))], axis=1)
    s3 = StandardScaler().fit(E) if pca_scale == 'unit' else None
    E = s3.transform(E) if s3 else E   # log ratios are already scale-free
    X = np.hstack([Z, E * size_w])
    if not project:
        return X

    def proj(bms, rh, rw):
        z = pca.transform(s1.transform(_hog(bms)))
        z = s2.transform(z) if s2 else z / z0
        e = np.stack([np.log(np.asarray(rh, float)), np.log(np.asarray(rw, float))], axis=1)
        e = s3.transform(e) if s3 else e
        return np.hstack([z, e * size_w])
    return X, proj


def jitter_tiles(ink, r, mh, n, px, scale, rnd):
    """--jitter (TXE-J, 9 Oct 2026; LANE TX-ENGINEER idea M11): n perturbed re-cuts of box r from the page's binarised
    ink -- the window shifted by an integer dx, dy in [-px, px] and scaled about the box centre by s in
    [1 - scale, 1 + scale], seeded. Inside the window only the components touching its central half are kept (a
    neighbour's stroke clipped in at the edge is not the sign). Returns [(48x48 bitmap, rh, rw)], the first entry
    being the unjittered re-cut (dx = dy = 0, s = 1), used to check that the re-cut reproduces the stored top-1."""
    x, y, w, h = (int(r[k]) for k in 'xywh')
    cx, cy = x + w / 2, y + h / 2
    H, W = ink.shape
    specs = [(0, 0, 1.0)] + [(int(rnd.integers(-px, px + 1)), int(rnd.integers(-px, px + 1)),
                              float(rnd.uniform(1 - scale, 1 + scale))) for _ in range(n)]
    out = []
    for dx, dy, s in specs:
        ww, hh = max(1, w * s), max(1, h * s)
        x0 = int(round(cx - ww / 2 + dx)); y0 = int(round(cy - hh / 2 + dy))
        x1 = int(round(cx + ww / 2 + dx)); y1 = int(round(cy + hh / 2 + dy))
        x0c, y0c, x1c, y1c = max(0, x0), max(0, y0), min(W, x1), min(H, y1)
        sub = np.zeros((max(1, y1 - y0), max(1, x1 - x0)), np.uint8)
        if x1c > x0c and y1c > y0c:
            sub[y0c - y0:y1c - y0, x0c - x0:x1c - x0] = ink[y0c:y1c, x0c:x1c]
        n_, lab, st, _ = cv2.connectedComponentsWithStats(sub, connectivity=8)
        qh, qw = sub.shape[0] / 4, sub.shape[1] / 4
        keep = [i for i in range(1, n_) if st[i, 0] < 3 * qw and st[i, 0] + st[i, 2] > qw
                and st[i, 1] < 3 * qh and st[i, 1] + st[i, 3] > qh]
        m = np.isin(lab, keep).astype(np.uint8) if keep else sub
        out.append((bitmap(m), hh / mh, ww / mh))
    return out


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
    if getattr(a, "pairs", None):
        return cmd_classify_pairs(a)
    if getattr(a, "pair", None):
        return cmd_classify_pair(a)
    if not a.labels or not (a.page or getattr(a, "boxes", None)):
        sys.exit("classify: --labels and --page (or --boxes) are required, unless --pair A B")
    from sklearn.neighbors import NearestNeighbors
    L = json.load(open(a.labels))
    over = dict(L.get('override', {}))
    rows = read(a.out, 'signs.tsv')
    if a.train_labels:
        tl = train_labels(a.train_labels, a.round, {r['sid'] for r in rows})
        over.update(tl)
        print(f'--train-labels: {len(tl)} box labels applied (round <= {a.round})')
    mrows = {r['mid']: r for r in read(a.out, 'marks.tsv')}
    cl = {(r['kind'], r['id']): r['cluster'] for r in read(a.out, 'clusters.tsv')}
    bm = np.load(os.path.join(a.out, 'bitmaps.npz'))['signs']
    jit = getattr(a, 'jitter', 0) or 0
    boxes_in = getattr(a, 'boxes', None)
    if boxes_in and jit:
        sys.exit('--boxes and --jitter together are not supported')
    if jit or boxes_in:
        X, proj = feats(bm, rows, pca_scale=a.pca_scale, project=True)
    else:
        X = feats(bm, rows, pca_scale=a.pca_scale)
    lab = np.array([over.get(r['sid'], L['signs'].get(cl.get(('sign', r['sid'])), '_')) for r in rows], dtype=object)
    mlab = {m: over.get(m, L['marks'].get(cl.get(('mark', m)), '_')) for m in mrows}
    hold = tuple(a.holdout or ())
    held = np.array([bool(hold) and r['sid'].startswith(hold) for r in rows])
    if getattr(a, 'only_train_labels', False):
        # --only-train-labels (TXE3-7 PROPAGATE, 11 Oct 2026): the kNN is built from the person's sorted tiles ALONE --
        # every box without a --train-labels row is held (never votes, no cluster code), so labels.json contributes
        # nothing. MQS-CLASSIFY-ROUNDS (9 Oct) layered train labels on top of labels.json and the 309 no.87 tune-tile
        # overrides out-voted them; this is the design in which the sorted tiles are the only voters.
        if not a.train_labels:
            sys.exit('--only-train-labels needs --train-labels')
        held |= np.array([r['sid'] not in tl for r in rows])
    lab[held] = '_held'                     # never a vote, never a cluster code
    if boxes_in and a.page:
        sys.exit('--boxes classifies the boxes in BOXES.tsv; do not pass --page')
    if not boxes_in and not a.page:
        sys.exit("classify needs --page NAME|all or --boxes BOXES.tsv")
    allp = a.page == 'all'
    tgt = [] if boxes_in else [i for i, r in enumerate(rows) if allp or r['page'] == a.page]
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
    if tgt:
        d, ix = nn.kneighbors(X[tgt])
        ix = cand[ix]
    def vote(dist, idx, i):
        pairs = [(x, j) for x, j in zip(dist, idx) if j != i]
        votes = collections.Counter()
        for x, j in pairs[:a.knn]:
            votes[lab[j]] += 1 / (x + 1e-6)
        return pairs, votes

    if boxes_in:
        return classify_boxes(a, boxes_in, nn, cand, lab, proj, vote)

    jres = {}
    if jit:
        # --jitter: every target box re-cut n times from the binarised page; one kNN query per re-cut in the SAME
        # fitted feature space; stab = share of re-cuts whose top-1 equals the box's unjittered top-1.
        pages = json.load(open(os.path.join(a.out, 'pages.json')))
        cache, inks, rnd = {}, {}, np.random.default_rng(a.jitter_seed)
        tiles, owner = [], []
        for n, i in enumerate(tgt):
            r = rows[i]
            if r['page'] not in inks:
                g = _page_grey(a.out, r['page'], cache)
                k = binarise(g, a.jitter_rel)
                inks[r['page']] = cv2.morphologyEx(k, cv2.MORPH_OPEN, np.ones((2, 2), np.uint8)) \
                    if min(g.shape) > 2500 else k
            mh = float(pages.get(r['page'], {}).get('median_h') or float(r['h']) / float(r['rh']))
            for t in jitter_tiles(inks[r['page']], r, mh, jit, a.jitter_px, a.jitter_scale, rnd):
                tiles.append(t); owner.append(n)
        Q = proj(np.array([t[0] for t in tiles]), [t[1] for t in tiles], [t[2] for t in tiles])
        dq, iq = nn.kneighbors(Q, n_neighbors=min(len(cand), a.knn + 1))
        iq = cand[iq]
        for q, n in enumerate(owner):
            _, v = vote(dq[q], iq[q], tgt[n])
            jres.setdefault(n, []).append(max(v, key=v.get))
    out = []
    for n, i in enumerate(tgt):
        pairs, votes = vote(d[n], ix[n], i)
        dd = [x for x, _ in pairs[:a.knn]]
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
        if jit:
            j0, js = jres[n][0], jres[n][1:]
            row['stab'] = f'{sum(c == best for c in js) / len(js):.2f}'
            row['k1_j'] = collections.Counter(js).most_common(1)[0][0]
            row['k1_0'] = j0
        out.append(row)
    out.sort(key=lambda r: (r['page'], r['line'], r['pos']))
    cols = (['page'] if allp else []) + ['line', 'box', 'pos', 'x', 'y', 'w', 'h', 'code', 'dist', 'share',
                                        'cluster_code', 'marks']
    if a.topk > 1:
        cols += [f'{v}{k + 1}' for k in range(a.topk) for v in 'kds']
    if jit:
        cols += ['stab', 'k1_j', 'k1_0']
    with open(a.tsv, 'w') as f:
        f.write('\t'.join(cols) + '\n')
        for r in out:
            f.write('\t'.join(str(r[c]) for c in cols) + '\n')
    agree = sum(r['code'] == r['cluster_code'] for r in out)
    print(f'{a.page}: {len(out)} boxes classified; kNN code = cluster code for {agree}; '
          f'{sum(r["code"] != "_" for r in out)} cipher codes')
    if jit:
        st = np.array([float(r['stab']) for r in out])
        print(f'--jitter {jit}: stab mean {st.mean():.3f}, share stab=1 {np.mean(st == 1):.3f}, share < 0.6 '
              f'{np.mean(st < 0.6):.3f}; unjittered re-cut top-1 = stored top-1 for '
              f'{sum(r["k1_0"] == r["code"] for r in out)}/{len(out)} (re-cut fidelity)')
    if a.strips and not allp:
        strips(a, out, [m for m in mrows.values() if m['page'] == a.page])


def classify_boxes(a, path, nn, cand, lab, proj, vote):
    """--boxes (TXE3-5 BOXES, 11 Oct 2026): kNN-classify boxes that are not atlas rows. Each box is re-cut from its
    own image (column crop|image|page: a file path, or a name in pages.json) with jitter_tiles's unjittered re-cut
    (binarise at --jitter-rel, keep the components touching the window's central half, 48x48 bitmap), projected into the
    atlas's fitted feature space and voted on by the atlas's labelled boxes exactly as a stored box is. rh/rw are
    h/mh, w/mh with mh = --boxes-median-h, else the median h of the file's kind=sign boxes (all boxes if no kind
    column), printed. Output columns as classify's, cluster_code empty, marks empty; line/pos from the file's
    line and order|pos columns when present, else the image name and file order."""
    rows = list(csv.DictReader(open(path), delimiter='\t'))
    if not rows:
        sys.exit(f'--boxes: {path} is empty')
    col = next((c for c in ('crop', 'image', 'page') if c in rows[0]), None)
    if not col or not all(k in rows[0] for k in 'xywh'):
        sys.exit('--boxes: needs columns box_id, crop|image|page, x, y, w, h')
    sign_rows = [r for r in rows if r.get('kind', 'sign') == 'sign'] or rows
    mh = float(a.boxes_median_h) if a.boxes_median_h else float(np.median([float(r['h']) for r in sign_rows]))
    pages = {}
    pj = os.path.join(a.out, 'pages.json')
    if os.path.exists(pj):
        pages = json.load(open(pj))
    inks, tiles = {}, []
    for r in rows:
        src = r[col]
        if src not in inks:
            img_path = pages.get(src, {}).get('image', src) if not os.path.exists(src) else src
            g = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
            if g is None:
                sys.exit(f'--boxes: cannot read image {img_path!r} for {src!r}')
            k = binarise(g, a.jitter_rel)
            inks[src] = cv2.morphologyEx(k, cv2.MORPH_OPEN, np.ones((2, 2), np.uint8)) if min(g.shape) > 2500 else k
        rr = dict(x=int(float(r['x'])), y=int(float(r['y'])), w=max(1, int(float(r['w']))), h=max(1, int(float(r['h']))))
        tiles.append(jitter_tiles(inks[src], rr, mh, 0, 0, 0.0, np.random.default_rng(0))[0])
    Q = proj(np.array([t[0] for t in tiles]), [t[1] for t in tiles], [t[2] for t in tiles])
    dq, iq = nn.kneighbors(Q)
    iq = cand[iq]
    out = []
    for n, r in enumerate(rows):
        pairs, votes = vote(dq[n], iq[n], -1)
        dd = [x for x, _ in pairs[:a.knn]]
        best = max(votes, key=votes.get)
        line = r.get('line') or os.path.splitext(os.path.basename(r[col]))[0]
        pos = r.get('order') or r.get('pos') or str(n + 1)
        row = dict(page=r[col], line=line, box=r.get('box_id') or r.get('sid') or f'b{n + 1}', pos=pos,
                   x=int(float(r['x'])), y=int(float(r['y'])), w=int(float(r['w'])), h=int(float(r['h'])), code=best,
                   dist=f'{dd[0]:.3f}', share=f'{votes[best] / sum(votes.values()):.2f}', cluster_code='', marks='',
                   kind=r.get('kind', 'sign'))
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
    cols = ['page', 'line', 'box', 'pos', 'x', 'y', 'w', 'h', 'code', 'dist', 'share', 'cluster_code', 'marks', 'kind']
    if a.topk > 1:
        cols += [f'{v}{k + 1}' for k in range(a.topk) for v in 'kds']
    with open(a.tsv, 'w') as f:
        f.write('\t'.join(cols) + '\n')
        for r in out:
            f.write('\t'.join(str(r[c]) for c in cols) + '\n')
    print(f'--boxes {path}: {len(out)} boxes classified from {len(inks)} image(s), median_h {mh:.1f}; '
          f'{sum(r["code"] != "_" for r in out)} cipher codes')


def train_labels(path, rnd=None, known=None):
    """--train-labels TSV (MQS-CLASSIFY-ROUNDS, 9 Oct 2026; Lasry 2026 HistoCrypt "train, correct, retrain"): columns
    box (or sid), code [, round]. Returns {box: code} for rows with round <= rnd (no round column: every row is round 1;
    rnd None: all rows; rnd 0: none). Empty codes are skipped; a later row for the same box wins (a correction in a
    later round overrides an earlier one). Boxes absent from signs.tsv are an error, not a silent no-op."""
    out = {}
    with open(path) as f:
        rd = csv.DictReader((ln for ln in f if not ln.startswith('#')), delimiter='\t')
        key = 'box' if 'box' in rd.fieldnames else 'sid'
        if key not in rd.fieldnames or 'code' not in rd.fieldnames:
            sys.exit(f'--train-labels {path}: needs columns box (or sid) and code')
        rows = sorted(((int(r.get('round') or 1), n, r) for n, r in enumerate(rd)), key=lambda t: t[:2])
        for rr, _, r in rows:                   # round order, then file order: the latest correction wins
            if (rnd is not None and rr > rnd) or not (r['code'] or '').strip():
                continue
            out[r[key]] = r['code'].strip()
    bad = sorted(set(out) - known) if known is not None else []
    if bad:
        sys.exit(f'--train-labels: {len(bad)} boxes not in signs.tsv, e.g. {bad[:3]}')
    return out


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
                # odd positions solid orange, even dashed blue; the printed position number is the non-colour key
                col = OVERLAY_ORANGE if b['pos'] % 2 else OVERLAY_BLUE
                if b['pos'] % 2:
                    cv2.rectangle(img, (b['x'] - cx0, b['y'] - y0), (b['x'] + b['w'] - cx0, b['y'] + b['h'] - y0), col, 2)
                else:
                    _dashed_rect(img, b['x'] - cx0, b['y'] - y0, b['w'], b['h'], col, 2)
                cv2.putText(img, str(b['pos']), (b['x'] - cx0, band.shape[0] + 16 + 20 * (j % 2)),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.6, col, 2)
            p = os.path.join(a.strips, f'{a.page}_L{li:02d}' + (f'{"abcdefgh"[k]}' if nparts > 1 else '') + '.jpg')
            cv2.imwrite(p, img, [cv2.IMWRITE_JPEG_QUALITY, 85])
            made.append(p)
    print(f'{len(made)} strips -> {a.strips}')


def _match_fit(bm, rows, n_pca=40, size_w=3.0):
    """classify-style features with the scaler and PCA fitted on the atlas only; returns (X_atlas, transform)."""
    hg = lambda B: np.array([hog(b.astype(float) / 255, orientations=9, pixels_per_cell=(8, 8), cells_per_block=(2, 2))
                             for b in B])
    sz = lambda R: np.log(np.array([[float(r['rh']), float(r['rw'])] for r in R]))
    H = hg(bm)
    s1 = StandardScaler().fit(H)
    pca = PCA(n_components=min(n_pca, len(bm) - 1, H.shape[1]), random_state=SEED).fit(s1.transform(H))
    s2 = StandardScaler().fit(pca.transform(s1.transform(H)))
    s3 = StandardScaler().fit(sz(rows))
    tf = lambda B, R: np.hstack([s2.transform(pca.transform(s1.transform(hg(B)))), s3.transform(sz(R)) * size_w])
    return tf(bm, rows), tf


def match_ir(X, lab, Q, q=0.9):
    """IR: share of query rows within the radius (q-quantile of member distances) of their nearest centroid."""
    ks = sorted(set(lab))
    C = np.array([X[lab == k].mean(axis=0) for k in ks])
    rad = np.array([np.quantile(np.linalg.norm(X[lab == k] - C[i], axis=1), q) if (lab == k).sum() >= 3 else np.nan
                    for i, k in enumerate(ks)])
    rad = np.where(np.isnan(rad), np.nanmedian(rad), rad)
    if not len(Q):
        return float('nan')
    d = np.sqrt(((Q[:, None, :] - C[None, :, :]) ** 2).sum(axis=2))
    j = d.argmin(axis=1)
    return float((d[np.arange(len(Q)), j] <= rad[j]).mean())


def cmd_match(a):
    rows, bm = read(a.out, 'signs.tsv'), np.load(os.path.join(a.out, 'bitmaps.npz'))['signs']
    excl = set(a.exclude_page or [])
    for p in a.stored or []:
        if p not in excl:
            sys.exit(f'--stored {p}: that page is still in the atlas; add --exclude-page {p}')
    keep = [i for i, r in enumerate(rows) if r['page'] not in excl]
    X, tf = _match_fit(bm[keep], [rows[i] for i in keep])
    lab = KMeans(n_clusters=min(a.k, len(keep)), n_init=10, random_state=SEED).fit(X).labels_
    seg = argparse.Namespace(rel=0.78, mark_h=0.55, mark_above=0.3, min_area=0.12, merge_vgap=0.6, debug=False,
                             shared_mh=None, out=None)
    queries = []
    for spec in a.page or []:
        name, rest = spec.split('=', 1)
        path, box = (rest.split('@') + [None])[:2]
        S, _, _, mh = segment_page(name, path, [int(v) for v in box.split(',')] if box else None, seg)
        queries.append((name, np.array([s['bm'] for s in S]), S))
        print(f'{name}: {len(S)} signs (median height {mh:.0f}px)')
    for p in a.stored or []:
        idx = [i for i, r in enumerate(rows) if r['page'] == p]
        queries.append((p, bm[idx], [rows[i] for i in idx]))
    Qs = [tf(B, R) if len(R) else np.zeros((0, X.shape[1])) for _, B, R in queries]
    real = [match_ir(X, lab, Q, a.radius_q) for Q in Qs]
    null = []
    for s in range(1, a.shuffle + 1):
        pl = np.random.default_rng(s).permutation(lab)
        null.append([match_ir(X, pl, Q, a.radius_q) for Q in Qs])
    order = sorted(range(len(queries)), key=lambda i: -real[i])
    rank = {i: order.index(i) + 1 for i in range(len(queries))}
    with open(a.tsv, 'w') as f:
        f.write('\t'.join(['leaf', 'n_signs', 'ir', 'rank'] + [f'ir_s{s + 1}' for s in range(len(null))]) + '\n')
        for i, (name, _, R) in enumerate(queries):
            f.write('\t'.join([name, str(len(R)), f'{real[i]:.4f}', str(rank[i])] +
                               [f'{n[i]:.4f}' for n in null]) + '\n')
    print(f'atlas: {len(keep)} signs, {len(set(lab))} clusters, excluded {sorted(excl)}')
    for i in order:
        print(f'  {rank[i]:2d} {queries[i][0]:>12s} n={len(queries[i][2]):4d} IR={real[i]:.4f}')
    if a.positive:
        names = [q[0] for q in queries]
        if a.positive not in names:
            sys.exit(f'--positive {a.positive} is not a query')
        pi = names.index(a.positive)
        mg = lambda v: v[pi] - max(v[j] for j in range(len(v)) if j != pi)
        m0 = mg(real)
        line = f'positive {a.positive}: rank {rank[pi]} of {len(names)}, margin {m0:+.4f}'
        if null:
            nm = np.array([mg(n) for n in null])
            line += f'; null margins mean {nm.mean():+.4f} p95 {np.quantile(nm, 0.95):+.4f} max {nm.max():+.4f}'
        print(line)


# ---------------------------------------------------------------- classify --pair A B (TXE3-10, 11 Oct 2026)
# A one-pair discriminator on topology: loop (hole) presence and vertical position, skeleton endpoints and where they sit
# against the loop, ink above/below the loop, a 4x4 ink grid, box geometry (rh rw dy). Pure numpy + PIL. PREREG
# benchmark-tx/PREREG-txeng3-10.md; prior pair instruments tools/tx_pair_clf.py (X2 pixels+HOG on secure tiles, X2b on
# dev lines). Pool labels come only from a known answer (dev truth, S-grade secure tokens) or a person's sort; the apply
# step never reads a truth file. Test: tools/tests/test_glyph_atlas_pair.py.
PAIR_TS = [round(0.1 * i, 1) for i in range(10)]
PAIR_MIN_COVER, PAIR_MIN_ACC = 0.5, 0.95


def zhang_suen(m):
    """Thin a boolean mask to a 1-px skeleton (Zhang-Suen 1984)."""
    im = np.pad(m.astype(np.uint8), 1)
    while True:
        changed = False
        for step in (0, 1):
            P = [im[1:-1, 1:-1]]
            sh = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]   # P2..P9 clockwise from N
            for dy, dx in sh:
                P.append(im[1 + dy:im.shape[0] - 1 + dy, 1 + dx:im.shape[1] - 1 + dx])
            B = sum(P[1:])
            A = sum(((P[i] == 0) & (P[i + 1 if i < 8 else 1] == 1)).astype(np.uint8) for i in range(1, 9))
            c1 = P[2] * P[4] * P[6] if step == 0 else P[2] * P[4] * P[8]
            c2 = P[4] * P[6] * P[8] if step == 0 else P[2] * P[6] * P[8]
            kill = (P[0] == 1) & (B >= 2) & (B <= 6) & (A == 1) & (c1 == 0) & (c2 == 0)
            if kill.any():
                im[1:-1, 1:-1][kill] = 0
                changed = True
        if not changed:
            return im[1:-1, 1:-1].astype(bool)


def components(m):
    """4-connected components of a boolean mask -> label array (0 = none), count."""
    h, w = m.shape
    lab = np.zeros((h, w), int)
    n = 0
    for y in range(h):
        for x in range(w):
            if m[y, x] and not lab[y, x]:
                n += 1
                st = [(y, x)]
                lab[y, x] = n
                while st:
                    cy, cx = st.pop()
                    for ny, nx in ((cy - 1, cx), (cy + 1, cx), (cy, cx - 1), (cy, cx + 1)):
                        if 0 <= ny < h and 0 <= nx < w and m[ny, nx] and not lab[ny, nx]:
                            lab[ny, nx] = n
                            st.append((ny, nx))
    return lab, n


def topo_feats(bm, geo=(0.0, 0.0, 0.0), n=32):
    """bm: 48x48 uint8 ink high; geo: (rh, rw, dy) from signs.tsv -> 1-D feature vector (29)."""
    from PIL import Image
    ys, xs = np.nonzero(bm > 64)
    a = bm[ys.min():ys.max() + 1, xs.min():xs.max() + 1] if len(ys) else bm
    s = np.asarray(Image.fromarray(((a > 64) * 255).astype(np.uint8)).resize((n, n), Image.BILINEAR), np.float32) / 255
    M = s > 0.5
    if not M.any():
        M[n // 2, n // 2] = True
    grid = s.reshape(4, n // 4, 4, n // 4).mean(axis=(1, 3)).ravel()
    bg, nb = components(~M)
    border = set(np.unique(np.concatenate([bg[0], bg[-1], bg[:, 0], bg[:, -1]]))) - {0}
    holes = [k for k in range(1, nb + 1) if k not in border]
    ink = M.sum()
    if holes:
        k = max(holes, key=lambda k: (bg == k).sum())
        hy, hx = np.nonzero(bg == k)
        n_h, cy, area, top, bot = len(holes), hy.mean() / n, len(hy) / (n * n), hy.min(), hy.max()
    else:
        n_h, cy, area, top, bot = 0, 0.5, 0.0, n // 2, n // 2
    above, below = M[:top].sum() / ink, M[bot + 1:].sum() / ink
    sk = zhang_suen(M)
    pad = np.pad(sk.astype(int), 1)
    nbrs = sum(pad[1 + dy:n + 1 + dy, 1 + dx:n + 1 + dx] for dy in (-1, 0, 1) for dx in (-1, 0, 1) if dy or dx)
    ep = sk & (nbrs == 1)
    jn = sk & (nbrs >= 3)
    ey = np.nonzero(ep)[0]
    return np.concatenate([grid, [n_h, cy, area, above, below, ep.sum(), jn.sum(), (ey < top).sum(), (ey > bot).sum(),
                                  sk.sum() / ink], np.asarray(geo, np.float32)]).astype(np.float32)


class PairLogit:
    """L2 logistic regression, class-balanced, Newton steps; features standardised on the training set."""
    def fit(self, X, y, lam=1.0, it=30):
        self.mu, self.sd = X.mean(0), X.std(0) + 1e-6
        Z = np.hstack([np.ones((len(X), 1)), (X - self.mu) / self.sd])
        w = np.zeros(Z.shape[1])
        cw = np.where(y == 1, len(y) / (2.0 * max(y.sum(), 1)), len(y) / (2.0 * max((1 - y).sum(), 1)))
        R = lam * np.eye(Z.shape[1]); R[0, 0] = 0
        for _ in range(it):
            p = 1 / (1 + np.exp(-Z @ w))
            g = Z.T @ (cw * (p - y)) + R @ w
            H = (Z * (cw * p * (1 - p))[:, None]).T @ Z + R
            step = np.linalg.solve(H + 1e-6 * np.eye(len(w)), g)
            w -= step
            if np.abs(step).max() < 1e-6:
                break
        self.w = w
        return self

    def p1(self, X):
        Z = np.hstack([np.ones((len(X), 1)), (X - self.mu) / self.sd])
        return 1 / (1 + np.exp(-Z @ self.w))


def pair_lolo(X, y, g, lam):
    """Leave-one-group-out held-out class-1 probability per tile (0.5 where the fold has one class)."""
    ph = np.full(len(y), 0.5)
    for h in sorted(set(g)):
        tr = g != h
        if len(set(y[tr])) == 2:
            ph[~tr] = PairLogit().fit(X[tr], y[tr], lam).p1(X[~tr])
    return ph


def pair_threshold(ph, y):
    """Smallest t with decided-tile accuracy >= PAIR_MIN_ACC at coverage >= PAIR_MIN_COVER; None -> disabled."""
    conf, pred = np.abs(2 * ph - 1), (ph > 0.5).astype(int)
    for t in PAIR_TS:
        d = conf > t
        if d.sum() >= PAIR_MIN_COVER * len(y) and (pred[d] == y[d]).mean() >= PAIR_MIN_ACC:
            return t, float((pred[d] == y[d]).mean()), int(d.sum())
    return None, float((pred == y).mean()), 0


def _pair_truth_lines(path, lines):
    """Pool step only: truth homophone sets for the named lines (scored, unflagged). Never called for an applied line."""
    lines = set(lines)
    out = {}
    with open(path) as f:
        rows = [l.rstrip('\n').split('\t') for l in f if not l.startswith('#')]
    head = rows[0]
    il, ip, it, ist = (head.index(c) for c in ('line', 'pos', 'truth', 'status'))
    ifl = head.index('flag') if 'flag' in head else None
    for r in rows[1:]:
        if r[il] in lines and r[ist] == 'scored' and not (r[ifl] if ifl is not None and len(r) > ifl else ''):
            out[(r[il], r[ip])] = set(r[it].split('|'))
    return out


def _pair_map(path, lines=None):
    with open(path, newline='') as f:
        r = csv.reader(f, delimiter='\t')
        head = next(r)
        ix = [head.index(c) for c in ('sid', 'line', 'pos', 'op')]          # named columns only: never 'truth'
        return {(row[ix[1]], row[ix[2]]): row[ix[0]] for row in r
                if row[ix[3]] == '1:1' and (lines is None or row[ix[1]] in lines)}


def pair_pool(a, sig, idx, exclude_lines=()):
    """-> list of (sid, label 0/1, group, source). Labels only from dev truth, S-grade secure tokens, a person's sort."""
    A, B = a.pair
    pool, seen = [], set()
    if a.pool_dev:
        L = [r for r in read(os.path.dirname(a.pool_dev), os.path.basename(a.pool_dev))]
        lines = {r['line'] for r in L} - set(exclude_lines)
        truth = _pair_truth_lines(a.truth, lines)
        box = _pair_map(a.map, lines)
        for r in L:
            k = (r['line'], r['pos'])
            if r['line'] not in lines or r['sign'] not in (A, B) or k not in box or k not in truth:
                continue
            ina, inb = A in truth[k], B in truth[k]
            if ina != inb and box[k] in idx:
                pool.append((box[k], int(inb), r['line'], 'dev')); seen.add(box[k])
    if a.pool_secure:
        for r in read(os.path.dirname(a.pool_secure), os.path.basename(a.pool_secure)):
            if r['grade'] == 'S' and r['code'] in (A, B) and r['page'] not in a.exclude_pool_page and r['sid'] in idx \
                    and r['sid'] not in seen:
                pool.append((r['sid'], int(r['code'] == B), sig[idx[r['sid']]]['page'], 'sec')); seen.add(r['sid'])
    if a.pool_owner:
        om = {r['sid']: r for r in read(os.path.dirname(a.owner_map), os.path.basename(a.owner_map))}
        for r in read(os.path.dirname(a.pool_owner), os.path.basename(a.pool_owner)):
            m = om.get(r['sid'])
            if r['new_sign'] in (A, B) and m and m['box'] and m['dup'] == '0' and float(m['dist_px']) <= 10 \
                    and m['box'] in idx and m['box'] not in seen and sig[idx[m['box']]]['page'] not in a.exclude_pool_page:
                pool.append((m['box'], int(r['new_sign'] == B), sig[idx[m['box']]]['page'], 'own')); seen.add(m['box'])
    return pool


# ---------------------------------------------------------------- TXE4-5 PAIR-BANK (12 Oct 2026): feature bank, L1 selection,
# machine-agreed pools, gated maps, several pairs per call. PREREG benchmark-tx/PREREG-txeng4-5.md; test
# tools/tests/test_glyph_atlas_pairbank.py. No owner, dev-truth or secure tile enters a --pool-agreed pool: its labels are the
# two blind passes' agreement, joined to atlas boxes by a tools/box_token_align.py map that tools/join_check.py has PASSed.
def _hog_small(s, cells=4, bins=8):
    """Gradient-orientation histogram per cell of an n x n float ink image (unsigned, 0..pi), L1-normalised per cell."""
    gy, gx = np.gradient(s)
    mag, ang = np.hypot(gx, gy), np.arctan2(gy, gx) % np.pi
    n = s.shape[0]; c = n // cells
    out = []
    for i in range(cells):
        for j in range(cells):
            m = mag[i * c:(i + 1) * c, j * c:(j + 1) * c].ravel(); t = ang[i * c:(i + 1) * c, j * c:(j + 1) * c].ravel()
            h, _ = np.histogram(t, bins=bins, range=(0, np.pi), weights=m)
            out.append(h / (h.sum() + 1e-6))
    return np.concatenate(out)


def bank_feats(bm, geo=(0.0, 0.0, 0.0)):
    """--feature-bank: topology (topo_feats, 29) + 4x4 zoning of the uncropped 48x48 tile (16) + HOG of the cropped 32x32 ink
    (4x4 cells x 8 bins = 128) -> 173 features; L1 selection per pair picks the ones that matter (l1_select)."""
    from PIL import Image
    topo = topo_feats(bm, geo)
    s48 = (bm > 64).astype(np.float32)
    zone = s48.reshape(4, 12, 4, 12).mean(axis=(1, 3)).ravel()
    ys, xs = np.nonzero(bm > 64)
    a = bm[ys.min():ys.max() + 1, xs.min():xs.max() + 1] if len(ys) else bm
    s = np.asarray(Image.fromarray(((a > 64) * 255).astype(np.uint8)).resize((32, 32), Image.BILINEAR), np.float32) / 255
    return np.concatenate([topo, zone, _hog_small(s)]).astype(np.float32)


def l1_select(X, y, lam1=0.05, it=400, min_keep=4):
    """L1-logistic (proximal gradient, class-balanced, standardised columns): indices of the non-zero weights, at least
    min_keep (the largest |w| if fewer survive). Deterministic."""
    mu, sd = X.mean(0), X.std(0) + 1e-6
    Z = (X - mu) / sd
    n, d = Z.shape
    n1 = max(int((y == 1).sum()), 1); n0 = max(n - n1, 1)
    sw = np.where(y == 1, n / (2.0 * n1), n / (2.0 * n0))
    eta = 1.0 / (0.25 * sw.max() * (np.linalg.norm(Z, 2) ** 2) / n + 1e-9)
    w, b = np.zeros(d), 0.0
    for _ in range(it):
        p = 1 / (1 + np.exp(-(Z @ w + b)))
        r = sw * (p - y)
        w = w - eta * (Z.T @ r) / n; b -= eta * r.sum() / n
        w = np.sign(w) * np.maximum(np.abs(w) - eta * lam1, 0)
    keep = np.nonzero(w)[0]
    if len(keep) < min_keep:
        keep = np.argsort(-np.abs(w))[:min_keep]
    return np.sort(keep)


def pair_lolo_sel(X, y, g, lam, select):
    """Leave-one-group-out held-out p(B) with the feature selection redone inside every fold (no held-out label leaks into
    the selection); select=False is pair_lolo."""
    if not select:
        return pair_lolo(X, y, g, lam)
    ph = np.zeros(len(y))
    for grp in sorted(set(g)):
        tr = g != grp
        if len(set(y[tr])) < 2:
            ph[~tr] = 0.5; continue
        keep = l1_select(X[tr], y[tr])
        ph[~tr] = PairLogit().fit(X[tr][:, keep], y[tr], lam).p1(X[~tr][:, keep])
    return ph


def _require_map(a, path):
    """R4a: a box<->position map is read only through tools/join_check.require() (a PASS sidecar whose sha256 matches), or
    with an explicit, printed --allow-unchecked-join REASON."""
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    import join_check
    return join_check.require(path, getattr(a, 'allow_unchecked_join', None))


def pool_agreed(a, sig, idx, exclude_lines, applied_lines, seen, pool):
    """--pool-agreed AGREE.tsv:MAP.tsv (repeatable): tiles at positions where the two blind passes agree (AGREE: line pos
    sign), joined to boxes by MAP (box_token_align output, op 1:1 only, gated by join_check). Never a tile from an excluded
    (applied) line; a tile on an applied page is grouped by its line, any other by its page."""
    A, B = a.pair
    for spec in a.pool_agreed or ():
        agree_p, map_p = spec.rsplit(':', 1)
        _require_map(a, map_p)
        box = _pair_map(map_p)
        for r in read(os.path.dirname(agree_p), os.path.basename(agree_p)):
            k = (r['line'], r['pos']); sid = box.get(k)
            if r['line'] in exclude_lines or r['sign'] not in (A, B) or sid is None or sid not in idx or sid in seen:
                continue
            grp = r['line'] if r['line'] in applied_lines else sig[idx[sid]]['page']
            pool.append((sid, int(r['sign'] == B), grp, 'agr')); seen.add(sid)
    return pool


def cmd_classify_pairs(a):
    """--pairs FILE (A B per line): one gated model per pair, outputs suffixed _A_B; then --tsv = the base with every pair's
    flips, a position flipped by two pairs kept as the base (conflict), --touched with a pair column."""
    pairs = [l.split() for l in open(a.pairs) if l.strip() and not l.startswith('#')]
    Lu = read(os.path.dirname(a.apply_unit), os.path.basename(a.apply_unit))
    flips, allt = {}, []
    stem = lambda p, A, B: (p and re.sub(r'(\.tsv)?$', f'_{A}_{B}\\1', p, 1))
    base_tsv, base_rep, base_t = a.tsv, a.report, a.touched
    for A, B in pairs:
        a.pair = [A, B]; a.tsv, a.report, a.touched = stem(base_tsv, A, B), stem(base_rep, A, B), stem(base_t, A, B) or stem(base_tsv + '.touched', A, B)
        cmd_classify_pair(a)
        for r in read(os.path.dirname(a.touched), os.path.basename(a.touched)):
            r['pair'] = f'{A}/{B}'; allt.append(r)
            if r['out'] != r['L']:
                flips.setdefault((r['line'], r['pos']), []).append(r['out'])
    out, conflicts = [], 0
    for r in Lu:
        f = flips.get((r['line'], r['pos']))
        sign = r['sign']
        if f and len(set(f)) == 1 and len(f) == 1:
            sign = f[0]
        elif f:
            conflicts += 1
        out.append((r['line'], r['pos'], sign))
    with open(base_tsv, 'w') as f:
        f.write('line\tpos\tsign\n' + ''.join('\t'.join(r) + '\n' for r in out))
    tc = ['pair', 'line', 'pos', 'sid', 'L', 'm', 't', 'out']
    with open(base_t or base_tsv + '.touched', 'w') as f:
        f.write('\t'.join(tc) + '\n' + ''.join('\t'.join(str(r[c]) for c in tc) + '\n' for r in allt))
    ch = sum(1 for o, r in zip(out, Lu) if o[2] != r['sign'])
    print(f'--pairs {len(pairs)}: combined {base_tsv}: changed {ch}, conflicts kept as base {conflicts}')
    return 0



def cmd_classify_pair(a):
    A, B = a.pair
    sig = read(a.out, 'signs.tsv')
    idx = {r['sid']: i for i, r in enumerate(sig)}
    bm = np.load(os.path.join(a.out, 'bitmaps.npz'))['signs']
    fcache = {}

    feat = bank_feats if getattr(a, 'feature_bank', False) else topo_feats

    def fx(sid):
        if sid not in fcache:
            r = sig[idx[sid]]
            fcache[sid] = feat(bm[idx[sid]], (float(r['rh']), float(r['rw']), float(r['dy'])))
        return fcache[sid]

    Lu = read(os.path.dirname(a.apply_unit), os.path.basename(a.apply_unit)) if a.apply_unit else []
    ulines = sorted({r['line'] for r in Lu})
    if a.map and Lu:
        _require_map(a, a.map)
    if getattr(a, 'exclude_own_line', False) and Lu:
        folds = [(i + 1, [h], [h]) for i, h in enumerate(ulines)]
    elif a.loo_lines:
        if not a.pool_dev or os.path.abspath(a.apply_unit) != os.path.abspath(a.pool_dev):
            sys.exit('--loo-lines: --apply-unit must be the --pool-dev file itself')
        folds = [(i + 1, [h], [h]) for i, h in enumerate(ulines)]
    else:
        if a.pool_dev and Lu:
            dl = {r['line'] for r in read(os.path.dirname(a.pool_dev), os.path.basename(a.pool_dev))}
            if dl & set(ulines):
                sys.exit('--apply-unit shares lines with --pool-dev: use --loo-lines or another unit')
        folds = [(0, ulines, [])]
    box = _pair_map(a.map, set(ulines)) if Lu else {}
    rep, out, touched = [], [], []
    for fold, alines, excl in folds:
        pool = pair_pool(a, sig, idx, excl)
        pool = pool_agreed(a, sig, idx, set(excl), set(ulines), {p[0] for p in pool}, pool)
        y = np.array([p[1] for p in pool], int)
        if getattr(a, 'reverse_labels', False) and len(y):
            y = 1 - y
        g = np.array([p[2] for p in pool])
        rng = np.random.default_rng(a.seed * 1000 + fold) if a.seed else None
        if rng is not None and len(y):
            y = rng.permutation(y)
        X = np.stack([fx(p[0]) for p in pool]) if pool else np.zeros((0, 29))
        sel = bool(getattr(a, 'feature_bank', False))
        row = dict(fold=fold, pool_a=int((y == 0).sum()), pool_b=int((y == 1).sum()), groups=len(set(g)), lolo_acc='',
                   t='', decided='', chance='', shuffled='', enabled=0, kept='')
        model, t, keep = None, None, None
        if row['pool_a'] >= 3 and row['pool_b'] >= 3 and row['groups'] >= 2:
            ph = pair_lolo_sel(X, y, g, a.lam, sel)
            t, acc, nd = pair_threshold(ph, y)
            if a.force_t is not None:
                t, nd = a.force_t, int((np.abs(2 * ph - 1) > a.force_t).sum())
            row.update(lolo_acc=f'{((ph > 0.5).astype(int) == y).mean():.3f}', chance=f'{max(y.mean(), 1 - y.mean()):.3f}',
                       t='' if t is None else t, decided=nd, enabled=int(t is not None))
            if a.shuffle_lolo and fold == folds[0][0]:
                accs = []
                for s in range(1, a.shuffle_lolo + 1):
                    ys = np.random.default_rng(10 ** 6 + s).permutation(y)
                    accs.append(((pair_lolo_sel(X, ys, g, a.lam, sel) > 0.5).astype(int) == ys).mean())
                row['shuffled'] = ' '.join(f'{v:.3f}' for v in accs)
            if t is not None:
                keep = l1_select(X, y) if sel else np.arange(X.shape[1])
                row['kept'] = len(keep)
                model = PairLogit().fit(X[:, keep], y, a.lam)
        rep.append(row)
        for r in Lu:
            if r['line'] not in alines:
                continue
            s = sign = r['sign']
            sid = box.get((r['line'], r['pos']))
            if model is not None and s in (A, B) and sid in idx:
                pb = float(model.p1(fx(sid)[None][:, keep])[0])
                pp = pb if s == A else 1 - pb
                m = 2 * pp - 1
                if m > t:
                    sign = B if s == A else A
                touched.append(dict(line=r['line'], pos=r['pos'], sid=sid, L=s, m=f'{m:.3f}', t=t, out=sign))
            out.append(dict(line=r['line'], pos=r['pos'], sign=sign))
    cols = ['fold', 'pool_a', 'pool_b', 'groups', 'lolo_acc', 't', 'decided', 'chance', 'enabled', 'shuffled', 'kept']
    print(f'--pair {A} {B}: ' + (f'labels permuted seed {a.seed}; ' if a.seed else '') + '\t'.join(cols))
    for r in rep:
        print('\t'.join(str(r[c]) for c in cols))
    if a.report:
        with open(a.report, 'w') as f:
            f.write('\t'.join(cols) + '\n' + ''.join('\t'.join(str(r[c]) for c in cols) + '\n' for r in rep))
    if Lu:
        order = {(r['line'], r['pos']): i for i, r in enumerate(Lu)}
        out.sort(key=lambda r: order[(r['line'], r['pos'])])
        with open(a.tsv, 'w') as f:
            f.write('line\tpos\tsign\n' + ''.join(f"{r['line']}\t{r['pos']}\t{r['sign']}\n" for r in out))
        ch = sum(1 for o, r in zip(out, Lu) if o['sign'] != r['sign'])
        print(f'applied {os.path.basename(a.apply_unit)}: positions {len(out)}, considered {len(touched)}, changed {ch} -> {a.tsv}')
        if a.touched:
            with open(a.touched, 'w') as f:
                tc = ['line', 'pos', 'sid', 'L', 'm', 't', 'out']
                f.write('\t'.join(tc) + '\n' + ''.join('\t'.join(str(r[c]) for c in tc) + '\n' for r in touched))
    return 0



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
    s.add_argument('--split-wide', type=float, default=0.0, help='default mode: split a merged sign box wider than this x median height into pieces at column-ink minima (0 = off; TXE3-6)')
    s.add_argument('--split-piece', type=float, default=1.0, help='--split-wide: pieces = max(2, round(width / (this x median height))) (1.0)')
    s.add_argument('--split-random', type=int, default=None, help='--split-wide: cut at uniformly random columns with this seed instead of ink minima (the rule-3 control)')
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
    k.add_argument('--labels', help='labels.json (not needed with --pair)')
    k.add_argument('--page', help="the page whose boxes are classified, or 'all' (or give --boxes; not needed with --pair)")
    k.add_argument('--boxes', help='TXE3-5: classify these boxes (TSV box_id, crop|image|page, x, y, w, h [, line, '
                   'order|pos, kind]) re-cut from their own image, instead of atlas rows; see the docstring')
    k.add_argument('--boxes-median-h', type=float, help='--boxes: median sign height (px) for the size features '
                   '(default: the median h of the file\'s kind=sign boxes)')
    k.add_argument('--tsv', required=True, help='output box list')
    k.add_argument('--knn', type=int, default=5)
    k.add_argument('--pca-scale', choices=['unit', 'shared'], default='unit')
    k.add_argument('--exclude-page', action='store_true',
                   help="never let the target page's own boxes vote (kNN over other pages' boxes only); use it when the "
                        "page is new and unlabelled, otherwise its boxes vote '_' for each other (debosnys c4, 25 Sept 2026)")
    k.add_argument('--strips', help='directory for per-line strips with box numbers')
    k.add_argument('--train-labels', help='TSV box (or sid), code [, round]: a person\'s sorted piles applied as per-box '
                   'overrides on top of labels.json before the kNN vote (human-in-the-loop retrain)')
    k.add_argument('--round', type=int, help='--train-labels: use rows with round <= this (0 = none; default all)')
    k.add_argument('--only-train-labels', action='store_true',
                   help='the --train-labels boxes are the ONLY voters: every other box is held and labels.json contributes '
                        'nothing (TXE3-7, 11 Oct 2026: a kNN from a person\'s sorted tiles alone)')
    k.add_argument('--topk', type=int, default=1, help='also write the k best codes with distance and vote share (3)')
    k.add_argument('--pool', type=int, default=40, help='neighbour pool for codes outside the --knn voters (40)')
    k.add_argument('--holdout', action='append', help='box-id prefix that never votes (repeatable)')
    k.add_argument('--jitter', type=int, default=0,
                   help='TXE-J (9 Oct 2026, idea M11): classify each target box N more times (5) under seeded crop '
                        'perturbations (shift, scale) and add columns stab (share of jitters whose top-1 = the '
                        'unjittered top-1), k1_j (majority jittered top-1), k1_0 (the unjittered re-cut\'s top-1). '
                        'Answers: the lattice had no per-position measure of how sure the IMAGE is')
    k.add_argument('--jitter-px', type=int, default=2, help='--jitter: max shift in page px, each axis (2)')
    k.add_argument('--jitter-scale', type=float, default=0.05, help='--jitter: max relative rescale of the window (0.05)')
    k.add_argument('--jitter-seed', type=int, default=1, help='--jitter: RNG seed (1)')
    k.add_argument('--jitter-rel', type=float, default=0.78, help="--jitter: binarisation rel, as segment's --rel (0.78)")
    k.add_argument('--max-w', type=int, default=1800, help='cut a line strip into parts under this width (px)')
    k.add_argument('--pair', nargs=2, metavar=('A', 'B'), help='TXE3-10: one look-alike pair discriminator on topology '
                   'features (loop position, stroke endpoints, ink grid, box geometry); pool = --pool-dev + --pool-secure + '
                   '--pool-owner tiles; applied at --apply-unit positions whose sign is A or B; writes --tsv (line pos sign)')
    k.add_argument('--pool-dev', help="--pair: a units label file (labels_<unit>.tsv) whose positions are labelled by the "
                   "truth file's homophone set (dev lines only; the truth is read for those lines and never for --apply-unit)")
    k.add_argument('--pool-secure', help='--pair: secure_tokens.tsv (sid code page grade), grade S, pages not in --exclude-pool-page')
    k.add_argument('--pool-owner', help="--pair: settled_labels.tsv (sid old_sign new_sign status), a person's sort")
    k.add_argument('--owner-map', help='--pair: owner_map.tsv (sid atlas_page box dist_px dup) mapping --pool-owner sids to atlas boxes')
    k.add_argument('--exclude-pool-page', action='append', default=[], help='--pair: atlas page never in the pool (the eval leaves)')
    k.add_argument('--map', help='--pair: box<->position map (sid fol line pos sign op; the truth column is never read)')
    k.add_argument('--truth', help='--pair: truth TSV (line pos ref_sign truth plain status flag), read for --pool-dev lines only')
    k.add_argument('--apply-unit', help='--pair: units label file (line pos sign) to apply to; output --tsv has every position')
    k.add_argument('--loo-lines', action='store_true', help='--pair: --apply-unit is the --pool-dev file itself; each line is '
                   'predicted by a pool that excludes that line (its truth never trains the model voting on it)')
    k.add_argument('--seed', type=int, default=0, help='--pair: > 0 permutes the pool labels (shuffled-label control)')
    k.add_argument('--shuffle-lolo', type=int, default=0, help='--pair: also report LOGO accuracy for N label permutations')
    k.add_argument('--lam', type=float, default=1.0, help='--pair: L2 strength of the logistic model (1.0)')
    k.add_argument('--force-t', type=float, help='--pair: ignore the LOGO threshold rule and apply at this margin (a '
                   'declared secondary control: lets a shuffled-label model flip at argmax so its fixed/broken can vary)')
    k.add_argument('--touched', help='--pair: TSV of the positions considered (line pos sid L m t out)')
    k.add_argument('--report', help='--pair: TSV report (fold pool_a pool_b groups lolo_acc t decided chance shuffled)')
    k.add_argument('--pairs', help='TXE4-5: FILE of pairs (A B per line) -> one gated model per pair, outputs suffixed _A_B, '
                                   'and --tsv/--touched combined (a position two pairs flip is kept as the base)')
    k.add_argument('--pool-agreed', action='append', default=[], metavar='AGREE.tsv:MAP.tsv',
                   help='TXE4-5: reader-agreed tiles (AGREE: line pos sign) joined by a join_check-PASSed box_token_align '
                        'MAP (op 1:1); never from an excluded/applied line; repeatable')
    k.add_argument('--feature-bank', action='store_true', help='TXE4-5: topology + 4x4 zoning + HOG (173) with L1-logistic '
                                                               'feature selection per pair (redone inside every LOGO fold)')
    k.add_argument('--exclude-own-line', action='store_true', help='TXE4-5: vote each applied line with a model whose pool '
                                                                   'excludes that line (own-ink pools)')
    k.add_argument('--reverse-labels', action='store_true', help='TXE4-5: swap the pair members in the pool (a control '
                                                                 'that must break)')
    k.add_argument('--allow-unchecked-join', help='reproduce an old result only: skip join_check.require() on --map and '
                                                  '--pool-agreed maps, printing this reason')
    m = sp.add_parser('match')
    m.add_argument('--out', required=True, help='the atlas directory (signs.tsv, bitmaps.npz)')
    m.add_argument('--page', action='append', help='NAME=IMAGE[@x0,y0,x1,y1]: a candidate leaf, segmented fresh')
    m.add_argument('--stored', action='append', help="an atlas page's own rows as a query (must also be --exclude-page)")
    m.add_argument('--exclude-page', action='append', help='atlas page left out of the fit (the held-out leaf), repeatable')
    m.add_argument('--k', type=int, default=140, help='k-means clusters on the atlas (140, the Birago atlas README)')
    m.add_argument('--radius-q', type=float, default=0.9, help='cluster radius = this quantile of member distances (0.9)')
    m.add_argument('--shuffle', type=int, default=0, help='shuffled-label null: N label permutations (seeds 1..N)')
    m.add_argument('--positive', help='query name whose margin over the others is printed')
    m.add_argument('--tsv', required=True, help='output table')
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
     'crop': cmd_crop, 'match': cmd_match}[a.cmd](a)


if __name__ == '__main__':
    main()
