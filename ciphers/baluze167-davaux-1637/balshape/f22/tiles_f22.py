#!/usr/bin/env python3
"""BAL22-SHAPE (14 Oct 2026, LANE DEFAULT-A2-0911-14): blind label-verification sheets for the 7 letter-sign tokens of Baluze 169
f.22r, BAL-WL design (PREREG-BAL22-SHAPE.md). Disk only. T = the 7 f.22r tiles (balshape/f22/locate.py) with their current value
proposed; P+ = a seeded half of the gloss-fixed f.258r/f.233r tiles (balshape/gloss_labels.tsv, same P list as BAL-WL) with the TRUE
label; P- = the other half with a WRONG label drawn from the f.22r value pool {a f m n r u} minus the true letter.
Exemplar sheet: the 12 gloss-fixed exemplars of BAL-SHAPE (balshape/tiles/exemplars.tsv) + E-m (m4) and E-u (gam) from f.229
(b167228/sig_tiles.py EXEMPLAR, published-key values) + E-f, the f column of Tomokiyo's table (images/louisxiii_davaux.png).
Usage (from the target folder): python3 balshape/f22/tiles_f22.py SEED HALF   -> balshape/f22/r<SEED>/"""
import os, random, sys, csv
sys.path.insert(0, 'balshape'); sys.path.insert(0, 'b167228'); sys.path.insert(0, 'balshape/f22')
from PIL import Image
from tiles import pos, sheet
from sig_tiles import tile, EXEMPLAR, W, H
from locate import F22, tile as tile22
seed, half = int(sys.argv[1]), int(sys.argv[2])
VALS = ['a', 'f', 'm', 'n', 'r', 'u']
lab = {r['id']: r['label'] for r in csv.DictReader(open('balshape/gloss_labels.tsv'), delimiter='\t') if r['label']}
seen, P = set(), []
for cid in lab:
    (P.append(cid) if lab[cid] in seen else None); seen.add(lab[cid])
rnd = random.Random(seed)
idx = list(range(len(P))); rnd.shuffle(idx)
plus = set(idx[:len(P) // 2 + (len(P) % 2)]) if half == 0 else set(idx[len(P) // 2 + (len(P) % 2):])
items = [(f'T:{l}/{p}', 'f22', x, y, v, v) for l, p, v, x, y in F22]
for i, cid in enumerate(P):
    src, x, y = pos(cid); true = lab[cid]
    items.append((f'P+:{cid}' if i in plus else f'P-:{cid}', src, x, y, true,
                  true if i in plus else rnd.choice([l for l in VALS if l != true])))
order = list(range(len(items))); rnd.shuffle(order)
out = f'balshape/f22/r{seed}'; os.makedirs(out, exist_ok=True)
key, tl = ['id\trole\tx\ty\ttrue_or_current\tproposed'], []
for n, i in enumerate(order, 1):
    r, src, x, y, v, prop = items[i]
    t = tile22(x, y) if src == 'f22' else tile(src, x, y)
    t.save(f'{out}/X{n:02d}.png'); tl.append((f'X{n:02d}: E-{prop}?', t)); key.append(f'X{n:02d}\t{r}\t{x}\t{y}\t{v}\t{prop}')
half_n = (len(tl) + 1) // 2
sheet(tl[:half_n], f'{out}/sheet_1.png'); sheet(tl[half_n:], f'{out}/sheet_2.png')
open(f'{out}/key_private.tsv', 'w').write('\n'.join(key) + '\n')
# exemplar sheet (same for every seed)
ex = []
for l in open('balshape/tiles/exemplars.tsv'):
    if l.startswith('E-'):
        e, cand = l.split('\t')[:2]; ex.append((e, tile(*pos(cand))))
for let, shape, src, x in EXEMPLAR:
    if let in ('m', 'u'):
        ex.append((f'E-{let}', tile(src, x)))
tb = Image.open('images/louisxiii_davaux.png').convert('L').crop((88, 22, 122, 80)).resize((W, H), Image.LANCZOS)
ex.append(('E-f', tb))
ex.sort(key=lambda t: t[0])
sheet(ex, 'balshape/f22/sheet_exemplars.png')
c = lambda p: sum(1 for k in key[1:] if k.split('\t')[1].startswith(p))
print(f'{out}: T {c("T:")}, P+ {c("P+:")}, P- {c("P-:")}, exemplars {" ".join(e for e, _ in ex)}')
