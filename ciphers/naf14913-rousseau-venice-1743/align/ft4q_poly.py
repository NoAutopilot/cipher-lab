#!/usr/bin/env python3
"""FT4q (account-4, 3 Oct 2026): 722 polyvalence test (pre-registered, PREREG-FT4q.md).

Part 1 (f.213 side, model gate_pair.Scorer.consistent, MAXLEN 12, group 73 dropped as FT4m, pins 22 de / 501 et,
722 free but tied at both its occurrences): every chunk V of the f.214r slip occurring >= 2 times for which pinning
722 = V gives a consistent fit (--limit1 s each; TIMEOUT reported, never counted as a fit). 'ti' is listed for the record.
Part 2 (f.249 side, FT4l one-edit CP-SAT model of one_edit_seg.py, <= 1 edit, decomposition per edit class, sublimit
10 s): E_X with the single 722 occurrence of f.249 pinned to chunk X (the pinned group can be neither released nor
dropped), for X = 'ti' and every f.213 candidate V from part 1 (at most --maxv, in order of length then text).
Control for part 2 (registered, can vary on the statistic's axis: the value pinned at 722): n random chunks of the same
length as X drawn from the f.250 slip's substrings with random.Random(3) (excluding X), the same E; share s_X with
unresolved counted as 1. f.216v carries no 722: a non-test by construction, not run.
  python3 ft4q_poly.py --part 1
  python3 ft4q_poly.py --part 2 --values ti,tis [--n 20]
"""
import argparse, os, random, sys, time
from collections import Counter
from multiprocessing import Pool
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import gate_pair as g
import one_edit as oe
import one_edit_seg as seg

T = oe.T
MAXLEN = oe.MAXLEN


def part1(limit):
    A, t = g.load(os.path.join(T, 'ciphertext_f213.txt'), os.path.join(T, 'slip_f214r.txt'))
    A = [x for i, x in enumerate(A) if i != 73]
    sc = g.Scorer(t, MAXLEN)
    base = {'22': 'de', '501': 'et'}
    subs = sorted({t[i:i + l] for l in range(1, MAXLEN + 1) for i in range(len(t) - l + 1)}, key=lambda s: (len(s), s))
    cand = [s for s in subs if bin(sc.smask(s)).count('1') >= 2 and sc.feasible(A, dict(base, **{'722': s}))]
    print(f'# part1 f213 minus g73: {len(A)} groups, {len(t)} letters, pins {base}; 722 x{A.count("722")}; '
          f'feasible candidates (>=2 occurrences in slip) {len(cand)}; ti feasible {"ti" in cand}', flush=True)
    fits, tos = [], []
    for s in cand + ([] if 'ti' in cand else ['ti']):
        t0 = time.time()
        r = sc.consistent(A, dict(base, **{'722': s}), time.time() + limit)
        res = 'TIMEOUT' if r is None else ('FIT' if r else 'NOFIT')
        print(f'V\t{s}\t{res}\t{time.time()-t0:.1f}', flush=True)
        (fits if r else tos if r is None else []).append(s)
    print(f'PART1: FIT {fits}; TIMEOUT {tos}', flush=True)


def solve_pinned(toks, text, pin_idx, pin_chunk, limit, force=None):
    """one_edit_seg.solve with group pin_idx fixed to pin_chunk (never released, never dropped)."""
    from ortools.sat.python import cp_model
    n, L = len(toks), len(text)
    cnt = Counter(toks)
    R = sorted(set(i for i, t in enumerate(toks) if cnt[t] > 1) | {pin_idx})
    m = cp_model.CpModel()
    chunks, rows = {}, []
    for p in range(L):
        for l in range(1, MAXLEN + 1):
            if p + l > L:
                break
            rows.append((p, l, chunks.setdefault(text[p:p + l], len(chunks))))
    rows += [(p, 0, len(chunks)) for p in range(L + 1)]
    if pin_chunk not in chunks:
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
    m.Add(kc[toks[pin_idx]] == chunks[pin_chunk])
    m.Add(w[pin_idx] == 0)
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
    edv += [w[i] for i in R if i != pin_idx]
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


def _force(j):
    toks, text, pi, pc, limit, f = j
    return solve_pinned(toks, text, pi, pc, limit, force=f)


def E_pinned(toks, text, pi, pc, sublimit):
    """1 / 0 / None per one_edit_seg.E_dec, with the pin. The pinned group's own release class is excluded."""
    cls = [f for f in seg.edit_classes(toks) if f != ('W', pi)] + [None]
    tos = 0
    with Pool(4) as pool:
        for r in pool.imap_unordered(_force, [(toks, text, pi, pc, sublimit, f) for f in cls]):
            if r:
                pool.terminate()
                return 1
            tos += r is None
    return None if tos else 0


def part2(values, n, sublimit, seed):
    toks, text, _ = seg.load('f249')
    pi = toks.index('722')
    assert toks.count('722') == 1
    print(f'# part2 f249: {len(toks)} groups, {len(text)} letters, 722 at group {pi} (context {" ".join(toks[pi-1:pi+2])}); '
          f'sublimit {sublimit}', flush=True)
    for X in values:
        t0 = time.time()
        e = E_pinned(toks, text, pi, X, sublimit)
        print(f'REAL 722={X}: E {e if e is not None else "unresolved"} ({time.time()-t0:.1f} s); in slip {X in text}', flush=True)
        rng = random.Random(seed)
        pool_ = sorted({text[i:i + len(X)] for i in range(len(text) - len(X) + 1)} - {X})
        draws = rng.sample(pool_, min(n, len(pool_)))
        k1 = 0; un = 0
        for d, Y in enumerate(draws):
            t0 = time.time()
            e2 = E_pinned(toks, text, pi, Y, sublimit)
            k1 += 1 if e2 != 0 else 0; un += e2 is None
            print(f'draw {X} {d} {Y} E {1 if e2 is None else e2} timedout {e2 is None} {time.time()-t0:.1f}', flush=True)
        print(f'CONTROL 722={X}: same-length random pins n={len(draws)}: E=1 in {k1} (share {k1/max(1,len(draws)):.3f}); '
              f'unresolved counted high {un}', flush=True)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--part', type=int, choices=[1, 2], required=True)
    ap.add_argument('--limit1', type=float, default=20)
    ap.add_argument('--values', default='ti')
    ap.add_argument('--n', type=int, default=20)
    ap.add_argument('--sublimit', type=float, default=10)
    ap.add_argument('--seed', type=int, default=3)
    a = ap.parse_args()
    if a.part == 1:
        part1(a.limit1)
    else:
        part2(a.values.split(','), a.n, a.sublimit, a.seed)


if __name__ == '__main__':
    main()
