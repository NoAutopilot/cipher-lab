"""keyed_running_key: family B', a running (book) key through a KEYED tableau, wrapping tools/running_key.py
(GOLD-2C, 25 Sept 2026). Bourdeau's 15 Sept 2026 unigram test and GOLD-2A's two-stream decoder both excluded the
standard tableau; this family covers the case both left open: c = S3(S1(p) + S2(k)) with the permutations built
from one keyword-mixed alphabet M (running_key.mixed_tabula: modes plain, key, both, full; arithmetic vig, beau,
varbeau). Restricted to keyword-mixed alphabets because that is what an agent could carry in his head.

Attack, two stages, both blind:
  1. RANK keywords by the multinomial log-likelihood of the pooled ciphertext letter counts under the letter
     distribution the tableau predicts, conv(plain unigram, key unigram) permuted by the tableau (26x26 per
     candidate, so a word list of thousands x 4 modes is seconds). Candidates: every distinct keyword-mixed alphabet
     from words of length minlen..maxlen occurring >= minocc times in the corpora given (plaintext corpus + key
     corpus), the `nwords` most frequent per corpus set, plus the identity alphabet (the standard tableau) as a
     reference row.
  2. DECODE the `top` ranked tableaux with running_key's two-stream beam decoder (LM_p from the plaintext corpus,
     LM_k from the key corpus; order, beam, spaces as params) on the first message, keep the tableau with the best
     joint log-likelihood per letter, and decode every message under it. The decode's pooled joint log-likelihood
     per letter is the family score (higher is better; compare with GOLD-2A's one-time-key noise band).

Control (rule 3): a plaintext window per target message length from one corpus book, enciphered under a window of a
DIFFERENT book (from `kcorpus` if given, else another corpus book) through a tableau whose keyword is drawn from the
same word list and whose mode is drawn from the four; both books held out of the models. So the control measures
the ranking plus the decode given that the keyword is in the list; a keyword outside the list (a name, a phrase, a
transposition-block alphabet) is outside this family's reach and is said so in HYPOTHESES.md.

params (--param k=v): kcorpus=DIR (key-language corpus; default: the plaintext corpus), arith=vig|beau|varbeau,
order=6, beam=300, per_hyp=10, spaces=1, top=3, nwords=4000, minlen=4, maxlen=12, minocc=3, sel_msg=0 (which
message picks the winner in stage 2), modes=plain,key,both,full, wordcorpus=DIR[,DIR] (draw the stage-1 keyword
list from these files/directories instead of the plaintext + key corpora; default None = unchanged, words come
from corpus + kcorpus -- for a keyword an agent from a different country could have carried, e.g. an English list).
Needs >= 2 corpus texts (3 when kcorpus is the plaintext corpus). About 1-3 minutes per seed at beam 300."""
import math, os, random, re, types
from collections import Counter
import running_key as rk
from families import draw_window, TOOLS

DESCRIPTION = ("keyed-tableau running key (keyword-mixed alphabet, 4 modes; stage 1 unigram-count ranking, stage 2 "
               "running_key.py two-stream beam on the top candidates; control = plain book x key book x random keyword)")
ROOT = os.path.dirname(TOOLS)
_STATE = {}


def _p(params):
    return types.SimpleNamespace(
        kcorpus=params.get("kcorpus"), arith=params.get("arith", "vig"), order=int(params.get("order", 6)),
        discount=float(params.get("discount", 0.9)), beam=int(params.get("beam", 300)),
        per_hyp=int(params.get("per_hyp", 10)), spaces=bool(int(params.get("spaces", 1))),
        top=int(params.get("top", 3)), nwords=int(params.get("nwords", 4000)), minlen=int(params.get("minlen", 4)),
        maxlen=int(params.get("maxlen", 12)), minocc=int(params.get("minocc", 3)), sel_msg=int(params.get("sel_msg", 0)),
        modes=tuple(params.get("modes", "plain,key,both,full").split(",")), wordcorpus=params.get("wordcorpus"))


