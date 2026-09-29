#!/usr/bin/env python3
"""H348 (runner 13 session_01MSoJWwZxNPSjQd4hszNdvQ, 29 Sept 2026), written before any call: H332's two f.106r SIGN prompts (passes/prompts_h332/
f106_signs{A,B}_c2.txt) re-targeted, text otherwise unchanged, at cipher rows 13-18 (bands L13..L18, sheets/f106r_b, same geometry; centring checked
by eye). No gloss passes (retired for this hand, H332). Outputs passes/prompts_h348/f106_signs{A,B}_c3.txt; each call writes passes/f106r_signs{A,B}_c3.tsv.
python3 gen_prompts_h348.py"""
import os
HERE = os.path.dirname(os.path.abspath(__file__)); P = f"{HERE}/passes"; os.makedirs(f"{P}/prompts_h348", exist_ok=True)
old = [f"{HERE}/sheets/f106r_b/f106r_L{b:02d}_s{s}.jpg" for b in range(7, 13) for s in range(1, 8)]
new = [f"{HERE}/sheets/f106r_b/f106r_L{b:02d}_s{s}.jpg" for b in range(13, 19) for s in range(1, 8)]
for pas in "AB":
    t = open(f"{P}/prompts_h332/f106_signs{pas}_c2.txt").read()
    t = t.replace("\n".join(old), "\n".join(new)).replace("cipher rows 7 to 12 of the leaf", "cipher rows 13 to 18 of the leaf")
    t = t.replace("L07..L12", "L13..L18").replace(f"passes/f106r_signs{pas}_c2.tsv", f"passes/f106r_signs{pas}_c3.tsv")
    assert "L07" not in t and "_c2" not in t and all(os.path.exists(p) for p in new)
    open(f"{P}/prompts_h348/f106_signs{pas}_c3.txt", "w").write(t)
print("written", sorted(os.listdir(f"{P}/prompts_h348")))
