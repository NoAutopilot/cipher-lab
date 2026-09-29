#!/usr/bin/env python3
"""VERIFY-F61-V7, after scoring (labelled post hoc, rule 3 per-unit check): per-leaf Fisher exact of shape (D vs A in setD; not-A vs A in setN)
x letter class (I vs DQ), and the H24-coded rows by shape. Descriptive.  python3 v7_perleaf.py [--check]"""
import csv, os, sys
from collections import Counter
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, f"{HERE}/../family")
import h190_4fam as h190
def rd(f): return [r for r in csv.DictReader((l for l in open(f) if not l.startswith("#")), delimiter="\t")]
its = rd(f"{HERE}/v7_items.tsv"); out = []
for tag, rep, alt in (("setD", "v7_reply_setD.tsv", lambda a: a == "D"), ("setN", "v7_reply_setN.tsv", lambda a: a != "A")):
    ans = {r["id"].strip(): r["answer"].strip().upper()[:1] for r in rd(f"{HERE}/{rep}")}
    T = [r for r in its if r["set"] == tag and r["kind"] == "T" and not r["dup_of"] and r["cls"] in ("I", "DQ")]
    for leaf in ("188r", "101r", "274r"):
        g = [r for r in T if r["leaf"] == leaf]; a = [r for r in g if ans[r["id"]] == "A"]; o = [r for r in g if alt(ans[r["id"]])]
        c = [sum(r["cls"] == "I" for r in o), sum(r["cls"] == "DQ" for r in o), sum(r["cls"] == "I" for r in a), sum(r["cls"] == "DQ" for r in a)]
        out.append(f"{tag} f.{leaf}: {'2#' if tag == 'setD' else 'not-4head'} I {c[0]} DQ {c[1]} | 4-head I {c[2]} DQ {c[3]} | Fisher p {h190.fisher(*c):.2g}")
    for code in ("HASH4", "H24"):
        out.append(f"{tag} all lettered leaves, pass code {code}: " + "; ".join(f"{cl} " + " ".join(f"{k}{v}" for k, v in sorted(Counter(ans[r['id']] for r in T if r['code'] == code and r['cls'] == cl).items())) for cl in ("I", "DQ")))
txt = "\n".join(out) + "\n"; p = f"{HERE}/v7_perleaf_result.txt"
if "--check" in sys.argv:
    ok = os.path.exists(p) and open(p).read() == txt; print("check", "OK" if ok else "STALE"); sys.exit(0 if ok else 1)
open(p, "w").write(txt); print(txt, end="")
