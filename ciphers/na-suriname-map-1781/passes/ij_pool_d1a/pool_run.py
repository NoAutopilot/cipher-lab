#!/usr/bin/env python3
"""D1A-SUR: pooled [ij] class test over inv. 373 0746 (NZ-SURIJ IJ labels) + 0758 (R15-SUR758 ONE labels), PREREG-D1A-SUR.md
(pushed 3fe2b69c0 before this script). Each scan is set up exactly by its own retok_run.py (labels -> tokens wrapper), then scored by
R15-SURALIAS alias_run.run() unchanged except that its per-draw C1 class counts are kept so the two scans' draws can be pooled.
Control first: the pooled C1 null is printed before the pooled real share; stop if its p99 is still 1.000. Writes pool.out."""
import os, re
H = os.path.dirname(os.path.abspath(__file__)); P = os.path.join(H, '..')
RUNSRC = open(os.path.join(P, 'inv373_alias_r15', 'alias_run.py'), encoding='utf-8').read()
RUNDEF = RUNSRC[RUNSRC.index('def run('):RUNSRC.index('\ndef dp_idx(')]
assert 'b, a = res[False], res[True]; passed = []' in RUNDEF
RUNDEF = RUNDEF.replace('b, a = res[False], res[True]; passed = []', 'b, a = res[False], res[True]; passed = []; _KEEP.append(res)')
def setup(d, stop):
    """exec the scan's own retok_run.py up to its run call; return its alias_run namespace with run() patched to keep res."""
    f = os.path.join(P, d, 'retok_run.py'); src = open(f, encoding='utf-8').read(); src = src[:src.index(stop)]
    g = {'__file__': f, '__name__': 'setup'}; exec(src, g); ns = g['ns']
    ns['_KEEP'] = []; exec(RUNDEF, ns); return ns
out = []; per = {}
for scan, d, stop, seed, aid in (('0746', 'inv373_0746_tok_nz', "tabs = ['inv373", 746, 'A3'),
                                 ('0758', 'inv373_0758_tok_r15', "out = []; passed = ns['run']", 758, 'A3')):
    ns = setup(d, stop)
    ns['run'](scan, d.replace('_tok_nz', '_r14').replace('_tok_r15', '_r14'), ['inv373_0693_r10', 'inv373_0702_r13', 'inv373_0730_r13'],
              seed, out)
    res = ns['_KEEP'][-1]; b, a = res[False], res[True]
    per[scan] = dict(real=a['share'].get(aid, (0, 0)), draws=[dr.get(aid, (0, 0)) for dr in a['c1a']],
                     scan_ok=a['A'] >= b['A'] - 0.010 and a['verdict'].startswith('SAME'))
# control first
draws = [(per['0746']['draws'][i][0] + per['0758']['draws'][i][0], per['0746']['draws'][i][1] + per['0758']['draws'][i][1]) for i in range(1000)]
dist = sorted((k / n) if n else 0.0 for n, k in draws); nd = sorted(n for n, _ in draws)
out.append(f"# POOLED C1 (control first): draws 1000; n_al per draw median {nd[500]} min {nd[0]} max {nd[-1]}; class share mean "
           f"{sum(dist)/1000:.3f} p95 {dist[949]:.3f} p99 {dist[989]:.3f} max {dist[-1]:.3f}")
if dist[989] >= 1.0:
    out.append('# STOP: pooled C1 p99 still 1.000 -> untestable at this n (PREREG stop rule); real share not used')
else:
    n = per['0746']['real'][0] + per['0758']['real'][0]; k = per['0746']['real'][1] + per['0758']['real'][1]; sh = k / n if n else 0
    ok = per['0746']['scan_ok'] and per['0758']['scan_ok']
    g = 'non-test (pooled n_al < 10)' if n < 10 else 'PASS' if sh >= 0.60 and sh > dist[989] and ok else 'FAIL'
    out.append(f"# POOLED real: 0746 {per['0746']['real']} + 0758 {per['0758']['real']} (n_al, agree) -> n_al {n}, agree {k}, share "
               f"{sh:.3f} vs C1 p99 {dist[989]:.3f}; scan checks {per['0746']['scan_ok']}/{per['0758']['scan_ok']} -> {g}")
    out.append(f"# exact tail: share of C1 draws with share >= real: {sum(1 for x in dist if x >= sh)}/1000")
open(os.path.join(H, 'pool.out'), 'w').write('\n'.join(out) + '\n'); print('\n'.join(out))
