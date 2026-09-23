#!/usr/bin/env python3
"""Joint simulated-annealing solver for small graphic-sign nomenclators (letters with homophones,
syllable signs, word signs, nulls), scored by a character n-gram LLR model (tools/italian_ngram.py).

Written 23 Sept 2026 for ciphers/sforza-maino-1446. Own code; design ideas (SA over a sign->value key,
n-gram scoring, restarts, greedy finish, caps against degenerate keys) are the common ones described in
LESSONS.md, no code copied from either solver repository.

Input files use D. Bourdeau's transcription format: whitespace-separated sign codes, '#' comments,
{clear text} in braces, '|' paragraph marks, '.' separators and '?' ignored (unless --dots boundary).

Subcommands
  solve  FILE... --model M.npz [--map signs.tsv] [--context none|clear] [--fix SIGN=VALUE ...]
         [--restarts R] [--iters N] [--max-syl S] [--max-word W] [--max-null Z] [--max-homo H]
         [--shuffle SEED] [--out result.json]
         One key shared by all FILEs (joint). --map is a TSV 'file<TAB>label<TAB>unified' that renames a
         file's label (e.g. keep f.70's E apart from f.68's E); unlisted labels are shared across files.
         --shuffle SEED permutes the cipher tokens (same symbols and counts, same run lengths): the
         search baseline on meaningless input.
  synth  PLAINTEXT --design design.json --out cipher.txt --truth truth.json [--pattern FILE] [--seed S]
         Encipher a normalised plaintext with a random key of the given design (see make_key()).
         --pattern FILE copies the run structure (cipher runs / clear runs) of a real transcription.
         --unit 'F p B H c' --vocab corpus.txt: that group must decode to one or two corpus words.
  eval   result.json truth.json      token and letter accuracy of a solved key against the truth.
  decode FILE... --key key.tsv [--map signs.tsv]   print the reading (used by check.py scripts).

Values: a single letter, a syllable (e.g. 'er'), a word (e.g. 'che') or '' (null). In readings,
syllable/word values are shown as written; nulls as nothing.
"""
import argparse
import ctypes
import difflib
import hashlib
import json
import math
import os
import random
import re
import subprocess
import sys
import tempfile
from collections import Counter

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import italian_ngram as ing  # noqa: E402

ALPHA = ing.ALPHA
K = ing.K
PAD = ing.IDX["#"]
VOWELS = "aeiou"
CONS = "bcdfghlmnpqrstxz"
DEFAULT_WORDS = "de che per quale con ma quello perche et el la lo non".split()

# ---------------------------------------------------------------- parsing


def parse(path, dots=False):
    """Return list of runs: ('c', [labels]) or ('p', 'clear letters')."""
    t = open(path, encoding="utf-8").read()
    t = "\n".join(l for l in t.splitlines() if not l.lstrip().startswith("#"))
    runs = []
    for part in re.split(r"(\{.*?\})", t, flags=re.S):
        if part.startswith("{"):
            z = ing.norm(part[1:-1]).replace("#", "")
            if z:
                runs.append(("p", z))
            continue
        cur = []
        for x in part.split():
            if x in ("|", "?"):
                continue
            if x == ".":
                if dots and cur:
                    runs.append(("c", cur))
                    cur = []
                continue
            cur.append(x)
        if cur:
            runs.append(("c", cur))
    # merge adjacent cipher runs split only by '|' (kept separate: '|' is a paragraph start)
    return runs


def load_map(path):
    m = {}
    if path:
        for line in open(path, encoding="utf-8"):
            if line.startswith("#") or not line.strip():
                continue
            f, lab, uni = line.rstrip("\n").split("\t")[:3]
            m[(f, lab)] = uni
    return m


def load_texts(files, mapfile=None, dots=False):
    m = load_map(mapfile)
    texts = []
    for f in files:
        base = os.path.basename(f)
        runs = []
        for kind, x in parse(f, dots):
            if kind == "c":
                x = [m.get((base, lab), lab) for lab in x]
            runs.append((kind, x))
        texts.append((base, runs))
    return texts


