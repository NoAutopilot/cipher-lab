import sys, os, random
HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__))); sys.path.insert(0, HERE)
os.chdir(HERE)
from f61crib import FOLDS, load_read, fit, score, load_spans
from f61crib3 import load_cells, cell_map, values, OPTS
from f61crib4 import split_lines
lines, spans, cells = split_lines(load_read()), load_spans(), load_cells()
by = {s:(s,l,m) for s,l,m in spans}
seed=int(sys.argv[1]); NC=int(sys.argv[2]); rng=random.Random(seed)
folds=[]
pooled=tot_all=0
for held in FOLDS:
    train=[by[s] for s in by if s not in held]; test=[by[s] for s in held]
    cm=cell_map(fit(train,lines,"v_"+"".join(held),OPTS,keep_dashes=True),cells); kmap=values(cm)
    mt,tot=score(kmap,lines,test); pooled+=mt; tot_all+=tot
    folds.append((kmap,test,tot))
ctrl=[0]*NC
for k in range(NC):
    for kmap,test,tot in folds:
        labs=sorted(kmap); v=[kmap[l] for l in labs]; rng.shuffle(v)
        ctrl[k]+=score(dict(zip(labs,v)),lines,test)[0]
pc=sorted(c/tot_all for c in ctrl)
ge=sum(1 for c in ctrl if c>=pooled)
print(f"seed {seed} target {pooled}/{tot_all}={pooled/tot_all:.3f}; {NC} perms: mean {sum(pc)/NC:.3f} p95 {pc[int(.95*NC)]:.3f} p99 {pc[int(.99*NC)]:.3f} max {pc[-1]:.3f}; perms >= target {ge} (p <= {(ge+1)/(NC+1):.4f})")
