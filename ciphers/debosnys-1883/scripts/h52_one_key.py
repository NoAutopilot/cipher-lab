#!/usr/bin/env python3
"""H52 (29 Sept 2026): verse and prose as one key, on the settled drafts with clear spans dropped. (1) H15's shared-key
Spearman test for every cryptogram pair (h15_shared_key's spearman and controls, same mixed design, 200 draws), now on
settled_lines(drop_clear=True) with '_'/MULTI dropped. (2) The verse's line-final signs (last non-punctuation sign of
each of the 20 verse lines) in the prose (c1+c2+c3): the share of those types that occur in the prose and their prose
token count, against 10,000 draws of the same number of verse tokens taken at random positions (types weighted as they
fall in the verse). A rhyme inventory used only in the verse would sit below the null. Writes h52_one_key.json."""
import os, sys, json, random, collections
here = os.path.dirname(os.path.abspath(__file__)); root = os.path.dirname(here); sys.path.insert(0, here)
import h3_unit_profile as h3, h10_mixed as h10
from h15_shared_key import spearman
from settled_lines import settled_lines
PUNCT = {'BLOB', 'HOOK-L', 'DASH-H', '_', 'MULTI'}
raw = settled_lines(root, 'c', drop_clear=True)
pg = lambda k: {'c2a': 'c2', 'c2b': 'c2', 'c4a0': 'c4', 'c4a': 'c4', 'c4b': 'c4'}.get(k.split('_')[0], k.split('_')[0])
T = collections.defaultdict(list)
for k, v in raw.items(): T[pg(k)].extend(s for s in v if s not in ('_', 'MULTI'))
K = len({s for g in T.values() for s in g}); rng = random.Random(52); W = h3.corpus_words(); out = {}
groups = ['c1', 'c2', 'c3', 'c4']
for i, a in enumerate(groups):
    for b in groups[i + 1:]:
        Na, Nb = len(T[a]), len(T[b]); obs = spearman(collections.Counter(T[a]), collections.Counter(T[b])); sh = []; ind = []
        for _ in range(200):
            o = rng.randrange(len(W) - Na - Nb - 50); toks = h10.encode(W[o:o + Na + Nb + 50], 0.3, K, rng); units = sorted(set(toks))
            k1 = dict(zip(units, rng.sample(range(len(units)), len(units)))); k2 = dict(zip(units, rng.sample(range(len(units)), len(units))))
            sa, sb = toks[:Na], toks[Na:Na + Nb]
            sh.append(spearman(collections.Counter(k1[u] for u in sa), collections.Counter(k1[u] for u in sb)))
            ind.append(spearman(collections.Counter(k1[u] for u in sa), collections.Counter(k2[u] for u in sb)))
        sh.sort(); ind.sort(); q = lambda v, p: round(v[int(p * len(v))], 3)
        row = dict(N=[Na, Nb], spearman=round(obs, 3), shared_band=[q(sh, .025), q(sh, .975)], indep_band=[q(ind, .025), q(ind, .975)])
        row['verdict'] = 'shared' if row['shared_band'][0] <= obs <= row['shared_band'][1] else ('independent' if row['indep_band'][0] <= obs <= row['indep_band'][1] else 'outside both')
        out[f'{a}-{b}'] = row; print(a, b, row)
verse = [[s for s in v if s not in PUNCT] for k, v in raw.items() if k.startswith('c4')]
finals = [l[-1] for l in verse if l]
prose = collections.Counter(s for k, v in raw.items() if not k.startswith('c4') for s in v if s not in PUNCT)
vt = [s for l in verse for s in l]
def score(signs): return sum(prose[s] > 0 for s in set(signs)) / len(set(signs)), sum(prose[s] for s in set(signs)) / len(set(signs))
obs = score(finals); null = [score(rng.sample(vt, len(finals))) for _ in range(10000)]
out['rhyme_in_prose'] = dict(final_types=sorted(set(finals)), share_in_prose=round(obs[0], 3), mean_prose_count=round(obs[1], 2),
                             null_share_band=[round(sorted(x[0] for x in null)[250], 3), round(sorted(x[0] for x in null)[9749], 3)],
                             null_count_band=[round(sorted(x[1] for x in null)[250], 2), round(sorted(x[1] for x in null)[9749], 2)],
                             p_share_le=sum(x[0] <= obs[0] for x in null) / 10000)
print(out['rhyme_in_prose']); json.dump(out, open(os.path.join(root, 'h52_one_key.json'), 'w'), indent=1)