def shuffle_texts(texts, seed):
    rng = random.Random(seed)
    toks = [t for _, runs in texts for k, x in runs if k == "c" for t in x]
    rng.shuffle(toks)
    out, i = [], 0
    for name, runs in texts:
        nr = []
        for k, x in runs:
            if k == "c":
                nr.append((k, toks[i:i + len(x)]))
                i += len(x)
            else:
                nr.append((k, x))
        out.append((name, nr))
    return out

# ---------------------------------------------------------------- C core

C_SRC = r"""
#include <stdint.h>
/* stream: sequence of sign ids; val[sign] -> value id; value v expands to chars
   echars[eoff[v] .. eoff[v]+elen[v]); char codes >= 64 mean 'reset context, unscored pad'.
   clear chars are passed as fixed signs whose value is one char with flag 32 (scored only within
   order-1 chars after a cipher char when ctxmode==1, never when ctxmode==0 (then they act as pad)). */
double score(const int32_t* stream, int32_t n, const int32_t* val, const int32_t* eoff,
             const int32_t* elen, const int32_t* echars, const float* llr, int32_t order,
             int32_t K, int32_t ctxmode) {
    int64_t H = 1; for (int i = 0; i < order - 1; i++) H *= K;
    int64_t h = 0; int filled = 0; double s = 0.0; int since = 1000;
    for (int i = 0; i < n; i++) {
        int32_t v = val[stream[i]];
        int32_t o = eoff[v], L = elen[v];
        for (int j = 0; j < L; j++) {
            int32_t c = echars[o + j];
            if (c >= 64) {            /* pad: reset context */
                h = 0; for (int q = 0; q < order - 1; q++) h = h * K + (c - 64);
                h %= H; filled = order - 1; since = 1000; continue;
            }
            int clear = (c >= 32); if (clear) c -= 32;
            int sc = 1;
            if (clear) { sc = (ctxmode == 1 && since < order); since++; }
            else since = 0;
            if (sc && filled >= order - 1) s += llr[h * K + c];
            h = (h * K + c) % H; if (filled < order - 1) filled++;
        }
    }
    return s;
}
"""

_lib = None


def lib():
    global _lib
    if _lib is None:
        d = os.path.join(tempfile.gettempdir(), "nomenclator_anneal")
        os.makedirs(d, exist_ok=True)
        tag = hashlib.md5(C_SRC.encode()).hexdigest()[:10]
        so = os.path.join(d, f"core_{tag}.so")
        if not os.path.exists(so):
            src = os.path.join(d, f"core_{tag}.c")
            open(src, "w").write(C_SRC)
            subprocess.check_call(["gcc", "-O3", "-shared", "-fPIC", "-o", so, src])
        L = ctypes.CDLL(so)
        P = ctypes.POINTER
        L.score.restype = ctypes.c_double
        L.score.argtypes = [P(ctypes.c_int32), ctypes.c_int32, P(ctypes.c_int32), P(ctypes.c_int32),
                            P(ctypes.c_int32), P(ctypes.c_int32), P(ctypes.c_float), ctypes.c_int32,
                            ctypes.c_int32, ctypes.c_int32]
        _lib = L
    return _lib

# ---------------------------------------------------------------- problem


