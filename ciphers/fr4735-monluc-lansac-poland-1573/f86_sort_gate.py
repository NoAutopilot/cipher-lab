#!/usr/bin/env python3
# MONLUC-F86 (9 Oct 2026): pre-registered gate on the blind sort (groups typed from the sorter reply, f86_k07_sort.tsv). python3 -I f86_sort_gate.py
import random
grp={2:'A',3:'A',5:'A',6:'A',7:'A',11:'A',18:'A',1:'B',8:'B',12:'B',13:'B',14:'B',16:'B',4:'C',10:'C',15:'C',17:'C'}
faced={1:'t',2:'g',3:'g',5:'g',6:'g',7:'t',8:'t',10:'n',12:'t',13:'g',14:'t',15:'t',16:'t',17:'s'}
def mx(f):
    c={}
    for t,v in f.items():
        if v=='t': c[grp[t]]=c.get(grp[t],0)+1
    return max(c.values())
obs=mx(faced); tiles=list(faced); vals=list(faced.values()); R=random.Random(886); ge=0; dist=[]
for _ in range(10000):
    R.shuffle(vals); s=mx(dict(zip(tiles,vals))); dist.append(s); ge+=s>=obs
dist.sort(); print('obs',obs,'p',ge/10000,'null p95',dist[9499])
# fixed-X version for reference
cnt=0
for _ in range(10000):
    R.shuffle(vals); f=dict(zip(tiles,vals)); cnt+=sum(1 for t,v in f.items() if v=='t' and grp[t]=='B')>=5
print('fixed X=B p',cnt/10000)
