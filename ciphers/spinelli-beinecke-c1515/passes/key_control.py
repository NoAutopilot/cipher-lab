#!/usr/bin/env python3
"""H4: apply the key on disk (Tomokiyo's reconstruction, keys/key_spinelli_c1515.tsv) to the atlas-coded transcription
and test it against a shuffled-key control (CLAUDE.md rule 3).

Inputs: passes/p1_reconciled.tsv (atlas v3 codes) and passes/p2_reconciled.tsv (atlas v2 codes, mapped to v3 here).
Output: passes/letter_codes_v3.tsv (the whole letter, one v3 code per row, both pages), passes/key_atlas_asread.tsv
(the code -> key value map used, grade M throughout: the map rests on matching the key image's shapes to the atlas
codes by eye, never on a calibration), and the control result printed.

Test: under the key-as-read map, the mapped positions become letters; their fit to 16th-century Italian is the mean
log unigram probability under tools/data/it16 (v->u, j->i, the key's own alphabet). Control: the same letter labels
permuted at random among the same mapped codes (200 shuffles), so the control keeps the multiset of letters and the
code frequencies and varies only WHICH code gets which letter -- the axis the key claims to fix. Reported: the real
map's score, the shuffle mean/sd/p95, and the letter profile against the corpus.
"""
import csv, os, random, math, glob, re
from collections import Counter
HERE=os.path.dirname(os.path.abspath(__file__)); T=os.path.dirname(HERE); REPO=os.path.dirname(os.path.dirname(T))
V2TOV3={'ELOOP':'HOOK','ECAP':'HOOK','RHO':'HOOK','TLOOP':'HOOK','UCURL':'HOOK','MU':'HOOK','LONGS':'HOOK','AMP':'HOOK',
        'SEVENB':'SEVEN','CARET':'SEVEN','TWOFLAT':'TWO','DEE':'TWO','OMEGA2':'OMEGABAR','STROKE':'_','EX':'XCURL','CHOOK':'HOOK','RSTROKE':'HOOK','CBOLD':'HOOK','ENARCH':'EM'}
rows=[]
for fn,page in (('p1_reconciled.tsv','p1'),('p2_reconciled.tsv','p2')):
    for r in csv.DictReader(open(os.path.join(HERE,fn)),delimiter='\t'):
        if r['code']=='_': continue
        c=V2TOV3.get(r['code'],r['code']) if page=='p2' else r['code']
        rows.append((page,r['line'],r['pos'],c,r['grade']))
with open(os.path.join(HERE,'letter_codes_v3.tsv'),'w') as f:
    f.write('page\tline\tpos\tcode\tgrade\n')
    for r in rows: f.write('\t'.join(r)+'\n')
codes=[r[3] for r in rows]; cnt=Counter(codes)
print('signs',len(codes),'| code counts:',cnt.most_common())
# key as read: atlas code -> key value (letters), 'null', or None (no key entry / ambiguous family)
KEY={'SEVEN':'o','NINE':'p','FOUR':'c','SIX':'n','THREE':'d','PHI':'a','TEE':'b','CIRCLE':'e','ESS':'s',
     'OMEGABAR':'null','PI':'null','EIGHT':'null','EM':'null','EREV':'null',
     'HOOK':None,'TWO':None,'XCURL':None,'DIAMOND':None,'THETA':None,'ENN':None,'HCURL':None,'LL':None,'EIGHTBAR':None,'OMEGADOT':None,'PLUS':None}
with open(os.path.join(HERE,'key_atlas_asread.tsv'),'w') as f:
    f.write('code\tvalue\tgrade\tnote\n')
    for c,n in cnt.most_common():
        v=KEY.get(c); f.write(f"{c}\t{v if v else '?'}\tM\tkey image shape matched to the atlas code by eye; {n} occurrences\n")
mapped=[(c,KEY[c]) for c in codes if KEY.get(c) not in (None,'null')]
nulls=sum(1 for c in codes if KEY.get(c)=='null'); unmapped=sum(1 for c in codes if KEY.get(c) is None)
print(f'mapped to letters {len(mapped)} ({len(mapped)/len(codes):.0%}); nulls {nulls} ({nulls/len(codes):.0%}); no key entry {unmapped} ({unmapped/len(codes):.0%})')
# corpus unigrams
txt=''
for p in glob.glob(os.path.join(REPO,'tools','data','it16','*.txt')): txt+=open(p,encoding='utf-8',errors='ignore').read().lower()
txt=txt.replace('v','u').replace('j','i')
uni=Counter(ch for ch in txt if 'a'<=ch<='z'); N=sum(uni.values())
logp={ch:math.log((uni[ch]+1)/(N+26)) for ch in 'abcdefghijklmnopqrstuvwxyz'}
def score(assign):  # assign: code -> letter
    L=[assign[c] for c,_ in mapped]; return sum(logp[l] for l in L)/len(L)
real={c:v for c,v in KEY.items() if v and v!='null'}
s_real=score(real)
letters=list(real.values()); mcodes=list(real.keys())
random.seed(7); sh=[]
for _ in range(200):
    perm=letters[:]; random.shuffle(perm); sh.append(score(dict(zip(mcodes,perm))))
mu=sum(sh)/len(sh); sd=(sum((x-mu)**2 for x in sh)/len(sh))**.5; p95=sorted(sh)[int(0.95*len(sh))]
better=sum(1 for x in sh if x>=s_real)
print(f'mean log unigram p (it16), mapped positions only: REAL key-as-read {s_real:.3f} | shuffled-key mean {mu:.3f} sd {sd:.3f} p95 {p95:.3f} | shuffles >= real: {better}/200')
print('letter profile under the key-as-read (mapped positions) vs it16 corpus:')
obs=Counter(v for _,v in mapped); m=len(mapped)
for l,n in obs.most_common(): print(f'  {l}: {n:3d} {100*n/m:5.1f}%   it16 {100*uni[l]/N:5.1f}%')
