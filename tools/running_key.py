#!/usr/bin/env python3
"""Running-key (Vigenere-family, book key) two-stream decoder, crib-drag and long-period scan. Pure Python.

  python3 tools/running_key.py CIPHER --pcorpus DE.txt [...] --kcorpus NL.txt [...] [--tabula vig|beau|varbeau]
          [--order 5] [--beam 3000] [--polish] [--out result.json]
  python3 tools/running_key.py --control --pcorpus DIR_OR_FILES --kcorpus DIR_OR_FILES --lengths 237,178,140,140,229
          [--seed 1] [--tabula vig]                       matched control (rule 3)
  python3 tools/running_key.py --noise --pcorpus ... --kcorpus ... --lengths ...   one-time-key noise band
  python3 tools/running_key.py CIPHER --crib-drag WORDS.txt --kcorpus ... [--top 30]
  python3 tools/running_key.py CIPHER --period-scan 31 120 [--seed 1]  coset IC per period + one-time-key band

CIPHER: a text file of letters, messages separated by blank lines, '#' lines ignored (ciphers/<t>/ciphertext.txt), or a spec JSON (specs/<slug>.json) whose
`ciphertext` list carries `groups` per message. Every message is decoded independently: the key offset in the book
is unknown per message, so no state is carried across messages.

Tabulae (mod 26, a=0): vig c = p + k; beau c = k - p; varbeau c = p - k.

Decoding: find p maximising LM_p(p) + LM_k(k(p, c)), where LM_p is a letter n-gram model built from --pcorpus
and LM_k one built from --kcorpus (order --order, interpolated absolute discounting, a Kneser-Ney-lite). Beam
search over the joint (plaintext context, key context) state with hypothesis recombination, width --beam; then an
optional local hill-climb (--polish) re-scoring single-letter changes over the affected n-gram windows of both
streams. Both streams are printed. Under vig the design is symmetric (p and k can swap with no change in c), so
with same-language models a decode can swap streams in stretches; --control reports strict plaintext recovery and
the swap-tolerant share (a position counts if the decoded pair {p, k} equals the true pair).

--control: plaintext cut from one book of --pcorpus (random start per message, --seed), key cut from a DIFFERENT
book of --kcorpus; both books are held out of both language models (the real key book is unknown, as is the
real plaintext). Needs at least two books overall (three when --pcorpus and --kcorpus are the same set). Prints
per-message and pooled recovery and the mean per-letter log-likelihood of both streams.

--noise: uniform random (one-time key) ciphertext of the same lengths, decoded with the same settings; the mean
per-letter log-likelihoods of both streams are the control-noise level a target decode must clear.

--crib-drag: slide each crib word through each message under each tabula, derive the key fragment it implies,
score it under the key LM (mean log-prob per letter from an empty context), print the top hits. A table of
candidates, never a claim.

--period-scan LO HI: per-message coset IC (pairs pooled over the five messages, the key restarting per message)
for each period LO..HI, with the same statistic on --noise-trials uniform random texts of the same lengths.

Corpora: files, or directories (every *.txt / *.txt.gz inside is one book). Letters are folded to a-z (umlauts
to base letters, sharp s to ss); everything else dropped.

Test: python3 tools/tests/test_running_key.py
"""
import argparse, gzip, heapq, json, math, os, random, re, sys, time, unicodedata
from collections import Counter, defaultdict

A = "abcdefghijklmnopqrstuvwxyz"
IDX = {c: i for i, c in enumerate(A)}


def fold(text):
    t = unicodedata.normalize("NFKD", text.lower().replace("ß", "ss"))
    t = "".join(c for c in t if not unicodedata.combining(c))
    return re.sub(r"[^a-z]", "", t)


SP = "_"
AS = A + SP  # model alphabet with a word boundary
IDXS = dict(IDX, **{SP: 26})


def fold_sp(text):
    """letters a-z with every run of non-letters as one '_' (word boundary)."""
    t = unicodedata.normalize("NFKD", text.lower().replace("ß", "ss"))
    t = "".join(c for c in t if not unicodedata.combining(c))
    return re.sub(r"[^a-z]+", SP, t)


def read_text(path):
    op = gzip.open if path.endswith(".gz") else open
    with op(path, "rt", encoding="utf-8", errors="replace") as f:
        return f.read()