class Problem:
    def __init__(self, texts, model, context="none", syl="vc", words=None, letters=ALPHA, scoring="gen",
                 p_null=0.03):
        self.model = model
        self.scoring = scoring
        self.p_null = p_null
        self.context = context
        self.values = []            # value strings
        self.vkind = []             # 'l' letter, 's' syllable, 'w' word, 'n' null, 'f' fixed
        for c in letters:
            self._add(c, "l")
        syls = []
        if syl in ("vc", "both"):
            syls += [v + c for v in VOWELS for c in CONS]
        if syl in ("cv", "both"):
            syls += [c + v for c in CONS for v in VOWELS]
        for s in syls:
            self._add(s, "s")
        for w in (words if words is not None else DEFAULT_WORDS):
            if w not in self.values:
                self._add(w, "w")
        self.null_v = self._add("", "n")
        self.pad_v = self._add("\x00pad", "f")
        # signs
        self.signs = []
        self.sidx = {}
        stream = []
        cnt = Counter()
        self.layout = []   # per text: list of runs with token positions in stream
        for name, runs in texts:
            stream.append(("pad",))
            lay = []
            for kind, x in runs:
                if kind == "c":
                    pos = []
                    for lab in x:
                        if lab not in self.sidx:
                            self.sidx[lab] = len(self.signs)
                            self.signs.append(lab)
                        cnt[lab] += 1
                        pos.append(len(stream))
                        stream.append(("s", lab))
                    lay.append(("c", pos))
                else:
                    if context == "clear":
                        stream.append(("clear", x))
                    else:
                        stream.append(("pad",))
                    lay.append(("p", x))
            self.layout.append((name, lay))
        self.counts = cnt
        self.nsign = len(self.signs)
        # fixed pseudo-signs for pad and clear runs
        vals0 = []
        ids = []
        for it in stream:
            if it[0] == "s":
                ids.append(self.sidx[it[1]])
            elif it[0] == "pad":
                ids.append(-1)
            else:
                v = self._add("\x00clear" + it[1], "f")
                ids.append(-(v + 10))
        # assign sign ids to fixed items after the real signs
        fixed_vals = []
        stream_ids = []
        for i in ids:
            if i >= 0:
                stream_ids.append(i)
            else:
                v = self.pad_v if i == -1 else -(i + 10)
                stream_ids.append(self.nsign + len(fixed_vals))
                fixed_vals.append(v)
        self.fixed_vals = fixed_vals
        self.stream = np.array(stream_ids, dtype=np.int32)
        # expansions
        eoff, elen, ech = [], [], []
        for v, s in enumerate(self.values):
            eoff.append(len(ech))
            if self.vkind[v] == "f":
                if s == "\x00pad":
                    ech.append(64 + PAD)
                else:
                    ech.extend(32 + ing.IDX[c] for c in s[len("\x00clear"):])
            else:
                ech.extend(ing.IDX[c] for c in s)
            elen.append(len(ech) - eoff[-1])
        self.eoff = np.array(eoff, dtype=np.int32)
        self.elen = np.array(elen, dtype=np.int32)
        self.ech = np.array(ech if ech else [0], dtype=np.int32)
        table = model.logp if scoring == "gen" else model.llr
        self.llr = np.ascontiguousarray(table, dtype=np.float32)
        self.cnt_arr = [self.counts[s] for s in self.signs]
        self.ntok = sum(self.cnt_arr)
        self.byk = {k: [i for i, kk in enumerate(self.vkind) if kk == k] for k in "lswn"}
        self.vid = {s: i for i, s in enumerate(self.values) if self.vkind[i] != "f"}

    def _add(self, s, kind):
        self.values.append(s)
        self.vkind.append(kind)
        return len(self.values) - 1

    def full_val(self, key):
        return np.ascontiguousarray(np.concatenate([np.asarray(key, dtype=np.int32),
                                                    np.asarray(self.fixed_vals, dtype=np.int32)]))

    def prior(self, key):
        """log P(sign | value) summed over tokens: uniform choice among the h signs that share a value,
        plus a null-insertion rate. Zero under --scoring llr."""
        if self.scoring != "gen":
            return 0.0
        h, nt = {}, {}
        for s, v in enumerate(key[:self.nsign]):
            h[v] = h.get(v, 0) + 1
            nt[v] = nt.get(v, 0) + self.cnt_arr[s]
        lp = -sum(nt[v] * math.log(h[v]) for v in h if h[v] > 1)
        nn = nt.get(self.null_v, 0)
        lp += nn * math.log(self.p_null) + (self.ntok - nn) * math.log(1 - self.p_null)
        return lp

    def set_units(self, units, vocab_path, penalty=25.0):
        """units: list of label sequences (e.g. repeated groups) that must decode to one or two whole
        words of the corpus vocabulary; each unit that does not costs `penalty` nats."""
        words, pairs = set(), set()
        for line in open(vocab_path):
            w = [x for x in line.strip().split("#") if x]
            words.update(w)
            pairs.update(a + b for a, b in zip(w, w[1:]))
        self.vocab = words | pairs
        self.units = [[self.sidx[l] for l in u] for u in units if all(l in self.sidx for l in u)]
        self.unit_pen = penalty

    def unit_score(self, key):
        if not getattr(self, "units", None):
            return 0.0
        bad = sum(1 for u in self.units if "".join(self.values[key[i]] for i in u) not in self.vocab)
        return -self.unit_pen * bad

    def score(self, key):
        return self.lm_score(key) + self.prior(key) + self.unit_score(key)

    def lm_score(self, key):
        v = self.full_val(key)
        P = ctypes.POINTER
        c32 = lambda a: a.ctypes.data_as(P(ctypes.c_int32))  # noqa: E731
        return lib().score(c32(self.stream), len(self.stream), c32(v), c32(self.eoff), c32(self.elen),
                           c32(self.ech), self.llr.ctypes.data_as(P(ctypes.c_float)), self.model.order,
                           K, 1 if self.context == "clear" else 0)

    def reading(self, key, upper_clear=True):
        out = []
        for name, lay in self.layout:
            parts = []
            for kind, x in lay:
                if kind == "c":
                    parts.append("".join(self.values[key[self.sidx_of(p)]] for p in x))
                else:
                    parts.append("{" + x.upper() + "}")
            out.append((name, " ".join(parts)))
        return out

    def sidx_of(self, pos):
        return int(self.stream[pos])

