#!/usr/bin/env python3
"""R7-OLDSORT (6 Oct 2026): sign-sorter inputs for blocks A (folio 54, leaf 001) and C2 (folio 56, leaf 006) of
Nationaal Archief 1.01.02 inv. 2442, built from the line crops R7-OLDA already cut (images/crops_AC2/, manifest_A.json,
manifest_C2.json; no network), the same way as ../../matignon-mayenne-1586/sorter/build_inputs.py.

Pages: each line's three overlapping deskewed crops (s1, s2, s3, native scale, 900 px wide) pasted at their manifest x
offsets into one strip, sorter/pages/<A|C2>_L<nn>.jpg; C2_L09 (the word under line 8) is its single hand-cut crop. The
deskew of each segment is the same, so the joins are close but can be a few px off vertically.
Tiles: this is a cursive hand, so signs touch and an ink profile cannot find them directly. Two steps: (1) a column ink
profile over the strip's middle rows splits it into word blobs, fitted to the reconciled draft's word count for that line
(transcription/reconciled_AC2_R7OLDA.tsv): the gaps between words are not reliable in this hand (tried 6 Oct: breaking at
the widest gaps put whole words in the wrong box), so the words are laid out along the line's ink extent (first to last
blob of 8 px or more over the x-height band, an isolated end blob under 40 px dropped) in proportion to their sign counts, a word space counting one sign width;
interlinear words ('+') are left out. (2) Each word
box is cut into as many tiles as the word has signs, at proportional positions snapped to the lowest-ink column within a
third of a sign width. Boxes are APPROXIMATE: a tile can be a sign off, or half of two signs; a bad cut goes to BAD-CUT.
Labels: pile = the reconciled draft's sign at that position (a draft, 36 of its 165 words marked uncertain; R7-OLDA
section 13), family = the same; a superscript a is joined to its sign ('s^a'); punctuation is not tiled. No sign values or
plaintext reading appear in sorter/ beyond the draft's own sign labels.
focus.tsv: tiles where blind pass A or pass B (passF/passG, aligned per line by the same edit-distance alignment as
matignon's score.py, after diff_pass2.norm_tok's notation folds) wrote another sign than the draft, ordered with the
look-alike pairs the brief names first (9/q, f/p, v/r, l/t, G/t; the G-shaped ligature is drawn 'l7'/'c7'/'b7' in the
passes), then R7-OLDA section 13's own split pairs (d/8 for the looped d, 5/s, p/g/l, c/t, m/n/r minims), then the
other splits. Notation splits are folded first (R7-OLDA's post-hoc fold: u/v/2, e/8, a/4, o/7, i/y/3,
final 5 = s, 6 = b), so the box asks about shapes, not spelling conventions; the question shows what each pass wrote,
unfolded, and the named pairs are matched on those unfolded signs; '-' means that pass has no sign there.

  python3 sorter/build_inputs.py      (from the repo root or anywhere; needs pillow, numpy)
"""
import csv, json, re
from collections import defaultdict
from pathlib import Path
from PIL import Image
import numpy as np
T = Path(__file__).resolve().parents[1]; CR = T / 'images' / 'crops_AC2'; S = T / 'sorter'; P = S / 'pages'
TR = T / 'transcription'
P.mkdir(exist_ok=True)
PAIRS = [{'9', 'q'}, {'f', 'p'}, {'v', 'r'}, {'l', 't'}, {'g', 't'}, {'c', 'l'}, {'b', 'l'}, {'6', 'l'}]  # brief's; G-lig l/c/b/6
PAIRS2 = [{'d', '8'}, {'5', 's'}, {'p', 'g'}, {'p', 'l'}, {'g', 'l'}, {'c', 't'}, {'m', 'n'}, {'n', 'r'}]  # R7-OLDA section 13's


def units(tok):
    """raw token -> sign units: strip pass markers and punctuation, join ^a to the sign before it."""
    t = tok.replace('~', '').replace('+', '')
    t = re.sub(r"[,.;:\-|'? ]", '', t)
    out = []
    i = 0
    while i < len(t):
        if t[i] == '^' and i + 1 < len(t) and out:
            out[-1] += '^' + t[i + 1]; i += 2
        else:
            out.append(t[i]); i += 1
    return out


FOLD = {'u': '2', 'v': '2', 'e': '8', 'a': '4', 'o': '7', 'i': '3', 'y': '3', '6': 'b'}


