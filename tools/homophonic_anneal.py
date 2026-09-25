#!/usr/bin/env python3
"""Pure-Python simulated annealing for a homophonic simple substitution (no numpy needed).

  python3 tools/homophonic_anneal.py CIPHER.tsv --corpus A.txt [--corpus B.txt ...] [--order 3]
          [--restarts 8] [--iters 40000] [--skip DOT,COL] [--seed 1] [--out result.json] [--fix 70=q,33=u]
          [--noise 0.1]   error-tolerant solve: see anneal_noisy (LANE R6 CM2, 25 Sept 2026)
          [--robust 0.1]  bounded-loss n-gram scoring: see RobustModel (LANE R6 CM2)
          [--backoff]     interpolated absolute-discount n-gram of --order with recursive backoff: see BackoffModel
                          (LANE R7 CM3, 25 Sept 2026); lets --order 4 or 5 run on a 2 MB corpus without add-k sparsity
  python3 tools/homophonic_anneal.py --control PLAIN.txt --signs K --length N --corpus ... (matched control)

CIPHER.tsv: long format, header with a `sign` column (and optional `line`); rows whose sign is in --skip are
dropped. Every distinct sign is mapped to one plaintext letter a-z (u/v, i/j merged; umlauts folded). Score =
sum of log n-gram probabilities (add-k smoothed, order --order, from the --corpus files after the same
folding, word spaces removed) + a unigram term keeping the letter distribution near the corpus's
(--uni-weight). Several restarts; the best key and decoding are printed and written to --out.

--control: enciphers the first N letters of PLAIN.txt (after folding) with a random homophonic key of K
signs, homophones allotted to letters by corpus frequency, each occurrence picking a homophone at random;
then solves it blind with the same settings and prints the share of letters recovered. This is rule 3's
matched control: run it with the target's own N and K before reporting any negative on the target.

Test: python3 tools/tests/test_homophonic_anneal.py
"""
import argparse, json, math, random, re, sys, unicodedata
from collections import Counter

ALPHA = "abcdefghiklmnopqrstuwxyz"  # j->i, v->u


W_AS_UU = False


def fold(text):
    t = unicodedata.normalize("NFKD", text.lower())
    t = "".join(c for c in t if not unicodedata.combining(c))
    t = t.replace("ß", "ss").replace("j", "i").replace("v", "u")
    if W_AS_UU:
        t = t.replace("w", "uu")
    return re.sub(r"[^a-z]", "", t)


class Model:
    def __init__(self, texts, order=3, k=0.5):
        s = "".join(fold(t) for t in texts)
        self.order = order
        self.n = Counter(s[i:i + order] for i in range(len(s) - order + 1))
        self.c = Counter(s[i:i + order - 1] for i in range(len(s) - order + 2))
        self.uni = Counter(s)
        tot = sum(self.uni.values())
        self.freq = {a: (self.uni[a] + 0.5) / (tot + 0.5 * len(ALPHA)) for a in ALPHA}
        self.k, self.V = k, len(ALPHA)
        self.cache = {}

    def logp(self, g):
        v = self.cache.get(g)
        if v is None:
            v = math.log((self.n[g] + self.k) / (self.c[g[:-1]] + self.k * self.V))
            self.cache[g] = v
        return v


class RobustModel:
    """Bounded-loss wrapper (LANE R6 CM2, 25 Sept 2026): logp(g) = log((1-q) * P(g) + q / V), so no single n-gram --
    and so no single misread sign -- can cost more than about -log(q/V). Same interface as Model (order, freq, logp);
    anneal() and score() take it unchanged. Use for a stream believed to carry a share q of misread signs."""
    def __init__(self, model, q):
        self.m, self.q, self.order, self.freq, self.V = model, q, model.order, model.freq, model.V
        self.floor, self.cache = q / model.V, {}

    def logp(self, g):
        v = self.cache.get(g)
        if v is None:
            v = math.log((1 - self.q) * math.exp(self.m.logp(g)) + self.floor)
            self.cache[g] = v
        return v


