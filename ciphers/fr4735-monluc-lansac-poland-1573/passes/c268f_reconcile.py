#!/usr/bin/env python3
"""SUP-MONLUC (20 Oct 2026): write passes/c268f_reconciled.tsv (c268 L26-L30) from the two blind passes (one call per pass for all five
lines, PREREG-SUP-MONLUC-L26; strongest model) and this worker's eye decisions on the line crops (images/scratch268f/l26/, regen_monll26.sh).
Same logic and folder conventions as c268e_reconcile.py (MONL-L21); read before the clear text facing these lines was opened."""
import difflib, re
from pathlib import Path
P = Path(__file__).resolve().parent

EYE = {  # (line, pos in pass A numbering) -> (sign, note)
}
SPAN = {  # (line, first pos, last pos in pass A numbering) -> (token, note)
}
DROP = {}


def parse(fn):
    out = {}
    for l in (P / fn).read_text().splitlines():
        m = re.match(r'LINE (L\d+): (.*)', l)
        if m:
            out[m.group(1)] = [t.replace(' ', '_') for t in re.findall(r'\?x\[[^\]]*\]|\S+', m.group(2))]
    return out


A, B = parse('c268f_passA_raw.txt'), parse('c268f_passB_raw.txt')
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
(P / 'c268f_reconciled.tsv').write_text(''.join(rows))
n = len(rows) - 1
print(f'{n} signs, H {sum(r.split(chr(9))[3] == "H" for r in rows[1:])}, M {sum(r.split(chr(9))[3] == "M" for r in rows[1:])}')
