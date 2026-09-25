#!/usr/bin/env python3
"""Extract Berthier-to-Napoleon Dec 1812 letters (Roman-numeral-marked) from
Chuquet 1912 vol.3 djvu OCR text, for the crib test in NOTES.md Y9 section.

Usage: python3 extract_chuquet_letters.py /tmp/chuquet_full.txt --out letters.json
"""
import re, sys, json, argparse

ROMAN_LINE = re.compile(r'^\s*([IVXLCDM]{1,7})\s*$')
NOISE_LINE = re.compile(
    r'^(LA\s+GU[EÈ]RRE\s+DE\s+RUSSIE|LA\s+GU[EÈ]RRE|\d{1,3}|LA\s+GUKRUE\s+DIù\s+RUSSIE|LA\s+GUKRRK\s+DE\s+RUSSIE)\s*$',
    re.IGNORECASE)
FOOTNOTE_START = re.compile(r'^\s*\d\.\s+\S')


def load_lines(path):
    with open(path, encoding='utf-8', errors='replace') as f:
        return f.read().split('\n')


def find_letters(lines, start_idx, end_idx):
    """Return dict roman -> {dateline, body_lines} for markers in [start_idx,end_idx)."""
    markers = []
    for i in range(start_idx, end_idx):
        m = ROMAN_LINE.match(lines[i])
        if m:
            markers.append((i, m.group(1)))
    letters = {}
    for k, (idx, roman) in enumerate(markers):
        body_start = idx + 1
        body_end = markers[k + 1][0] if k + 1 < len(markers) else end_idx
        block = lines[body_start:body_end]
        # first non-empty line after marker is the dateline
        dateline = None
        j = 0
        while j < len(block) and not block[j].strip():
            j += 1
        if j < len(block):
            dateline = block[j].strip()
            j += 1
        body = block[j:]
        # drop footnote paragraphs (a line starting "N. " ... to blank line) and page-header noise
        clean = []
        skipping_footnote = False
        for ln in body:
            s = ln.strip()
            if not s:
                skipping_footnote = False
                continue
            if NOISE_LINE.match(s):
                continue
            if FOOTNOTE_START.match(s):
                skipping_footnote = True
                continue
            if skipping_footnote:
                continue
            clean.append(s)
        text = ' '.join(clean)
        text = re.sub(r'\s+', ' ', text).strip()
        letters[roman] = {'dateline': dateline, 'text': text}
    return letters


def roman_to_int(s):
    vals = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    total = 0
    prev = 0
    for ch in reversed(s):
        v = vals.get(ch, 0)
        if v < prev:
            total -= v
        else:
            total += v
            prev = v
    return total


if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument('txt')
    ap.add_argument('--out', required=True)
    ap.add_argument('--from-line', type=int, default=7100)
    ap.add_argument('--to-line', type=int, default=9600)
    args = ap.parse_args()

    lines = load_lines(args.txt)
    letters = find_letters(lines, args.from_line, args.to_line)
    # keep only plausible roman numerals (I..L range for this chapter) with a december dateline
    out = {}
    for roman, d in letters.items():
        n = roman_to_int(roman)
        if not (1 <= n <= 60):
            continue
        if not d['dateline']:
            continue
        if 'cembre' not in (d['dateline'] or '') and '1812' not in (d['dateline'] or ''):
            continue
        out[roman] = d
    json.dump(out, open(args.out, 'w'), ensure_ascii=False, indent=1)
    print(f'{len(out)} letters written to {args.out}')
    for roman in sorted(out, key=roman_to_int):
        d = out[roman]
        print(roman, '|', d['dateline'], '|', len(d['text'].split()), 'words')
