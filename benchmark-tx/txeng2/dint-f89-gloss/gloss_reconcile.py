#!/usr/bin/env python3
"""TXP-D89: gloss.tsv from the two blind gloss reads glossA.tsv / glossB.tsv. Per line, letter-level difflib on the two
texts (struck [..] text dropped first): letters both readers agree on are kept; every stretch where they differ becomes
'?' (one per letter of the longer side), so a split is never guessed and later counts as gloss-unread (excluded). Word
spaces are kept where both readings have them. conf = the lower of the two readers' line conf. Mechanical (no Sonnet
look: a deviation from the brief, stated in RESULTS.md, to stay under the 80% cap line).
    python3 gloss_reconcile.py [--check]"""
import csv, difflib, os, re, sys
H = os.path.dirname(os.path.abspath(__file__))
rd = lambda p: {r['line']: r for r in csv.DictReader(open(p, newline=''), delimiter='\t')}
A, B = rd(os.path.join(H, 'glossA.tsv')), rd(os.path.join(H, 'glossB.tsv'))
ORDER = {'H': 2, 'M': 1, 'L': 0}


def clean(t):
    t = re.sub(r'\[[^\]]*\]', ' ', t or '')
    return re.sub(r'\s+', ' ', t).strip()


out = ['line\ttext\tconf\tagree_letters\tletters']
tot_ag = tot = 0
for ln in sorted(set(A) | set(B)):
    a, b = clean(A.get(ln, {}).get('text')), clean(B.get(ln, {}).get('text'))
    sm = difflib.SequenceMatcher(None, a, b, autojunk=False)
    res, ag = [], 0
    for op, i1, i2, j1, j2 in sm.get_opcodes():
        if op == 'equal':
            res.append(a[i1:i2]); ag += sum(1 for c in a[i1:i2] if c != ' ')
        else:
            seg_a, seg_b = a[i1:i2], b[j1:j2]
            n = max(len(seg_a.replace(' ', '')), len(seg_b.replace(' ', '')))
            res.append('?' * n if n else (' ' if ' ' in seg_a + seg_b else ''))
    text = re.sub(r'\s+', ' ', ''.join(res)).strip()
    n = len(text.replace(' ', ''))
    ca, cb = A.get(ln, {}).get('conf', 'L'), B.get(ln, {}).get('conf', 'L')
    conf = min((ca, cb), key=lambda c: ORDER.get(c, 0))
    out.append('%s\t%s\t%s\t%d\t%d' % (ln, text, conf, ag, n))
    tot_ag += ag; tot += n
t = '\n'.join(out) + '\n'
p = os.path.join(H, 'gloss.tsv')
if '--check' in sys.argv:
    sys.exit(0 if os.path.exists(p) and open(p).read() == t else 1)
open(p, 'w').write(t)
print('gloss.tsv: %d lines, letters agreed %d of %d (%.3f)' % (len(out) - 1, tot_ag, tot, tot_ag / max(1, tot)))
