#!/usr/bin/env python3
"""Extract the printed cipher-group passages for the 23 Thurloe items in
sources/ia-fulltext/thurloe-check.tsv into ciphers/thurloe-printed/<row>/ciphertext.txt.

For each row, reads the cached djvu text (sources/ia-fulltext/<identifier>_djvu.txt,
gitignored, fetched by tools/ia_numeral_runs.py), takes a window of OCR lines around
the row's reported ocr_lines range (padded, capped), and classifies each non-blank
line as a cipher-group line (mostly short numeral tokens, using the same detector
threshold as tools/ia_numeral_runs.py: NUM tokens >=70% of a line's tokens once it
has >=4 tokens) or a plain-text line. Cipher-group lines are written as a raw column
and a cleaned column (lowercase l/i -> 1, lowercase o -> 0, the same OCR-digit
normalisation ciphers/orange-nassau-1572/decode.py uses); a token that still is not
a clean 1-4 digit run after that substitution is marked with a trailing '?' in the
cleaned column. Plain-text lines are written as [PLAIN:"..."] with the line
verbatim. This is extraction only -- no decoding, no repair, no novelty wording.

    python3 tools/thurloe_extract.py --index sources/ia-fulltext/thurloe-check.tsv \
        --cache sources/ia-fulltext --out ciphers/thurloe-printed --pad 6 --cap 260

Reproducible: re-running against the same cached djvu text and thurloe-check.tsv
regenerates byte-identical output (deterministic classification, no randomness).
"""
import argparse
import csv
import os
import re

NUM = re.compile(r'^\d{1,4}[.,;:]?$')
DIGIT_SUBST = str.maketrans({'i': '1', 'I': '1', 'l': '1', 'L': '1', 'o': '0', 'O': '0'})

# The 5 letters (7 rows -- P11/P12/P13 are 3 clusters of the same Montagu letter)
# where Tomokiyo's cryptiana/web/thurloe.htm reconstructs the correspondent's own
# cipher system (Blake, Montagu x2, Protector-to-Blake-and-Montagu, Downing) from
# OTHER material -- not from a decipherment of this specific letter. P19/P21/P22/P23
# share a numeral STYLE with each other but have no Tomokiyo reconstruction and are
# NOT in this set.
KEYED_ROWS = {'P9', 'P11', 'P12', 'P13', 'P14', 'P15', 'P17'}


def parse_range(spec):
    """'46987' -> (46987, 46987); '15491-15531' -> (15491, 15531)."""
    spec = spec.strip()
    if '-' in spec:
        a, b = spec.split('-', 1)
        return int(a), int(b)
    return int(spec), int(spec)


def is_cipher_line(line):
    tk = line.split()
    if len(tk) < 4:
        return False
    return sum(1 for t in tk if NUM.match(t)) / len(tk) >= 0.7


def clean_token(tok):
    core = tok.rstrip('.,;:')
    trail = tok[len(core):]
    normalized = core.translate(DIGIT_SUBST)
    if normalized.isdigit() and 1 <= len(normalized) <= 4:
        return normalized + trail
    return normalized + trail + '?'


def load_djvu(cache, identifier):
    path = os.path.join(cache, identifier + '_djvu.txt')
    with open(path, encoding='utf-8', errors='ignore') as f:
        return f.read().split('\n')


