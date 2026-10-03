# Usage: python3 ciphers/sufi-fiddle/fig1-diff/profile_corr.py <dir with fig1.jpg>  (run from repo root)
# Column ink-profile correlation per line (Bulliet Fig.1 vs folder copy), best scale+shift; control: mismatched line pairs.
import numpy as np, sys
from PIL import Image
S=sys.argv[1]  # dir holding fig1.jpg (Bulliet Fig.1; URL and sha1 in ../images/manifest.json; not committed, no licence stated)
f=np.asarray(Image.open(S+'/fig1.jpg').convert('L')).astype(float)
w=np.asarray(Image.open('ciphers/sufi-fiddle/images/Suffi-Fiddle-614.png').convert('L')).astype(float)
fc=[105,290,440,620,830,1000,1200]; wc=[36,78,112,158,202,245,288]
def prof(a,c,h):
    b=a[max(0,c-h):c+h]; return (b < np.median(b)*0.72).sum(0).astype(float)
wp=[prof(w,c,16) for c in wc]; fp=[prof(f,c,62) for c in fc]
def corr(fpi,wpj):
    best=-1
    for s in np.linspace(0.22,0.30,33):
        x=np.interp(np.arange(0,len(fpi)*s)/s, np.arange(len(fpi)), fpi)
        for dx in range(-60,61):
            off=len(x)-len(wpj)+dx
            if off<0 or off+len(wpj)>len(x): continue
            a=x[off:off+len(wpj)]; b=wpj
            m=(a>0)|(b>0)
            if m.sum()<20: continue
            r=np.corrcoef(a,b)[0,1]; best=max(best,r)
    return best
D=[corr(fp[i],wp[i]) for i in range(7)]
C=[corr(fp[i],wp[j]) for i in range(7) for j in range(7) if j!=i]
for i,v in enumerate(D): print(f'line {i+1}: r={v:.3f}')
print('same-line r mean %.3f min %.3f | mismatched control (42 pairs) mean %.3f max %.3f'%(np.mean(D),min(D),np.mean(C),max(C)))
