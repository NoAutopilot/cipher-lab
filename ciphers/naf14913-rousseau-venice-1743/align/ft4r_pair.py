#!/usr/bin/env python3
"""FT4r (account-4, 3 Oct 2026): pair gate on f.266r numerals / f.265r slip, the FT4l one-edit form (PREREG-FT4i.md
amendment FT4l, decomposition per edit class) with the single 722 occurrence pinned, run once under 722 = 'i' and once
under 722 = 'ti' (pre-registered, PREREG-FT4r.md, pushed before any registered score).

Model: ft4q_poly.solve_pinned (= one_edit_seg.solve plus a pin: the 722 group carries exactly chunk X and can be neither
released nor dropped); E by decomposition (ft4q_poly.E_pinned: one exact subproblem per edit class + the no-edit model,
sublimit s each, Pool(4), early exit on a fit). E = 1 fit with <= 1 edit; 0 every class proved infeasible; unresolved.
Controls (as one_edit_seg.draws, seed 3, n 40): (s) slip words shuffled, real groups; (g) group order shuffled, real slip.
The pin goes with the 722 token wherever it lands in a (g) draw; in an (s) draw with no X in the shuffled text the
model is infeasible by construction (E 0, printed with the flag nochunk).
  python3 ft4r_pair.py --value i --real
  python3 ft4r_pair.py --value i --ctrl s --draws 0-19
  python3 ft4r_pair.py --summarize FILE...
Draw lines: 'draw <ctrl> <i> E <0|1> timedout <bool> <secs> [nochunk]'.
"""
import argparse, os, random, sys, time
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import gate_pair as g
import one_edit as oe
import ft4q_poly as fq

T = oe.T
C, S = 'ciphertext_f266r.txt', 'slip_f265r.txt'


def load():
    toks, text = g.load(os.path.join(T, C), os.path.join(T, S))
    words = [x for x in (g.letters(y) for y in ' '.join(l for l in open(os.path.join(T, S), encoding='utf-8')
                                                        if not l.startswith('#')).split()) if x]
    assert ''.join(words) == text
    assert toks.count('722') == 1
    return toks, text, words


def draws(n, seed):
    toks, text, words = load()
    rng = random.Random(seed)
    js, jg = [], []
    for _ in range(n):
        x = words[:]; rng.shuffle(x); js.append((toks, ''.join(x)))
    for _ in range(n):
        x = toks[:]; rng.shuffle(x); jg.append((x, text))
    return {'s': js, 'g': jg}


def E(toks, text, X, sub):
    return fq.E_pinned(toks, text, toks.index('722'), X, sub)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--value', choices=['i', 'ti'])
    ap.add_argument('--ctrl', choices=['s', 'g'])
    ap.add_argument('--real', action='store_true')
    ap.add_argument('--draws', default='0-39')
    ap.add_argument('--n', type=int, default=40)
    ap.add_argument('--seed', type=int, default=3)
    ap.add_argument('--sublimit', type=float, default=10.0)
    ap.add_argument('--summarize', nargs='*')
    a = ap.parse_args()
    if a.summarize:
        by = {}
        for f in a.summarize:
            for l in open(f):
                if l.startswith('draw '):
                    r = l.split(); by.setdefault((os.path.basename(f).split('_')[1], r[1]), []).append(r)
        for k, rs in sorted(by.items()):
            k1 = sum(int(r[4]) for r in rs); tos = sum(1 for r in rs if r[6] == 'True')
            print(f'722={k[0]} CONTROL ({k[1]}, n={len(rs)}): E=1 in {k1} (share {k1/len(rs):.3f}); unresolved counted high {tos}; '
                  f'resolved fits {k1 - tos} of {len(rs) - tos}; nochunk {sum(1 for r in rs if "nochunk" in r)}')
        return 0
    toks, text, _ = load()
    if a.real:
        print(f'# f266r: groups {len(toks)}, slip letters {len(text)}, 722 at group {toks.index("722")}; 722={a.value}', flush=True)
        t0 = time.time(); e = E(toks, text, a.value, a.sublimit)
        print(f'REAL 722={a.value}: E {"unresolved" if e is None else e} ({time.time()-t0:.1f} s)', flush=True)
        return 0
    D = draws(a.n, a.seed)[a.ctrl]
    lo, hi = (int(x) for x in a.draws.split('-'))
    for i in range(lo, hi + 1):
        t0 = time.time(); tk, tx = D[i]
        e = E(tk, tx, a.value, a.sublimit)
        print(f'draw {a.ctrl} {i} E {1 if e is None else e} timedout {e is None} {time.time()-t0:.1f}'
              f'{"" if a.value in tx else " nochunk"}', flush=True)
    return 0


if __name__ == '__main__':
    sys.exit(main())
