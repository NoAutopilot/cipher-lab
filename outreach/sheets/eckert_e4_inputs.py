#!/usr/bin/env python3
"""Inputs for the Huntington E4 sample sheet (MQS-SHEETS-R, 9 Oct 2026): the per-token and key TSVs that
tools/decipher_sheet.py reads through --tokens-tsv / --key-tsv, re-derived from ciphers/eckert-1864 (ciphertext.txt, key.md,
decode.py), plus the line-crop table for mssEC 19 p.49 (pointer 8941).  python3 outreach/sheets/eckert_e4_inputs.py [--check]
Grades are decode.py's own (H = mssEC 41 key row). Words no key row covers are the sender's plain words (grade 'clear')."""
import os, re, sys
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
sys.path.insert(0, os.path.join(ROOT, 'ciphers', 'eckert-1864'))
import decode

IMG = '../../ciphers/eckert-1864/images/mssEC19_p8941.jpg'
# line bands in full-resolution px of images/mssEC19_p8941.jpg (2583 x 3051), read by eye from a 1000 px preview, 9 Oct 2026
BANDS = [(1338, 'header'), (1441, 'L1'), (1542, 'L2'), (1640, 'L3'), (1736, 'L4'), (1839, 'L5'), (1932, 'L6'), (2033, 'L7'), (2131, 'L8')]
HALF = 62


def build():
    blocks = decode.load_ciphertext()
    header, lines = next(b for b in blocks if b[0].startswith('E4 |'))
    key = decode.load_key()
    full = decode.entry_text(lines).split()
    # words per manuscript line (lines[0] is the header line; the last line is the plain: note)
    counts = [len(decode.entry_text([header, l]).split()) if l.strip() and not l.startswith('plain:') else 0 for l in lines[1:]]
    ntext = sum(counts)
    assert ntext == len(full), (ntext, len(full))
    toks = []
    decode.decode_entry(decode.entry_text(lines), key, tokens=toks)
    by_idx = {t[0]: t for t in toks}
    rows, used, pos, n = [], {}, 0, 0
    for li, c in enumerate(counts):
        if not c:
            continue
        pos = 0
        for k in range(c):
            w = full[n + k].rstrip('\\')
            pos += 1
            if (n + k) in by_idx:
                _, word, meaning, grade, kind = by_idx[n + k]
                rows.append((f'L{li + 1}', pos, word, meaning, grade))
                used[word.lower()] = (meaning, grade)
            else:
                rows.append((f'L{li + 1}', pos, w, w.strip(' .,;:'), 'clear'))
        n += c
    keyrows = []
    km = {}
    for l in open(os.path.join(ROOT, 'ciphers', 'eckert-1864', 'key.md'), encoding='utf-8'):
        m = re.match(r'\|\s*([^|]+?)\s*\|\s*([^|]+?)\s*\|\s*([A-Z])\s*\|\s*([^|]+?)\s*\|', l)
        if m:
            km.setdefault(m.group(1).lower(), (m.group(2), m.group(3), m.group(4)))
    for w, (mean, g) in sorted(used.items()):
        src = km.get(w, ('', '', 'key.md (term or table not in the code-word rows)'))[2]
        keyrows.append((w, mean, g, f'mssEC 41 {src}'))
    return rows, keyrows


def main():
    rows, keyrows = build()
    t = 'line\tpos\tsign\tvalue\tgrade\n' + ''.join('\t'.join(map(str, r)) + '\n' for r in rows)
    k = 'code\tvalue\tgrade\tsource\n' + ''.join('\t'.join(r) + '\n' for r in keyrows)
    li = 'line\timage\tx0\ty0\tx1\ty1\n' + ''.join(f'{lab}\t{IMG}\t250\t{y - HALF}\t2350\t{y + HALF}\n' for y, lab in BANDS if lab != 'header')
    out = {'eckert-e4-tokens.tsv': t, 'eckert-e4-key.tsv': k, 'eckert-e4-lines.tsv': li}
    bad = 0
    for name, txt in out.items():
        p = os.path.join(HERE, name)
        if '--check' in sys.argv:
            if not os.path.exists(p) or open(p).read() != txt:
                print('STALE', name); bad = 1
        else:
            open(p, 'w').write(txt)
    sys.exit(bad)

main()
