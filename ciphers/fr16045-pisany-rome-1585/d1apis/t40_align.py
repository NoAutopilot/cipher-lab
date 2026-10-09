#!/usr/bin/env python3
"""D1A-PIS (PREREG-D1A-PIS.md): key86 T40 witness from the seven pages already aligned with their Colbert 16 pt II copies.
Each masked token decodes as one neutral slot (symbol 26, -1 against every letter); the clear letter aligned to it is its
witness. Gate G, null N0 and power control P exactly as pre-registered.
    python3 d1apis/t40_align.py [--check]   (--check: recompute and exit 1 if result.json / t40_witness.tsv differ)"""
import os, sys, json
from collections import Counter
import numpy as np
H = os.path.dirname(os.path.abspath(__file__)); T = os.path.dirname(H)
sys.path.insert(0, os.path.join(T, 'kp86')); sys.path.insert(0, os.path.join(T, '../../tools'))
from kp86 import norm, load_key
from stream_align import band_dp, A
PAGES = [('f244r', 'tx86/ciphertext_f244r.tsv', 'kp86/colbert_p49_50.txt'),
         ('f244v_f245r', 'tx86c/ciphertext_f244v_f245r.tsv', 'kp86b/colbert_p51_52.txt'),
         ('f247r', 'tx86g/ciphertext_f247r.tsv', 'kp86g/colbert_f247r.txt'),
         ('f275r', 'tx86e/ciphertext_f275r.tsv', 'kp86d/colbert_p121_123.txt'),
         ('f275v', 'tx86f/ciphertext_f275v.tsv', 'kp86f/colbert_f275v.txt'),
         ('f301v', 'tx87/ciphertext_f301v_preT32.tsv', 'kp87a/colbert_p338_339.txt'),
         ('f302v', 'tx87b/ciphertext_f302v_preT32.tsv', 'kp87b/colbert_p341_342.txt')]
KEY = load_key()
E = np.full((A + 1, A), -1.0); E[np.arange(A), np.arange(A)] = 2.0


def load(tx, cl):
    toks, where = [], []
    for ln in open(os.path.join(T, tx)):
        lab, body = ln.rstrip('\n').split('\t')
        if tx.startswith('tx86f') and lab not in {f'L{i:02d}' for i in range(1, 17)}:
            continue
        for k, t in enumerate(x for x in body.split() if x != '/'):
            toks.append(t.rstrip('?')); where.append((lab, k + 1))
    clear = np.array([ord(c) - 97 for c in norm(open(os.path.join(T, cl)).read())])
    return toks, where, clear


DATA = [(p,) + load(tx, cl) for p, tx, cl in PAGES]


def witness(toks, clear, masked):
    letters, owner = [], []
    for i, t in enumerate(toks):
        if i in masked:
            letters.append(A); owner.append(i); continue
        for c in KEY.get(t, ''):
            letters.append(ord(c) - 97); owner.append(i)
    dec = np.array(letters); N, M = len(dec), len(clear)
    ref = np.linspace(0, min(M, N), N + 1) if M >= N else np.arange(N + 1) * (M / N)
    path, _, _ = band_dp(dec, clear, E, ref, max(200, abs(M - N) + 200), 1.0, 1.0, free_start=True)
    got = {owner[i]: chr(97 + clear[j]) for i, j in path if dec[i] == A}
    return {i: got.get(i, 'GAP') for i in masked}


def top(ws):
    c = Counter(ws); v, n = max(((k, n) for k, n in c.items() if k != 'GAP'), key=lambda x: x[1], default=('-', 0))
    return v, n, n / len(ws)


def main():
    rng = np.random.default_rng(20261008)
    out = {}
    rows, allw = [], []
    for p, toks, where, clear in DATA:
        m = {i for i, t in enumerate(toks) if t == 'T40'}
        w = witness(toks, clear, m)
        for i in sorted(m):
            rows.append(f'{p}\t{where[i][0]}\t{where[i][1]}\t{w[i]}'); allw.append(w[i])
    v, n, s = top(allw)
    out['T40'] = dict(N=len(allw), letters=dict(Counter(allw).most_common()), top=v, count=n, share=round(s, 3),
                      per_page={p: dict(Counter(r.split('\t')[3] for r in rows if r.startswith(p + '\t'))) for p, *_ in DATA},
                      G=bool(s >= 0.70 and n >= 5))
    nT = [sum(t == 'T40' for t in toks) for _, toks, _, _ in DATA]
    nulls = []
    for d in range(200):
        ws = []
        for (p, toks, where, clear), k in zip(DATA, nT):
            pool = [i for i, t in enumerate(toks) if t != 'T40' and len(KEY.get(t, '')) == 1]
            ws += list(witness(toks, clear, set(rng.choice(pool, k, replace=False).tolist())).values())
        nulls.append(top(ws)[2])
    out['N0'] = dict(draws=200, mean=round(float(np.mean(nulls)), 3), p95=round(float(np.percentile(nulls, 95)), 3),
                     max=round(float(max(nulls)), 3), passes=bool(np.percentile(nulls, 95) < 0.70),
                     p_ge_obs=round(float(np.mean(np.array(nulls) >= s)), 3))
    for cell in ('T17', 'T46'):
        allpos = [(pi, i) for pi, (_, toks, _, _) in enumerate(DATA) for i, t in enumerate(toks) if t == cell]
        k = min(len(allT := allpos), sum(nT)); hits, shares = 0, []
        for d in range(50):
            pick = [allT[x] for x in rng.choice(len(allT), k, replace=False)]
            ws = []
            for pi, (p, toks, where, clear) in enumerate(DATA):
                m = {i for q, i in pick if q == pi}
                if m:
                    ws += list(witness(toks, clear, m).values())
            tv, tn, ts = top(ws); shares.append(ts); hits += (tv == KEY[cell] and ts >= 0.70)
        out['P_' + cell] = dict(key=KEY[cell], available=len(allT), masked=k, draws=50, hit_rate=hits / 50,
                                mean_share=round(float(np.mean(shares)), 3), passes=bool(hits / 50 >= 0.80))
    return out, 'page\tline\tpos\taligned\n' + '\n'.join(rows) + '\n'


if __name__ == '__main__':
    out, tsv = main()
    js = json.dumps(out, indent=1, sort_keys=True) + '\n'
    rp, wp = os.path.join(H, 'result.json'), os.path.join(H, 't40_witness.tsv')
    if '--check' in sys.argv:
        ok = os.path.exists(rp) and open(rp).read() == js and open(wp).read() == tsv
        print('up to date' if ok else 'STALE'); sys.exit(0 if ok else 1)
    open(rp, 'w').write(js); open(wp, 'w').write(tsv); print(js)
