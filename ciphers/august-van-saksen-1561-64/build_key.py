#!/usr/bin/env python3
"""Derive key_74.tsv, key_98.tsv, key.tsv (both systems) and key_conflicts.tsv from pairs_74/98.tsv (R21).
A sign whose sure aligned units all agree gets that unit at grade C (known plaintext); pairings marked '~' (or on
a sign read with '?') do not set the value when sure pairings exist, but are listed in key_conflicts.tsv;
disagreeing sure units give grade M and 'a|b'. u and v are merged. '?' units are ignored. --check: exit 1 if stale."""
import csv, collections, os, sys
D = os.path.dirname(os.path.abspath(__file__))
out = {}
allrows, conf = ["system\tsign\tvalue\tgrade\tn\tunits"], ["system\tsign\tunits"]
for sysn in ("74", "98"):
    m = collections.defaultdict(collections.Counter)
    for r in csv.DictReader(open(f"{D}/pairs_{sysn}.tsv", encoding="utf-8"), delimiter="\t"):
        u = r["unit"]
        if r["sign"].endswith("?") and not u.endswith("~"): u += "~"   # doubtful sign: pairing counts as uncertain
        m[r["sign"].rstrip("?")][u] += 1
    rows = ["sign\tvalue\tgrade\tsource\tnote"]
    for s in sorted(m):
        c = {u: k for u, k in m[s].items() if u.strip("~") != "?"}
        if not c: continue
        norm = lambda u: "u" if u == "v" else u        # u and v are one letter in this hand
        firm, loose = collections.Counter(), collections.Counter()
        for u, k in c.items():
            (loose if u.endswith("~") else firm)[norm(u.rstrip("~"))] += k
        # value from the firm (sure) pairings; '~' pairings only when nothing firm exists
        base = firm or loose
        vals = [u for u, _ in base.most_common()]
        grade = "C" if firm and len(firm) == 1 else "M"
        n = sum(firm.values()) + sum(loose.values())
        units = ",".join(f"{u}:{k}" for u, k in sorted(c.items(), key=lambda x: -x[1]))
        rows.append(f"{s}\t{'|'.join(vals)}\t{grade}\tpairs_{sysn}.tsv\tn={n} {units}")
        allrows.append(f"{sysn}\t{s}\t{'|'.join(vals)}\t{grade}\t{n}\t{units}")
        if len(set(firm) | set(loose)) > 1: conf.append(f"{sysn}\t{s}\t{units}")
    out[f"key_{sysn}.tsv"] = "\n".join(rows) + "\n"
out["key.tsv"] = "\n".join(allrows) + "\n"
out["key_conflicts.tsv"] = "\n".join(conf) + "\n"
bad = 0
for fn, txt in out.items():
    p = f"{D}/{fn}"
    if "--check" in sys.argv:
        if not os.path.exists(p) or open(p, encoding="utf-8").read() != txt: print("stale", fn); bad = 1
    else: open(p, "w", encoding="utf-8").write(txt); print("wrote", fn, txt.count("\n") - 1)
sys.exit(bad)
