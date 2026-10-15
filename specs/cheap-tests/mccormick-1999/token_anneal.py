#!/usr/bin/env python3
"""token_anneal.py -- mccormick-1999 cheap test 3 (spec cheap_tests_in_order[2]): token/nomenclator test.

LANE B3 worker bMCC4, 25 Sept 2026. Tokenizes both notes the way they are written (hyphen/slash/comma/'?'
as documented separators, parentheses stripped as brackets not characters), treats each distinct
multi-letter token (NCBE, the -RSE family, WLD, ...) as a candidate code-word and each single letter as
itself (no search), then does a small simulated anneal over the token vocabulary actually present,
assigning each distinct multi-letter token type to an English word so as to maximise a character 4-gram
log-likelihood of the assembled text (tools/judge_plaintext.py's own NgramModel over tools/data's 'en'
corpus -- pg1661_holmes.txt + pg2701_mobydick.txt -- so this test's language model is the same one the
judge itself uses, no separate model to keep consistent).

Matched control (rule 3): draws a same-length token stream from real English prose (same corpus), applies
the SAME per-position token-kind sequence as the real target (code / number / single-letter, in the
target's own order) and the SAME code-mapping scheme -- a word occupying a 'code' slot is replaced by a
freshly generated unique 4-letter placeholder, except that words drawn from the target's own frequent-word
list get one SHARED placeholder reused every time they recur (mirrors NCBE's 11 occurrences and the
handful of other repeated tokens; the other ~90 real code tokens are singletons, so most control code
tokens are singletons too). 'number' slots get a random 1-3 digit literal (no natural word underlies a
number slot); the two 'single-letter' slots get 'a' or 'I' (the only single-letter English words). No
vowel-dropped share is used: the target's own non-code share (number 10.6% + single-letter 1.5% = 12.1%
of 132 tokens) is covered exactly by the number/single-letter slots above, leaving nothing for a
vowel-dropped remainder -- documented per the brief's "document the choice."

False-positive floor: the target's own 116 code-token OCCURRENCES (not just the 99 distinct types) with
their order shuffled among the code slots (numbers/letters stay put), 3 shuffles, same solver.

Usage: python3 token_anneal.py --out results.json

Control length sweep (MCC-SWEEP, LANE DEFAULT-A1-1840, 11 Oct 2026): `--control-only --n-tokens N --seeds 1,2,3
--iters-per-type 80 --fast` runs only the matched control at N tokens (the target's per-position kind sequence tiled
to length N, same code scheme), with iterations scaled to the control's code-type count (8,000 iters / 99 types ~ 80
per type, bMCC4's setting) and an incremental scorer (`--fast`, same objective: mean 4-gram log10 P over the folded
text, checked against the full scorer by `--selftest`). Adds per-run diagnostics: token-weighted recovery, the
pool ceiling (share of truth types whose word is in the anneal's candidate pool) and recovery on repeated
(shared-code) types. No target run in this mode. Default behaviour without these flags is unchanged.

Word-level code-word anneal (MCC-WORD, LANE DEFAULT-A2-2209-14, 14 Oct 2026): `--control-only --objective wordbigram
--n-tokens N --seeds 1,2,3 --null [--lm heldout|insample] [--pool 1000] [--sweeps 200]` scores whole-word bigrams (top
`--pool` words, numbers/single letters break the chain) and Gibbs-anneals each code type over the pool on the total
log-prob scale; same control generator; reports the found total against the truth's total (search vs objective).
PREREG and results: ciphers/mccormick-1999/PREREG-MCC-WORD.md, NOTES.md "MCC-WORD". Test: tools/tests/test_mcc_wordbigram.py.

Abbreviation / consonant-skeleton model (MCC-SKEL, LANE DEFAULT-A1-0206-15, 15 Oct 2026): `--skeleton --scheme drop|keepfinal
--pool 3000 --n-list 132,500,2000 --seeds 1,2,3 --nulls 40 [--target]` reads each code token as one or more word skeletons
(first letter + consonants; keepfinal also keeps a final vowel) by lattice Viterbi under the same word-bigram LM, UNK at a
per-letter cost; control = skeletons of held-out prose on the target's kind sequence with run-on groups fitted to its token
length; nulls: code-token order (control read) and letters shuffled across tokens (coverage). PREREG and results:
ciphers/mccormick-1999/PREREG-MCC-SKEL.md, NOTES.md "MCC-SKEL". Test: tools/tests/test_mcc_skeleton.py.
"""
import argparse
import json
import math
import os
import random
import re
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "tools"))
import judge_plaintext as jp  # noqa: E402

CIPHER_FILE = ROOT / "specs" / "cheap-tests" / "mccormick-1999" / "cipher_both_notes.txt"
SPEC_FILE = ROOT / "specs" / "mccormick-1999.json"
CORPORA = jp.LANG_CORPORA["en"]
FREQ_N = 60          # how many "frequent" real-corpus words get a shared, reused placeholder in the control
POOL_N = 350          # candidate word pool size for the anneal's proposal moves
ITERS = 3000
RESTARTS = 2

# ---------------------------------------------------------------- tokenizer (shared: real target + control)


def tokenize(text):
    """Return [(kind, VALUE)] in reading order. kind in {'code','number','letter'}.
    Separators: whitespace, and within a whitespace chunk: '-', '/', ',', '?' (documented in the spec's
    alphabet field) plus '(' ')' which are stripped as brackets, not kept as characters."""
    toks = []
    for line in text.splitlines():
        if not line.strip():
            continue
        line = re.sub(r"[()\[\]{}]", " ", line)
        for chunk in line.split():
            for piece in re.split(r"[-/,?]", chunk):
                if not piece:
                    continue
                if re.fullmatch(r"[0-9.]+", piece):
                    toks.append(("number", piece))
                elif re.fullmatch(r"[A-Za-z]", piece):
                    toks.append(("letter", piece.upper()))
                else:
                    toks.append(("code", piece.upper()))
    return toks


# ---------------------------------------------------------------- corpus / vocab


def corpus_words():
    words = []
    for p in CORPORA:
        t = jp.read_corpus(p)
        words += re.findall(r"[A-Za-z]+", t)
    return [w.lower() for w in words]


def build_vocab(words):
    freq = Counter(words)
    pool_words = [w for w, _ in freq.most_common(POOL_N)]
    pool_weights = [freq[w] for w in pool_words]
    frequent = set(w for w, _ in freq.most_common(FREQ_N))
    return pool_words, pool_weights, frequent


# ---------------------------------------------------------------- control construction


