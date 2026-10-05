#!/usr/bin/env python3
"""N9-GRA4 (copy of n8gra3/splits.py): raw agreement of passA/passB (u1+u2) per line and the split pairs, for the reconciliation."""
import difflib, collections, sys
def load(fs):
    d = {}
    for f in fs:
        for l in open(f).read().splitlines()[1:]:
            r, *c = l.split("\t"); d[r] = [t.rstrip("?") for t in (c[0] if c else "").split() if t not in ("/", ".")]
    return d
A = load(["passA.tsv"]); B = load(["passB.tsv"])
lines = sorted({r[:-2] for r in A})
agree = tot = 0; pairs = collections.Counter(); where = collections.defaultdict(list)
for ln in lines:
    a = A[ln + "_a"] + A[ln + "_b"]; b = B[ln + "_a"] + B[ln + "_b"]
    sm = difflib.SequenceMatcher(None, a, b, autojunk=False)
    for op, a0, a1, b0, b1 in sm.get_opcodes():
        tot += max(a1 - a0, b1 - b0)
        if op == "equal": agree += a1 - a0
        else:
            k = (" ".join(a[a0:a1]), " ".join(b[b0:b1])); pairs[k] += 1; where[k].append(ln)
print(f"raw agreement {agree}/{tot} = {agree/tot:.3f}")
for k, n in pairs.most_common(): print(n, k, where[k][:4])
