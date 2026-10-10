#!/usr/bin/env python3
"""DV1d steps (3)-(4), read-free (TXE2-VIV102-REANCHOR, 10 Oct 2026). Counts only; never prints a sign or truth value.
(3) F48 two-rate decomposition of tx_bench --exclude-flagged on dev2: position errors at unflagged positions / unflagged
    (tools/tx_bench.position_errors on the flag-dropped truth), insertions (tx_bench.score_item, line-charged) / signs read
    (output signs on the item's lines); checks pos_err + ins equals tx_bench's flagged-excluded numerator.
(4) passZ_dv1's insertions against dev2 by line, s1/s2 half and overlap zone (from overlap_audit_passZ.json), against the
    plain-word lines L01, L34, L37."""
import json, os, sys
from collections import Counter
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import tx_bench as T  # noqa: E402
HERE = os.path.dirname(os.path.abspath(__file__))
TR = os.path.join(ROOT, 'benchmark-tx/vivonne1573-f102r-dev2.truth.tsv')
P = os.path.join(ROOT, 'benchmark-tx/outputs/vivonne1573-f102r-dev')
truth = T.read_tsv(TR)
lines = {r['line'] for r in truth}
tf = T.drop_flagged(truth)
unfl = sum(r['status'] == 'scored' for r in tf)
print('(3) F48 decomposition, dev2, unflagged positions %d' % unfl)
for n in ('passZ_dv1', 'passA_dv1', 'passB_dv1'):
    out = T.load_output([os.path.join(P, n + '.tsv')])
    pe = sum(T.position_errors(tf, out).values())
    r = T.score_item(tf, out)
    read = sum(len(v) for k, v in out.items() if k in lines)
    num = r['wrong'] + r['deleted'] + r['inserted']
    print('%s: flagged-excluded %d/%d = %.3f | position errors %d/%d = %.3f | insertions %d/%d read = %.3f | check %s' % (
        n, num, unfl, num / unfl, pe, unfl, pe / unfl, r['inserted'], read, r['inserted'] / read,
        'ok' if pe + r['inserted'] == num else 'MISMATCH'))
print('(4) passZ_dv1 insertions by line / half / zone')
oa = json.load(open(os.path.join(HERE, 'overlap_audit_passZ.json')))
ins = [x for x in oa['passes']['Z']['indels'] if x['kind'].startswith('ins')]
PLAIN = {'f102r_L01', 'f102r_L34', 'f102r_L37'}
def half(x):
    ln = oa['lines'][x['line']]
    a, b = ln['zones'][0]
    return 's1' if x['x_native'] < (a + b) / 2 else 's2'
per = Counter((x['line'], half(x), x['zone']) for x in ins)
byline = Counter(x['line'] for x in ins)
print('line\tins\ts1\ts2\tinside\tseam\toutside\tplain-word line')
for ln in sorted(byline):
    xs = [x for x in ins if x['line'] == ln]
    h = Counter(half(x) for x in xs); z = Counter(x['zone'] for x in xs)
    print('%s\t%d\t%d\t%d\t%d\t%d\t%d\t%s' % (ln, len(xs), h['s1'], h['s2'], z['inside'], z['seam'], z['outside'], 'yes' if ln in PLAIN else ''))
cls = Counter('plain-word line' if x['line'] in PLAIN else ('seam/overlap' if x['zone'] != 'outside' else 'elsewhere') for x in ins)
h = Counter(half(x) for x in ins)
print('total insertions %d: plain-word lines %d, seam/overlap (other lines) %d, elsewhere %d; s1 %d s2 %d; lines with any %d of %d' % (
    len(ins), cls['plain-word line'], cls['seam/overlap'], cls['elsewhere'], h['s1'], h['s2'], len(byline), len(lines)))
