#!/usr/bin/env python3
"""N8-GRA2 reconciliation of passA/passB (f.18r L01-L11). Shape decisions made by eye on crops L04_s1 and L07_s1
against atlas_f29.png/atlas_f30add.png, applied only where the two passes split (pair -> code); every other split
becomes '?' (wildcard, never scored). Agreements are kept. Writes recon.tsv."""
import difflib
PAIRS = {frozenset(p): v for p, v in [(("d", "n6"), "n6"), (("lz", "rs"), "rs"), (("br", "BOX"), "br"),
         (("NEW:J_barred", "r3"), "r3"), (("u", "zu"), "zu")]}
ALIAS = {"NEW:J_barred": "r3", "u": "zu"}
def load(f):
    d = {}
    for l in open(f).read().splitlines()[1:]:
        r, c = l.split("\t")
        d[r] = [ALIAS.get(t.rstrip("?"), t.rstrip("?")) for t in c.split() if t not in ("/", ".")]
    return d
A, B = load("passA.tsv"), load("passB.tsv")
out = ["row\tcodes"]; n = q = 0
for i in range(1, 12):
    a = A[f"f18r_L{i:02d}_s1"] + A[f"f18r_L{i:02d}_s2"]; b = B[f"f18r_L{i:02d}_s1"] + B[f"f18r_L{i:02d}_s2"]
    sm = difflib.SequenceMatcher(None, a, b, autojunk=False); row = []
    for op, a0, a1, b0, b1 in sm.get_opcodes():
        if op == "equal":
            row += a[a0:a1]
        elif op == "replace" and a1 - a0 == b1 - b0:
            row += [PAIRS.get(frozenset((x, y)), "?") for x, y in zip(a[a0:a1], b[b0:b1])]
        else:
            row += ["?"] * max(a1 - a0, b1 - b0)
    n += len(row); q += row.count("?")
    out.append(f"f18r_L{i:02d}\t" + " ".join(row))
open("recon.tsv", "w").write("\n".join(out) + "\n")
print(f"reconciled tokens {n}, unsettled '?' {q} ({q/n:.3f})")
