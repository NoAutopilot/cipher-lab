#!/usr/bin/env python3
"""H40 (28 Sept 2026): second shape split -- PHI (G vs I vs T) and the residue signs -- from two blind sorting passes.

  python3 passes/build_v6_split.py passes/split2_passO.tsv passes/split2_passP.tsv

Rule as in build_v5_split.py: both passes name the same candidate -> the sign's code becomes CODE_CAND at AB (PHI_G,
PHI_I, HOOK_T3 ...); otherwise it keeps its v5 code. Writes passes/letter_codes_v6.tsv, passes/ciphertext_v6.txt and
keys/key_domnina_2016_atlasmap_v6.tsv (the v5 map plus one row per new sub-code; PHI's own row becomes '?' since its
signs are now split). Shape sort only -- no crib, no frequencies.
"""
import csv, os, sys
from collections import Counter, defaultdict
HERE=os.path.dirname(os.path.abspath(__file__)); T=os.path.dirname(HERE)
A,B=sys.argv[1],sys.argv[2]
def load(p):
    d={}
    for r in csv.DictReader(open(p),delimiter='\t'):
        lab=r['label'].strip().split(' [')[0]; d[lab]=r['cell'].strip().upper().replace('/','_')
    return d
a,b=load(A),load(B)
VAL={'G':'g','I':'i','T':'t','A':'a','H':'h','C':'c','T1':'t','T2':'t','T3':'t','M1':'m','M2':'m','G3':'g','R2':'r','FF':'ff','U_V2':'u',
     'E1':'e','E2':'e','I2':'i','O1':'o','O2':'o','P1':'p','P2':'p','F1':'f','F2':'f','Z':'z','NULLA4':'null','NULLA6':'null','NULLAZ':'null','NULLA9':'null','QUE':'que','QUA':'qua','S2':'s'}
box={}
for fn,page in (('p1_reconciled_v4.tsv','p1'),('p2_reconciled_v4.tsv','p2')):
    for r in csv.DictReader(open(os.path.join(HERE,fn)),delimiter='\t'): box[(page,r['line'],r['pos'])]=r['box']
rows=list(csv.DictReader(open(os.path.join(HERE,'letter_codes_v5.tsv')),delimiter='\t'))
out=[]; stats=defaultdict(Counter); newsubs=set()
for r in rows:
    lab=f'{r["page"]}.L{r["line"]}.b{box[(r["page"],r["line"],r["pos"])]}'; code=r['code']; grade=r['grade']
    if lab in a or lab in b:
        x,y=a.get(lab,'?'),b.get(lab,'?')
        if x==y and x in VAL:
            code=f'{r["code"]}_{x}'; grade='AB'; stats[r['code']]['agree '+x]+=1; newsubs.add((code,VAL[x]))
        else: stats[r['code']]['keep']+=1
    out.append((r['page'],r['line'],r['pos'],code,grade))
for c,s in stats.items():
    n=sum(s.values()); print(f'{c}: {n-s["keep"]}/{n} agreed -> '+', '.join(f'{k[6:]} {v}' for k,v in sorted(s.items()) if k!='keep'))
with open(os.path.join(HERE,'letter_codes_v6.tsv'),'w') as f:
    f.write('page\tline\tpos\tcode\tgrade\n')
    for o in out: f.write('\t'.join(o)+'\n')
lines=defaultdict(list)
for o in out: lines[(o[0],int(o[1]))].append(o[3])
with open(os.path.join(HERE,'ciphertext_v6.txt'),'w') as f:
    for k in sorted(lines): f.write(' '.join(lines[k])+'\n')
src=[l for l in open(os.path.join(T,'keys','key_domnina_2016_atlasmap_v5.tsv')).read().splitlines()]
src=['PHI\t?\t?\tsplit in v6 (H40): PHI_G / PHI_I / PHI_T carry the values' if l.startswith('PHI\t') else l for l in src]
src.append('# v6 sub-codes (H40): from two blind sorting passes over PHI and the residue, passes/build_v6_split.py')
for code,v in sorted(newsubs): src.append(f'{code}\t{v}\tAB\tH40 shape sort, both passes')
open(os.path.join(T,'keys','key_domnina_2016_atlasmap_v6.tsv'),'w').write('\n'.join(src)+'\n')
print(f'{len(newsubs)} new sub-codes; files written')
