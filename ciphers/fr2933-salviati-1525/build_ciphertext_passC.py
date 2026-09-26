#!/usr/bin/env python3
"""bSALC (26 Sept 2026): rebuild ciphertext_<leaf>.tsv from the pass-C votes.

  python3 build_ciphertext_passC.py [leaf ...]      (default: every leaf with recon_box_<leaf>/settled_passC.tsv)

Every row of the committed ciphertext_<leaf>.tsv whose (line, pos) is in recon_box_<leaf>/settled_passC.tsv takes the
2-of-3 value (grade 'settledC') or, at a three-way split, the provisional/crop value (grade 'split'); all other rows
(both passes agreed) are unchanged. Prints the per-leaf count of rows whose code or marks changed.
"""
import csv, os, sys

leaves = sys.argv[1:] or [l for l in ("f54v", "f55r", "f55v", "f56r", "f56v", "f57r", "f57v")
                          if os.path.exists(f"recon_box_{l}/settled_passC.tsv")]
for lf in leaves:
    S = {(r["line"], r["pos"]): r for r in csv.DictReader(open(f"recon_box_{lf}/settled_passC.tsv"), delimiter="\t")}
    rows = list(csv.DictReader(open(f"ciphertext_{lf}.tsv"), delimiter="\t"))
    changed = code_changed = hit = 0
    for r in rows:
        s = S.get((r["line"], r["pos"]))
        if not s:
            continue
        hit += 1
        new = (s["code"], s["marks"])
        if new != (r["code"], r["marks"]):
            changed += 1
            code_changed += new[0] != r["code"]
        r["code"], r["marks"] = new
        r["grade"] = "split" if s["source"].startswith("split") else "settledC"
    assert hit == len(S), (lf, hit, len(S))
    with open(f"ciphertext_{lf}.tsv", "w") as f:
        f.write("line\tpos\tcode\tmarks\tgrade\n")
        for r in rows:
            f.write("\t".join((r["line"], r["pos"], r["code"], r["marks"], r["grade"])) + "\n")
    print(f"{lf}: {len(S)} disputed rows re-set, {changed} changed ({code_changed} base code)")
