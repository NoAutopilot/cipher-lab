#!/usr/bin/env python3
"""AX-MERGE3: known-answer test of the 4614 period-decipherment conflicts against key_full on the Groen-printed
letters 5810, 5811, 4503 (gate: NOTES.md, section AX-MERGE3, written before this ran).

Uses axnames/align_names.py unchanged (same MAXL/BASE/PER, per-page semi-global DP, same Groen spans). Codes 1-120
emit their key_full value (identical to key.tsv for 1-120); every code > 120 stays free as in AX-NAMES, except the
code under test, which is fixed to the tested value (NULL emits nothing). Counts the aligner's own exact matches per
letter pair, plus, per occurrence of the tested code, whether its emitted letter(s) landed on the same printed letter.
The known-answer pair 4613/4615 ('sib') is run too, for information only (not part of the gate).

  python3 axmerge3/conflict_test.py            write axmerge3/conflict_test.tsv and axmerge3/conflict_occ.tsv
  python3 axmerge3/conflict_test.py --check    exit 1 if either file is stale
"""
import csv, io, os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
T = os.path.dirname(HERE)
sys.path.insert(0, os.path.join(T, 'axnames'))
import align_names as A  # noqa: E402

CONFLICTS = [  # code, key_full value, 4614 period-decipherment value
    ('127', 'NULL', 'm'), ('129', 'NULL', 'm'), ('123', 'l', 'NULL'),
    ('107', 'k', 'i'), ('95', 'g', 'h'), ('57', 'z', 'x'),
]
GATE = ['5810', '5811', '4503']
INFO = ['sib']


def keyfull():
    with open(os.path.join(T, 'key_full.tsv')) as f:
        return {r['code']: r['value'] for r in csv.DictReader(f, delimiter='\t')}


def base(sign):
    if sign.startswith('='):
        return sign
    return sign.split('/')[0] if '/' in sign else sign


def run(letter, code, value, key):
    orig = A.emit

    def emit(sign, k):
        if base(sign) == code:
            return ('fix', '' if value == 'NULL' else A.letters(value))
        return orig(sign, k)
    A.emit = emit
    try:
        ct, spans = A.PAIRS[letter]
        pt = ''.join(A.letters(A.groen_body(*sp)) for sp in spans)
        toks = A.tokens(ct)
        pk = (lambda t: t[0].split('_')[0]) if letter == 'sib' else (lambda t: t[0].split('_')[1] if '_' in t[0] else t[0])
        pages = {}
        for t in toks:
            pages.setdefault(pk(t), []).append(t)
        matches = occ = occ_hit = 0
        occ_rows = []
        for pg, ptoks in pages.items():
            units, path, _ = A.align_page(ptoks, pt, key)
            for (ui, s, e) in path:
                ti, kind, v = units[ui]
                hit = kind == 'L' and e - s == 1 and A.mcost(v, pt[s]) < 0.5
                matches += hit
                line, pos, sign = ptoks[ti]
                if base(sign) == code and kind == 'L':
                    occ_hit += hit
                    occ_rows.append([letter, line, pos, sign, value, v, pt[s:e] or '-', int(hit),
                                     pt[max(0, s - 10):s], pt[e:e + 10]])
            occ += sum(1 for t in ptoks if base(t[2]) == code)
        return matches, occ, occ_hit, occ_rows
    finally:
        A.emit = orig


def build():
    key = keyfull()
    out = io.StringIO(); w = csv.writer(out, delimiter='\t', lineterminator='\n')
    w.writerow(['code', 'letter', 'occurrences', 'matches_keyfull', 'matches_4614', 'delta',
                'code_letters_hit_keyfull', 'code_letters_hit_4614', 'keyfull_value', 'v4614'])
    oo = io.StringIO(); ow = csv.writer(oo, delimiter='\t', lineterminator='\n')
    ow.writerow(['letter', 'line', 'pos', 'sign', 'tested_value', 'emitted', 'print_at', 'hit', 'ctx_left', 'ctx_right'])
    for code, kf, v4 in CONFLICTS:
        for letter in GATE + INFO:
            m1, n, h1, r1 = run(letter, code, kf, key)
            m2, _, h2, r2 = run(letter, code, v4, key)
            w.writerow([code, letter, n, m1, m2, m2 - m1, h1, h2, kf, v4])
            for r in r1 + r2:
                ow.writerow([r[0]] + r[1:])
    return out.getvalue(), oo.getvalue()


def main():
    a, b = build()
    pa, pb = os.path.join(HERE, 'conflict_test.tsv'), os.path.join(HERE, 'conflict_occ.tsv')
    if '--check' in sys.argv:
        ok = all(os.path.exists(p) and open(p).read() == t for p, t in ((pa, a), (pb, b)))
        print('up to date' if ok else 'stale'); sys.exit(0 if ok else 1)
    open(pa, 'w').write(a); open(pb, 'w').write(b)
    sys.stdout.write(a)


if __name__ == '__main__':
    main()
