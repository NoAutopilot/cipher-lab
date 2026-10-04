#!/usr/bin/env python3
"""RUN2-NXATL: line centres from the left 600 px of each text block (run inside the work dir holding c510.jpg..c516.jpg)."""
import numpy as np, sys
from PIL import Image
from scipy import ndimage as ndi
from scipy.signal import find_peaks
R={510:(1050,250,3780,5450),511:(930,600,4050,4990),512:(1180,40,3680,5480),513:(900,560,3680,4980),514:(900,560,3580,5060),515:(820,600,3700,5130),516:(1180,380,3650,4950)}
out={}
for n,(x,y,w,h) in R.items():
    g=np.asarray(Image.open(f'c{n}.jpg').convert('L'),dtype=float)[y:y+h,x:x+w]
    bg=ndi.grey_closing(g[::4,::4],size=(15,15)); bg=ndi.zoom(bg,4,order=1)[:h,:w]
    ink=(g/np.maximum(bg,1))<0.75
    # left strip: first 600 px with ink per row; use columns 0..700 relative to block ink start
    colink=ink.mean(0); x0=np.argmax(ndi.uniform_filter1d(colink,50)>0.03)
    prof=ndi.uniform_filter1d(ink[:,x0:x0+600].sum(1).astype(float),15)
    pk,_=find_peaks(prof,distance=80,prominence=0.15*prof.max())
    d=np.diff(pk)
    print(n,'x0',x0,len(pk),'lines; gaps',d.min(),int(np.median(d)),d.max(), 'big gaps at', [int(pk[i]) for i in np.where(d>170)[0]])
    out[n]=pk.tolist()
import json; json.dump(out,open(sys.argv[1] if len(sys.argv)>1 else 'centres.json','w'))
