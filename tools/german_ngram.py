#!/usr/bin/env python3
"""Early New High German (16th-c. chancery) character n-gram model for cipher solving.

Written 24 Sept 2026 (LANE R3 J7) for ciphers/jan-van-nassau-1572-75, on the pattern of tools/italian_ngram.py
(same file format and Model API, so tools/nomenclator_anneal.py can load either with --lang).

Subcommands
  corpus  SRC[:WEIGHT]... --out corpus.txt [--exclude FILE] [--min-ratio R]
          Keep paragraphs that look like German (function words und/vnd, der, die, das, zu, von, mit, sich, nit,
          E.G. ... outnumber French, Dutch and Latin ones), drop '#' comment lines, HTML navigation and editorial
          lines, normalise, and write one paragraph per line with '#' word boundaries. Paragraphs that share a
          40-letter stretch with any line of --exclude are dropped, so a control text is never in its own model.
  build   corpus.txt --out model.npz [--order 5]
          Dense interpolated Witten-Bell model over 24 symbols (23 letters + '#'), stored as the log-likelihood
          ratio table log P(c | previous) - log P(c), float32, exactly as italian_ngram.build.
  score   model.npz TEXT        mean LLR per letter of TEXT (a quick check that the model prefers German).

Normalisation (norm()): lower case, umlauts and accents stripped (ü->u, ö->o, ä->a), ß->ss, j->i, y->i, v->u;
k and w are kept (German uses both). Alphabet: a b c d e f g h i k l m n o p q r s t u w x z.

Test: python3 tools/tests/test_german_ngram.py (offline).
"""
import argparse
import re
import sys
import unicodedata

import numpy as np

ALPHA = "abcdefghiklmnopqrstuwxz"
SYMS = ALPHA + "#"
K = len(SYMS)
IDX = {c: i for i, c in enumerate(SYMS)}
# for nomenclator_anneal --lang de
CONS = "bcdfghklmnprstwz"
FREQ_LETTERS = "enirsatdhulgcombfwkzp"
DEFAULT_WORDS = "und der die das zu von mit nit sich den dem ist".split()

GERMAN = set("und vnd der die das dasz daß zu von mit nit nicht sich den dem ist auch auf uff auff ausz aus wir ich "
             "sie ein eine einen haben hab sein sey seyn wol wohl solle solte wurde werden bey bisz noch ahn an "
             "desz des so wie wan wann doch dan denn derhalben hiemit gnediger gnedigen herr eg".split())
FOREIGN = set("le la les de des et est que qui pour nous vous une en het van een ende niet dat wy u "
              "quod sunt est cum ad in non et ut per".split()) - GERMAN


def fold(s):
    s = unicodedata.normalize("NFKD", s.replace("ß", "ss"))
    s = "".join(c for c in s if not unicodedata.combining(c))
    return s.lower()


def norm(s):
    s = fold(s)
    s = s.replace("j", "i").replace("y", "i").replace("v", "u")
    s = re.sub(r"[^a-z]+", "#", s)
    s = re.sub(r"[^" + ALPHA + "#]", "", s)
    return re.sub(r"#+", "#", s)


def paragraphs(text):
    buf = []
    for line in text.splitlines():
        if line.lstrip().startswith("#"):
            continue
        if line.strip():
            buf.append(line.strip())
        elif buf:
            yield " ".join(buf)
            buf = []
    if buf:
        yield " ".join(buf)


def german_ratio(par):
    w = re.findall(r"[a-z]+", fold(par).replace("e.g.", "eg"))
    g = sum(1 for x in w if x in GERMAN)
    f = sum(1 for x in w if x in FOREIGN)
    return g, f, len(w)


def select(text, excl=(), min_ratio=2.0):
    out = []
    for par in paragraphs(text):
        g, f, n = german_ratio(par)
        if n < 8 or g < 3 or g < min_ratio * (f + 1) or "[/" in par or "http" in par:
            continue
        z = norm(par).strip("#")
        if any(e and e[:40] in z.replace("#", "") for e in excl):
            continue
        out.append(z)
    return out


