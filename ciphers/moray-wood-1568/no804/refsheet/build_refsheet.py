"""RUN1-MOR (account 1, 4 Oct 2026): the no.804 labelling reference sheet (no vision call). Input: the 134 glyph crops
cut by `tools/glyph_atlas.py crop --image IMG_R8345_I38545_P4.jpg --box ...` from no804/refsheet/boxes.tsv (full-size
DECODE image kept in the scratchpad, sha1 in images/manifest.json). Output: refsheet_classes.png (one row per glyph class in
key.tsv order = Aymeloglu's key.json order, every exemplar of that class, labelled position and value), refsheet_mi.png
(each M/I-graded token beside its three best-matching S-graded exemplars) and nearest_mi.tsv (the scores).
Similarity: each crop is binarised (grey < 150), the ink is cut to its own bounding box inside the line's core band +-
the crop, padded to square and resized to 32x32; score = max over +-2 px shifts of the Dice overlap of the two ink masks.
A script ranking, not a reading: it orders exemplars for a human labeller; it fixes no value (rule 4 grades unchanged).
Credit: transcription and key labels are Aymeloglu's (aaymeloglu/unsolved-ciphers moray-1568, cited, no code copied).
usage: python3 build_refsheet.py TILES_DIR OUT_DIR"""
import sys, os, glob, numpy as np
from PIL import Image, ImageDraw, ImageFont
T, O = sys.argv[1], sys.argv[2]
D = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..')
key = [l.rstrip('\n').split('\t') for l in open(f'{D}/key.tsv') if not l.startswith('#')][1:]
order = [k[0] for k in key]; val = {k[0]: k[1] for k in key}; grade = {k[0]: k[2] for k in key}
tiles = {}
for f in sorted(glob.glob(f'{T}/*.png')):
    pos, sign = os.path.basename(f)[:-4].split('_', 1); tiles[pos] = (sign, Image.open(f).convert('L'))
def norm(im):
    a = np.array(im) < 150
    ys, xs = np.nonzero(a)
    if len(xs) == 0: return np.zeros((32, 32), bool)
    a = a[ys.min():ys.max()+1, xs.min():xs.max()+1]; h, w = a.shape; s = max(h, w)
    sq = np.zeros((s, s), bool); sq[(s-h)//2:(s-h)//2+h, (s-w)//2:(s-w)//2+w] = a
    return np.array(Image.fromarray(sq.astype(np.uint8)*255).resize((32, 32), Image.BILINEAR)) > 100
def dice(a, b):
    best = 0
    for dy in range(-2, 3):
        for dx in range(-2, 3):
            bb = np.roll(np.roll(b, dy, 0), dx, 1); i = (a & bb).sum(); s = a.sum() + bb.sum()
            best = max(best, 2*i/s if s else 0)
    return best
N = {p: norm(im) for p, (s, im) in tiles.items()}
MI = [p for p, (s, im) in tiles.items() if grade.get(s) in ('M', 'I')]
SP = [p for p, (s, im) in tiles.items() if grade.get(s) == 'S']
font = ImageFont.load_default(size=18); fb = ImageFont.load_default(size=22)
def cell(p, cap, H=150):
    im = tiles[p][1]; r = H / im.height; im = im.resize((max(1, int(im.width*r)), H))
    c = Image.new('L', (max(im.width, 120)+8, H+30), 255); c.paste(im, (4, 26))
    ImageDraw.Draw(c).text((4, 2), cap, fill=0, font=font); return c
def sheet(rows, out, maxw=2400):
    W = min(maxw, max(sum(c.width for c in r[1]) + 260 for r in rows)); out_rows = []
    for title, cells in rows:  # wrap long rows
        line = []; x = 260
        for c in cells:
            if x + c.width > W and line: out_rows.append((title, line)); title = ''; line = []; x = 260
            line.append(c); x += c.width
        out_rows.append((title, line))
    H = sum(max(c.height for c in r[1]) + 10 for r in out_rows)
    S = Image.new('L', (W, H), 255); d = ImageDraw.Draw(S); y = 0
    for title, cells in out_rows:
        h = max(c.height for c in cells); d.text((6, y + h//3), title, fill=0, font=fb); x = 260
        for c in cells: S.paste(c, (x, y)); d.rectangle([x, y, x+c.width-1, y+h-1], outline=170); x += c.width
        y += h + 10; d.line([0, y-5, W, y-5], fill=200)
    S.save(out, optimize=True); return S.size
by = {}
for p, (s, im) in tiles.items(): by.setdefault(s, []).append(p)
key_pos = lambda p: (p.split('.')[0], int(p.split('.')[1]))
rows = [(f'{s} = {val[s]} ({grade[s]}) x{len(by[s])}', [cell(p, p) for p in sorted(by[s], key=key_pos)]) for s in order if s in by]
print('classes', len(rows), sheet(rows, f'{O}/refsheet_classes.png'))
lines = ['position\tsign\this_value\tgrade\trank\texemplar\texemplar_sign\texemplar_value\tdice']; rows = []
for p in sorted(MI, key=lambda p: (order.index(tiles[p][0]), key_pos(p))):
    s = tiles[p][0]; sc = sorted(((dice(N[p], N[q]), q) for q in SP), reverse=True)[:3]
    for k, (v, q) in enumerate(sc, 1):
        lines.append(f'{p}\t{s}\t{val[s]}\t{grade[s]}\t{k}\t{q}\t{tiles[q][0]}\t{val[tiles[q][0]]}\t{v:.3f}')
    rows.append((f'{p} {s} ({grade[s]})', [cell(p, f'{p} {s}={val[s]}?')] + [cell(q, f'{tiles[q][0]}={val[tiles[q][0]]} {v:.2f}') for v, q in sc]))
open(f'{O}/nearest_mi.tsv', 'w').write('# build_refsheet.py (RUN1-MOR, 4 Oct 2026): Dice of 32x32 ink masks, +-2 px shift; a ranking for a labeller, fixes no value\n' + '\n'.join(lines) + '\n')
print('mi tokens', len(MI), sheet(rows, f'{O}/refsheet_mi.png'))
# Power check of the ranking (not a gate): leave-one-out top-1 on S tokens whose class has >= 2 exemplars, against the
# same top-1 with the class labels shuffled over the S tokens (200 shuffles, seed 4).
rng = np.random.default_rng(4); Sm = [p for p in SP if len(by[tiles[p][0]]) >= 2]
nn = {p: max((dice(N[p], N[q]), q) for q in SP if q != p)[1] for p in Sm}
lab = {p: tiles[p][0] for p in SP}
hit = lambda L: sum(L[nn[p]] == L[p] for p in Sm) / len(Sm)
real = hit(lab); ks = list(lab); null = []
for _ in range(200):
    perm = rng.permutation([lab[k] for k in ks]); null.append(hit(dict(zip(ks, perm))))
msg = f'loo top-1 on {len(Sm)} S tokens: {real:.3f} vs label-shuffle mean {np.mean(null):.3f} p99 {np.percentile(null, 99):.3f}'
print(msg); open(f'{O}/nearest_mi.tsv', 'a').write('# ' + msg + '\n')
