import sys,json
seg=json.load(open(sys.argv[1]))
for l in open(sys.argv[2]):
    ln,p,b=l.split()
    S=seg[ln]
    if '@' in b:
        i,side=b.split('@'); a,e=S[int(i)-1]; cx=a+25 if side=='L' else e-25; hw=40
    else:
        ids=[int(x)-1 for x in b.split('+')]; a=S[ids[0]][0]; e=S[ids[-1]][1]; cx=(a+e)//2; hw=max(40,(e-a)//2+12)
    print(f"{ln}\t{p}\t{cx}\t{hw}\t0")
