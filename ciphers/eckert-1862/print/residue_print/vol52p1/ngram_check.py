import re,sys,glob,os,random,collections
def words(t): return re.findall(r"[a-z]+", re.sub(r'<[^>]+>',' ',t).lower().replace('&',' and '))
rd=open('print/residue/readings.md').read()
secs=re.split(r'\n## (\d+) ',rd)[1:]
ents=[]
for i in range(0,len(secs),2):
    ptr=secs[i]
    for e in re.split(r'\n\n',secs[i+1]):
        if e.startswith('*'): ents.append((ptr,e))
want={'4982','4999','4992','4984'}
sel=[(p,e) for p,e in ents if p in want or 'Camden' in e]
N=int(sys.argv[1]); vols={os.path.basename(f)[:-4]:words(open(f,errors='ignore').read()) for f in glob.glob('/tmp/claude-0/s/or/*.txt')}
idx={v:collections.Counter(' '.join(w[i:i+N]) for i in range(len(w)-N+1)) for v,w in vols.items()}
random.seed(1862)
print('entries',len(sel),'vols',list(vols))
for p,e in sel:
    w=words(re.sub(r'\{[^}]*\}','',e)); w2=w[:]; random.shuffle(w2)
    def hits(ws): return {v:sum(1 for i in range(len(ws)-N+1) if ' '.join(ws[i:i+N]) in idx[v]) for v in vols}
    print(p,e[:40].replace('\n',' '),len(w),hits(w),'shuf',hits(w2))
print('---detail')
v='warofrebellion015201rootrich'; W=vols[v]
for p,e in sel:
    if (p,e[:20]) not in [(x,y[:20]) for x,y in sel if ('11 PM' in y or 'F. Swain' in y)]: continue
    w=words(re.sub(r'\{[^}]*\}','',e)); out=[]
    for i in range(len(w)-N+1):
        g=' '.join(w[i:i+N])
        if g in idx[v]: out.append((g,idx[v][g]))
    print(p,e[:30],out[:12])
