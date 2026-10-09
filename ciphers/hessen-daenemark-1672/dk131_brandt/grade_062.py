#!/usr/bin/env python3
"""BRANDT-062 grades (PREREG-BRANDT-062.md, gate PASS): per-line LCS traceback of the C-value letters against the line's gloss letters.
C = C-value token LCS-matched to its line's gloss; M = every other cipher token. Writes reading_062.tsv; --check exits 1 if stale.
--sens drops the worker-settled glosses (L04 'König', L02 'gulden[?]') and reprints the gate."""
import csv, os, re, sys, random
H = os.path.dirname(os.path.abspath(__file__))
def norm(s):
    s = s.lower().replace('ä','ae').replace('ö','oe').replace('ü','ue').replace('ß','ss'); s = re.sub(r'\[\?\]', '', s)
    return re.sub(r'[^a-z]', '', s)
def rows(fn): return list(csv.DictReader((l for l in open(os.path.join(H, fn)) if not l.startswith('#')), delimiter='\t'))
key = {r['value']: r['letter'] for r in rows('values_gate.tsv') if r['grade'] == 'C'}
R = [r for r in rows('ciphertext_0062.tsv') if re.fullmatch(r'\d+', r['token'])]
if '--sens' in sys.argv:
    for r in R:
        if r['gloss'] in ('König', 'gulden[?]'): r['gloss'] = ''
L = sorted(set(r['line'] for r in R))
def lcs_tb(a, b):
    n, m = len(a), len(b); T = [[0]*(m+1) for _ in range(n+1)]
    for i in range(n):
        for j in range(m): T[i+1][j+1] = T[i][j]+1 if a[i] == b[j] else max(T[i][j+1], T[i+1][j])
    i, j, hit = n, m, set()
    while i and j:
        if a[i-1] == b[j-1] and T[i][j] == T[i-1][j-1]+1: hit.add(i-1); i -= 1; j -= 1
        elif T[i-1][j] >= T[i][j-1]: i -= 1
        else: j -= 1
    return T[n][m], hit
out, tot = [], 0
for l in L:
    rr = [r for r in R if r['line'] == l]; gl = norm(''.join(r['gloss'] for r in rr if r['gloss'] not in ('', '^')))
    cidx = [k for k, r in enumerate(rr) if r['token'] in key]
    s, hit = lcs_tb([key[rr[k]['token']] for k in cidx], gl); tot += s
    matched = {cidx[h] for h in hit}; inword = False
    for k, r in enumerate(rr):
        inword = r['gloss'] != '' and (r['gloss'] != '^' or inword)
        g = 'C' if (k in matched and inword) else 'M'  # PREREG: unglossed C-value tokens are M
        out.append((l, r['pos'], r['token'], key.get(r['token'], ''), 'glossed' if inword else 'unglossed', g))
if '--sens' in sys.argv:
    rng = random.Random(20261009); vals = sorted(key); lets = [key[v] for v in vals]; ctl = []
    def st(k):
        t = 0
        for l in L:
            rr = [r for r in R if r['line'] == l]; gl = norm(''.join(r['gloss'] for r in rr if r['gloss'] not in ('', '^')))
            t += lcs_tb([k[r['token']] for r in rr if r['token'] in k], gl)[0]
        return t
    for _ in range(2000):
        p = lets[:]; rng.shuffle(p); ctl.append(st(dict(zip(vals, p))))
    ctl.sort(); print(f'sensitivity: real {tot}; control p99 {ctl[1979]} max {ctl[-1]}'); sys.exit(0)
txt = 'line\tpos\ttoken\tC_letter\tgloss_cover\tgrade\n' + ''.join('\t'.join(map(str, o)) + '\n' for o in out)
fn = os.path.join(H, 'reading_062.tsv')
if '--check' in sys.argv:
    ok = os.path.exists(fn) and open(fn).read() == txt; print('reading_062.tsv', 'current' if ok else 'STALE'); sys.exit(0 if ok else 1)
open(fn, 'w').write(txt)
from collections import Counter
print('LCS', tot, Counter(o[5] for o in out), Counter((o[4], o[5]) for o in out))
