"""permuted_tableau: family B'', a running (book) key through a GENERAL permuted tableau, c = S3(S1(p) + S2(k)) mod 26
with S1, S2, S3 arbitrary permutations of the 26 letters (GOLD-B2D, 25 Sept 2026). First sub-family B''-c: S1 = S2 =
identity, S3 free (a free permutation on the cipher side of a standard running-key square; equivalently c' = S3^-1(c) is
a standard-tableau running-key ciphertext). Wraps tools/running_key.py (LM, beam_decode, key_of, encipher) the way
keyed_running_key.py does; `perm_tabula(S1, S2, S3, arith)` returns the same dict shape as running_key.mixed_tabula, so
the decoder accepts it unchanged. keyed_running_key covers the keyword-restricted corner of this family (four
placements of one keyword-mixed alphabet); this module searches the 26! cipher-side permutations blind.

Attack, three stages, all blind:
  1. START. The sort-match permutation (GOLD-2C step 1's statistic): the ciphertext letters sorted by count are matched
     to the letters of s = p + k sorted by the predicted distribution conv(plain unigram, key unigram). Chain 1 starts
     there, chains 2.. from uniform-random permutations.
  2. ANNEAL S3 under a CHEAP PROXY objective (the brief's option 2, made primary because the decoder objective at
     1-2 s per evaluation does not fit thousands of evaluations per chain into one box): the log-likelihood of the
     n-gram windows of c' = S3^-1(c) under the empirical n-gram distribution of s = p + k, built once by adding the
     training plaintext texts and the training key texts letter by letter mod 26 at `pairings` random offsets and
     counting n-grams (add-k smoothing; `proxy_order` 4 by default: 26^4 cells, about 2.4M x pairings letters).
     This is the marginal n-gram distribution of the sum stream, which is not S3-invariant (unlike the sorted count
     profile), so it ranks permutations; it ignores the joint plaintext-key inference the beam decoder does, which is
     why stage 3 exists. Moves: swap two cipher letters (80 pct) or a 3-cycle (20 pct); delta-scored over only the
     windows a move touches (about 0.2-0.4 ms per evaluation on 924 letters), so a chain of tens of thousands of
     evaluations costs seconds. Temperature: T0 = the median absolute delta of 200 random swaps from the start
     permutation (measured per run, printed), geometric cooling to T0/200 over `evals` evaluations; a chain stops
     early after `patience` consecutive non-improving proposals. Best of `chains` chains by the proxy, and the top
     `rescore` distinct chain winners go to stage 3.
  3. RESCORE with the two-stream beam decoder (LM_p from the plaintext corpus, LM_k from the key corpus): each
     candidate S3 decodes the first `anneal_len` letters of message `sel_msg` at ANNEAL settings (order `anneal_order`,
     beam `anneal_beam`, word boundaries on); the best joint log-likelihood per letter wins; the winner decodes every
     message at the STANDARD settings (order, beam, per_hyp, spaces: the same as keyed_running_key's, order 6 beam 300)
     and the pooled joint log-likelihood per letter is the family score, comparable to GOLD-2C's noise band.
     Measured on this container (4 cores, pure Python, 25 Sept 2026): one anneal-settings decoder evaluation (order 5,
     beam 80, 140 letters, spaces on) takes ANNEAL_EVAL_SECONDS below; the proxy evaluation about 0.3 ms.

Control (rule 3), in make_control: per seed, plaintext windows at the target's message lengths from one corpus book,
key windows from one held-out book of `kcorpus` (else another corpus book), S3 drawn uniformly at random from the 26!
permutations, S1 = S2 = identity, both books held out of the models and of the proxy table. solve() prints, for a
control, the letters of S3 placed correctly (of 26) by the sort-match start and by the anneal, exactly and under the
best cyclic shift (S3'(s) = S3(s + t) is the same tableau with the key Caesar-shifted by t, the family's one residual
near-symmetry; the Dutch key model separates it, the proxy only weakly). Score = pooled plaintext letters recovered.

params (--param k=v): kcorpus=DIR, arith=vig|beau|varbeau, order=6, beam=300, per_hyp=10, spaces=1, discount=0.9,
sel_msg=0, proxy_order=4, pairings=3, smooth=0.5, chains=3, evals=30000, patience=6000, rescore=3, anneal_order=5,
anneal_beam=80, anneal_len=140, start=sort|random (chain 1's start); search=anneal|beam (beam = the open-tableau beam
decoder open_beam() below, which searches the mapping inside the decoder instead of the proxy anneal: open_order=5,
open_beam=2000, per_open=30, per_map=10); refine=ROUNDS (0 = off) runs refine_decoder() on the stage-3 winner:
per round the refine_props=5 swaps with the least bad proxy delta plus refine_rand=3 random swaps, each scored by
the decoder at anneal settings (about 2 s each), the best accepted if it improves. Needs >= 2 corpus texts (3
without kcorpus)."""
import heapq, math, os, random, time, types
from collections import Counter
import running_key as rk
from families import draw_window, TOOLS

