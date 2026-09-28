"""Line B step B27 -- do the shorthand runs carry the function words (B25 reading b) or content words (names)?
Statistic: among the numeral tokens immediately flanking a run (both sides), the share that are 2-digit heads.
If runs replace function words, their neighbours are content (book values) -> LOW head share; if runs replace
content words (names, OOV), their neighbours are function words -> HIGH head share. Null: run positions permuted
among token positions (10,000 draws). Positive control: en18 letters (Bf layout, 99 heads + book) with 34 runs
placed on function-word stretches (share must fall below own p05 on >= 45/60); negative control: 34 runs placed on
content words (share above own p95 on >= 45/60). The target is read only if both controls separate."""
import random, sys
from collections import Counter
from pathlib import Path
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent / "b1")); sys.path.insert(0, str(HERE.parent / "b2"))
from padding_test import en18_words
import designs
def target_seq():
    seq = []
    for line in open(HERE.parents[1] / "ciphertext.txt", encoding="utf-8"):
        if line.startswith("#"): continue
        for t in line.split(): seq.append(int(t) if t.isdigit() else ("*" if t.startswith("*") else None))
    return seq
def stat(seq):
    n = h = 0
    for i, t in enumerate(seq):
        if t == "*":
            for j in (i - 1, i + 1):
                if 0 <= j < len(seq) and isinstance(seq[j], int) and seq[j] >= 10:
                    n += 1; h += seq[j] < 100
    return h / n if n else 0.0
def test(seq, rng, draws):
    s = stat(seq); nums = [t for t in seq if t != "*"]; k = seq.count("*"); null = []
    for _ in range(draws):
        pos = set(rng.sample(range(len(nums) + k), k)); out = []; it = iter(nums)
        for i in range(len(nums) + k): out.append("*" if i in pos else next(it))
        null.append(stat(out))
    null.sort(); return s, null[int(.05*draws)], null[int(.95*draws)], 100*sum(1 for x in null if x < s)/draws
words = en18_words(); freq = Counter(w for ws in words for w in ws); func = set(w for w, _ in freq.most_common(99))
code = designs.build(words, "Bf", random.Random(7))
def synth(rng, runs_on_function):
    ws = rng.choice(words); start = rng.randint(0, len(ws) - 3000); toks = []
    for w in ws[start:start + 600]:
        if w in code: toks.append((code[w], w in func))
    # choose 34 positions of the wanted class, replace each (and a random 0-3 following tokens of the same class) by a run
    idx = [i for i, (v, f) in enumerate(toks) if f == runs_on_function]
    chosen = sorted(rng.sample(idx, min(34, len(idx)))); out = []; skip = 0; i = 0
    while i < len(toks):
        if i in chosen:
            out.append("*"); i += 1
            while i < len(toks) and toks[i][1] == runs_on_function and rng.random() < 0.5: i += 1
        else: out.append(toks[i][0]); i += 1
    return out[:369 + 34]
rng = random.Random(9)
pos = [test(synth(random.Random(8000 + i), True), rng, 1000) for i in range(60)]
neg = [test(synth(random.Random(8000 + i), False), rng, 1000) for i in range(60)]
pc = sum(1 for p in pos if p[3] <= 5); nc = sum(1 for p in neg if p[3] >= 95)
print(f"positive control (runs = function words): head share mean {sum(p[0] for p in pos)/60:.3f}, below own p05: {pc}/60")
print(f"negative control (runs = content words):  head share mean {sum(p[0] for p in neg)/60:.3f}, above own p95: {nc}/60")
gate = pc >= 45 and nc >= 45; print("GATE:", "MET" if gate else "NOT MET")
t = test(target_seq(), rng, 10000)
print(f"TARGET: head share of run neighbours {t[0]:.3f}; null p05 {t[1]:.3f} p95 {t[2]:.3f}; percentile {t[3]:.1f}" + ("" if gate else "  [unlicensed]"))

# band readout (the 60-letter bands as controls, as in B19): where does the target's raw share fall?
pv = sorted(p[0] for p in pos); nv = sorted(p[0] for p in neg)
print(f"band, runs=function words: p05 {pv[3]:.3f} p50 {pv[30]:.3f} p95 {pv[57]:.3f}; target {t[0]:.3f} at pct {100*sum(1 for x in pv if x < t[0])/60:.0f}")
print(f"band, runs=content words:  p05 {nv[3]:.3f} p50 {nv[30]:.3f} p95 {nv[57]:.3f}; target {t[0]:.3f} at pct {100*sum(1 for x in nv if x < t[0])/60:.0f}")
