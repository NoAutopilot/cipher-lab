#!/usr/bin/env python3
"""erba-2006 test 4 (R12D-ERBA4, 6 Oct 2026): word-level constrained decoder for the letter-class design.
Pre-registered in PREREG-test4.md (pushed before the scored run). xs = word space; 8 token types = 8 letter classes;
a cipher word decodes only into an it21news dictionary word with the same class pattern. Control first (5 seeds,
held-out fold, target's exact word-length profile); target and 10 shuffled nulls only if the control mean >= 0.60.
Usage: python3 test4_wordconstrained.py [--quick]"""
import gzip, math, os, random, sys
from collections import Counter
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..', '..'))
D = os.path.join(ROOT, 'tools/data/it21news')
LM_FOLDS = ['y2005_06', 'y2007', 'y2008', 'y2009_10']
CTL_FOLD = 'y2011_26'
A = 'abcdefghilmnopqrstuvz'
IX = {c: i for i, c in enumerate(A)}
MAP = {'j': 'i', 'k': 'c', 'w': 'v', 'x': 's', 'y': 'i'}
K, NDICT, NCTL, RESTARTS, ITERS, GATE, NNULL, UNM = 8, 40000, 5, 8, 4000, 0.60, 10, math.log(0.01)
TYPES = ['cu', 'mi', 'fi', 'un', 'ro', 'ne', 'pi', 'me']
if '--quick' in sys.argv: NCTL, RESTARTS, ITERS = 1, 2, 800


def words(fold):
    for l in gzip.open(os.path.join(D, fold + '.txt.gz'), 'rt'):
        for w in l.split():
            w = ''.join(MAP.get(c, c) for c in w)
            if w and all(c in IX for c in w): yield w


def target_words():
    lines = [l.split() for l in open(os.path.join(HERE, 'transcription_bERB.txt')) if l.strip()]
    toks = [[t.rstrip('-').lower() for t in l] for l in lines]
    out = []
    for s in [sum(toks[0:17], []), sum(toks[17:20], []), sum(toks[20:22], [])]:
        cur = []
        for t in s + ['xs']:
            if t == 'xs':
                if cur: out.append([TYPES.index(x) for x in cur])
                cur = []
            else: cur.append(t)
    return out


class Dict:
    def __init__(self, cnt):
        top = cnt.most_common(NDICT)
        self.by_len = {}
        for L in sorted({len(w) for w, _ in top}):
            ws = [(w, f) for w, f in top if len(w) == L]
            self.by_len[L] = (np.array([[IX[c] for c in w] for w, _ in ws]), np.array([f for _, f in ws], float),
                              [w for w, _ in ws])
        self.pw = None

    def pat(self, key, L):
        M, F, W = self.by_len[L]
        return (key[M] * (K ** np.arange(L))).sum(1)

    def score(self, key, cws, decode=False):
        s, dec, cache = 0.0, [], {}
        for cw in cws:
            L = len(cw)
            if L not in self.by_len: s += UNM; dec.append(None); continue
            if L not in cache: cache[L] = self.pat(key, L)
            h = sum(c * K ** i for i, c in enumerate(cw))
            m = cache[L] == h
            f = self.by_len[L][1][m].sum()
            s += math.log(f) if f > 0 else UNM
            if decode:
                dec.append(self.by_len[L][2][int(np.flatnonzero(m)[np.argmax(self.by_len[L][1][m])])] if f > 0 else None)
        return (s, dec) if decode else s


def rand_partition(rng):
    while True:
        k = np.array([rng.randrange(K) for _ in A])
        if len(set(k)) == K: return k


def anneal(dic, cws, rng):
    best, bk = -1e18, None
    for _ in range(RESTARTS):
        key = rand_partition(rng); cur = dic.score(key, cws)
        for it in range(ITERS):
            T = 3.0 * (1 - it / ITERS) + 0.05
            k2 = key.copy(); i = rng.randrange(len(A)); k2[i] = rng.randrange(K)
            if len(set(k2)) < K: continue
            s2 = dic.score(k2, cws)
            if s2 >= cur or rng.random() < math.exp((s2 - cur) / T): key, cur = k2, s2
        if cur > best: best, bk = cur, key.copy()
    return best, bk


