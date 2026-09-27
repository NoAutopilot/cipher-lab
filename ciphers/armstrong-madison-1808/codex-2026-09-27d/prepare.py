"""Prepare local alternative-label tests; no language-derived target edits."""
from pathlib import Path
import collections,csv,gzip,json,random,sys
import numpy as np

D=Path(__file__).resolve().parent;R=D.parents[2]
sys.path.insert(0,str(R/'tools'));import subst_hillclimb as sh
B=D.parent/'codex-2026-09-27b'
texts=[gzip.open(p,'rt').read() for p in sorted((R/'tools/data/en18').glob('*.gz')) if 'thomas' not in p.name]
model=sh.Model(texts)
np.concatenate([x.flatten() for x in [model.uni,model.bi,model.tri,model.quad]]).astype('float32').tofile(D/'lm.bin')
symbols=json.loads((B/'glyph_symbols.json').read_text())
rows=list(csv.DictReader((B/'glyphs.tsv').open(),delimiter='\t'))
seq=[];locations={}
for row in rows:
    k=0
    for x in row['symbols'].split():
        if x=='|':seq.append(-1);continue
        k+=1;locations[(row['passage'],k)]=len(seq);seq.append(symbols.index(x))
    seq.append(-1)
assert seq==list(map(int,(B/'glyph.seq').read_text().split()))
alts=list(csv.DictReader((D/'alternatives.tsv').open(),delimiter='\t'))
positions={}
for row in alts:
    ix=locations[(row['passage'],int(row['position_1based']))]
    assert seq[ix]==symbols.index(row['original']),row
    positions[ix]=[seq[ix],symbols.index(row['alternative'])]

def save(name,values,candidates):
    (D/f'{name}.seq').write_text(' '.join(map(str,values))+'\n')
    (D/f'{name}.alt').write_text('\n'.join(str(ix)+' '+','.join(map(str,cs)) for ix,cs in candidates.items())+'\n')
save('target',seq,positions)
held=sh.norm(gzip.open(next((R/'tools/data/en18').glob('*thomas*')),'rt').read())
control_meta=[]
N=sum(x>=0 for x in seq);K=len(symbols)
for seed in [4,5]:
    rng=random.Random(2026092700+seed)
    start=rng.randrange(len(held)-N);plain=held[start:start+N]
    values=sorted(set(plain));key=values.copy();freq=collections.Counter(plain)
    extra=sorted((x for x in values if freq[x]>=2),key=lambda x:(-freq[x],x))[:K-len(values)]
    key+=extra;assert len(key)==K
    rng.shuffle(key);ids={x:[i for i,k in enumerate(key) if k==x] for x in values}
    seen=collections.Counter();clean=[]
    for x in plain:clean.append(ids[x][seen[x]%len(ids[x])]);seen[x]+=1
    it=iter(clean);truth=[next(it) if t>=0 else -1 for t in seq]
    observed=truth.copy();candidates={};wrong=set(rng.sample(list(positions),5))
    for ix in positions:
        distractor=rng.randrange(K)
        while key[distractor]==key[truth[ix]]:distractor=rng.randrange(K)
        if ix in wrong:observed[ix]=distractor
        candidates[ix]=[observed[ix],truth[ix] if ix in wrong else distractor]
    save(f'control{seed}',observed,candidates)
    control_meta.append(dict(seed=seed,start=start,N=N,K=K,key=key,plaintext=plain,
       truth_sequence=truth,observed_sequence=observed,wrong_positions=sorted(wrong)))
(D/'controls.json').write_text(json.dumps(control_meta,indent=2)+'\n')
(D/'locations.json').write_text(json.dumps([dict(passage=p,position_1based=k,sequence_index=ix)
    for (p,k),ix in locations.items()],indent=2)+'\n')
print(json.dumps([dict(seed=c['seed'],plaintext=c['plaintext']) for c in control_meta],indent=2))
