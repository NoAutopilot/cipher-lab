from pathlib import Path
import sys,gzip,numpy as np,unicodedata,json
D=Path(__file__).resolve().parent;R=D.parents[2];sys.path.insert(0,str(R/'tools'));import subst_hillclimb as sh
for name,folder,consonants in [('fr','fr18',False),('consonants','en18',True)]:
 texts=[unicodedata.normalize('NFKD',gzip.open(p,'rt').read()) for p in (R/'tools/data'/folder).glob('*.gz') if 'thomas' not in p.name]
 if consonants:texts=[''.join(c for c in sh.norm(t) if c not in 'aeiou') for t in texts]
 m=sh.Model(texts);np.concatenate([x.flatten() for x in [m.uni,m.bi,m.tri,m.quad]]).astype('float32').tofile(D/f'glyph_{name}_lm.bin')
sy=json.loads((D/'glyph_symbols.json').read_text());seq=list(map(int,(D/'glyph.seq').read_text().split()));
for name,tags in [('separator65',{'65'}),('coarsemerge',set())]:
 if name=='separator65':ss=[(-1 if n<0 or sy[n] in tags else n) for n in seq]
 else:
  merge={'12':'18','14':'10','16':'18','22':'20','23':'20','65':'64','73':'26'}
  ss=[n if n<0 else sy.index(merge.get(sy[n],sy[n])) for n in seq]
  used=sorted(set(ss)-{-1});ss=[used.index(n) if n>=0 else -1 for n in ss]
 (D/(name+'.seq')).write_text(' '.join(map(str,ss)))
print('prepared variants')
