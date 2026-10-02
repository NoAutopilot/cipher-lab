"""seeded_code: homophonic two-part code (syllables and words) with a partial key pinned and local alphabetical runs
used as bracket constraints (A2-CAS8, 2 Oct 2026, castelcicala-1816).

Design. Each numeric group is one codebook entry (a whole word or a syllable); frequent entries have several codes
(homophones); the code numbers run alphabetically only inside short runs, and the runs are shuffled through the
number space (the "local alphabetical runs" Bourdeau measured on castelcicala-1816: 2201 che, 2205 ci, 2211 di ...).
Part of the key is known (the target's key.tsv). The solver anneals one entry per unpinned group type under a
4-gram letter model of the training corpus plus an entry-frequency prior; an unpinned group whose nearest pinned
neighbours below and above (within --param bracket=W numbers) are in alphabetical order may only take an entry
between them.

Pins. A control token carrying its value is written "1234=di" (the control's own seeded key); for the target,
--param pins=ciphers/<t>/key.tsv (group<TAB>value rows, '#' comments; value NULL = a null) pins every group in it.
Tokens "NULL" are nulls (empty), tokens with "?" are kept as their own unpinned types.

Control (rule 3): a window of the training corpus as long in tokens as the target (N), segmented into entries
(the --param words=W most frequent corpus words are whole entries, every other word is split into syllables), given
the target's K codes (homophones to the most frequent entries), laid in alphabetical runs of --param run=R, the runs
shuffled; then types are pinned frequency-weighted at random until the pinned token share reaches the target's own
(computed from the pins file; --param pinshare=p overrides, pinshare=0 is the blind baseline), types drawn with
weight count**pinpow (default 2, so a few frequent types carry the share, as glossed keys do; the printed pinned type
count is compared with the target's). The printed line gives
the share of adjacent pinned pairs within the bracket that are in alphabetical order for control and target, so the
run length can be matched to the target's own run structure (--param run).

Recovery: share of UNPINNED token positions whose decoded entry equals the true entry (pinned positions are not
counted). Params: pins, pinshare, pinpow=2, words=400, vocab=2500, run=6, bracket=8, iters=300000, prior=1.0."""
import math, random, re
from collections import Counter, defaultdict

from families import draw_window

DESCRIPTION = ("homophonic two-part code of syllables/words, partial key pinned, local alphabetical runs as "
               "bracket constraints; token accuracy on unpinned positions")

FOLD = str.maketrans({"é": "e", "è": "e", "ê": "e", "à": "a", "ù": "u", "û": "u", "î": "i", "ô": "o", "â": "a",
                      "ë": "e", "ï": "i", "á": "a", "í": "i", "ó": "o", "ò": "o", "ì": "i", "ú": "u", "ç": "c"})
VOW = "aeiou"


def fold(s):
    return re.sub(r"[^a-z]", "", s.lower().translate(FOLD))


def words_of(text):
    return [w for w in (fold(x) for x in re.findall(r"[A-Za-zÀ-ÿ']+", text.replace("'", " "))) if w]


def syllables(w):
    parts = re.findall(r"[^aeiou]*[aeiou]+|[^aeiou]+$", w)
    if len(parts) > 1 and not any(c in VOW for c in parts[-1]):
        tail = parts.pop()
        parts[-1] += tail
    return parts or [w]


def segment(words, top):
    out = []
    for w in words:
        out.extend([w] if w in top else syllables(w))
    return out


def top_words(texts, n):
    c = Counter()
    for t in texts:
        c.update(words_of(t))
    return {w for w, _ in c.most_common(n)}


class Quad:
    def __init__(self, texts, k=0.1):
        s = "".join(fold(t) for t in texts)
        self.c = Counter(s[i:i + 4] for i in range(len(s) - 3))
        self.ctx = Counter(s[i:i + 3] for i in range(len(s) - 2))
        self.k = k
        self.cache = {}

    def lp(self, s):
        tot = 0.0
        for i in range(3, len(s)):
            g = s[i - 3:i + 1]
            v = self.cache.get(g)
            if v is None:
                v = math.log((self.c.get(g, 0) + self.k) / (self.ctx.get(g[:-1], 0) + 26 * self.k))
                self.cache[g] = v
            tot += v
        return tot


