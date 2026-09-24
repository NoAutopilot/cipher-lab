#!/usr/bin/env python3
"""Write ciphertext_f67.tsv: passA_f67/passB_f67 reconciled by eye against the Gallica natives of canvas 129 and 130
(btv1b9060495t f129/f130 native.jpg, fetched 24 Sept 2026 to a scratchpad, not committed; the folder is at its 30 MB cap).

Base: pass A, whose line labels are the 16 physical rows of canvas 129 (pass B merged rows 1+2 and 11+12 into one band
each and dropped a run of 10 groups in row 11). Pass B's bands are mapped onto pass A's rows and aligned per row with
difflib. Conf H = both passes agree at that position and the reconciler saw no reason to change it; M = settled by eye
from a disagreement, changed from what both passes wrote (the curly 3 convention below), or at the gutter.

Curly 3 (the f.86/f.88 convention, NOTES 'Folio 86-88' and 'f.88 tail'): this hand writes 3 with a rounded, descending
top that both passes read as 9, 7 or 2. Where the glyph on the image is that curly form it is read 3: 96/76/26 -> 36,
99 -> 39, 91 -> 31, 77 -> 33, 72 -> 32. Where the first stroke is a flat-topped 7 it is kept (f129 L02/3 _76, f130a L02/9 79).

--check exits 1 if ciphertext_f67.tsv is stale."""
import csv, difflib, sys
from collections import OrderedDict

HERE = __file__.rsplit('/', 1)[0] if '/' in __file__ else '.'
OUT = f'{HERE}/ciphertext_f67.tsv'
NONSIGN = {',', ';', '.', ':', '—', 'X'}

# pass B band -> pass A physical rows
BMAP = {'f129_L01': ['f129_L01', 'f129_L02'], 'f129_L10': ['f129_L11', 'f129_L12']}
for i in range(2, 10):
    BMAP[f'f129_L{i:02d}'] = [f'f129_L{i+1:02d}']
for i in range(11, 15):
    BMAP[f'f129_L{i:02d}'] = [f'f129_L{i+2:02d}']

# (row, pass-A pos) -> (group, reason). Settled by eye on the native.
SET = {
    ('f129_L01', 1): ('[PLAIN:en diburez parler a leurs Altesses Royalles]',
                      'clear French; A "Achrs.s.r Royallex", B "Alt.es Royalles"; "diburez" diplomatic (devrez)'),
    ('f129_L02', 17): ('36', 'curly 3 (B 96)'),
    ('f129_L03', 5): ('36', 'curly 3 (both 96)'), ('f129_L03', 9): ('36', 'curly 3 (both 96)'),
    ('f129_L03', 14): ('36', 'curly 3 (both 96)'),
    ('f129_L04', 14): ('36', 'curly 3 (A 96, B 36)'),
    ('f129_L06', 8): ('36', 'curly 3 (A 96, B 26)'),
    ('f129_L07', 2): ('36', 'curly 3 (A 96, B 26)'),
    ('f129_L07', 3): ('_5', 'long-s shaped 5 under the bar, as in 115 (both passes _6)'),
    ('f129_L07', 11): ('_6', 'bar over the 6 (A 6; B _6)'),
    ('f129_L07', 13): ('_16', 'small 1 under the bar before 6 (A _6, B _16)'),
    ('f129_L07', 19): ('154', 'written close, a slight gap before 4 (B 15 4); kept as one group, see f130a L04/5'),
    ('f129_L07', 22): ('_16', 'small 1 under the bar before 6 (both _6)'),
    ('f129_L08', 1): ('36', 'curly 3 convention (A 96); first stroke flatter than usual'),
    ('f129_L08', 2): ('_16', 'small 1 under the bar before 6 (both _6)'),
    ('f129_L08', 7): ('39', 'curly 3 (A 99, B 99)'),
    ('f129_L08', 14): ('36', 'curly 3 (both 96)'),
    ('f129_L08', 16): ('61', 'a small gap between 6 and 1 (B 6 1); kept as one group'),
    ('f129_L11', 3): ('36', 'curly 3 (A 76; B lost this run)'),
    ('f129_L11', 21): ('_6', 'bar over the 6 (A 6); B lost this run'),
    ('f129_L12', 11): ('_11', 'bar over 11 (A 11, B _11)'),
    ('f129_L12', 23): ('32', 'curly 3 (A 72, B 32)'),
    ('f129_L13', 15): ('36', 'curly 3 (A 96, B 76)'),
    ('f129_L13', 19): ('21', 'second digit blotted, read 1 (B 24)'),
    ('f129_L13', 20): ('31', 'curly 3 (A 91, B 31)'),
    ('f129_L15', 6): ('_6', 'bar over the 6 (A 6, B _6)'),
    ('f129_L15', 18): ('33', 'curly 3 twice (A 77, B 33)'),
    ('f129_L16', 19): ('_6', 'bar over the 6 (A 6, B _6)'),
    ('f130a_L02', 9): ('79', 'flat-topped first stroke (A 99, B 79); 39 not excluded'),
    ('f130a_L02', 11): ('_3', 'curly 3 under the bar (A _7, B _3); "_3 7 21" = pour, as in f.86'),
    ('f130a_L02', 17): ('2', 'B "2 21" at the gutter (A 20)'),
    ('f130a_L04', 1): ('31', 'curly 3 (A 31, B 71)'),
    ('f130a_L06', 2): ('1', 'single stroke (A 1, B 2)'),
    ('f130a_L07', 7): ("[PLAIN:Desja ie vous ay mandé ce qui s'est]", 'clear French (B stops at "qui")'),
    ('f130b_L01', 8): ('36', 'curly 3 (A 96, B 36)'),
    ('f130b_L02', 5): ('36', 'curly 3 (A 76, B 36)'),
    ('f130b_L03', 3): ('_26', 'bar over 26 (A _26, B 26)'),
    ('f130b_L04', 9): ('36', 'curly 3 (A 96, B 36)'),
    ('f130b_L05', 15): ('36', 'curly 3 (A 76, B 36)'),
}
# (row, after pass-A pos) -> [(group, reason)] inserted
INS = {
    ('f130a_L02', 17): [('21', 'B "2 21" at the gutter; A read one group 20')],
    ('f130a_L03', 20): [('2', 'B; at the gutter')],
    ('f130a_L04', 17): [('2', 'a 2 at the gutter after 62, in neither pass; seen on the native')],
}
GUTTER_LAST = True  # the last group of every cipher row on canvas 129 runs towards the fold


