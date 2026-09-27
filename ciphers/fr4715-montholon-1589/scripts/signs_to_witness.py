#!/usr/bin/env python3
"""Convert reconcile_passes.py's ciphertext_draft.tsv into the signs TSV tools/decode_witness.py takes.

MONT-4715, 27 Sept 2026. One-off for this target (not promoted to tools/ this job -- a future
worker calibrating a second witness against a homophonic key should consider generalising this).

Why not decode_witness.py's own 'nNN' numeral lookup: that lookup does a substring match against
the key file's 'sign' column in file order (`if digits in r["sign"]`), which is wrong whenever one
sign's digits are a substring of an earlier row's sign in the file (e.g. this key's row 22, sign
"1", is a substring of row 3's sign "10", which comes first in the file -- 'n1' would silently
resolve to row 3 (b) instead of row 22 (r)). This script does an exact string match instead.

    python3 scripts/signs_to_witness.py ciphertext_draft.tsv keys/key_vieuville_nevers.tsv OUT.tsv

Sign conventions from the blind passes: a bare digit string is a letter homophone (exact match
against the key's sign column); a leading apostrophe marks a dotted word-code group (key_row '?',
shape_note 'dotted'); 'F'/'T' are the two special glyphs transcribed as those letters by the
passes, mapped back to the key's printed glyphs before lookup; '[PLAIN:word]' is a clear
(un-enciphered) French word, passed through unchanged with key_row '#PLAIN', not decoded; '?' is
illegible, key_row '?'.
"""
import sys
import csv

def load_key(path):
    rows = []
    with open(path, encoding="utf-8") as f:
        header = None
        for ln in f:
            ln = ln.rstrip("\n")
            if not ln.strip() or ln.startswith("#"):
                continue
            cols = ln.split("\t")
            if header is None:
                header = cols
                continue
            rows.append(dict(zip(header, cols)))
    sign_to_row = {}
    for i, r in enumerate(rows, start=1):
        if r["sign"] in sign_to_row:
            raise SystemExit(f"duplicate sign {r['sign']!r} at rows {sign_to_row[r['sign']]} and {i}")
        sign_to_row[r["sign"]] = i
    return sign_to_row

def main():
    draft_path, key_path, out_path = sys.argv[1], sys.argv[2], sys.argv[3]
    sign_to_row = load_key(key_path)
    glyph_map = {"F": "♀", "T": "▽"}  # pass notation -> key file's printed glyphs (s, x)

    unmatched = []
    with open(draft_path, encoding="utf-8") as f, open(out_path, "w", encoding="utf-8") as out:
        reader = csv.DictReader(f, delimiter="\t")
        out.write("line\tpos\tkey_row\tshape_note\tconfidence\n")
        for r in reader:
            sign = r["sign"].strip()
            conf = r.get("confidence", "")
            if sign.startswith("[PLAIN:") and sign.endswith("]"):
                out.write(f"{r['line']}\t{r['position']}\t#PLAIN\t{sign}\t{conf}\n")
                continue
            if sign == "?" or sign == "":
                out.write(f"{r['line']}\t{r['position']}\t?\tillegible\t{conf}\n")
                continue
            note = ""
            lookup = sign
            if sign.startswith("'"):
                note = "dotted"
                out.write(f"{r['line']}\t{r['position']}\t?\tdotted:{sign}\t{conf}\n")
                continue
            lookup = glyph_map.get(sign, sign)
            row = sign_to_row.get(lookup)
            note = ""
            if row is None and len(lookup) > 1 and lookup[0] == "0":
                # A leading zero is common in the passes' output for the key's 1-digit
                # signs (1, 5); the key has no sign beginning with "0", so try without it.
                stripped = lookup.lstrip("0")
                if stripped in sign_to_row:
                    row = sign_to_row[stripped]
                    note = f"stripped-leading-zero:{sign}"
            if row is None:
                unmatched.append((r["line"], r["position"], sign))
                out.write(f"{r['line']}\t{r['position']}\t?\tunmatched:{sign}\t{conf}\n")
                continue
            out.write(f"{r['line']}\t{r['position']}\t{row}\t{note}\t{conf}\n")

    if unmatched:
        print(f"{len(unmatched)} unmatched (non-dotted, no exact key row) signs -- check by hand:", file=sys.stderr)
        for line, pos, sign in unmatched[:40]:
            print(f"  {line} pos={pos} sign={sign!r}", file=sys.stderr)

if __name__ == "__main__":
    main()
