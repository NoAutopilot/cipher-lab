#!/usr/bin/env python3
"""MONL-L16 (15 Oct 2026): write passes/c268d_reconciled.tsv (c268 L16-L20) from the two blind passes and this worker's eye
decisions on the native line crops (images/scratch268d/l16/, regen_monll16.sh). conf H = both passes agree (same position after
sequence match); conf M = an A/B split, settled by EYE below where the crop settles it, else pass A (the folder's base pass).
Read before the clear text facing these lines was opened (blind to the clear text; not blind to the key-sheet ids or to the
folder's sign conventions: K04 straight stem vs K12 curving descender, MONL-EYE; stem with diamond foot = K36, MONL-C268B;
C-curl = K38, MONLUC-RELABEL; cross with a loop to the upper right = K62, MONL-L11). Same logic as c268c_reconcile.py, plus
SPAN: a run of pass-A tokens the eye reads as one clear-written word (W:), the rest of the run dropped."""
import difflib, re
from pathlib import Path
P = Path(__file__).resolve().parent

EYE = {  # (line, pos in pass A numbering) -> (sign, note)
    ('L16', 11): ('K04', 'eye: straight stem after m; = A (B K12)'),
    ('L16', 28): ('K39', 'eye: y-form with long tail; = A (B K19)'),
    ('L17', 15): ('?x[epsilon]', 'eye: open epsilon, not c; = A (folder label ?x[epsilon], L13:19); B K15'),
    ('L17', 27): ('K38', 'eye: z-like sign inside a large curl = C-curl K38; = A (B K54 K63)'),
    ('L18', 8): ('K36', 'eye: stem with diamond foot; = A (B K14)'),
    ('L18', 25): ('K01', 'eye: plain round g, no bar; = A (B K22)'),
    ('L19', 8): ('K36', 'eye: stem with diamond foot; = B (A K14)'),
    ('L19', 17): ('K14', 'eye: b-form; = B (A K17)'),
    ('L19', 23): ('K05', 'eye: r-form; = A (B K37)'),
    ('L19', 28): ('K36', 'eye: stem with diamond foot; = B (A K14)'),
    ('L20', 13): ('K45', 'eye: small v/gamma without long tail; = A (B K39)'),
    ('L20', 21): ('K04', 'eye: straight stem; = B (A K01)'),
    ('L20', 29): ('K62', 'eye: bold cross with a flag to the upper right; = A (B K11)'),
    ('L20', 30): ('K38', 'eye: small z inside a large curl = C-curl K38; = A (B ?x[large arc enclosing a small 3])'),
}
SPAN = {  # (line, first pos, last pos in pass A numbering) -> (token, note)
    ('L18', 15, 18): ('W:Sepbre', "eye: '8cp' with superscript 'bre' is the clear-written word Sep^bre (the '8' an S), after W:Juillet; A K27 K15 K08 W:bre, B K27 K15 K29 ?x[b with superscript re]"),
}
DROP = {('L18', 33): "eye: the stroke 'below the line' is the descender of the preceding long s, not a sign; A ?x[b below line], B none"}


def parse(fn):
    out = {}
    for l in (P / fn).read_text().splitlines():
        m = re.match(r'LINE (L\d+): (.*)', l)
        if m:
            out[m.group(1)] = [t.replace(' ', '_') for t in re.findall(r'\?x\[[^\]]*\]|\S+', m.group(2))]
    return out


A, B = parse('c268d_passA_raw.txt'), parse('c268d_passB_raw.txt')
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
(P / 'c268d_reconciled.tsv').write_text(''.join(rows))
n = len(rows) - 1
print(f'{n} signs, H {sum(r.split(chr(9))[3] == "H" for r in rows[1:])}, M {sum(r.split(chr(9))[3] == "M" for r in rows[1:])}')
