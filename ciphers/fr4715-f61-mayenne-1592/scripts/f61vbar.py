#!/usr/bin/env python3
"""F61-VBAR (campaign step H13, 27 Sept 2026): is the reader's one 'V with bar' class two glyphs?

Pre-registered before the vision call's output was read (the call itself was launched in parallel; this file was
written without seeing it). Input: scripts/read_call_V.tsv, one Opus vision subagent's blind list of every V/triangle-
with-bar cipher sign on the six span sheets (no letters, no key, no expected count given), with its own 2-3 shape
groups. Reconciliation: per sheet, the subagent's V-signs in order are paired with read_call_A.tsv's VBAR positions in
order (L01: pos 10; L03: 5, 6; L05: 3, 18; L07: 9; L11: 6, 12); a sheet whose count differs is reported and its
positions are dropped from the score (no re-pairing by eye). Labels: the markup letter at each VBAR position under
the H12 all-span cell map's alignment (scripts/f61crib3.py): L03/5 s, L03/6 t, L05/3 t, L05/18 s, L07/9 s, L11/6 t,
L11/12 t; L01/10 unaligned (a dash), never scored.

Statistic: over the scored positions, the best assignment of the subagent's groups to {s, t} (each group -> one
letter, every 2^k mapping tried), matches / scored. Controls: the exact null over every arrangement of the s/t labels
on the scored positions (C(n, n_s) arrangements, small enough to enumerate) and, as registered in CAMPAIGN.md, 200
random permutations (seed 1). Gate: the observed statistic above the permutation p95 (exact one-sided p < 0.05).

  python3 scripts/f61vbar.py [--check]   (from the target folder)
"""
import csv, itertools, os, random, sys
from collections import defaultdict
HERE = os.path.dirname(os.path.abspath(__file__))
VBAR_POS = {"L01": [10], "L03": [5, 6], "L05": [3, 18], "L07": [9], "L11": [6, 12]}
LABELS = {("L03", 5): "s", ("L03", 6): "t", ("L05", 3): "t", ("L05", 18): "s", ("L07", 9): "s", ("L11", 6): "t", ("L11", 12): "t"}

def stat(groups, labels):
    """groups/labels: parallel lists. best over group->letter mappings of the match count."""
    gs = sorted(set(groups)); best = 0
    for letters in itertools.product("st", repeat=len(gs)):
        m = dict(zip(gs, letters))
        best = max(best, sum(1 for g, l in zip(groups, labels) if m[g] == l))
    return best

def main():
    rows = list(csv.DictReader(open(f"{HERE}/read_call_V.tsv"), delimiter="\t"))
    by = defaultdict(list)
    for r in rows: by[r["sheet"]].append(r)
    out = [f"read_call_V.tsv: {len(rows)} V-signs listed by the blind call; groups " + ", ".join(sorted({r['group'] for r in rows}))]
    groups, labels, scored = [], [], []
    for sheet, poss in VBAR_POS.items():
        got = sorted(by.get(sheet, []), key=lambda r: (int(r["segment"]), float(r["x_px"])))
        if len(got) != len(poss):
            out.append(f"  {sheet}: reader VBAR count {len(poss)}, blind call found {len(got)} -> NOT reconciled, {len(poss)} position(s) dropped")
            continue
        for r, pos in zip(got, poss):
            lab = LABELS.get((sheet, pos))
            out.append(f"  {sheet}/{pos}: group {r['group']}, letter {lab or '-'}, bar {r['bar_position']}, {r['closed']}, {r['weight']}, extra {r['extra']}")
            if lab: groups.append(r["group"]); labels.append(lab); scored.append((sheet, pos))
    n = len(labels)
    if n < 4:
        out.append(f"scored positions {n} < 4: NON-TEST (reconciliation failed)"); txt = "\n".join(out) + "\n"
    else:
        obs = stat(groups, labels)
        ns = labels.count("s")
        exact = [stat(groups, ["s" if i in comb else "t" for i in range(n)]) for comb in itertools.combinations(range(n), ns)]
        p_exact = sum(1 for e in exact if e >= obs) / len(exact)
        rng = random.Random(1); perm = []
        for _ in range(200):
            l2 = list(labels); rng.shuffle(l2); perm.append(stat(groups, l2))
        perm.sort(); p95 = perm[int(0.95 * 200) - 1]
        out.append(f"scored {n} positions (s {ns}, t {n - ns}); groups used {len(set(groups))}")
        out.append(f"observed best group->letter match {obs}/{n} = {obs/n:.3f}")
        out.append(f"exact null over {len(exact)} label arrangements: P(>= observed) = {p_exact:.3f}; max achievable {max(exact)}/{n}")
        out.append(f"200 permutations (seed 1): mean {sum(perm)/200:.2f}/{n}, p95 {p95}/{n}")
        out.append(f"GATE H13 (observed above permutation p95, exact p < 0.05): {'PASS' if obs > p95 and p_exact < 0.05 else 'FAIL'}")
        txt = "\n".join(out) + "\n"
    res = f"{HERE}/f61vbar_result.txt"
    if "--check" in sys.argv:
        ok = os.path.exists(res) and open(res).read() == txt
        print("fresh" if ok else "STALE"); sys.exit(0 if ok else 1)
    open(res, "w").write(txt); print(txt, end="")

if __name__ == "__main__":
    main()
