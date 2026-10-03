import difflib, csv
A={'c1':"Z N 8 0 Sb 5 3 Or? Dl? 0 Dl? 1 8 0 5 Dl? 1 3 5 Sb Sb 3 Or Sb? 3",
'c2':"L 3 Z Pb Sb M? Qg 5 9 Sb Pf? 3 9 0 1 Or NW M? 5 N Sb 3 Or 9 L Qg 3 L 0 1 L",
'c3':"NW HX 0 L 9 Yz? 3 Z 9 Pb 3? 4 Or Qg 3 9 1 0 Pb 3 N NEW:e-like NEW:k-like 9? Or 0 8 Dl? ? ? ? ? ?"}
B={'c1':"Z N 8 0 Sb 5 3 Td 0 D 1 8 0 5 D 1 3 5 Sb Sb 3 Or Pb? 3",
'c2':"Lf? 3 Z Pb? NEW:M Qg 5 9 Sb Qg? 3 9 0 1 Or N NEW:M 5 N Sb 3 Or 9 L Pf 3 L 0 1 L",
'c3':"N HX 0 L 9 Yz 3 Z 9 Pb 3 Sb 4 Or Pf 3 9 1 0 Pb 3 N NEW:e-loop NEW:K Pf? Or 0 8 Td? 3 ? 0 ? ? 5 ? ? ?"}
def norm(t):
    t=t.rstrip('?')
    if t.startswith('NEW:M'): return 'M'
    return t
out={}
for k in A:
    a=[norm(t) for t in A[k].split()]; b=[norm(t) for t in B[k].split()]
    sm=difflib.SequenceMatcher(a=a,b=b,autojunk=False); r=[];agree=tot=0
    for op,i1,i2,j1,j2 in sm.get_opcodes():
        if op=='equal': r+=a[i1:i2]; agree+=i2-i1; tot+=i2-i1
        else:
            n=max(i2-i1,j2-j1); tot+=n; r+=['?']*n
    out[k]=r; print(k,'agree %d/%d'%(agree,tot),' '.join(r))
import json; json.dump(out,open('recon.json','w'))
