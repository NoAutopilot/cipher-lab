#!/usr/bin/env python3
"""F61-SWAP-NOISE (campaign step H142, 28 Sept 2026, runner 5 session_01RbeePKZVn83gNfES8yFmhe), script-only: a noise scale
for H132. The 15 closest one-swaps of H132 (read from scripts/f61swap_family_result.txt) re-scored on 30 bootstrap resamples
of the family pool's lines (seed 142; each resample with its own 20 shuffles as H127), fitted map vs swap. Pre-registered: a
swap is CONFIRMED REJECTED when the fitted map has the higher gain in >= 29 of 30 resamples, PREFERRED when in <= 1, else OPEN.
  -> scripts/f61swap_noise_result.txt [--check]"""
import os, random, re, sys
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
ARGS = sys.argv[1:]; sys.argv = sys.argv[:1]
import f61seqgain_family as F
G = F.G
def main():
    C = dict(G.J.cells(), LOOPS="h/u", H24="i/x", ZBAR="f/s")
    sw = [re.findall(r"(\w+)\([a-z/]+\)", l) for l in open(f"{HERE}/f61swap_family_result.txt") if l.startswith("  ")][:15]
    pool = {}
    for leaf in ("f97r", "f101r", "f188r", "f124r"):
        for k, v in F.draft(leaf).items(): pool[f"{leaf}_{k}"] = v
    keys = sorted(pool); rng = random.Random(142); wins = [0] * len(sw)
    for _ in range(30):
        R = {f"r{i}": pool[rng.choice(keys)] for i in range(len(keys))}; S = G.shuffles(R); g0 = G.gain(R, S, C)
        for j, (a, b) in enumerate(sw):
            m = dict(C); m[a], m[b] = C[b], C[a]; wins[j] += g0 > G.gain(R, S, m)
    out = [f"{a}({C[a]})<->{b}({C[b]}): fitted wins {w}/30 -> " + ("CONFIRMED REJECTED" if w >= 29 else ("PREFERRED" if w <= 1 else "OPEN")) for (a, b), w in zip(sw, wins)]
    txt = "\n".join(out) + "\n"; rp = f"{HERE}/f61swap_noise_result.txt"
    if "--check" in ARGS:
        good = os.path.exists(rp) and open(rp).read() == txt; print("fresh" if good else "STALE"); sys.exit(0 if good else 1)
    open(rp, "w").write(txt); print(txt, end="")
if __name__ == "__main__": main()
