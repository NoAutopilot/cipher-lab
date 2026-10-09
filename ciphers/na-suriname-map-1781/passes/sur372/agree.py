"""A vs B cipher-sign agreement per line (signs only; '_' gaps and {clear} dropped; 'x?' -> 'x'). Writes disagreements.tsv."""
import difflib,re
def load(f):
    out=[]
    for ln in open(f,encoding='utf-8'):
        p=ln.rstrip('\n').split('\t')
        if len(p)>=3 and p[1]=='cipher':
            c=re.sub(r'\{[^}]*\}',' ',p[2]); out.append((p[0][-3:],[t.rstrip('?') if len(t)>1 else t for t in c.split() if t!='_']))
    return out
A,B=load('passA.tsv'),load('passB.tsv'); assert len(A)==len(B),(len(A),len(B))
tot=same=0; rows=[]
for (la,a),(lb,b) in zip(A,B):
    sm=difflib.SequenceMatcher(None,a,b,autojunk=False)
    m=sum(x.size for x in sm.get_matching_blocks()); n=max(len(a),len(b)); tot+=n; same+=m
    for op,i1,i2,j1,j2 in sm.get_opcodes():
        if op!='equal': rows.append((la,lb,op,i1,' '.join(a[i1:i2]),' '.join(b[j1:j2])))
    print(la,lb,len(a),len(b),m,f'{m/n:.3f}')
print(f'TOTAL agreement {same}/{tot} = {same/tot:.3f}; disagreement spans {len(rows)}')
with open('disagreements.tsv','w') as f:
    f.write('lineA\tlineB\top\tposA\tA\tB\n'); [f.write('\t'.join(map(str,r))+'\n') for r in rows]
