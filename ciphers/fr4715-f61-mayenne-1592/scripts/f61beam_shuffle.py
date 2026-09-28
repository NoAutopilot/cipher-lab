#!/usr/bin/env python3
"""F61-BEAM-SHUFFLE-CONTROL (campaign step H124, 28 Sept 2026, runner 5 session_01RbeePKZVn83gNfES8yFmhe), script-only.
CLAUDE.md rule 3 (ARM-C1): a gate the SHUFFLED target also passes is void for that family. The beam rank-1 results (H119
f.108r L04-L06 with HASH4 = i/x; H122 f.108v, both maps) could come from letter frequencies alone. Here each target's signs
are shuffled within each line (seeds 124-128) and ranked by the same instrument against the same 1000-permutation null
(f61ngram108r_repl.null, seeds 115/116). Pre-registered: a result stands only if its shuffled target's mean rank over the
five shuffles is > 50 of 1001 (outside the top 5%); else the beam rank is void as a gate for that target.
  -> scripts/f61beam_shuffle_result.txt [--check]"""
import os, random, sys
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
ARGS = sys.argv[1:]; sys.argv = sys.argv[:1]
import f61ngram108r_repl as R
H, J = R.H, R.J
def main():
    base = J.cells(); out = []
    for name, tag, C in (("H119 f.108r L04-L06, HASH4=i/x", "f108r_L04_L06_h108", dict(base, HASH4="i/x")),
                         ("H122 f.108v, 14 cells", "f108v", base), ("H122 f.108v, HASH4=i/x", "f108v", dict(base, HASH4="i/x"))):
        maps = R.null(None, C); L = J.lines(tag); t0, r0, _ = R.rk(L, C, maps); ranks = []
        for seed in range(124, 129):
            rng = random.Random(seed); S = {}
            for l, seq in L.items(): s = list(seq); rng.shuffle(s); S[l] = s
            ranks.append(R.rk(S, C, maps)[1])
        m = sum(ranks) / len(ranks)
        out.append(f"{name}: real order rank {r0} of 1001; shuffled-order ranks {ranks} (mean {m:.1f}) -> {'STANDS' if m > 50 else 'VOID as a gate'}")
    txt = "\n".join(out) + "\n"; rp = f"{HERE}/f61beam_shuffle_result.txt"
    if "--check" in ARGS:
        good = os.path.exists(rp) and open(rp).read() == txt; print("fresh" if good else "STALE"); sys.exit(0 if good else 1)
    open(rp, "w").write(txt); print(txt, end="")
if __name__ == "__main__": main()
