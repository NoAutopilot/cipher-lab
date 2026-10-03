# GAPS16-na-suriname-map-1781 (account-4), 2 Oct 2026: align the two blind passes of the native-resolution Remarque re-pass (copy of rem2039_merge.py with new file names).
import csv,difflib,re
def load(f):
    d={}
    for r in csv.DictReader(open(f),delimiter='\t'):
        toks=[t for t in r['glyphs'].replace('<,>',' ').replace('<.>',' ').replace('/',' ').replace(',',' ').split() if t not in ('.',) and not (t.startswith('<') and t.endswith('>') and not t[1:-1].replace('½','').isdigit())]
        norm={'f':'[f-loop]','h':'[h-loop]','1':'[l-bare]'}
        # GAPS16: the two readers' own names for one shape (each pairing consistent through both files), unified to
        # pass A's name before diffing (rule 3 notation lesson): B v = A y, [div] = [x-dot], [kappa] = K, [u-tail] = [thorn],
        # J = [J-rev], [amp] = &, A's [ct] = 'c t'
        norm.update({'v':'y','[div]':'[x-dot]','[kappa]':'K','[u-tail]':'[thorn]','J':'[J-rev]','[amp]':'&'})
        toks=[x for t in toks for x in (['c','t'] if t=='[ct]' else [t])]
        d[r['crop']]=[norm.get(t,t) for t in toks]
    return d
A=load('passes/remN_passA.tsv');B=load('passes/remN_passB.tsv')
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
with open('passes/remN_merged.tsv','w') as f:
    f.write('crop\tpos\tsign\tconf\tnote\n')
    for r in out: f.write('\t'.join(map(str,r))+'\n')
