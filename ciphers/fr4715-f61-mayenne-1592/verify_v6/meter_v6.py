#!/usr/bin/env python3
"""VERIFY-F61-V6 (29 Sept 2026): f.61r meter under key v5 (VERIFY-F61-V5's endorsed cells) plus this audit's endorsement: on f.61's hand
4TRI -> c/p (t dropped) and the one 4STEM token (L11) -> a/n, both graded S. Two forms: (A) 4TRI at code level (every f.61 4TRI token;
the tested ones were the bowl sign 10/10 over two blind readers) and (B) only the shape-read 4TRI tokens (L01's 4TRI, unmatched by shape
in both sessions, stays c/p/t). Bands as meter_v5.py.  python3 meter_v6.py [--check]"""
import csv, os, sys
from collections import Counter
HERE = os.path.dirname(os.path.abspath(__file__)); F = os.path.abspath(f"{HERE}/../family")
V5 = {"VBAR_A": "g/t", "EBR": "l/y", "SBS": "b/o", "ZHOOK": "i/x"}
def band(letters, cls):
    if cls == "C6" or letters in ("-", ""): return "unread/null"
    n = len(letters.split("/")); return "firm" if n == 1 else ("two-way" if n == 2 else "wider")
def main():
    d = list(csv.DictReader(open(f"{F}/f61_decode_period_v4_frac0.1_sbs.tsv"), delimiter="\t")); out = []
    def v5(r): return V5.get(r["class"], r["period_letters"])
    def v6(r, shape_only):
        if r["class"] == "4TRI" and not (shape_only and r["line"] == "L01"): return "c/p"
        if r["class"] == "4STEM": return "a/n"
        return v5(r)
    for tag, f in (("v5", v5), ("v5 + 4TRI c/p, 4STEM a/n (A: code level on f.61)", lambda r: v6(r, False)), ("v5 + (B: shape-read tokens only)", lambda r: v6(r, True))):
        c = Counter(band(f(r), r["class"]) for r in d)
        out.append(f"{tag}: {len(d)} signs: firm {c['firm']} / two-way {c['two-way']} / wider {c['wider']} / unread-or-null {c['unread/null']}")
        wid = Counter(r["class"] + "=" + f(r) for r in d if band(f(r), r["class"]) == "wider"); out.append("  still wider: " + " ".join(f"{k}:{v}" for k, v in sorted(wid.items())))
    txt = "\n".join(out) + "\n"; p = f"{HERE}/meter_v6_result.txt"
    if "--check" in sys.argv:
        ok = os.path.exists(p) and open(p).read() == txt; print("check", "OK" if ok else "STALE"); sys.exit(0 if ok else 1)
    open(p, "w").write(txt); print(txt, end="")
if __name__ == "__main__": main()
