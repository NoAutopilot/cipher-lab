#!/usr/bin/env python3
"""PAGET-KEY (2 Oct 2026): per-letter controls before the gloss alignment's values are merged into one key.

Letter 1 = pairs on f60R f61L f61R f65L (8 Apr 1714); letter 2 = f65R f66L f66R (28 Aug 1714).
For each letter, two gates, each against a shuffled-pairing control (cipher_raw permuted across the pairs being
aligned; both statistics depend on the pairing, so the control can fail differently from the real run):
  own:   align that letter alone; self-agreement (aligned code tokens whose chunk equals the code's top value, n>=2)
  cross: align the OTHER letter alone; spell this letter's codes from that key; gloss letters recovered (evaluate.predict)
A letter passes when its real figure exceeds the shuffle p95 on both gates. Settings are NEXT-PAG's, fixed on
training data before this run: null-cost -3, max-chunk 4, seg-bonus 0.5, len-prior 0.5. Writes per_letter.txt.
    python3 per_letter.py [--seeds 20]
"""
import os, random, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import evaluate as ev
ia = ev.ia

L1 = {'f60R', 'f61L', 'f61R', 'f65L'}


def shuffled(pairs, seed):
    c = [p['cipher_raw'] for p in pairs]
    random.Random(seed).shuffle(c)
    return [dict(p, cipher_raw=x) for p, x in zip(pairs, c)]


def own(pairs):
    pr, rs, cn, _ = ev.run(pairs, -3.0)
    a, t = ev.stats(pr, rs, cn)
    return a / t, a, t


def cross(train, test):
    _, _, cn, _ = ev.run(train, -3.0)
    g, w, _ = ev.predict(test, ev.key_of(cn))
    return g / w, g, w


def main():
    a = sys.argv[1:]
    seeds = int(a[a.index('--seeds') + 1]) if '--seeds' in a else 20
    ev.OPTS.update(max_chunk=4, seg_bonus=0.5, len_prior=0.5)
    pairs = [p for p in ia.load_pairs(os.path.join(HERE, 'pairs.tsv'))]
    let = {1: [p for p in pairs if p['page'] in L1], 2: [p for p in pairs if p['page'] not in L1]}
    p95 = lambda xs: sorted(xs)[min(len(xs) - 1, int(round(0.95 * (len(xs) - 1))))]
    out = ['settings null_cost -3 %s seeds %d' % (ev.OPTS, seeds)]
    for L, other in ((1, 2), (2, 1)):
        r, ag, t = own(let[L])
        sh = [own(shuffled(let[L], s))[0] for s in range(seeds)]
        c, g, w = cross(let[other], let[L])
        shc = [cross(shuffled(let[other], s), let[L])[0] for s in range(seeds)]
        ok = r > p95(sh) and c > p95(shc)
        out.append('letter %d (%d pairs): own self-agreement %d/%d = %.3f vs shuffle mean %.3f p95 %.3f; '
                   'cross (key from letter %d) %d/%d = %.3f vs shuffle mean %.3f p95 %.3f -> %s'
                   % (L, len(let[L]), ag, t, r, sum(sh) / seeds, p95(sh), other, g, w, c, sum(shc) / seeds,
                      p95(shc), 'PASS' if ok else 'HOLD'))
    open(os.path.join(HERE, 'per_letter.txt'), 'w').write('\n'.join(out) + '\n')
    print('\n'.join(out))


if __name__ == '__main__':
    main()
