#!/usr/bin/env python3
"""judge_input.py: letters-only judge input from reading_1646.txt (SPEC-FR17, 3 Oct 2026).

Writes judge_1646.txt: the header lines and the 'f226v_C01 |' labels are dropped; the brackets that mark one
key group's multi-letter value ('[que]') are removed and their letters kept, since every group here is cipher.
Also writes judge_gloss_1646.txt, the leaf's interlinear decipherment (dechiffre.tsv), as the rule-3 gloss control.
--check exits 1 if a committed judge_*.txt differs from what reading_1646.txt regenerates.
"""
import sys
from pathlib import Path
HERE = Path(__file__).resolve().parent

def extract():
    out = [l.split("|", 1)[1].replace("[", "").replace("]", "").strip()
           for l in (HERE / "reading_1646.txt").read_text(encoding="utf-8").splitlines() if " | " in l]
    return "\n".join(x for x in out if x) + "\n"

def gloss():  # the leaf's own interlinear decipherment (dechiffre.tsv 'words'), the rule-3 period-gloss control
    rows = (HERE / "dechiffre.tsv").read_text(encoding="utf-8").splitlines()[1:]
    return "\n".join(r.split("\t")[1] for r in rows if r.strip()) + "\n"

stale = 0
for name, text in (("judge_1646.txt", extract()), ("judge_gloss_1646.txt", gloss())):
    p = HERE / name
    if "--check" in sys.argv:
        ok = p.exists() and p.read_text(encoding="utf-8") == text
        print(("ok " if ok else "STALE ") + name); stale |= not ok
    else:
        p.write_text(text, encoding="utf-8"); print(f"wrote {name}: {sum(c.isalpha() for c in text)} letters")
sys.exit(1 if stale else 0)
