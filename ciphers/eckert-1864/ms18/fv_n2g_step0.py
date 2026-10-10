#!/usr/bin/env python3
"""FV-N2g (LANE LEDGER-12, 10 Oct 2026): Step-0 ruling recomputed for N2-KA, N2-KB, N2-KC with STEP0-RULE's own functions
(ms18/step0_ordered.py, everything above its sweep loop), plus its positive control E74. Disk only. Writes ms18/fv_n2g_step0.out."""
import os
HERE = os.path.dirname(os.path.abspath(__file__))
src = open(os.path.join(HERE, "step0_ordered.py")).read()
g = {"__file__": os.path.join(HERE, "step0_ordered.py")}
exec(src.split("EXTRA = ")[0], g)
out = []
for e in ("E74", "N2-KA", "N2-KB", "N2-KC"):
    p, line = g["ents"][e]; allw, codew = g["body"](line)
    r = g["measure"](e, allw, codew, g["windows"](g["blocks"]([p])), sum(map(ord, e)))
    out.append(f"{e} page {p} window {r['win']}: a={r['a']:.3f} ({r['lcs']}/{r['n']}) b_p95={r['b']:.3f} b2={r['b2']:.3f} "
               f"hit={'YES' if r['hit'] else 'no'} (c)={r['c']} key: {' '.join(r['ck'])} | plain absent: {' '.join(r['cp'])}")
open(os.path.join(HERE, "fv_n2g_step0.out"), "w").write("\n".join(out) + "\n"); print("\n".join(out))
