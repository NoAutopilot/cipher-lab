"""SUR-372 exploratory (not pre-registered as a gate): per sign code in pass R, the gloss letter at the aligned position.
Alignment = difflib opcodes of a decode with every keyed sign (Nieuw table, unkeyed -> '?') against the gloss; equal and
same-length replace blocks give a gloss letter per token. Also C/M grade counts for R under each key (PREREG grades)."""
import difflib, sys
from collections import Counter, defaultdict
sys.path.insert(0, '.'); sys.argv=['x']
import importlib.util
spec=importlib.util.spec_from_file_location('s','score_sur372.py'); s=importlib.util.module_from_spec(spec); spec.loader.exec_module(s)
gtxt, lines = s.load('R'); gl = s.norm(gtxt)
toks=[t for l in lines for t in l if t!='_' and t not in ',.:;-—']
def align(key):
    dec=[s.norm(key.get(t,'?')) or '?' for t in toks]
    letters=''.join(d if d!='?' else '#' for d in dec)
    sm=difflib.SequenceMatcher(None,letters,gl,autojunk=False); g=[None]*len(toks)
    for op,i1,i2,j1,j2 in sm.get_opcodes():
        if op=='equal' or (op=='replace' and i2-i1==j2-j1):
            for k in range(i2-i1): g[i1+k]=gl[j1+k]
    return dec,g
res={}
for kn,key in s.KEYS.items():
    dec,g=align(key); C=sum(1 for d,x in zip(dec,g) if x and d==x); res[kn]=(dec,g)
    print(f'{kn}: tokens {len(toks)}  C {C}  M {len(toks)-C}  ({C/len(toks):.1%} C)')
dec,g=res['nieuw']; by=defaultdict(Counter)
for t,x in zip(toks,g): by[t][x or '-']+=1
print('\ncode\tn\toud\tnieuw\tgloss letters at aligned positions')
for t,c in sorted(by.items(),key=lambda kv:-sum(kv[1].values())):
    o,n=s.OUD.get(t,'?'),s.NIEUW.get(t,'?')
    flag='' if o==n else '  <-- keys differ'
    print(f"{t}\t{sum(c.values())}\t{o}\t{n}\t{' '.join(f'{k}:{v}' for k,v in c.most_common(4))}{flag}")
