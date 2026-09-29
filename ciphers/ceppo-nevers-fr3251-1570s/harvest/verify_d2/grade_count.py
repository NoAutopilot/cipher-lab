"""Token grade counts on a verifier's blind sequence D (VERIFY-CEPPO-D2-1): S = both raw passes and D agree at H;
M = otherwise keyed by the printed table; W = X_THETA2 (r from the fr.3252 f.36v period gloss); I = X_POUND (l, context only);
U = X_NEW or '?'. Usage: grade_count.py passD.tsv"""
import csv,sys
from collections import Counter
c=Counter()
for r in csv.DictReader(open(sys.argv[1]),delimiter='\t'):
    s=r['sign_id']
    c['W' if s=='X_THETA2' else 'I' if s=='X_POUND' else 'U' if s in('X_NEW','?') else 'S' if (r['src']=='AB' and r['conf']=='H') else 'M']+=1
print(sum(c.values()),dict(c))
