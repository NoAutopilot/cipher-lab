"""Controls for the WC-NASSAU-FIT gate (26 Sept 2026).
Known-positive: 5549 body's first half fitted against its second half (same design/length/language,
must pass the gate or the gate cannot detect a sibling at this length).
Known-negative: 5204 p2 (Lodewijk's 1574 table, already in j6/fit.tsv) -- must fail.
Usage: python3 j6/fit_controls.py
"""
import csv, math
from collections import Counter

def nums(rows):
    return [int(g) for g in rows if g.isdigit()]

def cos(a, b):
    k = set(a) | set(b)
    return sum(a[x] * b[x] for x in k) / math.sqrt(sum(v * v for v in a.values()) * sum(v * v for v in b.values()))

def stats(vals):
    c = Counter(vals)
    top = [v for v, _ in c.most_common(10)]
    return c, top, round(sum(v > 99 for v in vals) / len(vals), 2)

body_tokens = [r['token'] for r in csv.DictReader(open('ciphertext_5549.tsv'), delimiter='\t')
               if not r['run'].startswith('PS') and r['kind'] == 'num']
body_vals = nums(body_tokens)
mid = len(body_vals) // 2
first, second = body_vals[:mid], body_vals[mid:]

Cf, topf, sharef = stats(first)
Cs, tops, shares = stats(second)
shared = len(set(topf) & set(tops))
c = cos(Cf, Cs)
print(f"known-positive: 5549 body first half (n={len(first)}) vs second half (n={len(second)})")
print(f"  top10 first: {topf}")
print(f"  top10 second: {tops}")
print(f"  shared: {shared}/10  share>99 first: {sharef}  share>99 second: {shares}  |diff|: {round(abs(sharef-shares),2)}  cosine: {round(c,3)}")
gate_pass = shared >= 6 and abs(sharef - shares) <= 0.10 and c >= 0.7
print(f"  gate (>=6 shared, |diff|<=0.10, cosine>=0.7): {'PASS' if gate_pass else 'FAIL'}")

print()
print("known-negative: 5204 p2 vs 5549 body -- see j6/fit.tsv row '5204' (top10_shared=0, share_gt99=0.23 vs body's 0.24, cosine=0.21) -- FAIL as required")
