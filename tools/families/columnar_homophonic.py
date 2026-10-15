"""columnar_homophonic: an irregular columnar transposition of a homophonic (or simple) substitution (R15-KAL14, 6 Oct 2026).

Design: plaintext letters -> signs by a homophonic key (one or more signs per letter), then the sign stream is written
in rows of width w and read off column by column in a keyed column order (irregular: the last row may be short).
Built for kaliningrad-2015, where unigram tests (A2-KAL2) cannot see a transposition of a substitution, since a
substitution changes every letter's identity and a transposition keeps every sign's count.

Control design: the `homophonic` family's own control (same N, K, corpus; profile=target matches the target's own
sign-count profile), then a columnar transposition at a width fixed per seed (param ctrl_widths, a comma list indexed
by seed-1, default 7,10,5,12,9) and a random column order (seeded); the solver is not told the width.
Solver: for every width in `widths` (default 2-12) it runs `restarts` joint anneals over (column order, sign->letter
key) scored by a smoothed trigram log-likelihood of the untransposed decode (numpy, model trained on the corpora given,
which for the control exclude its own window); moves: reassign one sign or swap two signs' letters (p 1-order_p together), swap two columns (0.6 order_p), move one
column (0.4 order_p; order_p default 0.25); linear temperature t0 -> 0 over `iters`. The best score over all widths wins; info keeps the per-width
bests. Recovery = share of plaintext positions read correctly (the control's untransposed truth), best over a shift of
-12..12 (a column-order rotation displaces the text; see score_recovery).
params: widths (e.g. 2-12 or 5,7), iters (default 30000), t0 (1.0), uni_weight (1.0, the -N*KL letter term), ctrl_widths, plus the homophonic family's
control params (profile, noise, alphabet). Width 1 is the no-transposition baseline if listed.

stage=two (KAL-2ST, 15 Oct 2026; the instrument named after KAL-BIG retired the joint anneal for kaliningrad-2015 under rule 3):
the transposition and the substitution are solved apart. Stage 1, per width, needs no language model: a hill climb over column
orders (swap / move one column; s1_restarts default 100, s1_iters default 4000) maximising the sign-adjacency statistic of the
untransposed stream, sum over sign bigrams of n*(n-1) -- in the right order every column end joins the next column's head in
its own row, so plaintext bigrams recur; in a wrong order the joins are random pairs. The s1_keep (default 2) best distinct
orders per width go on. Stage 2: the homophonic anneal (this module's _anneal at width 1, i.e. the order held fixed) on each
kept untransposed stream, s2_restarts (default: restarts) x s2_iters (default: iters). The per-width score is the best stage-2
score; the best width wins. Stage 1's statistic and choice are in info (stage1)."""
import math
import random
from collections import Counter

import numpy as np

import homophonic_anneal as ha
from families import homophonic as hom

DESCRIPTION = ("columnar transposition (widths 2-12, keyed order) of a homophonic substitution; joint numpy anneal "
               "over column order and key, trigram score")


def _p(params, k, d):
    return type(d)(params.get(k, d))


def _widths(spec):
    out = []
    for part in str(spec).split(","):
        if "-" in part:
            a, b = part.split("-")
            out += list(range(int(a), int(b) + 1))
        elif part.strip():
            out.append(int(part))
    return out


def col_positions(N, w):
    return [np.arange(c, N, w) for c in range(w)]


def transpose(seq, w, order):
    """Encipher: column c holds plaintext positions c, c+w, ...; read columns in `order`."""
    return [seq[i] for c in order for i in range(c, len(seq), w)]


def untranspose_index(N, w, order, cols=None):
    """Array src such that plain[pos] = cipher[...]: returns plainpos_of_cipher (cipher position k -> plain position)."""
    cols = cols or col_positions(N, w)
    return np.concatenate([cols[c] for c in order])


def make_control(spec, seed, corpora, params):
    msgs, plain, train = hom.make_control(spec, seed, corpora, params)
    seq = [s for m in msgs for s in m]
    cw = _widths(params.get("ctrl_widths", "7,10,5,12,9"))
    w = cw[(seed - 1) % len(cw)]
    order = list(range(w))
    random.Random(seed * 31 + 7).shuffle(order)
    print("columnar_homophonic control (seed %d): width %d, order %s, N %d, K %d" % (seed, w, order, len(seq),
                                                                                  len(set(seq))))
    return [transpose(seq, w, order)], plain, train


