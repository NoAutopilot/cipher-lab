#!/usr/bin/env python3
"""N8-NV05B: gloss_b2_diplomatic.tsv (reconciled GA/GB read of f.228 L05-L08) -> gloss_b2.tsv.

  python3 build_gloss_b2.py [--check]

The fixed rule of PREREG-ADDENDUM-N8.md, imported unchanged from build_gloss_v2.py (clean()). --check exits 1 if
gloss_b2.tsv is stale (rule 7).
"""
import csv, os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from build_gloss_v2 import clean  # noqa: E402

if __name__ == "__main__":
    out = ["line\ttext"]
    with open(os.path.join(HERE, "gloss_b2_diplomatic.tsv"), encoding="utf-8") as f:
        for r in csv.DictReader(f, delimiter="\t"):
            out.append(f"{r['line']}\t{clean(r['text'])}")
    txt, p = "\n".join(out) + "\n", os.path.join(HERE, "gloss_b2.tsv")
    if "--check" in sys.argv:
        ok = os.path.exists(p) and open(p, encoding="utf-8").read() == txt
        print("gloss_b2.tsv up to date" if ok else "gloss_b2.tsv is stale"); sys.exit(0 if ok else 1)
    open(p, "w", encoding="utf-8").write(txt); print(txt, end="")
