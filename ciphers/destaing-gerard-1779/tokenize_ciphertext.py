#!/usr/bin/env python3
"""tokenize_ciphertext.py: split ciphertext.txt into ciphertext.tsv (position, code_idx, kind, token, context).

d'Estaing to Gerard, 30 Apr 1779 (Clinton Papers vol.64:14). The transcription has one cipher-bearing
line (line 3) that runs CODE numbers, switches to a CLEAR French clause naming "le 9 de mars dernier"
(which itself contains a plain digit "9" -- not a code), then back to CODE numbers, framed by a CLEAR
dateline/salutation before it and a CLEAR closing paragraph + signature after it. A naive \\d{1,3} regex
over the raw token stream over-counts by 2 (the dateline's "30" and the embedded "9"); this script uses
the document structure instead, splitting line 3 at the "Je me flatte" / "si ce la est" clause boundaries
so only the two genuine cipher runs are tagged CODE.

Usage: python3 tokenize_ciphertext.py ciphertext.txt --out ciphertext.tsv
"""
import argparse
import sys

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("infile")
    ap.add_argument("--out", required=True)
    args = ap.parse_args()

    with open(args.infile, encoding="utf-8") as f:
        raw_lines = f.read().splitlines()

    header = raw_lines[0]
    salutation = raw_lines[1]
    cipher_line = raw_lines[2]
    closing_lines = [ln for ln in raw_lines[3:] if ln.strip()]

    clause_start = cipher_line.index("Je me flatte")
    clause_end = cipher_line.index("si ce la est") + len("si ce la est")
    seg_a = cipher_line[:clause_start].strip()
    seg_clause = cipher_line[clause_start:clause_end].strip()
    seg_b = cipher_line[clause_end:].strip()

    rows = []  # (pos, code_idx, kind, token, before, after, line_role)
    all_tokens = []  # (token, kind, line_role) in document order

    def add(tok, kind, role):
        all_tokens.append((tok, kind, role))

    for tok in header.split():
        add(tok, "CLEAR", "HEADER")
    for tok in salutation.split():
        add(tok, "CLEAR", "SALUTATION")
    for tok in seg_a.split():
        add(tok, "CODE", "BODY_CODE_A")
    for tok in seg_clause.split():
        add(tok, "CLEAR", "BODY_CLEAR_CLAUSE")
    for tok in seg_b.split():
        add(tok, "CODE", "BODY_CODE_B")
    for ln in closing_lines:
        for tok in ln.split():
            add(tok, "CLEAR", "CLOSING")

    code_idx = 0
    for i, (tok, kind, role) in enumerate(all_tokens):
        before = all_tokens[i - 1][0] if i > 0 else ""
        after = all_tokens[i + 1][0] if i + 1 < len(all_tokens) else ""
        if kind == "CODE":
            rows.append((i, code_idx, kind, tok, before, after, role))
            code_idx += 1
        else:
            rows.append((i, "", kind, tok, before, after, role))

    with open(args.out, "w", encoding="utf-8") as f:
        f.write("pos\tcode_idx\tkind\ttoken\tbefore\tafter\tline_role\n")
        for pos, cidx, kind, tok, before, after, role in rows:
            f.write(f"{pos}\t{cidx}\t{kind}\t{tok}\t{before}\t{after}\t{role}\n")

    n_code = sum(1 for r in rows if r[2] == "CODE")
    n_clear = sum(1 for r in rows if r[2] == "CLEAR")
    distinct = len({r[3] for r in rows if r[2] == "CODE"})
    codes = [int(r[3]) for r in rows if r[2] == "CODE"]
    print(f"tokens: {len(rows)} total, {n_code} CODE ({distinct} distinct, max {max(codes)}), "
          f"{n_clear} CLEAR -> {args.out}", file=sys.stderr)

if __name__ == "__main__":
    main()
