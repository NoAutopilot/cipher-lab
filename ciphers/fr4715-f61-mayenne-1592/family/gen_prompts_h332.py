#!/usr/bin/env python3
"""H332 (runner 13 session_01MSoJWwZxNPSjQd4hszNdvQ, 29 Sept 2026), written before any call: the four f.106r prompts of F61-FAMILY-3
(passes/prompts_f3/f106_{signs,gloss}{A,B}.txt, templates in passes/PROMPTS_f188_f184_f106.md) re-targeted, text otherwise unchanged, at
cipher rows 7-12 of the leaf (bands L07..L12, cut by cut_bands.py into sheets/f106r_b with the same geometry: 520 native px segments,
60 px overlap, up 78 / down 42, x3 -> 1560 x 360 px, 7 segments per band; hand-set centres from an eye-marked strip, --local 18 --slope -0.028).
Outputs passes/prompts_h332/f106_{signs,gloss}{A,B}_c2.txt; each call writes passes/f106r_{signs,gloss}{A,B}_c2.tsv. Four blind Opus calls,
no key, no letters, no other pass's output.   python3 gen_prompts_h332.py"""
import os
HERE = os.path.dirname(os.path.abspath(__file__)); P = f"{HERE}/passes"; os.makedirs(f"{P}/prompts_h332", exist_ok=True)
old = [f"{HERE}/sheets/f106r/f106r_L{b:02d}_s{s}.jpg" for b in range(1, 7) for s in range(1, 8)]
new = [f"{HERE}/sheets/f106r_b/f106r_L{b:02d}_s{s}.jpg" for b in range(7, 13) for s in range(1, 8)]
for kind in ("signs", "gloss"):
    for pas in "AB":
        t = open(f"{P}/prompts_f3/f106_{kind}{pas}.txt").read()
        t = t.replace("\n".join(old), "\n".join(new)).replace("the first six cipher rows of the leaf", "cipher rows 7 to 12 of the leaf")
        t = t.replace("L01..L06", "L07..L12").replace(f"passes/f106r_{kind}{pas}.tsv", f"passes/f106r_{kind}{pas}_c2.tsv")
        assert "sheets/f106r/" not in t and "L01" not in t and all(os.path.exists(p) for p in new)
        open(f"{P}/prompts_h332/f106_{kind}{pas}_c2.txt", "w").write(t)
print("written", sorted(os.listdir(f"{P}/prompts_h332")))
