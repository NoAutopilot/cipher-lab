"""GAPS117: iiif_lines s1 (x 400-2800) and s2 (x 2300-4700) overlap by 500 px; drop the s2 prefix that repeats
the s1 suffix (longest match, up to 8 signs; '?' matches '?'); write one merged line per Lnn."""
import sys, csv
rows=[r for r in csv.DictReader(open(sys.argv[1]),delimiter='\t')]
by={}
for r in rows: by.setdefault(r['line'],[]).append(r)
out=[]; log=[]
for L in sorted({k.rsplit('_s',1)[0] for k in by}):
    a=by.get(L+'_s1',[]); b=by.get(L+'_s2',[])
    sa=[r['sign'] for r in a]; sb=[r['sign'] for r in b]
    k=0
    for n in range(min(8,len(sa),len(sb)),0,-1):
        if sa[-n:]==sb[:n]: k=n; break
    log.append(f'{L}: dropped {k} overlap signs from s2')
    for i,r in enumerate(a+b[k:]): out.append([L,str(i+1),r['sign'],r['conf'],r['note']])
w=open(sys.argv[2],'w'); w.write('line\tpos\tsign\tconf\tnote\n'); w.write(''.join('\t'.join(x)+'\n' for x in out))
print('; '.join(log))
