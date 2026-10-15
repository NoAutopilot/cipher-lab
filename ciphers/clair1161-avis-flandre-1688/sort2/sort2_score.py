#!/usr/bin/env python3
"""C1161-SORT2 gates K-B, K-AB, A, T (sort2/PREREG-C1161-SORT2.md) from ssplit/sort.tsv (A), sort2/sort_B.tsv (B) and
ssplit/windows_key.tsv; writes the agreed-split harness sort2/ciphertext_split.tsv / key_split.tsv only when all four pass.
python3 sort2/sort2_score.py   (run from the target folder)"""
import csv, os, collections
H = os.path.dirname(os.path.abspath(__file__)); T = os.path.dirname(H)
rd = lambda p: {r['wid']: r['shape'].strip() for r in csv.DictReader(open(p), delimiter='\t')}
A, B = rd(f'{T}/ssplit/sort.tsv'), rd(f'{H}/sort_B.tsv')
key = {r['wid']: (r['line'], int(r['pos'])) for r in csv.DictReader(open(f'{T}/ssplit/windows_key.tsv'), delimiter='\t')}
assert set(A) == set(B) == set(key), 'window sets differ'
AG = {w: (A[w] if A[w] == B[w] and A[w] in 'OL' else '?') for w in key}
K = {('c188L_L24', 19): 'L', ('c185R_L23', 19): 'L', ('c187L_L15', 27): 'L', ('c188L_L07', 18): 'L',
     ('c185R_L18', 5): 'O', ('c187R_L22', 6): 'O', ('c187R_L25', 12): 'O', ('c188L_L27', 20): 'O', ('c187R_L22', 4): 'O'}
inv = {v: k for k, v in key.items()}
for t, v in K.items():
    w = inv[t]; print('K', w, t, 'agreed', v, 'A', A[w], 'B', B[w], 'AB', AG[w])
def kq(S):
    q = sum(S[inv[t]] == '?' for t in K); ok = sum(S[inv[t]] == v for t, v in K.items()); bad = len(K) - q - ok
    return ok, bad, q
ok, bad, q = kq(B); gkb = ok >= 8 and q <= 1
print(f'K-B: {ok}/{ok + bad} decided to agreed class, {q} marked ? -> {"PASS" if gkb else "FAIL"}')
ok, bad, q = kq(AG); gkab = bad == 0 and ok + bad >= 6
print(f'K-AB: {ok} right, {bad} wrong, {ok + bad} decided of 9 -> {"PASS" if gkab else "FAIL"}')
both = [w for w in key if A[w] in 'OL' and B[w] in 'OL']; n = len(both)
agree = sum(A[w] == B[w] for w in both) / n if n else 0
pa = collections.Counter(A[w] for w in both); pb = collections.Counter(B[w] for w in both)
pe = sum(pa[c] * pb[c] for c in 'OL') / n / n if n else 1
kap = (agree - pe) / (1 - pe) if pe < 1 else 0
ga = agree >= 0.85 and kap >= 0.60
print(f'A: both decided {n}; raw agreement {agree:.3f}; kappa {kap:.3f} -> {"PASS" if ga else "FAIL"}')
cm = collections.Counter((A[w], B[w]) for w in key)
print('A x B table (rows A, cols B):'); print('   ' + '  '.join(f'{c:>4}' for c in 'OL?'))
for a in 'OL?':
    print(f'{a}  ' + '  '.join(f'{cm[(a, b)]:>4}' for b in 'OL?'))
c = collections.Counter(AG.values()); gt = c['O'] >= 20 and c['L'] >= 20
print(f'B counts: {dict(collections.Counter(B.values()))}')
print(f'T: agreed O {c["O"]}, L {c["L"]}, ? {c["?"]} -> {"PASS" if gt else "FAIL"}')
with open(f'{H}/agreed_split.tsv', 'w') as f:
    f.write('wid\tline\tpos\tA\tB\tagreed\n')
    for w in sorted(key):
        f.write(f'{w}\t{key[w][0]}\t{key[w][1]}\t{A[w]}\t{B[w]}\t{AG[w]}\n')
if gkb and gkab and ga and gt:
    tok = {v: AG[k] for k, v in key.items()}
    rows = list(csv.DictReader(open(f'{T}/ciphertext.tsv'), delimiter='\t'))
    with open(f'{H}/ciphertext_split.tsv', 'w', newline='') as f:
        w = csv.DictWriter(f, rows[0].keys(), delimiter='\t'); w.writeheader()
        for r in rows:
            if r['sign'] == 'S':
                r = dict(r, sign={'O': 'So', 'L': 'Sl'}.get(tok[(r['line'], int(r['pos']))], 'S'))
            w.writerow(r)
    kr = list(csv.DictReader(open(f'{T}/key.tsv'), delimiter='\t'))
    with open(f'{H}/key_split.tsv', 'w', newline='') as f:
        w = csv.DictWriter(f, kr[0].keys(), delimiter='\t'); w.writeheader()
        for r in kr:
            w.writerow(r)
            if r['sign'] == 'S':
                for s in ('So', 'Sl'):
                    w.writerow(dict(r, sign=s, source='C1161-SORT2 harness: S split by two blind sorts agreeing, value as S'))
    print('ALL PASS: harness written')
else:
    print('NON-TEST: a gate failed; step 2 not run as a test')
