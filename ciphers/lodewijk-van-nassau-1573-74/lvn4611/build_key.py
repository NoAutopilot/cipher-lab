#!/usr/bin/env python3
"""LVN-4611 (15 Oct 2026): build lvn4611/key_<page>.tsv for the LVN16-3R per-token read of WVO 4611 (lvn4611/PREREG-LVN-4611.md),
same shape as lvn10p2/key.tsv. Per unit (page p1, p3): targets = every M numeral row of the page in lvn4611/ciphertext_4611_pre.tsv
(= ciphertext_4611.tsv before this job); A150/B150 = the two 150-dpi passes from settle_log_4611.tsv (A, B; '-' = segmentation gap;
a row absent from settle_log, 'agree-flagged', had both passes agree, so A150 = B150 = sign); 10 controls = H numeral rows on the
same lines (random.Random(20261015).sample), each candidate list = sign plus one look-alike by a seeded one-digit swap
(0>6 1>7 2>3 3>8 4>9 5>3 6>8 7>1 8>6 9>4); rows shuffled with the same seed. Deterministic; --check exits 1 if stale.
usage: build_key.py [--check]   (writes key_p1.tsv and key_p3.tsv)"""
import csv, io, os, random, sys
H = os.path.dirname(os.path.abspath(__file__)); T = os.path.dirname(H)
rd = lambda p: list(csv.DictReader(open(p), delimiter='\t'))
pre = rd(os.path.join(H, 'ciphertext_4611_pre.tsv'))
sl = {(r['line'], r['col']): r for r in rd(os.path.join(T, 'settle_log_4611.tsv'))}
SW = dict(zip('0123456789', '6738938164'))
stale = False
for pg in ('p1', 'p3'):
    ct = [r for r in pre if r['line'].startswith(pg + '_')]
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
    for i, r in enumerate(rows, 1): out.write('%s%02d\t' % (pg.upper(), i) + '\t'.join(r) + '\n')
    p = os.path.join(H, 'key_%s.tsv' % pg)
    if '--check' in sys.argv:
        if not os.path.exists(p) or open(p).read() != out.getvalue(): print('STALE', p); stale = True
    else:
        open(p, 'w').write(out.getvalue()); print(pg, len(tg), 'targets,', len(cs), 'controls')
if '--check' in sys.argv: print('STALE' if stale else 'up to date')
sys.exit(1 if stale else 0)
