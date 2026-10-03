#!/usr/bin/env python3
"""FT4u (account-4, 3 Oct 2026): the FT4s anchored split's other two segments of the f.266r numerals / f.265r slip pair,
S2 and S3, scored as second witnesses for the pinned f.206 C codes (pre-registered, PREREG-FT4u.md, pushed before any score).

Cut (FT4s's, unchanged): 501 'et' at groups 75, 139 <-> whole words 45, 78; anchors excluded.
  S2 = groups 76..138 (63) <-> words 46..77 ('le bergamasc ... audits confins', 163 letters); pins 22 de, 66 r, 581 au.
  S3 = groups 140..170 (31) <-> words 79..93 ('de faire de brescia ... sa residence', 75 letters); pins 22 de, 66 r.
Neither holds 722. Solver, E, controls (seed 3, n 40, (s)/(g)): ft4s_seg unchanged.
--mpin CODE pins one key.tsv M value in addition (registered consistency readout, run only on a segment that PASSes).
  python3 ft4u_seg.py --seg S2 --real
  python3 ft4u_seg.py --seg S2 --ctrl s --draws 0-39
  python3 ft4u_seg.py --seg S2 --real --mpin 121
  python3 ft4u_seg.py --summarize FILE...
"""
import argparse, csv, os, random, sys, time
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ft4s_seg as fs
import ft4r_pair as fr

SEGS = {'S2': {'22': 'de', '66': 'r', '581': 'au'}, 'S3': {'22': 'de', '66': 'r'}}


def segment(name):
    toks, text, words = fr.load()
    gi = [i for i, t in enumerate(toks) if t == '501']
    wi = [i for i, w in enumerate(words) if w == 'et']
    assert len(gi) == len(wi) == 2
    if name == 'S2':
        st, sw = toks[gi[0] + 1:gi[1]], words[wi[0] + 1:wi[1]]
    else:
        st, sw = toks[gi[1] + 1:], words[wi[1] + 1:]
    assert '722' not in st
    return st, ''.join(sw), sw


def mvalue(code):
    for r in csv.reader(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'key.tsv')), delimiter='\t'):
        if r[0] == code:
            assert r[2] == 'M', r
            assert '|' not in r[1], r
            return fr.g.letters(r[1])
    raise SystemExit(f'{code} not in key.tsv')


def draws(name, n, seed):
    toks, text, words = segment(name)
    rng = random.Random(seed)
    js, jg = [], []
    for _ in range(n):
        x = words[:]; rng.shuffle(x); js.append((toks, ''.join(x)))
    for _ in range(n):
        x = toks[:]; rng.shuffle(x); jg.append((x, text))
    return {'s': js, 'g': jg}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--seg', choices=['S2', 'S3'])
    ap.add_argument('--ctrl', choices=['s', 'g'])
    ap.add_argument('--real', action='store_true')
    ap.add_argument('--mpin')
    ap.add_argument('--draws', default='0-39')
    ap.add_argument('--n', type=int, default=40)
    ap.add_argument('--seed', type=int, default=3)
    ap.add_argument('--sublimit', type=float, default=10.0)
    ap.add_argument('--summarize', nargs='*')
    a = ap.parse_args()
    if a.summarize is not None:
        by = {}
        for f in a.summarize:
            v = os.path.basename(f).split('_')[1]
            for l in open(f):
                if l.startswith('draw '):
                    r = l.split(); by.setdefault((v, r[1]), []).append(r)
        for k, rs in sorted(by.items()):
            k1 = sum(int(r[4]) for r in rs); tos = sum(1 for r in rs if r[6] == 'True')
            print(f'{k[0]} CONTROL ({k[1]}, n={len(rs)}): E=1 in {k1} (share {k1/len(rs):.3f}); unresolved counted high {tos}; '
                  f'resolved fits {k1 - tos} of {len(rs) - tos}; nochunk {sum(1 for r in rs if "nochunk" in r)}')
        return 0
    pins = dict(SEGS[a.seg])
    toks, text, _ = segment(a.seg)
    if a.mpin:
        assert a.real and a.mpin in toks and a.mpin not in pins
        pins[a.mpin] = mvalue(a.mpin)
    if a.real:
        print(f'# {a.seg}: groups {len(toks)}, slip letters {len(text)}; pins {pins}', flush=True)
        t0 = time.time(); e = fs.E(toks, text, pins, a.sublimit)
        tag = f' +M {a.mpin}={pins[a.mpin]}' if a.mpin else ''
        print(f'REAL {a.seg}{tag}: E {"unresolved" if e is None else e} ({time.time()-t0:.1f} s)', flush=True)
        return 0
    D = draws(a.seg, a.n, a.seed)[a.ctrl]
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
