#!/usr/bin/env python3
"""VERIFY-F61-V8 (29 Sept 2026): f.61r meter (bands as verify_v5/meter_v5.py and verify_v7/meter_v7.py) under key v6 (family/key_period_v6.tsv,
F61-FAMILY-10, f.61 reading key) and with the two cells audited here: ZHOOK = the 2# (value i/x, unchanged from v6: a grade change only) and
f.61's 4PI as its own sign read a/n (H240), or held unread (the split without a value).  python3 meter_v8.py [--check]"""
import csv, os, sys
from collections import Counter
HERE = os.path.dirname(os.path.abspath(__file__)); F = os.path.abspath(f"{HERE}/../family"); sys.path.insert(0, F)
import build_key_v6 as bk
def band(letters, cls):
    if cls == "C6" or letters in ("-", ""): return "unread/null"
    n = len(letters.split("/")); return "firm" if n == 1 else ("two-way" if n == 2 else "wider")
def main():
    d = list(csv.DictReader(open(f"{F}/f61_decode_period_v4_frac0.1_sbs.tsv"), delimiter="\t")); k6 = bk.load_key_v6(ebr="B", f61=True); out = []
    V5 = {"VBAR_A": "g/t", "EBR": "l/y", "SBS": "b/o"}   # v5 cells carried into v6 unchanged (meter_v7.py)
    def v6(r):
        c = r["class"]
        if c in V5: return V5[c]
        if c in ("ZHOOK", "HASH4", "4TRI", "4STEM"): return "/".join(k6[c])
        return r["period_letters"]
    for tag, f in (("v6", v6), ("v6 + ZHOOK = 2# (value unchanged)", v6),
                   ("v6 + 4PI split, f.61 4PI a/n (H240)", lambda r: "a/n" if r["class"] == "4PI" else v6(r)),
                   ("v6 + 4PI split, f.61 4PI held unread", lambda r: "-" if r["class"] == "4PI" else v6(r))):
        c = Counter(band(f(r), r["class"]) for r in d)
        out.append(f"{tag}: {len(d)} signs: firm {c['firm']} / two-way {c['two-way']} / wider {c['wider']} / unread-or-null {c['unread/null']}")
        wid = Counter(r["class"] + "=" + f(r) for r in d if band(f(r), r["class"]) == "wider"); out.append("  still wider: " + " ".join(f"{k}:{v}" for k, v in sorted(wid.items())))
    txt = "\n".join(out) + "\n"; p = f"{HERE}/meter_v8_result.txt"
    if "--check" in sys.argv:
        ok = os.path.exists(p) and open(p).read() == txt; print("check", "OK" if ok else "STALE"); sys.exit(0 if ok else 1)
    open(p, "w").write(txt); print(txt, end="")
if __name__ == "__main__": main()
