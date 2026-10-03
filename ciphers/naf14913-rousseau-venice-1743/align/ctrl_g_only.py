#!/usr/bin/env python3
"""FT4k (account-4, 3 Oct 2026): run ONLY control (g) of one_edit.py for one pair, in halves, under
PREREG-FT4i.md as amended (FT4j: --limit 60). one_edit.py is imported unchanged; the draws are the same draws
one_edit.py makes: random.Random(seed) consumes the n (s) word shuffles first, then the n (g) group shuffles,
exactly as one_edit.main() does, so draw k here is draw k of the registered (g) control.
Each draw: E(toks_shuffled, real_slip, limit, high=True), single worker, Pool(4) -- as one_edit.py.
  python3 ctrl_g_only.py --pair f249 --limit 60 --draws 0-19   then   --draws 20-39
Prints one line per draw (index, E, timed out) and a per-half summary; --summarize FILE... pools the halves.
"""
import argparse, os, random, sys, time
from multiprocessing import Pool
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import one_edit as oe
import gate_pair as g


def draws(pair, n, seed, limit):
    c, s = oe.PAIRS[pair]
    toks, text = g.load(os.path.join(oe.T, c), os.path.join(oe.T, s))
    words = [w for w in (g.letters(x) for x in ' '.join(l for l in open(os.path.join(oe.T, s), encoding='utf-8')
                                                      if not l.startswith('#')).split()) if w]
    assert ''.join(words) == text
    rng = random.Random(seed)
    for _ in range(n):
        w = words[:]; rng.shuffle(w)
    jg = []
    for _ in range(n):
        x = toks[:]; rng.shuffle(x); jg.append((x, text, limit))
    return jg


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--pair', choices=sorted(oe.PAIRS))
    ap.add_argument('--n', type=int, default=40)
    ap.add_argument('--limit', type=float, default=60.0)
    ap.add_argument('--seed', type=int, default=3)
    ap.add_argument('--draws', default='0-39')
    ap.add_argument('--summarize', nargs='*')
    a = ap.parse_args()
    if a.summarize:
        rows = []
        for f in a.summarize:
            rows += [l.split() for l in open(f) if l.startswith('draw ')]
        k1 = sum(int(r[3]) for r in rows); tos = sum(1 for r in rows if r[5] == 'True')
        res1 = sum(int(r[3]) for r in rows if r[5] == 'False')
        print(f'CONTROL (g group shuffle, n={len(rows)}): E=1 in {k1} ({k1/len(rows):.3f}); timeouts counted high {tos}; '
              f'among resolved draws E=1 in {res1} of {len(rows) - tos} (descriptive)')
        return 0
    lo, hi = (int(x) for x in a.draws.split('-'))
    jg = draws(a.pair, a.n, a.seed, a.limit)
    t0 = time.time()
    with Pool(4) as pool:
        raw = pool.map(oe._job, jg[lo:hi + 1])
    for i, (e, t) in zip(range(lo, hi + 1), raw):
        print(f'draw {i} E {e} timedout {t}')
    k1 = sum(e for e, _ in raw); tos = sum(1 for _, t in raw if t)
    print(f'half {lo}-{hi}: E=1 in {k1} of {len(raw)}; timeouts {tos}; resolved fits {sum(e for e, t in raw if not t)} '
          f'of {len(raw) - tos}; {time.time() - t0:.0f} s')
    return 0


if __name__ == '__main__':
    sys.exit(main())
