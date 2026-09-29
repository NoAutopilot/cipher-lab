#!/usr/bin/env python3
"""H356 and H357 (runner 13 session_01MSoJWwZxNPSjQd4hszNdvQ, 29 Sept 2026), script-only, written before running; descriptive, H347's design (H342's
order gain under three within-run shuffle seeds 342/343/344 for its spread), on the held leaves f.124r and f.97r.
H356 (EBR forms): v7 as loaded (EBR_A a/l/s, EBR_B l/y folded i/l); forms swapped (EBR_A <- EBR_B's cell, EBR_B <- EBR_A's); one pooled cell (the
union) on both forms. H357 (4TRI mixed code): v7 (4TRI c/p/t) vs 4TRI widened to c/p/t + C43's a/n (the no-bowl sign's cell, H218/H231).
A variant 'raises' the gain iff higher than v7's under all three seeds, 'lowers' iff lower under all three, else 'unclear'. No cell is changed.
python3 h356_357_cells_order.py [--check]"""
import os, random, sys
HERE = os.path.dirname(os.path.abspath(__file__)); ARGS = sys.argv[1:]; out = []
src = open(f"{HERE}/h335_106r_v7_beam.py").read(); src = src[:src.index("real = score(cell)")]
for prefix in ("recf124r", "recf97r"):
    g = {"__file__": f"{HERE}/h335_106r_v7_beam.py", "__name__": "h356"}; sys.argv = [sys.argv[0]]
    exec(compile(src.replace("recf106rall/", f"{prefix}/"), f"h335_on_{prefix}", "exec"), g)
    runs, cell, score = g["runs"], g["cell"], g["score"]
    shufsets = []
    for seed in (342, 343, 344):
        rng = random.Random(seed); ss = []
        for _ in range(10):
            s = []
            for r in runs: r2 = r[:]; rng.shuffle(r2); s.append(r2)
            ss.append(s)
        shufsets.append(ss)
    def gains(cf):
        res = []
        for ss in shufsets:
            g["runs"] = runs; real = score(cf); sh = []
            for s in ss: g["runs"] = s; sh.append(score(cf))
            res.append(real - sum(sh) / len(sh))
        g["runs"] = runs; return res
    A, B, C43 = set(cell("EBR_A")), set(cell("EBR_B")), set(cell("C43")); T = set(cell("4TRI"))
    variants = {"v7": cell,
                "H356 EBR forms swapped": lambda c: B if c == "EBR_A" else A if c == "EBR_B" else cell(c),
                "H356 EBR pooled (union)": lambda c: A | B if c in ("EBR_A", "EBR_B") else cell(c),
                "H357 4TRI + a/n": lambda c: T | C43 if c == "4TRI" else cell(c)}
    base = gains(cell); f = lambda v: "/".join(f"{x:.4f}" for x in v)
    out.append(f"{prefix}: v7 {f(base)}")
    for name, cf in list(variants.items())[1:]:
        gv = gains(cf); d = [a - b for a, b in zip(gv, base)]
        lab = "raises" if all(x > 0 for x in d) else "lowers" if all(x < 0 for x in d) else "unclear"
        out.append(f"  {name}: {f(gv)} -> {lab} the gain")
txt = "\n".join(out) + "\n"; rs = f"{HERE}/h356_357_cells_order_result.txt"
if "--check" in ARGS:
    ok = os.path.exists(rs) and open(rs).read() == txt; print("check", "OK" if ok else "STALE"); sys.exit(0 if ok else 1)
open(rs, "w").write(txt); print(txt, end="")
