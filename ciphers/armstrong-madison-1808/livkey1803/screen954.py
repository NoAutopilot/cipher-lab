#!/usr/bin/env python3
"""Campaign step H12 (27 Sept 2026): screen the reel-9 frame-954/955/956 numbered table (James Monroe Papers,
LOC mss33217, the collection's featured undated key; 17 columns x 100 rows = values 1-1700, one-part sequential,
words and syllables mixed; frame 956 is its alphabetical encode side) against the 369 numeric groups of
ciphertext.txt, the ARM3-LIVCODE way: value range, fill map, the 901-1099 block, and the units-digit signature.
No plaintext is read. Writes screen954.tsv. Run from the target folder: python3 livkey1803/screen954.py
"""
import csv, importlib.util, pathlib, random, sys
from collections import Counter
HERE = pathlib.Path(__file__).resolve().parent
T = HERE.parent
ROOT = T.parent.parent
rng = random.Random(20260927)

body = [l for l in (T/'ciphertext.txt').read_text().splitlines() if l.strip() and not l.startswith('#')]
g = [int(t) for t in ' '.join(body).split() if t.isdigit()]
N = len(g)
rows = []

# (a) value range: the table ends at 1700 (frame 955 bottom right "1700 ac"; frame 956 encode side, no value above 1700 seen)
TABLE_MAX = 1700
over = [v for v in g if v > TABLE_MAX]
rows.append(('range', 'target groups above 1700', f'{len(over)}/{N} = {len(over)/N:.3f}', 'a letter encoded with this table: 0 by construction'))
four = [v for v in g if v >= 1000]
null_over = []
for _ in range(200):
    null_over.append(sum(rng.randint(1000, 9999) > TABLE_MAX for v in four)/N)
rows.append(('range', 'null: 4-digit groups redrawn uniform 1000-9999 (200 draws), fraction above 1700', f'mean {sum(null_over)/200:.3f}', 'reference only: a uniform draw exceeds 1700 almost always; the discriminating comparison is target vs encoded-prose 0'))
rows.append(('range', 'distinct target values above 1700', ' '.join(str(v) for v in sorted(set(over))), ''))

# (b) fill map, columns 1201-1681 rows 1-81 (f954_fillmap.tsv, one reader, grade M)
fm = {}
with open(HERE/'f954_fillmap.tsv') as f:
    for r in csv.DictReader((l for l in f if not l.startswith('#')), delimiter='\t', quoting=csv.QUOTE_NONE):
        fm[int(r['value'])] = r['status']
