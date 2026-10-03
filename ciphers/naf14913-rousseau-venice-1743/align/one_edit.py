#!/usr/bin/env python3
"""FT4i (account-4, 3 Oct 2026): one-edit alignment of an infeasible cipher+slip pair. Written and pushed before any
score (align/PREREG-FT4i.md). A different instrument from gate_pair.py / f249_diag.py, which require a
repetition-consistent exact-coverage fit with NO edit; both pairs f.249/f.250 and f.213/f.214r are proved to have none.

Model (exact coverage of the slip's letters by the passage's groups, in order): a free (non-repeated) group takes
1..MAXLEN letters; every occurrence of a repeated code takes one identical chunk (no pins: the ten f.206 C values are
not imposed). Exactly ONE edit is allowed, anywhere in the passage:
  W  wildcard: one group occurrence is released from its code and takes 0..MAXLEN letters
     (length >= 1: a misread digit, or one polyvalent use of that code; length 0: an extra group in the passage);
  D  dropped group: one free group of 1..MAXLEN letters is inserted between two groups (or at an end).
Statistic E: 1 if a fit with at most one edit exists, 0 if proved none; on timeout a control counts 1 (conservative
high), the real pair counts 0. E0 (the same with no edit) is printed beside it. For the real pair the script also
lists every single edit that gives a fit (edit, position, code, length) -- descriptive.
Controls (each can differ: E depends on the order of both sides):
  (s) wrong slip: the slip's words shuffled, same letters and words, the real passage, N draws;
  (g) group shuffle: the passage's group order shuffled, the real slip, N draws.
Gate (per pair): PASS if E_real = 1 AND the share of E = 1 is <= 0.05 in each control (p95 of E is 0).
  E_real = 1 with a control share > 0.05: the one-edit fit is not discriminating (non-informative, not a pass).
  E_real = 0: the pair needs two or more edits under this model; a negative for the one-edit model only, not for the key.
Search: an exact CP-SAT model (ortools): group start/length variables, a table constraint tying each repeated-code
occurrence's (start, length) to a chunk id shared by the code unless that occurrence is the wildcard. Sanity checks
(run before the gate): f216v (known to fit) gives E0 True; f213 and f249 give E0 False, as f213_diag/f249_diag proved.
  python3 one_edit.py --pair f213 [--n 40] [--limit 15] [--seed 3]   (pair f216v = solver sanity only)
"""
import argparse, os, random, sys, time
from collections import Counter
from multiprocessing import Pool
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import gate_pair as g

T = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PAIRS = {'f216v': ('ciphertext_f216v.txt', 'slip_f217r.txt'), 'f213': ('ciphertext_f213.txt', 'slip_f214r.txt'), 'f249': ('ciphertext_f249.txt', 'slip_f250.txt')}
MAXLEN = 12
sys.setrecursionlimit(100000)


def solve(toks, text, edits, limit, force=None, workers=1):
    """CP-SAT exact model. Returns True (fit), False (proved none), None (timed out).
    force: ('W', i) or ('D', i) fixes that one edit on (and edits = 1)."""
    from ortools.sat.python import cp_model
    n, L = len(toks), len(text)
    cnt = Counter(toks)
    rep = sorted(t for t, c in cnt.items() if c > 1)
    m = cp_model.CpModel()
    chunks = {}
    rows = []
    for p in range(L):
        for l in range(1, MAXLEN + 1):
            if p + l > L:
                break
            rows.append((p, l, chunks.setdefault(text[p:p + l], len(chunks))))
    rows += [(p, 0, len(chunks)) for p in range(L + 1)]  # zero-length (wildcard only)
    nid = len(chunks) + 1
    w = [m.NewBoolVar(f'w{i}') for i in range(n)]
    d = [m.NewBoolVar(f'd{i}') for i in range(n + 1)]
    m.Add(sum(w) + sum(d) <= edits)
    if force:
        m.Add((w if force[0] == 'W' else d)[force[1]] == 1)
    ins = []
    for i in range(n + 1):
        x = m.NewIntVar(0, MAXLEN, f'ins{i}')
        m.Add(x == 0).OnlyEnforceIf(d[i].Not())
        m.Add(x >= 1).OnlyEnforceIf(d[i])
        ins.append(x)
    a = [m.NewIntVar(0, L, f'a{i}') for i in range(n)]
    ln = [m.NewIntVar(0, MAXLEN, f'l{i}') for i in range(n)]
    m.Add(a[0] == ins[0])
    for i in range(n):
        m.Add(ln[i] >= 1).OnlyEnforceIf(w[i].Not())
        nxt = a[i + 1] if i + 1 < n else None
        if nxt is not None:
            m.Add(nxt == a[i] + ln[i] + ins[i + 1])
    m.Add(a[n - 1] + ln[n - 1] + ins[n] == L)
    kc = {c: m.NewIntVar(0, nid - 1, f'k{c}') for c in rep}
    for i, t in enumerate(toks):
        if t in kc:
            ki = m.NewIntVar(0, nid - 1, f'ki{i}')
            m.AddAllowedAssignments([a[i], ln[i], ki], rows)
            m.Add(ki == kc[t]).OnlyEnforceIf(w[i].Not())
    s = cp_model.CpSolver()
    s.parameters.max_time_in_seconds = limit
    s.parameters.num_search_workers = workers
    r = s.Solve(m)
    if r in (cp_model.OPTIMAL, cp_model.FEASIBLE):
        return True
    if r == cp_model.INFEASIBLE:
        return False
    return None


