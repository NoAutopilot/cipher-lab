#!/usr/bin/env python3
"""N8-GRA3 reconciliation of passA/passB (u1 + u2). Agreements kept. Reader-label aliases (pass B wrote atlas
descriptions or short forms): a -> A2 (atlas 'plain a'), O -> null_o, n -> n6, NEW:v* -> v (both readers saw the same
v shape; unkeyed, wildcard). Splits settled by this worker's eye on the crops against atlas_f29/atlas_f30add, WITHOUT
the print: (H, HASH) on f19r_L02 -> HASH (two verticals crossed by two bars, '#', not H's single bar); (zb, mx) -> zb
(a barred z on f19r_L02_b). Every other split -> '?' (wildcard, never scored). Writes recon.tsv."""
import difflib
ALIAS = {"a": "A2", "O": "null_o", "n": "n6", "v": "v"}
PAIRS = {frozenset(p): v for p, v in [(("H", "HASH"), "HASH"), (("zb", "mx"), "zb")]}
def norm(t):
    t = t.rstrip("?")
    if t.startswith("NEW:v"): return "v"
    return ALIAS.get(t, t)
def load(fs):
    d = {}
    for f in fs:
        for l in open(f).read().splitlines()[1:]:
            r, *c = l.split("\t"); d[r] = [norm(t) for t in (c[0] if c else "").split() if t not in ("/", ".")]
    return d
A = load(["passA_u1.tsv", "passA_u2.tsv"]); B = load(["passB_u1.tsv", "passB_u2.tsv"])
lines = [l for p in ("f18vA", "f18vB", "f18vC", "f19r") for l in sorted({r[:-2] for r in A if r.startswith(p)})]
out = ["row\tcodes"]; n = q = ag = 0
for ln in lines:
    a = A[ln + "_a"] + A[ln + "_b"]; b = B[ln + "_a"] + B[ln + "_b"]
    sm = difflib.SequenceMatcher(None, a, b, autojunk=False); row = []
    for op, a0, a1, b0, b1 in sm.get_opcodes():
        if op == "equal":
            row += a[a0:a1]; ag += a1 - a0
        elif op == "replace" and a1 - a0 == b1 - b0:
            row += [PAIRS.get(frozenset((x, y)), "?") for x, y in zip(a[a0:a1], b[b0:b1])]
        else:
            row += ["?"] * max(a1 - a0, b1 - b0)
    n += len(row); q += row.count("?")
    out.append(f"{ln}\t" + " ".join(row))
open("recon.tsv", "w").write("\n".join(out) + "\n")
print(f"reconciled tokens {n}, agreed after aliases {ag}, unsettled '?' {q} ({q/n:.3f})")
