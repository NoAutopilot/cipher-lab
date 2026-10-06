#!/usr/bin/env python3
"""erba-2006 spec test 3 (R12D-ERBA3, 6 Oct 2026): letter-like design. Each digraph token stands for one plaintext
LETTER CLASS (a polyphonic letter cipher: 9 case-folded token types cannot cover Italian's ~21 letters one-to-one, so a
letter-like design with this alphabet must map several letters to one token). Pre-registered in PREREG-test3.md.

Variants: V1 xs = word space (8 classes, spaces known); V2 xs = one more class (9 classes, no spaces).
LM: letter bigram (+ space in V1) from tools/data/it21news folds y2005_06..y2009_10; control text from the held-out
fold y2011_26 (no overlap with the LM). Key = assignment of the 21 letters to K classes (every class used).
Solver: simulated annealing over the key maximising the forward log-likelihood of the token sequence; Viterbi decode.
Control: real it21news window of the target's own length, enciphered under a random K-class partition, same solver.
Reported per control: letter accuracy of the solver's decode and of the TRUE key's Viterbi decode (oracle ceiling).
Usage: python3 test3_letterclass.py [--quick]"""
import gzip, math, os, random, sys
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..', '..'))
D = os.path.join(ROOT, 'tools/data/it21news')
LM_FOLDS = ['y2005_06', 'y2007', 'y2008', 'y2009_10']
CTL_FOLD = 'y2011_26'
A = 'abcdefghilmnopqrstuvz'
MAP = {'j': 'i', 'k': 'c', 'w': 'v', 'x': 's', 'y': 'i'}
NCTL, RESTARTS, ITERS, GATE = 5, 8, 5000, 0.60
if '--quick' in sys.argv: NCTL, RESTARTS, ITERS = 1, 2, 800


def norm(line):
    return ' '.join(''.join(MAP.get(c, c) for c in w) for w in line.split())


def load(fold):
    return [norm(l) for l in gzip.open(os.path.join(D, fold + '.txt.gz'), 'rt') if l.strip()]


def bigram(lines, spaces):
    sy = A + (' ' if spaces else '')
    ix = {c: i for i, c in enumerate(sy)}
    M = np.full((len(sy) + 1, len(sy)), 0.5)  # last row = start
    for l in lines:
        s = l if spaces else l.replace(' ', '')
        prev = len(sy)
        for c in s:
            M[prev, ix[c]] += 1; prev = ix[c]
    return np.log(M / M.sum(1, keepdims=True)), sy


def target_tokens():
    lines = [l.split() for l in open(os.path.join(HERE, 'transcription_bERB.txt')) if l.strip()]
    toks = [[t.rstrip('-').lower() for t in l] for l in lines]
    return [sum(toks[0:17], []), sum(toks[17:20], []), sum(toks[20:22], [])]


def loglik(key, obs, LP, nlet):
    """obs: list of class ids, -1 = known space. key: array letter->class. Forward algorithm, log-space."""
    K = LP.shape[1]
    out = 0.0
    alpha = None
    for o in obs:
        if o == -1:
            allowed = np.zeros(K, bool); allowed[nlet] = True
        else:
            allowed = np.zeros(K, bool); allowed[:nlet] = key == o
        if alpha is None:
            v = LP[-1].copy()
        else:
            m = alpha.max()
            v = m + np.log(np.exp(alpha - m) @ np.exp(LP[:-1]))
        v[~allowed] = -np.inf
        out_m = v.max(); alpha = v - out_m; out += out_m
    return out + math.log(np.exp(alpha).sum())


def viterbi(key, obs, LP, nlet, sy):
    K = LP.shape[1]; back = []; delta = None
    for o in obs:
        allowed = np.zeros(K, bool)
        if o == -1: allowed[nlet] = True
        else: allowed[:nlet] = key == o
        if delta is None:
            v = LP[-1].copy(); b = np.zeros(K, int)
        else:
            sc = delta[:, None] + LP[:-1]; b = sc.argmax(0); v = sc.max(0)
        v[~allowed] = -np.inf; back.append(b); delta = v
    i = int(delta.argmax()); path = [i]
    for b in reversed(back[1:]):
        i = int(b[i]); path.append(i)
    return ''.join(sy[i] for i in reversed(path))