def read_pins(path):
    pins = {}
    if not path:
        return pins
    for line in open(path, encoding="utf-8"):
        if line.startswith("#") or not line.strip():
            continue
        p = line.rstrip("\n").split("\t")
        if len(p) >= 2:
            pins[p[0]] = "" if p[1] == "NULL" else fold(p[1])
    return pins


def num(t):
    m = re.match(r"\d+", t)
    return int(m.group()) if m and "?" not in t else None


def order_share(pins, bracket):
    """share of pinned pairs with code numbers 1..bracket apart whose values are in alphabetical order."""
    ks = sorted((num(g), v) for g, v in pins.items() if num(g) is not None and v)
    ok = tot = 0
    for (a, va), (b, vb) in zip(ks, ks[1:]):
        if b - a <= bracket:
            tot += 1; ok += va <= vb
    return ok / tot if tot else float("nan"), tot


def target_pinshare(params):
    pins = read_pins(params.get("pins"))
    toks = [t for m in params["target_msgs"] for t in m]
    return sum(1 for t in toks if t in pins or t == "NULL") / max(1, len(toks)), pins


def make_control(spec, seed, corpora, params):
    N, K = params["N"], params["K"]
    rng = random.Random(seed)
    nwords = int(params.get("words", 400)); run = int(params.get("run", 6)); bracket = int(params.get("bracket", 8))
    share_t, tpins = target_pinshare(params)
    share = float(params.get("pinshare", share_t))
    pinpow = float(params.get("pinpow", 2.0))
    big = max(corpora, key=len)
    rest_c = [c for c in corpora if c is not big]
    top = top_words(corpora, nwords)
    # window of raw text long enough for N entries (~2.6 entries per word is generous)
    win, rest = draw_window(big, N * 6, seed)
    ents = segment(words_of(win), top)[:N]
    if len(ents) < N:
        raise SystemExit(f"control window gave {len(ents)} entries < N={N}")
    cnt = Counter(ents)
    E = len(cnt)
    codes = {e: 1 for e in cnt}
    extra = max(0, K - E)
    for _ in range(extra):  # homophones to the entry with the most occurrences per code
        e = max(cnt, key=lambda x: cnt[x] / codes[x])
        codes[e] += 1
    runs = []
    for p in range(max(codes.values())):
        lst = sorted(e for e in cnt if codes[e] > p)
        runs += [[(e, p) for e in lst[i:i + run]] for i in range(0, len(lst), run)]
    rng.shuffle(runs)
    codeof, n = {}, 1
    for r in runs:
        for ep in r:
            codeof[ep] = n; n += rng.choice((1, 1, 2))
    seq = [codeof[(e, rng.randrange(codes[e]))] for e in ents]
    ccount = Counter(seq)
    value = {c: e for (e, p), c in codeof.items()}
    pinned, cov, types = set(), 0, list(ccount)
    while cov < share * N and types:
        c = rng.choices(types, weights=[ccount[t] ** pinpow for t in types])[0]
        types.remove(c); pinned.add(c); cov += ccount[c]
    msgs, pos = [], 0
    for L in params["lengths"]:
        msgs.append([f"{c}={value[c]}" if c in pinned else str(c) for c in seq[pos:pos + L]]); pos += L
    truth = "|".join(("=" + value[c]) if c in pinned else value[c] for c in seq)
    cpins = {str(c): value[c] for c in pinned}
    co, _ = order_share(cpins, bracket); to, tn = order_share(tpins, bracket)
    print(f"  control seed {seed}: entries {E} (window types), codes {len({c for c in seq})}, pinned types "
          f"{len(pinned)} share {cov / N:.3f} (target {share_t:.3f}, {len(tpins)} pins); in-order pinned pairs "
          f"within {bracket}: control {co:.2f}, target {to:.2f} (n={tn})")
    return msgs, truth, rest_c + [rest]


