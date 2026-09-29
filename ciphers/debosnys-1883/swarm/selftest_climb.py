#!/usr/bin/env python3
"""DEB-SWARM-0 harness self-test only (29 Sept 2026): a plain homophonic hill-climber, used to show (1) the bar is
reachable by a genuine blind method on an answer-known control and (2) the same method does not pass on NULL.
Not a group tool and never run on c1/c2 by the harness. Usage: selftest_climb.py FIT_ID OUT.tsv [--lang fr]
[--restarts 8] [--iters 20000] [--seed 1]"""
import argparse, collections, math, random, sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import score

FREQ = {'fr': 'eeeeeeeeeeeeeeesssssssaaaaaaaiiiiiiittttttnnnnnnnrrrrrruuuuuulllllooooodddcccmmmpppvvqfbgh',
        'en': 'eeeeeeeeeeeettttttttaaaaaaaaoooooooiiiiiiinnnnnnnsssssshhhhhhrrrrrrddddllllcccuuummwwffggyypbvk',
        'pt': 'aaaaaaaaaaaaaeeeeeeeeeeeeooooooooooossssssrrrrrriiiiiinnnnnddddmmmmuuuutttccclllpppvvgqhf'}
if __name__ == '__main__':
    ap = argparse.ArgumentParser(); ap.add_argument('fit'); ap.add_argument('out')
    ap.add_argument('--lang', default='fr'); ap.add_argument('--restarts', type=int, default=8)
    ap.add_argument('--iters', type=int, default=20000); ap.add_argument('--seed', type=int, default=1)
    a = ap.parse_args()
    lp, floor, _ = score.model(a.lang)
    toks = score.flat(score.load_text(a.fit))
    signs = sorted(set(toks)); idx = {s: i for i, s in enumerate(signs)}
    seq = [idx[t] for t in toks]
    pos = collections.defaultdict(list)
    for i, t in enumerate(seq):
        pos[t].append(i)
    rng = random.Random(a.seed)
    pool = FREQ.get(a.lang, FREQ['fr'])
    def total(k):
        s = ''.join(k[t] for t in seq)
        return sum(lp.get(s[i:i + 4], floor) for i in range(len(s) - 3))
    best_all, best_key = -1e18, None
    for r in range(a.restarts):
        k = [rng.choice(pool) for _ in signs]
        cur = total(k); T = 2.0
        for it in range(a.iters):
            j = rng.randrange(len(signs)); old = k[j]
            k[j] = rng.choice('abcdefghijlmnopqrstuvxyz' if rng.random() < 0.3 else pool)
            new = total(k)
            if new >= cur or rng.random() < math.exp((new - cur) / T):
                cur = new
            else:
                k[j] = old
            T = max(0.05, 2.0 * (1 - it / a.iters))
        if cur > best_all:
            best_all, best_key = cur, list(k)
    open(a.out, 'w').write(''.join(f'{s}\t{v}\n' for s, v in zip(signs, best_key)))
    print(f'{a.fit} lang={a.lang} best={best_all / max(1, len(seq) - 3):.3f} per quad')