# ---------------------------------------------------------------- annealing


def anneal(pb, rng, iters, T0, T1, caps, fixed, init=None):
    n = pb.nsign
    lvals = pb.byk["l"]
    freq_letters = "eaoinrlstcdupmghbfqzx"
    if init is not None:
        key = list(init)
    else:
        key = [pb.vid[rng.choice(freq_letters[:12])] for _ in range(n)]
    for s, v in fixed.items():
        key[s] = v
    mutable = [s for s in range(n) if s not in fixed]
    wts = [math.sqrt(pb.counts[pb.signs[s]]) for s in mutable]

    def kinds_ok(k):
        c = Counter(pb.vkind[v] for v in k)
        if c["s"] > caps["syl"] or c["w"] > caps["word"] or c["n"] > caps["null"]:
            return False
        if caps["homo"]:
            lc = Counter(v for v in k if pb.vkind[v] == "l")
            if lc and max(lc.values()) > caps["homo"]:
                return False
        return True

    cur = pb.score(key)
    best, bestkey = cur, key[:]
    kinds = pb.vkind
    for it in range(iters):
        T = T0 * (T1 / T0) ** (it / max(1, iters - 1))
        s = rng.choices(mutable, wts)[0]
        old = key[s]
        r = rng.random()
        if r < 0.3 and len(mutable) > 1:
            s2 = rng.choice(mutable)
            if key[s2] == old:
                continue
            key[s], key[s2] = key[s2], old
            nv = None
        else:
            s2 = None
            q = rng.random()
            if q < 0.8:
                nv = rng.choice(lvals)
            elif q < 0.9 and pb.byk["s"] and caps["syl"]:
                nv = rng.choice(pb.byk["s"])
            elif q < 0.96 and pb.byk["w"] and caps["word"]:
                nv = rng.choice(pb.byk["w"])
            elif caps["null"]:
                nv = pb.null_v
            else:
                nv = rng.choice(lvals)
            if nv == old:
                continue
            key[s] = nv
            if not kinds_ok(key):
                key[s] = old
                continue
        new = pb.score(key)
        if new >= cur or rng.random() < math.exp((new - cur) / T):
            cur = new
            if cur > best:
                best, bestkey = cur, key[:]
        else:
            if s2 is not None:
                key[s2], key[s] = key[s], old
            else:
                key[s] = old
    return best, bestkey


