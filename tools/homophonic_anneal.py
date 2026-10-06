#!/usr/bin/env python3
"""Pure-Python simulated annealing for a homophonic simple substitution (no numpy needed).

  python3 tools/homophonic_anneal.py CIPHER.tsv --corpus A.txt [--corpus B.txt ...] [--order 3]
          [--restarts 8] [--iters 40000] [--skip DOT,COL] [--seed 1] [--out result.json] [--fix 70=q,33=u]
          [--norm nc2]    divide the n-gram score by sum N_c^2 (Lasry et al. 2023 App. A; SCORE-NC2, 4 Oct 2026)
          [--alphabet ru-s3p-soft]  a plaintext alphabet other than the 24 folded Latin letters (A2P4-KAL4, 3 Oct 2026)
          [--noise 0.1]   error-tolerant solve: see anneal_noisy (LANE R6 CM2, 25 Sept 2026)
          [--robust 0.1]  bounded-loss n-gram scoring: see RobustModel (LANE R6 CM2)
          [--backoff]     interpolated absolute-discount n-gram of --order with recursive backoff: see BackoffModel
                          (LANE R7 CM3, 25 Sept 2026); lets --order 4 or 5 run on a 2 MB corpus without add-k sparsity
  python3 tools/homophonic_anneal.py --control PLAIN.txt --signs K --length N --corpus ... (matched control)
  python3 tools/homophonic_anneal.py --control PLAIN.txt --profile CIPHER.tsv --corpus ... (exact-profile control)

CIPHER.tsv: long format, header with a `sign` column (and optional `line`); rows whose sign is in --skip are
dropped. Every distinct sign is mapped to one plaintext letter a-z (u/v, i/j merged; umlauts folded). Score =
sum of log n-gram probabilities (add-k smoothed, order --order, from the --corpus files after the same
folding, word spaces removed) + a unigram term keeping the letter distribution near the corpus's
(--uni-weight). Several restarts; the best key and decoding are printed and written to --out.

--control: enciphers the first N letters of PLAIN.txt (after folding) with a random homophonic key of K
signs, homophones allotted to letters by corpus frequency, each occurrence picking a homophone at random;
then solves it blind with the same settings and prints the share of letters recovered. This is rule 3's
matched control: run it with the target's own N and K before reporting any negative on the target.

--profile CIPHER.tsv (control mode; campaign espagnol142-mercy-1648 H1, 27 Sept 2026): a stricter control
whose sign occurrence multiset equals CIPHER.tsv's *exactly* (the target's own K counts, e.g. 57/42/41/.../1),
not corpus letter frequency allotted to homophone group sizes. N and K come from the profile (--signs/--length
are ignored). make_profile_control searches PLAIN.txt (seeded random window starts) for an N-letter window whose
letter counts can be partitioned exactly by the profile counts (largest counts first, backtracking with a node
cap), assigns each partition part to its letter as one sign, and enciphers each occurrence by a homophone drawn
in proportion to that sign's remaining quota, so every sign ends at exactly its profile count. The JSON out
carries `profile`, `window_start`, `profile_counts` and `sign_counts` (equal by construction). Answers the
question Y8 left open: does the target still beat a control that shares its whole symbol profile, or was the
gap carried by the skewed profile alone.

Test: python3 tools/tests/test_homophonic_anneal.py
"""
import argparse, json, math, random, re, sys, unicodedata
from collections import Counter

ALPHA = "abcdefghiklmnopqrstuwxyz"  # j->i, v->u
DEFAULT_ALPHA = ALPHA
CUSTOM_ALPHA = None  # set_alphabet(): a plaintext alphabet other than the 24 folded Latin letters (A2P4-KAL4)

# Named plaintext alphabets for --alphabet (A2P4-KAL4, 3 Oct 2026). Case-sensitive: an upper-case letter is a letter
# of its own, not a capital. The ru-*-soft alphabets are tools/data/ru19_soft's (README there: the softening rule).
ALPHABETS = {
    "ru-s3p-soft": "BDFHLMNPRSTWZabcdefghiklmnoprstuwyz",    # 35: S3' Latin, consonant+q merged into one letter
    "ru-s3-soft": "BDFGHKLMNPRSTWZabcdefghiklmnoprstuwyz",   # 37: S3 Latin, consonant+q merged into one letter
}


