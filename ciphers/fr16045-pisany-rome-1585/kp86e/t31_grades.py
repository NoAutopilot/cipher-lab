#!/usr/bin/env python3
"""RUN5-PIS3 (PREREG kp86e, grades paragraph). Same alignment as kp86b/cgrades.py (key86 arm A decode vs the Colbert
copy, tools/stream_align.band_dp, free start). Two outputs:
 1. kp86e/t31_witness.tsv -- every T31 token on the three pages tested so far (f.244r, f.244v+f.245r, f.275r) with the
    copy letter its decoded 'm' aligns to (or '-' if the alignment gaps it) and +/-8 letters of copy context: the page
    witnesses for the key86 T31 data conflict (HYPOTHESES.md).
 2. with --grade: kp86e/grades_f275r.tsv, rule-4 grades for f.275r (C = every decoded letter aligns identically; T31
    tokens are C only if that holds, i.e. never while key86 says m and the copy says o; other decoded tokens M; U).
    Run only when kp86e arm A is a licensed PASS."""
import os, sys
from collections import Counter
import numpy as np
H = os.path.dirname(os.path.abspath(__file__)); T = os.path.dirname(H)
sys.path.insert(0, os.path.join(T, 'kp86')); sys.path.insert(0, os.path.join(T, '../../tools'))
from kp86 import norm, load_key
from stream_align import band_dp, A
key = load_key()
PAGES = [('17 Sept 1586 f.244r', 'tx86/ciphertext_f244r.tsv', 'kp86/colbert_p49_50.txt'),
         ('17 Sept 1586 f.244v+f.245r', 'tx86c/ciphertext_f244v_f245r.tsv', 'kp86b/colbert_p51_52.txt'),
         ('4 Nov 1586 f.275r', 'tx86e/ciphertext_f275r.tsv', 'kp86d/colbert_p121_123.txt')]


def align(ctf, clf):
    toks, where = [], []
    for ln in open(os.path.join(T, ctf)):
        if not ln.strip():
            continue
        lab, body = ln.rstrip('\n').split('\t')
        for k, t in enumerate(x for x in body.split() if x != '/'):
            toks.append(t.rstrip('?')); where.append((lab, k + 1))
    ctext = norm(open(os.path.join(T, clf)).read())
    clear = np.array([ord(c) - 97 for c in ctext])
    letters, owner = [], []
    for i, t in enumerate(toks):
        for c in key.get(t, ''):
            letters.append(ord(c) - 97); owner.append(i)
    dec = np.array(letters); N, M = len(dec), len(clear)
    E = np.full((A + 1, A), -1.0); E[np.arange(A), np.arange(A)] = 2.0
    ref = np.linspace(0, min(M, N), N + 1) if M >= N else np.arange(N + 1) * (M / N)
    path, _, _ = band_dp(dec, clear, E, ref, max(200, abs(M - N) + 200), 1.0, 1.0, free_start=True)
    return toks, where, ctext, dec, owner, dict(path)


rows = []
for name, ctf, clf in PAGES:
    toks, where, ctext, dec, owner, pm = align(ctf, clf)
    for n, o in enumerate(owner):
        if toks[o] == 'T31':
            j = pm.get(n)
            rows.append((name, where[o][0], where[o][1], ctext[j] if j is not None else '-',
                         ctext[max(0, j - 8):j] + '[' + ctext[j] + ']' + ctext[j + 1:j + 9] if j is not None else ''))
with open(os.path.join(H, 't31_witness.tsv'), 'w') as f:
    f.write('letter_page\tline\tpos\tcopy_letter\tcopy_context\n')
    for r in rows:
        f.write('\t'.join(map(str, r)) + '\n')
for name, *_ in PAGES:
    print(name, Counter(r[3] for r in rows if r[0] == name))
if '--grade' in sys.argv:
    toks, where, ctext, dec, owner, pm = align(PAGES[2][1], PAGES[2][2])
    ok = {i for i, j in pm.items() if dec[i] == ord(ctext[j]) - 97}
    grade = []
    for i, t in enumerate(toks):
        idx = [n for n, o in enumerate(owner) if o == i]
        g = 'U' if not idx else 'C' if all(n in ok for n in idx) else 'M'
        grade.append('M' if t == 'T31' and g == 'C' else g)   # HYPOTHESES.md: T31 held at M (data conflict)
    with open(os.path.join(H, 'grades_f275r.tsv'), 'w') as f:
        f.write('line\tpos\tsign\tvalue\tgrade\n')
        for (l, p), t, g in zip(where, toks, grade):
            f.write(f'{l}\t{p}\t{t}\t{key.get(t, "")}\t{g}\n')
    print('f.275r grades', Counter(grade), 'tokens', len(toks), 'identical letters', len(ok), 'of', len(dec))
