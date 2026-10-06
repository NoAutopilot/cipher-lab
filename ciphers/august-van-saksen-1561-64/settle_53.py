#!/usr/bin/env python3
"""S1, 24 Sept 2026: build ciphertext_53.tsv (53 p1 postscript, 10 lines) from recon53/ciphertext_draft.tsv
(passA_53 + passB_53, tools/reconcile_passes.py) plus the settlements below, decided on the crops
(images/crops_s1/53_L*.png and re-crops of L01, L08, L09). --check verifies the committed file.
F1, 24 Sept 2026, appended f.266v's three cipher lines (82 rows, 53p2_L01-L03) as one careful hand reading with no
pass files; R11A-AVS9C (6 Oct 2026) moved those rows verbatim into f1_p2_53.tsv, the recorded input this script now
appends, so --check covers the whole S1/F1 file (ciphertext_53_s1.tsv, p1+p2). R11A-AVS53 kept that file under the
_s1 name; the current reading is ciphertext_53.tsv from settle_53n.py (native passes), not this script."""
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
    p2 = [l for l in open('f1_p2_53.tsv')][1:]  # F1's f.266v hand reading, verbatim
    return 'line\tpos\tsign\tconf\twhy\n' + ''.join('\t'.join(map(str, r)) + '\n' for r in out) + ''.join(p2)

t = build()
if '--check' in sys.argv:
    sys.exit(0 if open('ciphertext_53_s1.tsv').read() == t else 1)
open('ciphertext_53_s1.tsv', 'w').write(t)
