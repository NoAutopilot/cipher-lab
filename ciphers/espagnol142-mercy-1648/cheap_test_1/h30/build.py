"""H30: build blind reader packets (relabelled signs) for 3 corrupted controls + the target."""
import json,csv,random
from collections import Counter
CASES=[('A','h27/blind_seed1_n0.05.json','h27/ctl_seed1_n0.05.tsv'),
       ('B','h27/blind_seed2_n0.1.json','h27/ctl_seed2_n0.1.tsv'),
       ('C','target_marks_es17c7_seed2.json','../cipher_codes.tsv'),
       ('D','h27/blind_seed3_n0.05.json','h27/ctl_seed3_n0.05.tsv')]
INSTR=open('h30/instructions.txt').read()
maps={}
for lab,j,t in CASES:
    d=json.load(open(j)); seq=[r['sign'] for r in csv.DictReader(open(t),delimiter='\t')]
    assert ''.join(d['key'][x] for x in seq)==d['decoded']
    rng=random.Random(30+ord(lab)); signs=sorted(set(seq)); lbl=list(range(10,10+len(signs))); rng.shuffle(lbl)
    m={s:'g%d'%l for s,l in zip(signs,lbl)}; maps[lab]=m
    cnt=Counter(seq)
    out=[INSTR,'','KEY TABLE (glyph, current letter, occurrences):']
    for s in sorted(signs,key=lambda x:int(m[x][1:])): out.append(f'{m[s]}\t{d["key"][s]}\t{cnt[s]}')
    out.append(''); out.append('TEXT (each L line is the decode; the G line under it gives the glyph of each letter in order):')
    for i in range(0,len(seq),40):
        ch=seq[i:i+40]; out.append(f'L{i//40+1:02d}: '+''.join(d['key'][x] for x in ch)); out.append(f'G{i//40+1:02d}: '+' '.join(m[x] for x in ch))
    open(f'h30/packet_{lab}.txt','w').write('\n'.join(out)+'\n')
json.dump(maps,open('h30/labelmaps.json','w'),indent=0)
