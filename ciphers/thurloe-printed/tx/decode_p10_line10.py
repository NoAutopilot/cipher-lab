#!/usr/bin/env python3
"""P10 (Blake to the Protector, 6 July 1655), p.620 line 10: Birch's own print glosses only
the last 8 of this line's 22 cipher tokens ("e t u r e t h e", right-aligned under line 9's
gloss row; see NOTES.md s.18 and P10/image_transcription.tsv). This script looks the other
14 up in key_blake_extended.tsv (this letter's own pooled key, P8-P10) and key_montagu_extended.tsv
(a different correspondent's pool, comparison only) and reports per-token grades.

Usage: python3 decode_p10_line10.py [--check]
--check exits 1 if the committed reading_P10_L10.tsv differs from a fresh run.
"""
import csv
import re
import sys
import os

HERE = os.path.dirname(os.path.abspath(__file__))
TARGET = os.path.dirname(HERE)
sys.path.insert(0, HERE)
from common import load_key

TRANSCRIPTION = os.path.join(TARGET, 'P10', 'image_transcription.tsv')
BLAKE_KEY = os.path.join(TARGET, 'key_blake_extended.tsv')
MONTAGU_KEY = os.path.join(TARGET, 'key_montagu_extended.tsv')
OUT = os.path.join(HERE, 'reading_P10_L10.tsv')

# Birch's own gloss for line 10 (image_transcription.tsv line 9, kind=interlinear, right-aligned
# under line 10's cipher row): 8 letters "e t u r e t h e" for the *last* 8 of line 10's 22 tokens.
PRINTED_GLOSS = list("eturethe")


def load_line10_tokens():
    with open(TRANSCRIPTION, newline='') as f:
        rows = list(csv.reader(f, delimiter='\t'))
    for row in rows:
        if len(row) >= 4 and row[0] == '620' and row[1] == '10' and row[2] == 'cipher':
            text = row[3]
            break
    else:
        raise SystemExit("line 10 cipher row not found in " + TRANSCRIPTION)
    toks = [t.rstrip('.') for t in text.split() if re.match(r'^\d+\.?$', t)]
    return toks


def build_reading():
    tokens = load_line10_tokens()
    n_glossed = len(PRINTED_GLOSS)
    n_unglossed = len(tokens) - n_glossed
    blake = load_key(BLAKE_KEY)
    montagu = load_key(MONTAGU_KEY)
    rows = []
    for i, v in enumerate(tokens):
        pos = i + 1
        printed = PRINTED_GLOSS[i - n_unglossed] if i >= n_unglossed else ''
        b = blake.get(v)
        m = montagu.get(v)
        rows.append({
            'pos': pos,
            'value': v,
            'printed_gloss': printed,
            'blake_meaning': b['meaning'] if b else '',
            'blake_grade': b['grade'] if b else 'U',
            'montagu_meaning': m['meaning'] if m else '',
            'montagu_grade': m['grade'] if m else 'U',
            'status': 'glossed_in_print' if printed else 'unglossed_in_print',
        })
    return rows, n_unglossed


def write_reading(rows, path=OUT):
    with open(path, 'w', newline='') as f:
        w = csv.DictWriter(f, fieldnames=['pos', 'value', 'printed_gloss', 'blake_meaning',
                                           'blake_grade', 'montagu_meaning', 'montagu_grade',
                                           'status'], delimiter='\t')
        w.writeheader()
        for r in rows:
            w.writerow(r)


def summarize(rows, n_unglossed):
    unglossed = [r for r in rows if r['status'] == 'unglossed_in_print']
    assert len(unglossed) == n_unglossed
    blake_read = [r for r in unglossed if r['blake_grade'] != 'U']
    montagu_read = [r for r in unglossed if r['montagu_grade'] != 'U']
    both_read = [r for r in unglossed if r['blake_grade'] != 'U' and r['montagu_grade'] != 'U']
    print(f"Line 10: {len(rows)} cipher tokens total, {n_unglossed} unglossed by Birch's print, "
          f"{len(rows) - n_unglossed} glossed.")
    print(f"key_blake_extended.tsv (this letter's own pool, P8-P10): resolves "
          f"{len(blake_read)}/{n_unglossed} of the unglossed tokens.")
    for r in blake_read:
        print(f"  pos {r['pos']:>2} value {r['value']:>3} -> {r['blake_meaning']!r} "
              f"(grade {r['blake_grade']})")
    print(f"key_montagu_extended.tsv (different correspondent's pool, comparison only): resolves "
          f"{len(montagu_read)}/{n_unglossed}.")
    for r in montagu_read:
        print(f"  pos {r['pos']:>2} value {r['value']:>3} -> {r['montagu_meaning']!r} "
              f"(grade {r['montagu_grade']})")
    print(f"Both keys agree on a reading (not necessarily the same letter) for "
          f"{len(both_read)}/{n_unglossed}.")
    still_unread = [r for r in unglossed if r['blake_grade'] == 'U' and r['montagu_grade'] == 'U']
    print(f"Unread by either key: {len(still_unread)}/{n_unglossed} -> values "
          f"{[r['value'] for r in still_unread]}")
    # English sense check: blake-key reading of the whole 22-token line, in order.
    blake_line = ''.join(r['blake_meaning'] or '_' for r in rows)
    print(f"Whole-line blake-key reading (unglossed + glossed positions, '_' = not in key):")
    print(f"  {blake_line}")
    printed_tail = ''.join(PRINTED_GLOSS)
    print(f"Birch's own printed tail (positions {n_unglossed + 1}-{len(rows)}): {printed_tail!r}")


def main():
    check = '--check' in sys.argv
    rows, n_unglossed = build_reading()
    if check:
        if not os.path.exists(OUT):
            print(f"FAIL: {OUT} does not exist", file=sys.stderr)
            sys.exit(1)
        with open(OUT, newline='') as f:
            committed = f.read()
        import io
        buf = io.StringIO()
        w = csv.DictWriter(buf, fieldnames=['pos', 'value', 'printed_gloss', 'blake_meaning',
                                             'blake_grade', 'montagu_meaning', 'montagu_grade',
                                             'status'], delimiter='\t')
        w.writeheader()
        for r in rows:
            w.writerow(r)
        fresh = buf.getvalue()
        if fresh != committed:
            print("FAIL: committed reading_P10_L10.tsv is stale", file=sys.stderr)
            sys.exit(1)
        print("OK: reading_P10_L10.tsv matches a fresh run")
        summarize(rows, n_unglossed)
        return
    write_reading(rows)
    summarize(rows, n_unglossed)


if __name__ == '__main__':
    main()
