#!/usr/bin/env python3
"""Ciphertext-only simulated-annealing solver for short fragmentary English substitution ciphers
(many-to-one, at most --max-homo symbols per letter (default 2), so homophones are allowed), scored by an
interpolated letter 4-gram model. Written 23 Sept 2026 for ciphers/bowes-walsingham-1583; own code, nothing
copied from either solver repository (design is the usual hill-climb/anneal described in LESSONS.md).

Alphabet: 24 letters, 16th-century style (i=j, u=v): abcdefghiklmnopqrstuwxyz.

  python3 tools/subst_hillclimb.py solve CIPHER --corpus A.txt [B.txt ...] [--restarts R] [--iters N]
        [--seed S] [--shuffle SEED] [--fix SYM=letter ...] [--out result.json]
  CIPHER: one fragment per line, tokens separated by ';' (empty tokens ignored), '#' comments.
  --shuffle permutes the tokens across the fragments (same lengths, same symbol counts): the baseline.
  Output: best key, reading, score per token (mean log10 prob), and every restart's score.

Used as a library by the target's control.py (load_cipher, Model, anneal).
"""
import argparse, json, math, random, re, sys
from collections import Counter
import numpy as np

ALPHA = "abcdefghiklmnopqrstuwxyz"
IDX = {c: i for i, c in enumerate(ALPHA)}
A = len(ALPHA)


def norm(text):
    t = text.lower().replace("j", "i").replace("v", "u")
    return "".join(c for c in t if c in IDX)


def load_cipher(path):
    frags = []
    for line in open(path, encoding="utf-8"):
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        toks = [t.strip() for t in line.split(";") if t.strip()]
        if toks:
            frags.append(toks)
    return frags


class Model:
    """Interpolated log10 tables: uni[A], bi[A,A], tri[A,A,A], quad[A,A,A,A] (conditional)."""

    def __init__(self, texts):
        s = "".join(norm(t) for t in texts)
        a = np.array([IDX[c] for c in s], dtype=np.int64)
        c1 = np.bincount(a, minlength=A).astype(float) + 0.5
        c2 = np.bincount(a[:-1] * A + a[1:], minlength=A**2).reshape(A, A).astype(float)
        c3 = np.bincount((a[:-2] * A + a[1:-1]) * A + a[2:], minlength=A**3).reshape(A, A, A).astype(float)
        c4 = np.bincount(((a[:-3] * A + a[1:-2]) * A + a[2:-1]) * A + a[3:], minlength=A**4).reshape(A, A, A, A).astype(float)
        p1 = c1 / c1.sum()
        def cond(c, lower, lam):
            tot = c.sum(axis=-1, keepdims=True)
            ml = np.where(tot > 0, c / np.maximum(tot, 1), 0)
            w = tot / (tot + lam)
            return w * ml + (1 - w) * lower
        p2 = cond(c2, p1[None, :], 5.0)
        p3 = cond(c3, p2[None, :, :], 5.0)
        p4 = cond(c4, p3[None, :, :, :], 5.0)
        self.uni, self.bi, self.tri, self.quad = (np.log10(x) for x in (p1, p2, p3, p4))
        self.nchars = len(s)

    def score_frags(self, frags_idx):
        """frags_idx: list of int arrays of letter indices. Returns total log10 prob."""
        tot = 0.0
        for f in frags_idx:
            n = len(f)
            if n == 0:
                continue
            tot += self.uni[f[0]]
            if n > 1:
                tot += self.bi[f[0], f[1]]
            if n > 2:
                tot += self.tri[f[0], f[1], f[2]]
            if n > 3:
                tot += self.quad[f[:-3], f[1:-2], f[2:-1], f[3:]].sum()
        return tot