def extract_row(row, cache, pad, cap):
    lo, hi = parse_range(row['ocr_lines'])
    lines = load_djvu(cache, row['identifier'])
    start = max(0, lo - 1 - pad)
    end = min(len(lines), hi + pad)
    if end - start > cap:
        # keep the reported range in full, trim padding evenly from both ends
        core_lo = max(0, lo - 1)
        core_hi = min(len(lines), hi)
        extra = cap - (core_hi - core_lo)
        extra = max(extra, 0)
        start = max(0, core_lo - extra // 2)
        end = min(len(lines), core_hi + extra // 2)
    out = []
    in_cipher_run = False
    for i in range(start, end):
        raw = lines[i]
        stripped = raw.strip()
        lineno = i + 1
        if not stripped:
            continue
        if is_cipher_line(stripped):
            tokens = stripped.split()
            cleaned = ' '.join(clean_token(t) for t in tokens)
            out.append('L%d\tCIPHER\tRAW: %s' % (lineno, stripped))
            out.append('L%d\tCIPHER\tCLEANED: %s' % (lineno, cleaned))
            in_cipher_run = True
        else:
            out.append('L%d\t[PLAIN:"%s"]' % (lineno, stripped.replace('"', "'")))
            in_cipher_run = False
    return start + 1, end, out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--index', default='sources/ia-fulltext/thurloe-check.tsv')
    ap.add_argument('--cache', default='sources/ia-fulltext')
    ap.add_argument('--out', default='ciphers/thurloe-printed')
    ap.add_argument('--pad', type=int, default=6)
    ap.add_argument('--cap', type=int, default=260)
    a = ap.parse_args()

    os.makedirs(a.out, exist_ok=True)
    index_rows = []
    with open(a.index, encoding='utf-8') as f:
        for row in csv.DictReader(f, delimiter='\t'):
            row_id = row['row']
            folder = os.path.join(a.out, row_id)
            os.makedirs(folder, exist_ok=True)
            win_start, win_end, body = extract_row(row, a.cache, a.pad, a.cap)
            n_cipher_lines = sum(1 for l in body if '\tCIPHER\tRAW:' in l)
            n_cipher_tokens = sum(
                len(l.split('CLEANED: ', 1)[1].split())
                for l in body if 'CLEANED:' in l
            )
            header = [
                '# Thurloe State Papers, %s, printed p.%s' % (row['identifier'], row.get('printed_page', '?')),
                '# Sender: %s' % row.get('sender', '?'),
                '# Recipient: %s' % row.get('recipient', '?'),
                '# Date: %s' % row.get('date', '?'),
                '# Cipher system: %s' % row.get('cipher_system', 'unidentified'),
                '# Prior work: %s' % row.get('prior_work', 'none found'),
                '# Notes: %s' % row.get('notes', ''),
                '#',
                '# As transcribed (OCR), never silently repaired. Source: Internet Archive',
                '# identifier %s, cached djvu text sources/ia-fulltext/%s_djvu.txt' % (row['identifier'], row['identifier']),
                '# (gitignored; re-fetch with tools/ia_numeral_runs.py), djvu-text line numbers',
                '# %d-%d (NOT printed page numbers -- OCR running heads are unreliable at these',
                '# positions; printed_page above is from thurloe-check.tsv\'s own leaf check).',
                '# Regenerate this file with: python3 tools/thurloe_extract.py',
                '#',
                '# Format: one line per OCR source line, tagged with its djvu-text line number.',
                '# [PLAIN:"..."] = surrounding clear text, kept verbatim for orientation, not a',
                '# cipher group. A CIPHER pair (RAW / CLEANED) = a line the detector (>=4 tokens,',
                '# >=70% look like 1-4 digit numerals) judged to be cipher-group text: RAW is the',
                '# OCR verbatim, CLEANED applies only the l/i->1, o->0 OCR-digit-misread',
                '# normalisation (ciphers/orange-nassau-1572/decode.py\'s convention); a token still',
                '# not a clean 1-4 digit run after that gets a trailing \'?\' -- doubtful, not fixed.',
                '# %d cipher-tagged lines, %d numeral tokens (raw count, before dedup) in this window.' % (n_cipher_lines, n_cipher_tokens),
                '#',
                '# ' + '=' * 74,
                '',
            ]
            header[11] = header[11] % (win_start, win_end)
            ciphertext_path = os.path.join(folder, 'ciphertext.txt')
            with open(ciphertext_path, 'w', encoding='utf-8') as out:
                out.write('\n'.join(header))
                out.write('\n'.join(body))
                out.write('\n')
            index_rows.append({
                'row': row_id,
                'identifier': row['identifier'],
                'window_lines': '%d-%d' % (win_start, win_end),
                'printed_page': row.get('printed_page', '?'),
                'sender': row.get('sender', '?'),
                'recipient': row.get('recipient', '?'),
                'date': row.get('date', '?'),
                'cipher_system': row.get('cipher_system', 'unidentified'),
                'n_cipher_lines': n_cipher_lines,
                'n_numeral_tokens_raw': n_cipher_tokens,
                'keyed': 'yes' if row_id in KEYED_ROWS else 'no',
            })

    index_path = os.path.join(a.out, 'index.tsv')
    with open(index_path, 'w', encoding='utf-8', newline='') as f:
        w = csv.DictWriter(f, fieldnames=list(index_rows[0].keys()), delimiter='\t')
        w.writeheader()
        w.writerows(index_rows)
    print('wrote %d ciphertext.txt files + %s' % (len(index_rows), index_path))


if __name__ == '__main__':
    main()
