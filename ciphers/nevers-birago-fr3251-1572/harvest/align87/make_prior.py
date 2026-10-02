#!/usr/bin/env python3
"""Seed key for the no.87 alignment (NEVBIR-87ALIGN): the printed 1572 table as Tomokiyo prints it (T42 = g, NOT the
GAPS3 fit, so a T42 = m out of the sheet is evidence, not echo), coded as build_pairs.py codes it.
  python3 make_prior.py [--shuffle SEED] [--out prior.tsv]
--shuffle SEED: values permuted among the letter signs (word signs keep theirs) -- the wrong-seed control."""
import argparse, csv, random
from pathlib import Path
H = Path(__file__).resolve().parent.parent
WORD = {"T11", "T15", "T26", "T29", "T46", "T78", "T84", "T89"}
ap = argparse.ArgumentParser(); ap.add_argument("--shuffle", type=int)
ap.add_argument("--out", default=str(Path(__file__).resolve().parent / "prior.tsv")); a = ap.parse_args()
key = {r["sign"]: r["value"] for r in csv.DictReader(open(H / "key_1572_sheet.tsv"), delimiter="\t")}
key["T42"] = "g"  # as printed
if a.shuffle is not None:
    ids = sorted(s for s in key if s not in WORD); vals = [key[s] for s in ids]
    random.Random(a.shuffle).shuffle(vals); key.update(zip(ids, vals))
with open(a.out, "w") as f:
    f.write("code\tmeaning\n")
    for s, v in sorted(key.items()):
        if v.lower() in ("null", ""):
            continue
        f.write(f"{6000 + int(s[1:]) if s in WORD else int(s[1:])}\t{v}\n")
print(f"{len(key)} signs -> {a.out}")
