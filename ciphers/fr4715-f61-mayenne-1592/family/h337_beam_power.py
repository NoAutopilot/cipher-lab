#!/usr/bin/env python3
"""H337 (runner 13 session_01MSoJWwZxNPSjQd4hszNdvQ, 29 Sept 2026), script-only, written before running: power of H335's binned arm at f.106r's N.
H335's code (runs, cell, beam score, bins by the leaf's own token rank) is exec'd per in-sample leaf (f.101r, f.188r); 50 random subsets of 35 runs
(f.106r's run count; seed 337) are drawn from the leaf's runs, and each subset's v7 score is compared with 100 binned-permuted keys (the same bin rule)
on that subset. Power = share of subsets where real > the subset's binned p95. Pre-stated: power >= 0.8 on both leaves -> H335's f.106r binned result
(12/200, at p95) is a weak lead; else the binned arm is underpowered at this N and H335 stays a non-test.   python3 h337_beam_power.py [--check]"""
import os, random, sys
HERE = os.path.dirname(os.path.abspath(__file__)); ARGS = sys.argv[1:]; out = []
src = open(f"{HERE}/h335_106r_v7_beam.py").read(); src = src[:src.index("real = score(cell)")]
for pre in ("f101r", "f188r"):
    g = {"__file__": f"{HERE}/h335_106r_v7_beam.py", "__name__": "h337"}; sys.argv = [sys.argv[0]]
    exec(compile(src.replace("recf106rall/", f"rec{pre}/"), f"h335_on_{pre}", "exec"), g)
    allruns, cell, classes = g["runs"], g["cell"], g["classes"]; bins = [classes[i:i + 3] for i in range(0, len(classes), 3)]
    rng = random.Random(337); wins = 0; sizes = []
    for k in range(50):
        g["runs"] = rng.sample(allruns, 35); sizes.append(sum(len(r) for r in g["runs"])); real = g["score"](cell); null = []
        for _ in range(100):
            mp = {}
            for bn in bins:
                cs = [frozenset(cell(c)) for c in bn]; rng.shuffle(cs); mp.update(zip(bn, cs))
            null.append(g["score"](lambda c, mp=mp: set(mp.get(c, ()))))
        null.sort(); wins += real > null[94]
    out.append(f"{pre}: {len(allruns)} runs; subsets of 35 runs ({min(sizes)}-{max(sizes)} signs, mean {sum(sizes) / 50:.0f}); real > binned p95 in {wins}/50 = {wins / 50:.2f}")
pw = [int(l.split(" in ")[1].split("/")[0]) / 50 for l in out]
out.append("read-out: " + ("binned arm powered at f.106r's N (>= 0.8 on both) -- H335's 12/200 is a weak lead" if min(pw) >= 0.8 else "binned arm underpowered at f.106r's N -- H335 stays a non-test"))
txt = "\n".join(out) + "\n"; res = f"{HERE}/h337_beam_power_result.txt"
if "--check" in ARGS:
    ok = os.path.exists(res) and open(res).read() == txt; print("check", "OK" if ok else "STALE"); sys.exit(0 if ok else 1)
open(res, "w").write(txt); print(txt, end="")
