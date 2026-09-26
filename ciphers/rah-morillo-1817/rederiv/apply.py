#!/usr/bin/env python3
"""NX-MOR3: apply key_5186.tsv to this worker's own independent re-transcription
(ciphertext_rederiv.tsv) and write reading_rederiv.txt, one line per group:
  group N: <space-joined values, '?' for a code absent from the key>   (codes: ...)
Grade H throughout (key_5186.tsv is read from the leaf's own interlinear decipherment);
this script marks a code missing from the key as '?', it does not guess.
"""
import csv
import pathlib
import sys

HERE = pathlib.Path(__file__).parent
TARGET = HERE.parent


def load_key(path):
    key = {}
    with open(path, newline="") as f:
        lines = [line for line in f if not line.startswith("#")]
    for row in csv.DictReader(lines, delimiter="\t"):
        if not row.get("code"):
            continue
        key[row["code"]] = row["value"]
    return key


def load_ciphertext(path):
    groups = []
    with open(path, newline="") as f:
        lines = [line for line in f if not line.startswith("#")]
    for row in csv.DictReader(lines, delimiter="\t"):
        if not row or not row.get("group"):
            continue
        groups.append((row["group"], row["codes"].split(".")))
    return groups


def main():
    key = load_key(TARGET / "key_5186.tsv")
    groups = load_ciphertext(HERE / "ciphertext_rederiv.tsv")
    lines = []
    for gnum, codes in groups:
        values = [key.get(c, "?") for c in codes]
        lines.append(f"group {gnum}: {''.join(values)}   (codes: {'.'.join(codes)})")
    out = HERE / "reading_rederiv.txt"
    out.write_text(
        "# NX-MOR3 mechanical decode of this worker's own ciphertext_rederiv.tsv through\n"
        "# ciphers/rah-morillo-1817/key_5186.tsv (grade H). '?' = code absent from the key.\n"
        + "\n".join(lines)
        + "\n"
    )
    print(f"wrote {out}")
    for line in lines:
        print(line)


if __name__ == "__main__":
    sys.exit(main())
