#!/usr/bin/env python3
"""H350 (runner 13 session_01MSoJWwZxNPSjQd4hszNdvQ, 29 Sept 2026), script-only, written before running: power of H342's order statistic at f.106r's
N (51 runs, rows 1-18). From each in-sample leaf (f.101r, f.188r): 30 random 51-run subsets (seed 350); per subset, H342's gain for v7 (10 within-run shuffles)
against 50 binned-permuted keys' gains (H335's bin rule) on the same subset; power = share of subsets with gain(v7) > the binned gains' p95.
Pre-stated: power >= 0.8 on both leaves -> f.106r's H348 result (rows 1-18, 31/100, no order signal) is a negative for v7 in the secretary's hand at this N;
else it is untestable at this N (not a negative).   python3 h346_seqgain_power.py [--check]"""
import os, random, sys
HERE = os.path.dirname(os.path.abspath(__file__)); ARGS = sys.argv[1:]; out = []
src = open(f"{HERE}/h335_106r_v7_beam.py").read(); src = src[:src.index("real = score(cell)")]
pw = []
for prefix in ("recf101r", "recf188r"):
    g = {"__file__": f"{HERE}/h335_106r_v7_beam.py", "__name__": "h346"}; sys.argv = [sys.argv[0]]
    exec(compile(src.replace("recf106rall/", f"{prefix}/"), f"h335_on_{prefix}", "exec"), g)
    allruns, cell, classes, score = g["runs"], g["cell"], g["classes"], g["score"]; bins = [classes[i:i + 3] for i in range(0, len(classes), 3)]
    rng = random.Random(350); wins = 0
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
out.append("read-out: " + ("powered at f.106r's N -- f.106r's no-signal result is a negative for v7 in the secretary's hand at this N" if min(pw) >= 0.8 else "underpowered at f.106r's N -- f.106r's no-signal result is untestable at this N, not a negative"))
txt = "\n".join(out) + "\n"; rs = f"{HERE}/h350_seqgain_power51_result.txt"
if "--check" in ARGS:
    ok = os.path.exists(rs) and open(rs).read() == txt; print("check", "OK" if ok else "STALE"); sys.exit(0 if ok else 1)
open(rs, "w").write(txt); print(txt, end="")
