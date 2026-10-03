#!/usr/bin/env python3
"""A2-RAA8 vowel-column order test (pre-registered in data/vowelcol/PREREG.md, 3 Oct 2026).

Is the leaf-2 bottom-digit sequence ordered like the Dutch vowel sequence over {e,i,a,o}?
G = max over 24 bijections of (bigram LL - unigram LL) per token; null = 200 order permutations.
Controls POS (vowel sequences of held-out nl20 windows) and ALT (one-cell-per-letter ciphers on a
random 7x4 table) are scored first. Deterministic (seed 20261003). Writes data/vowelcol/result.tsv.
"""
import itertools, math, random, sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "tools"))
import judge_plaintext as jp  # noqa: E402

T = Path(__file__).resolve().parents[1]
V = "eiao"; N = 370; NPERM = 200; NCTL = 20; SEED = 20261003
HELD = "pg10820"


def vowels(letters):
    s = letters.replace("ij", "i").replace("y", "i")
    return [V.index(c) for c in s if c in V]


files = sorted((ROOT / "tools/data/nl20").glob("*.txt.gz"))
train = "".join(jp.fold(jp.read_corpus(f)) for f in files if HELD not in f.name)
held = jp.fold(jp.read_corpus([f for f in files if HELD in f.name][0]))
tv = vowels(train)
uni = Counter(tv); bi = Counter(zip(tv, tv[1:]))
lu = [math.log((uni[a] + .5) / (len(tv) + 2)) for a in range(4)]
lb = [[math.log((bi[(a, b)] + .5) / (uni[a] + 2)) for b in range(4)] for a in range(4)]
PERMS = list(itertools.permutations(range(4)))


def G(seq):
    best = -9e9
    for p in PERMS:
        s = [p[x] for x in seq]
        g = sum(lb[a][b] - lu[b] for a, b in zip(s, s[1:])) / (len(s) - 1)
        best = max(best, g)
    return best


def test(seq, rng):
    g = G(seq); s = list(seq); ge = 0
    for _ in range(NPERM):
        rng.shuffle(s); ge += G(s) >= g
    return g, (1 + ge) / (NPERM + 1)


rng = random.Random(SEED)
starts = rng.sample(range(0, len(held) - 5000), NCTL)
rows = []
for i, st in enumerate(starts):  # POS
    seq = vowels(held[st:st + 5000])[:N]
    g, p = test(seq, rng); rows.append(("POS", i, g, p))
lf = [c for c, _ in Counter(train).most_common()]
cells = [(t, b) for t in range(7) for b in range(4)]
for i, st in enumerate(starts):  # ALT
    cs = cells[:]; rng.shuffle(cs)
    m = {c: cs[j] for j, c in enumerate(lf[:24])}
    for j, c in enumerate(lf[24:]):
        m[c] = cs[24 + j % 4]
    seq = [m[c][1] for c in held[st + 7:st + 7 + N]]
    g, p = test(seq, rng); rows.append(("ALT", i, g, p))
tok = (T / "data/masc/cells_370.txt").read_text().split()
tseq = [int(t[1]) - 1 for t in tok]
g, p = test(tseq, rng); rows.append(("TARGET", 0, g, p))
with open(T / "data/vowelcol/result.tsv", "w") as f:
    f.write("set\ti\tG\tp\n")
    for r in rows:
        f.write(f"{r[0]}\t{r[1]}\t{r[2]:.5f}\t{r[3]:.4f}\n")
pos = [r for r in rows if r[0] == "POS"]; alt = [r for r in rows if r[0] == "ALT"]
pw = sum(r[3] < .05 for r in pos); fp = sum(r[3] < .05 for r in alt)
pg = sorted(r[2] for r in pos); ag = sorted(r[2] for r in alt)
a90 = ag[int(.9 * len(ag)) - 1]
print(f"POS power {pw}/{NCTL} G {pg[0]:.4f}..{pg[-1]:.4f}; ALT pass {fp}/{NCTL} G {ag[0]:.4f}..{ag[-1]:.4f} p90 {a90:.4f}")
print(f"TARGET G {g:.4f} p {p:.4f}; bottom counts {Counter(tseq)}")
if pw < 16:
    v = "non-test (POS power below 16/20)"
elif p < .05 and pg[0] <= g <= pg[-1] and g > a90:
    v = "consistent with Hv"
elif p >= .05:
    v = "against Hv"
else:
    v = "cannot decide"
print("VERDICT:", v)
