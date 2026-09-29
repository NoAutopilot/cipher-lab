#!/usr/bin/env python3
"""H223 (runner 9 session_012NTadgrCBftz3oRtgw5jFu, 29 Sept 2026), script-only, written before the run: one table, for the verifier and any v6 build, of
the blind hash-form answers by leaf and pass code (H218's table for the hash family), with the period letter set where the leaf has one. Sources: H212
(f.108v/f.108r HASH4, free sort A/B), H220 (f.101r HASH4 + H24, A/B/N), H224 (f.188r HASH4), H226 (f.101r/f.188r stray HASH4), H227 (f.101r HASH4
rest), H221 hash call (f.106r HASH4 + H24). Forms: A 4-head, B looped, C plain hash, D 2-hook ("2#"), N. Anchor tiles left out. Letter cells: d/q, i/x
(i x j y), other, '-' (no period letter / held leaf).  python3 h223_hash_table.py [--check]"""
import csv, os, sys
from collections import Counter, defaultdict
HERE = os.path.dirname(os.path.abspath(__file__)); P = f"{HERE}/passes"
def rd(f): return [r for r in csv.DictReader((l for l in open(f) if not l.startswith("#")), delimiter="\t")]
def cell(L): return "d/q" if L in ("d", "q") else "i/x" if L in ("i", "x", "j", "y") else "-" if L in ("", "-") else "other"
def main():
    T = defaultdict(Counter)   # (leaf, code) -> Counter of (form, cell)
    g212 = {f"T{int(r['tile'].split()[-1]):02d}": r["group"].strip() for r in rd(f"{P}/h212_sort.tsv")}
    for r in rd(f"{HERE}/h212_items.tsv"): T[("f." + r["leaf"], "HASH4")][(g212[r["item"]], "-")] += 1
    for items, rep, leafcol, codecol in (("h220_items.tsv", "h220_reply.tsv", None, "code"), ("h224_items.tsv", "h224_reply.tsv", None, None),
                                         ("h226_items.tsv", "h226_reply.tsv", "ref", None), ("h227_items.tsv", "h227_reply.tsv", None, None)):
        a = {r["id"]: r["answer"].strip().upper() for r in rd(f"{P}/{rep}")}
        for r in rd(f"{HERE}/{items}"):
            if r["kind"] != "T": continue
            leaf = {"h220_items.tsv": "f.101r", "h224_items.tsv": "f.188r", "h227_items.tsv": "f.101r"}.get(items) or ("f." + r[leafcol][1:])
            T[(leaf, r[codecol] if codecol else "HASH4")][(a.get(r["item"], "N"), cell(r["letter"]))] += 1
    a = {r["id"]: r["answer"].strip().upper() for r in rd(f"{P}/h221h_reply.tsv")}
    for r in rd(f"{HERE}/h221_items.tsv"):
        if r["set"] == "h221h" and r["kind"] == "T": T[("f.106r (held)", r["code"])][(a.get(r["item"], "N"), "-")] += 1
    out = ["leaf / code: form -> letters (A 4-head, B looped, C plain, D 2#, N)"]
    for k in sorted(T):
        by = defaultdict(Counter)
        for (f, c), n in T[k].items(): by[f][c] += n
        out.append(f"{k[0]} {k[1]}: " + "; ".join(f"{f} {sum(by[f].values())}" + (" (" + " ".join(f"{c} {n}" for c, n in sorted(by[f].items()) if c != "-") + ")" if any(c != "-" for c in by[f]) else "") for f in sorted(by)))
    txt = "\n".join(out) + "\n"; p = f"{HERE}/h223_hash_table_result.txt"
    if "--check" in sys.argv:
        ok = os.path.exists(p) and open(p).read() == txt; print("check", "OK" if ok else "STALE"); sys.exit(0 if ok else 1)
    open(p, "w").write(txt); print(txt, end="")
if __name__ == "__main__": main()
