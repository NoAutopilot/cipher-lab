"""H40: fresh design-matched controls corrupted at 5% (seeds 11-13, Cartas tomo 15 windows; tomes 13 used by H21/H27).
Builds with h21/vowel_control.py, then replaces 5% of positions with a sign drawn from the stream's own occurrence
distribution (exactprof_noisy.py's corruption)."""
import subprocess,random,sys
from collections import Counter
plain=sys.argv[1]
for s in (11,12,13):
    out=f'h40/ctl_seed{s}.tsv'
    subprocess.run(['python3','h21/vowel_control.py','--control',plain,'--n','521','--seed',str(s),'--out',out+'.clean'],check=True)
    rows=open(out+'.clean').read().split('\n')[1:]; seq=[r.split('\t')[2] for r in rows if r]
    rng=random.Random(s+7000); pool=[x for x,c in sorted(Counter(seq).items()) for _ in range(c)]
    for i in rng.sample(range(len(seq)),int(round(0.05*len(seq)))): seq[i]=rng.choice(pool)
    open(out,'w').write('line\tposition\tsign\n'+''.join(f'l1\t{i+1}\t{x}\n' for i,x in enumerate(seq)))
    open(out+'.plain','w').write(open(out+'.clean.plain').read())
