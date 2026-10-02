#!/usr/bin/env python3
"""GAPS7-moray-wood-1568 (2 Oct 2026): lexical fit of the 17 non-S tokens (16 M + 1 I) of Aymeloglu's reading against
tools/data/sco16 -- a script, not eyes. Disk only, no network, no vision.

Per non-S sign: the candidate values the key and the glyph evidence on file allow (CANDS below, each with its source).
Per occurrence group (all tokens of one sign inside one word, varied together; every other token at its key.tsv value),
each candidate word is scored in context:
  score(w) = log P(w | prev) + log P(next | w)
with an interpolated word bigram (0.7 bigram + 0.3 unigram) whose unigram is 0.9 word-list frequency + 0.1 a letter
5-gram model of words (so out-of-list spellings still get a finite, comparable score). Words come from Aymeloglu's own
segmentation (WORDS below), u/v and i/j folded. Person-signs and word-signs take whole words as candidates.

Pre-registered rule (written before any score was seen): a sign goes M/I -> S only if, at EVERY occurrence group of that
sign, the same candidate wins and beats the runner-up by MARGIN = ln(10) = 2.303 nats (a 10:1 likelihood ratio).
A sign with a single candidate on file is not contestable and stays as it is.

Matched control (rule 3): the same fit with the signs' candidate sets permuted across signs (20 seeds, derangements:
no sign keeps an identical set); report how often a shuffled assignment clears the same rule. The control varies on the
fit's own axis (which values compete in which word), so it can fail differently from the real run.
  python3 ciphers/moray-wood-1568/lexfit.py            # writes lexfit.tsv, prints the summary
"""
import math, random, re, sys
from collections import Counter
from pathlib import Path

HERE = Path(__file__).resolve().parent; ROOT = HERE.parents[1]
sys.path.insert(0, str(ROOT / "tools"))
from judge_plaintext import read_corpus, LANG_CORPORA  # noqa: E402

MARGIN = math.log(10)
# sign -> (candidates, source on file). Baseline (key.tsv value) first.
CANDS = {
    "g":  (["f", "ff"], "key.tsv note: single glyph for f or ff"),
    "4b": (["quene", "king", "regent", "lord"], "person-sign, context only (key.tsv); Queen presumed, other persons of the letter"),
    "Eb": (["quene", "king", "regent", "lord"], "person-sign, as 4b"),
    "c":  (["r", "e", "f"], "key.tsv: r in Carlyle, second should be e (slip); NOTES gap 4: L1.41 his e = f, read c"),
    "Z5": (["y", "i"], "key.tsv: i also possible (Carlile, haim)"),
    "o2": (["and", "of", "to", "in", "the"], "word-sign standing alone between two clauses (I); common function words"),
    "Zz": (["t", "k"], "key.tsv: k also possible (lattis/lakkis)"),
    "s":  (["p"], "key.tsv: spil; no alternative named on file"),
    "t":  (["t", "s"], "key.tsv: baseline t unidentified; s (es = as) a conjecture"),
    "x3": (["e", "n"], "key.tsv: fresh visual comparison favours n"),
    "Xs": (["u"], "GAPS5: u by identity with X; his value ?; no alternative letter named on file"),
}
# Aymeloglu's segmentation: (line, first pos, last pos) per word, in reading order.
WORDS = [("L1", 1, 1), ("L1", 3, 10), ("L1", 11, 12), ("L1", 13, 13), ("L1", 14, 19), ("L1", 20, 21), ("L1", 22, 28),
         ("L1", 30, 30), ("L1", 32, 38), ("L1", 40, 43), ("L1", 45, 46), ("L1", 47, 47), ("L1", 48, 51),
         ("L2", 1, 7), ("L2", 8, 10), ("L2", 11, 14), ("L2", 15, 19), ("L2", 20, 23), ("L2", 24, 26), ("L2", 27, 27),
         ("L2", 28, 28), ("L2", 30, 35), ("L2", 37, 40), ("L2", 41, 45),
         ("L3", 1, 6), ("L3", 8, 9), ("L3", 10, 13), ("L3", 14, 15), ("L3", 17, 20), ("L3", 21, 21), ("L3", 23, 27),
         ("L3", 28, 29), ("L3", 31, 34), ("L3", 36, 43), ("L4", 1, 7)]


def norm(w):
    return w.lower().replace("v", "u").replace("j", "i")


toks = [l.rstrip("\n").split("\t") for l in open(HERE / "reading_tokens.tsv") if not l.startswith("#")][1:]
tok = {(r[0], int(r[1])): (r[2], r[3], r[4]) for r in toks}
nonS = [(k, v) for k, v in tok.items() if v[2] in "MI"]
assert len(nonS) == 17 and all(v[0] in CANDS for _, v in nonS), nonS

# ---- models from sco16
words_c = []
for p in LANG_CORPORA["sco16"]:
    words_c += [norm(w) for w in re.findall(r"[A-Za-z]+", read_corpus(p))]
uni = Counter(words_c); big = Counter(zip(words_c, words_c[1:])); T = len(words_c)
ch = Counter(); ctx = Counter()
for w, n in uni.items():
    s = "^^^^" + w + "$"
    for i in range(4, len(s)):
        for k in range(1, 5):
            ch[s[i - k:i + 1]] += n; ctx[s[i - k:i]] += n
nch = sum(n * (len(w) + 1) for w, n in uni.items()); ch1 = Counter()
for w, n in uni.items():
    for c in w + "$":
        ch1[c] += n


