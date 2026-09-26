#!/usr/bin/env python3
"""AX2-BLANKS unit 1: every occurrence of codes 156 and 182 in every transcribed
letter (this target's ciphertext_*.tsv plus ../jan-van-nassau-1572-75's), with
the 12 tokens either side decoded under key_full.tsv (names in [brackets]).
Handles the several ciphertext schemas found on disk (line/position/sign/...,
run/pos/token/kind/..., line/pos/token/conf, line/idx/token/conf/briefnr).
Run: python3 ax2_blanks/contexts.py
"""
import csv
import glob
import os

HERE = os.path.dirname(os.path.abspath(__file__))
TARGET = os.path.dirname(HERE)
SIBLING = os.path.join(os.path.dirname(TARGET), "jan-van-nassau-1572-75")
CODES = ("156", "182")


def load_key_full(path):
    key = {}
    with open(path, newline="") as f:
        for row in csv.DictReader(f, delimiter="\t"):
            key[row["code"]] = (row["value"], row["grade"])
    return key


def load_rows(path):
    """Return a list of (line_id, token_str) in file order, skipping comments/blank."""
    rows = []
    with open(path, newline="") as f:
        lines = [l for l in f if not l.startswith("#") and l.strip()]
    if not lines:
        return rows
    header = lines[0].rstrip("\n").split("\t")
    reader = csv.DictReader(lines[1:], fieldnames=header, delimiter="\t")
    # figure out which column holds the token/sign and which holds the line id
    line_col = "line" if "line" in header else ("run" if "run" in header else header[0])
    tok_col = "sign" if "sign" in header else ("token" if "token" in header else header[2])
    for row in reader:
        if row is None:
            continue
        lid = row.get(line_col, "")
        tok = (row.get(tok_col) or "").strip()
        if tok == "":
            continue
        rows.append((lid, tok))
    return rows


def clean_token(tok):
    """Strip clear-text prefixes ('=' , 'w:') -> is_clear, display string."""
    if tok.startswith("="):
        return True, tok[1:]
    if tok.startswith("w:"):
        return True, tok[2:]
    if tok in ("[blank]",):
        return True, tok
    return False, tok


def decode_tok(tok, key):
    is_clear, disp = clean_token(tok)
    if is_clear:
        return disp
    val = key.get(tok)
    if val is None:
        return tok
    value, grade = val
    if value == "NULL":
        return f"{tok}[NULL]"
    return f"{tok}[{value}]"


def is_excerpt_label(lid):
    """5797's convention: isolated 'spot'/'control' excerpts around one blank each,
    not a continuous page transcription -- crossing into the next label here would
    stitch together two unrelated places on the leaf, not real neighbouring context."""
    l = lid.lower()
    return "spot" in l or "control" in l


def context_window(rows, idx, n=12):
    lid = rows[idx][0]
    lo = idx
    while lo > 0 and lo > idx - n and not (is_excerpt_label(lid) and rows[lo - 1][0] != lid):
        lo -= 1
    hi = idx + 1
    while hi < len(rows) and hi < idx + 1 + n and not (is_excerpt_label(lid) and rows[hi][0] != lid):
        hi += 1
    before = rows[lo:idx]
    after = rows[idx + 1:hi]
    return before, after


def main():
    key = load_key_full(os.path.join(TARGET, "key_full.tsv"))
    files = sorted(glob.glob(os.path.join(TARGET, "ciphertext_*.tsv"))) + sorted(
        glob.glob(os.path.join(SIBLING, "ciphertext_*.tsv"))
    )
    out_path = os.path.join(HERE, "contexts.tsv")
    with open(out_path, "w", newline="") as out:
        w = csv.writer(out, delimiter="\t")
        w.writerow(["file", "line", "code", "before_12", "after_12"])
        for path in files:
            fname = os.path.relpath(path, os.path.dirname(TARGET))
            rows = load_rows(path)
            for i, (lid, tok) in enumerate(rows):
                if tok in CODES:
                    before, after = context_window(rows, i, 12)
                    before_s = " ".join(decode_tok(t, key) for _, t in before)
                    after_s = " ".join(decode_tok(t, key) for _, t in after)
                    w.writerow([fname, lid, tok, before_s, after_s])
                    print(f"{fname}\t{lid}\t{tok}")
                    print(f"  before: {before_s}")
                    print(f"  after:  {after_s}")
    print(f"\nwrote {out_path}")


if __name__ == "__main__":
    main()
