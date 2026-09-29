#!/usr/bin/env python3
"""DEB-SWARM-D test P (29 Sept 2026): does the sign depend on its position modulo a period (a periodic polyalphabetic
system over the sign set, e.g. several pigpen-like alphabets used in turn)? Statistic per period p = 2..16: mutual
information between the sign and (index mod p) over the text read in line order; the scan statistic is the largest
z over p against 1,000 whole-text shuffles (which keep every count and destroy position). Also with the index
restarting at each line (a period that restarts at each line). Power control: FR letters under p alphabets, each a
homophonic key over its own share of the target's sign curve, at c2's N with 15 pct type noise."""
import dcore, random, math, collections, json, sys, statistics as st
def mi_mod(seq, p):
    c = collections.Counter((s, i % p) for i, s in enumerate(seq)); S = collections.Counter(seq); n = len(seq)
    P = collections.Counter(i % p for i in range(n))
    return sum(v / n * math.log2(v * n / (S[s] * P[r])) for (s, r), v in c.items())
def mi_mod_lines(lines, p):
    c = collections.Counter((s, i % p) for l in lines for i, s in enumerate(l)); S = collections.Counter(s for l in lines for s in l)
    P = collections.Counter(i % p for l in lines for i in range(len(l))); n = sum(S.values())
    return sum(v / n * math.log2(v * n / (S[s] * P[r])) for (s, r), v in c.items())
def scan(lines, rng, trials=300, P=range(2, 17)):
    seq = [s for l in lines for s in l]; lens = [len(l) for l in lines]
    best = {}
    for mode in ('text', 'line'):
        f = (lambda q, p: mi_mod(q, p)) if mode == 'text' else (lambda q, p: mi_mod_lines(dcore.cut(q, lens), p))
        obs = {p: f(seq, p) for p in P}; sh = {p: [] for p in P}
        for _ in range(trials):
            q = seq[:]; rng.shuffle(q)
            for p in P: sh[p].append(f(q, p))
        zs = {}
        for p in P:
            m = st.mean(sh[p]); sd = st.pstdev(sh[p]); zs[p] = (obs[p] - m) / sd if sd else 0
        pb = max(zs, key=zs.get); best[mode] = dict(p=pb, z=round(zs[pb], 2), z_by_p={p: round(v, 2) for p, v in zs.items()})
    return best
def poly(lens, curve, p, rng, noise=0.15):
    N = sum(lens); u = dcore.units('fr', N, rng, 'letters'); subs = [curve[i::p] for i in range(p)]
    keys = []; off = 0
    for sc in subs:
        key, _ = dcore.alloc(u, sc, rng); names = {}
        for x in key:
            for b in key[x]: names[id(b)] = f'S{off}'; off += 1
        keys.append((key, names))
    out = []
    for i, x in enumerate(u):
        key, names = keys[i % p]
        if x not in key: x = rng.choice(list(key))
        b = rng.choices(key[x], [y[1] for y in key[x]])[0]; out.append(names[id(b)])
    return dcore.cut(dcore.noise(out, noise, rng), lens)
if __name__ == '__main__':
    rng = random.Random(77); res = {}
    for cid in ('c1', 'c2'):
        t = dcore.target(cid); res[cid] = scan(t, rng); print(cid, {m: (v['p'], v['z']) for m, v in res[cid].items()}, flush=True)
    t1, t2 = dcore.target('c1'), dcore.target('c2'); L2 = [len(l) for l in t2]; cv = dcore.curve_of(t2)
    for name, gen in (('NULL-IID', lambda r: dcore.make('NULL-IID', L2, cv, r)), ('POLY-3', lambda r: poly(L2, cv, 3, r)),
                      ('POLY-5', lambda r: poly(L2, cv, 5, r)), ('POLY-7', lambda r: poly(L2, cv, 7, r))):
        zs = [scan(gen(rng), rng, 100) for _ in range(12)]
        res[name] = {m: dict(z_median=st.median(z[m]['z'] for z in zs), z_max=max(z[m]['z'] for z in zs), z_min=min(z[m]['z'] for z in zs)) for m in ('text', 'line')}
        print(name, res[name], flush=True)
    json.dump(res, open('period.json', 'w'), indent=1)
