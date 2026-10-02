#!/usr/bin/env python3
"""Extract Berthier-to-Napoleon Dec 1812 letters (Roman-numeral-marked) from
Chuquet 1912 vol.3 djvu OCR text, for the crib test in NOTES.md Y9 section.

Usage: python3 extract_chuquet_letters.py /tmp/chuquet_full.txt --out letters.json

Source: archive.org 1812laguerrederu03chuquoft_djvu.txt (Chuquet, 1812. La guerre de
Russie, 3e serie, 1912), note "45. Berthier a Napoleon" (djvu line 6365) up to note
"46. Murat a Napoleon" (line 8917). GF4b, 2 Oct 2026: the v1 run (lines 7100-9600)
started mid-chapter and ran into Murat's note 46, whose Roman keys II-XI overwrote
Berthier's; v1 output kept as letters_v1_mixedpool.json. Defaults now bound the run to
note 45, the OCR-damaged marker "1I[" (III) is mapped by --marker-fix, and letters
inside the note that are not Berthier's (Lefebvre a Berthier, 22/28 Dec) are dropped.
"""
import re, sys, json, argparse

ROMAN_LINE = re.compile(r'^\s*([IVXLCDM]{1,7})\s*$')
SKIP_LINES = set()  # line index (0-based) of a stray page-number 'marker'
MARKER_FIX = {}  # line index (0-based) -> roman, for OCR-damaged markers
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
        if i in SKIP_LINES:
            continue
        if i in MARKER_FIX:
            markers.append((i, MARKER_FIX[i]))
            continue
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
        letters.setdefault(roman, []).append({'dateline': dateline, 'text': text, 'djvu_line': idx + 1})
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
    ap.add_argument('--from-line', type=int, default=6365, help='1-based djvu line of note 45 header')
    ap.add_argument('--to-line', type=int, default=8917, help='1-based djvu line of note 46 header (exclusive)')
    ap.add_argument('--marker-fix', action='append', default=['6583:III', '7935:XXII'],
                    help='LINE:ROMAN for an OCR-damaged marker (1-based line)')
    ap.add_argument('--skip-line', type=int, action='append', default=[7123],
                    help='1-based line of a stray Roman-looking OCR line that is not a letter marker')
    ap.add_argument('--drop-author-re', default=r'\b\w+ +[aà] +Berthier\b',
                    help='drop a block whose first line names another writer to Berthier')
    args = ap.parse_args()

    for mf in args.marker_fix:
        ln, rn = mf.split(':')
        MARKER_FIX[int(ln) - 1] = rn
    SKIP_LINES.update(x - 1 for x in args.skip_line)
    lines = load_lines(args.txt)
    raw = find_letters(lines, args.from_line - 1, args.to_line - 1)
    letters = {}
    for roman, ds in raw.items():
      for d in ds:
        if d['dateline'] and re.search(args.drop_author_re, d['dateline']):
            print('dropped (not Berthier):', roman, '|', d['dateline'], '| djvu line', d['djvu_line'])
            continue
        if roman in letters:
            raise SystemExit(f'duplicate marker {roman} at djvu line {d["djvu_line"]}: range spans two notes')
        if d['dateline'] and not re.search(r'\d', d['dateline']):
            # no dateline printed (XXXIII): the first body line was taken as the dateline
            d['text'] = (d['dateline'] + ' ' + d['text']).strip()
            d['dateline'] = None
        d['source'] = ('Chuquet 1912, 1812. La guerre de Russie 3e serie, note 45 "Berthier a Napoleon", '
                       'archive.org 1812laguerrederu03chuquoft_djvu.txt line %d' % d['djvu_line'])
        letters[roman] = d
    # keep only plausible roman numerals (I..L range for this chapter) with a december dateline
    out = {}
    for roman, d in letters.items():
        n = roman_to_int(roman)
        if not (1 <= n <= 60):
            continue
        if d['dateline'] and 'cembre' not in d['dateline'] and '1812' not in d['dateline']:
            continue
        out[roman] = d
    json.dump(out, open(args.out, 'w'), ensure_ascii=False, indent=1)
    print(f'{len(out)} letters written to {args.out}')
    for roman in sorted(out, key=roman_to_int):
        d = out[roman]
        print(roman, '|', d['dateline'], '|', len(d['text'].split()), 'words')
