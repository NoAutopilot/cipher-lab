#!/usr/bin/env python3
"""H24 scorer: known-answer control for a plate-only shorthand reader (see PREREGISTRATION.md).
usage: score.py READER.tsv REF.txt [--seeds 200]   (READER.tsv columns: line, word, letters)
Prints S1 (aligned match rate), S2 (exact word skeletons), the 200-bijection null p95 of each, and PASS/FAIL."""
import sys,random,re,argparse
CONS='bdfghklmnprstvw'
def skel(w):
    w=w.lower(); w=w.replace('ph','f'); w=re.sub(r'[^a-z]','',w)
    w=w.replace('c','k').replace('q','k').replace('j','g').replace('z','s').replace('x','ks')
    w=re.sub(r'[aeiouy]','',w); w=re.sub(r'(.)\1+',r'\1',w); return w
def sw(a,b):
    n,m=len(a),len(b); best=0
    prev=[0]*(m+1); 
    for i in range(1,n+1):
        cur=[0]*(m+1)
        for j in range(1,m+1):
            d=prev[j-1]+(1 if a[i-1]==b[j-1] else -1)
            cur[j]=max(0,d,prev[j]-1,cur[j-1]-1)
            if cur[j]>best: best=cur[j]
        prev=cur
    return best
def scores(words,refwords,refstr):
    sk=[skel(w) for w in words]; s=''.join(sk)
    s1=sw(s,refstr)/max(1,len(s))
    s2=sum(1 for k in sk if len(k)>=2 and k in refwords)
    return s1,s2
def main():
    ap=argparse.ArgumentParser(); ap.add_argument('reader'); ap.add_argument('ref'); ap.add_argument('--seeds',type=int,default=200); ap.add_argument('--selftest',action='store_true')
    a=ap.parse_args()
    refs=[l.split(':',1)[-1] for l in open(a.ref) if l.strip()]
    words=[]
    for l in open(a.reader):
        p=l.rstrip('\n').split('\t')
        if len(p)<3 or p[0].startswith('#') or p[0]=='line': continue
        words.append(p[2])
    if a.selftest:
        random.seed(1); rw=refs[0].split()[:60]
        words=[ ''.join(random.choice('bdfghklmnprst') if random.random()<0.3 else ch for ch in w) for w in rw]
    best=None
    for ref in refs:
        refw=set(skel(w) for w in ref.split()); refstr=''.join(skel(w) for w in ref.split())
        s1,s2=scores(words,refw,refstr)
        rng=random.Random(20260928); n1=[];n2=[]
        for _ in range(a.seeds):
            perm=list(CONS); rng.shuffle(perm); tr=str.maketrans(CONS,''.join(perm))
            pw=[skel(w).translate(tr) for w in words]
            # translate after skel: feed skeletons through scores by wrapping
            s=''.join(pw); x1=sw(s,refstr)/max(1,len(s)); x2=sum(1 for k in pw if len(k)>=2 and k in refw)
            n1.append(x1); n2.append(x2)
        n1.sort(); n2.sort(); p1=n1[int(0.95*len(n1))-1]; p2=n2[int(0.95*len(n2))-1]
        res=(s1,s2,p1,p2,sum(x>=s1 for x in n1)/len(n1),sum(x>=s2 for x in n2)/len(n2))
        if best is None or res[0]>best[0]: best=res
    s1,s2,p1,p2,q1,q2=best
    verdict='PASS' if (s1>p1 and s2>=3 and s2>p2) else 'FAIL'
    print(f"reader_words={len(words)} S1={s1:.3f} null_p95={p1:.3f} p={q1:.3f} | S2={s2} null_p95={p2} p={q2:.3f} | {verdict}")
if __name__=='__main__' and not (len(sys.argv)>1 and sys.argv[1]=='--target'): main()

def target_mode(reader, skelfile, seeds=200):
    """T2: reader words (skeleton>=3) whose skeleton is an en18 word skeleton, vs the 200-bijection null."""
    S=set(open(skelfile).read().split())
    words=[l.split('\t')[2] for l in open(reader) if l.count('\t')>=2 and not l.startswith(('#','line'))]
    sk=[skel(w) for w in words]; t2=sum(1 for k in sk if len(k)>=3 and k in S)
    rng=random.Random(20260928); null=[]
    for _ in range(seeds):
        perm=list(CONS); rng.shuffle(perm); tr=str.maketrans(CONS,''.join(perm))
        null.append(sum(1 for k in sk if len(k)>=3 and k.translate(tr) in S))
    null.sort(); p95=null[int(0.95*seeds)-1]
    print(f"reader_words={len(words)} skel>=3={sum(1 for k in sk if len(k)>=3)} T2={t2} null_p95={p95} p={sum(x>=t2 for x in null)/seeds:.3f} | {'ABOVE NULL' if t2>p95 else 'INSIDE NULL'}")
if __name__=='__main__' and len(sys.argv)>1 and sys.argv[1]=='--target':
    target_mode(sys.argv[2], sys.argv[3])
