#!/usr/bin/env python3
"""F61-FAMILY-2 (28 Sept 2026): merge the per-leaf period key rows into one family key, keeping both sources per pair.
  python3 merge_period_keys.py OUT.tsv IN1.tsv IN2.tsv ...     (from the family folder)
Every input row (class, letter, n, leaf, bands) is copied as it is -- one row per (class, letter, leaf), never summed
across leaves, so a verifier sees which leaf attests which pair. A CONFLICT is recorded (not resolved) in OUT's header
when two leaves give a class different top letters (top = the most frequent letter with n >= 2 on that leaf): the
merged key carries both; the choice between them is context (grade M), never preference for one leaf.
"""
import csv, sys
from collections import defaultdict
out, ins = sys.argv[1], sys.argv[2:]
rows = []; top = defaultdict(dict)
for f in ins:
    for r in csv.DictReader((l for l in open(f) if not l.startswith("#")), delimiter="\t"):
        rows.append(r)
        if r["letter"] != "-" and int(r["n"]) >= 2:
            d = top[r["class"]].setdefault(r["leaf"], {}); d[r["letter"]] = d.get(r["letter"], 0) + int(r["n"])
conf = []
for c, per in sorted(top.items()):
    if len(per) < 2: continue
    tops = {leaf: max(d, key=d.get) for leaf, d in per.items()}
    if len(set(tops.values())) > 1: conf.append(f"{c}: " + "; ".join(f"{leaf} top {t} ({per[leaf]})" for leaf, t in tops.items()))
with open(out, "w") as f:
    f.write(f"# {out.split('/')[-1]} -- F61-FAMILY-2, 28 Sept 2026: family period key merged by merge_period_keys.py from " + ", ".join(i.split('/')[-1] for i in ins) + ".\n")
    f.write("# Key source: period (CLAUDE.md rule 10 vocabulary). One row per (class, letter, leaf): both leaves' rows are kept, nothing summed across leaves, nothing fitted.\n")
    f.write("# Cross-leaf conflicts on the top letter (recorded, not resolved; grade M where the choice is by context): " + (" | ".join(conf) if conf else "none") + "\n")
    f.write("class\tletter\tn\tleaf\tbands\n")
    for r in sorted(rows, key=lambda r: (r["class"], r["leaf"], -int(r["n"]), r["letter"])):
        f.write("\t".join(r[k] for k in ("class", "letter", "n", "leaf", "bands")) + "\n")
print("rows", len(rows), "classes", len(top), "conflicts", len(conf)); [print(" ", c) for c in conf]