def cmd_corpus(args):
    excl = []
    if args.exclude:
        excl = [norm(l).replace("#", "") for l in open(args.exclude, encoding="utf-8")
                if len(l.strip()) > 20 and not l.startswith("#")]
    out = []
    for spec in args.src:
        src, _, wt = spec.partition(":")
        raw = open(src, "rb").read()
        try:
            text = raw.decode("utf-8")
        except UnicodeDecodeError:
            text = raw.decode("cp1252", errors="replace")
        out.extend(select(text, excl, args.min_ratio) * int(wt or 1))
    with open(args.out, "w") as f:
        f.write("\n".join(out) + "\n")
    print(f"{len(out)} paragraphs, {sum(len(z.replace('#', '')) for z in out)} letters -> {args.out}",
          file=sys.stderr)


def encode(s):
    return np.array([IDX[c] for c in s if c in IDX], dtype=np.int64)


def build(corpus_lines, order=5):
    """Return (float32 LLR table of shape K**order, unigram p1); index = sum c_i * K**(order-1-i)."""
    counts = [np.zeros(K ** n, dtype=np.float64) for n in range(order + 1)]
    for line in corpus_lines:
        x = encode("#" * (order - 1) + line.replace("#", "") + "#")
        for n in range(1, order + 1):
            if len(x) < n:
                continue
            idx = np.zeros(len(x) - n + 1, dtype=np.int64)
            for j in range(n):
                idx = idx * K + x[j:len(x) - n + 1 + j]
            counts[n] += np.bincount(idx, minlength=K ** n)
    p1 = (counts[1] + 1.0) / (counts[1].sum() + K)
    prev = p1.reshape(1, K)
    for n in range(2, order + 1):
        c = counts[n].reshape(K ** (n - 1), K)
        tot = c.sum(1, keepdims=True)
        types = (c > 0).sum(1, keepdims=True)
        lower = np.tile(prev, (K, 1)) if n > 2 else np.tile(prev, (K ** (n - 1), 1))
        with np.errstate(invalid="ignore", divide="ignore"):
            p = np.where(tot > 0, (c + types * lower) / np.maximum(tot + types, 1e-12), lower)
        prev = p
    llr = np.log(prev) - np.log(p1).reshape(1, K)
    return llr.reshape(-1).astype(np.float32), p1


def cmd_build(args):
    lines = [l.strip() for l in open(args.corpus) if l.strip()]
    llr, p1 = build(lines, args.order)
    np.savez_compressed(args.out, llr=llr, p1=p1, order=args.order, syms=SYMS)
    print(f"model order {args.order}, {sum(len(l.replace('#', '')) for l in lines)} letters -> {args.out}",
          file=sys.stderr)


class Model:
    def __init__(self, path):
        z = np.load(path)
        if str(z["syms"]) != SYMS:
            raise SystemExit(f"{path}: not a german_ngram model (symbols {z['syms']})")
        self.llr = z["llr"]
        self.order = int(z["order"])
        self.p1 = z["p1"]
        # full conditional log-probabilities log P(c | previous), same indexing as llr (nomenclator_anneal 'gen')
        self.logp = (self.llr.reshape(-1, K) + np.log(self.p1).reshape(1, K)).reshape(-1).astype(np.float32)

    def score(self, x, w=None):
        o = self.order
        n = len(x) - o + 1
        if n <= 0:
            return 0.0
        idx = x[:n].copy()
        for j in range(1, o):
            idx = idx * K + x[j:j + n]
        v = self.llr[idx]
        if w is not None:
            v = v * w[o - 1:]
        return float(v.sum())

    def mean_llr(self, text):
        z = norm(text).replace("#", "")
        x = encode("#" * (self.order - 1) + z)
        return self.score(x) / max(1, len(z))


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sp = ap.add_subparsers(dest="cmd", required=True)
    a = sp.add_parser("corpus")
    a.add_argument("src", nargs="+")
    a.add_argument("--out", required=True)
    a.add_argument("--exclude")
    a.add_argument("--min-ratio", type=float, default=2.0)
    b = sp.add_parser("build")
    b.add_argument("corpus")
    b.add_argument("--out", required=True)
    b.add_argument("--order", type=int, default=5)
    c = sp.add_parser("score")
    c.add_argument("model")
    c.add_argument("text")
    args = ap.parse_args()
    if args.cmd == "score":
        print(round(Model(args.model).mean_llr(args.text), 3))
    else:
        {"corpus": cmd_corpus, "build": cmd_build}[args.cmd](args)


if __name__ == "__main__":
    main()