def acc(dec, truth):
    a = n = 0
    for d, t in zip(dec, truth):
        n += len(t)
        if d: a += sum(x == y for x, y in zip(d, t))
    return a / n


def run_ctl(dic, plain, rng, label):
    tk = rand_partition(rng)
    cws = [[int(tk[IX[c]]) for c in w] for w in plain]
    s, k = anneal(dic, cws, rng)
    _, dec = dic.score(k, cws, True)
    ts, tdec = dic.score(tk, cws, True)
    a, o = acc(dec, plain), acc(tdec, plain)
    print(f'  {label}: solver acc {a:.3f}  oracle {o:.3f}  solver score {s:.1f} vs true {ts:.1f}  '
          f'{"solver>=true" if s >= ts - 1e-9 else "solver<true"}')
    print(f'    plain : {" ".join(plain)}\n    decode: {" ".join(d or "?" for d in dec)}')
    return a, o, s >= ts - 1e-9


def main():
    rng = random.Random(4)
    cnt = Counter()
    for f in LM_FOLDS: cnt.update(words(f))
    dic = Dict(cnt)
    tw = target_words()
    lens = [len(w) for w in tw]
    print(f'target: {len(tw)} words, {sum(lens)} letters, lengths {lens}; dictionary top {NDICT} of {len(cnt)} types')
    held = list(words(CTL_FOLD))
    bylen = {}
    for w in held: bylen.setdefault(len(w), []).append(w)
    print(f'held-out tokens {len(held)}; length-matched pools: ' + ', '.join(f'{L}:{len(bylen.get(L, []))}' for L in sorted(set(lens))))
    print('PRIMARY CONTROL (gate): length-profile-matched held-out tokens')
    res = [run_ctl(dic, [rng.choice(bylen[L]) for L in lens], rng, f'seed {i}') for i in range(NCTL)]
    mean = sum(r[0] for r in res) / len(res)
    print(f'  mean solver acc {mean:.3f} (gate {GATE}); mean oracle {sum(r[1] for r in res)/len(res):.3f}; '
          f'solver>=true {sum(r[2] for r in res)}/{len(res)}')
    print('SECONDARY CONTROL (not gated): contiguous held-out windows, ~100 letters, real word boundaries')
    sec = []
    for i in range(NCTL):
        st = rng.randrange(len(held) - 200); win = []
        while sum(map(len, win)) < sum(lens): win.append(held[st]); st += 1
        sec.append(run_ctl(dic, win, rng, f'window {i}'))
    print(f'  mean solver acc {sum(r[0] for r in sec)/len(sec):.3f}; mean oracle {sum(r[1] for r in sec)/len(sec):.3f}')
    if mean < GATE:
        print(f'VERDICT: CONTROL BELOW GATE ({mean:.3f} < {GATE}) -- target not decoded (control-first order).')
        return 3
    s, k = anneal(dic, tw, rng)
    _, dec = dic.score(k, tw, True)
    matched = sum(d is not None for d in dec) / len(dec)
    flat = [t for w in tw for t in w]; nulls = []
    for i in range(NNULL):
        rng.shuffle(flat); it = iter(flat); nw = [[next(it) for _ in w] for w in tw]
        nulls.append(anneal(dic, nw, rng)[0])
    print(f'TARGET score {s:.1f}, matched words {matched:.2f}; nulls max {max(nulls):.1f} mean {sum(nulls)/len(nulls):.1f}')
    print('  key: ' + ' '.join(f'{TYPES[c]}={"".join(a for a, kk in zip(A, k) if kk == c)}' for c in range(K)))
    print('  decode: ' + ' '.join(d or '?' for d in dec))
    moves = s > max(nulls) and matched >= 0.60
    print('VERDICT: ' + ('target moves (exceeds all nulls, >=60% matched) -- grade S candidate, needs judge + verifier'
                         if moves else 'target does not move -- negative under this design at the control\'s power'))
    return 0


if __name__ == '__main__':
    sys.exit(main())
