"""nomenclator: two-level numeric word code (family C of ciphers/armstrong-madison-1808, ARM-C1 26 Sept 2026).

Design (ciphers/armstrong-madison-1808/design/family_C_spec.md, from ARM-DESIGN): whitespace-separated integer
tokens. Values 1-99 are a PARTICLE block (one plain list of function words); values >= 100 are a FAMILY BOOK
factorised as decade (10*d) -> a family of related entries and units digit -> a member slot with a book-wide
popularity order (0 the commonest member, 1 next, 4/6/7 middling, 8, then 2/3/5/9 rare). Wildcard tokens
(`*`, `**`, `***`, `<..>`) are out-of-vocabulary passages (the target's shorthand), scored as an unknown word and
never decoded. No alphabetical-order term anywhere (ARM-DESIGN Q1: not decidable, siblings block-local at best);
units digits are NOT a deterministic inflection map (Q2): every seen value is its own entry, with a soft
same-decade tie (shared crude stem) and a slot-order term (a commoner word belongs in a commoner slot).

Score = word-trigram LM log-probability (interpolated absolute discounting, D=0.75, trained on the spec's corpora
minus the held-out file) + prior penalty (a word outside the candidate prior costs `oov_pen` nats, never a ban)
+ `tie_w` per same-decade pair sharing a stem + `slot_w` per same-decade pair whose unigram-frequency order agrees
with the slot order (minus when it disagrees) - `dup_w` per extra value mapped to the same word. Solver: Gibbs
sampling over one value at a time with a shortlist of candidates drawn from the LM's own successor/predecessor
tables around the value's occurrences plus a sample of the prior list, temperature annealed T0 -> T1 over
`sweeps` sweeps, then greedy sweeps; `restarts` independent chains, best total score wins.

Matched control (spec control 1): a letter cut from the HELD-OUT corpus file (`holdout` = index into the spec's
corpus list, default 5 = Jefferson Vol IX in tools/data/en18; the file is removed from the LM's training set),
369 coded tokens (the target's own numeric-token count), particle block = the 99 commonest training words at a
random permutation of 1-99 (cold start: the solver never sees this key), family book = `decades` (180) decades
filled with the top content-word stem families, members in slots by the book-wide slot order (commonest member
slot 0 ...), remaining slots filled with the next most frequent unassigned forms, `book_forms` (1800) forms in
all, decade order random. Words in neither list become a `*` wildcard (a run of them one `*`, as a shorthand
passage). Recovery = share of coded tokens whose decoded word equals the true word; particles and book are also
reported separately (CLAUDE.md rule 3, unbalanced-class paragraph) on stdout.

Prior word lists for the solver (the same on control and target): particles = the `fw` (120) commonest training
words plus the 26 letters; book = the union of the four tools/data/uscodes-1800 tables' plaintext column, the
words of Bourdeau's THE=972 decodes in tools/data/uscodes-1800/decodes/, and the `top_content` (2500) commonest
training content forms. The LM vocabulary is every training word with count >= `vocab_min` (3); others are <unk>.

--param keys: holdout=5 phase1=20 sweeps=30 restarts (CLI) book_forms=1800 decades=180 tie_w=0.5 slot_w=0.3 dup_w=2.0
oov_pen=3.0 fw=120 top_content=2500 vocab_min=3 T0=1.5 T1=0.25 max_cands=700 greedy=3

Cribs (ARM3-LOOP, 26 Sept 2026, family D model-in-the-loop): `params["cribs"]` = {value: word} (keys int or
str) are held fixed through phase 1, every annealed sweep and the greedy sweeps of every restart -- a cribbed
value is never resampled and is set in the initial key of each restart, so its neighbours are scored against
the crib from the first sweep. Words are folded to the LM's vocabulary (an unseen word scores as <unk>). The
driver is `tools/crib_rounds.py --family nomenclator` (make / round / score / view); `info["restart_keys"]`
carries every restart's final key so the driver can report a per-value confidence (share of restarts agreeing
with the best one), and `info["cribs"]` the cribs actually applied.
Test: python3 tools/tests/test_nomenclator.py (offline, about a minute)."""
import math, os, random, re, sys
from collections import Counter, defaultdict

TOOLS = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if TOOLS not in sys.path:
    sys.path.insert(0, TOOLS)
import judge_plaintext as jp  # noqa: E402

DESCRIPTION = ("two-level numeric word code: particle block 1-99 + family book >= 100 (decade = family, units = "
               "member slot), word-trigram Gibbs anneal with a sibling-vocabulary prior; wildcards *,**,<..> = OOV "
               "(--param holdout=5 sweeps=30 tie_w=0.5 slot_w=0.3 book_forms=1800)")
WILD = re.compile(r"^(\*+|<\.\.>)$")
SLOT_ORDER_DEFAULT = [0, 1, 4, 6, 7, 8, 2, 3, 5, 9]
UNK = "<unk>"
D = 0.75
CODES_DIR = os.path.join(TOOLS, "data", "uscodes-1800")
_LAST_CONTROL = {"classes": None}
_LM_CACHE = {}


def get_lm(texts, vocab_min):
    key = (tuple((len(t), hash(t[:5000]), hash(t[-5000:])) for t in texts), vocab_min)
    lm = _LM_CACHE.get(key)
    if lm is None:
        _LM_CACHE.clear()
        lm = _LM_CACHE[key] = LM(texts, vocab_min)
    return lm


def _p(params, k, d):
    v = params.get(k, d)
    return type(d)(v) if not isinstance(v, type(d)) else v


def words_of(text):
    return re.findall(r"[a-z]+", text.lower().translate(jp.FOLD))


def stem(w):
    for suf in ("ations", "ation", "ments", "ment", "ness", "ings", "ing", "ions", "ion", "ers", "er", "est", "ies",
                "ied", "ed", "es", "ly", "s"):
        if w.endswith(suf) and len(w) - len(suf) >= 4:
            w = w[:-len(suf)]
            break
    return w[:6]


# ---------------------------------------------------------------- language model
class LM:
    """Word trigram, interpolated absolute discounting. Words outside the vocabulary are <unk>."""

    def __init__(self, texts, vocab_min=3):
        uni = Counter()
        seqs = []
        for t in texts:
            ws = words_of(t)
            seqs.append(ws)
            uni.update(ws)
        self.vocab = {w for w, c in uni.items() if c >= vocab_min}
        self.uni, self.bi, self.tri = Counter(), Counter(), Counter()
        self.succ2, self.succ3, self.pred2, self.mid = defaultdict(Counter), defaultdict(Counter), defaultdict(Counter), defaultdict(Counter)
        for ws in seqs:
            ws = ["<s>", "<s>"] + [w if w in self.vocab else UNK for w in ws] + ["</s>"]
            self.uni.update(ws[2:])
            for i in range(2, len(ws)):
                a, b, c = ws[i - 2], ws[i - 1], ws[i]
                self.bi[(b, c)] += 1
                self.tri[(a, b, c)] += 1
        for (b, c), n in self.bi.items():
            self.succ2[b][c] = n
            self.pred2[c][b] = n
        for (a, b, c), n in self.tri.items():
            self.succ3[(a, b)][c] = n
            self.mid[(a, c)][b] = n
        self.bic = Counter()
        self.nbi = Counter()
        for (b, c), n in self.bi.items():
            self.bic[b] += n
            self.nbi[b] += 1
        self.tric = Counter()
        self.ntri = Counter()
        for (a, b, c), n in self.tri.items():
            self.tric[(a, b)] += n
            self.ntri[(a, b)] += 1
        self.total = sum(self.uni.values())
        self.V = len(self.uni)
        self.logu = {w: math.log((c + 1) / (self.total + self.V)) for w, c in self.uni.items()}
        self.logu_unk = math.log(1 / (self.total + self.V))
        self.cache = {}
        self.freq = uni

    def p1(self, w):
        return math.exp(self.logu.get(w, self.logu_unk))

    def p2(self, w, b):
        cb = self.bic.get(b, 0)
        if not cb:
            return self.p1(w)
        n = self.bi.get((b, w), 0)
        return max(n - D, 0) / cb + D * self.nbi[b] / cb * self.p1(w)

    def p3(self, w, a, b):
        cab = self.tric.get((a, b), 0)
        if not cab:
            return self.p2(w, b)
        n = self.tri.get((a, b, w), 0)
        return max(n - D, 0) / cab + D * self.ntri[(a, b)] / cab * self.p2(w, b)

    def lp3(self, w, a, b):
        k = (a, b, w)
        v = self.cache.get(k)
        if v is None:
            v = math.log(self.p3(w, a, b))
            self.cache[k] = v
        return v

    def norm(self, w):
        return w if w in self.uni else UNK


