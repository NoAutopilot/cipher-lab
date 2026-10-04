#!/usr/bin/env python3
"""PISANY-SORTER (4 Oct 2026): owner sign-sorter inputs for Pisany to Henry III, Rome, 17 Jun 1585, BnF fr.16045 f.75r
(Gallica canvas 156), the 22 cipher lines PIS-T transcribed (two blind Sonnet passes, err_2reader 0.430, inventory unsettled).
Worked example: ciphers/fr16106-vivonne-longlee-1579/sorter/build_inputs.py (same method, same file layout).

Pages: one strip per line, following the line's own slant (traces()), cut from the public Gallica native region already on
disk (images/src_ark_12148_btv1b9060906j_f156_680_1830_3060_3520.jpg; images/manifest.json names it), full region width so
every strip shares one x origin, written to sorter/pages/f75_L<nn>.jpg -- the sorter draws lines n-1 / n+1 above and below
at the same x window. The clear opening line and the cipher tail of clear line 6 above L01 are not cut (PIS-T did not read them).
Tiles: APPROXIMATE. A column ink profile splits each strip into blobs; the blob list is fitted to the line's number of aligned
columns in tx/ciphertext_draft.tsv (tools/reconcile_passes.py alignment of pass A and pass B) by merging the narrowest blob
into its nearer neighbour or halving the widest one, and column k gets blob k. Signs touch and the superscript crosses sit
between lines, so a tile can be one or two positions from the sign its label came from; the context view decides.
Labels (piles): agreed column -> that label (e.g. `S15`); split column -> `A/B` (pass A / pass B, e.g. `S10/S41`) when that
pair occurs at least MINPAIR times, else `split-rare`; a column only one reader saw -> `<sign>+1r` when it occurs at least
MINPAIR times, else `one-reader`. A reader's trailing `?` (unsure) is dropped from the pile name; `?[shape]` (no matching
cell) becomes `NOCELL`. family = pass A's label (or the single reader's), so split piles sit beside their agreed pile.
Pile names are the shape labels of tx/SIGNS.md (cells of Tomokiyo's 1585 table); no plaintext value is in sorter/.
L02: pass A read only 29 signs against B's 54, so most of that line sits in `+1r` / `one-reader` piles.
Focus: the four confusable groups both readers named (NOTES.md: S15/S40/S13/S61, S10/S41/S02, S36/S42/S23, S46/S48/S25)
first, then the other most frequent splits; up to three tiles per pair, at most 40.

  python3 ciphers/fr16045-pisany-rome-1585/sorter/build_inputs.py     (writes sorter/signs.tsv, labels.tsv, focus.tsv, fit.tsv, pages/)
"""
import csv, json
from collections import Counter, defaultdict
from pathlib import Path
from PIL import Image
import numpy as np
T = Path(__file__).resolve().parents[1]; S = T / 'sorter'; P = S / 'pages'; P.mkdir(exist_ok=True)
INK = 150; MINPAIR = 4; PER_PAIR = 3; NFOCUS = 40; Y0 = 1830      # region top in canvas px
GROUPS = [{'S15', 'S40', 'S13', 'S61'}, {'S10', 'S41', 'S02'}, {'S36', 'S42', 'S23'}, {'S46', 'S48', 'S25'}]
SRC = 'src_ark_12148_btv1b9060906j_f156_680_1830_3060_3520.jpg'
src = Image.open(T / 'images' / SRC).convert('L'); ink = np.array(src) < INK   # paper ~215, stain ~130-190, ink ~70-130
H, W = ink.shape; PITCH = 140; WIN = 300


def smooth(v, k):
    return np.convolve(v.astype(float), np.ones(k) / k, 'same')


