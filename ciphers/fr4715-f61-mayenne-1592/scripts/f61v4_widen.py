#!/usr/bin/env python3
"""F61-V4-WIDENINGS (campaign step H148, 28 Sept 2026, runner 5 session_01RbeePKZVn83gNfES8yFmhe), script-only. H145's key-v4
widenings, each added ALONE to the pool map (14 cells + KEY.md equivalences LOOPS h/u, H24 i/x, ZBAR f/s): SBS b/o/e,
4TRI c/p/t, 4PI d/q/a/n, 4STEM a/n/c/e, HASH4 d/q/i. Sequence gain (H127) on the pooled family drafts, widened vs base, on
30 bootstrap resamples (seed 148, own shuffles each). Pre-registered: SUPPORTED at >= 29/30 widened wins, REJECTED at <= 1/30,
else OPEN. (A wider set also gives the shuffled text more freedom, so the gain is a fair comparison.)
  -> scripts/f61v4_widen_result.txt [--check]"""
import os, random, sys
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
ARGS = sys.argv[1:]; sys.argv = sys.argv[:1]
import f61seqgain_family as F
G = F.G
WIDE = {"SBS": "b/o/e", "4TRI": "c/p/t", "4PI": "d/q/a/n", "4STEM": "a/n/c/e", "HASH4": "d/q/i"}
def main():
    base = dict(G.J.cells(), LOOPS="h/u", H24="i/x", ZBAR="f/s", HASH4="d/q")   # HASH4's family value (KEY.md) as the base
    pool = {}
    for leaf in ("f97r", "f101r", "f188r", "f124r"):
        for k, v in F.draft(leaf).items(): pool[f"{leaf}_{k}"] = v
    keys = sorted(pool); rng = random.Random(148); wins = {c: 0 for c in WIDE}
    for _ in range(30):
        R = {f"r{i}": pool[rng.choice(keys)] for i in range(len(keys))}; S = G.shuffles(R); g0 = G.gain(R, S, base)
        for c, v in WIDE.items(): wins[c] += G.gain(R, S, dict(base, **{c: v})) > g0
    out = [f"{c}: {base.get(c)} -> {v}: widened wins {wins[c]}/30 -> " + ("SUPPORTED" if wins[c] >= 29 else ("REJECTED" if wins[c] <= 1 else "OPEN")) for c, v in WIDE.items()]
    txt = "\n".join(out) + "\n"; rp = f"{HERE}/f61v4_widen_result.txt"
    if "--check" in ARGS:
        good = os.path.exists(rp) and open(rp).read() == txt; print("fresh" if good else "STALE"); sys.exit(0 if good else 1)
    open(rp, "w").write(txt); print(txt, end="")
if __name__ == "__main__": main()
