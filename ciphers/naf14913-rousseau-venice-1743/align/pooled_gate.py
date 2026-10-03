#!/usr/bin/env python3
"""Pooled f.206 + f.216v consistency run under FT4b's gate form (FT4d, account-4, 3 Oct 2026; NOTES.md "FT4d").

Pre-registered: this script (statistic, controls, threshold, n, limit) was committed and pushed before its first run.
Model as align/gate_pair.py (exact coverage of each slip's letters by its passage's groups, every free group 1..MAXLEN
letters, every repeated code consistent within its passage), both pairs at once:
  pair 1 = ciphertext.txt / slip_f206r.txt (maxlen 9, as FT4), pair 2 = ciphertext_f216v.txt / slip_f217r.txt (maxlen 12, as FT4c).
FT4's ten C codes are pinned to their f.206 aligned chunks in both passages (379 as 'xinterets', NOTES FT4) (the key that PASSed FT4c's gate).
Statistic Hp: over the non-C codes that occur in BOTH passages ("shared"), the largest sum of occurrences (both passages)
of a set of shared codes that can be TIED -- one identical chunk at every occurrence in both passages -- in a pair of
segmentations that exist together (untied shared codes may differ between the passages, still consistent within each).
Controls (pooled N, as FT4b's two): (a) value permutation: pair 2's non-C code labels permuted at random among its own
non-C distinct labels (the shared label set is unchanged; which positions carry a shared label moves), 100 draws;
(b) pairing shuffle: both passages' group orders shuffled independently, pins kept on their codes, 100 draws.
A control run that times out counts at the H of the pin set it was on (high, conservative); the real run that times out
on a set counts it as not reached. Gate: Hp >= 5 AND Hp > p95(a) AND Hp > p95(b); fewer than 5 shared non-C occurrences
= non-test. Forced codes: with the C pins fixed, a shared code whose chunks feasible in both relaxed passages are exactly
one is forced if tied; it enters key.tsv at C only if the gate PASSes and the code is in the real best tied set.
  python3 pooled_gate.py [--n 100] [--limit 4] [--seed 7]
"""
import argparse, itertools, os, random, sys, time
from collections import Counter
from multiprocessing import Pool
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import gate_pair as g

T = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PINS = dict(g.PINS, **{'379': 'xinterets'})  # FT4's aligned chunk ([x]interets, 'aux interets'); 379 is not in f.216v


def subs(text, ml):
    return {text[i:i + l] for l in range(1, ml + 1) for i in range(len(text) - l + 1)}


def Hp(A, B, scA, scB, limit, high):
    pa = {c: v for c, v in PINS.items() if c in A}
    pb = {c: v for c, v in PINS.items() if c in B}
    ca, cb = Counter(A), Counter(B)
    X = sorted(c for c in set(ca) & set(cb) if c not in PINS)
    sa, sb = subs(scA.text, scA.maxlen), subs(scB.text, scB.maxlen)
    cand = {}
    for x in X:
        cand[x] = [s for s in sa & sb if bin(scA.smask(s)).count('1') >= ca[x] and bin(scB.smask(s)).count('1') >= cb[x]
                   and scA.feasible(A, dict(pa, **{x: s})) and scB.feasible(B, dict(pb, **{x: s}))]
    X = [x for x in X if cand[x]]
    sets = sorted(((sum(ca[x] + cb[x] for x in S), S) for r in range(len(X), 0, -1) for S in itertools.combinations(X, r)),
                  key=lambda z: -z[0])
    deadline = time.time() + limit
    for h, S in sets:
        S = sorted(S, key=lambda x: len(cand[x]))
        amap = {}

        def rec(j):
            if time.time() > deadline:
                raise TimeoutError
            if j == len(S):
                ra = scA.consistent(A, dict(pa, **amap), deadline)
                if ra is None:
                    raise TimeoutError
                if not ra:
                    return False
                rb = scB.consistent(B, dict(pb, **amap), deadline)
                if rb is None:
                    raise TimeoutError
                return rb
            for s in cand[S[j]]:
                amap[S[j]] = s
                if scA.feasible(A, dict(pa, **amap)) and scB.feasible(B, dict(pb, **amap)) and rec(j + 1):
                    return True
                del amap[S[j]]
            return False
        try:
            if rec(0):
                return h, dict(amap), False
        except TimeoutError:
            if high:
                return h, {}, True
            deadline = time.time() + limit
    return 0, {}, False


