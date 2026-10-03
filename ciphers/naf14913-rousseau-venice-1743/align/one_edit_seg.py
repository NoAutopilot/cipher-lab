#!/usr/bin/env python3
"""FT4l (account-4, 3 Oct 2026): the SAME statistic E as one_edit.py (PREREG-FT4i.md), solved by an equivalent but
smaller CP-SAT model (amendment FT4l in PREREG-FT4i.md, pushed before any registered draw was re-scored).

one_edit.py carries a start and a length variable for every group, free groups included. A free (non-repeated) group
constrains nothing except its own length (1..MAXLEN, or 0..MAXLEN when it is the wildcard), so a run of f free groups
between two repeated-code occurrences is exactly a gap of f..MAXLEN*f letters. This model keeps variables only for
the repeated-code occurrences (start, length, table-tied chunk id, as one_edit.py) and replaces each run of free groups
(prefix, between two repeated occurrences, suffix) by one gap constraint. The one edit becomes, per run, two booleans:
  wf (a free group in the run is the wildcard: lower bound f-1)  and  dd (a group dropped in the run: bounds +1 group),
plus w per repeated occurrence (released from its code, 0..MAXLEN letters). At most one edit in total. Feasibility is
identical to one_edit.py's model: which free group in a run is the wildcard, or where in the run the dropped group sits,
does not change which letters can be covered. The per-group single-edit list for a real pair is expanded from the runs.
Equivalence is checked, not assumed (registered): real E0/E and both single-edit lists must reproduce FT4i/FT4j, and
f216v must give E0 True.
  python3 one_edit_seg.py --pair f213 --ctrl s --draws 0-19 [--limit 60] [--seed 3] [--n 40]
  python3 one_edit_seg.py --pair f213 --real                 (real E0, E, single-edit list)
  python3 one_edit_seg.py --summarize FILE...                (pool halves; gate per PREREG-FT4i.md)
Draws are the registered ones: random.Random(seed) makes the n (s) word shuffles, then the n (g) group shuffles, as
one_edit.main(). Draw lines: 'draw <ctrl> <i> E <0|1> timedout <bool> <secs>'.
"""
import argparse, os, random, sys, time
from collections import Counter
from multiprocessing import Pool
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import one_edit as oe
import gate_pair as g

MAXLEN = oe.MAXLEN


def solve(toks, text, edits, limit, force=None, workers=1):
    """True fit / False proved none / None timeout. force: ('W', i) or ('D', i) per one_edit.py's group indexing."""
    from ortools.sat.python import cp_model
    n, L = len(toks), len(text)
    cnt = Counter(toks)
    R = [i for i, t in enumerate(toks) if cnt[t] > 1]          # repeated-code occurrences, in order
    m = cp_model.CpModel()
    chunks, rows = {}, []
    for p in range(L):
        for l in range(1, MAXLEN + 1):
            if p + l > L:
                break
            rows.append((p, l, chunks.setdefault(text[p:p + l], len(chunks))))
    rows += [(p, 0, len(chunks)) for p in range(L + 1)]
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
    # runs of free groups: (lo, hi) group index range [lo, hi), bounded by repeated occurrences or the ends
    bounds = [-1] + R + [n]
    edv, fmap = [], {}
    for k in range(len(bounds) - 1):
        p, q = bounds[k], bounds[k + 1]
        f = q - p - 1
        wf = m.NewBoolVar(f'wf{k}') if f > 0 else None
        dd = m.NewBoolVar(f'dd{k}')
        for i in range(p + 1, q):
            fmap[('W', i)] = wf
        for i in range(p + 1, q + 1):          # D before group i, i in p+1..q (q = n: at the end)
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
    edv += list(w.values())
    m.Add(sum(edv) <= edits)
    if force:
        m.Add(fmap[force] == 1)
    s = cp_model.CpSolver()
    s.parameters.max_time_in_seconds = limit
    s.parameters.num_search_workers = workers
    r = s.Solve(m)
    if r in (cp_model.OPTIMAL, cp_model.FEASIBLE):
        return True
    if r == cp_model.INFEASIBLE:
        return False
    return None


def load(pair):
    c, s = oe.PAIRS[pair]
    toks, text = g.load(os.path.join(oe.T, c), os.path.join(oe.T, s))
    words = [x for x in (g.letters(y) for y in ' '.join(l for l in open(os.path.join(oe.T, s), encoding='utf-8')
                                                        if not l.startswith('#')).split()) if x]
    assert ''.join(words) == text
    return toks, text, words


def draws(pair, n, seed):
    toks, text, words = load(pair)
    rng = random.Random(seed)
    js, jg = [], []
    for _ in range(n):
        x = words[:]; rng.shuffle(x); js.append((toks, ''.join(x)))
    for _ in range(n):
        x = toks[:]; rng.shuffle(x); jg.append((x, text))
    return {'s': js, 'g': jg}


def _job(j):
    toks, text, limit = j
    t0 = time.time()
    r = solve(toks, text, 1, limit)
    return (1 if r or r is None else 0), r is None, time.time() - t0


def edit_classes(toks):
    """One representative forced edit per class (run wildcard, run drop, each repeated occurrence released)."""
    cnt = Counter(toks)
    R = [i for i, t in enumerate(toks) if cnt[t] > 1]
    b = [-1] + R + [len(toks)]
    fs = []
    for k in range(len(b) - 1):
        p, q = b[k], b[k + 1]
        if q - p - 1 > 0:
            fs.append(('W', p + 1))
        fs.append(('D', p + 1))
    return fs + [('W', i) for i in R]


