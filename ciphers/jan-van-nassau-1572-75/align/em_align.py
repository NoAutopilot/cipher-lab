#!/usr/bin/env python3
"""Hard-EM alignment of cipher groups to printed plaintext (known-plaintext key recovery, grade C).

Each cipher run (from passes/align_<n>.tsv, RUN rows carry the print span in 'print: ...') is aligned to the letters of
its printed span by dynamic programming: every group emits 0 (null), 1, 2 or 3 letters (a syllable), or a whole word.
Scores come from the current key counts (smoothed); the prior favours one letter per group. Iterates until stable.
Writes align/pairs_<n>.tsv (group -> chunk per position) and align/key_counts.tsv (value, chunk, count, total).
Usage: em_align.py 5222 [5218 ...]
"""
import csv, math, re, sys, unicodedata, collections, os
HERE = os.path.dirname(os.path.abspath(__file__))
def letters(s):
    s = unicodedata.normalize('NFD', s.lower()); s = ''.join(c for c in s if c.isalpha() and c.isascii())
    return s.replace('j', 'i').replace('v', 'u').replace('w', 'uu')
def load(n):
    runs = []; cur = None
    for r in csv.DictReader(open(f'{HERE}/../passes/align_{n}.tsv'), delimiter='\t'):
        if r['group'] == 'RUN':
            m = re.search(r"print:\s*'(.*?)'\s*(\(Groen|$)", r['plain'])
            span = m.group(1) if m else ''
            span = span.split('...')[0]
            cur = {'span': span, 'plain': letters(span), 'groups': [], 'pos': []}; runs.append(cur)
        else:
            cur['groups'].append(r['group']); cur['pos'].append((r['page'], r['line'], r['idx']))
    return runs
PRIOR = {0: math.log(0.10), 1: math.log(0.80), 2: math.log(0.06), 3: math.log(0.04)}
def align(groups, plain, C, T, first):
    n, m = len(groups), len(plain); NEG = -1e18
    D = [[NEG] * (m + 1) for _ in range(n + 1)]; B = [[None] * (m + 1) for _ in range(n + 1)]; D[0][0] = 0
    for i in range(n):
        g = groups[i]; tot = T.get(g, 0)
        for j in range(m + 1):
            if D[i][j] == NEG: continue
            for k in (0, 1, 2, 3):
                if j + k > m: continue
                ch = plain[j:j + k] if k else '-'
                if first: s = PRIOR[k]
                else: s = PRIOR[k] + math.log((C.get((g, ch), 0) + 0.02) / (tot + 1.0))
                if D[i][j] + s > D[i + 1][j + k]: D[i + 1][j + k] = D[i][j] + s; B[i + 1][j + k] = (j, ch)
    # allow unmatched tail of plain (print span may run past the cipher): best end column
    jbest = max(range(m + 1), key=lambda j: D[n][j] - 3.0 * (m - j))
    out = []; j = jbest
    for i in range(n, 0, -1):
        pj, ch = B[i][j]; out.append(ch); j = pj
    return out[::-1], jbest
def main(ns):
    runs = [(n, r) for n in ns for r in load(n)]
    C = collections.Counter(); T = collections.Counter(); prev = None
    for it in range(12):
        newC = collections.Counter(); newT = collections.Counter(); res = []
        for n, r in runs:
            if len(r['groups']) < 0.5 * len(r['plain']) or not r['plain']: res.append((n, r, None, 0)); continue
            a, used = align(r['groups'], r['plain'], C, T, it == 0)
            res.append((n, r, a, used))
            for g, ch in zip(r['groups'], a): newC[(g, ch)] += 1; newT[g] += 1
        C, T = newC, newT
        sig = [tuple(x[2] or ()) for x in res]
        if sig == prev: break
        prev = sig
    print('iterations', it + 1)
    for n in ns:
        with open(f'{HERE}/pairs_{n}.tsv', 'w') as f:
            f.write('page\tline\tidx\tgroup\tchunk\trun_span\n')
            for nn, r, a, used in res:
                if nn != n: continue
                for k, g in enumerate(r['groups']):
                    ch = a[k] if a else '?'
                    f.write('\t'.join(r['pos'][k]) + f'\t{g}\t{ch}\t{r["span"][:60]}\n')
    with open(f'{HERE}/key_counts.tsv', 'w') as f:
        f.write('value\tchunk\tcount\ttotal\n')
        for g in sorted(T, key=lambda x: int(x) if x.isdigit() else 9999):
            for ch, c in sorted(((ch, c) for (gg, ch), c in C.items() if gg == g), key=lambda x: -x[1]):
                f.write(f'{g}\t{ch}\t{c}\t{T[g]}\n')
    for nn, r, a, used in res:
        if a: print(nn, r['span'][:50], '|', '.'.join(a), f'({used}/{len(r["plain"])} letters)')
if __name__ == '__main__': main(sys.argv[1:])
