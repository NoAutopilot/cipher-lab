#!/usr/bin/env python3
"""F61-108R-NGRAM-REPL (campaign step H115, 28 Sept 2026, runner 5 session_01RbeePKZVn83gNfES8yFmhe), script-only: H114's
f.108r L04-L06 figure (the 14-cell map at rank 2 of 201 by the 4-gram beam) replicated on fresh nulls. Same instrument
(scripts/f61hash4_108r.py resolve/score). Pre-registered (pushed before the first run):
  pooled null = 500 permutations at seed 115 + 500 at seed 116 (1000); statistic the fitted map's rank among 1001.
  GATE "signal on f.108r": rank <= 10 of 1001 (top 1%). Control: the known f.61 span lines on the same 1000-permutation
  null must also be <= 10 of 1001, or the target figure is a non-test. Reported, not gated: each of L04, L05, L06 alone
  (rank among 1001), so a verifier sees which rows carry it.
Amended before the run: the row's HASH4 split (bare hash vs 4-over-hash) is not run -- the H108 passes code every hash
HASH4 and their notes do not separate the two forms (L06's notes call several "crossed double loop, alt INF"), so the
split would be a guess; logged in NOTES.md.  -> scripts/f61ngram108r_repl_result.txt [--check]
"""
import os, random, sys
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
ARGS = sys.argv[1:]; sys.argv = sys.argv[:1]
import f61hash4_108r as H
J = H.J
def null(lines, C):
    labs = sorted(C); out = []
    for seed in (115, 116):
        rng = random.Random(seed)
        for _ in range(500):
            v = [C[l] for l in labs]; rng.shuffle(v); out.append(dict(zip(labs, v)))
    return out
def rk(lines, C, maps):
    t = H.score(lines, C); ns = [H.score(lines, m) for m in maps]
    return t, 1 + sum(1 for x in ns if x >= t), sorted(ns, reverse=True)
IX = "--hash4-ix" in ARGS; V108 = "--f108v" in ARGS   # H119 (28 Sept 2026): HASH4 = i/x added to the map before the permutations; gate and null unchanged
def main():
    C = J.cells()
    if IX: C = dict(C, HASH4="i/x")
    maps = null(None, C); out = []
    known = J.lines("known_h51"); tgt = J.lines("f108v" if V108 else "f108r_L04_L06_h108")   # H122: --f108v, the H59 reconciled f.108v draft
    t, r, ns = rk(known, C, maps); ok = r <= 10
    out.append(f"CONTROL known f.61 span lines: fitted {t:.3f}, rank {r} of 1001 (best permuted {ns[0]:.3f}, 10th {ns[9]:.3f}) -> {'PASS' if ok else 'FAIL'}")
    t, r, ns = rk(tgt, C, maps); g = r <= 10
    out.append(f"TARGET {'f.108v L01-L07' if V108 else 'f.108r L04-L06'} pooled: fitted {t:.3f}, rank {r} of 1001 (best permuted {ns[0]:.3f}, 10th {ns[9]:.3f}, median {ns[500]:.3f})")
    for L in sorted(tgt):
        t1, r1, n1 = rk({L: tgt[L]}, C, maps); out.append(f"  {L} alone: fitted {t1:.3f}, rank {r1} of 1001 (median permuted {n1[500]:.3f})")
    out.append("GATE H115 (rank <= 10 of 1001, control also): " + ("non-test (control FAIL)" if not ok else ("PASS" if g else "FAIL")))
    txt = "\n".join(out) + "\n"; rp = f"{HERE}/f61ngram{'108v' if V108 else '108r'}_repl{'_ix' if IX else ''}_result.txt"
    if "--check" in ARGS:
        good = os.path.exists(rp) and open(rp).read() == txt; print("fresh" if good else "STALE"); sys.exit(0 if good else 1)
    open(rp, "w").write(txt); print(txt, end="")
if __name__ == "__main__": main()
