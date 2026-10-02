"""NEVBIR-117C: decode input = passD (2-of-3 reconcile output); a tile still '?' after the rule takes the one-eye settle
label from ../recon_f117_final.tsv (counted, per PREREG.md). The L03 "8 5" -> T11 merge is applied first. Usage: python3 fill_unsettled.py passD.tsv OUT.tsv"""
import csv, sys
rows = list(csv.DictReader(open(sys.argv[1]), delimiter="\t"))
# Structural step carried over from NEVBIR-3252-B (segmentation, not a label vote): L03's "8 5" (T46 + X_S at pos 25-26)
# is one sign, cell T11 (word code 85); merge it and renumber L03 so positions match ../recon_f117_final.tsv.
i = next(k for k, r in enumerate(rows) if r["passage"] == "L03" and r["pos"] == "25")
assert rows[i]["sign_id"] == "T46" and rows[i + 1]["sign_id"] == "X_S", (rows[i], rows[i + 1])
rows[i]["sign_id"] = "T11"; rows[i]["note"] = "8 5 = T11 (structural, NEVBIR-3252-B)"; del rows[i + 1]
for k, r in enumerate([r for r in rows if r["passage"] == "L03"], 1):
    r["pos"] = str(k)
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
