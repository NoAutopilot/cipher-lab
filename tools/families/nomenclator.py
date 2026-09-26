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
    ranked = [w for w, c in lm.freq.most_common() if w in lm.vocab]
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
    ranked = [w for w, c in lm.freq.most_common() if w in lm.vocab]
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
        content = [w for w, c in reg.most_common() if w in lm.vocab and w not in key and len(w) > 1]
    else:
        freq = lambda w: (lm.freq[w],)
        content = [w for w in ranked if w not in key and len(w) > 1]
    fam = defaultdict(list)
    for w in content:
        fam[stem(w)].append(w)
    fam_rank = sorted(fam, key=lambda s: tuple(-x for x in map(sum, zip(*(freq(w) for w in fam[s])))))
    decades = list(range(100, 100 + 10 * n_dec, 10))
    rng.shuffle(decades)
    assigned, book = set(), {}
    for dec, s in zip(decades, fam_rank[:n_dec]):
        members = sorted(fam[s], key=lambda w: tuple(-x for x in freq(w)))[:10]
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

    plist = sorted(particles & lm.vocab, key=lambda w: -lm.freq[w])
    blist = sorted(bookprior & lm.vocab, key=lambda w: -lm.freq[w])
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
        cands = [w for w in cands if w in lm.uni]
        if len(cands) > max_cands:
            keep = set(rng.sample(cands, max_cands))
            keep.add(assign[v])
            cands = list(keep)
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
        return assign

    singles = [v for v in values if len(occ[v]) == 1]
    repeated = [v for v in values if len(occ[v]) > 1]
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
    for r in range(max(1, restarts)):
        rng = random.Random(seed * 7919 + r)
        assign = dict(params["_init"]) if params.get("_init") else init(rng)  # _init: test hook (start from a given key)
        # phase 1: repeated values only; every singleton reads as an unknown content word, so the anchors
        # (particles, repeated book values) are not scored against 100-odd wrong neighbours (ARM-C1 debug: from a
        # blind start the one-phase sampler stalled 600 nats below the true key on the memorised-letter test)
        if not params.get("_init") and phase1 > 0 and repeated:
            for v in singles:
                assign[v] = UNK
            ws = seq_words(assign)
            wcount = Counter(assign.values())
            for sw in range(phase1):
                T = T0 * (T1 / T0) ** (sw / max(1, phase1 - 1))
                gibbs_sweep(repeated[:], assign, ws, wcount, T, rng)
            for v in singles:  # greedy fill of the singletons given the anchors
                assign[v] = blist[0] if blist else ranked_content[0]
            ws = seq_words(assign)
            wcount = Counter(assign.values())
            gibbs_sweep(singles[:], assign, ws, wcount, 0.0, rng)
        order = values[:]
        total = sweeps + greedy
        for sw in range(total):
            T = T0 * (T1 / T0) ** (sw / max(1, sweeps - 1)) if sw < sweeps else 0.0
            ws = seq_words(assign)
            wcount = Counter(assign.values())
            gibbs_sweep(order, assign, ws, wcount, T, rng)
        sc = total_score(assign)
        print(f"    restart {r}: score {sc:.1f}")
        if sc > best_score:
            best, best_score = dict(assign), sc
            best_info = {"restart": r}
    dec = " ".join(best[v] if k != "W" else "*" for k, v in toks)
    info = {"family": "nomenclator", "seed": seed, "restarts": restarts, "sweeps": sweeps, "greedy": greedy,
            "T0": T0, "T1": T1, "tie_w": tie_w, "slot_w": slot_w, "dup_w": dup_w, "oov_pen": oov_pen,
            "vocab": lm.V, "particle_prior": len(plist), "book_prior": len(blist), "values": len(values),
            "singletons": len(singles), "phase1": phase1,
            "slot_order": slot_order, "best_restart": best_info.get("restart"), "score_per_token": best_score / n}
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
