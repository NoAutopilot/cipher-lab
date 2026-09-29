#!/usr/bin/env python3
"""H347 (runner 13 session_01MSoJWwZxNPSjQd4hszNdvQ, 29 Sept 2026), script-only, written before running: does key v7's change set raise H342's order
gain on the held leaves f.124r and f.97r over key v6? Cells: v7 as H335's cell(); v6 the same rule on build_key_v6.load_key_v6 (EBR_A -> form A, EBR_B
-> form B). Gains (real order minus the mean of 10 within-run shuffles) are computed under three shuffle seeds (342, 343, 344) for the spread. Reported:
gain(v6), gain(v7), and for each class whose cell differs between v6 and v7 (and occurs in the leaf's runs), gain(v7 with that class alone reverted to
v6). Descriptive only: a change 'helps' on a leaf iff reverting it lowers the gain under all three seeds, 'hurts' iff it raises it under all three,
else 'unclear'. No cell is changed.   python3 h347_seqgain_v6v7.py [--check]"""
import os, random, sys
from collections import Counter
HERE = os.path.dirname(os.path.abspath(__file__)); ARGS = sys.argv[1:]; out = []
src = open(f"{HERE}/h335_106r_v7_beam.py").read(); src = src[:src.index("real = score(cell)")]
sys.path.insert(0, HERE); _a = sys.argv; sys.argv = sys.argv[:1]
import build_key_v6 as b6
sys.argv = _a
K6B, K6A = b6.load_key_v6(ebr="B"), b6.load_key_v6(ebr="A")
def cell6(c): return set(K6A.get("EBR", ())) if c == "EBR_A" else set(K6B.get("EBR", ())) if c == "EBR_B" else set(K6B.get(c, ()))
for prefix in ("recf124r", "recf97r"):
    g = {"__file__": f"{HERE}/h335_106r_v7_beam.py", "__name__": "h347"}; sys.argv = [sys.argv[0]]
    exec(compile(src.replace("recf106rall/", f"{prefix}/"), f"h335_on_{prefix}", "exec"), g)
    runs, cell, score = g["runs"], g["cell"], g["score"]
    present = sorted({c for r in runs for c in r}); n_in = Counter(c for r in runs for c in r)
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
    g7 = gains(cell)
    # a v6 cell may be empty where v7 keys the class: score() skips runs with an empty set, so both keys are scored on the runs v6 can read
    g6 = gains(lambda c: cell6(c) if cell6(c) else cell(c))
    f = lambda v: "/".join(f"{x:.4f}" for x in v)
    out.append(f"{prefix}: gain v7 {f(g7)}; gain v6 (v7 where v6 has no cell) {f(g6)}")
    for c in present:
        if cell6(c) == cell(c) or not cell6(c): continue
        gr = gains(lambda x, c=c: cell6(x) if x == c else cell(x))
        d = [a - b for a, b in zip(g7, gr)]; lab = "helps" if all(x > 0 for x in d) else "hurts" if all(x < 0 for x in d) else "unclear"
        out.append(f"  {c:10s} v6 {'/'.join(sorted(cell6(c)))} -> v7 {'/'.join(sorted(cell(c)))} (signs {n_in[c]}): gain with v6 cell {f(gr)} -> v7 change {lab}")
txt = "\n".join(out) + "\n"; rs = f"{HERE}/h347_seqgain_v6v7_result.txt"
if "--check" in ARGS:
    ok = os.path.exists(rs) and open(rs).read() == txt; print("check", "OK" if ok else "STALE"); sys.exit(0 if ok else 1)
open(rs, "w").write(txt); print(txt, end="")
