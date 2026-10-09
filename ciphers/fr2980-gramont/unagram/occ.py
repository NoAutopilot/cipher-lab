#!/usr/bin/env python3
"""UNA-GRAM (PREREG-UNA-GRAM.md): build unagram/occ.tsv -- 6 targets X + decoys fh/n6 (24) + P (12) from r12zb/occ.tsv + 12 B
(fr.3040 tiles R12D-GRAZB2 sorted C1, seeded). New ids by random.Random(20261009). Columns as r12zb/occ.tsv plus old_id
(the r12zb id, whose r12zb2/fixes.tsv box fix is reused; '-' for X). python3 unagram/occ.py"""
import random, sys
from pathlib import Path
if "--help" in sys.argv: print(__doc__); sys.exit()
H = Path(__file__).resolve().parent; T = H.parent
occ = [l.split("\t") for l in (T / "r12zb/occ.tsv").read_text().splitlines()[1:]]
cl = dict(l.split("\t") for l in (T / "r12zb2/sort_sonnet.tsv").read_text().splitlines()[1:])
X = ["f18vC_L02 29", "f18vC_L07 8", "f18vC_L10 30", "f18vC_L13 26", "f18vC_L14 8", "f18vC_L14 18"]
rng = random.Random(20261009)
rows = []
for lp in X:
    ln, pos = lp.split(); pos = int(pos)
    rows.append(("X", "fr3040", lp, f"images/fr3040_f18/{ln}_a.jpg", "-"))  # half fixed below
keep = [r for r in occ if r[1] in ("fh", "n6", "P")]
rows += [(r[1], r[2], r[3], r[4], r[0]) for r in keep]
b = sorted([r for r in occ if r[1] in ("T2a", "T2b") and cl[r[0]] == "C1"], key=lambda r: int(r[0]))
rows += [("B", r[2], r[3], r[4], r[0]) for r in rng.sample(b, 12)]
halves = {l.split("\t")[0]: int(l.split("\t")[1]) for l in (T / "r12zb2/halves.tsv").read_text().splitlines()[1:]}
fixed = []
for st, src, lp, img, old in rows:
    if st == "X":
        ln, pos = lp.split()
        na = halves[f"images/fr3040_f18/{ln}_a.jpg"]
        img = f"images/fr3040_f18/{ln}_{'a' if int(pos) < na else 'b'}.jpg"
    fixed.append((st, src, lp, img, old))
ids = list(range(1, len(fixed) + 1)); rng.shuffle(ids)
out = ["id\tset\tsrc\tline_pos\timage\told_id"] + [f"{i}\t{st}\t{src}\t{lp}\t{img}\t{old}" for i, (st, src, lp, img, old) in sorted(zip(ids, fixed))]
(H / "occ.tsv").write_text("\n".join(out) + "\n")
print(len(fixed), "tiles;", sum(1 for r in fixed if r[0] == "B"), "B of", len(b), "C1 fr.3040")
