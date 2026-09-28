#!/usr/bin/env python3
"""F61-108V-L05 (campaign step H106, 28 Sept 2026, runner session_01NQpd6L9ZvLvjU1L7ttFmZs), script-only: f.108v row L05, the weak
row of H101 -- per cell position, the class, the draft grade, and the letter each of the four target resolutions chose
(H85 seeds 101-103, H94 seed 104), with the positions where they disagree marked, and the same disagreement rate for the
other rows. -> scripts/f108v_L05.txt [--check]"""
import csv, json, os, sys
from collections import Counter
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import f61judge108v as J
C = J.cells()
draft = [r for r in csv.DictReader((l for l in open(f"{HERE}/../family/passes/f108v3z_draft_reconciled.tsv") if not l.startswith("#")), delimiter="\t")]
R = {}
for s in (101, 102, 103, 104):
    k = json.load(open(f"{HERE}/f61judge_f108v_s{s}_key.json"))["key"]; t = [l for l, m in k.items() if m == 0][0]
    v = {r["label"].strip(): r for r in csv.DictReader((l for l in open(f"{HERE}/f61judge_f108v_s{s}_verdict.tsv") if not l.startswith("#")), delimiter="\t")}
    R[s] = [x.strip().replace(" ", "") for x in v[t]["reading"].split("|")]
out = ["row\tpositions\tall_four_agree\tdisagree\tdisagree_on_L\tdisagree_classes"]
detail = []
for li in range(7):
    line = f"L0{li + 1}"; sg = [r for r in draft if r["line"] == line and r["sign"] in C]
    four = [R[s][li] for s in (101, 102, 103, 104)]
    if not all(len(x) == len(sg) for x in four): out.append(f"{line}\tlength mismatch {[len(x) for x in four]} vs {len(sg)}"); continue
    dis = [k for k in range(len(sg)) if len({x[k] for x in four}) > 1]
    out.append("\t".join([line, str(len(sg)), str(len(sg) - len(dis)), str(len(dis)), str(sum(1 for k in dis if sg[k]["grade"] == "L")),
                          ", ".join(f"{c} {n}" for c, n in Counter(sg[k]["sign"] for k in dis).most_common())]))
    if line == "L05":
        for k, r in enumerate(sg):
            detail.append(f"L05\t{k + 1}\t{r['sign']}\t{C[r['sign']]}\t{r['grade']}\t" + "".join(x[k] for x in four) + ("\t*" if k in dis else ""))
txt = "\n".join(out) + "\n# L05 per position: pos, class, cell, draft grade, letters chosen in calls 101/102/103/104, * = disagreement\n" + "\n".join(detail) + "\n"
res = f"{HERE}/f108v_L05.txt"
if "--check" in sys.argv:
    ok = os.path.exists(res) and open(res).read() == txt; print("fresh" if ok else "STALE"); sys.exit(0 if ok else 1)
open(res, "w").write(txt); print("\n".join(out))
