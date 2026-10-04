#!/usr/bin/env python3
"""reconcile_f120r.py -- writes ciphertext_f120r.tsv (f.120r, two cipher paragraphs, 8 lines, before the clear dating line) from the
two blind passes and this worker's per-span decisions (N4-ES132, LANE-NEAR4, 4 Oct 2026). Base = pass A. Decisions from the crops
(L01, L02, L05, L08 at 2400 px) and the overlay f120r_lines_debug.jpg, by shape, before reading any Teulet text (PREREG_test2
amendment 1 overlap clause). After the first decode showed L01-L04 continue Teulet's printed 15 Oct 1578 paragraph,
the L01-L04 spans were re-set to pass A flagged '?' (A?), per that clause: printed lines are reconciled by A/B agreement only
(the eye decisions first made there were A, A, A, B, B). Same systematic rules as reconcile_f119vU.py ('20-1', '33-1', '17-1' = u-hook, not '+').
"""
import sys, difflib
from pathlib import Path
HERE = Path(__file__).resolve().parents[1]; sys.path.insert(0, str(HERE))
from test2 import load_pass
D = {('L01', 6): 'A?', ('L02', 9): 'A?', ('L02', 15): 'A?', ('L03', 1): 'A?', ('L04', 5): 'A?', ('L05', 3): 'B', ('L05', 14): 'B', ('L07', 9): 'B', ('L07', 18): 'B', ('L08', 6): 'B?', ('L08', 11): 'B', ('L08', 14): '15+@2@s 7+@s?', ('L08', 18): '15+@2@s? /'}
DEFAULT = 'B?'  # no span falls to the default on this page (every span decided below)
A, B = load_pass(HERE / 'passes/f120r_passA.tsv'), load_pass(HERE / 'passes/f120r_passB.tsv')
q = lambda ts: [t if t.endswith('?') else t + '?' for t in ts]
out, used = [], set()
for ln in sorted(set(A) | set(B)):
    a, b = A.get(ln, []), B.get(ln, [])
    sm = difflib.SequenceMatcher(None, [t.rstrip('?') for t in a], [t.rstrip('?') for t in b], autojunk=False)
    r = []
    for op, i1, i2, j1, j2 in sm.get_opcodes():
        if op == 'equal': r += a[i1:i2]; continue
        d = D.get((ln, i1 + 1), DEFAULT); used.add((ln, i1 + 1))
        r += {'A': a[i1:i2], 'B': b[j1:j2], 'A?': q(a[i1:i2]), 'B?': q(b[j1:j2])}.get(d, d.split())
    out.append(ln + '\t' + ' '.join(r))
assert set(D) <= used, set(D) - used
hdr = ['# BnF Espagnol 132 f.120r (Gallica btv1b10032556x canvas 117, right page, region 3600,1000,2600,1390), 8 bands (2 paragraphs).', '# Philip II to Juan de Vargas Mexia, Madrid, 15 Oct 1578 (letter f.119r-120r, dated "De Madrid a xv de Octubre" below), Cp.30.', '# Two blind Sonnet passes (passes/f120r_passA/B.tsv, shape notation run2/pass_prompt_f120r.md), normalised by test2.load_pass,', '# reconciled by run2/reconcile_f120r.py (N4-ES132, 4 Oct 2026) from the crops and overlay. ? = not settled by eye.']
(HERE / 'ciphertext_f120r.tsv').write_text('\n'.join(hdr + out) + '\n', encoding='utf-8')
print(len(out), 'lines;', sum(t.endswith('?') for l in out for t in l.split('\t')[1].split()), 'tokens flagged ?')
