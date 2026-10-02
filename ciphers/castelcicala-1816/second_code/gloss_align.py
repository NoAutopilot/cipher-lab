# Gloss-anchor recurrence check for the second code (R9586/R9588), NEXT-CAS 2 Oct 2026.
# Usage: python3 gloss_align.py "207 188" "1043 224" ... -- prints frequencies, the 9 pencil-gloss lines,
# and for each n-gram its count in original order vs 1000 within-record shuffles (seed 1).
import re,random,collections,sys
import os; D=os.path.join(os.path.dirname(os.path.abspath(__file__)),'')
recs={}
for r in ('R9586','R9588'):
    lines=open(D+r+'.txt').read().splitlines()
    toks=[];glosses=[]
    for i,l in enumerate(lines):
        if l.startswith('P:'): glosses.append((r,i,l,lines[i-1],lines[i+1] if i+1<len(lines) else ''))
        if l.startswith(('#','P:','C:')) or not l.strip(): continue
        toks+= [t.rstrip('^+') for t in l.split()]
    recs[r]=(toks,glosses)
allt=[t for r in recs for t in recs[r][0]]
print('tokens',len(allt),{r:len(recs[r][0]) for r in recs})
f=collections.Counter(allt)
print('top',f.most_common(15))
for r in recs:
    for g in recs[r][1]: print(g[0],'line',g[1],'|',g[2],'| above:',g[3],'| below:',g[4])
def ng(seq,n): return collections.Counter(tuple(seq[i:i+n]) for i in range(len(seq)-n+1))
def count(pat):
    n=len(pat);return sum(ng(recs[r][0],n)[tuple(pat)] for r in recs)
pats=[x.split() for x in sys.argv[1:]]
random.seed(1);R=1000
for p in pats:
    obs=count(p);sh=[]
    for _ in range(R):
        c=0
        for r in recs:
            s=recs[r][0][:];random.shuffle(s);c+=ng(s,len(p))[tuple(p)]
        sh.append(c)
    sh.sort();m=sum(sh)/R;p95=sh[int(.95*R)];pge=sum(1 for x in sh if x>=obs)/R
    ctx=[]
    for r in recs:
        s=recs[r][0]
        for i in range(len(s)-len(p)+1):
            if s[i:i+len(p)]==p: ctx.append(r[-2:]+':'+' '.join(s[max(0,i-2):i])+' ['+' '.join(p)+'] '+' '.join(s[i+len(p):i+len(p)+2]))
    print(' '.join(p),'freq',[f[x] for x in p],'obs',obs,'shuf mean %.2f p95 %d P(>=obs) %.3f'%(m,p95,pge),'|',' ; '.join(ctx))
