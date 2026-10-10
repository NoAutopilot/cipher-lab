#!/usr/bin/env python3
"""FV-O9b: letters-only phrase grep of every IA djvu text on disk (sources/ia-fulltext/print-check, scratch dirs given as args)."""
import gzip, glob, re, sys, os
PH = ["forty thousand bushels of grain", "seven hundred tons of hay", "quantity of forage to be placed", "do not use steamers",
      "large propeller dispatched", "deep entrance", "state reasons of doubt", "be certain of success",
      "reserve accommodations", "official visit to the department of the south", "three state rooms", "dont let the fulton",
      "let the fulton sail", "miss dix", "master painter", "brooklyn yard", "full names of", "franklin street", "absconded",
      "olcott", "s l brown", "van vliet"]
def norm(s): return re.sub(r"[^a-z]", "", s.lower())
files = sorted(glob.glob("sources/ia-fulltext/print-check/*_djvu.txt*")) + [f for d in sys.argv[1:] for f in glob.glob(d + "/*djvu.txt*")]
for f in files:
    raw = (gzip.open(f, "rt", errors="ignore") if f.endswith(".gz") else open(f, errors="ignore")).read()
    n = norm(raw); hits = []
    for p in PH:
        c = n.count(norm(p))
        if c: hits.append(f"{p}:{c}")
    print(os.path.basename(f), "|", "; ".join(hits) if hits else "0")
