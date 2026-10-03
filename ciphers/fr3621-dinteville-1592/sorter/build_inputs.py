#!/usr/bin/env python3
"""DIN-SORTER (3 Oct 2026): sign-sorter inputs for BnF fr.3623 f.23r (Dinteville cipher slip with an interlinear Italian
decipherment), built the same way as ../../birago-fr3252-1571-72/sorter/build_inputs.py. Disk only, no vision call.

Source: the native region already on disk, f3623/src_ark_12148_btv1b525245007_f55_560_1780_2950_1560.jpg (Gallica
ark btv1b525245007, canvas 55, region 560,1780,2950,1560).

Rows. The slip alternates a gloss row and a cipher row, sloping about -0.055 across the region. A row ink profile taken
along that slope gives 15 text rows (one faint, 908 columns, between R6 and R7); the cipher rows are the ones whose ink covers more columns (dense rows of
closely spaced signs, 2300-2410 of 2950 columns, R7 a shorter 1948; the gloss rows above them 900-1700; threshold
1900). This assignment is checked, not
assumed: the DIN-23P pilot's masked cipher strip (f3623/pilot/r4_cipher_s1.jpg) correlates best (r 0.73) with the
source at centre ~811, the 4th dense row, and its gloss strip (r 0.93) at ~724, the sparse row above it; the script
asserts it. That gives SEVEN cipher rows R1-R7 (the brief said six; DIN-23P's own selection sheet counted R1-R7).

Pages. Each cipher row is cut as a deskewed strip (per column, rows centre +-ROWHALF of a line tracked left to right in
200 px windows from the profile centre), written to sorter/pages/f23r_R<n>.jpg. Deskewing is a vertical shift per
column (slope ~3 degrees), so sign shapes are unchanged to the eye.

Tiles. A column ink profile over the row's core (+-CORE px of the tracked centre; the gloss rows sit 75-90 px away)
splits the strip into blobs; blobs with no pen-black pixel are dropped, and a blob wider than 1.7x the row's median blob
width is halved repeatedly. R4 is fitted to the DIN-23P consensus length (the pilot's two passes joined on their
overlap and aligned, f3623/pilot/align_pilot.py's own functions), so its tiles carry labels by position. Sign boxes are
APPROXIMATE: where two signs touch or one sign is in two pieces a tile can be one position off; the sorter's context view
shows the line, and a bad cut goes to BAD-CUT.

Labels. Only R4 was read (DIN-23P passes A and B). Where A and B agree the tile is seeded with that sheet label; where
they split it is UNREAD and goes to focus.tsv with both readings; every other row starts UNREAD (the build command uses
--auto-clusters to group UNREAD tiles by shape). 'plus' (pass A's spelling) is normalised to '+' (pass B's) before the
comparison. No sign values appear anywhere in this folder, only sheet labels.

  python3 sorter/build_inputs.py      (from ciphers/fr3621-dinteville-1592; writes sorter/signs.tsv, labels.tsv,
                                       focus.tsv, pages/, rows.json)
"""
import csv, json, sys
from pathlib import Path
from PIL import Image
import numpy as np

T = Path(__file__).resolve().parents[1]; S = T / 'sorter'; P = S / 'pages'
SRC = T / 'f3623' / 'src_ark_12148_btv1b525245007_f55_560_1780_2950_1560.jpg'
sys.path.insert(0, str(T / 'f3623' / 'pilot'))
import align_pilot as AP  # noqa: E402

SLOPE, INK, ROWHALF, CORE = -0.055, 110, 62, 30
P.mkdir(parents=True, exist_ok=True)


def row_centres(a):
    """14 text rows along SLOPE; returns [(centre at x=0, ink-column count)]."""
    H, W = a.shape; xs = np.arange(0, W, 2); prof = []
    for c in range(-200, H + 200):
        ys = (c + SLOPE * xs).astype(int); ok = (ys >= 0) & (ys < H)
        prof.append((a[ys[ok], xs[ok]] < INK).sum())
    prof = np.convolve(prof, np.ones(15) / 15, 'same'); out = []
    for i in range(1, len(prof) - 1):
        lo, hi = max(0, i - 30), min(len(prof), i + 31)
        if prof[i] == prof[lo:hi].max() and prof[i] > 60:
            c = i - 200
            if out and c - out[-1][0] < 30:
                continue
            cols = sum(1 for x in range(W) if (a[max(0, int(c + SLOPE * x) - 25):max(0, int(c + SLOPE * x) + 25), x] < INK).any())
            out.append((c, cols))
    return out


def track(a, c0, win=200, step=20):
    """the line's centre per column: per window, the densest ink row within +-step of the slope prediction (carrying
    the previous window's drift forward)."""
    H, W = a.shape; ink = (a < INK).astype(float); cs = np.zeros(W, int); drift = 0
    for x in range(0, W, win):
        pred = int(round(c0 + SLOPE * (x + win / 2))) + drift
        lo, hi = max(0, pred - step), min(H, pred + step + 1)
        prof = np.convolve(ink[:, x:x + win].sum(1), np.ones(15) / 15, 'same')[lo:hi]
        if len(prof) and prof.max() > 0:
            drift = lo + int(prof.argmax()) - int(round(c0 + SLOPE * (x + win / 2)))
        xs = np.arange(x, min(W, x + win)); cs[xs] = np.round(c0 + SLOPE * xs).astype(int) + drift
    return cs


