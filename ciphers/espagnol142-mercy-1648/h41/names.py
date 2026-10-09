# promoted to tools/name_candidates.py --index (h41_surnames) (MQS-NAMES, 9 Oct 2026); kept because its outputs are cited
"""H41 name list, built before scoring from a named printed source: Urkunden und Actenstücke zur Geschichte des
Kurfürsten Friedrich Wilhelm von Brandenburg, Bd. 4 (1867) and Bd. 5 (1869), Internet Archive
urkundenundacten04berluoft / urkundenundacten05berluoft, _djvu.txt OCR. Surnames = the word after von / v. / Graf(en) /
Freiherr(n) / Herr(n) / Oberst / Kanzler, or a capitalised word with a possessive 's; folded (umlauts dropped to the
base letter, ß->ss, j->i, v->u, w->uu as the target's alphabet has no w), 6-12 letters, seen at least twice."""
import re,sys,unicodedata
from collections import Counter
def fold(w):
    w=unicodedata.normalize('NFKD',w.lower()); w=''.join(c for c in w if not unicodedata.combining(c))
    return re.sub('[^a-z]','',w.replace('ß','ss').replace('j','i').replace('v','u').replace('w','uu').replace('k','c'))
c=Counter()
for f in sys.argv[1:]:
    t=open(f,encoding='utf-8',errors='replace').read()
    for m in re.finditer(r"\b(?:von|v\.|Graf|Grafen|Freiherr|Freiherrn|Herr|Herrn|Oberst|Kanzler)\s+([A-ZÄÖÜ][a-zäöüß]{4,14})\b",t): c[m.group(1)]+=1
    for m in re.finditer(r"\b([A-ZÄÖÜ][a-zäöüß]{4,14})'s\b",t): c[m.group(1)]+=1
out={}
for w,n in c.items():
    f=fold(w)
    if 6<=len(f)<=12 and n>=2: out[f]=out.get(f,0)+n
for f,n in sorted(out.items(),key=lambda x:-x[1]): print(f'{f}\t{n}')
