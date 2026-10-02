# BIRAGO-NUM3 objective check: true cut+key objective vs solver (python3 oracle_check.py SEED CELLS)
import sys,random;sys.path.insert(0,'/home/user/cipher-lab/tools')
import judge_plaintext as jp, glob, homophonic_anneal as ha
from families import phased_homophonic as f
corp=[jp.read_corpus(p) for p in sorted(glob.glob('/home/user/cipher-lab/tools/data/it16dip/*.txt.gz'))]
runs=[l.split() for l in open('/home/user/cipher-lab/ciphers/birago-fr3252-1571-72/num/joint/runs_digits.txt') if not l.startswith('#') and l.strip()]
s=int(sys.argv[1]); cells=sys.argv[2]
p={'lengths':[len(r) for r in runs],'target_msgs':runs,'cells':cells}
cm,truth,train=f.make_control({},s,corp,dict(p))
model=ha.Model(train,3)
# true cut and key
toks=[];key={};pos=0
for m in cm:
    t=[];i=0
    while i<len(m):
        if truth[pos+i]=='-': t.append(m[i]); i+=1
        else: pr=m[i]+m[i+1]; key[pr]=truth[pos+i]; t.append(pr); i+=2
    toks.append(t); pos+=len(m)
for a in '0123456789':
    for b in '0123456789': key.setdefault(a+b,'e')
print("true objective", round(f._objective(toks,key,model,1.0,-9.0,1.0),1))
seq=[x for t in toks for x in t if len(x)==2]
res=ha.solve(seq,model,16,100000,1,1.0)
sc,k=res[0]
acc=sum(k[x]==key[x] for x in seq)/len(seq)
print('oracle-cut anneal 16 restarts: acc %.3f score %.1f true-key score %.1f'%(acc,sc,ha.score(model,''.join(key[x] for x in seq),1.0)))
