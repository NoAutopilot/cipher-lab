#!/usr/bin/env python3
"""VERIFY-SPINELLI-2 (28 Sept 2026): per-line letter agreement of the committed v6 decode with the 2017 Cipherbrain
reading of the same leaf (Norbert #7 for p1, Thomas #10 for p2; editorial [bracketed] insertions dropped, ?? dropped),
and the same statistic for 200 shuffled-value decodes (values permuted among the mapped codes, the runner's control).
u/v, i/j folded in the reference. Agreement = 1 - levenshtein(decode_letters, ref_letters)/len(ref), unread signs ('?') count as errors.
  python3 verify2/compare_2017.py [--shuffles 200] [--seed 5]"""
import os, sys, csv, random, argparse
H=os.path.dirname(os.path.abspath(__file__)); T=os.path.dirname(H)
ap=argparse.ArgumentParser(); ap.add_argument('--shuffles',type=int,default=200); ap.add_argument('--seed',type=int,default=5); a=ap.parse_args()
REF=['etliditechemadama','margeritanonvolearrettarelagu','bernationedispagniaetchepiu','dinclinationesimosraalconte',
     'palatinocheadaltri','arrivocaroneloettrovola','resolutionedicostoromiliore','diqueloelpapadomandava',
     'seebisognioelgubernatoredibressa','andaraisuieri']
REF=[r.replace('v','u').replace('j','i') for r in REF]  # one convention: u/v and i/j folded, as the decode is
rows=[l for l in open(os.path.join(T,'keys','key_domnina_2016_atlasmap_v6.tsv')).read().splitlines() if l.strip() and not l.startswith('#')]
M={r['code']:r['value'].strip().lower() for r in csv.DictReader(rows,delimiter='\t')}
lines=[l.split() for l in open(os.path.join(T,'passes','ciphertext_v6.txt')).read().splitlines() if l.strip()]
def lev(s,t):
    p=list(range(len(t)+1))
    for i,c in enumerate(s,1):
        q=[i]
        for j,d in enumerate(t,1): q.append(min(p[j]+1,q[j-1]+1,p[j-1]+(c!=d)))
        p=q
    return p[-1]
def dec(m):
    out=[]
    for l in lines:
        s=''
        for c in l:
            v=m.get(c,'?') or '?'
            if v=='null': continue
            s+= '?' if v=='?' else v
        out.append(s)
    return out
def score(d): return [1-lev(x.replace('que','que'),r)/len(r) for x,r in zip(d,REF)]
real=score(dec(M))
valued=[c for c,v in M.items() if v not in ('?','null','')]
rng=random.Random(a.seed); sh=[]
for _ in range(a.shuffles):
    vals=[M[c] for c in valued]; rng.shuffle(vals); m=dict(M); m.update(zip(valued,vals)); sh.append(score(dec(m)))
print('line\tdecode\tref_2017\tagree_real\tshuf_mean\tshuf_max\tshuf_ge_real')
for i,(d,r) in enumerate(zip(dec(M),REF)):
    col=[s[i] for s in sh]
    print(f'{i+1}\t{d}\t{r}\t{real[i]:.2f}\t{sum(col)/len(col):.2f}\t{max(col):.2f}\t{sum(c>=real[i] for c in col)}/{len(col)}')
tot=lambda s: 1-sum(lev(x,r) for x,r in zip(s,REF))/sum(map(len,REF))
rt=tot(dec(M)); 
shv=[]
rng=random.Random(a.seed)
for _ in range(a.shuffles):
    vals=[M[c] for c in valued]; rng.shuffle(vals); m=dict(M); m.update(zip(valued,vals)); shv.append(tot(dec(m)))
print(f'ALL\t\t\t{rt:.3f}\t{sum(shv)/len(shv):.3f}\t{max(shv):.3f}\t{sum(v>=rt for v in shv)}/{len(shv)}')
