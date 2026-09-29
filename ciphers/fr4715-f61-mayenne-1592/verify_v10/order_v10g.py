#!/usr/bin/env python3
"""VERIFY-F61-V10 part (g), written and committed before running: claim (4), the f.124r 4TRI widening by a/n (H356-H358), and the split draft
(H360/H365, after the brief's window but on the same question), under this verifier's own order statistic (order_v10.py: own letter model, exact
decoder, seeds 10010 for the within-run shuffles).
  (g1) widening: gain with 4TRI = c/p/t + a/n vs 30 widenings of c/p/t by 2 letters drawn by fr16 frequency without replacement, c/p/t and the
       pair a/n excluded (seed 10070) -- the H358 design, re-coded. On f.124r (the claim), f.97r, and in-sample f.101r and f.188r. 'Pointer
       stands' on a leaf iff the a/n widening beats >= 0.95 of the random widenings. A pointer on f.124r is specific to that leaf's readers'
       4TRI only if it is not equally present on every leaf; f.101r's no-bowl share (H365: 0.64) predicts a pointer there too, f.188r unknown.
  (g2) split drafts: passes/recf124r_split and passes/recf101r_split (the readers' no-bowl 4TRI relabelled C43, v7 unchanged) under the full
       order test (100 binned null keys, bins of 3) beside the unsplit drafts' figures from order_v10_a_result.txt, plus 10 shuffled targets
       each (order_v10.py part b's design; valid iff <= 2/10).
No cell changed, no reading.  python3 order_v10g.py [--check]"""
import os, random, sys
from multiprocessing import Pool
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import order_v10 as o
def widen(args):
    p, seed = args
    runs, cl = o.leafdata(p); sh = o.shuffles(runs, 10010); base = o.basekey(cl)
    if "4TRI" not in base: return p, None
    named = o.gain(dict(base, **{"4TRI": ("a", "c", "n", "p", "t")}), runs, sh)
    rng = random.Random(seed); lf = {a: o.C[1][a] for a in o.ALPHA if a not in "cpt"}; alts = set()
    while len(alts) < 30:
        pool = dict(lf); s = []
        for _ in range(2):
            x = rng.random() * sum(pool.values())
            for a, w in pool.items():
                x -= w
                if x <= 0: break
            s.append(a); del pool[a]
        if set(s) != {"a", "n"}: alts.add(tuple(sorted(s)))
    ga = [o.gain(dict(base, **{"4TRI": tuple(sorted(set("cpt") | set(a)))}), runs, sh) for a in sorted(alts)]
    return p, (named, sum(named > g for g in ga) / 30, sum(ga) / 30, max(ga), o.gain(base, runs, sh))
if __name__ == "__main__":
    out = []
    with Pool(4) as pool:
        out.append("(g1) 4TRI c/p/t widened by a/n vs 30 frequency-drawn 2-letter widenings (seed 10070)")
        for p, r in pool.map(widen, [(p, 10070) for p in ("recf124r", "recf97r", "recf101r", "recf188r")]):
            out.append(f"{p}: " + ("no 4TRI" if r is None else f"v7 gain {r[4]:.4f}; a/n-widened {r[0]:.4f}; random widenings mean {r[2]:.4f} max {r[3]:.4f}; beats {r[1]:.2f} -> "
                                    + ("pointer stands" if r[1] >= 0.95 else "added letters, not these letters")))
        out.append("(g2) split drafts (no-bowl 4TRI -> C43), key v7 unchanged, bins of 3, 100 null keys; shuffled targets 10 x 40 keys")
        jobs, tags = [], []
        for p in ("recf124r_split", "recf101r_split"):
            runs, cl = o.leafdata(p); jobs.append((o.basekey(cl), runs, cl, 100, 10020, 3, 10010)); tags.append((p, runs))
        for (t, runs), r in zip(tags, pool.map(o.test, jobs)): out.append(o.fmt(t, runs, r, 100))
        for p in ("recf124r_split", "recf101r_split"):
            runs, cl = o.leafdata(p); rng = random.Random(10030); jobs = []
            for t in range(10):
                flat = [s for r in runs for s in r]; rng.shuffle(flat); it = iter(flat); jobs.append((o.basekey(cl), [[next(it) for _ in r] for r in runs], cl, 40, 10020 + t, 3, 10010))
            res = pool.map(o.test, jobs); fp = sum(r[0] > r[1] for r in res)
            out.append(f"{p}: shuffled targets with 'order signal' {fp}/10 -> " + ("design valid" if fp <= 2 else "VOID"))
    txt = "\n".join(out) + "\n"; rs = f"{HERE}/order_v10_g_result.txt"
    if "--check" in sys.argv:
        ok = os.path.exists(rs) and open(rs).read() == txt; print("check", "OK" if ok else "STALE"); sys.exit(0 if ok else 1)
    open(rs, "w").write(txt); print(txt, end="")
