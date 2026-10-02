#!/usr/bin/env python3
"""A2-HDK3, 2 Oct 2026: compare ../key.tsv (HCPortal key 255 letter table, = DECODE 4691) with the period decipher
scale in DECODE 4690 image P2, headed 'Scala über den Clavem mit Secretarium Linckern' (read M, one eye, top 62% of the
leaf at 1300 px; the image is account-gated and not committed). Writes scale4690_read.tsv; exit 1 on any disagreement."""
import os, sys
here = os.path.dirname(os.path.abspath(__file__))
cols = {20: "afbgchdiekafbgchdi", 47: "iekafbgchdiekafbgchdi", 78: "pulqmrnsotpulqmrnsotp",
        110: "lqmrnsotpuw-x-y-z---w-x-", 145: "-z---w-x-y-z---w-x-y-z"}
rows = [("code", "value", "note")]
for start, s in cols.items():
    for i, ch in enumerate(s): rows.append((str(start + i), "NULL" if ch == "-" else ch, ""))
for d, v in zip("LL MM NN OO PP QQ RR SS TT UU WW XX YY ZZ".split(), "iklmnopqrstuwx"): rows.append((d, v, "doubled column"))
open(os.path.join(here, "scale4690_read.tsv"), "w").write("".join("\t".join(r) + "\n" for r in rows))
key = {l.split("\t")[0]: l.split("\t")[1] for l in open(os.path.join(here, "..", "key.tsv")).read().splitlines()[1:]}
agree = dis = 0
for c, v, _ in rows[1:]:
    k = key.get(c)
    if k == v: agree += 1
    else: dis += 1; print("DISAGREE", c, "scale", v, "key.tsv", k)
print(f"scale entries {len(rows)-1}: agree {agree}, disagree {dis}")
sys.exit(1 if dis else 0)
