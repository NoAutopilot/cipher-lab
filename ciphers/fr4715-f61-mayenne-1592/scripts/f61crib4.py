#!/usr/bin/env python3
"""F61-CRIB4 (campaign step H14, second half, 27 Sept 2026): the H12 table-cell fit with the VBAR class split.

Pre-registered before the H14 confirmation call's output was read. Runs only if scripts/f61vbar3_result.txt carries
"GATE H13 under rule 3 ... PASS" (H15's confirmation, geometric de-duplication pre-registered; amended from H14's rule-1 guard). The split: read_call_A.tsv's VBAR signs are
relabelled VBAR_A / VBAR_B by the group the H15 call gives the sign at the same (sheet, order) position after
rule 3 de-duplication (per sheet, in order; counts must match on every sheet). Then scripts/f61crib3.py's leave-one-span-out
cell fit is re-run unchanged on the split classes (20 cell-permuted controls, seed 1). Gate (H14b): (a) pooled held-out
above every control AND (b) the cell of PHI, C43, 4TRI, VBAR_A, VBAR_B, DBL identical in all five folds; INF reported,
not gated (4 of its 5 signs sit in one span).

  python3 scripts/f61crib4.py [--check]   (from the target folder)
Writes scripts/f61crib4_result.txt and scripts/f61crib4_map.tsv.
"""
import csv, os, random, sys
from collections import Counter, defaultdict
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from f61crib import HERE, FOLDS, load_read, load_spans, fit, score
from f61crib3 import load_cells, cell_map, values, OPTS
from f61vbar import VBAR_POS

STABLE = ["PHI", "C43", "4TRI", "VBAR_A", "VBAR_B", "DBL"]

def split_lines(lines):
    # H15 (amended 27 Sept 2026 after H14, before H15's call): the H15 call's file, rule 3 (geometric de-duplication) PASS
    from f61vbar import dedup_by_geometry
    ok = os.path.exists(f"{HERE}/f61vbar3_result.txt") and "GATE H13 under rule 3 (observed above permutation p95, exact p < 0.05): PASS" in open(f"{HERE}/f61vbar3_result.txt").read()
    if not ok: raise SystemExit("f61vbar3_result.txt does not carry a rule-3 PASS: H15 second half not run")
    rows = dedup_by_geometry([r for r in csv.DictReader((l for l in open(f"{HERE}/read_call_V3.tsv") if not l.startswith("#")), delimiter="\t") if "4-shaped" not in r["extra"]])
    by = defaultdict(list)
    for r in rows: by[r["sheet"]].append(r)
    for sheet, poss in VBAR_POS.items():
        got = sorted(by.get(sheet, []), key=lambda r: (int(r["segment"]), float(r["x_px"])))
        assert len(got) == len(poss), (sheet, len(got), len(poss))
        for r, pos in zip(got, poss):
            assert lines[sheet][pos - 1] == "VBAR", (sheet, pos)
            lines[sheet][pos - 1] = "VBAR_" + r["group"].strip().upper()
    return lines

def main():
    lines, spans, cells = split_lines(load_read()), load_spans(), load_cells()
    by = {s: (s, l, m) for s, l, m in spans}
    classes = Counter(c for l in lines.values() for c in l)
    out = ["H12 cell fit re-run with VBAR split by the H14 confirmation call (rule 1 pairing); classes: " + " ".join(f"{c}:{n}" for c, n in classes.most_common())]
    rng = random.Random(1); NC = 20
    pooled = tot_all = 0; ctrl = [0] * NC; fc = {c: set() for c in STABLE + ["INF"]}
    for held in FOLDS:
        train = [by[s] for s in by if s not in held]; test = [by[s] for s in held]
        cm = cell_map(fit(train, lines, "c4_" + "".join(held), OPTS, keep_dashes=True), cells); kmap = values(cm)
        mt, tot = score(kmap, lines, test); pooled += mt; tot_all += tot
        for c in fc: fc[c].add(cm[c][0] if c in cm else "null")
        labs = sorted(kmap); vals = [kmap[l] for l in labs]; cs = []
        for k in range(NC):
            v = list(vals); rng.shuffle(v); cmk, _ = score(dict(zip(labs, v)), lines, test); ctrl[k] += cmk; cs.append(cmk)
        out.append(f"held-out {'+'.join(held)}\tmatched {mt}/{tot}\tcontrol max {max(cs)}/{tot} mean {sum(cs)/NC:.2f}\tcells " + " ".join(f"{l}={cm[l][0]}" for l in labs))
    pc = [c / tot_all for c in ctrl]
    out.append(f"POOLED held-out\t{pooled}/{tot_all} = {pooled/tot_all:.3f}  (H12 unsplit 37/55 = 0.673 vs max 0.436)")
    out.append("controls (20 cell-permuted maps, seed 1): " + " ".join(f"{c:.3f}" for c in pc))
    out.append(f"control mean {sum(pc)/NC:.3f} max {max(pc):.3f}")
    out.append("cell per fold: " + " ".join(f"{c}={'|'.join(sorted(v))}" for c, v in fc.items()))
    stable = all(len(fc[c]) == 1 for c in STABLE); a = pooled / tot_all > max(pc)
    out.append(f"GATE H14b (a) pooled above every control: {'PASS' if a else 'FAIL'}; (b) six classes cell-stable (INF not gated): {'PASS' if stable else 'FAIL'}; H14b {'PASS' if a and stable else 'FAIL'}")
    full = cell_map(fit(spans, lines, "c4_all", OPTS, keep_dashes=True), cells)
    with open(f"{HERE}/f61crib4_map.tsv", "w") as f:
        f.write("# F61-CRIB4 map on all five Tomokiyo spans, VBAR split by the H14 confirmation call: class -> Mayenne table cell, 27 Sept 2026. Grade M (cells from Tomokiyo's markup); the pair is the key's.\n"
                "class\tn_signs\tcell\tcell_counts\ttie\n")
        for c, n in classes.most_common():
            v = full.get(c)
            f.write(f"{c}\t{n}\t{v[0] if v else 'null'}\t{' '.join(f'{k}:{m}' for k, m in v[1].most_common()) if v else ''}\t{'yes' if v and v[2] else ''}\n")
    ins, _ = score(values(full), lines, spans)
    out.append(f"all-span map (scripts/f61crib4_map.tsv), in-sample, non-gating: {ins}/55")
    txt = "\n".join(out) + "\n"; res = f"{HERE}/f61crib4_result.txt"
    if "--check" in sys.argv:
        ok = os.path.exists(res) and open(res).read() == txt
        print("fresh" if ok else "STALE"); sys.exit(0 if ok else 1)
    open(res, "w").write(txt); print(txt, end="")

if __name__ == "__main__":
    main()
