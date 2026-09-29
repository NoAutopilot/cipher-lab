#!/usr/bin/env python3
"""H342 (runner 13 session_01MSoJWwZxNPSjQd4hszNdvQ, 29 Sept 2026), script-only, written before running: an order statistic for the beam check that
frequency matching cannot pass (H341 voided the binned arm). Per leaf, H335's runs (>= 4 v7-keyed signs) and beam; for a key K,
gain(K) = beam score of the real order - mean beam score over 10 WITHIN-RUN shuffles (each run's signs permuted in place, so run cuts and each run's
sign multiset are unchanged; the same 10 shuffles, seed 342, for every key). v7's gain is compared with the gains of 100 binned-permuted keys (H335's
bin rule, seed 3420). Pre-stated: 'order signal for v7' on a leaf iff gain(v7) > the binned gains' p95. Positive control first: in-sample f.101r and
f.188r must both pass, else the design is a non-test and the held leaves (f.106r rows 1-12, f.124r, f.97r, f.108v two drafts) are reported as
'not tested'.   python3 h342_beam_seqgain.py [--check]"""
import os, random, sys
HERE = os.path.dirname(os.path.abspath(__file__)); ARGS = sys.argv[1:]; out = []
src = open(f"{HERE}/h335_106r_v7_beam.py").read(); src = src[:src.index("real = score(cell)")]
def leaf(prefix):
    g = {"__file__": f"{HERE}/h335_106r_v7_beam.py", "__name__": "h342"}; sys.argv = [sys.argv[0]]
    exec(compile(src.replace("recf106rall/", f"{prefix}/"), f"h335_on_{prefix}", "exec"), g)
    runs, cell, classes, score = g["runs"], g["cell"], g["classes"], g["score"]
    rng = random.Random(342); shuf = []
    for _ in range(10):
        s = []
        for r in runs: r2 = r[:]; rng.shuffle(r2); s.append(r2)
        shuf.append(s)
    def gain(cf):
        g["runs"] = runs; real = score(cf); sh = []
        for s in shuf: g["runs"] = s; sh.append(score(cf))
        g["runs"] = runs; return real - sum(sh) / len(sh)
    gv = gain(cell); bins = [classes[i:i + 3] for i in range(0, len(classes), 3)]; rk = random.Random(3420); null = []
    for _ in range(100):
        mp = {}
        for bn in bins:
            cs = [frozenset(cell(c)) for c in bn]; rk.shuffle(cs); mp.update(zip(bn, cs))
        null.append(gain(lambda c, mp=mp: set(mp.get(c, ()))))
    null.sort(); p95 = null[94]
    return gv, p95, null, len(runs), sum(len(r) for r in runs)
res = {}
for prefix in ("recf101r", "recf188r", "recf106rall", "recf124r", "recf97r", "rec108v", "recf108vg"):
    gv, p95, null, nr, ns = leaf(prefix); res[prefix] = gv > p95
    out.append(f"{prefix}: runs {nr}, signs {ns}; gain(v7) {gv:.4f}; binned gains mean {sum(null) / 100:.4f} p95 {p95:.4f}, >= v7 {sum(x >= gv for x in null)}/100 -> {'order signal' if gv > p95 else 'no order signal'}")
ctl = res["recf101r"] and res["recf188r"]
out.append("positive control (in-sample f.101r and f.188r): " + ("PASS" if ctl else "FAIL -- design a non-test; the held-leaf lines above are 'not tested'"))
if ctl: out.append("held leaves: " + " ".join(f"{p}={'order signal' if res[p] else 'no order signal'}" for p in ("recf106rall", "recf124r", "recf97r", "rec108v", "recf108vg")))
txt = "\n".join(out) + "\n"; rs = f"{HERE}/h342_beam_seqgain_result.txt"
if "--check" in ARGS:
    ok = os.path.exists(rs) and open(rs).read() == txt; print("check", "OK" if ok else "STALE"); sys.exit(0 if ok else 1)
open(rs, "w").write(txt); print(txt, end="")
