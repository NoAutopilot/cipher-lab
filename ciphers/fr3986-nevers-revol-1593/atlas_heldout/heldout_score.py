#!/usr/bin/env python3
"""Re-score the LIKELY-6 held-out pass (2 Oct 2026) from heldout_answers.tsv and heldout_passB.tsv; exit 1 if the
committed numbers in score.txt (19/28) no longer reproduce. Order-preserving tag match (LCS); a trailing ' or ? on a
pass tag is ignored. Shuffle floor: pass tags permuted within crop, 2000 draws, seed 1."""
import csv, os, random, sys, collections
H=os.path.dirname(os.path.abspath(__file__))
ans=collections.defaultdict(list); pas=collections.defaultdict(list)
for r in csv.DictReader(open(f'{H}/heldout_answers.tsv'),delimiter='\t'): ans[r['crop']].append(r['tag'])
for r in csv.DictReader(open(f'{H}/heldout_passB.tsv'),delimiter='\t'): pas[r['crop']].append(r['tag'])
norm=lambda t: t.rstrip("'").rstrip('?')
def lcs(a,b):
    D=[[0]*(len(b)+1) for _ in range(len(a)+1)]
    for i in range(len(a)):
        for j in range(len(b)):
            D[i+1][j+1]=max(D[i][j+1],D[i+1][j],D[i][j]+(norm(a[i])==norm(b[j])))
    return D[len(a)][len(b)]
tot=sum(len(v) for v in ans.values()); hit=sum(lcs(ans[k],pas[k]) for k in ans)
random.seed(1); fl=[]
for _ in range(2000):
    s=0
    for k in ans:
        b=pas[k][:]; random.shuffle(b); s+=lcs(ans[k],b)
    fl.append(s/tot)
print(f"held-out {hit}/{tot} = {100*hit/tot:.1f}%; shuffle floor mean {100*sum(fl)/len(fl):.1f}%")
sys.exit(0 if (hit,tot)==(19,28) else 1)
