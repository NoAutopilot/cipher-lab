#!/usr/bin/env python3
"""Pure-Python simulated annealing for a homophonic simple substitution (no numpy needed).

  python3 tools/homophonic_anneal.py CIPHER.tsv --corpus A.txt [--corpus B.txt ...] [--order 3]
          [--restarts 8] [--iters 40000] [--skip DOT,COL] [--seed 1] [--out result.json] [--fix 70=q,33=u]
          [--norm nc2]    floor-shifted n-gram score divided by sum N_c^2 (SCORE-NC2, 4 Oct 2026) -- NOT the paper's
                          score (ngram_term: the floor shift can re-rank keys, and the KL unigram term is added)
          [--norm nc2paper]  the paper's S = raw n-gram log-likelihood / sum N_c^2, no floor (Lasry, Biermann and
                          Tomokiyo 2023 App. A pp.195-196; MQS-SOLVER, 9 Oct 2026); run with --uni-weight 0 for it alone
          MQS-SOLVER options (9 Oct 2026; the paper's App. A and the CTTS solver; graded on one matched and one
          mismatched control, tools/tests/MQS-SOLVER-controls.tsv):
          [--moves reassign|swap|both]   swap and its 0.7/0.3 mix ported from tools/subst_hillclimb.py
          [--max-homophones N]   no letter ever holds more than N signs (subst_hillclimb's max_homo)
          [--min-count N] [--homophone-budget K]   rare signs / signs beyond the K most frequent read as ? (CTTS)
          [--drop-letters h] [--collapse-doubles]  letters / doubled letters removed from corpus and model (CTTS)
          [--as-unknown CLASSFILE]  marked signs kept in the stream as gaps; no scored n-gram spans one (never --skip)
          [--alphabet ru-s3p-soft]  a plaintext alphabet other than the 24 folded Latin letters (A2P4-KAL4, 3 Oct 2026)
          [--noise 0.1]   error-tolerant solve: see anneal_noisy (LANE R6 CM2, 25 Sept 2026)
          [--robust 0.1]  bounded-loss n-gram scoring: see RobustModel (LANE R6 CM2)
          [--backoff]     interpolated absolute-discount n-gram of --order with recursive backoff: see BackoffModel
                          (LANE R7 CM3, 25 Sept 2026); lets --order 4 or 5 run on a 2 MB corpus without add-k sparsity
  python3 tools/homophonic_anneal.py --control PLAIN.txt --signs K --length N --corpus ... (matched control)
  python3 tools/homophonic_anneal.py --control PLAIN.txt --profile CIPHER.tsv --corpus ... (exact-profile control)
  python3 tools/homophonic_anneal.py --control PLAIN.txt --signs 40 --length 1500 --control-homs 1-2 --marked 0.3:60
          --marked-mode skip|unknown|wild|nomen --corpus ...   (marked-sign control, make_marked_control; MQS-SOLVER)

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
DROP_LETTERS = ""        # --drop-letters (MQS-SOLVER, 9 Oct 2026): letters removed from corpus, control text and model
COLLAPSE_DOUBLES = False  # --collapse-doubles (MQS-SOLVER): a doubled letter folded to one in corpus and control text
GAP = "?"                # a gap position (--as-unknown, --min-count, --homophone-budget): no scored n-gram spans it


def set_text_options(drop="", collapse=False):
    """--drop-letters / --collapse-doubles (MQS-SOLVER, 9 Oct 2026; CTTS paper p.2: the solver may ignore a letter such
    as h and doubled letters). Applied inside fold(), so the corpus, the control text and the model all see the same
    stream; Model then omits the dropped letters from its alphabet. Must catch: an 'h' or a doubled letter the cipher
    never writes (the model otherwise expects it). Must NOT change: drop="" and collapse=False (the defaults) leave
    fold() byte for byte as before (tools/tests/test_homophonic_mqs.py)."""
    global DROP_LETTERS, COLLAPSE_DOUBLES
    DROP_LETTERS, COLLAPSE_DOUBLES = drop or "", bool(collapse)


def fold(text):
    if CUSTOM_ALPHA is not None:
        keep = set(CUSTOM_ALPHA)
        return "".join(c for c in unicodedata.normalize("NFC", text) if c in keep)
    t = unicodedata.normalize("NFKD", text.lower())
    t = "".join(c for c in t if not unicodedata.combining(c))
    t = t.replace("ß", "ss").replace("j", "i").replace("v", "u")
    if W_AS_UU:
        t = t.replace("w", "uu")
    t = re.sub(r"[^a-z]", "", t)
    if DROP_LETTERS:
        t = "".join(c for c in t if c not in DROP_LETTERS)
    if COLLAPSE_DOUBLES:
        t = re.sub(r"(.)\1+", r"\1", t)
    return t


class Model:
    def __init__(self, texts, order=3, k=0.5):
        s = "".join(fold(t) for t in texts)
        self.order = order
        self.n = Counter(s[i:i + order] for i in range(len(s) - order + 1))
        self.c = Counter(s[i:i + order - 1] for i in range(len(s) - order + 2))
        self.uni = Counter(s)
        tot = sum(self.uni.values())
        al = "".join(a for a in ALPHA if a not in DROP_LETTERS) if DROP_LETTERS else ALPHA
        self.freq = {a: (self.uni[a] + 0.5) / (tot + 0.5 * len(al)) for a in al}
        self.k, self.V = k, len(al)
        if CUSTOM_ALPHA is not None or DROP_LETTERS:  # anneal() reads model.alpha; the default path never sets it
            self.alpha = al
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


NORMS = ("none", "nc2", "nc2paper")


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
    model._nc2_q0 = nc2_q0(model)
    return f


def nc2_q0(model):
    """The corpus's own sum of squared letter frequencies (a constant per model)."""
    if getattr(model, "_nc2_q0", None) is None:
        model._nc2_q0 = sum(v * v for v in model.freq.values()) / sum(model.freq.values()) ** 2
    return model._nc2_q0


