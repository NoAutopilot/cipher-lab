#!/usr/bin/env python3
"""LONGLEE-SORTER (4 Oct 2026): owner sign-sorter inputs for the Saint-Gouard cipher of 2 Mar 1580, fr.16107 c107 left
(f.101v), the one page VIV-T transcribed (two blind Sonnet passes, err_2reader 0.576, inventory unsettled).

Pages: one strip per line (following the line's own slant, see traces()), cut from the public Gallica native region already on disk
(images/src_ark_12148_btv1b9009661v_f107_550_550_3800_5350.jpg; the iiif_lines.py manifest names it),
full region width so every strip shares one x origin, written to sorter/pages/f101v_L<nn>.jpg -- the sorter draws
lines n-1 / n+1 above and below at the same x window.
Tiles: APPROXIMATE. A column ink profile splits each strip into blobs; the blob list is fitted to the line's number of
aligned columns in tx/ciphertext_draft.tsv (tools/reconcile_passes.py nw alignment of pass A and pass B) by merging the
narrowest blob into its nearer neighbour or halving the widest one, and column k gets blob k. Because the readers'
lines are themselves off (both readers said they picked up signs from neighbouring lines) and blobs touch, a tile can
sit one or two positions from the sign its label came from; the context view decides, never the label.
Labels (piles): agreed column -> that label (e.g. `x`); split column -> `A/B` (pass A / pass B, e.g. `a/c`) when that
pair occurs at least MINPAIR times, else `split-rare`; a column only one reader saw -> `<sign>+1r` (one reader) when it
occurs at least MINPAIR times, else `one-reader`. family = pass A's label (or the single reader's), so split piles sit
beside their agreed pile. Labels are the provisional shape names of tx/SIGNS.md; no plaintext value is in sorter/.
Focus: for the most frequent split pairs, up to three tiles each (the context view shows the line), at most 40.

  python3 ciphers/fr16106-vivonne-longlee-1579/sorter/build_inputs.py     (writes sorter/signs.tsv, labels.tsv, focus.tsv, pages/)
"""
import csv, json
from collections import Counter, defaultdict
from pathlib import Path
from PIL import Image
import numpy as np
T = Path(__file__).resolve().parents[1]; S = T / 'sorter'; P = S / 'pages'; P.mkdir(exist_ok=True)
INK = 168; MINPAIR = 4; NFOCUS_PAIRS = 14; PER_PAIR = 3
man = json.load(open(T / 'images' / 'manifest.json'))['iiif_lines']
src = Image.open(T / 'images' / man[0]['source_file']).convert('L'); ink = np.array(src) < INK   # paper ~238, strokes 105-160, verso bleed ~190+
H, W = ink.shape; PITCH = 143; WIN = 380


def smooth(v, k):
    return np.convolve(v.astype(float), np.ones(k) / k, 'same')


