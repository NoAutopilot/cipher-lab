"""H47: given name before the Burgsdorf candidate. List built before scoring: every capitalised word standing directly
before "von <Capitalised>" in Urkunden und Actenstücke Bd. 4-5 (IA urkundenundacten04berluoft / 05berluoft _djvu.txt,
the H41 downloads), folded as H41 (umlauts to base, ß->ss, j->i, v->u, w->uu, k->c), 4-10 letters, 2+ occurrences;
Spanish forms of the list's names are not added (the list is what it is). Each name X is fitted as "X" and as "Xde"
ending exactly at r16:15 (the token before "burgs"), with H41's scorer (S +1/-1, M and nomenclature tokens wildcards
for 1-2 letters). Pre-registered (CAMPAIGN.md H47): unique best, P < 0.05, >= 60% of letters agreeing at S tokens,
at most one mismatch."""
import re,sys,csv,unicodedata
from collections import Counter
from functools import lru_cache
def fold(w):
    w=unicodedata.normalize('NFKD',w.lower()); w=''.join(c for c in w if not unicodedata.combining(c))
    return re.sub('[^a-z]','',w.replace('ß','ss').replace('j','i').replace('v','u').replace('w','uu').replace('k','c'))
c=Counter()
for f in sys.argv[1:]:
    t=open(f,encoding='utf-8',errors='replace').read()
    for m in re.finditer(r"\b([A-ZÄÖÜ][a-zäöüß]{2,12})\s+(?:von|v\.)\s+[A-ZÄÖÜ]",t): c[fold(m.group(1))]+=1
stop={'herrn','herr','graf','grafen','freiherr','freiherrn','oberst','kanzler','fürsten','fursten','generals','general','rath','herzog','herzogs','kurfürst','churfursten','den','dem','des','der','die','und'}
names=sorted(w for w,n in c.items() if 4<=len(w)<=10 and n>=2 and w not in stop)
open('namelist.tsv','w').write(''.join(f'{w}\t{c[w]}\n' for w in sorted(names,key=lambda w:-c[w])))
key={r['code']:(r['letter'],r['grade']) for r in csv.DictReader(open('../key.tsv'),delimiter='\t')}
toks=[]
for r in csv.DictReader(open('../cipher_codes_522.tsv'),delimiter='\t'):
    if r['line'] in ('r15','r16'):
        l,g=key.get(r['sign'],('_','M')); toks.append((l, g!='S' or (r['sign'].isdigit() and int(r['sign'])>=48), f"{r['line']}:{r['position']}"))
    if r['line']=='r16' and r['position']=='15': break
toks=toks[::-1]   # align backwards from r16:15
def fit(name):
    nm=name[::-1]
    @lru_cache(None)
    def f(i,j):
        if j==len(nm): return (0,0,0)
        if i>=len(toks): return (-99,0,0)
        l,w,_=toks[i]
        if w: return max(f(i+1,j+k) for k in (1,2) if j+k<=len(nm))
        s,m,x=f(i+1,j+1); eq=l==nm[j]
        return (s+(1 if eq else -1), m+eq, x+(not eq))
    return f(0,0)
res=[]
for n in names:
    for form in (n, n+'de'):
        s,m,x=fit(form); res.append((s,m,x,form))
res.sort(reverse=True)
best=res[0]; tie=sum(1 for r in res if r[0]==best[0])
P=tie/len(res); ok=tie==1 and P<0.05 and best[1]>=0.6*len(best[3]) and best[2]<=1
print(f'{len(names)} names, {len(res)} forms; window ending r16:15 reads (backwards-aligned) ...{"".join("?" if w else l for l,w,_ in toks[::-1][-14:])}')
print(f'best {best}; ties {tie}; P {P:.3f}; rule met: {ok}')
print('top 12:',res[:12])
for f in ('conrad','conradde','conrado','conradode'):
    print(f,fit(f))
