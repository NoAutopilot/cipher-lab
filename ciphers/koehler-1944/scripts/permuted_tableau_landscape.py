import sys, time, random; sys.path.insert(0,'tools')
import families, running_key as rk
from families import draw_window
pt=families.load('permuted_tableau')
de=[rk.read_text(b) for b in rk.list_books(['tools/data/de20'])]
nl=[rk.read_text(b) for b in rk.list_books(['tools/data/nl20'])]
rng=random.Random(1)
idx=list(range(7)); rng.shuffle(idx); pi=idx[0]; kidx=list(range(7)); rng.shuffle(kidx)
ktext,ktrain=nl[kidx[0]],[nl[i] for i in kidx[1:]]; ptrain=[de[i] for i in idx[1:]]
S3=list(range(26)); rng.shuffle(S3); tab=pt.perm_tabula(None,None,S3,'vig')
ptext,kt=rk.fold(de[pi]),rk.fold(ktext)
msgs=[];plains=[]
for n in [237,178,140,140,229]:
    P,_=draw_window(ptext,n,rng.randrange(10**6)); K,_=draw_window(kt,n,rng.randrange(10**6))
    msgs.append([rk.A[rk.encipher(tab,rk.IDX[x],rk.IDX[y])] for x,y in zip(P,K)]); plains.append(P)
# (1) proxy: true vs anneal winner, orders 2,3,4
for order in (2,3,4):
    t=time.time(); cnt=pt.sum_stream_counts(ptrain,ktrain,order,3,1); logT=pt.sum_table(cnt,order,0.5); px=pt.Proxy(msgs,logT,order)
    true=px.score(pt.inverse(S3)); r=random.Random(5)
    rnd=[px.score(r.sample(range(26),26)) for _ in range(100)]
    inv,sc,ne,T0=pt.anneal(px,pt.inverse(pt.sort_match_start([sum(m.count(x) for m in msgs) for x in rk.A],pt.unigram(ptrain),pt.unigram(ktrain))),30000,6000,r)
    e,bs,tt=pt.letters_correct(pt.inverse(inv),S3)
    print(f"order {order}: true {true:.1f} random mean {sum(rnd)/100:.1f} max {max(rnd):.1f} anneal {sc:.1f} ({ne} evals, letters {e}/{bs}) build {time.time()-t:.0f}s",flush=True)
# (2) decoder landscape at anneal settings vs k swaps from truth
lmp,lmk=pt._models(ptrain,ktrain,5,0.9,True)
sel="".join(msgs[0])[:140]
def dec(S):
    d=rk.decode_message(sel,lmp,lmk,pt.perm_tabula(None,None,S,'vig'),80,10,False,True); return d['ll_joint']
print("truth",round(dec(S3),3),flush=True)
r=random.Random(3)
for k in (1,2,3,5,8,13):
    vals=[]
    for rep in range(2):
        S=list(S3)
        for _ in range(k):
            a,b=r.sample(range(26),2); S[a],S[b]=S[b],S[a]
        vals.append(round(dec(S),3))
    print(f"{k} swaps from truth: {vals}",flush=True)
Srand=r.sample(range(26),26); print("random S3",round(dec(Srand),3),flush=True)
# (3) proxy anneal vs length, English (Holmes plain, Moby key), order 3
hol=rk.fold(rk.read_text('tools/data/pg1661_holmes.txt')); mob=rk.fold(rk.read_text('tools/data/pg2701_mobydick.txt'))
for N in (2000,6000):
    r=random.Random(N); S=r.sample(range(26),26); tb=pt.perm_tabula(None,None,S,'vig')
    P=hol[200000:200000+N]; K=mob[300000:300000+N]
    m=[[rk.A[rk.encipher(tb,rk.IDX[x],rk.IDX[y])] for x,y in zip(P,K)]]
    ptr=[hol[:150000],hol[260000:]]; ktr=[mob[:250000],mob[400000:]]
    t=time.time(); cnt=pt.sum_stream_counts(ptr,ktr,3,3,1); logT=pt.sum_table(cnt,3,0.5); px=pt.Proxy(m,logT,3)
    true=px.score(pt.inverse(S))
    start=pt.inverse(pt.sort_match_start([m[0].count(x) for x in rk.A],pt.unigram(ptr),pt.unigram(ktr)))
    inv,sc,ne,T0=pt.anneal(px,start,30000,6000,r); e,bs,tt=pt.letters_correct(pt.inverse(inv),S)
    print(f"english N={N} order 3: true {true:.1f} anneal {sc:.1f} letters {e}/{bs} (shift {tt}) {ne} evals {time.time()-t:.0f}s",flush=True)
