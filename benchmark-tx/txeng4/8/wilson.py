#!/usr/bin/env python3
"""TXE4-8: per-pass table from scores/*.json: unit-cost edits (S/D/I), err_true with Wilson 95% on both masks, strict beside."""
import json, math, os
HERE = os.path.dirname(os.path.abspath(__file__))
def wilson(k, n, z=1.96):
    if not n: return (0, 0)
    p = k / n; d = 1 + z * z / n; c = p + z * z / (2 * n); h = z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n))
    return ((c - h) / d, (c + h) / d)
print('pass\tmask\tunit_cost_edits\tS\tD\tI\terr_true\terrors/scored\twilson95\tstrict_err_true')
for p in ['N1', 'N2', 'O1', 'O2', 'R1']:
    js = json.load(open(os.path.join(HERE, 'scores', p + '.json')))
    items = js['items'] if isinstance(js, dict) and 'items' in js else js
    d = items[0] if isinstance(items, list) else items[next(iter(items))]
    for mask, dd in (('as_measured', d), ('flagged_excluded', d.get('flagged_excluded') or d.get('excl') or {})):
        if not dd: continue
        k, n = dd['errors'], dd['scored']; lo, hi = wilson(k, n)
        print(f"{p}\t{mask}\t{dd['ser_errors']}\t{dd['ser_S']}\t{dd['ser_D']}\t{dd['ser_I']}\t{dd['err_true']:.3f}\t{k}/{n}\t{lo:.3f}-{hi:.3f}\t{dd.get('strict', {}).get('err_true', '')}")
