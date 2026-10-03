#!/usr/bin/env python3
"""FT4t (account-4, 3 Oct 2026): the FT4s anchored split (ft4s_seg.py) applied to the f.249 numerals / f.250 slip pair,
then 722 = 'ti' vs 'i' on the segment holding the 722 group (pre-registered, PREREG-FT4t.md, pushed before any score).

Anchor rule (FT4s's, unchanged): cut at a code with an f.206 C value whose occurrence count in the groups equals the count of
that value as a whole slip word. In f.249/f.250 exactly two qualify: 628 'hongrie' (group 38 <-> word 26) and 279 'plus'
(group 101 <-> word 64); 501, 581 are absent, 22 'de' is 5 groups vs 6 words. 722 is group 76, between the two anchors, so
the scored segment S = groups 39..100 (62) with slip words 27..63 ('de la maniere ... derober le'); both anchor tokens excluded,
as FT4s excluded its anchor. Pins in S (FT4s's pin family, f.206 repetition-consistent C values present in S, every
occurrence, never released): 22 'de' (group 79), 66 'r' (49, 62), and 722 = X. Solver, E, controls: ft4s_seg unchanged.
  python3 ft4t_seg.py --value ti --real
  python3 ft4t_seg.py --value ti --ctrl s --draws 0-39
  python3 ft4t_seg.py --summarize FILE...
"""
import argparse, os, random, sys, time
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import one_edit_seg as seg
import ft4s_seg as fs

PINS = {'22': 'de', '66': 'r'}
A1, A2 = ('628', 'hongrie'), ('279', 'plus')


def segment():
    toks, text, words = seg.load('f249')
    for c, w in (A1, A2):
        assert toks.count(c) == words.count(w) == 1
    g1, g2 = toks.index(A1[0]), toks.index(A2[0])
    w1, w2 = words.index(A1[1]), words.index(A2[1])
    st, sw = toks[g1 + 1:g2], words[w1 + 1:w2]
    assert '722' in st and st.count('722') == 1
    return st, ''.join(sw), sw


def draws(n, seed):
    toks, text, words = segment()
    rng = random.Random(seed)
    js, jg = [], []
    for _ in range(n):
        x = words[:]; rng.shuffle(x); js.append((toks, ''.join(x)))
    for _ in range(n):
        x = toks[:]; rng.shuffle(x); jg.append((x, text))
    return {'s': js, 'g': jg}


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
    if a.summarize is not None:
        sys.argv = [sys.argv[0], '--summarize'] + a.summarize
        return fs.main()
    pins = dict(PINS, **{'722': a.value})
    toks, text, _ = segment()
    if a.real:
        print(f'# S: groups {len(toks)}, slip letters {len(text)}, 722 at segment group {toks.index("722")}; pins {pins}', flush=True)
        t0 = time.time(); e = fs.E(toks, text, pins, a.sublimit)
        print(f'REAL 722={a.value}: E {"unresolved" if e is None else e} ({time.time()-t0:.1f} s)', flush=True)
        return 0
    D = draws(a.n, a.seed)[a.ctrl]
    lo, hi = (int(x) for x in a.draws.split('-'))
    for i in range(lo, hi + 1):
        t0 = time.time(); tk, tx = D[i]
        e = fs.E(tk, tx, pins, a.sublimit)
        miss = any(v not in tx for v in pins.values())
        print(f'draw {a.ctrl} {i} E {1 if e is None else e} timedout {e is None} {time.time()-t0:.1f}'
              f'{" nochunk" if miss else ""}', flush=True)
    return 0


if __name__ == '__main__':
    sys.exit(main())
