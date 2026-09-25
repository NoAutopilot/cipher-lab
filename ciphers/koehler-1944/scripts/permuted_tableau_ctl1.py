import sys, time, json; sys.path.insert(0,'tools')
import families, running_key as rk
seed=int(sys.argv[1]); extra=dict(kv.split('=') for kv in sys.argv[2:])
fam=families.load('permuted_tableau')
de=[rk.read_text(b) for b in rk.list_books(['tools/data/de20'])]
params={'N':924,'K':26,'lengths':[237,178,140,140,229],'messages_independent':True,'kcorpus':'tools/data/nl20','arith':'vig'}
params.update(extra)
t=time.time()
cm,plain,train=fam.make_control(None,seed,de,dict(params))
dec,sc,info=fam.solve(cm,None,seed,1,train,dict(params))
rec=fam.score_recovery(dec,plain)
print(f"CONTROL seed {seed}: recovery {rec:.3f} score {sc:.3f} S3 correct {info['S3_letters_correct']} sort {info['S3_sort_letters_correct']} {time.time()-t:.0f}s")
print(dec[:80]); print(plain[:80])
