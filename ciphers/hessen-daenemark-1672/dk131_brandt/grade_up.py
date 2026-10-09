#!/usr/bin/env python3
"""BRANDT-UP grades (after the PREREG-BRANDT-UP gate PASS): LCS traceback of each block's C-letter sequence against its gloss;
matched C tokens -> C, unmatched C tokens -> M, non-C groups -> M (meaning from the gloss where it is a word over one group).
Writes reading_up.tsv; --check exits 1 if the committed file is stale (rule 7)."""
import sys, os, re
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import score_up as s
WORD = {'259': 'heuraht (0020u margin + 0021 interlinear)', '244': 'Gesanter (0021)', '209': 'Schwedes (0021)',
        '196': 'der verwittibten Königin (0021)', '156': 'z (zwischen; 0049 also z, M)'}
def trace(a, b):
    n, m = len(a), len(b); L = [[0]*(m+1) for _ in range(n+1)]
    for i in range(n):
        for j in range(m):
            L[i+1][j+1] = L[i][j]+1 if a[i] == b[j] else max(L[i][j+1], L[i+1][j])
    i, j, hit = n, m, set()
    while i and j:
        if a[i-1] == b[j-1] and L[i][j] == L[i-1][j-1]+1: hit.add(i-1); i -= 1; j -= 1
        elif L[i-1][j] >= L[i][j-1]: i -= 1
        else: j -= 1
    return hit
out = ['block\tidx\tvalue\tgrade\tletter_or_meaning\tnote']
nG = {'C': 0, 'M': 0}
for name, g, gl in (('0020u', s.g20, s.gl20), ('0021', s.g21, s.gl21)):
    cidx = [k for k, v in enumerate(g) if v in s.key]
    hit = trace([s.key[g[k]] for k in cidx], gl)
    for k, v in enumerate(g):
        if v in s.key:
            gr = 'C' if cidx.index(k) in hit else 'M'
            out.append(f'{name}\t{k+1}\t{v}\t{gr}\t{s.key[v]}\t{"C value, LCS-matched to gloss" if gr=="C" else "C value, not matched in gloss"}')
        else:
            gr = 'M'; out.append(f'{name}\t{k+1}\t{v}\tM\t{WORD.get(v, "")}\tnot a C value')
        nG[gr] += 1
txt = '\n'.join(out) + f'\n# tokens {sum(nG.values())}: C {nG["C"]}, M {nG["M"]}\n'
fn = os.path.join(s.H, 'reading_up.tsv')
if '--check' in sys.argv:
    ok = os.path.exists(fn) and open(fn).read() == txt
    print('reading_up.tsv', 'up to date' if ok else 'STALE'); sys.exit(0 if ok else 1)
open(fn, 'w').write(txt); print(txt.splitlines()[-1])
