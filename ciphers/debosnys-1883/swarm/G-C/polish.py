#!/usr/bin/env python3
"""DEB-SWARM-C polish stage (29 Sept 2026): first-improvement hill-climb of a mixed-unit key under
   unit-bigram log-likelihood  +  lam * character 5-gram information gain of the concatenated decode
(per character: log P_5gram(c | 4 previous chars) - log P_unigram(c), stupid back-off 0.4, no spaces, since the cipher
shows no word divisions). The character model sees across unit joins (mon+de -> monde), which a unit bigram cannot.
Lines are scored separately and cached; a move rescans only the lines that contain the moved sign(s).
Moves: every sign x every unused unit (injective) or every unit (homophonic), and every sign pair swap; repeat sweeps
until a sweep makes no improvement or --sweeps is reached."""
import collections, math, os, random, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import syll

_CM = {}


def char_model(order=5, verse=True):
    k = (order, verse)
    if k in _CM:
        return _CM[k]
    ws = []
    for f in syll.LM_FILES:
        ws.extend(syll.words(f))
    if verse:
        keep = syll.FR19; syll.FR19 = os.path.join(syll.ROOT, 'tools', 'data', 'fr19v')
        ws.extend(syll.words('pg6099_Les_Fleurs_du_Mal.txt.gz') * 3); syll.FR19 = keep
    text = ''.join(ws)
    cnt = [collections.Counter() for _ in range(order + 1)]
    for n in range(1, order + 1):
        c = cnt[n]
        for i in range(len(text) - n + 1):
            c[text[i:i + n]] += 1
    tot = len(text)
    luni = {ch: math.log(v / tot) for ch, v in cnt[1].items()}
    _CM[k] = (cnt, luni, order)
    return _CM[k]


class CharScorer:
    def __init__(self, order=5, verse=True):
        self.cnt, self.luni, self.order = char_model(order, verse)
        self.cache = {}

    def lp(self, h, c):
        k = (h, c)
        r = self.cache.get(k)
        if r is not None:
            return r
        mult = 1.0
        while True:
            if not h:
                r = self.luni.get(c, math.log(1e-6)) + math.log(mult); break
            num = self.cnt[len(h) + 1].get(h + c, 0)
            if num:
                r = math.log(mult * num / self.cnt[len(h)][h]); break
            h = h[1:]; mult *= 0.4
        self.cache[k] = r
        return r

    def gain(self, s):
        tot = 0.0
        o = self.order - 1
        for i, c in enumerate(s):
            tot += self.lp(s[max(0, i - o):i], c) - self.luni.get(c, math.log(1e-6))
        return tot


def polish(lines, key, lm, lam=1.0, sweeps=3, injective=True, seed=1, verbose=True):
    """lines: list of sign lists; key: sign -> unit string (unit must be in lm.vocab). Returns (score, key)."""
    cs = CharScorer()
    rng = random.Random(seed)
    signs = sorted({s for l in lines for s in l})
    where = collections.defaultdict(set)
    for li, l in enumerate(lines):
        for s in l:
            where[s].add(li)
    csig = collections.Counter(s for l in lines for s in l)
    key = dict(key)
    idx = lm.idx

    def line_score(l):
        u = [idx[key[s]] for s in l]
        b = sum(lm.lp(x, y) for x, y in zip(u, u[1:]))
        return b + lam * cs.gain(''.join(key[s] for s in l))

    def chan():
        Cu = collections.Counter()
        for s in signs:
            Cu[key[s]] += csig[s]
        return -sum(v * math.log(v) for v in Cu.values())
    ls = [line_score(l) for l in lines]
    cur = sum(ls) + (0 if injective else chan())
    vocab = lm.vocab
    for sw in range(sweeps):
        improved = 0
        order = signs[:]; rng.shuffle(order)
        for s in order:
            used = set(key.values())
            cands = [u for u in vocab if u != key[s] and (not injective or u not in used)]
            # swaps with other signs
            others = [t for t in signs if t != s and key[t] != key[s]]
            best = (0.0, None)
            old = key[s]
            L = where[s]
            base = sum(ls[i] for i in L)
            ch0 = 0 if injective else chan()
            for u in cands:
                key[s] = u
                d = sum(line_score(lines[i]) for i in L) - base
                if not injective:
                    d += chan() - ch0
                if d > best[0] + 1e-9:
                    best = (d, ('set', u))
            key[s] = old
            for t in others:
                L2 = L | where[t]
                b2 = sum(ls[i] for i in L2)
                key[s], key[t] = key[t], key[s]
                d = sum(line_score(lines[i]) for i in L2) - b2
                key[s], key[t] = key[t], key[s]
                if d > best[0] + 1e-9:
                    best = (d, ('swap', t))
            if best[1]:
                kind, x = best[1]
                if kind == 'set':
                    key[s] = x; aff = L
                else:
                    key[s], key[x] = key[x], key[s]; aff = L | where[x]
                for i in aff:
                    ls[i] = line_score(lines[i])
                cur += best[0]; improved += 1
        if verbose:
            print(f'polish sweep {sw + 1}: {improved} moves, score {cur:.1f}', file=sys.stderr, flush=True)
        if not improved:
            break
    return cur, key


def anneal_combined(lines, key, lm, lam=1.0, iters=60000, T0=1.0, T1=0.05, injective=True, seed=1):
    """Metropolis anneal under the polish objective (unit bigram + lam * char gain), line-cached; starts from key.
    Returns the best (score, key) seen."""
    cs = CharScorer()
    rng = random.Random(seed)
    signs = sorted({s for l in lines for s in l})
    where = collections.defaultdict(set)
    for li, l in enumerate(lines):
        for s in l:
            where[s].add(li)
    key = dict(key); idx = lm.idx; vocab = lm.vocab

    def line_score(l):
        u = [idx[key[s]] for s in l]
        return sum(lm.lp(x, y) for x, y in zip(u, u[1:])) + lam * cs.gain(''.join(key[s] for s in l))
    ls = [line_score(l) for l in lines]
    cur = sum(ls); best = (cur, dict(key))
    used = set(key.values())
    for it in range(iters):
        T = T0 * (T1 / T0) ** (it / iters)
        s = rng.choice(signs)
        if rng.random() < 0.5:
            u = rng.choice(vocab)
            if u == key[s] or (injective and u in used):
                continue
            old = key[s]; L = where[s]
            b = sum(ls[i] for i in L); key[s] = u
            new = {i: line_score(lines[i]) for i in L}; d = sum(new.values()) - b
            if d >= 0 or rng.random() < math.exp(d / T):
                used.discard(old); used.add(u)
                for i, v in new.items():
                    ls[i] = v
                cur += d
            else:
                key[s] = old
        else:
            t = rng.choice(signs)
            if t == s or key[t] == key[s]:
                continue
            L = where[s] | where[t]
            b = sum(ls[i] for i in L)
            key[s], key[t] = key[t], key[s]
            new = {i: line_score(lines[i]) for i in L}; d = sum(new.values()) - b
            if d >= 0 or rng.random() < math.exp(d / T):
                for i, v in new.items():
                    ls[i] = v
                cur += d
            else:
                key[s], key[t] = key[t], key[s]
        if cur > best[0]:
            best = (cur, dict(key))
    return best
