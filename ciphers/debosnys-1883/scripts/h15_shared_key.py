#!/usr/bin/env python3
"""H15 (28 Sept 2026): one key or several? Spearman rank correlation of sign frequencies between each pair of
cryptograms (160-id draft; c1 = the H2-settled draft), over the union of sign ids (zeros for absent ids), against
two controls that can differ: French text (fr19) enciphered with the H10 mixed design (q 0.3, coarse syllabary,
K = pooled target K) then (a) ONE key shared by both samples, (b) two INDEPENDENT keys (random bijections from design
units to sign ids). 200 draws per pair and control, same N as the target pair; 10 pct invented-type noise is not
applied (it only lowers both controls alike). Writes h15_shared_key.json."""
import os, sys, json, random, collections
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import h3_unit_profile as h3, h10_mixed as h10
here = os.path.dirname(os.path.abspath(__file__)); root = os.path.dirname(here)
def spearman(c1, c2):
    ids = sorted(set(c1) | set(c2)); n = len(ids)
    def ranks(c):
        v = sorted(((c.get(i, 0), i) for i in ids)); r = {}; k = 0
        while k < n:
            j = k
            while j + 1 < n and v[j + 1][0] == v[k][0]: j += 1
            for m in range(k, j + 1): r[v[m][1]] = (k + j) / 2 + 1
            k = j + 1
        return r
    r1, r2 = ranks(c1), ranks(c2); m1 = sum(r1.values()) / n; m2 = sum(r2.values()) / n
    num = sum((r1[i] - m1) * (r2[i] - m2) for i in ids); d1 = sum((r1[i] - m1) ** 2 for i in ids) ** 0.5; d2 = sum((r2[i] - m2) ** 2 for i in ids) ** 0.5
    return num / (d1 * d2) if d1 and d2 else 0.0
def main():
    rng = random.Random(1); W = h3.corpus_words(); T = h3.target('id160'); K = len(set(T['all'])); out = {}
    groups = ['c1', 'c2', 'c3', 'c4']; pairs = [(a, b) for i, a in enumerate(groups) for b in groups[i + 1:]]
    for a, b in pairs:
        Na, Nb = len(T[a]), len(T[b]); obs = spearman(collections.Counter(T[a]), collections.Counter(T[b]))
        shared = []; indep = []
        for _ in range(200):
            o = rng.randrange(len(W) - Na - Nb - 50); toks = h10.encode(W[o:o + Na + Nb + 50], 0.3, K, rng)
            units = sorted(set(toks)); 
            k1 = {u: i for i, u in enumerate(rng.sample(range(len(units)), len(units)))}; k1 = dict(zip(units, rng.sample(range(len(units)), len(units))))
            k2 = dict(zip(units, rng.sample(range(len(units)), len(units))))
            sa, sb = toks[:Na], toks[Na:Na + Nb]
            shared.append(spearman(collections.Counter(k1[u] for u in sa), collections.Counter(k1[u] for u in sb)))
            indep.append(spearman(collections.Counter(k1[u] for u in sa), collections.Counter(k2[u] for u in sb)))
        shared.sort(); indep.sort(); q = lambda v, p: v[int(p * len(v))]
        row = dict(N=(Na, Nb), spearman=round(obs, 3), shared_band=(round(q(shared, .025), 3), round(q(shared, .975), 3)), shared_median=round(q(shared, .5), 3), indep_band=(round(q(indep, .025), 3), round(q(indep, .975), 3)), indep_median=round(q(indep, .5), 3))
        row['verdict'] = 'shared-key band' if row['shared_band'][0] <= obs <= row['shared_band'][1] else ('independent-keys band' if row['indep_band'][0] <= obs <= row['indep_band'][1] else 'between / outside both')
        out[f'{a}-{b}'] = row; print(a, b, row)
    json.dump(out, open(os.path.join(root, 'h15_shared_key.json'), 'w'), indent=1)
if __name__ == '__main__': main()
