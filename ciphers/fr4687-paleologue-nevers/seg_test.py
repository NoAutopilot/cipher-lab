# Segmentation test for fr4687: do the most frequent two-digit units sit on one parity within a line,
# as they must under a fixed two-digit grid? Observed vs matched synthetic controls (same line lengths).
import random
from collections import Counter
import os
HERE = os.path.dirname(os.path.abspath(__file__))
S = {}
for _l in open(os.path.join(HERE, "passC_native.tsv")):
    if _l.startswith("#") or _l.startswith("line\t"):
        continue
    _k, _s = _l.rstrip("\n").split("\t")
    S[_k] = _s.split()
FREQ = dict(e=11.8,a=11.7,i=11.3,o=9.8,n=6.9,l=6.5,r=6.4,t=5.6,s=5.0,c=4.5,d=3.7,p=3.0,u=3.0,m=2.5,
            v=2.1,g=1.6,h=1.5,f=1.1,b=0.9,q=0.5,z=0.5)
def top_units(lines,k=8):
    c=Counter(v[i]+v[i+1] for v in lines for i in range(len(v)-1)); return {u for u,_ in c.most_common(k)}
def lock(lines):
    T=top_units(lines); fr=[]
    for v in lines:
        par=Counter(i%2 for i in range(len(v)-1) if v[i]+v[i+1] in T)
        n=sum(par.values())
        if n>=3: fr.append(max(par.values())/n)
    return sum(fr)/len(fr)
lens=[len(v) for v in S.values()]
def letters(n,rng):
    ks=list(FREQ); w=[FREQ[k] for k in ks]; return rng.choices(ks,w,k=n)
def synth(kind,err,rng):
    if kind=='fixed2':
        pool=rng.sample(range(10,100),60); code={}; it=iter(pool)
        for k in FREQ: code[k]=[str(next(it)) for _ in range(3 if FREQ[k]>6 else 2 if FREQ[k]>2.5 else 1)]
    else:  # mixed 1/2/3-digit: single digits, 10-29, 100-299
        pool=[str(x) for x in rng.sample(range(3,10),7)]+[str(x) for x in rng.sample(range(10,30),20)]+[str(x) for x in rng.sample(range(100,300),20)]
        rng.shuffle(pool); it=iter(pool); code={}
        for k in FREQ: code[k]=[next(it) for _ in range(3 if FREQ[k]>6 else 2 if FREQ[k]>2.5 else 1)]
    s=''.join(rng.choice(code[c]) for c in letters(400,rng))
    s=list(s[rng.randrange(2):])
    out=[];i=0
    for L in lens:
        line=s[i:i+L]; i+=L
        e=[]
        for d in line:  # reading errors: drop or insert a digit
            r=rng.random()
            if r<err/2: continue
            e.append(d)
            if r>1-err/2: e.append(str(rng.randrange(10)))
        out.append(e)
    return out
rng=random.Random(7)
print('observed, y kept as a sign  : %.3f'%lock(list(S.values())))
print('observed, y dropped         : %.3f'%lock([[t for t in v if t!='y'] for v in S.values()]))
sh=sorted(lock([rng.sample(v,len(v)) for v in S.values()]) for _ in range(300))
print('shuffled observed lines     : mean %.3f  5-95%% %.3f-%.3f'%(sum(sh)/300,sh[15],sh[285]))
for kind in ('fixed2','mixed123'):
    for err in (0.0,0.05,0.10):
        r=sorted(lock(synth(kind,err,rng)) for _ in range(300))
        print('control %-8s err %.2f   : mean %.3f  5-95%% %.3f-%.3f'%(kind,err,sum(r)/300,r[15],r[285]))
