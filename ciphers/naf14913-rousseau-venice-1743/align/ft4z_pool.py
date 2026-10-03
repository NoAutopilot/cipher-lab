#!/usr/bin/env python3
"""FT4z (account-4, 3 Oct 2026): pooled EXACT pin run of the three passages that each fit with no edit -- f.206 (ciphertext.txt
/ slip_f206r.txt), f.216v (ciphertext_f216v.txt / slip_f217r.txt), f.266r S1 (ft4s_seg.segment1) -- on the disputed f.206
split values. Pre-registered in PREREG-FT4z.md, pushed before any run.

Instrument: FT4x's (align/ft4x_pool.py solve_exact, unchanged): the ft4s_seg segment CP-SAT with ZERO edits, blocks joined by
a '#SEP' token pinned to '|', so a code occurring in two blocks carries one chunk in both. C pins 22 de, 66 r, 581 au; 722 free;
MAXLEN 12; 30 s per solve; unresolved counts high.
Controls (seed 3, n 40), only the S1 block perturbed (f.206 + f.216v stay real): (s) S1 slip words shuffled; (g) S1 group order
shuffled.
  python3 ft4z_pool.py --stage0
  python3 ft4z_pool.py --ctrl s|g
  python3 ft4z_pool.py --real
"""
import argparse, os, random, sys, time
from collections import Counter
from multiprocessing import Pool
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import gate_pair as g
import ft4s_seg as fs
from ft4x_pool import solve_exact, PINS, LIMIT

T = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DISPUTED = {'121': 'ons', '188': 'lar', '834': 'kowitz', '344': 'mee', '24': 'in', '534': 'ches', '253': None}
READOUT_LIMIT = 600.0


def blocks():
    A, ta = g.load(os.path.join(T, 'ciphertext.txt'), os.path.join(T, 'slip_f206r.txt'))
    B, tb = g.load(os.path.join(T, 'ciphertext_f216v.txt'), os.path.join(T, 'slip_f217r.txt'))
    st, sx, sw = fs.segment1()
    return {'F206': (A, ta), 'F216V': (B, tb), 'S1': (st, sx)}, sw


def join(bl):
    toks, text = [], ''
    for t, x in bl:
        if toks:
            toks.append('#SEP'); text += '|'
        toks += t; text += x
    return toks, text


def J(job):
    toks, text = job
    return solve_exact(toks, text, PINS, LIMIT)


def lab(r):
    return 'unresolved' if r is None else ('fit' if r else 'nofit')


def release(B):
    A, ta = B['F206']
    for other in ('F216V', 'S1'):
        t2, x2 = B[other]
        sh = sorted((set(A) & set(t2)) - set(PINS), key=int)
        ok = []
        for c in sh:
            A2 = [t if t != c else 'R' + c for t in A]
            toks, text = join([(A2, ta), (t2, x2)])
            r = solve_exact(toks, text, PINS, LIMIT)
            if r is not False:
                ok.append((c, lab(r)))
        print(f'release F206+{other}: shared {sh}; single releases restoring fit {ok}', flush=True)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--stage0', action='store_true')
    ap.add_argument('--real', action='store_true')
    ap.add_argument('--ctrl', choices=['s', 'g'])
    ap.add_argument('--release', action='store_true', help='addendum secondary readout')
    a = ap.parse_args()
    B, sw = blocks()
    if a.stage0:
        for k, (t, x) in B.items():
            t0 = time.time()
            print(f'stage0 {k}: groups {len(t)} letters {len(x)} exact {lab(solve_exact(t, x, PINS, LIMIT))} {time.time()-t0:.1f}s')
        for k1, k2 in (('F206', 'F216V'), ('F206', 'S1'), ('F216V', 'S1')):
            toks, text = join([B[k1], B[k2]])
            print(f'stage0 pair {k1}+{k2}: exact {lab(solve_exact(toks, text, PINS, LIMIT))}')
        for c, v in DISPUTED.items():
            n = {k: B[k][0].count(c) for k in B}
            print(f'disputed {c} ({v}): occurrences {n} testable {sum(1 for x in n.values() if x) >= 2}')
        return
    real = [B['F216V'], B['S1']]  # PREREG-FT4z addendum: F206 dropped (jointly nofit with each other block)
    if a.release:
        return release(B)
    if a.real:
        toks, text = join(real)
        t0 = time.time(); r = J((toks, text))
        print(f'REAL F216V+S1: J {lab(r)} {time.time()-t0:.1f}s', flush=True)
        if r:
            deadline = time.time() + READOUT_LIMIT
            for c in ('121',):
                carriers = [x for t, x in real if c in t]
                cand = sorted({x[p:p + l] for x in carriers[:1] for l in range(1, fs.MAXLEN + 1) for p in range(len(x) - l + 1)
                               if all(x[p:p + l] in y for y in carriers)}, key=lambda s: (len(s), s))
                feas, unres, done = [], [], True
                for v in cand:
                    if time.time() > deadline:
                        done = False; break
                    rr = solve_exact(toks, text, dict(PINS, **{c: v}), LIMIT)
                    if rr:
                        feas.append(v)
                    elif rr is None:
                        unres.append(v)
                print(f'readout {c} (key M {DISPUTED[c]}): candidates {len(cand)} feasible {len(feas)} {feas} unresolved {unres} '
                      f'complete {done}', flush=True)
        return
    rng = random.Random(3)
    st, sx = B['S1']
    D = []
    for _ in range(40):
        if a.ctrl == 's':
            w = sw[:]; rng.shuffle(w); D.append((st, ''.join(w)))
        else:
            t = st[:]; rng.shuffle(t); D.append((t, sx))
    jobs = [join([B['F216V'], d]) for d in D]
    with Pool(4) as pool:
        res = pool.map(J, jobs)
    for i, r in enumerate(res):
        print(f'draw {a.ctrl} {i} J {lab(r)}')
    hi = sum(r is not False for r in res)
    print(f'CONTROL {a.ctrl}: fit-or-unresolved {hi}/40 share {hi/40:.3f}; unresolved {sum(r is None for r in res)}')


if __name__ == '__main__':
    sys.exit(main())