def E(toks, text, limit, high):
    r = solve(toks, text, 1, limit)
    if r is None:
        return (1 if high else 0), True
    return (1 if r else 0), False


def _force(j):
    toks, text, limit, f = j
    return solve(toks, text, 1, limit, force=f)


def _job(a):
    toks, text, limit = a
    return E(toks, text, limit, True)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--pair', required=True, choices=sorted(PAIRS))
    ap.add_argument("--n", type=int, default=40)
    ap.add_argument("--limit", type=float, default=15.0)
    ap.add_argument('--seed', type=int, default=3)
    ap.add_argument('--real-only', action='store_true')
    a = ap.parse_args()
    c, s = PAIRS[a.pair]
    toks, text = g.load(os.path.join(T, c), os.path.join(T, s))
    words = [w for w in (g.letters(x) for x in ' '.join(l for l in open(os.path.join(T, s), encoding='utf-8')
                                                      if not l.startswith('#')).split()) if w]
    assert ''.join(words) == text
    print(f'pair {a.pair}: groups {len(toks)}, distinct {len(set(toks))}, slip letters {len(text)}, words {len(words)}, maxlen {MAXLEN}')
    t0 = time.time()
    e0 = solve(toks, text, 0, a.limit * 3, workers=4)
    print(f'REAL E0 (no edit) = {e0} ({time.time()-t0:.1f} s)  (True fit / False proved none / None timed out)')
    t0 = time.time()
    r = solve(toks, text, 1, a.limit * 3, workers=4)
    er, to = (1 if r else 0), r is None
    print(f'REAL E (<= 1 edit) = {er}; timed out {to} ({time.time()-t0:.1f} s)')
    if r:
        with Pool(4) as pool:
            js = [(toks, text, a.limit, ('W', i)) for i in range(len(toks))] + \
                 [(toks, text, a.limit, ('D', i)) for i in range(len(toks) + 1)]
            res = pool.map(_force, js)
        ok = [(j[3], toks[j[3][1]] if j[3][0] == 'W' else '-') for j, x in zip(js, res) if x]
        tos = sum(1 for x in res if x is None)
        print(f'single edits giving a fit: {len(ok)} of {len(js)} (timed out {tos})')
        for (k, i), c in ok:
            print(f'  {k} at group {i} ({c})')
    if a.real_only:
        return 0
    rng = random.Random(a.seed)
    js, jg = [], []
    for _ in range(a.n):
        w = words[:]; rng.shuffle(w); js.append((toks, ''.join(w), a.limit))
    for _ in range(a.n):
        x = toks[:]; rng.shuffle(x); jg.append((x, text, a.limit))
    shares = {}
    with Pool(4) as pool:
        for name, jobs in (('s wrong slip (words shuffled)', js), ('g group shuffle', jg)):
            raw = pool.map(_job, jobs)
            k1 = sum(e for e, _ in raw)
            share = k1 / len(raw)
            tos = sum(1 for _, t in raw if t)
            res1 = sum(e for e, t in raw if not t)
            print(f'CONTROL ({name}, n={len(raw)}): E=1 in {k1} ({share:.3f}); timeouts counted high {tos}; '
                  f'among resolved draws E=1 in {res1} of {len(raw) - tos} (descriptive)')
            shares[name] = share
    ok = er == 1 and all(v <= 0.05 for v in shares.values())
    verdict = 'PASS' if ok else ('NON-INFORMATIVE (one-edit fit not discriminating)' if er == 1 else 'FAIL (needs >= 2 edits)')
    print(f'GATE {verdict} (E_real={er}, control shares {shares})')
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main())
