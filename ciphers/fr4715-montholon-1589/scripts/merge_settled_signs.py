#!/usr/bin/env python3
"""Merge a targeted crop reconciliation of witness/disagreements.tsv into a v2 signs TSV.

MONT-4715B, 27 Sept 2026. Per CLAUDE.md Usage 6 ("reconciliation is a distinct priced step") and this
job's brief: three Sonnet subagents each looked at the source crops for a contiguous line range and
adjudicated witness/disagreements.tsv's 1,037 rows (one row per position where MONT-4715's two blind
passes disagreed), reporting the sign actually drawn, or '?' if genuinely undecidable, with a one-word
reason. This script takes their combined output plus witness/ciphertext_draft.tsv (the position of
record for every position the two passes already agreed on) and produces witness/witness_signs_v2.tsv,
using the same exact-match sign lookup as scripts/signs_to_witness.py (not decode_witness.py's own
'nNN' substring convention, fixed this job but not used by this target's own signs file).

    python3 scripts/merge_settled_signs.py witness/ciphertext_draft.tsv witness/disagreements.tsv \
        witness/settled_disagreements.tsv keys/key_vieuville_nevers.tsv witness/witness_signs_v2.tsv

settled_disagreements.tsv: line, col, chosen_sign, reason -- the three subagents' U1/U2/U3 output files
concatenated (one header row kept). A (line, col) pair present in disagreements.tsv but absent from
settled_disagreements.tsv is left at v1's ciphertext_draft reading (not silently dropped) and flagged
in this script's stderr summary.
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


GLYPH_MAP = {"F": "♀", "T": "▽"}  # pass notation -> key file's printed glyphs (s, x)


def sign_to_key_row(sign_to_row, sign):
    """Exact-match sign -> 1-based key row, with the same glyph map and leading-zero fallback as
    scripts/signs_to_witness.py. Returns (key_row_str, shape_note) where key_row_str is '?' if unmatched."""
    sign = sign.strip()
    lookup = GLYPH_MAP.get(sign, sign)
    row = sign_to_row.get(lookup)
    if row is None and len(lookup) > 1 and lookup[0] == "0":
        stripped = lookup.lstrip("0")
        if stripped in sign_to_row:
            return str(sign_to_row[stripped]), f"stripped-leading-zero:{sign}"
    if row is None:
        return "?", f"unmatched:{sign}"
    return str(row), ""


def main():
    draft_path, disagreements_path, settled_path, key_path, out_path = sys.argv[1:6]
    sign_to_row = load_key(key_path)

    with open(draft_path, encoding="utf-8") as f:
        draft_rows = list(csv.DictReader(f, delimiter="\t"))

    disputed = set()
    with open(disagreements_path, encoding="utf-8") as f:
        for r in csv.DictReader(f, delimiter="\t"):
            disputed.add((r["line"], r["col"]))

    settled = {}
    with open(settled_path, encoding="utf-8") as f:
        for r in csv.DictReader(f, delimiter="\t"):
            settled[(r["line"], r["col"])] = (r["chosen_sign"], r["reason"])

    missing = disputed - set(settled)
    settled_count = 0
    stayed_q = 0

    with open(out_path, "w", encoding="utf-8") as out:
        out.write("line\tpos\tkey_row\tshape_note\tconfidence\n")
        for r in draft_rows:
            key = (r["line"], r["position"])
            conf = r.get("confidence", "")
            if key in settled:
                sign, reason = settled[key]
                sign = sign.strip()
                if sign == "?":
                    stayed_q += 1
                    out.write(f"{r['line']}\t{r['position']}\t?\tundecidable\t{conf}\n")
                    continue
                if sign.startswith("'"):
                    settled_count += 1
                    out.write(f"{r['line']}\t{r['position']}\t?\tdotted:{sign}\t{conf}\n")
                    continue
                key_row, note = sign_to_key_row(sign_to_row, sign)
                if key_row == "?":
                    # settled to a definite sign that still isn't in the letter-homophone key
                    # (e.g. a word-code digit group with no visible dot) -- record the reading,
                    # not a guessed letter.
                    settled_count += 1
                    out.write(f"{r['line']}\t{r['position']}\t?\t{note}:reconciled\t{conf}\n")
                else:
                    settled_count += 1
                    out.write(f"{r['line']}\t{r['position']}\t{key_row}\t{note or 'reconciled:' + reason}\t{conf}\n")
            elif key in disputed:
                # a disputed position no subagent covered -- keep v1's draft reading, not dropped.
                sign = r["sign"].strip()
                if sign == "-" or sign == "":
                    out.write(f"{r['line']}\t{r['position']}\t?\tillegible\t{conf}\n")
                elif sign.startswith("'"):
                    out.write(f"{r['line']}\t{r['position']}\t?\tdotted:{sign}\t{conf}\n")
                else:
                    key_row, note = sign_to_key_row(sign_to_row, sign)
                    out.write(f"{r['line']}\t{r['position']}\t{key_row}\t{note}\t{conf}\n")
            else:
                # agreed position, unchanged from v1 -- reuse the same conversion as signs_to_witness.py.
                sign = r["sign"].strip()
                if sign == "-" or sign == "":
                    out.write(f"{r['line']}\t{r['position']}\t?\tillegible\t{conf}\n")
                elif sign.startswith("'"):
                    out.write(f"{r['line']}\t{r['position']}\t?\tdotted:{sign}\t{conf}\n")
                else:
                    key_row, note = sign_to_key_row(sign_to_row, sign)
                    out.write(f"{r['line']}\t{r['position']}\t{key_row}\t{note}\t{conf}\n")

    print(f"disputed positions: {len(disputed)}", file=sys.stderr)
    print(f"settled to a definite sign or reconciled reading: {settled_count}", file=sys.stderr)
    print(f"left '?' (undecidable): {stayed_q}", file=sys.stderr)
    if missing:
        print(f"WARNING: {len(missing)} disputed positions have no settled row, kept v1 reading:", file=sys.stderr)
        for line, col in sorted(missing)[:20]:
            print(f"  {line} col={col}", file=sys.stderr)


if __name__ == "__main__":
    main()
