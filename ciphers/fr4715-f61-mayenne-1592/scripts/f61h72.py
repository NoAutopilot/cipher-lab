#!/usr/bin/env python3
"""F61-4TRI-ON-61 (campaign step H72, 28 Sept 2026, runner session_01NQpd6L9ZvLvjU1L7ttFmZs), script-only: after H69 put the
period c/p cell under the 4-over-triangle and a/n under 4-with-hook forms on the family leaves, tally Tomokiyo's letter
under every 4-shaped class our f.61/f.108r readers coded (the f61qo expected() machinery: joint cell map DP on his spans).
  python3 scripts/f61h72.py [--check]      -> scripts/f61h72_result.txt
"""
import os, sys
from collections import Counter
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import f61qo
f61qo.CLS = ("4TRI", "4STEM", "C43", "4PI", "HASH4")
c = Counter((x[2], x[3]) for x in f61qo.expected())
lines = [f"{k[0]}\t{k[1]}\t{v}" for k, v in sorted(c.items())]
tri, an = Counter(), Counter()
for (k, l), v in c.items():
    if k == "4TRI": tri[l] += v
    if k in ("C43", "4STEM"): an[l] += v
tri, an = dict(tri), dict(an)
lines.append(f"4TRI under Tomokiyo letters: {tri} -- c/p {tri.get('c', 0) + tri.get('p', 0)} of {sum(v for l, v in tri.items() if l != '-')} lettered")
lines.append(f"C43+4STEM: {an} -- a/n {an.get('a', 0) + an.get('n', 0)} of {sum(v for l, v in an.items() if l != '-')} lettered")
txt = "class\tletter\tn\n" + "\n".join(lines) + "\n"; res = f"{HERE}/f61h72_result.txt"
if "--check" in sys.argv:
    ok = os.path.exists(res) and open(res).read() == txt; print("check", "OK" if ok else "STALE"); sys.exit(0 if ok else 1)
open(res, "w").write(txt); print(txt)
