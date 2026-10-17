#!/usr/bin/env python3
"""VIV-KSPLIT step 1 (PREREG-VIV-KSPLIT.md): VIV-KCELLS2's ink-63 real-vs-shuffle with a frequency-matched shuffle.

    python3 tx/ksplit/null_fm.py      # writes tx/ksplit/null_fm.json

20 draws: c takes a letter whose fr16 frequency is within a factor 2 of p's, 2 one within a factor 2 of m's (p, m excluded).
Real c=p, 2=m passes iff s and hrunV both exceed the draws' p99. Report only, no key edit.
"""
import collections, gzip, json, os, random, sys
H = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(os.path.dirname(H), 'kcells2'))
import kcells2 as kc  # noqa: E402
jp = kc.jp


def freqs():
    c = collections.Counter()
    for p in kc.FR16:
        c.update(ch for ch in jp.read_corpus(p).lower() if 'a' <= ch <= 'z')
    n = sum(c.values())
    return {k: v / n for k, v in c.items()}


def main():
    f = freqs()
    pool = [x for x in 'abcdefghilnoqrstuvxyz' if x not in 'pm']
    band = {lab: [x for x in pool if f[real] / 2 <= f.get(x, 0) <= f[real] * 2] for lab, real in (('c', 'p'), ('2', 'm'))}
    k = {c: (v, g) for c, (v, g) in kc.v63.vd.key().items()}
    model = jp.NgramModel([jp.read_corpus(p) for p in kc.FR16])
    st = kc.streams()['63']
    sh = []
    for i in range(20):
        rng = random.Random(f'VIV-KSPLIT-fm-{i}')
        sh.append(kc.measure(st, k, {'c': rng.choice(band['c']), '2': rng.choice(band['2'])}, '63', model))
    real = kc.measure(st, k, {'c': 'p', '2': 'm'}, '63', model)
    p99 = {s: round(jp.pct(sorted(x[s] for x in sh), 0.99), 4) for s in ('s', 'hrunV')}
    rank = 1 + sum(x['s'] > real['s'] for x in sh)
    out = dict(freq={x: round(f.get(x, 0), 4) for x in sorted(f)}, band=band, draws=[(x['trial'], x['s'], x['hrunV']) for x in sh],
               real=dict(s=real['s'], hrunV=real['hrunV']), p99=p99, s_rank=f'{rank}/21',
               pass_=real['s'] > p99['s'] and real['hrunV'] > p99['hrunV'])
    json.dump(out, open(os.path.join(H, 'null_fm.json'), 'w'), indent=1)
    print(json.dumps({x: out[x] for x in ('band', 'real', 'p99', 's_rank', 'pass_')}))


if __name__ == '__main__':
    main()