def paper_score(raw, sumsq):
    """Lasry, Biermann and Tomokiyo 2023 App. A (p.195-196): S = sum_g N_g log F_g / sum_c N_c^2, here with F_g the
    model's n-gram probability: the raw n-gram log-likelihood divided by the sum of squared letter counts, no floor."""
    return raw / max(sumsq, 1)


def ngram_term(model, raw, n_grams, n, sumsq, norm="none"):
    """The n-gram part of the score from its running pieces: raw = sum of n-gram log-probs, n_grams = their number,
    n = text length, sumsq = sum over letters of N_c^2.
    norm "none": raw (the original score, unchanged).
    norm "nc2" (SCORE-NC2, 4 Oct 2026; after Lasry, Biermann and Tomokiyo 2023, Cryptologia 47:2, App. A p. 195,
    S = sum_g N_g log F_g / sum_c N_c^2): (raw - n_grams * floor) * n^2 * q0 / sumsq, with floor = nc2_floor(model)
    and q0 = the corpus's own sum of squared letter frequencies. Correction (MQS-SOLVER, 9 Oct 2026): this is NOT the
    paper's score. Subtracting n_grams * floor before dividing shifts every key's numerator by the same amount but
    divides it by a key-dependent sumsq, so two keys with different sum N_c^2 can rank differently from the paper's S;
    and score() adds the KL unigram term (uni_w, default 1.0) on top. A key that piles many signs onto one letter
    raises sumsq and is penalised in proportion. Its one real use was a NON-TEST (clair1161 planted control 0/3,
    LEDGER line 2583); C1161-LOLO: "nc2 rewards rare letters at this free share (D2, D3)"
    (ciphers/clair1161-avis-flandre-1688/tx/PREREG_reanneal_lolo.md point 1).
    norm "nc2paper" (MQS-SOLVER, 9 Oct 2026): the paper's S exactly, paper_score(raw, sumsq) = raw / sumsq, no floor,
    multiplied by the constant n^2 * q0 (fixed by the text length and the corpus, so every ranking between keys of one
    text is the paper's) only so anneal temperatures stay on the plain score's scale. Run it with uni_w 0 for the
    paper's objective alone. Note the sign: with F_g a probability, log F_g < 0, so a larger sumsq makes S less
    negative -- the paper's own F_g scale decides whether concentration is rewarded; ours is a log-probability.
    Must catch: a ranking that differs from raw / sumsq. Must NOT change: norm none and nc2 (offline tests)."""
    if norm == "none":
        return raw
    if norm == "nc2paper":
        return paper_score(raw, sumsq) * n * n * nc2_q0(model)
    if norm != "nc2":
        raise ValueError(f"norm {norm!r}: expected one of {NORMS}")
    fl = nc2_floor(model)
    return (raw - n_grams * fl) * n * n * model._nc2_q0 / max(sumsq, 1)