def list_books(specs):
    out = []
    for s in specs:
        if os.path.isdir(s):
            for n in sorted(os.listdir(s)):
                if (n.endswith(".txt") or n.endswith(".txt.gz")) and not n.upper().startswith(("LICENSE", "README", "MANIFEST")):
                    out.append(os.path.join(s, n))
        else:
            out.append(s)
    return out


def load_books(paths):
    return {p: fold(read_text(p)) for p in paths}


# ---------------------------------------------------------------- tabulae
def key_of(tab, p, c):
    """key letter implied by plaintext p and cipher c (ints)."""
    if tab == "vig":      # c = p + k
        return (c - p) % 26
    if tab == "beau":     # c = k - p
        return (c + p) % 26
    if tab == "varbeau":  # c = p - k
        return (p - c) % 26
    raise ValueError(tab)


def encipher(tab, p, k):
    if tab == "vig":
        return (p + k) % 26
    if tab == "beau":
        return (k - p) % 26
    if tab == "varbeau":
        return (p - k) % 26
    raise ValueError(tab)


# ---------------------------------------------------------------- language model
class LM:
    """Interpolated absolute-discounting letter n-gram model (order n); dist(ctx) -> 26 log-probs."""

    def __init__(self, texts, order=5, D=0.75, alphabet=A):
        self.order, self.D, self.alpha = order, D, alphabet
        self.idx = {a: i for i, a in enumerate(alphabet)}
        self.cnt = [None] + [Counter() for _ in range(order)]  # cnt[m][gram of length m]
        for s in texts:
            for m in range(1, order + 1):
                c = self.cnt[m]
                for i in range(len(s) - m + 1):
                    c[s[i:i + m]] += 1
        # Kneser-Ney: the highest order uses raw counts, every lower order continuation counts
        # (number of distinct letters seen before the gram)
        self.use = [None] * (order + 1)
        self.use[order] = self.cnt[order]
        for m in range(1, order):
            cc = Counter()
            for g in self.cnt[m + 1]:
                cc[g[1:]] += 1
            self.use[m] = cc
        self.tot = [None] + [defaultdict(int) for _ in range(order)]
        self.typ = [None] + [defaultdict(int) for _ in range(order)]
        for m in range(1, order + 1):
            for g, n in self.use[m].items():
                self.tot[m][g[:-1]] += n
                self.typ[m][g[:-1]] += 1
        self.cnt = None  # raw lower-order counts no longer needed (memory)
        self.cache = {}
        u = self.use[1]
        n1 = sum(u.values()) + len(alphabet)
        self.uni = [(u[a] + 1) / n1 for a in alphabet]

    def _probs(self, ctx, top=True):
        if ctx == "":
            return self.uni
        lower = self._probs(ctx[1:], False)
        m = len(ctx) + 1
        cm = self.use[m] if (top or m == self.order) else self.use[m]
        t = self.tot[m].get(ctx, 0)
        if t == 0:
            return lower
        D = self.D
        lam = D * self.typ[m][ctx] / t
        return [max(cm.get(ctx + a, 0) - D, 0) / t + lam * lower[i] for i, a in enumerate(self.alpha)]

    def dist(self, ctx):
        """log-prob list for the next letter; ctx trimmed to order-1."""
        ctx = ctx[-(self.order - 1):] if self.order > 1 else ""
        v = self.cache.get(ctx)
        if v is None:
            v = [math.log(x) for x in self._probs(ctx)]
            self.cache[ctx] = v
        return v

    def score(self, s, ctx=""):
        tot = 0.0
        h = ctx
        for ch in s:
            tot += self.dist(h)[self.idx[ch]]
            h = (h + ch)[-(self.order - 1):]
        return tot


# ---------------------------------------------------------------- decoder
def _options(lm, ctx, spaces):
    """per next letter: list of (logp, emitted string) -- the letter, or a word boundary then the letter."""
    d = lm.dist(ctx)
    if not spaces or ctx == "" or ctx.endswith(SP):
        return [((d[x], A[x]),) for x in range(26)]
    d2 = lm.dist(ctx + SP)
    ds = d[26]
    return [((d[x], A[x]), (ds + d2[x], SP + A[x])) for x in range(26)]


