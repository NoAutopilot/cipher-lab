#!/usr/bin/env python3
"""D1-SEURE: per-line edit distance between two blind passes (passA.tsv, passB.tsv), normalised by the longer line.
Usage: pass_err.py passA.tsv passB.tsv [--json out.json]. Braced clear words count as one token."""
import sys, json
def rd(p):
    d = {}
    for i, l in enumerate(open(p, encoding='utf-8')):
        if i == 0 or not l.strip(): continue
        k, _, v = l.rstrip('\n').partition('\t'); d[k.strip()] = v.split()
    return d
def ed(a, b):
    prev = list(range(len(b) + 1))
    for i, x in enumerate(a, 1):
        cur = [i]
        for j, y in enumerate(b, 1):
            cur.append(min(prev[j] + 1, cur[j - 1] + 1, prev[j - 1] + (x != y)))
        prev = cur
    return prev[-1]
A, B = rd(sys.argv[1]), rd(sys.argv[2])
tot_e = tot_n = 0; rows = []
for k in sorted(set(A) | set(B)):
    a, b = A.get(k, []), B.get(k, []); e = ed(a, b); n = max(len(a), len(b))
    tot_e += e; tot_n += n; rows.append((k, len(a), len(b), e, round(e / n, 3) if n else 0))
for r in rows: print(*r, sep='\t')
res = {'edits': tot_e, 'maxlen_signs': tot_n, 'err': round(tot_e / tot_n, 3), 'lenA': sum(len(v) for v in A.values()), 'lenB': sum(len(v) for v in B.values())}
print(json.dumps(res))
if '--json' in sys.argv: json.dump({'lines': rows, **res}, open(sys.argv[sys.argv.index('--json') + 1], 'w'), indent=1)
