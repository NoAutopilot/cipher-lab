# KH1-F, 7 Oct 2026: hand profile of fr.3988 f.143r passes (passP L05-L14 rough; passQ L06-L09 careful) against the no.60 atlas, GAPS4 method (fr3986 recto_profile.py). Usage: python3 profile.py passQ.tsv
import csv, os, sys, collections
R=os.path.join(os.path.dirname(os.path.abspath(__file__)),'..','..','..')
def rows(p):
    with open(p) as f: return list(csv.DictReader((l for l in f if not l.startswith('#')), delimiter='\t'))
atl=set()
for f in ('atlas264.tsv','atlas264ext.tsv'): atl|={r['tag'].strip() for r in rows(f'{R}/tools/keys/key60_atlas/{f}')}
key={r['sign'].strip() for r in rows(f'{R}/tools/keys/key60.tsv')}
H=f'{R}/ciphers/fr3986-nevers-revol-1593/'
for lab,p in [('leaf 298 office hand passD',H+'atlas_heldout/heldout298_passD.tsv'),('f.198 verso passA',H+'passes/v2/passA.tsv'),('f.198 verso passB',H+'passes/v2/passB.tsv'),('f.198 recto passA',H+'passes/recto/passA.tsv'),('fr.3988 f.143r pass under test',sys.argv[1])]:
    rr=rows(p); t=[x['tag'].strip() for x in rr]
    nw=sum(1 for x in t if x.startswith('NEW') or x.startswith('<'))
    hh=sum(1 for x in rr if x['confidence'].strip()=='H')
    print(f"{lab}\tN={len(t)}\tatlas {100*sum(x in atl for x in t)/len(t):.1f}%\tkey60 {100*sum(x in key for x in t)/len(t):.1f}%\tnew {100*nw/len(t):.1f}%\tH {100*hh/len(t):.1f}%")
rr=rows(sys.argv[1]); c=collections.Counter(x['tag'].strip() for x in rr)
print('distinct',len(c),'atlas tags used',len([t for t in c if t in atl]),'of',len(atl))
print('top',c.most_common(20))
print('not key60/not NEW',sorted({t for t in c if t not in key and not t.startswith('NEW')}))
print('NEW',[t for t in c if t.startswith('NEW')])
