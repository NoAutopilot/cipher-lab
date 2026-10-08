#!/usr/bin/env python3
"""SUR-BLIND: score the two blind passes of NA 1.05.03 inv. 373 scan 0744 LEFT page (PREREG-SUR-BLIND.md, pushed 09cd01ce8 before
either pass was read or this script existed). Each pass (A/, B/: passA_sonnet_blind.tsv = that pass verbatim, gloss_reconciled.tsv =
that pass's own gloss rows) is run through ../inv373_alias_r15/alias_run.py's run() unchanged (and through it R14-SURDP dp_align.py),
T = 0693+0702+0730 sign tables + [sh-lig]={h}, C1 = 1,000 deranged-gloss draws, seed 744.
Run 1 (gated): reader `[ij]` (dotted y/ij) tagged as A3. Run 2 (descriptive): reader undotted `y` tagged instead.
Gate per pass: n_al >= 10 (PREREG; alias_run's own n_al >= 5 line is re-gated here), share >= 0.60, share > C1 p99, scan A unchanged,
SAME SYSTEM. Unit PASS iff both passes PASS. Writes score.out. `--check` exits 1 if score.out is stale."""
import os, re, sys
H = os.path.dirname(os.path.abspath(__file__)); P = os.path.join(H, '..')
src = open(os.path.join(P, 'inv373_alias_r15', 'alias_run.py'), encoding='utf-8').read().split('\nout = []; allp = []')[0]
ns = {'__file__': os.path.join(P, 'inv373_alias_r15', 'alias_run.py')}; exec(src, ns)
mode = {'tag': '[ij]'}
def f_tag(s):
    if mode['tag'] == '[ij]': return s.replace('[ij]', '‹ij›')
    return ns['outside'](s, lambda p: re.sub(r'(?<!\S)y(?!\S)', '‹ij›', p))
ns['ALIASES'].clear(); ns['ALIASES']['A3'] = (('0744',), f_tag, '[ij] (reader dotted)')
tabs = ['inv373_0693_r10', 'inv373_0702_r13', 'inv373_0730_r13']
out = []; verdict = {}
for p in ('A', 'B'):
    d = os.path.join('inv373_0744_blind_sb', p)
    rows = [l.rstrip('\n').split('\t') for l in open(os.path.join(P, d, 'passA_sonnet_blind.tsv'), encoding='utf-8') if l[0] != '#']
    nij = sum(r[2].count('[ij]') for r in rows if len(r) > 2 and r[1] == 'cipher')
    ny = sum(len(re.findall(r'(?<!\S)y(?!\S)', re.sub(r'\[[^\]]*\]', ' ', r[2]))) for r in rows if len(r) > 2 and r[1] == 'cipher')
    out.append(f'# pass {p}: reader [ij] {nij}, undotted y {ny}')
    mode['tag'] = '[ij]'; out.append(f'# pass {p} run 1 (gated): [ij] -> A3')
    n0 = len(out); passed = ns['run']('0744', d, tabs, 744, out)
    ls = [l for l in out[n0:] if ' A3 -> ' in l]
    m = re.search(r'n_al (\d+), agree (\d+), share ([\d.]+); C1 share mean ([\d.]+) p99 ([\d.]+)', ls[-1]) if ls else None
    nal, k, sh, p99 = (int(m[1]), int(m[2]), float(m[3]), float(m[5])) if m else (0, 0, 0.0, 1.0)
    g = 'non-test (n_al < 10)' if nal < 10 else ('PASS' if passed and sh >= 0.60 and sh > p99 else 'FAIL')
    verdict[p] = g; out.append(f'  pass {p} PREREG gate (n_al >= 10): {g}')
    mode['tag'] = 'y'; out.append(f'# pass {p} run 2 (descriptive, no gate): undotted y -> A3')
    ns['run']('0744', d, tabs, 744, out)
v = verdict['A'], verdict['B']
unit = 'PASS' if v == ('PASS', 'PASS') else 'FAIL' if v == ('FAIL', 'FAIL') else 'non-test' if all(x.startswith('non') for x in v) else 'not shown (passes disagree)'
out.append(f'UNIT VERDICT (0744 left, [ij] in m|n): {unit}  [A {v[0]}; B {v[1]}]')
txt = '\n'.join(out) + '\n'; f = os.path.join(H, 'score.out')
if '--check' in sys.argv:
    sys.exit(0 if os.path.exists(f) and open(f, encoding='utf-8').read() == txt else 1)
open(f, 'w', encoding='utf-8').write(txt); print(txt, end='')
