#!/usr/bin/env python3
"""F61-VBAR-REPL (campaign step H151, 28 Sept 2026, runner 5 session_01RbeePKZVn83gNfES8yFmhe), script-only. Replication of
H146's VBAR_A result before the family worker acts on family/PROPOSAL_H146.md: VBAR_A g/t vs t/s (VBAR_B f/s, pool map as
H146) by sequence gain, (a) pooled family drafts on 50 fresh bootstrap resamples (seed 151), (b) each leaf alone (f.97r,
f.101r, f.188r, f.124r; full leaf, no resampling). Pre-registered: the result stands if g/t wins >= 48 of 50 pooled
resamples AND has the higher gain on at least three of the four leaves.   -> scripts/f61vbar_repl_result.txt [--check]"""
import os, random, sys
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
ARGS = sys.argv[1:]; sys.argv = sys.argv[:1]
import f61seqgain_family as F
G = F.G
def main():
    base = dict(G.J.cells(), LOOPS="h/u", H24="i/x", ZBAR="f/s"); A, B = dict(base, VBAR_A="g/t"), dict(base, VBAR_A="t/s")
    leaves = {leaf: F.draft(leaf) for leaf in ("f97r", "f101r", "f188r", "f124r")}
    pool = {f"{lf}_{k}": v for lf, d in leaves.items() for k, v in d.items()}; keys = sorted(pool); rng = random.Random(151); w = 0
    for _ in range(50):
        R = {f"r{i}": pool[rng.choice(keys)] for i in range(len(keys))}; S = G.shuffles(R); w += G.gain(R, S, A) > G.gain(R, S, B)
    out = [f"pooled, 50 resamples: g/t wins {w}/50"]; lw = 0
    for lf, d in leaves.items():
        S = G.shuffles(d); ga, gb = G.gain(d, S, A), G.gain(d, S, B); lw += ga > gb
        out.append(f"{lf}: g/t {ga:.4f}, t/s {gb:.4f} -> {'g/t' if ga > gb else 't/s'}")
    out.append(f"H151: {'STANDS' if w >= 48 and lw >= 3 else 'DOES NOT STAND'} (pooled {w}/50, leaves {lw}/4)")
    txt = "\n".join(out) + "\n"; rp = f"{HERE}/f61vbar_repl_result.txt"
    if "--check" in ARGS:
        good = os.path.exists(rp) and open(rp).read() == txt; print("fresh" if good else "STALE"); sys.exit(0 if good else 1)
    open(rp, "w").write(txt); print(txt, end="")
if __name__ == "__main__": main()
