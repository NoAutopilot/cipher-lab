#!/usr/bin/env python3
"""English plausibility scorers for hidden-message (acrostic, null-cipher) searches.

Written 23 Sept 2026 (ciphers/burgess-mysteries-1912). Own code; nothing copied from the solver repositories.

Model = counts from one or more plain-text corpora (default: tools/data/pg1661_holmes.txt, Doyle, The Adventures
of Sherlock Holmes, Project Gutenberg #1661, and tools/data/pg2701_mobydick.txt, Melville, Moby Dick, #2701; both
public domain, fetched once from gutenberg.org on 23 Sept 2026, independent of any target). Pass extra corpora with
EnglishModel(paths=[...]) or texts=[...].

  m = EnglishModel()
  m.quad(s)            mean log10 P(letter | 3 previous) over s (A-Z only), interpolated with lower orders
  m.best_window(s, w)  (score, start) of the best window of length w by quad()
  m.cover(s)           (longest run of letters covered by corpus words seen twice: >= 3 letters, A, I, 25 common 2-letter words)
  m.words_pmi(ws)      mean over consecutive pairs of log10 P(w2 | w1) - log10 P(w2) (add-k smoothed): how much
                       more the words follow one another than chance order; 0 for a random order
  m.best_word_window(ws, w)  best window of w words by words_pmi
  m.lift_scores(ws)    per consecutive pair: log10 P(w2 | w1) (Dirichlet prior 10 towards P(w2)) minus log10 of w2's
                       frequency in the sequence itself (add-one over the corpus vocabulary). Words that open most
                       units anyway ("oh", "yes", "he") earn nothing for following one another; a planted sentence
                       of rarer words that do follow one another scores high.
  m.lift_windows(ws, w, k)   top k non-overlapping windows of w words by mean lift: [(score, start), ...]
  shuffle_z(stat, units, n)   z-score of stat(units) against n random permutations of the same units

python3 tools/english_score.py "SOME TEXT" prints the scores.
"""
import math
import random
import re
import sys
from collections import Counter
from functools import lru_cache
from pathlib import Path

DATA = Path(__file__).resolve().parent / "data"
DEFAULT_CORPORA = [DATA / "pg1661_holmes.txt", DATA / "pg2701_mobydick.txt"]


def _read(p):
    t = Path(p).read_text(encoding="utf-8", errors="replace")
    a, b = t.find("*** START OF"), t.find("*** END OF")
    if a >= 0 and b > a:
        t = t[t.find("\n", a) + 1:b]
    return t


def az(s):
    if not isinstance(s, str):
        s = "".join(s)
    return re.sub(r"[^A-Z]", "", s.upper())


