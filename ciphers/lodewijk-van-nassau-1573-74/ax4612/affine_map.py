"""AX-4612 extension E4: is 4612 key.tsv's table read through a value transformation that destroys block contiguity?
Exhaustive over v' = (a*(v-1) + b) mod 120 + 1 for every unit a mod 120 (32) and every b (120) -- 3,840 maps, which
include every cyclic shift (a=1, W1 tested these) and the reversal v' = 121 - v (a=119, b=119) -- plus digit reversal
(12 -> 21) with and without each shift. Values outside 1-120 are left as unreadable. Score as digit_map.py (fr16
order-3 log-prob of the key.tsv decode, -8 per unreadable token).
Matched control: 5811 cut to 4612's numeral count through a random affine map (3 seeds); the search must find the
inverse map and return key.tsv's reading. Seeds 1-3 happen to draw
self-inverse maps (a*a = 1 and b*(a+1) = 0 mod 120), so seed 4 adds a fixed non-involution, a=7 b=5.
  python3 ciphers/lodewijk-van-nassau-1573-74/ax4612/affine_map.py"""
import sys, random, json, math
sys.path.insert(0, 'tools'); sys.path.insert(0, 'ciphers/lodewijk-van-nassau-1573-74/ax4612')
import homophonic_anneal as ha, judge_plaintext as jp
from digit_map import numerals, KEY

UNITS = [a for a in range(1, 120) if math.gcd(a, 120) == 1]


def fmap(runs, f):
    return [[f(int(x)) for x in r] for r in runs]


def score(model, vruns):
    o = model.order; tot = 0.0; bad = 0
    for r in vruns:
        seg = ''.join(KEY.get(v, '#') for v in r)
        for part in seg.split('#'):
            tot += sum(model.logp(part[i:i + o]) for i in range(len(part) - o + 1))
        bad += seg.count('#')
    return tot - 8.0 * bad


def aff(a, b):
    return lambda v: (a * (v - 1) + b) % 120 + 1 if 1 <= v <= 120 else v


def search(model, runs):
    best = []
    for a in UNITS:
        for b in range(120):
            best.append((score(model, fmap(runs, aff(a, b))), f'affine a={a} b={b}'))
    for b in range(120):
        f = lambda v, b=b: aff(1, b)(int(str(v)[::-1])) if 1 <= v <= 120 else v
        best.append((score(model, fmap(runs, f)), f'digit-reverse then shift b={b}'))
    best.sort(reverse=True)
    return best


def main():
    spec = json.load(open('specs/lodewijk-4612.json'))
    model = ha.Model([jp.read_corpus(p) for p in spec['judge']['corpora']], 3)
    tgt = numerals('4612'); n = sum(map(len, tgt))
    for seed in (1, 2, 3, 4):
        rng = random.Random(seed)
        a, b = rng.choice(UNITS[1:]), rng.randrange(120)
        if seed == 4:  # seeds 1-3 happen to draw self-inverse maps; seed 4 is a fixed non-involution (a=7, b=5)
            a, b = 7, 5
        ctl = numerals('5811', n)
        scr = fmap(ctl, aff(a, b))
        res = search(model, [[str(v) for v in r] for r in scr])
        ident = score(model, fmap(ctl, lambda v: v))
        # the inverse of v -> a(v-1)+b is v -> a^-1 (v-1-b); check the top map reproduces the unscrambled score
        print(f'CONTROL seed {seed}: 5811 N={n} scrambled by a={a} b={b}; top {res[0][1]} score {res[0][0]:.1f} '
              f'(unscrambled {ident:.1f}; recovered={abs(res[0][0] - ident) < 1e-6}); 2nd {res[1][0]:.1f}')
    res = search(model, tgt)
    print(f'TARGET 4612: identity {score(model, fmap(tgt, lambda v: v)):.1f}; top 5: ' +
          '; '.join(f'{s:.1f} {d}' for s, d in res[:5]))
    print(f'TARGET 4612: median over all {len(res)} maps {res[len(res) // 2][0]:.1f}')


if __name__ == '__main__':
    main()