def set_alphabet(alpha=None):
    """Switch the plaintext alphabet for every later fold()/Model/anneal in this process. None, "" or "default"
    restores the 24-letter default exactly (folding rules unchanged). Otherwise a name from ALPHABETS or a literal
    string of distinct characters; fold() then keeps only those characters, case-sensitive, with no lower-casing,
    accent folding or j/v merging -- the corpus is expected to be written in that alphabet already."""
    global ALPHA, CUSTOM_ALPHA
    if not alpha or alpha == "default":
        ALPHA, CUSTOM_ALPHA = DEFAULT_ALPHA, None
        return ALPHA
    a = ALPHABETS.get(alpha, alpha)
    if len(set(a)) != len(a):
        raise SystemExit(f"--alphabet {alpha!r}: characters must be distinct")
    ALPHA = CUSTOM_ALPHA = a
    return a


W_AS_UU = False


def fold(text):
    if CUSTOM_ALPHA is not None:
        keep = set(CUSTOM_ALPHA)
        return "".join(c for c in unicodedata.normalize("NFC", text) if c in keep)
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
        if CUSTOM_ALPHA is not None:  # anneal() reads model.alpha; the default path never sets it (unchanged)
            self.alpha = ALPHA
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
        if hasattr(model, "alpha"):
            self.alpha = model.alpha
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
        if CUSTOM_ALPHA is not None:
            self.alpha = ALPHA
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


NORMS = ("none", "nc2")


def nc2_floor(model):
    """The n-gram log-prob floor that --norm nc2 shifts by, so every n-gram term is >= 0 (Lasry et al. 2023's F_g
    scores are non-negative; with raw negative log-probs, dividing by sum N_c^2 would *reward* a degenerate key).
    add-k Model/UnitModel: the exact minimum, an unseen n-gram after the most frequent context. RobustModel: its
    bound log(q/V). Anything else: the lowest logp over the model's own cache plus a probe of unseen grams."""
    if getattr(model, "_nc2_floor", None) is not None:
        return model._nc2_floor
    if hasattr(model, "k") and hasattr(model, "c") and model.c:
        f = math.log(model.k / (max(model.c.values()) + model.k * model.V))
    elif hasattr(model, "floor"):
        f = math.log(model.floor)
    else:
        a = list(getattr(model, "alpha", ALPHA))
        probe = ["".join(a[(i * 7 + j * 3) % len(a)] for j in range(model.order)) for i in range(len(a))]
        f = min([model.logp(g) for g in probe] + list(getattr(model, "cache", {}).values()))
    model._nc2_floor = f
    model._nc2_q0 = sum(v * v for v in model.freq.values()) / sum(model.freq.values()) ** 2
    return f


def ngram_term(model, raw, n_grams, n, sumsq, norm="none"):
    """The n-gram part of the score from its running pieces: raw = sum of n-gram log-probs, n_grams = their number,
    n = text length, sumsq = sum over letters of N_c^2.
    norm "none": raw (the original score, unchanged).
    norm "nc2" (SCORE-NC2, 4 Oct 2026; Lasry, Biermann and Tomokiyo 2023, Cryptologia 47:2, App. A p. 195,
    S = sum_g N_g log F_g / sum_c N_c^2): (raw - n_grams * floor) * n^2 * q0 / sumsq, with floor = nc2_floor(model)
    and q0 = the corpus's own sum of squared letter frequencies. The n^2 * q0 factor is a constant for a given text
    length, so the ranking is exactly the paper's; it only rescales the score so a text with corpus-like letter
    use scores about what the shifted plain sum would, keeping anneal temperatures meaningful. A key that piles many
    signs onto one letter raises sumsq and is penalised in proportion."""
    if norm == "none":
        return raw
    if norm != "nc2":
        raise ValueError(f"norm {norm!r}: expected one of {NORMS}")
    fl = nc2_floor(model)
    return (raw - n_grams * fl) * n * n * model._nc2_q0 / max(sumsq, 1)


