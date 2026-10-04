#!/usr/bin/env python3
"""Rule-4 grade counts for the kp86c reading (RUN4-PIS1): a token is C when every letter it decodes to (key86, arm A)
aligns identically to the Colbert clear copy (kp86b/colbert_p51_52.txt) under the kp86 statistic's own alignment; other
decoded tokens M; nulls and uncovered signs U. Prints counts and writes kp86b/grades_f244v_f245r.tsv."""
import os, sys
from collections import Counter
import numpy as np
H = os.path.dirname(os.path.abspath(__file__)); T = os.path.dirname(H)
sys.path.insert(0, os.path.join(T, 'kp86')); sys.path.insert(0, os.path.join(T, '../../tools'))
from kp86 import norm, load_key
from stream_align import band_dp, A
key = load_key()
toks, where = [], []
for ln in open(os.path.join(T, 'tx86c/ciphertext_f244v_f245r.tsv')):
    lab, body = ln.rstrip('\n').split('\t')
    for k, t in enumerate(x for x in body.split() if x != '/'):
        toks.append(t.rstrip('?')); where.append((lab, k + 1))
clear = np.array([ord(c) - 97 for c in norm(open(os.path.join(H, 'colbert_p51_52.txt')).read())])
letters, owner = [], []
for i, t in enumerate(toks):
    for c in key.get(t, ''):
        letters.append(ord(c) - 97); owner.append(i)
dec = np.array(letters); N, M = len(dec), len(clear)
E = np.full((A + 1, A), -1.0); E[np.arange(A), np.arange(A)] = 2.0
ref = np.linspace(0, min(M, N), N + 1) if M >= N else np.arange(N + 1) * (M / N)
path, _, _ = band_dp(dec, clear, E, ref, max(200, abs(M - N) + 200), 1.0, 1.0, free_start=True)
ok = {i for i, j in path if dec[i] == clear[j]}
grade = []
for i, t in enumerate(toks):
    idx = [n for n, o in enumerate(owner) if o == i]
    grade.append('U' if not idx else 'C' if all(n in ok for n in idx) else 'M')
with open(os.path.join(H, 'grades_f244v_f245r.tsv'), 'w') as f:
    f.write('line\tpos\tsign\tvalue\tgrade\n')
    for (l, p), t, g in zip(where, toks, grade):
        f.write(f'{l}\t{p}\t{t}\t{key.get(t, "")}\t{g}\n')
print(Counter(grade), 'tokens', len(toks), 'identical letters', len(ok), 'of', N)
