import dcore, random, sys, statistics as st
cid = sys.argv[1]; p = float(sys.argv[2]); n = int(sys.argv[3])
t = dcore.target(cid); lens = [len(l) for l in t]; cv = dcore.curve_of(t)
for d in ['FR-HOMO', 'EN-HOMO', 'PT-HOMO', 'FR-SYLL', 'NULL-IID', 'NULL-HABIT', 'NULL-AVOID']:
    rng = random.Random(hash(d) & 0xffff); Z = []
    for i in range(n):
        x = dcore.make(d, lens, cv, rng, p); Z.append(dcore.zstats(x, rng, 100))
    print(d, ' '.join(f"{k}={st.median(z[k]['z'] for z in Z):+.1f}[{min(z[k]['z'] for z in Z):+.1f},{max(z[k]['z'] for z in Z):+.1f}]" for k in ('mi1', 'mi2', 'bg2', 'rep3', 'dbl')), flush=True)
