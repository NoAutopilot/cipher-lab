#!/usr/bin/env python3
"""H234 (runner 9 session_012NTadgrCBftz3oRtgw5jFu, 29 Sept 2026), script-only, written before the run, descriptive: f.61's meter (verify_v5/meter_v5.py's
bands, same decode file) under v5 + VERIFY-F61-V5's endorsed values, and under the same plus the shape readings found since, NONE of them endorsed:
 4TRI -> c/p and 4STEM -> a/n (H194: on f.61 every 4TRI is the bowl sign, every C43/4STEM the no-bowl sign; H219's test-key cells);
 HASH4 -> d/q (H233: f.61's one HASH4 is the 4-head hash, which reads d/q on f.101r 34/47 and f.188r 12/14, H224/H227);
 4PI -> unread (H233: f.61's 4PI is a 4 over a Pi, not f.101r's 4PI; no period value for that sign yet).
 ZHOOK stays i/x (H235 gives it a candidate glyph link; the grade, not the value, would change). The span gate is not run: none of these tokens moves a
 span score except 4TRI/4STEM, which H219 already scored (53/55 kept). No merge.  python3 h234_meter_shapes.py [--check]"""
import csv, os, sys
from collections import Counter
HERE = os.path.dirname(os.path.abspath(__file__))
V5 = {"VBAR_A": "g/t", "EBR": "l/y", "SBS": "b/o", "ZHOOK": "i/x"}; SH = dict(V5, **{"4TRI": "c/p", "4STEM": "a/n", "HASH4": "d/q", "4PI": "-"})
def band(letters, cls):
    if cls == "C6" or letters in ("-", ""): return "unread/null"
    n = len(letters.split("/")); return "firm" if n == 1 else ("two-way" if n == 2 else "wider")
def main():
    d = list(csv.DictReader(open(f"{HERE}/f61_decode_period_v4_frac0.1_sbs.tsv"), delimiter="\t")); out = []
    for tag, M in (("v5 (VERIFY-F61-V5)", V5), ("v5 + shape readings (not endorsed)", SH)):
        c = Counter(band(M.get(r["class"], r["period_letters"]), r["class"]) for r in d)
        out.append(f"{tag}: {len(d)} signs: firm {c['firm']} / two-way {c['two-way']} / wider {c['wider']} / unread-or-null {c['unread/null']}")
        wid = Counter(r["class"] + "=" + M.get(r["class"], r["period_letters"]) for r in d if band(M.get(r["class"], r["period_letters"]), r["class"]) == "wider")
        out.append(f"  still wider: " + " ".join(f"{k}:{v}" for k, v in sorted(wid.items())))
    ch = Counter((r["class"], V5.get(r["class"], r["period_letters"]), SH[r["class"]]) for r in d if r["class"] in SH and r["class"] not in V5)
    out.append("tokens changed by shape: " + "; ".join(f"{k[0]} {k[1]} -> {k[2]} x{v}" for k, v in sorted(ch.items())))
    txt = "\n".join(out) + "\n"; p = f"{HERE}/h234_meter_shapes_result.txt"
    if "--check" in sys.argv:
        ok = os.path.exists(p) and open(p).read() == txt; print("check", "OK" if ok else "STALE"); sys.exit(0 if ok else 1)
    open(p, "w").write(txt); print(txt, end="")
if __name__ == "__main__": main()
