"""NOX-ALN exploratory (not pre-registered; found from the random-merge control): the RUN2-NXALN target pipeline, unchanged
(run_pipeline, rng 1574, nulls a/c 200, b 40 on max), on the owner labels plus extra merges X->Y; writes results/full_pair_<X>_<Y>.json
and the counts. Usage: python3 full_pair.py X Y"""
import random, sys, json, os
import nox_aln as n
sa, nx = n.sa, n.nx
a = sys.argv[1:]; extra = dict(zip(a[0::2], a[1::2])); tag = '_'.join(a)
tr_s, he_s = n.streams(); f = lambda s: extra.get(s, s)
ids, tr, he = n.ids_of([f(s) for s in tr_s], [f(s) for s in he_s])
res, counts, path, key = nx.run_pipeline(tr, he, nx.dupuy_stream(), len(ids), 200, random.Random(1574), sa.letters(nx.fr16_text()),
                                         f'target owner + {extra}', None)
res['extra'] = extra; res['n_symbols'] = len(ids)
json.dump(res, open(f'results/full_pair_{tag}.json', 'w'), indent=1)
inv = {v: k for k, v in ids.items()}
with open(f'results/full_pair_{tag}_counts.tsv', 'w') as fo:
    fo.write('pile\t' + '\t'.join(chr(97 + i) for i in range(26)) + '\n')
    for i in range(len(ids)):
        fo.write(inv[i] + '\t' + '\t'.join(str(int(x)) for x in counts[i]) + '\n')
print(nx.summary(res))
