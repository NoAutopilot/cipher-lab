#!/usr/bin/env python3
"""BAL-SHAPE (BAL-CROP worker, 13 Oct 2026): cut the blind tile sheets of PREREG-BAL-SHAPE.md from images on disk (no network).
T = the 29 f.228 letter-sign tiles already located by SIG-B228/SIG-B228B (b167228/sig_tiles.py TARGET+DECOY minus 'wave',
b167228/sig2_tiles.py SHAPES; same tile() geometry and coordinates) with their current value; P/E = gloss-labelled signs of
Baluze 170 f.258r / f.233r (labels from balshape/gloss_labels.tsv: both blind gloss reads agree, PREREG step A); N = 8
letter-like signs of Baluze 169 f.208r (Saint-Chamond's key). Centres of P/N placed by eye on gridded copies (location only).
Writes balshape/tiles/X??.png, sheet_unknown_{1,2}.png, sheet_exemplars.png, key_private.tsv. Usage: python3 balshape/tiles.py [seed]"""
import csv, json, random, sys
sys.path.insert(0, 'b167228')
from PIL import Image, ImageDraw
from sig_tiles import tile, TARGET, DECOY, W, H
from sig2_tiles import SHAPES
VAL = {'q': 'c', 'll': 'l', 'g+': 'n', 'll|u4': 'l', 'v': 's', 'ff': 's', 'DECOY:hook=s': 's', 'DECOY:gam=u': 'u',
       'DECOY:y+=r': 'r', 'target:u4|4u': 'a', 'DECOY:h=n': 'n', 'ANCHOR:4u=a': 'a', 'ANCHOR:u4=t': 't'}
T = [(f'T:{s}', w, src, x, y, VAL[s]) for s, w, src, x, y in TARGET + DECOY if s != 'wave']
T += [(f'T:{r}', w, src, x, y, VAL[r]) for r, w, src, x, y in SHAPES]
# glossed candidates: '<row><segment>' ids of balshape/segs.json (column-ink segmentation of each cipher line, centre x, line
# centre y = tools/iiif_lines.py centres); labels from balshape/gloss_labels.tsv (both blind gloss reads agree; unlabelled ids unused)
SEG = json.load(open('balshape/segs.json'))
def pos(cid):
    row, i = cid.rstrip('0123456789'), int(cid[len(cid.rstrip('0123456789')):])
    f, c, segs = SEG[row]; return f, segs[i][0], c
N = [('N:y', 'N118'), ('N:3-form', 'N121'), ('N:gt', 'N123'), ('N:q', 'N20'), ('N:gamma', 'N23'), ('N:9-bar', 'N218'),
     ('N:3-form', 'N222'), ('N:m4', 'N322')]
N = [(r, SEG[c[:2]][0], SEG[c[:2]][2][int(c[2:])][0], SEG[c[:2]][1]) for r, c in N]  # 'N1' + segment index
def sheet(lst, path, cols=6):
    rows = (len(lst) + cols - 1) // cols
    out = Image.new('L', (cols * (W + 10), rows * (H + 40)), 255); d = ImageDraw.Draw(out)
    for k, (lab, t) in enumerate(lst):
        cx, cy = (k % cols) * (W + 10), (k // cols) * (H + 40)
        out.paste(t, (cx, cy + 30)); d.text((cx + 5, cy + 5), lab, fill=0)
        d.rectangle([cx, cy + 30, cx + W - 1, cy + 30 + H - 1], outline=128)
    out.save(path)
if __name__ == '__main__':
    seed = int(sys.argv[1]) if len(sys.argv) > 1 else 20261013
    lab = {r['id']: r['label'] for r in csv.DictReader(open('balshape/gloss_labels.tsv'), delimiter='\t') if r['label']}
    seen, E, P = set(), [], []
    for cid in lab:  # gloss_labels.tsv order = reading order: first labelled occurrence per letter is the exemplar (PREREG 3)
        src, x, y = pos(cid)
        (P if lab[cid] in seen else E).append((cid, src, x, y, lab[cid])); seen.add(lab[cid])
    items = T + [(f'P:{c}', c, s, x, y, l) for c, s, x, y, l in P] + [(r, r, s, x, y, '') for r, s, x, y in N]
    rnd = random.Random(seed); order = list(range(len(items))); rnd.shuffle(order)
    key = ['id\trole\twhere\tx\ty\tvalue']; tl = []
    for n, i in enumerate(order, 1):
        r, w, src, x, y, v = items[i]; t = tile(src, x, y); t.save(f'balshape/tiles/X{n:02d}.png'); tl.append((f'X{n:02d}', t))
        key.append(f'X{n:02d}\t{r}\t{w}\t{x}\t{y}\t{v}')
    half = (len(tl) + 1) // 2
    sheet(tl[:half], 'balshape/tiles/sheet_unknown_1.png'); sheet(tl[half:], 'balshape/tiles/sheet_unknown_2.png')
    ex = [(f'E-{l}', tile(s, x, y)) for c, s, x, y, l in sorted(E, key=lambda e: e[4])]
    sheet(ex, 'balshape/tiles/sheet_exemplars.png')
    open('balshape/tiles/key_private.tsv', 'w').write('\n'.join(key) + '\n')
    open('balshape/tiles/exemplars.tsv', 'w').write('label\tcand\tx\ty\n' + ''.join(f'E-{l}\t{c}\t{x}\t{y}\n' for c, s, x, y, l in E))
    print(f'T {len(T)}, P {len(P)}, N {len(N)}, exemplars {len(E)}: {" ".join(sorted(l for *_, l in E))}')