def anneal(frags, model, restarts=40, iters=6000, seed=1, fixed=None, t0=1.0, t1=0.02, max_homo=2):
    """frags: list of lists of symbol labels. Returns dict with best key and per-restart scores."""
    rng = random.Random(seed)
    syms = sorted({t for f in frags for t in f})
    sidx = {s: i for i, s in enumerate(syms)}
    fr = [np.array([sidx[t] for t in f], dtype=np.int64) for f in frags]
    ntok = sum(len(f) for f in fr)
    fixed = fixed or {}
    free = [i for i, s in enumerate(syms) if s not in fixed]
    freq = np.exp(model.uni * math.log(10))
    letters = list(range(A))
    def score(key):
        return model.score_frags([key[f] for f in fr])
    best_all, results = None, []
    for r in range(restarts):
        key = np.full(len(syms), -1, dtype=np.int64)
        for s, v in fixed.items():
            if s in sidx:
                key[sidx[s]] = IDX[v]
        for i in free:
            while True:
                v = rng.choices(letters, weights=freq)[0]
                if (key == v).sum() < max_homo:
                    key[i] = v; break
        cur = score(key)
        best, bkey = cur, key.copy()
        for it in range(iters):
            T = t0 * (t1 / t0) ** (it / iters)
            k2 = key.copy()
            if rng.random() < 0.7 or len(free) < 2:
                i = rng.choice(free)
                v = rng.randrange(A)
                if (key == v).sum() >= max_homo:
                    continue
                k2[i] = v
            else:
                i, j = rng.sample(free, 2)
                k2[i], k2[j] = key[j], key[i]
            s2 = score(k2)
            if s2 >= cur or rng.random() < math.exp((s2 - cur) / T):
                key, cur = k2, s2
                if cur > best:
                    best, bkey = cur, key.copy()
        # greedy polish
        improved = True
        while improved:
            improved = False
            for i in free:
                for v in range(A):
                    if v == bkey[i] or (bkey == v).sum() >= max_homo:
                        continue
                    k2 = bkey.copy(); k2[i] = v
                    s2 = score(k2)
                    if s2 > best + 1e-9:
                        best, bkey, improved = s2, k2, True
        results.append(best / ntok)
        if best_all is None or best > best_all[0]:
            best_all = (best, bkey.copy(), r)
    best, bkey, r = best_all
    keymap = {s: ALPHA[bkey[sidx[s]]] for s in syms}
    reading = ["".join(keymap[t] for t in f) for f in frags]
    return {"score_per_token": best / ntok, "best_restart": r, "restart_scores": results,
            "key": keymap, "reading": reading, "ntok": ntok}


def shuffle_frags(frags, seed):
    rng = random.Random(seed)
    toks = [t for f in frags for t in f]
    rng.shuffle(toks)
    out, k = [], 0
    for f in frags:
        out.append(toks[k:k + len(f)]); k += len(f)
    return out


def main():
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="cmd", required=True)
    s = sub.add_parser("solve")
    s.add_argument("cipher"); s.add_argument("--corpus", nargs="+", required=True)
    s.add_argument("--restarts", type=int, default=40); s.add_argument("--iters", type=int, default=6000)
    s.add_argument("--seed", type=int, default=1); s.add_argument("--shuffle", type=int)
    s.add_argument("--fix", nargs="*", default=[]); s.add_argument("--out")
    s.add_argument("--max-homo", type=int, default=2)
    a = ap.parse_args()
    frags = load_cipher(a.cipher)
    if a.shuffle is not None:
        frags = shuffle_frags(frags, a.shuffle)
    model = Model([open(p, encoding="utf-8", errors="replace").read() for p in a.corpus])
    fixed = dict(x.split("=") for x in a.fix)
    res = anneal(frags, model, a.restarts, a.iters, a.seed, fixed, max_homo=a.max_homo)
    print(json.dumps({k: v for k, v in res.items() if k != "restart_scores"}, indent=1))
    if a.out:
        json.dump(res, open(a.out, "w"), indent=1)


if __name__ == "__main__":
    main()
