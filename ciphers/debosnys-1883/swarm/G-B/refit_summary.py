#!/usr/bin/env python3
"""Refit-null summary: for each statistic, the real key's held-out value (keys/P2_fit_<fit>_test_<test>.json) against
the 50 refits on order-shuffled fit text (refit/refit_<fit>_*.json): refit p99 and the real value's rank.
  python3 refit_summary.py c2 c1 [REAL.json]"""
import glob, json, sys
fit, test = sys.argv[1], sys.argv[2]
real = json.load(open(sys.argv[3] if len(sys.argv) > 3 else f'keys/P2_fit_{fit}_test_{test}.json'))['stats']
refs = [json.load(open(f))['stats'] for f in sorted(glob.glob(f'refit/refit_{fit}_*.json'))]
out = {'fit': fit, 'test': test, 'refits': len(refs), 'stats': {}}
for k, v in real.items():
    vals = sorted(r[k]['real'] for r in refs)
    p99 = vals[min(len(vals) - 1, int(0.99 * len(vals)))]
    out['stats'][k] = {'real': v['real'], 'refit_p99': round(p99, 4), 'refit_median': round(vals[len(vals) // 2], 4),
                       'refits_below_real': sum(1 for x in vals if x < v['real']),
                       'refit_pct_plain_median': sorted(r[k]['pct'] for r in refs)[len(refs) // 2],
                       'refit_pct_plain_max': max(r[k]['pct'] for r in refs),
                       'refit_beats_all_both': sum(1 for r in refs if r[k]['beats_all'] and r[k]['beats_all_strat'])}
json.dump(out, open(f'refit/summary_{fit}_{test}.json', 'w'), indent=1)
for k, s in out['stats'].items(): print(k, s)
