#!/usr/bin/env python3
"""H351 (runner 13 session_01MSoJWwZxNPSjQd4hszNdvQ, 29 Sept 2026), script-only, written before running: power of H342's order statistic at f.106r's
N (51 runs, rows 1-18). From each HELD leaf that shows the order signal (f.124r, f.97r; H342/H344): 30 random 51-run subsets (seed 351); per subset, H342's gain for v7 (10 within-run shuffles)
against 50 binned-permuted keys' gains (H335's bin rule) on the same subset; power = share of subsets with gain(v7) > the binned gains' p95.
Pre-stated: power >= 0.8 on both held leaves -> f.106r's H348 miss stands as a negative relative to other held leaves; else
f.106r's miss is within what a held leaf with a real signal shows at 51 runs -> untestable at this N.   python3 h351_seqgain_heldpower.py [--check]"""
import os, random, sys
HERE = os.path.dirname(os.path.abspath(__file__)); ARGS = sys.argv[1:]; out = []
src = open(f"{HERE}/h335_106r_v7_beam.py").read(); src = src[:src.index("real = score(cell)")]
pw = []
for prefix in ("recf124r", "recf97r"):
    g = {"__file__": f"{HERE}/h335_106r_v7_beam.py", "__name__": "h346"}; sys.argv = [sys.argv[0]]
    exec(compile(src.replace("recf106rall/", f"{prefix}/"), f"h335_on_{prefix}", "exec"), g)
    allruns, cell, classes, score = g["runs"], g["cell"], g["classes"], g["score"]; bins = [classes[i:i + 3] for i in range(0, len(classes), 3)]
    rng = random.Random(351); wins = 0
    for _ in range(30):
        runs = rng.sample(allruns, 51); shuf = []
        for _ in range(10):
            s = []
            for r in runs: r2 = r[:]; rng.shuffle(r2); s.append(r2)
            shuf.append(s)
        def gain(cf):
            g["runs"] = runs; real = score(cf); sh = []
            for s in shuf: g["runs"] = s; sh.append(score(cf))
            return real - sum(sh) / len(sh)
        gv = gain(cell); null = []
        for _ in range(50):
            mp = {}
            for bn in bins:
                cs = [frozenset(cell(c)) for c in bn]; rng.shuffle(cs); mp.update(zip(bn, cs))
            null.append(gain(lambda c, mp=mp: set(mp.get(c, ()))))
        null.sort(); wins += gv > null[47]
    pw.append(wins / 30); out.append(f"{prefix}: 30 subsets of 51 runs; gain(v7) > binned p95 in {wins}/30 = {wins / 30:.2f}")
out.append("read-out: " + ("held leaves powered at 51 runs -- f.106r's miss stands as a negative relative to other held leaves" if min(pw) >= 0.8 else "held leaves underpowered at 51 runs -- f.106r's miss is untestable at this N, not a negative"))
txt = "\n".join(out) + "\n"; rs = f"{HERE}/h351_seqgain_heldpower_result.txt"
if "--check" in ARGS:
    ok = os.path.exists(rs) and open(rs).read() == txt; print("check", "OK" if ok else "STALE"); sys.exit(0 if ok else 1)
open(rs, "w").write(txt); print(txt, end="")
