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
Output since RUN3-ES41 (4 Oct 2026): ciphertext_f41r_pre.tsv (this stream) + run2/f41r_units.tsv (one row per default unit: line, start
index in the line's stream, token count there, A tokens, B tokens); settle_f41r.py applies PREREG_f41r_settle.md to write ciphertext_f41r.tsv.
"""
import sys, re, difflib
from pathlib import Path
HERE = Path(__file__).resolve().parents[1]; sys.path.insert(0, str(HERE))
from test2 import load_pass
PAGE = sys.argv[sys.argv.index('--page') + 1] if '--page' in sys.argv else 'f41r'  # --page f41v (RUN3-ES41): same rules, same hand
A, B = load_pass(HERE / f'passes/{PAGE}_passA.tsv'), load_pass(HERE / f'passes/{PAGE}_passB.tsv')
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


out, tally, units, firm = [], {}, [], []
for ln in sorted(set(A) | set(B)):
    a, b = A.get(ln, []), B.get(ln, [])
    sm = difflib.SequenceMatcher(None, [t.rstrip('?') for t in a], [t.rstrip('?') for t in b], autojunk=False)
    r = []
    for op, i1, i2, j1, j2 in sm.get_opcodes():
        if op == 'equal':
            firm += [(ln, len(r) + k, t) for k, t in enumerate(a[i1:i2]) if not t.endswith('?')]
            r += a[i1:i2]; continue
        if op == 'replace' and i2 - i1 == j2 - j1:
            for x, y in zip(a[i1:i2], b[j1:j2]):
                t, rule = settle(x, y); tally[rule] = tally.get(rule, 0) + 1
                if rule == 'default': units.append((ln, len(r), 1, x.rstrip('?'), y.rstrip('?')))
                r.append(t)
        else:
            units.append((ln, len(r), i2 - i1, ' '.join(t.rstrip('?') for t in a[i1:i2]) or '-',
                          ' '.join(t.rstrip('?') for t in b[j1:j2]) or '-'))
            r += q(a[i1:i2]); tally['default'] = tally.get('default', 0) + max(i2 - i1, j2 - j1)
    out.append(ln + '\t' + ' '.join(r))
HDR1 = {'f41r': '# BnF Espagnol 132 f.41r (Gallica btv1b10032556x canvas 38, right page, region 3500,1300,3150,3800), 30 bands = 30 lines.',
        'f41v': '# BnF Espagnol 132 f.41v (Gallica btv1b10032556x canvas 39, left page, region 650,850,2700,4300, --centres), 31 bands = 31 lines.',
        'f50v': '# BnF Espagnol 132 f.50v (Gallica btv1b10032556x canvas 48, left page, region 800,850,2750,3450), 27 bands = 27 lines.',  # RUN4-ES41V
        'f51r': '# BnF Espagnol 132 f.51r (Gallica btv1b10032556x canvas 48, right page, region 3450,650,3050,3700, 3 segments), 26 bands = 26 lines.',
        'f50r': '# BnF Espagnol 132 f.50r (Gallica btv1b10032556x canvas 47, right page, region 3600,1340,2850,3060, 3 segments), 24 bands = 24 lines (L01 clear, L02 clear then cipher). Pass B = RUN5-ES50B replacement (prompt run2/pass_prompt_f50r_B2.md, dot sign called out; RUN4 pass B kept as passes/f50r_passB_run4.tsv).'}  # RUN4-ES50 / RUN4-ES50R
HDR1['f51v'] = '# BnF Espagnol 132 f.51v (Gallica btv1b10032556x canvas 49, left page, region 1050,780,2450,3560, re-cut --max-width 1300: 2 segments, 150 px overlap), 25 bands = 25 lines.'  # RUN5-ES50B; re-cut RUN5-ES51
HDR1['f52r'] = '# BnF Espagnol 132 f.52r (Gallica btv1b10032556x canvas 49, right page, region 3950,640,2450,3220, --max-width 1275: 2 segments, 100 px overlap), 22 bands = 22 lines (L22 clear dating line).'  # RUN5-ES51
LETTER = {'f50v': '# Philip II to Juan de Vargas Mexia, Bosque de Segovia, 7 or 14 June 1578 (Tomokiyo TOC no.25-29 group, f.50 = no.25), Cp.30 (Vargas Mexia Cipher 3). Not read by cabinet-noir.'}
LETTER['f51r'] = LETTER['f50v'].replace('f.50 = no.25)', 'f.50 = no.25; f.51r follows f.50v)')  # RUN4-ES50
LETTER['f51v'] = LETTER['f50v'].replace('f.50 = no.25)', 'f.50 = no.25; f.51v follows f.51r)')  # RUN5-ES50B
LETTER['f52r'] = LETTER['f50v'].replace('f.50 = no.25)', 'f.50 = no.25; f.52r follows f.51v and ends the letter)')  # RUN5-ES51
LETTER['f50r'] = LETTER['f50v'].replace('f.50 = no.25)', 'f.50 = no.25; f.50r opens the letter)')  # RUN4-ES50R
hdr = [HDR1[PAGE],
       LETTER.get(PAGE, '# Philip II to Juan de Vargas Mexia, Madrid, 29 April 1578 (Tomokiyo TOC no.21), Cp.30 (Vargas Mexia Cipher 3). Not read by cabinet-noir.'),
       f'# Two blind Sonnet passes (passes/{PAGE}_passA/B.tsv, notation run2/pass_prompt_{PAGE}.md), normalised by test2.load_pass,',
       '# reconciled by run2/reconcile_f41r.py (ES132-C3, 4 Oct 2026) by shape rules R1-R7. ? = not settled by eye. rules: ' +
       ' '.join(f'{k}={v}' for k, v in sorted(tally.items()))]
(HERE / f'run2/{PAGE}_units.tsv').write_text('line\tstart\tlen\tA\tB\n' + ''.join('\t'.join(map(str, u)) + '\n' for u in units),
                                         encoding='utf-8')
(HERE / f'run2/{PAGE}_firm.tsv').write_text('line\tidx\ttoken\n' + ''.join('\t'.join(map(str, f)) + '\n' for f in firm), encoding='utf-8')
(HERE / (f'ciphertext_{PAGE}_pre.tsv' if PAGE == 'f41r' else f'ciphertext_{PAGE}.tsv')).write_text('\n'.join(hdr + out) + '\n', encoding='utf-8')
print(len(out), 'lines;', sum(len(l.split('\t')[1].split()) for l in out), 'tokens;',
      sum(t.endswith('?') for l in out for t in l.split('\t')[1].split()), 'flagged ?;', tally)
