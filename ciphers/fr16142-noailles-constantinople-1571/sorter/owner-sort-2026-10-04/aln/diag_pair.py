"""NOX-ALN diagnostic (exploratory, not pre-registered): owner labels plus one extra pile merge X->Y; train path end, held-out acc,
null (a) shuffled-key p99 and null (c) wrong-text p99 (100 draws each). Usage: python3 diag_pair.py X Y [X Y ...]"""
import random, sys, json
import numpy as np
import nox_aln as n
sa, nx = n.sa, n.nx
let = sa.letters(nx.dupuy_stream()); wp = sa.letters(nx.fr16_text())
a = sys.argv[1:]; extra = dict(zip(a[0::2], a[1::2]))
tr_s, he_s = n.streams()
f = lambda s: extra.get(s, s)
ids, tr, he = n.ids_of([f(s) for s in tr_s], [f(s) for s in he_s])
counts, path = sa.learn(np.array(tr), let, len(ids)); key = sa.decode(counts)
jend = path[-1][1] + 1; held = let[jend:]; acc = sa.nw_score(key[np.array(he)], held)
rng = random.Random(1574); na, nc = [], []
for _ in range(100):
    k2 = key.copy(); s = k2 >= 0; v = k2[s]; rng.shuffle(v); k2[s] = v; na.append(sa.nw_score(k2[np.array(he)], held))
    o = rng.randrange(0, len(wp) - len(held) - 1); nc.append(sa.nw_score(key[np.array(he)], wp[o:o + len(held)]))
print(json.dumps(dict(extra=extra, acc=round(float(acc), 4), train_end=int(jend), a_p99=round(float(np.percentile(na, 99)), 4),
                      c_p99=round(float(np.percentile(nc, 99)), 4))))
