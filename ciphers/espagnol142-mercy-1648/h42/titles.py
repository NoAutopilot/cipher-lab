"""H42 title list, built before scoring: every word X in "X mayor" in the es17c7 Cartas corpus (tools/data/es17c7,
seven tomes of the Memorial histórico español Cartas 1634-1648), folded as the target is (j->i, v->u), X of 4-12
letters, 3+ occurrences."""
import sys,glob,gzip,re
from collections import Counter
sys.path.insert(0,'../../../tools'); import homophonic_anneal as H
c=Counter()
for f in sorted(glob.glob('../../../tools/data/es17c7/*.txt.gz')):
    w=[H.fold(x) for x in re.findall(r"[^\W\d_]+",gzip.open(f,'rt',encoding='utf-8').read())]
    for a,b in zip(w,w[1:]):
        if b=='mayor' and 4<=len(a)<=12: c[a]+=1
for a,n in c.most_common():
    if n>=3: print(f'{a}\t{n}')
