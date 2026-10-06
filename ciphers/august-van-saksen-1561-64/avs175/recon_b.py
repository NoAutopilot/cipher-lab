# A4-AVS175 (6 Oct 2026): batch-1 reconciliation of the two blind reads of WVO 175 p1 lines y~1187/1300/1595/1700.
# Both readers mislabelled two signs when building their chart from the f.66 reference; the f.66 sheet itself (line 1
# '3 6 8 2 + 9 9' = '3 Sb 8 Z Or 9 9'; line 5 '... v' = N) fixes the label, so each reader's labels are remapped uniformly
# (A: Pf -> Or, the cross-topped circle; B: Pb -> Or, Or -> N, the v-shape). Not from the gloss. Then A vs B: agree -> sign,
# disagree -> '?'. Struck signs (x...) and [clear] dropped. L2 cut after its second word (only those two sit under gloss G1).
import json
A={'L1':"Qg Pf 4 L 3 N | D 1 Pf Z Td 3 N Z N Qf Z Sb Sb 3 N L Lf 0 N Td 3 N Td 3 Pf",
   'L2':"Pf 3 L Z Qg Z 4 N | 1 0 L Td 3 N",
   'L3':"3 Pf 3 L Qg 3 8 0 L 9 Sb 0 L 3 N 5 4 Pf N 1 3 L 3 N",
   'L4':"Qg 5 Pf 9 Qg 0 1 Pf 3 N M K 0 Pf L 3 N | D 1 Pf Z Td 3 N 0 1 N L Z Td M 9 5 Qg Qg"}
B={'L1':"Qg Pb 4 L 3 Or | D 1 Pb Z Td 3 Or Z Or Qf Z Sb Sb 3 Or L 0 Or Qf 3 Or Qf 3 Pb",
   'L2':"Qf 3 L Z Qg Z 4 Or | 1 0 L Td 3 Or",
   'L3':"3 Pb 3 L Qg 3 8 0 L 9 Sb 0 L 3 Or | 5 4 Pb Or | 1 3 L 3 Or",
   'L4':"Qg 5 Pb 9 Pf 4 0 1 Pb 3 Or | M K 0 Pb L 3 Or | D 1 Qf Z Td 3 Or 0 1 Or L 3 Z Td | M 9 5 Pf Pf"}
mA={'Pf':'Or'}; mB={'Pb':'Or','Or':'N'}
GL={'L1':"framen Christen dn Dieser Landen Der",'L2':"Religion halten",
    'L3':"Jrom gewaltsamen Vornemen",'L4':"fortfaren vnd die armen Christen an Leib vnd gutt"}
import difflib
lines={}; log=[]
for k in A:
    a=[mA.get(t,t) for t in A[k].split() if t!='|']; b=[mB.get(t,t) for t in B[k].split() if t!='|']
    sm=difflib.SequenceMatcher(a=a,b=b,autojunk=False); out=[]
    for op,i1,i2,j1,j2 in sm.get_opcodes():
        if op=='equal': out+=a[i1:i2]
        else:
            n=max(i2-i1,j2-j1); out+=['?']*n; log.append((k,op,a[i1:i2],b[j1:j2]))
    lines[k]=out
agree=sum(t!='?' for v in lines.values() for t in v); tot=sum(len(v) for v in lines.values())
print('A/B agreement after label remap: %d/%d'%(agree,tot))
for k,v in lines.items(): print(k,' '.join(v))
for l in log: print('split',l)
json.dump({'lines':lines,'gl':GL,'want':[0.753,0.387,0.398]},open('recon_b.json','w'),indent=0)
