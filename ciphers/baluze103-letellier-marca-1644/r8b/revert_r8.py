#!/usr/bin/env python3
"""R8-BAL103B, per r8b/PREREG.md: pre-R8 (-1.537) beats R8 (-1.569) and the look-alike pass (-1.562) on the fr17 judge, so the
10 R8-BAL103 'r8-2of3' columns of ciphertext.tsv go back to their pre-R8 sign (grade M), with the R8 sign kept in alt as
'r8 tried=X' and why 'r8-reverted'. The look-alike relabels (r8b/passD.tsv) are not applied. Idempotent."""
import os
H = os.path.dirname(os.path.abspath(__file__)); P = os.path.join(os.path.dirname(H), 'ciphertext.tsv')
hdr, *rows = [l.rstrip('\n').split('\t') for l in open(P)]
n = 0
for r in rows:
    if r[5] == 'r8-2of3':
        old = r[4].split('r8 old=')[1].split()[0]
        r[4] = r[4].replace(f'r8 old={old}', f'r8 tried={r[2]}'); r[2] = old; r[3] = 'M'; r[5] = 'r8-reverted'; n += 1
open(P, 'w').write('\t'.join(hdr) + '\n' + ''.join('\t'.join(r) + '\n' for r in rows))
print('reverted', n)
