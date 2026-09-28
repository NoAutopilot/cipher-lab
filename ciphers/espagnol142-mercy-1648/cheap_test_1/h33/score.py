"""H33 scorer: reply_<X>.txt verdicts vs answers.json; per-class accept rates, overall and for glyphs with >=2 occurrences."""
import json,sys
A=json.load(open('h33/answers.json'))
def parse(lab):
    t=open(f'h33/reply_{lab}.txt').read(); b=t.split('BEGIN',1)[1].split('END',1)[0]; v={}
    for l in b.strip().splitlines():
        c=[x.strip() for x in l.split('\t')]
        if len(c)>=2 and c[0].startswith('K'): v[c[0]]=(c[1].lower(),c[2].lower() if len(c)>2 else '')
    return v
tot={'true':[0,0],'decoy':[0,0]}
for lab in sys.argv[1:]:
    v=parse(lab); r={'true':[0,0],'decoy':[0,0]}; r2={'true':[0,0],'decoy':[0,0]}; rows=[]
    for kid,x,f,to,kind,n in A[lab]:
        acc=v.get(kid,('missing',''))[0].startswith('accept')
        r[kind][0]+=acc; r[kind][1]+=1
        if n>=2: r2[kind][0]+=acc; r2[kind][1]+=1
        rows.append(f'  {kid} {x} {f}->{to} n={n} {kind:5s} {v.get(kid,("missing",""))}')
    if lab=='C':
        print('C (target: "true" = M2 key.tsv corrections)'); print('\n'.join(rows))
    else:
        for k in tot: tot[k][0]+=r[k][0]; tot[k][1]+=r[k][1]
    print(f'{lab}: true accepted {r["true"][0]}/{r["true"][1]}, decoys rejected {r["decoy"][1]-r["decoy"][0]}/{r["decoy"][1]}; n>=2: true {r2["true"][0]}/{r2["true"][1]}, decoys rejected {r2["decoy"][1]-r2["decoy"][0]}/{r2["decoy"][1]}')
if tot['true'][1]: print(f'CONTROLS POOLED: true-accept {tot["true"][0]/tot["true"][1]:.2f} ({tot["true"][0]}/{tot["true"][1]}), decoy-reject {1-tot["decoy"][0]/tot["decoy"][1]:.2f}; gate 0.8/0.8')
