"""E62-CAM: every residue entry (readings.md) vs ORN ser. I vols. 22, 23 djvu text, shared 4-word runs, entry word-shuffled control (seed 1862).
usage: python3 ngram_orn.py DJVU_DIR  (from ciphers/eckert-1862). Printed text only; a miss is a search result, not a verdict."""
import re,sys,glob,os,random,collections
def words(t): return re.findall(r"[a-z]+", re.sub(r'<[^>]+>',' ',t).lower().replace('&',' and '))
rd=open('print/residue/readings.md').read()
secs=re.split(r'\n## (\d+) ',rd)[1:]
ents=[]
for i in range(0,len(secs),2):
    for e in re.split(r'\n\n',secs[i+1]):
        if e.startswith('*'): ents.append((secs[i],e))
N=4
vols={os.path.basename(f)[:-4]:words(open(f,errors='ignore').read()) for f in glob.glob(sys.argv[1]+'/*.txt')}
idx={v:set(' '.join(w[i:i+N]) for i in range(len(w)-N+1)) for v,w in vols.items()}
random.seed(1862)
print('entries',len(ents),'vols',list(vols))
for p,e in ents:
    w=words(re.sub(r'\{[^}]*\}','',e)); w2=w[:]; random.shuffle(w2)
    h=lambda ws:{v:sum(1 for i in range(len(ws)-N+1) if ' '.join(ws[i:i+N]) in idx[v]) for v in vols}
    a,b=h(w),h(w2)
    if max(a.values())>0 or max(b.values())>0: print(p,e[:30].replace('\n',' '),len(w),a,'shuf',b)
