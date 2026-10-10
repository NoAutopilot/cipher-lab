"""E62-CAM: longest shared word run, each residue entry vs ORN djvu text; control = same entry word-shuffled (seed 1862) AND a formula-matched control:
the longest run of the entry's own sentence-reversed order is NOT used; instead report run length only and flag >=8 words. usage: python3 longest_run.py DJVU_DIR [THRESH=7]  (dir may hold any ORN volumes; LR-RES 10 Oct 2026 added THRESH and the per-volume maximum line)"""
import re,sys,glob,os,random,collections
def words(t): return re.findall(r"[a-z]+", re.sub(r'<[^>]+>',' ',t).lower().replace('&',' and '))
rd=open('print/residue/readings.md').read()
secs=re.split(r'\n## (\d+) ',rd)[1:]
ents=[(secs[i],e) for i in range(0,len(secs),2) for e in re.split(r'\n\n',secs[i+1]) if e.startswith('*')]
vols={os.path.basename(f)[:-4]:words(open(f,errors='ignore').read()) for f in glob.glob(sys.argv[1]+'/*.txt')}
N=4
idx={}
for v,w in vols.items():
    d=collections.defaultdict(list)
    for i in range(len(w)-N+1): d[tuple(w[i:i+N])].append(i)
    idx[v]=d
def longest(ws,v):
    W=vols[v];best=(0,0)
    for i in range(len(ws)-N+1):
        for j in idx[v].get(tuple(ws[i:i+N]),()):
            k=N
            while i+k<len(ws) and j+k<len(W) and ws[i+k]==W[j+k]: k+=1
            if k>best[0]: best=(k,j)
    return best
random.seed(1862)
THRESH=int(sys.argv[2]) if len(sys.argv)>2 else 7
mx={v:0 for v in vols}; mxs={v:0 for v in vols}
for p,e in ents:
    w=words(re.sub(r'\{[^}]*\}','',e)); w2=w[:]; random.shuffle(w2)
    r={v:longest(w,v)[0] for v in vols}; s={v:longest(w2,v)[0] for v in vols}
    if max(r.values())>=THRESH: print(p,e[:28].replace('\n',' '),len(w),r,'shuf',s)
    for v in vols: mx[v]=max(mx[v],r[v]); mxs[v]=max(mxs[v],s[v])
print('MAX over',len(ents),'entries per volume:',mx,'shuffled',mxs)