def _job(args):
    A, B, ta, tb, limit = args
    h, _, to = Hp(A, B, g.Scorer(ta, 9), g.Scorer(tb, 12), limit, True)
    return h, to


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--n', type=int, default=100)
    ap.add_argument('--limit', type=float, default=4.0)
    ap.add_argument('--seed', type=int, default=7)
    a = ap.parse_args()
    A, ta = g.load(os.path.join(T, 'ciphertext.txt'), os.path.join(T, 'slip_f206r.txt'))
    B, tb = g.load(os.path.join(T, 'ciphertext_f216v.txt'), os.path.join(T, 'slip_f217r.txt'))
    ca, cb = Counter(A), Counter(B)
    X = sorted((c for c in set(ca) & set(cb) if c not in PINS), key=int)
    occ = sum(ca[x] + cb[x] for x in X)
    print(f'pair1 {len(A)} groups / {len(ta)} letters; pair2 {len(B)} groups / {len(tb)} letters')
    print('shared non-C codes (f206, f216v):', {x: (ca[x], cb[x]) for x in X}, 'occurrences', occ)
    if occ < 5:
        print('NON-TEST'); return 4
    scA, scB = g.Scorer(ta, 9), g.Scorer(tb, 12)
    H, tied, to = Hp(A, B, scA, scB, a.limit * 15, False)
    print(f'REAL: Hp = {H}; tied {tied}; timeouts on higher sets: {to}')
    # forced analysis (relaxed, pins fixed)
    pa = {c: v for c, v in PINS.items() if c in A}; pb = {c: v for c, v in PINS.items() if c in B}
    sa, sb = subs(ta, 9), subs(tb, 12)
    for x in X:
        cs = sorted(s for s in sa & sb if scA.feasible(A, dict(pa, **{x: s})) and scB.feasible(B, dict(pb, **{x: s})))
        print(f'  forced-check {x}: {len(cs)} joint chunk(s) {cs[:10]}')
    rng = random.Random(a.seed)
    labels = sorted(c for c in set(B) if c not in PINS)
    ja, jb = [], []
    for _ in range(a.n):
        p = labels[:]; rng.shuffle(p); m = dict(zip(labels, p))
        ja.append((A, [m.get(t, t) for t in B], ta, tb, a.limit))
    for _ in range(a.n):
        s1, s2 = A[:], B[:]; rng.shuffle(s1); rng.shuffle(s2)
        jb.append((s1, s2, ta, tb, a.limit))
    res = {}
    with Pool(4) as pool:
        for name, jobs in (('a value permutation', ja), ('b pairing shuffle', jb)):
            raw = pool.map(_job, jobs)
            hs = sorted(h for h, _ in raw)
            p95 = hs[int(0.95 * len(hs)) - 1]
            ge = sum(1 for h in hs if h >= H)
            print(f'CONTROL ({name}, n={len(hs)}): mean {sum(hs)/len(hs):.2f}, p95 {p95}, max {hs[-1]}, '
                  f'timeouts (counted high) {sum(1 for _, t in raw if t)}, >= real {ge} (p = {(ge+1)/(len(hs)+1):.4f})')
            print('  Hp distribution:', sorted(Counter(hs).items()))
            res[name] = p95
    ok = H >= 5 and all(H > p for p in res.values())
    print('GATE', 'PASS' if ok else 'FAIL', f'(Hp={H} >= 5 and > p95 of both controls: {res})')
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main())
