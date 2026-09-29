#!/usr/bin/env python3
"""DEB-SWARM2 R2-1 ORDER-DOSE (29 Sept 2026). D's frozen order battery (swarm/G-D/dcore.py, imported, not edited,
not retuned) on three texts, with D's calibration regenerated at each text's own N, K, curve, line lengths and
noise, under a noise model mixing replacement with insertion/deletion 3:1 (DIGEST-1 section 2).

Texts (each a pair: c1-shaped first member, c2-shaped second member, one key per pair, as D's pair score):
  a  = (c3, c4)           settled drafts, D's punctuation class and clear spans dropped (dcore.target)
  b  = (c1, c2) folded    PCT-SLASH->PCT, X-DOT->X, X-CURL->X
  c  = (c1, c2) strokes   BAR-SOLID, BAR-THIN, DASH-V dropped as well (BLOB, HOOK-L, DASH-H already dropped by D)
Usage: r21.py calib TEXT P N OUT   |   r21.py real TEXT OUT"""
import os, sys, json, random, collections
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', '..', 'G-D')); import dcore
FOLD = {'PCT-SLASH': 'PCT', 'X-DOT': 'X', 'X-CURL': 'X'}
STROKES = {'BAR-SOLID', 'BAR-THIN', 'BLOB', 'DASH-V', 'DASH-H', 'HOOK-L'}

def texts(tid):
    if tid == 'a': return dcore.target('c3'), dcore.target('c4')
    t1, t2 = dcore.target('c1'), dcore.target('c2')
    if tid == 'b': f = lambda ls: [[FOLD.get(s, s) for s in l] for l in ls]
    elif tid == 'c': f = lambda ls: [l for l in ([s for s in l if s not in STROKES] for l in ls) if l]
    elif tid == 'raw': f = lambda ls: ls
    return f(t1), f(t2)

def mixnoise(seq, p, rng, n_out, indel=0.25, fresh=0.5):
    """Per token, with prob p an error: replacement (1-indel), else deletion or insertion (half each). Replaced or
    inserted signs are fresh ids half the time (as dcore.noise), else drawn from the text's own curve. Cut to n_out."""
    cnt = collections.Counter(seq); ids = list(cnt); w = [cnt[i] for i in ids]; out = []; k = 0
    def draw():
        nonlocal k
        if rng.random() < fresh: k += 1; return f'N{k}'
        return rng.choices(ids, w)[0]
    for s in seq:
        if rng.random() < p:
            r = rng.random()
            if r < 1 - indel: out.append(draw())
            elif r < 1 - indel / 2: pass                       # deletion
            else: out.append(s); out.append(draw())            # insertion
        else: out.append(s)
    assert len(out) >= n_out, 'slack too small'
    return out[:n_out]

def make_pair_mix(design, lens1, lens2, curve, rng, p):
    """dcore.make_pair with p=0 on 12 pct longer texts (same key / same writer), then mixnoise cut to the target N."""
    N1, N2 = sum(lens1), sum(lens2); e1, e2 = int(N1 * 1.12) + 3, int(N2 * 1.12) + 3
    a, b = dcore.make_pair(design, [e1], [e2], curve, rng, 0.0, 0.0)
    return dcore.cut(mixnoise(a[0], p, rng, N1), lens1), dcore.cut(mixnoise(b[0], p, rng, N2), lens2)

DESIGNS = ['FR-HOMO', 'EN-HOMO', 'PT-HOMO', 'LA-HOMO', 'FR-SYLL', 'NULL-IID']

if __name__ == '__main__':
    mode, tid = sys.argv[1], sys.argv[2]
    t1, t2 = texts(tid); L1 = [len(l) for l in t1]; L2 = [len(l) for l in t2]; cv = dcore.curve_of(t1 + t2)
    if mode == 'calib':
        p, n, out = float(sys.argv[3]), int(sys.argv[4]), sys.argv[5]
        with open(out, 'w') as fo:
            for d in DESIGNS:
                rng = random.Random(f'r21-calib-{tid}-{d}-{p}')
                for i in range(n):
                    a, b = make_pair_mix(d, L1, L2, cv, rng, p)
                    fo.write(json.dumps(dict(text=tid, design=d, p=p, f=dcore.features(a, b, rng))) + '\n'); fo.flush()
    elif mode == 'real':
        out = []
        for seed in range(5): out.append(dcore.features(t1, t2, random.Random(1000 + seed), 400))
        res = dict(text=tid, N=(sum(L1), sum(L2)), K=len(cv), feats=out,
                   score={w: [round(dcore.score(f, w), 2) for f in out] for w in ('c1', 'c2', 'pair')})
        json.dump(res, open(sys.argv[3], 'w'), indent=1); print(tid, res['N'], res['K'], res['score'])
