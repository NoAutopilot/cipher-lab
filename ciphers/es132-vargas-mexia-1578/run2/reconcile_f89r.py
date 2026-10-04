#!/usr/bin/env python3
"""reconcile_f89r.py -- writes ciphertext_f89r.tsv from the two blind passes (normalised by test2.load_pass) and this
worker's per-span decisions (RUN2-ES132, 4 Oct 2026). Base = pass A; each disagreement span gets one decision below.
Decisions were made from the crops/overlay by shape (no printed text exists for f.89r; key was not consulted per span).
Codes: 'A' keep A, 'B' take B, 'A?'/'B?' take it but flag every token '?' (not settled by eye), or literal tokens.
Systematic rules (from crops L04, L09, L10s2, L11, L20 viewed at 2400 px): the looped e-like tail = ρ (B's convention,
test 1's passnorm), so A's 'σ' there -> ρ; the '2ι3' group = 2⊣ 3 (u-hook on 2, then 3); '1ı' without a top bar = 11.
"""
import sys, difflib
from pathlib import Path
HERE = Path(__file__).resolve().parents[1]; sys.path.insert(0, str(HERE))
from test2 import load_pass
D = {
 ('L01', 3): 'A', ('L01', 17): 'A?',
 ('L02', 5): 'A?', ('L02', 9): 'A?', ('L02', 11): '2⊣', ('L02', 19): 'A?', ('L02', 22): 'A?',
 ('L03', 1): 'A?', ('L03', 23): 'A?',
 ('L04', 7): '7⊣ 8', ('L04', 10): 'B', ('L04', 15): '24ρ', ('L04', 16): '24ρ 7+@n', ('L04', 21): 'B',
 ('L05', 8): 'A?', ('L05', 19): 'A?',
 ('L06', 2): 'B?', ('L06', 4): 'B?', ('L06', 6): 'B', ('L06', 8): 'B', ('L06', 15): 'A?',
 ('L07', 1): '2⊣ 3', ('L07', 6): '17σ 10', ('L07', 9): 'B', ('L07', 13): 'A?', ('L07', 16): 'A',
 ('L08', 3): 'A?', ('L08', 5): 'A?', ('L08', 7): 'B?', ('L08', 14): 'A?', ('L08', 18): 'A?',
 ('L09', 4): '8⊣', ('L09', 8): '13?', ('L09', 10): '23σ@2 88', ('L09', 15): 'B', ('L09', 18): 'A?',
 ('L10', 3): 'B', ('L10', 16): 'A',
 ('L11', 7): '11+@r', ('L11', 10): '11ρ@r 15ρ', ('L11', 16): '11ρ',
 ('L12', 1): 'A?', ('L12', 4): 'B', ('L12', 15): 'B?', ('L12', 18): '',
 ('L13', 20): '',
 ('L14', 4): 'A?', ('L15', 3): 'A?', ('L15', 9): 'B?', ('L15', 14): 'A?', ('L15', 17): '2⊣',
 ('L16', 3): 'A?', ('L17', 3): 'A?', ('L18', 4): 'A?', ('L18', 7): '25ρ@s 24ρ',
 ('L19', 16): 'B', ('L19', 19): 'A?',
 ('L20', 4): 'B', ('L20', 8): '2⊣ 3', ('L20', 12): 'B', ('L20', 16): 'A?',
 ('L21', 3): 'A?', ('L21', 10): 'A?', ('L21', 19): 'B?',
 ('L22', 3): 'B', ('L22', 9): 'A?', ('L22', 15): '2⊣ 3', ('L22', 18): 'A?',
 ('L23', 4): '11ρ 25+@r',
}
A, B = load_pass(HERE / 'passes/f89r_passA.tsv'), load_pass(HERE / 'passes/f89r_passB.tsv')
q = lambda ts: [t if t.endswith('?') else t + '?' for t in ts]
out, used = [], set()
for ln in sorted(set(A) | set(B)):
    a, b = A.get(ln, []), B.get(ln, [])
    sm = difflib.SequenceMatcher(None, [t.rstrip('?') for t in a], [t.rstrip('?') for t in b], autojunk=False)
    r = []
    for op, i1, i2, j1, j2 in sm.get_opcodes():
        if op == 'equal': r += a[i1:i2]; continue
        d = D[(ln, i1 + 1)]; used.add((ln, i1 + 1))
        r += {'A': a[i1:i2], 'B': b[j1:j2], 'A?': q(a[i1:i2]), 'B?': q(b[j1:j2])}.get(d, d.split())
    out.append(ln + '\t' + ' '.join(r))
assert used == set(D), set(D) - used
hdr = ['# BnF Espagnol 132 f.89r (Gallica btv1b10032556x canvas 86, right page, region 3450,1580,2950,3200), 23 lines.',
       '# Philip II to Juan de Vargas Mexia, Madrid, 19 Sept 1578 (letter f.89r-91r), Cp.30. Not printed by Teulet.',
       '# Two blind Sonnet passes (passes/f89r_passA/B.tsv, shape notation run2/pass_prompt_f89r.md), normalised by test2.load_pass,',
       '# reconciled by run2/reconcile_f89r.py (RUN2-ES132, 4 Oct 2026). ? = not settled by eye. L01 = clear opening (dropped) + cipher tail.']
(HERE / 'ciphertext_f89r.tsv').write_text('\n'.join(hdr + out) + '\n', encoding='utf-8')
print(len(out), 'lines;', sum(t.endswith('?') for l in out for t in l.split('\t')[1].split()), 'tokens flagged ?')
