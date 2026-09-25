#!/usr/bin/env python3
"""Regenerate reading_1069.txt from ciphertext_1069.tsv + key_1069.tsv; exit non-zero if the committed
reading is stale (CLAUDE.md rule 7). No decode.json layout exists for this fragment (too small, single
line), so this is the small target-specific check script the rule allows instead.

Usage: python3 check_1069.py [--check]
  (no args)   print the regenerated reading
  --check     exit 0 if reading_1069.txt matches the regeneration, exit 1 otherwise
"""
import csv
import sys
from pathlib import Path

HERE = Path(__file__).parent


def load_key(path):
    key = {}
    with open(path, encoding="utf-8") as f:
        for row in csv.DictReader(f, delimiter="\t"):
            if row["sign_desc"].startswith("#"):
                continue
            key[row["sign_desc"]] = (row["value"], row["grade"])
    return key


def load_ciphertext(path):
    signs = []
    with open(path, encoding="utf-8") as f:
        for row in csv.DictReader(f, delimiter="\t"):
            if row["page"].startswith("#"):
                continue
            signs.append(row["sign_desc"])
    return signs


def regenerate():
    key = load_key(HERE / "key_1069.tsv")
    signs = load_ciphertext(HERE / "ciphertext_1069.tsv")
    letters, grades = [], []
    for s in signs:
        if s not in key:
            letters.append("?")
            grades.append("?")
            continue
        value, grade = key[s]
        letters.append(value)
        grades.append(grade)
    plain = "".join(letters)
    counts = {g: grades.count(g) for g in set(grades)}
    return plain, counts


def main():
    plain, counts = regenerate()
    header = (
        "# briefnr 1069 (Willem van Hessen to Willem van Oranje, 23 Mar 1563), p2 line 1, "
        "confirmed fragment only -- 10 of an estimated 1000+ cipher signs across p2-p4 (see NOTES.md).\n"
        f"# grade counts: {counts}\n"
    )
    body = (
        f'raw decode: "{plain}"\n'
        'reading: "...mi[t] Gr(u/m)(n/mb)ach(s)..." -- the fragment\'s first sign is the same "t" that ends '
        '"mit"; the rest spells (a form of) Grumbachs, Wilhelm von Grumbach.\n'
    )
    regenerated = header + body

    if "--check" in sys.argv:
        existing = (HERE / "reading_1069.txt").read_text(encoding="utf-8")
        if existing != regenerated:
            print("STALE: reading_1069.txt does not match ciphertext_1069.tsv + key_1069.tsv")
            print("--- committed ---")
            print(existing)
            print("--- regenerated ---")
            print(regenerated)
            return 1
        print("OK: reading_1069.txt matches regeneration")
        return 0

    print(regenerated, end="")
    return 0


if __name__ == "__main__":
    sys.exit(main())