def load_kcorpus(path):
    if not path:
        return None
    p = path if os.path.isabs(path) else os.path.join(ROOT, path)
    return [rk.read_text(b) for b in rk.list_books([p])]


def load_wordcorpus(spec):
    """comma-separated files/directories the stage-1 keyword list is drawn from, in place of corpus + kcorpus
    (--param wordcorpus=DIR[,DIR]); None (default) keeps the old behaviour."""
    if not spec:
        return None
    paths = [p if os.path.isabs(p) else os.path.join(ROOT, p) for p in (s.strip() for s in spec.split(",")) if p]
    return [rk.read_text(b) for b in rk.list_books(paths)]


def word_list(texts, a):
    """distinct keyword-mixed alphabets from the most frequent words of the texts, with the word that gave each."""
    words = Counter()
    for t in texts:
        c = Counter(w for w in re.findall(r"[^\W\d_]+", t.lower()) if a.minlen <= len(w) <= a.maxlen)
        for w, n in c.most_common(a.nwords):
            if n >= a.minocc:
                words[rk.fold(w)] += n
    seen, out = {}, []
    for w, n in words.most_common():
        if len(w) < a.minlen:
            continue
        M = rk.keyword_alphabet(w)
        if M not in seen:
            seen[M] = w
            out.append(w)
    return out


def unigram(texts):
    c = Counter()
    for t in texts:
        c.update(rk.fold(t))
    n = sum(c.values()) + 26
    return [(c[x] + 1) / n for x in rk.A]


def stage1(counts, q, r, words, a):
    """rank (word, mode) by the multinomial log-likelihood of the counts, in nats above uniform."""
    n = sum(counts)
    base = n * math.log(1 / 26)
    rows = []
    for w in [""] + list(words):  # "" = the identity alphabet, the standard tableau, as a reference
        for mode in (("plain",) if w == "" else a.modes):
            t = rk.mixed_tabula(w, mode, a.arith)
            pc = [0.0] * 26
            enc = t["enc"]
            for p in range(26):
                qp = q[p]
                row = enc[p]
                for k in range(26):
                    pc[row[k]] += qp * r[k]
            ll = sum(counts[c] * math.log(pc[c]) for c in range(26) if counts[c]) - base
            rows.append((ll, w, mode))
    rows.sort(reverse=True)
    return rows


def _models(ptexts, ktexts, a):
    f, al = (rk.fold_sp, rk.AS) if a.spaces else (rk.fold, rk.A)
    lmp = rk.LM([f(t) for t in ptexts], a.order, a.discount, al)
    lmk = lmp if ktexts is None else rk.LM([f(t) for t in ktexts], a.order, a.discount, al)
    return lmp, lmk


def make_control(spec, seed, corpora, params):
    a = _p(params)
    kc = load_kcorpus(a.kcorpus)
    if kc is None and len(corpora) < 3:
        raise SystemExit("keyed_running_key control needs three corpus texts, or a kcorpus= directory")
    if kc is not None and len(kc) < 2:
        raise SystemExit("keyed_running_key control needs at least two key-corpus texts (one is held out)")
    rng = random.Random(seed)
    idx = list(range(len(corpora)))
    rng.shuffle(idx)
    pi = idx[0]
    if kc is None:
        ki = idx[1]
        ktext, ktrain = corpora[ki], [corpora[i] for i in idx[2:]]
        ptrain = ktrain
    else:
        kidx = list(range(len(kc)))
        rng.shuffle(kidx)
        ktext, ktrain = kc[kidx[0]], [kc[i] for i in kidx[1:]]
        ptrain = [corpora[i] for i in idx[1:]]
    words = word_list(load_wordcorpus(a.wordcorpus) or (list(corpora) + (kc or [])), a)
    word = rng.choice(words)
    mode = rng.choice(a.modes)
    tab = rk.mixed_tabula(word, mode, a.arith)
    ptext, kt = rk.fold(corpora[pi]), rk.fold(ktext)
    lengths = params.get("lengths") or [params["N"]]
    msgs, plains = [], []
    for n in lengths:
        P, _ = draw_window(ptext, n, rng.randrange(10 ** 6))
        K, _ = draw_window(kt, n, rng.randrange(10 ** 6))
        msgs.append([rk.A[rk.encipher(tab, rk.IDX[x], rk.IDX[y])] for x, y in zip(P, K)])
        plains.append(P)
    _STATE["ktrain"] = ktrain
    _STATE["words"] = words
    _STATE["truth"] = (word, mode)
    print(f"  control seed {seed}: keyword {word!r} mode {mode} arith {a.arith} (alphabet {tab['alphabet']}); "
          f"{len(words)} candidate alphabets; key corpus {'kcorpus' if kc else 'plain corpus'} book held out")
    return msgs, "".join(plains), ptrain


