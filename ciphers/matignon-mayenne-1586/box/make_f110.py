#!/usr/bin/env python3
"""MAT-BOX (15 Oct 2026): build an f.110-only copy of this target for decode_key.py --try (scope A of PREREG-MAT-BOX).
Copies decode.json and key.tsv unchanged and keeps only the f110-* lines of ciphertext.txt.
Usage: python3 ciphers/matignon-mayenne-1586/box/make_f110.py OUTDIR"""
import shutil, sys
from pathlib import Path
here = Path(__file__).resolve().parent.parent
out = Path(sys.argv[1]); out.mkdir(parents=True, exist_ok=True)
for f in ("decode.json", "key.tsv"):
    shutil.copy(here / f, out / f)
lines = [l for l in open(here / "ciphertext.txt") if l.startswith("f110-")]
open(out / "ciphertext.txt", "w").writelines(lines)
print(len(lines), "f.110 lines ->", out)
