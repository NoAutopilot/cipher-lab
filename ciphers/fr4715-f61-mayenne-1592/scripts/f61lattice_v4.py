#!/usr/bin/env python3
"""F61-LATTICE-V4 (campaign step H141, 28 Sept 2026, runner 5 session_01RbeePKZVn83gNfES8yFmhe), script-only, one run. H117:
the plain beam was near chance (23/42) on key v4's two-way form (verify_v4/f61r_v4_twoway.txt) with lines cut at unread
<CLASS> signs. Here the H136 word-lattice beam (fixed weights) resolves each line with the unread signs DROPPED (the line
closes up around them) over v4's sets (firm letters as one-letter sets), and its letter is scored at the 42 set positions
that carry a Tomokiyo letter inside the set (the T: rows), beside the plain beam under the same dropping.
GATE H141 (pre-registered): lattice >= 34/42 (0.80).   -> scripts/f61lattice_v4_result.txt [--check]"""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
ARGS = sys.argv[1:]; sys.argv = sys.argv[:1]
import f61beam_margin as BM
import f61beam_lattice as BL
def main():
    lines, known = BM.parse(); r = rp = n = 0
    for L, toks in lines.items():
        idx = [k for k, s in enumerate(toks) if s is not None]; sets = [toks[k] for k in idx]
        if not sets: continue
        a = BL.best_lattice(sets); b = BM.best(sets)[0]
        for i, k in enumerate(idx):
            if len(sets[i]) < 2 or (L, k) not in known: continue
            t = known[(L, k)][1]
            if t in sets[i]: n += 1; r += a[i] == t; rp += b[i] == t
    txt = (f"key v4 two-way form, unread signs dropped: lattice {r}/{n}, plain beam {rp}/{n} (H117 plain beam with cuts 23/42)\n"
           f"GATE H141 (lattice >= 34/42): {'PASS' if n >= 42 and r >= 34 else 'FAIL'}\n")
    rpth = f"{HERE}/f61lattice_v4_result.txt"
    if "--check" in ARGS:
        good = os.path.exists(rpth) and open(rpth).read() == txt; print("fresh" if good else "STALE"); sys.exit(0 if good else 1)
    open(rpth, "w").write(txt); print(txt, end="")
if __name__ == "__main__": main()
