#!/usr/bin/env python3
"""Re-score a held-out pass from heldout_answers.tsv and a pass file (default heldout_passB.tsv, the LIKELY-6 pass of
2 Oct 2026, committed score 19/28); `--pass FILE --expect HIT/TOT` scores another pass (GAPS, 2 Oct 2026:
heldout_passC.tsv against the 264-extended atlas) and exits 1 if the committed numbers no longer reproduce. Order-preserving tag match (LCS); a trailing ' or ? on a
pass tag is ignored. Shuffle floor: pass tags permuted within crop, 2000 draws, seed 1.
GAPS-fr3986-2 (2 Oct 2026): `--answers heldout298_answers.tsv --pass pass298.tsv --expect H/T` scores the widened held-out
(c.298 cipher lines 1-3, 65 gloss-aligned signs, '#' comment lines skipped, unit column `line` instead of `crop`) and adds
the Wilson 95% interval, the floor's p95 and max, and the hit split old-28 / new-37 (LCS backtrace). Tag normalisation also
maps the Unicode forms a reader may write to the ASCII tags (pi, do, del, ls, lam, alpha, inT, phi, pl, theta, beta) and
strips a trailing '.'; the defaults (pass B 19/28, pass C 20/28) reproduce unchanged."""
import csv, os, random, sys, collections, argparse
ap=argparse.ArgumentParser(); ap.add_argument('--pass',dest='pf',default='heldout_passB.tsv'); ap.add_argument('--expect',default='19/28'); ap.add_argument('--answers',default='heldout_answers.tsv'); A=ap.parse_args()
H=os.path.dirname(os.path.abspath(__file__))
ans=collections.defaultdict(list); pas=collections.defaultdict(list)
rows=lambda f: csv.DictReader((l for l in open(f'{H}/{f}') if not l.startswith('#')),delimiter='\t')
unit=lambda r: r.get('crop') or r.get('line')
old=collections.defaultdict(list)
for r in rows(A.answers): ans[unit(r)].append(r['tag']); old[unit(r)].append(r.get('old','1')=='1')
for r in rows(A.pf): pas[unit(r)].append(r['tag'])
U={'π':'pi','ꝺo':'do','∂':'del','ſ':'ls','λ':'lam','∝':'alpha','⊥':'inT','φ':'phi','ꝑ':'pl','θ':'theta','ß':'beta'}
def norm(t):
    t=t.strip().rstrip("'?.")
    return U.get(t,t)
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
def matched(a,b):
    D=[[0]*(len(b)+1) for _ in range(len(a)+1)]
    for i in range(len(a)):
        for j in range(len(b)):
            D[i+1][j+1]=max(D[i][j+1],D[i+1][j],D[i][j]+(norm(a[i])==norm(b[j])))
    i,j,m=len(a),len(b),set()
    while i and j:
        if norm(a[i-1])==norm(b[j-1]) and D[i][j]==D[i-1][j-1]+1: m.add(i-1); i-=1; j-=1
        elif D[i-1][j]>=D[i][j-1]: i-=1
        else: j-=1
    return m
z=1.96; p=hit/tot; c=(p+z*z/(2*tot))/(1+z*z/tot); w=z*((p*(1-p)/tot+z*z/(4*tot*tot))**.5)/(1+z*z/tot)
fs=sorted(fl)
print(f"held-out {hit}/{tot} = {100*hit/tot:.1f}%; shuffle floor mean {100*sum(fl)/len(fl):.1f}%")
print(f"Wilson 95% CI {100*(c-w):.1f}-{100*(c+w):.1f}%; floor p95 {100*fs[int(.95*len(fs))]:.1f}% max {100*fs[-1]:.1f}%; gate 80%")
if A.answers!='heldout_answers.tsv':
    ho=hn=to_=tn=0
    for k in ans:
        m=matched(ans[k],pas[k])
        for i,o in enumerate(old[k]):
            if o: to_+=1; ho+=(i in m)
            else: tn+=1; hn+=(i in m)
    print(f"old 28 (LIKELY-6 signs, now inside whole-line crops): {ho}/{to_}; new: {hn}/{tn}")
eh,et=map(int,A.expect.split('/'))
for k in ans: print(k, f'{lcs(ans[k],pas[k])}/{len(ans[k])}', 'answer:', ' '.join(ans[k]), '| pass:', ' '.join(pas[k]))
print('absent-from-264only tags hit:', sum(1 for k in ans for t in ans[k] if t in {'//','20','8','=','L40','c','r','ue'}), 'of answer positions carry them')
sys.exit(0 if (hit,tot)==(eh,et) else 1)
