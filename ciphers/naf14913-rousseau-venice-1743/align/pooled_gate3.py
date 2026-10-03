#!/usr/bin/env python3
"""Pooled three-pair consistency run: f.206 + f.216v + f.249r-v (FT4e, account-4, 3 Oct 2026; NOTES.md "FT4e").

Pre-registered: this script (statistic, controls, threshold, n, limit, seed) was committed and pushed before its first
scored run, and before the f.249 transcription was scored by anything. It extends align/pooled_gate.py (FT4d, two pairs)
to three pairs; what had to change for three pairs, and why, is listed here and nowhere else:
  1. "Shared" = a non-C code that occurs in AT LEAST TWO of the three passages (FT4d: in both of two).
  2. "Tied" = one identical chunk at every occurrence in every passage where the code occurs.
  3. Search: FT4d enumerated every subset of the shared codes in decreasing H (9 codes, 512 sets). Three pairs share
     too many codes for that, so the same maximum is found by branch-and-bound depth-first search (tie branches first,
     then the untied branch; prune when the running H plus every remaining code cannot beat the best found). On a time
     out a CONTROL run counts at the largest bound still open on the search stack (an upper bound: high, conservative,
     the analogue of FT4d's "the set it was on"); the REAL run counts the best fully checked set found (not reached).
  4. Control (a) permutes pair 2's and pair 3's non-C labels, each among its own non-C distinct labels (FT4d: pair 2's).
  5. Control (b) shuffles all three passages' group orders (FT4d: both).
  6. Pair 3 = ciphertext_f249.txt / slip_f250.txt, maxlen 12 (the slip's longest word, connoissance, has 12 letters).
Unchanged from FT4d: exact coverage of each slip's letters by its passage's groups; every free group 1..maxlen letters;
every repeated code consistent within its passage; FT4's ten C codes pinned to their f.206 aligned chunks in every
passage (379 as 'xinterets'); maxlen 9 for pair 1, 12 for pair 2.
Statistic Hp: the largest sum of occurrences (all passages) of a set of tied shared codes, in segmentations of the three
passages that exist together. Gate: Hp >= 5 AND Hp > p95(a) AND Hp > p95(b); fewer than 5 shared occurrences = non-test.
Key rule (as FT4d): a shared code whose joint chunks (pins fixed, relaxed, feasible in every passage where it occurs)
are exactly one AND that is in the real best tied set enters key.tsv at C only on a gate PASS.
Control (c), REPORTED BESIDE THE GATE, NOT PART OF IT (added because FT4d's control (b) could not vary at this N: the
pins fit only the real order, so every shuffle scored 0): pair 3's slip replaced by text from the OTHER pairs' slips --
words drawn at random without replacement from slips f.206r + f.217r, in random order, cut to exactly pair 3's letter
count. Because the decoy need not contain the pinned chunks (la reine, hongrie ...), pair 3 is run UNPINNED in (c) and
in the real-(c) statistic alike (pairs 1 and 2 keep their pins and real slips), so the decoy stays feasible and the
statistic can move either way: Hc(real) vs the Hc distribution over 100 decoys, same search, same time-out rules.
  python3 pooled_gate3.py [--n 100] [--limit 5] [--seed 7] [--skip-c]
"""
import argparse, os, random, sys, time
from collections import Counter
from multiprocessing import Pool
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import gate_pair as g

T = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PINS = dict(g.PINS, **{'379': 'xinterets'})
FILES = [('ciphertext.txt', 'slip_f206r.txt', 9), ('ciphertext_f216v.txt', 'slip_f217r.txt', 12),
         ('ciphertext_f249.txt', 'slip_f250.txt', 12)]


class Timeout(Exception):
    pass


def subs(text, ml):
    return {text[i:i + l] for l in range(1, ml + 1) for i in range(len(text) - l + 1)}


def Hp(P, texts, mls, limit, high, pinned=(True, True, True)):
    """P: list of token lists; returns (H, tied map, timed_out)."""
    scs = [g.Scorer(t, m) for t, m in zip(texts, mls)]
    pins = [{c: v for c, v in PINS.items() if c in A} if pinned[k] else {} for k, A in enumerate(P)]
    cnts = [Counter(A) for A in P]
    if not all(sc.feasible(A, pm) for sc, A, pm in zip(scs, P, pins)):
        return 0, {}, False
    allc = set().union(*[set(c) for c in cnts])
    X = [x for x in allc if x not in PINS and sum(1 for c in cnts if x in c) >= 2]
    where = {x: [k for k in range(len(P)) if x in cnts[k]] for x in X}
    occ = {x: sum(cnts[k][x] for k in where[x]) for x in X}
    deadline = time.time() + limit
    cand = {}
    for x in X:
        common = None
        for k in where[x]:
            s = subs(texts[k], mls[k])
            common = s if common is None else common & s
        cs = []
        for s in common:
            if time.time() > deadline:
                if high:
                    return sum(occ.values()), {}, True
                break
            if all(bin(scs[k].smask(s)).count('1') >= cnts[k][x] and scs[k].feasible(P[k], dict(pins[k], **{x: s}))
                   for k in where[x]):
                cs.append(s)
        if cs:
            cand[x] = sorted(cs, key=lambda s: (-len(s), s))
    X = sorted(cand, key=lambda x: (-occ[x], len(cand[x])))
    rem = [0] * (len(X) + 1)
    for i in range(len(X) - 1, -1, -1):
        rem[i] = rem[i + 1] + occ[X[i]]
    best = [0, {}]
    stack = []  # open bound per frame

    def leaf(amap):
        for k in range(len(P)):
            m = dict(pins[k], **{x: s for x, s in amap.items() if k in where[x]})
            r = scs[k].consistent(P[k], m, deadline)
            if r is None:
                raise Timeout
            if not r:
                return False
        return True

    def dfs(i, amap, h):
        if time.time() > deadline:
            raise Timeout
        if h + rem[i] <= best[0]:
            return
        if i == len(X):
            if leaf(amap):
                best[0], best[1] = h, dict(amap)
            return
        x = X[i]
        stack.append(h + rem[i])
        for s in cand[x]:
            amap[x] = s
            if all(scs[k].feasible(P[k], dict(pins[k], **{y: v for y, v in amap.items() if k in where[y]}))
                   for k in where[x]):
                dfs(i + 1, amap, h + occ[x])
            del amap[x]
        stack[-1] = h + rem[i + 1]  # only the untied branch left at this frame
        dfs(i + 1, amap, h)
        stack.pop()
    try:
        dfs(0, {}, 0)
    except Timeout:
        if high:
            return max([best[0]] + stack), {}, True
        return best[0], best[1], True
    return best[0], best[1], False


