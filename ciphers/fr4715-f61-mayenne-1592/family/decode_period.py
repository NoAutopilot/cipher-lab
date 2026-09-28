#!/usr/bin/env python3
"""F61-FAMILY step 5 (28 Sept 2026): apply family/key_period.tsv (period-gloss pairs, n >= 2, no refit) to the whole of
f.61r's atlas-coded sign transcription -- scripts/passA_classes.tsv (the six Tomokiyo span lines, VBAR split, H15) and
scripts/passU2_classes.tsv (L02, L04, L10, the second blind pass, H17; L06/L09 read as no cipher) -- and write
f61_decode_period.tsv (per token) and f61_decode_period.txt (per line). Grades per token (CLAUDE.md rule 4): C when the
period key gives the class ONE letter (n >= 2, no second letter with n >= 2); M when it gives two or more letters (a
polyphonic pair or a merged class: the choice is by context and is NOT made here -- the set is printed); '-' when the
class has no period pair (unread). Nothing is fitted; the known spans are not used. --check exits 1 if the files are stale.
  python3 decode_period.py [--check]   (from the family folder)
"""
import csv, os, sys
from collections import defaultdict
HERE = os.path.dirname(os.path.abspath(__file__)); S = os.path.abspath(f"{HERE}/../scripts")
key = defaultdict(dict)
for r in csv.DictReader((l for l in open(f"{HERE}/key_period.tsv") if not l.startswith("#")), delimiter="\t"):
    if r["letter"] != "-" and int(r["n"]) >= 2: key[r["class"]][r["letter"]] = key[r["class"]].get(r["letter"], 0) + int(r["n"])
lines = defaultdict(list)
for path in (f"{S}/passA_classes.tsv", f"{S}/passU2_classes.tsv"):
    for r in csv.DictReader((l for l in open(path) if not l.startswith("#")), delimiter="\t"):
        lines[r["line"]].append(r["sign"])
rows = []; tot = {"C": 0, "M": 0, "-": 0}; text = []
for line in sorted(lines):
    out = []
    for i, c in enumerate(lines[line], 1):
        v = key.get(c, {}); letters = "/".join(sorted(v, key=lambda k: -v[k]))
        g = "C" if len(v) == 1 else ("M" if v else "-"); tot[g] += 1
        rows.append((line, i, c, letters or "-", g)); out.append(letters if g == "C" else (f"[{letters}]" if g == "M" else f"<{c}>"))
    text.append(f"{line}: " + " ".join(out))
hdr = f"# f.61r under key_period.tsv (period pairs n>=2, no refit), 28 Sept 2026: {sum(tot.values())} signs, C {tot['C']} M {tot['M']} unread {tot['-']}. [a/b] = period pair, choice by context not made here; <CLASS> = no period pair.\n"
tsv = "line\tpos\tclass\tperiod_letters\tgrade\n" + "".join("\t".join(map(str, r)) + "\n" for r in rows)
txt = hdr + "\n".join(text) + "\n"
if "--check" in sys.argv:
    ok = open(f"{HERE}/f61_decode_period.tsv").read() == tsv and open(f"{HERE}/f61_decode_period.txt").read() == txt
    print("fresh" if ok else "STALE"); sys.exit(0 if ok else 1)
open(f"{HERE}/f61_decode_period.tsv", "w").write(tsv); open(f"{HERE}/f61_decode_period.txt", "w").write(txt); print(txt)
