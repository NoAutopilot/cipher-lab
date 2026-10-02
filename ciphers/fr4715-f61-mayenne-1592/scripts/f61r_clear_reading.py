#!/usr/bin/env python3
"""A2-F61R (2 Oct 2026): f.61r clear text, reconciled from two blind passes + one reconciliation.

  python3 scripts/f61r_clear_reading.py [--check]

Grades per word (CLAUDE.md rule 4, for the clear hand, not cipher): H both blind passes read it identically
(after the scorer's normalisation); M settled by the reconciliation at medium/high confidence; I settled at low
confidence or illegible. [#] = a cipher run (not graded here). Writes scripts/f61r_clear_reading.tsv;
--check exits 1 if the committed file differs.
"""
import sys, os
# VERIFY-F61R (2 Oct 2026) corrections, logged in scripts/f61r_clear_corrections.tsv: L11 sou/I -> soit/M, peu/I -> peu/M;
# L04 stop after the cipher run restored (punctuation, not counted). Diplomatic letterforms kept; normalised forms in that log.
# (word, grade) per line; words not in RECON are H (identical in passes A and B, scripts/f61r_clear_passA/B.tsv)
L = {
 "01": "N?us/I auons parlé familieremē/M et amplemē/M de toutes choses [#]",
 "02": "[#] particulieremē/M sur les plus Importances Il seroit trop long vous en dire les",
 "03": "propos Et Combiey/M a/I [#] a/I les/M entendud/M Et pleay/I de",
 "04": "generosité pour beaucoup desiree/M [#] . Mais on auoit Come Je le croys aussy/M que les",
 "05": "choses sont a/I [#] ./M Et que si nous mesmes ey/M",
 "06": "en conoyssant le fruit ey/M fesions la premiere pointe On ne desfieroit/I point du reste .",
 "07": "Cependant/M on n'ose enuoyer depard/M della pour ni mesr'/I a/I [#]",
 "08": "[#] maintenant qu'oy en a affere Vous/M estes",
 "09": "sur les lieux vous verres s'il s'ey/M presentoit les occasions Et s'il s'ey/M pouuoit",
 "10": "prendre quelqu'vne Je ne seroys pas paresseux si [#]",
 "11": "[#] tant soit/M peu/M .",
}
rows, n = ["line\tword\tgrade"], {"H": 0, "M": 0, "I": 0}
for ln, text in L.items():
    for tok in text.split():
        if tok in ("[#]", "."):
            continue
        w, g = (tok.rsplit("/", 1) + ["H"])[:2] if "/" in tok else (tok, "H")
        if w == ".":
            continue
        n[g] += 1
        rows.append(f"{ln}\t{w}\t{g}")
out = "\n".join(rows) + "\n" + f"# totals H {n['H']} M {n['M']} I {n['I']}\n"
here = os.path.dirname(os.path.abspath(__file__))
p = os.path.join(here, "f61r_clear_reading.tsv")
if "--check" in sys.argv:
    ok = os.path.exists(p) and open(p).read() == out
    print("OK" if ok else "STALE"); sys.exit(0 if ok else 1)
open(p, "w").write(out)
print(out.splitlines()[-1])