def _job(args):
    P, texts, mls, limit, pinned = args
    h, _, to = Hp(P, texts, mls, limit, True, pinned)
    return h, to


def decoy(words, L, rng):
    w = words[:]
    rng.shuffle(w)
    out = ''
    for x in w:
        out += x
        if len(out) >= L:
            break
    return out[:L]


def report(name, raw, H):
    hs = sorted(h for h, _ in raw)
    p95 = hs[int(0.95 * len(hs)) - 1]
    ge = sum(1 for h in hs if h >= H)
    print(f'CONTROL ({name}, n={len(hs)}): mean {sum(hs)/len(hs):.2f}, p95 {p95}, max {hs[-1]}, '
          f'timeouts (counted high) {sum(1 for _, t in raw if t)}, >= real {ge} (p = {(ge+1)/(len(hs)+1):.4f})')
    print('  distribution:', sorted(Counter(hs).items()))
    return p95


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--n', type=int, default=100)
    ap.add_argument('--limit', type=float, default=5.0)
    ap.add_argument('--seed', type=int, default=7)
    ap.add_argument('--skip-c', action='store_true')
    a = ap.parse_args()
    P, texts, mls = [], [], []
    for c, s, m in FILES:
        A, t = g.load(os.path.join(T, c), os.path.join(T, s))
        P.append(A); texts.append(t); mls.append(m)
    cnts = [Counter(A) for A in P]
    X = sorted((x for x in set().union(*[set(c) for c in cnts]) if x not in PINS and sum(1 for c in cnts if x in c) >= 2), key=int)
    occ = sum(sum(c[x] for c in cnts) for x in X)
    for k in range(3):
        print(f'pair{k+1} {len(P[k])} groups / {len(texts[k])} letters, maxlen {mls[k]}')
    print('shared non-C codes (occurrences per passage):', {x: tuple(c[x] for c in cnts) for x in X}, 'total', occ)
    if occ < 5:
        print('NON-TEST'); return 4
    H, tied, to = Hp(P, texts, mls, a.limit * 15, False)
    print(f'REAL: Hp = {H}; tied {dict(sorted(tied.items(), key=lambda z: int(z[0])))}; timed out: {to}')
    pins = [{c: v for c, v in PINS.items() if c in A} for A in P]
    for x in X:
        ks = [k for k in range(3) if x in cnts[k]]
        common = None
        for k in ks:
            s = subs(texts[k], mls[k]); common = s if common is None else common & s
        cs = sorted(s for s in common if all(g.Scorer(texts[k], mls[k]).feasible(P[k], dict(pins[k], **{x: s})) for k in ks))
        print(f'  forced-check {x}: {len(cs)} joint chunk(s) {cs[:10]}')
    rng = random.Random(a.seed)
    ja, jb, jc = [], [], []
    for _ in range(a.n):
        Q = [P[0]]
        for k in (1, 2):
            labels = sorted(c for c in set(P[k]) if c not in PINS)
            p = labels[:]; rng.shuffle(p); m = dict(zip(labels, p))
            Q.append([m.get(t, t) for t in P[k]])
        ja.append((Q, texts, mls, a.limit, (True, True, True)))
    for _ in range(a.n):
        Q = [A[:] for A in P]
        for q in Q:
            rng.shuffle(q)
        jb.append((Q, texts, mls, a.limit, (True, True, True)))
    words = [g.letters(w) for f in ('slip_f206r.txt', 'slip_f217r.txt')
             for l in open(os.path.join(T, f), encoding='utf-8') if not l.startswith('#') for w in l.split()]
    words = [w for w in words if w]
    for _ in range(a.n):
        jc.append((P, texts[:2] + [decoy(words, len(texts[2]), rng)], mls, a.limit, (True, True, False)))
    res = {}
    with Pool(4) as pool:
        res['a'] = report('a value permutation', pool.map(_job, ja), H)
        res['b'] = report('b pairing shuffle', pool.map(_job, jb), H)
        ok = H >= 5 and H > res['a'] and H > res['b']
        print('GATE', 'PASS' if ok else 'FAIL', f'(Hp={H} >= 5 and > p95 of (a) {res["a"]} and (b) {res["b"]})')
        if not a.skip_c:
            Hc, tc, toc = Hp(P, texts, mls, a.limit * 15, False, (True, True, False))
            print(f'REAL-(c) (pair 3 unpinned, real slip): Hc = {Hc}; timed out: {toc}')
            pc = report('c wrong-slip decoy from slips f206r+f217r, pair 3 unpinned; reported, not gated', pool.map(_job, jc), Hc)
            print(f'(c) {"real above p95" if Hc > pc else "real NOT above p95"} (Hc={Hc}, p95 {pc})')
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main())
