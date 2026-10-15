#!/usr/bin/env python3
"""MONL-L11 (15 Oct 2026): write passes/c268c_reconciled.tsv (c268 L11-L15) from the two blind passes and this worker's eye
decisions on the native line crops (images/scratch268c/l11/, regen_monll11.sh). conf H = both passes agree (same position after
sequence match); conf M = an A/B split, settled by EYE below where the crop settles it, else pass A (the folder's base pass).
Read before the clear text facing these lines was opened (blind to the clear text; not blind to the key sheet ids or to the
folder's sign conventions: K04 straight blunt stem vs K12 curving descender, MONL-EYE; stem with diamond foot = K36, MONL-C268B)."""
import difflib, re
from pathlib import Path
P = Path(__file__).resolve().parent

EYE = {  # (line, pos in pass A numbering) -> (sign, note)
    ('L11', 2): ('K04', 'eye: straight stem (K04|K12 rule); = B'),
    ('L11', 8): ('?h_bar', 'eye: h with a stroke through the stem, folder convention ?h_bar; = A (B K68)'),
    ('L11', 12): ('K11', 'eye: cross with a top loop; = B'),
    ('L11', 13): ('K01', 'eye: round g with left-hooked tail; = B (A K12); A/B misaligned here, B reads K11 K01 K04 K12 for A K10 K12 K04 K04'),
    ('L11', 14): ('K04', 'eye unsure (curving or straight); both passes K04 at this slot'),
    ('L11', 15): ('K04', 'eye: long straight stem; = A (B K12)'),
    ('L13', 1): ('K35', 'eye: plain h-form, no crossbar; = B'),
    ('L13', 21): ('K26', 'eye: one long stroke, not //; = B'),
    ('L13', 30): ('K26', 'eye: one long stroke, not //; = B'),
    ('L13', 31): ('K63', 'eye: z with swash below; = B (A K19); possible C-curl K38 form, unsettled'),
    ('L14', 4): ('K12', 'eye: curving descender; = A'),
    ('L14', 5): ('K36', 'eye: stem with diamond foot; = A'),
    ('L14', 6): ('K04', 'eye: straight stem; = B'),
    ('L14', 11): ('K36', 'eye: stem with diamond foot; = A'),
    ('L14', 15): ('K36', 'eye: stem with diamond foot; = A'),
    ('L14', 22): ('K36', 'eye: stem with diamond foot; = A'),
    ('L14', 27): ('K04', 'eye: long straight stem; = B'),
    ('L14', 28): ('K39', 'eye: y-form; = B'),
    ('L14', 29): ('K36', 'eye: stem with diamond foot; = A'),
    ('L15', 9): ('K62', 'eye: cross with loop to the upper right; = B'),
    ('L15', 18): ('K62', 'eye: cross with loop to the upper right; = B'),
}
SPLIT_NAMES = {'?x[large_looped_initial]': '?x[looped_initial]', '?x[g-like]': '?x[g_like_blotted]', '?x[ink_blot]': '?x[ink_blot]'}


def parse(fn):
    out = {}
    for l in (P / fn).read_text().splitlines():
        m = re.match(r'LINE (L\d+): (.*)', l)
        if m:
            out[m.group(1)] = [t.replace(' ', '_') for t in re.findall(r'\?x\[[^\]]*\]|\S+', m.group(2))]
    return out


A, B = parse('c268c_passA_raw.txt'), parse('c268c_passB_raw.txt')
rows = ['line\tpos\tsign\tconf\tpass_a\tpass_b\thow\n']
for lab in sorted(A):
    a, b = A[lab], B[lab]
    bpos = {}
    for t, i1, i2, j1, j2 in difflib.SequenceMatcher(None, a, b, autojunk=False).get_opcodes():
        if t in ('equal', 'replace') and i2 - i1 == j2 - j1:
            for k in range(i2 - i1):
                bpos[i1 + k] = (b[j1 + k], t == 'equal')
    for i, ta in enumerate(a):
        tb, eq = bpos.get(i, ('-', False))
        if (lab, i + 1) in EYE:  # an eye decision wins over a sequence-match 'agreement' inside a misaligned span (L11:12-15)
            (sign, how), conf = EYE[(lab, i + 1)], 'M'
        elif eq:
            sign, conf, how = ta, 'H', 'both passes'
        else:
            sign, conf, how = SPLIT_NAMES.get(ta, ta), 'M', 'A/B split, crop does not settle it: pass A'
        rows.append(f'{lab}\t{i+1}\t{sign}\t{conf}\t{ta}\t{tb}\t{how}\n')
(P / 'c268c_reconciled.tsv').write_text(''.join(rows))
n = len(rows) - 1
print(f'{n} signs, H {sum(r.split(chr(9))[3] == "H" for r in rows[1:])}, M {sum(r.split(chr(9))[3] == "M" for r in rows[1:])}')
