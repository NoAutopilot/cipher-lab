"""H41 fit: best alignment of a name to the r15-r18 token stream (key.tsv letters). S-graded tokens match exactly one
name letter (+1 equal, -1 unequal); M-graded / nomenclature tokens (grade M or code >= 48) are wildcards absorbing one
or two name letters at 0. The name must be aligned whole and contiguously; fit = best (matches - mismatches) over all
start positions. Null: the same fit for every name in namelist.tsv (built before scoring, names.py). Pre-registered:
a name is a crib candidate only if it is the list's unique best fit and P = share of list names fitting at least as well
is < 0.05."""
import csv,sys
key={r['code']:(r['letter'],r['grade']) for r in csv.DictReader(open('../key.tsv'),delimiter='\t')}
rows=[r for r in csv.DictReader(open('../cipher_codes_522.tsv'),delimiter='\t') if r['line'] in ('r15','r16','r17','r18')]
toks=[]; START=sys.argv[2] if len(sys.argv)>2 else None; on=START is None
for r in rows:
    if not on:
        on = f"{r['line']}:{r['position']}"==START
        if not on: continue
    l,g=key.get(r['sign'],('_','M')); wild = g!='S' or (r['sign'].isdigit() and int(r['sign'])>=48)
    toks.append((l,wild,f"{r['line']}:{r['position']}"))
def fit(name):
    best=(-99,None)
    for st in range(len(toks)):
        # DP over (token index from st, name index)
        from functools import lru_cache
        @lru_cache(None)
        def f(i,j):
            if j==len(name): return (0,())
            if st+i>=len(toks): return (-99,())
            l,w,loc=toks[st+i]
            if w:
                c=[(f(i+1,j+k)[0], f(i+1,j+k)[1]) for k in (1,2) if j+k<=len(name)]
                return max(c)
            s,path=f(i+1,j+1); return (s+(1 if l==name[j] else -1), path)
        s,_=f(0,0)
        if s>best[0]: best=(s,toks[st][2])
    return best
names=[l.split('\t')[0] for l in open('namelist.tsv') if l.strip()]
res=sorted(((fit(n),n) for n in names),key=lambda x:-x[0][0])
target=sys.argv[1] if len(sys.argv)>1 else 'burgsdorf'
ft=dict((n,f) for f,n in res)[target]
P=sum(1 for f,n in res if f[0]>=ft[0])/len(res)
print(f'list {len(res)} names; {target}: fit {ft[0]} at {ft[1]}; rank {1+sum(1 for f,n in res if f[0]>ft[0])}; P(list fit >= it) {P:.3f}')
print('top 12:',[(n,f[0],f[1]) for f,n in res[:12]])
