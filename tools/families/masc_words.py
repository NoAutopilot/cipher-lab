"""masc_words: simple substitution with a dictionary (word-segmentation) term in the objective -- a word-constrained
instrument for short texts where an n-gram anneal alone plateaus (R12D-FAIR, 6 Oct 2026, fair-game-2010 at N=67).

Stage 1 is the masc family's own n-gram anneal (homophonic_anneal.solve, one sign per letter). Stage 2 polishes every
restart's key by hill-climbing (swap two letters' assignments, or move a sign to an unused letter) on
    ha.score(plain) + lam * seg(plain),
where seg is the best segmentation of the unspaced decode into corpus words (DP; each word scores log p(word) from the
corpus word counts, an out-of-dictionary letter costs `oov`). The restart with the best combined score is returned.
Control design: identical to masc (a window with exactly the target's K distinct letters, one sign per letter), so a
gain over masc at the same N, K, seeds and restarts is a gain of the word term, not of the design.
params: iters (40000), order (3), uni_weight (1.0), lam (1.0), polish (4000), oov (-12.0), minc (3: min word count),
maxw (14: longest word considered)."""
import math, random, re
from collections import Counter
import homophonic_anneal as ha
from families import masc as _masc

DESCRIPTION = "simple substitution, n-gram anneal + dictionary-segmentation polish (word-constrained)"
make_control = _masc.make_control
score_recovery = _masc.score_recovery
_LEX = {}


def _p(params, k, d):
    return type(d)(params.get(k, d))


def lexicon(corpora, minc=3, maxw=14):
    key = (id(corpora[0]) if corpora else 0, len(corpora), minc, maxw)
    if key not in _LEX:
        words = Counter(w for t in corpora for w in re.findall(r"[a-z]+", t.lower()))
        keep = {w: c for w, c in words.items() if len(w) <= maxw and (c >= minc) and (len(w) > 1 or w in ("a", "i"))}
        tot = sum(keep.values()) or 1
        _LEX[key] = {w: math.log(c / tot) for w, c in keep.items()}
    return _LEX[key]


def seg(plain, lex, oov=-12.0, maxw=14):
    n = len(plain)
    best = [0.0] + [-1e18] * n
    for i in range(1, n + 1):
        b = best[i - 1] + oov
        for j in range(max(0, i - maxw), i):
            w = plain[j:i]
            lp = lex.get(w)
            if lp is not None and best[j] + lp > b:
                b = best[j] + lp
        best[i] = b
    return best[n]


def segment(plain, lex, oov=-12.0, maxw=14):
    """The words of the best segmentation (for reporting); OOV letters are returned upper-case."""
    n = len(plain)
    best, back = [0.0] + [-1e18] * n, [0] * (n + 1)
    for i in range(1, n + 1):
        best[i], back[i] = best[i - 1] + oov, i - 1
        for j in range(max(0, i - maxw), i):
            lp = lex.get(plain[j:i])
            if lp is not None and best[j] + lp > best[i]:
                best[i], back[i] = best[j] + lp, j
    out, i = [], n
    while i > 0:
        j = back[i]
        w = plain[j:i]
        out.append(w if w in lex else w.upper())
        i = j
    return out[::-1]


def _polish(seq, key, model, lex, params, rng):
    signs = sorted(set(seq))
    alpha = sorted(model.freq)
    lam, uni, oov, maxw = _p(params, "lam", 1.0), _p(params, "uni_weight", 1.0), _p(params, "oov", -12.0), _p(params, "maxw", 14)
    def tot(k):
        pl = "".join(k[s] for s in seq)
        return ha.score(model, pl, uni) + lam * seg(pl, lex, oov, maxw)
    k = dict(key)
    cur = tot(k)
    for _ in range(_p(params, "polish", 4000)):
        k2 = dict(k)
        if rng.random() < 0.5:
            a, b = rng.sample(signs, 2)
            k2[a], k2[b] = k2[b], k2[a]
        else:
            a = rng.choice(signs)
            used = set(k2.values())
            free = [x for x in alpha if x not in used]
            if not free:
                continue
            k2[a] = rng.choice(free)
        s2 = tot(k2)
        if s2 >= cur:
            k, cur = k2, s2
    return cur, k


def solve(cipher_msgs, spec, seed, restarts, corpora, params):
    model = ha.Model(corpora, _p(params, "order", 3))
    lex = lexicon(corpora, _p(params, "minc", 3), _p(params, "maxw", 14))
    seq = [s for m in cipher_msgs for s in m]
    res = ha.solve(seq, model, restarts, _p(params, "iters", 40000), seed, _p(params, "uni_weight", 1.0))
    rng = random.Random(seed + 77)
    pol = sorted((_polish(seq, key, model, lex, params, rng) for _, key in res), key=lambda x: -x[0])
    sc, key = pol[0]
    plain = "".join(key[x] for x in seq)
    return plain, sc, {"restart_scores": [round(p[0], 1) for p in pol], "key": key,
                       "segmentation": " ".join(segment(plain, lex, _p(params, "oov", -12.0), _p(params, "maxw", 14)))}
