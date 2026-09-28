"""H30 scorer: apply a reader's key changes (h30/reply_<X>.txt) and measure.
Controls: letter accuracy vs the clean .plain before/after, precision/recall of changes vs per-glyph majority truth.
Target: agreement of each change with key.tsv (M2's hand key)."""
import json,csv,sys
from collections import Counter,defaultdict
CASES={'A':('h27/blind_seed1_n0.05.json','h27/ctl_seed1_n0.05.tsv','h21/vowelctl_cartas13_seed1.tsv.plain'),
       'B':('h27/blind_seed2_n0.1.json','h27/ctl_seed2_n0.1.tsv','h21/vowelctl_cartas13_seed2.tsv.plain'),
       'C':('target_marks_es17c7_seed2.json','../cipher_codes.tsv',None),
       'D':('h27/blind_seed3_n0.05.json','h27/ctl_seed3_n0.05.tsv','h21/vowelctl_cartas13_seed3.tsv.plain')}
maps=json.load(open('h30/labelmaps.json'))
ref={r['code']:r['letter'] for r in csv.DictReader(open('../key.tsv'),delimiter='\t')}
def parse(lab):
    t=open(f'h30/reply_{lab}.txt').read(); b=t.split('BEGIN',1)[1].split('END',1)[0]
    out=[]
    for l in b.strip().splitlines():
        c=l.split('\t')
        if len(c)<4 or c[0].strip().lower()=='glyph': continue
        out.append((c[0].strip(),c[1].strip().lower(),c[2].strip().lower(),c[3].strip().lower()))
    return out
for lab in sys.argv[1:] or 'ABDC':
    j,t,p=CASES[lab]; d=json.load(open(j)); seq=[r['sign'] for r in csv.DictReader(open(t),delimiter='\t')]
    inv={v:k for k,v in maps[lab].items()}; key=dict(d['key']); ch=parse(lab)
    if p:
        plain=open(p).read().strip(); by=defaultdict(Counter)
        for x,q in zip(seq,plain): by[x][q]+=1
        truth={x:c.most_common(1)[0][0] for x,c in by.items()}
        wrong={x for x in by if key[x]!=truth[x]}
        acc=lambda k: sum(k[x]==q for x,q in zip(seq,plain))/len(seq)
        before=acc(key); ceil=acc(truth)
        for conf in ('high','high+medium','all'):
            ok={'high':('high',),'high+medium':('high','medium'),'all':('high','medium','low')}[conf]
            k2=dict(key); sel=[c for c in ch if c[3] in ok and c[0] in inv]
            for g,f,to,_ in sel: k2[inv[g]]=to
            right=sum(truth[inv[g]]==to for g,f,to,_ in sel)
            fixed=len({inv[g] for g,f,to,_ in sel if truth[inv[g]]==to} & wrong)
            print(f'{lab} {conf:12s} changes {len(sel):2d} right {right:2d} (prec {right/max(1,len(sel)):.2f}) wrong-glyphs fixed {fixed}/{len(wrong)} letters {before:.3f} -> {acc(k2):.3f} (ceiling {ceil:.3f})')
    else:
        print(f'{lab} target: blind glyphs differing from key.tsv: {sum(key[x]!=ref.get(x,key[x]) for x in key)}')
        for g,f,to,c in ch:
            x=inv.get(g,'?'); print(f'  {g}={x} {f}->{to} {c}: key.tsv {ref.get(x)} {"AGREE" if ref.get(x)==to else "differ"}')
        agree=sum(ref.get(inv.get(g))==to for g,f,to,c in ch)
        m2={x for x in key if x in ref and ref[x]!=key[x] and ref[x]!='_'}
        found={inv.get(g) for g,f,to,c in ch if ref.get(inv.get(g))==to}
        print(f'  reader changes {len(ch)}, agree with key.tsv {agree}; M2 changes recovered {len(found&m2)}/{len(m2)}')
