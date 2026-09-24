#!/usr/bin/env python3
"""Mechanically apply Tomokiyo's PARTIAL reconstructed keys (thurloe.htm) to the
5 Thurloe letters whose cipher system he has identified from OTHER correspondence
(Blake, Montagu x2, Protector-to-Blake-and-Montagu, Downing). Tomokiyo's page does
not print a full nomenclator for any of these systems -- only a handful of letter
homophones (E) plus a short list of higher-value code words per system, reconstructed
by him from letters this project has not re-verified beyond the crib checks already
logged in NOTES.md. This script applies exactly those published values, nothing more:
it does not guess, repair, or extend the key.

Reproducible per CLAUDE.md rule 7: regenerates reading_<letter>.txt from the
ciphertext.txt file(s) and the relevant key_*.tsv. --check recomputes in memory and
exits non-zero if a committed reading file is stale.

Grading:
  H  the CLEANED token (after thurloe_extract.py's own l/i->1, o->0 normalisation)
     parses as a bare integer that is a key in the relevant key_*.tsv.
  M  thurloe_extract.py itself marked the token doubtful (trailing '?' in CLEANED --
     not a clean 1-4 digit run even after normalisation).
  U  a clean integer that is simply not one of the few values the key covers (the
     overwhelming majority, since each system has ~600 real code elements and the
     published key gives only a dozen or so).
"""
import argparse
import csv
import re
import sys
from collections import Counter
from pathlib import Path

HERE = Path(__file__).resolve().parent

# (letter id, [row ciphertext.txt files in reading order], key file, reading-output file)
LETTERS = [
    ("P9", ["P9/ciphertext.txt"], "key_blake.tsv", "reading_P9.txt"),
    ("P11-13", ["P11/ciphertext.txt", "P12/ciphertext.txt", "P13/ciphertext.txt"], "key_montagu.tsv", "reading_P11-13.txt"),
    ("P14", ["P14/ciphertext.txt"], "key_montagu.tsv", "reading_P14.txt"),
    ("P15", ["P15/ciphertext.txt"], "key_montagu.tsv", "reading_P15.txt"),
    ("P17", ["P17/ciphertext.txt"], "key_downing.tsv", "reading_P17.txt"),
]

CLEANED_LINE_RE = re.compile(r"CLEANED: (.*)$")


def load_key(path):
    key = {}
    with open(path, encoding="utf-8") as f:
        for row in csv.DictReader(f, delimiter="\t"):
            key[int(row["value"])] = row["meaning"]
    return key


def cleaned_tokens(ciphertext_path):
    """Yield (lineno_tag, raw_cleaned_token) for every CLEANED line's tokens."""
    out = []
    for line in ciphertext_path.read_text(encoding="utf-8").split("\n"):
        m = CLEANED_LINE_RE.search(line)
        if not m:
            continue
        tag = line.split("\t", 1)[0]
        for tok in m.group(1).split():
            out.append((tag, tok))
    return out


def classify(token, key):
    """Return (kind, note) for one CLEANED token."""
    doubtful = token.endswith("?")
    core = token.rstrip("?").rstrip(".,;:")
    if doubtful:
        return "M", core
    if core.isdigit():
        n = int(core)
        if n in key:
            return "H", key[n]
        return "U", str(n)
    # punctuation-only or a stray non-numeral survivor (e.g. "qu'0n?" already
    # caught by doubtful above); anything else falls through as unread
    return "U", core


def decode_letter(letter_id, files, key):
    grades = Counter()
    out_lines = []
    for rel in files:
        for tag, tok in cleaned_tokens(HERE / rel):
            kind, note = classify(tok, key)
            grades[kind] += 1
            out_lines.append("%s\t%s\t%s\t%s" % (tag, tok, kind, note))
    return grades, out_lines


def render(letter_id, grades, out_lines):
    total = sum(grades.values())
    header = [
        "# Mechanical reading of Thurloe letter %s against Tomokiyo's partial key" % letter_id,
        "# (thurloe.htm), applied unchanged. Regenerate: python3 decode.py",
        "# Grades: H=%d M=%d U=%d (of %d cipher tokens total)" % (grades["H"], grades["M"], grades["U"], total),
        "#",
        "# Columns: djvu-line-tag  CLEANED-token  grade  decoded-value-or-token",
        "#" + "=" * 74,
    ]
    return "\n".join(header + out_lines) + "\n"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true")
    a = ap.parse_args()

    stale = False
    report = []
    for letter_id, files, keyfile, outfile in LETTERS:
        key = load_key(HERE / keyfile)
        grades, out_lines = decode_letter(letter_id, files, key)
        rendered = render(letter_id, grades, out_lines)
        out_path = HERE / outfile
        if a.check:
            if not out_path.exists() or out_path.read_text(encoding="utf-8") != rendered:
                print("STALE: %s" % outfile, file=sys.stderr)
                stale = True
        else:
            out_path.write_text(rendered, encoding="utf-8")
        total = sum(grades.values())
        report.append((letter_id, grades["H"], grades["M"], grades["U"], total))

    print("letter\tH\tM\tU\ttotal")
    for letter_id, h, m, u, total in report:
        print("%s\t%d\t%d\t%d\t%d" % (letter_id, h, m, u, total))

    if a.check and stale:
        sys.exit(1)


if __name__ == "__main__":
    main()
