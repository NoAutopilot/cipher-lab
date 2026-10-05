#!/usr/bin/env python3
"""DEF1-VIV54: tally the hand-placed judge (tx/lookalike54/viv54H_judge.tsv) against PREREG-N7VIV54R's built-in check. Writes tx/viv54H_tally.json."""
import csv, json, os
HERE = os.path.dirname(os.path.abspath(__file__)); LA = os.path.join(HERE, 'lookalike54')
key = {r['cid']: r for r in csv.DictReader(open(os.path.join(LA, 'viv54H_key.tsv')), delimiter='\t')}
j = {r['cid']: r for r in csv.DictReader(open(os.path.join(LA, 'viv54H_judge.tsv')), delimiter='\t')}
out = {'rows': []}
for s in ('after_to', 'foil'):
    ids = [c for c in key if key[c]['set'] == s]
    out[s] = {'n': len(ids), 'sigma_HM': sum(j[c]['class'] == 'SIGMA' and j[c]['conf'] in 'HM' for c in ids),
              'classes': {k: sum(j[c]['class'] == k for c in ids) for k in ('SIGMA', 'ZED', 'OTHER', 'UNSURE')}}
for c in sorted(key):
    out['rows'].append({**{k: key[c][k] for k in ('cid', 'id', 'label', 'set')}, 'class': j[c]['class'], 'conf': j[c]['conf']})
out['check_after_to_ge7'] = out['after_to']['sigma_HM'] >= 7
out['verdict'] = 'pass' if out['check_after_to_ge7'] else 'NON-TEST (after-to SIGMA H/M < 7)'
json.dump(out, open(os.path.join(HERE, 'viv54H_tally.json'), 'w'), indent=1)
print(json.dumps({k: v for k, v in out.items() if k != 'rows'}))
for r in out['rows']:
    print(r['cid'], r['id'], r['label'], r['set'], r['class'], r['conf'])
