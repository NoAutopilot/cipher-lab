#!/usr/bin/env python3
"""MONL-KING3: turn pass answer text (LINE Lnn: tokens / SKIPPED_OVERLAP / UNSURE) into passX.txt ('Lnn: tokens') and passX.tsv."""
import re, sys
src, stem = sys.argv[1], sys.argv[2]
rows, txt = ["line\tpos\tsign"], []
for ln in open(src):
    m = re.match(r"\s*LINE\s+(L\d\d):\s*(.*)", ln)
    if m:
        body = re.sub(r'\?x\[[^\]]*\]', lambda x: x.group(0).replace(' ', '_').replace(',', ''), m.group(2)); toks = body.split(); txt.append(f"{m.group(1)}: {' '.join(toks)}")
        rows += [f"{m.group(1)}\t{i}\t{t}" for i, t in enumerate(toks, 1)]
open(stem + ".txt", "w").write("\n".join(txt) + "\n"); open(stem + ".tsv", "w").write("\n".join(rows) + "\n")
print(stem, len(txt), "lines", len(rows) - 1, "tokens")
