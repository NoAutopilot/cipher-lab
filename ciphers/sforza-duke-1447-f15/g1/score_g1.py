#!/usr/bin/env python3
"""SFZ-G1 (14 Oct 2026) gloss-agreement score, fixed in ../PREREG-SFZ-G1.md before any decode.
Reads the decode_key.py token files for the R5323 key; decodes the control keys and permutations in-process with the same
token sequence (sign column of those token files).   python3 score_g1.py > score.out"""
import os, random, glob
H = os.path.dirname(os.path.abspath(__file__)); D = os.path.join(H, '..', '..', 'sforza-italien1584-1447', 'duke')
UNITS = [('f5', 'tokens_f5.tsv', 'clear_f7.txt'), ('f8', 'tokens_f8.tsv', 'clear_f10.txt')]

def gloss(fn):
    t = ''.join(l for l in open(os.path.join(D, fn)) if not l.startswith('#')).lower()
    t = ''.join(ch for ch in t if 'a' <= ch <= 'z')
    return t.translate(str.maketrans('vjy', 'uii'))

def tokens(fn):
    rows = open(os.path.join(H, fn)).read().split('\n'); hdr = rows[0].split('\t')
    si, vi = hdr.index('sign'), hdr.index('value')
    return [(r.split('\t')[si], r.split('\t')[vi]) for r in rows[1:] if r]

def align(dec, g):
    # global alignment, match +1, mismatch 0, gap -0.5; returns number of matched letters on one optimal path
    n, m = len(dec), len(g); G = -0.5
    prev = [(j * G, 0) for j in range(m + 1)]
    for i in range(1, n + 1):
        cur = [(i * G, 0)] + [None] * m; di = dec[i - 1]
        for j in range(1, m + 1):
            mt = 1 if di == g[j - 1] else 0
            a = (prev[j - 1][0] + mt, prev[j - 1][1] + mt); b = (prev[j][0] + G, prev[j][1]); c = (cur[j - 1][0] + G, cur[j - 1][1])
            cur[j] = max(a, b, c)
        prev = cur
    return prev[m][1]

def decode(signs, key): return [key.get(s, '?') for s in signs]

def readkey(p):
    k = {}
    for l in open(p).read().split('\n')[1:]:
        if l: s, v, _ = l.split('\t'); k[s] = v
    return k

def score(key, data):
    out = {}
    for u, signs, g in data: out[u] = align(decode(signs, key), g)
    return out

def main():
    data = []; real = {}
    for u, tf, gf in UNITS:
        tk = tokens(tf); signs = [s for s, _ in tk]; g = gloss(gf)
        data.append((u, signs, g))
        real[u] = align([v if v not in ('', '?') else '?' for _, v in tk], g)
    n = {u: len(s) for u, s, _ in data}; N = sum(n.values())
    key = readkey(os.path.join(H, 'key_r5323.tsv'))
    cov = {u: sum(1 for x in s if x in key) / len(s) for u, s, _ in data}
    R = (real['f5'] + real['f8']) / N
    print(f'# R5323 key: {len(key)} rows; tokens f5 {n["f5"]} f8 {n["f8"]}; gloss letters f5 {len(data[0][2])} f8 {len(data[1][2])}')
    print(f'unit\tA\tn\trate\tcoverage')
    for u in ('f5', 'f8'): print(f'{u}\t{real[u]}\t{n[u]}\t{real[u]/n[u]:.4f}\t{cov[u]:.3f}')
    print(f'pooled\t{real["f5"]+real["f8"]}\t{N}\t{R:.4f}\t{sum(cov[u]*n[u] for u in n)/N:.3f}')
    rng = random.Random(1447); labs = sorted(key); vals = [key[k] for k in labs]; nulls = []
    for _ in range(1000):
        v = vals[:]; rng.shuffle(v); s = score(dict(zip(labs, v)), data); nulls.append(s)
    pooled = sorted((s['f5'] + s['f8']) / N for s in nulls)
    p = (1 + sum(1 for x in pooled if x >= R)) / 1001
    def p95(xs): xs = sorted(xs); return xs[int(0.95 * len(xs)) - 1]
    u95 = {u: p95([s[u] / n[u] for s in nulls]) for u in n}
    print(f'# permutation null (1000, seed 1447): pooled mean {sum(pooled)/len(pooled):.4f} p95 {p95(pooled):.4f} max {pooled[-1]:.4f}; p = {p:.4f}')
    print(f'# unit p95: f5 {u95["f5"]:.4f} f8 {u95["f8"]:.4f}')
    print('control\trows\tf5_rate\tf8_rate\tpooled\tcoverage')
    cmax = 0
    for f in sorted(glob.glob(os.path.join(H, 'ctl', 'key_*.tsv'))):
        k = readkey(f); s = score(k, data); pr = (s['f5'] + s['f8']) / N; cmax = max(cmax, pr)
        cv = sum(1 for u, sg, _ in data for x in sg if x in k) / N
        print(f'{os.path.basename(f)[4:-4]}\t{len(k)}\t{s["f5"]/n["f5"]:.4f}\t{s["f8"]/n["f8"]:.4f}\t{pr:.4f}\t{cv:.3f}')
    lk = readkey(os.path.join(H, 'key_r5323_loose.tsv')); s = score(lk, data)
    print(f'# sensitivity (loose key, {len(lk)} rows, not gated): pooled {(s["f5"]+s["f8"])/N:.4f}')
    a, b = p <= 0.01, R > cmax; c = all(real[u] / n[u] > u95[u] for u in n)
    print(f'# gate: (a) p<=0.01 {a}; (b) R {R:.4f} > max control {cmax:.4f} {b}; (c) both units > own p95 {c}: '
          f'{"PASS" if a and b and c else "FAIL"}')

if __name__ == '__main__': main()
