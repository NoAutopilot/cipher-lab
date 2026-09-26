"""wordcode: letter-or-word nomenclator inside sign runs -- each sign type stands for one letter or one whole word.

Design (LANE B12 bSALW, 26 Sept 2026, for fr2933-salviati-1525, DSN sec. 5 b): the remaining untested design after the
syllabary ladder closed. A sign type maps to EITHER one Italian letter (a homophone of the alphabet) OR one Italian
word (a code, from a candidate list: the corpus's `vocab` commonest words, plus a `<NAME>` wildcard for a proper-name
or title code that no word list carries). Which types may be codes is --param codes=marked (every type carrying a
superscript mark: the target's 918 marked tokens are the natural candidates), codes=topk:N (the N most frequent types)
or codes=all; a code-capable type may still decode to a letter (codeletters=1, default).
A run is a word sequence: every sign run begins and ends at a word boundary (the plain boxes between runs are whole
words, not transcribed), and a code word is bounded on both sides; word boundaries inside a letter stretch stay
invisible, as on the leaf.
Score (higher is better) over the stream of each run, written with a boundary letter `w` (unused in folded Italian) at
the run edges and around every code word: trigrams with no `w` are scored by an unspaced letter model, trigrams that
touch a `w` by a spaced model (the segmentation term: is this a plausible word end / word start), plus a word-unigram
prior `wprior` * log(p(word) * vocab) per code occurrence, a fixed `namepen` per <NAME> occurrence (at most `names`
types may hold it), and the homophonic_anneal KL unigram term over the letters. Anneal over the type -> value map,
one type per move, only the runs holding that type rescored; `restarts` restarts, the best kept.

Control (rule 3): a window of the held-out corpus cut into words; the target's own run lengths (one run per spec
ciphertext line) are filled with whole words, the plain gaps between runs withhold whole words (the row_pattern's own
plain-run box counts, one word per box, cycled); every word in the control's code vocabulary (the corpus's top-k
words, k bisected so the code token share matches the target's code-capable token share) is one token, every other
word is spelt in letters; code words take the target's own code-capable type names by frequency rank, letters the
target's other type names by homophone allotment (syllabary.alloc); then the CM3 measured error mix
(syllabary.measured_error) at `err` (default 0.064, the target's measured rate). Recovery is TOKEN accuracy (a
deleted token counts wrong, an inserted one in neither numerator nor denominator), reported blended and per class
(letter tokens vs code tokens, CLAUDE.md rule 3 unbalanced-class paragraph) on stdout and in the decode info.

params: codes (marked), vocab (1000), err (0.064), iters (40000), order (3), uni_weight (0.5), wprior (0.5),
names (8), namepen (-6.0), codeletters (0: a code-capable type decodes only to a word or <NAME>; 1 lets it be a letter).
Calibration on the 0%-error control, seed 1, one restart, 20k iters (bSALW, 26 Sept 2026): the KL letter term taken
over code-word letters as well read 0.00-0.20; over letter types only at uni_weight 0.5 it read 0.72, at 1.0 0.20;
codeletters=1 read 0.00-0.44 (letter/word swaps stall the anneal). The defaults are those settings. Test: python3 tools/tests/test_wordcode.py"""
import math, random, re
from collections import Counter
import homophonic_anneal as ha
from families import draw_window
from families.syllabary import alloc, measured_error, split_tok

DESCRIPTION = ("letter-or-word nomenclator: each sign type = one letter or one whole word/<NAME> code (--param "
               "codes=marked vocab=1000 err=0.064); runs bounded by words; control on the target's run lengths; token accuracy per class")
NAME = "<NAME>"
_STASH = {}


def _p(params, k, d):
    return type(d)(params.get(k, d))


def words_of(text):
    """Folded word list (j->i, v->u, accents dropped; w, unused in Italian, cannot occur)."""
    return [w for w in (ha.fold(x) for x in text.split()) if w and "w" not in w]


def code_capable(types_freq, spec_str):
    """The set of type names that may be codes: marked (a mark string after ^), topk:N, all."""
    s = spec_str or "marked"
    if s == "all":
        return {t for t, _ in types_freq}
    if s.startswith("topk:"):
        return {t for t, _ in types_freq[:int(s[5:])]}
    return {t for t, _ in types_freq if split_tok(t)[1]}


def _gaps(spec):
    pat = spec.get("row_pattern") or ""
    g = [len(x) for x in re.findall(r"_+", pat)]
    return g or [2]


