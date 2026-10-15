#!/usr/bin/env python3
"""MONL-L21 (15 Oct 2026): write passes/c268e_reconciled.tsv (c268 L21-L25) from the two blind passes (one Sonnet call per pass for all five
lines, PREREG-MONL-L21) and this worker's eye decisions on the native line crops (images/scratch268e/l21/, regen_monll21.sh). conf H = both
passes agree (same position after sequence match); conf M = an A/B split, settled by EYE below where the crop settles it, else pass A.
Read before the clear text facing these lines was opened (blind to the clear text; not blind to the key-sheet ids or to the folder's sign
conventions: K04 straight stem vs K12 curving descender, MONL-EYE; stem with diamond foot = K36, MONL-C268B; C-curl Z = K38, MONLUC-RELABEL;
cross with a loop to the upper right = K62, MONL-L11; 'h' = ?h_bar, MONL-L11 L11:8; small v without tail = K45, MONL-L16 L20:13; pass B's
K47 for the y-form is the folder's K39, 0 K47 in c268 L01-L20). Same logic as c268d_reconcile.py (EYE, SPAN, DROP); EYE may override an
A/B agreement where the crop shows a stroke both passes missed (noted per entry)."""
import difflib, re
from pathlib import Path
P = Path(__file__).resolve().parent

EYE = {  # (line, pos in pass A numbering) -> (sign, note)
    ('L21', 14): ('K38', 'eye: z with a faint curl to its left = C-curl K38 (A K63, B K19)'),
    ('L21', 35): ('K01', 'eye: round g with closed bottom loop; = B (A K12)'),
    ('L22', 2): ('?h_bar', "eye: 'h' form, folder convention ?h_bar (MONL-L11 L11:8); A ?x[h], B K68"),
    ('L22', 6): ('K40', 'eye: omega with a bar over it = K40; both passes K41 (override of an agreement)'),
    ('L22', 12): ('K29', 'eye: rho with leftward descender = K29; = B (A K26)'),
    ('L22', 23): ('K36', "eye (zoom): after 'B m' a stem with diamond foot = K36; = B's K36 (A K14; B's extra K35 is the m's last minim)"),
    ('L22', 24): ('K38', 'eye (zoom): z with a large curl below-left = C-curl K38 (A K63, B K19)'),
    ('L22', 27): ('?h_bar', "eye: 'h' form, as L22:2; A ?x[h], B K68"),
    ('L23', 21): ('K01', 'eye: round g like its neighbours, not a curving 9; = B (A K12)'),
    ('L24', 3): ('K45', 'eye: small v without tail = K45 (MONL-L16 L20:13 convention); A K39, B K47'),
    ('L24', 16): ('K45', 'eye: small v without tail, as L24:3 = K45; A ?x[v], B K47'),
    ('L24', 27): ('K38', 'eye: z inside a large curl = C-curl K38 (A K63, B K19)'),
    ('L25', 14): ('K08', 'eye: phi form as L21:1 = K08; = B (A K60)'),
    ('L25', 16): ('K40', 'eye: omega with a bar over it = K40; both passes K41 (override of an agreement)'),
}
SPAN = {  # (line, first pos, last pos in pass A numbering) -> (token, note)
    ('L23', 1, 3): ('W:Astuing', "eye: one clear-written word, the long s joined to 'tuing'; = B (A ?x[u with arc] K26 W:tuing)"),
}
DROP = {}


def parse(fn):
    out = {}
    for l in (P / fn).read_text().splitlines():
        m = re.match(r'LINE (L\d+): (.*)', l)
        if m:
            out[m.group(1)] = [t.replace(' ', '_') for t in re.findall(r'\?x\[[^\]]*\]|\S+', m.group(2))]
    return out


A, B = parse('c268e_passA_raw.txt'), parse('c268e_passB_raw.txt')
rows = ['line\tpos\tsign\tconf\tpass_a\tpass_b\thow\n']
for lab in sorted(A):
    a, b = A[lab], B[lab]
    bpos = {}
    for t, i1, i2, j1, j2 in difflib.SequenceMatcher(None, a, b, autojunk=False).get_opcodes():
        if t in ('equal', 'replace') and i2 - i1 == j2 - j1:
            for k in range(i2 - i1):
                bpos[i1 + k] = (b[j1 + k], t == 'equal')
    out = []
    skip = set()
    for (sl, s1, s2), (tok, note) in SPAN.items():
        if sl == lab:
            skip |= set(range(s1 + 1, s2 + 1))
    for i, ta in enumerate(a):
        p = i + 1
        tb, eq = bpos.get(i, ('-', False))
        if p in skip or (lab, p) in DROP:
            continue
        span = [(tok, note, s2) for (sl, s1, s2), (tok, note) in SPAN.items() if sl == lab and s1 == p]
        if span:
            tok, note, s2 = span[0]
            out.append((tok, 'M', ' '.join(a[i:s2]), ' '.join(bpos.get(k, ('-',))[0] for k in range(i, s2)), note))
        elif (lab, p) in EYE:
            (sign, how) = EYE[(lab, p)]
            out.append((sign, 'M', ta, tb, how))
        elif eq:
            out.append((ta, 'H', ta, tb, 'both passes'))
        else:
            out.append((ta, 'M', ta, tb, 'A/B split, crop does not settle it: pass A'))
    for n, (sign, conf, ta, tb, how) in enumerate(out, 1):
        rows.append(f'{lab}\t{n}\t{sign}\t{conf}\t{ta}\t{tb}\t{how}\n')
(P / 'c268e_reconciled.tsv').write_text(''.join(rows))
n = len(rows) - 1
print(f'{n} signs, H {sum(r.split(chr(9))[3] == "H" for r in rows[1:])}, M {sum(r.split(chr(9))[3] == "M" for r in rows[1:])}')
