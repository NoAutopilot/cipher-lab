#!/usr/bin/env python3
"""F61-SEQGAIN-SHUFFLE (campaign step H128, 28 Sept 2026, runner 5 session_01RbeePKZVn83gNfES8yFmhe), script-only: CLAUDE.md
rule 3 (ARM-C1) for H127. Each H127 target (and the control text) has its signs shuffled within lines (seeds 1281-1285); each
shuffled text is then run through f61beam_seqgain.rank exactly as a real target. Pre-registered: H127 stands for a text only
if its shuffled versions rank > 10 of 201 in at least 4 of 5.   -> scripts/f61seqgain_shuffle_result.txt [--check]"""
import os, random, sys
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
ARGS = sys.argv[1:]; sys.argv = sys.argv[:1]
import f61beam_seqgain as G
def main():
    C = G.J.cells(); CI = dict(C, HASH4="i/x"); out = []
    for name, tag, m in (("known f.61 span lines, 14 cells", "known_h51", C), ("f.108v, 14 cells", "f108v", C), ("f.108v, HASH4=i/x", "f108v", CI),
                         ("f.108r L04-L06, 14 cells", "f108r_L04_L06_h108", C), ("f.108r L04-L06, HASH4=i/x", "f108r_L04_L06_h108", CI)):
        L = G.J.lines(tag); ranks = []
        for seed in range(1281, 1286):
            rng = random.Random(seed); S = {l: rng.sample(s, len(s)) for l, s in L.items()}; ranks.append(G.rank(S, m)[1])
        ok = sum(r > 10 for r in ranks) >= 4
        out.append(f"{name}: shuffled-target ranks {ranks} -> H127 {'STANDS' if ok else 'VOID'}")
    txt = "\n".join(out) + "\n"; rp = f"{HERE}/f61seqgain_shuffle_result.txt"
    if "--check" in ARGS:
        good = os.path.exists(rp) and open(rp).read() == txt; print("fresh" if good else "STALE"); sys.exit(0 if good else 1)
    open(rp, "w").write(txt); print(txt, end="")
if __name__ == "__main__": main()
