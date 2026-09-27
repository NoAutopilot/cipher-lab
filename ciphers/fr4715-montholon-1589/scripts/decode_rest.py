#!/usr/bin/env python3
"""Decode the 'rest of f.81r' (lines beyond Tomokiyo's printed opening) from witness_signs.tsv,
grading every token per CLAUDE.md rule 4. MONT-4715, 27 Sept 2026.

    python3 scripts/decode_rest.py witness/witness_signs.tsv keys/key_vieuville_nevers.tsv L18 L36

Grades: H = letter homophone decoded straight from keys/key_vieuville_nevers.tsv (Tomokiyo's key
table). M = a dotted word-code resolved from a named source (aligned_dump.txt's own gloss for this
letter, or nevers.htm's fr.3633 list for a sibling letter, marked as such). I = illegible, unmatched,
or an unresolved dotted code (no named source gives its value) -- never guessed.
"""
import sys
import csv

# Word-codes this letter's own printed alignment (aligned_dump.txt) resolves -- grade M, source
# "aligned_dump.txt (this letter's own alignment)".
OWN_GLOSS = {
    "47": "qui", "30": "ma", "41": "par", "65": "comme", "16": "de", "11": "au", "20": "est",
    "48": "quil", "42": "pour", "19": "et", "46": "que", "25": "la", "35": "ne", "50": "se",
    "99": "vous", "28": "luy", "64": "catholique", "75": "faire", "52": "si", "22": "je",
    "31": "me", "40": "ou", "27": "les", "14": "ce",
}
# fr.3633 sibling letter's list (nevers.htm) -- only used where OWN_GLOSS has no value; grade M with
# a "sibling letter, unconfirmed for this letter" caveat, per NOTES.md's own caution.
SIBLING_GLOSS = {
    "16": "de", "19": "et", "20": "est", "24": "il", "25": "la", "26": "le", "35": "ne", "36": "na",
    "40": "ou", "42": "pour", "43": "plus", "46": "que", "48": "quil", "11": "villes",
    "76": "gens de pied", "88": "duc", "93": "monsieur",
}


def load_key_values(path):
    rows = {}
    with open(path, encoding="utf-8") as f:
        header = None
        i = 0
        for ln in f:
            ln = ln.rstrip("\n")
            if not ln.strip() or ln.startswith("#"):
                continue
            cols = ln.split("\t")
            if header is None:
                header = cols
                continue
            i += 1
            rows[i] = dict(zip(header, cols))
    return rows


def main():
    signs_path, key_path, lo, hi = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]
    key_rows = load_key_values(key_path)
    lo_n, hi_n = int(lo[1:]), int(hi[1:])

    grades = {"H": 0, "M": 0, "I": 0}
    out_lines = []
    cur_line = None
    cur_tokens = []

    def flush():
        if cur_line is not None:
            out_lines.append((cur_line, "".join(cur_tokens)))

    with open(signs_path, encoding="utf-8") as f:
        reader = csv.DictReader(f, delimiter="\t")
        for r in reader:
            line = r["line"]
            if not (line.startswith("L") and line[1:].isdigit()):
                continue
            n = int(line[1:])
            if not (lo_n <= n <= hi_n):
                continue
            if line != cur_line:
                flush()
                cur_line = line
                cur_tokens = []
            key_row = r["key_row"].strip()
            note = r["shape_note"].strip()
            if key_row == "#PLAIN":
                cur_tokens.append(f" [{note}] ")
                continue
            if note.startswith("dotted:"):
                digits = note.split(":", 1)[1].lstrip("'")
                if digits in OWN_GLOSS:
                    cur_tokens.append(f"[{OWN_GLOSS[digits]}]")
                    grades["M"] += 1
                elif digits in SIBLING_GLOSS:
                    cur_tokens.append(f"[{SIBLING_GLOSS[digits]}?]")
                    grades["M"] += 1
                else:
                    cur_tokens.append(f"<'{digits}?>")
                    grades["I"] += 1
                continue
            if key_row in ("?", ""):
                cur_tokens.append("_")
                grades["I"] += 1
                continue
            row = key_rows.get(int(key_row))
            if row is None:
                cur_tokens.append("_")
                grades["I"] += 1
                continue
            cur_tokens.append(row["value"])
            grades["H"] += 1
    flush()

    total = sum(grades.values())
    for line, text in out_lines:
        print(f"{line}\t{text}")
    print("---", file=sys.stderr)
    print(f"grades: H={grades['H']} M={grades['M']} I={grades['I']} total={total}", file=sys.stderr)
    if total:
        print(f"unread fraction (I / total): {grades['I']/total:.3f}", file=sys.stderr)


if __name__ == "__main__":
    main()