def score(model, plain, uni_w, norm="none"):
    """plain may carry GAP ('?') positions (--as-unknown, --min-count): it is split into fragments at every gap and no
    scored n-gram window spans one (subst_hillclimb.score_frags' rule, 23 Sept 2026; partial_key_test.py's "a pair or
    triple counts only when every position is mapped"); gaps are left out of the letter counts. Without a gap this
    is the single-fragment sum, byte for byte the old score."""
    o = model.order
    if GAP in plain:
        frags = plain.split(GAP)
        s = sum(model.logp(f[i:i + o]) for f in frags for i in range(len(f) - o + 1))
        ngr = sum(max(0, len(f) - o + 1) for f in frags)
        cnt = Counter(c for c in plain if c != GAP)
        n = sum(cnt.values())
    else:
        s = sum(model.logp(plain[i:i + o]) for i in range(len(plain) - o + 1))
        cnt = Counter(plain)
        n = len(plain)
        ngr = max(0, n - o + 1)
    s = ngram_term(model, s, ngr, n, sum(c * c for c in cnt.values()), norm)
    # -N * KL(observed letter distribution || corpus distribution): penalises both wrong and over-concentrated
    # letter use (a plain multinomial term rewards decoding everything as e/n)
    u = sum(c * math.log(n * model.freq[a] / c) for a, c in cnt.items())
    return s + uni_w * u


SWAP_SHARE = 0.3  # moves="both": share of swap proposals (subst_hillclimb.anneal: reassign 0.7 / swap 0.3)
MOVES = ("reassign", "swap", "both")


def _allot(letters, freq, k, cap=0):
    """k signs over letters by frequency: at least one per letter (the most frequent k when k < len(letters)), the rest
    by largest remainder, never more than cap per letter (0 = no cap). make_control's rule. Returns {letter: count}."""
    ls = sorted(letters, key=lambda a: -freq[a])
    alloc = {a: 1 for a in ls[:k]}
    extra = k - len(alloc)
    while extra > 0:
        cand = [a for a in ls if not cap or alloc[a] < cap]
        if not cand:
            raise ValueError(f"{k} signs cannot fit {len(ls)} letters at most {cap} per letter")
        a = max(cand, key=lambda a: freq[a] / alloc[a])
        alloc[a] += 1
        extra -= 1
    return alloc


def _init_key_mqs(signs, fixed, allowed, init, letters, weights, rng, cap, moves):
    """Starting key when --max-homophones or --moves swap is set (MQS-SOLVER, 9 Oct 2026). Under a cap every sign draws
    (corpus-frequency-weighted, as in anneal) among the letters still below the cap -- subst_hillclimb's rejection
    draw, written as a filtered draw. Under moves=swap the letter multiset is fixed by the start, so it is the
    frequency allotment (_allot, capped) shuffled over the free signs: Lasry's fixed homophone count per element
    (LESSONS-LASRY.md s.2 practice 3)."""
    if cap and cap * len(letters) < len(signs):
        raise ValueError(f"--max-homophones {cap}: {len(signs)} signs cannot fit {len(letters)} letters")
    key = {s: fixed[s] for s in signs if s in fixed}
    hc = Counter(key.values())
    free = [s for s in signs if s not in fixed]
    if moves == "swap":
        rest = [s for s in free if s not in allowed and not (s in init and init[s] in letters)]
        for s in free:
            if s not in rest:
                key[s] = rng.choice(allowed[s]) if s in allowed else init[s]
                hc[key[s]] += 1
        fq = dict(zip(letters, weights))
        pool = []
        if rest:
            room = {a: (cap - hc[a]) if cap else len(rest) for a in letters}
            alloc = _allot([a for a in letters if room[a] > 0], fq, len(rest), 0)
            # re-cap per letter against what fixed/allowed signs already hold
            over = 0
            for a in list(alloc):
                if alloc[a] > room[a]:
                    over += alloc[a] - room[a]
                    alloc[a] = room[a]
            while over:
                a = max((a for a in letters if alloc.get(a, 0) < room[a]), key=lambda a: fq[a] / (alloc.get(a, 0) + 1))
                alloc[a] = alloc.get(a, 0) + 1
                over -= 1
            pool = [a for a, c in alloc.items() for _ in range(c)]
            rng.shuffle(pool)
        for s, a in zip(rest, pool):
            key[s] = a
        return key
    for s in free:
        ok = [a for a in letters if not cap or hc[a] < cap]
        if s in allowed:
            al = [a for a in allowed[s] if a in ok] or allowed[s]
            v = rng.choice(al)
        elif s in init and init[s] in ok:
            v = init[s]
        else:
            v = rng.choices(ok, [w for a, w in zip(letters, weights) if a in ok])[0]
        key[s] = v
        hc[v] += 1
    return key


