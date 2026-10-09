# AUD2-SIG-228 (9 Oct 2026): b167228/judge_null.py with the token file pointed at a scratch re-decode in which b167228/sig_marks.tsv was emptied (the 15 SIG-B228 mark regrades not applied); replace SCRATCH with that copy. Output: judge_corrected.out.
# B167-228 (8 Oct 2026): fr17 judge on reading_b170f228 cipher tokens vs shuffled-key nulls (20 each, seed 20261008); copy of d4vb167/judge_null.py.
# Unread (U) tokens are dropped from the text. Positive control: the first N cipher tokens of reading_b170f229 (same N, same judge).
# Run from repo root: python3 ciphers/baluze167-davaux-1637/d4vb167/judge_null.py <scratch dir containing spec.json>
import csv,random,subprocess,json,sys,statistics
S=sys.argv[1]
r=[t for t in csv.DictReader(open('SCRATCH/reading_tokens_b170f228.tsv'),delimiter='\t') if t['grade']!='U']
def text(rows,m=None,keep_w=False):
    out=[]
    for t in rows:
        if t['sign'].startswith('w:'):
            if keep_w: out.append(t['value'])
            continue
        out.append(m.get(t['sign'],t['value']) if m else t['value'])
    return ' '.join(out)
def judge(s,name):
    p=f'{S}/{name}.txt'; open(p,'w').write(s)
    o=subprocess.run(['python3','tools/judge_plaintext.py',f'{S}/spec.json','--file',p,'--json'],capture_output=True,text=True).stdout
    return json.loads(o)['checks']['language']
nc=[t for t in r if not t['sign'].startswith('w:')]
print('cipher tokens',len(nc),'letters',sum(c.isalpha() for c in text(r)))
res=judge(text(r),'real_cipher'); print('REAL cipher-only',res)
print('REAL with clear words',judge(text(r,keep_w=True),'real_all'))
signs=sorted({t['sign'] for t in nc}); vals={t['sign']:t['value'] for t in nc}
lsig=[s for s in signs if s.startswith('L:')]
rng=random.Random(20261008)
for kind,pool in (('all-signs',signs),('letter-signs-only',lsig)):
    sc=[]
    for i in range(20):
        perm=pool[:]; rng.shuffle(perm)
        m={a:vals[b] for a,b in zip(pool,perm)}
        sc.append(judge(text(r,m),f'null_{kind}_{i}')['score'])
    sc.sort(); print(kind,'n=20 min %.3f median %.3f max %.3f'%(sc[0],statistics.median(sc),sc[-1]))
N=len(nc)
p=[t for t in csv.DictReader(open('ciphers/baluze167-davaux-1637/reading_tokens_b170f229.tsv'),delimiter='\t') if not t['sign'].startswith('w:') and t['grade']!='U']
for off in (0,N,2*N):
    seg=p[off:off+N]; print('POSITIVE f229 tokens %d-%d'%(off,off+len(seg)),judge(' '.join(t['value'] for t in seg),f'pos_{off}'))
