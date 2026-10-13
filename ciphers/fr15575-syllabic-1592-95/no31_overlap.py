#!/usr/bin/env python3
"""SYL-31 (13 Oct 2026): count fr.15576 f.2's 3-digit tokens that fall on key no.31's 3-digit codes, against the matched null
pre-registered in PREREG-SYL-31.md (pushed 9928dcc53 before this count). Counts only; no decode, no reading.
  python3 ciphers/fr15575-syllabic-1592-95/no31_overlap.py      (exit 0 always: a census with one gate line)
"""
import csv, os, re, random, collections
H = os.path.dirname(os.path.abspath(__file__))
dig = lambda t: re.sub(r'\D', '', t)
f2 = []
for r in csv.DictReader(open(os.path.join(H, 'f2_fr15576/ciphertext_body.tsv')), delimiter='\t'):
    f2 += r['tokens'].split()
v3 = [int(dig(t)) for t in f2 if len(dig(t)) == 3]
cnt = collections.Counter(v3)
print(f'f.2: {len(f2)} tokens, {len(v3)} 3-digit tokens, {len(cnt)} distinct')
rows = list(csv.DictReader((l for l in open(os.path.join(H, 'key_no31.tsv')) if not l.startswith('#')), delimiter='\t'))
C = sorted({int(dig(r['code'])) for r in rows if len(dig(r['code'])) == 3})
k = len(C)
runs = []
for c in C:
    if runs and c == runs[-1][-1] + 1: runs[-1].append(c)
    else: runs.append([c])
lens = [len(r) for r in runs]
print(f'no.31 3-digit codes: k={k} {C}; runs {lens}')
T = sum(cnt[c] for c in C); D = sum(1 for c in C if cnt[c])
print(f'observed T={T} tokens {[(c, cnt[c]) for c in C if cnt[c]]}, D={D} distinct')
def stat(S): return sum(cnt[c] for c in S)
rng = random.Random(31); N = 10000
def draw_layout():
    while True:
        S = set()
        for L in lens:
            s = rng.randint(100, 999 - L + 1); S |= set(range(s, s + L))
        if len(S) == k: return S
nl = [stat(draw_layout()) for _ in range(N)]
nf = [stat(rng.sample(range(100, 1000), k)) for _ in range(N)]
for name, xs in (('layout (primary)', nl), ('free (secondary)', nf)):
    xs2 = sorted(xs); p = (1 + sum(1 for x in xs if x >= T)) / (N + 1)
    print(f'null {name}: mean {sum(xs)/N:.2f}, p95 {xs2[int(0.95*N)]}, max {xs2[-1]}, p(T>={T}) = {p:.4f}')
p = (1 + sum(1 for x in nl if x >= T)) / (N + 1)
print('GATE (p <= 0.05, layout null):', 'CLEARS' if p <= 0.05 else 'does not clear', f'(p = {p:.4f})')
