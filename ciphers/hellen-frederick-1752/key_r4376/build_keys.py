#!/usr/bin/env python3
"""Derive test keys from key.tsv (R4376 P3 transcription, N6-HEL76 4 Oct 2026), the way ../key_r4372/build_keys.py does.
key.tsv columns: code, left, right, grade_left, grade_right, page. R4376 (BL Add MS 32276 f.56, docket 1754) P3 prints codes
1-500 in blocks of 100, plus a cut 501-600 column at the right edge. Right entries of the strip LEFT of block 1-100 are stored on
row code c-100 (codes -99..0), so R100 sends them to c, the number their dash points at (README convention 6).
Attributions (pre-registered in PREREG.md, k = 4); no range restriction:
  key_L.tsv, key_R0.tsv, key_R100.tsv, key_LR100.tsv   gated keys, "zero" (null) cells DROPPED (PREREG item 3)
  key_<X>_z.tsv                                        same with "zero" kept (reported, not gated)
  key_decode.tsv  LR100 graded for tools/decode_key.py: left H/M as read; R100 S (M if the cell was M); zero kept as a null
Crossed-out readings ('~' prefix) are dropped; an M-graded cell is kept; codes <= 0 never reach a key.
Usage: python3 build_keys.py [--check]   (--check exits 1 if a committed key differs from what key.tsv gives)"""
import csv, os, re, sys
HERE = os.path.dirname(os.path.abspath(__file__))

def clean(s):
    s = re.sub(r'~\S+(\s|$)', '', (s or '').strip()).strip()
    s = s.rstrip('…').strip()
    return '' if s in ('', '?') else s

def isnull(v):
    return re.sub(r'[^a-z]', '', v.lower()) == 'zero'

def build():
    rows = list(csv.DictReader(open(os.path.join(HERE, 'key.tsv'), encoding='utf-8'), delimiter='\t'))
    L, R0, R100, G = {}, {}, {}, {}
    for r in rows:
        c = int(r['code']); l, rt = clean(r['left']), clean(r['right'])
        if l and c > 0: L[c] = l; G[('L', c)] = r['grade_left'] or 'H'
        if rt:
            if c > 0: R0[c] = rt
            R100[c + 100] = rt; G[('R', c + 100)] = r['grade_right'] or 'H'
    LR = dict(L); LR.update(R100)
    nz = lambda k: {c: v for c, v in k.items() if not isnull(v)}
    dec = 'code\tvalue\tgrade\tsource\n'
    for c in sorted(LR):
        if c in R100:
            dec += f"{c}\t{R100[c]}\t{'M' if G[('R', c)] == 'M' else 'S'}\tR4376 right entry of row {c - 100}, attributed +100\n"
        else:
            dec += f"{c}\t{L[c]}\t{G[('L', c)]}\tR4376 left entry\n"
    out = {}
    for name, k in (('L', L), ('R0', R0), ('R100', R100), ('LR100', LR)):
        out[f'key_{name}.tsv'] = nz(k); out[f'key_{name}_z.tsv'] = k
    out['key_decode.tsv'] = dec
    return out

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
            open(p, 'w', encoding='utf-8').write(txt); print(fn, len(k) if not isinstance(k, str) else txt.count('\n') - 1)
    sys.exit(bad)
