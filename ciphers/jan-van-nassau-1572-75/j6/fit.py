"""Fit test: compare numeral profile of candidate pages (j6/fit_<n>.tsv) with the 5549 body (runs 1-61).
Usage: python3 j6/fit.py  -> writes j6/fit.tsv"""
import csv, glob, math, re
from collections import Counter
def nums(rows):
    return [int(g) for g in rows if re.fullmatch(r'\d+', g)]
body = [r['token'] for r in csv.DictReader(open('ciphertext_5549.tsv'), delimiter='\t')
        if not r['run'].startswith('PS') and r['kind'] == 'num']
B = Counter(nums(body)); btop = [v for v, _ in B.most_common(10)]
def cos(a, b):
    k = set(a) | set(b); return sum(a[x]*b[x] for x in k) / math.sqrt(sum(v*v for v in a.values())*sum(v*v for v in b.values()))
out = [['cand', 'n', 'distinct', 'max', 'share_gt99', 'top10', 'top10_shared_with_5549', 'cosine', 'clear_suffix_rows']]
def row(name, vals, suff):
    c = Counter(vals); top = [v for v, _ in c.most_common(10)]
    out.append([name, len(vals), len(c), max(vals), round(sum(v > 99 for v in vals)/len(vals), 2),
                ','.join(map(str, top)), len(set(top) & set(btop)), round(cos(B, c), 2), suff])
row('5549body', nums(body), '')
for f in sorted(glob.glob('j6/fit_*.tsv')):
    rs = [r for r in csv.DictReader(open(f), delimiter='\t')]
    g = [r['group'] for r in rs]
    row(f[7:-4], nums(g) or [0], sum(x.startswith('s:') for x in g))
w = csv.writer(open('j6/fit.tsv', 'w'), delimiter='\t', lineterminator='\n'); w.writerows(out)
for r in out: print(*r, sep='\t')
