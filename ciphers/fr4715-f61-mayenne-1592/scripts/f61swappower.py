#!/usr/bin/env python3
"""F61-SWAP-POWER (campaign step H105, 28 Sept 2026, runner session_01NQpd6L9ZvLvjU1L7ttFmZs), script-only: for each one-swap
map of H100 (f.108v) and H102 (known lines), the number of rendered pair positions the swap changes (positions whose class
is one of the two swapped classes). A swap that changes a handful of positions can hardly score differently from the
fitted map (rule 3: a control that cannot vary). -> scripts/f61swappower_result.txt [--check]"""
import json, os, sys
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import f61judge108v as J
out = []
for tag in ("known_h51_swaps105", "f108v_swaps105"):
    k = json.load(open(f"{HERE}/f61judge_{tag}_key.json")); m = k["maps"]; C = m[0]
    L = J.lines("known_h51" if tag.startswith("known") else "f108v"); seq = [c for v in L.values() for c in v if c in C]
    res = sorted((sum(1 for c in seq if c in sw), lab, "+".join(sw)) for lab, i in k["key"].items() if i
                 for sw in [[c for c in C if m[i][c] != C[c]]])
    out.append(f"{tag}: {len(seq)} pair positions; changed per swap: " + ", ".join(f"{sw} {n} ({lab})" for n, lab, sw in res))
txt = "\n".join(out) + "\n"; res = f"{HERE}/f61swappower_result.txt"
if "--check" in sys.argv:
    ok = os.path.exists(res) and open(res).read() == txt; print("fresh" if ok else "STALE"); sys.exit(0 if ok else 1)
open(res, "w").write(txt); print(txt, end="")
