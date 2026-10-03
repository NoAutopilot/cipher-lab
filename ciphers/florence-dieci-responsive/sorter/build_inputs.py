#!/usr/bin/env python3
"""SORTER-FLORENCE (3 Oct 2026): sign-sorter inputs for ASFi Dieci di Balia Responsive filza 8 c.127 (DECODE R3766,
26 Dec 1430), the A2-FLO3 pilot stretch only (crops c127b1_L01-L04 = the leaf's cipher lines 6-9), built the same
way as ../birago-fr3252-1571-72/sorter/build_inputs.py. No model read any image to build this folder.

Pages: one strip per line cut from images/IMG_R3766_I23025_P.jpg, x from segment 1's left edge to segment 2's right
edge and y from the band in images/c127/manifest.json padded 30 px, written to sorter/pages/c127_L0<band>.jpg.

Tokens and labels: passes/c127b1_recon.tsv (A2-FLO3's reconciliation of the two blind passes against the same crops)
gives the sign sequence per crop with the s1/s2 overlap already dropped; its clear words (tokens starting '=') are not
tiles. Each recon position is aligned to pass A and pass B (difflib on the cipher tokens, '?[..]' kept as '?', 'o /'
read as the one sign 'o/' the reconciler merged; '·' where a pass wrote nothing there). labels.tsv carries the recon label; focus.tsv is every tile where
the two passes did not both write the recon label (a split, a '?', or a sign one pass skipped), with both readings.

Boxes (APPROXIMATE, no eye check): a segment's cipher signs are placed inside its own x range ([0,1980) for s1,
[1980,3860) for s2, strip coordinates; the 100 px overlap belongs to s1, since the recon dropped s2's overlap signs).
A column ink profile over the line's core rows (tracked left to right from the band centre) splits the range into
blobs. Where the segment also holds clear words (L01_s1 starts with one, L02_s2 and L04_s2 end with them, L03_s2
starts with them), the cipher run is taken as the n * pxs px of ink at its cipher end, pxs being the median width
per sign measured on the all-cipher segments (L01_s2, L02_s1, L04_s1); the blob list is then fitted to the sign count
by merging the narrowest blob into its nearer neighbour, or halving the widest. A tile can be a position or more off,
most likely next to a clear word; the sorter's context view shows the line, and a badly cut tile goes to BAD-CUT.

  python3 sorter/build_inputs.py      (from ciphers/florence-dieci-responsive; writes sorter/signs.tsv, labels.tsv,
                                       focus.tsv, pages/)
"""
import csv, difflib, json, re
from pathlib import Path
from PIL import Image
import numpy as np
T = Path(__file__).resolve().parents[1]; IM = T / 'images'; S = T / 'sorter'; P = S / 'pages'
P.mkdir(exist_ok=True)
PAD = 30
THR = 90                                   # ink: the paper is dark (median grey ~175, 10th pct ~130), so 120 caught stains
SEG = {1: (0, 1980), 2: (1980, 3860)}      # strip x range owned by each segment
CLEAR_SIDE = {'c127b1_L03_s2': 'L'}       # the recon row drops its clear words; its note: signs come 'after clear ... di potrebbe'


def tsv(p):
    return list(csv.DictReader(open(p), delimiter='\t'))


def norm(toks):
    out = []
    for t in toks:
        if t.startswith('='):
            continue
        if t.startswith('?'):
            t = '?'
        if t == '/' and out and out[-1] == 'o':
            out[-1] = 'o/'; continue
        out.append(t)
    return out


def split_tokens(s):
    return re.findall(r'\?\[[^\]]*\]|\S+', s)


def strip(band):
    es = [e for e in json.load(open(IM / 'c127' / 'manifest.json'))['iiif_lines'] if e['band'] == band]
    x0 = min(e['box'][0] for e in es); y0 = min(e['box'][1] for e in es)
    x1 = max(e['box'][2] for e in es); y1 = max(e['box'][3] for e in es)
    src = Image.open(IM / es[0]['source_file']); c = (y0 + y1) // 2
    y0 = max(0, y0 - PAD); y1 = min(src.height, y1 + PAD)
    return src.crop((x0, y0, x1, y1)), c - y0


def local_centres(a, c, thr=THR, win=200, step=20):
    ink = (a < thr).astype(float); cs = np.zeros(a.shape[1], int); prev = c
    for x in range(0, a.shape[1], win):
        lo, hi = max(0, prev - step), min(a.shape[0], prev + step + 1)
        prof = np.convolve(ink[:, x:x + win].sum(1), np.ones(21) / 21, 'same')[lo:hi]
        if prof.max() > 0:
            prev = lo + int(prof.argmax())
        cs[x:x + win] = prev
    return cs