def search_gaps(seq, gaps=(), min_count=0, budget=0):
    """The signs that stay out of the search and read as GAP (MQS-SOLVER, 9 Oct 2026). gaps: listed signs
    (--as-unknown, marked/nomenclature signs kept in the stream, never deleted); min_count: signs seen fewer times
    (CTTS README: threshold raised to 10, "93% of the transcribed symbols will be processed"); budget: at most this
    many signs searched, the most frequent first, ties by sign name (CTTS: 76 symbols against 68 allowed homophones).
    Returns (gap set, processed share of tokens)."""
    g = set(gaps or ())
    cnt = Counter(x for x in seq if x not in g)
    if min_count:
        g |= {s for s, c in cnt.items() if c < min_count}
    if budget:
        kept = sorted((s for s in cnt if s not in g), key=lambda s: (-cnt[s], str(s)))
        g |= set(kept[budget:])
    n = len(seq)
    return g, (sum(1 for x in seq if x not in g) / n if n else 0.0)


def anneal(seq, model, iters, rng, uni_w, t0=4.0, fixed=None, allowed=None, init=None, norm="none", pairs=None, pair_prob=0.0,
           moves="reassign", max_homophones=0, gaps=None, on_accept=None):
    """Incremental annealing: a move re-scores only the n-grams touching the changed sign's positions.
    allowed: optional {sign: "letters"} restricting what a sign may decode to (e.g. vowel-indicator marks to "aeiou").
    init: optional {sign: letter} starting map (e.g. a known key for a different letter, LANE AX2 26 Sept 2026) --
    a non-fixed, non-allowed-restricted sign starts here instead of a corpus-frequency-weighted random letter; the
    anneal is free to move away from it exactly as from any other starting point (this only seeds, never fixes).
    norm: "none" (default, unchanged), "nc2" or "nc2paper" (ngram_term).
    pairs/pair_prob (R9-KAL6, 6 Oct 2026, kaliningrad-2015): pairs = {letter: partner} (soft_pairs() builds n<->N for a
    soft-letter alphabet); with probability pair_prob a move flips one sign's letter to its partner as a single move
    (a sign at a letter with no partner skips the move), otherwise the ordinary random-letter move. Absent (None or
    pair_prob 0) the RNG stream and every result are byte-for-byte the old ones.
    MQS-SOLVER options (9 Oct 2026; Lasry, Biermann and Tomokiyo 2023 App. A pp.195-197, Figs A18-A19; CTTS; Kopal 2019;
    LESSONS-LASRY.md s.3). Defaults (reassign, 0, None) keep the RNG stream and every result byte for byte.
    moves: "reassign" (one sign takes a new random letter, the old behaviour), "swap" (two signs exchange their
    letters, so the per-letter homophone counts stay as the start set them, Lasry's fixed-count scheme) or "both"
    (reassign 0.7 / swap 0.3) -- the move and its mix ported from tools/subst_hillclimb.py (23 Sept 2026,
    bowes-walsingham-1583). Must catch: a key one exchange away from the truth that two reassigns cannot reach
    without crossing a worse state. Must NOT change: a swap preserves the multiset of assigned letters (test).
    max_homophones N: no letter ever holds more than N signs in any accepted state; a reassign that would exceed it is
    skipped (ported from subst_hillclimb's max_homo check; this anneal has no greedy polish, so the start key and every
    move carry the check). Must catch: a key piling many signs on e. Must NOT block: a key within the cap (test).
    gaps: signs kept in the stream as GAP positions (search_gaps: --as-unknown, --min-count, --homophone-budget); they
    are never deleted, and no scored n-gram window spans a gap (fragment splitting, as score()). Must catch: --skip's
    deletion, which joins the neighbours of a marked sign into a false n-gram (test).
    on_accept: test hook, called with the key after every accepted move."""
    o = model.order
    gaps = set(gaps or ())
    signs = sorted(set(seq) - gaps) if gaps else sorted(set(seq))
    letters = list(getattr(model, "alpha", ALPHA))  # a unit model (families/homophonic.py units=syl) carries its own
    weights = [model.freq[a] for a in letters]
    lf = {a: math.log(model.freq[a]) for a in letters}
    pos = {s: [i for i, x in enumerate(seq) if x == s] for s in signs}
    n = len(seq)
    ng = max(0, n - o + 1)
    if gaps:
        okw = [True] * ng
        for i, x in enumerate(seq):
            if x in gaps:
                for j in range(max(0, i - o + 1), min(i, n - o) + 1):
                    okw[j] = False
        wins = [j for j in range(ng) if okw[j]]
        starts = {s: sorted({j for i in pos[s] for j in range(max(0, i - o + 1), min(i, n - o) + 1) if okw[j]})
                  for s in signs}
    else:
        wins = range(ng)
        starts = {s: sorted({j for i in pos[s] for j in range(max(0, i - o + 1), min(i, n - o) + 1)}) for s in signs}
    fixed = fixed or {}
    allowed = {s: list(v) for s, v in (allowed or {}).items()}
    init = init or {}
    if moves not in MOVES:
        raise ValueError(f"moves {moves!r}: expected one of {MOVES}")
    if max_homophones or moves == "swap":
        key = _init_key_mqs(signs, fixed, allowed, init, letters, weights, rng, max_homophones, moves)
    else:
        key = {s: fixed.get(s) or (rng.choice(allowed[s]) if s in allowed else
               (init[s] if s in init and init[s] in letters else rng.choices(letters, weights)[0]))
               for s in signs}
    signs = [s for s in signs if s not in fixed]  # crib-fixed signs never move
    pl = [key.get(x, GAP) for x in seq]
    lp = model.logp

    def part(js):
        return sum(lp("".join(pl[j:j + o])) for j in js)

    cnt = Counter(c for c in pl if c != GAP) if gaps else Counter(pl)
    nn = sum(cnt.values()) if gaps else n
    nwin = len(wins) if gaps else ng
    hc = Counter(key.values())
    xlx = lambda c: c * math.log(c) if c > 0 else 0.0
    raw = sum(lp("".join(pl[j:j + o])) for j in wins)
    sq = sum(c * c for c in cnt.values())
    cur = score(model, "".join(pl), uni_w, norm)
    best, bestkey = cur, dict(key)
    swap_ok = moves in ("swap", "both") and len(signs) >= 2
    for it in range(iters):
        T = t0 * (1 - it / iters) + 0.02
        if swap_ok and (moves == "swap" or rng.random() < SWAP_SHARE):
            s1, s2 = rng.sample(signs, 2)
            a, b = key[s1], key[s2]
            if a == b or (s1 in allowed and b not in allowed[s1]) or (s2 in allowed and a not in allowed[s2]):
                continue
            js = sorted(set(starts[s1]) | set(starts[s2]))
            before = part(js)
            for i in pos[s1]:
                pl[i] = b
            for i in pos[s2]:
                pl[i] = a
            m1, m2 = len(pos[s1]), len(pos[s2])
            dl = {a: m2 - m1, b: m1 - m2}
            du = sum(v * lf[l] for l, v in dl.items()) - sum(xlx(cnt[l] + v) - xlx(cnt[l]) for l, v in dl.items())
            dr = part(js) - before
            sq2 = sq + sum((cnt[l] + v) ** 2 - cnt[l] ** 2 for l, v in dl.items())
            if norm == "none":
                d = dr + uni_w * du
            else:
                d = ngram_term(model, raw + dr, nwin, nn, sq2, norm) - ngram_term(model, raw, nwin, nn, sq, norm) + uni_w * du
            if d >= 0 or rng.random() < math.exp(d / T):
                key[s1], key[s2] = b, a
                sq, raw, cur = sq2, raw + dr, cur + d
                for l, v in dl.items():
                    cnt[l] += v
                if on_accept:
                    on_accept(key)
                if cur > best:
                    best, bestkey = cur, dict(key)
            else:
                for i in pos[s1]:
                    pl[i] = a
                for i in pos[s2]:
                    pl[i] = b
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
        if max_homophones and hc[new] >= max_homophones:
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
            d = ngram_term(model, raw + dr, nwin, nn, sq2, norm) - ngram_term(model, raw, nwin, nn, sq, norm) + uni_w * du
        if d >= 0 or rng.random() < math.exp(d / T):
            key[s] = new
            if norm != "none":
                sq = sq2
            raw += dr
            cnt[new] += m
            cnt[old] -= m
            hc[new] += 1
            hc[old] -= 1
            cur += d
            if on_accept:
                on_accept(key)
            if cur > best:
                best, bestkey = cur, dict(key)
        else:
            for i in pos[s]:
                pl[i] = old
    return score(model, "".join(bestkey.get(x, GAP) for x in seq), uni_w, norm), bestkey


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
          pairs=None, pair_prob=0.0, moves="reassign", max_homophones=0, gaps=None, min_count=0, homophone_budget=0):
    """noise > 0 (error-tolerant, anneal_noisy): results are (score, key, free) triples instead of (score, key).
    init: optional {sign: letter} starting map, same on every restart (each restart still explores independently
    via its own random moves; only the starting point is shared, not the search).
    norm: "none", "nc2" or "nc2paper" (ngram_term); only "none" is implemented for the noise > 0 path.
    moves, max_homophones, gaps, min_count, homophone_budget (MQS-SOLVER, 9 Oct 2026): see anneal() and search_gaps();
    a gap sign is absent from the returned key (decode it with key.get(sign, GAP)). Not implemented for noise > 0."""
    if noise and norm != "none":
        raise ValueError("norm nc2 is not implemented for the error-tolerant (noise > 0) anneal")
    mqs = moves != "reassign" or max_homophones or gaps or min_count or homophone_budget
    if noise and mqs:
        raise ValueError("the MQS-SOLVER options are not implemented for the error-tolerant (noise > 0) anneal")
    if gaps or min_count or homophone_budget:
        gaps, _ = search_gaps(seq, gaps, min_count, homophone_budget)
    rng = random.Random(seed)
    results = []
    for r in range(restarts):
        if noise:
            results.append(anneal_noisy(seq, model, iters, rng, uni_w, noise, fixed=fixed, allowed=allowed, init=init))
        elif mqs:
            results.append(anneal(seq, model, iters, rng, uni_w, fixed=fixed, allowed=allowed, init=init, norm=norm,
                                  pairs=pairs, pair_prob=pair_prob, moves=moves, max_homophones=max_homophones,
                                  gaps=gaps))
        else:
            results.append(anneal(seq, model, iters, rng, uni_w, fixed=fixed, allowed=allowed, init=init, norm=norm,
                                  pairs=pairs, pair_prob=pair_prob))
    results.sort(key=lambda x: -x[0])
    return results


