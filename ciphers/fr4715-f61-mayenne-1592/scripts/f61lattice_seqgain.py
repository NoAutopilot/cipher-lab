#!/usr/bin/env python3
"""F61-LATTICE-SEQGAIN-108R (campaign step H164, 28 Sept 2026, runner 5 session_01RbeePKZVn83gNfES8yFmhe), script-only, one run.
The H127 sequence gain with the H136 word-lattice resolution scored by the fr16 4-gram (per-letter mean of the lattice string)
in place of the plain beam's own path score: gain = score(real order) - mean score(10 within-line shuffles, seeds 1640-1649),
fitted 14-cell map vs 100 permuted maps (seed 164). Texts: the known f.61 lines (control) and f.108r L04-L06 (H108 draft,
HASH4 in the map as d/q per H162). Pre-registered: rank <= 5 of 101 on both (the top 5%), control first.
  -> scripts/f61lattice_seqgain_result.txt [--check]"""
import os, random, sys
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
ARGS = sys.argv[1:]; sys.argv = sys.argv[:1]
import f61beam_lattice as BL
H = BL.M14.BM.H; J, jp = H.J, H.jp
def sc(L, m):
    tot = n = 0
    for seq in L.values():
        prs = [tuple(jp.fold(x) for x in m[c].split("/")) for c in seq if c in m]
        if len(prs) < 4: continue
        s = BL.best_lattice(prs); tot += H.M.score(s) * (len(s) - 3); n += len(s) - 3
    return tot / n if n else -9.9
def shuf(L, k): rng = random.Random(1640 + k); return {l: rng.sample(s, len(s)) for l, s in L.items()}
def rank(L, C):
    SH = [shuf(L, k) for k in range(10)]
    g = lambda m: sc(L, m) - sum(sc(S, m) for S in SH) / len(SH)
    labs = sorted(C); rng = random.Random(164); g0 = g(C); null = []
    for _ in range(100):
        v = [C[l] for l in labs]; rng.shuffle(v); null.append(g(dict(zip(labs, v))))
    return g0, 1 + sum(1 for x in null if x >= g0), max(null)
def main():
    C = J.cells(); out = []
    for name, tag, m in (("CONTROL known f.61 lines", "known_h51", C), ("f.108r L04-L06, HASH4=d/q", "f108r_L04_L06_h108", dict(C, HASH4="d/q"))):
        g, r, b = rank(J.lines(tag), m); out.append(f"{name}: lattice gain {g:.3f}, rank {r} of 101 (best permuted {b:.3f}) -> {'PASS' if r <= 5 else 'FAIL'}"); print(out[-1], flush=True)
    txt = "\n".join(out) + "\n"; rp = f"{HERE}/f61lattice_seqgain_result.txt"
    if "--check" in ARGS:
        good = os.path.exists(rp) and open(rp).read() == txt; print("fresh" if good else "STALE"); sys.exit(0 if good else 1)
    open(rp, "w").write(txt)
if __name__ == "__main__": main()
