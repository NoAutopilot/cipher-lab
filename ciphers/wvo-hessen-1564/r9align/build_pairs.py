#!/usr/bin/env python3
"""R9-WVOALIGN (6 Oct 2026): build tools/interlinear_align.py PAIRS files for f.23 (WVO 1109 enclosure).
Gloss: gloss_reconciled.tsv (this worker's reconciliation of the two blind passes against crops_m/).
Cipher labels, three gloss-blind sets:
  piles  -- the R9-WVOSORT sorter's provisional k-means pile ids (sorter/labels.tsv), every tile of the row in x order
            (sorter/signs.tsv); the one tile that is a clear letter (f23_C01_01_014, the E of 'E.L.') is a clear token.
  passA / passB -- the two blind Sonnet passes (passA_*.tsv, passB_*.tsv), s1 + s2 per row; 'A/B' -> A.
            passB's L10 s2 holds the sloping tail of cipher row C09 (C10 ends at the signature) and is appended to C09.
Run from the repo root: python3 ciphers/wvo-hessen-1564/r9align/build_pairs.py"""
import csv, os
D = os.path.dirname(os.path.abspath(__file__))
S = os.path.join(D, '..', 'sorter')
CLEAR_TILES = {'f23_C01_01_014': 'EL'}

gloss = {r['row']: r['gloss'].replace('|', ' ') for r in csv.DictReader(open(os.path.join(D, 'gloss_reconciled.tsv')), delimiter='\t')}
rows = sorted(gloss)


def write(name, cipher):
    with open(os.path.join(D, 'pairs_%s.tsv' % name), 'w', newline='') as f:
        w = csv.writer(f, delimiter='\t', lineterminator='\n')
        w.writerow(['plain_line', 'plain_raw', 'cipher_line', 'cipher_raw'])
        for r in rows:
            w.writerow([r, gloss[r], r, ' '.join(cipher[r])])


lab = {r['sid']: r['sign'] for r in csv.DictReader(open(os.path.join(S, 'labels.tsv')), delimiter='\t')}
tiles = list(csv.DictReader(open(os.path.join(S, 'signs.tsv')), delimiter='\t'))
piles, order = {}, {}
for r in rows:
    t = sorted([x for x in tiles if x['page'] == 'f23_' + r], key=lambda x: int(x['x']))
    order[r] = [x['sid'] for x in t]
    piles[r] = [CLEAR_TILES.get(x['sid']) or '@' + lab[x['sid']] for x in t]
write('piles', piles)
with open(os.path.join(D, 'tile_order.tsv'), 'w') as f:
    f.write('row\tidx\tsid\tpile\n')
    for r in rows:
        for k, s in enumerate(order[r]):
            f.write('%s\t%d\t%s\t%s\n' % (r, k, s, lab[s]))

for p in ('A', 'B'):
    cip = {r: [] for r in rows}
    for h in (1, 2):
        for x in csv.DictReader(open(os.path.join(D, 'pass%s_%d.tsv' % (p, h))), delimiter='\t'):
            row = 'C' + x['pair'][1:]
            if p == 'B' and x['pair'] == 'L10' and x['seg'] == 's2':
                row = 'C09'
            cip[row] += ['@' + t.split('/')[0] for t in (x['cipher'] or '').split()]
    write('pass' + p, cip)
print({r: len(piles[r]) for r in rows})
