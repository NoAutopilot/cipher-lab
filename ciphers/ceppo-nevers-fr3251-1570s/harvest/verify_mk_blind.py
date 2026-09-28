import csv,json,random,sys
seqf,outdir,seed=sys.argv[1],sys.argv[2],int(sys.argv[3])
import os; H=os.path.dirname(os.path.abspath(__file__))+'/'
m={e['id']:e['value'] for e in json.load(open(H+'sign_id_map.json'))}
for x in sys.argv[4:]:  # extra ID=value (HARVEST-D2: X_THETA2=r)
    k,val=x.split('=',1); m[k]=val
P={}
for r in csv.DictReader(open(seqf),delimiter='\t'): P.setdefault(r['passage'],[]).append(r['sign_id'].strip())
def dec(mm):
    out=[]
    for k,s in P.items():
        t=''.join('_' if mm.get(x) is None else ('' if mm[x]=='null' else ('&' if mm[x]=='et' else mm[x])) for x in s)
        out.append(f'{k}\t{t}')
    return '\n'.join(out)
rng=random.Random(seed); ids=list(m); vals=[m[i] for i in ids]
texts=[('REAL',dec(m))]
for i in range(20):
    rng.shuffle(vals); texts.append((f'SH{i+1}',dec(dict(zip(ids,vals)))))
order=list(range(21)); rng.shuffle(order)
with open(f'{outdir}/blind_decodes.txt','w') as f:
    for n,j in enumerate(order): f.write(f'=== TEXT {n+1:02d} ===\n{texts[j][1]}\n\n')
json.dump({f'{n+1:02d}':texts[j][0] for n,j in enumerate(order)},open(f'{outdir}/blind_answer.json','w'))
