#!/usr/bin/env python3
"""BRANDT-REGRADE known-answer re-score of 0062 (PREREG-BRANDT-062B.md). Same statistic, control, seed and gate as score_062.py, but the
gloss of each line comes from one BLIND pass file (gloss62_blindA.tsv or gloss62_blindB.tsv: line, gloss_text) named on the command line,
and the key is values_gate.tsv's C rows after the V-BRANDT regrade. `--worker` scores the worker gloss column instead (reference only)."""
import csv, random, re, sys, os
H = os.path.dirname(os.path.abspath(__file__))
def norm(s):
    s = s.lower().replace('ä','ae').replace('ö','oe').replace('ü','ue').replace('ß','ss')
    s = re.sub(r'\[\?\]', '', s)
    return re.sub(r'[^a-z]', '', s)
def rows(fn):
    return [r for r in csv.DictReader((l for l in open(os.path.join(H, fn)) if not l.startswith('#')), delimiter='\t')]
key = {r['value']: r['letter'] for r in rows('values_gate.tsv') if r['grade'] == 'C'}
R = [r for r in rows('ciphertext_0062.tsv') if re.fullmatch(r'\d+', r['token'])]
L = sorted(set(r['line'] for r in R))
if sys.argv[1:] and sys.argv[1] == '--worker':
    G = {l: norm(''.join(r['gloss'] for r in R if r['line'] == l and r['gloss'] not in ('', '^'))) for l in L}; src = 'worker gloss column'
else:
    src = sys.argv[1]; G = {l: '' for l in L}
    for r in rows(src):
        l = r['line'] if r['line'].startswith('L') else 'L%02d' % int(r['line'])
        G[l] += norm(r['gloss_text'])
lines = [([r['token'] for r in R if r['line'] == l], G[l]) for l in L]
def lcs(a, b):
    prev = [0]*(len(b)+1)
    for x in a:
        cur = [0]
        for j, y in enumerate(b):
            cur.append(prev[j]+1 if x == y else max(prev[j+1], cur[j]))
        prev = cur
    return prev[-1]
def stat(k):
    return sum(lcs([k[v] for v in g if v in k], gl) for g, gl in lines)
nC = sum(1 for g, _ in lines for v in g if v in key)
real = stat(key)
rng = random.Random(20261009); vals = sorted(key); lets = [key[v] for v in vals]; ctl = []
for _ in range(2000):
    p = lets[:]; rng.shuffle(p); ctl.append(stat(dict(zip(vals, p))))
ctl.sort(); p99 = ctl[int(0.99*len(ctl))-1]; mean = sum(ctl)/len(ctl)
p = (1 + sum(c >= real for c in ctl)) / 2001
print(f'gloss: {src}; C values {len(key)}; lines {len(lines)}; groups {len(R)}; C-value tokens {nC}; gloss letters {sum(len(gl) for _, gl in lines)}')
print(f'real LCS {real}; control mean {mean:.2f} p99 {p99} max {ctl[-1]} n 2000; p = {p:.4f}')
if nC < 10: print('NON-TEST at this N (fewer than 10 C-value tokens)')
else: print('GATE', 'PASS' if (real > p99 and p < 0.01) else 'FAIL')
