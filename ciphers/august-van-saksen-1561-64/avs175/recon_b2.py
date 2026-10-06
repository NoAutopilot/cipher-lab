# A4-AVS175 (6 Oct 2026): batch-2 reconciliation of the two blind reads of WVO 175 p1 lines y~1850/1962/2150/2245.
# Readers were given label anchors from the f.66 sheet this time, so no remap. 'X?' counts as X; NEW:* and '?' as unknown.
# A vs B: agree -> sign, disagree -> '?'. [clear] dropped. Writes recon_b2.json for gate_b.py (python3 gate_b.py recon_b2.json).
import json,difflib
A={'L1':"2 0 L 3 Or L 2 D 1 3 N 5 3 Or 9 4 L Qg 3 N | M 3 NEW:hash 8 5 Or Qg 3 N L 0 Sb Sb 3 N",
   'L2':"8 5 Or Td 3 0 L Sb 4 Z Sb 3 Sb N 5 1 N 2 Lf 8 | 3 Or ? N",
   'L3':"? 0 2 3 2 N H 3 Or | N M Or ? Z ? D 3 Or N Qg ? Pb 3 Or N 3",
   'L4':"L 3 N | D 3 N | ? 3 8 Lf Z D 1 3 Sb 3 Td 9 0 1 N Sb Z D 1 Or Pf Or D 0 Z D ? NEW:box 0 M K L ? 0"}
B={'L1':"Z 0 L 3 Or L Z | D 1 3 N 5 3 Or 9 4 L Qg 3 N Z? 3 N M 3 NEW:hash-circle 8 5 Or Qg 3 N L 0 Sb Sb 3 N",
   'L2':"8 5 NEW:cross-stroke D 3 0 L Sb 4 Z D? 3 Sb N 5 1 N Z L 8 3 Or D N",
   'L3':"? 0 Z 3 Z N H? 3 Or | ? 3 Or N | M 0 Z? N D 3 Or N | Qg Sb? N 3 Or N 3 Or N 3",
   'L4':"L 3 N | ? 3 3 N | ? 3 8 L Z D 1 3 Sb 3 D 9 0 1 N Sb Z D 1 Or NEW:cross? Or 0 D 0 Z D N? | L? 0 M K? L N 0"}
GL={'L1':"Jamerlichen Verfolgen vnd ordnungen lassen vnnds",'L2':"Als ist er nun zu Cronick",
    'L3':"Dass sie zu Kunstporn vnd andern gebornamenten",'L4':"zliche Stadt an sich Practiziert vnd die nit"}
norm=lambda t: '?' if (t.startswith('NEW') or t=='?') else (t[:-1] if t.endswith('?') else t)
lines={}; log=[]
for k in A:
    a=[norm(t) for t in A[k].split() if t!='|']; b=[norm(t) for t in B[k].split() if t!='|']
    out=[]
    for op,i1,i2,j1,j2 in difflib.SequenceMatcher(a=a,b=b,autojunk=False).get_opcodes():
        if op=='equal': out+=a[i1:i2]
        else: out+=['?']*max(i2-i1,j2-j1); log.append((k,op,a[i1:i2],b[j1:j2]))
    lines[k]=out
print('A/B agreement: %d/%d'%(sum(t!='?' for v in lines.values() for t in v),sum(len(v) for v in lines.values())))
for k,v in lines.items(): print(k,' '.join(v))
json.dump({'lines':lines,'gl':GL,'want':[0.632,0.368,0.4]},open('recon_b2.json','w'),indent=0)
