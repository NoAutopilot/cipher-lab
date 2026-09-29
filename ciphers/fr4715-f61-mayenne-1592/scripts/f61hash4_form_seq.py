#!/usr/bin/env python3
"""H213 (runner 8 session_011Taenrv3JSdk7VjpiBjids, 29 Sept 2026), script-only, written before the run. f.108v relabelled by bowl (H201 map); its 14
HASH4 tokens split by H212's blind form groups (family/h212_items.tsv + passes/h212_sort.tsv, matched on line, segment, x): A (4-head) -> HASHA,
B (looped) -> HASHB. Candidates by sequence gain, 30 bootstrap resamples (seed 213), H198's rule (CONFIRMED >= 29/30, other PREFERRED <= 1/30, else
OPEN): SPLIT (A d/q, B i/x) against all d/q, all i/x and the REVERSE split (A i/x, B d/q). Descriptive.  -> scripts/f61hash4_form_seq_result.txt [--check]"""
import csv, os, random, sys
from collections import defaultdict
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE); sys.path.insert(0, f"{HERE}/../family")
ARGS = sys.argv[1:]; sys.argv = sys.argv[:1]
import f61beam_seqgain as G, f61bowl_108v_seq as BS, f61hash4_two_leaves as T
def main():
    F = f"{HERE}/../family"; key = {r["item"]: r for r in BS.rd(f"{F}/h212_items.tsv")}
    grp = {f"T{int(r['tile'].split()[-1]):02d}": r["group"].strip() for r in BS.rd(f"{F}/passes/h212_sort.tsv")}
    form = {(k["line"], k["segment"], k["x_px"]): grp[m] for m, k in key.items() if k["leaf"] == "108v"}
    A = defaultdict(list)
    for r in BS.rd(f"{F}/passes/f108v3z_signsA.tsv"): A[r["line"]].append(r)
    D = BS.draft(); ans = {(r["line"], r["column"]): r["bowl"] for r in BS.rd(f"{F}/h199_bowl_positions.tsv")}; colform = {}
    for l in sorted(A):
        k = 0
        for c in (r for r in BS.rd(f"{F}/passes/f108v3z_recon_task.tsv") if r["line"] == l):
            if c["alt"].startswith("A:-"): continue
            a = A[l][k]; k += 1; f = form.get((l, a["segment"], a["x_px"]))
            if f: colform[(l, c["position"])] = f
    L = BS.relabel(D, ans); L = {l: [("HASH" + colform[(l, p)]) if s == "HASH4" and (l, p) in colform else s for (p, _), s in zip(D[l], L[l])] for l in L}
    n = {x: sum(s.count(x) for s in L.values()) for x in ("HASHA", "HASHB", "HASH4")}
    M = dict(G.J.cells(), **{"4BOWL": "c/p", "4NOB": "a/n"})
    SP = dict(M, HASHA="d/q", HASHB="i/x"); cand = {"all d/q": dict(M, HASHA="d/q", HASHB="d/q"), "all i/x": dict(M, HASHA="i/x", HASHB="i/x"), "reverse": dict(M, HASHA="i/x", HASHB="d/q")}
    out = [f"f.108v HASH4 by form: {n}"]
    for k, m in cand.items(): out.append(T.verdict("split", k, T.duel(L, SP, m, 213)))
    txt = "\n".join(out) + "\n"; rp = f"{HERE}/f61hash4_form_seq_result.txt"
    if "--check" in ARGS:
        good = os.path.exists(rp) and open(rp).read() == txt; print("fresh" if good else "STALE"); sys.exit(0 if good else 1)
    open(rp, "w").write(txt); print(txt, end="")
if __name__ == "__main__": main()