# ---------------------------------------------------------------- shared helpers
def _split(msgs):
    """cipher tokens -> list of (kind, value): ('W', None) wildcard, ('P', v) particle, ('B', v) book."""
    out = []
    for m in msgs:
        for t in m:
            if WILD.match(t):
                out.append(("W", None))
            elif t.isdigit():
                v = int(t)
                out.append(("P" if v < 100 else "B", v))
            else:
                out.append(("W", None))  # anything unreadable is an OOV mark
    return out


def slot_order_from(tokens):
    """book-wide slot popularity order, from the ciphertext's own units-digit token counts (values >= 100)."""
    c = Counter(v % 10 for k, v in tokens if k == "B")
    if not c:
        return SLOT_ORDER_DEFAULT
    return sorted(range(10), key=lambda d: (-c[d], SLOT_ORDER_DEFAULT.index(d)))


def load_prior_words():
    words = set()
    if os.path.isdir(CODES_DIR):
        for f in os.listdir(CODES_DIR):
            if f.endswith(".tsv") and f != "stats.tsv":
                for line in open(os.path.join(CODES_DIR, f), encoding="utf-8"):
                    parts = line.rstrip("\n").split("\t")
                    if len(parts) >= 2 and parts[0].isdigit():
                        words.update(words_of(parts[1]))
        ddir = os.path.join(CODES_DIR, "decodes")
        if os.path.isdir(ddir):
            for f in os.listdir(ddir):
                txt = re.sub(r"\{\d+\}", " ", open(os.path.join(ddir, f), encoding="utf-8").read())
                words.update(words_of(txt))
    return words


def build_priors(lm, params):
    fw = _p(params, "fw", 120)
    top_content = _p(params, "top_content", 2500)
    ranked = [w for w, c in sorted(lm.freq.items(), key=lambda x: (-x[1], x[0])) if w in lm.vocab]
    function_words = ranked[:fw]
    particles = set(function_words) | set("abcdefghijklmnopqrstuvwxyz")
    content = [w for w in ranked[fw:] if len(w) > 1][:top_content]
    book = set(content) | {w for w in load_prior_words() if w in lm.vocab}
    return particles, book, ranked


# ---------------------------------------------------------------- control
def make_control(spec, seed, corpora, params):
    rng = random.Random(seed * 104729 + 17)
    hold = _p(params, "holdout", 5)
    if hold >= len(corpora):
        hold = len(corpora) - 1
    train = [c for i, c in enumerate(corpora) if i != hold]
    held = corpora[hold]
    tgt = _split(params.get("target_msgs") or [])
    n_coded = sum(1 for k, v in tgt if k != "W") or _p(params, "N", 369)
    slot_order = slot_order_from(tgt) if tgt else SLOT_ORDER_DEFAULT
    lm = get_lm(train, _p(params, "vocab_min", 3))
    ranked = [w for w, c in sorted(lm.freq.items(), key=lambda x: (-x[1], x[0])) if w in lm.vocab]
    # the letter's window in the held-out file is chosen first so the book's register counts can exclude it
    hw = words_of(held)
    lo, hi = len(hw) // 20, len(hw) * 19 // 20
    start = rng.randrange(lo, hi)
    # particle block, 99 values: the `pblock_fw` commonest training words, the 26 letters, then the next
    # words from rank `pblock_fill` on, up to 99 entries (a code of this period keeps letters somewhere: spec, Q3);
    # the target's block covers 132/369 coded tokens and its 99 commonest words alone would overshoot (~60%)
    pfw = _p(params, "pblock_fw", 30)
    pfill = _p(params, "pblock_fill", 200)
    plist = ranked[:pfw]
    plist += [c for c in "abcdefghijklmnopqrstuvwxyz" if c not in plist]
    plist += [w for w in ranked[pfill:] if w not in plist and len(w) > 1][:99 - len(plist)]
    function_words = plist[:99]
    pvals = list(range(1, 100))
    rng.shuffle(pvals)
    key = dict(zip(function_words, pvals))
    # family book: stem families in decades, members by frequency into slots by the book-wide slot order.
    # book_source=held ranks content words by their frequency in the held-out file OUTSIDE the letter's own
    # window (the code was compiled for this correspondent's register, spec: "built from the letter's own
    # register"); book_source=train ranks them by the training corpus instead.
    n_dec = _p(params, "decades", 180)
    book_forms = _p(params, "book_forms", 1800)
    if params.get("book_source", "held") == "held":
        span = 3000
        reg = Counter(hw[:max(0, start - span)] + hw[start + span:])
        freq = lambda w: (reg[w], lm.freq[w])
        content = [w for w, c in sorted(reg.items(), key=lambda x: (-x[1], x[0])) if w in lm.vocab and w not in key and len(w) > 1]
    else:
        freq = lambda w: (lm.freq[w],)
        content = [w for w in ranked if w not in key and len(w) > 1]
    fam = defaultdict(list)
    for w in content:
        fam[stem(w)].append(w)
    fam_rank = sorted(fam, key=lambda s: (tuple(-x for x in map(sum, zip(*(freq(w) for w in fam[s])))), s))
    decades = list(range(100, 100 + 10 * n_dec, 10))
    rng.shuffle(decades)
    assigned, book = set(), {}
    for dec, s in zip(decades, fam_rank[:n_dec]):
        members = sorted(fam[s], key=lambda w: (tuple(-x for x in freq(w)), w))[:10]
        for slot, w in zip(slot_order, members):
            book[w] = dec + slot
            assigned.add(w)
    taken = set(book.values())
    empty = [(slot_order.index(v % 10), v) for dec in decades for v in (dec + s for s in range(10)) if v not in taken]
    empty.sort()
    rest = (w for w in content if w not in assigned)
    for _, v in empty:
        if len(book) >= book_forms:
            break
        try:
            w = next(rest)
        except StopIteration:
            break
        book[w] = v
    key.update(book)
    # the letter: a run of held-out text long enough for n_coded coded tokens
    cipher, plain, classes, oov_words = [], [], [], 0
    coded, i, last_wild = 0, start, False
    while coded < n_coded and i < len(hw):
        w = hw[i]
        i += 1
        if w in key:
            v = key[w]
            cipher.append(str(v))
            plain.append(w)
            classes.append("P" if v < 100 else "B")
            coded += 1
            last_wild = False
        else:
            oov_words += 1
            if not last_wild:
                cipher.append("*")
                plain.append("*")
                classes.append("W")
                last_wild = True
    _LAST_CONTROL["classes"] = classes
    _LAST_CONTROL["stats"] = {"coded": coded, "distinct": len(set(cipher) - {"*"}),
                              "distinct_book": len({t for t in cipher if t.isdigit() and int(t) >= 100}),
                              "oov_words": oov_words, "wild_tokens": classes.count("W"), "book_forms": len(book),
                              "particle_tokens": classes.count("P"), "distinct_particle": len({t for t in cipher if t.isdigit() and int(t) < 100}),
                              "holdout_index": hold, "letter_start_word": start, "book_source": params.get("book_source", "held")}
    print(f"  control build: {_LAST_CONTROL['stats']}")
    return [cipher], " ".join(plain), train


