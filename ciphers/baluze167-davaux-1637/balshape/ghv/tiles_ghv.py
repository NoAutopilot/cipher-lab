#!/usr/bin/env python3
"""BAL167-GHV (13 Oct 2026, LANE DEFAULT-A4-0935): hook/v verification tiles (PREREG-BAL-GHV.md). Disk only. Every tile is
captioned 'Xnn: E-s2?'. T = f.228 hook and v tiles (BAL-SHAPE T coordinates); P+/P- from balshape/ghv/labels.tsv. Writes
balshape/ghv/r<seed>/X??.png, sheet.png, exemplars.png, key_private.tsv. Usage (target folder): python3 balshape/ghv/tiles_ghv.py [seed]"""
import csv, os, random, sys
sys.path.insert(0, 'balshape'); sys.path.insert(0, 'b167228')
from tiles import T, sheet
from sig_tiles import tile
from PIL import Image
seed = int(sys.argv[1]) if len(sys.argv) > 1 else 20261013
L = list(csv.DictReader(open('balshape/ghv/labels.tsv'), delimiter='\t'))
items = [(r, w, src, x, y, v) for r, w, src, x, y, v in T if r in ('T:v', 'T:DECOY:hook=s')]
items += [(f"{l['arm']}:{l['id']}", l['id'], l['src'], int(l['x']), int(l['y']), l['label']) for l in L if l['arm'] in ('P+', 'P-')]
ex = next(l for l in L if l['arm'] == 'exemplar')
rnd = random.Random(seed); order = list(range(len(items))); rnd.shuffle(order)
out = f'balshape/ghv/r{seed}'; os.makedirs(out, exist_ok=True)
key, tl = ['id\trole\twhere\tx\ty\ttrue_or_current\tproposed'], []
for n, i in enumerate(order, 1):
    r, w, src, x, y, v = items[i]; t = tile(src, x, y); t.save(f'{out}/X{n:02d}.png')
    tl.append((f'X{n:02d}: E-s2?', t)); key.append(f'X{n:02d}\t{r}\t{w}\t{x}\t{y}\t{v}\ts')
sheet(tl, f'{out}/sheet.png', cols=5)
sheet([('E-s2', tile(ex['src'], int(ex['x']), int(ex['y'])))], f'{out}/exemplar_s2.png', cols=1)
open(f'{out}/key_private.tsv', 'w').write('\n'.join(key) + '\n')
print(f'{out}: {len(items)} tiles', sorted(r.split(":")[0] for r, *_ in items))
