#!/usr/bin/env python3
"""AX-NAMES diagnostic (method bias): mark a random 10% of the numerals 1-120 as FREE codes (the aligner
does not know their letter) and record what they absorb. If the aligner manufactured nulls, many real
letter codes would come out absorbing nothing. Seeds 1-5, pairs 5810/5811/4503/sib."""
import random, sys, os, collections
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import align_names as A
key = A.keymap()
tot = collections.Counter()
for seed in range(1, 6):
    rnd = random.Random(seed)
    for letter, (ct, spans) in A.PAIRS.items():
        pt = "".join(A.letters(A.groen_body(*sp)) for sp in spans)
        toks = []
        for (l, p, s) in A.tokens(ct):
            if s.isdigit() and 1 <= int(s) <= 120 and rnd.random() < 0.10:
                s = str(1000 + int(s))  # FREE: > 120, value hidden
            toks.append((l, p, s))
        pk = (lambda t: t[0].split("_")[0]) if letter == "sib" else (lambda t: t[0].split("_")[1])
        import io, contextlib
        with contextlib.redirect_stderr(io.StringIO()):
            rows = A.run(letter, toks, pt, key, pk)
        for r in rows:
            c = int(r[5])
            if c < 1000:
                continue
            if min(r[7], r[8]) < 3:
                tot["weak anchors"] += 1; continue
            true = A.letters(key[str(c - 1000)])
            ab = r[6]
            tot["own letter" if ab == true or (true in "uv" and ab in ("u", "v")) else ("NULL" if ab == "" else "other")] += 1
n = sum(v for k, v in tot.items() if k != "weak anchors")
for k, v in tot.most_common():
    print(f"{k}\t{v}\t{100*v/n:.1f}%" if k != "weak anchors" else f"{k}\t{v}\t(excluded)")