def polish(pb, key, caps, fixed):
    """Steepest single-sign changes until no improvement."""
    key = key[:]
    cur = pb.score(key)
    allv = pb.byk["l"] + (pb.byk["s"] if caps["syl"] else []) + (pb.byk["w"] if caps["word"] else []) + \
        ([pb.null_v] if caps["null"] else [])
    improved = True
    while improved:
        improved = False
        for s in range(pb.nsign):
            if s in fixed:
                continue
            old = key[s]
            bv, bs = old, cur
            for v in allv:
                if v == old:
                    continue
                key[s] = v
                c = Counter(pb.vkind[x] for x in key)
                if c["s"] > caps["syl"] or c["w"] > caps["word"] or c["n"] > caps["null"]:
                    continue
                if caps["homo"] and pb.vkind[v] == "l" and sum(1 for x in key if x == v) > caps["homo"]:
                    continue
                sc = pb.score(key)
                if sc > bs + 1e-9:
                    bv, bs = v, sc
            key[s] = bv
            if bv != old:
                cur = bs
                improved = True
    return cur, key


def _worker(args):
    (files, mapfile, model_path, opts, seed) = args
    model = ing.Model(model_path)
    texts = load_texts(files, mapfile, opts["dots"])
    if opts.get("shuffle") is not None:
        texts = shuffle_texts(texts, opts["shuffle"])
    pb = Problem(texts, model, opts["context"], opts["syl"], opts.get("words"), scoring=opts["scoring"],
                 p_null=opts["p_null"])
    fixed = {pb.sidx[k]: pb.vid[v] for k, v in opts["fix"].items() if k in pb.sidx}
    if opts.get("units"):
        pb.set_units(opts["units"], opts["vocab"])
    rng = random.Random(seed)
    b, k = anneal(pb, rng, opts["iters"], opts["T0"], opts["T1"], opts["caps"], fixed)
    b, k = polish(pb, k, opts["caps"], fixed)
    return b, k


def solve(files, model_path, mapfile=None, context="none", restarts=8, iters=100000, T0=3.0, T1=0.05,
          caps=None, fix=None, syl="vc", words=None, dots=False, shuffle=None, seed=0, procs=4,
          scoring="gen", p_null=0.03, units=None, vocab=None):
    caps = caps or dict(syl=6, word=4, null=2, homo=4)
    opts = dict(context=context, iters=iters, T0=T0, T1=T1, caps=caps, fix=fix or {}, syl=syl, words=words,
                dots=dots, shuffle=shuffle, scoring=scoring, p_null=p_null,
                units=units, vocab=vocab)
    jobs = [(files, mapfile, model_path, opts, seed * 1000 + r) for r in range(restarts)]
    if procs > 1:
        import multiprocessing as mp
        with mp.Pool(procs) as pool:
            res = pool.map(_worker, jobs)
    else:
        res = [_worker(j) for j in jobs]
    model = ing.Model(model_path)
    texts = load_texts(files, mapfile, dots)
    if shuffle is not None:
        texts = shuffle_texts(texts, shuffle)
    pb = Problem(texts, model, context, syl, words, scoring=scoring, p_null=p_null)
    if units:
        pb.set_units(units, vocab)
    runs = []
    for b, k in res:
        runs.append(dict(score=b, lm=pb.lm_score(k), prior=pb.prior(k), units=pb.unit_score(k), key={pb.signs[s]: pb.values[k[s]] for s in range(pb.nsign)},
                         reading=pb.reading(k)))
    runs.sort(key=lambda r: -r["score"])
    ntok = int(sum(pb.counts.values()))
    return dict(files=[os.path.basename(f) for f in files], context=context, scoring=scoring, p_null=p_null, restarts=restarts,
                iters=iters, T0=T0, T1=T1, caps=caps, fix=fix or {}, syl=syl, shuffle=shuffle,
                ntokens=ntok, nsigns=pb.nsign, scores=[r["score"] for r in runs],
                best=runs[0], per_token=runs[0]["score"] / ntok, runs=runs)

