#!/usr/bin/env python3
"""reconcile_f41r.py -- writes ciphertext_f41r.tsv from the two blind passes (normalised by test2.load_pass) and this worker's
shape rules (ES132-C3, 4 Oct 2026). No printed text exists for f.41r; the key was not consulted per span.
Rules, settled from crops f41r_L02 and L07 (s1+s2 at 2400 px) and the f.89-f.91 reconciled convention of this hand:
 R1 A '21.' vs B '11.' -> 21. (the u-shaped group; f.89r-f.91r reconciled pages hold 21. x83 and 11. x0 for this shape)
 R2 A '77..'/'177..' vs B '7ρ..'/'17ρ..' -> B (the looped e-tail is ρ: run2 rule; A read it as a second 7)
 R3 A '6σ..' vs B '6ρ..'/'64ρ..' -> 6ρ + B's marks (looped tail = ρ; B's '4' is the loop)
 R4 A '12+'/'12ρ' vs B '124+'/'124'/'11+' where A has '12+' -> 12+ ('v24' ligature = 12+; B read the + as 4+)
 R5 A '16' vs B '161' -> 16⊣? (u-hook after the base, as 2⊣ on f.89r; flagged: hook vs digit not certain)
 R6 A '15+' vs B '158+' -> 15+ (B read the cross as 8+)
 R7 the same token with a mark or dot seen by one reader only -> the marked/dotted reading, flagged '?'
 Default: pass A's token(s), flagged '?' (not settled by eye; inserted/deleted tokens likewise flagged).
"""
import sys, re, difflib
from pathlib import Path
HERE = Path(__file__).resolve().parents[1]; sys.path.insert(0, str(HERE))
from test2 import load_pass
A, B = load_pass(HERE / 'passes/f41r_passA.tsv'), load_pass(HERE / 'passes/f41r_passB.tsv')
q = lambda ts: [t if t.endswith('?') else t + '?' for t in ts]
base = lambda t: re.sub(r'[@?].*$', '', t.rstrip('?'))
marks = lambda t: ''.join(re.findall(r'@\w', t))


def settle(a, b):
    a0, b0 = a.rstrip('?'), b.rstrip('?')
    if a0 == '21.' and b0 == '11.': return '21.', 'R1'
    if re.match(r'^1?77', a0) and re.match(r'^1?7ρ', b0): return b, 'R2'
    if a0.startswith('6σ') and re.match(r'^64?ρ', b0): return '6ρ' + marks(b0), 'R3'
    if a0 == '12+' and b0 in ('124+', '124', '11+'): return '12+', 'R4'
    if a0 == '16' and b0 == '161': return '16⊣?', 'R5'
    if a0 == '15+' and b0 == '158+': return '15+', 'R6'
    sa, sb = re.sub(r'(@\w|\.)', '', a0), re.sub(r'(@\w|\.)', '', b0)
    if sa == sb: return (a0 if len(a0) > len(b0) else b0) + '?', 'R7'
    return a0 + '?', 'default'


out, tally = [], {}
for ln in sorted(set(A) | set(B)):
    a, b = A.get(ln, []), B.get(ln, [])
    sm = difflib.SequenceMatcher(None, [t.rstrip('?') for t in a], [t.rstrip('?') for t in b], autojunk=False)
    r = []
    for op, i1, i2, j1, j2 in sm.get_opcodes():
        if op == 'equal': r += a[i1:i2]; continue
        if op == 'replace' and i2 - i1 == j2 - j1:
            for x, y in zip(a[i1:i2], b[j1:j2]):
                t, rule = settle(x, y); r.append(t); tally[rule] = tally.get(rule, 0) + 1
        else:
            r += q(a[i1:i2]); tally['default'] = tally.get('default', 0) + max(i2 - i1, j2 - j1)
    out.append(ln + '\t' + ' '.join(r))
hdr = ['# BnF Espagnol 132 f.41r (Gallica btv1b10032556x canvas 38, right page, region 3500,1300,3150,3800), 30 bands = 30 lines.',
       '# Philip II to Juan de Vargas Mexia, Madrid, 29 April 1578 (Tomokiyo TOC no.21), Cp.30 (Vargas Mexia Cipher 3). Not read by cabinet-noir.',
       '# Two blind Sonnet passes (passes/f41r_passA/B.tsv, notation run2/pass_prompt_f41r.md), normalised by test2.load_pass,',
       '# reconciled by run2/reconcile_f41r.py (ES132-C3, 4 Oct 2026) by shape rules R1-R7. ? = not settled by eye. rules: ' +
       ' '.join(f'{k}={v}' for k, v in sorted(tally.items()))]
(HERE / 'ciphertext_f41r.tsv').write_text('\n'.join(hdr + out) + '\n', encoding='utf-8')
print(len(out), 'lines;', sum(len(l.split('\t')[1].split()) for l in out), 'tokens;',
      sum(t.endswith('?') for l in out for t in l.split('\t')[1].split()), 'flagged ?;', tally)