class BackoffModel:
    """Interpolated absolute-discount n-gram with recursive backoff (LANE R7 CM3, 25 Sept 2026). Same interface as
    Model (order, freq, V, logp), so anneal(), anneal_noisy(), score() and RobustModel take it unchanged.
    P_k(g) = max(c(g) - D, 0) / c(ctx) + D * n1plus(ctx) / c(ctx) * P_{k-1}(g[1:]), falling to P_{k-1} when the context
    is unseen; P_1 is the add-half unigram. Why: the plain add-k Model at order 4 or 5 on a 2 MB corpus assigns most
    unseen 4-grams the same floor, so its optimum drifts; interpolation keeps the longer context where the corpus has it
    and the trigram elsewhere. CM2 (25 Sept 2026) measured that the trigram objective's optimum is no longer the true
    key at 10 percent transcription noise; a longer context per letter is the one lever that changes that, and a
    5-gram spans most Italian morphemes, which is what a word-aware model would add."""
    def __init__(self, texts, order=5, D=0.75):
        s = "".join(fold(t) for t in texts)
        self.order, self.D, self.V = order, D, len(ALPHA)
        self.n = [None] + [Counter(s[i:i + k] for i in range(len(s) - k + 1)) for k in range(1, order + 1)]
        self.ctx = [None, None] + [Counter() for _ in range(2, order + 1)]   # context counts and distinct continuations
        self.n1p = [None, None] + [Counter() for _ in range(2, order + 1)]
        for k in range(2, order + 1):
            for g, c in self.n[k].items():
                self.ctx[k][g[:-1]] += c
                self.n1p[k][g[:-1]] += 1
        self.uni = self.n[1]
        tot = sum(self.uni.values())
        self.freq = {a: (self.uni[a] + 0.5) / (tot + 0.5 * self.V) for a in ALPHA}
        self.cache = {}

    def prob(self, g):
        k = len(g)
        if k == 1:
            return self.freq.get(g, 0.5 / self.V)
        c = self.ctx[k][g[:-1]]
        lower = self.prob(g[1:])
        if c == 0:
            return lower
        return max(self.n[k][g] - self.D, 0) / c + self.D * self.n1p[k][g[:-1]] / c * lower

    def logp(self, g):
        v = self.cache.get(g)
        if v is None:
            v = math.log(self.prob(g))
            self.cache[g] = v
        return v


def score(model, plain, uni_w):
    o = model.order
    s = sum(model.logp(plain[i:i + o]) for i in range(len(plain) - o + 1))
    cnt = Counter(plain)
    n = len(plain)
    # -N * KL(observed letter distribution || corpus distribution): penalises both wrong and over-concentrated
    # letter use (a plain multinomial term rewards decoding everything as e/n)
    u = sum(c * math.log(n * model.freq[a] / c) for a, c in cnt.items())
    return s + uni_w * u


