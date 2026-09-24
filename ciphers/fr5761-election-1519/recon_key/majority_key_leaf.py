#!/usr/bin/env python3
"""Add one leaf's rows to key.tsv from two atlas-coded passes (key_passA2_atlas.tsv,
key_passC2_atlas.tsv, columns: leaf, line, section, plain, sign_code, note) plus the
existing free-text key_passB.tsv as a non-code third vote (it predates the atlas and
has no sign_code column, so it cannot itself supply a majority code -- see NOTES.md
"Key f.105-f.110" section for why).

Grade: H where A and C agree on the same non-blank sign_code (UNLISTED counts as
agreeing, per the f104 convention in this same key.tsv); M otherwise. B's cipher_desc
is carried into the note column for a human to cross-check, never counted as a vote.

Usage: recon_key/majority_key_leaf.py LEAF [--migrate-header]
--migrate-header adds a 'leaf' column to key.tsv's existing (f104) rows, defaulting
them to f104, before appending -- run this once, on the first leaf appended.
"""
import csv, sys, argparse
from pathlib import Path
from collections import Counter

def load(path):
    return list(csv.DictReader(open(path), delimiter="\t"))

def norm(s):
    return (s or "").strip()

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("leaf")
    ap.add_argument("--migrate-header", action="store_true")
    args = ap.parse_args()
    leaf = args.leaf

    root = Path(__file__).resolve().parent.parent
    key_path = root / "key.tsv"

    existing = load(key_path)
    if args.migrate_header:
        for r in existing:
            r.setdefault("leaf", "f104")
            r["leaf"] = "f104"

    a = [r for r in load(root / "key_passA2_atlas.tsv") if r["leaf"] == leaf]
    c = [r for r in load(root / "key_passC2_atlas.tsv") if r["leaf"] == leaf]
    b_all = load(root / "key_passB.tsv")
    b = [r for r in b_all if r["canvas"] == leaf]

    def section_of(r, key="section"):
        return norm(r[key]).lower()

    # alphabet: join by letter (plain)
    out_rows = []
    grade_counts = Counter()

    alpha_letters = []
    for r in a + c:
        if section_of(r) == "alphabet" and norm(r["plain"]) not in alpha_letters:
            alpha_letters.append(norm(r["plain"]))
    b_alpha = {norm(r["plain"]): r for r in b if section_of(r) == "alphabet"}

    for L in alpha_letters:
        ra = next((r for r in a if section_of(r) == "alphabet" and norm(r["plain"]) == L), None)
        rc = next((r for r in c if section_of(r) == "alphabet" and norm(r["plain"]) == L), None)
        rb = b_alpha.get(L)
        code_a, code_c = norm(ra["sign_code"]) if ra else "", norm(rc["sign_code"]) if rc else ""
        grade = "H" if code_a and code_a == code_c else "M"
        grade_counts[grade] += 1
        sign_code = code_a if grade == "H" else (code_a or code_c)
        b_desc = norm(rb["cipher_desc"]) if rb else ""
        note = f"votes[A:{code_a or '-'}|B(desc):{b_desc or '-'}|C:{code_c or '-'}]"
        out_rows.append([leaf, "1", "alphabet", L, sign_code, grade, note])

    # correspondent + nulls: join by ordinal position within section (reading order)
    for section, b_section_names in (("correspondent", ("names", "correspondent")), ("nulls", ("nulls", "null"))):
        ra_list = [r for r in a if section_of(r) == section]
        rc_list = [r for r in c if section_of(r) == section]
        b_list = [r for r in b if section_of(r, "section") in b_section_names]
        n = max(len(ra_list), len(rc_list), len(b_list))
        for i in range(n):
            ra = ra_list[i] if i < len(ra_list) else None
            rc = rc_list[i] if i < len(rc_list) else None
            rb = b_list[i] if i < len(b_list) else None
            code_a, code_c = norm(ra["sign_code"]) if ra else "", norm(rc["sign_code"]) if rc else ""
            grade = "H" if code_a and code_a == code_c else "M"
            grade_counts[grade] += 1
            sign_code = code_a if grade == "H" else (code_a or code_c)
            plain = norm(ra["plain"]) if ra else (norm(rc["plain"]) if rc else (norm(rb["plain"]) if rb else f"{section}{i+1}"))
            line = norm(ra["line"]) if ra else (norm(rc["line"]) if rc else str(i + 2))
            b_desc = norm(rb["cipher_desc"]) if rb else ""
            note = f"votes[A:{code_a or '-'}|B(desc):{b_desc or '-'}|C:{code_c or '-'}]"
            out_rows.append([leaf, line, section, plain, sign_code, grade, note])

    fieldnames = ["leaf", "line", "section", "plain", "sign_code", "grade", "note"]
    with open(key_path, "w", newline="") as f:
        w = csv.writer(f, delimiter="\t")
        w.writerow(fieldnames)
        for r in existing:
            w.writerow([r.get("leaf", "f104"), r["line"], r["section"], r["plain"], r["sign_code"], r["grade"], r["note"]])
        w.writerows(out_rows)

    print(f"{leaf}: appended {len(out_rows)} rows")
    for g in ("H", "M"):
        print(f"  grade {g}: {grade_counts[g]}")
    named = sum(1 for r in out_rows if r[4] and r[4] != "UNLISTED")
    print(f"  rows with a named K-code (A==C, excl. UNLISTED): {named}/{len(out_rows)}")

if __name__ == "__main__":
    main()