def solve(cipher_msgs, spec, seed, restarts, corpora, params):
    rng = random.Random(seed)
    nwords = int(params.get("words", 400)); nvocab = int(params.get("vocab", 2500))
    bracket = int(params.get("bracket", 8)); iters = int(params.get("iters", 300000))
    lam = float(params.get("prior", 1.0))
    pins = read_pins(params.get("pins"))
    toks = [t for m in cipher_msgs for t in m]
    sym, fixed = [], {}
    for t in toks:
        g, _, v = t.partition("=")
        if v:
            fixed[g] = v
        elif g == "NULL":
            fixed[g] = ""
        elif g in pins:
            fixed[g] = pins[g]
        sym.append(g)
    model = Quad(corpora)
    top = top_words(corpora, nwords)
    ec = Counter()
    for c in corpora:
        ec.update(segment(words_of(c), top))
    for v in fixed.values():
        if v:
            ec[v] += 1
    vocab = [e for e, _ in ec.most_common(nvocab)]
    tot = sum(ec[e] for e in vocab)
    logf = {e: math.log(ec[e] / tot) for e in vocab}
    svocab = sorted(vocab)
    pk = sorted((num(g), v) for g, v in fixed.items() if num(g) is not None and v)
    pnums = [a for a, _ in pk]
    import bisect
    cands = {}
    free = sorted({g for g in sym if g not in fixed})
    nb = 0
    for g in free:
        n = num(g); c = None
        if n is not None:
            i = bisect.bisect_left(pnums, n)
            if 0 < i < len(pnums) and n - pnums[i - 1] <= bracket and pnums[i] - n <= bracket:
                lo, hi = pk[i - 1][1], pk[i][1]
                if lo <= hi:
                    c = svocab[bisect.bisect_left(svocab, lo):bisect.bisect_right(svocab, hi)]
        if c:
            nb += 1
        cands[g] = c or vocab
    # proposals drawn frequency-weighted (count ** 0.5) so common entries are tried often (a uniform draw over a
    # 2,500-entry vocabulary proposed the right entry to a type only a few times per run)
    cw = {}
    for g in free:
        acc, cum = 0.0, []
        for e in cands[g]:
            acc += ec[e] ** 0.5; cum.append(acc)
        cw[g] = cum
    occ = defaultdict(list)
    for i, g in enumerate(sym):
        if g not in fixed:
            occ[g].append(i)
    L = len(sym)
    best = None
    for r in range(restarts):
        val = dict(fixed)
        for g in free:
            val[g] = rng.choices(cands[g], cum_weights=cw[g])[0]

        def local(g, v):
            s = 0.0
            for i in occ[g]:
                a, b = max(0, i - 2), min(L, i + 3)
                s += model.lp("".join(v if j == i else val[sym[j]] for j in range(a, b)))
            return s + lam * len(occ[g]) * logf.get(v, -15.0)

        T0, T1 = 3.0, 0.05
        for it in range(iters):
            g = free[rng.randrange(len(free))]
            new = rng.choices(cands[g], cum_weights=cw[g])[0]; old = val[g]
            if new == old:
                continue
            d = local(g, new) - local(g, old)
            T = T0 * (T1 / T0) ** (it / iters)
            if d >= 0 or rng.random() < math.exp(d / T):
                val[g] = new
        text = "".join(val[g] for g in sym)
        sc = model.lp(text) / max(1, len(text)) + lam * sum(logf.get(val[g], -15.0) for g in free for _ in occ[g]) / L
        if best is None or sc > best[0]:
            best = (sc, dict(val))
    sc, val = best
    dec = "|".join(("=" + val[g]) if g in fixed else val[g] for g in sym)
    return dec, sc, {"free_types": len(free), "bracketed": nb, "vocab": len(vocab), "iters": iters}


def score_recovery(plain, truth):
    d, t = plain.split("|"), truth.split("|")
    n = ok = 0
    for a, b in zip(d, t):
        if b.startswith("="):
            continue
        n += 1; ok += a == b
    return ok / n if n else 0.0


def split_decode(dec, msgs):
    parts, out, pos = dec.split("|"), [], 0
    for m in msgs:
        out.append(" ".join(p.lstrip("=").upper() if p.startswith("=") else p for p in parts[pos:pos + len(m)]))
        pos += len(m)
    return out
