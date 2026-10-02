#!/usr/bin/env python3
"""GAPS12-moray-wood-1568 (2 Oct 2026): the R4930 P3 step, run disk-only.

Premise found before any image work: R4930 images P3/P5 are byte-identical to R4931 (BL Cotton Caligula C II f.277r-v,
Randolph to Sussex, Edinburgh 5 July 1570), whose cipher runs were read from the contemporary decipherment on f.278
(DECODE R4932) by Bourdeau (github.com/dbourdeau/cyphersolver randolph1570/, MIT code / CC BY 4.0 text, credited; copied
in ../../randolph-sussex-1569/siblings/bourdeau-randolph1570/). So the "possible second text in this key" has a known
period key, and the step reduces to two disk-only tests:
 A. value comparison: f.278 values (period, H for Randolph's letter) against key.tsv (Aymeloglu, credited; S/M) on the
    sign shapes the two inventories share (shape match from the two transcribers' glyph descriptions, not from images).
 B. the Wood-line method (wood/wood_test.py) on Bourdeau's token transcription of run 1 (f.277r ll.3-10, the "P3 lines
    4-7" passage): shape-matched tokens relabelled into the Moray set (primary map fixed before scoring), decoded with
    key.tsv, unmatched tokens skipped, sco16 4-gram score vs 1,000 shuffled keys and 200 letter-order shuffles.
    Positive control at matched N AND matched sparsity: the Moray postscript reduced to tokens carrying the same mapped
    labels, decoded and scored identically (key.tsv is known to read it), windows of the target's N.
Deterministic (seed 1). Writes r4930_test.tsv.   python3 ciphers/moray-wood-1568/r4930/r4930_test.py
"""
import random, re, sys
from pathlib import Path

HERE = Path(__file__).resolve().parent; T = HERE.parent; ROOT = T.parents[1]
sys.path.insert(0, str(ROOT / "tools"))
from judge_plaintext import NgramModel, read_corpus, LANG_CORPORA  # noqa: E402

model = NgramModel([read_corpus(p) for p in LANG_CORPORA["sco16"]])
key = {r[0]: r[1] for r in (l.rstrip("\n").split("\t") for l in open(T / "key.tsv") if not l.startswith("#")) if r[0] != "code"}
WORD = {"U": "the", "o2": "and"}; DROP = {"4b", "Eb"}
letters = sorted(c for c, v in key.items() if len(v) == 1 and c not in WORD and c not in DROP)
rnd = random.Random(1); shuffled = []
for _ in range(1000):
    vals = [key[c] for c in letters]; rnd.shuffle(vals); shuffled.append(dict(key, **dict(zip(letters, vals))))

# A. shared shapes: (Bourdeau token, his glyph description, f.278 value, Moray label, Aymeloglu's glyph description)
SHARED = [
    ("K", "x with a bar (Ӿ)", "o", "X", "small crossed x"),
    ("x", "plain x", "not in Bourdeau's value list", "x", "straight-cross x"),
    ("e", "curly x (ꭓ, r-like)", "not in Bourdeau's value list", "xd", "cursive x, arced left arm"),
    ("4", "figure 4", "d", "4", "figure 4"),
    ("3", "figure 3 / ʒ", "f (3); a (tailed ʒ)", "Z3", "3-shape"),
    ("Q", "looped o with tail (ϙ)", "o", "M", "o with tail"),
    ("d", "delta (δ)", "t", "A", "triangle"),
    ("U", "cup u (ʋ)", "h", "U", "boxy u"),
]
out = [("part", "item", "a", "b", "c", "d", "e")]
agree = n = 0
print("A. shared shapes, f.278 period value vs key.tsv value:")
for tok, rd, rv, ml, md in SHARED:
    kv = key.get(ml, "?"); same = kv in re.findall(r"\b\w+\b", rv)
    agree += same; n += "not in" not in rv
    print(f"  {tok:4} {rd:38} f.278 {rv:24} | Moray {ml:3} {md:26} key.tsv {kv:4} {'AGREE' if same else 'differ'}")
    out.append(("A", tok, rd, rv, ml, kv, "no value" if "not in" in rv else "agree" if same else "differ"))
print(f"  agreement {agree}/{n} shapes with a stated f.278 value")