def score(model, plain, uni_w, norm="none"):
    o = model.order
    s = sum(model.logp(plain[i:i + o]) for i in range(len(plain) - o + 1))
    cnt = Counter(plain)
    n = len(plain)
    s = ngram_term(model, s, max(0, n - o + 1), n, sum(c * c for c in cnt.values()), norm)
    # -N * KL(observed letter distribution || corpus distribution): penalises both wrong and over-concentrated
    # letter use (a plain multinomial term rewards decoding everything as e/n)
    u = sum(c * math.log(n * model.freq[a] / c) for a, c in cnt.items())
    return s + uni_w * u


def anneal(seq, model, iters, rng, uni_w, t0=4.0, fixed=None, allowed=None, init=None, norm="none", pairs=None, pair_prob=0.0):
    """Incremental annealing: a move re-scores only the n-grams touching the changed sign's positions.
    allowed: optional {sign: "letters"} restricting what a sign may decode to (e.g. vowel-indicator marks to "aeiou").
    init: optional {sign: letter} starting map (e.g. a known key for a different letter, LANE AX2 26 Sept 2026) --
    a non-fixed, non-allowed-restricted sign starts here instead of a corpus-frequency-weighted random letter; the
    anneal is free to move away from it exactly as from any other starting point (this only seeds, never fixes).
    norm: "none" (default, unchanged) or "nc2" (ngram_term: divide by sum N_c^2, SCORE-NC2 4 Oct 2026).
    pairs/pair_prob (R9-KAL6, 6 Oct 2026, kaliningrad-2015): pairs = {letter: partner} (soft_pairs() builds n<->N for a
    soft-letter alphabet); with probability pair_prob a move flips one sign's letter to its partner as a single move
    (a sign at a letter with no partner skips the move), otherwise the ordinary random-letter move. Absent (None or
    pair_prob 0) the RNG stream and every result are byte-for-byte the old ones."""
    o = model.order
    signs = sorted(set(seq))
    letters = list(getattr(model, "alpha", ALPHA))  # a unit model (families/homophonic.py units=syl) carries its own
    weights = [model.freq[a] for a in letters]
    lf = {a: math.log(model.freq[a]) for a in letters}
    pos = {s: [i for i, x in enumerate(seq) if x == s] for s in signs}
    n = len(seq)
    starts = {s: sorted({j for i in pos[s] for j in range(max(0, i - o + 1), min(i, n - o) + 1)}) for s in signs}
    fixed = fixed or {}
    allowed = {s: list(v) for s, v in (allowed or {}).items()}
    init = init or {}
    key = {s: fixed.get(s) or (rng.choice(allowed[s]) if s in allowed else
           (init[s] if s in init and init[s] in letters else rng.choices(letters, weights)[0]))
           for s in signs}
    signs = [s for s in signs if s not in fixed]  # crib-fixed signs never move
    pl = [key[x] for x in seq]
    lp = model.logp

    def part(js):
        return sum(lp("".join(pl[j:j + o])) for j in js)

    cnt = Counter(pl)
    xlx = lambda c: c * math.log(c) if c > 0 else 0.0
    ng = max(0, n - o + 1)
    raw = sum(lp("".join(pl[j:j + o])) for j in range(ng))
    sq = sum(c * c for c in cnt.values())
    cur = score(model, "".join(pl), uni_w, norm)
    best, bestkey = cur, dict(key)
    for it in range(iters):
        T = t0 * (1 - it / iters) + 0.02
        s = rng.choice(signs)
        old = key[s]
        if pairs and pair_prob and rng.random() < pair_prob:
            new = pairs.get(old, old)
            if s in allowed and new not in allowed[s]:
                continue
        else:
            new = rng.choice(allowed.get(s, letters))
        if new == old:
            continue
        js = starts[s]
        before = part(js)
        for i in pos[s]:
            pl[i] = new
        m = len(pos[s])
        du = m * (lf[new] - lf[old]) - (xlx(cnt[new] + m) - xlx(cnt[new]) + xlx(cnt[old] - m) - xlx(cnt[old]))
        dr = part(js) - before
        if norm == "none":
            d = dr + uni_w * du
        else:
            sq2 = sq + (cnt[new] + m) ** 2 - cnt[new] ** 2 + (cnt[old] - m) ** 2 - cnt[old] ** 2
            d = ngram_term(model, raw + dr, ng, n, sq2, norm) - ngram_term(model, raw, ng, n, sq, norm) + uni_w * du
        if d >= 0 or rng.random() < math.exp(d / T):
            key[s] = new
            if norm != "none":
                sq = sq2
            raw += dr
            cnt[new] += m
            cnt[old] -= m
            cur += d
            if cur > best:
                best, bestkey = cur, dict(key)
        else:
            for i in pos[s]:
                pl[i] = old
    return score(model, "".join(bestkey[x] for x in seq), uni_w, norm), bestkey


