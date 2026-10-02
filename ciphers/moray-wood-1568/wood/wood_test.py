#!/usr/bin/env python3
"""GAPS9-moray-wood-1568 (2 Oct 2026): the Zz gap's Wood-line key test.

Applies Aymeloglu's key (../key.tsv, credited) to the 39-sign Wood line (wood_line.tsv, Bourdeau's sign order relabelled
into the Moray label set) and asks whether key.tsv reads it better than shuffled keys do.

Statistic: sco16 letter 4-gram mean log10 score (tools/judge_plaintext.NgramModel, the GAPS6 judge corpus) of the decode,
unmatched signs ('?') skipped. Null: 1,000 shuffled keys, the single-letter values permuted among the single-letter signs
(word- and person-signs fixed); the statistic is a function of the values, so the null can move it (rule 3: not orthogonal).
Result per text: rank = share of shuffled keys scoring below key.tsv.
Positive control (matched N): every contiguous 39-sign window of the Moray postscript itself (96 windows, gaps ignored),
same statistic, same 1,000 shuffled keys -- shows what rank key.tsv reaches at N=39 on text it is known to read.
Variants: the four low-confidence relabels (r3 -> Zz/Z5/?, Z -> Z3/Z5, x2 -> N/xd, x3 -> x3/x) run as 24 variants; the
primary is the first of each list, fixed before scoring. Also the one-value question the gap asks: Zz = t vs k.
Frequency check (added after the first run showed shuffled-key ranks reward letter frequency alone): absolute scores --
the Wood decode against (a) the 96 Moray windows' own scores and (b) 200 letter-order shuffles of the same Wood decode
(same letters, so frequency is held fixed and only order can move the score). Deterministic (seed 1). Writes wood_test.tsv.   python3 ciphers/moray-wood-1568/wood/wood_test.py
"""
import itertools, random, sys
from pathlib import Path

HERE = Path(__file__).resolve().parent; T = HERE.parent; ROOT = T.parents[1]
sys.path.insert(0, str(ROOT / "tools"))
from judge_plaintext import NgramModel, read_corpus, LANG_CORPORA, pct  # noqa: E402

model = NgramModel([read_corpus(p) for p in LANG_CORPORA["sco16"]])
key = {r[0]: r[1] for r in (l.rstrip("\n").split("\t") for l in open(T / "key.tsv") if not l.startswith("#")) if r[0] != "code"}
WORD = {"U": "the", "o2": "and"}; DROP = {"4b", "Eb"}
letters = sorted(c for c, v in key.items() if len(v) == 1 and c not in WORD and c not in DROP)
rnd = random.Random(1)
shuffled = []
for _ in range(1000):
    vals = [key[c] for c in letters]; rnd.shuffle(vals); shuffled.append(dict(key, **dict(zip(letters, vals))))


def render(seq, k):
    return "".join(WORD.get(s, k.get(s, "")) for s in seq if s not in DROP and s != "?" and s in k)


def rank(seq, k=key):
    sc = model.score(render(seq, k))
    null = [model.score(render(seq, kk)) for kk in shuffled]
    return sc, sum(x < sc for x in null) / len(null)


wood = [l.rstrip("\n").split("\t") for l in open(HERE / "wood_line.tsv") if not l.startswith("#")][1:]
bour = [r[1] for r in wood]
primary = {r[1]: r[2] for r in wood}
moray = [l.rstrip("\n").split("\t")[2] for l in open(T / "ciphertext.tsv") if not l.startswith("#")][1:]
moray = [s for s in moray if s != "|"]
out = [("text", "variant", "letters", "decode", "score", "rank_vs_1000_shuffled_keys", "lettershuffle_p99", "rank_vs_200_letter_shuffles", "moray_windows_below")]

# positive control: 39-sign Moray windows
ctl = []
for i in range(len(moray) - 39 + 1):
    w = moray[i:i + 39]; sc, rk = rank(w); ctl.append(rk)
    out.append(("moray_window", f"start {i + 1}", len(render(w, key)), render(w, key), round(sc, 4), rk))
