#!/usr/bin/env python3
"""BNF-G41 gate: decode fr.3983 f.178 digit passes with key no.41 alphabet; French 4-gram score vs shuffled keys.
Usage: gate_decode.py PASSFILE [--seeds 200]. Deterministic (seed 41)."""
import csv,sys,re,gzip,math,random,glob,collections
D='/home/user/cipher-lab/ciphers/fr3622-nevers-gondi-1594/'
def key():
    k={};nul=set()
    for r in csv.DictReader(open(D+'keys/key_no41_alphabet.tsv'),delimiter='\t'):
        for c in r['codes'].split():
            if r['letter']=='null': nul.add(c)
            else: k[c]=r['letter']
    return k,nul
def words():
    w=set()
    for p in 'AB':
        for r in csv.DictReader(open(D+f'keys/pass{p}.tsv'),delimiter='\t'):
            if r['table'].lower() in('alphabet','nulles'):continue
            for c in re.findall(r'\d+',r['code']):
                if len(c)==2: w.add(c)
    return w
def corpus():
    t=''
    for f in sorted(glob.glob('/home/user/cipher-lab/tools/data/fr16/*.gz')):
        t+=gzip.open(f,'rt',errors='ignore').read().lower()
    t=t.translate(str.maketrans('àâäéèêëîïôöùûüç','aaaeeeeiioouuuc'))
    return re.sub('[^a-z]','',t)
def lm(t,n=4):
    c=collections.Counter(t[i:i+n] for i in range(len(t)-n+1)); c3=collections.Counter(t[i:i+n-1] for i in range(len(t)-n+1))
    return c,c3
def score(s,c,c3,n=4):
    if len(s)<n:return -9
    v=0
    for i in range(len(s)-n+1):
        g=s[i:i+n];v+=math.log10((c[g]+0.1)/(c3[g[:-1]]+0.1*26))
    return v/(len(s)-n+1)
def dec(digs,k,nul,wd):
    n=len(digs);best=[(-1e9,None)]*(n+1);best[0]=(0,None)
    bk=[None]*(n+1)
    for i in range(n+1):
        if i==0:continue
    sc=[-1e9]*(n+1);sc[0]=0;bp=[None]*(n+1)
    for i in range(n):
        if sc[i]<-1e8:continue
        if sc[i]-1>sc[i+1]: pass
        if sc[i]-1>sc[i+1]: sc[i+1]=sc[i]-1;bp[i+1]=(i,'?')
        if i+2<=n:
            p=digs[i:i+2]
            g=1 if p in k else (0.3 if (p in nul or p in wd) else None)
            if g is not None and sc[i]+g>sc[i+2]:
                sc[i+2]=sc[i]+g;bp[i+2]=(i,p)
    out=[];j=n
    while j>0:
        i,p=bp[j];out.append(p);j=i
    return out[::-1]
def main():
    f=sys.argv[1];N=int(sys.argv[sys.argv.index('--seeds')+1]) if '--seeds' in sys.argv else 200
    k,nul=key();wd=words()
    rows=[(r['line'],r['segment'],re.sub(r'[~\s?]','',r['digits'])) for r in csv.DictReader(open(f),delimiter='\t')]
    # use s1 + non-overlapping s2: just score each segment separately
    segs=[d for _,_,d in rows if len(d)>=10]
    c,c3=lm(corpus())
    def total(keymap):
        s='';
        for d in segs:
            toks=dec(d,keymap,nul,wd); s+=''.join(keymap.get(t,'') for t in toks if t!='?')
            s+=''
        return s
    real=total(k);rs=score(real,c,c3)
    letters={}
    for code,l in k.items(): letters.setdefault(l,[]).append(code)
    random.seed(41);sh=[]
    codes=list(k);ls=[k[x] for x in codes]
    for _ in range(N):
        p=ls[:];random.shuffle(p);km=dict(zip(codes,p));sh.append(score(total(km),c,c3))
    sh.sort();p99=sh[int(.99*N)-1]
    print(f'{f}: letters {len(real)} real score {rs:.3f} shuffled mean {sum(sh)/N:.3f} p99 {p99:.3f} max {sh[-1]:.3f} rank {sum(1 for x in sh if x>=rs)}/{N}')
    print(real[:200])
main()
