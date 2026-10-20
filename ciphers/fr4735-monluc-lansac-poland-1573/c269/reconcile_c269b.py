#!/usr/bin/env python3
"""MONL-C269B (20 Oct 2026): write c269/c269b_reconciled.tsv (c269 = f.138v, L11-L22) from the two blind passes (strongest model, one call
per 6 lines per pass, PREREG-MONL-C269B.md) and this worker's eye decisions on the levelled crops (images/scratch269/l11/, regen_monlc269b.sh).
reconcile_c269.py's logic and folder conventions; read before any c269 L11-L22 decode or clear text was looked at."""
import difflib, re
from pathlib import Path
P = Path(__file__).resolve().parent

EYE = {}
RULE_BOTH = {'K68': ('?h_bar', "'h' form, folder convention ?h_bar (both passes K68)")}
RULE_SPLIT = {('K01', 'K12'): ('K01', 'round g with closed bottom loop = K01 (A K01, B K12; MONL-C269A eye rule)'),
              ('K38', 'K57'): ('K38', 'z inside a C-curl = K38 (A K38, B K57; c268f rule)'),
              ('K19', 'K38'): ('K38', 'eye (L20:1, L18:15): z inside a C-curl = K38 (A K19 read the z alone, B K38)'),
              ('K22', 'K12'): ('K22', 'eye (L18:9, L18:13): g with a closed bottom loop, not a 9 with a sweeping tail (A K22, B K12)'),
              ('K14', 'K36'): ('K36', 'stem with diamond foot = K36 (folder rule; A K14, B K36)'),
              ('K61', 'K57'): ('K38', 'z inside a C-curl = K38 (c268f rule)')}
SPAN = {  # (line, first pos, last pos in pass A numbering) -> (token, note)
    ('L16', 27, 28): ('W:Mare', "eye: the clear word Mara at the line end (folder W:Mare); A K48 W:ara, B K46 W:au"),
    ('L18', 23, 23): ('W:Juno', "eye: clear 'Jung' (folder W:Juno); A/B W:Juing"),
    ('L18', 24, 24): ('W:Nobre', "eye: clear 'No' with superscript 'bre'; A W:Nobre, B W:No.bre"),
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


A, B = parse(['passA3_raw.txt', 'passA4_raw.txt']), parse(['passB3_raw.txt', 'passB4_raw.txt'])
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
(P / 'c269b_reconciled.tsv').write_text(''.join(rows))
n = len(rows) - 1
print(f'agreement {agree}/{tot} = {agree / tot:.3f}; {n} signs, H {sum(r.split(chr(9))[3] == "H" for r in rows[1:])}, '
      f'M {sum(r.split(chr(9))[3] == "M" for r in rows[1:])}')
