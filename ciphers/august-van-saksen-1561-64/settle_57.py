#!/usr/bin/env python3
"""S1, 24 Sept 2026: build ciphertext_57.tsv from recon57/ciphertext_draft.tsv (passA_57 + passB_57 reconciled by
tools/reconcile_passes.py) plus the settlements below, each decided on the image crop (images/crops_s1/57_L0n.png,
and 7x re-crops of 57 p3 L1/L4) with the reading under key_74 as a check. Run with --check to verify the committed file."""
import sys
D = 'recon57/ciphertext_draft.tsv'
# (line, pos): (sign or None to delete, why)
SET = {
 ('57_L01', 3): ('9', 'image: g-like 9, as pos 1-6 "auff . f"'), ('57_L01', 4): ('9', 'same'), ('57_L01', 6): ('9', 'same'),
 ('57_L01', 33): ('G2', 'image: closed triangle after XX (wollen); both passes read G1'),
 ('57_L01', 39): ('EL', 'image: large barred sign (as 57 L7 pos 1), not E'), ('57_L01', 40): ('COL', 'image: colon'),
 ('57_L02', 14): ('9', 'image: 9'), ('57_L02', 21): ('G6', 'image: epsilon (A missed)'),
 ('57_L02', 22): ('0', 'image: slashed 0; value g from context (wenig), M'), ('57_L02', 23): ('G1', 'image: open tent'),
 ('57_L03', 6): ('7', 'image: second 7 of "3 7 7 Z"'), ('57_L03', 25): ('6', 'image: 6 (lassen)'),
 ('57_L03', 40): ('VmV', 'image 7x: V + w-loop + V joined (VmV, Konig, key_74)'), ('57_L03', 41): ('COL', 'image: colon'),
 ('57_L03', 42): ('G3', 'image: w-loop'), ('57_L03', 43): ('3', 'image: 3'),
 ('57_L03', 44): ('G1h', 'image 7x: tent with a hook at the right foot, not plain G1; value x from context (Maximilianum), M'),
 ('57_L04', 1): ('G6', 'image'), ('57_L04', 2): ('G3', 'image: w-loop (imilianum)'), ('57_L04', 3): ('G6', 'image'),
 ('57_L04', 9): ('G3', 'image: w-loop'), ('57_L04', 14): ('8', 'image: 8 (bei)'), ('57_L04', 22): ('G3', 'image: w-loop (seinem)'),
 ('57_L04', 23): ('Z', 'Z drawn 2-like in this hand'), ('57_L04', 34): (None, 'image 7x: no sign between 7 and the double-barred Z'),
 ('57_L04', 35): ('ZZ', 'image 7x: double-barred Z = zu (key_74)'), ('57_L04', 40): ('G3', 'image 7x: w-loop'),
 ('57_L04', 43): ('G3', 'image 7x: w-loop'), ('57_L04', 47): ('5', 'image: 5'),
 ('57_L04', 48): ('1+7', 'image 7x: final 7 at the right edge, outside the pass crop (romischen)'),
 ('57_L05', 1): ('VmV', 'image 7x: V + w-loop + V joined (VmV, Konig, key_74); passes split it'), ('57_L05', 2): (None, 'second V belongs to VmV'),
 ('57_L05', 15): (None, 'image: no X before the barred sign'), ('57_L05', 16): ('Xk', 'image: barred X-like sign (konnen)'),
 ('57_L06', 25): ('3', 'image 7x: 3 with a descender (auch); both passes read 7'),
 ('57_L06', 1): ('Z', 'Z drawn 2-like in this hand'), ('57_L06', 15): ('5', 'image: 5'), ('57_L06', 23): ('6', 'image: 6 (gestalt)'),
 ('57_L07', 1): ('EL', 'image: large barred sign, as L1 pos 39'), ('57_L07', 17): ('G3', 'image: w-loop (geheim)'),
 ('57_L07', 25): ('ZZ', 'image: double-barred Z (zu halten)'), ('57_L07', 28): ('6', 'image: 6 (halten)'),
}
# ZZ at 57_L05 5-6: two passes wrote Z Z for the double-barred sign (zu erwelen)
MERGE_ZZ = {('57_L05', 4)}

def build():
    rows = [l.rstrip('\n').split('\t') for l in open(D)][1:]
    out = []
    for r in rows:
        L, p, s, c = r[0], int(r[1]), r[2], r[3]
        why = r[5] if len(r) > 5 else ''
        if (L, p) in SET:
            ns, w = SET[(L, p)]
            if ns is None:
                continue
            if ns == '1+7':
                out.append([L, '1', c, why]); out.append([L, '7', 'M', 'settled: ' + w]); continue
            s, c, why = ns, 'H', 'settled: ' + w
        elif s == 'E':
            s, c, why = 'G6', c, 'E-coded epsilon = G6 (no capital E in this block, checked on crops L1-L7)'
        out.append([L, s, c, why])
    # merge X X -> XX (w, key_74) and the listed Z Z -> ZZ
    res = []
    for L, s, c, why in out:
        if res and res[-1][0] == L and s == 'X' and res[-1][1] == 'X' and res[-1][4] == 0:
            res[-1][1] = 'XX'; res[-1][3] = 'X X written as a pair = XX (w, key_74)'; res[-1][4] = 1
            continue
        res.append([L, s, c, why, 0])
    fin, pos = [], {}
    skip = False
    for i, (L, s, c, why, _) in enumerate(res):
        pos[L] = pos.get(L, 0) + 1
        fin.append([L, pos[L], s, c, why])
    # Z Z merge at 57_L05 pos 5
    for i, r in enumerate(fin):
        if (r[0], r[1]) in MERGE_ZZ and fin[i + 1][2] == 'Z' and r[2] == 'Z':
            r[2] = 'ZZ'; r[4] = 'settled: image, double-barred Z (zu erwelen); passes wrote Z Z'
            del fin[i + 1]
            break
    pos = {}
    for r in fin:
        pos[r[0]] = pos.get(r[0], 0) + 1; r[1] = pos[r[0]]
    return 'line\tpos\tsign\tconf\twhy\n' + ''.join('\t'.join(map(str, r)) + '\n' for r in fin)

txt = build()
if '--check' in sys.argv:
    sys.exit(0 if open('ciphertext_57.tsv').read() == txt else 1)
open('ciphertext_57.tsv', 'w').write(txt)
