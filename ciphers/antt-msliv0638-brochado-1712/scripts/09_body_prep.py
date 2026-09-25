#!/usr/bin/env python3
"""Prep body_ciphertext.tsv for tools/decode_key.py (PX-BRODEC, 25 Sept 2026, step 1).

Two small, reproducible edits to body_ciphertext.tsv, both idempotent:

1. Add a 'conf' column duplicating the existing 'grade' column (H/M, the transcription-pass agreement
   grade set by PX-BROBODY/PX-BROBODY2). tools/decode_key.py looks for a column literally named
   'conf'/'confidence' to force a token to grade M regardless of the key's own per-code grade
   (its uncertain_conf default includes 'M'); this repo's shared script is not modified (out of this
   worker's file scope) -- this column lets it do that job unmodified. The original 'grade' column is
   left in place, unchanged, as the human-readable label PX-BROBODY's notes already describe.
2. Correct letter_no from 'none' to '134' for the m0275/m0276 rows: PX-BROBODY2 (NOTES.md) read page
   134 directly off m0273 and showed m0274-m0277 are one continuous letter with no cipher on m0273/
   m0274 itself; m0275's run continues directly into m0276-r1 with no intervening plain text. This is
   a metadata correction from an already-established fact in NOTES.md, not a ciphertext repair (rule 2
   is about the transcribed tokens, which are untouched).

Run: python3 scripts/09_body_prep.py   (from the target folder; rewrites body_ciphertext.tsv in place)
"""
import csv
import os

PATH = os.path.join(os.path.dirname(__file__), '..', 'body_ciphertext.tsv')


def main():
    with open(PATH, encoding='utf-8', newline='') as f:
        rows = list(csv.reader(f, delimiter='\t'))
    header, body = rows[0], rows[1:]
    if 'conf' not in header:
        header = header + ['conf']
        gi = rows[0].index('grade')
        for r in body:
            r.append(r[gi])
    li = header.index('leaf')
    ni = header.index('letter_no')
    for r in body:
        if r[li] in ('m0275', 'm0276') and r[ni] == 'none':
            r[ni] = '134'
    with open(PATH, 'w', encoding='utf-8', newline='') as f:
        w = csv.writer(f, delimiter='\t')
        w.writerow(header)
        w.writerows(body)
    print(f'wrote {PATH}: {len(header)} columns, {len(body)} rows')


if __name__ == '__main__':
    main()