# ---------------------------------------------------------------- synthetic controls


def make_key(design, rng, corpus_vc=None):
    """design: {"homophones": {"e":3,"a":2,...}, "homo_weights": {"2":[.6,.4],"3":[.5,.3,.2]},
    "syllables": n or [list], "words": n or [list], "word_pool": [...], "nulls": n, "null_rate": r,
    "syl_rate": p, "letters": "abc..."}"""
    letters = design.get("letters", ALPHA)
    signs = []   # (value, weight within value)
    table = {}
    for c in letters:
        h = design["homophones"].get(c, 1)
        w = design.get("homo_weights", {}).get(str(h), [1.0 / h] * h)
        table[c] = [(f"S{len(signs) + i}", w[i]) for i in range(h)]
        signs += [(c, w[i]) for i in range(h)]
    syl = design.get("syllables", 0)
    if isinstance(syl, int):
        pool = corpus_vc or [v + c for v in VOWELS for c in "nrlst"]
        syl = rng.sample(pool, syl)
    words = design.get("words", 0)
    if isinstance(words, int):
        words = rng.sample(design.get("word_pool", ["de", "che", "per", "quale", "con", "ma", "quello",
                                                    "perche"]), words)
    nxt = len(signs)
    for s in syl:
        table[s] = [(f"S{nxt}", 1.0)]
        nxt += 1
    for w in words:
        table["#" + w] = [(f"S{nxt}", 1.0)]
        nxt += 1
    nulls = [f"S{nxt + i}" for i in range(design.get("nulls", 0))]
    # random glyph labels so the solver cannot use label order
    labels = [f"S{i}" for i in range(nxt + len(nulls))]
    perm = labels[:]
    rng.shuffle(perm)
    ren = dict(zip(labels, perm))
    table = {k: [(ren[s], w) for s, w in v] for k, v in table.items()}
    nulls = [ren[s] for s in nulls]
    return dict(table=table, syllables=syl, words=words, nulls=nulls,
                null_rate=design.get("null_rate", 0.03), syl_rate=design.get("syl_rate", 0.8))


def encipher(plain, key, rng, ntok=None):
    """plain: normalised text with '#' word boundaries. Returns [(label, value)]."""
    words = plain.strip("#").split("#")
    out = []
    table = key["table"]

    def pick(v):
        opts = table[v]
        r, acc = rng.random() * sum(w for _, w in opts), 0.0
        for s, w in opts:
            acc += w
            if r <= acc:
                return s
        return opts[-1][0]

    for w in words:
        if "#" + w in table:
            out.append((pick("#" + w), w))
        else:
            i = 0
            while i < len(w):
                two = w[i:i + 2]
                if len(two) == 2 and two in table and rng.random() < key["syl_rate"]:
                    out.append((pick(two), two))
                    i += 2
                else:
                    out.append((pick(w[i]), w[i]))
                    i += 1
        if ntok and len(out) >= ntok:
            break
    # nulls inserted at random positions
    if key["nulls"]:
        m = int(round(key["null_rate"] * len(out)))
        for _ in range(m):
            out.insert(rng.randrange(len(out) + 1), (rng.choice(key["nulls"]), ""))
    if ntok:
        out = out[:ntok]
    return out


def run_pattern(path):
    """Cipher-run token lengths and clear-run letter lengths of a real transcription."""
    return [(k, len(x)) for k, x in parse(path)]

# ---------------------------------------------------------------- evaluation