def beam_decode(cipher, lmp, lmk, tab="vig", beam=3000, per_hyp=10, spaces=False):
    """cipher: string a-z. Returns (plain, key, score); with spaces=True the streams carry '_' word boundaries."""
    c_ints = [IDX[ch] for ch in cipher]
    np_, nk = lmp.order - 1, lmk.order - 1
    # hypothesis: (pctx, kctx) -> (score, node); node = (p_emitted, k_emitted, parent)
    hyps = {("", ""): (0.0, None)}
    perm = {cv: [key_of(tab, p, cv) for p in range(26)] for cv in range(26)}
    ocache_p, ocache_k = {}, {}
    for cv in c_ints:
        kmap = perm[cv]
        cand = []
        for (pc, kc), (sc, node) in hyps.items():
            op = ocache_p.get(pc)
            if op is None:
                op = ocache_p[pc] = _options(lmp, pc, spaces)
            ok = ocache_k.get(kc)
            if ok is None:
                ok = ocache_k[kc] = _options(lmk, kc, spaces)
            loc = []
            for p in range(26):
                okk = ok[kmap[p]]
                for vp, ep in op[p]:
                    for vk, ek in okk:
                        loc.append((vp + vk, ep, ek))
            if per_hyp < len(loc):
                loc = heapq.nlargest(per_hyp, loc)
            for v, ep, ek in loc:
                cand.append((sc + v, ep, ek, pc, kc, node))
        if len(cand) > beam * 2:
            cand = heapq.nlargest(beam * 2, cand, key=lambda x: x[0])
        else:
            cand.sort(key=lambda x: -x[0])
        new = {}
        for s, ep, ek, pc, kc, node in cand:
            key = ((pc + ep)[-np_:] if np_ else "", (kc + ek)[-nk:] if nk else "")
            if key in new:
                continue
            new[key] = (s, (ep, ek, node))
            if len(new) >= beam:
                break
        hyps = new
        if len(ocache_p) > 200000:
            ocache_p.clear()
            ocache_k.clear()
    best = max(hyps.values(), key=lambda x: x[0])
    ps, ks = [], []
    node = best[1]
    while node is not None:
        ps.append(node[0])
        ks.append(node[1])
        node = node[2]
    return "".join(reversed(ps)), "".join(reversed(ks)), best[0]


def total_score(plain, cipher, lmp, lmk, tab):
    key = "".join(A[key_of(tab, IDX[p], IDX[c])] for p, c in zip(plain, cipher))
    return lmp.score(plain) + lmk.score(key), key


def polish(plain, cipher, lmp, lmk, tab, rounds=5):
    """single-letter hill-climb on the joint score (full rescoring of the affected windows)."""
    p = list(plain)
    n = len(p)
    w = max(lmp.order, lmk.order)
    best, _ = total_score("".join(p), cipher, lmp, lmk, tab)
    for _ in range(rounds):
        improved = False
        for i in range(n):
            lo, hi = max(0, i - w + 1), min(n, i + w)
            orig = p[i]
            ctxlo = max(0, lo - w)

            def local(pl):
                seg = "".join(pl[ctxlo:hi])
                cs = cipher[ctxlo:hi]
                ks = "".join(A[key_of(tab, IDX[a], IDX[b])] for a, b in zip(seg, cs))
                off = lo - ctxlo
                return (lmp.score(seg[off:], seg[:off]) + lmk.score(ks[off:], ks[:off]))

            base = local(p)
            bl, bv = orig, base
            for a in A:
                if a == orig:
                    continue
                p[i] = a
                v = local(p)
                if v > bv + 1e-9:
                    bl, bv = a, v
            p[i] = bl
            if bl != orig:
                improved = True
        if not improved:
            break
    return "".join(p)


