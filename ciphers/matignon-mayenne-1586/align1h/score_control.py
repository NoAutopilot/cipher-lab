#!/usr/bin/env python3
"""bMAT1G (copied from align1e): score the blinded control answers (align1e/control_answers.tsv) against key.tsv values
(labels_control.tsv). Exact match on the value; NULL never matches a keyed H value. Exit 0 if k >= 16."""
import csv, os, sys
h = os.path.dirname(os.path.abspath(__file__))
truth = {r['label']: r['key_value'] for r in csv.DictReader(open(os.path.join(h, 'labels_control.tsv')), delimiter='\t') if r['label'].startswith('X')}
rows = list(csv.DictReader(open(os.path.join(h, 'control_answers.tsv')), delimiter='\t'))
conf = {r['label']: (r.get('confidence') or '').strip().upper()[:1] for r in rows}
ans = {r['label']: r['value'].strip().lower() for r in csv.DictReader(open(os.path.join(h, 'control_answers.tsv')), delimiter='\t')}
k = 0
for l in sorted(truth):
    ok = ans.get(l, '') in truth[l].split('|')
    k += ok
    print('%s\ttrue=%s\tgot=%s\t%s' % (l, truth[l], ans.get(l, ''), 'OK' if ok else 'x'))
hk = [l for l in truth if conf.get(l) == 'H']
print('H-confidence answers: %d/%d correct' % (sum(ans.get(l, '') in truth[l].split('|') for l in hk), len(hk)))
print('control k=%d/20 gate 16' % k)
sys.exit(0 if k >= 16 else 1)
