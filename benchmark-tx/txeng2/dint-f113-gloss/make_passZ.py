#!/usr/bin/env python3
"""TXP-D113: passZ_pipeline.tsv = rec/ciphertext_draft.tsv (reconcile_passes.py A/B --keep-dots) with every adjud_queue row
replaced by the Sonnet adjudicator's choice (adjud_out.tsv; NONE deletes, two labels insert). Run from the repo root."""
import csv
D = 'benchmark-tx/txeng2/dint-f113-gloss'
rd = lambda p: list(csv.DictReader(open(p), delimiter='\t'))
draft = rd(D + '/rec/ciphertext_draft.tsv')
adj = {(r['line'], int(r['col'])): r['sign'].strip() for r in rd(D + '/adjud_out.tsv')}
assert len(adj) == len(rd(D + '/adjud_queue.tsv'))
out = {}
for r in draft:
    k = (r['line'], int(r['position']))
    if k in adj:
        a = adj[k]
        ss = [] if a == 'NONE' else ([a] if a.startswith('NEW') else a.split())
    else:
        ss = [r['sign']] if r['sign'] != '-' else []
    out.setdefault(r['line'], []).extend(ss)
with open(D + '/passZ_pipeline.tsv', 'w') as f:
    f.write('line\tpos\tsign\n')
    for l, ss in out.items():
        for i, s in enumerate(ss):
            f.write('%s\t%d\t%s\n' % (l, i + 1, s))