def strip(a, rgb, cs):
    H, W = a.shape; out = np.full((2 * ROWHALF + 1, W, 3), 255, np.uint8)
    for x in range(W):
        for r in range(2 * ROWHALF + 1):
            y = cs[x] - ROWHALF + r
            if 0 <= y < H:
                out[r, x] = rgb[y, x]
    return out


def blobs(g, gap=4, minw=6):
    core = g[ROWHALF - CORE:ROWHALF + CORE + 1] < INK
    col = core.sum(0) > 1; segs, s, last = [], None, -99
    for x, v in enumerate(col):
        if v:
            s = x if s is None else s; last = x
        elif s is not None and x - last > gap:
            segs.append([s, last]); s = None
    if s is not None:
        segs.append([s, last])
    segs = [q for q in segs if q[1] - q[0] >= minw and g[:, q[0]:q[1] + 1].min() <= 60]
    med = float(np.median([q[1] - q[0] for q in segs]))
    out = []
    for q in segs:
        parts = [q]
        while any(p[1] - p[0] > 1.7 * med for p in parts):
            i = max(range(len(parts)), key=lambda k: parts[k][1] - parts[k][0]); a0, b0 = parts[i]; m = (a0 + b0) // 2
            parts[i:i + 1] = [[a0, m], [m + 1, b0]]
        out += parts
    return out


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


def r4_pairs():
    norm = lambda xs: ['+' if t == 'plus' else t for t in xs]
    a1, a2 = AP.read_pass('passA.txt'); b1, b2 = AP.read_pass('passB.txt')
    A, _ = AP.join_segments(norm(a1), norm(a2)); B, _ = AP.join_segments(norm(b1), norm(b2))
    return AP.lcs_align(A, B)


rgb = np.array(Image.open(SRC).convert('RGB')); a = rgb.mean(2)
rows = row_centres(a)
split = 1900   # gloss rows 900-1700 ink columns, cipher rows 1948-2410 (R7 is a shorter line)
cipher = [c for c, n in rows if n > split]
assert len(cipher) == 7, rows
assert abs(cipher[3] - 811) <= 15, cipher        # R4 = the DIN-23P pilot row (pilot strip match, centre ~811)
signs, labels, focus, meta = [], [], [], []
pairs = r4_pairs()
for k, c in enumerate(cipher, 1):
    page = f'f23r_R{k}'; cs = track(a, c)
    st = strip(a, rgb, cs); Image.fromarray(st).save(P / f'{page}.jpg', quality=85)
    g = st.mean(2); bl = blobs(g)
    if k == 4:
        print("R4 raw blobs", len(bl), "fitted to", len(pairs)); bl = fit(bl, len(pairs))
    meta.append(dict(row=k, page=page, centre_x0=int(c), tiles=len(bl)))
    for i, (x0, x1) in enumerate(bl, 1):
        sid = f'f23r_R{k}_{i:02d}'
        sub = g[:, x0:x1 + 1] < INK
        # vertical extent: ink rows connected to the core band
        ys = np.where(sub.any(1))[0]; ys = ys[(ys >= ROWHALF - CORE - 25) & (ys <= ROWHALF + CORE + 25)]
        y0, y1 = (int(ys.min()), int(ys.max())) if len(ys) else (ROWHALF - CORE, ROWHALF + CORE)
        signs.append(dict(sid=sid, page=page, x=int(x0), y=y0, w=int(x1 - x0 + 1), h=y1 - y0 + 1))
        lab = 'UNREAD'
        if k == 4:
            pa, pb = pairs[i - 1]
            if pa == pb and pa not in (None, '?'):
                lab = pa
            else:
                focus.append((sid, f"R4.{i}: pass A {pa or '-'}, pass B {pb or '-'}; which sheet label?"))
        labels.append(dict(sid=sid, sign=lab, family=lab))
for name, rs in (('signs.tsv', signs), ('labels.tsv', labels)):
    with open(S / name, 'w', newline='') as o:
        w = csv.DictWriter(o, fieldnames=list(rs[0]), delimiter='\t'); w.writeheader(); w.writerows(rs)
with open(S / 'focus.tsv', 'w') as o:
    for sid, q in focus:
        o.write(f'{sid}\t{q}\n')
json.dump(dict(slope=SLOPE, rows_all=[dict(centre_x0=int(c), ink_cols=int(n)) for c, n in rows], split=split,
               cipher_rows=meta), open(S / 'rows.json', 'w'), indent=1)
print(len(signs), 'tiles;', len(meta), 'rows', [m['tiles'] for m in meta], ';', len(focus), 'focus;',
      sum(l['sign'] != 'UNREAD' for l in labels), 'seeded;', len(set(l['sign'] for l in labels)), 'piles')
