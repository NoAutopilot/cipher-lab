# AVS175 (3 Oct 2026): pre-registered gate of prereg_avs175.md on WVO 175 p1 c1-c3. Run from this folder: python3 gate.py --check
# Inputs: enc.json (from mk.py over recon.json), prior.tsv (key_98 letter values). Null draws seeded (random.Random(175)).
import json,csv,random,subprocess,sys,statistics,os
E=json.load(open('enc.json')); codes=E['codes']; inv={v:k for k,v in codes.items()}
key={r['sign']:r['value'] for r in csv.DictReader(open('../key_98.tsv'),delimiter='\t')}
ids=['c1','c2','c3']
def run(glosses,tag):
    p='pairs_%s.tsv'%tag
    with open(p,'w') as f:
        f.write('plain_line\tplain_raw\tcipher_line\tcipher_raw\n')
        for i,k in enumerate(ids): f.write('%d\t%s\t%s\t%s\n'%(i,glosses[k],k,' '.join(E['cip'][k])))
    subprocess.run(['python3','../../../tools/interlinear_align.py','align',p,'al_%s.tsv'%tag,'k_%s.tsv'%tag,'--prior','prior.tsv','--keep-fs'],capture_output=True,check=True)
    rows=list(csv.reader(open('al_%s.tsv'%tag),delimiter='\t'))[1:]
    hit=n=0; per=[]
    for r in rows:
        line,k,raw,kind,val,rep,chunk,st=r[:8]
        s=inv.get(raw)
        per.append((line,k,s,chunk))
        if s and len(key.get(s,''))==1 and int(raw)<50:
            n+=1; hit+= chunk.replace('v','u')==key[s].replace('v','u')
    for f in (p,'al_%s.tsv'%tag,'k_%s.tsv'%tag):
        if tag!='real': os.remove(f)
    return hit/n if n else 0, n, per
real,n,per=run(E['gl'],'real')
rng=random.Random(175)
rot=[];shf=[]
for d in range(200):
    k=1+d%2; g={}
    for i,c in enumerate(ids):
        s=E['gl'][ids[(i+k)%3]].replace(' ',''); o=rng.randrange(len(s)); g[c]=s[o:]+s[:o]
    rot.append(run(g,'r')[0])
    g={}
    for c in ids:
        l=list(E['gl'][c].replace(' ','')); rng.shuffle(l); g[c]=''.join(l)
    shf.append(run(g,'s')[0])
p95=lambda x: sorted(x)[int(0.95*len(x))-1]
print('real %.3f on n=%d letter positions'%(real,n))
print('rotated mean %.3f p95 %.3f; shuffled mean %.3f p95 %.3f (200 draws each)'%(statistics.mean(rot),p95(rot),statistics.mean(shf),p95(shf)))
print('gate', 'PASS' if real>=0.60 and real>p95(rot) and real>p95(shf) else 'FAIL')
for t in per:
    if t[2] in ('NW','HX','M','4','1') or t[2] is None: print(t)
# --check: exit 1 if the committed figures (AVS175, 3 Oct 2026) no longer reproduce
if '--check' in sys.argv:
    want=(0.615,0.385,0.446)
    got=(round(real,3),round(p95(rot),3),round(p95(shf),3))
    print('check', 'OK' if got==want else 'STALE %s'%(got,)); sys.exit(0 if got==want else 1)