def random_code(rng, used):
    while True:
        c = "".join(rng.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ") for _ in range(4))
        if c not in used:
            used.add(c)
            return c


def build_control(kind_seq, words, frequent, rng, used_codes):
    """kind_seq: the real target's [(kind, _)] with values ignored, positions/kinds kept.
    Returns (toks, truth) where toks is [(kind, VALUE)] for the control and truth maps each code VALUE
    (the placeholder) to the real English word it stands for."""
    start = rng.randrange(0, len(words) - len(kind_seq) - 1)
    draw = words[start:start + len(kind_seq)]
    word_to_code = {}
    truth = {}
    toks = []
    for (kind, _), w in zip(kind_seq, draw):
        if kind == "number":
            toks.append(("number", str(rng.randint(1, 999))))
        elif kind == "letter":
            toks.append(("letter", rng.choice("AI")))
        else:  # code
            if w in frequent and w in word_to_code:
                code = word_to_code[w]
            elif w in frequent:
                code = random_code(rng, used_codes)
                word_to_code[w] = code
            else:
                code = random_code(rng, used_codes)
            truth[code] = w
            toks.append(("code", code))
    return toks, truth


# ---------------------------------------------------------------- anneal


def assemble(toks, assign):
    parts = []
    for kind, v in toks:
        if kind == "code":
            parts.append(assign.get(v, v.lower()))
        elif kind == "letter":
            parts.append(v)
        else:
            parts.append(v)  # numbers: fold() drops non-letters, harmless
    return " ".join(parts)


def anneal_solve(toks, model, pool_words, pool_weights, rng, iters=ITERS, restarts=RESTARTS):
    code_types = sorted(set(v for k, v in toks if k == "code"))
    best_assign, best_score = None, -1e18
    for r in range(restarts):
        assign = {c: rng.choices(pool_words, weights=pool_weights)[0] for c in code_types}
        cur = model.score(jp.fold(assemble(toks, assign)))
        local_best, local_assign = cur, dict(assign)
        T0, T1 = 2.0, 0.05
        for it in range(iters):
            T = T0 * (T1 / T0) ** (it / max(1, iters - 1))
            c = rng.choice(code_types)
            old = assign[c]
            new = rng.choices(pool_words, weights=pool_weights)[0]
            if new == old:
                continue
            assign[c] = new
            sc = model.score(jp.fold(assemble(toks, assign)))
            if sc >= cur or rng.random() < math.exp((sc - cur) / T):
                cur = sc
                if cur > local_best:
                    local_best, local_assign = cur, dict(assign)
            else:
                assign[c] = old
        if local_best > best_score:
            best_score, best_assign = local_best, local_assign
    return best_score, best_assign


class FastScorer:
    """Incremental version of model.score(fold(assemble(toks, assign))): keeps the total log10 sum and the folded
    length, and re-scores only the spans a code type's occurrences can affect (each occurrence plus >= n-1 fixed
    letters after it; spans of the same type that touch are merged). Same objective as anneal_solve."""

    def __init__(self, toks, model, assign):
        self.m = model
        self.n = model.n
        self.toks = toks
        self.code_at = [v if k == "code" else None for k, v in toks]
        self.fixed = [None if k == "code" else jp.fold(v) for k, v in toks]
        self.assign = dict(assign)
        self.wf = {}  # folded word cache
        self.occ = {}
        for i, c in enumerate(self.code_at):
            if c is not None:
                self.occ.setdefault(c, []).append(i)
        full = jp.fold(assemble(toks, self.assign))
        self.L = len(full)
        self.tot = self._sum(full, 0)

    def _spans(self, c):
        """token spans [a, b] whose letters can change score when c changes: each occurrence plus tokens up to
        n-1 letters of other tokens after it (lengths read now; they do not change during c's move)."""
        spans = []
        for i in self.occ[c]:
            j, got = i, 0
            while got < self.n - 1 and j + 1 < len(self.toks):
                j += 1
                if self.code_at[j] != c:
                    got += len(self._tokstr(j))
            if spans and i <= spans[-1][1] + 1:
                spans[-1][1] = max(spans[-1][1], j)
            else:
                spans.append([i, j])
        return spans

    def _w(self, w):
        f = self.wf.get(w)
        if f is None:
            f = self.wf[w] = jp.fold(w)
        return f

    def _tokstr(self, i):
        c = self.code_at[i]
        return self.fixed[i] if c is None else self._w(self.assign.get(c, c.lower()))

    def _lp(self, g):
        m = self.m
        return math.log10((m.c.get(g, 0) + m.k) / (m.ctx.get(g[:-1], 0) + m.V * m.k))

    def _sum(self, s, ctxlen):
        """sum of log10 P over n-grams ending at positions >= max(ctxlen, n-1) of s."""
        n = self.n
        return sum(self._lp(s[i - n + 1:i + 1]) for i in range(max(ctxlen, n - 1), len(s)))

    def _left(self, a):
        out, i = "", a - 1
        while i >= 0 and len(out) < self.n - 1:
            out = self._tokstr(i) + out
            i -= 1
        return out[-(self.n - 1):] if len(out) > self.n - 1 else out

    def _span_contrib(self, a, b):
        left = self._left(a)
        body = "".join(self._tokstr(i) for i in range(a, b + 1))
        return self._sum(left + body, len(left)), len(body)

    def score(self):
        cnt = self.L - self.n + 1
        return -9.9 if self.L < self.n else self.tot / cnt

    def propose(self, c, new):
        """apply assign[c]=new; return the new mean score (state updated; call undo(c, old, d) to revert)."""
        old = self.assign.get(c)
        spans = self._spans(c)
        before = [self._span_contrib(a, b) for a, b in spans]
        self.assign[c] = new
        after = [self._span_contrib(a, b) for a, b in spans]
        dtot = sum(x[0] for x in after) - sum(x[0] for x in before)
        dL = sum(x[1] for x in after) - sum(x[1] for x in before)
        self.tot += dtot
        self.L += dL
        return self.score(), (old, dtot, dL)

    def undo(self, c, info):
        old, dtot, dL = info
        self.assign[c] = old
        self.tot -= dtot
        self.L -= dL


def anneal_solve_fast(toks, model, pool_words, pool_weights, rng, iters=ITERS, restarts=RESTARTS, temp_scale="mean"):
    """anneal_solve with FastScorer; identical move set, schedule and acceptance rule. temp_scale='total' (MCC-SWEEP
    addendum) multiplies the mean-score change by the scored n-gram count before the Metropolis test, so the same
    2.0 -> 0.05 schedule acts on total log10 P (a move's size no longer shrinks as 1/length); objective unchanged."""
    code_types = sorted(set(v for k, v in toks if k == "code"))
    best_assign, best_score = None, -1e18
    for r in range(restarts):
        assign = {c: rng.choices(pool_words, weights=pool_weights)[0] for c in code_types}
        fs = FastScorer(toks, model, assign)
        cur = fs.score()
        local_best, local_assign = cur, dict(fs.assign)
        T0, T1 = 2.0, 0.05
        for it in range(iters):
            T = T0 * (T1 / T0) ** (it / max(1, iters - 1))
            c = rng.choice(code_types)
            new = rng.choices(pool_words, weights=pool_weights)[0]
            if new == fs.assign[c]:
                continue
            sc, info = fs.propose(c, new)
            d = sc - cur
            if temp_scale == "total":
                d *= max(1, fs.L - fs.n + 1)
            if sc >= cur or rng.random() < math.exp(d / T):
                cur = sc
                if cur > local_best:
                    local_best, local_assign = cur, dict(fs.assign)
            else:
                fs.undo(c, info)
        if local_best > best_score:
            best_score, best_assign = local_best, local_assign
    return best_score, best_assign


def tile_kinds(real_toks, n):
    """the target's per-position kind sequence, repeated to length n (values ignored by build_control)."""
    return [real_toks[i % len(real_toks)] for i in range(n)]


def diagnostics(assign, truth, ctoks, pool_words):
    pool = set(pool_words)
    occ = Counter(v for k, v in ctoks if k == "code")
    n_occ = sum(occ.values())
    tok_ok = sum(occ[c] for c, w in truth.items() if assign.get(c, "").lower() == w.lower())
    rep = [c for c in truth if occ[c] >= 2]
    rep_ok = sum(1 for c in rep if assign.get(c, "").lower() == truth[c].lower())
    return {"token_recovery": tok_ok / n_occ if n_occ else 0.0,
            "pool_ceiling_tokens": sum(occ[c] for c, w in truth.items() if w in pool) / n_occ if n_occ else 0.0,
            "pool_ceiling_types": sum(1 for w in truth.values() if w in pool) / len(truth) if truth else 0.0,
            "repeated_types": len(rep), "repeated_type_share": len(rep) / len(truth) if truth else 0.0,
            "repeated_type_recovery": rep_ok / len(rep) if rep else None,
            "code_occurrences": n_occ}


def selftest(model, pool_words, pool_weights, real_toks, words, frequent):
    rng = random.Random(7)
    ctoks, _ = build_control(tile_kinds(real_toks, 400), words, frequent, rng, set())
    for toks in (real_toks, ctoks):
        codes = sorted(set(v for k, v in toks if k == "code"))
        assign = {c: rng.choice(pool_words) for c in codes}
        fs = FastScorer(toks, model, assign)
        for _ in range(300):
            c = rng.choice(codes)
            sc, info = fs.propose(c, rng.choice(pool_words + ["a", "i", "zz"]))
            if rng.random() < 0.3:
                fs.undo(c, info)
            ref = model.score(jp.fold(assemble(toks, fs.assign)))
            if abs(ref - fs.score()) > 1e-9:
                print(f"SELFTEST FAIL: fast {fs.score()} vs full {ref}", file=sys.stderr)
                return 1
    print("selftest OK: FastScorer equals the full scorer on 600 random moves", file=sys.stderr)
    return 0


def recovery_fraction(assign, truth):
    if not truth:
        return 0.0
    ok = sum(1 for c, w in truth.items() if assign.get(c, "").lower() == w.lower())
    return ok / len(truth)


# ---------------------------------------------------------------- word-level code-word anneal (MCC-WORD, 14 Oct 2026)

HELDOUT_EN = [ROOT / "tools" / "data" / "en" / f for f in ("pg1342_pride.txt", "pg64317_gatsby.txt", "pg76_huckfinn.txt")]
WB_LAMBDA = 0.8      # Jelinek-Mercer weight of the bigram term against the unigram


def corpus_words_from(paths):
    words = []
    for p in paths:
        words += re.findall(r"[A-Za-z]+", jp.read_corpus(p))
    return [w.lower() for w in words]


class WordBigram:
    """Whole-word bigram model over a closed vocabulary: the top `pool` corpus words, plus UNK (any other word) and
    BND (a boundary: start of text, and every number or single-letter token, which break the word chain on both the
    control and the target). log P(w|v) = log(lam P_ml(w|v) + (1-lam) P_uni(w)), add-one unigram. Dense matrix
    L[v, w] (natural log), v, w in 0..V+1 (V = UNK, V+1 = BND)."""

    def __init__(self, words, pool, lam=WB_LAMBDA, allowed=None):
        import numpy as np
        freq = Counter(words)
        if allowed is None:
            self.pool = [w for w, _ in freq.most_common(pool)]
        else:  # MCC-GREGG: the top `pool` corpus words that pass the lexicon filter (lexicon_allows)
            self.pool = [w for w, _ in freq.most_common() if allowed(w)][:pool]
        self.idx = {w: i for i, w in enumerate(self.pool)}
        V = len(self.pool)
        self.UNK, self.BND, self.size = V, V + 1, V + 2
        ids = [self.idx.get(w, self.UNK) for w in words]
        uni = np.ones(self.size)
        for i in ids:
            uni[i] += 1
        uni[self.BND] = 1.0
        uni /= uni.sum()
        big = np.zeros((self.size, self.size))
        np.add.at(big, (np.array(ids[:-1]), np.array(ids[1:])), 1.0)
        rows = big.sum(axis=1, keepdims=True)
        ml = np.divide(big, rows, out=np.zeros_like(big), where=rows > 0)
        lam_row = np.where(rows > 0, lam, 0.0)
        self.L = np.log(lam_row * ml + (1 - lam_row) * uni[None, :])
        self.weights = [freq[w] for w in self.pool]

    def seq_ids(self, toks, assign):
        """token list -> word-id list (code tokens through assign; other tokens BND)."""
        out = []
        for k, v in toks:
            out.append(self.idx.get(assign.get(v, ""), self.UNK) if k == "code" else self.BND)
        return out

    def total(self, toks, assign):
        ids = [self.BND] + self.seq_ids(toks, assign)
        return float(sum(self.L[a, b] for a, b in zip(ids[:-1], ids[1:]) if b != self.BND))


def load_lexicon(path):
    """MCC-GREGG: a word list file (one lower-case word per line) -> set."""
    return set(x.strip().lower() for x in Path(path).read_text().split() if x.strip())


def lexicon_lemmas(w):
    """the word itself and its regular-inflection lemmas (fixed in PREREG-MCC-GREGG.md): -s, -es, -ies>y, -ed, -d,
    -ied>y, -ing, -ing>+e, -ly, -ily>y, with a doubled final consonant undone after -ed/-ing (stopped > stop)."""
    out = {w}
    for suf, rep in (("ies", "y"), ("ied", "y"), ("ily", "y"), ("es", ""), ("s", ""), ("ed", ""), ("ed", "e"),
                     ("ing", ""), ("ing", "e"), ("ly", "")):
        if w.endswith(suf) and len(w) - len(suf) >= 2:
            b = w[:-len(suf)]
            out.add(b + rep)
            if suf in ("ed", "ing") and len(b) >= 3 and b[-1] == b[-2] and b[-1] not in "aeiou":
                out.add(b[:-1])
    return out


def lexicon_allows(lex):
    """MCC-GREGG pool filter: a corpus word enters the pool iff it or one of its lexicon_lemmas is in the lexicon."""
    return lambda w: any(x in lex for x in lexicon_lemmas(w))


def wordbigram_solve(toks, wb, rng, sweeps=200, restarts=2, t0=3.0, t1=0.05, init=None):
    """Heat-bath (Gibbs) annealing over code types: each type's word is resampled from softmax(dscore/T) over the
    whole pool, dscore = the exact total log-prob of the text with that type set to each candidate (others fixed);
    T geometric t0 -> t1 over `sweeps`, then one greedy sweep. Objective = WordBigram.total (natural log, total scale)."""
    import numpy as np
    nprng = np.random.default_rng(rng.randrange(2 ** 31))
    codes = sorted(set(v for k, v in toks if k == "code"))
    pos = {}
    for i, (k, v) in enumerate(toks):
        if k == "code":
            pos.setdefault(v, []).append(i)
    is_code = [k == "code" for k, _ in toks]
    vals = [v for _, v in toks]
    V = len(wb.pool)
    Lp = wb.L[:, :V]          # candidate columns (pool words only)
    diag = np.diag(wb.L)[:V]
    w = np.array(wb.weights, dtype=float)
    w /= w.sum()
    best_a, best_s = None, -1e300
    for r in range(restarts):
        cur = {c: int(nprng.choice(V, p=w)) for c in codes}
        if init:
            cur.update({c: wb.idx[init[c]] for c in codes if init.get(c) in wb.idx})

        def wid(i):
            return cur[vals[i]] if is_code[i] else wb.BND

        def cand_scores(c):
            s = np.zeros(V)
            for i in pos[c]:
                prev_same = i > 0 and is_code[i - 1] and vals[i - 1] == c
                if prev_same:
                    s += diag
                else:
                    s += Lp[wid(i - 1) if i > 0 else wb.BND]
                if i + 1 < len(toks):
                    nxt_same = is_code[i + 1] and vals[i + 1] == c
                    if not nxt_same and is_code[i + 1]:
                        s += wb.L[:V, wid(i + 1)]
            return s

        nsw = sweeps + 1
        for sw in range(nsw):
            greedy = sw == sweeps
            T = t0 * (t1 / t0) ** (sw / max(1, sweeps - 1))
            order = list(codes)
            rng.shuffle(order)
            for c in order:
                s = cand_scores(c)
                if greedy:
                    cur[c] = int(np.argmax(s))
                else:
                    z = (s - s.max()) / T
                    p = np.exp(z)
                    p /= p.sum()
                    cur[c] = int(nprng.choice(V, p=p))
        assign = {c: wb.pool[cur[c]] for c in codes}
        sc = wb.total(toks, assign)
        if sc > best_s:
            best_s, best_a = sc, assign
    return best_s, best_a


def wordbigram_sweep(a, real_toks, words, frequent):
    """MCC-WORD control sweep (PREREG-MCC-WORD.md): bMCC4's control generator unchanged, the word-bigram solver."""
    import time
    lm_paths = HELDOUT_EN if a.lm == "heldout" else HELDOUT_EN + list(CORPORA)
    wb = WordBigram(corpus_words_from(lm_paths), a.pool)
    n = a.n_tokens or len(real_toks)
    kinds_seq = tile_kinds(real_toks, n)
    runs, used = [], set()
    for seed in [int(x) for x in a.seeds.split(",")]:
        crng = random.Random(1000 + seed)
        ctoks, truth = build_control(kinds_seq, words, frequent, crng, used)
        t = time.time()
        sc, asg = wordbigram_solve(ctoks, wb, crng, a.sweeps, a.restarts)
        row = {"seed": seed, "n_tokens": n, "code_types": len(truth), "score": sc,
               "recovery": recovery_fraction(asg, truth), "secs": round(time.time() - t, 1)}
        row.update(diagnostics(asg, truth, ctoks, wb.pool))
        row["truth_total"] = wb.total(ctoks, truth)
        if a.null:
            srng = random.Random(2000 + seed)
            ps = [i for i, (k, _) in enumerate(ctoks) if k == "code"]
            vs = [ctoks[i][1] for i in ps]
            srng.shuffle(vs)
            stoks = list(ctoks)
            for i, v in zip(ps, vs):
                stoks[i] = ("code", v)
            _, sa = wordbigram_solve(stoks, wb, srng, a.sweeps, a.restarts)
            row["null_recovery"] = recovery_fraction(sa, truth)
            row["null_token_recovery"] = diagnostics(sa, truth, stoks, wb.pool)["token_recovery"]
        runs.append(row)
        print(json.dumps(row), file=sys.stderr)
    m = lambda key: sum(r[key] for r in runs) / len(runs)  # noqa: E731
    out = {"mode": "wordbigram-control", "lm": a.lm, "pool_size": a.pool, "sweeps": a.sweeps, "restarts": a.restarts,
           "n_tokens": n, "runs": runs, "recovery_mean": m("recovery"), "token_recovery_mean": m("token_recovery"),
           "pool_ceiling_types_mean": m("pool_ceiling_types"), "pool_ceiling_tokens_mean": m("pool_ceiling_tokens"),
           "gate": {"threshold": a.gate, "met": m("recovery") >= a.gate}}
    if a.null:
        nt = [r["null_token_recovery"] for r in runs]
        out["null_token_recovery_max"] = max(nt)
        out["token_read"] = out["token_recovery_mean"] >= a.gate and min(r["token_recovery"] for r in runs) > max(nt)
    print(json.dumps({k: out[k] for k in out if k != "runs"}))
    if a.out:
        Path(a.out).write_text(json.dumps(out, indent=1))
    return 0 if out.get("token_read", out["gate"]["met"]) else 3


# ---------------------------------------------------------------- abbreviation / consonant-skeleton model (MCC-SKEL)

VOWELS = set("AEIOU")


def skeleton(word, scheme="drop"):
    """Consonant skeleton of a word: upper case, first letter kept, every later vowel dropped, runs of one letter
    collapsed (would -> WLD, letter -> LTR). scheme 'keepfinal' also keeps the word's last letter when it is a vowel
    (house -> HSE, there -> THRE)."""
    w = word.upper()
    out = [w[0]]
    for i, ch in enumerate(w[1:], 1):
        if ch in VOWELS and not (scheme == "keepfinal" and i == len(w) - 1):
            continue
        if ch != out[-1]:
            out.append(ch)
    return "".join(out)


def build_skel_control(kind_seq, words, rng, scheme, p_join):
    """Matched control for the skeleton design: a contiguous word stream (same draw as build_control) on the target's
    per-position kind sequence; each code slot carries one word's skeleton, and with probability p_join the next word's
    skeleton is written onto the same token (run-on groups, matching the target's mean letters per code token); number
    and single-letter slots as in build_control (the word under them is dropped). Returns (toks, truth) where truth[i]
    is the list of words under token i (None for non-code tokens)."""
    start = rng.randrange(0, len(words) - 4 * len(kind_seq) - 1)
    pos = start
    toks, truth = [], []
    for kind, _ in kind_seq:
        if kind == "number":
            toks.append(("number", str(rng.randint(1, 999)))); truth.append(None); pos += 1
        elif kind == "letter":
            toks.append(("letter", rng.choice("AI"))); truth.append(None); pos += 1
        else:
            grp = [words[pos]]; pos += 1
            while rng.random() < p_join:
                grp.append(words[pos]); pos += 1
            toks.append(("code", "".join(skeleton(w, scheme) for w in grp))); truth.append(grp)
    return toks, truth


class SkelDecoder:
    """Lattice Viterbi: each code token is segmented into one or more word skeletons (a word may not cross a token
    boundary), each segment read as a pool word with that skeleton or as UNK at a cost of `alpha` nats per letter;
    the path score is the WordBigram total (numbers and single letters are BND). Beam of `beam` previous-word states
    per position; at most `cands` words per skeleton (most frequent first)."""

    def __init__(self, wb, scheme="drop", alpha=3.0, beam=200, cands=10, maxlen=12, keyfn=None):
        self.wb, self.alpha, self.beam = wb, alpha, beam
        idx = {}
        for i, w in enumerate(wb.pool):  # pool is frequency-ordered
            s = keyfn(w) if keyfn else skeleton(w, scheme)
            if len(s) <= maxlen and len(idx.setdefault(s, [])) < cands:
                idx[s].append(i)
        self.idx, self.maxlen = idx, max(len(s) for s in idx if s)

    def decode(self, toks):
        import numpy as np
        L, UNK, BND = self.wb.L, self.wb.UNK, self.wb.BND
        cur = {BND: (0.0, None)}  # word id -> (score, backpointer node)
        for k, v in toks:
            if k != "code":
                w, (sc, bp) = max(cur.items(), key=lambda kv: kv[1][0])
                cur = {BND: (sc, ("tok", None, w, bp))}
                continue
            n = len(v)
            dp = [dict() for _ in range(n + 1)]
            dp[0] = cur
            for i in range(n):
                if not dp[i]:
                    continue
                items = sorted(dp[i].items(), key=lambda kv: -kv[1][0])[:self.beam]
                pid = np.array([p for p, _ in items]); psc = np.array([s for _, (s, _) in items])
                for j in range(i + 1, min(n, i + self.maxlen) + 1):
                    sub = v[i:j]
                    for w in self.idx.get(sub, []) + [UNK]:
                        tot = psc + L[pid, w] - (self.alpha * (j - i) if w == UNK else 0.0)
                        b = int(tot.argmax())
                        if w not in dp[j] or tot[b] > dp[j][w][0]:
                            dp[j][w] = (float(tot[b]), (sub, w, int(pid[b]), items[b][1][1]))
            cur = dp[n]
        w, (best, bp) = max(cur.items(), key=lambda kv: kv[1][0])
        segs = []  # walk back: list of (skeleton, word id) in reading order, '|' at token boundaries
        node = bp
        while node is not None:
            sub, wid, prev, nxt = node
            segs.append((sub, wid))
            node = nxt
        segs.reverse()
        return best, segs

    def words_per_token(self, toks, segs):
        """split the decoded segment list back into per-code-token word lists (None for non-code tokens)."""
        out, k = [], 0
        for kind, v in toks:
            if kind != "code":
                while k < len(segs) and segs[k][0] == "tok":
                    k += 1
                out.append(None)
                continue
            got, letters = [], 0
            while letters < len(v):
                while segs[k][0] == "tok":
                    k += 1
                sub, wid = segs[k]; k += 1
                got.append((sub, None if wid == self.wb.UNK else self.wb.pool[wid]))
                letters += len(sub)
            out.append(got)
        return out


def lcs(a, b):
    m = [[0] * (len(b) + 1) for _ in range(len(a) + 1)]
    for i in range(len(a)):
        for j in range(len(b)):
            m[i + 1][j + 1] = m[i][j] + 1 if a[i] == b[j] else max(m[i][j + 1], m[i + 1][j])
    return m[-1][-1]


def skel_stats(dec, toks, truth=None):
    best, segs = dec.decode(toks)
    per = dec.words_per_token(toks, segs)
    letters = sum(len(v) for k, v in toks if k == "code")
    covered = sum(len(s) for g in per if g for s, w in g if w is not None)
    row = {"score": best, "score_per_letter": best / letters, "coverage": covered / letters,
           "decode": " ".join("[" + "+".join(w or ("?" + s) for s, w in g) + "]" if g else v
                              for g, (k, v) in zip(per, toks))}
    if truth is not None:
        tw = sum(len(t) for t in truth if t)
        row["word_recovery"] = sum(lcs(t, [w for _, w in g]) for t, g in zip(truth, per) if t) / tw
        row["truth_in_pool"] = sum(1 for t in truth if t for w in t if w in dec.wb.idx) / tw
    return row


def shuffle_letters(toks, rng):
    """letter-shuffled null: all code letters permuted across the code tokens, each token keeping its length."""
    letters = [ch for k, v in toks if k == "code" for ch in v]
    rng.shuffle(letters)
    out, p = [], 0
    for k, v in toks:
        if k == "code":
            out.append(("code", "".join(letters[p:p + len(v)]))); p += len(v)
        else:
            out.append((k, v))
    return out


def shuffle_letters_keep_final(toks, rng):
    """position-keeping null (PREREG-MCC-SKEL addendum 2): each code token keeps its length and its last letter; all
    other code letters are permuted across the code tokens. Keeps the target's token-final E profile, breaks the rest."""
    inner = [ch for k, v in toks if k == "code" for ch in v[:-1]]
    rng.shuffle(inner)
    out, p = [], 0
    for k, v in toks:
        if k == "code":
            out.append(("code", "".join(inner[p:p + len(v) - 1]) + v[-1])); p += len(v) - 1
        else:
            out.append((k, v))
    return out


def shuffle_order(toks, truth, rng):
    """order-shuffled null: code tokens (with their truth) permuted among the code slots."""
    ps = [i for i, (k, _) in enumerate(toks) if k == "code"]
    perm = ps[:]
    rng.shuffle(perm)
    t2, tr2 = list(toks), list(truth)
    for i, j in zip(ps, perm):
        t2[i], tr2[i] = toks[j], truth[j]
    return t2, tr2


def match_p_join(real_toks, scheme, words, rng_seed=7):
    """p_join (grid 0.00-0.90, step 0.05) whose control mean letters per code token is nearest the target's."""
    tgt = [len(v) for k, v in real_toks if k == "code"]
    tmean = sum(tgt) / len(tgt)
    best = None
    for p in [x / 20 for x in range(19)]:
        ctoks, _ = build_skel_control(tile_kinds(real_toks, 2000), words, random.Random(rng_seed), scheme, p)
        c = [len(v) for k, v in ctoks if k == "code"]
        d = abs(sum(c) / len(c) - tmean)
        if best is None or d < best[0]:
            best = (d, p, sum(c) / len(c))
    return best[1], best[2], tmean


def skeleton_run(a, real_toks, words):
    """MCC-SKEL (PREREG-MCC-SKEL.md): control first at each N; target and its letter-shuffled null only with
    --target, and only if the control read at the target's own N (checked here, exit 3 otherwise)."""
    import time
    wb = WordBigram(corpus_words_from(HELDOUT_EN), a.pool)
    dec = SkelDecoder(wb, a.scheme, a.alpha, a.beam)
    p_join, cmean, tmean = match_p_join(real_toks, a.scheme, words)
    out = {"mode": "skeleton", "scheme": a.scheme, "pool_size": a.pool, "alpha": a.alpha, "beam": a.beam,
           "p_join": p_join, "control_mean_letters": cmean, "target_mean_letters": tmean, "controls": {}}
    print(json.dumps({k: out[k] for k in out if k != "controls"}), file=sys.stderr)
    seeds = [int(x) for x in a.seeds.split(",")]
    for n in [int(x) for x in a.n_list.split(",")]:
        runs = []
        for seed in seeds:
            crng = random.Random(1000 + seed)
            ctoks, truth = build_skel_control(tile_kinds(real_toks, n), words, crng, a.scheme, p_join)
            t = time.time()
            row = {"seed": seed, "n_tokens": n}
            r = skel_stats(dec, ctoks, truth); r.pop("decode")
            row.update(r)
            st, sr = shuffle_order(ctoks, truth, random.Random(2000 + seed))
            row["null_order_word_recovery"] = skel_stats(dec, st, sr)["word_recovery"]
            lnull = [skel_stats(dec, shuffle_letters(ctoks, random.Random(3000 + seed * 100 + i))) for i in range(a.nulls)]
            row["letter_null_coverage_max"] = max(x["coverage"] for x in lnull)
            row["letter_null_spl_max"] = max(x["score_per_letter"] for x in lnull)
            row["secs"] = round(time.time() - t, 1)
            runs.append(row)
            print(json.dumps(row), file=sys.stderr)
        mean = sum(r["word_recovery"] for r in runs) / len(runs)
        nmax = max(r["null_order_word_recovery"] for r in runs)
        read = mean >= a.gate and min(r["word_recovery"] for r in runs) > nmax
        out["controls"][str(n)] = {"runs": runs, "word_recovery_mean": mean, "null_order_max": nmax, "read": read}
        print(json.dumps({"n": n, "word_recovery_mean": mean, "null_order_max": nmax, "read": read}))
    if a.target:
        n0 = str(len(real_toks))
        c0 = out["controls"].get(n0, {})
        power = bool(c0) and all(r["coverage"] > r["letter_null_coverage_max"] for r in c0["runs"])
        out["coverage_power_at_target_n"] = power
        if not (c0.get("read") or (a.target_on_power and power)):
            out["target"] = "not run: control did not read at the target's own N"
        else:
            tr = skel_stats(dec, real_toks)
            ln = [skel_stats(dec, shuffle_letters(real_toks, random.Random(5000 + i))) for i in range(a.nulls)]
            tr["letter_null_coverage"] = sorted(x["coverage"] for x in ln)
            tr["letter_null_spl"] = sorted(x["score_per_letter"] for x in ln)
            if a.null_keep_final:
                kf = [skel_stats(dec, shuffle_letters_keep_final(real_toks, random.Random(6000 + i))) for i in range(a.nulls)]
                tr["keepfinal_null_coverage"] = sorted(x["coverage"] for x in kf)
                tr["keepfinal_null_spl"] = sorted(x["score_per_letter"] for x in kf)
                tr["coverage_above_keepfinal_null_max"] = tr["coverage"] > max(tr["keepfinal_null_coverage"])
                tr["spl_above_keepfinal_null_max"] = tr["score_per_letter"] > max(tr["keepfinal_null_spl"])
            tr["coverage_above_null_max"] = tr["coverage"] > max(tr["letter_null_coverage"])
            tr["spl_above_null_max"] = tr["score_per_letter"] > max(tr["letter_null_spl"])
            out["target"] = tr
        print(json.dumps(out["target"] if isinstance(out["target"], str) else
                         {k: v for k, v in out["target"].items() if k != "decode"}))
    if a.out:
        Path(a.out).write_text(json.dumps(out, indent=1))
    ok = all(c["read"] for c in out["controls"].values())
    return 0 if ok else 3


# ---------------------------------------------------------------- MCC-SUFX: suffix-mark abbreviation model

SUFX_CLASSES = ["ing", "ed", "ly", "s", "e", "y", "d", "t", "n", "r", "other"]
SUFX_MARKS = ["", "E", "SE", "BE"]   # PREREG-MCC-SUFX: the target's token-final endings of length 1-2 seen >= 10 times, plus no mark


def suffix_class(word):
    """(base, class): the word's ending stripped by fixed rules, longest first -- inflections ing/ed/ly/s(es), then the
    single final letters e/y/d/t/n/r; 'other' (base = the whole word) when no rule applies or the word is too short."""
    w = word.lower()
    for suf, minlen in (("ing", 5), ("ed", 4), ("ly", 4)):
        if w.endswith(suf) and len(w) >= minlen:
            return w[:-len(suf)], suf
    if w.endswith("es") and len(w) >= 4:
        return w[:-2], "s"
    if w.endswith("s") and not w.endswith("ss") and len(w) >= 3:
        return w[:-1], "s"
    if len(w) >= 2 and w[-1] in "eydtnr":
        return w[:-1], w[-1]
    return w, "other"


def sufx_key(word, fmap):
    """code string of a word under mark map fmap (class -> mark): drop-skeleton of the base, then the class's mark."""
    base, cls = suffix_class(word)
    return skeleton(base, "drop") + fmap[cls]


def build_sufx_control(kind_seq, words, rng, fmap, p_join):
    """Matched control: as build_skel_control, each code-slot word written as sufx_key(word, fmap); run-on groups
    with probability p_join. Returns (toks, truth)."""
    start = rng.randrange(0, len(words) - 4 * len(kind_seq) - 1)
    pos = start
    toks, truth = [], []
    for kind, _ in kind_seq:
        if kind == "number":
            toks.append(("number", str(rng.randint(1, 999)))); truth.append(None); pos += 1
        elif kind == "letter":
            toks.append(("letter", rng.choice("AI"))); truth.append(None); pos += 1
        else:
            grp = [words[pos]]; pos += 1
            while rng.random() < p_join:
                grp.append(words[pos]); pos += 1
            toks.append(("code", "".join(sufx_key(w, fmap) for w in grp))); truth.append(grp)
    return toks, truth


def mark_profile(toks):
    """share of code tokens whose final mark (longest match among SUFX_MARKS) is each mark; '' = none of them."""
    c = Counter()
    n = 0
    for k, v in toks:
        if k != "code":
            continue
        n += 1
        m = next((m for m in ("SE", "BE", "E") if v.endswith(m) and len(v) > len(m)), "")
        c[m] += 1
    return {m: c[m] / n for m in SUFX_MARKS}


def fit_true_map(real_toks, words, rng_seed=7):
    """generator-only fit of the control's (fmap, p_join) to the target's mark profile and mean letters per code token:
    every class -> mark map (4^7) scored by L1 distance of the token-final mark profile on a 2,000-token control
    (p_join 0.5), the best map kept, then p_join fitted on letters per token. No decode, no target score."""
    import itertools
    import numpy as np
    tprof = mark_profile(real_toks)
    tl = [len(v) for k, v in real_toks if k == "code"]
    tmean = sum(tl) / len(tl)
    kinds = tile_kinds(real_toks, 2000)
    # the profile depends only on the class of each token's last word: class shares from one fixed control draw
    _, truth = build_sufx_control(kinds, words, random.Random(rng_seed), {c: "" for c in SUFX_CLASSES}, 0.5)
    finals = Counter(suffix_class(t[-1])[1] for t in truth if t)
    share = np.array([finals[c] for c in SUFX_CLASSES], float); share /= share.sum()
    combos = np.array(list(itertools.product(range(len(SUFX_MARKS)), repeat=len(SUFX_CLASSES))), dtype=np.int8)
    prof = np.stack([(share[None, :] * (combos == j)).sum(axis=1) for j in range(len(SUFX_MARKS))], axis=1)
    tvec = np.array([tprof[m] for m in SUFX_MARKS])
    d = np.abs(prof - tvec[None, :]).sum(axis=1)
    i = int(d.argmin())
    best = (float(d[i]), {c: SUFX_MARKS[combos[i, j]] for j, c in enumerate(SUFX_CLASSES)},
            {m: float(prof[i, j]) for j, m in enumerate(SUFX_MARKS)})
    fmap = best[1]
    bp = None
    for p in [x / 20 for x in range(19)]:
        ct, _ = build_sufx_control(kinds, words, random.Random(rng_seed), fmap, p)
        c = [len(v) for k, v in ct if k == "code"]
        d = abs(sum(c) / len(c) - tmean)
        if bp is None or d < bp[0]:
            bp = (d, p, sum(c) / len(c))
    ct, _ = build_sufx_control(kinds, words, random.Random(rng_seed), fmap, bp[1])
    return {"fmap": fmap, "profile_l1_class_shares": best[0], "control_profile_realised": mark_profile(ct),
            "class_shares": {c: float(x) for c, x in zip(SUFX_CLASSES, share)}, "profile_l1": best[0], "control_profile": best[2], "target_profile": tprof,
            "p_join": bp[1], "control_mean_letters": bp[2], "target_mean_letters": tmean}


def fit_marks(wb, toks, alpha, beam, passes=3, starts=("", "E")):
    """the instrument: coordinate ascent over the class -> mark map, each candidate map scored by the lattice decode's
    total (SkelDecoder with keyfn = sufx_key under that map); starts: every class -> '' and every class -> 'E'.
    Returns (best fmap, its stats row, decoder)."""
    cache = {}

    def run(fmap):
        key = tuple(fmap[c] for c in SUFX_CLASSES)
        if key not in cache:
            dec = SkelDecoder(wb, alpha=alpha, beam=beam, keyfn=lambda w: sufx_key(w, fmap))
            cache[key] = (skel_stats(dec, toks), dec)
        return cache[key]

    best = None
    for s0 in starts:
        fmap = {c: s0 for c in SUFX_CLASSES}
        cur = run(fmap)[0]["score"]
        for _ in range(passes):
            moved = False
            for c in SUFX_CLASSES:
                for m in SUFX_MARKS:
                    if m == fmap[c]:
                        continue
                    trial = dict(fmap); trial[c] = m
                    sc = run(trial)[0]["score"]
                    if sc > cur + 1e-9:
                        fmap, cur, moved = trial, sc, True
            if not moved:
                break
        if best is None or cur > best[0]:
            best = (cur, dict(fmap))
    row, dec = run(best[1])
    return best[1], dict(row), dec


def shuffle_types(toks, rng, keep_marks=False):
    """repeated-type-keeping null: the letters of the distinct code TYPES are permuted across types (each type keeps its
    length), and every occurrence of a type gets its type's new string, so repeated types stay repeated (NCBE x11 stays
    one type x11). keep_marks: each type's final mark (longest of SE/BE/E, not the whole type) is kept and only the
    letters before it are permuted."""
    types = sorted(set(v for k, v in toks if k == "code"))

    def split(v):
        if keep_marks:
            m = next((m for m in ("SE", "BE", "E") if v.endswith(m) and len(v) > len(m)), "")
            return (v[:len(v) - len(m)], m)
        return (v, "")
    parts = [split(v) for v in types]
    letters = [ch for st, _ in parts for ch in st]
    rng.shuffle(letters)
    new, p = {}, 0
    for v, (st, m) in zip(types, parts):
        new[v] = "".join(letters[p:p + len(st)]) + m; p += len(st)
    return [(k, new[v]) if k == "code" else (k, v) for k, v in toks]


_SUFX = {}


def _null_fit(job):
    """worker for the null fits (fork-shared WordBigram in _SUFX): job = (toks, rng seed, keep_marks)."""
    toks, seed, km = job
    return fit_marks(_SUFX["wb"], shuffle_types(toks, random.Random(seed), keep_marks=km), _SUFX["alpha"], _SUFX["beam"])[1]


def _null_rows(toks, seeds, km, procs):
    if procs <= 1:
        return [_null_fit((toks, s, km)) for s in seeds]
    import multiprocessing as mp
    with mp.get_context("fork").Pool(procs) as pool:
        return pool.map(_null_fit, [(toks, s, km) for s in seeds])


def sufx_run(a, real_toks, words):
    """MCC-SUFX (PREREG-MCC-SUFX.md): control first at N = the target's own (and --n-list), target only with --target
    and only if the control read at the target's own N (exit 3 otherwise)."""
    import time
    allowed = lexicon_allows(load_lexicon(a.lexicon)) if a.lexicon else None
    wb = WordBigram(corpus_words_from(HELDOUT_EN), a.pool, allowed=allowed)
    _SUFX.update(wb=wb, alpha=a.alpha, beam=a.beam)
    gen = fit_true_map(real_toks, words)
    out = {"mode": "sufx", "pool_size": a.pool, "alpha": a.alpha, "beam": a.beam, "generator": gen, "controls": {},
           "lexicon": a.lexicon, "target_nulls": a.target_nulls or a.nulls}
    print(json.dumps(gen), file=sys.stderr)
    seeds = [int(x) for x in a.seeds.split(",")]
    for n in [int(x) for x in a.n_list.split(",")]:
        runs = []
        for seed in seeds:
            t = time.time()
            ctoks, truth = build_sufx_control(tile_kinds(real_toks, n), words, random.Random(1000 + seed), gen["fmap"],
                                              gen["p_join"])
            fmap, r, dec = fit_marks(wb, ctoks, a.alpha, a.beam)
            r = skel_stats(dec, ctoks, truth); r.pop("decode")
            tw = [w for t in truth if t for w in t]
            mark_rec = sum(1 for w in tw if fmap[suffix_class(w)[1]] == gen["fmap"][suffix_class(w)[1]]) / len(tw)
            row = {"seed": seed, "n_tokens": n, "fitted_map": fmap, "mark_map_recovery": mark_rec, **r}
            nl = _null_rows(ctoks, [3000 + seed * 100 + i for i in range(a.nulls)], True, a.procs)
            row["typemark_null_coverage_max"] = max(x["coverage"] for x in nl)
            row["secs"] = round(time.time() - t, 1)
            runs.append(row)
            print(json.dumps(row), file=sys.stderr)
        mean = sum(r["word_recovery"] for r in runs) / len(runs)
        read = (mean >= a.gate and all(r["mark_map_recovery"] >= 0.8 for r in runs)
                and all(r["coverage"] > r["typemark_null_coverage_max"] for r in runs))
        out["controls"][str(n)] = {"runs": runs, "word_recovery_mean": mean, "read": read}
        print(json.dumps({"n": n, "word_recovery_mean": mean, "read": read,
                          "mark_map_recovery": [r["mark_map_recovery"] for r in runs],
                          "coverage": [r["coverage"] for r in runs],
                          "typemark_null_max": [r["typemark_null_coverage_max"] for r in runs]}))
    if a.target:
        c0 = out["controls"].get(str(len(real_toks)), {})
        if not c0.get("read"):
            out["target"] = "not run: control did not read at the target's own N"
        else:
            fmap, tr, _ = fit_marks(wb, real_toks, a.alpha, a.beam)
            tr["fitted_map"] = fmap
            for name, km, base in (("type_null", False, 5000), ("typemark_null", True, 6000)):
                nl = _null_rows(real_toks, [base + i for i in range(a.target_nulls or a.nulls)], km, a.procs)
                tr[name + "_coverage"] = sorted(x["coverage"] for x in nl)
                tr[name + "_spl"] = sorted(x["score_per_letter"] for x in nl)
                tr["coverage_above_" + name + "_max"] = tr["coverage"] > max(tr[name + "_coverage"])
                tr["spl_above_" + name + "_max"] = tr["score_per_letter"] > max(tr[name + "_spl"])
            out["target"] = tr
        print(json.dumps(out["target"] if isinstance(out["target"], str) else
                         {k: v for k, v in out["target"].items() if k not in ("decode",) and not k.endswith(("_coverage", "_spl"))}))
    if a.out:
        Path(a.out).write_text(json.dumps(out, indent=1))
    ok = all(c["read"] for c in out["controls"].values())
    return 0 if ok else 3


# ---------------------------------------------------------------- main


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out")
    ap.add_argument("--iters", type=int, default=ITERS)
    ap.add_argument("--restarts", type=int, default=RESTARTS)
    ap.add_argument("--n-tokens", type=int, default=None, help="control length (default: the target's own)")
    ap.add_argument("--control-only", action="store_true", help="run only the matched control (no target, no shuffles)")
    ap.add_argument("--seeds", default="1,2,3")
    ap.add_argument("--iters-per-type", type=float, default=None,
                    help="iterations = max(--iters, this x the control's code-type count)")
    ap.add_argument("--fast", action="store_true", help="incremental scorer (same objective)")
    ap.add_argument("--selftest", action="store_true", help="check FastScorer against the full scorer, then exit")
    ap.add_argument("--gate", type=float, default=0.5)
    ap.add_argument("--temp-scale", choices=["mean", "total"], default="mean",
                    help="--fast only: Metropolis test on the mean-score change (bMCC4) or on it x n-gram count")
    ap.add_argument("--null", action="store_true",
                    help="also run each control with its code-token order shuffled among the code slots (rng 2000+seed)")
    ap.add_argument("--objective", choices=["char4", "wordbigram"], default="char4",
                    help="char4: bMCC4's char 4-gram anneal (default); wordbigram: MCC-WORD whole-word bigram Gibbs anneal "
                         "(--control-only only)")
    ap.add_argument("--lm", choices=["heldout", "insample"], default="heldout",
                    help="wordbigram: LM trained on tools/data/en/ (held out from the control's Holmes+Moby-Dick draw) "
                         "or on those plus Holmes+Moby-Dick (in-sample upper bound, diagnostic only)")
    ap.add_argument("--pool", type=int, default=1000, help="wordbigram: candidate word pool (top LM-corpus words)")
    ap.add_argument("--sweeps", type=int, default=200, help="wordbigram: annealing sweeps over all code types")
    ap.add_argument("--sufx", action="store_true", help="MCC-SUFX: suffix-mark abbreviation model (fitted class -> mark map; "
                    "uses --pool/--alpha/--beam/--n-list/--seeds/--nulls/--target/--gate)")
    ap.add_argument("--procs", type=int, default=1, help="sufx: processes for the null fits")
    ap.add_argument("--lexicon", help="sufx (MCC-GREGG): word-list file; the pool is the top --pool LM-corpus words that are "
                    "in it or inflect a word in it (lexicon_allows)")
    ap.add_argument("--target-nulls", type=int, default=None, help="sufx: nulls per kind on the target (default --nulls)")
    ap.add_argument("--generator-only", action="store_true", help="sufx: print the control generator's fit and exit")
    ap.add_argument("--skeleton", action="store_true", help="MCC-SKEL: abbreviation/consonant-skeleton lattice decoder")
    ap.add_argument("--scheme", choices=["drop", "keepfinal"], default="drop", help="skeleton: vowel rule")
    ap.add_argument("--alpha", type=float, default=3.0, help="skeleton: UNK cost in nats per letter")
    ap.add_argument("--beam", type=int, default=200, help="skeleton: previous-word states kept per position")
    ap.add_argument("--n-list", default="132", help="skeleton: control lengths, comma-separated")
    ap.add_argument("--nulls", type=int, default=40, help="skeleton: letter-shuffled nulls per run")
    ap.add_argument("--target", action="store_true", help="skeleton: also run the target (only if the control read at its N)")
    ap.add_argument("--null-keep-final", action="store_true",
                    help="skeleton (PREREG-MCC-SKEL addendum 2): also score the target against nulls that keep each code "
                         "token's length and last letter")
    ap.add_argument("--target-on-power", action="store_true",
                    help="skeleton (PREREG-MCC-SKEL addendum 1): also run the target when the control's coverage beats its "
                         "letter-shuffled null on every seed at the target's N, even if the word-recovery read failed")
    a = ap.parse_args()

    text = CIPHER_FILE.read_text()
    real_toks = tokenize(text)
    kinds = Counter(k for k, _ in real_toks)
    print(f"real target tokens: {len(real_toks)} {dict(kinds)}", file=sys.stderr)
    ntypes = len(set(v for k, v in real_toks if k == "code"))
    print(f"distinct code token types: {ntypes}", file=sys.stderr)

    words = corpus_words()
    pool_words, pool_weights, frequent = build_vocab(words)
    model = jp.NgramModel([jp.read_corpus(p) for p in CORPORA])

    if a.selftest:
        return selftest(model, pool_words, pool_weights, real_toks, words, frequent)
    if a.sufx and a.generator_only:
        print(json.dumps(fit_true_map(real_toks, words), indent=1)); return 0
    if a.sufx:
        return sufx_run(a, real_toks, words)
    if a.skeleton:
        return skeleton_run(a, real_toks, words)
    if a.control_only and a.objective == "wordbigram":
        return wordbigram_sweep(a, real_toks, words, frequent)
    if a.control_only:
        return control_sweep(a, real_toks, words, frequent, pool_words, pool_weights, model)

    out = {"real_tokens": len(real_toks), "kinds": dict(kinds), "distinct_code_types": ntypes,
           "pool_size": POOL_N, "freq_n": FREQ_N, "iters": a.iters, "restarts": a.restarts}

    # --- target ---
    rng = random.Random(2025)
    t_score, t_assign = anneal_solve(real_toks, model, pool_words, pool_weights, rng, a.iters, a.restarts)
    t_decode = assemble(real_toks, t_assign)
    out["target"] = {"score": t_score, "decode_preview": t_decode[:300]}
    Path(ROOT / "ciphers/mccormick-1999/families").mkdir(parents=True, exist_ok=True)
    (ROOT / "ciphers/mccormick-1999/families/token-anneal-target.txt").write_text(
        "# LANE B3 bMCC4 token/nomenclator anneal, target decode (candidate, NOT a reading; rule 10)\n"
        + t_decode + "\n")

    # --- control, 3 seeds ---
    control_runs = []
    used_codes = set()
    for seed in (1, 2, 3):
        crng = random.Random(1000 + seed)
        ctoks, truth = build_control(real_toks, words, frequent, crng, used_codes)
        c_score, c_assign = anneal_solve(ctoks, model, pool_words, pool_weights, crng, a.iters, a.restarts)
        rec = recovery_fraction(c_assign, truth)
        control_runs.append({"seed": seed, "score": c_score, "recovery": rec, "n_truth_types": len(truth)})
        print(f"control seed {seed}: recovery={rec:.3f} score={c_score:.3f}", file=sys.stderr)
    recs = [r["recovery"] for r in control_runs]
    out["control"] = {"runs": control_runs, "recovery_mean": sum(recs) / len(recs),
                      "recovery_range": [min(recs), max(recs)]}

    # --- false-positive floor: shuffle the real target's code-token VALUES among the code slots ---
    shuffle_runs = []
    code_positions = [i for i, (k, _) in enumerate(real_toks) if k == "code"]
    code_values = [real_toks[i][1] for i in code_positions]
    for seed in (1, 2, 3):
        srng = random.Random(2000 + seed)
        shuffled_vals = code_values[:]
        srng.shuffle(shuffled_vals)
        shuf_toks = list(real_toks)
        for pos, val in zip(code_positions, shuffled_vals):
            shuf_toks[pos] = ("code", val)
        s_score, s_assign = anneal_solve(shuf_toks, model, pool_words, pool_weights, srng, a.iters, a.restarts)
        shuffle_runs.append({"seed": seed, "score": s_score})
        print(f"shuffle seed {seed}: score={s_score:.3f}", file=sys.stderr)
    out["shuffled_target"] = shuffle_runs

    # --- judge the target decode ---
    spec = json.loads(SPEC_FILE.read_text())
    verdict = jp.judge(spec, t_decode)
    out["judge"] = verdict

    gate_met = out["control"]["recovery_mean"] >= 0.5
    out["gate"] = {"threshold": 0.5, "met": gate_met}
    print(json.dumps({"control_recovery_mean": out["control"]["recovery_mean"],
                      "control_recovery_range": out["control"]["recovery_range"],
                      "target_score": t_score, "shuffled_scores": [r["score"] for r in shuffle_runs],
                      "gate_met": gate_met, "judge_pass": verdict["pass"]}, indent=1))
    if a.out:
        Path(a.out).write_text(json.dumps(out, indent=1))
    return 0 if gate_met else 3


def control_sweep(a, real_toks, words, frequent, pool_words, pool_weights, model):
    import time
    n = a.n_tokens or len(real_toks)
    kinds_seq = tile_kinds(real_toks, n)
    if a.fast:
        def solve(*args):
            return anneal_solve_fast(*args, temp_scale=a.temp_scale)
    else:
        solve = anneal_solve
    runs, used_codes = [], set()
    for seed in [int(x) for x in a.seeds.split(",")]:
        crng = random.Random(1000 + seed)  # bMCC4's control seeding
        ctoks, truth = build_control(kinds_seq, words, frequent, crng, used_codes)
        ntypes = len(set(v for k, v in ctoks if k == "code"))
        iters = a.iters if a.iters_per_type is None else max(a.iters, int(a.iters_per_type * ntypes))
        t0 = time.time()
        c_score, c_assign = solve(ctoks, model, pool_words, pool_weights, crng, iters, a.restarts)
        rec = recovery_fraction(c_assign, truth)
        row = {"seed": seed, "n_tokens": n, "code_types": ntypes, "iters": iters, "restarts": a.restarts,
               "score": c_score, "recovery": rec, "n_truth_types": len(truth), "secs": round(time.time() - t0, 1)}
        row.update(diagnostics(c_assign, truth, ctoks, pool_words))
        if a.null:
            srng = random.Random(2000 + seed)
            pos = [i for i, (k, _) in enumerate(ctoks) if k == "code"]
            vals = [ctoks[i][1] for i in pos]
            srng.shuffle(vals)
            stoks = list(ctoks)
            for i, v in zip(pos, vals):
                stoks[i] = ("code", v)
            _, s_assign = solve(stoks, model, pool_words, pool_weights, srng, iters, a.restarts)
            d = diagnostics(s_assign, truth, stoks, pool_words)
            row["null_recovery"] = recovery_fraction(s_assign, truth)
            row["null_token_recovery"] = d["token_recovery"]
        runs.append(row)
        print(json.dumps(row), file=sys.stderr)
    recs = [r["recovery"] for r in runs]
    mean = sum(recs) / len(recs)
    out = {"mode": "control-only", "n_tokens": n, "fast": a.fast, "temp_scale": a.temp_scale, "pool_size": POOL_N, "freq_n": FREQ_N,
           "runs": runs, "recovery_mean": mean, "recovery_range": [min(recs), max(recs)],
           "token_recovery_mean": sum(r["token_recovery"] for r in runs) / len(runs),
           "pool_ceiling_types_mean": sum(r["pool_ceiling_types"] for r in runs) / len(runs),
           "pool_ceiling_tokens_mean": sum(r["pool_ceiling_tokens"] for r in runs) / len(runs),
           "gate": {"threshold": a.gate, "met": mean >= a.gate}}
    if a.null:
        nt = [r["null_token_recovery"] for r in runs]
        out["null_token_recovery_mean"] = sum(nt) / len(nt)
        out["null_token_recovery_max"] = max(nt)
        # MCC-SWEEP PREREG token criterion: control token recovery mean >= gate AND every seed above the null's max
        out["token_read"] = (out["token_recovery_mean"] >= a.gate
                             and min(r["token_recovery"] for r in runs) > max(nt))
    print(json.dumps({k: out[k] for k in ("n_tokens", "recovery_mean", "recovery_range", "token_recovery_mean", "gate",
                                          "pool_ceiling_types_mean", "pool_ceiling_tokens_mean")
                      + (("null_token_recovery_mean", "null_token_recovery_max", "token_read") if a.null else ())}))
    if a.out:
        Path(a.out).write_text(json.dumps(out, indent=1))
    return 0 if mean >= a.gate else 3


if __name__ == "__main__":
    sys.exit(main())
