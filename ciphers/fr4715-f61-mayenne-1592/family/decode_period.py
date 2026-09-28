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
# F61-FAMILY-2 (28 Sept 2026): --key FILE decodes with another key file (output files gain the key's suffix, e.g. _v2);
# EBR_A/EBR_B rows (H22 split, f.101r) are folded into EBR, f.61's own unsplit class. With a non-default key the C+ grade (two
# leaves agree on the one letter) and counts leaves per pair from the 'leaf' column.
KEYFILE = sys.argv[sys.argv.index("--key") + 1] if "--key" in sys.argv else f"{HERE}/key_period.tsv"
SUF = "" if os.path.basename(KEYFILE) == "key_period.tsv" else "_" + os.path.basename(KEYFILE).replace("key_period_", "").replace(".tsv", "")
if "--frac" in sys.argv: SUF += "_frac" + sys.argv[sys.argv.index("--frac") + 1]
leaves = defaultdict(lambda: defaultdict(set))
FRAC = float(sys.argv[sys.argv.index("--frac") + 1]) if "--frac" in sys.argv else 0.0   # same rule as test_period_key.py --frac
_rows = [r for r in csv.DictReader((l for l in open(KEYFILE) if not l.startswith("#")), delimiter="\t")]
_tot = defaultdict(int)
for r in _rows:
    if r["letter"] != "-": _tot[(r["class"], r["leaf"])] += int(r["n"])
for r in _rows:
    cl = {"EBR_A": "EBR", "EBR_B": "EBR"}.get(r["class"], r["class"])
    if r["letter"] != "-" and int(r["n"]) >= 2 and int(r["n"]) >= FRAC * _tot[(r["class"], r["leaf"])]:
        key[cl][r["letter"]] = key[cl].get(r["letter"], 0) + int(r["n"]); leaves[cl][r["letter"]].add(r["leaf"])
lines = defaultdict(list)
for path in (f"{S}/passA_classes.tsv", f"{S}/passU2_classes.tsv"):
    for r in csv.DictReader((l for l in open(path) if not l.startswith("#")), delimiter="\t"):
        lines[r["line"]].append(r["sign"])
# F61-FAMILY-6 (28 Sept 2026): --sbs relabels f.61r's side-by-side loop signs (H26 G2 + pass-A DBL) as SBS (sbs_relabel.py),
# the class key v4 carries (b/o, split out of PHI by the family re-sort); the output files gain '_sbs'.
if "--sbs" in sys.argv:
    sys.path.insert(0, HERE); from sbs_relabel import relabel; relabel(lines); SUF += "_sbs"
# F61-FAMILY-6 (28 Sept 2026): a C+ token is now printed as its letter in the .txt (it was printed as <CLASS>, like an
# unread sign; the .tsv and the header counts were always right). v1-v3 .txt files regenerated for this display fix only.
rows = []; tot = {"C": 0, "M": 0, "-": 0}; text = []
for line in sorted(lines):
    out = []
    for i, c in enumerate(lines[line], 1):
        v = key.get(c, {}); letters = "/".join(sorted(v, key=lambda k: -v[k]))
        g = "C" if len(v) == 1 else ("M" if v else "-")
        if g == "C" and SUF and len(leaves[c][letters]) >= 2: g = "C+"
        tot[g] = tot.get(g, 0) + 1
        rows.append((line, i, c, letters or "-", g)); out.append(letters if g in ("C", "C+") else (f"[{letters}]" if g == "M" else f"<{c}>"))
    text.append(f"{line}: " + " ".join(out))
cplus = f" C+ {tot['C+']}" if tot.get("C+") else ""
hdr = f"# f.61r under {os.path.basename(KEYFILE)} (period pairs n>=2{f', n >= {FRAC:g} x the leaf class total' if FRAC else ''}, no refit), 28 Sept 2026: {sum(tot.values())} signs, C {tot['C']}{cplus} M {tot['M']} unread {tot['-']}. [a/b] = period pair, choice by context not made here; <CLASS> = no period pair{'; C+ = two leaves agree on the one letter' if cplus else ''}.\n"
tsv = "line\tpos\tclass\tperiod_letters\tgrade\n" + "".join("\t".join(map(str, r)) + "\n" for r in rows)
txt = hdr + "\n".join(text) + "\n"
if "--check" in sys.argv:
    ok = open(f"{HERE}/f61_decode_period{SUF}.tsv").read() == tsv and open(f"{HERE}/f61_decode_period{SUF}.txt").read() == txt
    print("fresh" if ok else "STALE"); sys.exit(0 if ok else 1)
open(f"{HERE}/f61_decode_period{SUF}.tsv", "w").write(tsv); open(f"{HERE}/f61_decode_period{SUF}.txt", "w").write(txt); print(txt)
