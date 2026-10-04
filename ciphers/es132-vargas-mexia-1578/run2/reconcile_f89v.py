#!/usr/bin/env python3
"""reconcile_f89v.py -- writes ciphertext_f89v.tsv from the two blind passes (normalised by test2.load_pass) and this
worker's per-span decisions (RUN2-ES132, 4 Oct 2026). Base = pass A; each disagreement span gets one decision below.
Decisions were made from the crops/overlay by shape (no printed text exists for f.89r; key was not consulted per span).
Codes: 'A' keep A, 'B' take B, 'A?'/'B?' take it but flag every token '?' (not settled by eye), or literal tokens.
Same systematic rules as reconcile_f89r.py (from f.89r crops L04, L09, L10s2, L11, L20 viewed at 2400 px): the looped e-like tail = ρ (B's convention,
test 1's passnorm), so A's 'σ' there -> ρ; the '2ι3' group = 2⊣ 3 (u-hook on 2, then 3); '1ı' without a top bar = 11.
"""
import sys, difflib
from pathlib import Path
HERE = Path(__file__).resolve().parents[1]; sys.path.insert(0, str(HERE))
from test2 import load_pass
D = {
 ('L02', 1): 'B', ('L02', 16): 'A?', ('L03', 1): '7⊣', ('L03', 15): 'B', ('L07', 15): 'A?', ('L07', 18): '',
 ('L08', 9): 'A', ('L08', 12): 'A?', ('L10', 9): 'A?', ('L11', 5): 'A?',
 ('L17', 11): 'B', ('L18', 2): 'B', ('L19', 10): 'B', ('L21', 13): 'B', ('L20', 12): 'B', ('L22', 13): 'A?',
 ('L23', 12): 'A', ('L24', 3): 'B', ('L24', 5): 'A?', ('L25', 3): 'A?', ('L25', 9): 'A?', ('L07', 12): 'A?',
 ('L04', 17): 'A?', ('L05', 15): 'A?', ('L15', 1): 'A?', ('L15', 12): 'A',
}
DEFAULT = 'B?'  # every other span: B, flagged (mostly a bar/dot mark seen by B only)
A, B = load_pass(HERE / 'passes/f89v_passA.tsv'), load_pass(HERE / 'passes/f89v_passB.tsv')
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
hdr = ['# BnF Espagnol 132 f.89v (Gallica btv1b10032556x canvas 87, left page, region 520,880,2720,3980), 26 bands (3 paragraphs).',
       '# Philip II to Juan de Vargas Mexia, Madrid, 19 Sept 1578 (letter f.89r-91r), Cp.30. Not printed by Teulet. Right edge at the gutter.',
       '# Two blind Sonnet passes (passes/f89v_passA/B.tsv, shape notation run2/pass_prompt_f89v.md), normalised by test2.load_pass,',
       '# reconciled by run2/reconcile_f89v.py (RUN2-ES132, 4 Oct 2026) from the overlay f89v_lines_debug.jpg. ? = not settled by eye.']
(HERE / 'ciphertext_f89v.tsv').write_text('\n'.join(hdr + out) + '\n', encoding='utf-8')
print(len(out), 'lines;', sum(t.endswith('?') for l in out for t in l.split('\t')[1].split()), 'tokens flagged ?')