# B. Wood-line method on run 1
MAP = {"x": "x", "K": "X", "e": "xd", "4": "4", "3": "Z3", "Q": "M", "d": "A", "U": "U"}   # primary, fixed before scoring
src = (ROOT / "ciphers/randolph-sussex-1569/siblings/bourdeau-randolph1570/transcription.txt").read_text().split("\n")
run1, on = [], False
for l in src:
    if l.startswith("[f277r l.3"): on = True; continue
    if l.startswith("# ---- second run"): break
    if on and not l.startswith("["):
        run1 += [t for w in l.split() for t in w.split(".") if t and t != "-" and not t.startswith('"') and t.isascii()]
run1 = [t for t in run1 if len(t) == 1]
seq = [MAP[t] for t in run1 if t in MAP]


def render(s, k):
    return "".join(WORD.get(c, k.get(c, "")) for c in s if c not in DROP and c in k)


def stats(s):
    sc = model.score(render(s, key)); null = [model.score(render(s, kk)) for kk in shuffled]
    L = list(s); sh = []   # sign-order shuffle: keeps word-signs ('the') whole, so only order can move the score
    for sd in range(200):
        random.Random(sd).shuffle(L); sh.append(model.score(render(L, key)))
    return sc, sum(x < sc for x in null) / 1000, sum(x < sc for x in sh) / 200


sc, rk, lr = stats(seq); N = len(seq)
print(f"B. run 1: {len(run1)} single-sign tokens, {N} shape-matched ({N / len(run1):.0%}); decode '{render(seq, key)}'")
print(f"   target: score {sc:.3f}, rank vs 1000 shuffled keys {rk:.3f}, rank vs 200 sign-order shuffles {lr:.3f}")
out.append(("B", "target_run1", len(run1), N, render(seq, key), round(sc, 4), f"keyrank {rk:.3f} signshufrank {lr:.3f}"))
moray = [l.rstrip("\n").split("\t")[2] for l in open(T / "ciphertext.tsv") if not l.startswith("#")][1:]
msub = [s for s in moray if s in MAP.values()]
ctl = []
for i in range(0, len(msub) - N + 1):
    w = msub[i:i + N]; c = stats(w); ctl.append(c)
    out.append(("B", f"moray_sparse_window {i + 1}", len(w), N, render(w, key), round(c[0], 4), f"keyrank {c[1]:.3f} signshufrank {c[2]:.3f}"))
if ctl:
    lrs = sorted(c[2] for c in ctl); scs = sorted(c[0] for c in ctl)
    print(f"   positive control: Moray postscript reduced to the same {len(MAP)} labels ({len(msub)} of {len([s for s in moray if s != '|'])} tokens), "
          f"{len(ctl)} windows of N={N}: score min {scs[0]:.3f} median {scs[len(scs) // 2]:.3f}; sign-shuffle rank min {lrs[0]:.3f} "
          f"median {lrs[len(lrs) // 2]:.3f}, >=0.95 in {sum(x >= 0.95 for x in lrs)}/{len(ctl)}")
else:
    print(f"   positive control: Moray reduced to the same labels has only {len(msub)} tokens < N={N}; no matched window")
    out.append(("B", "moray_sparse_full", len(msub), N, render(msub, key), round(stats(msub)[0], 4), "shorter than N; keyrank/signshufrank printed"))
    c = stats(msub); print(f"   whole reduced postscript (N={len(msub)}): score {c[0]:.3f}, rank vs shuffled keys {c[1]:.3f}, sign-shuffle rank {c[2]:.3f}")
    full = [x for x in moray if x != "|"]; c = stats(full)
    print(f"   whole postscript, all labels (N={len(full)}): score {c[0]:.3f}, rank vs shuffled keys {c[1]:.3f}, sign-shuffle rank {c[2]:.3f}")
    out.append(("B", "moray_full", len(full), len(full), render(full, key), round(c[0], 4), f"keyrank {c[1]:.3f} signshufrank {c[2]:.3f}"))
with open(HERE / "r4930_test.tsv", "w") as f:
    f.write("# generated by r4930_test.py (GAPS12-moray-wood-1568, 2 Oct 2026); do not edit\n")
    for r in out: f.write("\t".join(map(str, r)) + "\n")