class EnglishModel:
    def __init__(self, paths=None, texts=(), min_word=2):
        texts = [_read(p) for p in (paths or DEFAULT_CORPORA)] + list(texts)
        self.c = [Counter() for _ in range(5)]  # c[n] counts of n-grams, n = 1..4
        wc, bc = Counter(), Counter()
        for t in texts:
            words = [w for w in re.findall(r"[A-Za-z]+(?:'[A-Za-z]+)?", t)]
            L = az(t)
            for n in range(1, 5):
                self.c[n].update(L[i:i + n] for i in range(len(L) - n + 1))
            lw = [w.lower() for w in words]
            wc.update(lw)
            bc.update(zip(lw, lw[1:]))
        self.N = sum(self.c[1].values())
        self.wc, self.bc = wc, bc
        self.W = sum(wc.values())
        self.V = len(wc)
        two = {"is", "it", "in", "to", "of", "on", "at", "be", "by", "he", "we", "me", "my", "no", "so", "up", "us",
               "an", "as", "am", "do", "go", "if", "or", "oh"}
        self.dict = {w.upper().replace("'", "") for w, n in wc.items()
                     if n >= min_word and (len(w) >= 3 or w in ("a", "i") or w in two)}
        self.maxw = max(len(w) for w in self.dict)
        self._lp = {}

    # ---- letters
    def lp(self, ctx, ch):
        """log10 P(ch | ctx), ctx up to 3 letters; recursive interpolation, weight n/(n+3) on a context seen n times."""
        key = (ctx, ch)
        v = self._lp.get(key)
        if v is None:
            uni = (self.c[1][ch] + 1) / (self.N + 26)
            p = uni
            for k in (1, 2, 3):  # recursive interpolation: p_k = l*ML_k + (1-l)*p_{k-1}
                if len(ctx) >= k:
                    h = ctx[-k:]
                    den = self.c[k][h]
                    if den:
                        lam = den / (den + 3.0)  # Witten-Bell-like confidence in the longer context
                        p = lam * self.c[k + 1][h + ch] / den + (1 - lam) * p
            v = self._lp[key] = math.log10(p)
        return v

    def quad(self, s):
        s = az(s)
        if not s:
            return -9.0
        return sum(self.lp(s[max(0, i - 3):i], s[i]) for i in range(len(s))) / len(s)

    def best_window(self, s, w):
        s = az(s)
        if len(s) <= w:
            return self.quad(s), 0
        # incremental: per-position log-probs with a 3-letter context inside the window approximated by the
        # full context (the window's first 3 letters differ only slightly); exact recomputation for the best one
        v = [self.lp(s[max(0, i - 3):i], s[i]) for i in range(len(s))]
        cur = sum(v[:w])
        best, bi = cur, 0
        for i in range(1, len(s) - w + 1):
            cur += v[i + w - 1] - v[i - 1]
            if cur > best:
                best, bi = cur, i
        return self.quad(s[bi:bi + w]), bi

    def cover(self, s):
        """Longest stretch of s that splits wholly into dictionary words (see self.dict)."""
        s = az(s)
        n = len(s)
        # ok[j] = start of the longest covered run ending at j (exclusive), or None
        best_start = [None] * (n + 1)
        best, bpos = 0, 0
        for j in range(1, n + 1):
            st = None
            for L in range(1, min(self.maxw, j) + 1):
                i = j - L
                if s[i:j] in self.dict:
                    cand = best_start[i] if best_start[i] is not None else i
                    if st is None or cand < st:
                        st = cand
            best_start[j] = st
            if st is not None and j - st > best:
                best, bpos = j - st, st
        return best, bpos

    # ---- words
    def lpw(self, w):
        return math.log10((self.wc[w] + 0.5) / (self.W + 0.5 * (self.V + 1)))

    def lpw2(self, w1, w2, k=0.1):
        return math.log10((self.bc[(w1, w2)] + k * (self.wc[w2] + 0.5) / self.W * self.V) /
                          (self.wc[w1] + k * self.V))

    def words_pmi(self, ws):
        ws = [re.sub(r"[^a-z']", "", w.lower()) for w in ws]
        ws = [w for w in ws if w]
        if len(ws) < 2:
            return 0.0
        return sum(self.lpw2(a, b) - self.lpw(b) for a, b in zip(ws, ws[1:])) / (len(ws) - 1)

    def best_word_window(self, ws, w):
        ws = [re.sub(r"[^a-z']", "", x.lower()) for x in ws]
        ws = [x for x in ws if x]
        if len(ws) <= w:
            return self.words_pmi(ws), 0
        v = [self.lpw2(a, b) - self.lpw(b) for a, b in zip(ws, ws[1:])]
        cur = sum(v[:w - 1])
        best, bi = cur, 0
        for i in range(1, len(v) - (w - 1) + 1):
            cur += v[i + w - 2] - v[i - 1]
            if cur > best:
                best, bi = cur, i
        return best / (w - 1), bi

    def lift_scores(self, ws, beta=10.0):
        ws = [re.sub(r"[^a-z']", "", w.lower()) for w in ws]
        ws = [w for w in ws if w]
        fc = Counter(ws)
        n = len(ws)
        p1 = lambda w: (self.wc[w] + 0.5) / (self.W + 0.5 * self.V)
        v = [math.log10((self.bc[(a, b)] + beta * p1(b)) / (self.wc[a] + beta)) -
             math.log10((fc[b] + 1) / (n + self.V)) for a, b in zip(ws, ws[1:])]
        return ws, v

    def lift_windows(self, ws, w, k=1):
        ws, v = self.lift_scores(ws)
        if len(v) < w - 1:
            return [(sum(v) / max(1, len(v)), 0)], ws
        cs = [0.0]
        for x in v:
            cs.append(cs[-1] + x)
        cand = sorted(((cs[i + w - 1] - cs[i]) / (w - 1), i) for i in range(len(v) - w + 2))[::-1]
        out, taken = [], []
        for sc, i in cand:
            if all(abs(i - j) >= w for j in taken):
                out.append((sc, i))
                taken.append(i)
                if len(out) >= k:
                    break
        return out, ws


def shuffle_z(stat, units, n=200, seed=1):
    rnd = random.Random(seed)
    obs = stat(units)
    xs = []
    u = list(units)
    for _ in range(n):
        rnd.shuffle(u)
        xs.append(stat(u))
    mu = sum(xs) / n
    sd = (sum((x - mu) ** 2 for x in xs) / (n - 1)) ** 0.5 or 1e-9
    return obs, (obs - mu) / sd, mu, sd, xs


@lru_cache(maxsize=None)
def default_model():
    return EnglishModel()


if __name__ == "__main__":
    m = default_model()
    for s in sys.argv[1:]:
        print(f"{s!r}: quad {m.quad(s):.3f}  cover {m.cover(s)}  words_pmi {m.words_pmi(s.split()):.3f}")
