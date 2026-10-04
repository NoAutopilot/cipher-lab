#!/usr/bin/env python3
"""Derive test keys from key.tsv (R4372 transcription, NEAR3-HEL4 4 Oct 2026), the same way as ../key_r4369/build_keys.py.
key.tsv columns: code, left, right, grade_left, grade_right, page. R4372 (BL Add MS 32276 f.48) prints codes 1-1000 in
blocks of 100 (P2 1-500, P3 501-1000). Attributions (pre-registered in PREREG.md, k = 4), each restricted to codes 1-800,
the R1953 tokens R4369 cannot reach:
  key_L.tsv       left meanings only
  key_R0.tsv      right entries -> the same row's code
  key_R100.tsv    right entries -> code + 100 (the next block's same row; the dash points at it)
  key_LR100.tsv   left meanings plus R100, R100 taking the code where both land on it
  key_full_LR100.tsv  LR100 over every code the sheet carries (1-1000), for the 801-900 overlap with R4369 (gate A)
  key_comb_<X>.tsv  combined test keys (PREREG item 6, reported not gated): R4372 attribution X (1-800) + ../key_r4369/key_LR100.tsv (801+)
  key_decode.tsv  key_LR100 (1-800) graded for tools/decode_key.py: left H/M as read; R100 S (M if the cell was M)
Crossed-out readings ('~' prefix) are dropped; an M-graded cell is kept.
Usage: python3 build_keys.py [--check]   (--check exits 1 if a committed key differs from what key.tsv gives)"""
import csv, os, re, sys
HERE = os.path.dirname(os.path.abspath(__file__))
LIMIT = 800

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
            R0[c] = rt; R100[c + 100] = rt; G[('R', c + 100)] = r['grade_right'] or 'H'
    full = dict(L); full.update(R100)
    lim = lambda k: {c: v for c, v in k.items() if c <= LIMIT}
    L8, R08, R1008, LR8 = lim(L), lim(R0), lim(R100), lim(full)
    dec = 'code\tvalue\tgrade\tsource\n'
    for c in sorted(LR8):
        if c in R1008:
            dec += f"{c}\t{R1008[c]}\t{'M' if G[('R', c)] == 'M' else 'S'}\tR4372 right entry of row {c - 100}, attributed +100\n"
        else:
            dec += f"{c}\t{L8[c]}\t{G[('L', c)]}\tR4372 left entry\n"
    r69 = {int(r['code']): r['meaning'] for r in csv.DictReader(open(os.path.join(HERE, '..', 'key_r4369', 'key_LR100.tsv'),
           encoding='utf-8'), delimiter='\t') if r['meaning'].strip()}
    comb = lambda k: {**{c: v for c, v in r69.items() if c > LIMIT}, **k}
    return {'key_comb_L.tsv': comb(L8), 'key_comb_R0.tsv': comb(R08), 'key_comb_R100.tsv': comb(R1008), 'key_comb_LR100.tsv': comb(LR8),
            'key_decode.tsv': dec, 'key_L.tsv': L8, 'key_R0.tsv': R08, 'key_R100.tsv': R1008, 'key_LR100.tsv': LR8,
            'key_full_LR100.tsv': full}

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