def anneal_noisy(seq, model, iters, rng, uni_w, noise, t0=4.0, fixed=None, allowed=None, init=None, cap_mult=1.5, pos_prob=0.3,
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
    letters = list(getattr(model, "alpha", ALPHA))  # a unit model (families/homophonic.py units=syl) carries its own
    weights = [model.freq[a] for a in letters]
    lf = {a: math.log(model.freq[a]) for a in letters}
    pos = {s: [i for i, x in enumerate(seq) if x == s] for s in signs}
    n = len(seq)
    starts = {s: sorted({j for i in pos[s] for j in range(max(0, i - o + 1), min(i, n - o) + 1)}) for s in signs}
    fixed = fixed or {}
    allowed = {s: list(v) for s, v in (allowed or {}).items()}
    init = init or {}
    key = {s: fixed.get(s) or (rng.choice(allowed[s]) if s in allowed else
           (init[s] if s in init and init[s] in letters else rng.choices(letters, weights)[0]))
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
        if pairs and pair_prob and rng.random() < pair_prob:
            new = pairs.get(old, old)
            if s in allowed and new not in allowed[s]:
                continue
        else:
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


def soft_pairs(alpha):
    """{letter: partner} for a soft-letter alphabet (ru-s3p-soft, ru-s3-soft): each upper-case letter whose lower case
    is also in the alphabet is paired with it, both ways (n<->N). R9-KAL6, 6 Oct 2026."""
    out = {}
    for c in alpha:
        if c.isupper() and c.lower() in alpha:
            out[c], out[c.lower()] = c.lower(), c
    return out


def solve(seq, model, restarts, iters, seed, uni_w, fixed=None, allowed=None, noise=0.0, init=None, norm="none",
          pairs=None, pair_prob=0.0):
    """noise > 0 (error-tolerant, anneal_noisy): results are (score, key, free) triples instead of (score, key).
    init: optional {sign: letter} starting map, same on every restart (each restart still explores independently
    via its own random moves; only the starting point is shared, not the search).
    norm: "none" or "nc2" (ngram_term); nc2 is not implemented for the noise > 0 path."""
    if noise and norm != "none":
        raise ValueError("norm nc2 is not implemented for the error-tolerant (noise > 0) anneal")
    rng = random.Random(seed)
    results = []
    for r in range(restarts):
        if noise:
            results.append(anneal_noisy(seq, model, iters, rng, uni_w, noise, fixed=fixed, allowed=allowed, init=init))
        else:
            results.append(anneal(seq, model, iters, rng, uni_w, fixed=fixed, allowed=allowed, init=init, norm=norm,
                                  pairs=pairs, pair_prob=pair_prob))
    results.sort(key=lambda x: -x[0])
    return results


def anneal_nomen(seq, model, iters, rng, uni_w, vocab, word_prob=0.1, t0=4.0, fixed=None, word_bonus=0.0,
                 unique_words=True):
    """Homophonic + nomenclator anneal (R10-SIENA7N, 6 Oct 2026, siena-concistoro-2308 no. 7). Each sign decodes to one
    plaintext letter OR to one whole word from `vocab` (a list of folded strings: the nomenclator layer, a sign standing
    for a frequent word or name, R4750-style). The decode is the concatenation of the values, so its length varies;
    score() is the same (n-gram + uni_w x the -N*KL letter term) on that concatenation. A move picks a free sign and,
    with probability word_prob, a random vocab word, else a random letter. Incremental: only the n-grams touching the
    changed tokens are re-scored, from a window of order-1 tokens on each side (every value is >= 1 char long).
    word_bonus: added per extra character of each decoded word token (len(value)-1), offsetting the n-gram model's
    length penalty (a 3-letter value pays about three characters' log-probability where a letter pays one); 0 = off.
    unique_words: a vocab word may sit on at most one sign at a time (a move onto a word another sign holds is skipped);
    without it a positive word_bonus lets the anneal pile one long word onto many signs.
    Returns (score, key) with key {sign: value}; the score includes the bonus. Does not touch anneal()/solve(); their results are unchanged."""
    o = model.order
    signs = sorted(set(seq))
    letters = list(getattr(model, "alpha", ALPHA))
    weights = [model.freq[a] for a in letters]
    vocab = [w for w in vocab if w]
    pos = {s: [i for i, x in enumerate(seq) if x == s] for s in signs}
    n = len(seq)
    fixed = fixed or {}
    key = {s: fixed.get(s) or rng.choices(letters, weights)[0] for s in signs}
    free = [s for s in signs if s not in fixed]
    clusters = {}
    for s in signs:  # positions closer than o tokens share n-grams: group them so each n-gram is counted once
        cl, cur = [], None
        for i in pos[s]:
            if cur and i - cur[-1] < o:
                cur.append(i)
            else:
                cur = [i]
                cl.append(cur)
        clusters[s] = [(c[0], c[-1]) for c in cl]
    pl = [key[x] for x in seq]
    lp = model.logp
    pad = o - 1

    def local(a, b):
        # n-grams of the window [a-pad, b+pad] that touch at least one char of tokens a..b
        lo, hi = max(0, a - pad), min(n, b + pad + 1)
        left = "".join(pl[lo:a])[-pad:] if a > lo else ""
        mid = "".join(pl[a:b + 1])
        right = "".join(pl[b + 1:hi])[:pad]
        w = left + mid + right
        st, en = len(left), len(left) + len(mid)
        return sum(lp(w[j:j + o]) for j in range(max(0, st - o + 1), min(en, len(w) - o + 1)))

    def total(vals):
        return score(model, "".join(vals), uni_w) + word_bonus * sum(len(v) - 1 for v in vals)

    from collections import Counter as _C
    cnt = _C("".join(pl))
    raw = sum(lp(t[j:j + o]) for t in ["".join(pl)] for j in range(len(t) - o + 1))

    def uterm(c):
        N = sum(c.values())
        return sum(v * math.log(N * model.freq[a] / v) for a, v in c.items() if v > 0)

    cur = raw + uni_w * uterm(cnt)
    best, bestkey = cur, dict(key)
    held = {v for v in key.values() if len(v) > 1}
    for it in range(iters):
        T = t0 * (1 - it / iters) + 0.02
        s = rng.choice(free)
        old = key[s]
        new = rng.choice(vocab) if vocab and rng.random() < word_prob else rng.choice(letters)
        if new == old or (unique_words and len(new) > 1 and new in held):
            continue
        before = sum(local(a, b) for a, b in clusters[s])
        for i in pos[s]:
            pl[i] = new
        after = sum(local(a, b) for a, b in clusters[s])
        m = len(pos[s])
        c2 = cnt.copy()
        for ch in old:
            c2[ch] -= m
        for ch in new:
            c2[ch] += m
        d = (after - before) + uni_w * (uterm(c2) - uterm(cnt)) + word_bonus * m * (len(new) - len(old))
        if d >= 0 or rng.random() < math.exp(d / T):
            key[s] = new
            held.discard(old)
            if len(new) > 1:
                held.add(new)
            cnt = c2
            cur += d
            if cur > best:
                best, bestkey = cur, dict(key)
        else:
            for i in pos[s]:
                pl[i] = old
    return total([bestkey[x] for x in seq]), bestkey


def solve_nomen(seq, model, restarts, iters, seed, uni_w, vocab, word_prob=0.1, fixed=None, word_bonus=0.0,
                unique_words=True):
    """Restarts of anneal_nomen(), best first; same seeding pattern as solve()."""
    rng = random.Random(seed)
    res = [anneal_nomen(seq, model, iters, rng, uni_w, vocab, word_prob, fixed=fixed, word_bonus=word_bonus,
                         unique_words=unique_words)
           for _ in range(restarts)]
    res.sort(key=lambda x: -x[0])
    return res


def load_init_key(path):
    """--init: a key.tsv/key_full.tsv-style TSV (code, value, ...) -> {sign_str: letter}, folded and restricted
    to single a-z letters (NULL rows, name/word values and multi-letter values are skipped -- those signs start
    random, same as with no --init at all)."""
    rows = [l.rstrip("\n").split("\t") for l in open(path, encoding="utf-8") if l.strip() and not l.startswith("#")]
    h = rows[0]
    ci = h.index("code") if "code" in h else h.index("sign")
    vi = h.index("value")
    out = {}
    for r in rows[1:]:
        if len(r) <= max(ci, vi):
            continue
        v = fold(r[vi])
        if len(v) == 1 and v in ALPHA:
            out[r[ci]] = v
    return out


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


def load_profile(path, skip):
    """Sign occurrence counts of a long-format CIPHER.tsv (same reading rules as target mode)."""
    rows = [l.rstrip("\n").split("\t") for l in open(path, encoding="utf-8") if l.strip() and not l.startswith("#")]
    si = rows[0].index("sign")
    seq = [r[si].rstrip("?") for r in rows[1:] if r[si].rstrip("?") not in skip]
    return sorted(Counter(seq).values(), reverse=True)


def partition_exact(counts, needs, node_cap=200000):
    """Assign every part of `counts` (desc) to a letter so each letter's parts sum to needs[letter] exactly.
    Returns {index_in_counts: letter} or None. Backtracking, largest part first, letters by remaining need."""
    letters = list(needs)
    rem = dict(needs)
    assign = {}
    nodes = [0]

    def rec(i):
        nodes[0] += 1
        if nodes[0] > node_cap:
            return False
        if i == len(counts):
            return all(v == 0 for v in rem.values())
        c = counts[i]
        # a letter whose remaining need is positive but smaller than every remaining part can never be filled
        smallest_left = counts[-1]
        if any(0 < v < smallest_left for v in rem.values()):
            return False
        tried = set()
        for a in sorted(letters, key=lambda a: -rem[a]):
            if rem[a] < c or rem[a] in tried:
                continue
            tried.add(rem[a])
            rem[a] -= c
            assign[i] = a
            if rec(i + 1):
                return True
            rem[a] += c
            del assign[i]
        return False

    return dict(assign) if rec(0) else None


def make_profile_control(plain_text, profile_counts, seed, tries=5000):
    """Exact-profile control: a window of PLAIN.txt enciphered so the sign counts equal profile_counts exactly."""
    rng = random.Random(seed + 1000)
    p_all = fold(plain_text)
    N, K = sum(profile_counts), len(profile_counts)
    if len(p_all) < N:
        raise SystemExit(f"--control text has {len(p_all)} letters, profile needs {N}")
    for _ in range(tries):
        start = rng.randrange(0, len(p_all) - N + 1)
        p = p_all[start:start + N]
        needs = dict(Counter(p))
        if len(needs) > K:
            continue
        assign = partition_exact(profile_counts, needs)
        if assign is None:
            continue
        homs = {a: [] for a in needs}
        quota = {}
        for i, a in assign.items():
            s = f"s{i}"
            homs[a].append(s)
            quota[s] = profile_counts[i]
        seq = []
        for a in p:
            ss = homs[a]
            s = rng.choices(ss, weights=[quota[x] for x in ss])[0]
            quota[s] -= 1
            seq.append(s)
        assert all(v == 0 for v in quota.values())
        truth = {s: a for a, ss in homs.items() for s in ss}
        return seq, p, truth, start
    raise SystemExit(f"no {N}-letter window of the control text admits an exact partition by the profile after {tries} tries")


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
    ap.add_argument("--norm", choices=NORMS, default="none",
                    help="n-gram score normalisation: none (default) or nc2 = divide by the sum of squared letter counts "
                         "(Lasry et al. 2023 App. A), which penalises keys piling many signs on one letter")
    ap.add_argument("--out")
    ap.add_argument("--w-as-uu", action="store_true", help="fold w to uu in corpus and control (ciphers writing w as a doubled u sign)")
    ap.add_argument("--alphabet", default="default",
                    help="plaintext alphabet: 'default' (24 folded Latin letters a-z minus j, v; unchanged), a name "
                         "from ALPHABETS (" + ", ".join(ALPHABETS) + "; case-sensitive, an upper-case letter is its "
                         "own letter -- tools/data/ru19_soft/README.md gives the softening rule), or a literal string "
                         "of distinct characters. With a non-default alphabet the corpus must already be written in "
                         "it: fold() keeps only its characters and does no lower-casing or accent folding.")
    ap.add_argument("--control")
    ap.add_argument("--signs", type=int)
    ap.add_argument("--profile", help="control mode: replicate this CIPHER.tsv's sign occurrence multiset exactly "
                    "(N and K taken from it; --signs/--length ignored)")
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
    ap.add_argument("--init", help="target mode: start the anneal from this key file's sign->letter map instead of "
                    "a corpus-frequency-weighted random letter (LANE AX2 26 Sept 2026, a key-seeded anneal). A "
                    "TSV with 'code'/'sign' and 'value' columns (key.tsv/key_full.tsv's own format); rows whose "
                    "value is not a single a-z letter (NULL, a name, multi-letter) are skipped, that sign starts "
                    "random as usual. A sign named in --fix still overrides --init for that sign. "
                    "Default behaviour (no --init) is unchanged: every sign starts at a random letter.")
    ap.add_argument("--fix-first", type=int, default=0,
                    help="control mode: hold the signs of the first N positions at their true letters (the matched "
                         "control for a target crib of N letters)")
    a = ap.parse_args()
    global W_AS_UU
    W_AS_UU = a.w_as_uu
    set_alphabet(a.alphabet)
    texts = [open(f, encoding="utf-8").read() for f in a.corpus]
    model = BackoffModel(texts, a.order) if a.backoff else Model(texts, a.order)
    if a.robust:
        model = RobustModel(model, a.robust)
    if a.control:
        extra = {}
        if a.profile:
            prof = load_profile(a.profile, set(a.skip.split(",")))
            seq, p, truth, start = make_profile_control(open(a.control, encoding="utf-8").read(), prof, a.seed)
            extra = {"profile": a.profile, "window_start": start, "profile_counts": prof,
                     "sign_counts": sorted(Counter(seq).values(), reverse=True)}
        else:
            seq, p, truth = make_control(open(a.control, encoding="utf-8").read(), a.signs, a.length, model, a.seed)
        fixed = {seq[i]: truth[seq[i]] for i in range(a.fix_first)}
        res = solve(seq, model, a.restarts, a.iters, a.seed, a.uni_weight, fixed, noise=a.noise, norm=a.norm)
        sc, key = res[0][:2]
        free = res[0][2] if a.noise else {}
        dec = "".join(free.get(i, key[x]) for i, x in enumerate(seq))
        ok = sum(1 for x, y in zip(dec, p) if x == y)
        out = {"mode": "control", "N": len(seq), "K": len(set(seq)), "letters_correct": ok,
               "share": round(ok / len(p), 3), "score": sc, "plain": p, "decoded": dec,
               "restart_scores": [round(r[0], 1) for r in res], **extra,
               **({"noise": a.noise, "free": len(free)} if a.noise else {})}
        print(f"control N={len(seq)} K={len(set(seq))}: {ok}/{len(p)} letters = {ok/len(p):.1%}; score {sc:.1f}"
              + (f"; exact profile, window start {extra['window_start']}" if a.profile else ""))
        print(dec[:200])
    else:
        rows = [l.rstrip("\n").split("\t") for l in open(a.cipher, encoding="utf-8") if l.strip() and not l.startswith("#")]
        h = rows[0]
        si = h.index("sign")
        skip = set(a.skip.split(","))
        seq = [r[si].rstrip("?") for r in rows[1:] if r[si].rstrip("?") not in skip]
        fixed = dict(kv.split("=") for kv in a.fix.split(",")) if a.fix else {}
        init = load_init_key(a.init) if a.init else None
        res = solve(seq, model, a.restarts, a.iters, a.seed, a.uni_weight, fixed, noise=a.noise, init=init, norm=a.norm)
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
