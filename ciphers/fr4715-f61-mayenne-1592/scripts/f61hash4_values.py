#!/usr/bin/env python3
"""F61-108R-HASH4-HU (campaign step H118, 28 Sept 2026, runner 5 session_01RbeePKZVn83gNfES8yFmhe), script-only. H114 showed
HASH4 = d/q moves f.108r L04-L06 from rank 2 to rank 12 of 201; the H108 L06 passes note several HASH4 as "crossed double
loop, alt INF". Same instrument and null as H114 (f61hash4_108r.rank: 4-gram beam, 200 permutations, seed 114; its known-lines
control PASSed at rank 1), with HASH4 = h/u (INF's cell) and HASH4 = i/x (H98's bare hash) in turn. Reported per value
beside H114's no-HASH4 (rank 2) and d/q (rank 12); no gate beyond H114's control (pre-registered in CAMPAIGN.md H118).
  -> scripts/f61hash4_values_result.txt [--check]"""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
ARGS = sys.argv[1:]; sys.argv = sys.argv[:1]
import f61hash4_108r as H
def main():
    C = H.J.cells(); tgt = H.J.lines("f108r_L04_L06_h108"); out = []
    for v in ("h/u", "i/x"):
        t, r, b, med, p5 = H.rank(tgt, dict(C, HASH4=v))
        out.append(f"f.108r L04-L06, 14 cells + HASH4={v}: fitted {t:.3f}, rank {r} of 201; best permuted {b:.3f}, median {med:.3f}")
    out.append("for comparison (H114): 14 cells rank 2 of 201; + HASH4=d/q rank 12 of 201")
    txt = "\n".join(out) + "\n"; rp = f"{HERE}/f61hash4_values_result.txt"
    if "--check" in ARGS:
        good = os.path.exists(rp) and open(rp).read() == txt; print("fresh" if good else "STALE"); sys.exit(0 if good else 1)
    open(rp, "w").write(txt); print(txt, end="")
if __name__ == "__main__": main()
