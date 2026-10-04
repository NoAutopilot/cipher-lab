#!/usr/bin/env python3
"""reconcile_f91r.py -- writes ciphertext_f91r.tsv (f.91r, the f.89 letter's last page, 7 cipher lines in 2 paragraphs above the clear
dating line) from the two blind passes and this worker's per-span decisions (N4-ES132B, LANE-NEAR4, 4 Oct 2026). Base = pass A.
Decisions from the crops (L01_s2, L04_s1 at 2400 px) and the overlay f91r_lines_debug.jpg, by shape; no printed text exists for these
lines (PREREG_test2 amendment 2) and the key was not consulted per span. Systematic: the '1' + long-s-shaped digit + looped tail
('1fe') = 15rho, as every earlier reconciled page of this letter (f.89r/v, f.90v: 15rho 42x, 12rho 0x); '2fe' = 25rho; '6f' = 6sigma
(prior pages 6sigma 30x vs 65 6x). A digit group ending in a short down-stroke ('12i', '11+i') left flagged '?'.
"""
import sys, difflib
from pathlib import Path
HERE = Path(__file__).resolve().parents[1]; sys.path.insert(0, str(HERE))
from test2 import load_pass
D = {('L01', 9): 'B', ('L01', 12): '12⊣?', ('L02', 14): 'B', ('L02', 16): 'B', ('L03', 1): 'B', ('L04', 1): 'B', ('L04', 11): 'B', ('L05', 1): 'B', ('L05', 5): 'B', ('L06', 11): 'B', ('L07', 9): 'B', ('L07', 12): 'A?'}
DEFAULT = 'B?'  # no span falls to the default on this page (every span decided below)
A, B = load_pass(HERE / 'passes/f91r_passA.tsv'), load_pass(HERE / 'passes/f91r_passB.tsv')
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
hdr = ['# BnF Espagnol 132 f.91r (Gallica btv1b10032556x canvas 88, right page, region 3650,860,2650,1020), 7 bands (2 paragraphs).', '# Philip II to Juan de Vargas Mexia, Madrid, 19 Sept 1578 (letter f.89r-91r, dated "De Madrid a xix de Sept.e MDLXXVIII" below), Cp.30.', '# Two blind Sonnet passes (passes/f91r_passA/B.tsv, shape notation run2/pass_prompt_f91r.md), normalised by test2.load_pass,', '# reconciled by run2/reconcile_f91r.py (N4-ES132B, 4 Oct 2026) from the crops and overlay. ? = not settled by eye.']
(HERE / 'ciphertext_f91r.tsv').write_text('\n'.join(hdr + out) + '\n', encoding='utf-8')
print(len(out), 'lines;', sum(t.endswith('?') for l in out for t in l.split('\t')[1].split()), 'tokens flagged ?')
