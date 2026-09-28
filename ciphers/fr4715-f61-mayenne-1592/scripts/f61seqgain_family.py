#!/usr/bin/env python3
"""F61-SEQGAIN-FAMILY (campaign step H129, 28 Sept 2026, runner 5 session_01RbeePKZVn83gNfES8yFmhe), script-only. The H127
sequence-gain rank (validated null on shuffled text, H128) of f.61's 14-cell map on the family leaves' reconciled drafts
(family/passes/rec<leaf>/ciphertext_draft.tsv; lines as the draft gives them; classes outside the map dropped, coverage
reported). 200 permuted maps (seed 127), 20 within-line shuffles, as H127. Pre-registered: the known-lines control ranks
<= 10 of 201 (else non-test); a leaf is "in f.61's cells" at rank <= 10 of 201.  -> scripts/f61seqgain_family_result.txt [--check]"""
import csv, os, sys
HERE = os.path.dirname(os.path.abspath(__file__)); FAM = os.path.abspath(f"{HERE}/../family/passes"); sys.path.insert(0, HERE)
ARGS = sys.argv[1:]; sys.argv = sys.argv[:1]
import f61beam_seqgain as G
LEAVES = ["f97r", "f101r", "f188r", "f124r", "f106r", "f274"]
def draft(leaf):
    L = {}
    for r in csv.DictReader((l for l in open(f"{FAM}/rec{leaf}/ciphertext_draft.tsv") if not l.startswith("#")), delimiter="\t"):
        L.setdefault(r["line"], []).append(r["sign"])
    return L
def main():
    C = G.J.cells(); out = []
    g, r, b, med = G.rank(G.J.lines("known_h51"), C); ok = r <= 10
    out.append(f"CONTROL known f.61 span lines: gain {g:.3f}, rank {r} of 201 -> {'PASS' if ok else 'FAIL'}")
    for leaf in LEAVES:
        L = draft(leaf); n = sum(len(s) for s in L.values()); cov = sum(1 for s in L.values() for c in s if c in C)
        g, r, b, med = G.rank(L, C)
        out.append(f"{leaf}: {n} signs, {cov} covered ({cov / n:.2f}); gain {g:.3f}, rank {r} of 201 (best permuted {b:.3f}, median {med:.3f}) -> "
                   + ("non-test" if not ok else ("in f.61's cells" if r <= 10 else "not shown")))
        print(out[-1], flush=True)
    txt = "\n".join(out) + "\n"; rp = f"{HERE}/f61seqgain_family_result.txt"
    if "--check" in ARGS:
        good = os.path.exists(rp) and open(rp).read() == txt; print("fresh" if good else "STALE"); sys.exit(0 if good else 1)
    open(rp, "w").write(txt); print(out[0])
if __name__ == "__main__": main()
