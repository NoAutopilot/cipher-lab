"""Independently check the reported objective and identify selected alternatives."""
from pathlib import Path
import collections,json
import numpy as np

D=Path(__file__).resolve().parent;B=D.parent/'codex-2026-09-27b'
raw,key,reading,edits=(D/'results/target-soft.tsv').read_text().splitlines()[0].split('\t')
assert max(collections.Counter(key).values())<=2
changes={int(x.split(':')[0]):int(x.split(':')[1]) for x in edits.split(',') if x}
orig=list(map(int,(D/'target.seq').read_text().split()));seq=orig.copy()
choices={int(line.split()[0]):list(map(int,line.split()[1].split(','))) for line in (D/'target.alt').read_text().splitlines()}
for ix,v in changes.items():
    assert v in choices[ix]
    seq[ix]=v
check=''.join('|' if v<0 else key[v] for v in seq);assert check==reading
A=24;alpha='abcdefghiklmnopqrstuwxyz'
lm=np.fromfile(D/'lm.bin',dtype='float32')
uni,bi,tri,quad=np.split(lm,[A,A+A*A,A+A*A+A*A*A])
bi=bi.reshape(A,A);tri=tri.reshape(A,A,A);quad=quad.reshape(A,A,A,A)
likelihood=0.0
for text in reading.split('|'):
    f=np.array([alpha.index(c) for c in text],dtype=int)
    if len(f)>0:likelihood+=float(uni[f[0]])
    if len(f)>1:likelihood+=float(bi[f[0],f[1]])
    if len(f)>2:likelihood+=float(tri[f[0],f[1],f[2]])
    if len(f)>3:likelihood+=quad[f[:-3],f[1:-2],f[2:-1],f[3:]].sum(dtype=np.float64)
assert abs(likelihood-.3*len(changes)-float(raw))<1e-7
locations={r['sequence_index']:r for r in json.loads((D/'locations.json').read_text())}
symbols=json.loads((B/'glyph_symbols.json').read_text())
edits=[dict(**locations[ix],original=symbols[orig[ix]],selected=symbols[v]) for ix,v in changes.items()]
result=dict(status='unsolved; no coherent target reading',penalized_score=float(raw),
            log10_likelihood=likelihood,change_penalty=.3,selected_alternatives=edits,
            key=key,fragments=reading.strip('|').split('|'))
(D/'target_result.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