def evaluate(result, truth):
    key = result["best"]["key"] if "best" in result else result
    tok_ok = tok_n = 0
    true_s, got_s = [], []
    for name, pairs in truth["texts"].items():
        for lab, val in pairs:
            if lab is None:
                continue
            got = key.get(lab, "?")
            tok_n += 1
            tok_ok += (got == val)
            true_s.append(val)
            got_s.append(got)
    a, b = "".join(true_s), "".join(got_s)
    sm = difflib.SequenceMatcher(None, a, b, autojunk=False)
    matched = sum(bl.size for bl in sm.get_matching_blocks())
    # sign-level: fraction of distinct signs whose value is right
    tk = truth["key"]
    sig_ok = sum(1 for s, v in tk.items() if key.get(s) == v and s in key)
    sig_n = sum(1 for s in tk if s in key)
    return dict(token_acc=tok_ok / max(1, tok_n), letter_acc=matched / max(1, len(a)),
                sign_acc=sig_ok / max(1, sig_n), ntok=tok_n)

# ---------------------------------------------------------------- key files


def read_key(path):
    key = {}
    for line in open(path, encoding="utf-8"):
        if line.startswith("#") or not line.strip():
            continue
        parts = line.rstrip("\n").split("\t")
        key[parts[0]] = parts[1] if len(parts) > 1 else ""
    return key


def decode_texts(files, key, mapfile=None):
    texts = load_texts(files, mapfile)
    out = []
    for name, runs in texts:
        parts = []
        for k, x in runs:
            if k == "c":
                parts.append("".join(key.get(lab, "?") for lab in x))
            else:
                parts.append("{" + x.upper() + "}")
        out.append((name, " ".join(parts)))
    return out

# ---------------------------------------------------------------- CLI


