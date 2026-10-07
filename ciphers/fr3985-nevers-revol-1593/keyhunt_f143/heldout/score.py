# KHF-4, 7 Oct 2026: score the blind family-check pass against key_sealed.tsv per PREREG.md. Exit 0 = scored and the
# committed score.txt matches (or --write); exit 1 on a stale score.txt.  Usage: python3 score.py [--write]
import csv, os, sys, math
H=os.path.dirname(os.path.abspath(__file__))
def rows(p): return list(csv.DictReader(open(os.path.join(H,p)),delimiter='\t'))
SYN=[{'⊥','inT','_|_'},{'alpha','∝','α',"alpha'"},{'do','ꝺo'},{'r','ꝛ'},{'pi','π'},{'lam','λ'},{'T','TL'}]
def canon(t):
    t=t.strip()
    for s in SYN:
        if t in s: return min(s)
    return t
def wil(k,n,z=1.96):
    if n==0: return (0,0)
    p=k/n; d=1+z*z/n; c=p+z*z/(2*n); h=z*math.sqrt(p*(1-p)/n+z*z/(4*n*n)); return (100*(c-h)/d,100*(c+h)/d)
key={(r['set'],r['idx']):r for r in rows('key_sealed.tsv')}
tm={r['tile']:(r['set'],r['src_idx']) for r in rows('tile_map.tsv')}
rd={r['tile'].strip():r for r in rows('pass_blind.tsv')}
out=[]; st={}
for tile,(s,i) in sorted(tm.items()):
    r=rd[tile]; tag=r['tag'].strip(); conf=r['confidence'].strip(); sealed=key[(s,i)]['sealed_tag']
    hit=canon(tag)==canon(sealed); fam=tag!='NONE' and conf in('H','M')
    d=st.setdefault(s,[0,0,0]); d[0]+=1; d[1]+=hit; d[2]+=fam
    out.append(f'{tile}\t{s}\t{sealed}\t{tag}\t{conf}\t{"hit" if hit else "-"}\t{"fam" if fam else "-"}')
res={}
lines=['tile\tset\tsealed\tread\tconf\tS1\tS2']+out+['']
for s,(n,h,f) in st.items():
    res[s]=(100*h/n,100*f/n)
    a,b=wil(h,n); c,e=wil(f,n)
    lines.append(f'{s}: N={n}  S1 {h}/{n}={100*h/n:.1f}% (Wilson {a:.1f}-{b:.1f})  S2 {f}/{n}={100*f/n:.1f}% (Wilson {c:.1f}-{e:.1f})')
P,N,F=res['leaf298'],res['mayenne61'],res['f143r']
ga=P[0]>=80; gb=N[1]<=50 and P[1]-N[1]>=30; gc=F[0]>=80 and F[1]>=N[1]+30
lines.append(f'gate (a) leaf298 S1>=80: {ga}; (b) mayenne61 S2<=50 and >=30 below leaf298 S2: {gb}; (c) f143r S1>=80 and S2>=mayenne S2+30: {gc}')
v='NON-TEST (a)' if not ga else 'NON-TEST (b)' if not gb else 'PASS' if gc else 'FAIL'
lines.append('VERDICT: '+v)
txt='\n'.join(lines)+'\n'
p=os.path.join(H,'score.txt')
if '--write' in sys.argv: open(p,'w').write(txt)
print(txt)
if not '--write' in sys.argv and (not os.path.exists(p) or open(p).read()!=txt): print('score.txt stale'); sys.exit(1)
