#!/usr/bin/env python3
"""A1B-VILL-TX2: score the settled sample (PREREG-VILL-TX2.md item 3-4). Reads sample_key.tsv, settled.tsv,
agreement.tsv; writes settle_score.tsv. --check exits 1 if the committed settle_score.tsv is stale."""
import csv, math, sys, collections
def wilson(k, n, z=1.96):
    if n == 0: return (0.0, 1.0)
    p = k/n; d = 1+z*z/n; c = p+z*z/(2*n); h = z*math.sqrt(p*(1-p)/n+z*z/(4*n*n))
    return ((c-h)/d, (c+h)/d)
key = {r['id']: r for r in csv.DictReader(open('sample_key.tsv'), delimiter='\t')}
st = {r['id']: r for r in csv.DictReader(open('settled.tsv'), delimiter='\t')}
cols = sum(int(r['columns']) for r in csv.DictReader(open('agreement.tsv'), delimiter='\t'))
agree = sum(int(r['agree']) for r in csv.DictReader(open('agreement.tsv'), delimiter='\t'))
NOTATION = {'S50'}  # o vs 0: notation, not a reading split (normalised before the final reconcile)
out = collections.Counter(); strat = collections.defaultdict(collections.Counter)
for i, k in key.items():
    v = st[i]['verdict'].strip()
    if i in NOTATION: out['excluded_notation'] += 1; continue
    if k['kind'] == 'agr':
        out['agr_' + ('A_right' if v == 'confirm' else 'A_wrong' if v == 'correct' else 'cannot')] += 1; continue
    if v == 'cannot': out['dis_cannot'] += 1; strat[k['stratum']]['cannot'] += 1; continue
    if v == 'neither': w = 'A_wrong'
    else:
        chosen = k['opt1'] if v == 'opt1' else k['opt2']
        w = 'A_right' if chosen == (k['A'] or '(nothing)') else 'A_wrong'
    out['dis_' + w] += 1; strat[k['stratum']][w] += 1
d = 1 - agree/cols
nd = out['dis_A_right'] + out['dis_A_wrong']; na = out['agr_A_right'] + out['agr_A_wrong']
pd = out['dis_A_wrong']/nd; pa = out['agr_A_wrong']/na
lo_d, hi_d = wilson(out['dis_A_wrong'], nd); lo_a, hi_a = wilson(out['agr_A_wrong'], na)
err = d*pd + (1-d)*pa; lo = d*lo_d + (1-d)*lo_a; hi = d*hi_d + (1-d)*hi_a
pb = out['dis_A_right']/nd  # B wrong share among settled disagreements (B wrong when A right; 'neither' none)
rows = [('columns', cols), ('agree', agree), ('err_2reader', round(d, 3))] + sorted(out.items()) + \
       [('p_dis_A_wrong', round(pd, 3)), ('p_dis_ci', f'{lo_d:.3f}-{hi_d:.3f}'), ('p_agr_A_wrong', round(pa, 3)),
        ('p_agr_ci', f'{lo_a:.3f}-{hi_a:.3f}'), ('err_adjudicated_A', round(err, 3)), ('err_A_ci95', f'{lo:.3f}-{hi:.3f}'),
        ('err_adjudicated_B', round(d*pb + (1-d)*pa, 3))] + \
       [(f'stratum_{s}', ' '.join(f'{k}={v}' for k, v in sorted(c.items()))) for s, c in sorted(strat.items())]
txt = 'stat\tvalue\n' + ''.join(f'{a}\t{b}\n' for a, b in rows)
if '--check' in sys.argv:
    sys.exit(0 if open('settle_score.tsv').read() == txt else 1)
open('settle_score.tsv', 'w').write(txt); print(txt)