DESCRIPTION = ("running key through a general permuted tableau, first B''-c (free cipher-side permutation S3, S1 = S2 = "
               "identity): sort-match start, simulated anneal under an n-gram sum-stream proxy, beam rescoring; control = "
               "plain book x held-out key book x uniformly random S3")
ROOT = os.path.dirname(TOOLS)
ANNEAL_EVAL_SECONDS = None  # filled by the calibration in the docstring's terms; measured live and printed by solve()
_STATE = {}
IDENT = list(range(26))


def _p(params):
    return types.SimpleNamespace(
        kcorpus=params.get("kcorpus"), arith=params.get("arith", "vig"), order=int(params.get("order", 6)),
        discount=float(params.get("discount", 0.9)), beam=int(params.get("beam", 300)),
        per_hyp=int(params.get("per_hyp", 10)), spaces=bool(int(params.get("spaces", 1))),
        sel_msg=int(params.get("sel_msg", 0)), proxy_order=int(params.get("proxy_order", 4)),
        pairings=int(params.get("pairings", 3)), smooth=float(params.get("smooth", 0.5)),
        chains=int(params.get("chains", 3)), evals=int(params.get("evals", 30000)),
        patience=int(params.get("patience", 6000)), rescore=int(params.get("rescore", 3)),
        anneal_order=int(params.get("anneal_order", 5)), anneal_beam=int(params.get("anneal_beam", 80)),
        anneal_len=int(params.get("anneal_len", 140)), start=params.get("start", "sort"),
        search=params.get("search", "anneal"), open_order=int(params.get("open_order", 5)),
        open_beam=int(params.get("open_beam", 2000)), per_open=int(params.get("per_open", 30)),
        per_map=int(params.get("per_map", 10)), refine=int(params.get("refine", 0)),
        refine_props=int(params.get("refine_props", 5)), refine_rand=int(params.get("refine_rand", 3)))


# ---------------------------------------------------------------- tabula
def perm_tabula(S1=None, S2=None, S3=None, arith="vig"):
    """c = S3[(S1[p] (+/-) S2[k]) mod 26]; each S a list of 26 letter indices (None = identity). Same dict shape as
    running_key.mixed_tabula (enc, kof, name, alphabet), so key_of/encipher/beam_decode accept it. alphabet is S3 as
    letters (alphabet[s] = the cipher letter written for sum s)."""
    S1, S2, S3 = list(S1 or IDENT), list(S2 or IDENT), list(S3 or IDENT)
    enc = [[0] * 26 for _ in range(26)]
    kof = [[0] * 26 for _ in range(26)]
    for p in range(26):
        for k in range(26):
            if arith == "vig":
                s = (S1[p] + S2[k]) % 26
            elif arith == "beau":
                s = (S2[k] - S1[p]) % 26
            elif arith == "varbeau":
                s = (S1[p] - S2[k]) % 26
            else:
                raise ValueError(arith)
            c = S3[s]
            enc[p][k] = c
            kof[c][p] = k
    alphabet = "".join(rk.A[c] for c in S3)
    return {"enc": enc, "kof": kof, "S1": S1, "S2": S2, "S3": S3, "alphabet": alphabet, "arith": arith,
            "mode": "perm", "word": "", "name": f"perm:{alphabet}:{arith}"}