def decode_message(cipher, lmp, lmk, tab, beam, per_hyp, do_polish, spaces=False):
    n = len(cipher)
    if spaces:
        pseg, kseg, _ = beam_decode(cipher, lmp, lmk, tab, beam, per_hyp, spaces=True)
        lp, lk = lmp.score(pseg), lmk.score(kseg)
        return {"plain": pseg.replace(SP, ""), "key": kseg.replace(SP, ""), "plain_seg": pseg, "key_seg": kseg,
                "ll_p": lp / n, "ll_k": lk / n, "ll_joint": (lp + lk) / n}
    plain, key, _ = beam_decode(cipher, lmp, lmk, tab, beam, per_hyp)
    if do_polish:
        plain = polish(plain, cipher, lmp, lmk, tab)
    s, key = total_score(plain, cipher, lmp, lmk, tab)
    return {"plain": plain, "key": key, "ll_p": lmp.score(plain) / n, "ll_k": lmk.score(key) / n,
            "ll_joint": s / n}


# ---------------------------------------------------------------- input
def read_cipher(path):
    if path.endswith(".json"):
        d = json.load(open(path))
        return [fold(m["groups"]) for m in d["ciphertext"]]
    # text: '#' lines are comments; messages are separated by blank lines
    msgs, cur = [], []
    for line in read_text(path).splitlines() + [""]:
        if line.lstrip().startswith("#"):
            continue
        if line.strip():
            cur.append(line)
        elif cur:
            msgs.append(fold(" ".join(cur)))
            cur = []
    return [m for m in msgs if m]


def build_models(args, exclude=()):
    pb = [b for b in list_books(args.pcorpus) if b not in exclude]
    kb = [b for b in list_books(args.kcorpus or args.pcorpus) if b not in exclude]
    cache = {}
    f, al = (fold_sp, AS) if args.spaces else (fold, A)
    for b in set(pb) | set(kb):
        cache[b] = f(read_text(b))
    lmp = LM([cache[b] for b in pb], args.order, args.discount, al)
    lmk = lmp if sorted(pb) == sorted(kb) else LM([cache[b] for b in kb], args.order, args.discount, al)
    return lmp, lmk, pb, kb


def fmt_ll(x):
    return f"{x:.3f}"


# ---------------------------------------------------------------- modes
def run_decode(args, msgs, lmp, lmk, label="target"):
    out = []
    for i, c in enumerate(msgs):
        t0 = time.time()
        r = decode_message(c, lmp, lmk, args.tabula, args.beam, args.per_hyp, args.polish, args.spaces)
        r.update({"msg": i + 1, "n": len(c), "cipher": c, "secs": round(time.time() - t0, 1)})
        out.append(r)
        print(f"[{label}] msg {i+1} n={len(c)} tab={args.tabula} ll_p={fmt_ll(r['ll_p'])} "
              f"ll_k={fmt_ll(r['ll_k'])} ({r['secs']}s)")
        print(f"  P: {r.get('plain_seg', r['plain'])}")
        print(f"  K: {r.get('key_seg', r['key'])}")
        sys.stdout.flush()
    pooled(out, label)
    return out


def pooled(rs, label):
    n = sum(r["n"] for r in rs)
    llp = sum(r["ll_p"] * r["n"] for r in rs) / n
    llk = sum(r["ll_k"] * r["n"] for r in rs) / n
    print(f"[{label}] POOLED n={n} mean ll_p={llp:.3f} ll_k={llk:.3f} joint={llp+llk:.3f}")
    return llp, llk