def E_dec(toks, text, sublimit, pool):
    """Amendment FT4l: E by decomposition. 1 if some forced edit class fits; 0 if every class is proved infeasible;
    None (unresolved) if no class fits and at least one timed out. Early exit on the first fit."""
    tos = 0
    for r in pool.imap_unordered(_force, [(toks, text, sublimit, f) for f in edit_classes(toks)]):
        if r:
            pool.terminate()
            return 1
        tos += r is None
    return None if tos else 0


def _force(j):
    toks, text, limit, f = j
    return solve(toks, text, 1, limit, force=f)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--pair', choices=sorted(oe.PAIRS))
    ap.add_argument('--ctrl', choices=['s', 'g'])
    ap.add_argument('--draws', default='0-39')
    ap.add_argument('--n', type=int, default=40)
    ap.add_argument('--limit', type=float, default=60.0)
    ap.add_argument('--seed', type=int, default=3)
    ap.add_argument('--real', action='store_true')
    ap.add_argument('--summarize', nargs='*')
    ap.add_argument('--dec', action='store_true', help='amendment FT4l: decomposition per edit class, --sublimit s each')
    ap.add_argument('--sublimit', type=float, default=10.0)
    a = ap.parse_args()
    if a.summarize:
        rows = []
        for f in a.summarize:
            rows += [l.split() for l in open(f) if l.startswith('draw ')]
        by = {}
        for r in rows:
            by.setdefault(r[1], []).append(r)
        shares = {}
        for c, rs in sorted(by.items()):
            k1 = sum(int(r[4]) for r in rs); tos = sum(1 for r in rs if r[6] == 'True')
            res1 = sum(int(r[4]) for r in rs if r[6] == 'False')
            shares[c] = k1 / len(rs)
            print(f'CONTROL ({c}, n={len(rs)}): E=1 in {k1} ({k1/len(rs):.3f}); timeouts counted high {tos}; '
                  f'resolved fits {res1} of {len(rs) - tos}')
        return 0
    toks, text, words = load(a.pair)
    if a.real and not a.dec:
        print(f'pair {a.pair}: groups {len(toks)}, distinct {len(set(toks))}, repeated occurrences '
              f'{sum(1 for t in toks if Counter(toks)[t] > 1)}, slip letters {len(text)}')
        t0 = time.time(); e0 = solve(toks, text, 0, a.limit * 3, workers=4)
        print(f'REAL E0 (no edit) = {e0} ({time.time()-t0:.1f} s)')
        t0 = time.time(); r = solve(toks, text, 1, a.limit * 3, workers=4)
        print(f'REAL E (<= 1 edit) = {1 if r else 0}; timed out {r is None} ({time.time()-t0:.1f} s)')
        if r:
            js = [(toks, text, a.limit, ('W', i)) for i in range(len(toks))] + \
                 [(toks, text, a.limit, ('D', i)) for i in range(len(toks) + 1)]
            with Pool(4) as pool:
                res = pool.map(_force, js)
            ok = [j[3] for j, x in zip(js, res) if x]
            print(f'single edits giving a fit: {len(ok)} of {len(js)} (timed out {sum(1 for x in res if x is None)})')
            for k, i in ok:
                print(f'  {k} at group {i} ({toks[i] if k == "W" else "-"})')
        return 0
    lo, hi = (int(x) for x in a.draws.split('-'))
    if a.dec:
        D = draws(a.pair, a.n, a.seed)[a.ctrl] if not a.real else [(toks, text)]
        rng = [0] if a.real else range(lo, hi + 1)
        t00 = time.time(); out = []
        for i in rng:
            t0 = time.time()
            with Pool(4) as pool:
                e = E_dec(*D[i], a.sublimit, pool)
            out.append(e)
            print(f'draw {a.ctrl or "real"} {i} E {1 if e is None else e} timedout {e is None} {time.time()-t0:.1f}', flush=True)
        tos = sum(1 for e in out if e is None)
        print(f'{a.pair} {a.ctrl or "real"} dec {lo}-{hi}: E=1 in {sum(1 for e in out if e != 0)} of {len(out)}; unresolved {tos}; '
              f'resolved fits {sum(1 for e in out if e == 1)} of {len(out) - tos}; {time.time() - t00:.0f} s')
        return 0
    jobs = [(t, x, a.limit) for t, x in draws(a.pair, a.n, a.seed)[a.ctrl][lo:hi + 1]]
    t0 = time.time()
    with Pool(4) as pool:
        raw = pool.map(_job, jobs)
    for i, (e, to, sec) in zip(range(lo, hi + 1), raw):
        print(f'draw {a.ctrl} {i} E {e} timedout {to} {sec:.1f}')
    tos = sum(1 for _, t, _ in raw if t)
    print(f'{a.pair} {a.ctrl} {lo}-{hi}: E=1 in {sum(e for e, _, _ in raw)} of {len(raw)}; timeouts {tos}; '
          f'resolved fits {sum(e for e, t, _ in raw if not t)} of {len(raw) - tos}; {time.time() - t0:.0f} s')
    return 0


if __name__ == '__main__':
    sys.exit(main())
