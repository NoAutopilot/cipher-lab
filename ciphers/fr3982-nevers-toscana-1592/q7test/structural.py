#!/usr/bin/env python3
"""BNF-Q7-TEST step 1: structural fit of BnF fr.3982 f.25 against Nevers key no.62 (key_no62.tsv).
Parse share = max fraction of the digit string covered by key codes in a left-to-right segmentation where
uncovered digits are skipped (leftover). Null: 1000 digit-order shuffles of the same string (seed 62).
'?' rule: (a) removed; (b) wildcard matching any digit (reported both ways). No reading is produced."""
import csv, random, sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); T = os.path.dirname(HERE)
def load_codes():
    codes = []
    for r in csv.reader(open(os.path.join(T, 'key_no62.tsv')), delimiter='\t'):
        if not r or r[0].startswith('#') or r[0] == 'value': continue
        if len(r[0]) <= 3: codes.append(r[0])
    return sorted(set(codes))
def load_ct():
    s = ''
    for r in csv.reader(open(os.path.join(T, 'ciphertext.tsv')), delimiter='\t'):
        if r and r[0].startswith('f25_'): s += r[1]
    return s
def share(s, codes):
    n = len(s); best = [0]*(n+1)
    for i in range(n-1, -1, -1):
        b = best[i+1]
        for c in codes:
            L = len(c)
            if i+L <= n and all(x == '?' or x == y for x, y in zip(s[i:i+L], c)):
                b = max(b, L + best[i+L])
        best[i] = b
    return best[0]/n
if __name__ == '__main__':
    codes = load_codes(); ct = load_ct()
    letters = {'a','b','c','d','e','f','g','h','i','l','m','n','o','p','q','r','s','t','u','v','z'}
    print('codes', len(codes), 'by length', {L: sum(len(c)==L for c in codes) for L in (1,2,3)})
    for mode, s in (('?removed', ct.replace('?', '')), ('?wildcard', ct)):
        obs = share(s, codes); rng = random.Random(62); null = []
        for _ in range(1000):
            l = list(s); rng.shuffle(l); null.append(share(''.join(l), codes))
        null.sort(); p = (1+sum(x >= obs for x in null))/1001
        print(f'{mode}: N={len(s)} parse_share={obs:.3f} shuffle mean={sum(null)/1000:.3f} p95={null[949]:.3f} p99={null[989]:.3f} p={p:.4f}')
