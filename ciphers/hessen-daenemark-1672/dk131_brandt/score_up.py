#!/usr/bin/env python3
"""BRANDT-UP known-answer test (PREREG-BRANDT-UP.md). Reads values_gate.tsv (C rows), ciphertext_0020u.tsv,
ciphertext_0021.tsv, gloss_0020u.txt and the gloss column of ciphertext_0021.tsv; prints real LCS, control stats, gate."""
import csv, random, re, sys, os
H = os.path.dirname(os.path.abspath(__file__))
def norm(s):
    s = s.lower().replace('ä','ae').replace('ö','oe').replace('ü','ue').replace('ß','ss')
    s = re.sub(r'\[\?\]', '', s)
    return re.sub(r'[^a-z]', '', s)
def rows(fn):
    return [r for r in csv.DictReader((l for l in open(os.path.join(H, fn)) if not l.startswith('#')), delimiter='\t')]
key = {r['value']: r['letter'] for r in rows('values_gate.tsv') if r['grade'] == 'C'}
def groups(fn):
    return [r['token'] for r in rows(fn) if re.fullmatch(r'\d+', r['token'])]
g20 = groups('ciphertext_0020u.tsv'); g21 = groups('ciphertext_0021.tsv')
gl20 = norm(open(os.path.join(H, 'gloss_0020u.txt')).read().split('\n#')[0] if False else
            ''.join(l for l in open(os.path.join(H, 'gloss_0020u.txt')) if not l.startswith('#')))
gl21 = norm(''.join(r['gloss'] for r in rows('ciphertext_0021.tsv') if r['gloss'] not in ('', '^')))
def lcs(a, b):
    prev = [0]*(len(b)+1)
    for x in a:
        cur = [0]
        for j, y in enumerate(b):
            cur.append(prev[j]+1 if x == y else max(prev[j+1], cur[j]))
        prev = cur
    return prev[-1]
def stat(k):
    s = 0
    for g, gl in ((g20, gl20), (g21, gl21)):
        seq = [k[v] for v in g if v in k]
        s += lcs(seq, gl)
    return s
nC = sum(1 for g in (g20, g21) for v in g if v in key)
real = stat(key)
rng = random.Random(20261009); vals = sorted(key); lets = [key[v] for v in vals]; ctl = []
for _ in range(2000):
    p = lets[:]; rng.shuffle(p); ctl.append(stat(dict(zip(vals, p))))
ctl.sort(); p99 = ctl[int(0.99*len(ctl))-1]; mean = sum(ctl)/len(ctl)
p = (1 + sum(c >= real for c in ctl)) / 2001
print(f'groups 0020u {len(g20)} 0021 {len(g21)}; C-value tokens {nC}; gloss letters 0020u {len(gl20)} 0021 {len(gl21)}')
print(f'real LCS {real}; control mean {mean:.2f} p99 {p99} max {ctl[-1]} n 2000; p = {p:.4f}')
if nC < 10: print('NON-TEST at this N (fewer than 10 C-value tokens)')
else: print('GATE', 'PASS' if (real > p99 and p < 0.01) else 'FAIL')
