#!/usr/bin/env python3
"""SORTER-BIRAGO2 (3 Oct 2026): sign-sorter inputs for fr.3252 f.117r (no.77, 13 Mar 1572), built the same way as
../nevers-birago-fr3251-1572/sorter/build_inputs.py.

Pages are the ten cipher lines cut from the public Gallica region image already on disk
(images/f117/src_ark_12148_btv1b9060232m_f118_4380_1400_3150_1300.jpg, canvas 118; band boxes from
images/f117/manifest.json, which are in that file's own pixel coordinates), one strip per line, written to
sorter/pages/f117_L<band>.jpg. The whole block is cipher, so every line is fitted whole ('W'): a column ink profile
over the line's core rows (within 32 px of the line's own
centre, tracked left to right from the manifest centre since the lines are skewed; the band overlaps the
neighbouring lines' ink) splits the strip into blobs and the blob list is fitted to the line's sign count by merging the narrowest blob into its
nearer neighbour, or halving the widest. A blob wider than 120 px starting in the last tenth of the strip is the scan's
shaded right edge and is dropped first, as is any blob with no pen-black pixel (min grey > 60). Strips are the manifest
bands padded 40 px top and bottom, since the skewed line ends of L06-L09 ran off the fixed bands. L10 is a short closing line, so its signs are taken from the left ('L').
Sign boxes are APPROXIMATE: where two signs touch or one sign is in two pieces a tile can be one position off; the
sorter's context view shows the line. Labels come from harvest/f117/la/passD.tsv (the 2-of-3 reconcile after the
look-alike pass); '?' becomes UNREAD. focus.tsv is harvest/f117/la/focus.tsv (the 12 tiles the look-alike pass left
unsettled) with its ids renamed to this folder's tile ids. No values are written anywhere in sorter/.

  python3 sorter/build_inputs.py      (from ciphers/birago-fr3252-1571-72; writes sorter/signs.tsv, labels.tsv,
                                       focus.tsv, pages/)
"""
import csv, json
from pathlib import Path
from PIL import Image
import numpy as np
T = Path(__file__).resolve().parents[1]; IM = T / 'images' / 'f117'; LA = T / 'harvest' / 'f117' / 'la'
S = T / 'sorter'; P = S / 'pages'
P.mkdir(exist_ok=True)
ANCHOR = {'L10': 'L'}   # default 'W'
PAD = 40                # strips are the manifest bands +-40 px: the skewed line ends ran off the fixed bands


def strip(band):
    es = [e for e in json.load(open(IM / 'manifest.json'))['iiif_lines'] if e['band'] == band]
    x0 = min(e['box'][0] for e in es); y0 = min(e['box'][1] for e in es)
    x1 = max(e['box'][2] for e in es); y1 = max(e['box'][3] for e in es)
    src = Image.open(IM / es[0]['source_file']); y0 = max(0, y0 - PAD); y1 = min(src.height, y1 + PAD)
    c = es[0]['params']['centres_given'][band - 1] - y0      # the line's own centre inside the strip
    return src.crop((x0, y0, x1, y1)), c


def local_centres(a, c, thr=120, win=200, step=22):
    """The lines are skewed (L06-L09 fall about 60 px across the strip): track the line left to right, per 200 px window
    taking the row of densest ink within +-22 px of the previous window's centre, starting from the manifest centre."""
    ink = (a < thr).astype(float); cs = np.zeros(a.shape[1], int); prev = c
    for x in range(0, a.shape[1], win):
        lo, hi = max(0, prev - step), min(a.shape[0], prev + step + 1)
        prof = np.convolve(ink[:, x:x + win].sum(1), np.ones(21) / 21, 'same')[lo:hi]
        if prof.max() > 0:
            prev = lo + int(prof.argmax())
        cs[x:x + win] = prev
    return cs


def blobs(im, c, gap=4, minw=8, thr=120, core=32):
    a = np.array(im.convert('L')); cs = local_centres(a, c, thr)
    rows = np.arange(a.shape[0])[:, None]
    mid = (a < thr) & (np.abs(rows - cs[None, :]) <= core)   # the line's own core rows: the band overlaps its neighbours' ink
    mid = mid[max(0, c - 60 - core):c + 60 + core]
    segs = [g for g in _segs(mid, gap) if g[1] - g[0] >= minw]
    lo = max(0, c - 60 - core)
    faint = [g for g in segs if a[lo:c + 60 + core, g[0]:g[1] + 1].min() > 60]   # shading at the scan edge has no pen-black pixel
    return [g for g in segs if g not in faint], cs


def _segs(mid, gap):
    col = (mid.sum(0) > 1) & (mid.mean(0) < .6)
    segs, s, last = [], None, -99
    for x, v in enumerate(col):
        if v:
            s = x if s is None else s; last = x
        elif s is not None and x - last > gap:
            segs.append([s, last]); s = None
    if s is not None:
        segs.append([s, last])
    return segs


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


rows = list(csv.DictReader(open(LA / 'passD.tsv'), delimiter='\t'))
by = {}
for r in rows:
    by.setdefault(r['passage'], []).append(r)
signs, labels = [], []
for psg, rs in by.items():
    band = int(psg[1:]); page = f'f117_L{band:02d}'
    im, c = strip(band); im.save(P / f'{page}.jpg', quality=85)
    bl, cs = blobs(im, c); n = len(rs)
    bl = [g for g in bl if not (g[0] > im.width * .9 and g[1] - g[0] > 120)]   # right-edge scan shading, not a sign
    if ANCHOR.get(psg, 'W') == 'W':
        boxes = fit(bl, n)
    else:
        boxes = [g for g in bl if g[1] - g[0] >= 15][:n]
    for r, (x0, x1) in zip(rs, boxes):
        sid = f"f117_{psg}_{int(r['pos']):02d}"
        cc = int(cs[(x0 + x1) // 2]); top, bot = max(0, cc - 60), min(im.height, cc + 60)          # vertical extent searched near the line only
        a = np.array(im.convert('L').crop((x0, top, x1 + 1, bot)))
        ys = np.where((a < 120).sum(1) > 0)[0]
        y0, y1 = (top + int(ys.min()), top + int(ys.max())) if len(ys) else (top, bot - 1)
        signs.append(dict(sid=sid, page=page, x=x0, y=y0, w=x1 - x0 + 1, h=y1 - y0 + 1))
        lab = r['sign_id'] if r['sign_id'] not in ('', '?') else 'UNREAD'
        labels.append(dict(sid=sid, sign=lab, family=lab))
for name, rs in (('signs.tsv', signs), ('labels.tsv', labels)):
    with open(S / name, 'w', newline='') as o:
        w = csv.DictWriter(o, fieldnames=list(rs[0]), delimiter='\t'); w.writeheader(); w.writerows(rs)
have = {s['sid'] for s in signs}; focus = []
for line in open(LA / 'focus.tsv'):
    old, q = line.rstrip('\n').split('\t', 1)
    _, psg, pos = old.split('_')
    sid = f'f117_{psg}_{int(pos):02d}'
    assert sid in have, sid
    focus.append((sid, q))
with open(S / 'focus.tsv', 'w') as o:
    for sid, q in focus:
        o.write(f'{sid}\t{q}\n')
print(len(signs), 'signs;', len(set(s['page'] for s in signs)), 'pages;', len(focus), 'focus tiles;',
      len(set(l['sign'] for l in labels)), 'piles')
