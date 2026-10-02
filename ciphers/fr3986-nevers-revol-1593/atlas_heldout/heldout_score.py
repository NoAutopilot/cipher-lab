#!/usr/bin/env python3
"""Re-score a held-out pass from heldout_answers.tsv and a pass file (default heldout_passB.tsv, the LIKELY-6 pass of
2 Oct 2026, committed score 19/28); `--pass FILE --expect HIT/TOT` scores another pass (GAPS, 2 Oct 2026:
heldout_passC.tsv against the 264-extended atlas) and exits 1 if the committed numbers no longer reproduce. Order-preserving tag match (LCS); a trailing ' or ? on a
pass tag is ignored. Shuffle floor: pass tags permuted within crop, 2000 draws, seed 1."""
import csv, os, random, sys, collections, argparse
ap=argparse.ArgumentParser(); ap.add_argument('--pass',dest='pf',default='heldout_passB.tsv'); ap.add_argument('--expect',default='19/28'); A=ap.parse_args()
H=os.path.dirname(os.path.abspath(__file__))
ans=collections.defaultdict(list); pas=collections.defaultdict(list)
for r in csv.DictReader(open(f'{H}/heldout_answers.tsv'),delimiter='\t'): ans[r['crop']].append(r['tag'])
for r in csv.DictReader(open(f'{H}/{A.pf}'),delimiter='\t'): pas[r['crop']].append(r['tag'])
norm=lambda t: t.rstrip("'?")
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
eh,et=map(int,A.expect.split('/'))
for k in ans: print(k, f'{lcs(ans[k],pas[k])}/{len(ans[k])}', 'answer:', ' '.join(ans[k]), '| pass:', ' '.join(pas[k]))
print('absent-from-264only tags hit:', sum(1 for k in ans for t in ans[k] if t in {'//','20','8','=','L40','c','r','ue'}), 'of answer positions carry them')
sys.exit(0 if (hit,tot)==(eh,et) else 1)
