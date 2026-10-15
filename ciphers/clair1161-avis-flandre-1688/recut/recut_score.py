#!/usr/bin/env python3
"""C1161-RECUT gate K exactly as ssplit/PREREG-C1161-SSPLIT.md (>= 8 of the not-? K windows to the agreed class AND <= 1 marked ?)
and T, on sort A (ssplit/sort.tsv) and sort B (sort2/sort_B.tsv) with the three K windows' rows replaced by the blind re-reads of
the re-cut windows (recut/read_A.tsv -> A, recut/read_B.tsv -> B; rid -> token via recut/recut_key.tsv). If K(A') and T pass, writes
the registered SSPLIT step-2 harness on sort A' (recut/ciphertext_split.tsv, key_split.tsv, key_split_P2.tsv).   run from the target folder"""
import csv, os, collections
H = os.path.dirname(os.path.abspath(__file__)); T = os.path.dirname(H)
rd = lambda p, k='wid': {r[k]: r['shape'].strip() for r in csv.DictReader(open(p), delimiter='\t')}
wkey = {r['wid']: (r['line'], int(r['pos'])) for r in csv.DictReader(open(f'{T}/ssplit/windows_key.tsv'), delimiter='\t')}
inv = {v: k for k, v in wkey.items()}
rkey = {r['rid']: (r['line'], int(r['pos'])) for r in csv.DictReader(open(f'{H}/recut_key.tsv'), delimiter='\t')}
K = {('c188L_L24', 19): 'L', ('c185R_L23', 19): 'L', ('c187L_L15', 27): 'L', ('c188L_L07', 18): 'L',
     ('c185R_L18', 5): 'O', ('c187R_L22', 6): 'O', ('c187R_L25', 12): 'O', ('c188L_L27', 20): 'O', ('c187R_L22', 4): 'O'}
RECUT = [('c185R_L23', 19), ('c185R_L18', 5), ('c188L_L07', 18)]
def apply(sort, reads):
    s = dict(sort)
    for rid, t in rkey.items():
        if t in RECUT:
            s[inv[t]] = reads[rid]
    return {wkey[w]: v for w, v in s.items()}
res = {}
for name, sp, rp in (('A', f'{T}/ssplit/sort.tsv', f'{H}/read_A.tsv'), ('B', f'{T}/sort2/sort_B.tsv', f'{H}/read_B.tsv')):
    tok = apply(rd(sp), rd(rp, 'rid'))
    for t, v in K.items():
        print(f"K{name}'", t, 'agreed', v, 'sort', tok[t], '(re-cut)' if t in RECUT else '')
    q = sum(tok[t] == '?' for t in K); ok = sum(tok[t] == v for t, v in K.items()); n = len(K) - q
    gk = ok >= 8 and q <= 1
    c = collections.Counter(tok.values()); gt = c['O'] >= 20 and c['L'] >= 20
    print(f"K({name}'): {ok}/{n} decided to agreed class, {q} marked ? -> {'PASS' if gk else 'FAIL'}")
    print(f"T({name}'): O {c['O']}, L {c['L']}, ? {c['?']} -> {'PASS' if gt else 'FAIL'}")
    res[name] = (gk and gt, tok)
ok, tok = res['A']
if ok:
    rows = list(csv.DictReader(open(f'{T}/ciphertext.tsv'), delimiter='\t'))
    with open(f'{H}/ciphertext_split.tsv', 'w', newline='') as f:
        w = csv.DictWriter(f, rows[0].keys(), delimiter='\t'); w.writeheader()
        for r in rows:
            if r['sign'] == 'S':
                r = dict(r, sign={'O': 'So', 'L': 'Sl'}.get(tok[(r['line'], int(r['pos']))], 'S'))
            w.writerow(r)
    kr = list(csv.DictReader(open(f'{T}/key.tsv'), delimiter='\t'))
    for fn, p2 in (('key_split.tsv', False), ('key_split_P2.tsv', True)):
        with open(f'{H}/{fn}', 'w', newline='') as f:
            w = csv.DictWriter(f, kr[0].keys(), delimiter='\t'); w.writeheader()
            for r in kr:
                if p2 and r['sign'] == 'a':
                    r = dict(r, value='o')
                w.writerow(r)
                if r['sign'] == 'S':
                    for s in ('So', 'Sl'):
                        w.writerow(dict(r, sign=s, source="C1161-RECUT harness: S split by sort A' (SSPLIT sort, 3 K windows re-cut and re-read), value as S"))
    print("harness written (sort A')")
else:
    print("NON-TEST: K(A') or T failed; step 2 not run")