def inverse(S):
    inv = [0] * 26
    for i, v in enumerate(S):
        inv[v] = i
    return inv


def letters_correct(S3, truth):
    """(exact letters of S3 placed as in truth, best count under a cyclic shift of the sum index, that shift)."""
    exact = sum(1 for a, b in zip(S3, truth) if a == b)
    best = max(((sum(1 for s in range(26) if S3[(s + t) % 26] == truth[s]), t) for t in range(26)), key=lambda x: x[0])
    return exact, best[0], best[1]


# ---------------------------------------------------------------- proxy: the n-gram distribution of the sum stream
def unigram(texts):
    c = Counter()
    for t in texts:
        c.update(rk.fold(t))
    n = sum(c.values()) + 26
    return [(c[x] + 1) / n for x in rk.A]


def sum_stream_counts(ptexts, ktexts, n, pairings, seed, arith="vig"):
    """n-gram counts of s = S1(p) (+/-) S2(k) with S1 = S2 = identity: the training plaintext texts and key texts, folded,
    added letter by letter mod 26 at `pairings` random relative offsets (an empirical convolution)."""
    rng = random.Random(seed)
    P = [[rk.IDX[ch] for ch in rk.fold(t)] for t in ptexts]
    K = [[rk.IDX[ch] for ch in rk.fold(t)] for t in ktexts]
    kall = [x for k in K for x in k]
    counts = Counter()
    for p in P:
        for _ in range(pairings):
            off = rng.randrange(len(kall))
            m = len(p)
            ks = kall[off:off + m]
            if len(ks) < m:
                ks = ks + kall[:m - len(ks)]
            if arith == "vig":
                s = [(a + b) % 26 for a, b in zip(p, ks)]
            elif arith == "beau":
                s = [(b - a) % 26 for a, b in zip(p, ks)]
            else:
                s = [(a - b) % 26 for a, b in zip(p, ks)]
            idx = 0
            mask = 26 ** n
            for i, v in enumerate(s):
                idx = (idx * 26 + v) % mask
                if i >= n - 1:
                    counts[idx] += 1
    return counts


def sum_table(counts, n, smooth):
    """flat list of log-probabilities over the 26^n n-grams (add-k smoothing)."""
    size = 26 ** n
    tot = sum(counts.values()) + smooth * size
    base = math.log(smooth / tot)
    T = [base] * size
    for idx, c in counts.items():
        T[idx] = math.log((c + smooth) / tot)
    return T


class Proxy:
    """delta-scored n-gram objective over the cipher messages: score(S3inv) = sum over every n-letter window of
    log T[c'_i .. c'_{i+n-1}] with c' = S3inv[c]. Windows never cross a message boundary."""

    def __init__(self, msgs, logT, n):
        self.n, self.T = n, logT
        self.win = []           # window id -> tuple of cipher ints
        self.by_letter = [[] for _ in range(26)]
        for m in msgs:
            c = [rk.IDX[x] for x in m]
            for i in range(len(c) - n + 1):
                w = tuple(c[i:i + n])
                wid = len(self.win)
                self.win.append(w)
                for x in set(w):
                    self.by_letter[x].append(wid)
        self.pow = [26 ** (n - 1 - j) for j in range(n)]

    def _idx(self, w, inv):
        idx = 0
        for x in w:
            idx = idx * 26 + inv[x]
        return idx

    def score(self, inv):
        T = self.T
        return sum(T[self._idx(w, inv)] for w in self.win)

    def partial(self, inv, letters):
        T = self.T
        wids = set()
        for x in letters:
            wids.update(self.by_letter[x])
        return sum(T[self._idx(self.win[wid], inv)] for wid in wids)


