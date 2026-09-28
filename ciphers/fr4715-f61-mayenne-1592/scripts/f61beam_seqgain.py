#!/usr/bin/env python3
"""F61-BEAM-SEQGAIN (campaign step H127, 28 Sept 2026, runner 5 session_01RbeePKZVn83gNfES8yFmhe), script-only.
H124 showed the beam's plain rank measures letter frequency on long texts (f.108v ranks the fitted map first even shuffled).
Statistic here, which frequency alone cannot produce: gain(map) = beam score of the real sign order - mean beam score of 20
within-line shuffles (seeds 1270-1289, the same shuffles for every map) under that map. The fitted map's gain is ranked
among 200 permuted maps (seed 127). Pre-registered gates: CONTROL known f.61 span lines (14 cells) rank <= 10 of 201, else
every target is a non-test; each target PASSes at rank <= 10 of 201. Targets: f.108v (14 cells; + HASH4 = i/x), f.108r
L04-L06 (14 cells; + HASH4 = i/x).   -> scripts/f61beam_seqgain_result.txt [--check]"""
import os, random, sys
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
ARGS = sys.argv[1:]; sys.argv = sys.argv[:1]
import f61hash4_108r as H
J = H.J
def shuffles(L):
    out = []
    for seed in range(1270, 1290):
        rng = random.Random(seed); S = {}
        for l, seq in L.items(): s = list(seq); rng.shuffle(s); S[l] = s
        out.append(S)
    return out
def gain(L, SH, m): return H.score(L, m) - sum(H.score(S, m) for S in SH) / len(SH)
def rank(L, C):
    SH = shuffles(L); labs = sorted(C); rng = random.Random(127); g0 = gain(L, SH, C); null = []
    for _ in range(200):
        v = [C[l] for l in labs]; rng.shuffle(v); null.append(gain(L, SH, dict(zip(labs, v))))
    null.sort(reverse=True); return g0, 1 + sum(1 for x in null if x >= g0), null[0], null[100]
def main():
    C = J.cells(); CI = dict(C, HASH4="i/x"); out = []
    g, r, b, med = rank(J.lines("known_h51"), C); ok = r <= 10
    out.append(f"CONTROL known f.61 span lines, 14 cells: gain {g:.3f}, rank {r} of 201 (best permuted {b:.3f}, median {med:.3f}) -> {'PASS' if ok else 'FAIL'}")
    for name, tag, m in (("f.108v, 14 cells", "f108v", C), ("f.108v, HASH4=i/x", "f108v", CI),
                         ("f.108r L04-L06, 14 cells", "f108r_L04_L06_h108", C), ("f.108r L04-L06, HASH4=i/x", "f108r_L04_L06_h108", CI)):
        g, r, b, med = rank(J.lines(tag), m)
        out.append(f"TARGET {name}: gain {g:.3f}, rank {r} of 201 (best permuted {b:.3f}, median {med:.3f}) -> " + ("non-test" if not ok else ("PASS" if r <= 10 else "FAIL")))
    txt = "\n".join(out) + "\n"; rp = f"{HERE}/f61beam_seqgain_result.txt"
    if "--check" in ARGS:
        good = os.path.exists(rp) and open(rp).read() == txt; print("fresh" if good else "STALE"); sys.exit(0 if good else 1)
    open(rp, "w").write(txt); print(txt, end="")
if __name__ == "__main__": main()
