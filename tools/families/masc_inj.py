"""masc_inj: strictly injective simple substitution by a word-pattern beam search (branch-and-bound over dictionary
words), not an anneal (R12D-FAIR2, 6 Oct 2026, fair-game-2010 at N=67).

The decode is built left to right over the unspaced ciphertext. A state is (position, partial key, score). From a state,
each dictionary word whose letter pattern (isomorph) equals the pattern of the next L cipher letters, and which agrees
with the partial key, extends it -- strictly one-to-one: a cipher letter takes one plain letter and no plain letter is
taken by two cipher letters. A single cipher letter may also be skipped as out-of-dictionary (cost `oov`, no key
assignment), so names do not block the search. The first word may be the tail of a dictionary word and the last word
its head (a cut window starts and ends mid-word), each at a penalty `edge`. States are kept position-synchronously:
the best `beam` states reaching each position (one per distinct key there). Cipher letters left unassigned at the end
are filled one by one, injectively, with the plain letter that maximizes the n-gram score.
Score = sum of word log-probs (corpus counts) + `lam_ng` x the full decode's n-gram score at the end (re-ranking only).
Control design: identical to masc / masc_words (a window with exactly the target's K distinct letters, one sign per
letter; the training text keeps word boundaries, window +- 2000 letters removed), so a control result is directly
comparable with both. `restarts` is unused (the search is deterministic); it is accepted for the family_run interface.
params: beam (400), vocab (12000: most frequent corpus words), oov (-11.0), edge (-3.0), maxw (14), order (3),
uni_weight (1.0), lam_ng (0.3), final (40: end states re-ranked with the n-gram term)."""
import math
from collections import Counter, defaultdict
import homophonic_anneal as ha
from families import masc as _masc
from families import masc_words as _mw

DESCRIPTION = "strictly injective simple substitution, word-pattern beam search (branch-and-bound), not an anneal"
score_recovery = _masc.score_recovery
make_control = _mw.make_control


def _p(params, k, d):
    return type(d)(params.get(k, d))


def pattern(s):
    m, out = {}, []
    for ch in s:
        if ch not in m:
            m[ch] = len(m)
        out.append(m[ch])
    return tuple(out)


def build_lexicon(corpora, vocab, maxw):
    cnt = Counter(f for t in corpora for f in (ha.fold(w) for w in t.split()) if f)
    items = [(w, c) for w, c in cnt.most_common() if len(w) <= maxw and (len(w) > 1 or w in ("a", "i"))][:vocab]
    tot = sum(c for _, c in items) or 1
    full = defaultdict(list)   # pattern -> [(word, logp)]
    head = defaultdict(dict)   # pattern of a prefix -> {prefix: logp} (best word it starts)
    tail = defaultdict(dict)   # pattern of a suffix -> {suffix: logp}
    for w, c in items:
        lp = math.log(c / tot)
        full[pattern(w)].append((w, lp))
        for i in range(1, len(w)):
            pre, suf = w[:i], w[i:]
            if lp > head[pattern(pre)].get(pre, -1e9):
                head[pattern(pre)][pre] = lp
            if lp > tail[pattern(suf)].get(suf, -1e9):
                tail[pattern(suf)][suf] = lp
    return full, {k: list(v.items()) for k, v in head.items()}, {k: list(v.items()) for k, v in tail.items()}


def _extend(key, used, csub, word):
    """Return (key2, used2) if word agrees injectively with key on csub, else None."""
    k2, u2 = None, used
    for c, p in zip(csub, word):
        cur = key[c] if k2 is None else k2[c]
        if cur is None:
            bit = 1 << (ord(p) - 97)
            if u2 & bit:
                return None
            if k2 is None:
                k2 = list(key)
            k2[c] = p
            u2 |= bit
        elif cur != p:
            return None
    return (tuple(k2) if k2 is not None else key), u2


def solve(cipher_msgs, spec, seed, restarts, corpora, params):
    beam, vocab, maxw = _p(params, "beam", 400), _p(params, "vocab", 12000), _p(params, "maxw", 14)
    oov, edge = _p(params, "oov", -11.0), _p(params, "edge", -3.0)
    seq = [s for m in cipher_msgs for s in m]
    signs = sorted(set(seq))
    idx = {s: i for i, s in enumerate(signs)}
    cs = [idx[s] for s in seq]
    n = len(cs)
    full, head, tail = build_lexicon(corpora, vocab, maxw)
    # candidate words per (start, length), by isomorph
    cand = {}
    for i in range(n):
        for L in range(1, min(maxw, n - i) + 1):
            pt = pattern(cs[i:i + L])
            lst = list(full.get(pt, []))
            if i == 0:
                lst += [(w, lp + edge) for w, lp in tail.get(pt, [])]
            if i + L == n:
                lst += [(w, lp + edge) for w, lp in head.get(pt, [])]
            if lst:
                cand[(i, L)] = lst
    empty = tuple([None] * len(signs))
    states = [dict() for _ in range(n + 1)]   # pos -> {key: (score, used)}
    states[0][empty] = (0.0, 0)

    def push(pos, key, sc, used):
        d = states[pos]
        old = d.get(key)
        if old is None or sc > old[0]:
            d[key] = (sc, used)

    for i in range(n):
        if not states[i]:
            continue
        cur = sorted(states[i].items(), key=lambda kv: -kv[1][0])[:beam]
        states[i] = None
        for key, (sc, used) in cur:
            push(i + 1, key, sc + oov, used)
            for L in range(1, min(maxw, n - i) + 1):
                lst = cand.get((i, L))
                if not lst:
                    continue
                csub = cs[i:i + L]
                for w, lp in lst:
                    r = _extend(key, used, csub, w)
                    if r is not None:
                        push(i + L, r[0], sc + lp, r[1])
        # prune the near future lazily: done when each position is expanded
    ends = sorted(states[n].items(), key=lambda kv: -kv[1][0])[:_p(params, "final", 40)]
    model = ha.Model(corpora, _p(params, "order", 3))
    uni, lam_ng = _p(params, "uni_weight", 1.0), _p(params, "lam_ng", 0.3)
    alpha = sorted(model.freq)
    best = None
    for key, (wsc, used) in ends:
        k = list(key)
        for j in sorted(range(len(signs)), key=lambda j: -cs.count(j)):
            if k[j] is not None:
                continue
            free = [a for a in alpha if a not in k]
            bestp, bestv = None, -1e18
            for a in free:
                k[j] = a
                pl = "".join(k[x] if k[x] is not None else "?" for x in cs)
                v = ha.score(model, pl.replace("?", ""), uni)
                if v > bestv:
                    bestp, bestv = a, v
            k[j] = bestp
        pl = "".join(k[x] for x in cs)
        tot = wsc + lam_ng * ha.score(model, pl, uni)
        if best is None or tot > best[0]:
            best = (tot, pl, wsc, {signs[j]: k[j] for j in range(len(signs))})
    if best is None:
        return "?" * n, -1e18, {"note": "no end state"}
    tot, pl, wsc, key = best
    return pl, tot, {"word_score": round(wsc, 2), "key": key, "end_states": len(ends)}
