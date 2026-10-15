#!/usr/bin/env python3
"""C1161-S275 gates per s275/PREREG-C1161-275.md (addendum B): K per reader (exactly as ssplit/PREREG-C1161-SSPLIT.md), A on both-decided
windows (raw >= 0.85, kappa >= 0.60), reconciliation list (windows where R1 and R2 do not both decide the same class), and -- once
s275/read_R3.tsv exists -- final class = the class >= 2 of R1/R2/R3 decided, else ?, T (O >= 20, L >= 20), and the step-2 harness.
  python3 s275/score.py      (run from the target folder)"""
import csv, os, collections
H = os.path.dirname(os.path.abspath(__file__)); T = os.path.dirname(H)
def tok(R):
    key = {r['wid']: (r['line'], int(r['pos'])) for r in csv.DictReader(open(f'{H}/key_{R}.tsv'), delimiter='\t')}
    rd = {r['wid'].strip(): r['shape'].strip() for r in csv.DictReader(open(f'{H}/read_{R}.tsv'), delimiter='\t')}
    miss = [w for w in key if w not in rd]
    if miss:
        print(f'{R}: {len(miss)} windows not returned -> counted ?')
    return {t: (rd.get(w, '?') if rd.get(w, '?') in ('O', 'L') else '?') for w, t in key.items()}
K = {('c188L_L24', 19): 'L', ('c185R_L23', 19): 'L', ('c187L_L15', 27): 'L', ('c188L_L07', 18): 'L',
     ('c185R_L18', 5): 'O', ('c187R_L22', 6): 'O', ('c187R_L25', 12): 'O', ('c188L_L27', 20): 'O', ('c187R_L22', 4): 'O'}
r1, r2 = tok('R1'), tok('R2'); gate = {}
for name, t in (('R1', r1), ('R2', r2)):
    for k, v in K.items():
        print(f'K({name})', k, 'agreed', v, 'read', t[k])
    q = sum(t[k] == '?' for k in K); ok = sum(t[k] == v for k, v in K.items()); n = len(K) - q
    gate[name] = ok >= 8 and q <= 1
    c = collections.Counter(t.values())
    print(f"K({name}): {ok}/{n} decided to agreed class, {q} marked ? -> {'PASS' if gate[name] else 'FAIL'}   (O {c['O']}, L {c['L']}, ? {c['?']})")
both = [k for k in r1 if r1[k] in 'OL' and r2[k] in 'OL']
agree = sum(r1[k] == r2[k] for k in both); n = len(both)
po = agree / n if n else 0
p1 = collections.Counter(r1[k] for k in both); p2 = collections.Counter(r2[k] for k in both)
pe = sum(p1[c] * p2[c] for c in 'OL') / n / n if n else 1
kap = (po - pe) / (1 - pe) if pe < 1 else 0
gate['A'] = po >= 0.85 and kap >= 0.60
cm = collections.Counter((r1[k], r2[k]) for k in both)
print(f"A: both decided {n}; raw agreement {po:.3f}; kappa {kap:.3f} -> {'PASS' if gate['A'] else 'FAIL'}   {dict(cm)}")
rec = [k for k in r1 if not (r1[k] in 'OL' and r1[k] == r2[k])]
with open(f'{H}/recon_tokens.tsv', 'w') as f:
    f.write('line\tpos\n'); [f.write(f'{l}\t{p}\n') for l, p in rec]
print('reconciliation windows:', len(rec))
if not all(gate.values()):
    print('GATE FAIL: stop (no harness)'); raise SystemExit(0)
if not os.path.exists(f'{H}/read_R3.tsv'):
    print('R3 not read yet'); raise SystemExit(0)
r3 = tok('R3'); fin = {}
for k in r1:
    v = collections.Counter(x for x in (r1[k], r2[k], r3.get(k, '?')) if x in 'OL')
    top = [c for c, m in v.items() if m >= 2]
    fin[k] = top[0] if top else '?'
c = collections.Counter(fin.values()); gt = c['O'] >= 20 and c['L'] >= 20
print(f"T: O {c['O']}, L {c['L']}, ? {c['?']} -> {'PASS' if gt else 'FAIL'}")
with open(f'{H}/final_split.tsv', 'w') as f:
    f.write('line\tpos\tR1\tR2\tR3\tfinal\n'); [f.write(f"{l}\t{p}\t{r1[(l,p)]}\t{r2[(l,p)]}\t{r3.get((l,p),'-')}\t{fin[(l,p)]}\n") for l, p in r1]
if not gt:
    raise SystemExit(0)
rows = list(csv.DictReader(open(f'{T}/ciphertext.tsv'), delimiter='\t'))
with open(f'{H}/ciphertext_split.tsv', 'w', newline='') as f:
    w = csv.DictWriter(f, rows[0].keys(), delimiter='\t'); w.writeheader()
    for r in rows:
        if r['sign'] == 'S':
            r = dict(r, sign={'O': 'So', 'L': 'Sl'}.get(fin[(r['line'], int(r['pos']))], 'S'))
        w.writerow(r)
kr = list(csv.DictReader(open(f'{T}/key.tsv'), delimiter='\t'))
for name, P2 in (('key_split.tsv', False), ('key_split_P2.tsv', True)):
    with open(f'{H}/{name}', 'w', newline='') as f:
        w = csv.DictWriter(f, kr[0].keys(), delimiter='\t'); w.writeheader()
        for r in kr:
            if P2 and r['sign'] == 'a':
                r = dict(r, value='o')
            w.writerow(r)
            if r['sign'] == 'S':
                for s in ('So', 'Sl'):
                    w.writerow(dict(r, sign=s, source='C1161-S275 harness: S split by R1/R2/R3 blind shape reads, value as S'))
print('harness written')
