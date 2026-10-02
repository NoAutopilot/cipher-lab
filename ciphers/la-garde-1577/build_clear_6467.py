#!/usr/bin/env python3
"""A2-LAG (2 Oct 2026): place 6467's clear-text words around cipher run 1, including the margin insertion
"justifier le faict de Gand", as C-grade (known-plaintext: read from the manuscript image and printed in GSME and
LMSAC) rows anchored to ciphertext_6467_v2.tsv, and render the run-1 sentence.

  python3 ciphers/la-garde-1577/build_clear_6467.py [--check]

Reads cleartext_6467.tsv (each row sits immediately before the cipher sign at before_line/before_pos; an anchor one
past a line's last sign means "after that line") and ciphertext_6467_v2.tsv; writes reading_6467_run1.txt.
--check exits 1 if an anchor is missing from v2 or the committed reading is stale (rule 7). The cipher signs stay
unread: they are rendered as their v2 groups in brackets, nothing is decoded.
"""
import csv, os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
def rows(p):
    with open(os.path.join(HERE, p), newline="") as f:
        return list(csv.DictReader(f, delimiter="\t"))
v2 = rows("ciphertext_6467_v2.tsv")
run1 = [r for r in v2 if r["line"] in ("p2L6", "p2L7", "p2L8")]
clear = [r for r in rows("cleartext_6467.tsv") if r["letter"] == "6467"]
keys = [(r["line"], int(r["pos"])) for r in run1]
maxpos = {}
for l, p in keys: maxpos[l] = max(maxpos.get(l, 0), p)
bad = [c for c in clear if (c["before_line"], int(c["before_pos"])) not in keys
       and int(c["before_pos"]) != maxpos.get(c["before_line"], -9) + 1]
out, i = [], 0
def emit(anchor):
    for c in clear:
        if (c["before_line"], int(c["before_pos"])) == anchor:
            out.append(("[%s] " % c["text"]) if c["kind"] == "margin-insertion" else c["text"] + " ")
for l, p in keys:
    emit((l, p)); out.append("<%s> " % next(r["group"] for r in run1 if (r["line"], int(r["pos"])) == (l, p)))
emit(("p2L8", maxpos["p2L8"] + 1))
grades = {}
for c in clear: grades[c["grade"]] = grades.get(c["grade"], 0) + len(c["text"].split())
text = ("".join(out).strip() + "\n\nclear words by grade: " + ", ".join("%s %d" % kv for kv in sorted(grades.items()))
        + "; cipher signs in <>: %d, unread (no key)\n[] = left-margin insertion\n" % len(run1))
target = os.path.join(HERE, "reading_6467_run1.txt")
if bad:
    print("anchor not in ciphertext_6467_v2.tsv:", [(c["before_line"], c["before_pos"]) for c in bad]); sys.exit(1)
if "--check" in sys.argv:
    cur = open(target).read() if os.path.exists(target) else ""
    if cur != text: print("STALE: reading_6467_run1.txt"); sys.exit(1)
    print("ok: reading_6467_run1.txt current"); sys.exit(0)
open(target, "w").write(text); print(text)
