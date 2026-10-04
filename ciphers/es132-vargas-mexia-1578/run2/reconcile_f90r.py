#!/usr/bin/env python3
"""reconcile_f90r.py -- writes ciphertext_f90r.tsv (f.90r, the f.89 letter's second recto, 27 lines: L01-L21 and L22-L27) from the two
blind passes and this worker's per-span decisions (N4-ES132B, LANE-NEAR4, 4 Oct 2026). Base = pass A. No printed text exists for these
lines (PREREG_test2 amendment 2); the key was not consulted per span. Three kinds of decision:
(1) by eye from the crops (L01_s1, L10_s1, L12_s1 at 2400 px) and the overlay f90r_lines_debug.jpg: L01 '28'; L10 '11-hook' with hat,
    bar over 15+, '35rho 7.'; L12 bar over 6. and r-mark over 7., the word {Xum}, '115' (long-s digit = 5, as the '1fe' = 15rho rule);
(2) by the earlier pages' systematic rules: pass A's {y} = the letter y (notation only, 12 spans); the looped e-tail = rho where the
    passes split rho/sigma; '20-1', '11-1' = u-hook (U+22A3);
(3) everything else (mark present in one pass only, digit splits not checked by eye, single-pass insertions) kept but flagged '?'.
"""
import sys, difflib
from pathlib import Path
HERE = Path(__file__).resolve().parents[1]; sys.path.insert(0, str(HERE))
from test2 import load_pass
D = {('L01', 6): 'A', ('L02', 4): 'B', ('L02', 8): 'B?', ('L02', 11): 'A?', ('L02', 19): 'A?', ('L04', 2): 'A?', ('L04', 7): 'B', ('L04', 10): 'B', ('L05', 13): 'B', ('L06', 9): 'B', ('L07', 5): 'B', ('L08', 4): 'B?', ('L08', 8): 'A?', ('L08', 12): 'B', ('L09', 6): '20⊣', ('L10', 3): '11⊣@n?', ('L10', 7): '15+@s 60? y', ('L10', 15): 'B', ('L10', 17): '35ρ 7.', ('L11', 8): 'A?', ('L11', 11): 'B?', ('L11', 13): 'A', ('L11', 18): 'B?', ('L12', 6): 'A', ('L12', 9): '{Xum} y', ('L12', 12): '115?', ('L13', 5): 'B', ('L13', 7): 'B?', ('L13', 19): 'A?', ('L14', 15): 'B', ('L14', 19): 'B?', ('L15', 2): 'A?', ('L15', 13): 'B', ('L15', 16): '13@n? 20ρ@r', ('L17', 12): 'B', ('L17', 18): 'B?', ('L18', 1): 'A?', ('L18', 7): 'A', ('L18', 12): 'B', ('L19', 14): 'A?', ('L21', 2): 'B', ('L22', 11): '11⊣?', ('L22', 15): '91@s?', ('L23', 3): 'A?', ('L23', 11): 'B', ('L24', 2): 'A?', ('L24', 4): 'B', ('L25', 2): 'A?', ('L25', 5): 'B', ('L25', 7): 'A?', ('L25', 12): 'B', ('L25', 14): 'A?', ('L26', 1): 'B', ('L26', 6): '20⊣', ('L26', 9): 'A?', ('L26', 19): '25+? 4@l?', ('L27', 11): '17ρ@m? y', ('L27', 18): '15+@2 /'}
DEFAULT = 'B?'  # no span falls to the default on this page (every span decided below)
A, B = load_pass(HERE / 'passes/f90r_passA.tsv'), load_pass(HERE / 'passes/f90r_passB.tsv')
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
hdr = ['# BnF Espagnol 132 f.90r (Gallica btv1b10032556x canvas 87, right page, region 3580,900,2680,3900), 27 bands (L01-L21, L22-L27).', '# Philip II to Juan de Vargas Mexia, Madrid, 19 Sept 1578 (letter f.89r-91r), Cp.30.', '# Two blind Sonnet passes (passes/f90r_passA/B.tsv, shape notation run2/pass_prompt_f90r.md), normalised by test2.load_pass,', '# reconciled by run2/reconcile_f90r.py (N4-ES132B, 4 Oct 2026) from the crops and overlay. ? = not settled by eye.']
(HERE / 'ciphertext_f90r.tsv').write_text('\n'.join(hdr + out) + '\n', encoding='utf-8')
print(len(out), 'lines;', sum(t.endswith('?') for l in out for t in l.split('\t')[1].split()), 'tokens flagged ?')
