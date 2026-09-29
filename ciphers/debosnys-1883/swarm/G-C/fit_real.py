#!/usr/bin/env python3
"""DEB-SWARM-C Phase 2 fitter (29 Sept 2026). Reads ONLY the named real text (c1 or c2, through score.py's own loader,
the settled drafts minus `_`, MULTI and the H43 clear spans) and fits the same mixed-unit key as solve_control.py
(syll.py annealer, harness FR-SYLL unit rules, fr19 prose + Fleurs du Mal LM). Writes KEY_fit_<text>.tsv.
Run only after the group's Phase 1 bar is met on FR-SYLL (swarm/README.md).
  python3 fit_real.py c2 --S 160 --iters 4000000 --restarts 6 [--injective 0]
--injective 0 lets several signs share a unit (homophones, the H34/H39 working model), scored with the channel term.
"""
import argparse, os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE); sys.path.insert(0, os.path.dirname(HERE))
import syll
import score  # read-only use of the frozen loader


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('text', choices=['c1', 'c2'])
    ap.add_argument('--S', type=int, default=160)
    ap.add_argument('--W', type=int, default=17)
    ap.add_argument('--order', type=int, default=2)
    ap.add_argument('--iters', type=int, default=4000000)
    ap.add_argument('--restarts', type=int, default=6)
    ap.add_argument('--seed', type=int, default=1)
    ap.add_argument('--injective', type=int, default=1)
    ap.add_argument('--T0', type=float, default=2.0)
    ap.add_argument('--T1', type=float, default=0.05)
    a = ap.parse_args()
    lines = score.load_text(a.text)
    seq, breaks = [], set()
    for ln, sg in lines.items():
        breaks.add(len(seq)); seq.extend(sg)
    tok, lm = syll.build_lm(a.S, a.W, order=a.order, func='harness', verse=True)
    sc, key = syll.Solver(lm).run(seq, a.iters, a.restarts, a.seed, breaks=breaks, injective=bool(a.injective),
                                  T0=a.T0, T1=a.T1)
    out = os.path.join(HERE, f'KEY_fit_{a.text}.tsv')
    with open(out, 'w') as f:
        f.write('sign\tvalue\n')
        for s in sorted(key):
            f.write(f'{s}\t{key[s]}\n')
    print(dict(text=a.text, N=len(seq), K=len(set(seq)), score=round(sc, 1), key=out))


if __name__ == '__main__':
    main()
