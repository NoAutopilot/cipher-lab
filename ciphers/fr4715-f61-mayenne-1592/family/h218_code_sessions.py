#!/usr/bin/env python3
"""H218 (runner 8 session_011Taenrv3JSdk7VjpiBjids, 29 Sept 2026), script-only, descriptive, for the verifier and any v6 build. One table: for each leaf
and each blind shape step on disk, the pass code(s) under which each shape answer fell -- bowl yes / no / n for the 4-family (H193 f.176v/f.176r,
H194 f.61, H199 f.108v, H202 f.108r, H207 f.101r) and 4-head (A) / looped (B) for HASH4 (H212 f.108v, f.108r). Shows which code each reading
session wrote for which shape, so pooled key counts can be re-split by shape.  -> h218_code_sessions_result.txt [--check]"""
import csv, os, sys
from collections import Counter, defaultdict
HERE = os.path.dirname(os.path.abspath(__file__)); P = f"{HERE}/passes"
def rd(f): return [r for r in csv.DictReader((l for l in open(f) if not l.startswith("#")), delimiter="\t")]
def main():
    T = defaultdict(Counter)   # (leaf, step, code) -> answers
    a = {r["item"]: r["answer"].strip().lower() for r in rd(f"{P}/h193_attribute.tsv")}
    for r in rd(f"{HERE}/h193_items.tsv"):
        code = {"CP": "4TRI (both passes)", "AN": "4TRI|C43 (passes split)", "T": "4TRI (both passes)"}[r["group"]]
        T[("f.176v" if r["leaf"] == "176v" else "f.176r", "H193", code)][a.get(r["item"], "-")] += 1
    for l in open(f"{HERE}/h194_bowl_f61_result.txt"):
        f = l.rstrip("\n").split("\t")
        if len(f) == 5 and f[0].startswith("L") and f[1].isdigit(): T[("f.61", "H194", f[2])][f[3]] += 1
    for r in rd(f"{HERE}/h199_bowl_positions.tsv"): T[("f.108v", "H199 (H59 reconciled code)", r["rec"])][r["bowl"]] += 1
    for items, reply, step, leaf in (("h202_items.tsv", "h202_reply.tsv", "H202 (pass A code)", "f.108r L02-L03"), ("h207_items.tsv", "h207_reply.tsv", "H207 (period-aligned code)", "f.101r")):
        a = {r["id"]: r["answer"].strip().lower() for r in rd(f"{P}/{reply}")}
        for r in rd(f"{HERE}/{items}"): T[(leaf, step, r["code"])][a.get(r["item"], "-")] += 1
    g = {f"T{int(r['tile'].split()[-1]):02d}": r["group"].strip() for r in rd(f"{P}/h212_sort.tsv")}
    for r in rd(f"{HERE}/h212_items.tsv"): T[("f.108v" if r["leaf"] == "108v" else "f.108r L06", "H212 hash form (A 4-head, B looped)", "HASH4")][g[r["item"]]] += 1
    out = ["leaf\tstep\tcode\tanswers"]
    for (leaf, step, code), c in sorted(T.items()): out.append(f"{leaf}\t{step}\t{code}\t" + " ".join(f"{k}:{v}" for k, v in sorted(c.items())))
    txt = "\n".join(out) + "\n"; rp = f"{HERE}/h218_code_sessions_result.txt"
    if "--check" in sys.argv:
        ok = os.path.exists(rp) and open(rp).read() == txt; print("check", "OK" if ok else "STALE"); sys.exit(0 if ok else 1)
    open(rp, "w").write(txt); print(txt, end="")
if __name__ == "__main__": main()
