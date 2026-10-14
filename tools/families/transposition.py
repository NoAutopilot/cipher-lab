"""transposition: pure letter transposition of English plaintext -- keyed columnar and fixed routes (FAIR-TRANS, 14 Oct 2026).

Design: the ciphertext letters ARE the plaintext letters, permuted; no substitution. Sub-families searched by `solve`:
  colK   keyed columnar, plaintext written in rows of width w (last row short), columns read in a keyed order
         (columnar_homophonic.transpose, imported); widths `widths` (default 2-12), exhaustive orders for w <= `exh`
         (default 7), anneal over the order above that (swap / move one column, `restarts` x `iters`)
  colKi  the inverse orientation (written in keyed columns, read off in rows), same widths and search
  route  fixed, keyless routes, every one enumerated: unkeyed columnar (identity order) and its inverse for widths
         2-34; column boustrophedon (columns read alternately down and up) and its inverse for widths 2-34; rail fence
         2-12 rails, both orientations; clockwise spiral from the top-left of a w-wide row grid (empty cells of the
         short last row skipped), both orientations, widths 2-34; each also on the reversed ciphertext.
Score: quadgram log-likelihood of the candidate plaintext (26 letters, add-k), a gram touching the unknown sign `?`
scores the corpus's mean gram log-probability. The best score over all sub-families wins; info names it.
Not covered here (already run by marker/marker_sweep.py, D2-FAIR, 8 Oct 2026): whole-text reversal alone, decimation
(every n-th letter mod N), two-line interleave; double transposition; Myszkowski; any transposition of a substitution
(that is columnar_homophonic).

Control design (rule 3): an English window of the target's N starting at a word start, cut from the corpus (removed from the solver's training
text), enciphered with a design fixed per seed from `ctrl_designs` (default cycles colK at w = 2..12, then colKi at
w = 2..12, then route kinds), random keyed order; cipher positions where the TARGET carries `?` are masked to `?`,
so the control has the target's N and its unknown sign at the same place. Recovery = share of positions read right,
best over a shift of -12..12 (columnar_homophonic.score_recovery, imported: a column-order rotation displaces the
text). params: widths (2-12), exh (7), iters (4000), restarts from --restarts, route_max (34), ctrl_designs."""
import itertools
import math
import random

import numpy as np

from families.columnar_homophonic import transpose, untranspose_index, score_recovery as _rec, _widths

DESCRIPTION = ("pure transposition of English: keyed columnar (widths 2-12, both orientations) and keyless routes "
               "(columnar, boustrophedon, rail fence, spiral, reversed); quadgram score")

A = 26
UNK = 26


def _p(params, k, d):
    return type(d)(params.get(k, d))


def fold26(text):
    return "".join(c for c in text.lower() if "a" <= c <= "z")


class Quad:
    def __init__(self, corpora, k=0.5):
        s = fold26("\n".join(corpora))
        x = np.frombuffer(s.encode(), dtype=np.uint8).astype(np.int64) - 97
        q = np.bincount(((x[:-3] * A + x[1:-2]) * A + x[2:-1]) * A + x[3:], minlength=A ** 4).astype(float)
        tri = q.reshape(A ** 3, A).sum(axis=1)
        lp = np.log((q.reshape(A ** 3, A) + k) / (tri[:, None] + k * A)).reshape(A ** 4)
        mean = float((lp * q).sum() / q.sum())
        B = A + 1  # index 26 = unknown sign
        full = np.full(B ** 4, mean)
        a, b, c, d = np.meshgrid(*[np.arange(A)] * 4, indexing="ij")
        full[(((a * B + b) * B + c) * B + d).ravel()] = lp[(((a * A + b) * A + c) * A + d).ravel()]
        self.lp, self.B = full, B

    def score(self, p):
        B = self.B
        return float(self.lp[((p[:-3] * B + p[1:-2]) * B + p[2:-1]) * B + p[3:]].sum())


def enc(seq):
    return np.array([UNK if s == "?" else ord(s.lower()[0]) - 97 for s in seq], dtype=np.int64)


def dec(arr):
    return "".join("?" if v == UNK else chr(97 + v) for v in arr)


# ---- permutations: each returns perm with plain = cipher[perm] (perm[i] = cipher index of plaintext position i)
def perm_columnar(N, w, order):
    """Encipher wrote rows of width w, read columns in `order`: plain[src[k]] = cipher[k]."""
    src = untranspose_index(N, w, order)
    perm = np.empty(N, dtype=np.int64)
    perm[src] = np.arange(N)
    return perm


