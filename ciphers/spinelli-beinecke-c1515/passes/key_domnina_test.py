#!/usr/bin/env python3
"""H35 (28 Sept 2026): apply a code -> value map read from Domnina's key table to the v4 transcription and test it.

  python3 passes/key_domnina_test.py MAP.tsv [--shuffles 200] [--seed 7] [--show]

MAP.tsv: columns code, value, grade[, note]. value is a letter (a-z), a doubled letter (nn, ss ...), a syllable
(qua, que), 'null', or '?' (no key entry / undecided; the code stays unmapped). Several codes may share one value
(homophones). Input ciphertext: passes/ciphertext_v4.txt (one line per manuscript line, atlas codes).

Tests (CLAUDE.md rule 3, all against the same control -- the values permuted at random among the mapped codes, so
the control keeps the multiset of values and every code's frequency and varies only WHICH code gets which value):
  1. coverage: signs mapped to a value / to null / left unmapped;
  2. mean log unigram probability of the mapped letters under tools/data/it16 (v->u, j->i), as in H4;
  3. mean log bigram probability over adjacent mapped letters (nulls removed first; an unmapped sign breaks the
     chain), add-one smoothed on the same corpus -- the unigram test cannot see order, this one can;
  4. the known phrase (Tomokiyo, Jan 2024: "la gubernation d'ispagnia") searched in the decoded letter, nulls removed,
     as the best window by edit distance with unmapped signs as wildcards; reported as (distance, position, the
     window) for the real map and the distribution of the best distance under the shuffled maps.
Prints everything; with --show also prints the decoded lines. Never writes a reading: a result under the shuffled
p05 on tests 2-3 and a phrase window well inside the shuffled distribution's tail is "worth the orchestrator's look",
not a reading (rule 10).
"""
import sys, os, csv, glob, math, random, argparse
from collections import Counter
HERE=os.path.dirname(os.path.abspath(__file__)); T=os.path.dirname(HERE); REPO=os.path.dirname(os.path.dirname(T))
ap=argparse.ArgumentParser(); ap.add_argument('map'); ap.add_argument('--shuffles',type=int,default=200)
ap.add_argument('--seed',type=int,default=7); ap.add_argument('--show',action='store_true')
ap.add_argument('--phrase',default="la gubernation d'ispagnia"); ap.add_argument('--cipher',default='ciphertext_v4.txt'); a=ap.parse_args()
MAP={}
_rows=[l for l in open(a.map).read().splitlines() if l.strip() and not l.startswith('#')]
for r in csv.DictReader(_rows,delimiter='\t'):
    MAP[r['code'].strip()]=r['value'].strip().lower()
lines=[l.split() for l in open(os.path.join(HERE,a.cipher) if not os.path.isabs(a.cipher) else a.cipher).read().splitlines() if l.strip()]
codes=[c for l in lines for c in l]; cnt=Counter(codes)
def val(c,m): 
    v=m.get(c,'?'); return v if v else '?'
mapped_codes=[c for c in cnt if MAP.get(c) not in (None,'','?','null')]
nmap=sum(cnt[c] for c in mapped_codes); nnull=sum(cnt[c] for c in cnt if MAP.get(c)=='null'); nun=len(codes)-nmap-nnull
print(f'signs {len(codes)}: mapped to a value {nmap} ({nmap/len(codes):.0%}), null {nnull} ({nnull/len(codes):.0%}), unmapped {nun} ({nun/len(codes):.0%})')
# corpus
txt=''
for p in glob.glob(os.path.join(REPO,'tools','data','it16','*.txt')): txt+=open(p,encoding='utf-8',errors='ignore').read().lower()
txt=txt.replace('v','u').replace('j','i'); letters=[ch for ch in txt if 'a'<=ch<='z']
uni=Counter(letters); N=sum(uni.values()); A='abcdefghijklmnopqrstuvwxyz'
logp={ch:math.log((uni[ch]+1)/(N+26)) for ch in A}
bi=Counter(zip(letters,letters[1:])); 
def logb(x,y): return math.log((bi[(x,y)]+1)/(uni[x]+26))
def decode(m):
    out=[]
    for l in lines:
        s=[]
        for c in l:
            v=val(c,m)
            if v=='null': continue
            s.append(v)
        out.append(s)
    return out
def scores(m):
    dec=decode(m); u=[];b=[]
    for s in dec:
        prev=None
        for v in s:
            if v=='?': prev=None; continue
            for ch in v:
                if ch not in logp: prev=None; continue
                u.append(logp[ch])
                if prev: b.append(logb(prev,ch))
                prev=ch
    return (sum(u)/len(u) if u else float('nan'), sum(b)/len(b) if b else float('nan'))
def flat(m):
    return ''.join(v if v!='?' else '?' for s in decode(m) for v in s)
def best_window(text,phrase):
    P=phrase.lower().replace("'",'').replace(' ','').replace('v','u'); n=len(P); best=(10**9,-1,'')
    for i in range(0,max(1,len(text)-n//2)):
        for L in (n-2,n-1,n,n+1,n+2):
            w=text[i:i+L]
            if len(w)<n-2: continue
            # edit distance with '?' wildcard
            prev=list(range(len(w)+1))
            for j,pc in enumerate(P,1):
                cur=[j]
                for k,wc in enumerate(w,1):
                    cost=0 if (wc=='?' or wc==pc) else 1
                    cur.append(min(prev[k]+1,cur[k-1]+1,prev[k-1]+cost))
                prev=cur
            d=prev[-1]
            if d<best[0]: best=(d,i,w)
    return best
su,sb=scores(MAP); text=flat(MAP); bw=best_window(text,a.phrase)
print(f'REAL map: mean log unigram {su:.3f} | mean log bigram {sb:.3f} | phrase best window: distance {bw[0]} at {bw[1]}: {bw[2]}')
random.seed(a.seed); vals=[MAP[c] for c in mapped_codes]; SU=[];SB=[];BD=[]
for _ in range(a.shuffles):
    perm=vals[:]; random.shuffle(perm); m=dict(MAP); m.update(dict(zip(mapped_codes,perm)))
    x,y=scores(m); SU.append(x); SB.append(y); BD.append(best_window(flat(m),a.phrase)[0])
def summ(v,real,hi_good=True):
    v2=sorted(v); mu=sum(v)/len(v); sd=(sum((x-mu)**2 for x in v)/len(v))**.5
    p95=v2[int(0.95*len(v))-1]; p05=v2[int(0.05*len(v))]
    ge=sum(1 for x in v if (x>=real if hi_good else x<=real))
    return f'shuffled mean {mu:.3f} sd {sd:.3f} p05 {p05:.3f} p95 {p95:.3f} | shuffles at or beyond real: {ge}/{len(v)}'
print('unigram:', summ(SU,su)); print('bigram :', summ(SB,sb)); print('phrase distance:', summ(BD,bw[0],hi_good=False))
if a.show:
    for i,s in enumerate(decode(MAP),1): print(f'L{i:02d}: '+' '.join(s))
