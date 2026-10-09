#!/usr/bin/env python3
"""Build key.tsv for Alonso Sanchez's cipher (Ko.9) from Tomokiyo's published reconstruction (SALAZ-KEY, 9 Oct 2026).

  python3 scripts/build_key.py            write key.tsv beside this folder
  python3 scripts/build_key.py --check    exit 1 if the committed key.tsv differs from a rebuild

Inputs, both already in the repository (nothing fetched):
  sources/cryptiana/keys/AlonsoSanchez_1.tsv            Tomokiyo's 177-row nomenclature (three-letter word codes), parsed
                                                        27 Sept 2026 from cryptiana.web.fc2.com/code/AlonsoSanchez.htm
  ciphers/rah-juan-manuel-1521/siblings/shapes.tsv      rows 'AS': the letter alphabet of Tomokiyo's AlonsoSanchez.png as
                                                        shape labels, read by eye at 3x by R11-RJMSIB, 6 Oct 2026
Key source: published (Satoshi Tomokiyo, Cryptiana, reconstructed from the contemporary decipherment of DECODE R9605,
1522 letters). Every row is grade M: a modern reconstruction from 1522 letters applied to 1524-1528 letters.
Alphabet signs are the shape vocabulary of shapes.tsv; a shape Tomokiyo draws under two letters reads 'a|b'; a shape
drawn grey or with '?' (firm=0) is marked in the note. Codes and shapes share no token (checked on build).
"""
import os, sys
HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ROOT = os.path.dirname(os.path.dirname(HERE))
NOMEN = os.path.join(ROOT, 'sources/cryptiana/keys/AlonsoSanchez_1.tsv')
SHAPES = os.path.join(ROOT, 'ciphers/rah-juan-manuel-1521/siblings/shapes.tsv')
OUT = os.path.join(HERE, 'key.tsv')
SRC_A = 'Tomokiyo AlonsoSanchez.png alphabet (shapes.tsv AS rows, R11-RJMSIB eye read)'
SRC_N = 'Tomokiyo AlonsoSanchez.htm nomenclature (sources/cryptiana/keys/AlonsoSanchez_1.tsv)'


def build():
    shapes = {}
    for line in open(SHAPES, encoding='utf-8'):
        p = line.rstrip('\n').split('\t')
        if p[0] != 'AS':
            continue
        letter, shape, firm = p[1], p[2], p[3].strip() == '1'
        shapes.setdefault(shape, []).append((letter, firm))
    rows = []
    for shape in sorted(shapes):
        ls = shapes[shape]
        vals = sorted(set('NULL' if l == 'null' else l for l, _ in ls))
        note = 'letter'
        if len(vals) > 1:
            note = 'Tomokiyo draws this shape under %s: ambiguous' % ' and '.join(vals)
        weak = [l for l, f in ls if not f]
        if weak:
            note += '; drawn grey or with ? under %s (firm=0)' % ','.join(weak)
        rows.append((shape, '|'.join(vals), 'M', SRC_A, note))
    rows.append(('q_dbar', 's', 'M', SRC_A, "Tomokiyo: 'a q with double bar is often affixed to a three-letter code' = plural -s"))
    codes = set()
    for line in open(NOMEN, encoding='utf-8'):
        if line.startswith('#') or line.startswith('sign\t'):
            continue
        p = line.rstrip('\n').split('\t')
        if len(p) < 2:
            continue
        note = p[4] if len(p) > 4 else ''
        note = 'word code' + ('; ' + note.split('; ', 1)[1] if '; ' in note else '')
        rows.append((p[0], p[1], 'M', SRC_N, note))
        codes.add(p[0])
    clash = codes & set(shapes)
    if clash:
        sys.exit('shape/code token clash: %s' % sorted(clash))
    head = ['# Alonso Sanchez (imperial ambassador, Venice) -> Charles V, cipher Ko.9. Key source: published -- Satoshi Tomokiyo,',
            '# Cryptiana, https://cryptiana.web.fc2.com/code/AlonsoSanchez.htm (reconstructed from DECODE R9605, 1522), credited.',
            '# Built by scripts/build_key.py (SALAZ-KEY, 9 Oct 2026); do not edit by hand. Grade M throughout: a 1522 key, items',
            '# 4 (1524) and 5 (1528) are 2-6 years later. Not for Lope de Soria (items 1-3: Ko.6 or Ko.16, spanish2C.htm).',
            'code\tvalue\tgrade\tsource\tnote']
    return '\n'.join(head + ['\t'.join(r) for r in rows]) + '\n'


if __name__ == '__main__':
    text = build()
    if '--check' in sys.argv:
        cur = open(OUT, encoding='utf-8').read() if os.path.exists(OUT) else ''
        print('key.tsv current' if cur == text else 'key.tsv STALE')
        sys.exit(0 if cur == text else 1)
    open(OUT, 'w', encoding='utf-8').write(text)
    print('wrote %s (%d rows)' % (OUT, text.count('\n') - 5))
