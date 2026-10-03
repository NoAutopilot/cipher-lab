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
            signs.append((row["sign_desc"], row.get("value_override") or "", row.get("grade_override") or "", row["line"]))
    return signs


def regenerate():
    key = load_key(HERE / "key_1069.tsv")
    signs = load_ciphertext(HERE / "ciphertext_1069.tsv")
    letters, grades = [], []
    lines = {}
    for s, ov, og, line in signs:
        if ov:
            lines.setdefault(line, []).append(ov)
            letters.append(ov)
            grades.append(og or "M")
            continue
        if s not in key:
            letters.append("?")
            grades.append("?")
            continue
        value, grade = key[s]
        lines.setdefault(line, []).append(value)
        letters.append(value)
        grades.append(grade)
    plain = " | ".join("".join(v) for _, v in sorted(lines.items(), key=lambda kv: int(kv[0])))
    counts = {g: grades.count(g) for g in sorted(set(grades))}
    return plain, counts, len(grades)


def main():
    plain, counts, n = regenerate()
    header = (
        "# briefnr 1069 (Willem van Hessen to Willem van Oranje, 23 Mar 1563), p2 lines 1-6, "
        f"{n} signs of an estimated 1000+ across p2-p4 (GAPS78 lines 1-3, GAPS80 lines 4-6, 3 Oct 2026; see NOTES.md).\n"
        f"# grade counts: {counts}\n"
    )
    body = (
        f'raw decode (lines joined by |; o = the decipherer\'s null mark, [-] = no gloss, ? = gloss split): "{plain}"\n'
        'reading: "...?o?mit Grumpachs [oo] bewerbung. | ist [o] FR nicht [o] garnichts [---] es ?igen | auch [oo] schon '
        '[o] dreimal hündert [o] u tausent" -- the decipherer\'s gloss read through the key; FR (overlined, over the V sign) '
        'is a code word, plausibly Frankreich; see NOTES.md GAPS78 for grades and caveats. Lines 4-6 (GAPS80): only the clear '
        'words are segmented -- L4 "... darauf [gloss davauf, Kurrent r read v] ... wir", L5 "... chen", L6 "... bewer?nng '
        '[bewerbung?] ... ?nnerhindern"; the rest is left as the raw gloss string above, not interpreted.\n'
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
