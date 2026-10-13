#!/usr/bin/env python3
"""BAL167-GSEQ (13 Oct 2026, LANE DEFAULT-A2-2013): PREREG-BAL-GPLUS (b) g+ verification tiles, run after PREREG-BAL-GSEQ settled the
f.124 gt gloss letter. Disk only. Every tile captioned 'Xnn: E-g+?'. E-g+ = f.124r first gt; T = the 3 f.228 g+ (b167228/sig_tiles.py);
P+ = f.124r line-final gt, f.124v gt; P- = crossed y = r (f.229 L4 exemplar, f.228 DECOY:y+=r), r-shape = g (f.239r, ghv labels N3).
Centres on the f.124 strips located by this worker on gridded copies (location only). Writes balshape/gplus/r<seed>/.
Usage (target folder): python3 balshape/gplus/tiles_gplus.py [seed]"""
import csv, os, random, sys
sys.path.insert(0, 'balshape'); sys.path.insert(0, 'b167228')
from tiles import sheet
from sig_tiles import tile, TARGET, DECOY, L4, VB, VBY
seed = int(sys.argv[1]) if len(sys.argv) > 1 else 20261013
S131, S132 = 'images/gplus/b170_c131_pct_73_52_5_27_5.jpg', 'images/gplus/b170_c132_pct_15_32_5_20_5.jpg'
lab = {l['id']: l for l in csv.DictReader(open('balshape/ghv/labels.tsv'), delimiter='\t')}
items = [(f'T:g+', w, src, x, y, 'n?') for s, w, src, x, y in TARGET if s == 'g+']
items += [('P+:gt', 'f124r_line_final', S131, 1785, 170, 'n'), ('P+:gt', 'f124v_after_K', S132, 1050, 170, 'n')]
items += [('P-:y+', 'f229r_L04_exemplar', L4, 1444, None, 'r'), ('P-:y+', 'f228v_b_L02_decoy', VB, 1713, VBY[2], 'r'),
          ('P-:rshape', 'f239r_N3', lab['N3']['src'], int(lab['N3']['x']), int(lab['N3']['y']), 'g')]
rnd = random.Random(seed); order = list(range(len(items))); rnd.shuffle(order)
out = f'balshape/gplus/r{seed}'; os.makedirs(out, exist_ok=True)
key, tl = ['id\trole\twhere\tx\ty\ttrue_or_current\tproposed'], []
for n, i in enumerate(order, 1):
    r, w, src, x, y, v = items[i]; t = tile(src, x, y); t.save(f'{out}/X{n:02d}.png')
    tl.append((f'X{n:02d}: E-g+?', t)); key.append(f'X{n:02d}\t{r}\t{w}\t{x}\t{y}\t{v}\tg+')
sheet(tl, f'{out}/sheet.png', cols=4)
sheet([('E-g+', tile(S131, 785, 170))], f'{out}/exemplar_gplus.png', cols=1)
open(f'{out}/key_private.tsv', 'w').write('\n'.join(key) + '\n')
print(f'{out}: {len(items)} tiles', sorted(r for r, *_ in items))
