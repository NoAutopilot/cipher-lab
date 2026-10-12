#!/usr/bin/env python3
"""THUR-94 (12 Oct 2026): Birch vol 6 p.576 (IA bim_..._1742_6 leaf n579), "A letter of intelligence from col. Bamfylde",
Oct 25 / Nov 3 1657 (Second Cipher period). Printed gloss read by eye per code (x-position and count) from crops
bamf/crops/v6p576*_L*.jpg; compared with Tomokiyo's Second Cipher table bamf/tomokiyo/bamp2_table.tsv.
Writes bamf/thur94_v6p576_cells.tsv; --check exits 1 if the committed TSV is stale. No key edit (rule 4)."""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__))
# (run, codes, printed glosses by position) as read from the page image
RUNS = [
 (1, "388 20 398 436 62 69 87 813 167 674 46 56 151 45 66 89 792 426 752 19 20 576",
     "giv|s|great|hope|t|o|Fran|ce|that|prince|R|o|b|e|r|t|whom|he|trust|e|s|much"),
 (2, "22 49 12 318 58 65 433 475 744 729 627 457",
     "a|n|d|in|gag'|d|him|in|the|service|of|Hungary"),
 (3, "402 2 38 62 30 79 31 45 792 21 14 555 12 20 65 359 342 40 36 87 392 802",
     "Generall|Wi|del|t|a|z|a|c|who|c|o|man|d|s|for|elector|Palati|n|i|s|gone|yesterd."),
 (4, "43 56 67 62 744 371 238 139 41 19 62 20 107 8 54 11 15 359 572 59 23 37 25",
     "p|o|s|t|the|French|court|at|M|e|t|s|about|m|o|n|y|for|more|l|e|v|y"),
 (5, "68 20 139 29 16 36 700 426 391 67 64 54 348 749 528 9 46 22 70 75 626",
     "e|s|at|h|i|s|retuin|he|goe|s|t|o|Brandenburg|the|land|g|r|a|v|e|of"),
 (6, "6 68 67 86 360 813 71 49 12 342",
     "H|e|s|s|from|France|a|n|d|Palatinate"),
]
def tomokiyo():
    t = {}
    for ln in open(os.path.join(HERE, "tomokiyo", "bamp2_table.tsv"), encoding="utf-8"):
        if ln.startswith("#") or ln.startswith("code\t") or not ln.strip(): continue
        c, v = ln.rstrip("\n").split("\t")[:2]; t[c] = v
    return t
def build():
    T = tomokiyo(); out = ["run\tpos\tcode\tprinted_gloss\ttomokiyo\tstatus"]
    for run, codes, gl in RUNS:
        cs, gs = codes.split(), gl.split("|")
        assert len(cs) == len(gs), (run, len(cs), len(gs))
        for i, (c, g) in enumerate(zip(cs, gs), 1):
            tv = T.get(c, "")
            if not tv: st = "not-in-tomokiyo"
            elif tv == "[-]": st = "conflict(tomokiyo-null)"
            elif g.lower().rstrip(".") == tv.lower(): st = "agree"
            else: st = "conflict"
            out.append(f"{run}\t{i}\t{c}\t{g}\t{tv}\t{st}")
    return "\n".join(out) + "\n"
if __name__ == "__main__":
    p = os.path.join(HERE, "thur94_v6p576_cells.tsv"); txt = build()
    if "--check" in sys.argv:
        ok = os.path.exists(p) and open(p, encoding="utf-8").read() == txt
        print("OK" if ok else "STALE"); sys.exit(0 if ok else 1)
    open(p, "w", encoding="utf-8").write(txt); print("wrote", p)
