#!/usr/bin/env python3
"""bMAT1H: score the blinded seed-8620 control against the PRE-REGISTERED gate (fixed by the LANE B9 orchestrator at
08:17 UTC 26 Sept 2026, commit fa0b429, before any run): PASS iff n_high >= 8 AND right_high >= ceil(0.9 * n_high).
k/20 overall is reported for the record only. Also lists each drawn code's passage frequency, and flags the degenerate
case where every H answer is a code occurring 3+ times. Exit 0 on PASS, 1 on FAIL."""
import csv, math, os, sys
h = os.path.dirname(os.path.abspath(__file__))
lab = {r['label']: r for r in csv.DictReader(open(os.path.join(h, 'labels_control.tsv')), delimiter='\t') if r['label'].startswith('X')}
ans = {r['label']: r for r in csv.DictReader(open(os.path.join(h, 'control_answers.tsv')), delimiter='\t')}
k = 0; hi = []; out = []
for l in sorted(lab):
    t = lab[l]; a = ans.get(l, {})
    v = (a.get('value') or '').strip().lower(); c = (a.get('confidence') or '').strip().upper()[:1]
    ok = v in t['key_value'].split('|'); k += ok
    if c == 'H': hi.append((l, ok, int(t['count'])))
    out.append('%s\tcode=%s\tcount=%s\ttrue=%s\tgot=%s\tconf=%s\t%s' % (l, t['code'], t['count'], t['key_value'], v, c, 'OK' if ok else 'x'))
n = len(hi); r = sum(o for _, o, _ in hi); need = math.ceil(0.9 * n)
ok = n >= 8 and r >= need
print('\n'.join(out))
print('overall k=%d/20 (record only)' % k)
print('H answers n_high=%d, right=%d, need >=8 and >=%d -> %s' % (n, r, need, 'PASS' if ok else 'FAIL'))
if n and all(c >= 3 for _, _, c in hi): print('NOTE: every H answer is a code occurring 3+ times in the passage')
print('H answers by passage count: ' + ', '.join('%s(%d,%s)' % (l, c, 'ok' if o else 'x') for l, o, c in hi))
sys.exit(0 if ok else 1)
