#!/usr/bin/env python3
"""Write ciphertext_f86.tsv: passA_f86/passB_f86 reconciled by eye against images/native/f168.jpg, f169.jpg
(24 Sept 2026). L13-L16 re-read from fresh native crops (bands centred on y=1740,1860,1988,2120 of f169).
Conf H = both passes agree and the reconciler saw no reason to change; M = changed, disputed, or at the gutter.
Clear-French words are in [brackets]; they are not cipher groups."""
import csv
from collections import OrderedDict

R = """L01 _18 15 19 _3 7 21 61 64 9 m _28 15 21 2 20 _21 m 15
L02 18 _30 9 37 19 _0 _34 M. 35 17 5 _14 17 _37 7 _3 7 21
L03 60 _28 15 21 33 18 19 _13 7 _26 _3 7 21 61 _14 15 71 21
L04 35 18 20 61 20 23 _12 19 36 M. _18 18 42 16 10 56
L05 71 20 30 7 _13 15 20 40 15 _11 71 _23 21 19 m 115 36 60 4 _13
L06 15 _11 30 _0 5 61 39 71 m 4 _22 24 18 _17 73 15 _11
L07 6 _16 _13 15 19 31 16 61 60 [mais] [aussy] 55 9 _0 9 71 36
L08 4 _13 15 _11 6 M. 35 17 5 _14 18 _16 _18 15 19 _20 18
L09 24 7 9 62 2 [et] [c'est] [ce] [qui] [donne] [lieu] [de] 36 _17 _11 21
L10 20 30 _28 15 21 18 6 16 10 _11 21 66 20 115 _1 7 19
L11 m _28 15 21 _0 21 61 m 31 7 8 _7 24 18 19 _0 21 19 71
L12 20 61 20 m 1 40 15 _11 20 m 42 18 5 20 _16 17 9 60
L13 61 20 37 _26 21 20 37 20 33 7 21 20 6 16 61 m _21
L14 24 18 59 46 _17 30 2 20 _21 7 18 2 1 41 4 19 36
L15 59 20 _22 31 24 7 36 _15 50 9 71 _7 m 9 19 78 18
L16 62 2 7 m 31 7 8 _7 24 18 19 2 20 21 _4 9 62 21"""

NOTES = {
    ('L01', 4): 'curly 3-shaped glyph, passes read _7',
    ('L02', 16): 'curly 3-shaped glyph, passes read _7',
    ('L03', 11): 'curly 3-shaped glyph, passes read _7',
    ('L01', 5): 'by eye single 7 (passes 9/4)',
    ('L02', 5): 'by eye 19 (passes 29)',
    ('L02', 14): 'passes _37/_97',
    ('L03', 5): 'by eye 33 (A 37)',
    ('L04', 16): 'by eye 56 (passes 86/96); a ; stands before it',
    ('L09', 4): 'clear-word spacing only',
    ('L14', 12): '2 1 spaced; could be one group 21',
    ('L10', 15): 'gutter crop shows overlined 1 then a space then 7; passes read _17 (A) / _7 (B)',
    ('L10', 16): 'see pos 15',
}
GUTTER = {'L09', 'L10', 'L11', 'L12', 'L13', 'L14', 'L15', 'L16'}


def passes():
    out = []
    for p in ('passA_f86.tsv', 'passB_f86.tsv'):
        L = OrderedDict()
        for r in csv.DictReader(open(p), delimiter='\t'):
            L.setdefault(r['line'], []).append(r['group'])
        out.append(L)
    return out


def main():
    A, B = passes()
    with open('ciphertext_f86.tsv', 'w') as f:
        f.write('line\tpos\tgroup\tconf\tnote\n')
        for ln in R.split('\n'):
            t = ln.split(); k, g = t[0], t[1:]
            a, b = A[k], B[k]
            for i, x in enumerate(g, 1):
                note = NOTES.get((k, i), '')
                if x.startswith('['):
                    f.write(f'{k}\t{i}\t{x}\tH\tclear French\n'); continue
                agree = len(a) == len(b) == len(g) and a[i-1] == b[i-1] == x
                conf = 'H' if agree and not note else 'M'
                if k in ('L13', 'L14', 'L15', 'L16'):
                    note = note or 'recropped, read by eye'
                if x.lstrip('_') in ('30', '36', '37', '33'):
                    note = (note + '; ' if note else '') + 'curly 3/7 glyph read as 3'
                if i == len(g) and k in GUTTER:
                    note = (note + '; ' if note else '') + 'at gutter, a further group may be hidden'; conf = 'M'
                f.write(f'{k}\t{i}\t{x}\t{conf}\t{note}\n')


if __name__ == '__main__':
    main()
