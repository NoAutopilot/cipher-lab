#!/usr/bin/env python3
"""FT4s (account-4, 3 Oct 2026): anchored split of the f.266r numerals / f.265r slip pair, then the 722 = 'ti' vs 'i'
question on the segment holding group 49 (pre-registered, PREREG-FT4s.md, pushed before any registered score).

Anchor rule (fixed in the PREREG, no score consulted): the cut is at a code with an f.206 C value whose occurrence count
in the groups equals the count of that value as a whole slip word, so the k-th occurrence anchors to the k-th word.
Only 501 'et' qualifies (2 groups, 75 and 139; 2 whole words 'et', word 45 and 78). Segment S1 = groups 0..74 and the
slip words before word 45 ('... couvrir le Bressan', 251 letters); 75 groups, f.213-sized (84). 722 (group 49) is in S1.
Pins inside S1 (f.206 C values, every occurrence; never released): 22 'de' (2, 28), 66 'r' (56, 58), 581 'au' (30), and
722 = X. Model: ft4q_poly.solve_pinned generalised to several pinned codes (one_edit_seg's segment CP-SAT, <= 1 edit,
MAXLEN 12, a pinned occurrence is never released). E by decomposition per edit class (sublimit s, Pool(4), early exit).
Controls (as FT4l/FT4r): seed 3, n 40; (s) S1 slip words shuffled / S1 groups; (g) S1 group order shuffled / S1 slip;
pins move with their tokens; a draw whose text lacks a pinned value is infeasible by construction (E 0, flag nochunk).
  python3 ft4s_seg.py --value ti --real
  python3 ft4s_seg.py --value ti --ctrl s --draws 0-9
  python3 ft4s_seg.py --summarize FILE...
Draw lines: 'draw <ctrl> <i> E <0|1> timedout <bool> <secs> [nochunk]'.
"""
import argparse, os, random, sys, time
from collections import Counter
from multiprocessing import Pool
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import one_edit_seg as seg
import ft4r_pair as fr

MAXLEN = seg.MAXLEN
PINS = {'22': 'de', '66': 'r', '581': 'au'}
CUT_CODE, CUT_WORD = '501', 'et'


def segment1():
    toks, text, words = fr.load()
    gi = toks.index(CUT_CODE)
    wi = words.index(CUT_WORD)
    assert toks.count(CUT_CODE) == words.count(CUT_WORD) == 2
    sw = words[:wi]
    return toks[:gi], ''.join(sw), sw


def solve_pins(toks, text, pins, limit, force=None):
    """solve_pinned with several pinned codes: every occurrence of a pinned code carries its chunk, never released."""
    from ortools.sat.python import cp_model
    n, L = len(toks), len(text)
    cnt = Counter(toks)
    P = [i for i, t in enumerate(toks) if t in pins]
    R = sorted(set(i for i, t in enumerate(toks) if cnt[t] > 1) | set(P))
    m = cp_model.CpModel()
    chunks, rows = {}, []
    for p in range(L):
        for l in range(1, MAXLEN + 1):
            if p + l > L:
                break
            rows.append((p, l, chunks.setdefault(text[p:p + l], len(chunks))))
    rows += [(p, 0, len(chunks)) for p in range(L + 1)]
    if any(pins[toks[i]] not in chunks for i in P):
        return False
    nid = len(chunks) + 1
    a = {i: m.NewIntVar(0, L, f'a{i}') for i in R}
    ln = {i: m.NewIntVar(0, MAXLEN, f'l{i}') for i in R}
    w = {i: m.NewBoolVar(f'w{i}') for i in R}
    kc = {t: m.NewIntVar(0, nid - 1, f'k{t}') for t in set(toks[i] for i in R)}
    for i in R:
        ki = m.NewIntVar(0, nid - 1, f'ki{i}')
        m.AddAllowedAssignments([a[i], ln[i], ki], rows)
        m.Add(ki == kc[toks[i]]).OnlyEnforceIf(w[i].Not())
        m.Add(ln[i] >= 1).OnlyEnforceIf(w[i].Not())
    for t in set(toks[i] for i in P):
        m.Add(kc[t] == chunks[pins[t]])
    for i in P:
        m.Add(w[i] == 0)
    bounds = [-1] + R + [n]
    edv, fmap = [], {}
    for k in range(len(bounds) - 1):
        p, q = bounds[k], bounds[k + 1]
        f = q - p - 1
        wf = m.NewBoolVar(f'wf{k}') if f > 0 else None
        dd = m.NewBoolVar(f'dd{k}')
        for i in range(p + 1, q):
            fmap[('W', i)] = wf
        for i in range(p + 1, q + 1):
            fmap[('D', i)] = dd
        edv += [x for x in (wf, dd) if x is not None]
        gap = m.NewIntVar(0, L, f'gap{k}')
        if p < 0 and q == n:
            m.Add(gap == L)
        elif p < 0:
            m.Add(gap == a[q])
        elif q == n:
            m.Add(gap == L - a[p] - ln[p])
        else:
            m.Add(gap == a[q] - a[p] - ln[p])
        lo = f - (wf if wf is not None else 0) + dd
        m.Add(gap >= lo)
        m.Add(gap <= MAXLEN * (f + dd))
    for i in R:
        fmap[('W', i)] = w[i]
    edv += [w[i] for i in R if i not in P]
    m.Add(sum(edv) <= 1)
    if force:
        if fmap.get(force) is None:
            return False
        m.Add(fmap[force] == 1)
    s = cp_model.CpSolver()
    s.parameters.max_time_in_seconds = limit
    s.parameters.num_search_workers = 1
    r = s.Solve(m)
    if r in (cp_model.OPTIMAL, cp_model.FEASIBLE):
        return True
    if r == cp_model.INFEASIBLE:
        return False
    return None