def anneal(obs, K, LP, nlet, rng):
    best, bk = -1e18, None
    for r in range(RESTARTS):
        key = np.array([rng.randrange(K) for _ in range(nlet)])
        for c in range(K): key[rng.randrange(nlet)] = c  # rough cover, fixed below
        while len(set(key)) < K: key[rng.randrange(nlet)] = rng.randrange(K)
        cur = loglik(key, obs, LP, nlet); kb, sb = key.copy(), cur
        for it in range(ITERS):
            T = 3.0 * (1 - it / ITERS) + 0.05
            k2 = key.copy(); k2[rng.randrange(nlet)] = rng.randrange(K)
            if len(set(k2)) < K: continue
            s2 = loglik(k2, obs, LP, nlet)
            if s2 >= cur or rng.random() < math.exp((s2 - cur) / T):
                key, cur = k2, s2
                if cur > sb: kb, sb = key.copy(), cur
        if sb > best: best, bk = sb, kb
    return bk, best


def rand_partition(K, nlet, rng):
    while True:
        key = np.array([rng.randrange(K) for _ in range(nlet)])
        if len(set(key)) == K: return key


def acc(a, b):
    pairs = [(x, y) for x, y in zip(a, b) if y != ' ']
    return sum(x == y for x, y in pairs) / len(pairs)


def main():
    rng = random.Random(3)
    lm_lines = sum((load(f) for f in LM_FOLDS), [])
    ctl_text = ' '.join(load(CTL_FOLD))
    T = target_tokens()
    allt = [t for s in T for t in s]
    print(f'target tokens {len(allt)}; types {sorted(set(allt))}')
    res = {}
    for var, spaces in (('V1 xs=space', True), ('V2 xs=class', False)):
        LP, sy = bigram(lm_lines, spaces); nlet = len(A)
        types = sorted(set(allt) - ({'xs'} if spaces else set())); K = len(types); cid = {t: i for i, t in enumerate(types)}
        obs = []
        for s in T:
            for t in s:
                obs.append(-1 if (spaces and t == 'xs') else cid[t])
            if spaces: obs.append(-1)
        if spaces:  # collapse doubled spaces, drop leading/trailing
            o2 = []
            for o in obs:
                if o == -1 and (not o2 or o2[-1] == -1): continue
                o2.append(o)
            obs = o2[:-1] if o2 and o2[-1] == -1 else o2
        nlet_t = sum(o != -1 for o in obs)
        print(f'\n== {var}: K={K}, target letters {nlet_t}, obs len {len(obs)}')
        accs, oracles, searchok = [], [], 0
        for c in range(NCTL):
            i = rng.randrange(len(ctl_text) - 3000)
            i = ctl_text.index(' ', i) + 1
            chunk, n = [], 0
            for ch in ctl_text[i:]:
                if not spaces and ch == ' ': continue
                chunk.append(ch); n += ch != ' '
                if n >= nlet_t: break
            plain = ''.join(chunk)
            tk = rand_partition(K, nlet, rng)
            cobs = [-1 if ch == ' ' else int(tk[A.index(ch)]) for ch in plain]
            ok = acc(viterbi(tk, cobs, LP, nlet, sy), plain)
            k, sc = anneal(cobs, K, LP, nlet, rng)
            dec = viterbi(k, cobs, LP, nlet, sy)
            a = acc(dec, plain); accs.append(a); oracles.append(ok)
            searchok += sc >= loglik(tk, cobs, LP, nlet) - 1e-6
            print(f'  control {c+1}: solver letter acc {a:.3f}; true-key (oracle) acc {ok:.3f}; '
                  f'loglik solver {sc:.1f} vs true {loglik(tk, cobs, LP, nlet):.1f}')
            print(f'    plain: {plain[:80]}\n    dec  : {dec[:80]}')
        mean = sum(accs) / len(accs); omean = sum(oracles) / len(oracles)
        print(f'control mean solver acc {mean:.3f} (gate {GATE}); oracle mean {omean:.3f}; solver loglik >= true-key loglik in {searchok}/{NCTL}')
        if mean >= GATE:
            k, sc = anneal(obs, K, LP, nlet, rng)
            dec = viterbi(k, obs, LP, nlet, sy)
            print(f'TARGET decode (loglik {sc:.1f}): {dec}')
            print('  key: ' + ', '.join(f"{t}={''.join(A[j] for j in range(nlet) if k[j]==cid[t])}" for t in types))
            res[var] = f'control {mean:.3f} >= gate; target decoded'
        else:
            print(f'VERDICT {var}: CONTROL BELOW GATE -- untestable by this method at N={nlet_t}; target not run')
            res[var] = f'CONTROL BELOW GATE ({mean:.3f}, oracle {omean:.3f})'
    print('\nSUMMARY: ' + '; '.join(f'{k}: {v}' for k, v in res.items()))


if __name__ == '__main__':
    main()
