#!/usr/bin/env python3
"""H341 (runner 13 session_01MSoJWwZxNPSjQd4hszNdvQ, 29 Sept 2026), script-only, written before running: the order control for H335/H338-H340's
binned beam arm (rule 3's ARM-C1 lesson: score the family's decode of the SHUFFLED target through the same gate). The binned keys permute cells only
among classes of similar frequency, so v7 could beat them by matching letter frequency to sign frequency regardless of order. For each leaf
(recf106rall, recf124r, recf97r, rec108v, recf108vg, and in-sample recf101r, recf188r) the draft rows' signs are shuffled within the leaf (line and
position kept, 5 shuffles, seeds 3410..3414), H335's code then runs unchanged (runs, beam, 200 binned keys). Pre-stated: the binned arm is voided as
a gate for this family at this N if v7 still beats its binned p95 on shuffled order in >= 2 of 5 shuffles of a leaf; if it beats it in at most 1 of 5
on every leaf, the real-order passes (H338-H340) rest on sequence, not frequency alone.   python3 h341_beam_shuffled.py [--check]"""
import os, random, sys
HERE = os.path.dirname(os.path.abspath(__file__)); ARGS = sys.argv[1:]; out = []
src = open(f"{HERE}/h335_106r_v7_beam.py").read(); src = src[:src.index('txt = "\\n".join(out)')]
inj = 'rows = rd(f"{P}/recf106rall/ciphertext_draft.tsv")'
assert inj in src
voided = []
for prefix in ("recf106rall", "recf124r", "recf97r", "rec108v", "recf108vg", "recf101r", "recf188r"):
    wins = []; reals = []
    for seed in range(3410, 3415):
        code = src.replace(inj, inj.replace("recf106rall/", f"{prefix}/") + f"\n_sg = [r['sign'] for r in rows]; __import__('random').Random({seed}).shuffle(_sg)\nfor _r, _s in zip(rows, _sg): _r['sign'] = _s")
        g = {"__file__": f"{HERE}/h335_106r_v7_beam.py", "__name__": "h341"}; sys.argv = [sys.argv[0]]
        exec(compile(code, f"h335_shuf_{prefix}_{seed}", "exec"), g)
        wins.append(g["real"] > g["p95"]); reals.append(f"{g['real']:.3f}/{g['p95']:.3f}")
    k = sum(wins); voided += [prefix] if k >= 2 else []
    out.append(f"{prefix}: shuffled order, v7 > binned p95 in {k}/5 (real/p95: {' '.join(reals)})")
out.append("read-out: " + (f"binned beam arm VOIDED as a gate at this N on {' '.join(voided)} (v7 wins on shuffled order: frequency, not sequence)" if voided else "binned beam arm holds: v7 beats it on shuffled order in at most 1/5 on every leaf"))
txt = "\n".join(out) + "\n"; res = f"{HERE}/h341_beam_shuffled_result.txt"
if "--check" in ARGS:
    ok = os.path.exists(res) and open(res).read() == txt; print("check", "OK" if ok else "STALE"); sys.exit(0 if ok else 1)
open(res, "w").write(txt); print(txt, end="")
