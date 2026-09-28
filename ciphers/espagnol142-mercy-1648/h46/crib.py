"""H46: which word follows "y que corra por su" at v04? List built before scoring: every word after "por su" in the
es17c7 Cartas corpus, 4-12 letters, 3+ occurrences (folded as the target). Each word aligned to the start of v04 with
H41's scorer (S-graded tokens +1/-1, M and nomenclature tokens one-or-two-letter wildcards; start fixed at v04:1).
Pre-registered: a candidate only as the list's unique best with P < 0.05."""
import sys,glob,gzip,re,csv
from collections import Counter
sys.path.insert(0,'../../../tools'); import homophonic_anneal as H
c=Counter()
for f in sorted(glob.glob('../../../tools/data/es17c7/*.txt.gz')):
    w=[H.fold(x) for x in re.findall(r"[^\W\d_]+",gzip.open(f,'rt',encoding='utf-8').read())]
    for a,b,d in zip(w,w[1:],w[2:]):
        if a=='por' and b=='su' and 4<=len(d)<=12: c[d]+=1
words=[w for w,n in c.items() if n>=3]
open('wordlist.tsv','w').write(''.join(f'{w}\t{c[w]}\n' for w in sorted(words,key=lambda w:-c[w])))
key={r['code']:(r['letter'],r['grade']) for r in csv.DictReader(open('../key.tsv'),delimiter='\t')}
toks=[]
for r in csv.DictReader(open('../cipher_codes_522.tsv'),delimiter='\t'):
    if r['line'] in ('v04','v05'):
        l,g=key.get(r['sign'],('_','M')); toks.append((l, g!='S' or (r['sign'].isdigit() and int(r['sign'])>=48)))
from functools import lru_cache
def fit(name):
    @lru_cache(None)
    def f(i,j):
        if j==len(name): return 0
        if i>=len(toks): return -99
        l,w=toks[i]
        if w: return max(f(i+1,j+k) for k in (1,2) if j+k<=len(name))
        return f(i+1,j+1)+(1 if l==name[j] else -1)
    return f(0,0)
res=sorted(((fit(w),w) for w in words),reverse=True)
top=res[0][0]; n_top=sum(1 for s,w in res if s==top)
print('v04 letters:',''.join('?' if w else l for l,w in toks[:20]))
print(f'{len(res)} words; top fit {top} by {n_top} word(s): {[w for s,w in res if s==top]}; P(top) {n_top/len(res):.3f}')
print('top 15:',res[:15])
