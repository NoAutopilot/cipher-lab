#!/usr/bin/env python3
"""doubled_runs.py PASSFILE... -- per pass file, the lines in which some run of 3 consecutive tokens ('?' stripped, normalised by
test2.load_pass) occurs twice: the join-doubling detector of RUN5-ES50B, as a script (RUN5-ES51, 4 Oct 2026)."""
import sys
from pathlib import Path
HERE = Path(__file__).resolve().parents[1]; sys.path.insert(0, str(HERE))
from test2 import load_pass
for f in sys.argv[1:]:
    P = load_pass(Path(f)); hit = []
    for ln, ts in sorted(P.items()):
        t = [x.rstrip('?') for x in ts]
        g = [tuple(t[i:i + 3]) for i in range(len(t) - 2)]
        if len(g) != len(set(g)): hit.append(ln)
    print(f'{f}\t{len(hit)}/{len(P)} lines\t{" ".join(hit)}')
