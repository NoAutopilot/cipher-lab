#!/usr/bin/env python3
"""Positive control for score_f247.py (PREREG-N8BAL.md): plant both fragments, enciphered greedily with key.tsv (longest syllable
first, else a letter sign), between clear filler words, then corrupt a share of cipher tokens (replace by a random key code of
another value) and score. Prints pooled agreement per error level (0, 0.10, 0.20, 0.30), 20 seeds each for >0.
  python3 planted_control.py
"""
import os, random, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import score_f247 as S
key = S.load_key()
inv = {}
for c, v in key.items():
    nv = S.norm(v) if not v.startswith('(') else ''
    if nv and c[-1] in "'L:" or c.startswith('L:'): inv.setdefault(nv, c)
def encipher(text):
    t, out, i = S.norm(text), [], 0
    while i < len(t):
        for L in (3, 2, 1):
            if t[i:i+L] in inv: out.append(inv[t[i:i+L]]); i += L; break
        else: out.append('?'); i += 1
    return out
codes = list(key)
def build(err, rng):
    toks = [('clear', 'monsieur ie vous diray que')]
    for f in S.FRAGS:
        for c in encipher(f):
            if rng.random() < err:
                c2 = rng.choice(codes)
                while key[c2] == key.get(c): c2 = rng.choice(codes)
                c = c2
            toks.append(('cipher', c))
        toks.append(('clear', 'et pour le reste de ces affaires'))
    return toks
for err in (0.0, 0.10, 0.20, 0.30):
    vals = []
    for seed in range(1 if err == 0 else 20):
        r = S.score(build(err, random.Random(seed)), key)
        vals.append(sum(a for a, b in r) / sum(b for a, b in r))
    print(f'planted, token error {err:.2f}: pooled agreement mean {sum(vals)/len(vals):.3f}, min {min(vals):.3f} (n={len(vals)})')
