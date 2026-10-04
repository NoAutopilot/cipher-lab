#!/usr/bin/env python3
"""reconcile_f119vU.py -- writes ciphertext_f119vU.tsv (f.119v upper paragraph, 12 lines) from the two blind passes (normalised by
test2.load_pass) and this worker's per-span decisions (N4-ES132, LANE-NEAR4, 4 Oct 2026). Base = pass A. Decisions from the crops
(L01, L02, L07, L08, L09 at 2400 px) and the overlay f119vU_lines_debug.jpg, by shape; no printed text exists for these lines and
the key was not consulted per span. Systematic (same as reconcile_f89r/f89v.py): the looped e-like tail = rho (here pass B wrote
sigma); a number followed by a horizontal stroke ending in a down-tick ('2o-1', '7-1', '23-1') = u-hook (U+22A3), distinct from
the crossed '+'. Codes: 'A' keep A, 'B' take B, 'A?'/'B?' take it but flag '?', or literal tokens.
"""
import sys, difflib
from pathlib import Path
HERE = Path(__file__).resolve().parents[1]; sys.path.insert(0, str(HERE))
from test2 import load_pass
D = {('L01', 4): 'A', ('L01', 7): 'A', ('L01', 13): '7ρ 16⊣?', ('L01', 16): 'A', ('L01', 18): 'y? ?', ('L02', 1): 'A?', ('L02', 12): 'A', ('L02', 18): '15ρ y ?', ('L03', 7): 'B', ('L03', 15): 'A', ('L04', 3): 'A', ('L04', 7): 'B', ('L05', 8): 'A', ('L05', 11): 'A?', ('L05', 15): 'A', ('L06', 4): 'A', ('L07', 4): '35ρ 7⊣', ('L07', 11): 'B', ('L08', 3): 'B', ('L08', 11): '20⊣', ('L08', 13): 'B', ('L08', 15): 'A', ('L08', 17): '11⊣@n?', ('L09', 4): '7⊣', ('L09', 11): '10 23⊣', ('L10', 4): 'A', ('L10', 7): 'A', ('L10', 18): 'A', ('L11', 7): '11⊣?', ('L11', 14): 'A', ('L12', 3): 'A', ('L12', 6): 'A', ('L12', 9): 'A?'}
DEFAULT = 'B?'  # no span falls to the default on this page (every span decided below)
A, B = load_pass(HERE / 'passes/f119vU_passA.tsv'), load_pass(HERE / 'passes/f119vU_passB.tsv')
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
hdr = ['# BnF Espagnol 132 f.119v upper paragraph (Gallica btv1b10032556x canvas 117, left page, region 900,1020,2500,1780), 12 bands.', '# Philip II to Juan de Vargas Mexia, Madrid, 15 Oct 1578 (letter f.119r-120r), Cp.30. Not printed by Teulet (his paragraph is f.119v lower). Right edge at the binding.', '# Two blind Sonnet passes (passes/f119vU_passA/B.tsv, shape notation run2/pass_prompt_f119vU.md), normalised by test2.load_pass,', '# reconciled by run2/reconcile_f119vU.py (N4-ES132, 4 Oct 2026) from the crops and overlay. ? = not settled by eye.']
(HERE / 'ciphertext_f119vU.tsv').write_text('\n'.join(hdr + out) + '\n', encoding='utf-8')
print(len(out), 'lines;', sum(t.endswith('?') for l in out for t in l.split('\t')[1].split()), 'tokens flagged ?')