def anneal(seq, model, iters, rng, uni_w, t0=4.0, fixed=None, allowed=None):
    """Incremental annealing: a move re-scores only the n-grams touching the changed sign's positions.
    allowed: optional {sign: "letters"} restricting what a sign may decode to (e.g. vowel-indicator marks to "aeiou")."""
    o = model.order
    signs = sorted(set(seq))
    letters = list(ALPHA)
    weights = [model.freq[a] for a in letters]
    lf = {a: math.log(model.freq[a]) for a in letters}
    pos = {s: [i for i, x in enumerate(seq) if x == s] for s in signs}
    n = len(seq)
    starts = {s: sorted({j for i in pos[s] for j in range(max(0, i - o + 1), min(i, n - o) + 1)}) for s in signs}
    fixed = fixed or {}
    allowed = {s: list(v) for s, v in (allowed or {}).items()}
    key = {s: fixed.get(s) or (rng.choice(allowed[s]) if s in allowed else rng.choices(letters, weights)[0])
           for s in signs}
    signs = [s for s in signs if s not in fixed]  # crib-fixed signs never move
    pl = [key[x] for x in seq]
    lp = model.logp

    def part(js):
        return sum(lp("".join(pl[j:j + o])) for j in js)

    cnt = Counter(pl)
    xlx = lambda c: c * math.log(c) if c > 0 else 0.0
    cur = score(model, "".join(pl), uni_w)
    best, bestkey = cur, dict(key)
    for it in range(iters):
        T = t0 * (1 - it / iters) + 0.02
        s = rng.choice(signs)
        old = key[s]
        new = rng.choice(allowed.get(s, letters))
        if new == old:
            continue
        js = starts[s]
        before = part(js)
        for i in pos[s]:
            pl[i] = new
        m = len(pos[s])
        du = m * (lf[new] - lf[old]) - (xlx(cnt[new] + m) - xlx(cnt[new]) + xlx(cnt[old] - m) - xlx(cnt[old]))
        d = part(js) - before + uni_w * du
        if d >= 0 or rng.random() < math.exp(d / T):
            key[s] = new
            cnt[new] += m
            cnt[old] -= m
            cur += d
            if cur > best:
                best, bestkey = cur, dict(key)
        else:
            for i in pos[s]:
                pl[i] = old
    return score(model, "".join(bestkey[x] for x in seq), uni_w), bestkey


def anneal_noisy(seq, model, iters, rng, uni_w, noise, t0=4.0, fixed=None, allowed=None, cap_mult=1.5, pos_prob=0.3,
                 pos_start=0.5):
    """Error-tolerant anneal (LANE R6 CM2, 25 Sept 2026): the same homophonic key as anneal(), plus a per-position
    erasure variable. Generative model: at each position the plaintext letter is key[sign] with probability 1-noise,
    or, with probability noise, a letter drawn from the corpus unigram distribution (a misread sign: the type on the
    page is not the type transcribed). The solver's state is (key, free) where free = {position: letter} names the
    positions it treats as misread and the letter it puts there. Objective = n-gram score of the corrected plaintext
    + uni_w * unigram term + sum over free positions of log(noise) + log(freq[letter]) - log(1-noise). Moves: a sign
    move as in anneal() (free positions do not follow the key), or, with probability pos_prob, a position move (make
    a position free with a proposed letter, change a free letter, or revert it to the key). At most
    ceil(cap_mult * noise * N) positions may be free; position moves start at pos_start of the schedule, so the key
    forms first. Returns (score, key, free)."""
    o = model.order
    signs = sorted(set(seq))
    letters = list(ALPHA)
    weights = [model.freq[a] for a in letters]
    lf = {a: math.log(model.freq[a]) for a in letters}
    pos = {s: [i for i, x in enumerate(seq) if x == s] for s in signs}
    n = len(seq)
    starts = {s: sorted({j for i in pos[s] for j in range(max(0, i - o + 1), min(i, n - o) + 1)}) for s in signs}
    fixed = fixed or {}
    allowed = {s: list(v) for s, v in (allowed or {}).items()}
    key = {s: fixed.get(s) or (rng.choice(allowed[s]) if s in allowed else rng.choices(letters, weights)[0])
           for s in signs}
    signs = [s for s in signs if s not in fixed]
    pl = [key[x] for x in seq]
    free = {}
    cap = math.ceil(cap_mult * noise * n)
    pen = math.log(noise) - math.log(1 - noise)  # per free position, before the letter's own log freq
    lp = model.logp

    def part(js):
        return sum(lp("".join(pl[j:j + o])) for j in js)

    cnt = Counter(pl)
    xlx = lambda c: c * math.log(c) if c > 0 else 0.0
    cur = score(model, "".join(pl), uni_w)
    best, bestkey, bestfree = cur, dict(key), {}
    for it in range(iters):
        T = t0 * (1 - it / iters) + 0.02
        if it >= pos_start * iters and rng.random() < pos_prob:
            i = rng.randrange(n)
            old = pl[i]
            if i in free:
                if rng.random() < 0.5:
                    new, dprior = key[seq[i]], -(pen + lf[old])          # revert to the key
                    becomes_free = False
                else:                                                 # change the free letter
                    new = rng.choices(letters, weights)[0]
                    dprior, becomes_free = lf[new] - lf[old], True
            else:
                if len(free) >= cap:
                    continue
                new = rng.choices(letters, weights)[0]
                dprior, becomes_free = pen + lf[new], True
            if new == old and becomes_free == (i in free):
                continue
            js = range(max(0, i - o + 1), min(i, n - o) + 1)
            before = part(js)
            pl[i] = new
            du = (lf[new] - lf[old]) - (xlx(cnt[new] + 1) - xlx(cnt[new]) + xlx(cnt[old] - 1) - xlx(cnt[old])) if new != old else 0.0
            d = part(js) - before + uni_w * du + dprior
            if d >= 0 or rng.random() < math.exp(d / T):
                if new != old:
                    cnt[new] += 1; cnt[old] -= 1
                if becomes_free:
                    free[i] = new
                else:
                    free.pop(i, None)
                cur += d
                if cur > best:
                    best, bestkey, bestfree = cur, dict(key), dict(free)
            else:
                pl[i] = old
            continue
        s = rng.choice(signs)
        old = key[s]
        new = rng.choice(allowed.get(s, letters))
        if new == old:
            continue
        js = starts[s]
        before = part(js)
        moved = [i for i in pos[s] if i not in free]
        for i in moved:
            pl[i] = new
        m = len(moved)
        du = m * (lf[new] - lf[old]) - (xlx(cnt[new] + m) - xlx(cnt[new]) + xlx(cnt[old] - m) - xlx(cnt[old]))
        d = part(js) - before + uni_w * du
        if d >= 0 or rng.random() < math.exp(d / T):
            key[s] = new
            cnt[new] += m
            cnt[old] -= m
            cur += d
            if cur > best:
                best, bestkey, bestfree = cur, dict(key), dict(free)
        else:
            for i in moved:
                pl[i] = old
    corrected = [bestfree.get(i, bestkey[x]) for i, x in enumerate(seq)]
    total = score(model, "".join(corrected), uni_w) + sum(pen + lf[a] for a in bestfree.values())
    return total, bestkey, bestfree