def inverse(perm):
    inv = np.empty_like(perm)
    inv[perm] = np.arange(len(perm))
    return inv


def _enc_order_from_routes(N, cells):
    """cells: plaintext positions in the order the encipherer reads them out -> perm (plain = cipher[perm])."""
    perm = np.empty(N, dtype=np.int64)
    perm[np.array(cells)] = np.arange(N)
    return perm


def route_boustro(N, w):
    cells = []
    for c in range(w):
        col = list(range(c, N, w))
        cells += col if c % 2 == 0 else col[::-1]
    return _enc_order_from_routes(N, cells)


def route_rail(N, r):
    if r < 2 or r >= N:
        return None
    cyc = 2 * (r - 1)
    rails = [min(i % cyc, cyc - i % cyc) for i in range(N)]
    cells = [i for k in range(r) for i in range(N) if rails[i] == k]
    return _enc_order_from_routes(N, cells)


def route_spiral(N, w):
    h = -(-N // w)
    grid = [[r * w + c if r * w + c < N else None for c in range(w)] for r in range(h)]
    top, bot, left, right, cells = 0, h - 1, 0, w - 1, []
    while top <= bot and left <= right:
        cells += [grid[top][c] for c in range(left, right + 1)]
        cells += [grid[r][right] for r in range(top + 1, bot + 1)]
        if top < bot:
            cells += [grid[bot][c] for c in range(right - 1, left - 1, -1)]
        if left < right:
            cells += [grid[r][left] for r in range(bot - 1, top, -1)]
        top, bot, left, right = top + 1, bot - 1, left + 1, right - 1
    return _enc_order_from_routes(N, [x for x in cells if x is not None])


def route_perms(N, route_max=34):
    """Every keyless route permutation, both orientations, plain and on the reversed ciphertext."""
    base = []
    for w in range(2, min(route_max, N - 1) + 1):
        base.append(("colU w%d" % w, perm_columnar(N, w, list(range(w)))))
        base.append(("boustro w%d" % w, route_boustro(N, w)))
        base.append(("spiral w%d" % w, route_spiral(N, w)))
    for r in range(2, 13):
        p = route_rail(N, r)
        if p is not None:
            base.append(("rail r%d" % r, p))
    out = []
    rev = np.arange(N)[::-1]
    for name, p in base:
        for oname, q in ((name, p), (name + " inv", inverse(p))):
            out.append((oname, q))
            out.append((oname + " rev", rev[q]))  # cipher reversed before the route is undone
    return out


def _search_order(c, N, w, inv, model, iters, restarts, exh, rng):
    def sc(order):
        p = perm_columnar(N, w, order)
        if inv:
            p = inverse(p)
        return model.score(c[p]), p
    best = (-1e18, None, None)
    if w <= exh:
        for order in itertools.permutations(range(w)):
            s, p = sc(list(order))
            if s > best[0]:
                best = (s, list(order), p)
        return best
    for _ in range(max(1, restarts)):
        order = list(range(w))
        rng.shuffle(order)
        cur, p = sc(order)
        for it in range(iters):
            T = 3.0 * (1 - it / iters) + 0.01
            o2 = list(order)
            i, j = rng.sample(range(w), 2)
            if rng.random() < 0.5:
                o2[i], o2[j] = o2[j], o2[i]
            else:
                o2.insert(j, o2.pop(i))
            new, p2 = sc(o2)
            if new >= cur or rng.random() < math.exp((new - cur) / T):
                cur, order, p = new, o2, p2
                if cur > best[0]:
                    best = (cur, list(order), p)
        if cur > best[0]:
            best = (cur, list(order), p)
    return best


def candidates(c, model, params, restarts, seed):
    """All sub-family bests as (score, name, perm)."""
    N = len(c)
    rng = random.Random(seed)
    out = []
    for w in _widths(params.get("widths", "2-12")):
        if w >= N:
            continue
        for inv in (False, True):
            s, order, p = _search_order(c, N, w, inv, model, _p(params, "iters", 4000), restarts,
                                        _p(params, "exh", 7), rng)
            out.append((s, "%s w%d order %s" % ("colKi" if inv else "colK", w, order), p))
    for name, p in route_perms(N, _p(params, "route_max", 34)):
        out.append((model.score(c[p]), "route " + name, p))
    return out


# ---- family_run interface
def _ctrl_designs(params):
    spec = params.get("ctrl_designs")
    if spec:
        return [d.strip() for d in str(spec).split(";") if d.strip()]
    return (["colK:%d" % w for w in range(2, 13)] + ["colKi:%d" % w for w in range(2, 13)] +
            ["boustro:5", "spiral:8", "rail:3", "colU:9", "spiral:5 rev", "boustro:11 inv"])


_WORDS = {}


def word_window(raw, n, seed, margin=2000, want_rest=True):
    """An n-letter window that starts at a word start (a message does), from the middle 90% of the corpus; returns
    (window, rest) with the window and a margin removed from the solver's training text."""
    key = (len(raw), hash(raw[:1000]))
    if _WORDS.get("key") != key:
        ws = "".join(c if c.isalpha() else " " for c in raw.lower()).split()
        _WORDS.update(key=key, words=[f for f in (fold26(w) for w in ws) if f])
    words = _WORDS["words"]
    rng = random.Random(seed * 7919 + n)
    lo, hi = len(words) // 20, len(words) * 19 // 20
    i = rng.randrange(lo, hi)
    out, j = "", i
    while len(out) < n:
        out += words[j]
        j += 1
    m = max(1, margin // 5)
    rest = " ".join(words[:max(0, i - m)] + words[j + m:]) if want_rest else None
    return out[:n], rest


def make_control(spec, seed, corpora, params):
    N = params["N"]
    plain, rest = word_window("\n".join(corpora), N, seed)
    designs = _ctrl_designs(params)
    d = designs[(seed - 1) % len(designs)]
    kind, rest_ = d.split(":")
    parts = rest_.split()
    w = int(parts[0])
    rng = random.Random(seed * 31 + 7)
    if kind in ("colK", "colKi"):
        order = list(range(w))
        while order == sorted(order) and w > 1:
            rng.shuffle(order)
        perm = perm_columnar(N, w, order)
        if kind == "colKi":
            perm = inverse(perm)
    else:
        perm = dict(route_perms(N, max(w, 2)))["%s %s%d%s" % (kind, "r" if kind == "rail" else "w", w,
                                                              "".join(" " + x for x in parts[1:]))]
        order = None
    # plain = cipher[perm]  ->  cipher[perm[i]] = plain[i]
    cipher = [""] * N
    for i, k in enumerate(perm):
        cipher[k] = plain[i]
    tgt = [s for m in params.get("target_msgs") or [] for s in m]
    for k, s in enumerate(tgt[:N]):
        if s == "?":
            cipher[k] = "?"
    print("transposition control (seed %d): design %s order %s, N %d, masked %d" %
          (seed, d, order, N, cipher.count("?")))
    return [cipher], plain, [rest]


def solve(cipher_msgs, spec, seed, restarts, corpora, params):
    model = Quad(corpora)
    seq = [s for m in cipher_msgs for s in m]
    c = enc(seq)
    cands = sorted(candidates(c, model, params, restarts, seed), key=lambda t: -t[0])
    s, name, p = cands[0]
    top = [(round(x[0], 1), x[1]) for x in cands[:5]]
    print("transposition solve: best %s score %.1f; top5 %s" % (name, s, top))
    return dec(c[p]), float(s), {"best": name, "top5": top, "n_candidates": len(cands)}


def block_recovery(plain, truth, minlen=6):
    """Share of truth letters inside a common run of >= minlen letters with the decode, runs taken greedily
    longest-first, each position used once. A keyed columnar read in the inverse orientation decodes legible
    clause-blocks in a permuted order that a quadgram score cannot rank (rotation ambiguity), which the strict
    per-position measure scores near 0 although every word is readable."""
    a, b = list(plain), list(truth)
    used_a, used_b, got = [False] * len(a), [False] * len(b), 0
    while True:
        best = (0, 0, 0)
        for i in range(len(a)):
            for j in range(len(b)):
                k = 0
                while (i + k < len(a) and j + k < len(b) and not used_a[i + k] and not used_b[j + k]
                       and a[i + k] == b[j + k]):
                    k += 1
                if k > best[0]:
                    best = (k, i, j)
        k, i, j = best
        if k < minlen:
            break
        for t in range(k):
            used_a[i + t] = used_b[j + t] = True
        got += k
    return got / max(1, len(b))


def score_recovery(plain, truth):
    """Gate measure (PREREG-FAIR-TRANS): block_recovery (runs >= 6 letters); the strict shift measure is printed."""
    print("transposition recovery: strict(shift<=12) %.3f block6 %.3f" % (_rec(plain, truth), block_recovery(plain, truth)))
    return block_recovery(plain, truth)
