#!/usr/bin/env python3
"""Regenerate ciphers/pro3055-clinton-1779/passes/p186_reading.txt from p186_reconciled.tsv (CLAUDE.md rule 7).

    python3 ciphers/pro3055-clinton-1779/passes/build_p186.py            # write the reading and print the token grade counts
    python3 ciphers/pro3055-clinton-1779/passes/build_p186.py --check    # exit 1 if the committed reading is stale

The reading is the period decipherment of HMC 2894 (Clinton to Haldimand, 6 July 1780) as copied on LAC reel H-1649
page 186 (= BL Add MS 21807 fo.161), lines 1-23 of the reconciled TSV; the struck endorsement fragment (line 24) and
the fo.161v endorsement (line 25) are printed after a blank line. Tokens carry grade H (read from the period
decipherment, a key source) unless marked [M] in the TSV.
"""
import csv, os, re, sys
here = os.path.dirname(os.path.abspath(__file__))
rows = list(csv.DictReader(open(os.path.join(here, "p186_reconciled.tsv")), delimiter="\t"))
body = [r["text"] for r in rows if int(r["line"]) <= 23]
tail = [r["text"] for r in rows if int(r["line"]) > 23]
text = "\n".join(body) + "\n\n" + "\n".join(tail) + "\n"
toks = re.findall(r"\S+", "\n".join(body))
m = sum(1 for t in toks if "[M]" in t)
summary = f"tokens {len(toks)}: H {len(toks)-m}, M {m}, C 0, S 0, I 0"
out = os.path.join(here, "p186_reading.txt")
if "--check" in sys.argv:
    cur = open(out).read() if os.path.exists(out) else ""
    if cur != text + "# " + summary + "\n":
        print("STALE: p186_reading.txt differs from p186_reconciled.tsv"); sys.exit(1)
    print("OK", summary); sys.exit(0)
open(out, "w").write(text + "# " + summary + "\n")
print(summary)