def main():
    ap = argparse.ArgumentParser()
    sp = ap.add_subparsers(dest="cmd", required=True)
    s = sp.add_parser("solve")
    s.add_argument("files", nargs="+")
    s.add_argument("--model", required=True)
    s.add_argument("--map")
    s.add_argument("--context", default="none", choices=["none", "clear"])
    s.add_argument("--fix", action="append", default=[])
    s.add_argument("--restarts", type=int, default=8)
    s.add_argument("--iters", type=int, default=100000)
    s.add_argument("--T0", type=float, default=3.0)
    s.add_argument("--T1", type=float, default=0.05)
    s.add_argument("--max-syl", type=int, default=6)
    s.add_argument("--max-word", type=int, default=4)
    s.add_argument("--max-null", type=int, default=2)
    s.add_argument("--max-homo", type=int, default=4)
    s.add_argument("--syl", default="vc", choices=["vc", "cv", "both", "none"])
    s.add_argument("--dots", action="store_true")
    s.add_argument("--shuffle", type=int)
    s.add_argument("--seed", type=int, default=0)
    s.add_argument("--procs", type=int, default=4)
    s.add_argument("--scoring", default="gen", choices=["gen", "llr"])
    s.add_argument("--p-null", type=float, default=0.03)
    s.add_argument("--unit", action="append", default=[],
                   help="label sequence, e.g. 'F p B H c', that must decode to 1-2 corpus words")
    s.add_argument("--vocab", help="corpus file with '#' word boundaries (for --unit)")
    s.add_argument("--out")
    y = sp.add_parser("synth")
    y.add_argument("plain")
    y.add_argument("--design", required=True)
    y.add_argument("--out", required=True)
    y.add_argument("--truth", required=True)
    y.add_argument("--pattern")
    y.add_argument("--ntok", type=int)
    y.add_argument("--seed", type=int, default=0)
    y.add_argument("--key-from", help="reuse the key of an earlier truth.json (joint pair)")
    e = sp.add_parser("eval")
    e.add_argument("result")
    e.add_argument("truth", nargs="+")
    d = sp.add_parser("decode")
    d.add_argument("files", nargs="+")
    d.add_argument("--key", required=True)
    d.add_argument("--map")
    a = ap.parse_args()

    if a.cmd == "solve":
        fix = dict(f.split("=", 1) for f in a.fix)
        caps = dict(syl=a.max_syl if a.syl != "none" else 0, word=a.max_word, null=a.max_null,
                    homo=a.max_homo)
        r = solve(a.files, a.model, a.map, a.context, a.restarts, a.iters, a.T0, a.T1, caps, fix,
                  a.syl if a.syl != "none" else "vc", None, a.dots, a.shuffle, a.seed, a.procs,
                  a.scoring, a.p_null, [u.split() for u in a.unit] or None, a.vocab)
        print(json.dumps(dict(scores=[round(x, 1) for x in r["scores"]], per_token=round(r["per_token"], 3),
                              ntokens=r["ntokens"], nsigns=r["nsigns"]), ensure_ascii=False))
        for name, txt in r["best"]["reading"]:
            print(name, ":", txt[:600])
        if a.out:
            json.dump(r, open(a.out, "w"), ensure_ascii=False, indent=1)
    elif a.cmd == "synth":
        rng = random.Random(a.seed)
        design = json.load(open(a.design))
        plain = open(a.plain).read().strip()
        if a.key_from:
            key = json.load(open(a.key_from))["cipher_key"]
        else:
            key = make_key(design, rng, design.get("syllable_pool"))
        pairs = []
        if a.pattern:
            pat = run_pattern(a.pattern)
            words = plain.strip("#").split("#")
            wi = 0
            lines = []
            for kind, n in pat:
                if kind == "c":
                    seg = []
                    while len(seg) < n and wi < len(words):
                        seg += encipher("#" + words[wi] + "#", dict(key, nulls=[]), rng)
                        wi += 1
                    if key["nulls"]:
                        for _ in range(int(round(key["null_rate"] * n))):
                            seg.insert(rng.randrange(min(len(seg), n) + 1), (rng.choice(key["nulls"]), ""))
                    seg = seg[:n]
                    pairs += seg
                    lines.append(" ".join(l for l, _ in seg))
                else:
                    cl = ""
                    while len(cl) < n and wi < len(words):
                        cl += words[wi] + " "
                        wi += 1
                    pairs.append((None, cl.strip()))
                    lines.append("{" + cl.strip() + "}")
            body = "\n".join(lines)
        else:
            pairs = encipher(plain, key, rng, a.ntok)
            body = " ".join(l for l, _ in pairs)
        open(a.out, "w").write(f"# synthetic control, design {os.path.basename(a.design)}, seed {a.seed}\n"
                               + body + "\n")
        inv = {}
        for v, lst in key["table"].items():
            for sgn, _ in lst:
                inv[sgn] = v.lstrip("#")
        for n in key["nulls"]:
            inv[n] = ""
        used = Counter(l for l, _ in pairs if l)
        json.dump(dict(texts={os.path.basename(a.out): pairs}, key=inv, cipher_key=key,
                       ntok=sum(used.values()), ntypes=len(used),
                       profile=[round(100 * c / sum(used.values()), 1) for _, c in used.most_common()]),
                  open(a.truth, "w"), ensure_ascii=False, indent=1)
        print(f"{a.out}: {sum(used.values())} tokens, {len(used)} types; top %: "
              + " ".join(str(round(100 * c / sum(used.values()), 1)) for _, c in used.most_common(8)))
    elif a.cmd == "eval":
        r = json.load(open(a.result))
        truth = dict(texts={}, key={})
        for t in a.truth:
            tj = json.load(open(t))
            truth["texts"].update(tj["texts"])
            truth["key"].update(tj["key"])
        print(json.dumps(evaluate(r, truth)))
    elif a.cmd == "decode":
        key = read_key(a.key)
        for name, txt in decode_texts(a.files, key, a.map):
            print(name, ":", txt)


if __name__ == "__main__":
    main()
