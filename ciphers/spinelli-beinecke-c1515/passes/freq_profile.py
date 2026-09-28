#!/usr/bin/env python3
"""H12: the 265-sign atlas-coded letter as a homophonic/simple-substitution profile, with controls.

Reads passes/letter_codes_v3.tsv. Reports: (1) code frequencies and the index of coincidence (IC) of the code
sequence, against the IC of it16 Italian text (v->u, j->i) and of a uniform 26-symbol random text of the same N;
(2) Sukhotin's vowel-identification algorithm on the code sequence, calibrated on 20 Italian samples of the same
N drawn from it16 (how many of a e i o u it recovers at N=265, and how many false vowels), and controlled on
20 order-shuffled copies of the cipher (a shuffled-order text has no contact structure: the vowel set it returns
is the null distribution). A code named vowel-like here is a hypothesis for H16's solver, not a reading.
"""
import csv, os, glob, random
from collections import Counter
HERE=os.path.dirname(os.path.abspath(__file__)); REPO=os.path.dirname(os.path.dirname(os.path.dirname(HERE)))
seq=[r['code'] for r in csv.DictReader(open(os.path.join(HERE,'letter_codes_v3.tsv')),delimiter='\t')]
N=len(seq); cnt=Counter(seq)
def ic(s):
    c=Counter(s); n=len(s); return sum(v*(v-1) for v in c.values())/(n*(n-1))
txt=''
for p in glob.glob(os.path.join(REPO,'tools','data','it16','*.txt')): txt+=open(p,encoding='utf-8',errors='ignore').read().lower()
txt=''.join(ch for ch in txt.replace('v','u').replace('j','i') if 'a'<=ch<='z')
random.seed(11)
def sample(n):
    i=random.randrange(0,len(txt)-n); return list(txt[i:i+n])
ic_it=sum(ic(sample(N)) for _ in range(50))/50
ic_rand=sum(ic([random.randrange(26) for _ in range(N)]) for _ in range(50))/50
print(f'N={N}, {len(cnt)} distinct codes; IC cipher {ic(seq):.4f} | it16 samples of N {ic_it:.4f} | uniform 26-symbol random {ic_rand:.4f}')
print('rank/frequency (cipher codes vs it16 letters):')
itc=Counter(txt); tot=sum(itc.values())
for (c,n),(l,m) in zip(cnt.most_common(15),itc.most_common(15)): print(f'  {c:9s} {n:3d} {100*n/N:5.1f}%   |  {l} {100*m/tot:5.1f}%')
def sukhotin(s):
    syms=sorted(set(s)); idx={x:i for i,x in enumerate(syms)}; k=len(syms)
    M=[[0]*k for _ in range(k)]
    for a,b in zip(s,s[1:]):
        if a!=b: M[idx[a]][idx[b]]+=1; M[idx[b]][idx[a]]+=1
    rs=[sum(r) for r in M]; vowels=[]; cons=set(range(k))
    while True:
        best=max(cons,key=lambda i:rs[i]) if cons else None
        if best is None or rs[best]<=0: break
        vowels.append(best); cons.discard(best)
        for j in cons: rs[j]-=2*M[best][j]
    return [syms[i] for i in vowels]
V=set('aeiou')
hits=[];fp=[]
for _ in range(20):
    v=sukhotin(sample(N)); hits.append(len(set(v)&V)); fp.append(len(set(v)-V))
print(f'Sukhotin calibration on 20 it16 samples of N={N}: true vowels found mean {sum(hits)/20:.1f} of 5, false vowels mean {sum(fp)/20:.1f}')
v=sukhotin(seq); print('Sukhotin on the cipher (codes named vowel-like, in order):',v)
sh=Counter()
for _ in range(20):
    s2=seq[:]; random.shuffle(s2); sh.update(sukhotin(s2))
print('order-shuffled control, 20 runs: how often each code is named vowel-like:',sh.most_common(12))
