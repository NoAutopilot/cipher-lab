#!/usr/bin/env python3
"""H345 (runner 13 session_01MSoJWwZxNPSjQd4hszNdvQ, 29 Sept 2026), script-only, written before running: which v7 cells carry H342's order signal on
the held leaves f.124r and f.97r. Design change from the CAMPAIGN row, logged before running: bins of 3 give only 2 alternative cells per class, so
instead each keyed class's cell is replaced in turn by EVERY other keyed class's v7 cell (all other cells fixed), and H342's gain (real order minus
the mean of the same 10 within-run shuffles, seed 342) is computed for each. Per class, v7's own cell is ranked among the alternatives (rank 1 = best).
Pre-stated per class: 'supported' iff rank 1; 'consistent' iff rank 2-3; else 'not supported'. Descriptive (the AX-NAMES per-class breakdown); a
class with under 30 signs in runs is marked 'small'. No cell is changed.   python3 h345_seqgain_perclass.py [--check]"""
import os, random, sys
from collections import Counter
HERE = os.path.dirname(os.path.abspath(__file__)); ARGS = sys.argv[1:]; out = []
src = open(f"{HERE}/h335_106r_v7_beam.py").read(); src = src[:src.index("real = score(cell)")]
for prefix in ("recf124r", "recf97r"):
    g = {"__file__": f"{HERE}/h335_106r_v7_beam.py", "__name__": "h345"}; sys.argv = [sys.argv[0]]
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
    n_in = Counter(c for r in runs for c in r); gv = gain(cell)
    out.append(f"{prefix}: gain(v7) {gv:.4f}; {len(classes)} keyed classes")
    for c in classes:
        alts = []
        for d in classes:
            if d == c or set(cell(d)) == set(cell(c)): continue
            alts.append((gain(lambda x, c=c, d=d: set(cell(d)) if x == c else cell(x)), d))
        rank = 1 + sum(a > gv for a, _ in alts); best = max(alts)
        lab = "supported" if rank == 1 else "consistent" if rank <= 3 else "not supported"
        out.append(f"  {c:10s} cell {'/'.join(sorted(cell(c))):8s} signs {n_in[c]:4d}{' small' if n_in[c] < 30 else ''}: rank {rank}/{len(alts) + 1}, best alt {best[1]} ({'/'.join(sorted(cell(best[1])))}) {best[0]:.4f} -> {lab}")
txt = "\n".join(out) + "\n"; rs = f"{HERE}/h345_seqgain_perclass_result.txt"
if "--check" in ARGS:
    ok = os.path.exists(rs) and open(rs).read() == txt; print("check", "OK" if ok else "STALE"); sys.exit(0 if ok else 1)
open(rs, "w").write(txt); print(txt, end="")