def load(p):
    L = OrderedDict()
    for r in csv.DictReader(open(f'{HERE}/{p}'), delimiter='\t'):
        L.setdefault(r['line'], []).append(r)
    return L


def build():
    A, B = load('passA_f67.tsv'), load('passB_f67.tsv')
    bmap = dict(BMAP)
    for k in B:
        if k.startswith('f130'):
            bmap[k] = [k]
    agree = {}  # (row,pos) -> True where B has the same group at the aligned position
    for bk, aks in bmap.items():
        a = [(k, int(r['pos']), r['group']) for k in aks for r in A[k]]
        b = [r['group'] for r in B[bk]]
        sm = difflib.SequenceMatcher(None, [x[2] for x in a], b, autojunk=False)
        for op, i1, i2, j1, j2 in sm.get_opcodes():
            if op == 'equal':
                for x in a[i1:i2]:
                    agree[(x[0], x[1])] = True
    rows = []
    for k, rs in A.items():
        pos = 0
        for r in rs:
            p = int(r['pos'])
            g, note = r['group'], ''
            if (k, p) in SET:
                g, note = SET[(k, p)]
            if g.startswith('[') and not g.startswith('[PLAIN:'):
                g = '[PLAIN:' + g[1:]
            pos += 1
            if g.startswith('[PLAIN:') or g in NONSIGN:
                conf = 'H' if agree.get((k, p)) and not note else 'M'
            else:
                conf = 'H' if agree.get((k, p)) and (k, p) not in SET else 'M'
            rows.append((k, pos, g, conf, note))
            for g2, n2 in INS.get((k, p), []):
                pos += 1
                rows.append((k, pos, g2, 'M', n2))
    return rows


def render(rows):
    out = ['line\tpos\tgroup\tconf\tnote']
    out += [f'{k}\t{p}\t{g}\t{c}\t{n}' for k, p, g, c, n in rows]
    return '\n'.join(out) + '\n'


def main():
    text = render(build())
    if '--check' in sys.argv:
        ok = open(OUT).read() == text
        print('ciphertext_f67.tsv', 'up to date' if ok else 'STALE')
        sys.exit(0 if ok else 1)
    open(OUT, 'w').write(text)
    rows = build()
    cip = [r for r in rows if not r[2].startswith('[') and r[2] not in NONSIGN]
    print(f'{len(rows)} rows, {len(cip)} cipher groups: H {sum(r[3]=="H" for r in cip)} M {sum(r[3]=="M" for r in cip)}')


if __name__ == '__main__':
    main()
