"""NEVBIR-117C: decode input = passD (2-of-3 reconcile output); a tile still '?' after the rule takes the one-eye settle
label from ../recon_f117_final.tsv (counted, per PREREG.md). Usage: python3 fill_unsettled.py passD.tsv OUT.tsv"""
import csv, sys
rows = list(csv.DictReader(open(sys.argv[1]), delimiter="\t"))
fin = {(r["passage"], r["pos"]): r for r in csv.DictReader(open("../recon_f117_final.tsv"), delimiter="\t")}
n = 0
for r in rows:
    if r["sign_id"] in ("?", "") or r["sign_id"].startswith("SPLIT"):
        f = fin[(r["passage"], r["pos"])]
        if f["sign_id"] != r["sign_id"]:
            r["sign_id"] = f["sign_id"]; r["note"] = (r.get("note") or "") + " one-eye fill"; n += 1
w = csv.DictWriter(open(sys.argv[2], "w"), fieldnames=list(rows[0].keys()), delimiter="\t", lineterminator="\n")
w.writeheader(); w.writerows(rows)
print(f"{len(rows)} signs; {n} unsettled tiles filled from the one-eye settle")
