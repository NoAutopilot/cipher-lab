#!/usr/bin/env python3
"""DEB-SWARM-C Phase 1 driver (29 Sept 2026): fit a mixed-unit key BLIND on a harness control's ciphertext
(swarm/controls/<ID>.tsv only; never controls/sealed/), write it as KEY_<ID>_<tag>.tsv, and let score.py report recovery.
  python3 solve_control.py FR-SYLL --S 110 --W 17 --order 3 --iters 400000 --restarts 4 [--fit c1+c2 | c2 | c1]
The same function fits the real texts in Phase 2 (fit_text), so the control and the target share one method."""
import argparse, collections, csv, json, os, subprocess, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import syll

SW = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))


def read_control(cid):
    rows = list(csv.DictReader(open(os.path.join(SW, 'controls', cid + '.tsv')), delimiter='\t'))
    lines = collections.OrderedDict()
    for r in rows:
        lines.setdefault(r['line'], []).append(r['sign'])
    return lines


def seq_of(lines, part):
    parts = part.split('+')
    seq, breaks = [], set()
    for ln, sg in lines.items():
        p = ln.split('_')[0]
        if p in parts or (p.startswith('c2') and 'c2' in parts):
            breaks.add(len(seq)); seq.extend(sg)
    return seq, breaks


def fit(seq, breaks, a, seed=1):
    """order-2 anneal; with --refine, the best order-2 key seeds a cooler order-3 anneal (one run, same seed)."""
    tok, lm = syll.build_lm(a.S, a.W, order=a.order, func=a.func, verse=a.verse)
    sc, key = syll.Solver(lm).run(seq, a.iters, a.restarts, seed, breaks=breaks, injective=a.injective,
                                  T0=a.T0, T1=a.T1)
    if a.refine:
        tok3, lm3 = syll.build_lm(a.S, a.W, order=3, func=a.func, verse=a.verse)
        sc, key = syll.Solver(lm3).run(seq, a.refine, 1, seed, breaks=breaks, injective=a.injective,
                                       T0=a.rT0, T1=a.T1, init=key)
        lm = lm3
    return sc, key, lm


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('control')
    ap.add_argument('--fit', default='c1+c2')
    ap.add_argument('--S', type=int, default=150)
    ap.add_argument('--W', type=int, default=17)
    ap.add_argument('--order', type=int, default=3)
    ap.add_argument('--iters', type=int, default=400000)
    ap.add_argument('--restarts', type=int, default=4)
    ap.add_argument('--seed', type=int, default=1)
    ap.add_argument('--T0', type=float, default=2.0)
    ap.add_argument('--T1', type=float, default=0.05)
    ap.add_argument('--injective', type=int, default=1)
    ap.add_argument('--verse', type=int, default=1)
    ap.add_argument('--tag', default='a')
    ap.add_argument('--refine', type=int, default=0, help='iterations of an order-3 anneal seeded by the order-2 key')
    ap.add_argument('--rT0', type=float, default=0.5)
    ap.add_argument('--func', default='harness', help='harness (FR-SYLL unit rules) or 1 (top-W words, own syllabifier)')
    a = ap.parse_args()
    a.func = a.func if a.func == 'harness' else a.func == '1'
    lines = read_control(a.control)
    seq, breaks = seq_of(lines, a.fit)
    sc, key, lm = fit(seq, breaks, a, a.seed)
    out = os.path.join(os.path.dirname(os.path.abspath(__file__)), f'KEY_{a.control}_{a.fit}_{a.tag}.tsv')
    with open(out, 'w') as f:
        f.write('sign\tvalue\n')
        for s in sorted(key):
            f.write(f'{s}\t{key[s]}\n')
    res = subprocess.run([sys.executable, os.path.join(SW, 'score.py'), out, '--control', a.control, '--shuffles', '10'],
                         capture_output=True, text=True)
    print(json.dumps(dict(control=a.control, fit=a.fit, S=a.S, W=a.W, order=a.order, iters=a.iters,
                          restarts=a.restarts, refine=a.refine, injective=a.injective, verse=a.verse, vocab=len(lm.vocab),
                          N=len(seq), K=len(set(seq)), score=round(sc, 1), key=os.path.basename(out))))
    print(res.stdout[-3000:], res.stderr[-1500:])


if __name__ == '__main__':
    main()
