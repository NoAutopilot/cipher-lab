#!/usr/bin/env python3
"""R11-SURWT: pre-registered word test y = d vs m vs n on the 2039/2061 Nieuw readings (see PREREG.md).
Calibration gate (H-graded n tokens, 200 subsamples of N=24) first; target only if it passes.
Usage: python3 ciphers/na-suriname-map-1781/passes/surwt_r11/score.py [--alt 2]  -> score.out (or score_alt2.out)
"""
import math, random, sys
from collections import Counter
from pathlib import Path

HERE = Path(__file__).resolve().parent
T = HERE.parents[1]
sys.path.insert(0, str(T.parents[1] / "tools"))
from judge_plaintext import LANG_CORPORA, NgramModel, fold, read_corpus  # noqa: E402

ALT = 1 if "--alt" not in sys.argv else int(sys.argv[sys.argv.index("--alt") + 1])
FILES = ["reading_2039_legend_nieuw_tokens.tsv", "reading_2061_battery_nieuw_tokens.tsv"]
CANDS = "dmn"
NDRAW, NBOOT, NSUB, N = 10000, 10000, 200, 24

texts = [read_corpus(p) for p in LANG_CORPORA["nl18"]]
M = NgramModel(texts, n=4)
uni = Counter(fold("".join(texts)))
letters, weights = zip(*sorted(uni.items()))

def lp(g):
    return math.log10((M.c.get(g, 0) + M.k) / (M.ctx.get(g[:-1], 0) + M.V * M.k))

# lines -> list of segments; each segment a list of (tokenid, letter, sign, grade)
lines = {}
for f in FILES:
    for ln in (T / f).read_text(encoding="utf-8").splitlines():
        if ln.startswith("#") or ln.startswith("line\t"):
            continue
        line, pos, sign, val, gr = ln.split("\t")
        lines.setdefault(line, []).append((f"{line}:{pos}", sign, val, gr))
segs, where = [], {}
for line, toks in lines.items():
    cur = []
    for tid, sign, val, gr in toks:
        v = val.split("|")[min(ALT, len(val.split("|"))) - 1] if "|" in val else val
        if len(v) != 1 or not v.isalpha():
            if cur: segs.append(cur)
            cur = []
            continue
        cur.append([tid, v, sign, gr])
    if cur: segs.append(cur)
for si, s in enumerate(segs):
    for j, t in enumerate(s):
        where[t[0]] = (si, j)

target = [t[0] for s in segs for t in s if t[2] == "y" and t[1] == "d"]
ctrl_n = [t[0] for s in segs for t in s if t[1] == "n" and t[3] == "H"]
ctrl_d = [t[0] for s in segs for t in s if t[1] == "d" and t[3] == "H"]

def wvec(pos_ids, assign):
    """per-position window score; assign: dict tid -> letter for all pos_ids (set simultaneously)."""
    out = []
    for tid in pos_ids:
        si, j = where[tid]
        s = "".join(assign.get(t[0], t[1]) for t in segs[si])
        tot = 0.0
        for e in range(j, j + 4):
            if e - 3 >= 0 and e < len(s):
                tot += lp(s[e - 3:e + 1])
        out.append(tot)
    return out

def test(pos_ids, rng):
    W = {v: wvec(pos_ids, {t: v for t in pos_ids}) for v in CANDS}
    S = {v: sum(W[v]) for v in CANDS}
    nulls = sorted(sum(wvec(pos_ids, {t: rng.choices(letters, weights)[0] for t in pos_ids})) for _ in range(NDRAW))
    p99 = nulls[int(0.99 * NDRAW)]
    k = len(pos_ids); wins = {v: 0 for v in CANDS}
    for _ in range(NBOOT):
        idx = [rng.randrange(k) for _ in range(k)]
        sb = {v: sum(W[v][i] for i in idx) for v in CANDS}
        for v in CANDS:
            if all(sb[v] > sb[u] for u in CANDS if u != v):
                wins[v] += 1
    passed = [v for v in CANDS if S[v] > p99 and wins[v] / NBOOT >= 0.95]
    return S, p99, sum(nulls) / NDRAW, {v: wins[v] / NBOOT for v in CANDS}, passed, W

out = [f"R11-SURWT score.py alt={ALT}; target N={len(target)}, ctrl n(H) pool={len(ctrl_n)}, d(H) pool={len(ctrl_d)}"]
rng = random.Random(1781)
nd, nb = NDRAW, NBOOT
NDRAW, NBOOT = 1000, 1000  # per-subsample null/bootstrap size for the 200 calibration runs (stated in score.out)
npass = wrong = 0
for _ in range(NSUB):
    sub = rng.sample(ctrl_n, N)
    passed = test(sub, rng)[4]
    npass += "n" in passed
    wrong += ("d" in passed) or ("m" in passed)
gate = npass / NSUB >= 0.80 and wrong / NSUB <= 0.05
out.append(f"CALIBRATION (H n tokens, {NSUB} subsamples of {N}, 1000 null draws + 1000 bootstraps each): "
           f"n passes {npass}/{NSUB} = {npass/NSUB:.3f}; d or m passes {wrong}/{NSUB} = {wrong/NSUB:.3f} -> "
           f"{'GATE PASS' if gate else 'GATE FAIL'} (needs >=0.80 and <=0.05)")
NDRAW, NBOOT = nd, nb
S, p99, mu, wins, passed, _ = test(ctrl_d, random.Random(1781))
out.append(f"descriptive d(H) N={len(ctrl_d)}: S " + " ".join(f"{v}={S[v]:.2f}" for v in CANDS)
           + f"; null mean {mu:.2f} p99 {p99:.2f}; boot wins " + " ".join(f"{v}={wins[v]:.3f}" for v in CANDS) + f"; passes {passed}")
if gate:
    S, p99, mu, wins, passed, W = test(target, random.Random(1781))
    out.append(f"TARGET y positions N={len(target)}: S " + " ".join(f"{v}={S[v]:.2f}" for v in CANDS)
               + f"; null mean {mu:.2f} p99 {p99:.2f}; boot wins " + " ".join(f"{v}={wins[v]:.3f}" for v in CANDS))
    out.append("TARGET verdict: " + (f"PASS {passed[0]}" if len(passed) == 1 else f"{'TIE' if passed else 'FAIL'} (passing: {passed})"))
    for i, tid in enumerate(target):
        si, j = where[tid]
        s = "".join(t[1] for t in segs[si])
        ctx = s[max(0, j - 5):j] + "_" + s[j + 1:j + 6]
        best = max(CANDS, key=lambda v: W[v][i])
        out.append(f"  {tid}\t{ctx}\t" + "\t".join(f"{v}={W[v][i]:.2f}" for v in CANDS) + f"\tbest={best}")
else:
    out.append("TARGET not run: calibration gate failed -> non-test at this N.")
tot = sum(1 for s in segs for t in s); m_obs = sum(1 for s in segs for t in s if t[1] == "m")
out.append(f"descriptive: decoded m {m_obs} of {tot} letters; nl18 expectation {tot*uni['m']/sum(uni.values()):.1f}")
name = "score.out" if ALT == 1 else f"score_alt{ALT}.out"
(HERE / name).write_text("\n".join(out) + "\n")
print("\n".join(out))