def peaks(x0, x1, k=41, thr=4):
    pr = smooth(ink[:, x0:x1].sum(1), k); r = int(.45 * PITCH); out = []
    for y in range(1, H - 1):
        if pr[y] == pr[max(0, y - r):y + r].max() and pr[y] > thr and not (out and y - out[-1] < PITCH // 2):
            out.append(y)
    return out


def traces():
    """Line centre y(x) for each cipher line. Seeds = row-profile peaks in the 380 px window at x 1520-1900, which
    with one gap filled from the window to its left, finds the 33 lines of f.101v (checked against the region by eye, 4 Oct 2026; VIV-T's iiif_lines.py bands were 32: its bands 30-32 straddle lines 30-33 here); each line is then followed through
    overlapping 380 px windows (step 190) to the nearest peak within +-PITCH/3 of the last one (kept if none),
    median-smoothed over three windows and interpolated linearly in x. The iiif_lines.py bands are horizontal; the
    lines are not, so tiles follow these traces instead."""
    seeds = peaks(1520, 1900)
    for y in peaks(1140, 1520):     # f.101v L04 has a blank stretch at x 1520-1900: fill any seed gap > 1.6 pitch
        if all(abs(y - z) > .6 * PITCH for z in seeds) and any(b - a > 1.6 * PITCH and a < y < b for a, b in zip(seeds, seeds[1:])):
            seeds.append(y)
    seeds.sort(); assert len(seeds) == 33, len(seeds)
    xs = list(range(0, W - WIN // 2, WIN // 2)); pk = {x: peaks(x, min(W, x + WIN)) for x in xs}
    i0 = xs.index(1520); out = []
    for c0 in seeds:
        ys = {xs[i0]: c0}
        for rng in (xs[i0 + 1:], xs[:i0][::-1]):
            last = c0
            for x in rng:
                near = [y for y in pk[x] if abs(y - last) < PITCH / 3]
                if near:
                    last = min(near, key=lambda y: abs(y - last))
                ys[x] = last
        xx = sorted(ys); yy = np.array([ys[x] for x in xx], float)
        yy = np.array([np.median(yy[max(0, i - 1):i + 2]) for i in range(len(yy))])
        out.append(np.interp(np.arange(W), np.array(xx) + WIN / 2, yy))
    return out


def blobs(core, gap=3, minw=6):
    col = core.sum(0) > 1
    col[:450] = False; col[-40:] = False     # left margin (the cipher starts at x ~600) and the gutter's dark scan edge
    segs, s, last = [], None, -99
    for x, v in enumerate(col):
        if v:
            s = x if s is None else s; last = x
        elif s is not None and x - last > gap:
            segs.append([s, last]); s = None
    if s is not None:
        segs.append([s, last])
    return [g for g in segs if g[1] - g[0] >= minw]


def fit(segs, n):
    segs = [list(g) for g in segs]
    while len(segs) > n:
        i = min(range(len(segs)), key=lambda k: segs[k][1] - segs[k][0])
        if i == 0: j = 1
        elif i == len(segs) - 1: j = i - 1
        else: j = i - 1 if segs[i][0] - segs[i - 1][1] < segs[i + 1][0] - segs[i][1] else i + 1
        a, b = sorted((i, j)); segs[a] = [segs[a][0], segs[b][1]]; del segs[b]
    while len(segs) < n:
        i = max(range(len(segs)), key=lambda k: segs[k][1] - segs[k][0]); a, b = segs[i]; m = (a + b) // 2
        segs[i:i + 1] = [[a, m], [m + 1, b]]
    return segs


def main():
    draft = defaultdict(list)
    for r in csv.DictReader(open(T / 'tx' / 'ciphertext_draft.tsv'), delimiter='\t'):
        a, alt = r['sign'] or '?', r['alt'] if r['alt'][-1:] != ':' else r['alt'] + '?'
        if r['why'] == 'agree':
            draft[r['line']].append(('agree', a, a))
        else:
            who, other = alt.split(':', 1); other = other or '?'
            A, B = (a, other) if who == 'B' else (other, a)
            draft[r['line']].append(('gap' if r['why'] == 'gap' else 'differ', A, B))
    pairs = Counter((A, B) for ln, v in draft.items() if int(ln[-2:]) <= 29 for k, A, B in v if k == 'differ')
    ones = Counter((A if A != '-' else B) for ln, v in draft.items() if int(ln[-2:]) <= 29 for k, A, B in v if k == 'gap')
    signs, labels, cand = [], [], defaultdict(list)
    stats = []
    TR = traces()
    MAPPED = 29      # VIV-T bands 1-29 sit on lines 1-29 here (centres within 15 px); bands 30-32 straddle lines 30-33
    for n, tr in enumerate(TR, 1):
        page = f'f101v_L{n:02d}'; line = f'c107_L{n:02d}'
        y0 = max(0, int(tr.min() - .75 * PITCH)); y1 = min(H, int(tr.max() + .75 * PITCH))
        src.crop((0, y0, W, y1)).save(P / f'{page}.jpg', quality=82)
        ty = np.arange(H)[:, None]; cen = tr[None, :]
        core = ink & (np.abs(ty - cen) < .42 * PITCH); zone = ink & (np.abs(ty - cen) < .62 * PITCH)
        bl = blobs(core)
        if n <= MAPPED:
            cols = draft[line]; boxes = fit(bl, len(cols))
        else:             # no reader row belongs to this line alone: tiles are the blobs as found, in one pile
            wmed = np.median([g['w'] for g in signs]); n_est = max(len(bl), round(sum(b - a + 1 for a, b in bl) / wmed))
            boxes = fit(bl, n_est); cols = [('foot', '', '')] * n_est
        stats.append((page, len(bl), len(cols) if n <= MAPPED else ''))
        for k, ((kind, A, B), (x0, x1)) in enumerate(zip(cols, boxes), 1):
            sid = f'{page}_{k:02d}'
            ys = np.where(zone[:, x0:x1 + 1].sum(1) > 0)[0]
            ty0, ty1 = (int(ys.min()), int(ys.max())) if len(ys) else (y0, y1 - 1)
            signs.append(dict(sid=sid, page=page, x=x0, y=ty0 - y0, w=x1 - x0 + 1, h=ty1 - ty0 + 1))
            if kind == 'foot':
                lab = fam = 'foot-unplaced'
            elif kind == 'agree':
                lab, fam = (A if A not in ('', '?') else 'UNREAD'), A
            elif kind == 'differ':
                lab = f'{A}/{B}' if pairs[(A, B)] >= MINPAIR else 'split-rare'; fam = A
                cand[(A, B)].append(sid)
            else:
                one = A if A != '-' else B; lab = f'{one}+1r' if ones[one] >= MINPAIR else 'one-reader'; fam = one
            fam = fam if fam not in ('', '?', '-') else 'UNREAD'
            labels.append(dict(sid=sid, sign=lab.replace('?', 'UNREAD') if lab != 'split-rare' else lab, family=fam))
    focus = []
    for (A, B), c in pairs.most_common(NFOCUS_PAIRS):
        sids = cand[(A, B)]; step = max(1, len(sids) // PER_PAIR)
        for sid in sids[::step][:PER_PAIR]:
            focus.append((sid, f'{sid.split("_", 1)[1]}: reader A {A}, reader B {B} (x{c} on the page); which, or another sign?'))
    for name, rows in (('signs.tsv', signs), ('labels.tsv', labels)):
        with open(S / name, 'w', newline='') as o:
            w = csv.DictWriter(o, fieldnames=list(rows[0]), delimiter='\t'); w.writeheader(); w.writerows(rows)
    with open(S / 'focus.tsv', 'w') as o:
        for sid, q in focus[:40]:
            o.write(f'{sid}\t{q}\n')
    with open(S / 'fit.tsv', 'w') as o:
        o.write('page\tblobs\tcolumns\n'); o.writelines(f'{p}\t{b}\t{c}\n' for p, b, c in stats)
    print(len(signs), 'tiles;', len(stats), 'pages;', len(set(l['sign'] for l in labels)), 'piles;', len(focus[:40]), 'focus tiles')


if __name__ == '__main__':
    main()
