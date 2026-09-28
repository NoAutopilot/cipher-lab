#!/usr/bin/env python3
"""H38 (28 Sept 2026): split the atlas codes Domnina's key separates, from two blind Opus sorting passes.

  python3 passes/build_v5_split.py passes/split_passM.tsv passes/split_passN.tsv

Inputs: the two passes (code, label, cell, conf, why; label = page.Lline.bbox) over every v4 sign of SEVEN, NINE,
EIGHT, TWO, HOOK, sorted among Domnina's candidate cells. Rule: both passes name the same cell -> the sign's code
becomes CODE_CELL (e.g. SEVEN_I) at grade AB; otherwise (disagreement, or either UNCLEAR) the sign keeps its lumped
code (value stays '?', as in v4). Writes passes/letter_codes_v5.tsv, passes/ciphertext_v5.txt,
keys/key_domnina_2016_atlasmap_v5.tsv (the H35 map plus one row per sub-code, value = the cell's plaintext), and
prints the agreement per code. Nothing here looks at the crib or the letter frequencies: shape sort only.
"""
import csv, os, sys
from collections import Counter, defaultdict
HERE=os.path.dirname(os.path.abspath(__file__)); T=os.path.dirname(HERE)
A,B=sys.argv[1],sys.argv[2]
def load(p):
    d={}
    for r in csv.DictReader(open(p),delimiter='\t'):
        d[(r['code'].strip(),r['label'].strip())]=r['cell'].strip().upper().replace('U/V','U_V')
    return d
a,b=load(A),load(B)
CELLVAL={'E':'e','I':'i','NULLA':'null','O':'o','R':'r','CC':'cc','RR':'rr','P':'p','Z':'z','T':'t','C':'c','M':'m','G':'g','FF':'ff','U_V':'u','H':'h','A':'a'}
agree={}; stats=defaultdict(Counter)
for k in sorted(set(a)|set(b)):
    x,y=a.get(k,'?'),b.get(k,'?'); code=k[0]
    if x==y and x not in ('UNCLEAR','?'): agree[k]=x; stats[code]['agree '+x]+=1
    else: stats[code]['keep']+=1
for code,c in stats.items():
    n=sum(c.values()); ag=n-c['keep']; print(f'{code}: {ag}/{n} agreed -> '+', '.join(f'{k[6:]} {v}' for k,v in sorted(c.items()) if k!='keep'))
# rebuild codes
box={}
for fn,page in (('p1_reconciled_v4.tsv','p1'),('p2_reconciled_v4.tsv','p2')):
    for r in csv.DictReader(open(os.path.join(HERE,fn)),delimiter='\t'): box[(page,r['line'],r['pos'])]=r['box']
rows=list(csv.DictReader(open(os.path.join(HERE,'letter_codes_v4.tsv')),delimiter='\t'))
out=[]; changed=0
for r in rows:
    lab=f'{r["page"]}.L{r["line"]}.b{box[(r["page"],r["line"],r["pos"])]}'
    k=(r['code'],lab); code=r['code']; grade=r['grade']
    if k in agree: code=f'{r["code"]}_{agree[k]}'; grade='AB'; changed+=1
    out.append((r['page'],r['line'],r['pos'],code,grade))
with open(os.path.join(HERE,'letter_codes_v5.tsv'),'w') as f:
    f.write('page\tline\tpos\tcode\tgrade\n')
    for o in out: f.write('\t'.join(o)+'\n')
lines=defaultdict(list)
for o in out: lines[(o[0],int(o[1]))].append(o[3])
with open(os.path.join(HERE,'ciphertext_v5.txt'),'w') as f:
    for k in sorted(lines): f.write(' '.join(lines[k])+'\n')
src=open(os.path.join(T,'keys','key_domnina_2016_atlasmap.tsv')).read().rstrip('\n')
extra=['# v5 sub-codes (H38): CODE_CELL rows written by passes/build_v5_split.py from two blind sorting passes; grade AB = both passes named the cell']
for sub in sorted(set(f'{k[0]}_{v}' for k,v in agree.items())):
    cell=sub.split('_',1)[1]; extra.append(f'{sub}\t{CELLVAL[cell]}\tAB\tH38 shape sort, both passes')
open(os.path.join(T,'keys','key_domnina_2016_atlasmap_v5.tsv'),'w').write(src+'\n'+'\n'.join(extra)+'\n')
print(f'{changed} of {len(rows)} signs re-coded; files written')
