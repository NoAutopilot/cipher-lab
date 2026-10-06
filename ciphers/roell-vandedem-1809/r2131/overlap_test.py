#!/usr/bin/env python3
"""R10-ROELL12: R2131 group overlap with R1469/R1470 vs the 1788-89 Van Dedem family (PREREG.md). Disk only.
Usage: python3 overlap_test.py [--check]   (--check: exit 1 if overlap_result.tsv differs from a fresh run)"""
import random, re, sys, pathlib
H = pathlib.Path(__file__).resolve().parent
def groups(p):
    out = []
    for line in open(p):
        if line.startswith('#'): continue
        out += [int(x) for x in re.findall(r'\d+', line.replace('?', ''))]
    return out
FRAMES = {701, 801, 301, 401, 501, 601, 2504, 2604, 2704}
r2131 = groups(H / 'R2131_cipher.txt')
Q = sorted(set(r2131) - FRAMES)
ROELL = groups(H.parent / 'decode_transcription/R1469_groups.txt') + groups(H.parent / 'decode_transcription/R1470_groups.txt')
FAM = sum((groups(H / f'{r}_cipher.txt') for r in ('R1947', 'R2053', 'R2121', 'R2122')), [])
LO, HI, NDRAW = 2, 3839, 10000
def pct(a, p): a = sorted(a); return a[min(len(a) - 1, int(p * len(a)))]
rows = [('pool', 'tokens', 'distinct', 'Q', 'S', 'S_pct', 'N1_mean', 'N1_p95', 'N1_p99', 'N1_frac_ge', 'N2_mean', 'N2_p99', 'N2_frac_ge')]
for name, pool in (('FAM_positive_control', FAM), ('ROELL_target', ROELL)):
    D = set(pool); S = len(set(Q) & D)
    rng = random.Random(20261006)
    n1 = []
    for _ in range(NDRAW):
        s = set()
        for q in Q:
            while True:
                d = rng.randint(-50, 50)
                v = min(HI, max(LO, q + d))
                if d != 0 and v not in s: s.add(v); break
        n1.append(len(s & D))
    n2 = [len(set(rng.sample(range(LO, HI + 1), len(Q))) & D) for _ in range(NDRAW)]
    rows.append((name, len(pool), len(D), len(Q), S, f'{100*S/len(Q):.1f}', f'{sum(n1)/NDRAW:.2f}', pct(n1, .95), pct(n1, .99),
                 f'{sum(x >= S for x in n1)/NDRAW:.4f}', f'{sum(n2)/NDRAW:.2f}', pct(n2, .99), f'{sum(x >= S for x in n2)/NDRAW:.4f}'))
txt = '\n'.join('\t'.join(map(str, r)) for r in rows) + '\n'
# descriptive: frame/opener positions
R69 = groups(H.parent / 'decode_transcription/R1469_groups.txt'); R70 = groups(H.parent / 'decode_transcription/R1470_groups.txt')
for nm, t in (('R1469', R69), ('R1470', R70), ('R2131', r2131)):
    txt += f'# frames {nm} (n={len(t)}): ' + ', '.join(f'{f}@{[i for i, x in enumerate(t) if x == f]}' for f in sorted(FRAMES) if f in t) + '\n'
out = H / 'overlap_result.tsv'
if '--check' in sys.argv:
    sys.exit(0 if out.exists() and out.read_text() == txt else 1)
out.write_text(txt); print(txt, end='')