ctl_s = sorted(ctl)
print(f"positive control: {len(ctl)} Moray 39-sign windows, key.tsv rank vs 1000 shuffled keys: min {ctl_s[0]:.3f} "
      f"median {ctl_s[len(ctl_s) // 2]:.3f}; >=0.95 in {sum(r >= 0.95 for r in ctl)}/{len(ctl)}; >=0.99 in {sum(r >= 0.99 for r in ctl)}/{len(ctl)}")

# target: the Wood line, primary relabel and 24 variants
VAR = {"r3": ["Zz", "Z5", "?"], "Z": ["Z3", "Z5"], "x2": ["N", "xd"], "x3": ["x3", "x"]}
ranks = []
for combo in itertools.product(*VAR.values()):
    m = dict(primary, **dict(zip(VAR, combo)))
    seq = [m[b] for b in bour]; sc, rk = rank(seq); ranks.append(rk)
    tag = " ".join(f"{a}={b}" for a, b in zip(VAR, combo))
    out.append(("wood_line", tag, len(render(seq, key)), render(seq, key), round(sc, 4), rk))
    if len(ranks) == 1:
        print(f"wood line, primary relabel ({tag}): decode '{render(seq, key)}' score {sc:.3f} rank {rk:.3f}")
rs = sorted(ranks)
print(f"wood line, 24 relabel variants: rank min {rs[0]:.3f} median {rs[12]:.3f} max {rs[-1]:.3f}; >=0.95 in {sum(r >= 0.95 for r in ranks)}/24")

# frequency-held null: absolute score of each Wood variant vs Moray windows (positive) and letter-order shuffles (negative)
mw = sorted(r[4] for r in out if r[0] == "moray_window")
real, nul, _ = model.controls(35, samples=1000)
print(f"sco16 in-sample windows at N=35 (1000, seed 1): real p01 {real[10]:.3f} p05 {real[50]:.3f}; letter-shuffled null p99 {nul[990]:.3f}")
print(f"moray windows absolute score: min {mw[0]:.3f} median {mw[len(mw) // 2]:.3f} max {mw[-1]:.3f}")
for r in [r for r in out if r[0] == "wood_line"]:
    L = list(r[3]); sh = []
    for sd in range(200):
        random.Random(sd).shuffle(L); sh.append(model.score("".join(L)))
    sh.sort(); r2 = list(r) + [round(sh[-3], 4), round(sum(x < r[4] for x in sh) / 200, 3), sum(x < r[4] for x in mw)]
    out[out.index(r)] = tuple(r2)
wl = [r for r in out if r[0] == "wood_line"]
print("wood variants: letter-shuffle rank min %.3f median %.3f max %.3f; abs score max %.3f (Moray windows below it: %d/96)" % (
    min(r[7] for r in wl), sorted(r[7] for r in wl)[12], max(r[7] for r in wl), max(r[4] for r in wl), max(r[8] for r in wl)))
print("primary: letter-shuffle p99 %.3f, rank %.3f" % (wl[0][6], wl[0][7]))

# the gap's own question: Zz t vs k on the Wood line (primary relabel, r3 = Zz)
seq = [primary[b] for b in bour]
for v in ("t", "k"):
    sc, rk = rank(seq, dict(key, Zz=v))
    out.append(("wood_line", f"Zz={v}", len(render(seq, key)), render(seq, dict(key, Zz=v)), round(sc, 4), rk))
    print(f"wood line, Zz={v}: score {sc:.4f} rank {rk:.3f}")
with open(HERE / "wood_test.tsv", "w") as f:
    f.write("# generated by wood_test.py (GAPS9-moray-wood-1568, 2 Oct 2026); do not edit\n")
    for r in out:
        f.write("\t".join(map(str, r)) + "\n")
