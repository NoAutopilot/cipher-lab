# A4-AVS175 (6 Oct 2026): prereg_avs175.md addendum "A4-AVS175" gate on WVO 175 p1 lines beyond AVS175's c1-c3.
# Same statistic, nulls and gate as gate.py, over the new lines only. Run from this folder: python3 gate_b.py [--check]
# Input: recon_b.json {"lines": {id: [sign codes, '?' unknown]}, "gl": {id: gloss as H-read}, "want": [real, rot_p95, shf_p95]}.
import json,csv,random,subprocess,sys,statistics,os
R=json.load(open('recon_b.json')); ids=sorted(R['lines'])
key={r['sign']:r['value'] for r in csv.DictReader(open('../key_98.tsv'),delimiter='\t')}
codes={};nx=[1];wn=[100];un=[50]
def code(t):
    if t in ('?',''): un[0]+=1; return str(un[0])
    if t not in codes:
        if len(key.get(t,''))==1: codes[t]=str(nx[0]); nx[0]+=1
        else: codes[t]=str(wn[0]); wn[0]+=1
    return codes[t]
cip={k:[code(t) for t in R['lines'][k]] for k in ids}
inv={v:k for k,v in codes.items()}
with open('prior_b.tsv','w') as f:
    f.write('code\tmeaning\n')
    for s,c in codes.items():
        if int(c)<50: f.write('%s\t%s\n'%(c,key[s]))
def run(gl,tag):
    p='pairs_b%s.tsv'%tag
    with open(p,'w') as f:
        f.write('plain_line\tplain_raw\tcipher_line\tcipher_raw\n')
        for i,k in enumerate(ids): f.write('%d\t%s\t%s\t%s\n'%(i,gl[k],k,' '.join(cip[k])))
    subprocess.run(['python3','../../../tools/interlinear_align.py','align',p,'al_b%s.tsv'%tag,'k_b%s.tsv'%tag,'--prior','prior_b.tsv','--keep-fs'],capture_output=True,check=True)
    rows=list(csv.reader(open('al_b%s.tsv'%tag),delimiter='\t'))[1:]
    hit=n=0; per=[]
    for r in rows:
        line,k,raw,kind,val,rep,chunk,st=r[:8]
        s=inv.get(raw); per.append((line,k,s,chunk))
        if s and len(key.get(s,''))==1 and int(raw)<50:
            n+=1; hit+=chunk.replace('v','u')==key[s].replace('v','u')
    if tag!='real':
        for f in (p,'al_b%s.tsv'%tag,'k_b%s.tsv'%tag): os.remove(f)
    return (hit/n if n else 0),n,per
real,n,per=run(R['gl'],'real')
rng=random.Random(1751); rot=[];shf=[]; m=len(ids)
for d in range(200):
    k=1+d%(m-1); g={}
    for i,c in enumerate(ids):
        s=R['gl'][ids[(i+k)%m]].replace(' ',''); o=rng.randrange(len(s)); g[c]=s[o:]+s[:o]
    rot.append(run(g,'r')[0]); g={}
    for c in ids:
        l=list(R['gl'][c].replace(' ','')); rng.shuffle(l); g[c]=''.join(l)
    shf.append(run(g,'s')[0])
p95=lambda x: sorted(x)[int(0.95*len(x))-1]
print('real %.3f on n=%d letter positions'%(real,n))
print('rotated mean %.3f p95 %.3f; shuffled mean %.3f p95 %.3f (200 draws each)'%(statistics.mean(rot),p95(rot),statistics.mean(shf),p95(shf)))
print('gate','PASS' if real>=0.60 and real>p95(rot) and real>p95(shf) else 'FAIL')
for t in per:
    if t[2] is None or len(key.get(t[2],'x'))!=1 or t[2] in ('Qf','Pf','1'): print(t)
if '--check' in sys.argv:
    got=[round(real,3),round(p95(rot),3),round(p95(shf),3)]
    print('check','OK' if got==R.get('want') else 'STALE %s'%got); sys.exit(0 if got==R.get('want') else 1)
