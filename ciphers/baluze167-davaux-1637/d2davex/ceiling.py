#!/usr/bin/env python3
"""Oracle ceiling for the D2-DAVEX leave-one-out control (PREREG-D2DAVEX.md gate 1). Reads the known-answer letter-sign positions of
167 f.157 from known_answer.py's EXPECTED and ciphertext.txt (L: tokens with a single-letter expected value), and reports how many have
another exemplar of the same letter. Exit 0 if the ceiling reaches the 0.80 gate, 3 if the gate is unreachable by construction.
  python3 d2davex/ceiling.py"""
import os, sys, collections
D = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
src = open(f'{D}/known_answer.py').read()
EXPECTED = eval(src[src.index('EXPECTED = ') + 11: src.index('}\n', src.index('EXPECTED = ')) + 1])
toks = {}
for l in open(f'{D}/ciphertext.txt'):
    if l.startswith('#') or '|' not in l: continue
    h, b = l.split('|', 1); toks[h.strip()] = [t.rstrip('?') for t in b.split()]
pos = [(line, i, e) for line, exp in EXPECTED.items() for i, (t, e) in enumerate(zip(toks[line], exp)) if e and t.startswith('L:')]
cnt = collections.Counter(e for _, _, e in pos)
ok = sum(cnt[e] >= 2 for _, _, e in pos)
for line, i, e in pos: print(f'{line}\t{i}\t{e}\texemplars_of_letter={cnt[e]}\t{"testable" if cnt[e] >= 2 else "singleton"}')
c = ok / len(pos)
print(f'positions {len(pos)}, letters {len(cnt)} {dict(cnt)}; oracle LOO ceiling {ok}/{len(pos)} = {c:.3f}; gate 0.80 '
      + ('reachable' if c >= 0.8 else 'UNREACHABLE by construction'))
sys.exit(0 if c >= 0.8 else 3)
