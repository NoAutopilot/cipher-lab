#!/usr/bin/env python3
"""S1, 24 Sept 2026: build ciphertext_53.tsv (53 p1 postscript, 10 lines) from recon53/ciphertext_draft.tsv
(passA_53 + passB_53, tools/reconcile_passes.py) plus the settlements below, decided on the crops
(images/crops_s1/53_L*.png and re-crops of L01, L08, L09). --check verifies the committed file."""
import sys
SET = {  # draft (line, pos): (sign or None, why)
 ('53_L08', 28): (None, 'image: B\'s OQ is the two dots over the preceding triangle (diaeresis), not a sign'),
 ('53_L08', 30): ('F', 'image: long-s with bar (A); B missed it'),
 ('53_L09', 20): ('V', 'image: V under an ink blot; M'),
 ('53_L09', 23): (None, 'image: S-shaped pen flourish between signs (line filler), not a sign'),
 ('53_L09', 25): ('X', 'image: X before the barred X (A)'),
 ('53_L10', 20): ('G3', 'image: w-loop (B); A NEW1'),
}
NOTE = {('53_L08', 27): 'triangle carries two dots (diaeresis)'}

def build():
    rows = [l.rstrip('\n').split('\t') for l in open('recon53/ciphertext_draft.tsv')][1:]
    out, pos = [], {}
    for r in rows:
        L, p, s, c, alt = r[0], int(r[1]), r[2], r[3], r[4]
        why = r[5] if len(r) > 5 else ''
        if (L, p) in SET:
            ns, w = SET[(L, p)]
            if ns is None:
                continue
            s, c, why = ns, ('M' if 'M;' in w or w.endswith('M') else 'H'), 'settled: ' + w
        elif s == 'S' or (s == '5' and 'S' in alt):
            s, why = '5', 'S and 5 are one glyph in this hand (checked L01 pos 1, L09); passes split them'
        elif s == 'E':
            s, why = 'G6', 'E-coded epsilon = G6'
        if (L, p) in NOTE:
            why = (why + '; ' if why else '') + NOTE[(L, p)]
        pos[L] = pos.get(L, 0) + 1
        out.append([L, pos[L], s, c, why])
    return 'line\tpos\tsign\tconf\twhy\n' + ''.join('\t'.join(map(str, r)) + '\n' for r in out)

t = build()
if '--check' in sys.argv:
    sys.exit(0 if open('ciphertext_53.tsv').read() == t else 1)
open('ciphertext_53.tsv', 'w').write(t)
