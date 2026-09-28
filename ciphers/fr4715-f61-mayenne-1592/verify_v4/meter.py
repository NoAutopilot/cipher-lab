#!/usr/bin/env python3
"""VERIFY-F61-V4 step 4: recount firm (C, C+) / two-way-or-wider (M) / unread (-) from the committed v3 and v4 decodes of
f.61r, list every sign whose grade moved, and the INF rows of each key leaf behind the moves. -> verify_v4/meter_result.txt"""
import csv, os, sys
from collections import Counter
H = os.path.dirname(os.path.abspath(__file__)); F = f"{H}/../family"
def load(p): return {(r["line"], int(r["pos"])): r for r in csv.DictReader(open(p), delimiter="\t")}
v3 = load(f"{F}/f61_decode_period_v3_frac0.1.tsv"); v4 = load(f"{F}/f61_decode_period_v4_frac0.1_sbs.tsv")
b = lambda g: "firm" if g in ("C", "C+") else ("two-way+" if g == "M" else "unread")
out = []
for tag, d in (("v3", v3), ("v4", v4)):
    c = Counter(b(r["grade"]) for r in d.values()); g = Counter(r["grade"] for r in d.values())
    sz = Counter(len(r["period_letters"].split("/")) for r in d.values() if r["grade"] == "M")
    out.append(f"{tag}: {len(d)} signs, firm {c['firm']} (C {g['C']}, C+ {g['C+']}) / two-way+ {c['two-way+']} / unread {c['unread']}; M set sizes " + " ".join(f"{k}:{v}" for k, v in sorted(sz.items())))
mv = [(k, v3[k], v4[k]) for k in sorted(v4) if b(v3[k]["grade"]) != b(v4[k]["grade"])]
out.append(f"grade band changed: {len(mv)}")
for k, a, z in mv: out.append(f"  {k[0]}/{k[1]}: {a['class']} {a['period_letters']} {a['grade']} -> {z['class']} {z['period_letters']} {z['grade']}")
firm4 = Counter(r["class"] + "=" + r["period_letters"] for r in v4.values() if r["grade"] in ("C", "C+"))
out.append("v4 firm tokens by class: " + " ".join(f"{k}:{v}" for k, v in sorted(firm4.items())))
for kf in ("key_period_v3.tsv", "key_period_v4.tsv"):
    rows = [r for r in csv.DictReader((l for l in open(f"{F}/{kf}") if not l.startswith("#")), delimiter="\t") if r["class"] == "INF"]
    tot = Counter(); [tot.update({r["leaf"]: int(r["n"])}) for r in rows if r["letter"] != "-"]
    out.append(f"{kf} INF: " + "; ".join(f"{r['leaf']} {r['letter']} {r['n']}/{tot[r['leaf']]}" for r in rows if int(r["n"]) >= 2))
txt = "\n".join(out) + "\n"; p = f"{H}/meter_result.txt"
if "--check" in sys.argv: ok = open(p).read() == txt; print("fresh" if ok else "STALE"); sys.exit(0 if ok else 1)
open(p, "w").write(txt); print(txt, end="")
