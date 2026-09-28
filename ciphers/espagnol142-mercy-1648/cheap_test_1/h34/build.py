"""H34 round 2: apply the H30 reader's key changes (h30/reply_X.txt) to each packet's key and rebuild the packet in
H30's format (same relabelling), so a fresh blind reader starts from the corrected decode."""
import json,csv,sys
from collections import Counter
sys.path.insert(0,'h30')
CASES={'A':('h27/blind_seed1_n0.05.json','h27/ctl_seed1_n0.05.tsv'),'B':('h27/blind_seed2_n0.1.json','h27/ctl_seed2_n0.1.tsv'),
       'C':('target_marks_es17c7_seed2.json','../cipher_codes.tsv'),'D':('h27/blind_seed3_n0.05.json','h27/ctl_seed3_n0.05.tsv')}
maps=json.load(open('h30/labelmaps.json')); INSTR=open('h30/instructions.txt').read()
keys={}
for lab,(j,t) in CASES.items():
    d=json.load(open(j)); seq=[r['sign'] for r in csv.DictReader(open(t),delimiter='\t')]; m=maps[lab]; inv={v:k for k,v in m.items()}
    key=dict(d['key']); b=open(f'h30/reply_{lab}.txt').read().split('BEGIN',1)[1].split('END',1)[0]
    for l in b.strip().splitlines():
        c=l.split('\t')
        if len(c)>=3 and c[0].strip() in inv: key[inv[c[0].strip()]]=c[2].strip().lower()
    keys[lab]=key; cnt=Counter(seq)
    out=[INSTR,'','KEY TABLE (glyph, current letter, occurrences):']
    for s in sorted(set(seq),key=lambda x:int(m[x][1:])): out.append(f'{m[s]}\t{key[s]}\t{cnt[s]}')
    out+=['','TEXT (each L line is the decode; the G line under it gives the glyph of each letter in order):']
    for i in range(0,len(seq),40):
        ch=seq[i:i+40]; out.append(f'L{i//40+1:02d}: '+''.join(key[x] for x in ch)); out.append(f'G{i//40+1:02d}: '+' '.join(m[x] for x in ch))
    open(f'h34/packet_{lab}.txt','w').write('\n'.join(out)+'\n')
json.dump(keys,open('h34/round1_keys.json','w'),indent=0)
