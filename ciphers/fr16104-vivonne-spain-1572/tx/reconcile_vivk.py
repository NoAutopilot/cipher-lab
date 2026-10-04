#!/usr/bin/env python3
"""N5-VIVK reconciliation: tools/reconcile_passes.py draft (pass A at a split, B as alt) + label rules settled by eye.

    python3 ciphers/fr16104-vivonne-spain-1572/tx/reconcile_vivk.py f102r [f102v f103r ...] [--viv54]

Rules (worker's eye on the crops, 4 Oct 2026, NOTES "N5-VIVK"): at a split between the two blind passes, the pair is
a label split, not a glyph split, and resolves to the winner below; any other split keeps pass A (the draft) and is
counted as not settled. A token only one pass wrote (a gap) keeps the draft. Writes tx/<page>_rec.tsv (wide) and prints
counts. Tokens outside tx/SIGNS.md written by a pass ({t}, Y, u, q) are mapped as listed when they are the draft sign.
"""
import os, sys
from collections import defaultdict

HERE = os.path.dirname(os.path.abspath(__file__))
RULES = {frozenset(p): w for p, w in [
    (('S', 's'), 's'),      # f.102v pass A wrote S for the short closed s throughout (crops L02-L05 checked)
    (('c', ':'), ':'),      # the ".." pair is often written as a small c-like stroke + dot
    (('4', '{t}'), '4'),    # the crossed-descender sign is the 4 of SIGNS.md
    (('y', 'V'), 'y'),      # the swash lead-in of the y read as V by one pass
    (('z', 'r'), 'z'),      # z with a top hook read as r by one pass
    (('x', 'r'), 'x'),
]}
# N5-VIV54 (f.173r-v only, --viv54): one pass wrote each small dot as 'o', the other as ':' (crops f.173r L05 s1-s2 checked:
# solid dots, not the round o of 'o o')
RULES54 = {frozenset((':', 'o')): ':'}
MAP = {'{t}': '4', 'Y': 'y', 'u': 'a', 'q': '@'}


def main():
    pages = [a for a in sys.argv[1:] if not a.startswith('--')]
    rules = {**RULES, **RULES54} if '--viv54' in sys.argv else RULES
    for page in pages:
        rows = defaultdict(list)
        n = settled = unsettled = gaps = 0
        for ln in open(os.path.join(HERE, f'rec_{page}', 'ciphertext_draft.tsv'), encoding='utf-8'):
            f = ln.rstrip('\n').split('\t')
            if f[0] == 'line':
                continue
            line, pos, sign, conf, alt, why = (f + [''] * 6)[:6]
            a = sign.rstrip('?')
            b = alt[2:].rstrip('?') if alt.startswith('B:') else ''
            if why == 'differ' and b and b != '-':
                w = rules.get(frozenset((a, b)))
                if w:
                    a = w; settled += 1
                else:
                    unsettled += 1
            elif why == 'gap':
                gaps += 1
            if a in ('', '-'):
                continue
            a = MAP.get(a, a)
            rows[line].append(a); n += 1
        with open(os.path.join(HERE, f'{page}_rec.tsv'), 'w', encoding='utf-8') as out:
            out.write('row\tcodes\n')
            for line in sorted(rows):
                out.write(f'{line}\t{" ".join(rows[line])}\n')
        print(f'{page}: {n} signs written; splits settled by label rule {settled}, splits left at pass A {unsettled}, '
              f'one-pass gaps kept as drafted {gaps}')


if __name__ == '__main__':
    main()
