#!/usr/bin/env python3
"""C1161-SSPLIT gates K and T (PREREG-C1161-SSPLIT.md) from sort.tsv + windows_key.tsv; writes the split harness
ciphertext_split.tsv / key_split.tsv when both pass.   python3 ssplit/ss_score.py   (run from the target folder)"""
import csv, os, collections
H = os.path.dirname(os.path.abspath(__file__)); T = os.path.dirname(H)
sort = {r['wid']: r['shape'] for r in csv.DictReader(open(f'{H}/sort.tsv'), delimiter='\t')}
key = {r['wid']: (r['line'], int(r['pos'])) for r in csv.DictReader(open(f'{H}/windows_key.tsv'), delimiter='\t')}
tok = {v: sort[k] for k, v in key.items()}
K = {('c188L_L24', 19): 'L', ('c185R_L23', 19): 'L', ('c187L_L15', 27): 'L', ('c188L_L07', 18): 'L',
     ('c185R_L18', 5): 'O', ('c187R_L22', 6): 'O', ('c187R_L25', 12): 'O', ('c188L_L27', 20): 'O', ('c187R_L22', 4): 'O'}
q = sum(tok[t] == '?' for t in K); ok = sum(tok[t] == v for t, v in K.items()); n = len(K) - q
for t, v in K.items():
    print('K', t, 'agreed', v, 'sort', tok[t])
gk = ok >= 8 and q <= 1 if n >= 8 else False
print(f'K: {ok}/{n} sorted to agreed class, {q} marked ? -> {"PASS" if gk else "FAIL"}')
c = collections.Counter(tok.values()); gt = c['O'] >= 20 and c['L'] >= 20
print(f'T: O {c["O"]}, L {c["L"]}, ? {c["?"]} -> {"PASS" if gt else "FAIL"}')
if gk and gt:
    rows = list(csv.DictReader(open(f'{T}/ciphertext.tsv'), delimiter='\t'))
    with open(f'{H}/ciphertext_split.tsv', 'w', newline='') as f:
        w = csv.DictWriter(f, rows[0].keys(), delimiter='\t'); w.writeheader()
        for r in rows:
            if r['sign'] == 'S':
                s = tok[(r['line'], int(r['pos']))]; r = dict(r, sign={'O': 'So', 'L': 'Sl'}.get(s, 'S'))
            w.writerow(r)
    kr = list(csv.DictReader(open(f'{T}/key.tsv'), delimiter='\t'))
    with open(f'{H}/key_split.tsv', 'w', newline='') as f:
        w = csv.DictWriter(f, kr[0].keys(), delimiter='\t'); w.writeheader()
        for r in kr:
            w.writerow(r)
            if r['sign'] == 'S':
                for s in ('So', 'Sl'):
                    w.writerow(dict(r, sign=s, source='C1161-SSPLIT harness: S split by one-reader shape sort, value as S'))
    print('harness written')
