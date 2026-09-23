#!/usr/bin/env python3
"""Period Italian (15th-c. Lombard chancery) character n-gram model for cipher solving.

Written 23 Sept 2026 for ciphers/sforza-maino-1446. Own code (no copying from the solver repositories).

Subcommands
  corpus  SRC[:WEIGHT]... --out corpus.txt [--exclude FILE] [--min-ratio R]
          Keep only paragraphs that look like 15th-c. chancery Italian (archaic function words such as
          et, ad, de, el, dela, havemo, nuy outnumber modern ones such as il, della, di, sono), normalise
          them and write one paragraph per line. Paragraphs that contain any line of --exclude (the
          control passages) are dropped, so a control is never scored by a model that saw it.
  build   corpus.txt --out model.npz [--order 5]
          Dense interpolated Witten-Bell model over 22 symbols (21 letters + '#' boundary). Stores the
          log-likelihood-ratio table log P(c | 4 previous) - log P(c) as float32.

Normalisation (norm()): lower case, accents stripped, j->i, y->i, v->u, k->ch, w->u; every run of
non-letters becomes '#' in the corpus file (word boundary, used by the control generator); build()
drops those and trains on run-together letters with '#' only at paragraph start and end (the target
ciphers show no word division). Alphabet: a b c d e f g h i l m n o p q r s t u x z.
"""
import argparse
import re
import sys
import unicodedata

import numpy as np

ALPHA = "abcdefghilmnopqrstuxz"
SYMS = ALPHA + "#"
K = len(SYMS)
IDX = {c: i for i, c in enumerate(SYMS)}

ARCHAIC = set("et ad de el dela dele delo deli nuy nui vuy vui havemo havere havuto habiamo epso epsa "
              "anchora perho cossi dicto dicta facto predicto predicta cum sua signoria excellentia "
              "illustrissimo illustrissima prefato prefata quale quali niuno etiam tamen circa lo li "
              "ne se scripto littera lettera".split())
FOREIGN = set("le les des est une qui que dans pour sont avec ont nous vous quod sunt eius atque enim nobis "
              "uobis vobis quae autem sive ipse ipsum illius dominus domini domino nostri sancti eiusdem "
              "item ipsius quam hoc esse erat fuit los las muy senor".split())
MODERN = set("il della delle degli dello nella nelle nel di sono ed alla alle dalla fu stato anche "
             "essere era erano questo gli".split())
# note: 'questo', 'gli', 'essere' also occur in the period; they are counted as modern only to keep
# 19th-c. editorial prose out, and the ratio threshold is set low enough that period letters pass.


def fold(s):
    s = unicodedata.normalize("NFKD", s)
    s = "".join(c for c in s if not unicodedata.combining(c))
    return s.lower()


def norm(s):
    s = fold(s)
    s = s.replace("j", "i").replace("y", "i").replace("v", "u").replace("k", "ch").replace("w", "u")
    s = re.sub(r"[^a-z]+", "#", s)
    s = re.sub(r"[^" + ALPHA + "#]", "", s)
    return re.sub(r"#+", "#", s)


def paragraphs(text):
    buf = []
    for line in text.splitlines():
        if line.strip():
            buf.append(line.strip())
        elif buf:
            yield " ".join(buf)
            buf = []
    if buf:
        yield " ".join(buf)


def archaic_ratio(par):
    w = re.findall(r"[a-z]+", fold(par))
    a = sum(1 for x in w if x in ARCHAIC)
    m = sum(1 for x in w if x in MODERN)
    f = sum(1 for x in w if x in FOREIGN)
    # Latin documents share et/ad/de/cum with period Italian: count Latin inflections as foreign
    f += sum(1 for x in w if len(x) > 3 and re.search(r"(us|um|orum|arum|ibus|ae|is|ur|unt|ent)$", x))
    return a, m, f, len(w)


def cmd_corpus(args):
    excl = []
    if args.exclude:
        excl = [norm(l).strip("#") for l in open(args.exclude, encoding="utf-8") if len(l.strip()) > 20]
    out, kept, total = [], 0, 0
    for spec in args.src:
        src, _, wt = spec.partition(":")
        wt = int(wt or 1)
        raw = open(src, "rb").read()
        try:
            text = raw.decode("utf-8")
        except UnicodeDecodeError:
            text = raw.decode("cp1252", errors="replace")
        for par in paragraphs(text):
            a, m, f, n = archaic_ratio(par)
            total += 1
            if n < 12 or a < 3 or a < args.min_ratio * (m + 1) or f > 0.12 * n:
                continue
            # drop editorial apparatus lines of editions: 'lemma] variant SIGLUM'
            if par.count("]") >= 2:
                continue
            z = norm(par).strip("#")
            if any(e and e[:40] in z for e in excl):
                continue
            out.extend([z] * wt)
            kept += 1
    with open(args.out, "w") as f:
        f.write("\n".join(out) + "\n")
    nchar = sum(len(z) for z in out)
    print(f"kept {kept}/{total} paragraphs, {nchar} symbols -> {args.out}", file=sys.stderr)


def encode(s):
    return np.array([IDX[c] for c in s if c in IDX], dtype=np.int64)


def build(corpus_lines, order=5):
    """Return float32 LLR table of shape K**order, index = sum c_i * K**(order-1-i)."""
    counts = [np.zeros(K ** n, dtype=np.float64) for n in range(order + 1)]
    for line in corpus_lines:
        # corpus lines keep '#' at word boundaries (the control generator needs them); the model is
        # trained on run-together letters, '#' only as paragraph start/end, like the cipher runs
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
    print(f"model order {args.order}, {sum(map(len, lines))} symbols -> {args.out}", file=sys.stderr)


class Model:
    def __init__(self, path):
        z = np.load(path)
        self.llr = z["llr"]
        self.order = int(z["order"])
        self.p1 = z["p1"]
        # full conditional log-probabilities log P(c | 4 previous), same indexing as llr
        self.logp = (self.llr.reshape(-1, K) + np.log(self.p1).reshape(1, K)).reshape(-1).astype(np.float32)

    def score(self, x, w=None):
        """x: int array of symbol ids; w: weight per position (0 = do not score). Positions < order-1
        are context only."""
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


def main():
    ap = argparse.ArgumentParser()
    sp = ap.add_subparsers(dest="cmd", required=True)
    a = sp.add_parser("corpus")
    a.add_argument("src", nargs="+")
    a.add_argument("--out", required=True)
    a.add_argument("--exclude")
    a.add_argument("--min-ratio", type=float, default=1.5)
    b = sp.add_parser("build")
    b.add_argument("corpus")
    b.add_argument("--out", required=True)
    b.add_argument("--order", type=int, default=5)
    args = ap.parse_args()
    {"corpus": cmd_corpus, "build": cmd_build}[args.cmd](args)


if __name__ == "__main__":
    main()