def anneal_nomen(seq, model, iters, rng, uni_w, vocab, word_prob=0.1, t0=4.0, fixed=None, word_bonus=0.0,
                 unique_words=True, word_signs=None):
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
    word_signs: optional set of signs that may take a vocab word (R13-SIENAWC, 6 Oct 2026: a structural restriction, e.g.
    only signs the transcriber wrote as multi-character units or drawn non-alphanumeric marks); every other sign is
    proposed letters only. None = no restriction, and the random stream is then exactly as before.
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
        wok = word_signs is None or s in word_signs
        new = rng.choice(vocab) if vocab and wok and rng.random() < word_prob else rng.choice(letters)
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
                unique_words=True, word_signs=None):
    """Restarts of anneal_nomen(), best first; same seeding pattern as solve()."""
    rng = random.Random(seed)
    res = [anneal_nomen(seq, model, iters, rng, uni_w, vocab, word_prob, fixed=fixed, word_bonus=word_bonus,
                         unique_words=unique_words, word_signs=word_signs)
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


def make_marked_control(plain_text, K, N, seed, homs=(1, 2), marked_share=0.0, marked_types=0):
    """A homophonic control with 1..hi homophones per letter plus marked word/name signs (MQS-SOLVER, 9 Oct 2026;
    matched to the Mary Stuart cipher, Lasry, Biermann and Tomokiyo 2023 Fig. 8 p.119: 1-2 homophones per letter plus
    nomenclature). The words of PLAIN.txt are read from the start; the `marked_types` most frequent word types of that
    stretch become marked signs m0, m1, ... (one token per word occurrence, replaced with a probability q chosen so
    marked tokens are about `marked_share` of the N tokens; q is capped at 1, and the achieved share is reported).
    The remaining letter stream gets K letter signs allotted by frequency (_allot: at least homs[0]... one per letter,
    at most homs[1] per letter) and each occurrence draws a homophone at random, as make_control.
    Returns (seq of N tokens, plain with '-' at marked positions, truth {sign: letter}, marked set, info)."""
    rng = random.Random(seed + 2000)
    words = [w for w in (fold(x) for x in plain_text.split()) if w]
    pre, tot = [], 0
    for w in words:  # a generous stretch: N letters even before any word is marked
        pre.append(w)
        tot += len(w)
        if tot >= 2 * N:
            break
    if tot < N:
        raise SystemExit(f"--control text has {tot} letters, N={N} needs more")
    wc = Counter(pre)
    marked_words = [w for w, _ in wc.most_common(marked_types)] if marked_share and marked_types else []
    mw = {w: f"m{i}" for i, w in enumerate(marked_words)}
    q = 0.0
    if mw:
        m_all = sum(c for w, c in wc.items() if w in mw)
        lm = sum(c * len(w) for w, c in wc.items() if w in mw)
        lo = sum(c * len(w) for w, c in wc.items() if w not in mw)
        sh = marked_share
        q = min(1.0, sh * (lo + lm) / (m_all * (1 - sh) + sh * lm))
    toks = []  # (marked sign or None, letter or '-')
    for w in words:
        if w in mw and rng.random() < q:
            toks.append((mw[w], "-"))
        else:
            toks.extend((None, c) for c in w)
        if len(toks) >= N:
            break
    toks = toks[:N]
    p = "".join(c for _, c in toks)
    lcnt = Counter(c for c in p if c != "-")
    alloc = _allot(list(lcnt), lcnt, K, homs[1])
    hm, i = {}, 0
    for a in sorted(alloc, key=lambda a: -lcnt[a]):
        hm[a] = [f"s{i + j}" for j in range(alloc[a])]
        i += alloc[a]
    seq = [m if m else rng.choice(hm[c]) for m, c in toks]
    truth = {x: a for a, xs in hm.items() for x in xs}
    marked = {m for m, _ in toks if m}
    info = {"q": round(q, 3), "marked_share": round(sum(1 for m, _ in toks if m) / max(1, len(toks)), 3),
            "marked_types_used": len(marked), "letter_signs": len(truth), "homs_per_letter": dict(Counter(alloc.values()))}
    return seq, p, truth, marked, info


def corpus_vocab(texts, n=100, minlen=2):
    """The n most frequent folded words of at least minlen letters in the corpus texts (solve_nomen's vocab for the
    marked-sign control's word_signs cell)."""
    c = Counter(w for t in texts for w in (fold(x) for x in t.split()) if len(w) >= minlen)
    return [w for w, _ in c.most_common(n)]


def read_sign_list(path):
    """--as-unknown CLASSFILE: one sign per line (a TSV's first column; '#' comments), or commas within a line."""
    out = set()
    for l in open(path, encoding="utf-8"):
        l = l.split("#")[0].strip()
        if l:
            out |= {x.strip() for x in l.split("\t")[0].split(",") if x.strip()}
    return out


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
    ap.add_argument("--moves", choices=MOVES, default="reassign",
                    help="MQS-SOLVER: reassign (default, unchanged), swap (two signs exchange letters; homophone counts "
                         "fixed at the start) or both (reassign 0.7 / swap 0.3, ported from subst_hillclimb.py)")
    ap.add_argument("--max-homophones", type=int, default=0,
                    help="MQS-SOLVER: no letter ever holds more than N signs (0 = no cap)")
    ap.add_argument("--min-count", type=int, default=0,
                    help="MQS-SOLVER: signs seen fewer than N times stay out of the search and decode as ? (gaps)")
    ap.add_argument("--homophone-budget", type=int, default=0,
                    help="MQS-SOLVER: search at most K signs, the most frequent; the rest decode as ? (gaps)")
    ap.add_argument("--drop-letters", default="",
                    help="MQS-SOLVER: letters removed from corpus, control text and model (e.g. h)")
    ap.add_argument("--collapse-doubles", action="store_true",
                    help="MQS-SOLVER: fold a doubled letter to one in corpus and control text")
    ap.add_argument("--as-unknown", metavar="CLASSFILE",
                    help="MQS-SOLVER: the listed signs stay in the stream as gaps (?); no scored n-gram spans a gap; "
                         "never deleted (contrast --skip, which deletes and joins the neighbours)")
    ap.add_argument("--control-homs", default="",
                    help="control mode, MQS-SOLVER: LO-HI homophones per letter (e.g. 1-2) with --signs K letter signs "
                         "(make_marked_control)")
    ap.add_argument("--marked", default="",
                    help="control mode, MQS-SOLVER: SHARE:TYPES, e.g. 0.3:60 -- about SHARE of the N tokens are TYPES "
                         "marked word signs (make_marked_control)")
    ap.add_argument("--marked-mode", choices=("skip", "unknown", "wild", "nomen"), default="skip",
                    help="control mode with --marked: skip (delete the marked signs, the --skip behaviour), unknown "
                         "(gaps, the --as-unknown behaviour), wild (each occurrence its own letter, families/homophonic "
                         "wild=) or nomen (solve_nomen with word_signs = the marked signs, vocab = corpus_vocab 100)")
    ap.add_argument("--fix-first", type=int, default=0,
                    help="control mode: hold the signs of the first N positions at their true letters (the matched "
                         "control for a target crib of N letters)")
    a = ap.parse_args()
    global W_AS_UU
    W_AS_UU = a.w_as_uu
    set_alphabet(a.alphabet)
    set_text_options(a.drop_letters, a.collapse_doubles)
    mq = {"moves": a.moves, "max_homophones": a.max_homophones, "min_count": a.min_count,
          "homophone_budget": a.homophone_budget}
    unknown = read_sign_list(a.as_unknown) if a.as_unknown else set()
    texts = [open(f, encoding="utf-8").read() for f in a.corpus]
    model = BackoffModel(texts, a.order) if a.backoff else Model(texts, a.order)
    if a.robust:
        model = RobustModel(model, a.robust)
    if a.control and (a.marked or a.control_homs):
        lo, hi = (int(x) for x in (a.control_homs or "1-2").split("-"))
        sh, ty = (a.marked.split(":") + ["0"])[:2] if a.marked else ("0", "0")
        ptext = open(a.control, encoding="utf-8").read()
        seq, p, truth, marked, info = make_marked_control(ptext, a.signs, a.length, a.seed, (lo, hi), float(sh), int(ty))
        lpos = [i for i, c in enumerate(p) if c != "-"]
        mode = a.marked_mode if marked else "unknown"
        if mode == "skip":
            sseq = [x for x in seq if x not in marked]
            res = solve(sseq, model, a.restarts, a.iters, a.seed, a.uni_weight, norm=a.norm, gaps=unknown or None, **mq)
            key = res[0][1]
            dec = [key.get(x, GAP) for x in sseq]
        elif mode == "unknown":
            res = solve(seq, model, a.restarts, a.iters, a.seed, a.uni_weight, norm=a.norm, gaps=(marked | unknown) or None, **mq)
            key = res[0][1]
            dec = [key.get(seq[i], GAP) for i in lpos]
        elif mode == "wild":
            sw = [f"{x}#{i}" if x in marked else x for i, x in enumerate(seq)]
            res = solve(sw, model, a.restarts, a.iters, a.seed, a.uni_weight, norm=a.norm, gaps=unknown or None, **mq)
            key = res[0][1]
            dec = [key.get(sw[i], GAP) for i in lpos]
        else:
            vocab = corpus_vocab(texts)
            res = solve_nomen(seq, model, a.restarts, a.iters, a.seed, a.uni_weight, vocab, word_signs=marked)
            key = res[0][1]
            dec = [key.get(seq[i], GAP) for i in lpos]
        gold = [p[i] for i in lpos]
        ok = sum(1 for x, y in zip(dec, gold) if x == y)
        proc = sum(1 for x in dec if x != GAP) / max(1, len(gold))
        out = {"mode": "control-marked", "marked_mode": mode, "N": len(seq), "K_letter": len(truth),
               "marked_types": len(marked), **info, "letter_tokens": len(gold), "letters_correct": ok,
               "share": round(ok / max(1, len(gold)), 4), "processed_share": round(proc, 4), "score": res[0][0],
               "restart_scores": [round(r[0], 1) for r in res], **mq, "norm": a.norm, "uni_weight": a.uni_weight,
               "restarts": a.restarts, "seed": a.seed}
        print(f"control-marked N={len(seq)} letters={len(gold)} K={len(truth)} marked={len(marked)} "
              f"({info['marked_share']:.1%}) mode={mode}: {ok}/{len(gold)} = {ok / max(1, len(gold)):.1%}; "
              f"processed {proc:.1%}")
        print("".join(dec)[:200])
    elif a.control:
        extra = {}
        if a.profile:
            prof = load_profile(a.profile, set(a.skip.split(",")))
            seq, p, truth, start = make_profile_control(open(a.control, encoding="utf-8").read(), prof, a.seed)
            extra = {"profile": a.profile, "window_start": start, "profile_counts": prof,
                     "sign_counts": sorted(Counter(seq).values(), reverse=True)}
        else:
            seq, p, truth = make_control(open(a.control, encoding="utf-8").read(), a.signs, a.length, model, a.seed)
        fixed = {seq[i]: truth[seq[i]] for i in range(a.fix_first)}
        res = solve(seq, model, a.restarts, a.iters, a.seed, a.uni_weight, fixed, noise=a.noise, norm=a.norm,
                    gaps=unknown or None, **mq)
        sc, key = res[0][:2]
        free = res[0][2] if a.noise else {}
        dec = "".join(free.get(i, key.get(x, GAP)) for i, x in enumerate(seq))
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
        res = solve(seq, model, a.restarts, a.iters, a.seed, a.uni_weight, fixed, noise=a.noise, init=init, norm=a.norm,
                    gaps=unknown or None, **mq)
        sc, key = res[0][:2]
        free = res[0][2] if a.noise else {}
        dec = "".join(free.get(i, key.get(x, GAP)) for i, x in enumerate(seq))
        proc = sum(1 for c in dec if c != GAP) / max(1, len(dec))
        if unknown or a.min_count or a.homophone_budget:
            print(f"processed share {proc:.1%} of {len(dec)} tokens (the rest are gaps: --as-unknown/--min-count/"
                  f"--homophone-budget)")
        out = {"mode": "target", "N": len(seq), "K": len(set(seq)), "score": sc, "key": key, "decoded": dec,
               **({"processed_share": round(proc, 4)} if (unknown or a.min_count or a.homophone_budget) else {}),
               "restart_scores": [round(r[0], 1) for r in res],
               "restart_decodes": ["".join(r[1].get(x, GAP) for x in seq)[:120] for r in res[:4]],
               **({"noise": a.noise, "free": {str(i): l for i, l in sorted(free.items())}} if a.noise else {})}
        print(f"target N={len(seq)} K={len(set(seq))} best score {sc:.1f}; restarts {out['restart_scores']}")
        print(dec)
    if a.out:
        json.dump(out, open(a.out, "w"), ensure_ascii=False, indent=1)


if __name__ == "__main__":
    main()
