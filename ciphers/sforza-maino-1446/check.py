#!/usr/bin/env python3
"""Regenerate best_reading.txt from ciphertext.txt, ciphertext_f70.txt, key.tsv and signs_mapB.tsv, and
exit non-zero if the committed file is stale (CLAUDE.md rule 7). 23 Sept 2026.

best_reading.txt is the decode of the best-scoring key of a closed-negative campaign, not a claimed
reading: no token of it is graded above unread (see NOTES.md "Grading").
Usage: python3 check.py [--write]
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "..", "tools"))
import nomenclator_anneal as na  # noqa: E402

files = [os.path.join(HERE, f) for f in ("ciphertext.txt", "ciphertext_f70.txt")]
key = na.read_key(os.path.join(HERE, "key.tsv"))
out = "".join(f"{name}: {txt}\n" for name, txt in na.decode_texts(files, key, os.path.join(HERE, "signs_mapB.tsv")))
header = "# NOT A READING. Decode of key.tsv (best-scoring key, run T-joint-mapB); regenerate with check.py --write\n"
path = os.path.join(HERE, "best_reading.txt")
if "--write" in sys.argv:
    open(path, "w").write(header + out)
    print("written", path)
    sys.exit(0)
cur = open(path).read() if os.path.exists(path) else ""
if cur != header + out:
    print("STALE: best_reading.txt does not match ciphertext + key.tsv", file=sys.stderr)
    sys.exit(1)
print("ok: best_reading.txt reproduces from ciphertext.txt, ciphertext_f70.txt, key.tsv")
