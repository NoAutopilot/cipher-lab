#!/usr/bin/env python3
"""GAPS94: render ciphertext_fig1.txt's sign names in Arabic/Jawi letters for a blind text-only reader.

Usage: render_arabic.py [--out reader/fig1_arabic.txt]. One line per inscription line, groups separated by ' / ' and also
listed numbered (1-based, right-to-left order as transcribed). 'tooth' -> dotless tooth U+066E; OBSCURED -> [...];
a trailing '?' on a sign (UNSETTLED in the look-alike pass) is dropped from the letters and listed separately.
"""
import argparse, os, re
HERE = os.path.dirname(os.path.abspath(__file__))
CT = os.path.join(HERE, '..', 'ciphertext_fig1.txt')
L = {'alif': 'ا', 'ba': 'ب', 'ta': 'ت', 'tha': 'ث', 'nun': 'ن', 'ya': 'ي', 'jim': 'ج', 'ha2': 'ح', 'kha': 'خ',
     'dal': 'د', 'ra': 'ر', 'sin': 'س', 'shin': 'ش', 'fa': 'ف', 'ghayn': 'غ', 'ain': 'ع', 'kaf': 'ك', 'lam': 'ل',
     'mim': 'م', 'ha': 'ه', 'waw': 'و', 'hamza': 'ء', 'lamalif': 'لا', 'nga': 'ڠ', 'tooth': 'ٮ', 'qaf': 'ق'}


def render():
    out, unsure = [], []
    for raw in open(CT, encoding='utf-8'):
        m = re.match(r'^(L\d\d):(.*)', raw)
        if not m:
            continue
        gs = []
        for gi, g in enumerate(m.group(2).split('|'), 1):
            letters = ''
            for t in g.split():
                if t == 'OBSCURED':
                    letters += '[...]'
                    continue
                if t.endswith('?'):
                    unsure.append('%s group %d: %s' % (m.group(1), gi, L[t[:-1]]))
                letters += L[t.rstrip('?')]
            gs.append(letters)
        out.append((m.group(1), gs))
    return out, unsure


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--out', default=os.path.join(HERE, 'fig1_arabic.txt'))
    a = ap.parse_args()
    lines, unsure = render()
    with open(a.out, 'w', encoding='utf-8') as f:
        f.write('Continuous (each line right to left; " / " = a visible gap in the hand):\n')
        for name, gs in lines:
            f.write('%s: %s\n' % (name, ' / '.join(gs)))
        f.write('\nNumbered groups:\n')
        for name, gs in lines:
            f.write('%s: %s\n' % (name, '  '.join('(%d) %s' % (i, g) for i, g in enumerate(gs, 1))))
        f.write('\nLetters the transcribers could not settle (dot count or stroke): %s\n' % '; '.join(unsure))
    print(open(a.out, encoding='utf-8').read())


if __name__ == '__main__':
    main()