def anchors():
    """Two points per line from PIS-T's own crops (eye-checked by PIS-T; the readers read these): the middle of the s1 box
    (x 0-1600 of the region, centre x 800) and of the s2 box (x 1460-3060, centre x 2260), region px. L08 s2 and L09 use
    images/fix_f75_L08_L09.py's re-cut lines (y = c0 + 0.05 x, c0 = 1133 and 1270), since the tool's crops jumped there."""
    man = json.load(open(T / 'images' / 'manifest.json'))['iiif_lines']; out = defaultdict(dict)
    for e in man:
        if e['crop'].startswith('f75_L') and e['band'] <= 22 and e['box'][0] in (680, 2140):
            out[e['band']][e['segment']] = (e['box'][1] + e['box'][3]) / 2 - Y0
    out[8][2] = 1133 + .05 * 2260; out[9] = {1: 1270 + .05 * 800, 2: 1270 + .05 * 2260}
    return [(out[n][1], out[n][2]) for n in range(1, 23)]


def traces():
    """Line centre y(x) per line: the straight line through the two anchors(), then in each 300 px window (step 150) moved
    to the row-profile peak within +-16 px of it if there is one, median-smoothed over five windows, interpolated in x.
    Peak-following on its own (Longlee's method, and a joint 22-line version) slid onto the next line at the right edge:
    the lines are evenly spaced, so a one-pitch slip scores as well as the truth."""
    xs = list(range(0, W - WIN // 2, WIN // 2)); out = []
    for y1, y2 in anchors():
        b = (y2 - y1) / 1460; ys = {}
        for x in xs:
            xm = x + WIN / 2; yl = y1 + b * (xm - 800); lo = int(max(0, yl - 16)); hi = int(min(H, yl + 17))
            pr = smooth(ink[:, x:x + WIN].sum(1), 31)[lo:hi]
            k = int(np.argmax(pr)); ys[xm] = lo + k if 0 < k < len(pr) - 1 else yl
        xx = sorted(ys); yy = np.array([ys[x] for x in xx], float)
        yy = np.array([np.median(yy[max(0, i - 2):i + 3]) for i in range(len(yy))])
        out.append(np.interp(np.arange(W), xx, yy))
    return out


def blobs(core, gap=3, minw=6):
    col = core.sum(0) > 1
    col[:15] = False; col[2870:] = False     # the scan's dark right edge starts at x ~2880
    segs, s, last = [], None, -99
    for x, v in enumerate(col):
        if v:
            s = x if s is None else s; last = x
        elif s is not None and x - last > gap:
            segs.append([s, last]); s = None
    if s is not None:
        segs.append([s, last])
    return [g for g in segs if g[1] - g[0] >= minw]


def fit(segs, n, prof):
    """Merge the narrowest blob into its nearer neighbour while too many; while too few, split the widest blob at the
    lowest point of the line's column ink profile in its middle 60% (Longlee halves it; signs here touch more)."""
    segs = [list(g) for g in segs]
    while len(segs) > n:
        i = min(range(len(segs)), key=lambda k: segs[k][1] - segs[k][0])
        if i == 0: j = 1
        elif i == len(segs) - 1: j = i - 1
        else: j = i - 1 if segs[i][0] - segs[i - 1][1] < segs[i + 1][0] - segs[i][1] else i + 1
        a, b = sorted((i, j)); segs[a] = [segs[a][0], segs[b][1]]; del segs[b]
    while len(segs) < n:
        i = max(range(len(segs)), key=lambda k: segs[k][1] - segs[k][0]); a, b = segs[i]
        lo, hi = a + int(.2 * (b - a)), b - int(.2 * (b - a)); m = lo + int(np.argmin(prof[lo:hi + 1])) if hi > lo else (a + b) // 2
        m = min(max(m, a), b - 1)
        segs[i:i + 1] = [[a, m], [m + 1, b]]
    return segs


def norm(x):
    x = (x or '').strip()
    if x in ('', '-'): return x
    if x.startswith('?'): return 'NOCELL'
    return x.rstrip('?')


def main():
    global signs, labels
    draft = defaultdict(list)
    for r in csv.DictReader(open(T / 'tx' / 'ciphertext_draft.tsv'), delimiter='\t'):
        a = norm(r['sign']) or 'UNREAD'
        if r['why'] == 'agree':
            draft[r['line']].append(('agree', a, a))
        else:
            who, other = r['alt'].split(':', 1); other = norm(other) or 'UNREAD'
            A, B = (a, other) if who == 'B' else (other, a)
            draft[r['line']].append(('gap' if r['why'] == 'gap' else 'differ', A, B))
    pairs = Counter((A, B) for v in draft.values() for k, A, B in v if k == 'differ')
    ones = Counter((A if A != '-' else B) for v in draft.values() for k, A, B in v if k == 'gap')
    signs, labels, cand, stats = [], [], defaultdict(list), []
    for n, tr in enumerate(traces(), 1):
        page = f'f75_L{n:02d}'; line = f'L{n:02d}'
        y0 = max(0, int(tr.min() - .75 * PITCH)); y1 = min(H, int(tr.max() + .75 * PITCH))
        src.crop((0, y0, W, y1)).save(P / f'{page}.jpg', quality=82)
        ty = np.arange(H)[:, None]; cen = tr[None, :]
        core = ink & (np.abs(ty - cen) < .40 * PITCH); zone = ink & (np.abs(ty - cen) < .60 * PITCH)
        bl = blobs(core); cols = draft[line]; boxes = fit(bl, len(cols), smooth(core.sum(0), 5))
        stats.append((page, len(bl), len(cols)))
        for k, ((kind, A, B), (x0, x1)) in enumerate(zip(cols, boxes), 1):
            sid = f'{page}_{k:02d}'
            ys = np.where(zone[:, x0:x1 + 1].sum(1) > 0)[0]
            ty0, ty1 = (int(ys.min()), int(ys.max())) if len(ys) else (y0, y1 - 1)
            signs.append(dict(sid=sid, page=page, x=x0, y=ty0 - y0, w=x1 - x0 + 1, h=ty1 - ty0 + 1))
            if kind == 'agree':
                lab = fam = A
            elif kind == 'differ':
                lab = f'{A}/{B}' if pairs[(A, B)] >= MINPAIR else 'split-rare'; fam = A
                cand[(A, B)].append(sid)
            else:
                one = A if A != '-' else B; lab = f'{one}+1r' if ones[one] >= MINPAIR else 'one-reader'; fam = one
            labels.append(dict(sid=sid, sign=lab, family=fam))


    def ingroup(p):
        return any(p[0] in g and p[1] in g for g in GROUPS)


    order = sorted(pairs, key=lambda p: (not ingroup(p), -pairs[p]))
    focus = []
    for A, B in order:
        sids = cand[(A, B)]; step = max(1, len(sids) // PER_PAIR)
        for sid in sids[::step][:PER_PAIR]:
            tag = ' (confusable group named by both readers)' if ingroup((A, B)) else ''
            focus.append((sid, f'{sid.split("_", 1)[1]}: reader A {A}, reader B {B} (x{pairs[(A, B)]} on the page){tag}; which, or another sign?'))
        if len(focus) >= NFOCUS:
            break
    for name, rows in (('signs.tsv', signs), ('labels.tsv', labels)):
        with open(S / name, 'w', newline='') as o:
            w = csv.DictWriter(o, fieldnames=list(rows[0]), delimiter='\t'); w.writeheader(); w.writerows(rows)
    with open(S / 'focus.tsv', 'w') as o:
        for sid, q in focus[:NFOCUS]:
            o.write(f'{sid}\t{q}\n')
    with open(S / 'fit.tsv', 'w') as o:
        o.write('page\tblobs\tcolumns\n'); o.writelines(f'{p}\t{b}\t{c}\n' for p, b, c in stats)
    print(len(signs), 'tiles;', len(stats), 'pages;', len(set(l['sign'] for l in labels)), 'piles;', len(focus[:NFOCUS]), 'focus tiles')


if __name__ == '__main__':
    main()