def blobs(a, cs, gap=4, minw=8, thr=THR, core=40):
    rows = np.arange(a.shape[0])[:, None]
    mid = (a < thr) & (np.abs(rows - cs[None, :]) <= core)
    col = (mid.sum(0) > 1) & (mid.mean(0) < .6)
    segs, s, last = [], None, -99
    for x, v in enumerate(col):
        if v:
            s = x if s is None else s; last = x
        elif s is not None and x - last > gap:
            segs.append([s, last]); s = None
    if s is not None:
        segs.append([s, last])
    segs = [g for g in segs if g[1] - g[0] >= minw]
    return [g for g in segs if a[:, g[0]:g[1] + 1].min() <= 60]      # no pen-black pixel: shading, not ink


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


def readings(recon, other):
    """For each recon position, the token the other pass wrote there ('-' where it wrote nothing)."""
    out = ['·'] * len(recon)
    for tag, i1, i2, j1, j2 in difflib.SequenceMatcher(None, recon, other, autojunk=False).get_opcodes():
        if tag in ('equal', 'replace'):
            for k in range(i1, i2):
                j = j1 + (k - i1)
                if j < j2:
                    out[k] = other[j]
    return out


rec = {r['crop']: r for r in tsv(T / 'passes' / 'c127b1_recon.tsv')}
pa = {r['crop']: r['tokens'] for r in tsv(T / 'passes' / 'c127b1_passA.tsv')}
pb = {r['crop']: r['tokens'] for r in tsv(T / 'passes' / 'c127b1_passB.tsv')}
crops = sorted(pa)
units = []          # (band, seg, crop, recon cipher tokens, clear side or None)
for crop in crops:
    band, seg = int(crop[8:10]), int(crop[-1])
    raw = split_tokens(rec[crop]['tokens']) if crop in rec else []
    toks = norm(raw)
    if not toks:
        continue
    clear = [i for i, t in enumerate(raw) if t.startswith('=')]
    side = CLEAR_SIDE.get(crop) or (None if not clear else ('L' if clear[0] == 0 else 'R'))
    units.append((band, seg, crop, toks, side))

strips = {}
for band in sorted({u[0] for u in units}):
    im, c = strip(band); page = f'c127_L{band:02d}'; im.save(P / f'{page}.jpg', quality=85)
    a = np.array(im.convert('L')); strips[band] = (page, im, a, local_centres(a, c))

seg_blobs = {}
for band, seg, crop, toks, side in units:
    page, im, a, cs = strips[band]; lo, hi = SEG[seg]
    seg_blobs[crop] = [[g[0] + lo, g[1] + lo] for g in blobs(a[:, lo:hi], cs[lo:hi])]
pure = [u for u in units if u[4] is None]
pxs = float(np.median([(seg_blobs[u[2]][-1][1] - seg_blobs[u[2]][0][0]) / len(u[3]) for u in pure]))

signs, labels, focus = [], [], []
pos_in_line = {}
for band, seg, crop, toks, side in units:
    page, im, a, cs = strips[band]; bl = seg_blobs[crop]; n = len(toks)
    if side == 'L':                        # clear words first: the signs are the last n * pxs px of ink
        cut = bl[-1][1] - n * pxs; bl = [g for g in bl if g[1] > cut]; bl[0][0] = max(bl[0][0], int(cut))
    elif side == 'R':                      # clear words last: the signs are the first n * pxs px of ink
        cut = bl[0][0] + n * pxs; bl = [g for g in bl if g[0] < cut]; bl[-1][1] = min(bl[-1][1], int(cut))
    boxes = fit(bl, n)
    ra, rb = readings(toks, norm(split_tokens(pa[crop]))), readings(toks, norm(split_tokens(pb[crop])))
    for i, (t, (x0, x1)) in enumerate(zip(toks, boxes)):
        p = pos_in_line[band] = pos_in_line.get(band, 0) + 1
        sid = f'c127_L{band:02d}_{p:02d}'
        cc = int(cs[(x0 + x1) // 2]); top, bot = max(0, cc - 55), min(im.height, cc + 55)
        sub = a[top:bot, x0:x1 + 1]; ys = np.where((sub < 120).sum(1) > 0)[0]
        y0, y1 = (top + int(ys.min()), top + int(ys.max())) if len(ys) else (top, bot - 1)
        signs.append(dict(sid=sid, page=page, x=x0, y=y0, w=x1 - x0 + 1, h=y1 - y0 + 1))
        labels.append(dict(sid=sid, sign=t, family=t))
        if not (ra[i] == rb[i] == t):       # '·' = that pass wrote no sign at this position
            focus.append((sid, f'{crop[4:]}.{i + 1}: pass A {ra[i]}, pass B {rb[i]}, reconciler {t}; '
                               f'which form is it, or X_NEW?'))
for name, rs in (('signs.tsv', signs), ('labels.tsv', labels)):
    with open(S / name, 'w', newline='') as o:
        w = csv.DictWriter(o, fieldnames=list(rs[0]), delimiter='\t'); w.writeheader(); w.writerows(rs)
with open(S / 'focus.tsv', 'w') as o:
    for sid, q in focus:
        o.write(f'{sid}\t{q}\n')
print(len(signs), 'signs;', len(strips), 'pages;', len(focus), 'focus tiles;', len({l['sign'] for l in labels}),
      'piles; px per sign on all-cipher segments', round(pxs))
