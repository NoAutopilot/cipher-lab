#!/usr/bin/env python3
"""LVN-4611P2 (15 Oct 2026): build lvn4611/key_p2a.tsv and key_p2b.tsv for the per-token read of WVO 4611 p2 (PREREG-LVN-4611.md,
addendum LVN-4611P2); build_key.py's rule on lvn4611/ciphertext_4611_pre_p2.tsv. Units: p2a = lines p2_L01-L18, p2b = p2_L19-L33.
Targets = every M numeral row; A150/B150 from settle_log_4611.tsv (absent = 'agree-flagged', A150 = B150 = sign); 10 controls = H numeral
rows on the unit's lines (random.Random(20261015).sample), candidates = sign + one seeded one-digit look-alike; rows shuffled, same seed.
usage: build_key_p2.py [--check]"""
import csv, io, os, random, sys
H = os.path.dirname(os.path.abspath(__file__)); T = os.path.dirname(H)
rd = lambda p: list(csv.DictReader(open(p), delimiter='\t'))
pre = rd(os.path.join(H, 'ciphertext_4611_pre_p2.tsv'))
sl = {(r['line'], r['col']): r for r in rd(os.path.join(T, 'settle_log_4611.tsv'))}
SW = dict(zip('0123456789', '6738938164'))
UNITS = {'p2a': (1, 18), 'p2b': (19, 33)}
stale = False
for u, (lo, hi) in UNITS.items():
    ct = [r for r in pre if lo <= int(r['line'][4:]) <= hi]
    tg = [r for r in ct if r['confidence'] == 'M' and r['sign'].isdigit()]
    lines = {r['line'] for r in tg}
    pool = [r for r in ct if r['confidence'] == 'H' and r['sign'].isdigit() and r['line'] in lines]
    R = random.Random(20261015)
    cs = R.sample(pool, 10)
    rows = []
    for r in tg:
        s = sl.get((r['line'], r['position']))
        A, B = (s['A'], s['B']) if s else (r['sign'], r['sign'])
        c = sorted({v for v in (A, B) if v != '-'}); R.shuffle(c)
        rows.append([r['line'], r['position'], 'target', r['sign'], A, B, ' | '.join(c)])
    for r in cs:
        s = r['sign']; i = R.randrange(len(s)); la = s[:i] + SW[s[i]] + s[i + 1:]
        c = [s, la]; R.shuffle(c)
        rows.append([r['line'], r['position'], 'control', s, s, s, ' | '.join(c)])
    R.shuffle(rows)
    out = io.StringIO(); out.write('tid\tline\tposition\trole\tsign\tA150\tB150\tcandidates\n')
    for i, r in enumerate(rows, 1): out.write('%s%03d\t' % (u.upper(), i) + '\t'.join(r) + '\n')
    p = os.path.join(H, 'key_%s.tsv' % u)
    if '--check' in sys.argv:
        if not os.path.exists(p) or open(p).read() != out.getvalue(): print('STALE', p); stale = True
    else:
        open(p, 'w').write(out.getvalue()); print(u, len(tg), 'targets,', len(cs), 'controls')
if '--check' in sys.argv: print('STALE' if stale else 'up to date')
sys.exit(1 if stale else 0)