def solve(seq, model, restarts, iters, seed, uni_w, fixed=None, allowed=None, noise=0.0):
    """noise > 0 (error-tolerant, anneal_noisy): results are (score, key, free) triples instead of (score, key)."""
    rng = random.Random(seed)
    results = []
    for r in range(restarts):
        if noise:
            results.append(anneal_noisy(seq, model, iters, rng, uni_w, noise, fixed=fixed, allowed=allowed))
        else:
            results.append(anneal(seq, model, iters, rng, uni_w, fixed=fixed, allowed=allowed))
    results.sort(key=lambda x: -x[0])
    return results


def make_control(plain_text, K, N, model, seed):
    rng = random.Random(seed + 1000)
    p = fold(plain_text)[:N]
    cnt = Counter(p)
    letters = [a for a, _ in cnt.most_common()]
    # allot K signs: at least one per letter present, the rest by frequency (largest remainder)
    alloc = {a: 1 for a in letters}
    extra = K - len(letters)
    while extra > 0:
        a = max(letters, key=lambda a: cnt[a] / alloc[a])
        alloc[a] += 1
        extra -= 1
    homs, i = {}, 0
    for a in letters:
        homs[a] = [f"s{i + j}" for j in range(alloc[a])]
        i += alloc[a]
    seq = [rng.choice(homs[a]) for a in p]
    truth = {s: a for a, ss in homs.items() for s in ss}
    return seq, p, truth


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("cipher", nargs="?")
    ap.add_argument("--corpus", action="append", required=True)
    ap.add_argument("--order", type=int, default=3)
    ap.add_argument("--restarts", type=int, default=8)
    ap.add_argument("--iters", type=int, default=40000)
    ap.add_argument("--skip", default="DOT,COL")
    ap.add_argument("--seed", type=int, default=1)
    ap.add_argument("--uni-weight", type=float, default=1.0)
    ap.add_argument("--out")
    ap.add_argument("--w-as-uu", action="store_true", help="fold w to uu in corpus and control (ciphers writing w as a doubled u sign)")
    ap.add_argument("--control")
    ap.add_argument("--signs", type=int)
    ap.add_argument("--length", type=int)
    ap.add_argument("--noise", type=float, default=0.0,
                    help="error-tolerant solve (anneal_noisy): share of positions assumed misread; the result names "
                         "the positions the solver corrected (free) and the corrected decode")
    ap.add_argument("--robust", type=float, default=0.0,
                    help="bounded-loss scoring (RobustModel): mixture weight q of a uniform n-gram floor")
    ap.add_argument("--backoff", action="store_true",
                    help="BackoffModel: interpolated absolute-discount n-gram of --order with recursive backoff "
                         "(use with --order 4 or 5); default stays the add-k Model")
    ap.add_argument("--fix", help="crib: sign=letter pairs held fixed, e.g. 70=q,33=u,67=e (target mode)")
    ap.add_argument("--fix-first", type=int, default=0,
                    help="control mode: hold the signs of the first N positions at their true letters (the matched "
                         "control for a target crib of N letters)")
    a = ap.parse_args()
    global W_AS_UU
    W_AS_UU = a.w_as_uu
    texts = [open(f, encoding="utf-8").read() for f in a.corpus]
    model = BackoffModel(texts, a.order) if a.backoff else Model(texts, a.order)
    if a.robust:
        model = RobustModel(model, a.robust)
    if a.control:
        seq, p, truth = make_control(open(a.control, encoding="utf-8").read(), a.signs, a.length, model, a.seed)
        fixed = {seq[i]: truth[seq[i]] for i in range(a.fix_first)}
        res = solve(seq, model, a.restarts, a.iters, a.seed, a.uni_weight, fixed, noise=a.noise)
        sc, key = res[0][:2]
        free = res[0][2] if a.noise else {}
        dec = "".join(free.get(i, key[x]) for i, x in enumerate(seq))
        ok = sum(1 for x, y in zip(dec, p) if x == y)
        out = {"mode": "control", "N": len(seq), "K": len(set(seq)), "letters_correct": ok,
               "share": round(ok / len(p), 3), "score": sc, "plain": p, "decoded": dec,
               "restart_scores": [round(r[0], 1) for r in res], **({"noise": a.noise, "free": len(free)} if a.noise else {})}
        print(f"control N={len(seq)} K={len(set(seq))}: {ok}/{len(p)} letters = {ok/len(p):.1%}")
        print(dec[:200])
    else:
        rows = [l.rstrip("\n").split("\t") for l in open(a.cipher, encoding="utf-8") if l.strip() and not l.startswith("#")]
        h = rows[0]
        si = h.index("sign")
        skip = set(a.skip.split(","))
        seq = [r[si].rstrip("?") for r in rows[1:] if r[si].rstrip("?") not in skip]
        fixed = dict(kv.split("=") for kv in a.fix.split(",")) if a.fix else {}
        res = solve(seq, model, a.restarts, a.iters, a.seed, a.uni_weight, fixed, noise=a.noise)
        sc, key = res[0][:2]
        free = res[0][2] if a.noise else {}
        dec = "".join(free.get(i, key[x]) for i, x in enumerate(seq))
        out = {"mode": "target", "N": len(seq), "K": len(set(seq)), "score": sc, "key": key, "decoded": dec,
               "restart_scores": [round(r[0], 1) for r in res],
               "restart_decodes": ["".join(r[1][x] for x in seq)[:120] for r in res[:4]],
               **({"noise": a.noise, "free": {str(i): l for i, l in sorted(free.items())}} if a.noise else {})}
        print(f"target N={len(seq)} K={len(set(seq))} best score {sc:.1f}; restarts {out['restart_scores']}")
        print(dec)
    if a.out:
        json.dump(out, open(a.out, "w"), ensure_ascii=False, indent=1)


if __name__ == "__main__":
    main()
