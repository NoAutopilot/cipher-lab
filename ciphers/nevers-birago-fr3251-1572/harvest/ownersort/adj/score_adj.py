#!/usr/bin/env python3
"""BIR-ADJ scoring (PREREG_adj.md). Run from the repo root:
  python3 ciphers/nevers-birago-fr3251-1572/harvest/ownersort/adj/score_adj.py
Reads answers/<batch>_p1.tsv, _p2.tsv (blind Sonnet passes) and answers/reconcile.tsv (blind Opus, splits only) and key.tsv;
writes control.tsv, verdicts.tsv, owner_right.tsv, summary.json beside this file."""
import csv, json, os
from collections import Counter, defaultdict
H = os.path.dirname(os.path.abspath(__file__)); A = H + '/answers'
def tsv(p): return list(csv.DictReader(open(p), delimiter='\t')) if os.path.exists(p) else []
key = {r['item']: r for r in tsv(H + '/key.tsv')}
def ans(p):
    d = {}
    for f in sorted(os.listdir(A)):
        if f.endswith(f'_{p}.tsv'):
            for r in tsv(f'{A}/{f}'): d[r['item'].strip()] = r
    return d
P1, P2, RC = ans('p1'), ans('p2'), {r['item'].strip(): r for r in tsv(A + '/reconcile.tsv')}
def side(it, a):
    """map a strip answer to machine / owner / both / neither"""
    a = a.strip().lower()
    if a in ('both', 'neither'): return a
    if a not in ('1', '2'): return 'missing'
    return key[it]['strip1_is'] if a == '1' else ('owner' if key[it]['strip1_is'] == 'machine' else 'machine')
out = {}
# control: 'machine' column holds the true pile, 'owner' column the look-alike
ctl = [it for it in key if key[it]['kind'] == 'control']
cr = []; hits = Counter()
for it in ctl:
    s1, s2 = side(it, P1.get(it, {}).get('answer', '')), side(it, P2.get(it, {}).get('answer', ''))
    hits['p1'] += s1 == 'machine'; hits['p2'] += s2 == 'machine'; hits['both_passes'] += s1 == s2 == 'machine'
    cr.append(dict(item=it, sid=key[it]['sid'], true=key[it]['mach_pile'], lookalike=key[it]['owner_pile'], p1=s1, p2=s2))
with open(H + '/control.tsv', 'w') as f:
    f.write('item\tsid\ttrue_pile\tlookalike_pile\tp1\tp2\n')
    for r in cr: f.write('\t'.join(str(r[k]) for k in ('item', 'sid', 'true', 'lookalike', 'p1', 'p2')) + '\n')
gate = hits['p1'] >= 24 and hits['p2'] >= 24
out['control'] = dict(n=len(ctl), p1_true=hits['p1'], p2_true=hits['p2'], both_true=hits['both_passes'], gate_24=gate,
                      p1_counts=dict(Counter(r['p1'] for r in cr)), p2_counts=dict(Counter(r['p2'] for r in cr)))
NAME = dict(machine='machines right', owner='owner right', both='both plausible', neither='neither')
tg = [it for it in key if key[it]['kind'] == 'target']
vr = []
for it in tg:
    k = key[it]
    if not k['m_tiles'] or not k['o_tiles']:
        vr.append(dict(item=it, sid=k['sid'], leaf=k['leaf'], mach=k['mach_pile'], owner=k['owner_pile'], p1='', p2='', rc='', verdict='untestable (empty strip)', grade='')); continue
    a, b = P1.get(it, {}), P2.get(it, {})
    s1, s2 = side(it, a.get('answer', '')), side(it, b.get('answer', ''))
    if s1 == s2 and s1 != 'missing':
        v = s1; g = 'agreed' if 'high' in (a.get('conf', ''), b.get('conf', '')) else 'agreed-low'; rc = ''
    else:
        rc = side(it, RC.get(it, {}).get('answer', '')) if it in RC else 'missing'; v = rc; g = 'reconciled'
    vr.append(dict(item=it, sid=k['sid'], leaf=k['leaf'], mach=k['mach_pile'], owner=k['owner_pile'], p1=s1, p2=s2, rc=rc,
                   verdict=NAME.get(v, 'unresolved'), grade=g))
cols = ['item', 'sid', 'leaf', 'mach', 'owner', 'p1', 'p2', 'rc', 'verdict', 'grade']
with open(H + '/verdicts.tsv', 'w') as f:
    f.write('\t'.join(cols) + '\n')
    for r in sorted(vr, key=lambda r: r['sid']): f.write('\t'.join(str(r[c]) for c in cols) + '\n')
with open(H + '/owner_right.tsv', 'w') as f:
    f.write('sid\titem\tleaf\tmachine_pile\towner_pile\tgrade\tcorrection_grade\n')
    for r in sorted(vr, key=lambda r: r['sid']):
        if r['verdict'] == 'owner right': f.write(f"{r['sid']}\t{r['item']}\t{r['leaf']}\t{r['mach']}\t{r['owner']}\t{r['grade']}\tM\n")
per = defaultdict(Counter)
for r in vr: per[r['leaf']][r['verdict']] += 1; per['all'][r['verdict']] += 1
out['targets'] = {lf: dict(c) for lf, c in sorted(per.items())}
out['target_grades'] = dict(Counter(r['grade'] for r in vr))
out['splits'] = sum(1 for r in vr if r['grade'] == 'reconciled')
json.dump(out, open(H + '/summary.json', 'w'), indent=1); print(json.dumps(out, indent=1))
