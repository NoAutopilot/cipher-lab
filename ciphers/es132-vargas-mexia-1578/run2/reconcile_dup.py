#!/usr/bin/env python3
"""reconcile_dup.py PAGE -- writes ciphertext_<PAGE>.tsv for the duplicate copy (f.93r-f.95r) of the 19 Sept 1578 letter from the
two blind passes (normalised by test2.load_pass) and this worker's per-span decisions in run2/decisions_<PAGE>.tsv
(A3V3-ES9396, 4 Oct 2026). Base = pass A; each disagreement span (line, A start index) gets one decision:
'A' keep A, 'B' take B, 'A?'/'B?' take it but flag every token '?' (not settled by eye), or literal tokens ('' = drop).
Decisions were made from the crops / overlay by shape, without looking at the f.89 letter's tokens for the span.
Folder conventions applied (as run2/reconcile_f89r.py): the looped e-like tail = ρ; the '1'+crossed-'4' glyph = 12+
(the f.89 letter's reading of the same glyph, 34 times); a cross after a number = '+', not a digit 4.
Mechanical rule after the decisions (declared before alignment): a token <n>0ρ with n a Cp.30 base 2-37 and <n>0 not itself a base (> 37) -> <n>ρ (the e-loop read
as '0ρ' by the passes: 70ρ, 150ρ, 170ρ, 280ρ ...), counted in the printout."""
import sys, re, difflib
from pathlib import Path
HERE = Path(__file__).resolve().parents[1]; sys.path.insert(0, str(HERE))
from test2 import load_pass
pg = sys.argv[1]
D = {}
for l in open(HERE / f'run2/decisions_{pg}.tsv', encoding='utf-8'):
    if l.startswith('#') or not l.strip(): continue
    ln, i, dec = (l.rstrip('\n').split('\t') + [''])[:3]
    D[(ln, int(i))] = dec
A, B = load_pass(HERE / f'passes/{pg}_passA.tsv'), load_pass(HERE / f'passes/{pg}_passB.tsv')
q = lambda ts: [t if t.endswith('?') else t + '?' for t in ts]
out, used, NR = [], set(), [0]
for ln in sorted(set(A) | set(B)):
    a, b = A.get(ln, []), B.get(ln, [])
    sm = difflib.SequenceMatcher(None, [t.rstrip('?') for t in a], [t.rstrip('?') for t in b], autojunk=False)
    r = []
    for op, i1, i2, j1, j2 in sm.get_opcodes():
        if op == 'equal': r += a[i1:i2]; continue
        d = D[(ln, i1 + 1)]; used.add((ln, i1 + 1))
        r += {'A': a[i1:i2], 'B': b[j1:j2], 'A?': q(a[i1:i2]), 'B?': q(b[j1:j2])}.get(d, d.split())
    r2 = []
    for t in r:
        m = re.match(r'^(\d+)0ρ(.*)$', t)
        if m and 2 <= int(m.group(1)) <= 37 and int(m.group(1) + '0') > 37: t = m.group(1) + 'ρ' + m.group(2); NR[0] += 1
        r2.append(t)
    out.append(ln + '\t' + ' '.join(r2))
assert used == set(D), set(D) - used
hdr = [f'# BnF Espagnol 132 {pg[:3]}.{pg[3:]} -- duplicate cipher copy (f.93r-f.95r) of Philip II to Juan de Vargas Mexia, Madrid, 19 Sept 1578',
       '# (same letter as f.89r-f.91r; Gallica btv1b10032556x canvases 90-92; regions in NOTES.md "Duplicate copy f.93-95").',
       f'# Two blind Sonnet passes (passes/{pg}_passA/B.tsv, run2/pass_prompt_{pg}.md), normalised by test2.load_pass, reconciled by',
       f'# run2/reconcile_dup.py {pg} with run2/decisions_{pg}.tsv (A3V3-ES9396, 4 Oct 2026). ? = not settled by eye. Clear words dropped by load_pass.']
(HERE / f'ciphertext_{pg}.tsv').write_text('\n'.join(hdr + out) + '\n', encoding='utf-8')
print(pg, len(out), 'lines;', sum(len(l.split('\t')[1].split()) for l in out), 'tokens;',
      sum(t.endswith('?') for l in out for t in l.split('\t')[1].split()), 'flagged ?;', NR[0], 'x <n>0ρ -> <n>ρ')
