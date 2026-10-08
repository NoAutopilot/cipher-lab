#!/usr/bin/env python3
"""MANT-0609: rank unglossed cipher frames by Krauske-table coverage of their eye-read codes.
Krauske = key.tsv rows whose source starts 'Krauske' (codes 1-401). 'any key' adds the period-gloss and pooled rows.
Writes mant0609/rank_unglossed.tsv. Coverage is of the eye-read sample (grade M), not of a transcription."""
import csv, os, re
D = os.path.dirname(os.path.abspath(__file__)) + '/..'
K, A = set(), set()
for r in csv.DictReader(open(D + '/key.tsv'), delimiter='\t'):
    A.add(r['code'])
    if r['source'].startswith('Krauske'): K.add(r['code'])
rows = [r for r in csv.DictReader((l for l in open(D + '/mant0609/unglossed_codes.tsv') if not l.startswith('#')), delimiter='\t')]
out = []
for r in rows:
    toks = [t for g in r['codes'].split() for t in g.split('.') if t]
    n = len(toks); k = sum(t in K for t in toks); a = sum(t in A for t in toks)
    runs = [g for g in r['codes'].split() if '.' in g]
    longest = max((len(g.split('.')) for g in runs), default=0)
    out.append(dict(loc=r['loc'], frame=r['frame'], folio_date=r['folio_date'], tokens_seen=n, runs=len(runs), longest_run=longest,
                    krauske_cov=f'{k/n:.2f}' if n else '', anykey_cov=f'{a/n:.2f}' if n else '',
                    outside_krauske=' '.join(sorted({t for t in toks if t not in K}, key=int)), source=r['source'], leaf_note=r['leaf_note']))
# rank: Krauske coverage x readable length (tokens in runs), ties by longest run
def score(o):
    c = float(o['krauske_cov'] or 0); return (round(c * o['tokens_seen'], 2), o['longest_run'])
out.sort(key=score, reverse=True)
with open(D + '/mant0609/rank_unglossed.tsv', 'w') as f:
    w = csv.DictWriter(f, fieldnames=['rank'] + list(out[0]), delimiter='\t'); w.writeheader()
    for i, o in enumerate(out, 1): w.writerow(dict(rank=i, **o))
for i, o in enumerate(out, 1): print(i, o['loc'], o['frame'], o['tokens_seen'], o['krauske_cov'], o['anykey_cov'], o['outside_krauske'])
