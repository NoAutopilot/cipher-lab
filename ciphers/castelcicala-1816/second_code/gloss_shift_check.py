# A2-CAS5, 2 Oct 2026. Cross-line consistency of the image-read pencil anchors (gloss_image_anchors.tsv), with a
# control that can fail differently: every line's gloss is shifted k groups (k=-2..+2, one shift per line, all
# 5^n combinations, n = lines with H/M confidence) and we count, per combination, group->gloss agreements across
# lines (same group, same gloss in two lines) and conflicts (same group, different gloss). The image placement is k=0
# on every line. Usage: python3 gloss_shift_check.py [--all] (--all includes the L-confidence lines).
import itertools,os,sys,collections
D=os.path.dirname(os.path.abspath(__file__))
rows=[l.rstrip('\n').split('\t') for l in open(os.path.join(D,'gloss_image_anchors.tsv')) if l.strip() and not l.startswith('#')]
rows=[r for r in rows if '--all' in sys.argv or r[4] in 'HM']
lines=[(r[0]+r[1],r[2].split(),r[3].split()) for r in rows]
def score(shifts):
    m=collections.defaultdict(set);hits=collections.Counter()
    for (lab,c,g),k in zip(lines,shifts):
        for i,s in enumerate(g):
            if s=='-': continue
            j=i+k
            if 0<=j<len(c): m[c[j]].add(s);hits[(c[j],s)]+=1
    agree=sum(1 for v in hits.values() if v>=2); conf=sum(1 for v in m.values() if len(v)>=2)
    return agree,conf
base=score([0]*len(lines))
res=[score(s) for s in itertools.product(range(-2,3),repeat=len(lines))]
n=len(res);ge=sum(1 for a,c in res if a>=base[0] and c<=base[1])
print('lines',len(lines),'combinations',n)
print('image placement (k=0): agreements %d conflicts %d'%base)
print('shifted: mean agreements %.2f mean conflicts %.2f; combinations with >=%d agreements and <=%d conflicts: %d (%.4f)'%(sum(a for a,_ in res)/n,sum(c for _,c in res)/n,base[0],base[1],ge,ge/n))
m=collections.defaultdict(list)
for lab,c,g in lines:
    for x,s in zip(c,g):
        if s!='-': m[x].append(s+'@'+lab)
print('groups glossed in >=2 lines:',{k:v for k,v in m.items() if len(v)>=2})
