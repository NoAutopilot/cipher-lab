#!/usr/bin/env python3
"""H41 (28 Sept 2026): re-read the five unread cipher lines against Domnina's key cells as the alphabet.

  python3 passes/build_v7_lines.py passes/h41_passQ.tsv passes/h41_passR.tsv

Inputs: two blind passes (line p1_L01.., box, reading = key sign name(s) such as A1, E2, Nulla4, T3, CC, or X+Y for two
signs in one box, FRAG, MARK; conf; why). Rule: both passes give the same reading -> the box's token(s) become
KEY_<name> at grade AB (value = the cell's plaintext, nulls for Nulla*); FRAG/MARK agreed -> the box is dropped; any
disagreement -> the box keeps its v6 code (and its v6 grade), or is dropped if v6 had no token there. Other lines are
copied from v6 unchanged. Writes passes/letter_codes_v7.tsv, passes/ciphertext_v7.txt, keys/key_domnina_2016_atlasmap_v7.tsv
(v6 map plus KEY_* rows) and prints agreement per line. Shape sort only: no crib, no frequencies.
"""
import csv, os, sys, re
from collections import defaultdict, Counter
HERE=os.path.dirname(os.path.abspath(__file__)); T=os.path.dirname(HERE)
A,B=sys.argv[1],sys.argv[2]
LINES={'p1_L01':('p1','1'),'p1_L02':('p1','2'),'p1_L05':('p1','5'),'p1_L06':('p1','6'),'p2_L02':('p2','2')}
def val(name):
    n=name.upper()
    if n.startswith('NULLA'): return 'null'
    m=re.match(r'^(CC|FF|NN|PP|RR|SS|TT|QUA|QUE)$',n)
    if m: return n.lower()
    m=re.match(r'^([A-Z])(\d?)$',n) or re.match(r'^(U/?V)(\d?)$',n)
    if m: return 'u' if m.group(1).startswith('U') else m.group(1).lower()
    return None
def load(p):
    d={}
    for r in csv.DictReader(open(p),delimiter='\t'):
        d[(r['line'].strip(),r['box'].strip())]=r['reading'].strip().upper().replace(' ','')
    return d
a,b=load(A),load(B)
box={}
for fn,page in (('p1_reconciled_v4.tsv','p1'),('p2_reconciled_v4.tsv','p2')):
    for r in csv.DictReader(open(os.path.join(HERE,fn)),delimiter='\t'): box[(page,r['line'],r['pos'])]=r['box']
v6=list(csv.DictReader(open(os.path.join(HERE,'letter_codes_v6.tsv')),delimiter='\t'))
v6by={}
for r in v6: v6by[(r['page'],r['line'],box[(r['page'],r['line'],r['pos'])])]=r
out=[]; stats=defaultdict(Counter); newkeys={}
done_lines=set()
for r in v6:
    if (r['page'],r['line']) in [v for v in LINES.values()]: continue
    out.append((r['page'],r['line'],int(r['pos']),r['code'],r['grade']))
for ln,(page,line) in LINES.items():
    boxes=sorted({int(k[1]) for k in list(a)+list(b) if k[0]==ln})
    pos=0
    for bx in boxes:
        x,y=a.get((ln,str(bx)),'?'),b.get((ln,str(bx)),'?')
        prev=v6by.get((page,line,str(bx)))
        if x==y and x not in ('?',''):
            if x in ('FRAG','MARK'): stats[ln]['agree drop']+=1; continue
            parts=x.split('+'); ok=all(val(p) for p in parts)
            if ok:
                for p in parts:
                    pos+=1; code='KEY_'+p; newkeys[code]=val(p); out.append((page,line,pos,code,'AB'))
                stats[ln]['agree sign']+=1; continue
        stats[ln]['keep v6' if prev else 'disagree, no v6 token']+=1
        if prev: pos+=1; out.append((page,line,pos,prev['code'],prev['grade']))
for ln,c in stats.items(): print(ln, dict(c))
out.sort(key=lambda o:(o[0],int(o[1]),o[2]))
with open(os.path.join(HERE,'letter_codes_v7.tsv'),'w') as f:
    f.write('page\tline\tpos\tcode\tgrade\n')
    for o in out: f.write(f'{o[0]}\t{o[1]}\t{o[2]}\t{o[3]}\t{o[4]}\n')
lines=defaultdict(list)
for o in out: lines[(o[0],int(o[1]))].append(o[3])
with open(os.path.join(HERE,'ciphertext_v7.txt'),'w') as f:
    for k in sorted(lines): f.write(' '.join(lines[k])+'\n')
src=open(os.path.join(T,'keys','key_domnina_2016_atlasmap_v6.tsv')).read().rstrip('\n').splitlines()
src.append('# v7 KEY_* codes (H41): boxes of the five re-read lines named directly as Domnina cells by both blind passes, passes/build_v7_lines.py')
for code,v in sorted(newkeys.items()): src.append(f'{code}\t{v}\tAB\tH41 both passes')
open(os.path.join(T,'keys','key_domnina_2016_atlasmap_v7.tsv'),'w').write('\n'.join(src)+'\n')
print(f'{len(out)} tokens in v7; {len(newkeys)} KEY_* codes')
