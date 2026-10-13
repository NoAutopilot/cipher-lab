#!/usr/bin/env python3
"""BAL-WL (13 Oct 2026, LANE DEFAULT-A1-0640): same-key wrong-label negative for BAL-SHAPE (PREREG-BAL-WL.md). Disk only.
Builds a blind label-VERIFICATION sheet: each tile is shown with one proposed exemplar label; the reader answers yes/no.
Arms: T = the f.228 tiles of balshape/tiles.py with their current value proposed (classes whose value has no exemplar dropped);
P+ = half the gloss-fixed f.258r/f.233r tiles (balshape/gloss_labels.tsv) with their TRUE gloss label proposed; P- = the other half with
a WRONG label proposed (seeded draw from the T value pool minus the true letter, restricted to letters that have an exemplar).
Same tile() geometry, same exemplar sheet as BAL-SHAPE. Writes balshape/wl/r<seed>/X??.png, sheet_{1,2,3}.png, key_private.tsv.
Usage (from the target folder): python3 balshape/wl/tiles_wl.py [seed] [half]   half=0 (default) or 1 swaps which P half is P+."""
import os, random, sys
sys.path.insert(0, 'balshape'); sys.path.insert(0, 'b167228')
import csv
from tiles import T, pos, sheet
from sig_tiles import tile
EX = {l.strip().split('\t')[0][2:] for l in open('balshape/tiles/exemplars.tsv') if l.startswith('E-')}
POOL = sorted({v for *_, v in T} & EX)
seed = int(sys.argv[1]) if len(sys.argv) > 1 else 20261013
half = int(sys.argv[2]) if len(sys.argv) > 2 else 0
lab = {r['id']: r['label'] for r in csv.DictReader(open('balshape/gloss_labels.tsv'), delimiter='\t') if r['label']}
seen, P = set(), []
for cid in lab:  # same exemplar/P split as balshape/tiles.py (first labelled occurrence per letter = exemplar)
    (P.append(cid) if lab[cid] in seen else None); seen.add(lab[cid])
rnd = random.Random(seed)
idx = list(range(len(P))); rnd.shuffle(idx)
plus = set(idx[:len(P) // 2 + (len(P) % 2)]) if half == 0 else set(idx[len(P) // 2 + (len(P) % 2):])
items = [(f'{r}', w, src, x, y, v, v) for r, w, src, x, y, v in T if v in EX]
for i, cid in enumerate(P):
    src, x, y = pos(cid); true = lab[cid]
    if i in plus:
        items.append((f'P+:{cid}', cid, src, x, y, true, true))
    else:
        items.append((f'P-:{cid}', cid, src, x, y, true, rnd.choice([l for l in POOL if l != true])))
order = list(range(len(items))); rnd.shuffle(order)
out = f'balshape/wl/r{seed}'; os.makedirs(out, exist_ok=True)
key, tl = ['id\trole\twhere\tx\ty\ttrue_or_current\tproposed'], []
for n, i in enumerate(order, 1):
    r, w, src, x, y, v, prop = items[i]; t = tile(src, x, y); t.save(f'{out}/X{n:02d}.png')
    tl.append((f'X{n:02d}: E-{prop}?', t)); key.append(f'X{n:02d}\t{r}\t{w}\t{x}\t{y}\t{v}\t{prop}')
third = (len(tl) + 2) // 3
for k in range(3):
    sheet(tl[k * third:(k + 1) * third], f'{out}/sheet_{k + 1}.png')
open(f'{out}/key_private.tsv', 'w').write('\n'.join(key) + '\n')
c = lambda p: sum(1 for k in key[1:] if k.split('\t')[1].startswith(p))
print(f'{out}: T {c("T:")}, P+ {c("P+:")}, P- {c("P-:")}, pool {"".join(POOL)}, exemplars {"".join(sorted(EX))}')
