#!/usr/bin/env python3
"""Majority-vote key_passA_atlas.tsv, key_passB_atlas.tsv and key_passC_atlas.tsv (line, section,
plain, sign_code, note) into key.tsv (correspondent/line, section, plain, sign_code, grade, note).

Rows are matched across the three passes by line number (the one anchor all three passes agree
on for a given physical line of the key list, even where the plain-text name or its position
count differs between passes -- see recon_key/reconcile_key.py's docstring for why line number,
not plain text, is the join key for correspondent rows). Alphabet rows (line 1) are matched by
letter (the 'plain' column, a-x); Nulle rows are matched positionally within their line, in the
order each pass lists them.

Grade: H where at least 2 of the (up to 3) sign_code readings for a row agree on the same
non-blank code; M otherwise (no majority, or fewer than 2 passes read a code at all).
"""
import csv, sys
from pathlib import Path
from collections import Counter, defaultdict

def load(path):
    return list(csv.DictReader(open(path), delimiter="\t"))

def norm(s):
    return (s or "").strip()

def is_null(sec):
    return norm(sec).lower() in ("nulls", "nulle", "null")

def is_alpha(sec):
    return norm(sec).lower() == "alphabet"

def main():
    root = Path(__file__).resolve().parent.parent
    a = load(root / "key_passA_atlas.tsv")
    b = load(root / "key_passB_atlas.tsv")
    c = load(root / "key_passC_atlas.tsv")

    # drop header-only rows (not sign positions)
    a = [r for r in a if norm(r["section"]).lower() != "header"]

    groups = []  # list of (label, [rows from A, B, C where present])

    # alphabet: join by letter
    letters = []
    for r in a + b + c:
        if is_alpha(r["section"]) and norm(r["plain"]) not in letters:
            letters.append(norm(r["plain"]))
    for L in letters:
        rows = [r for r in (a, b, c) for r in [next((x for x in r if is_alpha(x["section"]) and norm(x["plain"]) == L), None)]]
        groups.append((("1", "alphabet", L), rows))

    # nulle: positional within line 5 (or whichever line each pass uses for nulls)
    a_n = [r for r in a if is_null(r["section"])]
    b_n = [r for r in b if is_null(r["section"])]
    c_n = [r for r in c if is_null(r["section"])]
    for i in range(max(len(a_n), len(b_n), len(c_n))):
        rows = [lst[i] if i < len(lst) else None for lst in (a_n, b_n, c_n)]
        line = next(r["line"] for r in rows if r)
        groups.append(((line, "nulls", f"Null{i+1}"), rows))

    # correspondent rows: join by line number (name spelling varies pass to pass)
    a_corr = {r["line"]: r for r in a if not is_alpha(r["section"]) and not is_null(r["section"])}
    b_corr = {r["line"]: r for r in b if not is_alpha(r["section"]) and not is_null(r["section"])}
    c_corr = {r["line"]: r for r in c if not is_alpha(r["section"]) and not is_null(r["section"])}
    for line in sorted(set(a_corr) | set(b_corr) | set(c_corr), key=lambda x: int(x)):
        rows = [a_corr.get(line), b_corr.get(line), c_corr.get(line)]
        # prefer the plain-text reading two passes agree on (case-insensitive), else C's, else A's
        plains = [norm(r["plain"]) for r in rows if r]
        plain_counts = Counter(p.lower() for p in plains)
        best = max(plain_counts.items(), key=lambda kv: kv[1])[0] if plain_counts else ""
        plain = next((p for p in plains if p.lower() == best), plains[0] if plains else "")
        groups.append(((line, "correspondent", plain), rows))

    out_rows = []
    grade_counts = Counter()
    for (line, section, plain), rows in groups:
        codes = [norm(r["sign_code"]) for r in rows if r and norm(r["sign_code"])]
        vote = Counter(codes)
        sign_code, n_agree = (vote.most_common(1)[0] if vote else ("", 0))
        grade = "H" if n_agree >= 2 else "M"
        grade_counts[grade] += 1
        readings = "|".join(f"{p}:{(norm(r['sign_code']) or '-') if r else '(no row)'}" for p, r in zip("ABC", rows))
        note = f"votes[{readings}]"
        out_rows.append([line, section, plain, sign_code, grade, note])

    out_rows.sort(key=lambda r: (0 if r[1] == "alphabet" else 1, int(r[0]) if r[1] != "alphabet" else 0, r[2]))

    with open(root / "key.tsv", "w", newline="") as f:
        w = csv.writer(f, delimiter="\t")
        w.writerow(["line", "section", "plain", "sign_code", "grade", "note"])
        w.writerows(out_rows)

    print(f"key.tsv rows: {len(out_rows)}")
    for g in ("H", "M"):
        print(f"  grade {g}: {grade_counts[g]}")
    coded = sum(1 for r in out_rows if r[3])
    named = sum(1 for r in out_rows if r[3] and r[3] != "UNLISTED")
    print(f"  rows with any majority sign_code (incl. UNLISTED): {coded}/{len(out_rows)}")
    print(f"  rows with a named K-code majority (excl. UNLISTED/blank): {named}/{len(out_rows)}")

if __name__ == "__main__":
    main()