def sort_match_start(counts, q, r, arith="vig"):
    """S3 with the most frequent cipher letter written for the most probable sum, and so on down."""
    pc = [0.0] * 26
    for p in range(26):
        for k in range(26):
            s = (p + k) % 26 if arith == "vig" else ((k - p) % 26 if arith == "beau" else (p - k) % 26)
            pc[s] += q[p] * r[k]
    srank = sorted(range(26), key=lambda s: -pc[s])
    crank = sorted(range(26), key=lambda c: -counts[c])
    S3 = [0] * 26
    for s, c in zip(srank, crank):
        S3[s] = c
    return S3


def anneal(proxy, start_inv, evals, patience, rng, T0=None, cool=200.0, verbose=""):
    """simulated annealing over S3inv (cipher letter -> sum); swap (80 pct) or 3-cycle (20 pct); returns (best_inv,
    best_score, evaluations, T0)."""
    inv = list(start_inv)
    cur = proxy.score(inv)
    best, best_inv = cur, list(inv)
    if T0 is None:   # median |delta| of 200 random swaps from the start
        ds = []
        for _ in range(200):
            a, b = rng.sample(range(26), 2)
            old = proxy.partial(inv, (a, b))
            inv[a], inv[b] = inv[b], inv[a]
            ds.append(abs(proxy.partial(inv, (a, b)) - old))
            inv[a], inv[b] = inv[b], inv[a]
        ds.sort()
        T0 = max(ds[len(ds) // 2], 1e-3)
    T1 = T0 / cool
    since = 0
    n_eval = 0
    for it in range(evals):
        T = T0 * (T1 / T0) ** (it / max(1, evals - 1))
        if rng.random() < 0.8:
            a, b = rng.sample(range(26), 2)
            L = (a, b)
            old = proxy.partial(inv, L)
            inv[a], inv[b] = inv[b], inv[a]
            new = proxy.partial(inv, L)
            d = new - old
            if d >= 0 or rng.random() < math.exp(d / T):
                cur += d
            else:
                inv[a], inv[b] = inv[b], inv[a]
        else:
            a, b, c = rng.sample(range(26), 3)
            L = (a, b, c)
            old = proxy.partial(inv, L)
            va, vb, vc = inv[a], inv[b], inv[c]
            inv[a], inv[b], inv[c] = vb, vc, va
            new = proxy.partial(inv, L)
            d = new - old
            if d >= 0 or rng.random() < math.exp(d / T):
                cur += d
            else:
                inv[a], inv[b], inv[c] = va, vb, vc
        n_eval += 1
        if cur > best + 1e-9:
            best, best_inv, since = cur, list(inv), 0
        else:
            since += 1
            if since >= patience:
                break
    return best_inv, best, n_eval, T0


# ---------------------------------------------------------------- open-tableau beam (search=beam)
def open_beam(msgs, lmp, lmk, beam=2000, per_open=30, per_map=10, arith="vig"):
    """Two-stream beam decoder with the cipher-side permutation UNKNOWN: every hypothesis carries a partial mapping
    cipher letter -> sum s (injective) besides its plaintext and key contexts. At a cipher letter already mapped the
    options are the 26 (p, k) pairs on that sum line (as in running_key.beam_decode); at a letter's first occurrence
    every (p, k) pair whose sum is still free is an option and the hypothesis commits to it (the mapped set depends on
    the position only, so exactly 26 positions are open). Contexts reset at message boundaries, the mapping persists,
    so all messages inform S3. Word boundaries off. Returns (plain, S3inv list with -1 for letters never seen, score)."""
    assert lmp.alpha == rk.A and lmk.alpha == rk.A, "open_beam needs letter-only models (spaces off)"
    np_, nk = lmp.order - 1, lmk.order - 1
    EMPTY = tuple([-1] * 26)
    hyps = {("", "", EMPTY): (0.0, None, 0)}   # key -> (score, node, used bitmask); node = (p, k, parent)
    def kof(s, p):
        return (s - p) % 26 if arith == "vig" else ((s + p) % 26 if arith == "beau" else (p - s) % 26)
    def sof(p, k):
        return (p + k) % 26 if arith == "vig" else ((k - p) % 26 if arith == "beau" else (p - k) % 26)
    for m in msgs:
        # contexts reset, mapping kept: merge hypotheses that now coincide
        merged = {}
        for (pc, kc, mp), v in hyps.items():
            key = ("", "", mp)
            if key not in merged or v[0] > merged[key][0]:
                merged[key] = v
        hyps = merged
        for ch in m:
            cv = rk.IDX[ch]
            cand = []
            for (pc, kc, mp), (sc, node, used) in hyps.items():
                dp, dk = lmp.dist(pc), lmk.dist(kc)
                s_known = mp[cv]
                if s_known >= 0:
                    loc = [(dp[p] + dk[kof(s_known, p)], p, kof(s_known, p)) for p in range(26)]
                    if per_map < 26:
                        loc = heapq.nlargest(per_map, loc)
                    for v, p, k in loc:
                        cand.append((sc + v, p, k, pc, kc, mp, used, -1))
                else:
                    loc = []
                    for p in range(26):
                        dpp = dp[p]
                        for k in range(26):
                            if used >> sof(p, k) & 1:
                                continue
                            loc.append((dpp + dk[k], p, k))
                    loc = heapq.nlargest(per_open, loc)
                    for v, p, k in loc:
                        cand.append((sc + v, p, k, pc, kc, mp, used, sof(p, k)))
            if len(cand) > beam * 2:
                cand = heapq.nlargest(beam * 2, cand, key=lambda x: x[0])
            else:
                cand.sort(key=lambda x: -x[0])
            new = {}
            for s, p, k, pc, kc, mp, used, snew in cand:
                if snew >= 0:
                    mpl = list(mp)
                    mpl[cv] = snew
                    mp2 = tuple(mpl)
                    used2 = used | (1 << snew)
                else:
                    mp2, used2 = mp, used
                key = ((pc + rk.A[p])[-np_:] if np_ else "", (kc + rk.A[k])[-nk:] if nk else "", mp2)
                if key in new:
                    continue
                new[key] = (s, (p, k, node), used2)
                if len(new) >= beam:
                    break
            hyps = new
    (pc, kc, mp), (sc, node, used) = max(hyps.items(), key=lambda kv: kv[1][0])
    ps = []
    while node is not None:
        ps.append(rk.A[node[0]])
        node = node[2]
    return "".join(reversed(ps)), list(mp), sc


def complete_inv(inv, rng):
    """fill the cipher letters the open beam never saw with the unused sums, at random."""
    inv = list(inv)
    free = [s for s in range(26) if s not in inv]
    rng.shuffle(free)
    for c in range(26):
        if inv[c] < 0:
            inv[c] = free.pop()
    return inv


# ---------------------------------------------------------------- decoder-guided refinement (refine=ROUNDS)
def refine_decoder(proxy, S3, lmp, lmk, sel, a, rng, truth=None):
    """greedy local search on the DECODER objective from S3: each round proposes the `refine_props` swaps with the
    least bad proxy delta (the proxy as a proposal filter, the brief's option 2) plus `refine_rand` random swaps,
    scores each by the beam decoder at anneal settings on `sel`, and accepts the best if it improves; stops after a
    round with no improvement or after `refine` rounds. Prints which kind of proposal won each round, so the log says
    whether the filter earns its keep. Returns (S3, joint ll/letter, rounds used)."""
    def dec(S):
        return rk.decode_message(sel, lmp, lmk, perm_tabula(None, None, S, a.arith), a.anneal_beam, a.per_hyp, False,
                                 a.spaces)["ll_joint"]
    cur = dec(S3)
    rounds = 0
    for r in range(a.refine):
        rounds += 1
        inv = inverse(S3)
        base = {}
        deltas = []
        for x in range(26):
            for y in range(x + 1, 26):
                old = proxy.partial(inv, (x, y))
                inv[x], inv[y] = inv[y], inv[x]
                deltas.append((proxy.partial(inv, (x, y)) - old, x, y))
                inv[x], inv[y] = inv[y], inv[x]
        deltas.sort(reverse=True)
        props = [("proxy", x, y) for _, x, y in deltas[:a.refine_props]]
        while len(props) < a.refine_props + a.refine_rand:
            x, y = rng.sample(range(26), 2)
            if not any(p[1:] == (x, y) or p[1:] == (y, x) for p in props):
                props.append(("random", x, y))
        best = None
        for kind, x, y in props:
            inv2 = inverse(S3)
            inv2[x], inv2[y] = inv2[y], inv2[x]
            S = inverse(inv2)
            v = dec(S)
            if best is None or v > best[0]:
                best = (v, S, kind)
        line = f"  refine round {r + 1}: current {cur:.3f}, best proposal {best[0]:.3f} ({best[2]})"
        if best[0] > cur + 1e-9:
            cur, S3 = best[0], best[1]
            if truth:
                e, bs, t = letters_correct(S3, truth)
                line += f"; accepted, S3 letters correct {e}/26 exact, {bs}/26 under shift {t}"
            else:
                line += "; accepted"
            print(line, flush=True)
        else:
            print(line + "; no improvement, stop", flush=True)
            break
    return S3, cur, rounds


# ---------------------------------------------------------------- family interface
def load_kcorpus(path):
    if not path:
        return None
    p = path if os.path.isabs(path) else os.path.join(ROOT, path)
    return [rk.read_text(b) for b in rk.list_books([p])]


def _models(ptexts, ktexts, order, discount, spaces):
    f, al = (rk.fold_sp, rk.AS) if spaces else (rk.fold, rk.A)
    lmp = rk.LM([f(t) for t in ptexts], order, discount, al)
    lmk = lmp if ktexts is None else rk.LM([f(t) for t in ktexts], order, discount, al)
    return lmp, lmk


def make_control(spec, seed, corpora, params):
    a = _p(params)
    kc = load_kcorpus(a.kcorpus)
    if kc is None and len(corpora) < 3:
        raise SystemExit("permuted_tableau control needs three corpus texts, or a kcorpus= directory")
    if kc is not None and len(kc) < 2:
        raise SystemExit("permuted_tableau control needs at least two key-corpus texts (one is held out)")
    rng = random.Random(seed)
    idx = list(range(len(corpora)))
    rng.shuffle(idx)
    pi = idx[0]
    if kc is None:
        ktext, ktrain = corpora[idx[1]], [corpora[i] for i in idx[2:]]
        ptrain = ktrain
    else:
        kidx = list(range(len(kc)))
        rng.shuffle(kidx)
        ktext, ktrain = kc[kidx[0]], [kc[i] for i in kidx[1:]]
        ptrain = [corpora[i] for i in idx[1:]]
    S3 = list(range(26))
    rng.shuffle(S3)
    tab = perm_tabula(None, None, S3, a.arith)
    ptext, kt = rk.fold(corpora[pi]), rk.fold(ktext)
    lengths = params.get("lengths") or [params["N"]]
    msgs, plains, keys = [], [], []
    for n in lengths:
        P, _ = draw_window(ptext, n, rng.randrange(10 ** 6))
        K, _ = draw_window(kt, n, rng.randrange(10 ** 6))
        msgs.append([rk.A[rk.encipher(tab, rk.IDX[x], rk.IDX[y])] for x, y in zip(P, K)])
        plains.append(P)
        keys.append(K)
    _STATE["ktrain"] = ktrain
    _STATE["truth"] = S3
    _STATE["truth_key"] = "".join(keys)
    print(f"  control seed {seed}: S3 {tab['alphabet']} (uniform random of 26!), arith {a.arith}; "
          f"key corpus {'kcorpus' if kc else 'plain corpus'} book held out")
    return msgs, "".join(plains), ptrain


def solve(cipher_msgs, spec, seed, restarts, corpora, params):
    a = _p(params)
    ktrain = _STATE.pop("ktrain", None)
    truth = _STATE.pop("truth", None)
    truth_key = _STATE.pop("truth_key", None)
    if ktrain is None:
        ktrain = load_kcorpus(a.kcorpus)
    ktexts = ktrain if ktrain is not None else list(corpora)
    rng = random.Random(seed * 1009 + 7)
    t0 = time.time()
    counts = sum_stream_counts(corpora, ktexts, a.proxy_order, a.pairings, seed, a.arith)
    logT = sum_table(counts, a.proxy_order, a.smooth)
    proxy = Proxy(cipher_msgs, logT, a.proxy_order)
    q, r = unigram(corpora), unigram(ktexts)
    cc = Counter("".join("".join(m) for m in cipher_msgs))
    cc = [cc.get(x, 0) for x in rk.A]
    S3_sort = sort_match_start(cc, q, r, a.arith)
    print(f"  proxy: order {a.proxy_order}, {sum(counts.values())} sum-stream n-grams from {a.pairings} pairings, "
          f"{len(proxy.win)} target windows; built in {time.time() - t0:.1f}s")
    if truth:
        e, bs, t = letters_correct(S3_sort, truth)
        print(f"  start: sort-match S3 letters correct {e}/26 exact, {bs}/26 under shift {t}")
    if a.search == "beam":
        # open-tableau beam: the mapping is searched inside the decoder (see open_beam); the proxy is not used
        lmp_o, lmk_o = _models(corpora, ktrain, a.open_order, a.discount, False)
        tb = time.time()
        plain_o, inv_o, sc_o = open_beam(cipher_msgs, lmp_o, lmk_o, a.open_beam, a.per_open, a.per_map, a.arith)
        n_o = sum(len(m) for m in cipher_msgs)
        inv_o = complete_inv(inv_o, rng)
        S3_o = inverse(inv_o)
        line = (f"  open beam (order {a.open_order}, beam {a.open_beam}, per_open {a.per_open}, per_map {a.per_map}): "
                f"joint ll/letter {sc_o / n_o:.3f} in {time.time() - tb:.0f}s; S3 {''.join(rk.A[c] for c in S3_o)}")
        if truth:
            e, bs, t = letters_correct(S3_o, truth)
            line += f"; S3 letters correct {e}/26 exact, {bs}/26 under shift {t}"
        print(line)
        results = [(sc_o / n_o, S3_o)]
        per_eval = (time.time() - tb)
        cands = results
    # stage 2: chains
    results = [] if a.search != "beam" else results
    t1 = time.time()
    for ch in range(a.chains if a.search != "beam" else 0):
        if ch == 0 and a.start == "sort":
            start = inverse(S3_sort)
        else:
            S = list(range(26))
            rng.shuffle(S)
            start = inverse(S)
        inv, sc, ne, T0 = anneal(proxy, start, a.evals, a.patience, rng)
        S3 = inverse(inv)
        line = f"  chain {ch + 1}: proxy {sc:.1f} after {ne} evals (T0 {T0:.2f})"
        if truth:
            e, bs, t = letters_correct(S3, truth)
            line += f"; S3 letters correct {e}/26 exact, {bs}/26 under shift {t}"
        print(line)
        results.append((sc, S3))
    if a.search != "beam":
        per_eval = (time.time() - t1) / max(1, len(results) * a.evals)
    results.sort(key=lambda x: -x[0])
    distinct, seen = [], set()
    for sc, S3 in results:
        key = tuple(S3)
        if key not in seen:
            seen.add(key)
            distinct.append((sc, S3))
    cands = distinct[:a.rescore]
    # stage 3: beam rescoring
    lmp_a, lmk_a = _models(corpora, ktrain, a.anneal_order, a.discount, a.spaces)
    sel = "".join(cipher_msgs[min(a.sel_msg, len(cipher_msgs) - 1)])[:a.anneal_len]
    best = None
    tb = time.time()
    for sc, S3 in cands:
        tab = perm_tabula(None, None, S3, a.arith)
        d = rk.decode_message(sel, lmp_a, lmk_a, tab, a.anneal_beam, a.per_hyp, False, a.spaces)
        print(f"  rescore: {tab['alphabet']} proxy {sc:.1f} -> msg{a.sel_msg + 1}[:{len(sel)}] joint ll/letter {d['ll_joint']:.3f}")
        if best is None or d["ll_joint"] > best[0]:
            best = (d["ll_joint"], tab, sc)
    eval_s = (time.time() - tb) / max(1, len(cands))
    print(f"  decoder evaluation at anneal settings (order {a.anneal_order}, beam {a.anneal_beam}, {len(sel)} letters): "
          f"{eval_s:.2f}s each; proxy evaluation {per_eval * 1000:.2f} ms")
    _, tab, sc_proxy = best
    if a.refine > 0:
        S3_r, ll_r, rounds = refine_decoder(proxy, tab["S3"], lmp_a, lmk_a, sel, a, rng, truth)
        print(f"  refine: {rounds} rounds, msg{a.sel_msg + 1}[:{len(sel)}] joint ll/letter {best[0]:.3f} -> {ll_r:.3f}")
        tab = perm_tabula(None, None, S3_r, a.arith)
    lmp, lmk = _models(corpora, ktrain, a.order, a.discount, a.spaces)
    out, keys, tot, n = [], [], 0.0, 0
    for m in cipher_msgs:
        c = "".join(m)
        d = rk.decode_message(c, lmp, lmk, tab, a.beam, a.per_hyp, False, a.spaces)
        out.append(d["plain"])
        keys.append(d["key"])
        tot += d["ll_joint"] * len(c)
        n += len(c)
    info = {"tabula": tab["name"], "alphabet": tab["alphabet"], "S3": tab["S3"], "proxy_score": round(sc_proxy, 2),
            "proxy_order": a.proxy_order, "chains": a.chains, "evals": a.evals, "order": a.order, "beam": a.beam,
            "spaces": a.spaces, "anneal_order": a.anneal_order, "anneal_beam": a.anneal_beam, "anneal_len": a.anneal_len,
            "decoder_eval_seconds": round(eval_s, 2), "proxy_eval_ms": round(per_eval * 1000, 3),
            "ll_joint_per_letter": round(tot / max(1, n), 4), "key_stream": keys}
    if truth:
        e, bs, t = letters_correct(tab["S3"], truth)
        info["S3_letters_correct"] = [e, bs, t]
        info["S3_sort_letters_correct"] = list(letters_correct(S3_sort, truth))
        info["truth_S3"] = truth
        print(f"  winner S3 letters correct {e}/26 exact, {bs}/26 under shift {t}")
    if truth_key is not None:
        info["truth_key"] = truth_key
    return "".join(out), tot / max(1, n), info


def score_recovery(plain, truth):
    n = max(1, len(truth))
    return sum(1 for x, y in zip(plain, truth) if x == y) / n
