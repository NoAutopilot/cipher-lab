#!/usr/bin/env python3
"""VIV-105: write tx/plain_f105_rec.txt, the reconciled clerk's copy f.105r-f.105v with per-line reader agreement.
f.105r: base text = VIV-T's read (tx/plain_c110_f105r.txt, checked against strips S01-S03 by the reconciler and found the
stronger read); per-line agreement = share of its words matched by the blind reader B (tx/plain_c110_f105r_B.txt).
f.105v: base text = the reconciler's settlement (v105/rec_f105v.tsv, made by eye from strips S01-S09 with readers A and B
side by side); per-line agreement = A vs B on reader B's line (B's numbering, 35 lines; A has 33).
All agreement is word-level after --expand normalization (v105/agree.py). Grade I throughout (a transcription, not a reading).
Usage: python3 v105/build_rec.py [--check]"""
import subprocess, sys
def per_line(a, b):
    out = subprocess.run([sys.executable, "v105/agree.py", a, b, "--label", "x", "--expand"], capture_output=True, text=True).stdout
    rows = [l.split("\t") for l in out.splitlines()[2:]]
    return [(r[1], r[2], r[3]) for r in rows], out.splitlines()[0].split("\t")
def load(path):
    from importlib.machinery import SourceFileLoader
    return [l.rstrip("\n") for l in open(path, encoding="utf-8") if l.strip() and not l.startswith("#")]
L = ["# Clerk's copy of the 2 Mar 1580 letter (fr.16107 f.105r-f.105v), reconciled by VIV-105, 13 Oct 2026. Grade I throughout.",
     "# Conventions: tx/CONVENTIONS_f105.md. {?} illegible word, [word?] doubtful. Columns: line, agree (matched/words, share), text.",
     "# agree = word-level agreement of the two independent reads on that line (v105/agree.py --expand); low agreement = unsettled line."]
pr, head_r = per_line("tx/plain_c110_f105r.txt", "tx/plain_c110_f105r_B.txt")
base_r = load("tx/plain_c110_f105r.txt")
L.append(f"## f.105r (c110 right): base VIV-T (4 Oct), second read B (VIV-105); page agreement {head_r[-1].split()[-1]}")
for (lid, mn, sh), txt in zip(pr, base_r):
    L.append(f"r{int(lid):02d}\t{mn}\t{sh}\t{txt}")
L.append("r--\t-\t-\tsubscription at foot (both readers): Madame je supplie le Createur ... de Madrid ce [deux]me de Mars 1580 / ... De Vivonne")
pv, head_v = per_line("tx/plain_c110_f105v_B.txt", "tx/plain_c110_f105v_A.txt")
rec = dict(l.split("\t", 1) for l in load("v105/rec_f105v.tsv"))
L.append(f"## f.105v (c111 left): reads A and B (VIV-105), settled by the reconciler; page agreement A-B {head_v[-1].split()[-1]}")
for lid, mn, sh in pv:
    L.append(f"v{lid}\t{mn}\t{sh}\t{rec[lid]}")
text = "\n".join(L) + "\n"
if "--check" in sys.argv:
    ok = open("tx/plain_f105_rec.txt", encoding="utf-8").read() == text
    print("check OK" if ok else "STALE"); sys.exit(0 if ok else 1)
open("tx/plain_f105_rec.txt", "w", encoding="utf-8").write(text); print(f"wrote tx/plain_f105_rec.txt, {len(L)} lines")
