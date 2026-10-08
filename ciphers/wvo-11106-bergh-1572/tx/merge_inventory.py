#!/usr/bin/env python3
"""Merged-inventory variant for FAM-11106L (PREREG-FAM-11106L.md item 5): dd->d, yx->y, S->s.
python3 merge_inventory.py [--check]  -- writes tx/ciphertext_oneline_merged.txt from tx/ciphertext_oneline.txt."""
import os, sys
D = os.path.dirname(os.path.abspath(__file__))
MERGE = {"dd": "d", "yx": "y", "S": "s"}
toks = open(os.path.join(D, "ciphertext_oneline.txt")).read().split()
out = " ".join(MERGE.get(t, t) for t in toks) + "\n"
p = os.path.join(D, "ciphertext_oneline_merged.txt")
if "--check" in sys.argv:
    sys.exit(0 if os.path.exists(p) and open(p).read() == out else 1)
open(p, "w").write(out)
print(f"N={len(toks)} K={len(set(toks))} -> K={len(set(out.split()))}")
