# V6 (LANE V2, 24 Sept 2026): align reading_5200_p1.txt to Groen IV no. CCCLXXXIX (DBNL snapshot) and count
# how many key-decoded (lowercase) letters land on the same letter in Groen's print. Run from this folder.
import re,unicodedata,sys,subprocess
SRC='../../sources/dbnl/groe009arch04_01_0004.html'
def norm(c):
    c=unicodedata.normalize('NFD',c.lower())[0]
    return {'j':'i','v':'u','w':'x'}.get(c,c)
g=subprocess.run(['python3','../../tools/html2text.py',SRC],capture_output=True,text=True).stdout
a=g.index('Monsieur mon frère. J'); b=g.index('sinon après que ils ouirent')+len('sinon')
gt=re.sub(r'Ga naar voetnoot\S*\s*\[#\d+\]','',g[a:b])
gt=re.sub(r'\[pagina \d+\]|\[p\. \d+\]|Ga naar margenoot\+ \[#\d+\]','',gt)
G=[norm(c) for c in gt if c.isalpha()]
R=[]  # (char, kind)
for line in open('reading_5200_p1.txt'):
    if line.startswith('#'): continue
    _,txt=line.rstrip('\n').split('\t',1)
    txt=re.sub(r'\[[^\]]*\]',' ',txt)
    for w in txt.split():
        kind='clear' if (w.isupper() or not w.isalpha()) and len(re.sub(r'\W','',w))>1 else 'cipher'
        if len(re.sub(r'\W','',w))==1 and w.isupper(): kind='clearL'
        for c in w:
            if c.isalpha(): R.append((norm(c),kind))
n,m=len(R),len(G)
# global-local: free end gaps in G
import array
MA,MI,GP=2,-1,-1
D=[[0]*(m+1) for _ in range(n+1)]
for i in range(1,n+1): D[i][0]=D[i-1][0]+GP
for i in range(1,n+1):
    ri=R[i-1][0]; Di=D[i]; Dp=D[i-1]
    for j in range(1,m+1):
        s=Dp[j-1]+(MA if ri==G[j-1] else MI)
        x=Dp[j]+GP; y=Di[j-1]+GP
        Di[j]=max(s,x,y)
j=max(range(m+1),key=lambda k:D[n][k]); i=n
pairs=[]
while i>0 and j>0:
    s=D[i-1][j-1]+(MA if R[i-1][0]==G[j-1] else MI)
    if D[i][j]==s: pairs.append((i-1,j-1)); i-=1; j-=1
    elif D[i][j]==D[i-1][j]+GP: pairs.append((i-1,None)); i-=1
    else: j-=1
while i>0: pairs.append((i-1,None)); i-=1
from collections import Counter
c=Counter()
for ri,gj in pairs:
    k=R[ri][1]
    if gj is None: c[(k,'unaligned')]+=1
    elif R[ri][0]==G[gj]: c[(k,'match')]+=1
    else: c[(k,'mismatch')]+=1
for k in sorted(c): print(k,c[k])
print('G span chars',m,'R chars',n)
