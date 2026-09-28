"""H34: cumulative recall/precision after round 2 (h34/reply_X.txt applied on top of round1_keys.json)."""
import json,csv,sys
from collections import Counter,defaultdict
CASES={'A':('h27/ctl_seed1_n0.05.tsv','h21/vowelctl_cartas13_seed1.tsv.plain','h27/blind_seed1_n0.05.json'),
       'B':('h27/ctl_seed2_n0.1.tsv','h21/vowelctl_cartas13_seed2.tsv.plain','h27/blind_seed2_n0.1.json'),
       'D':('h27/ctl_seed3_n0.05.tsv','h21/vowelctl_cartas13_seed3.tsv.plain','h27/blind_seed3_n0.05.json')}
maps=json.load(open('h30/labelmaps.json')); r1=json.load(open('h34/round1_keys.json'))
for lab in sys.argv[1:]:
    t,p,j=CASES[lab]; seq=[r['sign'] for r in csv.DictReader(open(t),delimiter='\t')]; plain=open(p).read().strip()
    blind=json.load(open(j))['key']; inv={v:k for k,v in maps[lab].items()}
    by=defaultdict(Counter)
    for x,q in zip(seq,plain): by[x][q]+=1
    truth={x:c.most_common(1)[0][0] for x,c in by.items()}; wrong={x for x in by if blind[x]!=truth[x]}
    k2=dict(r1[lab]); ch=[]
    b=open(f'h34/reply_{lab}.txt').read().split('BEGIN',1)[1].split('END',1)[0]
    for l in b.strip().splitlines():
        c=[z.strip() for z in l.split('\t')]
        if len(c)>=3 and c[0] in inv: ch.append((inv[c[0]],c[1].lower(),c[2].lower(),c[3].lower() if len(c)>3 else '')); k2[inv[c[0]]]=c[2].lower()
    acc=lambda k: sum(k[x]==q for x,q in zip(seq,plain))/len(seq)
    right=sum(truth[x]==to for x,f,to,cf in ch)
    print(f'{lab} round2 changes {len(ch)} right {right}; wrong glyphs fixed blind->r1->r2: {len([x for x in wrong if r1[lab][x]==truth[x]])} -> {len([x for x in wrong if k2[x]==truth[x]])} of {len(wrong)}; newly broken {len([x for x in by if blind[x]==truth[x] and k2[x]!=truth[x]])}; letters {acc(blind):.3f} -> {acc(r1[lab]):.3f} -> {acc(k2):.3f}')
    for x,f,to,cf in ch: print(f'    {maps[lab][x]}={x} {f}->{to} {cf} truth {truth[x]}')
