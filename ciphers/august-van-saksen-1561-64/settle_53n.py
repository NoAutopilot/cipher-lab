#!/usr/bin/env python3
"""R11A-AVS53, 6 Oct 2026: build ciphertext_53.tsv (native re-read of WVO 53 p1+p2, f.266r-v) from recon53n/ciphertext_draft.tsv
(passA_53n + passB_53n, two blind Sonnet passes per page on images/crops_r11a53/, reconciled by tools/reconcile_passes.py) plus the
settlements below, each decided on 1.6-3x zooms of the native crops. Agreed rows that one pass flagged (recon53n/uncertain.tsv; pass A
flagged every G1/G7/SG/Z/G6 row mechanically) were looked at on the same zooms and are kept at H unless SET names them.
Also writes exceptions_53.tsv: the two sign-9 rows (F1) at their new positions, and an AVS53 regrade row only where the native token is
still M with the same sign (mapped from the S1 positions by sign alignment). The S1/F1 100 dpi file is kept as ciphertext_53_s1.tsv and its
exceptions as exceptions_53_s1.tsv (regrade_53.py / regrade_53b.py / settle_53.py read those). Run with --check to verify both files."""
import difflib, os, sys
os.chdir(os.path.dirname(os.path.abspath(__file__)))
D, OUT, EXO = 'recon53n/ciphertext_draft.tsv', 'ciphertext_53.tsv', 'exceptions_53.tsv'
# (line, draft position): list of (sign, conf, why) to put in its place ([] deletes it)
SET = {
 ('53_L01', 28): [('Z', 'H', 'native: barred z as at pos 9, not the 4 of pos 20 ("itz-mals"); S1 read 4 (itc-)')],
 ('53_L06', 4): [('G7', 'H', 'native: first of two lambdas (diesse)')],
 ('53_L06', 5): [],
 ('53_L06', 6): [('G7', 'H', 'native: second of two lambdas; both passes read a third sign between them, there are two')],
 ('53_L06', 32): [('G7', 'H', 'native: lambda (sollen)')],
 ('53_L06', 33): [('G2', 'M', 'native: tent with a faint hairline base, read as the triangle (o, sollen); pass B coded the same sign twice (G1 G2), A as G1')],
 ('53_L06', 34): [],
 ('53_L09', 20): [('V', 'M', 'native: V under an ink blot (nauarra), as S1')],
 ('53p2_L01', 1): [('2', 'H', 'native: same curled d-sign as pos 12; B read Z')],
 ('53p2_L01', 18): [('X', 'H', 'native: plain x (uueil); A read Xk')],
 ('53p2_L01', 19): [('SG', 'H', 'native: sigma loop with the long stroke over the next sign; A read 6')],
 ('53p2_L01', 20): [('2', 'H', 'native: d-sign under that stroke; B read Z')],
 ('53p2_L02', 11): [('G7', 'H', 'native: lambda with its hook (so); both passes read X')],
 ('53p2_L02', 13): [],
 ('53p2_L02', 14): [('X', 'H', 'native: x with a dot above it, one sign (i, iung); A read DOT 1')],
 ('53p2_L02', 27): [('2', 'H', 'native: unbarred d-sign; B read Z')],
 ('53p2_L02', 28): [('1', 'M', 'native: an upright stroke with a loop attached (blotted or overwritten); both passes read G4 (p), e by context (uuerde), as F1')],
 ('53p2_L03', 11): [('7', 'M', 'native: second of the pair carries a stroke across its foot like a barred z; u by context (geuuinnen); A read Z')],
 ('53p2_L03', 14): [('5', 'M', 'native: an S-like sign with a hooked descender, nearer 9 than the 5 before it; n by context (geuuinnen); B read 9')],
}

def build():
    rows = [l.rstrip('\n').split('\t') for l in open(D)][1:]
    out = []
    for r in rows:
        L, p, s, c, why = r[0], int(r[1]), r[2], r[3], r[5]
        if (L, p) in SET:
            for ns, nc, w in SET[(L, p)]:
                out.append([L, ns, nc, 'settled: ' + w])
            continue
        if why != 'agree' or c != 'H':
            why, c = 'checked on native zoom: ' + why, 'H'
        out.append([L, s, c, why])
    lines, pos, res = ['line\tpos\tsign\tconf\twhy'], {}, []
    for L, s, c, why in out:
        pos[L] = pos.get(L, 0) + 1
        res.append((L, pos[L], s, c))
        lines.append(f'{L}\t{pos[L]}\t{s}\t{c}\t{why}')
    return '\n'.join(lines) + '\n', res

def exceptions(res):
    old = [l.rstrip('\n').split('\t') for l in open('ciphertext_53_s1.tsv')][1:]
    oex = [l.rstrip('\n').split('\t') for l in open('exceptions_53_s1.tsv')][1:]
    m = {}
    for L in dict.fromkeys(r[0] for r in old):
        a = [r for r in old if r[0] == L]; b = [r for r in res if r[0] == L]
        for op, i1, i2, j1, j2 in difflib.SequenceMatcher(None, [r[2] for r in a], [r[2] for r in b], autojunk=False).get_opcodes():
            if op == 'equal':
                for k in range(i2 - i1):
                    m[(L, int(a[i1 + k][1]))] = b[j1 + k]
    ex = ['line\tpos\tvalue\tgrade\treason']
    for L, p, v, g, why in oex:
        n = m.get((L, int(p)))
        if n is None:
            continue
        if 'AVS53' in why and n[3] != 'M':
            continue  # the native re-read settles this token; key_53's own grade applies
        ex.append('\t'.join([L, str(n[1]), v, g, why + ('' if 'AVS53' not in why else '; kept: still M after the native re-read (R11A-AVS53)')]))
    return '\n'.join(ex) + '\n'

if __name__ == '__main__':
    t, res = build(); e = exceptions(res)
    if '--check' in sys.argv:
        ok = open(OUT).read() == t and open(EXO).read() == e
        print('ciphertext_53.tsv + exceptions_53.tsv ' + ('up to date' if ok else 'STALE')); sys.exit(0 if ok else 1)
    open(OUT, 'w').write(t); open(EXO, 'w').write(e); print('wrote', OUT, EXO)
