import sys, numpy as np
c=np.array(list(map(int,sys.argv[1].split())),float); H=int(sys.argv[2])
p=21.3; c0=c[0]
for it in range(5):
    k=np.round((c-c0)/p); A=np.vstack([np.ones_like(k),k]).T
    r=c-(A@np.linalg.lstsq(A,c,rcond=None)[0]); keep=np.abs(r)<6
    a,b=np.linalg.lstsq(A[keep],c[keep],rcond=None)[0]; c0=a; p=b
k=np.round((c-a)/b); res=c-(a+b*k)
kmin=int(np.ceil((8-a)/b)); kmax=int(np.floor((H-8-a)/b))
g=[int(round(a+b*j)) for j in range(kmin,kmax+1)]
print(','.join(map(str,g))); print('pitch %.2f phase %.1f n %d inl %d/%d maxres_inl %.1f'%(b,a,len(g),keep.sum(),len(c),np.abs(res[keep]).max()),file=sys.stderr)