def cmp_unit(u, last):
    # focus only: R7-OLDA's post-hoc notation fold (vowel letter vs digit, final 5 = s), so a notation split is not asked
    u = u.lower(); u = 's' if (last and u == '5') else u
    return FOLD.get(u, u)


def read(path):
    d = defaultdict(list)
    for r in csv.DictReader(open(path), delimiter='\t'):
        d[(r['block'], int(r['line']))].append(r)
    return d


def strip(block, line):
    if (block, line) == ('C2', 9):
        return Image.open(CR / 'C2_L09_s1.jpg').convert('L')
    es = sorted([e for e in json.load(open(CR / f'manifest_{block}.json'))['iiif_lines'] if e['band'] == line],
                key=lambda e: e['segment'])
    ims = [Image.open(CR / e['crop']).convert('L') for e in es]
    x0 = es[0]['box'][0]
    out = Image.new('L', (es[-1]['box'][0] - x0 + ims[-1].width, max(i.height for i in ims)), 255)
    for e, im in reversed(list(zip(es, ims))):
        im = im.point(lambda v: 255 if v < 45 else v)       # the deskew's black corner fill is not ink
        out.paste(im, (e['box'][0] - x0, 0))
    return out


def band(a, thr, half=24):
    """rows of the line's x-height band: peak of the smoothed row ink profile in the middle half, +- half."""
    h = a.shape[0]; r = np.convolve((a < thr).sum(1), np.ones(15), 'same')
    c = h // 4 + int(np.argmax(r[h // 4: 3 * h // 4]))
    return max(0, c - half), min(h, c + half)


def blobs(a, gap, minw, thr):
    y0, y1 = band(a, thr); mid = a[y0:y1]
    col = (mid < thr).sum(0) > 1
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


def gapsplit(segs, n):
    """word boxes: fine blobs joined, breaking at the n-1 widest gaps between them (halve the widest if too few)."""
    if len(segs) < n:
        return fit(segs, n)
    g = sorted(range(len(segs) - 1), key=lambda k: segs[k + 1][0] - segs[k][1], reverse=True)[:n - 1]
    out, s = [], segs[0][0]
    for k in sorted(g):
        out.append([s, segs[k][1]]); s = segs[k + 1][0]
    out.append([s, segs[-1][1]])
    return out


def spread(x0, x1, lens, space=1.0):
    """word boxes laid out along the line's ink extent in proportion to sign count, a word space = one sign width."""
    w = (x1 - x0 + 1) / (sum(lens) + space * (len(lens) - 1)); out, x = [], float(x0)
    for n in lens:
        out.append([int(round(x)), int(round(x + n * w)) - 1]); x += (n + space) * w
    return out


def cut(a, x0, x1, n, thr):
    y0, y1 = band(a, thr); ink = (a[y0:y1, x0:x1 + 1] < thr).sum(0)
    w = (x1 - x0 + 1) / n; cuts = [0]
    for k in range(1, n):
        c = int(round(k * w)); r = max(1, int(w / 3))
        lo, hi = max(cuts[-1] + 2, c - r), min(x1 - x0 - 1, c + r)
        cuts.append(lo + int(np.argmin(ink[lo:hi + 1])) if hi >= lo else c)
    cuts.append(x1 - x0 + 1)
    return [(x0 + cuts[k], x0 + cuts[k + 1] - 1) for k in range(n)]


def nw(a, b):   # matignon f110crops/score.py's alignment
    n, m = len(a), len(b); D = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(n + 1): D[i][0] = i
    for j in range(m + 1): D[0][j] = j
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            D[i][j] = min(D[i - 1][j] + 1, D[i][j - 1] + 1, D[i - 1][j - 1] + (a[i - 1] != b[j - 1]))
    i, j, pairs = n, m, {}
    while i > 0 and j > 0:
        if D[i][j] == D[i - 1][j - 1] + (a[i - 1] != b[j - 1]): pairs[i - 1] = j - 1; i -= 1; j -= 1
        elif D[i][j] == D[i - 1][j] + 1: i -= 1
        else: j -= 1
    return pairs


def seq(rows):
    """per line: list of (word index, unit, compare unit) over the non-interlinear words."""
    out = []
    for r in rows:
        if r['token'].startswith('+'): continue
        us = units(r['token'])
        for k, u in enumerate(us):
            out.append((int(r['pos']), u, cmp_unit(u, k == len(us) - 1)))
    return out


