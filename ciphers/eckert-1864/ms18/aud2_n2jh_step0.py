#!/usr/bin/env python3
"""AUD2-LEDGER10-3 (second audit of N2-JH, 10 Oct 2026): the Wave 3 Step-0 ruling re-measured on the CURRENT reading-no2.md
(after FIX-FM21 made 'business' and 'George' plain), reusing ms18/step0_ordered.py's own functions (lines 1-105, exec'd so its
TSV is not rewritten). Also reports the FV-N2f-era figure by restoring the two pre-fix code tokens, and a 200-draw shuffle p95.
Disk only."""
import os, random
HERE = os.path.dirname(os.path.abspath(__file__))
src = open(os.path.join(HERE, "step0_ordered.py")).read().split("\n")
g = {"__file__": os.path.join(HERE, "step0_ordered.py")}
exec("\n".join(src[:105]), g)
p, line = g["ents"]["N2-JH"]
assert p == 9780
for label, ln in (("current (post FIX-FM21)", line),
                  ("pre-fix (FV-N2f era)", line.replace("pressure of business", "pressure of [Browns Ferry]").replace("and George Town", "and [McCallum D C] Town"))):
    allw, codew = g["body"](ln)
    wins = g["windows"](g["blocks"]([p]))
    r = g["measure"]("N2-JH", allw, codew, wins, 0)
    rnd = random.Random(1); w = dict(wins)[r["win"]]; ctl = []
    for _ in range(200):
        s = w[:]; rnd.shuffle(s); ctl.append(g["lcs"](allw, s)/len(allw))
    print(f"{label}: window {r['win']} (a) {r['a']:.3f} ({r['lcs']}/{r['n']}) (b) p95/20 {r['b']:.3f} b2 {r['b2']:.3f} "
          f"p95/200 {sorted(ctl)[189]:.3f} max/200 {max(ctl):.3f} hit {r['hit']}")
    print(f"   (c) {r['c']} absent; key meanings among them: {' '.join(r['ck'])}; plain/spelling: {' '.join(r['cp'])}")
