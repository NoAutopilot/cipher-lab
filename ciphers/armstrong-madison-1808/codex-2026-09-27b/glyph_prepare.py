from pathlib import Path
import sys,gzip,numpy as np,json,random,collections
D=Path(__file__).resolve().parent;R=D.parents[2];sys.path.insert(0,str(R/'tools'))
import subst_hillclimb as sh
texts=[gzip.open(p,'rt').read() for p in sorted((R/'tools/data/en18').glob('*.gz')) if 'thomas' not in p.name];m=sh.Model(texts)
np.concatenate([x.flatten() for x in [m.uni,m.bi,m.tri,m.quad]]).astype('float32').tofile(D/'glyph_lm.bin')
rows=list(__import__('csv').DictReader((D/'glyphs.tsv').open(),delimiter='\t'))
(D/'glyphs.txt').write_text('\n'.join(';'.join(part.split()) for row in rows for part in row['symbols'].split('|'))+'\n')
fr=sh.load_cipher(D/'glyphs.txt');sy=sorted({t for f in fr for t in f});si={s:i for i,s in enumerate(sy)}
(D/'glyph_symbols.json').write_text(json.dumps(sy))
def save(name,fs):
 (D/(name+'.seq')).write_text('\n'.join(' '.join(str(v) for v in f)+' -1' for f in fs)+'\n')
fs=[[si[t] for t in f] for f in fr];save('glyph',fs)
lengths=[len(f) for f in fs];N=sum(lengths);K=len(sy)
held=sh.norm(gzip.open(next((R/'tools/data/en18').glob('*thomas*')),'rt').read());controls=[]
for seed in range(4):
 rng=random.Random(seed);start=rng.randrange(len(held)-N);plain=held[start:start+N];counts=collections.Counter(plain);distinct=sorted(counts);extra=K-len(distinct)
 eligible=[c for c in distinct if counts[c]>=2]
 if extra>len(eligible):raise ValueError('control cannot match K under maxhomo2')
 rng.shuffle(eligible);duplicated=set(eligible[:extra]);key={};nextid=0
 for c in distinct:key[c]=[nextid];nextid+=1
 for c in sorted(duplicated):key[c].append(nextid);nextid+=1
 used=collections.Counter();cipher=[]
 for c in plain:cipher.append(key[c][used[c]%len(key[c])]);used[c]+=1
 cfr=[];at=0
 for le in lengths:cfr.append(cipher[at:at+le]);at+=le
 save('control'+str(seed),cfr);controls.append({'seed':seed,'start':start,'plain':plain,'N':N,'K':len(set(cipher))})
for seed in range(3):
 flat=[v for f in fs for v in f];random.Random(seed).shuffle(flat);cfr=[];at=0
 for le in lengths:cfr.append(flat[at:at+le]);at+=le
 save('shuffle'+str(seed),cfr)
(D/'glyph_controls.json').write_text(json.dumps(controls,indent=2)+'\n');print('prepared',N,K)
