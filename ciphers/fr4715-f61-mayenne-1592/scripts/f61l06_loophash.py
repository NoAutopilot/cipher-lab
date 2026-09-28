#!/usr/bin/env python3
"""F61-108R-L06-LOOPHASH (campaign step H167, 28 Sept 2026, runner 5 session_01RbeePKZVn83gNfES8yFmhe), script-only,
descriptive. f.108r L06 alone (H108 draft; its HASH4 signs are mostly the looped 4-over-hash of H162): sequence-gain rank
(H127 statistic) of the 14-cell map among 200 permuted maps with HASH4 = d/q, i/x, h/u, and dropped. No gate (one line).
  -> scripts/f61l06_loophash_result.txt [--check]"""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
ARGS = sys.argv[1:]; sys.argv = sys.argv[:1]
import f61beam_seqgain as G
def main():
    C = G.J.cells(); L = {"L06": G.J.lines("f108r_L04_L06_h108")["L06"]}; n = L["L06"].count("HASH4"); out = [f"f.108r L06: {len(L['L06'])} signs, HASH4 {n}"]
    for v in ("d/q", "i/x", "h/u", None):
        m = dict(C, HASH4=v) if v else C; g, r, b, med = G.rank(L, m)
        out.append(f"HASH4 = {v or 'dropped'}: gain {g:.3f}, rank {r} of 201 (best permuted {b:.3f})")
    txt = "\n".join(out) + "\n"; rp = f"{HERE}/f61l06_loophash_result.txt"
    if "--check" in ARGS:
        good = os.path.exists(rp) and open(rp).read() == txt; print("fresh" if good else "STALE"); sys.exit(0 if good else 1)
    open(rp, "w").write(txt); print(txt, end="")
if __name__ == "__main__": main()