# ---------------------------------------------------------------- solver
def solve(cipher_msgs, spec, seed, restarts, corpora, params):
    lm = get_lm(corpora, _p(params, "vocab_min", 3))
    particles, bookprior, ranked = build_priors(lm, params)
    toks = _split(cipher_msgs)
    n = len(toks)
    slot_order = slot_order_from(toks)
    slot_rank = {d: slot_order.index(d) for d in range(10)}
    sweeps = _p(params, "sweeps", 30)
    greedy = _p(params, "greedy", 3)
    tie_w, slot_w, dup_w, oov_pen = (_p(params, "tie_w", 0.5), _p(params, "slot_w", 0.3), _p(params, "dup_w", 2.0),
                                     _p(params, "oov_pen", 3.0))
    T0, T1 = _p(params, "T0", 1.5), _p(params, "T1", 0.25)
    max_cands = _p(params, "max_cands", 700)
    values = sorted({v for k, v in toks if k != "W"})
    occ = defaultdict(list)
    for i, (k, v) in enumerate(toks):
        if k != "W":
            occ[v].append(i)
    kind = {v: ("P" if v < 100 else "B") for v in values}
    # cribs: value -> word, held fixed in every restart and sweep (family D hook; values not in the cipher are
    # reported in info and ignored, never an error, so a round can carry cribs from an earlier control)
    fixed = {}
    for k_, w_ in (params.get("cribs") or {}).items():
        v_ = int(k_)
        if v_ in kind:
            fixed[v_] = words_of(str(w_))[0] if words_of(str(w_)) else UNK
    decade_of = {v: v // 10 for v in values if v >= 100}
    same_dec = defaultdict(list)
    for v, d in decade_of.items():
        same_dec[d].append(v)
    stem_of = {}

    def st(w):
        s = stem_of.get(w)
        if s is None:
            s = stem_of[w] = stem(w)
        return s

    plist = sorted(particles & lm.vocab, key=lambda w: (-lm.freq[w], w))
    blist = sorted(bookprior & lm.vocab, key=lambda w: (-lm.freq[w], w))
    ranked_content = [w for w in ranked[len(plist):] if len(w) > 1][:3000]

    def seq_words(assign):
        return [assign[v] if k != "W" else UNK for k, v in toks]

    def local_terms(i, ws, w):
        """LM terms touching position i when word w sits there (others from ws)."""
        a = ws[i - 2] if i >= 2 else "<s>"
        b = ws[i - 1] if i >= 1 else "<s>"
        s = lm.lp3(w, a, b)
        if i + 1 < n:
            s += lm.lp3(ws[i + 1], b, w)
            if i + 2 < n:
                s += lm.lp3(ws[i + 2], w, ws[i + 1])
        return s

    def total_score(assign):
        ws = seq_words(assign)
        s = 0.0
        for i, w in enumerate(ws):
            a = ws[i - 2] if i >= 2 else "<s>"
            b = ws[i - 1] if i >= 1 else "<s>"
            s += lm.lp3(w, a, b)
        cnt = Counter(w for w in assign.values() if w != UNK)
        s -= dup_w * sum(c - 1 for c in cnt.values() if c > 1)
        for v, w in assign.items():
            if w not in (particles if kind[v] == "P" else bookprior):
                s -= oov_pen
        for d, vs in same_dec.items():
            for x in range(len(vs)):
                for y in range(x + 1, len(vs)):
                    v1, v2 = vs[x], vs[y]
                    w1, w2 = assign[v1], assign[v2]
                    if st(w1) == st(w2) and w1 != w2:
                        s += tie_w
                    r1, r2 = slot_rank[v1 % 10], slot_rank[v2 % 10]
                    if r1 != r2 and w1 != w2:
                        f1, f2 = lm.freq[w1], lm.freq[w2]
                        if f1 != f2:
                            s += slot_w if ((r1 < r2) == (f1 > f2)) else -slot_w
        return s

    def structural(v, w, assign, wcount):
        """prior, duplicate, tie and slot terms for value v taking word w (others fixed)."""
        s = 0.0
        if w == UNK:
            return s
        if w not in (particles if kind[v] == "P" else bookprior):
            s -= oov_pen
        others = wcount.get(w, 0) - (1 if assign[v] == w else 0)
        if others > 0:
            s -= dup_w * others
        if v >= 100:
            fw_ = lm.freq[w]
            r1 = slot_rank[v % 10]
            sw = st(w)
            for v2 in same_dec[decade_of[v]]:
                if v2 == v:
                    continue
                w2 = assign[v2]
                if w2 == w or w2 == UNK:
                    continue
                if st(w2) == sw:
                    s += tie_w
                r2 = slot_rank[v2 % 10]
                if r1 != r2:
                    f2 = lm.freq[w2]
                    if fw_ != f2:
                        s += slot_w if ((r1 < r2) == (fw_ > f2)) else -slot_w
        return s

    def candidates(v, ws, assign, rng):
        cands = {assign[v]}
        prior = plist if kind[v] == "P" else blist
        if kind[v] == "P":
            cands.update(prior)
        else:
            cands.update(prior[:60])
            cands.update(rng.sample(prior, min(120, len(prior))))
            cands.update(rng.sample(ranked_content, min(40, len(ranked_content))))
        for i in occ[v][:6]:
            a = ws[i - 2] if i >= 2 else "<s>"
            b = ws[i - 1] if i >= 1 else "<s>"
            c = ws[i + 1] if i + 1 < n else "</s>"
            d = ws[i + 2] if i + 2 < n else None
            cands.update(w for w, _ in lm.succ3.get((a, b), Counter()).most_common(80))
            cands.update(w for w, _ in lm.succ2.get(b, Counter()).most_common(120))
            cands.update(w for w, _ in lm.pred2.get(c, Counter()).most_common(120))
            cands.update(w for w, _ in lm.mid.get((b, c), Counter()).most_common(80))
        cands.discard(UNK); cands.discard("<s>"); cands.discard("</s>")
        cands = sorted(w for w in cands if w in lm.uni)  # sorted: set order varies per process (hash seed)
        if len(cands) > max_cands:
            keep = set(rng.sample(cands, max_cands))
            keep.add(assign[v])
            cands = sorted(keep)
        return cands

    def init(rng):
        assign = {}
        pv = sorted((v for v in values if kind[v] == "P"), key=lambda v: -len(occ[v]))
        for r, v in enumerate(pv):  # blind frequency-rank start for the particle block
            assign[v] = plist[r] if r < len(plist) else rng.choice(plist)
        bv = [v for v in values if kind[v] == "B"]
        pool = blist[:1500] or ranked_content
        for v in bv:
            assign[v] = rng.choice(pool)
        assign.update(fixed)
        return assign

    singles = [v for v in values if len(occ[v]) == 1]
    repeated = [v for v in values if len(occ[v]) > 1]
    free = lambda vs: [v for v in vs if v not in fixed]  # anchors path: a cribbed value is never resampled
    phase1 = _p(params, "phase1", 20)

    def gibbs_sweep(order, assign, ws, wcount, T, rng):
        rng.shuffle(order)
        for v in order:
            cands = candidates(v, ws, assign, rng)
            scores = []
            for w in cands:
                s = structural(v, w, assign, wcount)
                for i in occ[v]:
                    s += local_terms(i, ws, w)
                scores.append(s)
            if T > 0:
                m = max(scores)
                weights = [math.exp((s - m) / T) for s in scores]
                w = rng.choices(cands, weights)[0]
            else:
                w = cands[max(range(len(cands)), key=scores.__getitem__)]
            wcount[assign[v]] -= 1
            wcount[w] += 1
            assign[v] = w
            for i in occ[v]:
                ws[i] = w
        if len(lm.cache) > 3_000_000:
            lm.cache.clear()

    best, best_score, best_info = None, -float("inf"), {}
    restart_keys, restart_scores = [], []
    for r in range(max(1, restarts)):
        rng = random.Random(seed * 7919 + r)
        assign = dict(params["_init"]) if params.get("_init") else init(rng)  # _init: test hook (start from a given key)
        assign.update(fixed)
        # phase 1: repeated values only; every singleton reads as an unknown content word, so the anchors
        # (particles, repeated book values) are not scored against 100-odd wrong neighbours (ARM-C1 debug: from a
        # blind start the one-phase sampler stalled 600 nats below the true key on the memorised-letter test)
        if not params.get("_init") and phase1 > 0 and repeated:
            for v in free(singles):
                assign[v] = UNK
            ws = seq_words(assign)
            wcount = Counter(assign.values())
            for sw in range(phase1):
                T = T0 * (T1 / T0) ** (sw / max(1, phase1 - 1))
                gibbs_sweep(free(repeated), assign, ws, wcount, T, rng)
            for v in free(singles):  # greedy fill of the singletons given the anchors
                assign[v] = blist[0] if blist else ranked_content[0]
            ws = seq_words(assign)
            wcount = Counter(assign.values())
            gibbs_sweep(free(singles), assign, ws, wcount, 0.0, rng)
        order = free(values)
        total = sweeps + greedy
        for sw in range(total):
            T = T0 * (T1 / T0) ** (sw / max(1, sweeps - 1)) if sw < sweeps else 0.0
            ws = seq_words(assign)
            wcount = Counter(assign.values())
            gibbs_sweep(order, assign, ws, wcount, T, rng)
        sc = total_score(assign)
        print(f"    restart {r}: score {sc:.1f}")
        restart_keys.append({str(v): w for v, w in assign.items()})
        restart_scores.append(round(sc, 2))
        if sc > best_score:
            best, best_score = dict(assign), sc
            best_info = {"restart": r}
    dec = " ".join(best[v] if k != "W" else "*" for k, v in toks)
    info = {"family": "nomenclator", "seed": seed, "restarts": restarts, "sweeps": sweeps, "greedy": greedy,
            "T0": T0, "T1": T1, "tie_w": tie_w, "slot_w": slot_w, "dup_w": dup_w, "oov_pen": oov_pen,
            "vocab": lm.V, "particle_prior": len(plist), "book_prior": len(blist), "values": len(values),
            "singletons": len(singles), "phase1": phase1,
            "slot_order": slot_order, "best_restart": best_info.get("restart"), "score_per_token": best_score / n,
            "cribs": {str(v): w for v, w in fixed.items()}, "restart_keys": restart_keys,
            "restart_scores": restart_scores}
    return dec, best_score, info


def score_recovery(plain, truth):
    p, t = plain.split(), truth.split()
    classes = _LAST_CONTROL.get("classes")
    hits = Counter()
    tot = Counter()
    for i, (a, b) in enumerate(zip(p, t)):
        if b == "*":
            continue
        k = classes[i] if classes and len(classes) == len(t) else "B"
        tot[k] += 1
        hits[k] += (a == b)
    n = sum(tot.values())
    if n == 0:
        return 0.0
    if classes:
        per = " ".join(f"{k}={hits[k]}/{tot[k]} ({hits[k] / tot[k]:.3f})" for k in ("P", "B") if tot[k])
        print(f"  recovery by class: {per}; blended {sum(hits.values())}/{n}")
    return sum(hits.values()) / n


def split_decode(dec, msgs):
    ws, out, pos = dec.split(), [], 0
    for m in msgs:
        out.append(" ".join(ws[pos:pos + len(m)]))
        pos += len(m)
    return out


# ---------------------------------------------------------------- slot grammar (H27, 28 Sept 2026)
# `--param slot_grammar=1`: the book above 100 is one ROOT lemma per decade with its inflected forms at fixed
# slots (0 root, 1 plural/past, slots 2-9 one suffix class each, the class->slot map fixed per book and given to
# the solver through params["slot_map"], the most favourable case). The solver's unknowns are then the particle
# words and one root per occupied decade (campaign step H27 of ciphers/armstrong-madison-1808: a power test of
# the crib loop on this design before any further crib round on the target).
GRAMMAR_CLASSES = ["ing", "er", "ly", "ion", "ment", "ness", "est", "able"]  # slots 2-9, per-book order
VOWELS = set("aeiou")


def inflect(root, cls):
    """surface form of root under suffix class cls ('' root, 's', 'ed', or one of GRAMMAR_CLASSES)."""
    if cls == "" or not root:
        return root
    e = root.endswith("e")
    cy = len(root) > 2 and root.endswith("y") and root[-2] not in VOWELS
    if cls == "s":
        if root.endswith(("s", "x", "z", "ch", "sh")):
            return root + "es"
        return root[:-1] + "ies" if cy else root + "s"
    if cls == "ed":
        return root + "d" if e else (root[:-1] + "ied" if cy else root + "ed")
    if cls == "ing":
        return root[:-1] + "ing" if e and not root.endswith("ee") else root + "ing"
    if cls == "er":
        return root + "r" if e else (root[:-1] + "ier" if cy else root + "er")
    if cls == "ly":
        if root.endswith("le"):
            return root[:-1] + "y"
        return root[:-1] + "ily" if cy else root + "ly"
    if cls == "ion":
        return root[:-1] + "ion" if e else root + "ion"
    if cls == "ment":
        return root + "ment"
    if cls == "ness":
        return root[:-1] + "iness" if cy else root + "ness"
    if cls == "est":
        return root + "st" if e else (root[:-1] + "iest" if cy else root + "est")
    if cls == "able":
        return root[:-1] + "able" if e else root + "able"
    return root + cls


def deinflect(form, cls):
    """every root r with inflect(r, cls) == form (0, 1 or 2 candidates)."""
    if cls == "":
        return [form]
    outs = set()
    ends = {"s": ["s", "es", "ies"], "ed": ["d", "ed", "ied"], "ing": ["ing"], "er": ["r", "er", "ier"],
            "ly": ["ly", "ily", "y"], "ion": ["ion"], "ment": ["ment"], "ness": ["ness", "iness"],
            "est": ["st", "est", "iest"], "able": ["able"]}.get(cls, [cls])
    for suf in ends:
        if form.endswith(suf) and len(form) > len(suf) + 1:
            base = form[:-len(suf)]
            for r in (base, base + "e", base + "y", base + "le" if suf == "y" else None):
                if r and len(r) >= 2 and inflect(r, cls) == form:
                    outs.add(r)
    return sorted(outs)


def make_slot_map(rng):
    order = list(GRAMMAR_CLASSES)
    rng.shuffle(order)
    return {0: "", 1: "s|ed", **{s: c for s, c in zip(range(2, 10), order)}}


def _slot_map_param(params):
    m = params.get("slot_map")
    if isinstance(m, str):
        m = dict(kv.split(":") for kv in m.split(";") if kv)
    return {int(k): v for k, v in m.items()}


def grammar_book(content, freq, rng, n_dec, slot_map):
    """content words (frequency order) -> families {root: {slot: form}} under the slot grammar; decades assigned
    to the n_dec most frequent families. A form that is another word's inflection joins that root's family; a
    root's slot 1 holds its commoner of plural/past, the other form becomes a root of its own."""
    cset = set(content)
    cls_slot = {c: s for s, c in slot_map.items() if s >= 2}
    fam, member_of = {}, {}
    for w in content:
        if w in member_of:
            continue
        best = None
        for cls in ["s", "ed"] + GRAMMAR_CLASSES:
            for r in deinflect(w, cls):
                if r in cset and r != w and (best is None or freq(r) > freq(best[0])):
                    best = (r, cls)
        if best is None:
            fam.setdefault(w, {0: w})
            member_of[w] = w
            continue
        r, cls = best
        fam.setdefault(r, {0: r})
        member_of.setdefault(r, r)
        slot = 1 if cls in ("s", "ed") else cls_slot[cls]
        if slot in fam[r] and fam[r][slot] != w:
            fam.setdefault(w, {0: w})  # slot taken by the commoner form: this form is its own root
            member_of[w] = w
        else:
            fam[r][slot] = w
            member_of[w] = r
    order = sorted(fam, key=lambda r: (-sum(freq(f) for f in fam[r].values()), r))[:n_dec]
    decades = list(range(100, 100 + 10 * n_dec, 10))
    rng.shuffle(decades)
    book, roots = {}, {}
    for dec, r in zip(decades, order):
        roots[dec // 10] = r
        for slot, f in fam[r].items():
            book[f] = dec + slot
    return book, roots


def make_control_grammar(spec, seed, corpora, params):
    rng = random.Random(seed * 104729 + 17)
    hold = _p(params, "holdout", 5)
    if hold >= len(corpora):
        hold = len(corpora) - 1
    train = [c for i, c in enumerate(corpora) if i != hold]
    held = corpora[hold]
    tgt = _split(params.get("target_msgs") or [])
    n_coded = sum(1 for k, v in tgt if k != "W") or _p(params, "N", 369)
    lm = get_lm(train, _p(params, "vocab_min", 3))
    ranked = [w for w, c in sorted(lm.freq.items(), key=lambda x: (-x[1], x[0])) if w in lm.vocab]
    hw = words_of(held)
    lo, hi = len(hw) // 20, len(hw) * 19 // 20
    start = rng.randrange(lo, hi)
    pfw, pfill = _p(params, "pblock_fw", 30), _p(params, "pblock_fill", 200)
    plist = ranked[:pfw]
    plist += [c for c in "abcdefghijklmnopqrstuvwxyz" if c not in plist]
    plist += [w for w in ranked[pfill:] if w not in plist and len(w) > 1][:99 - len(plist)]
    pvals = list(range(1, 100))
    rng.shuffle(pvals)
    key = dict(zip(plist[:99], pvals))
    n_dec = _p(params, "decades", 180)
    span = 3000
    reg = Counter(hw[:max(0, start - span)] + hw[start + span:])
    freq = lambda w: reg[w] + lm.freq[w] / 1e6
    content = [w for w, c in sorted(reg.items(), key=lambda x: (-x[1], x[0])) if w in lm.vocab and w not in key and len(w) > 2]
    slot_map = make_slot_map(rng)
    book, roots = grammar_book(content, freq, rng, n_dec, slot_map)
    key.update(book)
    cipher, plain, classes, oov_words = [], [], [], 0
    coded, i, last_wild = 0, start, False
    while coded < n_coded and i < len(hw):
        w = hw[i]
        i += 1
        if w in key:
            v = key[w]
            cipher.append(str(v)); plain.append(w); classes.append("P" if v < 100 else "B")
            coded += 1; last_wild = False
        else:
            oov_words += 1
            if not last_wild:
                cipher.append("*"); plain.append("*"); classes.append("W"); last_wild = True
    used_dec = {int(t) // 10 for t in cipher if t.isdigit() and int(t) >= 100}
    _LAST_CONTROL["classes"] = classes
    _LAST_CONTROL["roots"] = {d: roots[d] for d in used_dec}
    _LAST_CONTROL["slot_map"] = slot_map
    _LAST_CONTROL["stats"] = {"coded": coded, "distinct": len(set(cipher) - {"*"}),
                              "distinct_book": len({t for t in cipher if t.isdigit() and int(t) >= 100}),
                              "decades_used": len(used_dec), "book_forms": len(book), "book_roots": len(roots),
                              "oov_words": oov_words, "wild_tokens": classes.count("W"),
                              "particle_tokens": classes.count("P"),
                              "distinct_particle": len({t for t in cipher if t.isdigit() and int(t) < 100}),
                              "holdout_index": hold, "letter_start_word": start, "slot_grammar": 1}
    print(f"  control build (slot grammar): {_LAST_CONTROL['stats']}")
    return [cipher], " ".join(plain), train


def solve_grammar(cipher_msgs, spec, seed, restarts, corpora, params):
    """Gibbs anneal over particle words and one root per decade; forms follow the given slot map."""
    lm = get_lm(corpora, _p(params, "vocab_min", 3))
    particles, bookprior, ranked = build_priors(lm, params)
    slot_map = _slot_map_param(params)
    toks = _split(cipher_msgs)
    n = len(toks)
    sweeps, greedy = _p(params, "sweeps", 30), _p(params, "greedy", 3)
    dup_w, oov_pen = _p(params, "dup_w", 2.0), _p(params, "oov_pen", 3.0)
    T0, T1 = _p(params, "T0", 1.5), _p(params, "T1", 0.25)
    max_cands = _p(params, "max_cands", 700)
    values = sorted({v for k, v in toks if k != "W"})
    occ = defaultdict(list)
    for i, (k, v) in enumerate(toks):
        if k != "W":
            occ[v].append(i)
    pvals = [v for v in values if v < 100]
    dec_vals = defaultdict(list)
    for v in values:
        if v >= 100:
            dec_vals[v // 10].append(v)
    decs = sorted(dec_vals)
    units = [("P", v) for v in pvals] + [("D", d) for d in decs]
    cls_of = {v: slot_map.get(v % 10, "") for v in values if v >= 100}

    def forms_of(root, d):
        out = {}
        for v in dec_vals[d]:
            c = cls_of[v]
            if c == "s|ed":
                fs, fe = inflect(root, "s"), inflect(root, "ed")
                out[v] = fs if lm.freq.get(fs, 0) >= lm.freq.get(fe, 0) else fe
            else:
                out[v] = inflect(root, c)
        return out

    fixed_p, fixed_r = {}, {}
    for k_, w_ in (params.get("cribs") or {}).items():
        v_ = int(k_)
        if v_ not in occ:
            continue
        w = words_of(str(w_))[0] if words_of(str(w_)) else UNK
        if v_ < 100:
            fixed_p[v_] = w
        else:
            c = cls_of[v_]
            cands = []
            for cc in (["s", "ed"] if c == "s|ed" else [c]):
                cands += deinflect(w, cc)
            fixed_r[v_ // 10] = max(cands, key=lambda r: lm.freq.get(r, 0)) if cands else w
    plist = sorted(particles & lm.vocab, key=lambda w: (-lm.freq[w], w))
    blist = sorted(bookprior & lm.vocab, key=lambda w: (-lm.freq[w], w))
    ranked_content = [w for w in ranked[len(plist):] if len(w) > 2][:3000]
    rootprior = [w for w in blist if len(w) > 2]

    def window_score(ws, positions):
        s = 0.0
        for j in positions:
            a = ws[j - 2] if j >= 2 else "<s>"
            b = ws[j - 1] if j >= 1 else "<s>"
            s += lm.lp3(ws[j], a, b)
        return s

    def affected(vs):
        out = set()
        for v in vs:
            for i in occ[v]:
                out.update(j for j in (i, i + 1, i + 2) if j < n)
        return sorted(out)

    def total_score(assign, roots):
        ws = [assign[v] if k != "W" else UNK for k, v in toks]
        s = window_score(ws, range(n))
        cnt = Counter(w for w in assign.values() if w != UNK)
        s -= dup_w * sum(c - 1 for c in cnt.values() if c > 1)
        for v in pvals:
            if assign[v] not in particles:
                s -= oov_pen
        for d, r in roots.items():
            if r != UNK and r not in bookprior:
                s -= oov_pen
            for v in dec_vals[d]:
                if assign[v] != UNK and assign[v] not in lm.uni:
                    s -= oov_pen
        return s

    def set_unit(u, x, assign, roots, ws, wcount):
        kind, key_ = u
        if kind == "P":
            wcount[assign[key_]] -= 1
            assign[key_] = x
            wcount[x] += 1
            for i in occ[key_]:
                ws[i] = x
        else:
            roots[key_] = x
            fm = forms_of(x, key_) if x != UNK else {v: UNK for v in dec_vals[key_]}
            for v, f in fm.items():
                wcount[assign[v]] -= 1
                assign[v] = lm.norm(f) if f != UNK else UNK
                wcount[assign[v]] += 1
                for i in occ[v]:
                    ws[i] = assign[v]

    def cand_particles(v, ws, rng):
        cands = {ws[occ[v][0]]}
        cands.update(plist)
        for i in occ[v][:6]:
            a = ws[i - 2] if i >= 2 else "<s>"
            b = ws[i - 1] if i >= 1 else "<s>"
            c = ws[i + 1] if i + 1 < n else "</s>"
            cands.update(w for w, _ in lm.succ3.get((a, b), Counter()).most_common(80))
            cands.update(w for w, _ in lm.succ2.get(b, Counter()).most_common(120))
            cands.update(w for w, _ in lm.pred2.get(c, Counter()).most_common(120))
            cands.update(w for w, _ in lm.mid.get((b, c), Counter()).most_common(80))
        cands.discard(UNK); cands.discard("<s>"); cands.discard("</s>")
        return sorted(w for w in cands if w in lm.uni)

    def cand_roots(d, roots, ws, rng):
        cands = {roots[d]} if roots[d] != UNK else set()
        cands.update(rootprior[:60])
        cands.update(rng.sample(rootprior, min(120, len(rootprior))))
        cands.update(rng.sample(ranked_content, min(40, len(ranked_content))))
        for v in dec_vals[d]:
            c = cls_of[v]
            classes = ["s", "ed"] if c == "s|ed" else [c]
            sugg = set()
            for i in occ[v][:4]:
                a = ws[i - 2] if i >= 2 else "<s>"
                b = ws[i - 1] if i >= 1 else "<s>"
                cn = ws[i + 1] if i + 1 < n else "</s>"
                sugg.update(w for w, _ in lm.succ3.get((a, b), Counter()).most_common(60))
                sugg.update(w for w, _ in lm.succ2.get(b, Counter()).most_common(100))
                sugg.update(w for w, _ in lm.pred2.get(cn, Counter()).most_common(100))
                sugg.update(w for w, _ in lm.mid.get((b, cn), Counter()).most_common(60))
            for w in sugg:
                if w in (UNK, "<s>", "</s>") or len(w) < 3:
                    continue
                for cc in classes:
                    cands.update(r for r in deinflect(w, cc) if len(r) > 2)
        cands = sorted(cands)
        if len(cands) > max_cands:
            keep = set(rng.sample(cands, max_cands))
            if roots[d] != UNK:
                keep.add(roots[d])
            cands = sorted(keep)
        return cands

    def unit_score(u, x, assign, roots, ws, wcount):
        kind, key_ = u
        if kind == "P":
            v = key_
            old = assign[v]
            s = 0.0 if x in particles else -oov_pen
            others = wcount.get(x, 0) - (1 if old == x else 0)
            if others > 0:
                s -= dup_w * others
            pos = affected([v])
            for i in occ[v]:
                ws[i] = x
            s += window_score(ws, pos)
            for i in occ[v]:
                ws[i] = old
            return s
        d = key_
        s = 0.0 if x in bookprior else -oov_pen
        fm = forms_of(x, d)
        olds = {v: assign[v] for v in dec_vals[d]}
        seen = Counter()
        for v, f in fm.items():
            fn = lm.norm(f)
            if fn == UNK:
                s -= oov_pen
            others = wcount.get(fn, 0) - (1 if olds[v] == fn else 0) + seen[fn]
            if others > 0:
                s -= dup_w * others
            seen[fn] += 1
            for i in occ[v]:
                ws[i] = fn
        s += window_score(ws, affected(dec_vals[d]))
        for v, o in olds.items():
            for i in occ[v]:
                ws[i] = o
        return s

    def gibbs_sweep(order, assign, roots, ws, wcount, T, rng):
        rng.shuffle(order)
        for u in order:
            cands = cand_particles(u[1], ws, rng) if u[0] == "P" else cand_roots(u[1], roots, ws, rng)
            if not cands:
                continue
            scores = [unit_score(u, x, assign, roots, ws, wcount) for x in cands]
            if T > 0:
                m = max(scores)
                x = rng.choices(cands, [math.exp((s - m) / T) for s in scores])[0]
            else:
                x = cands[max(range(len(cands)), key=scores.__getitem__)]
            set_unit(u, x, assign, roots, ws, wcount)
        if len(lm.cache) > 3_000_000:
            lm.cache.clear()

    is_fixed = lambda u: (u[0] == "P" and u[1] in fixed_p) or (u[0] == "D" and u[1] in fixed_r)
    free = [u for u in units if not is_fixed(u)]
    rep_u = [u for u in free if (u[0] == "P" and len(occ[u[1]]) > 1) or (u[0] == "D" and sum(len(occ[v]) for v in dec_vals[u[1]]) > 1)]
    sing_u = [u for u in free if u not in rep_u]
    phase1 = _p(params, "phase1", 20)
    best, best_roots, best_score, best_info = None, None, -float("inf"), {}
    restart_keys, restart_scores, restart_roots = [], [], []
    for r in range(max(1, restarts)):
        rng = random.Random(seed * 7919 + r)
        assign, roots = {}, {}
        ws = [UNK] * n
        wcount = Counter()
        pv = sorted(pvals, key=lambda v: -len(occ[v]))
        for rk, v in enumerate(pv):
            assign[v] = plist[rk] if rk < len(plist) else rng.choice(plist)
        for d in decs:
            roots[d] = UNK
            for v in dec_vals[d]:
                assign[v] = UNK
        for v in pvals:
            for i in occ[v]:
                ws[i] = assign[v]
        wcount = Counter(assign.values())
        for v, w in fixed_p.items():
            set_unit(("P", v), w, assign, roots, ws, wcount)
        for d, rt in fixed_r.items():
            set_unit(("D", d), rt, assign, roots, ws, wcount)
        for d in decs:
            if roots[d] == UNK and d not in fixed_r and ("D", d) not in rep_u:
                pass
        if phase1 > 0 and rep_u:
            for u in rep_u:
                if u[0] == "D":
                    set_unit(u, rng.choice(rootprior[:1500]), assign, roots, ws, wcount)
            for sw in range(phase1):
                T = T0 * (T1 / T0) ** (sw / max(1, phase1 - 1))
                gibbs_sweep(list(rep_u), assign, roots, ws, wcount, T, rng)
        for u in sing_u:
            if u[0] == "D":
                set_unit(u, rootprior[0], assign, roots, ws, wcount)
        gibbs_sweep(list(sing_u), assign, roots, ws, wcount, 0.0, rng)
        for sw in range(sweeps + greedy):
            T = T0 * (T1 / T0) ** (sw / max(1, sweeps - 1)) if sw < sweeps else 0.0
            gibbs_sweep(list(free), assign, roots, ws, wcount, T, rng)
        sc = total_score(assign, roots)
        print(f"    restart {r}: score {sc:.1f}")
        restart_keys.append({str(v): w for v, w in assign.items()})
        restart_roots.append({str(d): w for d, w in roots.items()})
        restart_scores.append(round(sc, 2))
        if sc > best_score:
            best, best_roots, best_score, best_info = dict(assign), dict(roots), sc, {"restart": r}
    dec = " ".join(best[v] if k != "W" else "*" for k, v in toks)
    info = {"family": "nomenclator", "slot_grammar": 1, "seed": seed, "restarts": restarts, "sweeps": sweeps,
            "greedy": greedy, "T0": T0, "T1": T1, "dup_w": dup_w, "oov_pen": oov_pen, "vocab": lm.V,
            "particle_prior": len(plist), "book_prior": len(blist), "values": len(values), "decades": len(decs),
            "singletons": sum(1 for v in values if len(occ[v]) == 1), "phase1": phase1, "slot_map": slot_map,
            "best_restart": best_info.get("restart"), "score_per_token": best_score / n,
            "cribs": {**{str(v): w for v, w in fixed_p.items()}, **{str(d * 10): r for d, r in fixed_r.items()}},
            "roots": {str(d): w for d, w in best_roots.items()}, "restart_roots": restart_roots,
            "restart_keys": restart_keys, "restart_scores": restart_scores}
    return dec, best_score, info


# ---------------------------------------------------------------- vocabulary-prior, one-part-by-decade (H73)
# H73 (3 Oct 2026, ciphers/armstrong-madison-1808/h73/PREREGISTRATION.md): Tomokiyo's "learn the vocabulary of a
# sibling code", taken as an ORDER constraint. `vocab_order=1` assumes the book is one-part at decade level: the
# target's decades, sorted by value, map in the same order onto one sibling maker's alphabetical whole-word list
# (`prior=WE028|THE972`), and every value of a decade takes a word from that decade's window of the list
# (`win` entries from the decade's base position). Moves: a per-value move inside the window and a whole-decade
# block shift, both keeping every position of decade k below every position of decade k+1; particles are a Gibbs
# move over the siblings' short-word entries that are also en18 function words. Score: the same word-trigram LM,
# the duplicate penalty and the slot-order term. The control (`make_control_vocab`) re-encodes Bourdeau's
# decodes of Armstrong's 15 and 22 Feb 1808 letters (words rebuilt from syllable fragments by `rebuild_words`)
# into a synthetic code whose book is the OTHER sibling's list (`book=THE972|WE028`), alphabetical blocks of
# `block` (6) entries per decade, members ranked by en18 frequency onto the target's slot order, decades on a
# seed-dependent increasing subset of 10..199. `thin` (0-1) drops prior entries that are true book words until
# that token coverage remains (the realistic-overlap control). Two-part (vocabulary only) is NOT offered: it is
# ARM-C1's soft prior with one knob turned (prereg, same-instrument check).
TABLES = {"WE028": "WE028.tsv", "THE972": "THE972_bourdeau.tsv"}
CONTROL_LETTERS = ["armstrong_1808-02-15.txt", "armstrong_1808-02-22.txt"]


def table_words(name, vocab):
    """alphabetical whole-word entries of a sibling table that the LM knows (len >= 2)."""
    out = set()
    for line in open(os.path.join(CODES_DIR, TABLES[name]), encoding="utf-8"):
        parts = line.rstrip("\n").split("\t")
        if len(parts) >= 2 and parts[0].isdigit():
            w = parts[1].strip().lower()
            if re.fullmatch(r"[a-z]+", w) and len(w) >= 2 and w in vocab:
                out.add(w)
    return sorted(out)


def rebuild_words(text, vocab):
    """Bourdeau decode -> words. `{nnnn}` (unread) -> '*'; adjacent fragments are joined when the joined string is a
    vocabulary word and not every fragment is one already (DP over each run, longest-known-word first)."""
    text = re.sub(r"^==.*==\s*$", " ", text, flags=re.M)
    raw = re.findall(r"\{\d+\}|[A-Za-z]+", text.replace("?", "").replace("*", ""))
    out, run = [], []

    def flush():
        n = len(run)
        best = [(0, None)] * (n + 1)
        best[0] = (0, [])
        for i in range(1, n + 1):
            cands = []
            for j in range(max(0, i - 6), i):
                s = "".join(run[j:i])
                if best[j][1] is None:
                    continue
                if i - j == 1:
                    sc = 1.0 if s in vocab else 0.0
                elif s in vocab and not all(f in vocab for f in run[j:i]):
                    sc = 1.0 + 0.5 * (i - j)
                else:
                    continue
                cands.append((best[j][0] + sc, best[j][1] + [s]))
            best[i] = max(cands, key=lambda x: x[0])
        out.extend(best[n][1])
        run.clear()

    for t in raw:
        if t.startswith("{"):
            flush()
            out.append("*")
        else:
            run.append(t.lower())
    flush()
    return out


def make_control_vocab(spec, seed, corpora, params):
    rng = random.Random(seed * 104729 + 73)
    lm = get_lm(corpora, _p(params, "vocab_min", 3))
    ranked = [w for w, c in sorted(lm.freq.items(), key=lambda x: (-x[1], x[0])) if w in lm.vocab]
    tgt = _split(params.get("target_msgs") or [])
    n_coded = sum(1 for k, v in tgt if k != "W") or _p(params, "N", 369)
    slot_order = slot_order_from(tgt) if tgt else SLOT_ORDER_DEFAULT
    words = []
    for f in params.get("letters") or CONTROL_LETTERS:
        words += rebuild_words(open(os.path.join(CODES_DIR, "decodes", f), encoding="utf-8").read(), lm.vocab)
    plist = ranked[:30] + [c for c in "abcdefghijklmnopqrstuvwxyz" if c not in ranked[:30]]
    plist += [w for w in ranked[200:] if w not in plist and len(w) > 1][:99 - len(plist)]
    pvals = list(range(1, 100))
    rng.shuffle(pvals)
    key = dict(zip(plist[:99], pvals))
    blist = [w for w in table_words(params.get("book", "THE972"), lm.vocab) if w not in key]
    bsz = _p(params, "block", 6)
    blocks = [blist[i:i + bsz] for i in range(0, len(blist), bsz)]
    decs = sorted(rng.sample(range(10, 200), min(len(blocks), 190)))
    for d, blk in zip(decs, blocks):
        for slot, w in zip(slot_order, sorted(blk, key=lambda w: (-lm.freq[w], w))):
            key[w] = 10 * d + slot
    cipher, plain, classes, last_wild, coded, oov = [], [], [], False, 0, 0
    for w in words:
        if coded >= n_coded:
            break
        if w in key:
            v = key[w]
            cipher.append(str(v)); plain.append(w); classes.append("P" if v < 100 else "B")
            coded += 1; last_wild = False
        else:
            oov += 1
            if not last_wild:
                cipher.append("*"); plain.append("*"); classes.append("W"); last_wild = True
    _LAST_CONTROL["classes"] = classes
    btoks = [int(t) for t in cipher if t.isdigit() and int(t) >= 100]
    bwords = [w for w, k in zip(plain, classes) if k == "B"]
    cnt = Counter(t for t in cipher if t != "*")
    prior = table_words(params.get("prior", "WE028"), lm.vocab)
    pset = set(prior)
    _LAST_CONTROL["stats"] = {
        "coded": coded, "distinct": len(cnt), "singletons": sum(1 for c in cnt.values() if c == 1),
        "particle_tokens": classes.count("P"), "book_tokens": len(btoks), "distinct_book": len(set(btoks)),
        "oov_words": oov, "wild_tokens": classes.count("W"), "book_list": len(blist), "blocks": len(blocks),
        "slot0_share": round(sum(1 for v in btoks if v % 10 == slot_order[0]) / max(1, len(btoks)), 3),
        "prior_list": len(prior), "book_list_in_prior": round(len(pset & set(blist)) / max(1, len(blist)), 3),
        "book_token_coverage": round(sum(1 for w in bwords if w in pset) / max(1, len(bwords)), 3),
        "plain_words": len(words)}
    print(f"  control build: {_LAST_CONTROL['stats']}")
    return [cipher], " ".join(plain), corpora


def solve_vocab(cipher_msgs, spec, seed, restarts, corpora, params):
    lm = get_lm(corpora, _p(params, "vocab_min", 3))
    toks = _split(cipher_msgs)
    n = len(toks)
    prior = table_words(params.get("prior", "WE028"), lm.vocab)
    thin = float(params.get("thin", 0) or 0)
    if thin and params.get("_truth_book"):  # realistic-overlap control only: drop true book words from the prior
        rng0 = random.Random(seed * 31 + 7)
        tb = [w for w in params["_truth_book"] if w in set(prior)]
        tw = Counter(params["_truth_book"])
        cov_all = sum(tw.values())
        drop, have = set(), sum(tw[w] for w in set(tb))
        for w in sorted(set(tb), key=lambda x: rng0.random()):
            if have / cov_all <= thin:
                break
            drop.add(w); have -= tw[w]
        prior = [w for w in prior if w not in drop]
    fwset = set(sorted(lm.vocab, key=lambda w: -lm.freq[w])[:_p(params, "fw", 120)]) | set("abcdefghijklmnopqrstuvwxyz")
    sib = set()
    for nm_ in TABLES:
        sib.update(table_words(nm_, lm.vocab))
    plist = sorted((fwset & sib) | set("abcdefghijklmnopqrstuvwxyz"), key=lambda w: (-lm.freq[w], w))
    P = [w for w in prior if w not in plist] if params.get("drop_particles_from_book", 1) else prior
    slot_order = slot_order_from(toks)
    slot_rank = {d: slot_order.index(d) for d in range(10)}
    bsz = _p(params, "block", 6)
    book_est = int(params.get("book_size") or 0) or bsz * len({v // 10 for k, v in toks if k == "B"})
    win = max(bsz, int(round(2 * bsz * len(P) / max(1, book_est))))
    sweeps, greedy = _p(params, "sweeps", 30), _p(params, "greedy", 3)
    T0, T1, dup_w, slot_w = _p(params, "T0", 1.5), _p(params, "T1", 0.25), _p(params, "dup_w", 2.0), _p(params, "slot_w", 0.3)
    occ = defaultdict(list)
    for i, (k, v) in enumerate(toks):
        if k != "W":
            occ[v].append(i)
    pvals = sorted(v for v in occ if v < 100)
    decs = sorted({v // 10 for v in occ if v >= 100})
    members = {d: sorted(v for v in occ if v >= 100 and v // 10 == d) for d in decs}
    K = len(decs)

    def lmsum(ws, idx):
        s = 0.0
        for i in idx:
            a = ws[i - 2] if i >= 2 else "<s>"
            b = ws[i - 1] if i >= 1 else "<s>"
            s += lm.lp3(ws[i], a, b)
        return s

    def touched(vals):
        idx = set()
        for v in vals:
            for i in occ[v]:
                idx.update(j for j in (i, i + 1, i + 2) if j < n)
        return sorted(idx)

    def slot_term(d, pos):
        s, ms = 0.0, members[d]
        for x in range(len(ms)):
            for y in range(x + 1, len(ms)):
                r1, r2 = slot_rank[ms[x] % 10], slot_rank[ms[y] % 10]
                f1, f2 = lm.freq[P[pos[ms[x]]]], lm.freq[P[pos[ms[y]]]]
                if r1 != r2 and f1 != f2:
                    s += slot_w if ((r1 < r2) == (f1 > f2)) else -slot_w
        return s

    def word_of(v, pos, pw):
        return pw[v] if v < 100 else P[pos[v]]

    def dup_pen(wc):
        return -dup_w * sum(c - 1 for c in wc.values() if c > 1)

    best = (None, -float("inf"), None, None)
    rkeys, rscores = [], []
    for r in range(max(1, restarts)):
        rng = random.Random(seed * 7919 + r + 73)
        pw = {}
        for i_, v in enumerate(sorted(pvals, key=lambda v: -len(occ[v]))):
            pw[v] = plist[i_] if i_ < len(plist) else rng.choice(plist)
        pos, base = {}, {}
        span = max(1, len(P) - win)
        for k, d in enumerate(decs):
            base[d] = int(round((k + 0.5) / K * span))
            offs = rng.sample(range(win), min(win, len(members[d])))
            for v, o in zip(members[d], offs):
                pos[v] = min(len(P) - 1, base[d] + o)
        # repair to strict decade order
        last = -1
        for d in decs:
            for v in sorted(members[d], key=lambda v: pos[v]):
                if pos[v] <= last:
                    pos[v] = last + 1
                last = max(last, pos[v])
        for v in pos:
            pos[v] = min(pos[v], len(P) - 1)
        ws = [UNK if k == "W" else word_of(v, pos, pw) for k, v in toks]
        wc = Counter(word_of(v, pos, pw) for v in occ)

        def bounds(k):
            lo = max((pos[v] for v in members[decs[k - 1]]), default=-1) if k > 0 else -1
            hi = min((pos[v] for v in members[decs[k + 1]]), default=len(P)) if k + 1 < K else len(P)
            return lo, hi

        def pick(cands, scores, T):
            if T > 0:
                m = max(scores)
                return rng.choices(range(len(cands)), [math.exp((s - m) / T) for s in scores])[0]
            return max(range(len(cands)), key=scores.__getitem__)

        def set_word(v, w):
            wc[ws[occ[v][0]]] -= 1
            wc[w] += 1
            for i in occ[v]:
                ws[i] = w

        total = sweeps + greedy
        for sw in range(total):
            T = T0 * (T1 / T0) ** (sw / max(1, sweeps - 1)) if sw < sweeps else 0.0
            # particles
            order = list(pvals); rng.shuffle(order)
            for v in order:
                idx = touched([v]); cur = ws[occ[v][0]]
                cands, scores = [], []
                for w in plist:
                    set_word(v, w)
                    cands.append(w); scores.append(lmsum(ws, idx) - dup_w * max(0, wc[w] - 1))
                set_word(v, cands[pick(cands, scores, T)]); pw[v] = ws[occ[v][0]]
                _ = cur
            # decades: block shift, then per-value moves
            korder = list(range(K)); rng.shuffle(korder)
            for k in korder:
                d = decs[k]; ms = members[d]
                lo, hi = bounds(k)
                pmin, pmax = min(pos[v] for v in ms), max(pos[v] for v in ms)
                deltas = [x for x in range(lo + 1 - pmin, hi - pmax) if abs(x) <= win]
                if len(deltas) > 1:
                    idx = touched(ms); old = {v: pos[v] for v in ms}
                    scores = []
                    for x in deltas:
                        for v in ms:
                            pos[v] = old[v] + x; set_word(v, P[pos[v]])
                        scores.append(lmsum(ws, idx) + slot_term(d, pos) + dup_pen(wc))
                    x = deltas[pick(deltas, scores, T)]
                    for v in ms:
                        pos[v] = old[v] + x; set_word(v, P[pos[v]])
                for v in rng.sample(ms, len(ms)):
                    others = [pos[u] for u in ms if u != v]
                    lo2, hi2 = bounds(k)
                    a_ = max(lo2 + 1, (max(others) - win + 1) if others else lo2 + 1)
                    b_ = min(hi2 - 1, (min(others) + win - 1) if others else hi2 - 1)
                    cands = [p for p in range(max(0, a_), min(len(P) - 1, b_) + 1) if p not in others]
                    if len(cands) < 2:
                        continue
                    idx = touched([v]); scores = []
                    for p in cands:
                        pos[v] = p; set_word(v, P[p])
                        scores.append(lmsum(ws, idx) + slot_term(d, pos) + dup_pen(wc))
                    p = cands[pick(cands, scores, T)]
                    pos[v] = p; set_word(v, P[p])
            if len(lm.cache) > 3_000_000:
                lm.cache.clear()
        sc = lmsum(ws, range(n)) + dup_pen(wc) + sum(slot_term(d, pos) for d in decs)
        print(f"    restart {r}: score {sc:.1f}")
        key = {str(v): word_of(v, pos, pw) for v in occ}
        rkeys.append(key); rscores.append(round(sc, 2))
        if sc > best[1]:
            best = (key, sc, r, dict(pos))
    key = best[0]
    dec = " ".join(key[str(v)] if k != "W" else "*" for k, v in toks)
    info = {"family": "nomenclator", "mode": "vocab_order", "prior": params.get("prior", "WE028"), "prior_list": len(P),
            "particle_prior": len(plist), "win": win, "book_est": book_est, "block": bsz, "thin": thin,
            "seed": seed, "restarts": restarts, "sweeps": sweeps, "greedy": greedy, "decades": K,
            "best_restart": best[2], "score_per_token": best[1] / max(1, n), "restart_keys": rkeys,
            "restart_scores": rscores}
    return dec, best[1], info


_solve_plain, _make_control_plain = solve, make_control


def solve(cipher_msgs, spec, seed, restarts, corpora, params):  # noqa: F811
    if int(params.get("vocab_order", 0) or 0):
        return solve_vocab(cipher_msgs, spec, seed, restarts, corpora, params)
    if int(params.get("slot_grammar", 0) or 0):
        return solve_grammar(cipher_msgs, spec, seed, restarts, corpora, params)
    return _solve_plain(cipher_msgs, spec, seed, restarts, corpora, params)


def make_control(spec, seed, corpora, params):  # noqa: F811
    if int(params.get("vocab_order", 0) or 0):
        return make_control_vocab(spec, seed, corpora, params)
    if int(params.get("slot_grammar", 0) or 0):
        return make_control_grammar(spec, seed, corpora, params)
    return _make_control_plain(spec, seed, corpora, params)
