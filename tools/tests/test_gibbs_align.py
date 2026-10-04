#!/usr/bin/env python3
"""Offline test for tools/gibbs_align.py (RUN1-PAG, 4 Oct 2026).

A synthetic homophonic syllabary: 40 codes, values 1-3 letters with several codes sharing a value, 4 null codes,
120 runs of 4-9 codes, and an inserted gloss word on 15% of runs. The sampler must (1) recover the planted value
of most non-null codes that occur >= 3 times, and (2) do much better on the true pairing than on a shuffled
pairing (the shuffle is what a null control does to it). Runs in a few seconds.
    python3 tools/tests/test_gibbs_align.py
"""
import collections, os, random, sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
import gibbs_align as ga

SYL = ['de', 'la', 'le', 're', 'en', 'on', 'ma', 'po', 'ur', 's', 'e', 'a', 't', 'qu', 'ion', 'ne', 'ce', 'pr', 'is', 'au']


def synth(seed, nruns=120, ncodes=40, nnull=4, ins_rate=0.15):
    rng = random.Random(seed)
    key = {c: rng.choice(SYL) for c in range(100, 100 + ncodes)}
    for c in rng.sample(sorted(key), nnull):
        key[c] = ''
    codes = sorted(key)
    w = [1.0 / (1 + i) ** 0.7 for i in range(ncodes)]
    rng.shuffle(w)
    pairs = []
    for k in range(nruns):
        run = rng.choices(codes, weights=w, k=rng.randint(4, 9))
        gloss = ''.join(key[c] for c in run)
        if rng.random() < ins_rate:
            p = rng.randint(0, len(gloss))
            gloss = gloss[:p] + rng.choice(['dup', 'mais', 'qui']) + gloss[p:]
        pairs.append({'plain_raw': gloss, 'cipher_raw': ' '.join(map(str, run))})
    return pairs, key


def recovery(pairs, key, seed=0, iters=80):
    prep, keep = ga.sample(pairs, iters=iters, seed=seed)
    k = ga.code_key(ga.token_modes(prep, keep))
    n = collections.Counter(int(t) for p in pairs for t in p['cipher_raw'].split())
    test = [c for c in key if key[c] and n[c] >= 3]
    return sum(k.get(c, ('',))[0] == key[c] for c in test) / len(test)


def main():
    pairs, key = synth(1)
    real = recovery(pairs, key)
    g = [p['plain_raw'] for p in pairs]
    random.Random(7).shuffle(g)
    shuf = recovery([dict(p, plain_raw=x) for p, x in zip(pairs, g)], key)
    print('recovered planted values: real pairing %.3f, shuffled pairing %.3f' % (real, shuf))
    assert real >= 0.7, real
    assert shuf <= 0.3, shuf
    # degenerate inputs: a clear token and a doubtful token do not break sampling
    prep, keep = ga.sample([{'plain_raw': 'dela', 'cipher_raw': '100 (2) 0? 101'}], iters=4, seed=0)
    assert len(keep[0]) == 4
    print('OK test_gibbs_align')


if __name__ == '__main__':
    main()
