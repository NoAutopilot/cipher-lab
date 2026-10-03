#!/usr/bin/env python3
"""Score key no.70 against a leaf's own period interlinear gloss (NV01-READ, 3 Oct 2026).

  python3 gloss_score.py LINES.tsv [--key keys/key_no70.tsv] [--shuffles 200] [--seed 1] [--err E]

LINES.tsv: columns line, digits, gloss (digits = reconciled two-digit groups separated by spaces, non-digit tokens in
[brackets]; gloss = the period interlinear letters, space separated). For each line the key's decode (nulls dropped,
qu->q, j->i, v->u) is aligned to the gloss by edit distance; agreement = matched letters / gloss letters, pooled.
Null: the same with the key's values permuted over its codes, --shuffles times (max and mean reported).
--err E: power control -- replace a fraction E of the digit groups with a random two-digit group before decoding.
"""
import argparse, random, re, sys

def load_key(p):
    k = {}
    for ln in open(p):
        if ln.startswith('#') or ln.startswith('code\t') or not ln.strip(): continue
        c, v = ln.rstrip('\n').split('\t')[:2]
        k[c] = v
    return k

def norm(s):
    return s.lower().replace('qu', 'q').replace('j', 'i').replace('v', 'u')

def decode(groups, key):
    out = []
    for g in groups:
        v = key.get(g)
        if v is None or v == 'NULL': continue
        out.append(norm(v))
    return ''.join(out)

def align(a, b):
    n, m = len(a), len(b)
    D = [[0]*(m+1) for _ in range(n+1)]
    for i in range(n+1): D[i][0] = i
    for j in range(m+1): D[0][j] = j
    for i in range(1, n+1):
        for j in range(1, m+1):
            D[i][j] = min(D[i-1][j]+1, D[i][j-1]+1, D[i-1][j-1]+(a[i-1] != b[j-1]))
    i, j, match = n, m, 0
    while i > 0 and j > 0:
        if D[i][j] == D[i-1][j-1]+(a[i-1] != b[j-1]):
            match += a[i-1] == b[j-1]; i -= 1; j -= 1
        elif D[i][j] == D[i-1][j]+1: i -= 1
        else: j -= 1
    return match

def load_lines(p):
    rows = []
    for ln in open(p):
        if ln.startswith('#') or ln.startswith('line\t') or not ln.strip(): continue
        f = ln.rstrip('\n').split('\t')
        groups = re.sub(r'\[[^\]]*\]', ' ', f[1]).split()
        gloss = norm(''.join(f[2].split())) if len(f) > 2 and f[2] != 'NONE' else ''
        rows.append((f[0], groups, gloss))
    return rows

def score(rows, key):
    m = t = 0
    for _, g, gl in rows:
        if not gl: continue
        m += align(decode(g, key), gl); t += len(gl)
    return m / t if t else 0.0, m, t

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('lines'); ap.add_argument('--key', default='keys/key_no70.tsv')
    ap.add_argument('--shuffles', type=int, default=200); ap.add_argument('--seed', type=int, default=1)
    ap.add_argument('--err', type=float, default=0.0)
    a = ap.parse_args()
    rng = random.Random(a.seed)
    key = load_key(a.key); rows = load_lines(a.lines)
    if a.err:
        rows = [(l, [(f'{rng.randrange(100):02d}' if rng.random() < a.err else x) for x in g], gl) for l, g, gl in rows]
    real, m, t = score(rows, key)
    codes, vals = list(key), list(key.values()); null = []
    for _ in range(a.shuffles):
        rng.shuffle(vals); null.append(score(rows, dict(zip(codes, vals)))[0])
    mean = sum(null)/len(null); sd = (sum((x-mean)**2 for x in null)/len(null))**.5
    print(f'real {real:.3f} ({m}/{t} gloss letters) | shuffled-key n={a.shuffles} mean {mean:.3f} max {max(null):.3f} '
          f'z {(real-mean)/sd if sd else 0:.1f} | err {a.err} | rank {1+sum(x>=real for x in null)}/{a.shuffles+1}')
    for l, g, gl in rows:
        print(f'  {l}\tdecode {decode(g, key)}\n  {"":{len(l)}}\tgloss  {gl}')

if __name__ == '__main__':
    main()
