#!/usr/bin/env python3
"""Reconcile two blind pass TSVs (leaf, order, code, gloss, note) of the Janssens
decipherment leaves into key.tsv (code -> value) and conflicts.tsv.

Usage: python3 build_key.py passA.tsv passB.tsv --out-dir .
"""
import argparse
import csv
import sys
from collections import defaultdict


def load(path):
    rows = []
    with open(path, newline="", encoding="utf-8") as f:
        r = csv.DictReader(f, delimiter="\t")
        for row in r:
            rows.append(row)
    return rows


def norm(s):
    return (s or "").strip()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("passA")
    ap.add_argument("passB")
    ap.add_argument("--out-dir", default=".")
    args = ap.parse_args()

    a_rows = load(args.passA)
    b_rows = load(args.passB)

    a_by_leaf = defaultdict(list)
    b_by_leaf = defaultdict(list)
    for row in a_rows:
        a_by_leaf[row["leaf"]].append(row)
    for row in b_rows:
        b_by_leaf[row["leaf"]].append(row)

    agree_rows = []
    disagree_rows = []
    for leaf in sorted(set(a_by_leaf) | set(b_by_leaf), key=lambda x: int(x)):
        al = a_by_leaf.get(leaf, [])
        bl = b_by_leaf.get(leaf, [])
        n = max(len(al), len(bl))
        for i in range(n):
            ra = al[i] if i < len(al) else None
            rb = bl[i] if i < len(bl) else None
            ca = norm(ra["code"]) if ra else None
            ga = norm(ra["gloss"]) if ra else None
            cb = norm(rb["code"]) if rb else None
            gb = norm(rb["gloss"]) if rb else None
            rec = {
                "leaf": leaf, "order": i + 1,
                "codeA": ca, "glossA": ga, "noteA": norm(ra["note"]) if ra else "",
                "codeB": cb, "glossB": gb, "noteB": norm(rb["note"]) if rb else "",
            }
            if ca == cb and ga == gb and ca is not None:
                agree_rows.append(rec)
            else:
                disagree_rows.append(rec)

    # Build key.tsv from agreed (code, gloss) pairs, counting occurrences and pages.
    key = defaultdict(lambda: defaultdict(lambda: {"n": 0, "pages": set()}))
    for rec in agree_rows:
        code = rec["codeA"]
        gloss = rec["glossA"]
        if not code or not gloss:
            continue
        key[code][gloss]["n"] += 1
        key[code][gloss]["pages"].add(rec["leaf"])

    conflicts = []
    key_out = []
    for code, variants in sorted(key.items(), key=lambda x: int(x[0])):
        if len(variants) == 1:
            gloss, info = next(iter(variants.items()))
            key_out.append({
                "code": code, "value": gloss, "n": info["n"],
                "pages": ",".join(sorted(info["pages"], key=int)), "grade": "C",
            })
        else:
            conflicts.append({
                "code": code,
                "variants": "; ".join(f"{g} (n={i['n']}, pages={','.join(sorted(i['pages'], key=int))})"
                                       for g, i in variants.items()),
            })

    with open(f"{args.out_dir}/key.tsv", "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=["code", "value", "n", "pages", "grade"], delimiter="\t")
        w.writeheader()
        for row in key_out:
            w.writerow(row)

    with open(f"{args.out_dir}/conflicts.tsv", "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=["code", "variants"], delimiter="\t")
        w.writeheader()
        for row in conflicts:
            w.writerow(row)

    with open(f"{args.out_dir}/pass_disagreements.tsv", "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=["leaf", "order", "codeA", "glossA", "noteA", "codeB", "glossB", "noteB"], delimiter="\t")
        w.writeheader()
        for row in disagree_rows:
            w.writerow(row)

    total = len(agree_rows) + len(disagree_rows)
    print(f"rows: {total}  agree: {len(agree_rows)}  disagree(row-level): {len(disagree_rows)}  "
          f"agreement: {len(agree_rows)/total*100:.1f}%" if total else "no rows")
    print(f"unique codes: {len(key)}  clean (single gloss): {len(key_out)}  conflicting: {len(conflicts)}")


if __name__ == "__main__":
    main()
