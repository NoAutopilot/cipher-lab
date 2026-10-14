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

    def __init__(self, words, pool, lam=WB_LAMBDA):
        import numpy as np
        freq = Counter(words)
        self.pool = [w for w, _ in freq.most_common(pool)]
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