def pchar(w):
    s = "^^^^" + w + "$"; lp = 0.0
    for i in range(4, len(s)):
        p = (ch1[s[i]] + 1) / (nch + 28)
        for k in range(1, 5):  # interpolated, Witten-Bell-ish fixed weights
            if ctx[s[i - k:i]]:
                p = 0.6 * ch[s[i - k:i + 1]] / ctx[s[i - k:i]] + 0.4 * p
        lp += math.log(p)
    return math.exp(lp)


def puni(w):
    return 0.9 * uni[w] / T + 0.1 * pchar(w)


def pbig(a, b):
    return (0.7 * big[(a, b)] / uni[a] if uni[a] else 0.0) + 0.3 * puni(b)


def render(assign):
    """assign: {(line,pos): value}; returns list of normalized words in reading order."""
    out = []
    for ln, a, b in WORDS:
        out.append(norm("".join(assign.get((ln, p), tok[(ln, p)][1]) for p in range(a, b + 1) if (ln, p) in tok)))
    return out


def word_index(ln, pos):
    for i, (l, a, b) in enumerate(WORDS):
        if l == ln and a <= pos <= b:
            return i
    raise KeyError((ln, pos))


def ctx_score(words, i):
    w = words[i]; s = math.log(pbig(words[i - 1], w)) if i else math.log(puni(w))
    if i + 1 < len(words):
        s += math.log(pbig(w, words[i + 1]))
    return s


def groups_of(sign):
    g = {}
    for (ln, pos), v in tok.items():
        if v[0] == sign:
            g.setdefault(word_index(ln, pos), []).append((ln, pos))
    return g


def fit(cands):
    """cands: {sign: [values]} -> {sign: dict(result)}"""
    res = {}
    for sign, cs in cands.items():
        rows = []
        for wi, occ in sorted(groups_of(sign).items()):
            sc = []
            for v in cs:
                words = render({o: v for o in occ})
                sc.append((ctx_score(words, wi), v, words[wi]))
            sc.sort(reverse=True)
            m = sc[0][0] - sc[1][0] if len(sc) > 1 else None
            rows.append(dict(word=wi, occ=occ, ranked=sc, winner=sc[0][1], margin=m))
        win = {r["winner"] for r in rows}
        ok = len(cs) > 1 and len(win) == 1 and all(r["margin"] >= MARGIN for r in rows)
        res[sign] = dict(rows=rows, promote=ok, value=rows[0]["winner"] if ok else None)
    return res


if __name__ == "__main__":
    real_c = {s: c for s, (c, _) in CANDS.items()}
    real = fit(real_c)
    out = [("kind", "seed", "sign", "word_index", "occurrences", "winner", "margin_nats", "ranked", "promote")]
    for s, r in real.items():
        for row in r["rows"]:
            out.append(("real", 0, s, row["word"], ",".join(f"{l}.{p}" for l, p in row["occ"]), row["winner"],
                        "" if row["margin"] is None else round(row["margin"], 3),
                        " ".join(f"{w}={sc:.2f}" for sc, v, w in row["ranked"]), r["promote"]))
    signs = list(CANDS); sets = [real_c[s] for s in signs]
    ctl = []
    for seed in range(1, 21):
        rng = random.Random(seed)
        while True:
            perm = sets[:]; rng.shuffle(perm)
            if all(perm[i] != sets[i] for i in range(len(signs))):
                break
        res = fit(dict(zip(signs, perm)))
        prom = [s for s in signs if res[s]["promote"]]
        ctl.append((seed, prom, sum(len(perm[i]) > 1 for i in range(len(signs)))))
        for s in signs:
            for row in res[s]["rows"]:
                out.append(("shuffled", seed, s, row["word"], ",".join(f"{l}.{p}" for l, p in row["occ"]), row["winner"],
                            "" if row["margin"] is None else round(row["margin"], 3),
                            " ".join(f"{w}={sc:.2f}" for sc, v, w in row["ranked"]), res[s]["promote"]))
    with open(HERE / "lexfit.tsv", "w") as f:
        f.write("# generated by lexfit.py (GAPS7, 2 Oct 2026); do not edit. margin rule ln(10)=2.303 nats at every occurrence group\n")
        for r in out:
            f.write("\t".join(map(str, r)) + "\n")
    print(f"corpus sco16: {T} words, {len(uni)} types; MARGIN {MARGIN:.3f} nats")
    for s, r in real.items():
        rs = "; ".join(f"[{' '.join(f'{w}={sc:.2f}' for sc, v, w in row['ranked'])}] m={'-' if row['margin'] is None else round(row['margin'], 2)}"
                       for row in r["rows"])
        print(f"REAL {s:3} {'PROMOTE '+r['value'] if r['promote'] else 'stay':14} {rs}")
    contest = sum(len(c) > 1 for c in sets)
    n_prom = sum(len(p) for _, p, _ in ctl)
    print(f"REAL promoted: {sum(r['promote'] for r in real.values())} of {contest} contestable signs")
    print(f"CONTROL (20 derangements of candidate sets): sign-promotions {n_prom} of {sum(c for _, _, c in ctl)} contestable "
          f"slots ({100*n_prom/sum(c for _, _, c in ctl):.1f} pct); seeds with >=1 promotion {sum(bool(p) for _, p, _ in ctl)}/20")
    print("  per seed:", "; ".join(f"{sd}:{','.join(p) or '-'}" for sd, p, _ in ctl))
