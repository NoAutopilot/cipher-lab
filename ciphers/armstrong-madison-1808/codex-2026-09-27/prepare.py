from pathlib import Path
import sys,re,gzip,csv,json,numpy as np
out=Path(__file__).resolve().parent; r=out.parents[2];sys.path.insert(0,str(r/'tools'))
import subst_hillclimb as sh
texts=[gzip.open(p,'rt').read() for p in sorted((r/'tools/data/en18').glob('*.gz')) if 'thomas' not in p.name]
m=sh.Model(texts)
txt=(r/'ciphers/armstrong-madison-1808/ciphertext.txt').read_text(); toks=[int(w) if w.isdigit() else -1 for l in txt.splitlines() if not l.startswith('#') for w in l.split()]
(out/'target.seq').write_text(' '.join(map(str,toks)))
clean=(out/'ciphertext_editorial_clean.txt').read_text()
ct=[int(w) if w.isdigit() else -1 for l in clean.splitlines() if not l.startswith('#') for w in l.split()]
(out/'target_clean.seq').write_text(' '.join(map(str,ct)))
for name in ['THE972_bourdeau','WE028']:
 t={int(x['value']):x['plaintext'] for x in csv.DictReader(open(r/f'tools/data/uscodes-1800/{name}.tsv'),delimiter='\t')}; s={k:np.array([sh.IDX[c] for c in sh.norm(v)],dtype=int) for k,v in t.items()};s={k:v for k,v in s.items() if len(v)}
 a=np.zeros((2001,2001),dtype=np.float32)
 # bridge log likelihood against uniform letters; unknown = zero information.
 for i,u in s.items():
  for j,v in s.items():
   z=np.concatenate([u[-3:],v[:3]]); n=len(u[-3:]); b=m.score_frags([z])-m.score_frags([z[:n]]);a[i,j]=max(-3.,b/len(v[:3])+np.log10(sh.A))
 a.tofile(out/f'{name}.bin');(out/f'{name}.known').write_text(' '.join(map(str,s)))
 print(name,len(s),flush=True)
