#!/usr/bin/env python3
"""RUN4-PIS1 unit (a): per-occurrence context for key86 cells flagged by kp86/anchored_map.tsv (T31 T45 T47 T49 T57).
Same key86-anchored alignment as kp86/anchored_map.py; prints line, position, the decoded neighbourhood and the clear
letters aligned to it, so each occurrence can be eye-checked on the f.244r crops. Disk only."""
import os, sys
import numpy as np
H = os.path.dirname(os.path.abspath(__file__)); T = os.path.dirname(H)
sys.path.insert(0, os.path.join(T, '../../tools')); sys.path.insert(0, os.path.join(T, 'kp86'))
from stream_align import band_dp, A
from kp86 import load_key, norm
key = load_key()
toks, where = [], []
for ln in open(os.path.join(T, 'tx86/ciphertext_f244r.tsv')):
    lab, body = ln.rstrip('\n').split('\t')
    k = 0
    for t in body.split():
        if t == '/': continue
        k += 1
        if t.startswith('?'): continue
        toks.append(t.rstrip('?')); where.append((lab, k))
clear = np.array([ord(c) - 97 for c in norm(open(os.path.join(T, 'kp86/colbert_p49_50.txt')).read())])
letters, owner = [], []
for i, t in enumerate(toks):
    for c in key.get(t, ''):
        letters.append(ord(c) - 97); owner.append(i)
dec = np.array(letters); N, M = len(dec), len(clear)
ref = np.linspace(0, min(M, N), N + 1) if M >= N else np.arange(N + 1) * (M / N)
path, _, _ = band_dp(dec, clear, E := (lambda e: (e.__setitem__((np.arange(A), np.arange(A)), 2.0), e)[1])(np.full((A + 1, A), -1.0)), ref, max(200, abs(M - N) + 200), 1.0, 1.0, free_start=True)
al = dict(path)
for target in sys.argv[1:] or ['T31', 'T45', 'T47', 'T49', 'T57']:
    print('==', target, key.get(target))
    for i, t in enumerate(toks):
        if t != target: continue
        idx = [n for n, o in enumerate(owner) if o == i]
        lo = max(0, (idx[0] if idx else 0) - 6)
        hi = (idx[-1] if idx else lo) + 7
        d = ''.join(chr(97 + dec[n]).upper() if owner[n] == i else chr(97 + dec[n]) for n in range(lo, min(hi, N)))
        js = [al[n] for n in range(lo, min(hi, N)) if n in al]
        c = ''.join(chr(97 + x) for x in clear[min(js) - 2:max(js) + 3]) if js else '-'
        print(f'  {where[i][0]} tok{where[i][1]:>3}  dec {d:<16} clear {c}')
