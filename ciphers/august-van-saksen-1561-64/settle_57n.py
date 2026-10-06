#!/usr/bin/env python3
"""R11A-AVS57, 6 Oct 2026: build ciphertext_57.tsv (native re-read of WVO 57 p3) from recon57n/ciphertext_draft.tsv
(passA_57n + passB_57n, two blind Sonnet passes on images/crops_r11a57/, reconciled by tools/reconcile_passes.py) plus the
settlements below, each decided on the native crops (2-4x zooms of images/crops_r11a57/57n_L0n.jpg). Agreed rows one pass
flagged doubtful (recon57n/uncertain.tsv) were looked at on the same zooms and are kept at H unless SET names them.
X X written as one joined pair is merged to XX (w, key_74), as S1 did. The 100 dpi S1 file is kept as
ciphertext_57_s1.tsv. Run with --check to verify the committed file."""
import os, sys
os.chdir(os.path.dirname(os.path.abspath(__file__)))
D = 'recon57n/ciphertext_draft.tsv'
OUT = 'ciphertext_57.tsv'
# (line, draft position): list of (sign, conf, why) to put in its place ([] deletes it)
SET = {
 ('57_L01', 9): [('X', 'H', 'native: plain x (freundtlich); B read Xk')],
 ('57_L01', 23): [('V', 'H', 'native: V, then a separate tent; both passes joined them as VmV'),
                  ('G1', 'M', 'native: open tent with an arc drawn over its apex; t by context (uertrawen), shape not plain')],
 ('57_L01', 31): [], ('57_L01', 32): [('X', 'H', 'native: x x then the triangle (wollen)')],
 ('57_L01', 33): [('X', 'H', 'native: second x of the pair; B read G1')],
 ('57_L02', 38): [], ('57_L03', 39): [],
 ('57_L02', 39): [('1', 'M', 'native: two upright strokes between 7 and T (both passes count two); "seine stadtliche" expects one; the first is thin and may be the 7\'s tail, so this one stays M')],
 ('57_L03', 5): [('7', 'H', 'agree'), ('7', 'H', 'native: second 7 of "T 3 7 7 Z" (gesanndt); both passes read one')],
 ('57_L03', 40): [('VmV', 'H', 'native: radical-like stroke + loop with an arc + V, one joined group as at L5 start (Konig); A read J 0 V, B G3 V')],
 ('57_L03', 41): [],
 ('57_L03', 42): [('COL', 'H', 'native: colon after the group')],
 ('57_L03', 45): [('G1h', 'H', 'native: tent with a flick at the right foot, then a separate comma; the flick looks like the right feet of L1\'s two closing tents, so the shape alone does not separate G1h from G1; value x by context (exceptions_57.tsv, M)')],
 ('57_L04', 2): [('G3', 'H', 'native: bar over a w-loop (m, imilianum); B read G4')],
 ('57_L04', 9): [('G3', 'H', 'native: as pos 2')], ('57_L04', 22): [('G3', 'H', 'native: as pos 2 (seinem)')],
 ('57_L04', 30): [], ('57_L04', 31): [], ('57_L04', 36): [],
 ('57_L04', 37): [('ZZ', 'H', 'native: one z with two bars (zu); A read Zb, B ZZ')],
 ('57_L04', 40): [('COL', 'H', 'native: slanted colon (B coded it NEW1)')],
 ('57_L05', 1): [('VmV', 'H', 'native: same joined group as L3 (Konig); A read J G3, B G3 V')],
 ('57_L05', 2): [], ('57_L05', 3): [],
 ('57_L05', 6): [('ZZ', 'H', 'native: the two barred z strokes are one joined sign (zu erwelen), as S1 settled')],
 ('57_L05', 7): [],
 ('57_L05', 16): [], ('57_L05', 17): [('Xk', 'H', 'native: x with a bar (konnen); A read 3 + G6')],
 ('57_L05', 30): [],
 ('57_L05', 38): [('X', 'H', 'native: x x pair (werde)')], ('57_L05', 39): [('X', 'H', 'native: second x of the pair; B read Xk')],
 ('57_L06', 25): [('3', 'H', 'native: 3 with a descender (auch); A read Xy')],
 ('57_L07', 16): [],
 ('57_L07', 26): [('ZZ', 'H', 'native: double-barred z (zu halten); A read Z')],
 ('57_L07', 31): [('COL', 'H', 'native: two dots')],
}

def build():
    rows = [l.rstrip('\n').split('\t') for l in open(D)][1:]
    out = []
    for r in rows:
        L, p, s, c, why = r[0], int(r[1]), r[2], r[3], r[5]
        if (L, p) in SET:
            for ns, nc, w in SET[(L, p)]:
                out.append([L, ns, nc, w if w == 'agree' else 'settled: ' + w])
            continue
        if why != 'agree' or c != 'H':
            why, c = 'checked on native zoom: ' + why, 'H'
        out.append([L, s, c, why])
    res = []
    for L, s, c, why in out:
        if res and res[-1][0] == L and s == 'X' and res[-1][1] == 'X' and not res[-1][4]:
            res[-1][1] = 'XX'; res[-1][3] = 'X X written as a pair = XX (w, key_74)'; res[-1][4] = 1
            continue
        res.append([L, s, c, why, 0])
    lines, pos = ['line\tpos\tsign\tconf\twhy'], {}
    for L, s, c, why, _ in res:
        pos[L] = pos.get(L, 0) + 1
        lines.append(f'{L}\t{pos[L]}\t{s}\t{c}\t{why}')
    return '\n'.join(lines) + '\n'

if __name__ == '__main__':
    t = build()
    if '--check' in sys.argv:
        ok = open(OUT).read() == t
        print('ciphertext_57.tsv ' + ('up to date' if ok else 'STALE')); sys.exit(0 if ok else 1)
    open(OUT, 'w').write(t); print('wrote', OUT)