class Tri:
    def __init__(self, corpora, k=0.5):
        s = "".join(ha.fold(t) for t in corpora)
        self.alpha = ha.ALPHA
        A = len(self.alpha)
        idx = {a: i for i, a in enumerate(self.alpha)}
        x = np.array([idx[c] for c in s if c in idx], dtype=np.int64)
        tri = np.bincount(x[:-2] * A * A + x[1:-1] * A + x[2:], minlength=A ** 3).reshape(A, A, A).astype(float)
        bi = tri.sum(axis=2)
        self.lp = np.log((tri + k) / (bi[:, :, None] + k * A))
        self.uni = np.bincount(x, minlength=A) / len(x)
        self.A = A


def _anneal(cseq, K, N, w, model, iters, rng, t0, uni_w=1.0, order_p=0.25):
    A = model.A
    lp = model.lp
    logq = np.log(model.uni + 1e-9)
    cols = col_positions(N, w)
    order = list(range(w))
    rng.shuffle(order)
    # initial key: signs by frequency onto letters by frequency, cycling (homophones on the commonest letters)
    cnt = np.bincount(cseq, minlength=K)
    letters_by_f = list(np.argsort(-model.uni))
    key = np.zeros(K, dtype=np.int64)
    for r, s in enumerate(np.argsort(-cnt)):
        key[s] = letters_by_f[r % A] if rng.random() < 0.7 else rng.randrange(A)
    plain = np.empty(N, dtype=np.int64)

    def score(order, key):
        plain[untranspose_index(N, w, order, cols)] = cseq
        p = key[plain]
        # -N * KL(decode letters || corpus), as homophonic_anneal.score: stops piling every sign onto a few letters
        c = np.bincount(p, minlength=A)
        nz = c > 0
        u = (c[nz] * (math.log(N) + logq[nz] - np.log(c[nz]))).sum()
        return lp[p[:-2], p[1:-1], p[2:]].sum() + uni_w * u

    cur = score(order, key)
    best, best_state = cur, (list(order), key.copy())
    for it in range(iters):
        T = t0 * (1 - it / iters) + 1e-3
        r = rng.random()
        if r >= order_p or w < 2:
            s = rng.randrange(K)
            if rng.random() < 0.5:  # swap two signs' letters (keeps letter counts) or reassign one sign
                s2 = rng.randrange(K)
                old = (key[s], key[s2])
                key[s], key[s2] = old[1], old[0]
                undo = lambda: (key.__setitem__(s, old[0]), key.__setitem__(s2, old[1]))
            else:
                s2, old = s, (key[s], None)
                key[s] = rng.randrange(A)
                undo = lambda: key.__setitem__(s, old[0])
            if key[s] == old[0]:
                undo()
                continue
            new = score(order, key)
            if new >= cur or rng.random() < math.exp((new - cur) / T):
                cur = new
            else:
                undo()
                continue
        else:
            o2 = list(order)
            if r < order_p * 0.6:
                i, j = rng.sample(range(w), 2)
                o2[i], o2[j] = o2[j], o2[i]
            else:
                i, j = rng.sample(range(w), 2)
                c = o2.pop(i)
                o2.insert(j, c)
            new = score(o2, key)
            if new >= cur or rng.random() < math.exp((new - cur) / T):
                cur, order = new, o2
            else:
                continue
        if cur > best:
            best, best_state = cur, (list(order), key.copy())
    return best, best_state


def bigram_stat(cseq, K, untr):
    """sum n_ij (n_ij - 1) over sign bigrams of the stream read in plaintext order (untr = plain position of each cipher
    position)."""
    plain = np.empty(len(cseq), dtype=np.int64)
    plain[untr] = cseq
    c = np.bincount(plain[:-1] * K + plain[1:], minlength=K * K)
    return int((c * (c - 1)).sum())


def stage1_orders(cseq, K, N, w, rng, restarts=100, iters=4000, keep=2):
    """Hill climb over column orders at width w on bigram_stat; returns [(stat, order)] best first, distinct."""
    cols = col_positions(N, w)
    found = {}
    for _ in range(restarts):
        order = list(range(w))
        rng.shuffle(order)
        cur = bigram_stat(cseq, K, untranspose_index(N, w, order, cols))
        stale = 0
        for _ in range(iters):
            o2 = list(order)
            i, j = rng.sample(range(w), 2)
            if rng.random() < 0.5:
                o2[i], o2[j] = o2[j], o2[i]
            else:
                o2.insert(j, o2.pop(i))
            new = bigram_stat(cseq, K, untranspose_index(N, w, o2, cols))
            if new >= cur:
                stale = 0 if new > cur else stale + 1
                cur, order = new, o2
            else:
                stale += 1
            if stale > 600:
                break
        t = tuple(order)
        found[t] = max(found.get(t, -1), cur)
    ranked = sorted(((v, list(k)) for k, v in found.items()), reverse=True)
    return ranked[:keep]


