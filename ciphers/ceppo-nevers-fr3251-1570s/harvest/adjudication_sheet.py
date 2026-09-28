#!/usr/bin/env python3
"""Write the sheet a third blind reader settles disputed positions from (HARVEST-D2): for each row of
<out>_disagreements.tsv, the passage, the merged position, the four merged sign ids before and after it (so the
reader can find the mark on the line crop by counting), and the two candidates.  No sign value is involved.
  python3 adjudication_sheet.py f35/passC > f35/adjudicate_in.tsv
"""
import csv, sys
base = sys.argv[1]
mer = {}
for r in csv.DictReader(open(base + ".tsv"), delimiter="\t"):
    mer.setdefault(r["passage"], []).append(r["sign_id"])
print("passage\tpos\tcontext_before\tcontext_after\tcandA\tconfA\tcandB\tconfB\tnoteA\tnoteB")
for r in csv.DictReader(open(base + "_disagreements.tsv"), delimiter="\t"):
    if not r["merged_pos"]:
        continue
    p, k = r["passage"], int(r["merged_pos"]); seq = mer[p]
    before = " ".join(seq[max(0, k - 5):k - 1]); after = " ".join(seq[k:k + 4])
    print(f"{p}\t{k}\t{before}\t{after}\t{r['idA'] or '(none)'}\t{r['confA']}\t{r['idB'] or '(none)'}\t{r['confB']}\t{r['noteA']}\t{r['noteB']}")
