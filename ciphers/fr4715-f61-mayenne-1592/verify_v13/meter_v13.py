#!/usr/bin/env python3
"""VERIFY-F61-V13 (29 Sept 2026): span count and meter (verify_v8/meter_v8 bands, key v8, verify_v12/meter_v12's own meter and span
functions, unchanged) for (c) V12's endorsed state; (c') the state this verifier endorses = (c) + none of the three held signs (score_result:
all three hold); and, for comparison only, runner 16's H432 proposal = (c) + L11/8 CROSS + L02 opening LL.  python3 meter_v13.py [--check]"""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__)); CHECK = "--check" in sys.argv; sys.argv = sys.argv[:1]
sys.path.insert(0, f"{HERE}/../verify_v12"); import meter_v12 as m
m.LET["CROSS"] = "-"
V13 = list(m.MINE); RUNNER16 = m.MINE + [("L11", "8", "relabel", "CROSS"), ("L02", "0", "insert", "LL")]
out = [f"{tag}: spans {m.spans(c)}; meter {m.meter(c)}" for tag, c in (("(c') V13 endorsed = V12 (c); none of L11/8, L01/11, L02 LL added", V13),
       ("runner 16 H432 proposal = (c) + L11/8 CROSS + L02 LL (comparison, not endorsed)", RUNNER16))]
txt = "\n".join(out) + "\n"; p = f"{HERE}/meter_v13_result.txt"
if CHECK: ok = os.path.exists(p) and open(p).read() == txt; print("check", "OK" if ok else "STALE"); sys.exit(0 if ok else 1)
open(p, "w").write(txt); print(txt, end="")
