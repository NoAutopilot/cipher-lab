#!/usr/bin/env python3
"""DEB-SWARM-D escape-route battery (29 Sept 2026). A language hidden from the order score by the system itself:
(1) POLY-SHARED: p homophonic alphabets over ONE shared sign set used in turn (Vigenere-like); test = periodicity
    scan (period.py) -- position-dependent sign distribution.
(2) TRANS-R: homophonic FR letters then a columnar transposition with column height R (plaintext neighbours land R
    apart); test = MI at every distance d 1..60 on the text read in line order, max z over d.
(3) NULLS-q: a share q of random null signs interleaved (drawn from the same curve); test = the frozen c2 score.
(4) WORDMIX: the 60 commonest words as single signs, every other word spelled with homophonic letters; frozen score.
(5) VERTICAL: the text written down columns and transcribed across rows; test = MI between vertical neighbours.
Each route: 20 controls at c2 shape, 15 pct type noise, X-like null 0.13 where marked; the real c2 through the same
test. Writes escape.json."""
import dcore, period, random, math, collections, json, statistics as st, sys
t2 = dcore.target('c2'); L2 = [len(l) for l in t2]; N2 = sum(L2); cv = dcore.curve_of(t2)
rng = random.Random(4242)
def homo_seq(units, curve, rng, prefix='S'):
    key, _ = dcore.alloc(units, curve, rng); names = {}; k = 0
    for u in key:
        for b in key[u]: names[id(b)] = f'{prefix}{k}'; k += 1
    out = []
    for u in units:
        if u not in key: u = rng.choice(list(key))
        b = rng.choices(key[u], [x[1] for x in key[u]])[0]; out.append(names[id(b)])
    return out
def poly_shared(p):
    u = dcore.units('fr', N2, rng, 'letters'); keys = []
    for i in range(p):
        key, _ = dcore.alloc(u, cv, rng); names = {}; perm = list(range(len(cv))); rng.shuffle(perm); k = 0
        for x in key:
            for b in key[x]: names[id(b)] = f'S{perm[k]}'; k += 1   # same sign set, different assignment
        keys.append((key, names))
    out = []
    for i, x in enumerate(u):
        key, names = keys[i % p]
        if x not in key: x = rng.choice(list(key))
        b = rng.choices(key[x], [y[1] for y in key[x]])[0]; out.append(names[id(b)])
    return dcore.cut(dcore.noise(out, 0.15, rng), L2)
def trans(R):
    s = homo_seq(dcore.units('fr', N2, rng, 'letters'), cv, rng); C = math.ceil(N2 / R)
    rows = [s[i * C:(i + 1) * C] for i in range(R)]  # write in rows of C, read down columns (height R)
    out = [r[j] for j in range(C) for r in rows if j < len(r)]
    return dcore.cut(dcore.noise(out, 0.15, rng), L2)
def dist_scan(lines, rng, trials=100, D=range(1, 61)):
    seq = [s for l in lines for s in l]
    def mi(q, d):
        c = collections.Counter(zip(q, q[d:])); A = collections.Counter(q[:-d]); B = collections.Counter(q[d:]); n = len(q) - d
        return sum(v / n * math.log2(v * n / (A[a] * B[b])) for (a, b), v in c.items())
    obs = {d: mi(seq, d) for d in D}; sh = {d: [] for d in D}
    for _ in range(trials):
        q = seq[:]; rng.shuffle(q)
        for d in D: sh[d].append(mi(q, d))
    z = {d: (obs[d] - st.mean(sh[d])) / st.pstdev(sh[d]) for d in D}; best = max(z, key=z.get)
    return dict(d=best, z=round(z[best], 2), z_by_d={d: round(v, 2) for d, v in z.items()})
