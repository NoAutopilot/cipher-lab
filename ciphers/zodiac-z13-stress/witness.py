#!/usr/bin/env python3
"""Print one concrete rule set (Params + per-letter ops) that turns the unchanged Z13 into each named label."""
import itertools, sys
from mechanism import run, load
from enumerate import options, dp, grid, OPS
from namecheck import names_in

z = load()
LP = [k for k, t in enumerate(z, 1) if t.isalpha()]
for want in sys.argv[1:]:
    mode = "name7" if "+" in want else "name6"
    for p in grid():
        if want not in dp(options(z, p), mode)[2]:
            continue
        for combo in itertools.product(OPS, repeat=len(LP)):
            ops = dict(zip(LP, combo))
            o = run(z, p, ops)
            if o and want in names_in(o, mode):
                print(f"{want}\t{o}\t{p}\t{''.join(f'{k}:{v} ' for k, v in ops.items()).strip()}")
                break
        break
