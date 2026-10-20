#!/usr/bin/env python3
"""SUP-MONLUC (20 Oct 2026): write passes/c268f_reconciled.tsv (c268 L26-L30) from the two blind passes (one call per pass for all five
lines, PREREG-SUP-MONLUC-L26; strongest model) and this worker's eye decisions on the line crops (images/scratch268f/l26/, regen_monll26.sh).
Same logic and folder conventions as c268e_reconcile.py (MONL-L21); read before the clear text facing these lines was opened."""
import difflib, re
from pathlib import Path
P = Path(__file__).resolve().parent

EYE = {  # (line, pos in pass A numbering) -> (sign, note); built by the rules below, each checked on the crops by eye
}
# Folder conventions applied by rule (c268e_reconcile.py header): stem with diamond foot = K36 (A K49 / B K36 split, both
# diamond-foot on the crops); 'h' form = ?h_bar (both passes K68); z inside a C-curl = K38 (A K61 / B K57, a sign never used
# in c268 L01-L25, the curl visible at every one on the crops); theta = K09 (A K09 / B K21; K21 0 times in L01-L25);
# hash-like = K16 (A K20 / B K16; K16 6, K20 1 in L01-L25). Other splits (K12|K22, K50|?x, K16|K50 at L27:13): pass A, conf M.
RULE_BOTH = {'K68': ('?h_bar', "eye: 'h' form, folder convention ?h_bar (both passes K68)")}
RULE_SPLIT = {('K49', 'K36'): ('K36', 'eye: stem with diamond foot = K36 (A K49, B K36)'),
              ('K61', 'K57'): ('K38', 'eye: z inside a C-curl = K38 (A K61, B K57)'),
              ('K09', 'K21'): ('K09', 'theta = K09 (A K09, B K21; K21 unused in L01-L25)'),
              ('K20', 'K16'): ('K16', 'hash form = K16 (A K20, B K16)'),
              ('K14', 'K36'): ('K36', 'eye (L26:23, 27): stem with diamond foot = K36; = B (A K14)')}
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
        elif (ta, tb) in RULE_SPLIT and not eq:
            sign, how = RULE_SPLIT[(ta, tb)]
            out.append((sign, 'M', ta, tb, how))
        elif eq and ta in RULE_BOTH:
            sign, how = RULE_BOTH[ta]
            out.append((sign, 'M', ta, tb, how))
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
