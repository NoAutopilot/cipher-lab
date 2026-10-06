#!/usr/bin/env python3
"""R12D-GRAZB2: token list per half-line image for every r12zb/occ.tsv row (same sources as r12zb/occ.py). Writes r12zb2/halves.tsv:
image, n tokens, the tokens in order. python3 r12zb2/ntok.py"""
import sys
from pathlib import Path
if "--help" in sys.argv: print(__doc__); sys.exit()
H = Path(__file__).resolve().parent; T = H.parent
def half_rows(f):
    d = {}
    for l in Path(f).read_text().splitlines()[1:]:
        r, c = l.split("\t"); d[r] = [t for t in c.split() if t not in ("/", ".")]
    return d
def recon(f): return [(l.split("\t")[0], l.split("\t")[1].split()) for l in Path(f).read_text().splitlines()[1:]]
halves = {}
pa2 = half_rows(T / "n8gra2/passA.tsv")
for ln, tt in recon(T / "n8gra2/recon.tsv"):
    if ln + "_s1" not in pa2: continue
    n1 = len(pa2[ln + "_s1"])
    halves[f"images/fr3040_f18/{ln}_s1.jpg"] = tt[:n1]; halves[f"images/fr3040_f18/{ln}_s2.jpg"] = tt[n1:]
pa3 = {}; pa3.update(half_rows(T / "n8gra3/passA_u1.tsv")); pa3.update(half_rows(T / "n8gra3/passA_u2.tsv"))
for ln, tt in recon(T / "n8gra3/recon.tsv"):
    if ln + "_a" not in pa3: continue
    na = len(pa3[ln + "_a"])
    halves[f"images/fr3040_f18/{ln}_a.jpg"] = tt[:na]; halves[f"images/fr3040_f18/{ln}_b.jpg"] = tt[na:]
pr = half_rows(T / "passR_f30.tsv"); f30 = {}
for l in (T / "ciphertext_f30.tsv").read_text().splitlines()[1:]:
    line, pos, s, cf = l.split("\t"); f30.setdefault(line, {})[int(pos)] = s
for line, d in f30.items():
    toks = [d[i] for i in sorted(d)]; na = len(pr[line + "a"])
    halves[f"images/crops_f30/{line}a.jpg"] = toks[:na]; halves[f"images/crops_f30/{line}b.jpg"] = toks[na:]
need = {l.split("\t")[4] for l in (T / "r12zb/occ.tsv").read_text().splitlines()[1:]}
(H / "halves.tsv").write_text("image\tn\ttokens\n" + "".join(f"{k}\t{len(halves[k])}\t{' '.join(halves[k])}\n" for k in sorted(halves)))
print(len(need), "halves")
