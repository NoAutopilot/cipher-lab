#!/usr/bin/env python3
"""Depth check for WVO 11008 under the 8 Oct 2026 depth bar (AUD2-WVO11008): authentication distance vs the
longest H stretch.

  python3 depth_ad.py

H(K) is the design's key space (a 23-letter simple substitution: log2 23!), not the period table's zero-liberty
key -- an unfitted period table does not shrink H(K) to the liberties (the bar). Two liberties are added (run 4
pos 5 M, run 5 pos 3 g-for-i). R is reported three ways: held-out fr16 4-gram redundancy (measured), the textbook
French 3.2, and the ceiling log2(alphabet) (all redundancy counted, the most generous possible AD).
The longest stretch counts consecutive H-graded letters inside one run (nulls skipped; runs are separated by
clear text, so no stretch crosses a run boundary).
"""
import csv, glob, gzip, math, os, re
from collections import Counter
H = os.path.dirname(os.path.abspath(__file__)); R0 = os.path.join(H, '..', '..')
key = {int(r['code']): r['value'] for r in csv.DictReader(open(os.path.join(H, '..', 'jan-van-nassau-1572-75', 'key_1572.tsv')), delimiter='\t')}
# reading grades per token (NOTES.md "Grading", KHF-2): M = run 1 all, run 3 all, run 4 pos 5, run 5 pos 3 and 12
M = {(1, p) for p in range(1, 5)} | {(3, p) for p in range(1, 9)} | {(4, 5), (5, 3), (5, 12)}
best = (0, ''); cur = ''; last = None
for r in csv.DictReader(open(os.path.join(H, 'ciphertext.tsv')), delimiter='\t'):
    run, pos, code = int(r['run']), int(r['pos']), int(r['code'])
    if run != last: cur = ''; last = run
    v = key.get(code)
    if v == 'NULL': continue
    if v is None or (run, pos) in M: cur = ''; continue
    cur += v
    if len(cur) > best[0]: best = (len(cur), cur)
t = ''
for f in sorted(glob.glob(os.path.join(R0, 'tools', 'data', 'fr16', '*.gz'))): t += gzip.open(f, 'rt', errors='replace').read().lower()
t = re.sub(r'[^a-z]', '', t.translate(str.maketrans('àâçéèêëîïôûùüjvwk', 'aaceeeeiiouuuiuuc')))
V = len(set(t)); tr, te = t[:len(t) // 2], t[len(t) // 2:][:400000]
C4 = Counter(tr[i:i + 4] for i in range(len(tr) - 3)); C3 = Counter(tr[i:i + 3] for i in range(len(tr) - 2))
h = -sum(math.log2((C4[te[i - 3:i + 1]] + .01) / (C3[te[i - 3:i]] + .01 * V)) for i in range(3, len(te))) / (len(te) - 3)
HK = math.log2(math.factorial(23)) + 2 * math.log2(23)
print(f'longest H stretch: {best[0]} letters ({best[1]})')
print(f'H(K) = log2(23!) + 2 liberties = {HK:.1f} bits; fr16 alphabet {V}, held-out 4-gram entropy {h:.3f} bits/letter')
for name, R in (('fr16 4-gram measured', math.log2(V) - h), ('textbook French', 3.2), ('ceiling log2(V)', math.log2(V))):
    U = HK / R; print(f'R={R:.2f} ({name}): unicity {U:.1f}, AD {1.5 * U:.1f} letters -> clause {"MET" if best[0] > 1.5 * U else "not met"}')
