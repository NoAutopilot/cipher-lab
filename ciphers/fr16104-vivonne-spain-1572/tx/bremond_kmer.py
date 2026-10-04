# VIV-BREMOND (4 Oct 2026): shared k-mers between our decodes (inks 53, 54, 63) and three on-disk IA texts (d Ars 1884, Gachard II, Catherine IV as background). Run from the repo root.
import gzip,unicodedata,re,sys
def norm(s):
    s=unicodedata.normalize('NFD',s.lower()); s=''.join(c for c in s if 'a'<=c<='z')
    return s.replace('v','u').replace('j','i').replace('y','i')
D='sources/ia-fulltext/print-check/'
books={'dars':'lepredemadamede00dargoog','gachardII':'labibliothquen02gachuoft','catherineIV':'lettresdecatheri04cathuoft'}
txt={k:norm(gzip.open(D+v+'_djvu.txt.gz','rt',errors='ignore').read()) for k,v in books.items()}
F='ciphers/fr16104-vivonne-spain-1572/'
pieces={'53':'piece53_L_decode.txt','54':'piece54_decode_L.txt','63':'piece63_decode.txt'}
for K in (10,12,15):
  for p,f in pieces.items():
    d=norm(open(F+f).read())
    km={d[i:i+K] for i in range(len(d)-K+1)}
    row=[]
    for b,t in txt.items():
        S={t[i:i+K] for i in range(len(t)-K+1)}
        hits=km&S
        row.append(f"{b}={len(hits)}/{len(km)}")
        if K==15 and hits and b=='dars': print('   dars15',p,sorted(hits)[:20])
    print(K,p,len(d),' '.join(row))
print({b:len(t) for b,t in txt.items()})
K=12
S={txt['dars'][i:i+K] for i in range(len(txt['dars'])-K+1)}
for p,f in pieces.items():
    d=norm(open(F+f).read()); print(p,sorted({d[i:i+K] for i in range(len(d)-K+1)}&S))
