# A4-AVS175B (6 Oct 2026): reconciliation of the two blind reads of WVO 175 p1's last 5 cipher lines (left-edge centres y~2372, 2508,
# 2628, 2755, 2870; the lines slope down ~30 px to the right, so each line was cut as two halves at their own heights).
# Readers had the batch-2 label anchors, so no remap. 'X?' counts as X; NEW:* and '?' as unknown. A vs B: agree -> sign, disagree -> '?'.
# Gloss = the subagent gloss read as given to the aligner, with its '[?]' marks and '...' removed (same practice as batch 2).
# Writes recon_b3.json for gate_b.py (python3 gate_b.py recon_b3.json --check).
import json,difflib
A={'L1':"Z Or 3 L V Or Z 3 Qg 5? 4 L D V Z N Qg 3 | N 1 4? L 3 N | M Pb 3 | Sb 3 9 Yz? 3 9",
   'L2':"1 0 9 | M K 0 Dp? L 3 N L 3 5 Z 1 3 | 5 3 Z N L 5 N Qg? 3 8 4 N L Z D 1 3 N",
   'L3':"N 3 5 3 Pb? 0 Z Td Td? Z N Qg 3 9 D? 0 5 4 | N NEW:H | K? Z N L Z 3 Qg 3 N Td 3",
   'L4':"0 Pb Sb Td? Z Qg? 5 Pb 3 Td? Sb 3 N Td 3 N | Z N Qg L 3 Z D 1 3 L 1 0 Pb 3 N",
   'L5':"R 0 Pb | NEW:B 0 N Td Z Or? N"}
B={'L1':"Z Or 3 L | V Or Z 3 Qg Sb 4 L D V Z N Qg 3 N 1 4 L 3 N | M Pb 3 Sb 3 9 Yz 3 9",
   'L2':"1 0 9 | M K 0 Or L 3 N L 3 5 9 1 3 5 3 Z N 3 L 5 N Qg 3 8 4 N L Z D 1 3 N",
   'L3':"N 3 5 3 ? 0 Z Td Td Or Z N Qg 3 9 Td 0 5 4 N NEW:H? K? Z N L Z 3 Qg 3 N Td 3",
   'L4':"0 Pb Sb | Or? Z 9 Pf | 5 Pb 3 | Or? Sb 3 N | Td 3 N Z N Qg L 3 Z | D 1 3 | L 1 0 Pb 3 N",
   'L5':"R 0 Pb | NEW:B 0 N Td Z Or N"}
GL={'L1':"Jrem Kriegsvolck eingenommen vnd vnd Rosolzer hat",'L2':"vnd die armen Leute zu einem gnesinlichem",
    'L3':"nauem aids dringet Damit wir E.L. Jnhingmuds",'L4':"abschrifft vbersenden Jn gleichem haben E.L. ab",
    'L5':"Jnr andern"}
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
for l in log: print(l)
want=json.load(open('recon_b3.json'))['want'] if __import__('os').path.exists('recon_b3.json') else None
json.dump({'lines':lines,'gl':GL,'want':want},open('recon_b3.json','w'),indent=0)