def solve(cipher_msgs, spec, seed, restarts, corpora, params):
    a = _p(params)
    ktrain = _STATE.pop("ktrain", None)
    truth = _STATE.pop("truth", None)
    if ktrain is None:
        ktrain = load_kcorpus(a.kcorpus)
    words = _STATE.pop("words", None) or word_list(load_wordcorpus(a.wordcorpus) or (list(corpora) + (ktrain or [])), a)
    q = unigram(corpora)
    r = unigram(ktrain) if ktrain is not None else q
    counts = Counter("".join("".join(m) for m in cipher_msgs))
    counts = [counts.get(x, 0) for x in rk.A]
    ranked = stage1(counts, q, r, words, a)
    ident = next(row for row in ranked if row[1] == "")
    top = [row for row in ranked if row[1] != ""][:a.top]
    print(f"  stage 1: {len(ranked)} candidates; top {[(round(ll, 1), w, m) for ll, w, m in top]}; "
          f"standard tableau {ident[0]:.1f} nats (rank {ranked.index(ident) + 1})")
    if truth:
        pos = next((i + 1 for i, row in enumerate(ranked) if (row[1], row[2]) == truth), None)
        print(f"  stage 1: true keyword {truth} ranked {pos}")
    lmp, lmk = _models(corpora, ktrain, a)
    sel = "".join(cipher_msgs[min(a.sel_msg, len(cipher_msgs) - 1)])
    best = None
    for ll1, w, mode in top:
        t = rk.mixed_tabula(w, mode, a.arith)
        d = rk.decode_message(sel, lmp, lmk, t, a.beam, a.per_hyp, False, a.spaces)
        print(f"  stage 2: {t['name']} stage1 {ll1:.1f} -> msg{a.sel_msg + 1} joint ll/letter {d['ll_joint']:.3f}")
        if best is None or d["ll_joint"] > best[0]:
            best = (d["ll_joint"], t, ll1)
    _, tab, ll1 = best
    out, tot, n = [], 0.0, 0
    keys = []
    for m in cipher_msgs:
        c = "".join(m)
        d = rk.decode_message(c, lmp, lmk, tab, a.beam, a.per_hyp, False, a.spaces)
        out.append(d["plain"])
        keys.append(d["key"])
        tot += d["ll_joint"] * len(c)
        n += len(c)
    info = {"tabula": tab["name"], "alphabet": tab["alphabet"], "stage1_nats": round(ll1, 2),
            "stage1_top": [(round(ll, 2), w, m) for ll, w, m in top], "standard_tableau_nats": round(ident[0], 2),
            "candidates": len(ranked), "order": a.order, "beam": a.beam, "spaces": a.spaces,
            "ll_joint_per_letter": round(tot / max(1, n), 4), "key_stream": keys}
    return "".join(out), tot / max(1, n), info


def score_recovery(plain, truth):
    n = max(1, len(truth))
    return sum(1 for x, y in zip(plain, truth) if x == y) / n