REC = read(TR / 'reconciled_AC2_R7OLDA.tsv')
PA, PB = read(TR / 'passF_blindA_R7OLDA.tsv'), read(TR / 'passG_blindB_R7OLDA.tsv')
signs, labels, focus, fitlog = [], [], [], []
for (block, line) in sorted(REC, key=lambda k: (k[0] != 'A', k[1])):
    page = f'{block}_L{line:02d}'; im = strip(block, line); im.save(P / f'{page}.jpg', quality=85)
    a = np.array(im); med = float(np.median(a)); thr = med - 40      # pale iron-gall ink: threshold from the paper tone
    words = [r for r in REC[(block, line)] if not r['token'].startswith('+') and units(r['token'])]
    a[:, np.median(a, 0) < 120] = 255                                # columns of the deskew's dark corner fill
    bl = [g for g in blobs(a, 4, 3, thr) if g[1] - g[0] >= 8]
    while len(bl) > 2 and bl[1][0] - bl[0][1] > 50 and bl[0][1] - bl[0][0] < 40: bl = bl[1:]       # stray mark before the line
    while len(bl) > 2 and bl[-1][0] - bl[-2][1] > 50 and bl[-1][1] - bl[-1][0] < 40: bl = bl[:-1]  # or after it
    wboxes = spread(bl[0][0], bl[-1][1], [len(units(r['token'])) for r in words])
    fitlog.append((page, len(words), len(bl), len(wboxes)))
    rs = seq(REC[(block, line)]); ca = [c for _, _, c in rs]
    al = {}
    for k, d in (('A', PA), ('B', PB)):
        ps = seq(d.get((block, line), []))
        al[k] = (nw(ca, [c for _, _, c in ps]), [c for _, _, c in ps], [u.lower() for _, u, _ in ps])
    conf = {int(r['pos']): r['conf'] for r in REC[(block, line)]}
    i = 0
    for r, (x0, x1) in zip(words, wboxes):
        us = units(r['token'])
        for k, (u0, u1) in enumerate(cut(a, x0, x1, len(us), thr)):
            sid = f'{page}_{i + 1:03d}'
            ys = np.where((a[:, u0:u1 + 1] < thr).sum(1) > 0)[0]
            y0, y1 = (int(ys.min()), int(ys.max())) if len(ys) else (0, im.height - 1)
            signs.append(dict(sid=sid, page=page, x=u0, y=y0, w=u1 - u0 + 1, h=y1 - y0 + 1))
            labels.append(dict(sid=sid, sign=us[k], family=us[k]))
            c = ca[i]; fa = al['A'][1][al['A'][0][i]] if i in al['A'][0] else '-'
            fb = al['B'][1][al['B'][0][i]] if i in al['B'][0] else '-'
            ra = al['A'][2][al['A'][0][i]] if i in al['A'][0] else '-'      # what the pass wrote, unfolded
            rb = al['B'][2][al['B'][0][i]] if i in al['B'][0] else '-'
            split = fa != c or fb != c
            if split:
                seen = {us[k].lower(), ra, rb} - {'-'}
                rank = 0 if any(p <= seen for p in PAIRS) else (1 if any(p <= seen for p in PAIRS2) else 2)
                why = 'uncertain word in the draft' if conf[int(r['pos'])] == 'uncertain' else 'draft word marked high'
                focus.append((rank, sid, f'{block} line {line}, word {r["pos"]} "{r["token"]}", sign {k + 1}: draft {us[k]}, '
                                         f'blind pass A {ra}, pass B {rb} ({why}); which sign is this?'))
            i += 1
focus.sort(key=lambda f: f[0])
for name, rs in (('signs.tsv', signs), ('labels.tsv', labels)):
    with open(S / name, 'w', newline='') as o:
        w = csv.DictWriter(o, fieldnames=list(rs[0]), delimiter='\t'); w.writeheader(); w.writerows(rs)
with open(S / 'focus.tsv', 'w') as o:
    for _, sid, q in focus: o.write(f'{sid}\t{q}\n')
with open(S / 'fit.tsv', 'w') as o:
    o.write('page\twords\tblobs\tword_boxes\n')
    for r in fitlog: o.write('\t'.join(map(str, r)) + '\n')
print(len(signs), 'signs;', len(focus), 'focus tiles (', sum(f[0] == 0 for f in focus), 'named pairs,',
      sum(f[0] == 1 for f in focus), "R7-OLDA's pairs,", sum(f[0] == 2 for f in focus), 'other splits );',
      len(set(l['sign'] for l in labels)), 'piles')
