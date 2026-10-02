#!/usr/bin/env python3
"""Printed-key reading vs clerk-value variant, per letter (NEVBIR-87ALIGN): grade counts and every changed token with
+-10 letters of context.  python3 harvest/align87/compare_variant.py"""
import csv
from collections import Counter
from pathlib import Path
H = Path(__file__).resolve().parent.parent
for name, f in (("no.71", "reading_f139v_tokens.tsv"), ("no.86", "reading_no86_tokens.tsv"), ("no.90", "reading_no90_tokens.tsv")):
    a = list(csv.DictReader(open(H / f), delimiter="\t")); b = list(csv.DictReader(open(H / "clerkvar" / f), delimiter="\t"))
    assert len(a) == len(b)
    ga, gb = Counter(r["grade"] for r in a), Counter(r["grade"] for r in b)
    print(f"{name}: {len(a)} signs; printed+fit {dict(sorted(ga.items()))} -> variant {dict(sorted(gb.items()))}")
    val = lambda r: "" if r["value"] in ("NULL", "?", "") else r["value"]
    ch = [i for i, (x, y) in enumerate(zip(a, b)) if x["value"] != y["value"]]
    print(f"  changed tokens {len(ch)}: " + str(Counter(f"{a[i]['sign']} {a[i]['value']}->{b[i]['value']}" for i in ch)))
    for i in ch:
        ctx = lambda rows: "".join(val(r) for r in rows[max(0, i - 8):i]) + "[" + val(rows[i]) + "]" + "".join(val(r) for r in rows[i + 1:i + 9])
        print(f"  {a[i]['line']}/{a[i]['pos']}  {ctx(a)}  ->  {ctx(b)}")
