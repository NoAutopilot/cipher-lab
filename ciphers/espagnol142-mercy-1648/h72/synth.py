"""H72: synthetic-name null. A character trigram model (add-0.1) trained on the 883-name list (h61/names_bd1to6.tsv,
word boundaries as ^ and $) samples 10,000 name-shaped strings of 6-12 letters (seed 72; list names themselves
dropped); each fitted to r16:2-r18:21 with tools/crib_list_fit.py (default wildcards). Reported: the share with a fit
>= 7 and 0 mismatches (Burgsdorf's), and the share >= 6."""
import sys,random
from collections import Counter,defaultdict
sys.path.insert(0,'../../tools'); import crib_list_fit as clf
names=[l.split('\t')[0] for l in open('h61/names_bd1to6.tsv') if l.strip()]
A=sorted(set(''.join(names)))+['$']; tri=defaultdict(Counter)
for n in names:
    w='^^'+n+'$'
    for i in range(len(w)-2): tri[w[i:i+2]][w[i+2]]+=1
rng=random.Random(72)
def sample():
    ctx='^^'; out=''
    while True:
        c=tri[ctx]; opts=A; wts=[c[a]+0.1 for a in A]
        ch=rng.choices(opts,wts)[0]
        if ch=='$' or len(out)>=14: return out
        out+=ch; ctx=ctx[1]+ch
S=set(names); synth=[]
while len(synth)<10000:
    s=sample()
    if 6<=len(s)<=12 and s not in S: synth.append(s)
toks=clf.load_window('cipher_codes_522.tsv','key.tsv','r16:2','r18:21')
f7=f6=0; best=[]
for s in synth:
    sc,ag,mm,at=clf.fit(s,toks)
    if sc>=7 and mm==0: f7+=1
    if sc>=6: f6+=1
    best.append((sc,ag,mm,s,at))
best.sort(reverse=True)
print(f'10000 synthetic names: fit >= 7 with 0 mismatches {f7} ({f7/100:.2f}%); fit >= 6 {f6} ({f6/100:.2f}%)')
print('top 10:',best[:10])
