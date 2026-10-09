#!/usr/bin/env python3
"""SIG-7208: for every code > 120 (and every 1-120 code with no one-letter key_full value) in ciphertext_7208.tsv, the
period-decipherment letters it aligns to, using sig7208/gate.py's key_full-anchored Levenshtein alignment: the span
between the decipherment positions of the nearest aligned scored letters on either side. Writes sig7208/spans_7208.tsv.
    python3 sig7208/spans.py"""
import csv, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import gate
from rapidfuzz.distance import Levenshtein

key = {r['code']: r['value'] for r in csv.DictReader(open(os.path.join(gate.TOP, 'key_full.tsv'), encoding='utf-8'), delimiter='\t')}
rows, P = gate.tokens(), gate.plain()
chars, owner = [], []          # owner = token index for each char
targets = []
for i, r in enumerate(rows):
    s = r['sign']
    if s.startswith('='):
        for ch in gate.letters(s[1:]): chars.append(ch); owner.append(i)
    elif s.isdigit():
        v = key.get(s)
        if int(s) > 120 or v is None:
            targets.append(i); continue
        if v == 'NULL': continue
        for ch in gate.letters(v): chars.append(ch); owner.append(i)
A = ''.join(chars)
amap = [None] * len(A)
for op in Levenshtein.opcodes(A, P):
    if op.tag == 'equal':
        for k in range(op.src_end - op.src_start): amap[op.src_start + k] = op.dest_start + k
first_char = {}
for k, o in enumerate(owner): first_char.setdefault(o, k)
out = csv.writer(open(os.path.join(gate.TOP, 'sig7208', 'spans_7208.tsv'), 'w', encoding='utf-8'), delimiter='\t', lineterminator='\n')
out.writerow(['code', 'line', 'position', 'confidence', 'span', 'left_plain', 'right_plain'])
for i in targets:
    # char index boundary: chars of tokens before i
    b = next((first_char[o] for o in range(i + 1, len(rows)) if o in first_char), len(A))
    L = next((amap[k] for k in range(b - 1, -1, -1) if amap[k] is not None), -1)
    R = next((amap[k] for k in range(b, len(A)) if amap[k] is not None), len(P))
    r = rows[i]
    out.writerow([r['sign'], r['line'], r['position'], r['confidence'], P[L + 1:R], P[max(0, L - 11):L + 1], P[R:R + 12]])
