#!/usr/bin/env python3
"""Build ciphertext_verified.tsv from verified_lines.txt (the image-read transcription of letter 602)
and record every difference from the OCR token list tokens.tsv (rule 2: image over OCR).

Classes: NUM (a numeral group, marks kept in `raw`, `value` is the bare number), SYM (a printed
letter-symbol among the numerals: r rr nn ee gg ll u d aa H t n W. mm 0), CLEAR (plain words).
    python3 build_verified.py [--check]
"""
import csv, difflib, re, sys, io, os
HERE = os.path.dirname(os.path.abspath(__file__))
SYMS = {'r', 'rr', 'nn', 'ee', 'gg', 'll', 'u', 'd', 'aa', 'H', 't', 'n', 'W', 'mm', '0'}


def tokens():
    out = []
    for ln in open(os.path.join(HERE, 'verified_lines.txt'), encoding='utf-8'):
        if ln.startswith('#') or not ln.strip():
            continue
        loc, text = ln.rstrip('\n').split('\t')
        text = text.split('[DATELINE]')[0]
        for raw in text.split():
            parts = raw.split('.') if re.fullmatch(r'\d+\.\d+', raw) else [raw]
            for p in parts:
                core = p.rstrip('.,;:')
                m = re.fullmatch(r'(\d{1,4})(["°½]?)', core)
                if m and core != '0':
                    out.append((loc, 'NUM', p, m.group(1), m.group(2)))
                elif core in SYMS:
                    out.append((loc, 'SYM', p, core, ''))
                else:
                    out.append((loc, 'CLEAR', p, core, ''))
    return out


def ocr_tokens():
    rows = list(csv.DictReader(open(os.path.join(HERE, 'tokens.tsv'), encoding='utf-8'), delimiter='\t'))
    return [r['raw'] for r in rows]


def build():
    toks = tokens()
    ocr = ocr_tokens()
    key = lambda s: s.rstrip('.,;:').replace('°', '').replace('*', '').replace('"', '')
    sm = difflib.SequenceMatcher(a=[key(t) for t in ocr], b=[key(t[2]) for t in toks], autojunk=False)
    change = [''] * len(toks)
    for op, a0, a1, b0, b1 in sm.get_opcodes():
        if op == 'equal':
            continue
        for j in range(b0, b1):
            change[j] = f"{op}: OCR '{' '.join(ocr[a0:a1])}'"
        if op == 'delete':
            if b0 < len(change):
                change[b0] = (change[b0] + '; ' if change[b0] else '') + f"OCR extra '{' '.join(ocr[a0:a1])}' dropped"
    buf = io.StringIO()
    w = csv.writer(buf, delimiter='\t', lineterminator='\n')
    w.writerow(['pos', 'page_line', 'class', 'raw', 'value', 'mark', 'grade', 'change_from_ocr'])
    for i, (t, c) in enumerate(zip(toks, change), 1):
        grade = 'H' if t[1] != 'SYM' else 'M'  # printed tokens read off the image; SYM identity as a cipher sign is uncertain
        w.writerow([i, t[0], t[1], t[2], t[3], t[4], grade, c])
    return buf.getvalue()


if __name__ == '__main__':
    out = build()
    path = os.path.join(HERE, 'ciphertext_verified.tsv')
    if '--check' in sys.argv:
        sys.exit(0 if open(path, encoding='utf-8').read() == out else 1)
    open(path, 'w', encoding='utf-8').write(out)