def solve_two_stage(cseq, signs, model, restarts, rng, params):
    N, K = len(cseq), len(signs)
    s2_iters = _p(params, "s2_iters", _p(params, "iters", 30000))
    s2_restarts = _p(params, "s2_restarts", max(1, restarts))
    t0, uw = _p(params, "t0", 1.0), _p(params, "uni_weight", 1.0)
    best, per_w, st1 = None, {}, {}
    for w in _widths(params.get("widths", "2-12")):
        if w < 2:
            cands = [(bigram_stat(cseq, K, np.arange(N)), [0])]
        else:
            cands = stage1_orders(cseq, K, N, w, rng, _p(params, "s1_restarts", 100), _p(params, "s1_iters", 4000),
                                  _p(params, "s1_keep", 2))
        st1[w] = [(v, o) for v, o in cands]
        for stat, order in cands:
            stream = np.empty(N, dtype=np.int64)
            stream[untranspose_index(N, w, order)] = cseq
            for _ in range(s2_restarts):
                sc, (_, key) = _anneal(stream, K, N, 1, model, s2_iters, rng, t0, uw, 0.0)
                per_w[w] = max(per_w.get(w, -1e18), sc)
                if best is None or sc > best[0]:
                    best = (sc, w, order, key)
    return best, per_w, st1


def solve(cipher_msgs, spec, seed, restarts, corpora, params):
    ha.set_alphabet(params.get("alphabet"))
    model = Tri(corpora)
    seq = [s for m in cipher_msgs for s in m]
    signs = sorted(set(seq))
    sid = {s: i for i, s in enumerate(signs)}
    cseq = np.array([sid[s] for s in seq], dtype=np.int64)
    N, K = len(seq), len(signs)
    iters, t0 = _p(params, "iters", 30000), _p(params, "t0", 1.0)
    rng = random.Random(seed)
    if str(params.get("stage", "joint")) == "two":
        (sc, w, order, key), per_w, st1 = solve_two_stage(cseq, signs, model, restarts, rng, params)
        plain = np.empty(N, dtype=np.int64)
        plain[untranspose_index(N, w, order)] = cseq
        dec = "".join(model.alpha[key[i]] for i in plain)
        info = {"width": w, "order": order, "per_width_best": {k: round(v, 1) for k, v in per_w.items()},
                "stage1": {k: [(v, o) for v, o in c] for k, c in st1.items()},
                "key": {signs[i]: model.alpha[key[i]] for i in range(K)}}
        print("columnar_homophonic two-stage solve: best width %d order %s score %.1f; per width %s; stage-1 best per width %s"
              % (w, order, sc, info["per_width_best"], {k: c[0] for k, c in st1.items()}))
        return dec, float(sc), info
    per_w, best = {}, None
    for w in _widths(params.get("widths", "2-12")):
        for _ in range(max(1, restarts)):
            sc, st = _anneal(cseq, K, N, w, model, iters, rng, t0, _p(params, "uni_weight", 1.0), _p(params, "order_p", 0.25))
            per_w[w] = max(per_w.get(w, -1e18), sc)
            if best is None or sc > best[0]:
                best = (sc, w, st)
    sc, w, (order, key) = best
    plain = np.empty(N, dtype=np.int64)
    plain[untranspose_index(N, w, order)] = cseq
    dec = "".join(model.alpha[key[i]] for i in plain)
    info = {"width": w, "order": order, "per_width_best": {k: round(v, 1) for k, v in per_w.items()},
            "key": {signs[i]: model.alpha[key[i]] for i in range(K)}}
    print("columnar_homophonic solve: best width %d score %.1f; per width %s" % (w, sc, info["per_width_best"]))
    return dec, float(sc), info


def score_recovery(plain, truth, max_shift=12):
    """Share of positions read correctly, maximised over a global shift of -max_shift..max_shift (R15-KAL14 fix,
    6 Oct 2026): a rotation of the column order decodes the right text displaced by a few positions, which a strict
    per-position comparison scores near 0 (seed 1 of the first control: 0.066 strict, 0.795 at shift 4)."""
    n = max(1, len(truth))
    return max(sum(1 for a, b in zip(plain[max(0, k):], truth[max(0, -k):]) if a == b)
               for k in range(-max_shift, max_shift + 1)) / n
