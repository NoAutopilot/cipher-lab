#!/usr/bin/env python3
"""bMALX step 6: system-match check -- how many of record 509's codes occur in pool/pooled.tsv's
sign set (same number range/forms), and the frequency ranks of the shared ones."""
import csv, re
from collections import Counter

pool_rows = list(csv.DictReader(open('pool/pooled.tsv'), delimiter='\t'))
pool_counts = Counter(r['sign'] for r in pool_rows)
print('pool distinct signs:', len(pool_counts), 'total pool signs:', sum(pool_counts.values()))

cribs = list(csv.DictReader(open('cribs.tsv'), delimiter='\t'))
codes_509 = set()
for r in cribs:
    code = r['code']
    m = re.match(r'^([A-Z]\.?)?(\d{1,3})([A-Z]\.?)?$', code)
    if m and m.group(2):
        codes_509.add(m.group(2))
print('distinct 509 numeric codes (this crib pass):', len(codes_509))

shared = sorted(codes_509 & set(pool_counts.keys()), key=lambda v: -pool_counts[v])
ranked = sorted(pool_counts.items(), key=lambda x: -x[1])
rank_of = {v: i + 1 for i, (v, c) in enumerate(ranked)}
print(f'shared with pool: {len(shared)}/{len(codes_509)} = {len(shared)/len(codes_509):.3f}')
print('shared codes, pool_count, rank (of 173 distinct pool values):')
for v in shared:
    print(' ', v, 'pool_count=', pool_counts[v], 'rank=', rank_of[v])
not_shared = sorted(codes_509 - set(pool_counts.keys()), key=lambda x: int(x))
print('509 codes not seen in pool:', not_shared)
