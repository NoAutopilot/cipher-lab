"""H37: design conformance as an arbiter. Design (H16, DECODE 958's stated style; H21 controls built so): each vowel
a e i o u has 3 codes, each other letter 1. Violation count V(key) = sum over letters of |codes - expected| on the glyphs
of the stream, counting only glyphs with >= 2 occurrences (a 1-occurrence glyph is as likely a misread as a code).
Rule: accept a candidate change iff it lowers V. Calibrated on h33/answers.json controls first (gate 0.8/0.8 on
changes to glyphs with >= 2 occurrences); target scored only if met."""
import json,csv
from collections import Counter
ans=json.load(open('h33/answers.json'))
CASES={'A':('h27/blind_seed1_n0.05.json','h27/ctl_seed1_n0.05.tsv'),'B':('h27/blind_seed2_n0.1.json','h27/ctl_seed2_n0.1.tsv'),
       'D':('h27/blind_seed3_n0.05.json','h27/ctl_seed3_n0.05.tsv'),'C':('target_marks_es17c7_seed2.json','../cipher_codes.tsv')}
def V(key,glyphs):
    c=Counter(key[g] for g in glyphs); letters=set(c)|set('aeiou')
    return sum(abs(c[l]-(3 if l in 'aeiou' else 1)) for l in letters)
def run(lab):
    j,t=CASES[lab]; key=json.load(open(j))['key']; seq=[r['sign'] for r in csv.DictReader(open(t),delimiter='\t')]
    cnt=Counter(seq); glyphs=[g for g in cnt if cnt[g]>=2]; v0=V(key,glyphs); rows=[]
    for kid,x,f,to,kind,n in ans[lab]:
        if n<2: continue
        k2=dict(key); k2[x]=to; rows.append((kid,x,f,to,kind,n,V(k2,glyphs)-v0))
    return v0,rows
tally={'true':[0,0],'decoy':[0,0]}; log=[]
for lab in 'ABD':
    v0,rows=run(lab); log.append(f'{lab}: blind-key violations {v0}')
    for r in rows:
        tally[r[4]][0]+=r[6]<0; tally[r[4]][1]+=1; log.append(f'  {r}')
ta=tally['true'][0]/tally['true'][1]; dr=1-tally['decoy'][0]/tally['decoy'][1]
print('\n'.join(log)); print(f'CONTROLS (n>=2): true-accept {ta:.2f} ({tally["true"][0]}/{tally["true"][1]}), decoy-reject {dr:.2f} ({tally["decoy"][1]-tally["decoy"][0]}/{tally["decoy"][1]})')
gate=ta>=0.8 and dr>=0.8; print('GATE','MET' if gate else 'NOT MET')
if gate:
    v0,rows=run('C'); print(f'C: blind-key violations {v0}')
    for r in rows: print(f'  {r} {"accept" if r[6]<0 else "reject"}')
