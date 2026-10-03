#!/usr/bin/env python3
"""A2-RAA10 stronger bottom-digit statistics (pre-registered in data/vowelcol2/PREREG.md, 3 Oct 2026).

T = max over 24 bijections of vowel-trigram minus unigram LL per token (bottom digit);
X = I(b_{i-1}; t_i) + I(b_{i-1}; b_i), label-free plug-in MI (both digits).
Null: 200 whole-cell permutations. POS/ALT controls at N=370 first; power gate 18/20 per statistic.
Deterministic (seed 20261003). Writes data/vowelcol2/result.tsv.
v2: POS windows folded per word (v1 used jp.fold on the whole window, which drops spaces, so
the pre-registered "same word" rule was not applied; v1 kept as data/vowelcol2/*_v1_wordbreak_bug.*).
"""
import itertools, math, random, sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "tools"))
import judge_plaintext as jp  # noqa: E402

T = Path(__file__).resolve().parents[1]
V = "eiao"; N = 370; NPERM = 200; NCTL = 20; SEED = 20261003; GATE = 18
HELD = "pg10820"


def fold_v(s):
    return s.replace("ij", "i").replace("y", "i")


def vowels(letters):
    return [V.index(c) for c in fold_v(letters) if c in V]


files = sorted((ROOT / "tools/data/nl20").glob("*.txt.gz"))
train = "".join(jp.fold(jp.read_corpus(f)) for f in files if HELD not in f.name)
held_raw = jp.read_corpus([f for f in files if HELD in f.name][0])
held = jp.fold(held_raw)
tv = vowels(train)
uni = Counter(tv); bi = Counter(zip(tv, tv[1:])); tri = Counter(zip(tv, tv[1:], tv[2:]))
lu = [math.log((uni[a] + .5) / (len(tv) + 2)) for a in range(4)]
lt = {(a, b, c): math.log((tri[(a, b, c)] + .5) / (bi[(a, b)] + 2))
      for a in range(4) for b in range(4) for c in range(4)}
PERMS = list(itertools.permutations(range(4)))


def stat_T(cells):
    seq = [b for _, b in cells]; best = -9e9
    for p in PERMS:
        s = [p[x] for x in seq]
        g = sum(lt[(a, b, c)] - lu[c] for a, b, c in zip(s, s[1:], s[2:])) / (len(s) - 2)
        best = max(best, g)
    return best


def mi(pairs):
    n = len(pairs); j = Counter(pairs); x = Counter(a for a, _ in pairs); y = Counter(b for _, b in pairs)
    return sum(c / n * math.log(c * n / (x[a] * y[b])) for (a, b), c in j.items())


def stat_X(cells):
    pb = [c[1] for c in cells[:-1]]
    return mi(list(zip(pb, [c[0] for c in cells[1:]]))) + mi(list(zip(pb, [c[1] for c in cells[1:]])))


STATS = {"T": stat_T, "X": stat_X}


def test(cells, rng):
    real = {k: f(cells) for k, f in STATS.items()}; ge = Counter(); s = list(cells)
    for _ in range(NPERM):
        rng.shuffle(s)
        for k, f in STATS.items():
            ge[k] += f(s) >= real[k]
    return {k: (real[k], (1 + ge[k]) / (NPERM + 1)) for k in STATS}


CONS = sorted(set("bcdfghjklmnpqrstvwxz"))


def pos_cells(text, rng):
    rows = {c: rng.randrange(6) for c in CONS}
    out = []; prev = None
    for w in (fold_v(jp.fold(w)) for w in text.split()):  # fold per word: jp.fold drops spaces
        prev = None
        for ch in w:
            if ch in V:
                out.append((6 if prev is None else rows[prev], V.index(ch))); prev = None
            elif ch in rows:
                prev = ch
            if len(out) == N:
                return out
    return out


rng = random.Random(SEED)
starts = rng.sample(range(0, len(held) - 8000), NCTL)
rows = []
for i, st in enumerate(starts):  # POS: windows of word-separated held-out text
    r = test(pos_cells(held_raw[st:st + 8000], rng), rng)  # raw text keeps word breaks
    rows.append(("POS", i, r))
lf = [c for c, _ in Counter(train).most_common() if c != " "]
cells28 = [(t, b) for t in range(7) for b in range(4)]
for i, st in enumerate(starts):  # ALT, as A2-RAA8
    cs = cells28[:]; rng.shuffle(cs)
    m = {c: cs[j] for j, c in enumerate(lf[:24])}
    for j, c in enumerate(lf[24:]):
        m[c] = cs[24 + j % 4]
    seq = [m[c] for c in held[st + 7:].replace(" ", "")[:N]]
    rows.append(("ALT", i, test(seq, rng)))
pw = {k: sum(r[2][k][1] < .05 for r in rows if r[0] == "POS") for k in STATS}
fp = {k: sum(r[2][k][1] < .05 for r in rows if r[0] == "ALT") for k in STATS}
for k in STATS:
    print(f"{k}: POS power {pw[k]}/{NCTL}; ALT pass {fp[k]}/{NCTL}")
passing = [k for k in STATS if pw[k] >= GATE]
with open(T / "data/vowelcol2/result.tsv", "w") as f:
    f.write("set\ti\tT\tpT\tX\tpX\n")
    for s, i, r in rows:
        f.write(f"{s}\t{i}\t{r['T'][0]:.5f}\t{r['T'][1]:.4f}\t{r['X'][0]:.5f}\t{r['X'][1]:.4f}\n")
    if passing:
        tok = (T / "data/masc/cells_370.txt").read_text().split()
        tc = [(int(t[0]) - 1 if t[0].isdigit() else 0, int(t[1]) - 1) for t in tok]
        r = test(tc, rng)
        f.write(f"TARGET\t0\t{r['T'][0]:.5f}\t{r['T'][1]:.4f}\t{r['X'][0]:.5f}\t{r['X'][1]:.4f}\n")
        for k in passing:
            g, p = r[k]; p = min(1, p * len(passing))
            pg = sorted(x[2][k][0] for x in rows if x[0] == "POS")
            ag = sorted(x[2][k][0] for x in rows if x[0] == "ALT"); a90 = ag[int(.9 * len(ag)) - 1]
            v = ("consistent with H_rv" if p < .05 and pg[0] <= g <= pg[-1] and g > a90
                 else "against H_rv" if p >= .05 else "cannot decide")
            print(f"TARGET {k} {g:.4f} p(adj) {p:.4f} -> {v}")
    else:
        print("VERDICT: non-test at N=370 (no statistic reaches POS 18/20); target not scored")
