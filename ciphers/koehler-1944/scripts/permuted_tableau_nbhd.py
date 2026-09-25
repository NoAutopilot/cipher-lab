import sys, time; sys.path.insert(0,'tools')
import families, running_key as rk
seed=int(sys.argv[1]); S3s=sys.argv[2]; part=int(sys.argv[3]); nparts=int(sys.argv[4])
pt=families.load('permuted_tableau')
de=[rk.read_text(b) for b in rk.list_books(['tools/data/de20'])]
params={'N':924,'K':26,'lengths':[237,178,140,140,229],'messages_independent':True,'kcorpus':'tools/data/nl20','arith':'vig'}
cm,plain,train=pt.make_control(None,seed,de,dict(params))
truth=pt._STATE['truth']; ktrain=pt._STATE['ktrain']
lmp,lmk=pt._models(train,ktrain,5,0.9,True)
sel="".join(cm[0])[:140]
S3=[rk.IDX[c] for c in S3s]
def dec(S): return rk.decode_message(sel,lmp,lmk,pt.perm_tabula(None,None,S,'vig'),80,10,False,True)['ll_joint']
if part==0: print("base",round(dec(S3),4),pt.letters_correct(S3,truth),flush=True)
i=0
for x in range(26):
    for y in range(x+1,26):
        if i%nparts==part:
            inv=pt.inverse(S3); inv[x],inv[y]=inv[y],inv[x]; S=pt.inverse(inv)
            e,bs,t=pt.letters_correct(S,truth)
            print(f"swap {rk.A[x]}{rk.A[y]} {dec(S):.4f} {e} {bs}",flush=True)
        i+=1