def make_control(spec, seed, corpora, params):
    N = params["N"]
    err = _p(params, "err", 0.064)
    rng = random.Random(seed + 7000)
    tmsgs = params.get("target_msgs") or [[]]
    ttoks = [t for m in tmsgs for t in m]
    types = Counter(ttoks).most_common()
    cap = code_capable(types, params.get("codes"))
    code_share = sum(n for t, n in types if t in cap) / max(1, len(ttoks))
    lengths = [len(m) for m in tmsgs] or [N]
    gaps = _gaps(spec)
    text = "\n".join(corpora)
    allw = words_of(text)
    # a window of words from the middle of the corpus (draw_window on the joined word string, cut at spaces)
    joined = " ".join(allw)
    n_chars = int(N * 9 + sum(gaps) * 8) + 2000
    win, rest = draw_window(joined, min(n_chars, len(joined) // 2), seed)
    ww = win.split()[1:-1]
    freq_rank = [w for w, _ in Counter(words_of(rest)).most_common()]

    n_codes = len([t for t, _ in types if t in cap])
    wrng = random.Random(seed + 7100)

    def lay(a):
        """Code vocabulary = the corpus's top-a words plus rarer words of the window drawn at random until the
        vocabulary present in the control reaches the target's own code-type count (a real nomenclator lists
        particles and common words but also names and substantives that occur once in a letter)."""
        vocab = set(freq_rank[:a])
        pool = sorted({w for w in ww if w not in vocab})
        wrng.seed(seed + 7100)
        wrng.shuffle(pool)
        for _ in range(3):
            toks, runs, i, gi, n, li = [], [], 0, 0, 0, 0
            while n < N:
                L = lengths[li % len(lengths)]; li += 1
                cur = []
                while i < len(ww):
                    w = ww[i]
                    tw = [w] if w in vocab else list(w)
                    if cur and len(cur) + len(tw) > L:
                        break
                    cur += tw; i += 1
                    if len(cur) >= L:
                        break
                toks += cur; runs.append(len(cur)); n += len(cur)
                i += gaps[gi % len(gaps)]; gi += 1
                if i >= len(ww):
                    raise SystemExit("wordcode: control word window too short for the target's runs")
            present = {t for t in toks if len(t) > 1 or t in vocab}
            short = n_codes - len(present)
            if short <= 0 or not pool:
                break
            used = set(ww[:i])
            add = [w for w in pool if w in used and w not in vocab][:short]
            vocab |= set(add)
        return toks[:N], runs, vocab

    lo, hi = 0, min(len(freq_rank), n_codes)
    for _ in range(12):  # bisect the common-word part a on the code token share
        a = (lo + hi) // 2
        toks, runs, vocab = lay(a)
        sh = sum(1 for t in toks if len(t) > 1 or t in vocab) / len(toks)
        if abs(sh - code_share) < 0.01 or hi - lo <= 1:
            break
        lo, hi = (a, hi) if sh < code_share else (lo, a)
    tot = 0
    for q, L in enumerate(runs):
        if tot + L >= N:
            runs = runs[:q] + [N - tot]; break
        tot += L
    is_code = [(t in vocab) for t in toks]
    # names: code words by frequency rank -> code-capable target types by frequency rank; letters -> the rest
    cw = Counter(t for t, c in zip(toks, is_code) if c).most_common()
    cnames = [t for t, _ in types if t in cap]
    lnames = [(t, n) for t, n in types if t not in cap]
    extra = 0
    cmap = {}
    for j, (w, _) in enumerate(cw):
        if j < len(cnames):
            cmap[w] = cnames[j]
        else:
            extra += 1
            cmap[w] = f"X{extra}^c"
    lf = Counter(t for t, c in zip(toks, is_code) if not c)
    lhom = alloc(lnames, {a: lf.get(a, 0) for a in ha.ALPHA if a != "w"}) if lnames else {}
    seq = []
    for t, c in zip(toks, is_code):
        if c:
            seq.append(cmap[t])
        else:
            n_, w_ = zip(*lhom[t])
            seq.append(rng.choices(n_, w_)[0])
    counts, tix = {}, list(range(len(seq)))
    if err:
        codes_f = Counter(split_tok(t)[0] for t in ttoks).most_common()
        seq, tix, counts = measured_error(seq, types, codes_f, err, random.Random(seed + 9500))
    starts, acc = set(), 0
    for L in runs:
        starts.add(acc); acc += L
    msgs, cur = [], []
    for s_, j in zip(seq, tix):
        if j is not None and j in starts and cur:
            msgs.append(cur); cur = []
        cur.append(s_)
    if cur:
        msgs.append(cur)
    _STASH.clear()
    _STASH.update({"truth_tokens": toks, "truth_code": is_code, "truth_index": tix, "err": err, "vocab_k": len(vocab), "common_a": a,
                   "code_share": round(sum(is_code) / len(toks), 3), "target_code_share": round(code_share, 3),
                   "code_types": len(cw), "extra_code_names": extra, "control_types": len(set(seq)), **counts})
    # the solver trains on the rest (window removed); cap-names travel with the messages via params
    return msgs, "".join(toks), [rest]


class Scorer:
    def __init__(self, corpora, order, vocab_n):
        self.mu = ha.Model(corpora, order)
        self.ms = ha.Model([re.sub(r"\s+", "w", " ".join(words_of(t))) for t in corpora], order)
        self.o = order
        wc = Counter(w for t in corpora for w in words_of(t))
        tot = sum(wc.values())
        self.words = [w for w, _ in wc.most_common(vocab_n)]
        self.wlog = {w: math.log(wc[w] / tot * vocab_n) for w in self.words}
        self.wweights = [wc[w] for w in self.words]

    def ngrams(self, s):
        o, lu, ls = self.o, self.mu.logp, self.ms.logp
        return sum((ls if "w" in s[i:i + o] else lu)(s[i:i + o]) for i in range(len(s) - o + 1))


def _run_string(run, key):
    out = ["w"]
    for t in run:
        v = key[t]
        if len(v) == 1:
            out.append(v)
        else:
            if out[-1] != "w":
                out.append("w")
            if v != NAME:
                out.append(v); out.append("w")
    if out[-1] != "w":
        out.append("w")
    return "".join(out)


def solve(cipher_msgs, spec, seed, restarts, corpora, params):
    order, iters = _p(params, "order", 3), _p(params, "iters", 40000)
    uni_w, wprior = _p(params, "uni_weight", 0.5), _p(params, "wprior", 0.5)
    names, namepen = _p(params, "names", 8), _p(params, "namepen", -6.0)
    codeletters = str(params.get("codeletters", "0")) not in ("0", "no", "false")
    sc = Scorer(corpora, order, _p(params, "vocab", 1000))
    runs = [list(m) for m in cipher_msgs]
    tf = Counter(t for r in runs for t in r)
    types = sorted(tf)
    ttoks = [t for m in params.get("target_msgs") or [] for t in m]
    cap = code_capable(Counter(ttoks).most_common(), params.get("codes")) if ttoks else set()
    if params.get("codes", "marked") == "marked":
        cap |= {t for t in types if split_tok(t)[1]}  # inserted/confused types in a control carry their own mark
    letters = [a for a in ha.ALPHA if a != "w"]
    lw = [sc.mu.freq[a] for a in letters]
    lf = {a: math.log(sc.mu.freq[a]) for a in letters}
    inruns = {t: sorted({i for i, r in enumerate(runs) if t in r}) for t in types}
    capl = [t for t in types if t in cap]
    rng = random.Random(seed)

    def run_score(i, key):
        s = _run_string(runs[i], key)
        v = sc.ngrams(s)
        for t in runs[i]:
            x = key[t]
            if x == NAME:
                v += namepen
            elif len(x) > 1:
                v += wprior * sc.wlog[x]
        return v

    def letter_counts(key):
        c = Counter()
        for t in types:
            if len(key[t]) == 1:  # letter types only: a code word's letters are not in the letter stream's KL
                c[key[t]] += tf[t]
        return c

    xlx = lambda c: c * math.log(c) if c > 0 else 0.0

    def kl(c):
        n = sum(c.values())
        return sum(v * math.log(n * sc.mu.freq[a] / v) for a, v in c.items() if v > 0 and a in sc.mu.freq)

    results = []
    for r in range(restarts):
        key = {}
        for t in types:
            if t in cap and rng.random() < 0.5:
                key[t] = rng.choices(sc.words, sc.wweights)[0]
            else:
                key[t] = rng.choices(letters, lw)[0]
        rs = [run_score(i, key) for i in range(len(runs))]
        cnt = letter_counts(key)
        nname = sum(1 for t in types if key[t] == NAME)
        cur = sum(rs) + uni_w * kl(cnt)
        best, bestkey = cur, dict(key)
        for it in range(iters):
            T = 4.0 * (1 - it / iters) + 0.02
            if capl and rng.random() < 0.5:
                t = rng.choice(capl)
                u = rng.random()
                if u < 0.6:
                    new = rng.choices(sc.words, sc.wweights)[0]
                elif u < 0.68 and (nname < names or key[t] == NAME):
                    new = NAME
                elif codeletters:
                    new = rng.choices(letters, lw)[0]
                else:
                    continue
            else:
                t = rng.choice(types)
                if t in cap and not codeletters:
                    continue
                new = rng.choices(letters, lw)[0]
            old = key[t]
            if new == old:
                continue
            key[t] = new
            idx = inruns[t]
            nr = [run_score(i, key) for i in idx]
            dn = sum(nr) - sum(rs[i] for i in idx)
            m = tf[t]
            c2 = Counter(cnt)
            if len(old) == 1:
                c2[old] -= m
            if len(new) == 1:
                c2[new] += m
            du = kl(c2) - kl(cnt) if (len(old) > 1 or len(new) > 1) else None
            if du is None:
                du = m * (lf[new] - lf[old]) - (xlx(cnt[new] + m) - xlx(cnt[new]) + xlx(cnt[old] - m) - xlx(cnt[old]))
            d = dn + uni_w * du
            if d >= 0 or rng.random() < math.exp(d / T):
                cur += d
                for i, v in zip(idx, nr):
                    rs[i] = v
                cnt = c2
                nname += (new == NAME) - (old == NAME)
                if cur > best:
                    best, bestkey = cur, dict(key)
            else:
                key[t] = old
        results.append((best, bestkey))
    results.sort(key=lambda x: -x[0])
    best, key = results[0]
    dec_tokens = [key[t] for r in runs for t in r]
    lines = []
    for r in runs:
        parts, buf = [], ""
        for t in r:
            x = key[t]
            if len(x) == 1:
                buf += x
            else:
                if buf:
                    parts.append(buf); buf = ""
                parts.append("_" if x == NAME else x.upper())
        if buf:
            parts.append(buf)
        lines.append(" ".join(parts))
    _STASH["dec_tokens"] = dec_tokens
    _STASH["solver_vocab"] = sc.wlog
    _STASH["dec_lines"] = lines
    nsym = sum(len(r) for r in runs)
    ncode = sum(1 for x in dec_tokens if len(x) > 1)
    info = {"restart_scores": [round(x[0], 1) for x in results], "score_per_token": round(best / max(1, nsym), 4),
            "code_tokens_decoded": ncode, "name_types": sum(1 for v in key.values() if v == NAME),
            "code_words": Counter(x for x in dec_tokens if len(x) > 1 and x != NAME).most_common(25),
            **{k: v for k, v in _STASH.items() if k not in ("truth_tokens", "truth_index", "truth_code", "dec_tokens", "dec_lines", "solver_vocab")}}
    dec = "".join(x for x in dec_tokens if x != NAME)
    return dec, best, info


def score_recovery(plain, truth):
    """Token accuracy on the control stash, blended; the per-class numbers are printed and kept in _STASH."""
    tt, tc, tix, dt = (_STASH.get(k) for k in ("truth_tokens", "truth_code", "truth_index", "dec_tokens"))
    if not (tt and tix and dt and len(dt) == len(tix)):
        n = max(1, len(truth))
        return sum(1 for a, b in zip(plain, truth) if a == b) / n
    ok = [False] * len(tt)
    for i, j in enumerate(tix):
        if j is not None and dt[i] == tt[j]:
            ok[j] = True
    nl = sum(1 for c in tc if not c); nc = sum(tc)
    al = sum(1 for o, c in zip(ok, tc) if o and not c) / max(1, nl)
    ac = sum(1 for o, c in zip(ok, tc) if o and c) / max(1, nc)
    voc = _STASH.get("solver_vocab") or {}
    reach = sum(1 for t, c in zip(tt, tc) if c and t in voc) / max(1, nc)  # code tokens the word list can read at all
    _STASH["per_class"] = {"letters": round(al, 3), "codes": round(ac, 3), "n_letters": nl, "n_codes": nc,
                           "codes_in_wordlist": round(reach, 3)}
    print(f"  per class: letters {al:.3f} (n={nl}) codes {ac:.3f} (n={nc}, {reach:.3f} in the word list); vocab k={_STASH.get('vocab_k')} "
          f"code share {_STASH.get('code_share')} (target {_STASH.get('target_code_share')}), code types "
          f"{_STASH.get('code_types')}, control K {_STASH.get('control_types')}")
    return sum(ok) / len(tt)


def split_decode(dec, msgs):
    lines = _STASH.get("dec_lines")
    if not lines or len(lines) != len(msgs):
        return None
    return lines
