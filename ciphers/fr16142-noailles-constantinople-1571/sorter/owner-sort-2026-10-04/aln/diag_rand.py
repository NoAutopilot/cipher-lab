"""NOX-ALN diagnostic: for named random-merge sets, report the train path end and null (a) shuffled-key p99 / null (c) wrong text p99."""
import random, sys, json
import numpy as np
import nox_aln as n
sa, nx = n.sa, n.nx
let = sa.letters(nx.dupuy_stream()); wp = sa.letters(nx.fr16_text())
out = []
for k in map(int, sys.argv[1:]):
    rnd = random.Random(20261004 + k); mp, used = {}, set()
    for x0, y0 in n.merges.items():
        x = rnd.choice(n.nearest(x0, used | {x0})); y = rnd.choice(n.nearest(y0, used | {x, y0})); used |= {x, y}; mp[x] = y
    ids, tr, he = n.ids_of(*n.streams(mp))
    counts, path = sa.learn(np.array(tr), let, len(ids)); key = sa.decode(counts)
    jend = path[-1][1] + 1; held = let[jend:]; acc = sa.nw_score(key[np.array(he)], held)
    rng = random.Random(1574); na, nc = [], []
    for _ in range(100):
        k2 = key.copy(); s = k2 >= 0; v = k2[s]; rng.shuffle(v); k2[s] = v; na.append(sa.nw_score(k2[np.array(he)], held))
        o = rng.randrange(0, len(wp) - len(held) - 1); nc.append(sa.nw_score(key[np.array(he)], wp[o:o + len(held)]))
    d = dict(set=k, acc=round(float(acc), 4), train_end=int(jend), held_letters=len(held), n_held=len(he),
             a_p99=round(float(np.percentile(na, 99)), 4), c_p99=round(float(np.percentile(nc, 99)), 4), merges=mp)
    print({k: v for k, v in d.items() if k != 'merges'}, flush=True); out.append(d)
json.dump(out, open('results/diag_rand.json', 'w'), indent=1)
