#!/usr/bin/env python3
"""H338-H340 (runner 13 session_01MSoJWwZxNPSjQd4hszNdvQ, 29 Sept 2026), script-only, written before running: H335's gloss-free beam check of key v7
on the three family leaves on disk that v7 was NOT built from (key_period_v7.tsv's leaf column: f.101r, f.188r/f.184r, f.274r, f.176r/f.177r, f.61r
only): H338 fr.3982 f.124r (de Diou's letter, passes/recf124r, 2839 draft rows), H339 fr.3982 f.97r (recf97r, 2485), H340 fr.3983 f.108v (f.61's own
hand; two drafts, rec108v 308 and recf108vg 293). H335's code unchanged (runs >= 4 keyed signs, fr16 4-gram beam, log10/letter, 200 binned keys,
seed 3350). Gate (pre-stated): the binned arm only -- 'consistent with key v7 on a held leaf' iff real > binned p95 -- since H336 showed the
frequency-key arm fails in-sample for beam scores (it is still printed). For f.108v (under 35 runs) the in-sample power at its own run count is also
computed as H337 does (f.101r and f.188r, 50 subsets, seed 338); a miss there is a negative only if that power is >= 0.8.
python3 h338_beam_held.py [--check]"""
import os, random, sys
HERE = os.path.dirname(os.path.abspath(__file__)); ARGS = sys.argv[1:]; out = []
src = open(f"{HERE}/h335_106r_v7_beam.py").read()
full = src[:src.index('txt = "\\n".join(out)')]; pre_only = src[:src.index("real = score(cell)")]
def run(prefix, code):
    g = {"__file__": f"{HERE}/h335_106r_v7_beam.py", "__name__": "h338"}; sys.argv = [sys.argv[0]]
    exec(compile(code.replace("recf106rall/", f"{prefix}/"), f"h335_on_{prefix}", "exec"), g); return g
res_small = {}
for hid, prefix in (("H338", "recf124r"), ("H339", "recf97r"), ("H340", "rec108v"), ("H340", "recf108vg")):
    g = run(prefix, full); nb = g["null"]; ok = g["real"] > g["p95"]
    out.append(f"{hid} {prefix}: {g['out'][0]}"); out.append(f"  {g['out'][1]}")
    out.append(f"  read-out (binned arm): {'consistent with key v7 on a held leaf' if ok else 'no signal beyond the binned keys'}")
    if hid == "H340": res_small[prefix] = (len(g["runs"]), ok)
for prefix, (nr, ok) in res_small.items():
    pw = []
    for pre in ("recf101r", "recf188r"):
        g = run(pre, pre_only); allruns, cell, classes = g["runs"], g["cell"], g["classes"]; bins = [classes[i:i + 3] for i in range(0, len(classes), 3)]
        rng = random.Random(338); wins = 0
        for _ in range(50):
            g["runs"] = rng.sample(allruns, nr); real = g["score"](cell); null = []
            for _ in range(100):
                mp = {}
                for bn in bins:
                    cs = [frozenset(cell(c)) for c in bn]; rng.shuffle(cs); mp.update(zip(bn, cs))
                null.append(g["score"](lambda c, mp=mp: set(mp.get(c, ()))))
            null.sort(); wins += real > null[94]
        pw.append(wins / 50)
    out.append(f"H340 {prefix} power at {nr} runs (in-sample f.101r, f.188r): {pw[0]:.2f}, {pw[1]:.2f} -> " +
               ("pass" if ok else "a negative at this N" if min(pw) >= 0.8 else "underpowered: a miss is untestable at this N, not a negative"))
txt = "\n".join(out) + "\n"; res = f"{HERE}/h338_beam_held_result.txt"
if "--check" in ARGS:
    ok = os.path.exists(res) and open(res).read() == txt; print("check", "OK" if ok else "STALE"); sys.exit(0 if ok else 1)
open(res, "w").write(txt); print(txt, end="")
