#!/usr/bin/env python3
"""Test x/10x pairs against a null preserving occupied decades and units-digit margins.
This tests pair enrichment, not plaintext equivalence. Does not treat inferred zeros as removable.
"""
import random,json,re,statistics
from pathlib import Path
D=Path(__file__).resolve().parent; src=D/'ciphertext_editorial_clean.txt'
s=[int(w) for l in src.read_text().splitlines() if not l.startswith('#') for w in l.split() if w.isdigit()];v=set(s)
def stat(v):return sum(10*x in v for x in v)
def sample(v,rng,steps):
 a=list(v);ss=set(v)
 for _ in range(steps):
  i,j=rng.sample(range(len(a)),2);x,y=a[i],a[j];xx=x//10*10+y%10;yy=y//10*10+x%10
  if xx<=0 or yy<=0 or xx in ss or yy in ss:continue
  ss.remove(x);ss.remove(y);ss.add(xx);ss.add(yy);a[i]=xx;a[j]=yy
 return ss
rng=random.Random(20260927);z=v;null=[]
for i in range(2500):
 z=sample(z,rng,3000 if i==0 else 300)
 if i>=500:null.append(stat(z))
pairs=sorted((x,10*x) for x in v if x*10 in v)
r={'numeric_tokens':len(s),'distinct':len(v),'pairs':pairs,'pair_count':len(pairs),'null':'2x2 occupied-cell swaps preserving decade totals and units-digit totals; 500 burn-in samples, 2000 samples, 300 proposals/sample','null_mean':statistics.mean(null),'null_sd':statistics.stdev(null),'null_p95':sorted(null)[int(.95*len(null))],'p_upper':(1+sum(n>=len(pairs) for n in null))/(len(null)+1),'null_min':min(null),'null_max':max(null)}
(D/'padding_clean_results.json').write_text(json.dumps(r,indent=2)+'\n');print(json.dumps(r,indent=2))
