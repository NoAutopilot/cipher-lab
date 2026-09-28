#!/usr/bin/env python3
"""F61-SWAP-FAMILY (campaign step H132, 28 Sept 2026, runner 5 session_01RbeePKZVn83gNfES8yFmhe), script-only. Every
one-swap neighbour of f.61's cell map tested on the pooled family leaves (f.97r, f.101r, f.188r, f.124r reconciled drafts;
H129 ranks each in f.61's cells), with KEY.md's period equivalences for this hand added (LOOPS = h/u, H24 = i/x,
ZBAR = f/s). Statistic: the H127 sequence gain (real order minus the mean of 20 within-line shuffles; null on shuffled
text, H128). For each pair of classes whose cells differ, the swapped map's gain vs the fitted map's, and the number of
pooled positions the swap changes. Pre-registered: a swap is REJECTED (the fitted assignment confirmed against it) when the
fitted gain exceeds the swap's; the swap is PREFERRED when its gain is higher. No threshold beyond the sign of the difference;
the difference is reported so the verifier can weigh it.   -> scripts/f61swap_family_result.txt [--check]"""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
ARGS = sys.argv[1:]; sys.argv = sys.argv[:1]
import f61seqgain_family as F
G = F.G
def main():
    L = {}
    for leaf in ("f97r", "f101r", "f188r", "f124r"):
        for k, v in F.draft(leaf).items(): L[f"{leaf}_{k}"] = v
    C = dict(G.J.cells(), LOOPS="h/u", H24="i/x", ZBAR="f/s"); SH = G.shuffles(L); g0 = G.gain(L, SH, C)
    cnt = {c: sum(s.count(c) for s in L.values()) for c in C}; labs = sorted(C); rows = []
    for i, a in enumerate(labs):
        for b in labs[i + 1:]:
            if C[a] == C[b]: continue
            m = dict(C); m[a], m[b] = C[b], C[a]; g = G.gain(L, SH, m); rows.append((g0 - g, a, b, cnt[a] + cnt[b]))
    rows.sort()
    out = [f"pool {sum(len(v) for v in L.values())} signs; fitted gain {g0:.4f}; {len(rows)} one-swaps",
           f"swaps PREFERRED over the fitted map (gain higher): {sum(1 for d, *_ in rows if d < 0)}; rejected: {sum(1 for d, *_ in rows if d > 0)}",
           "closest 15 (fitted minus swap gain, classes, cells, positions changed):"]
    out += [f"  {d:+.4f}  {a}({C[a]})<->{b}({C[b]})  {n}" for d, a, b, n in rows[:15]]
    txt = "\n".join(out) + "\n"; rp = f"{HERE}/f61swap_family_result.txt"
    if "--check" in ARGS:
        good = os.path.exists(rp) and open(rp).read() == txt; print("fresh" if good else "STALE"); sys.exit(0 if good else 1)
    open(rp, "w").write(txt); print(txt, end="")
if __name__ == "__main__": main()
