#!/usr/bin/env python3
"""VERIFY-F61-V7 (29 Sept 2026): f.61r meter (bands as verify_v5/meter_v5.py) under key v5, v5 + this audit's HASH4 cell (f.61's one HASH4,
L01, read d/q -- only if the blind sort puts that token on the 4-head), v5 + VERIFY-F61-V6's endorsed part (4TRI c/p, the one 4STEM a/n, form A),
and both together. H24 does not occur on f.61, so the H24 half of the re-split moves no f.61 token.  python3 meter_v7.py [--check]"""
import csv, os, sys
from collections import Counter
HERE = os.path.dirname(os.path.abspath(__file__)); F = os.path.abspath(f"{HERE}/../family")
V5 = {"VBAR_A": "g/t", "EBR": "l/y", "SBS": "b/o", "ZHOOK": "i/x"}
def band(letters, cls):
    if cls == "C6" or letters in ("-", ""): return "unread/null"
    n = len(letters.split("/")); return "firm" if n == 1 else ("two-way" if n == 2 else "wider")
def main():
    d = list(csv.DictReader(open(f"{F}/f61_decode_period_v4_frac0.1_sbs.tsv"), delimiter="\t")); out = []
    v5 = lambda r: V5.get(r["class"], r["period_letters"])
    h = lambda r: "d/q" if r["class"] == "HASH4" else v5(r)
    b6 = lambda r, g: "c/p" if r["class"] == "4TRI" else ("a/n" if r["class"] == "4STEM" else g(r))
    for tag, f in (("v5", v5), ("v5 + HASH4 d/q (V7)", h), ("v5 + 4TRI c/p, 4STEM a/n (V6, form A)", lambda r: b6(r, v5)),
                   ("v5 + V6 + V7", lambda r: b6(r, h))):
        c = Counter(band(f(r), r["class"]) for r in d)
        out.append(f"{tag}: {len(d)} signs: firm {c['firm']} / two-way {c['two-way']} / wider {c['wider']} / unread-or-null {c['unread/null']}")
        wid = Counter(r["class"] + "=" + f(r) for r in d if band(f(r), r["class"]) == "wider"); out.append("  still wider: " + " ".join(f"{k}:{v}" for k, v in sorted(wid.items())))
    txt = "\n".join(out) + "\n"; p = f"{HERE}/meter_v7_result.txt"
    if "--check" in sys.argv:
        ok = os.path.exists(p) and open(p).read() == txt; print("check", "OK" if ok else "STALE"); sys.exit(0 if ok else 1)
    open(p, "w").write(txt); print(txt, end="")
if __name__ == "__main__": main()
