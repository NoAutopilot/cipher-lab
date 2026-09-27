#!/usr/bin/env python3
"""F61-CRIB2 (campaign step H11, 27 Sept 2026): H1's class map refitted with a null-aware alignment.

Same classes, folds, scoring DP and 20 shuffled class-maps (seed 1) as scripts/f61crib.py (imported from it). The
fit differs in two ways, both through options added to tools/interlinear_align.py for this step: Tomokiyo's dashes
are kept in the markup as explicit unread positions (--wildcard -) instead of being deleted, and a class that takes
no letter is charged --null-cost X instead of the Thurloe default -3.0. Pre-registered main run: X = -1. Sensitivity
(non-gating): X = 0 and X = -3, both with the dashes kept.

Gate (H11, CAMPAIGN.md), both parts: (a) pooled held-out match above every one of the 20 pooled shuffled-map
values; (b) the top-2 value sets of PHI, C43, 4TRI, VBAR, DBL and INF are identical in all five folds.

  python3 scripts/f61crib2.py [--check]   (from the target folder)
Writes scripts/f61crib2_result.txt and scripts/f61crib2_map.tsv (map fitted on all five spans at X = -1).
"""
import os, random, sys
from collections import Counter
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from f61crib import HERE, FOLDS, load_read, load_spans, fit, to_map, score

STABLE = ["PHI", "C43", "4TRI", "VBAR", "DBL", "INF"]

def run(lines, spans, null_cost, out, gate=False):
    by = {s: (s, l, m) for s, l, m in spans}
    opts = ("--wildcard", "-", "--null-cost", str(null_cost))
    rng = random.Random(1); NC = 20
    pooled = tot_all = 0; ctrl = [0] * NC; sets = {c: set() for c in STABLE}
    for held in FOLDS:
        train = [by[s] for s in by if s not in held]; test = [by[s] for s in held]
        kmap = to_map(fit(train, lines, f"nc{null_cost}_{''.join(held)}", opts, keep_dashes=True))
        mt, tot = score(kmap, lines, test); pooled += mt; tot_all += tot
        for c in STABLE: sets[c].add("".join(sorted(kmap.get(c, ()))))   # compared as sets: 'cp' == 'pc' (order-of-count bug fixed before the result was written)
        labs = sorted(kmap); vals = [kmap[l] for l in labs]; cs = []
        for k in range(NC):
            v = list(vals); rng.shuffle(v)
            cm, _ = score(dict(zip(labs, v)), lines, test); ctrl[k] += cm; cs.append(cm)
        out.append(f"  null-cost {null_cost}\theld-out {'+'.join(held)}\tmatched {mt}/{tot}\tshuffled max {max(cs)}/{tot} mean {sum(cs)/NC:.2f}"
                   f"\tmap {' '.join(l + '=' + ''.join(kmap[l]) for l in labs)}")
    pc = [c / tot_all for c in ctrl]
    stab = {c: sorted(sets[c]) for c in STABLE}
    stable = all(len(v) == 1 for v in stab.values())
    out.append(f"null-cost {null_cost}: POOLED held-out {pooled}/{tot_all} = {pooled/tot_all:.3f}; controls mean {sum(pc)/NC:.3f} max {max(pc):.3f}"
               f"; fold-stable sets: {'yes' if stable else 'no'} " + " ".join(f"{c}={'|'.join(v) or '-'}" for c, v in stab.items()))
    if gate:
        out.append("controls (20 shuffled class-maps pooled across folds, seed 1): " + " ".join(f"{c:.3f}" for c in pc))
        a = pooled / tot_all > max(pc)
        out.append(f"GATE H11 (a) pooled above every shuffle: {'PASS' if a else 'FAIL'}; (b) six classes fold-stable: {'PASS' if stable else 'FAIL'}"
                   f"; H11 {'PASS' if a and stable else 'FAIL'}  (H1 was 24/55 = 0.436 vs max 0.345, unstable)")
    return pooled, tot_all

def main():
    lines, spans = load_read(), load_spans()
    out = ["reader file: read_call_A.tsv (marks column only); fit: tools/interlinear_align.py --code-prefix @ --wildcard - --null-cost X; score: f61cal.py DP"]
    out.append("main run (pre-registered): null-cost -1")
    run(lines, spans, -1, out, gate=True)
    out.append("sensitivity (non-gating): null-cost 0 and -3, dashes kept")
    run(lines, spans, 0, out); run(lines, spans, -3, out)
    classes = Counter(c for l in lines.values() for c in l)
    full = fit(spans, lines, "all_nc-1", ("--wildcard", "-", "--null-cost", "-1"), keep_dashes=True)
    with open(f"{HERE}/f61crib2_map.tsv", "w") as f:
        f.write("# F61-CRIB2 map fitted on all five Tomokiyo spans (tools/interlinear_align.py --code-prefix @ --wildcard - --null-cost -1), 27 Sept 2026.\n"
                "# value set = top-2 letters by count; '-' = no letter ever aligned (a null under this map). Grade M: from Tomokiyo's own 'Solution Incomplete' markup.\n"
                "class\tn_signs\tvalues\tcounts\n")
        for c, n in classes.most_common():
            cnt = full.get(c, Counter())
            f.write(f"{c}\t{n}\t{'/'.join(to_map({c: cnt})[c]) if cnt else '-'}\t{' '.join(f'{l}:{k}' for l, k in cnt.most_common())}\n")
    out.append("map on all five spans (null-cost -1) -> scripts/f61crib2_map.tsv")
    txt = "\n".join(out) + "\n"
    res = f"{HERE}/f61crib2_result.txt"
    if "--check" in sys.argv:
        ok = os.path.exists(res) and open(res).read() == txt
        print("fresh" if ok else "STALE"); sys.exit(0 if ok else 1)
    open(res, "w").write(txt); print(txt, end="")

if __name__ == "__main__":
    main()
