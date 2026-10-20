#!/usr/bin/env python3
"""MONL-C269A (20 Oct 2026): write c269/c269_reconciled.tsv (c269 = f.138v, L01-L10) from the two blind passes (strongest model, one call
per 5 lines per pass, PREREG-MONL-C269A.md) and this worker's eye decisions on the levelled crops (images/scratch269/l01/, regen_monlc269.sh).
Same logic as passes/c268f_reconcile.py: conf H = both passes agree after sequence match; M = split, settled by rule/EYE/SPAN, else pass A.
Read before any c269 decode or clear text was looked at. Folder conventions (c268e_reconcile.py header): round g with closed bottom loop
= K01, 9 with left-sweeping tail = K12 (MONL-EYE); hooked-ascender b = K14 (both c172/c268 jobs, NOTES MONL-C268B table); z in a C-curl
= K38 (A K61 / B K57 here, as c268f); theta = K09; 'h' form = ?h_bar."""
import difflib, re
from pathlib import Path
P = Path(__file__).resolve().parent

EYE = {  # (line, pos in pass A numbering) -> (sign, note)
    ('L06', 15): ('?h_bar', "eye: 'h' with a left-curling descender = folder 'h' form ?h_bar (A ?x[h with long descender], B K19)"),
    ('L08', 19): ('?h_bar', "eye: same 'h' form as L06:15 (A ?x[h with long descender], B K19)"),
    ('L10', 28): ('?h_bar', "eye: same 'h' form as L06:15 (A ?x[h with long descender], B K19)"),
}
# Remaining splits at line ends (L02:25-29, L03:29-32, L05:34-35, L06:28-30): small signs running into the gutter that pass B left
# out; checked on the crops (images/scratch269/z_ends.jpg): pass A's extra signs are real ink of the line, kept as pass A, M.
RULE_BOTH = {'K68': ('?h_bar', "'h' form, folder convention ?h_bar (both passes K68)")}
RULE_SPLIT = {('K01', 'K12'): ('K01', 'eye (L01:1,6, L02:2,5): round g with closed bottom loop = K01 (A K01, B K12)'),
              ('K14', 'K49'): ('K14', 'eye (L01:3, L02:1): hooked-ascender b = folder K14 (A K14, B K49)'),
              ('K61', 'K57'): ('K38', 'z inside a C-curl = K38 (A K61, B K57; c268f rule)'),
              ('K21', 'K09'): ('K09', 'theta = K09 (A K21, B K09)')}
SPAN = {  # (line, first pos, last pos in pass A numbering) -> (token, note)
    ('L01', 10, 13): ('W:Sepbre', "eye: clear 'Sep.' with superscript 'bre' (overview); = B W:Sepbre (A K27 K15 K29 ?x[dot]); c268 has W:Sepbre"),
    ('L04', 13, 13): ('W:Mare', "eye: the clear word Mare (overview, the folder's W:Mare); A W:Maur, B K46 K66 K05 K57"),
    ('L01', 29, 29): ('?x[faded_end]', 'small faded signs run into the gutter (A W:cyrf, B none); unread'),
}
DROP = {}


def parse(fn):
    out = {}
    for f in fn:
        for l in (P / f).read_text().splitlines():
            m = re.match(r'LINE (L\d+): (.*)', l)
            if m:
                out[m.group(1)] = [t.replace(' ', '_') for t in re.findall(r'\?x\[[^\]]*\]|\S+', m.group(2))]
    return out


A, B = parse(['passA1_raw.txt', 'passA2_raw.txt']), parse(['passB1_raw.txt', 'passB2_raw.txt'])
rows = ['line\tpos\tsign\tconf\tpass_a\tpass_b\thow\n']
agree = tot = 0
for lab in sorted(A):
    a, b = A[lab], B[lab]
    bpos = {}
    for t, i1, i2, j1, j2 in difflib.SequenceMatcher(None, a, b, autojunk=False).get_opcodes():
        if t in ('equal', 'replace') and i2 - i1 == j2 - j1:
            for k in range(i2 - i1):
                bpos[i1 + k] = (b[j1 + k], t == 'equal')
    agree += sum(e for _, e in bpos.values()); tot += max(len(a), len(b))
    out, skip = [], set()
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
            sign, how = EYE[(lab, p)]
            out.append((sign, 'M', ta, tb, how))
        elif eq:
            out.append((ta, 'H', ta, tb, 'both passes'))
        else:
            out.append((ta, 'M', ta, tb, 'A/B split, crop does not settle it: pass A'))
    for n, (sign, conf, ta, tb, how) in enumerate(out, 1):
        rows.append(f'{lab}\t{n}\t{sign}\t{conf}\t{ta}\t{tb}\t{how}\n')
(P / 'c269_reconciled.tsv').write_text(''.join(rows))
n = len(rows) - 1
print(f'agreement {agree}/{tot} = {agree / tot:.3f}; {n} signs, H {sum(r.split(chr(9))[3] == "H" for r in rows[1:])}, '
      f'M {sum(r.split(chr(9))[3] == "M" for r in rows[1:])}')