def run_control(args):
    rng = random.Random(args.seed)
    lengths = [int(x) for x in args.lengths.split(",")]
    pbooks = list_books(args.pcorpus)
    kbooks = list_books(args.kcorpus or args.pcorpus)
    pbook = args.plain_book or rng.choice(pbooks)
    kchoices = [b for b in kbooks if b != pbook]
    if not kchoices:
        sys.exit("--control needs a key book different from the plaintext book")
    kbook = args.key_book or rng.choice(kchoices)
    ptext, ktext = fold(read_text(pbook)), fold(read_text(kbook))
    lmp, lmk, pb, kb = build_models(args, exclude=(pbook, kbook))
    if not pb or not kb:
        sys.exit("--control: no training books left after holding out the plaintext and key books")
    print(f"control seed={args.seed} tab={args.tabula} order={args.order} beam={args.beam} "
          f"plain_book={os.path.basename(pbook)} key_book={os.path.basename(kbook)} "
          f"LM_p books={len(pb)} ({sum(len(fold(read_text(b))) for b in pb) if args.verbose else '-'}) "
          f"LM_k books={len(kb)}")
    res = []
    for i, n in enumerate(lengths):
        # middle 90% of each book: skips front matter and transcriber's notes
        ps = rng.randrange(len(ptext) // 20, len(ptext) * 19 // 20 - n)
        ks = rng.randrange(len(ktext) // 20, len(ktext) * 19 // 20 - n)
        P, K = ptext[ps:ps + n], ktext[ks:ks + n]
        C = "".join(A[encipher(args.tabula, IDX[a], IDX[b])] for a, b in zip(P, K))
        t0 = time.time()
        r = decode_message(C, lmp, lmk, args.tabula, args.beam, args.per_hyp, args.polish, args.spaces)
        strict = sum(a == b for a, b in zip(r["plain"], P))
        swap = sum((a == b) or (a == kk) for a, b, kk in zip(r["plain"], P, K)) if args.tabula == "vig" else strict
        kstrict = sum(a == b for a, b in zip(r["key"], K))
        res.append({"n": n, "strict": strict, "swap": swap, "key": kstrict, "ll_p": r["ll_p"], "ll_k": r["ll_k"]})
        print(f"  msg {i+1} n={n} plain {strict}/{n}={strict/n:.1%}  swap-tolerant {swap/n:.1%}  "
              f"key {kstrict/n:.1%}  ll_p={fmt_ll(r['ll_p'])} ll_k={fmt_ll(r['ll_k'])} ({time.time()-t0:.0f}s)")
        if args.verbose:
            if not args.spaces:
                tj = (lmp.score(P) + lmk.score(K)) / n
                print(f"    joint ll/letter: decoded {r['ll_joint']:.3f} vs true pair {tj:.3f} "
                      f"({'model error' if r['ll_joint'] >= tj else 'search error'})")
            print(f"    true P: {P}\n    dec  P: {r.get('plain_seg', r['plain'])}\n"
                  f"    true K: {K}\n    dec  K: {r.get('key_seg', r['key'])}")
        sys.stdout.flush()
    N = sum(r["n"] for r in res)
    s = sum(r["strict"] for r in res) / N
    w = sum(r["swap"] for r in res) / N
    k = sum(r["key"] for r in res) / N
    llp = sum(r["ll_p"] * r["n"] for r in res) / N
    llk = sum(r["ll_k"] * r["n"] for r in res) / N
    print(f"CONTROL POOLED seed={args.seed} tab={args.tabula} plain={s:.1%} swap-tolerant={w:.1%} key={k:.1%} "
          f"ll_p={llp:.3f} ll_k={llk:.3f}")
    return {"seed": args.seed, "tab": args.tabula, "plain": s, "swap": w, "key": k, "ll_p": llp, "ll_k": llk,
            "per_msg": res, "plain_book": pbook, "key_book": kbook}


def run_noise(args):
    rng = random.Random(args.seed)
    lengths = [int(x) for x in args.lengths.split(",")]
    lmp, lmk, _, _ = build_models(args)
    msgs = ["".join(rng.choice(A) for _ in range(n)) for n in lengths]
    return run_decode(args, msgs, lmp, lmk, label=f"noise seed={args.seed}")


def run_crib(args, msgs, lmk):
    words = [fold(w) for w in read_text(args.crib_drag).split()]
    words = [w for w in words if len(w) >= 3]
    rows = []
    for w in words:
        for mi, c in enumerate(msgs):
            for i in range(len(c) - len(w) + 1):
                for tab in (["vig", "beau", "varbeau"] if args.all_tabulae else [args.tabula]):
                    k = "".join(A[key_of(tab, IDX[a], IDX[b])] for a, b in zip(w, c[i:i + len(w)]))
                    rows.append((lmk.score(k) / len(k), w, mi + 1, i, tab, k))
    rows.sort(reverse=True)
    print("score/letter\tcrib\tmsg\tpos\ttabula\tkey_fragment")
    for r in rows[:args.top]:
        print(f"{r[0]:.3f}\t{r[1]}\t{r[2]}\t{r[3]}\t{r[4]}\t{r[5]}")
    return rows[:args.top]


def coset_ic(msgs, P):
    num = den = 0
    for m in msgs:
        for j in range(P):
            col = m[j::P]
            n = len(col)
            if n < 2:
                continue
            f = Counter(col)
            num += sum(v * (v - 1) for v in f.values())
            den += n * (n - 1)
    return num / den if den else float("nan")


def run_period_scan(args, msgs):
    lo, hi = args.period_scan
    rng = random.Random(args.seed)
    lengths = [len(m) for m in msgs]
    tgt = {P: coset_ic(msgs, P) for P in range(lo, hi + 1)}
    trials = []
    for _ in range(args.noise_trials):
        r = ["".join(rng.choice(A) for _ in range(n)) for n in lengths]
        trials.append({P: coset_ic(r, P) for P in range(lo, hi + 1)})
    print("period\ttarget_IC\tnoise_mean\tnoise_p95\tz")
    for P in range(lo, hi + 1):
        vals = sorted(t[P] for t in trials)
        mu = sum(vals) / len(vals)
        sd = (sum((v - mu) ** 2 for v in vals) / len(vals)) ** 0.5 or 1e-9
        print(f"{P}\t{tgt[P]:.4f}\t{mu:.4f}\t{vals[int(0.95*len(vals))-1]:.4f}\t{(tgt[P]-mu)/sd:+.2f}")
    maxes = sorted(max(t.values()) for t in trials)
    bp = max(tgt, key=tgt.get)
    print(f"target max coset IC {tgt[bp]:.4f} at P={bp}; noise max-over-periods: mean "
          f"{sum(maxes)/len(maxes):.4f}, p95 {maxes[int(0.95*len(maxes))-1]:.4f} ({args.noise_trials} trials)")
    return tgt


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0],
                                 formatter_class=argparse.RawDescriptionHelpFormatter, epilog=__doc__)
    ap.add_argument("cipher", nargs="?", help="ciphertext file (one message per line) or specs/<slug>.json")
    ap.add_argument("--pcorpus", nargs="+", default=[], help="plaintext-language corpus files or dirs")
    ap.add_argument("--kcorpus", nargs="+", default=[], help="key-language corpus files or dirs (default = pcorpus)")
    ap.add_argument("--tabula", default="vig", choices=["vig", "beau", "varbeau"])
    ap.add_argument("--order", type=int, default=6)
    ap.add_argument("--discount", type=float, default=0.9)
    ap.add_argument("--beam", type=int, default=3000)
    ap.add_argument("--per-hyp", type=int, default=10, help="letters expanded per hypothesis (26 = all)")
    ap.add_argument("--spaces", action="store_true",
                    help="model word boundaries as latent '_' symbols in both streams (4x slower, usually better)")
    ap.add_argument("--polish", action="store_true", help="local single-letter hill-climb after the beam")
    ap.add_argument("--seed", type=int, default=1)
    ap.add_argument("--control", action="store_true")
    ap.add_argument("--noise", action="store_true")
    ap.add_argument("--lengths", default="237,178,140,140,229")
    ap.add_argument("--plain-book", help="control: force the plaintext book")
    ap.add_argument("--key-book", help="control: force the key book")
    ap.add_argument("--crib-drag", metavar="WORDLIST")
    ap.add_argument("--all-tabulae", action="store_true", help="crib-drag under all three tabulae")
    ap.add_argument("--top", type=int, default=30)
    ap.add_argument("--period-scan", nargs=2, type=int, metavar=("LO", "HI"))
    ap.add_argument("--noise-trials", type=int, default=200)
    ap.add_argument("--out", help="write JSON result")
    ap.add_argument("--verbose", action="store_true")
    a = ap.parse_args(argv)

    result = None
    if a.control:
        result = run_control(a)
    elif a.noise:
        result = run_noise(a)
    else:
        if not a.cipher:
            ap.error("cipher file required")
        msgs = read_cipher(a.cipher)
        if a.period_scan:
            result = run_period_scan(a, msgs)
        elif a.crib_drag:
            lmk = LM([fold(read_text(b)) for b in list_books(a.kcorpus or a.pcorpus)], a.order, a.discount)  # letters only
            result = run_crib(a, msgs, lmk)
        else:
            lmp, lmk, _, _ = build_models(a)
            result = run_decode(a, msgs, lmp, lmk)
    if a.out:
        with open(a.out, "w") as f:
            json.dump(result, f, indent=1, default=str)
    return result


if __name__ == "__main__":
    main()
