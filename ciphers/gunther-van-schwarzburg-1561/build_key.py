#!/usr/bin/env python3
"""G1 24 Sept 2026: key.tsv (grade C, source pairs_5109.tsv) and key_conflicts.tsv. --check exits 1 if stale.
u/v/w are one class in this hand (Willem writes v for w); capital/lower merged."""
import csv,collections,sys
norm=lambda u:{'v':'u','w':'u','V':'u','W':'u'}.get(u,u.lower() if len(u)==1 else u)
d=collections.defaultdict(collections.Counter); m=collections.defaultdict(collections.Counter)
for r in csv.DictReader(open('pairs_5109.tsv'),delimiter='\t'):
    (d if r['conf']=='C' else m)[r['sign']][norm(r['unit'])]+=1
key=['sign\tvalue\tgrade\tsource\tnote']; conf=['sign\tvalues\tnote']
for s in sorted(set(d)|set(m)):
    c=d[s]; mm=m[s]
    if c:
        v,n=c.most_common(1)[0]
        key.append(f"{s}\t{v}\tC\tpairs_5109.tsv\tn={sum(c.values())} "+','.join(f'{a}:{b}' for a,b in c.items())+(' M:'+','.join(f'{a}:{b}' for a,b in mm.items()) if mm else ''))
        if len(c)>1: conf.append(f"{s}\t"+','.join(f'{a}:{b}' for a,b in c.items())+"\tC-grade pairs disagree")
    else:
        v,n=mm.most_common(1)[0]
        if v=='-': continue
        key.append(f"{s}\t{v}\tM\tpairs_5109.tsv\tn={sum(mm.values())} only doubtful alignments")
    if mm and c and any(a not in c and a!='-' for a in mm): conf.append(f"{s}\t"+','.join(f'{a}:{b}' for a,b in mm.items())+f"\tM-grade alignment differs from C value {v}")
K='\n'.join(key)+'\n'; C='\n'.join(conf)+'\n'
if '--check' in sys.argv:
    ok=open('key.tsv').read()==K and open('key_conflicts.tsv').read()==C
    print('key current' if ok else 'STALE'); sys.exit(0 if ok else 1)
open('key.tsv','w').write(K); open('key_conflicts.tsv','w').write(C); print(len(key)-1,'signs')
