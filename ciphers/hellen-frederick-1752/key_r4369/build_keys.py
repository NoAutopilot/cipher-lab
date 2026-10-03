#!/usr/bin/env python3
"""Derive test keys from key.tsv (R4369 transcription, READ2-HEL 3 Oct 2026).
key.tsv columns: code, left, right, grade, page. 'left' is the meaning written straight after the printed code
number; 'right' is the right-aligned entry (ending in a dash) at the far right of the same row. Which code a right
entry belongs to is not settled from the sheet, so three attributions are written as separate keys and all three
are tested (test_sibling.py --key):
  key_L.tsv       left meanings only
  key_R0.tsv      right entries -> the same row's code
  key_R100.tsv    right entries -> the code on the same row of the next block (code + 100; the dash points at it)
  key_LR100.tsv   left meanings plus R100, R100 taking the code where both land on it
  key_Lonly.tsv   left meanings on codes R100 does not reach
  conflicts_L_R100.tsv  codes carrying both a left meaning and an R100 entry (left | right)
  key_decode.tsv  key_LR100 with grades for tools/decode_key.py: left H/M as read; R100 S (M if the cell was M)
Crossed-out readings (prefixed '~') are dropped; an M-graded cell is kept (it is what the readers settled on).
Usage: python3 build_keys.py [--check]   (--check exits 1 if a committed key differs from what key.tsv gives)"""
import csv, os, re, sys
HERE = os.path.dirname(os.path.abspath(__file__))

def clean(s):
    s = re.sub(r'~\S+(\s|$)', '', (s or '').strip()).strip()
    return '' if s in ('', '?') else s

def build():
    rows = list(csv.DictReader(open(os.path.join(HERE, 'key.tsv'), encoding='utf-8'), delimiter='\t'))
    L, R0, R100, G = {}, {}, {}, {}
    for r in rows:
        c = int(r['code']); l, rt = clean(r['left']), clean(r['right'])
        if l: L[c] = l; G[('L', c)] = r['grade_left'] or 'H'
        if rt:
            R0[c] = rt
            if 901 <= c <= 1700: R100[c + 100] = rt; G[('R', c + 100)] = r['grade_right'] or 'H'
    LR = dict(L); LR.update(R100)                     # R100 wins where both land on one code
    Lonly = {c: v for c, v in L.items() if c not in R100}
    both = {c: f'{L[c]} | {R100[c]}' for c in L if c in R100}
    dec = 'code\tvalue\tgrade\tsource\n'
    for c in sorted(LR):
        if c in R100:   # attribution to code+100 is the test's choice, not the sheet's: S (or M if the cell was M)
            dec += f"{c}\t{R100[c]}\t{'M' if G[('R', c)] == 'M' else 'S'}\tR4369 right entry of row {c - 100}, attributed +100\n"
        else:
            dec += f"{c}\t{L[c]}\t{G[('L', c)]}\tR4369 left entry\n"
    return {'key_decode.tsv': dec, 'key_L.tsv': L, 'key_R0.tsv': R0, 'key_R100.tsv': R100, 'key_LR100.tsv': LR,
            'key_Lonly.tsv': Lonly, 'conflicts_L_R100.tsv': both}

def render(k):
    return 'code\tmeaning\n' + ''.join(f'{c}\t{v}\n' for c, v in sorted(k.items()))

if __name__ == '__main__':
    bad = 0
    for fn, k in build().items():
        p = os.path.join(HERE, fn); txt = k if isinstance(k, str) else render(k)
        if '--check' in sys.argv:
            if not os.path.exists(p) or open(p, encoding='utf-8').read() != txt:
                print('STALE', fn); bad = 1
        else:
            open(p, 'w', encoding='utf-8').write(txt); print(fn, len(k))
    sys.exit(bad)
