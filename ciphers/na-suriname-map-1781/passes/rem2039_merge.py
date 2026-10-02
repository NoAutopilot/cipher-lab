import csv,difflib,re
def load(f):
    d={}
    for r in csv.DictReader(open(f),delimiter='\t'):
        toks=[t for t in r['glyphs'].replace('<,>',' ').replace('<.>',' ').replace('/',' ').replace(',',' ').split() if t not in ('.',)]
        norm={'f':'[f-loop]','h':'[h-loop]','1':'[l-bare]'}
        d[r['crop']]=[norm.get(t,t) for t in toks]
    return d
A=load('passes/rem2039_passA.tsv');B=load('passes/rem2039_passB.tsv')
out=[];tot=agree=0
for c in A:
    a,b=A[c],B[c]; sm=difflib.SequenceMatcher(None,a,b,autojunk=False); pos=0
    for op,i1,i2,j1,j2 in sm.get_opcodes():
        if op=='equal':
            for t in a[i1:i2]: out.append((c,pos,t,'H','')); pos+=1; agree+=1; tot+=1
        else:
            for k in range(max(i2-i1,j2-j1)):
                ta=a[i1+k] if i1+k<i2 else '-'; tb=b[j1+k] if j1+k<j2 else '-'
                out.append((c,pos,ta if ta!='-' else tb,'M',f'A:{ta} B:{tb}')); pos+=1; tot+=1
    print(c,len(a),len(b),round(sm.ratio(),3))
print('agree',agree,'of',tot)
with open('passes/rem2039_merged.tsv','w') as f:
    f.write('crop\tpos\tsign\tconf\tnote\n')
    for r in out: f.write('\t'.join(map(str,r))+'\n')