def edit_classes(toks, pins):
    cnt = Counter(toks)
    R = sorted(set(i for i, t in enumerate(toks) if cnt[t] > 1) | set(i for i, t in enumerate(toks) if t in pins))
    b = [-1] + R + [len(toks)]
    fs = []
    for k in range(len(b) - 1):
        p, q = b[k], b[k + 1]
        if q - p - 1 > 0:
            fs.append(('W', p + 1))
        fs.append(('D', p + 1))
    return fs + [('W', i) for i in R if toks[i] not in pins]


def _force(j):
    toks, text, pins, limit, f = j
    return solve_pins(toks, text, pins, limit, force=f)


def E(toks, text, pins, sublimit):
    """1 fit with <= 1 edit / 0 every class (and the no-edit model) proved infeasible / None unresolved."""
    cls = edit_classes(toks, pins) + [None]
    tos = 0
    with Pool(4) as pool:
        for r in pool.imap_unordered(_force, [(toks, text, pins, sublimit, f) for f in cls]):
            if r:
                pool.terminate()
                return 1
            tos += r is None
    return None if tos else 0


def draws(n, seed):
    toks, text, words = segment1()
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
    if a.summarize:
        by = {}
        for f in a.summarize:
            v = os.path.basename(f).split('_')[1]
            for l in open(f):
                if l.startswith('draw '):
                    r = l.split(); by.setdefault((v, r[1]), []).append(r)
        for k, rs in sorted(by.items()):
            k1 = sum(int(r[4]) for r in rs); tos = sum(1 for r in rs if r[6] == 'True')
            print(f'722={k[0]} CONTROL ({k[1]}, n={len(rs)}): E=1 in {k1} (share {k1/len(rs):.3f}); unresolved counted high {tos}; '
                  f'resolved fits {k1 - tos} of {len(rs) - tos}; nochunk {sum(1 for r in rs if "nochunk" in r)}')
        return 0
    pins = dict(PINS, **{'722': a.value})
    toks, text, _ = segment1()
    if a.real:
        print(f'# S1: groups {len(toks)}, slip letters {len(text)}, 722 at group {toks.index("722")}; pins {pins}', flush=True)
        t0 = time.time(); e = E(toks, text, pins, a.sublimit)
        print(f'REAL 722={a.value}: E {"unresolved" if e is None else e} ({time.time()-t0:.1f} s)', flush=True)
        return 0
    D = draws(a.n, a.seed)[a.ctrl]
    lo, hi = (int(x) for x in a.draws.split('-'))
    for i in range(lo, hi + 1):
        t0 = time.time(); tk, tx = D[i]
        e = E(tk, tx, pins, a.sublimit)
        miss = any(v not in tx for v in pins.values())
        print(f'draw {a.ctrl} {i} E {1 if e is None else e} timedout {e is None} {time.time()-t0:.1f}'
              f'{" nochunk" if miss else ""}', flush=True)
    return 0


if __name__ == '__main__':
    sys.exit(main())
