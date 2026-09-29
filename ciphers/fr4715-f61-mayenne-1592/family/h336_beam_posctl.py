#!/usr/bin/env python3
"""H336 (runner 13 session_01MSoJWwZxNPSjQd4hszNdvQ, 29 Sept 2026), script-only, written before running: positive control for H335's design. H335's
code unchanged (exec of h335_106r_v7_beam.py) on a leaf whose period gloss key v7 was built from -- in-sample, so the design must pass here for
H335's miss to mean anything: fr.3982 f.101r (passes/recf101r/ciphertext_draft.tsv) and fr.3984 f.188r (passes/recf188r). Pre-stated: the design
is a test iff it reads 'consistent' (real > binned p95 AND real > frequency key) on both in-sample leaves; if not, H335 is a non-test of v7 on
f.106r (the control cannot pass), not a negative.   python3 h336_beam_posctl.py [--check]"""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__)); ARGS = sys.argv[1:]; out = []
src = open(f"{HERE}/h335_106r_v7_beam.py").read(); src = src[:src.index('txt = "\\n".join(out)')]
for pre in ("f101r", "f188r"):
    g = {"__file__": f"{HERE}/h335_106r_v7_beam.py", "__name__": "h336"}; sys.argv = [sys.argv[0]]
    exec(compile(src.replace("recf106rall/", f"rec{pre}/"), f"h335_on_{pre}", "exec"), g)
    out.append(f"{pre} (in-sample):"); out += ["  " + l for l in g["out"]]
txt = "\n".join(out) + "\n"; res = f"{HERE}/h336_beam_posctl_result.txt"
if "--check" in ARGS:
    ok = os.path.exists(res) and open(res).read() == txt; print("check", "OK" if ok else "STALE"); sys.exit(0 if ok else 1)
open(res, "w").write(txt); print(txt, end="")
