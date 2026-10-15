#!/usr/bin/env python3
"""LVN-P2 (15 Oct 2026): build lvn10p2/key.tsv for the LVN16-3R per-token read of WVO 4610 p2 (lvn10p2/PREREG-LVN-P2.md),
same shape as lvn10p1/key.tsv: targets = every M numeral row of ciphertext_4610.tsv on p2; A150/B150 = the two 150-dpi passes
from settle_log_4610.tsv (A, B; '-' = segmentation gap); 10 controls = H numeral rows on the same lines
(random.Random(20261015).sample), each candidate list = sign plus one look-alike by a seeded one-digit swap
(map 0>6 1>7 2>3 3>8 4>9 5>3 6>8 7>1 8>6 9>4); rows shuffled with the same seed. Deterministic; --check exits 1 if stale."""
import csv, io, os, random, sys
H = os.path.dirname(os.path.abspath(__file__)); T = os.path.dirname(H)
rd = lambda p: list(csv.DictReader(open(p), delimiter='\t'))
ct = [r for r in rd(os.path.join(T, 'ciphertext_4610.tsv')) if r['line'].startswith('p2_')]
sl = {(r['line'], r['col']): r for r in rd(os.path.join(T, 'settle_log_4610.tsv'))}
num = lambda s: s.isdigit()
tg = [r for r in ct if r['confidence'] == 'M' and num(r['sign'])]
lines = {r['line'] for r in tg}
pool = [r for r in ct if r['confidence'] == 'H' and num(r['sign']) and r['line'] in lines]
R = random.Random(20261015)
cs = R.sample(pool, 10)
SW = dict(zip('0123456789', '6738938164'))
rows = []
for r in tg:
    s = sl[(r['line'], r['position'])]; A, B = s['A'], s['B']
    c = sorted({v for v in (A, B) if v != '-'}); R.shuffle(c)
    rows.append([r['line'], r['position'], 'target', r['sign'], A, B, ' | '.join(c)])
for r in cs:
    s = r['sign']; i = R.randrange(len(s)); la = s[:i] + SW[s[i]] + s[i + 1:]
    c = [s, la]; R.shuffle(c)
    rows.append([r['line'], r['position'], 'control', s, s, s, ' | '.join(c)])
R.shuffle(rows)
out = io.StringIO(); out.write('tid\tline\tposition\trole\tsign\tA150\tB150\tcandidates\n')
for i, r in enumerate(rows, 1): out.write('T%02d\t' % i + '\t'.join(r) + '\n')
p = os.path.join(H, 'key.tsv')
if '--check' in sys.argv:
    st = not os.path.exists(p) or open(p).read() != out.getvalue(); print('STALE' if st else 'up to date'); sys.exit(1 if st else 0)
open(p, 'w').write(out.getvalue()); print(len(tg), 'targets,', len(cs), 'controls')