def nulls(q):
    s = homo_seq(dcore.units('fr', int(N2 * (1 - q)) + 5, rng, 'letters'), cv, rng); out = []
    for x in s:
        while rng.random() < q / (1 - q) * 0.5 and len(out) < N2: out.append(rng.choices([f'S{i}' for i in range(len(cv))], cv)[0])
        out.append(x)
        if rng.random() < q / (1 - q) * 0.5 and len(out) < N2: out.append(rng.choices([f'S{i}' for i in range(len(cv))], cv)[0])
    out = (out + out)[:N2]
    out = ['XN' if rng.random() < 0.13 else x for x in out]
    return dcore.cut(dcore.noise(out, 0.15, rng), L2)
W = dcore.words('fr'); TOP = [w for w, _ in collections.Counter(W).most_common(60)]
def wordmix():
    o = rng.randrange(len(W) - 2000); us = []
    for w in W[o:]:
        us += [('W', w)] if w in TOP else list(w)
        if len(us) >= N2: break
    return dcore.cut(dcore.noise(homo_seq(us[:N2], cv, rng), 0.15, rng), L2)
def vertical_mi(lines):
    c = collections.Counter(); A = collections.Counter(); B = collections.Counter()
    for l1, l2 in zip(lines, lines[1:]):
        for a, b in zip(l1, l2): c[(a, b)] += 1; A[a] += 1; B[b] += 1
    n = sum(c.values()); return sum(v / n * math.log2(v * n / (A[a] * B[b])) for (a, b), v in c.items())
def vertical_z(lines, rng, trials=200):
    obs = vertical_mi(lines); seq = [s for l in lines for s in l]; lens = [len(l) for l in lines]; sh = []
    for _ in range(trials):
        q = seq[:]; rng.shuffle(q); sh.append(vertical_mi(dcore.cut(q, lens)))
    return round((obs - st.mean(sh)) / st.pstdev(sh), 2)
def vertical_ctrl():
    s = homo_seq(dcore.units('fr', N2, rng, 'letters'), cv, rng); R = len(L2); C = max(L2)
    grid = [[None] * C for _ in range(R)]; k = 0
    for j in range(C):
        for i in range(R):
            if j < L2[i] and k < N2: grid[i][j] = s[k]; k += 1
    out = [grid[i][j] for i in range(R) for j in range(L2[i])]
    return dcore.cut(dcore.noise(out, 0.15, rng), L2)
th = json.load(open('threshold.json'))
def c2score(lines):
    z = dcore.zstats(lines, rng, 100); return z['mi1']['z'] + z['bg2']['z'] + z['rep3']['z'] - z['dbl']['z']
res = {}
def rep(name, vals, tgt):
    v = sorted(vals); res[name] = dict(median=st.median(v), p5=v[max(0, int(0.05 * len(v)) - 0)], min=v[0], max=v[-1], target=tgt, share_le_target=sum(x <= tgt for x in v) / len(v))
    print(name, res[name], flush=True)
n = 20
tp = period.scan(t2, rng, 300)['text']['z']
for p in (3, 7, 13): rep(f'POLY-SHARED-{p} periodicity z', [period.scan(poly_shared(p), rng, 100)['text']['z'] for _ in range(n)], tp)
td = dist_scan(t2, rng, 300); res['target_dist_scan'] = td; print('target dist scan', td['d'], td['z'])
rep('NULL-IID dist-scan z', [dist_scan(dcore.make('NULL-IID', L2, cv, rng), rng)['z'] for _ in range(n)], td['z'])
for R in (7, 19, 33): rep(f'TRANS-{R} dist-scan z', [dist_scan(trans(R), rng)['z'] for _ in range(n)], td['z'])
ts = c2score(t2)
for q in (0.2, 0.35, 0.5): rep(f'NULLS-{q} c2 score', [c2score(nulls(q)) for _ in range(n)], ts)
rep('WORDMIX c2 score', [c2score(wordmix()) for _ in range(n)], ts)
tv = vertical_z(t2, rng)
rep('NULL-IID vertical z', [vertical_z(dcore.make('NULL-IID', L2, cv, rng), rng) for _ in range(n)], tv)
rep('VERTICAL vertical z', [vertical_z(vertical_ctrl(), rng) for _ in range(n)], tv)
json.dump(res, open('escape.json', 'w'), indent=1)