inmap = [v for v in g if v in fm]
blank_hits = [v for v in inmap if fm[v] == 'blank']
rows.append(('fill', 'target groups whose value is a cell of the fill map (1201-1681, rows 1-81)', f'{len(inmap)}', ''))
rows.append(('fill', 'of those, landing on a BLANK cell (occurrences)', f'{len(blank_hits)}/{len(inmap)} = {len(blank_hits)/len(inmap):.3f}', 'distinct: ' + ' '.join(str(v) for v in sorted(set(blank_hits)))))
# expected blank fraction under "random value in the same column" null, weighted by the target's own column occupancy
col_blank = {c: sum(fm[v]=='blank' for v in range(c, c+81))/81 for c in (1201,1301,1401,1501,1601)}
exp = sum(col_blank[(v//100)*100+1] for v in inmap)/len(inmap)
rows.append(('fill', 'per-column blank rate rows 1-81 (1201/1301/1401/1501/1601)', ' '.join(f'{col_blank[c]:.3f}' for c in (1201,1301,1401,1501,1601)), ''))
rows.append(('fill', 'expected blank fraction if the target values were random cells of the same columns', f'{exp:.3f}', 'a letter encoded with this table (as it stands): 0 by construction'))
# binomial tail: P(blank hits <= observed | random-cell null)
from math import comb
n, k = len(inmap), len(blank_hits)
p_le = sum(comb(n, j)*exp**j*(1-exp)**(n-j) for j in range(0, k+1))
rows.append(('fill', 'P(blank hits <= observed | random-cell null)', f'{p_le:.3f}', 'small = target is more table-like than random; near 0.5 = indistinguishable from random values'))

# null C (rule 3, same-axis control): the target's units digits are 0/1-heavy and the sparse columns' blanks are not
# uniform over units digits, so redraw each mapped value as a random row of the SAME column with the SAME units digit
expC = 0.0
for v in inmap:
    col = (v//100)*100+1
    cands = [w for w in range(col, col+81) if w % 10 == v % 10]
    expC += sum(fm[w]=='blank' for w in cands)/len(cands)
expC /= len(inmap)
p_leC = sum(comb(n, j)*expC**j*(1-expC)**(n-j) for j in range(0, k+1))
rows.append(('fill', 'null C: expected blank fraction, same column AND same units digit', f'{expC:.3f}', 'controls for the target 0/1 units skew'))
rows.append(('fill', 'P(blank hits <= observed | null C)', f'{p_leC:.3f}', 'the fill screen against the units-matched null'))
blank_units = Counter(w % 10 for w in fm if fm[w]=='blank')
rows.append(('fill', 'blank cells by units digit 0..9 (all five columns)', ' '.join(str(blank_units[d]) for d in range(10)), ''))

# (c) the 901-1099 block: table fully populated there (frame 954 cols 901, 1001: every row 1-81 filled, read directly)
b = sum(901 <= v <= 1099 for v in g)
nb = [sum(c <= v <= c+199 for v in g) for c in (701, 1101)]
rows.append(('block', 'target groups in 901-1099 vs the two flanking 200-blocks (701-900, 1101-1300)', f'{b} vs {nb[0]} / {nb[1]}', 'the table has 200 ordinary entries there (consul, twelve, are, find, europe, june, power, time, virginia ...)'))
# comparator: THE972 real usage (Armstrong's other 1808 letters, a sequential table of the same size class), same three windows
spec = importlib.util.spec_from_file_location('ustats', ROOT/'tools/data/uscodes-1800/stats.py')
m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
pooled = [int(x) for v in m.THE972_USAGE.values() for x in v.split()]
pb = sum(901 <= v <= 1099 for v in pooled); pnb = [sum(c <= v <= c+199 for v in pooled) for c in (701, 1101)]
rows.append(('block', 'THE972 real usage pooled (474 tokens), same windows', f'{pb} vs {pnb[0]} / {pnb[1]}', 'sequential-table usage shows no such trough'))
# within-target: is 901-1099 the emptiest 200-window among 101-1700?
wins = {c: sum(c <= v <= c+199 for v in g) for c in range(101, 1501, 100)}
rows.append(('block', 'target 200-windows 101-1700 (start:count)', ' '.join(f'{c}:{n}' for c, n in wins.items()), f'min at {min(wins, key=wins.get)}'))

# (d) units digits: a sequential table gives near-flat usage; the target's shape
u = Counter(v % 10 for v in g); pu = Counter(v % 10 for v in pooled)
rows.append(('units', 'target units-digit shares 0..9', ' '.join(f'{u[d]/N:.2f}' for d in range(10)), 'digit 0+1 = %.2f' % ((u[0]+u[1])/N)))
rows.append(('units', 'THE972 real usage units-digit shares 0..9', ' '.join(f'{pu[d]/len(pooled):.2f}' for d in range(10)), 'digit 0+1 = %.2f' % ((pu[0]+pu[1])/len(pooled))))
# the frame-954 table's own decade rows (x0) are ordinary entries (netherlands, able, ove, ation, it ...): no reason for 0/1 skew

with open(HERE/'screen954.tsv', 'w') as f:
    f.write('section\tstatistic\tvalue\tnote\n')
    for r in rows: f.write('\t'.join(r)+'\n')
for r in rows: print(' | '.join(r))
